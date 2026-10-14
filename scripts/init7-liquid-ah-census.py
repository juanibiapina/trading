#!/usr/bin/env python3
"""Initiative 7: census of liquid after-hours movers, per docs/investigations/init7-liquid-ah-census-freeze.json.

Does the AH->PM continuation behind the core strategy pay after costs in the top 1000 names by dollar volume?

  init7-liquid-ah-census.py --out DIR            # fetch (resumable; caches in DIR) and evaluate
  init7-liquid-ah-census.py --out DIR --replay   # evaluate cached inputs only
Run from the repo root with ALPACA_API_KEY / ALPACA_SECRET_KEY set.
"""
import argparse
import datetime as dt
import gzip
import json
import os
import random
import statistics
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
FREEZE = ROOT / 'docs/investigations/init7-liquid-ah-census-freeze.json'
UNIVERSE = ROOT / 'log/2026-10-12/init7-reversal20-pit/universe.json.gz'
DATA = 'https://data.alpaca.markets'
ET = ZoneInfo('America/New_York')
FIRST, LAST = '2025-10-01', '2026-09-30'
HISTORY_START = '2025-08-25'          # 20+ AH sessions of volume history before FIRST
DAILY_END = '2026-10-09'              # last daily bar fetched (covers 20-session holds after LAST)
MONTHLY_RANGE = ('2025-07-01', '2026-08-31')
TOP, MOVE, SPIKE, MIN_DOLLARS, LOOKBACK = 1000, 0.03, 3.0, 1_000_000, 20
AUCTION_BPS, STRESS_BPS = 5, 20
EXITS = ('exit_0430', 'exit_open', 'exit_close')
FOLD = {'GOOG': 'GOOGL', 'BRK.A': 'BRK.B', 'FOX': 'FOXA', 'NWS': 'NWSA'}


def headers():
    return {'APCA-API-KEY-ID': os.environ['ALPACA_API_KEY'],
            'APCA-API-SECRET-KEY': os.environ['ALPACA_SECRET_KEY']}


def get_json(url):
    for attempt in range(8):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=headers()), timeout=120) as response:
                return json.load(response)
        except urllib.error.HTTPError as error:
            if error.code not in (429, 500, 502, 503, 504):
                raise
        except (urllib.error.URLError, TimeoutError):
            pass
        time.sleep(min(60, 5 * 2 ** attempt))
    raise RuntimeError('gave up: ' + url)


def save(path, data):
    tmp = path.with_suffix('.tmp')
    with gzip.open(tmp, 'wt') as handle:
        json.dump(data, handle)
    tmp.replace(path)


def load(path):
    with gzip.open(path, 'rt') as handle:
        return json.load(handle)


def bars(symbols, timeframe, start, end, adjustment, batch=200):
    out = {}
    for k in range(0, len(symbols), batch):
        chunk, token = symbols[k:k + batch], None
        while True:
            query = {'symbols': ','.join(chunk), 'timeframe': timeframe, 'feed': 'sip', 'adjustment': adjustment,
                     'start': start, 'end': end, 'limit': 10000, 'sort': 'asc'}
            if token:
                query['page_token'] = token
            payload = get_json(DATA + '/v2/stocks/bars?' + urllib.parse.urlencode(query))
            for s, rows in (payload.get('bars') or {}).items():
                out.setdefault(s, []).extend({f: r.get(f) for f in ('t', 'o', 'c', 'v', 'vw')} for r in rows)
            token = payload.get('next_page_token')
            if not token:
                break
    return out


def et(day, hhmm):
    h, m = divmod(hhmm, 100)
    return dt.datetime.combine(dt.date.fromisoformat(day), dt.time(h, m), ET)


def iso(stamp):
    return stamp.astimezone(dt.timezone.utc).isoformat().replace('+00:00', 'Z')


def last_quote(symbol, start, end):
    query = {'feed': 'sip', 'start': iso(start), 'end': iso(end), 'limit': 1, 'sort': 'desc'}
    payload = get_json(f'{DATA}/v2/stocks/{urllib.parse.quote(symbol)}/quotes?' + urllib.parse.urlencode(query))
    quotes = payload.get('quotes') or []
    return {k: quotes[0].get(k) for k in ('t', 'bp', 'ap', 'bs', 'as')} if quotes else None


