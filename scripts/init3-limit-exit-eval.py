#!/usr/bin/env python3
"""Initiative 3 study, log-only: does a resting sell-limit exit beat the 04:30 ET market exit?

Uses the 89 real Alpaca AH entries archived by `volume-entry-eval.py` (entry price, fill time,
realized return, entry-evening SIP bars). Fetch mode adds each entry's next-session premarket
5-minute SIP bars (04:00-09:30 ET) under OUT/sip-pm; `--replay` recomputes offline.

Rules, each scored as a return on the real entry price:
  base0430    sell at the open of the first premarket bar at or after 04:30 ET (modeled market exit)
  exitL<k>    the standing proposal: at 04:30 rest a sell-limit k% above the base0430 price; fill
              at the limit on the first bar from 04:30 whose high reaches it; else sell at the last
              close before 09:30 ET
  entryL<k>   rest a sell-limit k% above the entry price from the first bar after the fill (rest of
              the AH evening, then premarket); fill at the limit on the first touch; else sell at
              the base0430 price
  exitV/entryV  the same rules, filling only when the bar's VWAP reaches the limit (most of the
              bar's volume traded near or above it), a conservative check on thin-print touches
  realized    the real paired exit (some real trades held past the next morning)

Limit fills at a touched 5-minute high are optimistic: a thin print can touch without filling.
Market exits at a bar open omit the spread, which also flatters the baselines.
"""

import argparse
import datetime as dt
import json
import os
from pathlib import Path
import random
import statistics
import urllib.parse
import urllib.request
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")
LIMITS = (5, 10, 15, 20)


def stamp(value):
    return dt.datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(dt.timezone.utc)


def at(day, hour, minute=0):
    return dt.datetime.combine(day, dt.time(hour, minute), ET).astimezone(dt.timezone.utc)


def fetch_pm(symbol, day):
    query = {"timeframe": "5Min", "feed": "sip", "adjustment": "raw",
             "start": at(day, 4).isoformat(), "end": at(day, 9, 30).isoformat(), "limit": 1000}
    headers = {"APCA-API-KEY-ID": os.environ["ALPACA_API_KEY"],
               "APCA-API-SECRET-KEY": os.environ["ALPACA_SECRET_KEY"]}
    url = os.environ.get("ALPACA_DATA_URL", "https://data.alpaca.markets").rstrip("/")
    request = urllib.request.Request(f"{url}/v2/stocks/{symbol}/bars?{urllib.parse.urlencode(query)}",
                                     headers=headers)
    with urllib.request.urlopen(request, timeout=25) as response:
        page = json.load(response)
    if page.get("next_page_token"):
        raise ValueError(f"Unexpected second page for {symbol} {day}")
    return {"symbol": symbol, "date": day.isoformat(), "feed": "sip", "timeframe": "5Min",
            "observed_utc": dt.datetime.now(dt.timezone.utc).isoformat(), "bars": page.get("bars") or []}


def first_touch(bars, target, key="h"):
    """Fill price and the touching bar's start time, or (None, None)."""
    for bar in bars:
        if bar[key] >= target:
            return target, bar["t"]
    return None, None


def evaluate(entry, ah_bars, pm_bars, day):
    price = entry["entry_price"]
    fill = stamp(entry["as_of_utc"]) + dt.timedelta(minutes=15)  # as_of = fill - 15 min lag
    cap = at(day, 9, 30)
    pm = [b for b in pm_bars if stamp(b["t"]) < cap]
    from0430 = [b for b in pm if stamp(b["t"]) >= at(day, 4, 30)]
    row = {"symbol": entry["symbol"], "date": entry["date"], "pm_date": day.isoformat(),
           "entry_price": price, "realized": entry["return"], "pm_bars": len(pm)}
    if not from0430:
        row["measured"] = False
        return row
    base = from0430[0]["o"]
    last = pm[-1]["c"]
    row.update(measured=True, base0430=base / price - 1, pm_high=max(b["h"] for b in pm) / price - 1,
               pm_last=last / price - 1)
    # Bars that start after the fill: a bar containing the fill may have peaked before it.
    after = [b for b in ah_bars if stamp(b["t"]) > fill] + pm
    for k in LIMITS:
        for tag, key in (("L", "h"), ("V", "vw")):
            hit, _ = first_touch(from0430, base * (1 + k / 100), key)
            row[f"exit{tag}{k}"] = (hit if hit is not None else last) / price - 1
            row[f"exit{tag}{k}_filled"] = hit is not None
            hit, when = first_touch(after, price * (1 + k / 100), key)
            row[f"entry{tag}{k}"] = (hit if hit is not None else base) / price - 1
            row[f"entry{tag}{k}_filled"] = hit is not None
            row[f"entry{tag}{k}_fill_session"] = None if when is None else ("pm" if stamp(when) >= at(day, 4) else "ah")
    return row


