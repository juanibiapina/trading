#!/usr/bin/env python3
"""Archive SIP coverage and current IEX books for the fixed Initiative 7 basket."""

import argparse
import datetime as dt
import json
import os
from pathlib import Path
import statistics
import time
import urllib.parse
import urllib.request
from zoneinfo import ZoneInfo

from volume_metric import timestamp

ET = ZoneInfo("America/New_York")
SYMBOLS = ("AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "META", "TSLA", "QQQ")
SLOT = dt.timedelta(minutes=5)


def request(base, path, query):
    headers = {"APCA-API-KEY-ID": os.environ["ALPACA_API_KEY"],
               "APCA-API-SECRET-KEY": os.environ["ALPACA_SECRET_KEY"]}
    url = base.rstrip("/") + path + "?" + urllib.parse.urlencode(query)
    started = time.monotonic()
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=25) as response:
        payload = json.load(response)
    return {"received_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
            "elapsed_seconds": round(time.monotonic() - started, 3), "payload": payload}


def session(calendar):
    day = dt.date.fromisoformat(calendar["date"])
    return tuple(dt.datetime.combine(day, dt.time.fromisoformat(calendar[key]), ET)
                 .astimezone(dt.timezone.utc) for key in ("open", "close"))


def fetch_bars(base, start, end):
    query = {"symbols": ",".join(SYMBOLS), "timeframe": "5Min", "feed": "sip",
             "adjustment": "raw", "start": start.isoformat(), "end": end.isoformat(), "limit": 1000}
    pages, seen = [], set()
    while True:
        page = request(base, "/v2/stocks/bars", query)
        pages.append(page)
        token = page["payload"].get("next_page_token")
        if not token:
            return {"feed": "sip", "timeframe": "5Min", "adjustment": "raw",
                    "start_utc": start.isoformat(), "end_utc": end.isoformat(), "pages": pages}
        if token in seen:
            raise ValueError("Repeated SIP page token")
        seen.add(token)
        query["page_token"] = token


def capture(history_day):
    data = os.environ.get("ALPACA_DATA_URL", "https://data.alpaca.markets")
    trading = os.environ.get("ALPACA_BASE_URL", "https://paper-api.alpaca.markets")
    clock = request(trading, "/v2/clock", {})
    now = timestamp(clock["payload"]["timestamp"])
    current_day = now.astimezone(ET).date()
    if history_day >= current_day or not clock["payload"]["is_open"]:
        raise ValueError("Capture requires an open regular session and an earlier completed history date")
    calendars = request(trading, "/v2/calendar", {"start": history_day.isoformat(), "end": current_day.isoformat()})
    indexed = {row["date"]: row for row in calendars["payload"]}
    previous = indexed[history_day.isoformat()]
    current = indexed[current_day.isoformat()]
    start, end = session(previous)
    current_start, current_end = session(current)
    history = fetch_bars(data, start, end)
    # Explicitly request delayed SIP; never substitute an IEX bar for SIP coverage.
    delayed_end = min(now - dt.timedelta(minutes=16), current_end)
    if delayed_end <= current_start:
        raise ValueError("Wait until 16 minutes after the regular open for current SIP coverage")
    live = fetch_bars(data, current_start, delayed_end)
    quotes = request(data, "/v2/stocks/quotes/latest", {"symbols": ",".join(SYMBOLS), "feed": "iex"})
    latest = request(data, "/v2/stocks/bars/latest", {"symbols": ",".join(SYMBOLS), "feed": "iex"})
    return {"version": "init7-data-census-v1", "symbols": list(SYMBOLS), "clock": clock,
            "calendar": calendars, "history_session": previous, "current_session": current,
            "history_sip": history, "current_delayed_sip": live, "iex_quotes": quotes,
            "iex_latest_bars": latest}


