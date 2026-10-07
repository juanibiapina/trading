#!/usr/bin/env python3
"""Initiative 3 study, log-only: would a later-rebuild AH entry beat the real entries?

Offline replay of the archive built by `volume-entry-eval.py` (89 real Alpaca AH entries, each
with 5-minute SIP bars through the entry evening and its realized return). No network, orders or
rule changes.

Gate (ported from `ah-5m-confirmation-replay.js`): an ignition is a green 5-minute AH bar that
closes >=10% above the regular close, makes a new AH high, has >=20 trades and volume >=2x the
median of up to three preceding active bars. Confirmation holds every later close at >=80% of
the running high and needs the confirming bar's close and volume at least the ignition's.

Variants:
  first   only the first ignition may confirm (the October 1-2 replay rule)
  rearm   after a failed confirmation, the next ignition (a later rebuild to a new AH high) may
          confirm; the first confirming ignition is used

Entry is the open of the first bar starting at least LAG minutes after the confirming bar
closes (15 = the measured screener and free-SIP delay). The exit is the real trade's realized
exit price, so each variant changes only selection and entry price. Bar opens carry no spread,
while real fills crossed it, so variant returns lean optimistic by about half a spread.
The regular close is the last 5-minute bar before 16:00 ET, not the official closing auction.
"""

import argparse
import datetime as dt
import json
import random
import statistics
from pathlib import Path
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")
PRICE_MIN, VOLUME_JUMP, MIN_TRADES, HOLD_FRAC = 1.10, 2, 20, 0.8
SLOT = dt.timedelta(minutes=5)


def stamp(value):
    return dt.datetime.fromisoformat(value.replace("Z", "+00:00"))


def sessions(bars, day):
    regular, ah = [], []
    for bar in bars:
        local = stamp(bar["t"]).astimezone(ET)
        if local.date() != day:
            continue
        if dt.time(9, 30) <= local.time() < dt.time(16, 0):
            regular.append(bar)
        elif dt.time(16, 0) <= local.time() < dt.time(20, 0):
            ah.append(bar)
    return regular, ah


def ignition(ah, base, start):
    for i in range(max(1, start), len(ah)):
        prior = [b for b in ah[max(0, i - 3):i] if b["v"] > 0]
        if not prior:
            continue
        bar = ah[i]
        if (bar["c"] >= base * PRICE_MIN and bar["c"] >= bar["o"]
                and bar["h"] > max(b["h"] for b in ah[:i]) and bar["n"] >= MIN_TRADES
                and bar["v"] / statistics.median(b["v"] for b in prior) >= VOLUME_JUMP):
            return i
    return None


def confirm(ah, i, offset):
    end = i + offset
    if end + 1 >= len(ah):
        return None
    high = ah[i]["h"]
    for k in range(i + 1, end + 1):
        high = max(high, ah[k]["h"])
        if ah[k]["c"] < high * HOLD_FRAC:
            return None
    if ah[end]["c"] < ah[i]["c"] or ah[end]["v"] < ah[i]["v"]:
        return None
    return end


def entry_bar(ah, end, lag):
    ready = stamp(ah[end]["t"]) + SLOT + dt.timedelta(minutes=lag)
    return next((b for b in ah if stamp(b["t"]) >= ready), None)


def evaluate(ah, base, offset, rearm, lag):
    start, number = 1, 0
    while True:
        i = ignition(ah, base, start)
        if i is None:
            return None
        number += 1
        end = confirm(ah, i, offset)
        if end is not None:
            bar = entry_bar(ah, end, lag)
            if bar is None:
                return None
            return {"ignition_et": stamp(ah[i]["t"]).astimezone(ET).strftime("%H:%M"), "ignition_number": number,
                    "entry_et": stamp(bar["t"]).astimezone(ET).strftime("%H:%M"), "entry": bar["o"]}
        if not rearm:
            return None
        start = i + 1


