#!/usr/bin/env python3
"""Initiative 3: replay a resting take-profit limit on real paper fills, per docs/investigations/init3-take-profit-freeze.json.

  init3-take-profit-replay.py --out DIR            # fetch (cached in DIR) and evaluate
Run from the repo root with ALPACA_API_KEY / ALPACA_SECRET_KEY set.
"""
import argparse
import datetime as dt
import importlib.util
import json
import statistics
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location('lc', ROOT / 'scripts/init7-liquid-ah-census.py')
lc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lc)

FREEZE = ROOT / 'docs/investigations/init3-take-profit-freeze.json'
FIRST, LAST = '2026-06-25', '2026-10-15'
VARIANTS = {'tp10': 0.10, 'tp15': 0.15, 'tp20': 0.20}
TAIL = 0.025 / 3
PAPER = 'https://paper-api.alpaca.markets'


def buy_fills():
    orders, after = [], f'{FIRST}T00:00:00Z'
    while True:
        query = {'status': 'closed', 'limit': 500, 'direction': 'asc', 'after': after, 'until': f'{LAST}T23:59:59Z'}
        page = lc.get_json(f'{PAPER}/v2/orders?' + urllib.parse.urlencode(query))
        orders += page
        if len(page) < 500:
            break
        after = page[-1]['submitted_at']
    fills = []
    for o in orders:
        if o['side'] != 'buy' or not o.get('filled_at') or not float(o.get('filled_qty') or 0):
            continue
        at = dt.datetime.fromisoformat(o['filled_at'].replace('Z', '+00:00')).astimezone(lc.ET)
        if not (16 <= at.hour < 20) or not (FIRST <= at.date().isoformat() <= LAST):
            continue
        fills.append({'id': o['id'], 'symbol': o['symbol'], 'date': at.date().isoformat(),
                      'filled_at': lc.iso(at), 'fill': float(o['filled_avg_price'])})
    return fills


def minute_bars(symbol, start, end):
    out, token = [], None
    while True:
        query = {'symbols': symbol, 'timeframe': '1Min', 'feed': 'sip', 'adjustment': 'raw',
                 'start': lc.iso(start), 'end': lc.iso(end), 'limit': 10000, 'sort': 'asc'}
        if token:
            query['page_token'] = token
        payload = lc.get_json(lc.DATA + '/v2/stocks/bars?' + urllib.parse.urlencode(query))
        out += [{k: r[k] for k in ('t', 'o', 'h')} for r in (payload.get('bars') or {}).get(symbol, [])]
        token = payload.get('next_page_token')
        if not token:
            return out


def fetch(out):
    path = out / 'inputs.json'
    if path.exists():
        return json.loads(path.read_text())
    cal = lc.get_json(f'{PAPER}/v2/calendar?' + urllib.parse.urlencode({'start': FIRST, 'end': '2026-10-31'}))
    dates = [d['date'] for d in cal]
    rows = []
    for f in buy_fills():
        nxt = dates[dates.index(f['date']) + 1]
        fill_minute = dt.datetime.fromisoformat(f['filled_at'].replace('Z', '+00:00')).replace(second=0, microsecond=0)
        ah = [b for b in minute_bars(f['symbol'], fill_minute, lc.et(f['date'], 1959))
              if b['t'] > lc.iso(fill_minute)]
        pm = minute_bars(f['symbol'], lc.et(nxt, 400), lc.et(nxt, 429))
        rows.append({**f, 'next': nxt, 'ah': ah, 'pm': pm,
                     'quote_0430': lc.last_quote(f['symbol'], lc.et(nxt, 400), lc.et(nxt, 430))})
        print(f"{f['symbol']} {f['date']} {len(ah)} AH / {len(pm)} PM bars", flush=True)
    path.write_text(json.dumps(rows))
    return rows


def paired(rows, key):
    if len(rows) < 2:
        return {'n': len(rows)}
    ordered = sorted(rows, key=lambda r: r['date'])
    half = ordered[len(ordered) // 2]['date']
    first = [r[key] for r in ordered if r['date'] < half]
    second = [r[key] for r in ordered if r['date'] >= half]
    lo, hi = lc.by_date_interval(rows, key, TAIL)
    mean = statistics.mean(r[key] for r in rows)
    return {'n': len(rows), 'mean_diff_pct': round(mean * 100, 3), 'interval_pct': [round(lo * 100, 3), round(hi * 100, 3)],
            'halves_pct': [round(statistics.mean(first) * 100, 3) if first else None,
                           round(statistics.mean(second) * 100, 3) if second else None],
            'passed': mean > 0 and lo > 0 and bool(first) and bool(second)
            and statistics.mean(first) > 0 and statistics.mean(second) > 0}


def evaluate(out, inputs):
    rows, fallback, skipped = [], 0, 0
    for r in inputs:
        q = r['quote_0430']
        if lc.valid(q):
            base = q['bp']
        elif r['pm']:
            base, fallback = r['pm'][0]['o'], fallback + 1
        else:
            skipped += 1
            continue
        row = {'symbol': r['symbol'], 'date': r['date'], 'fill': r['fill'], 'base': base / r['fill'] - 1}
        highs = [b['h'] for b in r['ah'] + r['pm']]
        for name, x in VARIANTS.items():
            hit = any(h > r['fill'] * (1 + x) for h in highs)
            row[name + '_hit'] = hit
            row[name] = x if hit else row['base']
            row[name + '_diff'] = row[name] - row['base']
        row['max_up'] = max(highs) / r['fill'] - 1 if highs else None
        rows.append(row)
    result = {'freeze': str(FREEZE.relative_to(ROOT)), 'fills': len(inputs), 'scored': len(rows),
              'baseline_fallback': fallback, 'skipped_no_exit': skipped,
              'baseline_mean_pct': round(statistics.mean(r['base'] for r in rows) * 100, 3), 'variants': {}}
    for name in VARIANTS:
        result['variants'][name] = {'fill_rate': round(sum(r[name + '_hit'] for r in rows) / len(rows), 3),
                                    'mean_pct': round(statistics.mean(r[name] for r in rows) * 100, 3),
                                    **paired(rows, name + '_diff')}
    result['passed'] = [n for n in VARIANTS if result['variants'][n].get('passed')]
    result['since_oct12'] = [{k: (round(v, 4) if isinstance(v, float) else v) for k, v in r.items()
                              if k in ('symbol', 'date', 'fill', 'base', 'max_up', 'tp10', 'tp15', 'tp20')}
                             for r in rows if r['date'] >= '2026-10-12']
    (out / 'result.json').write_text(json.dumps(result, indent=1))
    print(json.dumps(result, indent=1))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    evaluate(args.out, fetch(args.out))


if __name__ == '__main__':
    main()
