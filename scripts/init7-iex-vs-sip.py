#!/usr/bin/env python3
"""Compare archived pre-decision IEX books (Oct 7-8) with the SIP NBBO at their receipt times. Run from the repo root."""
import sys, json, glob, statistics, datetime as dt
sys.path.insert(0, 'scripts')
import importlib.util
spec = importlib.util.spec_from_file_location('c', 'scripts/init7-data-census.py'); c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
def bps(b, a): return (a - b) / ((a + b) / 2) * 1e4 if b > 0 and a >= b else None
rows = []
for path in sorted(glob.glob('log/2026-10-0[78]/init7-observe/*/market.json')):
    m = json.load(open(path)); q = m['iex_quotes']; at = q['received_utc']
    end = dt.datetime.fromisoformat(at)
    for sym, iq in q['payload']['quotes'].items():
        r = c.request('https://data.alpaca.markets', f'/v2/stocks/{sym}/quotes',
                      {'feed': 'sip', 'start': (end - dt.timedelta(seconds=60)).isoformat(), 'end': end.isoformat(), 'limit': 1, 'sort': 'desc'})
        sq = (r['payload'].get('quotes') or [None])[0]
        rows.append({'book': path.split('/')[1] + '/' + path.split('/')[3], 'symbol': sym, 'iex_received_utc': at,
                     'iex_bid': iq['bp'], 'iex_ask': iq['ap'], 'iex_bps': bps(iq['bp'], iq['ap']),
                     'sip_t': sq and sq['t'], 'sip_bid': sq and sq['bp'], 'sip_ask': sq and sq['ap'],
                     'sip_bps': sq and bps(sq['bp'], sq['ap']), 'sip_received_utc': r['received_utc']})
summary = {}
for sym in sorted({r['symbol'] for r in rows}):
    rs = [r for r in rows if r['symbol'] == sym and r['sip_bps'] is not None and r['iex_bps'] is not None]
    summary[sym] = {'n': len(rs), 'iex_median_bps': round(statistics.median(r['iex_bps'] for r in rs), 2),
                    'sip_median_bps': round(statistics.median(r['sip_bps'] for r in rs), 2),
                    'iex_ask_over_sip_ask_median_bps': round(statistics.median((r['iex_ask'] / r['sip_ask'] - 1) * 1e4 for r in rs), 2),
                    'sip_bid_over_iex_bid_median_bps': round(statistics.median((r['sip_bid'] / r['iex_bid'] - 1) * 1e4 for r in rs), 2)}
ok = [r for r in rows if r['sip_bps'] is not None]
out = {'script': 'scripts/init7-iex-vs-sip.py', 'books': len(rows), 'with_sip': len(ok),
       'iex_median_bps': round(statistics.median(r['iex_bps'] for r in ok), 2),
       'sip_median_bps': round(statistics.median(r['sip_bps'] for r in ok), 2),
       'iex_mean_bps': round(statistics.mean(r['iex_bps'] for r in ok), 2),
       'sip_mean_bps': round(statistics.mean(r['sip_bps'] for r in ok), 2), 'by_symbol': summary, 'rows': rows}
json.dump(out, open('log/2026-10-08/init7-execute/iex-vs-sip-spreads.json', 'w'), indent=2)
print(json.dumps({k: v for k, v in out.items() if k != 'rows'}, indent=1))
