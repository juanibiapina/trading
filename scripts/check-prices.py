#!/usr/bin/env python3
"""
Check current prices for given tickers, including premarket/after-hours data.

Usage:
    python scripts/check-prices.py TICKER1 TICKER2 ...
    python scripts/check-prices.py --ah-history TICKER1 TICKER2 ...
    python scripts/check-prices.py --pm-history TICKER1 TICKER2 ...

Modes:
    default:       Show current price, premarket price, and change from close
    --ah-history:  Show after-hours price action (5-min intervals, 16:00-20:00 ET)
    --pm-history:  Show premarket price action (5-min intervals, 04:00-09:30 ET)
"""

import argparse
import json
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone, timedelta

ET = timezone(timedelta(hours=-5))


def fetch_yahoo(ticker, interval="1m", range_str="1d", include_pre_post=True):
    """Fetch data from Yahoo Finance API."""
    url = (
        f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
        f"?interval={interval}&range={range_str}"
        f"&includePrePost={'true' if include_pre_post else 'false'}"
    )
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        resp = urllib.request.urlopen(req, timeout=10)
        return json.loads(resp.read())
    except Exception as e:
        print(f"  {ticker}: Error fetching data: {e}", file=sys.stderr)
        return None


def get_current_price(ticker):
    """Get current/latest price info for a ticker."""
    data = fetch_yahoo(ticker, interval="1m", range_str="1d")
    if not data or "chart" not in data:
        return None

    result = data["chart"]["result"][0]
    meta = result["meta"]

    return {
        "ticker": ticker,
        "regular_price": meta.get("regularMarketPrice"),
        "previous_close": meta.get("previousClose") or meta.get("chartPreviousClose"),
        "current_price": meta.get("regularMarketPrice"),
        "pre_market_price": meta.get("preMarketPrice"),
        "post_market_price": meta.get("postMarketPrice"),
        "exchange": meta.get("exchangeName"),
        "name": meta.get("longName") or meta.get("shortName", ""),
    }


def get_ah_history(ticker):
    """Get after-hours price action using 5-min intervals."""
    data = fetch_yahoo(ticker, interval="5m", range_str="5d")
    if not data or "chart" not in data:
        return None

    result = data["chart"]["result"][0]
    meta = result["meta"]
    timestamps = result.get("timestamp", [])
    quotes = result["indicators"]["quote"][0]
    closes = quotes.get("close", [])
    volumes = quotes.get("volume", [])

    # Get trading periods to identify AH bars
    trading_periods = meta.get("currentTradingPeriod", {})
    regular_end = trading_periods.get("regular", {}).get("end", 0)
    post_end = trading_periods.get("post", {}).get("end", 0)

    # Find the most recent trading day's AH bars
    ah_bars = []
    for i, ts in enumerate(timestamps):
        dt = datetime.fromtimestamp(ts, tz=ET)
        hour, minute = dt.hour, dt.minute
        t = hour * 60 + minute
        # After-hours: 4:00 PM - 8:00 PM ET
        if 16 * 60 <= t < 20 * 60:
            price = closes[i] if i < len(closes) else None
            vol = volumes[i] if i < len(volumes) else None
            if price is not None:
                ah_bars.append({
                    "time": dt.strftime("%H:%M"),
                    "date": dt.strftime("%Y-%m-%d"),
                    "price": price,
                    "volume": vol or 0,
                })

    # Group by date, return most recent day
    if not ah_bars:
        return None

    latest_date = ah_bars[-1]["date"]
    latest_bars = [b for b in ah_bars if b["date"] == latest_date]

    previous_close = meta.get("previousClose") or meta.get("chartPreviousClose")

    return {
        "ticker": ticker,
        "date": latest_date,
        "previous_close": previous_close,
        "regular_close": meta.get("regularMarketPrice"),
        "bars": latest_bars,
        "ah_high": max(b["price"] for b in latest_bars) if latest_bars else None,
        "ah_low": min(b["price"] for b in latest_bars) if latest_bars else None,
        "ah_volume": sum(b["volume"] for b in latest_bars),
        "name": meta.get("longName") or meta.get("shortName", ""),
    }


def get_pm_history(ticker):
    """Get premarket price action using 5-min intervals."""
    data = fetch_yahoo(ticker, interval="5m", range_str="5d")
    if not data or "chart" not in data:
        return None

    result = data["chart"]["result"][0]
    meta = result["meta"]
    timestamps = result.get("timestamp", [])
    quotes = result["indicators"]["quote"][0]
    closes = quotes.get("close", [])
    volumes = quotes.get("volume", [])

    # Find the most recent trading day's PM bars
    pm_bars = []
    for i, ts in enumerate(timestamps):
        dt = datetime.fromtimestamp(ts, tz=ET)
        hour, minute = dt.hour, dt.minute
        t = hour * 60 + minute
        # Premarket: 4:00 AM - 9:30 AM ET
        if 4 * 60 <= t < 9 * 60 + 30:
            price = closes[i] if i < len(closes) else None
            vol = volumes[i] if i < len(volumes) else None
            if price is not None:
                pm_bars.append({
                    "time": dt.strftime("%H:%M"),
                    "date": dt.strftime("%Y-%m-%d"),
                    "price": price,
                    "volume": vol or 0,
                })

    if not pm_bars:
        return None

    latest_date = pm_bars[-1]["date"]
    latest_bars = [b for b in pm_bars if b["date"] == latest_date]

    previous_close = meta.get("previousClose") or meta.get("chartPreviousClose")

    return {
        "ticker": ticker,
        "date": latest_date,
        "previous_close": previous_close,
        "bars": latest_bars,
        "pm_high": max(b["price"] for b in latest_bars) if latest_bars else None,
        "pm_low": min(b["price"] for b in latest_bars) if latest_bars else None,
        "pm_volume": sum(b["volume"] for b in latest_bars),
        "name": meta.get("longName") or meta.get("shortName", ""),
    }


