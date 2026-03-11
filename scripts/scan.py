#!/usr/bin/env python3
"""
Micro-cap volume spike scanner.

Uses TradingView's screener API to find stocks with unusual volume.
Auto-detects the current trading session (premarket, regular, after-hours)
and uses the appropriate fields for each.

Usage:
    python scripts/scan.py              # Single scan (auto-detect session)
    python scripts/scan.py --watch      # Poll every 60s
    python scripts/scan.py --watch 30   # Poll every 30s
    python scripts/scan.py --all        # All sectors (default: biotech only)
"""

import argparse
import subprocess
import sys
import time
from datetime import datetime, timezone, timedelta

import requests

API_URL = "https://scanner.tradingview.com/america/scan"

ET = timezone(timedelta(hours=-5))

# Common filters
MIN_PRICE = 0.5
MAX_PRICE = 10.0
MAX_MARKET_CAP = 100_000_000  # $100M
SECTOR = "Health Technology"

# Regular session filters
MIN_INTRADAY_RVOL = 10       # 10x the typical volume for this time of day
MIN_5M_VOLUME = 5000         # Absolute minimum volume per 5m bar

# Premarket filters
MIN_PM_VOLUME = 50_000       # Minimum premarket volume
MIN_PM_CHANGE = 5            # Minimum premarket change %

# After-hours filters
MIN_AH_VOLUME = 50_000       # Minimum after-hours volume
MIN_AH_CHANGE = 5            # Minimum after-hours change %


def get_session():
    """Detect current trading session based on ET time.

    Returns one of: 'premarket', 'regular', 'afterhours', 'closed'.
    """
    now = datetime.now(ET)
    hour, minute = now.hour, now.minute
    t = hour * 60 + minute  # minutes since midnight

    if t < 4 * 60:          # before 4:00 AM
        return "closed"
    elif t < 9 * 60 + 30:   # 4:00 AM - 9:30 AM
        return "premarket"
    elif t < 16 * 60:       # 9:30 AM - 4:00 PM
        return "regular"
    elif t < 20 * 60:       # 4:00 PM - 8:00 PM
        return "afterhours"
    else:
        return "closed"


# --- Column definitions per session ---

COLUMNS_REGULAR = [
    "name",
    "close",
    "change",
    "volume|5",
    "average_volume_10d_calc|5",
    "relative_volume_intraday|5",
    "volume_change|5",
    "sector",
    "industry",
    "float_shares_outstanding",
    "market_cap_basic",
]

COLUMNS_PREMARKET = [
    "name",
    "close",
    "premarket_change",
    "premarket_volume",
    "premarket_close",
    "average_volume_10d_calc",
    "sector",
    "industry",
    "float_shares_outstanding",
    "market_cap_basic",
]

COLUMNS_AFTERHOURS = [
    "name",
    "close",
    "postmarket_change",
    "postmarket_volume",
    "postmarket_close",
    "average_volume_10d_calc",
    "change",                      # regular session change % (from prev close)
    "sector",
    "industry",
    "float_shares_outstanding",
    "market_cap_basic",
]


def build_filters(session, biotech_only=True):
    """Build filter list appropriate for the current session."""
    filters = [
        {"left": "market_cap_basic", "operation": "in_range", "right": [0, MAX_MARKET_CAP]},
        {"left": "close", "operation": "in_range", "right": [MIN_PRICE, MAX_PRICE]},
    ]

    if session == "regular":
        filters.extend([
            {"left": "relative_volume_intraday|5", "operation": "greater", "right": MIN_INTRADAY_RVOL},
            {"left": "volume|5", "operation": "greater", "right": MIN_5M_VOLUME},
        ])
    elif session == "premarket":
        filters.extend([
            {"left": "premarket_volume", "operation": "greater", "right": MIN_PM_VOLUME},
            {"left": "premarket_change", "operation": "greater", "right": MIN_PM_CHANGE},
        ])
    elif session == "afterhours":
        filters.extend([
            {"left": "postmarket_volume", "operation": "greater", "right": MIN_AH_VOLUME},
            {"left": "postmarket_change", "operation": "greater", "right": MIN_AH_CHANGE},
        ])

    if biotech_only:
        filters.append({"left": "sector", "operation": "equal", "right": SECTOR})

    return filters


