#!/usr/bin/env python3
"""Check 10-day volume history for premarket gainers to find first-day unusual volume spikes."""

import json
import urllib.request
import sys
from datetime import datetime

# All premarket gainers from TradingView with PM change > 5% and market cap < $200M
# Format: (ticker, pm_change, pm_vol, market_cap_str, sector_note)
tickers = [
    ("BYAH", "+90.34%", "23.35M", "2.67M", "Biological Tech"),
    ("ELPW", "+51.09%", "2.78M", "8.65M", "Power/Holdings"),
    ("CIGL", "+34.07%", "359K", "72.86M", "International Group"),
    ("BOXL", "+29.46%", "3.27M", "1.23M", "Boxlight/Tech"),
    ("SUNE", "+28.93%", "500K", "2.67M", "Energy"),
    ("NDRA", "+15.22%", "2K", "4.29M", "Life Sciences"),
    ("LIMN", "+14.95%", "344K", "28.96M", "Pharma"),
    ("INHD", "+16.38%", "195K", "9.76M", "Holdings"),
    ("ONCY", "+11.37%", "7.7K", "94.46M", "Biotech"),
    ("SPRO", "+9.81%", "1.5K", "120.57M", "Therapeutics"),
    ("FEED", "+8.13%", "7.3K", "2.68M", "Medical"),
    ("ALUR", "+8.15%", "2.2K", "16.58M", "Med Tech"),
    ("SGMO", "+5.82%", "11.5K", "131.23M", "Therapeutics"),
    ("GTBP", "+6.23%", "1.2K", "5.55M", "Biopharma"),
    ("ARAI", "+8.28%", "9K", "57.82M", "AI"),
    ("AGRZ", "+6.93%", "5K", "10.04M", "Agriculture"),
]

def get_volume_history(ticker):
    """Get 10-day daily volume history from Yahoo Finance."""
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?interval=1d&range=15d"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        resp = urllib.request.urlopen(req, timeout=10)
        data = json.loads(resp.read())
        result = data["chart"]["result"][0]
        timestamps = result["timestamp"]
        volumes = result["indicators"]["quote"][0]["volume"]
        closes = result["indicators"]["quote"][0]["close"]
        
        days = []
        for i, ts in enumerate(timestamps):
            dt = datetime.utcfromtimestamp(ts)
            days.append({
                "date": dt.strftime("%Y-%m-%d"),
                "volume": volumes[i] if volumes[i] else 0,
                "close": closes[i] if closes[i] else 0,
            })
        return days
    except Exception as e:
        return None

print("=" * 100)
print(f"PREMARKET VOLUME SPIKE SCREENER - {datetime.now().strftime('%Y-%m-%d %H:%M')}")
print("Looking for first-day unusual volume (today or yesterday was the FIRST spike)")
print("=" * 100)

first_day_spikes = []
multi_day_momentum = []

for ticker, pm_chg, pm_vol, mcap, note in tickers:
    days = get_volume_history(ticker)
    if not days or len(days) < 3:
        print(f"\n{ticker}: Could not fetch data")
        continue
    
    # Calculate average volume excluding last 2 days
    hist_days = days[:-2] if len(days) > 4 else days[:2]
    avg_vol = sum(d["volume"] for d in hist_days) / len(hist_days) if hist_days else 0
    
    # Last 2 days
    recent = days[-2:]
    
    print(f"\n{'='*60}")
    print(f"{ticker} | PM: {pm_chg} | PM Vol: {pm_vol} | MCap: {mcap} | {note}")
    print(f"{'='*60}")
    print(f"  10-day avg volume (excl last 2): {avg_vol:,.0f}")
    
    for d in days:
        ratio = d["volume"] / avg_vol if avg_vol > 0 else 0
        marker = " <<<" if ratio > 3 else ""
        print(f"  {d['date']}: vol={d['volume']:>12,}  close=${d['close']:.2f}  ratio={ratio:.1f}x{marker}")
    
    # Check if last day or second-to-last was the FIRST unusual volume day
    if avg_vol > 0:
        last_ratio = days[-1]["volume"] / avg_vol
        prev_ratio = days[-2]["volume"] / avg_vol if len(days) > 1 else 0
        
        # Check if any day before the last 2 had unusual volume
        earlier_spike = any(d["volume"] / avg_vol > 3 for d in days[:-2]) if avg_vol > 0 else False
        
        if last_ratio > 3 and not earlier_spike:
            if prev_ratio <= 3:
                first_day_spikes.append((ticker, pm_chg, pm_vol, mcap, note, last_ratio, 1))
                print(f"  >>> FIRST DAY SPIKE: {last_ratio:.1f}x average <<<")
            else:
                first_day_spikes.append((ticker, pm_chg, pm_vol, mcap, note, last_ratio, 2))
                print(f"  >>> DAY 2 SPIKE (started yesterday): {last_ratio:.1f}x avg, prev {prev_ratio:.1f}x <<<")

print("\n")
print("=" * 100)
print("SUMMARY: First-Day Volume Spikes")
print("=" * 100)
if first_day_spikes:
    for t, chg, pvol, mc, note, ratio, day_num in first_day_spikes:
        print(f"  {t:6s} | PM {chg:>8s} | PM Vol: {pvol:>8s} | MCap: {mc:>8s} | {ratio:.1f}x avg | Day {day_num} | {note}")
else:
    print("  No first-day spikes found")
