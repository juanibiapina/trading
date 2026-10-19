#!/usr/bin/env python3
"""Initiative 7: ignition-bar entry census, per docs/investigations/init7-ignition-entry-freeze.json.

Buy micro-cap AH movers at the first 5-minute bar with >=10x the day's largest regular-session bar
(Juan, Oct 19 XXII) instead of at the 17:00+ scans; sell at the 04:30 ET bid or the open.
Reuses the AH bars, daily bars and calendar cached by scripts/init7-microcap-short-fade.py.

  init7-ignition-entry.py --out DIR            # fetch regular-session bars and quotes (resumable), evaluate
  init7-ignition-entry.py --out DIR --replay   # evaluate cached inputs only
Run from the repo root with ALPACA_API_KEY / ALPACA_SECRET_KEY set.
"""
import argparse
import datetime as dt
import importlib.util
import json
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location('lc', ROOT / 'scripts/init7-liquid-ah-census.py')
lc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lc)

FREEZE = ROOT / 'docs/investigations/init7-ignition-entry-freeze.json'
SRC = ROOT / 'log/2026-10-16/init7-short-fade'
MONTHLY = ROOT / 'log/2026-10-14/init7-liquid-fade-oos/census/monthly.json.gz'
FIRST, LAST = '2024-10-01', '2025-09-30'
GATE, CEILING, DAY_FLOOR, RATIO = 0.10, 1.50, -0.15, 10
MIN_SHARES, MIN_DOLLARS = 100_000, 100_000
SLIP, STRESS = 1 - 50 / 1e4, 0.01
EXITS, SUBSETS, TAIL = ('exit_0430', 'exit_open'), ('all', 'early'), 0.025 / 4


def hhmm(stamp):
    t = dt.datetime.fromisoformat(stamp.replace('Z', '+00:00')).astimezone(lc.ET)
    return t.hour * 100 + t.minute


def plus(day, at, minutes):
    return lc.et(day, at) + dt.timedelta(minutes=minutes)


def setup():
    cal = json.loads((SRC / 'calendar.json').read_text())
    daily = {s: {r['t'][:10]: r for r in rows} for s, rows in lc.load(SRC / 'daily-raw.json.gz').items()}
    splitc = {s: {r['t'][:10]: r['c'] for r in rows} for s, rows in lc.load(SRC / 'daily-split.json.gz').items()}
    days = [d['date'] for d in cal if d['close'] == '16:00' and FIRST <= d['date'] <= LAST]
    top = lc.rankings(lc.load(MONTHLY), sorted({d[:7] for d in days}))
    return cal, daily, splitc, days, top


def ah_rows(day):
    early, late = lc.load(SRC / 'ah' / f'{day}.json.gz'), lc.load(SRC / 'ah-late' / f'{day}.json.gz')['bars']
    start = lc.iso(lc.et(day, 1600))
    return early['fetched'], {s: sorted([r for r in early['bars'].get(s, []) + late.get(s, []) if r['t'] >= start],
                                        key=lambda r: r['t']) for s in early['fetched']}


def candidates_by_day(daily, days, top):
    """Symbol-days passing every rule that does not need the regular-session peak."""
    dates = sorted({d for rows in daily.values() for d in rows})
    out = {}
    for day in days:
        fetched, ah = ah_rows(day)
        prev = dates[dates.index(day) - 1]
        excluded = set(top.get(day[:7], []))
        for s in fetched:
            close, c1 = daily[s][day]['c'], daily[s].get(prev, {}).get('c')
            if s in excluded or not c1 or close / c1 - 1 <= DAY_FLOOR:
                continue
            if any(GATE < r['c'] / close - 1 <= CEILING for r in ah[s] if hhmm(r['t']) <= 1825):
                out.setdefault(day, {})[s] = ah[s]
    return out


def fetch_rth(path, cands):
    cache = lc.load(path) if path.exists() else {}
    for n, day in enumerate(sorted(cands), 1):
        if day in cache:
            continue
        names = sorted(cands[day])
        bars = lc.bars(names, '5Min', lc.iso(lc.et(day, 930)), lc.iso(lc.et(day, 1559)), 'raw', batch=500)
        cache[day] = {s: max((r['v'] for r in bars.get(s, [])), default=None) for s in names}
        if n % 25 == 0:
            lc.save(path, cache)
            print(f'rth {n}/{len(cands)}', flush=True)
    lc.save(path, cache)
    return cache