def get_sort_field(session):
    """Return the sort field for the current session."""
    if session == "regular":
        return "relative_volume_intraday|5"
    elif session == "premarket":
        return "premarket_volume"
    elif session == "afterhours":
        return "postmarket_volume"
    return "volume"


def get_columns(session):
    """Return the columns for the current session."""
    if session == "premarket":
        return COLUMNS_PREMARKET
    elif session == "afterhours":
        return COLUMNS_AFTERHOURS
    return COLUMNS_REGULAR


def scan(session, biotech_only=True):
    """Run a single scan and return results."""
    columns = get_columns(session)
    payload = {
        "columns": columns,
        "filter": build_filters(session, biotech_only),
        "sort": {"sortBy": get_sort_field(session), "sortOrder": "desc"},
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

        if session == "regular":
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
                "sector": d[7],
                "industry": d[8],
                "float": int(d[9]) if d[9] else 0,
                "market_cap": int(d[10]) if d[10] else 0,
            })
        elif session == "premarket":
            avg_vol = int(d[5]) if d[5] else 0
            pm_vol = int(d[3]) if d[3] else 0
            results.append({
                "ticker": ticker,
                "exchange": exchange,
                "name": d[0],
                "price": d[1],
                "change_pct": d[2] or 0,
                "ext_volume": pm_vol,
                "ext_close": d[4] or 0,
                "avg_vol_daily": avg_vol,
                "vol_ratio": round(pm_vol / avg_vol, 1) if avg_vol else 0,
                "sector": d[6],
                "industry": d[7],
                "float": int(d[8]) if d[8] else 0,
                "market_cap": int(d[9]) if d[9] else 0,
            })
        elif session == "afterhours":
            avg_vol = int(d[5]) if d[5] else 0
            ah_vol = int(d[3]) if d[3] else 0
            results.append({
                "ticker": ticker,
                "exchange": exchange,
                "name": d[0],
                "price": d[1],
                "change_pct": d[2] or 0,
                "ext_volume": ah_vol,
                "ext_close": d[4] or 0,
                "avg_vol_daily": avg_vol,
                "vol_ratio": round(ah_vol / avg_vol, 1) if avg_vol else 0,
                "day_change_pct": d[6] or 0,
                "sector": d[7],
                "industry": d[8],
                "float": int(d[9]) if d[9] else 0,
                "market_cap": int(d[10]) if d[10] else 0,
            })

    return results


def fmt_number(n):
    """Format large numbers with K/M suffix."""
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n / 1_000:.0f}K"
    return str(n)


