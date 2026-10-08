#!/usr/bin/env python3
"""Initiative 7 modeled execution layer. Quote-based modeled fills only: no orders.

The frozen design (docs/investigations/init7-comparison-v1.json, "future_pilot_execution" and
"cost_accounting") requires an entry quote received after each observation's decision is
persisted, exits at the next observation and a final flatten at 15:55 ET. init7-observe.py
captures only a pre-decision book diagnostic, and its hash is pinned in every decision, so this
separate script captures the post-decision books and builds the modeled ledger.

Subcommands:
  capture  Capture one post-decision IEX book for all eight basket symbols plus asset status.
           Slots wait for that slot's decision.json (up to the cutoff plus 30 s); 15:55 is the
           flatten capture. Writes log/<ET date>/init7-execute/<HHMM>/capture.json exclusively.
  daemon   Sleep until each slot and the flatten time and run `capture`, through --until.
           Start it with `gob add python3 scripts/init7-execute.py daemon --until YYYY-MM-DD`.
  nbbo     For one ET date, fetch the SIP NBBO at each capture's receipt time once the 16-minute
           SIP delay has passed. Writes <HHMM>/nbbo.json next to capture.json exclusively.
  ledger   Build the modeled N1/A1/A2/CASH/QQQ ledger for one ET date under the base and
           stress cost scenarios, with the spread paid on every fill. Offline and repeatable.
           --fill-source iex prices fills at the IEX book (frozen v1 design); sip prices them at
           the delayed SIP NBBO for the same instant, after the same IEX availability checks.
  spreads  Summarize IEX spreads from archived pre-decision diagnostics and captures.
"""

import argparse
import datetime as dt
import importlib.util
import json
import math
import os
from pathlib import Path
import statistics
import time
import traceback
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
ET = ZoneInfo("America/New_York")
UTC = dt.timezone.utc
VERSION = "init7-execute-v1"
DESIGN = ROOT / "docs" / "investigations" / "init7-comparison-v1.json"
CENSUS = ROOT / "scripts" / "init7-data-census.py"
ARMS = ("N1", "A1", "A2")
FULL_SESSION = dt.timedelta(hours=6, minutes=30)


def now():
    return dt.datetime.now(UTC)


def iso(value):
    return value.astimezone(UTC).isoformat().replace("+00:00", "Z")


def stamp(value):
    result = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    if result.tzinfo is None:
        raise ValueError(f"Timestamp needs an explicit time zone: {value}")
    return result.astimezone(UTC)


def quote_time(value):
    # Alpaca returns nanoseconds; Python parses microseconds.
    head, _, tail = value.rstrip("Z").partition(".")
    return stamp(f"{head}.{(tail + '000000')[:6]}Z" if tail else f"{head}Z")


def census():
    spec = importlib.util.spec_from_file_location("init7_census", CENSUS)
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


def design():
    return json.loads(DESIGN.read_text())


def slot_time(day, clock):
    hour, minute = map(int, clock.split(":"))
    return dt.datetime(day.year, day.month, day.day, hour, minute, tzinfo=ET)


