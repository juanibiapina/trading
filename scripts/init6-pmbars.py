#!/usr/bin/env python3
"""Init 6: dump premarket+early-regular bars for a ticker on a given date, to
classify a PM-only gapper as holdable (sustained elevated window) vs
uninvestable (instant spike/decay).

Usage: init6-pmbars.py TICKER YYYY-MM-DD [interval]
  interval default 15m. range=1mo reaches ~1 month back. A browser User-Agent
  and the query2 host are both required for historical intraday bars.
"""
import sys, json, urllib.request, datetime

def get(t, interval):
    u = (f"https://query2.finance.yahoo.com/v8/finance/chart/{t}"
         f"?interval={interval}&range=1mo&includePrePost=true")
    req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
    return json.load(urllib.request.urlopen(req))

def main():
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(1)
    t, day = sys.argv[1].upper(), sys.argv[2]
    interval = sys.argv[3] if len(sys.argv) > 3 else '15m'
    r = get(t, interval)['chart']['result'][0]
    ts = r['timestamp']; q = r['indicators']['quote'][0]
    close, vol, high = q['close'], q['volume'], q['high']
    pc = r['meta'].get('chartPreviousClose') or r['meta'].get('previousClose')
    print(f"=== {t} {day}  prevClose~{pc} ({interval}) ===")
    for i, t0 in enumerate(ts):
        # ET = UTC-4 (EDT). Good enough for session bucketing.
        dt = datetime.datetime.fromtimestamp(t0, datetime.UTC) - datetime.timedelta(hours=4)
        if dt.strftime('%Y-%m-%d') != day:
            continue
        et = dt.strftime('%H:%M')
        if not ('04:00' <= et <= '10:30'):
            continue
        c = close[i]
        if c is None:
            continue
        h = high[i]; v = vol[i] or 0
        pct = (c/pc - 1)*100 if pc else 0
        print(f"  {et} ET  close={c:.3f} high={h:.3f} vol={v:>10}  {pct:+.0f}%")

if __name__ == '__main__':
    main()