def print_results(results, session, previous_tickers=None):
    """Print results in a formatted table."""
    et = datetime.now(ET)
    session_label = {
        "premarket": "PREMARKET",
        "regular": "REGULAR",
        "afterhours": "AFTER-HOURS",
        "closed": "CLOSED",
    }[session]

    mode = "biotech" if any(r.get("sector") == SECTOR for r in results) else "all"

    print(f"\n{'=' * 115}")
    print(f"  {session_label} Scan: {et.strftime('%Y-%m-%d %H:%M:%S')} ET  |  {len(results)} hits")
    print(f"{'=' * 115}")

    if not results:
        print("  No matches.")
        return

    if session == "regular":
        print(f"  {'Ticker':<8} {'Price':>6} {'Chg%':>7} {'5mVol':>8} {'Avg5m':>8} {'IRVol':>7} {'VChg%':>7} {'Float':>8} {'MCap':>8} {'Industry':<25} {'New'}")
        print(f"  {'-' * 109}")

        for r in results:
            is_new = ""
            if previous_tickers is not None and r["ticker"] not in previous_tickers:
                is_new = " ⚡ NEW"

            print(
                f"  {r['ticker']:<8} "
                f"{r['price']:>6.2f} "
                f"{r['change_pct']:>+7.1f} "
                f"{fmt_number(r['vol_5m']):>8} "
                f"{fmt_number(r['avg_vol_5m']):>8} "
                f"{r['intraday_rvol']:>7.1f} "
                f"{r['vol_change_pct']:>+7.1f} "
                f"{fmt_number(r['float']):>8} "
                f"{fmt_number(r['market_cap']):>8} "
                f"{r['industry']:<25}"
                f"{is_new}"
            )
    else:
        # Premarket or after-hours
        ext_label = "PM" if session == "premarket" else "AH"
        show_day_chg = session == "afterhours"

        if show_day_chg:
            print(f"  {'Ticker':<8} {'Close':>6} {'Day%':>7} {ext_label + ' Chg%':>8} {ext_label + ' Price':>8} {ext_label + ' Vol':>8} {'AvgVol':>8} {'VRatio':>7} {'Float':>8} {'MCap':>8} {'Industry':<25} {'New'}")
            print(f"  {'-' * 120}")
        else:
            print(f"  {'Ticker':<8} {'Close':>6} {ext_label + ' Chg%':>8} {ext_label + ' Price':>8} {ext_label + ' Vol':>8} {'AvgVol':>8} {'VRatio':>7} {'Float':>8} {'MCap':>8} {'Industry':<25} {'New'}")
            print(f"  {'-' * 113}")

        for r in results:
            is_new = ""
            if previous_tickers is not None and r["ticker"] not in previous_tickers:
                is_new = " ⚡ NEW"

            day_chg = f"{r.get('day_change_pct', 0):>+7.1f} " if show_day_chg else ""

            print(
                f"  {r['ticker']:<8} "
                f"{r['price']:>6.2f} "
                f"{day_chg}"
                f"{r['change_pct']:>+8.1f} "
                f"{r['ext_close']:>8.2f} "
                f"{fmt_number(r['ext_volume']):>8} "
                f"{fmt_number(r['avg_vol_daily']):>8} "
                f"{r['vol_ratio']:>7.1f} "
                f"{fmt_number(r['float']):>8} "
                f"{fmt_number(r['market_cap']):>8} "
                f"{r['industry']:<25}"
                f"{is_new}"
            )


def notify(ticker, price, change_pct):
    """Send macOS desktop notification."""
    title = f"🔔 {ticker} volume spike"
    msg = f"${price:.2f} ({change_pct:+.1f}%)"
    try:
        subprocess.run(
            ["osascript", "-e", f'display notification "{msg}" with title "{title}"'],
            capture_output=True,
            timeout=5,
        )
    except Exception:
        pass


def watch(interval, session, biotech_only=True):
    """Poll continuously."""
    previous_tickers = set()
    mode = "biotech" if biotech_only else "all sectors"
    print(f"Watching every {interval}s ({mode}, {session})... (Ctrl+C to stop)")

    while True:
        try:
            # Re-detect session in case it changes during watch
            current_session = get_session()
            if current_session == "closed":
                print(f"\n  Market closed. Waiting...")
                time.sleep(interval)
                continue

            if current_session != session:
                print(f"\n  Session changed: {session} → {current_session}")
                session = current_session
                previous_tickers = set()

            results = scan(session, biotech_only)
            current_tickers = {r["ticker"] for r in results}
            print_results(results, session, previous_tickers)

            # Notify on new tickers
            for r in results:
                if r["ticker"] not in previous_tickers:
                    notify(r["ticker"], r["price"], r["change_pct"])

            previous_tickers = current_tickers
            time.sleep(interval)

        except KeyboardInterrupt:
            print("\nStopped.")
            break
        except Exception as e:
            print(f"  Error: {e}")
            time.sleep(interval)


def main():
    parser = argparse.ArgumentParser(description="Micro-cap volume spike scanner")
    parser.add_argument("--watch", nargs="?", const=60, type=int, metavar="SECS",
                        help="Poll continuously (default: every 60s)")
    parser.add_argument("--all", action="store_true",
                        help="Search all sectors (default: Health Technology only)")
    parser.add_argument("--session", choices=["premarket", "regular", "afterhours"],
                        help="Force a specific session (default: auto-detect)")
    args = parser.parse_args()

    biotech_only = not args.all

    if args.session:
        session = args.session
    else:
        session = get_session()
        if session == "closed":
            print("Market is closed (outside 4:00 AM - 8:00 PM ET).")
            sys.exit(0)

    print(f"Session: {session.upper()}")

    if args.watch:
        watch(args.watch, session, biotech_only)
    else:
        results = scan(session, biotech_only)
        print_results(results, session)


if __name__ == "__main__":
    main()