def configure(first, last):
    """Move the event window (default: the October 13 census year). History, daily and monthly ranges follow it."""
    global FIRST, LAST, HISTORY_START, DAILY_END, MONTHLY_RANGE
    FIRST, LAST = first, last
    HISTORY_START = (dt.date.fromisoformat(first) - dt.timedelta(days=37)).isoformat()
    DAILY_END = min(dt.date(2026, 10, 9), dt.date.fromisoformat(last) + dt.timedelta(days=45)).isoformat()
    end_month = month_add(last[:7], -1)
    y, m = map(int, end_month.split('-'))
    last_day = (dt.date(y + m // 12, m % 12 + 1, 1) - dt.timedelta(days=1)).isoformat()
    MONTHLY_RANGE = (month_add(first[:7], -3) + '-01', last_day)


def month_add(ym, k):
    y, m = map(int, ym.split('-'))
    m += k
    y, m = y + (m - 1) // 12, (m - 1) % 12 + 1
    return f'{y:04d}-{m:02d}'


def rankings(monthly, months):
    dv, seen = {}, {}
    for s, rows in sorted(monthly.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        for r in rows:
            if not r.get('v') or not r.get('vw'):
                continue
            ym, key = r['t'][:7], (r['t'][:7], r['v'])
            if key in seen:
                continue
            seen[key] = s
            dv.setdefault(ym, {})[FOLD.get(s, s)] = dv.get(ym, {}).get(FOLD.get(s, s), 0) + r['v'] * r['vw']
    top = {}
    for month in months:
        prior = [month_add(month, -k) for k in (1, 2, 3)]
        names = set.intersection(*(set(dv.get(p, {})) for p in prior))
        score = {s: sum(dv[p][s] for p in prior) for s in names}
        top[month] = sorted(score, key=lambda s: (-score[s], s))[:TOP]
    return top


def calendar():
    url = 'https://paper-api.alpaca.markets/v2/calendar?' + urllib.parse.urlencode(
        {'start': HISTORY_START, 'end': DAILY_END})
    return [{'date': d['date'], 'close': d['close']} for d in get_json(url)]


def fetch(out, quotes_too=True):
    uni = load(UNIVERSE)
    symbols = sorted(set(uni['alpaca']) | set(uni['sp500_since_2016']))
    if not (out / 'calendar.json').exists():
        (out / 'calendar.json').write_text(json.dumps(calendar()))
    cal = json.loads((out / 'calendar.json').read_text())
    if not (out / 'monthly.json.gz').exists():
        save(out / 'monthly.json.gz', bars(symbols, '1Month', *MONTHLY_RANGE, 'raw'))
    months = sorted({d['date'][:7] for d in cal if FIRST <= d['date'] <= LAST})
    top = rankings(load(out / 'monthly.json.gz'), months)
    members = sorted({s for names in top.values() for s in names})
    print(f'{len(members)} symbols ever in the top {TOP}', flush=True)
    for adjustment in ('raw', 'split'):
        path = out / f'daily-{adjustment}.json.gz'
        if not path.exists():
            save(path, bars(members, '1Day', HISTORY_START, DAILY_END, adjustment, batch=100))
    ah_dir = out / 'ah'
    ah_dir.mkdir(exist_ok=True)
    full = [d['date'] for d in cal if d['close'] == '16:00' and d['date'] <= LAST]
    for day in full:
        path = ah_dir / f'{day}.json.gz'
        if not path.exists():
            save(path, bars(members, '5Min', iso(et(day, 1600)), iso(et(day, 1659)), 'raw', batch=500))
    print('bars cached', flush=True)
    if not quotes_too:
        return
    events = candidates(out, top, cal)
    qpath = out / 'quotes.json.gz'
    quotes = load(qpath) if qpath.exists() else {}
    pending = [e for e in events if e['key'] not in quotes]
    print(f'{len(events)} events, {len(pending)} need quotes', flush=True)
    for n, e in enumerate(pending, 1):
        quotes[e['key']] = {
            'entry': last_quote(e['symbol'], et(e['date'], 1655), et(e['date'], 1700)),
            'exit_0430': last_quote(e['symbol'], et(e['next'], 400), et(e['next'], 430)),
        }
        if n % 100 == 0:
            save(qpath, quotes)
            print(f'quotes {n}/{len(pending)}', flush=True)
    save(qpath, quotes)


def candidates(out, top, cal):
    """Long and short ignitions per the frozen move and volume tests, with D+1 attached."""
    raw = load(out / 'daily-raw.json.gz')
    split = load(out / 'daily-split.json.gz')
    daily = {s: {r['t'][:10]: r for r in rows} for s, rows in raw.items()}
    splitc = {s: {r['t'][:10]: r['c'] for r in rows} for s, rows in split.items()}
    dates = [d['date'] for d in cal]
    full = [d['date'] for d in cal if d['close'] == '16:00' and d['date'] <= LAST]
    window, events = {}, []                 # window[symbol] -> list of prior 16:05-16:55 volumes
    for day in full:
        ah = load(out / 'ah' / f'{day}.json.gz')
        members = set(top.get(day[:7], [])) if FIRST <= day <= LAST else set()
        today = {}
        for s, rows in ah.items():
            rows = [r for r in rows if r['t'] >= iso(et(day, 1605)) and r['t'] <= iso(et(day, 1655))]
            today[s] = (sum(r['v'] for r in rows), sum(r['v'] * (r['vw'] or r['c']) for r in rows))
        for s in members:
            history = window.get(s, [])
            bars_today = [r for r in ah.get(s, []) if r['t'] <= iso(et(day, 1655))]
            close = daily.get(s, {}).get(day)
            if not bars_today or not close or len(history) < LOOKBACK:
                continue
            move = bars_today[-1]['c'] / close['c'] - 1
            volume, dollars = today.get(s, (0, 0))
            base = statistics.median(history[-LOOKBACK:])
            if abs(move) < MOVE or dollars < MIN_DOLLARS or volume < SPIKE * max(base, 1):
                continue
            nxt = dates[dates.index(day) + 1]
            d1 = daily.get(s, {}).get(nxt)
            ratio = lambda d: daily[s][d]['c'] / splitc[s][d] if d in splitc.get(s, {}) else None
            events.append({'key': f'{s}|{day}', 'symbol': s, 'date': day, 'next': nxt,
                           'side': 'long' if move > 0 else 'short', 'move': move, 'close': close['c'],
                           'ah_last': bars_today[-1]['c'], 'volume_ratio': volume / max(base, 1),
                           'ah_dollars': dollars, 'open1': d1 and d1['o'], 'close1': d1 and d1['c'],
                           'split': d1 is not None and ratio(day) is not None and ratio(nxt) is not None
                           # adjusted closes are rounded to cents, so only a 1% ratio change marks a split
                           and abs(ratio(day) / ratio(nxt) - 1) > 0.01})
        for s in set(window) | set(today):
            window.setdefault(s, []).append(today.get(s, (0, 0))[0])
    return events


def valid(q):
    return q and q.get('bp') and q.get('ap') and q['bp'] > 0 and q['ap'] > q['bp']


def returns(events, quotes):
    rows, counts = [], {'no_entry_quote': 0, 'no_next_bar': 0, 'split': 0, 'exit_0430_fallback': 0}
    for e in events:
        q = quotes.get(e['key'], {})
        if e['split']:
            counts['split'] += 1
            continue
        if not e['open1'] or not e['close1']:
            counts['no_next_bar'] += 1
            continue
        if not valid(q.get('entry')):
            counts['no_entry_quote'] += 1
            continue
        long = e['side'] == 'long'
        entry = q['entry']['ap'] if long else q['entry']['bp']
        sign, slip = (1, 1 - AUCTION_BPS / 1e4) if long else (-1, 1 + AUCTION_BPS / 1e4)
        x = q.get('exit_0430')
        if valid(x):
            p0430 = x['bp'] if long else x['ap']
        else:
            p0430 = e['open1'] * slip
            counts['exit_0430_fallback'] += 1
        exits = {'exit_0430': p0430, 'exit_open': e['open1'] * slip, 'exit_close': e['close1'] * slip}
        mid = (q['entry']['ap'] + q['entry']['bp']) / 2
        rows.append({**e, 'entry': entry, 'spread_bps': (q['entry']['ap'] - q['entry']['bp']) / mid * 1e4,
                     **{k: sign * (p / entry - 1) for k, p in exits.items()},
                     **{'gross_' + k: sign * (p / mid - 1) for k, p in
                        {'exit_0430': (x['ap'] + x['bp']) / 2 if valid(x) else e['open1'],
                         'exit_open': e['open1'], 'exit_close': e['close1']}.items()}})
    return rows, counts


def by_date_interval(rows, key, tail, draws=4000, seed=13):
    groups = {}
    for r in rows:
        groups.setdefault(r['date'], []).append(r[key])
    days = sorted(groups)
    rng, means = random.Random(seed), []
    for _ in range(draws):
        sample = [v for _ in days for v in groups[days[rng.randrange(len(days))]]]
        means.append(statistics.mean(sample))
    means.sort()
    return means[int(tail * draws)], means[int((1 - tail) * draws) - 1]


def summary(rows, key, stress=0.0, tail=0.025 / 3):
    if len(rows) < 2:
        return {'n': len(rows)}
    shifted = [dict(r, **{key: r[key] - stress}) for r in rows]
    ordered = sorted(shifted, key=lambda r: r['date'])
    half = ordered[len(ordered) // 2]['date']
    first = [r[key] for r in ordered if r['date'] < half]
    second = [r[key] for r in ordered if r['date'] >= half]
    lo, hi = by_date_interval(shifted, key, tail)
    mean = statistics.mean(r[key] for r in shifted)
    return {'n': len(rows), 'mean_pct': round(mean * 100, 3), 'median_pct': round(
        statistics.median(r[key] for r in shifted) * 100, 3),
        'interval_pct': [round(lo * 100, 3), round(hi * 100, 3)],
        'win_rate': round(sum(r[key] > 0 for r in shifted) / len(shifted), 3),
        'halves_pct': [round(statistics.mean(first) * 100, 3) if first else None,
                       round(statistics.mean(second) * 100, 3) if second else None],
        'passed': mean > 0 and lo > 0 and bool(first) and bool(second)
        and statistics.mean(first) > 0 and statistics.mean(second) > 0}


def evaluate(out):
    cal = json.loads((out / 'calendar.json').read_text())
    months = sorted({d['date'][:7] for d in cal if FIRST <= d['date'] <= LAST})
    top = rankings(load(out / 'monthly.json.gz'), months)
    events = candidates(out, top, cal)
    quotes = load(out / 'quotes.json.gz')
    rows, counts = returns(events, quotes)
    longs = [r for r in rows if r['side'] == 'long']
    shorts = [r for r in rows if r['side'] == 'short']
    result = {'freeze': str(FREEZE.relative_to(ROOT)), 'window': [FIRST, LAST],
              'ah_dates': sum(1 for d in cal if d['close'] == '16:00' and FIRST <= d['date'] <= LAST),
              'symbols_ever_in_top': len({s for v in top.values() for s in v}),
              'events_long': sum(e['side'] == 'long' for e in events),
              'events_short': sum(e['side'] == 'short' for e in events), 'excluded': counts,
              'long': {k: {'base': summary(longs, k), 'stress': summary(longs, k, STRESS_BPS / 1e4)} for k in EXITS},
              'long_gross_mid': {k: summary(longs, 'gross_' + k) for k in EXITS},
              'short_descriptive': {k: summary(shorts, k) for k in EXITS},
              'long_by_move': {}, 'long_by_month': {},
              'entry_spread_bps_long': {q: round(statistics.quantiles([r['spread_bps'] for r in longs], n=4)[i], 1)
                                        for i, q in enumerate(('p25', 'p50', 'p75'))} if len(longs) > 3 else None}
    for label, lo, hi in (('3-6%', .03, .06), ('6-10%', .06, .10), ('>10%', .10, 99)):
        sub = [r for r in longs if lo <= r['move'] < hi]
        result['long_by_move'][label] = {k: summary(sub, k) for k in EXITS}
    for r in longs:
        result['long_by_month'][r['date'][:7]] = result['long_by_month'].get(r['date'][:7], 0) + 1
    result['passed_exits'] = [k for k in EXITS if result['long'][k]['base'].get('passed')]
    result['passed'] = bool(result['passed_exits'])
    best = sorted(longs, key=lambda r: -r['exit_0430'])
    pick = lambda r: {k: (round(r[k], 4) if isinstance(r[k], float) else r[k])
                      for k in ('symbol', 'date', 'move', 'volume_ratio', 'spread_bps', *EXITS)}
    result['long_top5_exit_0430'] = [pick(r) for r in best[:5]]
    result['long_bottom5_exit_0430'] = [pick(r) for r in best[-5:]]
    (out / 'result.json').write_text(json.dumps(result, indent=1))
    with gzip.open(out / 'events.json.gz', 'wt') as handle:
        json.dump(rows, handle)
    print(json.dumps(result, indent=1))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--replay', action='store_true')
    parser.add_argument('--first', default=FIRST)
    parser.add_argument('--last', default=LAST)
    parser.add_argument('--bars-only', action='store_true', help='fetch bars, skip quotes and evaluation')
    args = parser.parse_args()
    configure(args.first, args.last)
    args.out.mkdir(parents=True, exist_ok=True)
    if not args.replay:
        fetch(args.out, quotes_too=not args.bars_only)
    if not args.bars_only:
        evaluate(args.out)


if __name__ == '__main__':
    main()