def events(cands, peaks, daily, splitc):
    dates = sorted({d for rows in daily.values() for d in rows})
    out, counts = [], {'no_rth_bars': 0}
    for day, names in sorted(cands.items()):
        nxt = dates[dates.index(day) + 1]
        for s, rows in sorted(names.items()):
            peak = peaks[day].get(s)
            if not peak:
                counts['no_rth_bars'] += 1
                continue
            close, shares, dollars = daily[s][day]['c'], 0, 0.0
            for r in rows:
                at = hhmm(r['t'])
                if at > 1825:
                    break
                shares += r['v']
                dollars += r['v'] * (r['vw'] or r['c'])
                move = r['c'] / close - 1
                if (r['v'] >= RATIO * peak and GATE < move <= CEILING
                        and shares >= MIN_SHARES and dollars >= MIN_DOLLARS):
                    d1 = daily[s].get(nxt)
                    ratio = lambda d: daily[s][d]['c'] / splitc[s][d] if d in splitc.get(s, {}) and d in daily[s] else None
                    out.append({'key': f'{s}|{day}', 'symbol': s, 'date': day, 'next': nxt, 'bar': at, 'close': close,
                                'bar_close': r['c'], 'move': move, 'ratio': r['v'] / peak, 'open1': d1 and d1['o'],
                                'split': d1 is not None and ratio(day) is not None and ratio(nxt) is not None
                                and abs(ratio(day) / ratio(nxt) - 1) > 0.01})
                    break
    return out, counts


def fetch_quotes(path, evs, old):
    quotes = lc.load(path) if path.exists() else {}
    pending = [e for e in evs if e['key'] not in quotes]
    print(f'{len(evs)} events, {len(pending)} need quotes', flush=True)
    for n, e in enumerate(pending, 1):
        prior = old.get(e['key'], {})
        quotes[e['key']] = {
            'entry': lc.last_quote(e['symbol'], lc.et(e['date'], e['bar']), plus(e['date'], e['bar'], 6)),
            'exit_0430': prior['exit_0430'] if 'exit_0430' in prior else
            lc.last_quote(e['symbol'], lc.et(e['next'], 400), lc.et(e['next'], 430)),
        }
        if n % 100 == 0:
            lc.save(path, quotes)
            print(f'quotes {n}/{len(pending)}', flush=True)
    lc.save(path, quotes)
    return quotes


def score(evs, quotes, etb, scan_rows):
    rows, counts = [], {'split': 0, 'no_next_open': 0, 'no_entry_quote': 0, 'exit_0430_fallback': 0}
    for e in evs:
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
        entry, mid = q['entry']['ap'], (q['entry']['ap'] + q['entry']['bp']) / 2
        x = q.get('exit_0430')
        if lc.valid(x):
            s0430, m0430 = x['bp'], (x['ap'] + x['bp']) / 2
        else:
            s0430, m0430 = e['open1'] * SLIP, e['open1']
            counts['exit_0430_fallback'] += 1
        scan = scan_rows.get(e['key'])
        rows.append({**e, 'entry': entry, 'spread_bps': (entry - q['entry']['bp']) / mid * 1e4,
                     'exit_0430': s0430 / entry - 1, 'exit_open': e['open1'] * SLIP / entry - 1,
                     'gross_exit_0430': m0430 / mid - 1, 'gross_exit_open': e['open1'] / mid - 1,
                     'all': True, 'early': e['bar'] <= 1640, 'etb': e['symbol'] in etb,
                     'scan_exit_0430': scan, 'paired_diff': None if scan is None else s0430 / entry - 1 - scan})
    return rows, counts


def scan_returns():
    """Long return of the 872 short-fade events bought at the scan ask, sold at the 04:30 bid (as Initiative 3)."""
    quotes, out = lc.load(SRC / 'quotes.json.gz'), {}
    for e in lc.load(SRC / 'events.json.gz'):
        q = quotes[e['key']]
        x = q.get('exit_0430')
        sell = x['bp'] if lc.valid(x) else e['open1'] * SLIP
        out[e['key']] = sell / q['entry']['ap'] - 1
    return out