def permutation_p(selected, rest, seed=7, draws=10000):
    if not selected or not rest:
        return None
    pooled, k = selected + rest, len(selected)
    observed = statistics.mean(selected) - statistics.mean(rest)
    rng, hits = random.Random(seed), 0
    for _ in range(draws):
        rng.shuffle(pooled)
        if abs(statistics.mean(pooled[:k]) - statistics.mean(pooled[k:])) >= abs(observed) - 1e-12:
            hits += 1
    return hits / draws


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--archive", type=Path, default=Path("log/2026-10-06/init1-volume-policy"))
    parser.add_argument("--lags", default="15,0")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    entries = json.loads((args.archive / "result.json").read_text())["entries"]
    cases = []
    for entry in entries:
        day = dt.date.fromisoformat(entry["date"])
        bars = json.loads((args.archive / "sip" / f"{entry['symbol']}-{entry['date']}.json").read_text())["bars"]
        regular, ah = sessions(bars, day)
        exit_price = entry["entry_price"] * (1 + entry["return"])
        cases.append({"symbol": entry["symbol"], "date": entry["date"], "fill_et": entry["fill_et"],
                      "entry_price": entry["entry_price"], "exit_price": exit_price, "return": entry["return"],
                      "base": regular[-1]["c"] if regular else None, "ah": ah})
    base_returns = [c["return"] for c in cases]
    summary = {"study": "init3-rebuild-eval-v1", "archive": str(args.archive), "entries": len(cases),
               "base": {"n": len(cases), "mean_pct": statistics.mean(base_returns) * 100,
                        "median_pct": statistics.median(base_returns) * 100,
                        "wins": sum(r > 0 for r in base_returns)},
               "variants": []}
    for lag in [int(x) for x in args.lags.split(",")]:
        for offset, label in ((1, "2bar"), (2, "3bar")):
            for rearm in (False, True):
                name = f"{'rearm' if rearm else 'first'}-{label}-lag{lag}"
                admitted, rows = [], []
                for case in cases:
                    if case["base"] is None:
                        continue
                    result = evaluate(case["ah"], case["base"], offset, rearm, lag)
                    if not result:
                        continue
                    variant = case["exit_price"] / result["entry"] - 1
                    admitted.append(case)
                    rows.append({"symbol": case["symbol"], "date": case["date"], **result,
                                 "variant_return_pct": variant * 100, "actual_fill_et": case["fill_et"],
                                 "actual_entry": case["entry_price"], "actual_return_pct": case["return"] * 100,
                                 "legal_grid": result["entry_et"] >= "17:00"})
                keys = {(c["symbol"], c["date"]) for c in admitted}
                rest = [c["return"] for c in cases if (c["symbol"], c["date"]) not in keys]
                variant = [r["variant_return_pct"] / 100 for r in rows]
                actual = [r["actual_return_pct"] / 100 for r in rows]
                legal = [r["variant_return_pct"] / 100 for r in rows if r["legal_grid"]]
                summary["variants"].append({
                    "name": name, "admitted": len(rows),
                    "later_rebuild_admits": sum(r["ignition_number"] > 1 for r in rows),
                    "variant_mean_pct": statistics.mean(variant) * 100 if variant else None,
                    "variant_median_pct": statistics.median(variant) * 100 if variant else None,
                    "variant_wins": sum(v > 0 for v in variant),
                    "variant_usd_at_100": sum(variant) * 100,
                    "same_names_actual_mean_pct": statistics.mean(actual) * 100 if actual else None,
                    "price_effect_pct_points": (statistics.mean(variant) - statistics.mean(actual)) * 100 if variant else None,
                    "selection_p": permutation_p(actual, rest),
                    "entries_at_or_after_1700": len(legal),
                    "legal_mean_pct": statistics.mean(legal) * 100 if legal else None,
                    "rows": rows})
    for v in summary["variants"]:
        fmt = lambda x: "n/a" if x is None else f"{x:+.1f}%"
        print(f"{v['name']:<18} n={v['admitted']:>2} (rebuilds {v['later_rebuild_admits']}) "
              f"mean {fmt(v['variant_mean_pct'])} median {fmt(v['variant_median_pct'])} wins {v['variant_wins']} "
              f"${v['variant_usd_at_100']:+.0f} | same names actual {fmt(v['same_names_actual_mean_pct'])} "
              f"p={v['selection_p'] if v['selection_p'] is None else round(v['selection_p'], 3)} | "
              f">=17:00 n={v['entries_at_or_after_1700']} mean {fmt(v['legal_mean_pct'])}")
    b = summary["base"]
    print(f"base (89 real entries) mean {b['mean_pct']:+.1f}% median {b['median_pct']:+.1f}% wins {b['wins']}")
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("x") as file:
            file.write(json.dumps(summary, indent=2) + "\n")


if __name__ == "__main__":
    main()
