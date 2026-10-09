#!/usr/bin/env python3
"""Initiative 3 study, log-only: where does the realized-vs-modeled exit gap come from?

On the 89 real AH entries, real exits return 2.45 points less than a modeled market exit at the
04:30 ET bar open (init3-limit-exit, 2026-10-08). This script splits that gap per trade into

  execution  (fill price - SIP NBBO mid at the fill instant) / entry price: spread and slippage
  timing     (NBBO mid at the fill - 04:30 ET open) / entry price: when we sold, not how

The two parts add up exactly to realized - base0430. Each exit fill is a real Alpaca sell from the
archived order list; partial exits are weighted by quantity. Fetch mode stores the last SIP quote
at or before each fill under OUT/sip-quotes; `--replay` recomputes offline from that archive.
"""

import argparse
import datetime as dt
import json
import os
from pathlib import Path
import statistics
import urllib.parse
import urllib.request
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")
ARCHIVE = Path("log/2026-10-06/init1-volume-policy")
LIMIT_EXIT = Path("log/2026-10-08/init3-limit-exit/result.json")


def stamp(value):
    return dt.datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(dt.timezone.utc)


def lots(orders):
    """FIFO pairing of buys and sells, the same rule as volume-entry-eval.py."""
    queues, result = {}, []
    for order in sorted(orders, key=lambda o: o["filled_at"]):
        qty, price, time = float(order["filled_qty"]), float(order["filled_avg_price"]), stamp(order["filled_at"])
        if order["side"] == "buy":
            lot = {"symbol": order["symbol"], "fill": time, "qty": qty, "price": price, "open": qty,
                   "exits": []}
            queues.setdefault(order["symbol"], []).append(lot)
            result.append(lot)
            continue
        remaining = qty
        for lot in queues.get(order["symbol"], []):
            take = min(lot["open"], remaining)
            if take <= 0:
                continue
            lot["open"] -= take
            lot["exits"].append({"utc": time, "qty": take, "price": price, "ext": order.get("extended_hours")})
            remaining -= take
            if remaining <= 1e-9:
                break
    return result


def fetch_quote(symbol, when):
    query = {"feed": "sip", "start": (when - dt.timedelta(hours=2)).isoformat(), "end": when.isoformat(),
             "sort": "desc", "limit": 1}
    headers = {"APCA-API-KEY-ID": os.environ["ALPACA_API_KEY"],
               "APCA-API-SECRET-KEY": os.environ["ALPACA_SECRET_KEY"]}
    url = os.environ.get("ALPACA_DATA_URL", "https://data.alpaca.markets").rstrip("/")
    request = urllib.request.Request(f"{url}/v2/stocks/{symbol}/quotes?{urllib.parse.urlencode(query)}",
                                     headers=headers)
    with urllib.request.urlopen(request, timeout=25) as response:
        page = json.load(response)
    return {"symbol": symbol, "fill_utc": when.isoformat(), "feed": "sip",
            "observed_utc": dt.datetime.now(dt.timezone.utc).isoformat(), "quotes": page.get("quotes") or []}


def bucket(entry_day, exit_time, pm_day):
    local = exit_time.astimezone(ET)
    if local.date() == entry_day:
        return "same evening"
    if local.date() == pm_day:
        if local.time() < dt.time(4, 30):
            return "next PM before 04:30"
        if local.time() < dt.time(9, 30):
            return "next PM 04:30-09:30"
        return "next day regular or later"
    return "later day"


