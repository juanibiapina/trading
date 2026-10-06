#!/usr/bin/env python3
"""Compute causal AH SIP volume ratios and write a log-only review report."""

import argparse
import datetime as dt
import json
import os
from pathlib import Path
import re
import statistics
import urllib.parse
import urllib.request
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")
SLOT = dt.timedelta(minutes=5)
VERSION = "sip-ah-volume-v1"
VERSION_V2 = "sip-ah-volume-v2"
FLOOR_SHARES = 100  # one round lot; a zero or near-zero baseline cannot inflate a ratio past bar shares / 100


def timestamp(value):
    value = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    if value.tzinfo is None:
        raise ValueError("Timestamps require a UTC offset")
    return value.astimezone(dt.timezone.utc)


def bounds(day):
    return tuple(dt.datetime.combine(day, dt.time(hour), ET).astimezone(dt.timezone.utc)
                 for hour in (16, 20))


def fetch_sip(symbol, prior_day, day):
    start, end = bounds(prior_day)[0], bounds(day)[1]
    query = {"timeframe": "5Min", "feed": "sip", "adjustment": "raw",
             "start": start.isoformat(), "end": end.isoformat(), "limit": 1000}
    headers = {"APCA-API-KEY-ID": os.environ["ALPACA_API_KEY"],
               "APCA-API-SECRET-KEY": os.environ["ALPACA_SECRET_KEY"]}
    url = os.environ.get("ALPACA_DATA_URL", "https://data.alpaca.markets").rstrip("/")
    bars = []
    seen = set()
    while True:
        request = urllib.request.Request(
            f"{url}/v2/stocks/{symbol}/bars?{urllib.parse.urlencode(query)}", headers=headers)
        with urllib.request.urlopen(request, timeout=25) as response:
            page = json.load(response)
        bars.extend(page.get("bars", []))
        token = page.get("next_page_token")
        if not token:
            break
        if token in seen:
            raise ValueError("Repeated SIP page token")
        seen.add(token)
        query["page_token"] = token
    return {"symbol": symbol, "feed": "sip", "timeframe": "5Min", "adjustment": "raw",
            "requested_start": start.isoformat(), "requested_end": end.isoformat(),
            "observed_utc": dt.datetime.now(dt.timezone.utc).isoformat(), "bars": bars}


def index_bars(source, day, prior_day):
    if source.get("feed") != "sip" or source.get("timeframe") != "5Min":
        raise ValueError("Metric requires explicitly identified SIP 5Min input")
    if source.get("adjustment") != "raw":
        raise ValueError("Metric requires raw shares, with corporate actions reviewed separately")
    if prior_day >= day:
        raise ValueError("Prior session must precede current session")
    indexed = {}
    for bar in source["bars"]:
        time = timestamp(bar["t"])
        if time in indexed or time.minute % 5 or time.second or time.microsecond:
            raise ValueError("SIP bars require unique five-minute start timestamps")
        volume = bar.get("v")
        if not isinstance(volume, (int, float)) or volume < 0:
            raise ValueError("SIP volume must be present and nonnegative")
        indexed[time] = bar
    return indexed


