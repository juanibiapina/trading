#!/usr/bin/env python3
"""
Generate ASCII price timelines for trading analysis.
Uses yahoo-fetch.py data to show AH and PM price action.

Usage:
    python3 scripts/price-timeline.py TICKER [TICKER2 ...]
"""

import sys
import json
import subprocess
from datetime import datetime, timezone

def fetch_data(ticker, interval="5m", range_="2d"):
    """Fetch price data using yahoo-fetch.py"""
    cmd = ["python3", "scripts/yahoo-fetch.py", ticker, 
           "--interval", interval, "--range", range_, "--prepost"]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            return json.loads(result.stdout)
    except Exception as e:
        print(f"Error fetching {ticker}: {e}", file=sys.stderr)
    return None

def parse_yahoo_data(data):
    """Parse Yahoo chart format to list of (timestamp, open, high, low, close, volume)"""
    try:
        result = data.get('chart', {}).get('result', [{}])[0]
        timestamps = result.get('timestamp', [])
        quotes = result.get('indicators', {}).get('quote', [{}])[0]
        
        opens = quotes.get('open', [])
        highs = quotes.get('high', [])
        lows = quotes.get('low', [])
        closes = quotes.get('close', [])
        volumes = quotes.get('volume', [])
        
        parsed = []
        for i, ts in enumerate(timestamps):
            if i < len(closes) and closes[i]:
                dt = datetime.fromtimestamp(ts, tz=timezone.utc)
                parsed.append({
                    'dt': dt,
                    'open': opens[i] if i < len(opens) else None,
                    'high': highs[i] if i < len(highs) else None,
                    'low': lows[i] if i < len(lows) else None,
                    'close': closes[i],
                    'volume': volumes[i] if i < len(volumes) else 0
                })
        return parsed
    except Exception as e:
        print(f"Parse error: {e}", file=sys.stderr)
        return []

def ascii_chart(prices, width=60, height=12):
    """Generate ASCII chart from price list"""
    if not prices or len(prices) < 2:
        return "Insufficient data"
    
    closes = [p['close'] for p in prices if p['close']]
    if not closes:
        return "No price data"
    
    min_p = min(closes)
    max_p = max(closes)
    range_p = max_p - min_p or 0.01
    
    # Sample prices to fit width
    step = max(1, len(closes) // width)
    sampled = closes[::step][:width]
    
    # Scale prices to chart height
    scaled = [int((p - min_p) / range_p * (height - 1)) for p in sampled]
    
    # Build chart
    chart = [[' ' for _ in range(len(sampled))] for _ in range(height)]
    
    for col, row in enumerate(scaled):
        if row is not None and col < len(sampled):
            chart[height - 1 - row][col] = '█'
    
    # Add axis labels
    lines = []
    for i, row in enumerate(chart):
        price = max_p - (i / (height - 1)) * range_p
        if i == 0:
            lines.append(f"${price:7.2f} │{''.join(row)}")
        elif i == height - 1:
            lines.append(f"${price:7.2f} │{''.join(row)}")
        else:
            lines.append(f"         │{''.join(row)}")
    
    lines.append("         └" + "─" * len(sampled))
    
    return '\n'.join(lines)

def find_peak(prices):
    """Find the highest price point"""
    if not prices:
        return None
    max_price = 0
    peak = None
    for p in prices:
        if p['high'] and p['high'] > max_price:
            max_price = p['high']
            peak = p
    return peak

def print_timeline(ticker):
    """Print price timeline for ticker"""
    data = fetch_data(ticker)
    if not data:
        print(f"No data for {ticker}")
        return
    
    prices = parse_yahoo_data(data)
    if not prices:
        print(f"No price data for {ticker}")
        return
    
    # Get metadata
    meta = data.get('chart', {}).get('result', [{}])[0].get('meta', {})
    prev_close = meta.get('previousClose', meta.get('chartPreviousClose'))
    current = prices[-1]['close'] if prices else None
    
    print(f"\n{'='*72}")
    print(f" {ticker} - 2-Day Price Timeline (5-min intervals)")
    print(f"{'='*72}")
    
    closes = [p['close'] for p in prices if p['close']]
    highs = [p['high'] for p in prices if p['high']]
    
    if prev_close:
        print(f"\nPrevious Close: ${prev_close:.2f}")
    
    if closes:
        min_p = min(closes)
        max_p = max(highs) if highs else max(closes)
        print(f"2-Day Range: ${min_p:.2f} - ${max_p:.2f}")
        if current and prev_close:
            pct = ((current - prev_close) / prev_close) * 100
            print(f"Current: ${current:.2f} ({pct:+.1f}% from prev close)")
    
    # Find peak
    peak = find_peak(prices)
    if peak:
        peak_time = peak['dt'].strftime('%m-%d %H:%M') + " ET"
        if prev_close:
            peak_pct = ((peak['high'] - prev_close) / prev_close) * 100
            print(f"Peak: ${peak['high']:.2f} ({peak_pct:+.1f}%) at {peak_time}")
        else:
            print(f"Peak: ${peak['high']:.2f} at {peak_time}")
    
    print(f"\nChart (oldest → newest):")
    print(ascii_chart(prices))
    
    # Session breakdown
    print(f"\nSession Timeline (last 24h):")
    print("-" * 60)
    
    # Group by session
    for p in prices[-48:]:  # Last ~4 hours at 5-min intervals
        hour = p['dt'].hour
        if hour >= 16 and hour < 20:
            session = "AH"
        elif hour >= 4 and hour < 9:
            session = "PM"
        elif hour >= 9 and hour < 16:
            session = "REG"
        else:
            session = "OVN"
        
        time_str = p['dt'].strftime('%m-%d %H:%M')
        vol_str = f"{p['volume']:>10,}" if p['volume'] else "          "
        pct = ""
        if prev_close and p['close']:
            pct = f" ({((p['close'] - prev_close) / prev_close) * 100:+6.1f}%)"
        print(f"  [{session}] {time_str} ET: ${p['close']:7.2f}{pct}  Vol: {vol_str}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/price-timeline.py TICKER [TICKER2 ...]")
        sys.exit(1)
    
    for ticker in sys.argv[1:]:
        if not ticker.startswith('-'):
            print_timeline(ticker.upper())

if __name__ == "__main__":
    main()