def evaluate(out, evs, quotes, extra):
    flags = lc.load(SRC / 'assets.json.gz')['flags']
    etb = {s for s, (shortable, easy) in flags.items() if shortable and easy}
    rows, counts = score(evs, quotes, etb, scan_returns())
    summ = lambda sub, k, stress=0.0: lc.summary(sub, k, stress, tail=TAIL)
    result = {'freeze': str(FREEZE.relative_to(ROOT)), 'window': [FIRST, LAST], 'events': len(evs),
              'scored': len(rows), 'excluded': {**extra, **counts}, 'cells': {}, 'gross_mid': {}, 'descriptive': {}}
    for name in SUBSETS:
        sub = [r for r in rows if r[name]]
        result['cells'][name] = {k: {'base': summ(sub, k), 'stress': summ(sub, k, STRESS)} for k in EXITS}
        result['gross_mid'][name] = {k: summ(sub, 'gross_' + k) for k in EXITS}
    result['passed_cells'] = [f'{n}/{k}' for n in SUBSETS for k in EXITS if result['cells'][n][k]['base'].get('passed')]
    result['passed'] = bool(result['passed_cells'])
    d = result['descriptive']
    paired = [r for r in rows if r['paired_diff'] is not None]
    d['paired_with_scan_events'] = {'ignition_exit_0430': summ(paired, 'exit_0430'),
                                    'scan_exit_0430': summ(paired, 'scan_exit_0430'),
                                    'diff': summ(paired, 'paired_diff')}
    buckets = {'bar': (('16:00-16:25', 1600, 1630), ('16:30-16:40', 1630, 1645), ('16:45-17:25', 1645, 1730),
                       ('17:30-18:25', 1730, 1830)),
               'ratio': (('10-30x', 10, 30), ('30-100x', 30, 100), ('>100x', 100, 1e12)),
               'move': (('10-25%', .10, .25), ('25-50%', .25, .50), ('50-150%', .50, 9))}
    for field, spec_ in buckets.items():
        d[field] = {lab: {k: summ([r for r in rows if lo <= r[field] < hi], k) for k in EXITS} for lab, lo, hi in spec_}
    d['etb'] = {str(v): {k: summ([r for r in rows if r['etb'] == v], k) for k in EXITS} for v in (True, False)}
    if len(rows) > 3:
        d['entry_spread_bps'] = dict(zip(('p25', 'p50', 'p75'), (
            round(v, 1) for v in statistics.quantiles([r['spread_bps'] for r in rows], n=4))))
    months = {}
    for r in rows:
        months[r['date'][:7]] = months.get(r['date'][:7], 0) + 1
    d['scored_by_month'] = months
    pick = lambda r: {k: (round(r[k], 4) if isinstance(r[k], float) else r[k])
                      for k in ('symbol', 'date', 'bar', 'move', 'ratio', 'entry', 'exit_0430', 'exit_open')}
    best = sorted(rows, key=lambda r: -r['exit_0430'])
    result['top5_exit_0430'] = [pick(r) for r in best[:5]]
    result['bottom5_exit_0430'] = [pick(r) for r in best[-5:]]
    (out / 'result.json').write_text(json.dumps(result, indent=1))
    lc.save(out / 'rows.json.gz', rows)
    print(json.dumps({k: result[k] for k in ('events', 'scored', 'excluded', 'passed_cells')}, indent=1))
    for n in SUBSETS:
        for k in EXITS:
            b, s, g = result['cells'][n][k]['base'], result['cells'][n][k]['stress'], result['gross_mid'][n][k]
            print(n, k, b.get('n'), b.get('mean_pct'), b.get('interval_pct'), b.get('halves_pct'),
                  'stress', s.get('mean_pct'), 'mid', g.get('mean_pct'))
    print('paired', json.dumps(d['paired_with_scan_events']))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--replay', action='store_true')
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    cal, daily, splitc, days, top = setup()
    cands = candidates_by_day(daily, days, top)
    print(f'{sum(len(v) for v in cands.values())} candidate symbol-days on {len(cands)} days', flush=True)
    rth_path = args.out / 'rth-peak.json.gz'
    peaks = lc.load(rth_path) if args.replay else fetch_rth(rth_path, cands)
    evs, counts = events(cands, peaks, daily, splitc)
    qpath = args.out / 'quotes.json.gz'
    old = lc.load(SRC / 'quotes.json.gz')
    quotes = lc.load(qpath) if args.replay else fetch_quotes(qpath, evs, old)
    evaluate(args.out, evs, quotes, counts)


if __name__ == '__main__':
    main()
