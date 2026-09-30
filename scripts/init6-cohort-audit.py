#!/usr/bin/env python3
"""Compare a frozen Initiative 6 discovery cohort with the later PM tracker."""

import argparse
import csv
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
ET = ZoneInfo("America/New_York")


def rows(path):
    with path.open(newline="") as file:
        return list(csv.DictReader(file))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("date", type=date.fromisoformat, help="US trading date, YYYY-MM-DD")
    args = parser.parse_args()
    day = args.date.isoformat()
    cohort = rows(ROOT / "log" / "init6-cohort" / f"{day}.csv")
    tracker = [r for r in rows(ROOT / "log" / "pm-open-scan.csv") if r["date"] == day]
    frozen = {r["ticker"]: r for r in cohort}
    observed = {r["observed_utc"] for r in cohort}
    if len(observed) != 1 or len(frozen) != len(cohort):
        raise ValueError("Cohort needs one observation time and unique tickers")
    snapshot = datetime.fromisoformat(observed.pop()).astimezone(ET)
    if snapshot.date() != args.date:
        raise ValueError("Cohort observation date does not match requested ET date")

    with_age = [float(r["quote_age_sec"]) for r in cohort if r["quote_age_sec"]]
    fresh_ask = [r for r in cohort if r["quote_age_sec"] and float(r["quote_age_sec"]) <= 60
                 and float(r["ask"] or 0) > 0 and float(r["ask_size"] or 0) > 0]
    two_sided = [r for r in cohort if r["quote_status"] == "two-sided"]
    pm_only = [r for r in tracker if r["ah_footprint"] == "none"]
    overlap = [r for r in tracker if r["ticker"] in frozen]

    print(f"{day}: frozen at {snapshot:%H:%M:%S ET}; {len(cohort)} names; "
          f"later tracker {len(tracker)} names ({len(pm_only)} marked PM-only)")
    print(f"Tracker overlap: {len(overlap)}/{len(tracker)}; "
          f"PM-only overlap: {sum(r['ticker'] in frozen for r in pm_only)}/{len(pm_only)}")
    for r in tracker:
        print(f"  {r['ticker']}: {r['ah_footprint']}, {r['classification']}, "
              f"{'captured' if r['ticker'] in frozen else 'absent at snapshot'}")
    print(f"Quotes: {len(two_sided)} labeled two-sided; {len(fresh_ask)} asks <=60s old "
          f"with positive size; {len(cohort) - len(with_age)} ages unavailable")
    if with_age:
        print(f"Quote age: {min(with_age):.0f}–{max(with_age):.0f}s")
    print("Tracker only classifies selected gappers after the observation; "
          "uncatalogued cohort names and late igniters have no verified outcome here.")


if __name__ == "__main__":
    main()
