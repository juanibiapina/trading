#!/usr/bin/env python3
"""Initiative 7: short-fade test of micro-cap AH ignitions, per docs/investigations/init7-microcap-short-fade-freeze.json.

Short the union of the 17:00 and late-entry census events at the scan bid, cover at the 04:30 ET ask or the open.
Event selection reuses scripts/init7-microcap-census.py and scripts/init7-microcap-late-census.py unchanged.

  init7-microcap-short-fade.py --out DIR                  # prior-year fetch (resumable; caches in DIR) and evaluate
  init7-microcap-short-fade.py --out DIR --replay         # evaluate cached inputs only
  init7-microcap-short-fade.py --out DIR --last D         # smaller event window (verification)
  init7-microcap-short-fade.py --out DIR --in-sample      # rescore the October 15 caches (code check; not evidence)
Run from the repo root with ALPACA_API_KEY / ALPACA_SECRET_KEY set.
"""
import argparse
import datetime as dt
import gzip
import importlib.util
import json
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


mc = module('mc', 'scripts/init7-microcap-census.py')
lm = module('lm', 'scripts/init7-microcap-late-census.py')
lm.mc = mc
lc = mc.lc

FREEZE = ROOT / 'docs/investigations/init7-microcap-short-fade-freeze.json'
FIRST, LAST = '2024-10-01', '2025-09-30'
HISTORY_START, DAILY_END = '2024-08-26', '2025-11-14'
MONTHLY = ROOT / 'log/2026-10-14/init7-liquid-fade-oos/census/monthly.json.gz'
IS_EARLY = ROOT / 'log/2026-10-15/init7-microcap-census'
IS_LATE = ROOT / 'log/2026-10-15/init7-microcap-late'
AUCTION_BPS, FEE_BPS = 50, 25
STRESS_BPS, STRESS_FEE_BPS = 100, 100
EXITS = ('exit_0430', 'exit_open')
SUBSETS = ('all', 'etb')
TAIL = 0.025 / 4
ENTRY_FROM = {1700: 1645, **lm.QUOTE_FROM}


def assets(path):
    if not path.exists():
        rows = lc.get_json('https://paper-api.alpaca.markets/v2/assets?asset_class=us_equity')
        lc.save(path, {'fetched_utc': dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds'),
                       'flags': {a['symbol']: [bool(a.get('shortable')), bool(a.get('easy_to_borrow'))] for a in rows}})
    flags = lc.load(path)['flags']
    return {s for s, (shortable, etb) in flags.items() if shortable and etb}


def union(early, late):
    for e in early:
        e['scan'] = 1700
    return early + late


def fetch_quotes(path, events):
    quotes = lc.load(path) if path.exists() else {}
    pending = [e for e in events if e['key'] not in quotes]
    print(f'{len(events)} events, {len(pending)} need quotes', flush=True)
    for n, e in enumerate(pending, 1):
        quotes[e['key']] = {
            'entry': lc.last_quote(e['symbol'], lc.et(e['date'], ENTRY_FROM[e['scan']]), lc.et(e['date'], e['scan'])),
            'exit_0430': lc.last_quote(e['symbol'], lc.et(e['next'], 400), lc.et(e['next'], 430)),
        }
        if n % 100 == 0:
            lc.save(path, quotes)
            print(f'quotes {n}/{len(pending)}', flush=True)
    lc.save(path, quotes)
    return quotes


def score(events, quotes, etb):
    rows, counts = [], {'no_entry_quote': 0, 'no_next_open': 0, 'split': 0, 'exit_0430_fallback': 0}
    slip = 1 + AUCTION_BPS / 1e4
    for e in events:
        q = quotes.get(e['key'], {})
        if e['split']:
            counts['split'] += 1
            continue
        if not e['open1']:
            counts['no_next_open'] += 1
            continue
        if not lc.valid(q.get('entry')):
            counts['no_entry_quote'] += 1
            continue
        entry, mid = q['entry']['bp'], (q['entry']['ap'] + q['entry']['bp']) / 2
        x = q.get('exit_0430')
        if lc.valid(x):
            c0430, m0430 = x['ap'], (x['ap'] + x['bp']) / 2
        else:
            c0430, m0430 = e['open1'] * slip, e['open1']
            counts['exit_0430_fallback'] += 1
        nights = (dt.date.fromisoformat(e['next']) - dt.date.fromisoformat(e['date'])).days
        fee = nights * FEE_BPS / 1e4
        rows.append({**e, 'entry': entry, 'nights': nights, 'spread_bps': (q['entry']['ap'] - entry) / mid * 1e4,
                     'exit_0430': 1 - c0430 / entry - fee, 'exit_open': 1 - e['open1'] * slip / entry - fee,
                     'gross_exit_0430': 1 - m0430 / mid, 'gross_exit_open': 1 - e['open1'] / mid,
                     'origin': '1700' if e['scan'] == 1700 else 'late', 'all': True, 'etb': e['symbol'] in etb})
    return rows, counts


def stressed(rows, key):
    extra = lambda r: STRESS_BPS / 1e4 + r['nights'] * (STRESS_FEE_BPS - FEE_BPS) / 1e4
    return [dict(r, **{key: r[key] - extra(r)}) for r in rows]