def calculate(source, day, prior_day, as_of):
    indexed = index_bars(source, day, prior_day)
    prior_start, prior_end = bounds(prior_day)
    if as_of < prior_end:
        raise ValueError("Prior AH session must be complete by as-of time")
    prior_slots = [prior_start + SLOT * i for i in range(48)]
    prior = [indexed[t] for t in prior_slots if t in indexed]
    observed_peak = max((b["v"] for b in prior), default=None)
    prior_complete = len(prior) == 48
    prior_peak = observed_peak if prior_complete else None
    start, end = bounds(day)
    rows = []
    for time in sorted(indexed):
        if not start <= time < end or time + SLOT > as_of:
            continue
        bar = indexed[time]
        local_ratio = None
        baseline = None
        if time - 3 * SLOT < start:
            status = "warmup"
        elif any(time - SLOT * i not in indexed for i in (1, 2, 3)):
            status = "missing-baseline"
        else:
            baseline = statistics.median(indexed[time - SLOT * i]["v"] for i in (1, 2, 3))
            status = "ok" if baseline > 0 else "zero-baseline"
            if baseline > 0:
                local_ratio = bar["v"] / baseline
        rows.append({"bar_start_utc": time.isoformat(),
                     "bar_end_utc": (time + SLOT).isoformat(),
                     "bar_et": time.astimezone(ET).strftime("%H:%M"),
                     "shares": bar["v"], "trades": bar.get("n"),
                     "baseline_shares": baseline, "local_ratio": local_ratio,
                     "local_status": status,
                     "local_ge_10": None if local_ratio is None else local_ratio >= 10,
                     "prior_peak_ratio": bar["v"] / prior_peak if prior_peak else None})
    return {"metric_version": VERSION, "symbol": source["symbol"],
            "date": day.isoformat(), "prior_date": prior_day.isoformat(),
            "as_of_utc": as_of.isoformat(), "source_observed_utc": source["observed_utc"],
            "prior_observed_slots": len(prior), "prior_expected_slots": 48,
            "prior_complete": prior_complete, "prior_observed_peak_shares": observed_peak,
            "rows": rows}


def calculate_v2(source, day, prior_day, as_of, floor=FLOOR_SHARES):
    """v2: absent slots inside the returned span are zero-trade intervals; ratios use a round-lot floor.

    Alpaca emits a bar only for an interval with trades. A slot is inferred zero when it lies at or
    after the request start (or the first returned bar when the start is unrecorded) and before the
    latest bar already closed by `as_of`. Slots after that bar stay unknown because data can lag.
    """
    indexed = index_bars(source, day, prior_day)
    prior_start, prior_end = bounds(prior_day)
    if as_of < prior_end:
        raise ValueError("Prior AH session must be complete by as-of time")
    visible = sorted(t for t in indexed if t + SLOT <= as_of)
    requested = source.get("requested_start")
    span_start = timestamp(requested) if requested else (visible[0] if visible else None)
    last = visible[-1] if visible else None

    def shares(time):
        if time in indexed and time + SLOT <= as_of:
            return indexed[time]["v"], "observed"
        if last is not None and span_start <= time < last:
            return 0, "absent-zero"
        return None, "unknown"

    prior = [shares(prior_start + SLOT * i) for i in range(48)]
    prior_known = all(value is not None for value, _ in prior)
    prior_peak = max(value for value, _ in prior) if prior_known else None
    prior_denominator = max(prior_peak, floor) if prior_known else None
    start, end = bounds(day)
    rows = []
    for time in visible:
        if not start <= time < end:
            continue
        bar = indexed[time]
        median = denominator = local_ratio = None
        if time - 3 * SLOT < start:
            status = "warmup"
        else:
            previous = [shares(time - SLOT * i)[0] for i in (1, 2, 3)]
            if any(value is None for value in previous):
                status = "unknown-baseline"
            else:
                median = statistics.median(previous)
                denominator = max(median, floor)
                local_ratio = bar["v"] / denominator
                status = "ok" if median >= floor else "floored"
        rows.append({"bar_start_utc": time.isoformat(),
                     "bar_end_utc": (time + SLOT).isoformat(),
                     "bar_et": time.astimezone(ET).strftime("%H:%M"),
                     "shares": bar["v"], "trades": bar.get("n"),
                     "baseline_median_shares": median, "baseline_shares": denominator,
                     "local_ratio": local_ratio, "local_status": status,
                     "local_ge_10": None if local_ratio is None else local_ratio >= 10,
                     "prior_peak_ratio": bar["v"] / prior_denominator if prior_denominator else None})
    return {"metric_version": VERSION_V2, "symbol": source["symbol"],
            "date": day.isoformat(), "prior_date": prior_day.isoformat(),
            "as_of_utc": as_of.isoformat(), "source_observed_utc": source["observed_utc"],
            "floor_shares": floor,
            "prior_observed_slots": sum(status == "observed" for _, status in prior),
            "prior_inferred_zero_slots": sum(status == "absent-zero" for _, status in prior),
            "prior_expected_slots": 48, "prior_complete": prior_known,
            "prior_peak_shares": prior_peak, "rows": rows}