def coverage(source, calendar):
    if (source.get("feed"), source.get("timeframe"), source.get("adjustment")) != ("sip", "5Min", "raw"):
        raise ValueError("Coverage requires explicitly identified raw SIP 5Min bars")
    start, close = session(calendar)
    end = min(timestamp(source["end_utc"]), close)
    expected = {start + SLOT * i for i in range(int((end - start) // SLOT))}
    rows = {symbol: [] for symbol in SYMBOLS}
    for page in source["pages"]:
        for symbol, bars in page["payload"].get("bars", {}).items():
            if symbol in rows:
                rows[symbol].extend(bars)
    result = {}
    observed = timestamp(source["pages"][-1]["received_utc"])
    for symbol, bars in rows.items():
        stamps = [timestamp(bar["t"]) for bar in bars]
        if len(stamps) != len(set(stamps)):
            raise ValueError(f"Duplicate {symbol} SIP bars")
        matched = sorted(set(stamps) & expected)
        last_end = matched[-1] + SLOT if matched else None
        result[symbol] = {"observed_slots": len(matched), "expected_slots": len(expected),
                          "missing_utc": [t.isoformat() for t in sorted(expected - set(stamps))],
                          "last_complete_end_utc": last_end.isoformat() if last_end else None,
                          "last_end_age_seconds": (observed - last_end).total_seconds() if last_end else None}
    return result


def analyze(source):
    if source["version"] != "init7-data-census-v1" or tuple(source["symbols"]) != SYMBOLS:
        raise ValueError("Census input must use the fixed basket and version")
    historical = coverage(source["history_sip"], source["history_session"])
    live = coverage(source["current_delayed_sip"], source["current_session"])
    observed = timestamp(source["iex_quotes"]["received_utc"])
    current_open, current_close = session(source["current_session"])
    in_session = current_open <= observed < current_close
    rows = []
    for symbol in SYMBOLS:
        q = source["iex_quotes"]["payload"].get("quotes", {}).get(symbol, {})
        age = (observed - timestamp(q["t"])).total_seconds() if q.get("t") else None
        bid, ask, bs, ass = (q.get(key, 0) for key in ("bp", "ap", "bs", "as"))
        two_sided = bid > 0 and ask >= bid and bs > 0 and ass > 0
        spread_bps = (ask - bid) / ((ask + bid) / 2) * 10000 if two_sided else None
        fresh = in_session and two_sided and age is not None and 0 <= age <= 60
        rows.append({"symbol": symbol, "history": historical[symbol], "current_sip": live[symbol],
                     "quote_utc": q.get("t"), "quote_age_seconds": age,
                     "bid": bid, "ask": ask, "bid_size": bs, "ask_size": ass,
                     "bid_exchange": q.get("bx"), "ask_exchange": q.get("ax"),
                     "fresh_two_sided": fresh, "spread_bps": spread_bps})
    return {"history_date": source["history_session"]["date"], "observed_utc": observed.isoformat(),
            "observation_in_regular_session": in_session, "rows": rows}


def report(source, result):
    fresh = sum(row["fresh_two_sided"] for row in result["rows"])
    spreads = [row["spread_bps"] for row in result["rows"] if row["fresh_two_sided"]]
    lines = ["# Initiative 7 — liquid regular-session data census", "",
             f"Captured {result['observed_utc']}; completed SIP date {result['history_date']}.", "",
             f"**{fresh}/8 fresh, positive-size two-sided IEX books at this observation.**",
             "The exchange calendar supplies session bounds; SIP requests consume every page and never fall back to IEX.", "",
             "| Symbol | Completed SIP slots | Current delayed SIP slots | Quote age (s) | Bid / ask | Sizes bid / ask | Spread (bps) | Fresh <=60s |",
             "|---|---:|---:|---:|---|---|---:|---|"]
    for row in result["rows"]:
        h, c = row["history"], row["current_sip"]
        age = "unknown" if row["quote_age_seconds"] is None else f"{row['quote_age_seconds']:.3f}"
        spread = "unknown" if row["spread_bps"] is None else f"{row['spread_bps']:.3f}"
        lines.append(f"| {row['symbol']} | {h['observed_slots']}/{h['expected_slots']} | "
                     f"{c['observed_slots']}/{c['expected_slots']} | {age} | {row['bid']} / {row['ask']} | "
                     f"{row['bid_size']} / {row['ask_size']} | {spread} | {row['fresh_two_sided']} |")
    lines += ["", "## Frequency, friction and cost", ""]
    if spreads:
        median = statistics.median(spreads)
        lines.append(f"Median fresh-book spread: **{median:.3f} bps**; observed range {min(spreads):.3f}–{max(spreads):.3f} bps.")
        lines.append(f"At a $100 research allocation, crossing this median spread once per round trip costs about **${median / 100:.4f}**, before slippage and fees.")
    delays = [r["current_sip"]["last_end_age_seconds"] for r in result["rows"] if r["current_sip"]["last_end_age_seconds"] is not None]
    if delays:
        lines.append(f"Current SIP last completed-bar ends were {min(delays):.1f}–{max(delays):.1f} seconds old at receipt, with a deliberate 16-minute request buffer.")
    pages = len(source["history_sip"]["pages"]) + len(source["current_delayed_sip"]["pages"])
    requests = pages + 4
    elapsed = sum(source[key]["elapsed_seconds"] for key in ("clock", "calendar", "iex_quotes", "iex_latest_bars"))
    elapsed += sum(page["elapsed_seconds"] for key in ("history_sip", "current_delayed_sip") for page in source[key]["pages"])
    lines += [f"Capture made {requests} read requests ({pages} SIP pages), totaling {elapsed:.3f} seconds in requests. Existing access required no new subscription.",
              "The normal session supplies 78 five-minute slots per symbol. Six hourly basket observations at 10:00–15:00 ET are feasible in calendar time, but repeated fresh-book availability is unmeasured.",
              "A numerical control needs zero model calls. A bounded agent variant would make one call per basket observation: six calls per full session.",
              "Its actual inference price and token count remain unknown. A prospective $0.05/call budget would cap six calls at $0.30/session; this is a design budget, not a measured bill.",
              "For comparison, at $100 allocation and six actual trades a $0.30 inference bill alone needs 5 bps average gross return per trade, plus spread, slippage and fees. Opportunity count is unknown.",
              "", "## Decision and limits", "",
              "Data feasibility supports specifying one numerical control and one bounded agent variant before observing future outcomes. It does not establish a profitable strategy or a fill.",
              "IEX is one venue, not a consolidated executable book. A single snapshot cannot establish all-day coverage, depth at a proposed size, historical slippage, or an edge over AH→PM.",
              "Current SIP is delayed; a future control must use only bars actually returned at each decision. Archive quote and source receipt times.",
              "Initiative 6 retains the sole pilot slot. Any regular-session trading adoption stays a proposal for Juan's daily email; no order or schedule change follows from this census.",
              "", "## Reproduce", "",
              "```bash",
              "python3 scripts/init7-data-census.py --input log/2026-10-01/init7-data-census.json \\",
              "  --report /tmp/init7-census-replay.md",
              "```",
              "", "## Next deliverable", "",
              "October 2 15:00 CEST: write one frozen numerical control and one bounded agent variant, with causal observation timing, equal capital, cash/QQQ comparators, net dollars per session, model costs and a complete trial record. Keep this at Research until a prospective instrumentation protocol is ready."]
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--history-date", type=dt.date.fromisoformat)
    parser.add_argument("--input", type=Path, help="Replay the archived capture without network requests")
    parser.add_argument("--output", type=Path, help="Archive the raw capture")
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    if not args.input and (not args.history_date or not args.output):
        parser.error("Network capture requires --history-date and --output")
    source = json.loads(args.input.read_text()) if args.input else capture(args.history_date)
    result = analyze(source)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(source, indent=2, allow_nan=False) + "\n")
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(report(source, result))
    print(json.dumps(result, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
