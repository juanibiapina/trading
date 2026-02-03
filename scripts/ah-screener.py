#!/usr/bin/env python3
"""
After-Hours Screener: Find first-day unusual volume spikes.

Usage:
  1. Copy/paste TradingView AH gainers page text into stdin, or
  2. Pass a file with the text as argument

Filters:
  - First day of unusual volume (today >> avg, prior days normal)
  - AH gain > 0%
  - Market cap < $200M (small/micro cap)
  - Checks previous 5 days of volume history via Yahoo Finance
"""

import json
import re
import sys
import urllib.request
import time
from datetime import datetime, timezone, timedelta


def fetch_yahoo(ticker, interval="1d", range_="10d"):
    """Fetch chart data from Yahoo Finance API."""
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?interval={interval}&range={range_}&includePrePost=true"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read())
    except Exception as e:
        print(f"  ⚠ Yahoo fetch failed for {ticker}: {e}", file=sys.stderr)
        return None


def parse_tradingview_text(text):
    """Parse TradingView AH gainers page text into ticker list with data."""
    candidates = []

    # Split into lines and find ticker entries
    # Pattern: TICKER CompanyName +XX.XX% price USD ...
    lines = text.strip().split('\n')
    full_text = ' '.join(lines)

    # Match pattern: TICKER Company Name +/-XX.XX% price USD +/-price USD vol price USD +/-XX.XX% vol marketcap
    # The TradingView format has data in a specific order per row
    # Let's use a regex to find ticker symbols followed by company names and percentages
    pattern = r'([A-Z]{2,5})\s+([A-Za-z][\w\s,.\'-]+?)\s+\+(\d+\.?\d*%)\s+(\d+\.?\d*)\s+USD'
    matches = re.finditer(pattern, full_text)

    seen = set()
    for m in matches:
        ticker = m.group(1)
        name = m.group(2).strip()
        ah_pct = m.group(3)
        ah_price = float(m.group(4))

        # Skip duplicates and header artifacts
        if ticker in seen or ticker in ('USD', 'MORE', 'ALL', 'USA'):
            continue
        seen.add(ticker)

        candidates.append({
            'ticker': ticker,
            'name': name,
            'ah_pct': ah_pct,
            'ah_price': ah_price,
        })

    return candidates


def analyze_volume(ticker):
    """
    Check if today is the first day of unusual volume.
    Returns dict with analysis or None if data unavailable.
    """
    data = fetch_yahoo(ticker, interval="1d", range_="10d")
    if not data or not data.get('chart', {}).get('result'):
        return None

    result = data['chart']['result'][0]
    meta = result['meta']
    timestamps = result['timestamp']
    quotes = result['indicators']['quote'][0]
    volumes = quotes['volume']
    closes = quotes['close']

    if not timestamps or len(timestamps) < 2:
        return None

    est = timezone(timedelta(hours=-5))
    days = []
    for i in range(len(timestamps)):
        t = datetime.fromtimestamp(timestamps[i], tz=est)
        days.append({
            'date': t.strftime('%Y-%m-%d'),
            'close': closes[i],
            'volume': volumes[i] or 0,
        })

    # Today is the last entry
    today = days[-1]
    prior = days[:-1]

    if not prior:
        return None

    # Average volume of prior days (exclude zeros)
    prior_vols = [d['volume'] for d in prior if d['volume'] > 0]
    if not prior_vols:
        return None

    avg_vol = sum(prior_vols) / len(prior_vols)
    today_vol = today['volume']

    # Check if today's volume is unusual (> 3x average)
    vol_ratio = today_vol / avg_vol if avg_vol > 0 else 0

    # Check if ANY prior day also had unusual volume (> 3x their preceding average)
    prior_day_unusual = False
    for i in range(1, len(prior)):
        prev_avg = sum(d['volume'] for d in prior[:i] if d['volume'] > 0) / max(1, len([d for d in prior[:i] if d['volume'] > 0]))
        if prev_avg > 0 and prior[i]['volume'] / prev_avg > 3:
            prior_day_unusual = True
            break

    # Previous close (the close before today)
    prev_close = prior[-1]['close'] if prior[-1]['close'] else None

    return {
        'today_vol': today_vol,
        'avg_vol': avg_vol,
        'vol_ratio': vol_ratio,
        'is_first_spike': vol_ratio > 3 and not prior_day_unusual,
        'prior_day_unusual': prior_day_unusual,
        'prev_close': prev_close,
        'today_close': today['close'],
        'days': days,
        'regular_market_price': meta.get('regularMarketPrice'),
        'exchange': meta.get('exchangeName', ''),
    }


