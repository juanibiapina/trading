#!/usr/bin/env python3
"""Record one immutable, early premarket Initiative 6 shadow cohort per ET trading day."""

import argparse
import csv
import os
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import requests

from scan import scan

ET = ZoneInfo("America/New_York")
OUT = Path(__file__).resolve().parent.parent / "log" / "init6-cohort"
FIELDS = (
    "observed_utc", "ticker", "exchange", "pm_change_pct", "pm_price",
    "pm_volume", "quote_utc", "bid", "bid_size", "ask", "ask_size",
    "bid_exchange", "ask_exchange", "quote_age_sec", "quote_status",
)


def quote(symbol, observed):
    key = os.environ.get("ALPACA_API_KEY")
    secret = os.environ.get("ALPACA_SECRET_KEY")
    if not key or not secret:
        return {"quote_status": "missing credentials"}
    try:
        resp = requests.get(
            f"{os.environ.get('ALPACA_DATA_URL', 'https://data.alpaca.markets')}/v2/stocks/{symbol}/quotes/latest",
            params={"feed": "iex"},
            headers={"APCA-API-KEY-ID": key, "APCA-API-SECRET-KEY": secret},
            timeout=6,
        )
        resp.raise_for_status()
        q = resp.json().get("quote") or {}
        stamp = q.get("t", "")
        age = (observed - datetime.fromisoformat(stamp.replace("Z", "+00:00"))).total_seconds() if stamp else ""
        return {
            "quote_utc": stamp, "bid": q.get("bp", ""), "bid_size": q.get("bs", ""),
            "ask": q.get("ap", ""), "ask_size": q.get("as", ""),
            "bid_exchange": q.get("bx", ""), "ask_exchange": q.get("ax", ""),
            "quote_age_sec": round(age, 1) if age != "" else "",
            "quote_status": "two-sided" if q.get("bp", 0) > 0 and q.get("ap", 0) > 0 else "missing side",
        }
    except (requests.RequestException, ValueError) as exc:
        return {"quote_status": type(exc).__name__}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="check data sources without writing a cohort")
    args = parser.parse_args()
    now = datetime.now(timezone.utc)
    local = now.astimezone(ET)
    minute = local.hour * 60 + local.minute
    if not args.dry_run and (local.weekday() > 4 or not 4 * 60 + 7 <= minute <= 4 * 60 + 14):
        raise SystemExit(f"Snapshot only writes 04:07-04:14 ET weekdays; now {local:%Y-%m-%d %H:%M ET}. No cohort written.")
    dest = OUT / f"{local:%Y-%m-%d}.csv"
    if dest.exists() and not args.dry_run:
        raise SystemExit(f"Cohort already captured: {dest}")

    # scan() uses the same filters and top-50 volume sort as the PM-open pulse.
    candidates = scan("premarket")
    observed = datetime.now(timezone.utc)
    with ThreadPoolExecutor(max_workers=6) as pool:
        quotes = list(pool.map(lambda c: quote(c["ticker"], observed), candidates))
    rows = [
        {
            "observed_utc": observed.isoformat(), "ticker": c["ticker"],
            "exchange": c["exchange"], "pm_change_pct": c["change_pct"],
            "pm_price": c["ext_close"], "pm_volume": c["ext_volume"], **q,
        }
        for c, q in zip(candidates, quotes)
    ]
    if args.dry_run:
        print(f"DRY RUN {local:%Y-%m-%d %H:%M ET}: {len(rows)} candidates; "
              f"{sum(r['quote_status'] == 'two-sided' for r in rows)} two-sided IEX quotes; no file written")
        return
    OUT.mkdir(parents=True, exist_ok=True)
    with dest.open("x", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Captured {len(rows)} PM candidates at {local:%H:%M ET} in {dest}; "
          f"{sum(r['quote_status'] == 'two-sided' for r in rows)} two-sided IEX quotes. "
          "IEX quote availability is not a SIP or paper fill guarantee.")


if __name__ == "__main__":
    main()
