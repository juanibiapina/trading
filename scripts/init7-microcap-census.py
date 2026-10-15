#!/usr/bin/env python3
"""Initiative 7: census of micro-cap after-hours ignitions, per docs/investigations/init7-microcap-census-freeze.json.

Does the core AH->PM strategy have any positive subset when entries pay the SIP ask and exits get the SIP bid?

  init7-microcap-census.py --out DIR                 # fetch (resumable; caches in DIR) and evaluate
  init7-microcap-census.py --out DIR --replay        # evaluate cached inputs only
  init7-microcap-census.py --out DIR --first D --last D   # smaller window (verification runs)
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
spec = importlib.util.spec_from_file_location('lc', ROOT / 'scripts/init7-liquid-ah-census.py')
lc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lc)

FREEZE = ROOT / 'docs/investigations/init7-microcap-census-freeze.json'
MONTHLY = ROOT / 'log/2026-10-13/init7-liquid-ah-census/monthly.json.gz'
REAL = ROOT / 'log/2026-10-09/init3-exec-gap/result.json'
FIRST, LAST = '2025-10-01', '2026-09-30'
HISTORY_START, DAILY_END = '2025-08-25', '2026-10-09'
PRICE = (0.50, 10.00)
GATE, CEILING, DAY_FLOOR = 0.10, 1.50, -0.15
MIN_SHARES, MIN_DOLLARS, SPIKE, LOOKBACK = 100_000, 100_000, 3.0, 20
AUCTION_BPS, STRESS_BPS = 50, 100
EXITS = ('exit_0430', 'exit_open')
SUBSETS = ('all', 'build', 'fresh', 'build_fresh')
TAIL = 0.025 / 8


def daily_maps(out):
    raw = lc.load(out / 'daily-raw.json.gz')
    split = lc.load(out / 'daily-split.json.gz')
    return ({s: {r['t'][:10]: r for r in rows} for s, rows in raw.items()},
            {s: {r['t'][:10]: r['c'] for r in rows} for s, rows in split.items()})


def full_days(cal, first, last):
    return [d['date'] for d in cal if d['close'] == '16:00' and first <= d['date'] <= last]


def fetch_set(daily, day):
    return sorted(s for s, rows in daily.items() if day in rows and PRICE[0] <= rows[day]['c'] <= PRICE[1])


def fetch(out, quotes_too=True):
    uni = lc.load(lc.UNIVERSE)
    symbols = sorted(set(uni['alpaca']) | set(uni['sp500_since_2016']))
    lc.HISTORY_START, lc.DAILY_END = HISTORY_START, DAILY_END
    if not (out / 'calendar.json').exists():
        (out / 'calendar.json').write_text(json.dumps(lc.calendar()))
    cal = json.loads((out / 'calendar.json').read_text())
    for adjustment in ('raw', 'split'):
        path = out / f'daily-{adjustment}.json.gz'
        if not path.exists():
            lc.save(path, lc.bars(symbols, '1Day', HISTORY_START, DAILY_END, adjustment, batch=100))
            print(f'daily {adjustment} cached', flush=True)
    daily, _ = daily_maps(out)
    ah_dir = out / 'ah'
    ah_dir.mkdir(exist_ok=True)
    days = full_days(cal, HISTORY_START, LAST)
    for n, day in enumerate(days, 1):
        path = ah_dir / f'{day}.json.gz'
        if path.exists():
            continue
        names = fetch_set(daily, day)
        data = lc.bars(names, '5Min', lc.iso(lc.et(day, 1600)), lc.iso(lc.et(day, 1659)), 'raw', batch=500)
        lc.save(path, {'fetched': names, 'bars': data})
        print(f'ah {day} {len(names)} symbols ({n}/{len(days)})', flush=True)
    print('bars cached', flush=True)
    if not quotes_too:
        return
    events = candidates(out, cal)
    qpath = out / 'quotes.json.gz'
    quotes = lc.load(qpath) if qpath.exists() else {}
    pending = [e for e in events if e['key'] not in quotes]
    print(f'{len(events)} events, {len(pending)} need quotes', flush=True)
    for n, e in enumerate(pending, 1):
        quotes[e['key']] = {
            'entry': lc.last_quote(e['symbol'], lc.et(e['date'], 1645), lc.et(e['date'], 1700)),
            'exit_0430': lc.last_quote(e['symbol'], lc.et(e['next'], 400), lc.et(e['next'], 430)),
        }
        if n % 100 == 0:
            lc.save(qpath, quotes)
            print(f'quotes {n}/{len(pending)}', flush=True)
    lc.save(qpath, quotes)


def last_close(rows, day, hhmm):
    cut = lc.iso(lc.et(day, hhmm))
    rows = [r for r in rows if r['t'] <= cut]
    return rows[-1]['c'] if rows else None


def candidates(out, cal):
    daily, splitc = daily_maps(out)
    months = sorted({d['date'][:7] for d in cal if FIRST <= d['date'] <= LAST})
    top = lc.rankings(lc.load(MONTHLY), months)
    dates = [d['date'] for d in cal]
    window, events = {}, []
    for day in full_days(cal, HISTORY_START, LAST):
        cached = lc.load(out / 'ah' / f'{day}.json.gz')
        ah, fetched = cached['bars'], cached['fetched']
        today = {}
        for s in fetched:
            rows = [r for r in ah.get(s, []) if lc.iso(lc.et(day, 1600)) <= r['t'] <= lc.iso(lc.et(day, 1655))]
            today[s] = (sum(r['v'] for r in rows), sum(r['v'] * (r['vw'] or r['c']) for r in rows))
        if FIRST <= day <= LAST:
            excluded = set(top.get(day[:7], []))
            i = dates.index(day)
            prev, nxt = dates[i - 1], dates[i + 1]
            for s in fetched:
                history = window.get(s, [])
                bar = daily[s][day]
                close = bar['c']
                p1630, p1700 = last_close(ah.get(s, []), day, 1625), last_close(ah.get(s, []), day, 1655)
                volume, dollars = today[s]
                if s in excluded or len(history) < LOOKBACK or p1630 is None or p1700 is None:
                    continue
                if p1630 / close - 1 < GATE or p1700 / close - 1 < GATE or p1700 / close - 1 > CEILING:
                    continue
                c1 = daily[s].get(prev, {}).get('c')
                if not c1 or close / c1 - 1 <= DAY_FLOOR:
                    continue
                if volume < MIN_SHARES or dollars < MIN_DOLLARS or volume < SPIKE * statistics.median(history[-LOOKBACK:]):
                    continue
                closes = [daily[s].get(dates[i - k], {}).get('c') for k in range(4)]   # D, D-1, D-2, D-3
                runner = (any(closes[k] and closes[k + 1] and closes[k] / closes[k + 1] - 1 >= 0.5 for k in range(3))
                          or bool(closes[3] and close >= 2 * closes[3]))
                d1 = daily[s].get(nxt)
                ratio = lambda d: daily[s][d]['c'] / splitc[s][d] if d in splitc.get(s, {}) and d in daily[s] else None
                events.append({'key': f'{s}|{day}', 'symbol': s, 'date': day, 'next': nxt, 'close': close,
                               'p1630': p1630, 'p1700': p1700, 'move': p1700 / close - 1, 'day_change': close / c1 - 1,
                               'build': p1700 >= p1630, 'fresh': not runner,
                               'volume_ratio': volume / max(statistics.median(history[-LOOKBACK:]), 1),
                               'ah_shares': volume, 'ah_dollars': dollars, 'open1': d1 and d1['o'],
                               'split': d1 is not None and ratio(day) is not None and ratio(nxt) is not None
                               and abs(ratio(day) / ratio(nxt) - 1) > 0.01})
        for s in fetched:
            window.setdefault(s, []).append(today[s][0])
    return events


def returns(events, quotes):
    rows, counts = [], {'no_entry_quote': 0, 'no_next_open': 0, 'split': 0, 'exit_0430_fallback': 0}
    slip = 1 - AUCTION_BPS / 1e4
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
        entry, x = q['entry']['ap'], q.get('exit_0430')
        if lc.valid(x):
            p0430, m0430 = x['bp'], (x['ap'] + x['bp']) / 2
        else:
            p0430, m0430 = e['open1'] * slip, e['open1']
            counts['exit_0430_fallback'] += 1
        mid = (q['entry']['ap'] + q['entry']['bp']) / 2
        rows.append({**e, 'entry': entry, 'spread_bps': (entry - q['entry']['bp']) / mid * 1e4,
                     'exit_0430': p0430 / entry - 1, 'exit_open': e['open1'] * slip / entry - 1,
                     'gross_exit_0430': m0430 / mid - 1, 'gross_exit_open': e['open1'] / mid - 1,
                     'all': True, 'build_fresh': e['build'] and e['fresh']})
    return rows, counts


def recall(events, rows):
    real = json.loads(REAL.read_text())['rows']
    keys = {e['key'] for e in events}
    scored = {r['key'] for r in rows}
    window = [r for r in real if FIRST <= r['date'] <= LAST]
    return {'real_entries_in_window': len(window),
            'as_events': sum(f"{r['symbol']}|{r['date']}" in keys for r in window),
            'as_scored_rows': sum(f"{r['symbol']}|{r['date']}" in scored for r in window)}


def evaluate(out):
    cal = json.loads((out / 'calendar.json').read_text())
    events = candidates(out, cal)
    quotes = lc.load(out / 'quotes.json.gz')
    rows, counts = returns(events, quotes)
    summary = lambda sub, key, stress=0.0: lc.summary(sub, key, stress, tail=TAIL)
    result = {'freeze': str(FREEZE.relative_to(ROOT)), 'window': [FIRST, LAST],
              'ah_dates': len(full_days(cal, FIRST, LAST)), 'events': len(events), 'scored': len(rows),
              'excluded': counts, 'cells': {}, 'gross_mid': {}, 'descriptive': {}}
    for name in SUBSETS:
        sub = [r for r in rows if r[name]]
        result['cells'][name] = {k: {'base': summary(sub, k), 'stress': summary(sub, k, STRESS_BPS / 1e4)}
                                 for k in EXITS}
        result['gross_mid'][name] = {k: summary(sub, 'gross_' + k) for k in EXITS}
    result['passed_cells'] = [f'{n}/{k}' for n in SUBSETS for k in EXITS if result['cells'][n][k]['base'].get('passed')]
    result['passed'] = bool(result['passed_cells'])
    buckets = {'move': (('10-25%', .10, .25), ('25-50%', .25, .50), ('50-150%', .50, 9)),
               'close': (('$0.50-1', 0, 1), ('$1-3', 1, 3), ('$3-10', 3, 99)),
               'ah_dollars': (('<$300k', 0, 3e5), ('$300k-1M', 3e5, 1e6), ('>$1M', 1e6, 1e12))}
    for field, spec_ in buckets.items():
        result['descriptive'][field] = {label: {k: summary([r for r in rows if lo <= r[field] < hi], k) for k in EXITS}
                                        for label, lo, hi in spec_}
    if len(rows) > 3:
        result['descriptive']['entry_spread_bps'] = dict(zip(('p25', 'p50', 'p75'), (
            round(v, 1) for v in statistics.quantiles([r['spread_bps'] for r in rows], n=4))))
    by_month = {}
    for r in rows:
        by_month[r['date'][:7]] = by_month.get(r['date'][:7], 0) + 1
    result['descriptive']['scored_by_month'] = by_month
    result['recall'] = recall(events, rows)
    pick = lambda r: {k: (round(r[k], 4) if isinstance(r[k], float) else r[k])
                      for k in ('symbol', 'date', 'move', 'entry', 'spread_bps', 'build', 'fresh', *EXITS)}
    best = sorted(rows, key=lambda r: -r['exit_0430'])
    result['top5_exit_0430'] = [pick(r) for r in best[:5]]
    result['bottom5_exit_0430'] = [pick(r) for r in best[-5:]]
    (out / 'result.json').write_text(json.dumps(result, indent=1))
    with gzip.open(out / 'events.json.gz', 'wt') as handle:
        json.dump(rows, handle)
    print(json.dumps({k: result[k] for k in ('events', 'scored', 'excluded', 'passed_cells', 'recall')}, indent=1))
    for n in SUBSETS:
        for k in EXITS:
            b = result['cells'][n][k]['base']
            print(n, k, b.get('n'), b.get('mean_pct'), b.get('interval_pct'), b.get('halves_pct'))


def main():
    global FIRST, LAST
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--replay', action='store_true')
    parser.add_argument('--first', default=FIRST)
    parser.add_argument('--last', default=LAST)
    args = parser.parse_args()
    FIRST, LAST = args.first, args.last
    args.out.mkdir(parents=True, exist_ok=True)
    if not args.replay:
        fetch(args.out)
    evaluate(args.out)


if __name__ == '__main__':
    main()
