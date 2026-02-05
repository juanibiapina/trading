#!/usr/bin/env python3
"""
Biotech micro-cap volume spike scanner.

Uses TradingView's screener API to find Health Technology stocks
with unusual intraday volume on the 5-minute timeframe.

Usage:
    python scanner/scan.py              # Single scan
    python scanner/scan.py --watch      # Poll every 60s
    python scanner/scan.py --watch 30   # Poll every 30s
"""

import argparse
import json
import subprocess
import sys
import time
from datetime import datetime, timezone, timedelta

import requests

API_URL = "https://scanner.tradingview.com/america/scan"

# Filters
MIN_INTRADAY_RVOL = 10      # 10x the typical volume for this time of day
MIN_5M_VOLUME = 5000         # Absolute minimum volume per 5m bar
MIN_PRICE = 0.5
MAX_PRICE = 10.0
MAX_MARKET_CAP = 100_000_000  # $100M
SECTOR = "Health Technology"

COLUMNS = [
    "name",
    "close",
    "change",
    "volume|5",
    "average_volume_10d_calc|5",
    "relative_volume_intraday|5",
    "volume_change|5",
    "postmarket_change",
    "postmarket_volume",
    "postmarket_close",
    "sector",
    "industry",
    "float_shares_outstanding",
    "market_cap_basic",
]

FILTERS = [
    {"left": "relative_volume_intraday|5", "operation": "greater", "right": MIN_INTRADAY_RVOL},
    {"left": "market_cap_basic", "operation": "in_range", "right": [0, MAX_MARKET_CAP]},
    {"left": "close", "operation": "in_range", "right": [MIN_PRICE, MAX_PRICE]},
    {"left": "sector", "operation": "equal", "right": SECTOR},
    {"left": "volume|5", "operation": "greater", "right": MIN_5M_VOLUME},
]


def scan():
    """Run a single scan and return results."""
    payload = {
        "columns": COLUMNS,
        "filter": FILTERS,
        "sort": {"sortBy": "relative_volume_intraday|5", "sortOrder": "desc"},
        "markets": ["america"],
        "symbols": {"query": {"types": ["stock"]}},
        "options": {"lang": "en"},
        "range": [0, 50],
    }

    resp = requests.post(API_URL, json=payload, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    results = []
    for item in data.get("data", []):
        ticker = item["s"].split(":")[1]
        exchange = item["s"].split(":")[0]
        d = item["d"]

        results.append({
            "ticker": ticker,
            "exchange": exchange,
            "name": d[0],
            "price": d[1],
            "change_pct": d[2] or 0,
            "vol_5m": int(d[3]) if d[3] else 0,
            "avg_vol_5m": int(d[4]) if d[4] else 0,
            "intraday_rvol": d[5] or 0,
            "vol_change_pct": d[6] or 0,
            "pm_change_pct": d[7] or 0,
            "pm_volume": int(d[8]) if d[8] else 0,
            "pm_close": d[9] or 0,
            "sector": d[10],
            "industry": d[11],
            "float": int(d[12]) if d[12] else 0,
            "market_cap": int(d[13]) if d[13] else 0,
        })

    return results


def fmt_number(n):
    """Format large numbers with K/M suffix."""
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n / 1_000:.0f}K"
    return str(n)


def print_results(results, previous_tickers=None):
    """Print results in a formatted table."""
    et = datetime.now(timezone(timedelta(hours=-5)))
    print(f"\n{'=' * 110}")
    print(f"  Scan: {et.strftime('%Y-%m-%d %H:%M:%S')} ET  |  {len(results)} hits  |  IntraRVol>{MIN_INTRADAY_RVOL}x  Vol>{MIN_5M_VOLUME}")
    print(f"{'=' * 110}")

    if not results:
        print("  No matches.")
        return

    print(f"  {'Ticker':<8} {'Price':>6} {'Chg%':>6} {'5mVol':>8} {'Avg5m':>8} {'IRVol':>7} {'VChg%':>7} {'Float':>8} {'MCap':>8} {'Industry':<25} {'New'}")
    print(f"  {'-' * 104}")

    for r in results:
        is_new = ""
        if previous_tickers is not None and r["ticker"] not in previous_tickers:
            is_new = " ⚡ NEW"

        print(
            f"  {r['ticker']:<8} "
            f"{r['price']:>6.2f} "
            f"{r['change_pct']:>+6.1f} "
            f"{fmt_number(r['vol_5m']):>8} "
            f"{fmt_number(r['avg_vol_5m']):>8} "
            f"{r['intraday_rvol']:>7.1f} "
            f"{r['vol_change_pct']:>+7.1f} "
            f"{fmt_number(r['float']):>8} "
            f"{fmt_number(r['market_cap']):>8} "
            f"{r['industry']:<25}"
            f"{is_new}"
        )

    # Post-market data if available
    pm_results = [r for r in results if r["pm_volume"] > 0]
    if pm_results:
        print(f"\n  Post-market data:")
        for r in pm_results:
            print(f"    {r['ticker']}: PM close ${r['pm_close']:.2f} ({r['pm_change_pct']:+.1f}%) vol {fmt_number(r['pm_volume'])}")


def notify(ticker, price, intraday_rvol, change_pct):
    """Send macOS desktop notification."""
    title = f"🔔 {ticker} volume spike"
    msg = f"${price:.2f} ({change_pct:+.1f}%) | {intraday_rvol:.0f}x intraday vol"
    try:
        subprocess.run(
            ["osascript", "-e", f'display notification "{msg}" with title "{title}"'],
            capture_output=True,
            timeout=5,
        )
    except Exception:
        pass


def watch(interval):
    """Poll continuously."""
    previous_tickers = set()
    print(f"Watching every {interval}s... (Ctrl+C to stop)")

    while True:
        try:
            results = scan()
            current_tickers = {r["ticker"] for r in results}
            print_results(results, previous_tickers)

            # Notify on new tickers
            for r in results:
                if r["ticker"] not in previous_tickers:
                    notify(r["ticker"], r["price"], r["intraday_rvol"], r["change_pct"])

            previous_tickers = current_tickers
            time.sleep(interval)

        except KeyboardInterrupt:
            print("\nStopped.")
            break
        except Exception as e:
            print(f"  Error: {e}")
            time.sleep(interval)


def main():
    parser = argparse.ArgumentParser(description="Biotech volume spike scanner")
    parser.add_argument("--watch", nargs="?", const=60, type=int, metavar="SECS",
                        help="Poll continuously (default: every 60s)")
    args = parser.parse_args()

    if args.watch:
        watch(args.watch)
    else:
        results = scan()
        print_results(results)


if __name__ == "__main__":
    main()