def write_new(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x") as file:
        file.write(json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + "\n")


# ---------------------------------------------------------------- capture

def capture(day, clock, out=None, wait_decision=True):
    """Capture one post-decision book. clock is a frozen slot or the flatten time."""
    frozen = design()
    flatten = clock == frozen["future_pilot_execution"]["final_flatten_et"]
    if not flatten and clock not in frozen["observation_times_et"]:
        raise ValueError(f"{clock} is not a frozen slot or the flatten time")
    scheduled = slot_time(day, clock)
    hhmm = clock.replace(":", "")
    decision_path = ROOT / "log" / day.isoformat() / "init7-observe" / hhmm / "decision.json"
    persisted = None
    if not flatten:
        limit = scheduled + dt.timedelta(seconds=frozen["observation_deadline_seconds"] + 30)
        while wait_decision and not decision_path.exists() and now() < limit:
            time.sleep(0.25)
        if decision_path.exists():
            persisted = json.loads(decision_path.read_text())["decision_persisted_utc"]
    helpers = census()
    data = os.environ.get("ALPACA_DATA_URL", "https://data.alpaca.markets")
    trading = os.environ.get("ALPACA_BASE_URL", "https://paper-api.alpaca.markets")
    record = {"version": VERSION, "scheduled_et": scheduled.isoformat(), "kind": "flatten" if flatten else "slot",
              "decision_persisted_utc": persisted, "requested_utc": iso(now()), "quotes": None, "assets": {},
              "errors": []}
    try:
        record["quotes"] = helpers.request(data, "/v2/stocks/quotes/latest",
                                           {"symbols": ",".join(helpers.SYMBOLS), "feed": "iex"})
    except Exception as error:
        record["errors"].append(f"quotes: {type(error).__name__}: {error}")
    if not flatten:
        for symbol in helpers.SYMBOLS:
            try:
                record["assets"][symbol] = helpers.request(trading, f"/v2/assets/{symbol}", {})
            except Exception as error:
                record["errors"].append(f"asset {symbol}: {type(error).__name__}: {error}")
    path = out or ROOT / "log" / day.isoformat() / "init7-execute" / hhmm / "capture.json"
    write_new(path, record)
    return path, record


def command_capture(args):
    day = dt.date.fromisoformat(args.date) if args.date else now().astimezone(ET).date()
    path, record = capture(day, args.slot, args.out, wait_decision=not args.no_wait)
    quotes = ((record["quotes"] or {}).get("payload") or {}).get("quotes") or {}
    print(json.dumps({"path": str(path.relative_to(ROOT) if path.is_relative_to(ROOT) else path),
                      "decision_persisted_utc": record["decision_persisted_utc"],
                      "quotes_received_utc": (record["quotes"] or {}).get("received_utc"),
                      "spread_bps": {s: spread_bps(q) for s, q in quotes.items()},
                      "errors": record["errors"]}, indent=2))


def command_daemon(args):
    frozen = design()
    helpers = census()
    clocks = frozen["observation_times_et"] + [frozen["future_pilot_execution"]["final_flatten_et"]]
    trading = os.environ.get("ALPACA_BASE_URL", "https://paper-api.alpaca.markets")
    until = dt.date.fromisoformat(args.until)
    done = set()
    print(f"{iso(now())} daemon started; through {until}", flush=True)
    while True:
        today = now().astimezone(ET).date()
        if today > until:
            break
        try:
            rows = helpers.request(trading, "/v2/calendar", {"start": today.isoformat(),
                                                             "end": until.isoformat()})["payload"]
        except Exception as error:
            print(f"{iso(now())} calendar failed: {error}; retry in 10 minutes", flush=True)
            time.sleep(600)
            continue
        rows = [row for row in rows if row["date"] not in done]
        if not rows:
            break
        row = rows[0]
        day = dt.date.fromisoformat(row["date"])
        opened, closed = helpers.session(row)
        if closed - opened < FULL_SESSION:
            print(f"{iso(now())} {day} half-day; skipped", flush=True)
            done.add(row["date"])
            continue
        for clock in clocks:
            scheduled = slot_time(day, clock)
            wait = (scheduled - now()).total_seconds()
            if wait > 0:
                time.sleep(wait)
            if (now() - scheduled).total_seconds() > frozen["observation_deadline_seconds"] + 60:
                print(f"{iso(now())} {day} {clock} missed", flush=True)
                continue
            try:
                path, record = capture(day, clock)
                print(f"{iso(now())} {day} {clock} captured {path.relative_to(ROOT)} "
                      f"(decision {record['decision_persisted_utc']}, errors {len(record['errors'])})", flush=True)
            except Exception:
                print(f"{iso(now())} {day} {clock} failed:\n{traceback.format_exc()}", flush=True)
        done.add(row["date"])
    print(f"{iso(now())} daemon finished", flush=True)


# ---------------------------------------------------------------- ledger

def spread_bps(quote):
    bid, ask = quote.get("bp") or 0, quote.get("ap") or 0
    if bid <= 0 or ask <= 0 or ask < bid:
        return None
    return round((ask - bid) / ((ask + bid) / 2) * 1e4, 2)


def book(capture_record, symbol, side, anchor, frozen, nbbo=None):
    """Return (quote, problem). side is 'buy' or 'sell'; anchor is the time the quote must follow.

    With nbbo (a dict of SIP quotes for this capture), the IEX book still decides availability and
    the SIP NBBO at the same instant sets the price and displayed size.
    """
    if capture_record is None:
        return None, "no_capture"
    quotes = capture_record.get("quotes")
    if not quotes:
        return None, "quote_request_failed"
    quote = (quotes["payload"].get("quotes") or {}).get(symbol)
    if not quote:
        return None, "no_quote"
    received = stamp(quotes["received_utc"])
    execution = frozen["future_pilot_execution"]
    if anchor is not None and received <= anchor:
        return None, "quote_before_decision"
    if anchor is not None and side == "sell" and (received - anchor).total_seconds() > execution["exit_quote_deadline_seconds"]:
        return None, "exit_quote_late"
    if (received - quote_time(quote["t"])).total_seconds() > execution["quote_max_age_seconds"]:
        return None, "stale_quote"
    if not (quote.get("bp", 0) > 0 and quote.get("ap", 0) > 0 and quote.get("bs", 0) > 0 and quote.get("as", 0) > 0):
        return None, "one_sided_book"
    if quote["ap"] < quote["bp"]:
        return None, "crossed_book"
    if side == "buy":
        asset = ((capture_record.get("assets") or {}).get(symbol) or {}).get("payload") or {}
        if not (asset.get("status") == "active" and asset.get("tradable") and asset.get("fractionable")):
            return None, "asset_not_eligible"
    if nbbo is not None:
        sip = (nbbo.get("quotes") or {}).get(symbol)
        if not sip:
            return None, "no_sip_quote"
        if (received - quote_time(sip["t"])).total_seconds() > execution["quote_max_age_seconds"]:
            return None, "stale_sip_quote"
        if not (sip["bp"] > 0 and sip["ap"] >= sip["bp"] and sip["bs"] > 0 and sip["as"] > 0):
            return None, "bad_sip_book"
        return sip, None
    return quote, None


def run_arm(name, tickers, captures, anchors, frozen, start_equity, hold=False, nbbos=None):
    """Simulate one arm through the session. tickers maps slot -> ticker or None.

    Arms close at the next slot before any new entry; hold=True keeps one entry until flatten.
    """
    costs = frozen["cost_accounting"]
    fee = costs["fee_bps_per_side_assumed"]
    capital = frozen["future_pilot_capital"]
    out = {}
    for scenario, slip in (("base", costs["base_slippage_bps_per_side"]),
                           ("stress", costs["stress_slippage_bps_per_side"])):
        side_cost = (slip + fee) / 1e4
        equity, held, trades, events, paused = start_equity, None, [], [], False
        for clock in list(tickers) + ["flatten"]:
            record, anchor = captures.get(clock), anchors.get(clock)
            if held and (not hold or clock == "flatten"):
                quote, problem = book(record, held["symbol"], "sell", anchor, frozen, pick(nbbos, clock))
                if problem or quote["bs"] < held["shares"]:
                    events.append({"at": clock, "event": "exit_unresolved", "symbol": held["symbol"],
                                   "reason": problem or "bid_size_below_shares"})
                    paused = True
                    break
                proceeds = held["shares"] * quote["bp"] * (1 - side_cost)
                mid = (quote["ap"] + quote["bp"]) / 2
                trade = dict(held, exit_at=clock, exit_bid=quote["bp"], exit_ask=quote["ap"],
                             exit_spread_bps=spread_bps(quote), proceeds=round(proceeds, 6))
                trade["spread_paid_usd"] = round(held["entry_half_spread_usd"] + held["shares"] * (mid - quote["bp"]), 6)
                trade["net_usd"] = round(proceeds - held["cost"], 6)
                trade["gross_mid_return_pct"] = round((mid / held["entry_mid"] - 1) * 100, 4)
                equity += proceeds
                trades.append(trade)
                held = None
            if clock == "flatten":
                break
            symbol = tickers[clock]
            if symbol is None:
                continue
            if paused:
                events.append({"at": clock, "event": "entry_skipped", "symbol": symbol, "reason": "paused"})
                continue
            quote, problem = book(record, symbol, "buy", anchor, frozen, pick(nbbos, clock))
            if problem:
                events.append({"at": clock, "event": "entry_skipped", "symbol": symbol, "reason": problem})
                continue
            budget = equity * capital["maximum_equity_fraction_per_position"]
            price = quote["ap"] * (1 + side_cost)
            shares = math.floor(budget / price * 1e9) / 1e9
            if shares > quote["as"]:
                events.append({"at": clock, "event": "entry_skipped", "symbol": symbol, "reason": "ask_size_below_shares"})
                continue
            cost = shares * price
            mid = (quote["ap"] + quote["bp"]) / 2
            equity -= cost
            held = {"symbol": symbol, "entry_at": clock, "shares": shares, "entry_ask": quote["ap"],
                    "entry_bid": quote["bp"], "entry_spread_bps": spread_bps(quote), "entry_mid": mid,
                    "cost": round(cost, 6), "entry_half_spread_usd": shares * (quote["ap"] - mid)}
        if held and not paused:  # no flatten resolved it
            events.append({"at": "end", "event": "exit_unresolved", "symbol": held["symbol"], "reason": "open_at_end"})
            paused = True
        for trade in trades:
            trade.pop("entry_half_spread_usd", None)
        out[scenario] = {"end_equity": None if paused else round(equity, 6),
                         "net_usd": None if paused else round(equity - start_equity, 6),
                         "realized_net_usd": round(sum(t["net_usd"] for t in trades), 6),
                         "round_trips": len(trades), "spread_paid_usd": round(sum(t["spread_paid_usd"] for t in trades), 6),
                         "unresolved_exposure": paused, "trades": trades, "events": events}
    return out


def pick(nbbos, clock):
    if nbbos is None:
        return None
    return nbbos.get(clock) or {"quotes": {}}


def ledger(day, start_equity=100.0, base=None, fill_source="iex"):
    frozen = design()
    base = base or ROOT / "log" / day.isoformat()
    slots = [clock.replace(":", "") for clock in frozen["observation_times_et"]]
    captures, anchors, decisions, nbbos = {}, {}, {}, {}
    for hhmm in slots + ["1555"]:
        path = base / "init7-execute" / hhmm / "capture.json"
        key = "flatten" if hhmm == "1555" else hhmm
        captures[key] = json.loads(path.read_text()) if path.exists() else None
        sip = path.with_name("nbbo.json")
        nbbos[key] = json.loads(sip.read_text()) if sip.exists() else None
    nbbos = nbbos if fill_source == "sip" else None
    for hhmm in slots:
        path = base / "init7-observe" / hhmm / "decision.json"
        record = json.loads(path.read_text()) if path.exists() else None
        decisions[hhmm] = record
        anchors[hhmm] = stamp(record["decision_persisted_utc"]) if record else None
    anchors["flatten"] = slot_time(day, frozen["future_pilot_execution"]["final_flatten_et"]).astimezone(UTC)
    rows = {}
    for arm in ARMS:
        key = arm.lower()
        tickers = {hhmm: (decisions[hhmm]["decision"][key] if decisions[hhmm] else None) for hhmm in slots}
        rows[arm] = run_arm(arm, tickers, captures, anchors, frozen, start_equity, nbbos=nbbos)
    # QQQ: enter at the first slot with a valid entry book, exit at flatten.
    first = next((hhmm for hhmm in slots if decisions[hhmm]
                  and book(captures[hhmm], "QQQ", "buy", anchors[hhmm], frozen, pick(nbbos, hhmm))[1] is None), None)
    rows["QQQ"] = run_arm("QQQ", {hhmm: ("QQQ" if hhmm == first else None) for hhmm in slots},
                          captures, anchors, frozen, start_equity, hold=True, nbbos=nbbos)
    rows["CASH"] = {scenario: {"end_equity": start_equity, "net_usd": 0.0, "round_trips": 0}
                    for scenario in ("base", "stress")}
    coverage = {"decisions": sum(1 for v in decisions.values() if v), "slot_captures":
                sum(1 for h in slots if captures[h]), "flatten_capture": captures["flatten"] is not None,
                "slots": len(slots)}
    spreads = {}
    for key, record in captures.items():
        quotes = ((record or {}).get("quotes") or {}).get("payload", {}).get("quotes") or {}
        spreads[key] = {symbol: spread_bps(quote) for symbol, quote in quotes.items()}
    return {"version": VERSION, "date": day.isoformat(), "mode": "modeled_quote_fills_no_orders",
            "fill_source": fill_source,
            "start_equity_usd_per_arm": start_equity, "coverage": coverage,
            "decisions": {h: (v["decision"] if v else None) for h, v in decisions.items()},
            "arms": rows, "iex_spread_bps": spreads}


def command_ledger(args):
    day = dt.date.fromisoformat(args.date)
    result = ledger(day, args.start_equity, args.base, args.fill_source)
    text = json.dumps(result, indent=2, allow_nan=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    summary = {arm: {s: {k: v[s].get(k) for k in ("net_usd", "round_trips", "spread_paid_usd", "unresolved_exposure")}
                     for s in ("base", "stress")} for arm, v in result["arms"].items()}
    print(json.dumps({"date": result["date"], "fill_source": result["fill_source"], "coverage": result["coverage"], "arms": summary}, indent=2))


# ---------------------------------------------------------------- nbbo

def command_nbbo(args):
    helpers = census()
    data = os.environ.get("ALPACA_DATA_URL", "https://data.alpaca.markets")
    base = args.base or ROOT / "log" / args.date
    written = []
    for path in sorted(base.glob("init7-execute/*/capture.json")):
        target = path.with_name("nbbo.json")
        record = json.loads(path.read_text())
        if target.exists() or not record.get("quotes"):
            continue
        at = stamp(record["quotes"]["received_utc"])
        if now() < at + dt.timedelta(minutes=16):
            continue  # inside the SIP delay; fetch on a later run
        quotes, receipts = {}, []
        for symbol in helpers.SYMBOLS:
            response = helpers.request(data, f"/v2/stocks/{symbol}/quotes",
                                       {"feed": "sip", "start": iso(at - dt.timedelta(seconds=60)),
                                        "end": iso(at), "limit": 1, "sort": "desc"})
            receipts.append(response["received_utc"])
            rows = response["payload"].get("quotes") or []
            if rows:
                quotes[symbol] = rows[0]
        write_new(target, {"version": VERSION, "feed": "sip", "as_of_utc": iso(at),
                           "rule": "last SIP quote in the 60 s up to the IEX capture receipt",
                           "fetched_utc": max(receipts), "quotes": quotes})
        written.append(str(target.relative_to(ROOT) if target.is_relative_to(ROOT) else target))
    print(json.dumps({"written": written}, indent=2))


# ---------------------------------------------------------------- spreads

def command_spreads(args):
    rows = []
    for path in sorted(ROOT.glob("log/*/init7-observe/*/market.json")):
        payload = json.loads(path.read_text())["iex_quotes"]["payload"]["quotes"]
        for symbol, quote in payload.items():
            rows.append(("pre_decision", path.parts[-4], path.parts[-2], symbol, spread_bps(quote)))
    for path in sorted(ROOT.glob("log/*/init7-execute/*/capture.json")):
        record = json.loads(path.read_text())
        payload = ((record.get("quotes") or {}).get("payload") or {}).get("quotes") or {}
        for symbol, quote in payload.items():
            rows.append(("post_decision", path.parts[-4], path.parts[-2], symbol, spread_bps(quote)))
    by_symbol = {}
    for _, _, _, symbol, value in rows:
        by_symbol.setdefault(symbol, []).append(value)
    summary = {}
    for symbol, values in sorted(by_symbol.items()):
        valid = sorted(v for v in values if v is not None)
        summary[symbol] = {"n": len(values), "invalid": len(values) - len(valid),
                           "median_bps": statistics.median(valid) if valid else None,
                           "max_bps": valid[-1] if valid else None,
                           "over_20_bps": sum(1 for v in valid if v > 20)}
    allv = sorted(v for *_, v in rows if v is not None)
    print(json.dumps({"books": len(rows), "median_bps": statistics.median(allv) if allv else None,
                      "p90_bps": allv[int(0.9 * (len(allv) - 1))] if allv else None,
                      "by_symbol": summary}, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("capture")
    p.add_argument("--slot", required=True, help="Frozen slot or flatten time in ET, e.g. 12:30 or 15:55")
    p.add_argument("--date", help="ET date (default today)")
    p.add_argument("--out", type=Path, help="Rehearsal output path outside the prospective log")
    p.add_argument("--no-wait", action="store_true", help="Do not wait for the slot's decision")
    p = sub.add_parser("daemon")
    p.add_argument("--until", required=True, help="Last ET date to capture")
    p = sub.add_parser("ledger")
    p.add_argument("--date", required=True)
    p.add_argument("--start-equity", type=float, default=100.0)
    p.add_argument("--base", type=Path, help="Day directory (default log/<date>)")
    p.add_argument("--output", type=Path)
    p.add_argument("--fill-source", choices=("iex", "sip"), default="iex")
    p = sub.add_parser("nbbo")
    p.add_argument("--date", required=True)
    p.add_argument("--base", type=Path, help="Day directory (default log/<date>)")
    sub.add_parser("spreads")
    args = parser.parse_args()
    {"capture": command_capture, "daemon": command_daemon, "ledger": command_ledger,
     "nbbo": command_nbbo, "spreads": command_spreads}[args.command](args)


if __name__ == "__main__":
    main()
