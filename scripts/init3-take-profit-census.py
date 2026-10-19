#!/usr/bin/env python3
"""Initiative 3: resting take-profit on the prior-year micro-cap census events, per
docs/investigations/init3-take-profit-census-freeze.json.

  init3-take-profit-census.py --out DIR     # fetch 1-minute highs (cached in DIR/highs.json.gz) and evaluate
Run from the repo root with ALPACA_API_KEY / ALPACA_SECRET_KEY set.
"""
import argparse
import importlib.util
import json
import statistics
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location('lc', ROOT / 'scripts/init7-liquid-ah-census.py')
lc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lc)

FREEZE = ROOT / 'docs/investigations/init3-take-profit-census-freeze.json'
SRC = ROOT / 'log/2026-10-16/init7-short-fade'
VARIANTS = {'tp10': 0.10, 'tp15': 0.15, 'tp20': 0.20}
TAIL = 0.025 / 3
SLIP = 1 - 50 / 1e4


def highs(symbols, start, end):
    out, token = {}, None
    while True:
        query = {'symbols': ','.join(symbols), 'timeframe': '1Min', 'feed': 'sip', 'adjustment': 'raw',
                 'start': lc.iso(start), 'end': lc.iso(end), 'limit': 10000, 'sort': 'asc'}
        if token:
            query['page_token'] = token
        payload = lc.get_json(lc.DATA + '/v2/stocks/bars?' + urllib.parse.urlencode(query))
        for s, rows in (payload.get('bars') or {}).items():
            out.setdefault(s, []).extend([r['t'], r['h']] for r in rows)
        token = payload.get('next_page_token')
        if not token:
            return out


def fetch(path, events):
    cache = lc.load(path) if path.exists() else {}
    by_date = {}
    for e in events:
        by_date.setdefault((e['date'], e['next']), set()).add(e['symbol'])
    for n, ((day, nxt), names) in enumerate(sorted(by_date.items()), 1):
        if day in cache:
            continue
        names = sorted(names)
        cache[day] = {'ah': highs(names, lc.et(day, 1700), lc.et(day, 1959)),
                      'pm': highs(names, lc.et(nxt, 400), lc.et(nxt, 429))}
        if n % 25 == 0:
            lc.save(path, cache)
            print(f'highs {n}/{len(by_date)}', flush=True)
    lc.save(path, cache)
    return cache


def evaluate(out, events, quotes, cache):
    rows, fallback = [], 0
    for e in events:
        q = quotes[e['key']]
        entry = q['entry']['ap']
        x = q.get('exit_0430')
        if lc.valid(x):
            base = x['bp']
        else:
            base, fallback = e['open1'] * SLIP, fallback + 1
        t0 = lc.iso(lc.et(e['date'], e['scan']))
        hs = [h for t, h in cache[e['date']]['ah'].get(e['symbol'], []) if t >= t0]
        hs += [h for _, h in cache[e['date']]['pm'].get(e['symbol'], [])]
        row = {'symbol': e['symbol'], 'date': e['date'], 'scan': e['scan'], 'etb': e['etb'], 'entry': entry,
               'base': base / entry - 1, 'max_up': max(hs) / entry - 1 if hs else None, 'bars': len(hs)}
        for name, lim in VARIANTS.items():
            hit = any(h > entry * (1 + lim) for h in hs)
            row[name + '_hit'] = hit
            row[name] = lim if hit else row['base']
            row[name + '_diff'] = row[name] - row['base']
        rows.append(row)
    result = {'freeze': str(FREEZE.relative_to(ROOT)), 'events': len(events), 'scored': len(rows),
              'baseline_fallback': fallback, 'no_bars_after_entry': sum(r['bars'] == 0 for r in rows),
              'baseline': lc.summary(rows, 'base', tail=TAIL), 'variants': {}}
    for name in VARIANTS:
        result['variants'][name] = {'fill_rate': round(sum(r[name + '_hit'] for r in rows) / len(rows), 3),
                                    'return': lc.summary(rows, name, tail=TAIL),
                                    'paired_diff': lc.summary(rows, name + '_diff', tail=TAIL)}
    v = result['variants']
    result['beats_exit'] = [n for n in VARIANTS if v[n]['paired_diff']['passed']]
    result['rescues'] = [n for n in result['beats_exit'] if v[n]['return']['passed']]
    ups = [r['max_up'] for r in rows if r['max_up'] is not None]
    result['max_up_quantiles_pct'] = [round(u * 100, 1) for u in statistics.quantiles(ups, n=10)]
    (out / 'result.json').write_text(json.dumps(result, indent=1))
    lc.save(out / 'rows.json.gz', rows)
    print(json.dumps(result, indent=1))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    events = lc.load(SRC / 'events.json.gz')
    quotes = lc.load(SRC / 'quotes.json.gz')
    evaluate(args.out, events, quotes, fetch(args.out / 'highs.json.gz', events))


if __name__ == '__main__':
    main()