def report(result):
    if result["metric_version"] == VERSION_V2:
        raise ValueError("The Markdown report describes v1 semantics; render v2 from its JSON rows")
    lines = [f"# {result['symbol']} shared volume audit — {result['date']}", "",
             f"Metric: `{result['metric_version']}`; SIP raw 5-minute shares; log-only.", "",
             f"Reconstructed through {result['as_of_utc']}; source fetched {result['source_observed_utc']}.",
             "Historical reconstruction does not prove these bars were available live at their closing times.", "",
             f"Prior AH session: {result['prior_date']}, {result['prior_observed_slots']}/48 observed slots; "
             f"largest observed bar {result['prior_observed_peak_shares']} shares.", "",
             "Local ratio = current shares / median of the three preceding five-minute slots in this AH session.",
             "Explicit zeros count; missing slots and a zero median yield an unknown ratio.",
             "Prior ratio = current shares / prior AH maximum; unavailable unless all 48 prior slots are observed.",
             "The 10x column reports a measurement; it does not authorize an entry.", "",
             "| Bar start ET | Shares | Trades | Prior 3-slot median | Local ratio | Local >=10x | Prior AH peak ratio | Status |",
             "|---|---:|---:|---:|---:|---|---:|---|"]
    for row in result["rows"]:
        ratio = "unknown" if row["local_ratio"] is None else f"{row['local_ratio']:.4f}x"
        prior = "unknown" if row["prior_peak_ratio"] is None else f"{row['prior_peak_ratio']:.4f}x"
        flag = "unknown" if row["local_ge_10"] is None else str(row["local_ge_10"]).lower()
        baseline = "unknown" if row["baseline_shares"] is None else f"{row['baseline_shares']:,.0f}"
        lines.append(f"| {row['bar_et']} | {row['shares']:,} | {row['trades']} | {baseline} | "
                     f"{ratio} | {flag} | {prior} | {row['local_status']} |")
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("symbol")
    parser.add_argument("date", type=dt.date.fromisoformat)
    parser.add_argument("--prior-date", required=True, type=dt.date.fromisoformat,
                        help="Previous completed trading date, checked against the exchange calendar")
    parser.add_argument("--as-of", required=True, type=timestamp, help="Include only bars closed by this ISO time")
    parser.add_argument("--input", type=Path, help="Replay an archived SIP input instead of fetching")
    parser.add_argument("--save-input", type=Path, help="Archive fetched SIP bars with source metadata")
    parser.add_argument("--report", type=Path, help="Write a Markdown review from the same computed rows")
    parser.add_argument("--metric-version", choices=(VERSION, VERSION_V2), default=VERSION,
                        help="v1 (default) keeps absent slots unknown; v2 infers zero-trade slots, floors at 100 shares")
    args = parser.parse_args()
    if args.metric_version == VERSION_V2 and args.report:
        parser.error("--report renders v1 only")
    symbol = args.symbol.upper()
    if not re.fullmatch(r"[A-Z][A-Z.\-]*", symbol):
        parser.error("Invalid symbol")
    source = json.loads(args.input.read_text()) if args.input else fetch_sip(symbol, args.prior_date, args.date)
    if source["symbol"] != symbol:
        parser.error("Archived symbol does not match requested symbol")
    compute = calculate_v2 if args.metric_version == VERSION_V2 else calculate
    result = compute(source, args.date, args.prior_date, args.as_of)
    if args.save_input:
        args.save_input.parent.mkdir(parents=True, exist_ok=True)
        args.save_input.write_text(json.dumps(source, indent=2) + "\n")
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(report(result))
    print(json.dumps(result, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