def stats(values):
    return {"n": len(values), "mean_pts": round(100 * statistics.mean(values), 2) if values else None,
            "median_pts": round(100 * statistics.median(values), 2) if values else None}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("out", type=Path)
    parser.add_argument("--replay", action="store_true")
    args = parser.parse_args()
    entries = json.loads((ARCHIVE / "result.json").read_text())["entries"]
    limit_rows = {(r["symbol"], r["date"]): r for r in json.loads(LIMIT_EXIT.read_text())["rows"]}
    all_lots = lots(json.loads((ARCHIVE / "orders.json").read_text()))
    quote_dir = args.out / "sip-quotes"
    quote_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    for entry in entries:
        fill = stamp(entry["as_of_utc"]) + dt.timedelta(minutes=15)
        match = [l for l in all_lots if l["symbol"] == entry["symbol"]
                 and abs((l["fill"] - fill).total_seconds()) < 120 and abs(l["price"] - entry["entry_price"]) < 1e-9]
        if len(match) != 1:
            raise ValueError(f"{entry['symbol']} {entry['date']}: {len(match)} matching lots")
        lot, base_row = match[0], limit_rows[(entry["symbol"], entry["date"])]
        cost = lot["qty"] * lot["price"]
        execution = timing = 0.0
        exits, missing = [], 0
        for leg in lot["exits"]:
            path = quote_dir / f"{entry['symbol']}-{leg['utc'].strftime('%Y%m%dT%H%M%S%f')}.json"
            if not path.exists():
                if args.replay:
                    raise FileNotFoundError(path)
                path.write_text(json.dumps(fetch_quote(entry["symbol"], leg["utc"]), indent=1) + "\n")
            quotes = json.loads(path.read_text())["quotes"]
            q = quotes[0] if quotes else None
            usable = q is not None and q["bp"] > 0 and q["ap"] >= q["bp"]
            if not usable:
                missing += 1
            mid = (q["bp"] + q["ap"]) / 2 if usable else None
            exits.append({"et": leg["utc"].astimezone(ET).isoformat(), "qty": leg["qty"], "price": leg["price"],
                          "bid": q["bp"] if q else None, "ask": q["ap"] if q else None,
                          "quote_age_s": round((leg["utc"] - stamp(q["t"])).total_seconds(), 1) if q else None,
                          "spread_pct_of_mid": round(100 * (q["ap"] - q["bp"]) / mid, 2) if usable else None,
                          "vs_bid_pct": round(100 * (leg["price"] / q["bp"] - 1), 2) if usable else None})
            if usable:
                execution += leg["qty"] * (leg["price"] - mid) / cost
                timing += leg["qty"] * (mid / lot["price"] - 1 - base_row["base0430"]) / lot["qty"]
        realized = sum(l["qty"] * l["price"] for l in lot["exits"]) / cost - 1
        day = dt.date.fromisoformat(entry["date"])
        pm_day = dt.date.fromisoformat(base_row["pm_date"])
        final = lot["exits"][-1]["utc"]
        rows.append({"symbol": entry["symbol"], "date": entry["date"], "entry_price": lot["price"],
                     "realized": realized, "archived_return": entry["return"],
                     "base0430": base_row.get("base0430"), "measured": base_row["measured"] and missing == 0,
                     "exit_bucket": bucket(day, final, pm_day), "legs": len(exits),
                     "gap": realized - base_row["base0430"] if base_row["measured"] else None,
                     "execution": execution if missing == 0 else None,
                     "timing": timing if missing == 0 else None, "exits": exits})
    for r in rows:
        if abs(r["realized"] - r["archived_return"]) > 1e-9:
            raise ValueError(f"{r['symbol']} {r['date']}: realized {r['realized']} != {r['archived_return']}")
    measured = [r for r in rows if r["measured"]]
    by_bucket = {}
    for r in measured:
        by_bucket.setdefault(r["exit_bucket"], []).append(r)
    legs = [e for r in measured for e in r["exits"] if e["spread_pct_of_mid"] is not None]
    result = {
        "study": "init3-exec-gap", "entries": len(rows), "measured": len(measured),
        "unmeasured": [f"{r['symbol']} {r['date']}" for r in rows if not r["measured"]],
        "total": {k: stats([r[k] for r in measured]) for k in ("gap", "execution", "timing")},
        "by_exit_bucket": {b: {k: stats([r[k] for r in g]) for k in ("gap", "execution", "timing")}
                           for b, g in sorted(by_bucket.items())},
        "exit_legs": {"n": len(legs),
                      "spread_pct_of_mid": stats([e["spread_pct_of_mid"] / 100 for e in legs]),
                      "fill_vs_bid_pct": stats([e["vs_bid_pct"] / 100 for e in legs]),
                      "quote_age_s_median": statistics.median(e["quote_age_s"] for e in legs)},
        "rows": rows}
    print(json.dumps(result, indent=1))


if __name__ == "__main__":
    main()