def evaluate(out, events, quotes, etb, window, label):
    rows, counts = score(events, quotes, etb)
    summary = lambda sub, key: lc.summary(sub, key, 0.0, tail=TAIL)
    result = {'freeze': str(FREEZE.relative_to(ROOT)), 'mode': label, 'window': window, 'events': len(events),
              'scored': len(rows), 'excluded': counts, 'cells': {}, 'gross_mid': {}, 'descriptive': {}}
    for name in SUBSETS:
        sub = [r for r in rows if r[name]]
        result['cells'][name] = {}
        for k in EXITS:
            base = summary(sub, k)
            if len(sub) >= 100:
                base['worst_1pct_pct'] = round(statistics.quantiles([r[k] for r in sub], n=100)[0] * 100, 2)
            result['cells'][name][k] = {'base': base, 'stress': summary(stressed(sub, k), k)}
        result['gross_mid'][name] = {k: summary(sub, 'gross_' + k) for k in EXITS}
    result['passed_cells'] = [f'{n}/{k}' for n in SUBSETS for k in EXITS if result['cells'][n][k]['base'].get('passed')]
    result['passed'] = bool(result['passed_cells'])
    d = result['descriptive']
    d['origin'] = {o: {k: summary([r for r in rows if r['origin'] == o], k) for k in EXITS} for o in ('1700', 'late')}
    d['scan'] = {str(t): {k: summary([r for r in rows if r['scan'] == t], k) for k in EXITS}
                 for t in (1700, 1730, 1800, 1830)}
    buckets = {'move': (('10-25%', .10, .25), ('25-50%', .25, .50), ('50-150%', .50, 9)),
               'close': (('$0.50-1', 0, 1), ('$1-3', 1, 3), ('$3-10', 3, 99)),
               'ah_dollars': (('<$300k', 0, 3e5), ('$300k-1M', 3e5, 1e6), ('>$1M', 1e6, 1e12))}
    for field, spec_ in buckets.items():
        d[field] = {lab: {k: summary([r for r in rows if lo <= r[field] < hi], k) for k in EXITS}
                    for lab, lo, hi in spec_}
    if len(rows) > 3:
        d['entry_spread_bps'] = dict(zip(('p25', 'p50', 'p75'), (
            round(v, 1) for v in statistics.quantiles([r['spread_bps'] for r in rows], n=4))))
    by_month = {}
    for r in rows:
        by_month[r['date'][:7]] = by_month.get(r['date'][:7], 0) + 1
    d['scored_by_month'] = by_month
    pick = lambda r: {k: (round(r[k], 4) if isinstance(r[k], float) else r[k])
                      for k in ('symbol', 'date', 'scan', 'move', 'entry', 'spread_bps', 'etb', *EXITS)}
    best = sorted(rows, key=lambda r: -r['exit_0430'])
    result['top5_exit_0430'] = [pick(r) for r in best[:5]]
    result['bottom5_exit_0430'] = [pick(r) for r in best[-5:]]
    (out / 'result.json').write_text(json.dumps(result, indent=1))
    with gzip.open(out / 'events.json.gz', 'wt') as handle:
        json.dump(rows, handle)
    print(json.dumps({k: result[k] for k in ('mode', 'events', 'scored', 'excluded', 'passed_cells')}, indent=1))
    for n in SUBSETS:
        for k in EXITS:
            b, s = result['cells'][n][k]['base'], result['cells'][n][k]['stress']
            g = result['gross_mid'][n][k]
            print(n, k, b.get('n'), b.get('mean_pct'), b.get('interval_pct'), b.get('halves_pct'),
                  'stress', s.get('mean_pct'), 'mid', g.get('mean_pct'))


def in_sample(out):
    cal = json.loads((IS_EARLY / 'calendar.json').read_text())
    early = mc.candidates(IS_EARLY, cal)
    late = lm.candidates(IS_LATE, cal)
    quotes = {**lc.load(IS_EARLY / 'quotes.json.gz'), **lc.load(IS_LATE / 'quotes.json.gz')}
    evaluate(out, union(early, late), quotes, assets(out / 'assets.json.gz'), [mc.FIRST, mc.LAST], 'in-sample')


def prior_year(out, first, last, replay):
    mc.FIRST, mc.LAST = first, last
    mc.HISTORY_START, mc.DAILY_END, mc.MONTHLY = HISTORY_START, DAILY_END, MONTHLY
    lm.EARLY = out
    if not replay:
        mc.fetch(out, quotes_too=False)
    cal = json.loads((out / 'calendar.json').read_text())
    if not replay:
        lm.fetch_bars(out, cal, mc.full_days(cal, HISTORY_START, last))
    events = union(mc.candidates(out, cal), lm.candidates(out, cal))
    qpath = out / 'quotes.json.gz'
    quotes = lc.load(qpath) if replay else fetch_quotes(qpath, events)
    evaluate(out, events, quotes, assets(out / 'assets.json.gz'), [first, last], 'prior-year')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--replay', action='store_true')
    parser.add_argument('--in-sample', action='store_true')
    parser.add_argument('--first', default=FIRST)
    parser.add_argument('--last', default=LAST)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    if args.in_sample:
        in_sample(args.out)
    else:
        prior_year(args.out, args.first, args.last, args.replay)


if __name__ == '__main__':
    main()
