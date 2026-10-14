#!/usr/bin/env python3
"""Initiative 7: multi-day drift after liquid after-hours ignitions, per docs/investigations/init7-liquid-drift-freeze.json.

Entered in the regular session (next open or next close) and held 5 or 20 sessions, do the October 13 census
ignitions beat the equal-weight point-in-time top 1000 after a 10 bps round trip?

  init7-liquid-drift.py [--census DIR] [--out DIR]
Offline: reads only the census cache. Run from the repo root.
"""
import argparse
import gzip
import importlib.util
import json
import random
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FREEZE = ROOT / 'docs/investigations/init7-liquid-drift-freeze.json'
spec = importlib.util.spec_from_file_location('census', ROOT / 'scripts/init7-liquid-ah-census.py')
census = importlib.util.module_from_spec(spec)
spec.loader.exec_module(census)

COST, STRESS = 10 / 1e4, 20 / 1e4
HOLDS, ENTRIES, SIDES = (5, 20), ('open', 'close'), ('long', 'short')
TAIL = 0.05 / 8 / 2                 # Bonferroni over 8 cells; --tail overrides (fade OOS freeze: 0.025)


def month_interval(values, draws=4000, seed=13):
    groups = {}
    for month, v in values:
        groups.setdefault(month, []).append(v)
    months = sorted(groups)
    rng, means = random.Random(seed), []
    for _ in range(draws):
        sample = [v for _ in months for v in groups[months[rng.randrange(len(months))]]]
        means.append(statistics.mean(sample))
    means.sort()
    return means[int(TAIL * draws)], means[int((1 - TAIL) * draws) - 1]


def summary(rows, key, shift=0.0):
    if len(rows) < 2:
        return {'n': len(rows)}
    ordered = sorted(rows, key=lambda r: r['date'])
    vals = [(r['date'][:7], r[key] - shift) for r in ordered]
    half = ordered[len(ordered) // 2]['date']
    first = [r[key] - shift for r in ordered if r['date'] < half]
    second = [r[key] - shift for r in ordered if r['date'] >= half]
    lo, hi = month_interval(vals)
    mean = statistics.mean(v for _, v in vals)
    pct = lambda x: round(x * 100, 3)
    return {'n': len(rows), 'mean_pct': pct(mean), 'median_pct': pct(statistics.median(v for _, v in vals)),
            'interval_pct': [pct(lo), pct(hi)], 'win_rate': round(sum(v > 0 for _, v in vals) / len(vals), 3),
            'halves_pct': [pct(statistics.mean(first)) if first else None,
                           pct(statistics.mean(second)) if second else None],
            'passed': mean > 0 and lo > 0 and bool(first) and bool(second)
            and statistics.mean(first) > 0 and statistics.mean(second) > 0}


def main():
    global TAIL
    parser = argparse.ArgumentParser()
    parser.add_argument('--census', type=Path, default=ROOT / 'log/2026-10-13/init7-liquid-ah-census')
    parser.add_argument('--out', type=Path, default=ROOT / 'log/2026-10-13/init7-liquid-drift')
    parser.add_argument('--first', default=census.FIRST)
    parser.add_argument('--last', default=census.LAST)
    parser.add_argument('--tail', type=float, default=0.05 / 8 / 2, help='one-sided bootstrap tail per interval end')
    args = parser.parse_args()
    TAIL = args.tail
    census.configure(args.first, args.last)
    args.out.mkdir(parents=True, exist_ok=True)

    cal = json.loads((args.census / 'calendar.json').read_text())
    dates = [d['date'] for d in cal]
    months = sorted({d[:7] for d in dates if census.FIRST <= d <= census.LAST})
    top = census.rankings(census.load(args.census / 'monthly.json.gz'), months)
    events = census.candidates(args.census, top, cal)
    adj = {s: {r['t'][:10]: r for r in rows}
           for s, rows in census.load(args.census / 'daily-split.json.gz').items()}

    def window(day, entry, hold):
        i = dates.index(day)
        start = i + 1                       # both entries trade on D+1
        end = i + hold if entry == 'open' else i + 1 + hold
        if end >= len(dates):
            return None
        return dates[start], dates[end]

    def ret(symbol, entry, a, b):
        bars = adj.get(symbol, {})
        if a not in bars or b not in bars or not bars[a]['o'] or not bars[a]['c'] or not bars[b]['c']:
            return None
        return bars[b]['c'] / bars[a]['o' if entry == 'open' else 'c'] - 1

    bench_cache = {}

    def bench(day, entry, hold, a, b):
        key = (day, entry, hold)
        if key not in bench_cache:
            vals = [r for s in top[day[:7]] if (r := ret(s, entry, a, b)) is not None]
            bench_cache[key] = (statistics.mean(vals), len(vals))
        return bench_cache[key]

    counts = {'split': 0, 'events_long': 0, 'events_short': 0}
    cells = {f'{side}_{entry}_{hold}': [] for side in SIDES for entry in ENTRIES for hold in HOLDS}
    trunc = {k: 0 for k in cells}
    missing = {k: 0 for k in cells}
    for e in events:
        if e['split']:
            counts['split'] += 1
            continue
        counts['events_' + e['side']] += 1
        for entry in ENTRIES:
            for hold in HOLDS:
                k = f"{e['side']}_{entry}_{hold}"
                w = window(e['date'], entry, hold)
                if w is None:
                    trunc[k] += 1
                    continue
                r = ret(e['symbol'], entry, *w)
                if r is None:
                    missing[k] += 1
                    continue
                b, nb = bench(e['date'], entry, hold, *w)
                sign = 1 if e['side'] == 'long' else -1
                cells[k].append({'symbol': e['symbol'], 'date': e['date'], 'move': e['move'],
                                 'raw': r, 'bench': b, 'bench_n': nb,
                                 'net': sign * (r - b) - COST})

    result = {'freeze': str(FREEZE.relative_to(ROOT)), 'census': str(args.census.relative_to(ROOT)),
              'last_bar': dates[-1], 'window': [census.FIRST, census.LAST], 'tail': TAIL, 'counts': counts, 'truncated': trunc, 'missing_bars': missing,
              'cells': {}, 'by_move_open_20': {}, 'events_by_month': {}}
    for k, rows in cells.items():
        result['cells'][k] = {'base': summary(rows, 'net'), 'stress': summary(rows, 'net', STRESS),
                              'raw_event_mean_pct': round(statistics.mean(r['raw'] for r in rows) * 100, 3),
                              'bench_mean_pct': round(statistics.mean(r['bench'] for r in rows) * 100, 3),
                              'bench_members_min': min(r['bench_n'] for r in rows)}
    for side in SIDES:
        rows = cells[f'{side}_open_20']
        for label, lo, hi in (('3-6%', .03, .06), ('6-10%', .06, .10), ('>10%', .10, 99)):
            sub = [r for r in rows if lo <= abs(r['move']) < hi]
            result['by_move_open_20'][f'{side} {label}'] = summary(sub, 'net')
        for r in cells[f'{side}_open_5']:
            m = result['events_by_month'].setdefault(r['date'][:7], {'long': 0, 'short': 0})
            m[side] += 1
    result['passed_cells'] = [k for k, v in result['cells'].items() if v['base'].get('passed')]
    result['passed'] = bool(result['passed_cells'])
    (args.out / 'result.json').write_text(json.dumps(result, indent=1))
    with gzip.open(args.out / 'rows.json.gz', 'wt') as handle:
        json.dump(cells, handle)
    print(json.dumps(result, indent=1))


if __name__ == '__main__':
    main()