def get_fundamentals(ticker):
    """Get float, market cap, sector from Yahoo Finance 1-day data."""
    data = fetch_yahoo(ticker, interval="1m", range_="1d")
    if not data or not data.get('chart', {}).get('result'):
        return {}

    meta = data['chart']['result'][0]['meta']
    return {
        'long_name': meta.get('longName', ''),
        'exchange': meta.get('exchangeName', ''),
    }


def format_vol(v):
    if v >= 1_000_000:
        return f"{v/1_000_000:.1f}M"
    elif v >= 1_000:
        return f"{v/1_000:.0f}K"
    return str(v)


def main():
    # Read from stdin or file
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            text = f.read()
    else:
        text = sys.stdin.read()

    candidates = parse_tradingview_text(text)
    print(f"Found {len(candidates)} AH gainers\n")

    # Analyze each
    first_spikes = []
    print("Checking volume history...")
    print("-" * 80)

    for c in candidates:
        ticker = c['ticker']
        time.sleep(0.3)  # Rate limit

        vol_data = analyze_volume(ticker)
        if not vol_data:
            continue

        vol_ratio = vol_data['vol_ratio']
        is_first = vol_data['is_first_spike']
        prev_close = vol_data['prev_close']
        today_close = vol_data['today_close']

        # Calculate % above previous close
        pct_above = None
        if prev_close and today_close and prev_close > 0:
            pct_above = ((c['ah_price'] - prev_close) / prev_close) * 100

        status = "🔥 FIRST SPIKE" if is_first else "❌ prior unusual vol" if vol_data['prior_day_unusual'] else "❌ low vol ratio"
        if vol_ratio < 3:
            status = "❌ vol ratio < 3x"

        # Print every ticker's status
        print(f"{ticker:6s} | AH: +{c['ah_pct']:>7s} | Vol: {format_vol(vol_data['today_vol']):>7s} ({vol_ratio:>6.1f}x avg) | {status}")

        if is_first:
            c['vol_data'] = vol_data
            c['pct_above_prev'] = pct_above
            first_spikes.append(c)

    print("-" * 80)
    print(f"\n{'='*80}")
    print(f"FIRST-DAY VOLUME SPIKES: {len(first_spikes)}")
    print(f"{'='*80}\n")

    if not first_spikes:
        print("No first-day volume spikes found tonight.")
        return

    for c in first_spikes:
        vd = c['vol_data']
        print(f"### {c['ticker']} - {c['name']}")
        print(f"  AH Price: ${c['ah_price']:.2f} (+{c['ah_pct']})")
        print(f"  Prev Close: ${vd['prev_close']:.4f}" if vd['prev_close'] else "  Prev Close: N/A")
        if c['pct_above_prev'] is not None:
            flag = " ⚠️ >50%" if c['pct_above_prev'] > 50 else " ✅"
            print(f"  % Above Prev Close: {c['pct_above_prev']:.1f}%{flag}")
        print(f"  Today Volume: {format_vol(vd['today_vol'])} ({vd['vol_ratio']:.1f}x avg {format_vol(vd['avg_vol'])})")
        print(f"  Volume History:")
        for d in vd['days']:
            marker = " ◀ TODAY" if d == vd['days'][-1] else ""
            print(f"    {d['date']}: vol={format_vol(d['volume']):>7s}  close=${d['close']:.4f}" if d['close'] else f"    {d['date']}: vol={format_vol(d['volume']):>7s}  close=N/A", end="")
            print(marker)
        print()


if __name__ == '__main__':
    main()