def fmt_number(n):
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n / 1_000:.0f}K"
    return str(int(n))


def main():
    parser = argparse.ArgumentParser(description="Check prices via Yahoo Finance")
    parser.add_argument("tickers", nargs="+", help="Ticker symbols to check")
    parser.add_argument("--ah-history", action="store_true",
                        help="Show after-hours price history (16:00-20:00 ET)")
    parser.add_argument("--pm-history", action="store_true",
                        help="Show premarket price history (04:00-09:30 ET)")
    args = parser.parse_args()

    if args.pm_history:
        results = {}
        with ThreadPoolExecutor(max_workers=len(args.tickers)) as pool:
            futures = {pool.submit(get_pm_history, t): t for t in args.tickers}
            for future in as_completed(futures):
                ticker = futures[future]
                try:
                    results[ticker] = future.result()
                except Exception:
                    results[ticker] = None

        for ticker in args.tickers:
            info = results[ticker]
            if not info:
                print(f"\n{ticker}: No PM data available")
                continue

            prev = info["previous_close"] or 0
            print(f"\n{'=' * 60}")
            print(f"{ticker} — {info['name']}")
            print(f"Date: {info['date']}  |  Prev Close: ${prev:.2f}")
            print(f"PM High: ${info['pm_high']:.2f}  |  PM Low: ${info['pm_low']:.2f}  |  PM Vol: {fmt_number(info['pm_volume'])}")
            if prev > 0:
                pm_chg = ((info['pm_high'] - prev) / prev) * 100
                print(f"PM Peak Change: {pm_chg:+.1f}%")
            print(f"{'-' * 60}")
            print(f"  {'Time':<8} {'Price':>8} {'Vol':>8} {'Chg%':>8}")
            for bar in info["bars"]:
                chg = ((bar["price"] - prev) / prev * 100) if prev > 0 else 0
                print(f"  {bar['time']:<8} ${bar['price']:>7.2f} {fmt_number(bar['volume']):>8} {chg:>+7.1f}%")

    elif args.ah_history:
        # Fetch all tickers in parallel to avoid sequential timeout accumulation
        results = {}
        with ThreadPoolExecutor(max_workers=len(args.tickers)) as pool:
            futures = {pool.submit(get_ah_history, t): t for t in args.tickers}
            for future in as_completed(futures):
                ticker = futures[future]
                try:
                    results[ticker] = future.result()
                except Exception:
                    results[ticker] = None

        for ticker in args.tickers:
            info = results[ticker]
            if not info:
                print(f"\n{ticker}: No AH data available")
                continue

            prev = info["previous_close"] or 0
            print(f"\n{'=' * 60}")
            print(f"{ticker} — {info['name']}")
            print(f"Date: {info['date']}  |  Prev Close: ${prev:.2f}")
            print(f"AH High: ${info['ah_high']:.2f}  |  AH Low: ${info['ah_low']:.2f}  |  AH Vol: {fmt_number(info['ah_volume'])}")
            if prev > 0:
                ah_chg = ((info['ah_high'] - prev) / prev) * 100
                print(f"AH Peak Change: {ah_chg:+.1f}%")
            print(f"{'-' * 60}")
            print(f"  {'Time':<8} {'Price':>8} {'Vol':>8} {'Chg%':>8}")
            for bar in info["bars"]:
                chg = ((bar["price"] - prev) / prev * 100) if prev > 0 else 0
                print(f"  {bar['time']:<8} ${bar['price']:>7.2f} {fmt_number(bar['volume']):>8} {chg:>+7.1f}%")
    else:
        # Fetch all tickers in parallel
        results = {}
        with ThreadPoolExecutor(max_workers=len(args.tickers)) as pool:
            futures = {pool.submit(get_current_price, t): t for t in args.tickers}
            for future in as_completed(futures):
                ticker = futures[future]
                try:
                    results[ticker] = future.result()
                except Exception:
                    results[ticker] = None

        print(f"\n{'Ticker':<8} {'Close':>8} {'PM Price':>9} {'PM Chg%':>8} {'AH Price':>9} {'AH Chg%':>8}")
        print(f"{'-' * 55}")
        for ticker in args.tickers:
            info = results[ticker]
            if not info:
                print(f"{ticker:<8} {'N/A':>8}")
                continue

            close = info["previous_close"] or info["regular_price"] or 0
            pm = info["pre_market_price"]
            ah = info["post_market_price"]
            pm_chg = ((pm - close) / close * 100) if pm and close else 0
            ah_chg = ((ah - close) / close * 100) if ah and close else 0

            pm_str = f"${pm:.2f}" if pm else "—"
            ah_str = f"${ah:.2f}" if ah else "—"
            pm_chg_str = f"{pm_chg:+.1f}%" if pm else "—"
            ah_chg_str = f"{ah_chg:+.1f}%" if ah else "—"

            print(f"{ticker:<8} ${close:>7.2f} {pm_str:>9} {pm_chg_str:>8} {ah_str:>9} {ah_chg_str:>8}")


if __name__ == "__main__":
    main()
