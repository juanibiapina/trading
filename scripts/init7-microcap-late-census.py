#!/usr/bin/env python3
"""Initiative 7: late-entry micro-cap census, per docs/investigations/init7-microcap-late-census-freeze.json.

Do micro-cap AH ignitions entered at the 17:30, 18:00 or 18:30 ET scan (names that were not 17:00 events) net positive?
Reuses the 17:00 census cache (daily bars, 16:00-16:59 ET bars) and adds 17:00-18:29 ET bars.

  init7-microcap-late-census.py --out DIR              # fetch (resumable) and evaluate
  init7-microcap-late-census.py --out DIR --replay     # evaluate cached inputs only
  init7-microcap-late-census.py --out DIR --first D --last D   # smaller event window (verification)
Run from the repo root with ALPACA_API_KEY / ALPACA_SECRET_KEY set.
"""
import argparse
import gzip
import importlib.util
import json
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location('mc', ROOT / 'scripts/init7-microcap-census.py')
mc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mc)
lc = mc.lc

FREEZE = ROOT / 'docs/investigations/init7-microcap-late-census-freeze.json'
EARLY = ROOT / 'log/2026-10-15/init7-microcap-census'
SCANS = ((1730, 1700, 1725), (1800, 1730, 1755), (1830, 1800, 1825))   # entry T, prior checkpoint, last bar start
CHECK_BAR = {1700: 1655, 1730: 1725, 1800: 1755}
QUOTE_FROM = {1730: 1715, 1800: 1745, 1830: 1815}


def fetch_bars(out, cal, days):
    late = out / 'ah-late'
    late.mkdir(exist_ok=True)
    for n, day in enumerate(days, 1):
        path = late / f'{day}.json.gz'
        if path.exists():
            continue
        names = lc.load(EARLY / 'ah' / f'{day}.json.gz')['fetched']
        data = lc.bars(names, '5Min', lc.iso(lc.et(day, 1700)), lc.iso(lc.et(day, 1829)), 'raw', batch=500)
        lc.save(path, {'fetched': names, 'bars': data})
        print(f'late {day} {len(names)} symbols ({n}/{len(days)})', flush=True)
    print('late bars cached', flush=True)


def candidates(out, cal):
    daily, splitc = mc.daily_maps(EARLY)
    months = sorted({d['date'][:7] for d in cal if mc.FIRST <= d['date'] <= mc.LAST})
    top = lc.rankings(lc.load(mc.MONTHLY), months)
    early_keys = {e['key'] for e in mc.candidates(EARLY, cal)}
    dates = [d['date'] for d in cal]
    history, events = {}, []
    for day in mc.full_days(cal, mc.HISTORY_START, mc.LAST):
        early = lc.load(EARLY / 'ah' / f'{day}.json.gz')
        late = lc.load(out / 'ah-late' / f'{day}.json.gz')['bars']
        fetched = early['fetched']
        start = lc.iso(lc.et(day, 1600))
        today = {}
        for s in fetched:
            rows = sorted(early['bars'].get(s, []) + late.get(s, []), key=lambda r: r['t'])
            rows = [r for r in rows if r['t'] >= start]
            vol = {}
            for t, _, last in SCANS:
                cut = lc.iso(lc.et(day, last))
                upto = [r for r in rows if r['t'] <= cut]
                vol[t] = (sum(r['v'] for r in upto), sum(r['v'] * (r['vw'] or r['c']) for r in upto))
            today[s] = (rows, vol)
        if mc.FIRST <= day <= mc.LAST:
            excluded = set(top.get(day[:7], []))
            i = dates.index(day)
            prev, nxt = dates[i - 1], dates[i + 1]
            for s in fetched:
                if s in excluded or f'{s}|{day}' in early_keys or len(history.get(s, [])) < mc.LOOKBACK:
                    continue
                rows, vol = today[s]
                close = daily[s][day]['c']
                c1 = daily[s].get(prev, {}).get('c')
                if not c1 or close / c1 - 1 <= mc.DAY_FLOOR:
                    continue
                for t, prior, last in SCANS:
                    p_prior, p_t = mc.last_close(rows, day, CHECK_BAR[prior]), mc.last_close(rows, day, last)
                    if p_prior is None or p_t is None:
                        continue
                    if p_prior / close - 1 < mc.GATE or p_t / close - 1 < mc.GATE or p_t / close - 1 > mc.CEILING:
                        continue
                    shares, dollars = vol[t]
                    med = statistics.median([h[t] for h in history[s][-mc.LOOKBACK:]])
                    if shares < mc.MIN_SHARES or dollars < mc.MIN_DOLLARS or shares < mc.SPIKE * med:
                        continue
                    closes = [daily[s].get(dates[i - k], {}).get('c') for k in range(4)]
                    runner = (any(closes[k] and closes[k + 1] and closes[k] / closes[k + 1] - 1 >= 0.5 for k in range(3))
                              or bool(closes[3] and close >= 2 * closes[3]))
                    d1 = daily[s].get(nxt)
                    ratio = lambda d: daily[s][d]['c'] / splitc[s][d] if d in splitc.get(s, {}) and d in daily[s] else None
                    events.append({'key': f'{s}|{day}', 'symbol': s, 'date': day, 'next': nxt, 'scan': t, 'close': close,
                                   'p_prior': p_prior, 'p_entry': p_t, 'move': p_t / close - 1,
                                   'day_change': close / c1 - 1, 'build': p_t >= p_prior, 'fresh': not runner,
                                   'volume_ratio': shares / max(med, 1), 'ah_shares': shares, 'ah_dollars': dollars,
                                   'open1': d1 and d1['o'],
                                   'split': d1 is not None and ratio(day) is not None and ratio(nxt) is not None
                                   and abs(ratio(day) / ratio(nxt) - 1) > 0.01})
                    break
        for s in fetched:
            history.setdefault(s, []).append({t: today[s][1][t][0] for t, _, _ in SCANS})
    return events