def paired(rows, rule, against):
    diffs = [r[rule] - r[against] for r in rows]
    observed = statistics.mean(diffs)
    rng, extreme = random.Random(7), 0
    for _ in range(10000):  # sign-flip test on the paired mean difference, seed 7
        flipped = statistics.mean(d if rng.random() < 0.5 else -d for d in diffs)
        extreme += abs(flipped) >= abs(observed) - 1e-12
    return {"mean_diff": observed, "better": sum(d > 1e-12 for d in diffs),
            "worse": sum(d < -1e-12 for d in diffs), "p": extreme / 10000}


def summary(rows, rule):
    values = [r[rule] for r in rows]
    top = sorted(rows, key=lambda r: r[rule], reverse=True)[:2]
    trimmed = [r[rule] for r in rows if r not in top]
    out = {"rule": rule, "n": len(values), "mean": statistics.mean(values), "median": statistics.median(values),
           "wins": sum(v > 0 for v in values), "mean_without_top2": statistics.mean(trimmed),
           "top2": [r["symbol"] for r in top]}
    filled = f"{rule}_filled"
    if filled in rows[0]:
        out["filled"] = sum(r[filled] for r in rows)
    if f"{rule}_fill_session" in rows[0]:
        out["filled_in_ah"] = sum(r[f"{rule}_fill_session"] == "ah" for r in rows)
    # Chronological halves: an edge that only shows in one half is not stable.
    order = sorted(rows, key=lambda r: r["date"])
    half = len(order) // 2
    out["mean_first_half"] = statistics.mean(r[rule] for r in order[:half])
    out["mean_second_half"] = statistics.mean(r[rule] for r in order[half:])
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("out", type=Path)
    parser.add_argument("--archive", type=Path, default=Path("log/2026-10-06/init1-volume-policy"))
    parser.add_argument("--replay", action="store_true")
    args = parser.parse_args()
    entries = json.loads((args.archive / "result.json").read_text())["entries"]
    calendar = [dt.date.fromisoformat(d["date"]) for d in json.loads((args.archive / "calendar.json").read_text())]
    pm_dir = args.out / "sip-pm"
    pm_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    for entry in entries:
        day = dt.date.fromisoformat(entry["date"])
        pm_day = calendar[calendar.index(day) + 1]
        path = pm_dir / f"{entry['symbol']}-{pm_day.isoformat()}.json"
        if not path.exists():
            if args.replay:
                raise FileNotFoundError(path)
            path.write_text(json.dumps(fetch_pm(entry["symbol"], pm_day), indent=1) + "\n")
        ah = json.loads((args.archive / "sip" / f"{entry['symbol']}-{entry['date']}.json").read_text())["bars"]
        ah = [b for b in ah if at(day, 16) <= stamp(b["t"]) < at(day, 20)]
        rows.append(evaluate(entry, ah, json.loads(path.read_text())["bars"], pm_day))
    measured = [r for r in rows if r["measured"]]
    rules = ["realized", "base0430"] + [f"{a}{t}{k}" for t in "LV" for a in ("exit", "entry") for k in LIMITS]
    result = {"study": "init3-limit-exit", "entries": len(rows), "measured": len(measured),
              "unmeasured": [f"{r['symbol']} {r['pm_date']}" for r in rows if not r["measured"]],
              "summaries": [summary(measured, rule) for rule in rules],
              "paired_vs_base0430": {rule: paired(measured, rule, "base0430") for rule in rules[2:] + ["realized"]},
              "rows": rows}
    print(json.dumps(result, indent=1))


if __name__ == "__main__":
    main()