def fetch_quotes(out, events):
    qpath = out / 'quotes.json.gz'
    quotes = lc.load(qpath) if qpath.exists() else {}
    pending = [e for e in events if e['key'] not in quotes]
    print(f'{len(events)} events, {len(pending)} need quotes', flush=True)
    for n, e in enumerate(pending, 1):
        quotes[e['key']] = {
            'entry': lc.last_quote(e['symbol'], lc.et(e['date'], QUOTE_FROM[e['scan']]), lc.et(e['date'], e['scan'])),
            'exit_0430': lc.last_quote(e['symbol'], lc.et(e['next'], 400), lc.et(e['next'], 430)),
        }
        if n % 100 == 0:
            lc.save(qpath, quotes)
            print(f'quotes {n}/{len(pending)}', flush=True)
    lc.save(qpath, quotes)


def evaluate(out, cal, events):
    quotes = lc.load(out / 'quotes.json.gz')
    rows, counts = mc.returns(events, quotes)
    summary = lambda sub, key, stress=0.0: lc.summary(sub, key, stress, tail=mc.TAIL)
    result = {'freeze': str(FREEZE.relative_to(ROOT)), 'window': [mc.FIRST, mc.LAST], 'events': len(events),
              'scored': len(rows), 'excluded': counts, 'cells': {}, 'gross_mid': {}, 'descriptive': {}}
    for name in mc.SUBSETS:
        sub = [r for r in rows if r[name]]
        result['cells'][name] = {k: {'base': summary(sub, k), 'stress': summary(sub, k, mc.STRESS_BPS / 1e4)}
                                 for k in mc.EXITS}
        result['gross_mid'][name] = {k: summary(sub, 'gross_' + k) for k in mc.EXITS}
    result['passed_cells'] = [f'{n}/{k}' for n in mc.SUBSETS for k in mc.EXITS
                              if result['cells'][n][k]['base'].get('passed')]
    result['passed'] = bool(result['passed_cells'])
    result['descriptive']['scan'] = {str(t): {k: summary([r for r in rows if r['scan'] == t], k) for k in mc.EXITS}
                                     for t, _, _ in SCANS}
    buckets = {'move': (('10-25%', .10, .25), ('25-50%', .25, .50), ('50-150%', .50, 9)),
               'close': (('$0.50-1', 0, 1), ('$1-3', 1, 3), ('$3-10', 3, 99)),
               'ah_dollars': (('<$300k', 0, 3e5), ('$300k-1M', 3e5, 1e6), ('>$1M', 1e6, 1e12))}
    for field, spec_ in buckets.items():
        result['descriptive'][field] = {label: {k: summary([r for r in rows if lo <= r[field] < hi], k)
                                                for k in mc.EXITS} for label, lo, hi in spec_}
    if len(rows) > 3:
        result['descriptive']['entry_spread_bps'] = dict(zip(('p25', 'p50', 'p75'), (
            round(v, 1) for v in statistics.quantiles([r['spread_bps'] for r in rows], n=4))))
    result['recall'] = mc.recall(events, rows)
    real = json.loads(mc.REAL.read_text())['rows']
    early_keys = {e['key'] for e in mc.candidates(EARLY, cal)}
    scored = {r['key']: r for r in rows}
    missed = [r for r in real if mc.FIRST <= r['date'] <= mc.LAST and f"{r['symbol']}|{r['date']}" not in early_keys]
    result['recall']['early_missed'] = len(missed)
    result['recall']['early_missed_now_scored'] = sum(f"{r['symbol']}|{r['date']}" in scored for r in missed)
    pick = lambda r: {k: (round(r[k], 4) if isinstance(r[k], float) else r[k])
                      for k in ('symbol', 'date', 'scan', 'move', 'entry', 'spread_bps', 'build', 'fresh', *mc.EXITS)}
    best = sorted(rows, key=lambda r: -r['exit_0430'])
    result['top5_exit_0430'] = [pick(r) for r in best[:5]]
    result['bottom5_exit_0430'] = [pick(r) for r in best[-5:]]
    (out / 'result.json').write_text(json.dumps(result, indent=1))
    with gzip.open(out / 'events.json.gz', 'wt') as handle:
        json.dump(rows, handle)
    print(json.dumps({k: result[k] for k in ('events', 'scored', 'excluded', 'passed_cells', 'recall')}, indent=1))
    for n in mc.SUBSETS:
        for k in mc.EXITS:
            b = result['cells'][n][k]['base']
            print(n, k, b.get('n'), b.get('mean_pct'), b.get('interval_pct'), b.get('halves_pct'))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--replay', action='store_true')
    parser.add_argument('--first', default=mc.FIRST)
    parser.add_argument('--last', default=mc.LAST)
    args = parser.parse_args()
    mc.FIRST, mc.LAST = args.first, args.last
    args.out.mkdir(parents=True, exist_ok=True)
    cal = json.loads((EARLY / 'calendar.json').read_text())
    if not args.replay:
        fetch_bars(args.out, cal, mc.full_days(cal, mc.HISTORY_START, mc.LAST))
    events = candidates(args.out, cal)
    if not args.replay:
        fetch_quotes(args.out, events)
    evaluate(args.out, cal, events)


if __name__ == '__main__':
    main()
