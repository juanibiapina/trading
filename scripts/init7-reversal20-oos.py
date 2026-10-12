#!/usr/bin/env python3
"""Out-of-sample test of the frozen Initiative 7 20-session reversal rule.

The rule and pass criterion are frozen in docs/investigations/init7-reversal20-freeze.json before
this script first fetched data older than 2025-10-01. It fetches adjusted daily SIP bars, replays
the rule close to close, and reports excess return over QQQ against the frozen criterion.

Design-stage research only; no order, live rule or prospective decision depends on it.

Usage:
  init7-reversal20-oos.py --out DIR            # fetch daily bars, then evaluate
  init7-reversal20-oos.py --out DIR --replay   # evaluate cached bars
"""
import argparse
import datetime as dt
import gzip
import json
import os
import random
import statistics
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FREEZE = ROOT / 'docs/investigations/init7-reversal20-freeze.json'
HURDLE_BPS = 13.29
START, END = '2016-01-01', '2025-09-30'
HOLD = 20


def get(path, query):
    headers = {'APCA-API-KEY-ID': os.environ['ALPACA_API_KEY'],
               'APCA-API-SECRET-KEY': os.environ['ALPACA_SECRET_KEY']}
    base = os.environ.get('ALPACA_DATA_URL', 'https://data.alpaca.markets')
    url = base.rstrip('/') + path + '?' + urllib.parse.urlencode(query)
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=60) as response:
        return json.load(response)


def fetch(symbols, out):
    bars = {s: [] for s in symbols}
    token, pages = None, 0
    while True:
        query = {'symbols': ','.join(symbols), 'timeframe': '1Day', 'feed': 'sip', 'adjustment': 'all',
                 'start': START, 'end': END, 'limit': 10000, 'sort': 'asc'}
        if token:
            query['page_token'] = token
        payload = get('/v2/stocks/bars', query)
        pages += 1
        for s, rows in payload.get('bars', {}).items():
            bars[s].extend({'t': r['t'][:10], 'c': r['c']} for r in rows)
        token = payload.get('next_page_token')
        if not token:
            break
    source = {'start': START, 'end': END, 'pages': pages, 'adjustment': 'all',
              'fetched_utc': dt.datetime.now(dt.timezone.utc).isoformat(), 'bars': bars}
    with gzip.open(out / 'daily.json.gz', 'wt') as handle:
        json.dump(source, handle)
    return source


def block_lower(values, block=HOLD, draws=4000, seed=13):
    rng = random.Random(seed)
    n, means = len(values), []
    for _ in range(draws):
        sample = []
        while len(sample) < n:
            s = rng.randrange(n - block + 1)
            sample.extend(values[s:s + block])
        means.append(statistics.mean(sample[:n]))
    means.sort()
    return means[int(0.025 * draws)], means[int(0.975 * draws) - 1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--replay', action='store_true')
    args = parser.parse_args()
    freeze = json.loads(FREEZE.read_text())
    basket = freeze['rule']['basket']
    symbols = basket + [freeze['rule']['benchmark']]
    args.out.mkdir(parents=True, exist_ok=True)
    if args.replay:
        with gzip.open(args.out / 'daily.json.gz', 'rt') as handle:
            source = json.load(handle)
    else:
        source = fetch(symbols, args.out)

    closes = {s: {r['t']: r['c'] for r in rows} for s, rows in source['bars'].items()}
    coverage = {s: [min(c), max(c), len(c)] if c else None for s, c in closes.items()}
    days = sorted(set.intersection(*(set(c) for c in closes.values())))

    # One record per possible decision day i: excess return of the pick over QQQ for days i..i+HOLD.
    records = []
    for i in range(HOLD, len(days) - HOLD):
        d0, d1, d2 = days[i - HOLD], days[i], days[i + HOLD]
        back = {s: closes[s][d1] / closes[s][d0] - 1 for s in symbols}
        rel = {s: back[s] - back['QQQ'] for s in basket}
        worst = sorted(basket, key=lambda s: (rel[s], s))[0]
        pick = worst if back[worst] < 0 and rel[worst] < 0 else None
        fwd = {s: closes[s][d2] / closes[s][d1] - 1 for s in symbols}
        basket_fwd = statistics.mean(fwd[s] for s in basket)
        records.append({'date': d1, 'pick': pick,
                        'basket_excess': basket_fwd - fwd['QQQ'],
                        'pick_vs_basket': (fwd[pick] - basket_fwd) if pick else None,
                        'gross': fwd[pick] if pick else 0.0,
                        'excess': (fwd[pick] - fwd['QQQ']) if pick else -fwd['QQQ'],
                        'traded': pick is not None})

    def stats(rows):
        traded = [r for r in rows if r['traded']]
        if not traded:
            return {'trades': 0}
        ex = [r['excess'] * 10000 for r in traded]
        return {'trades': len(traded), 'cash_periods': len(rows) - len(traded),
                'mean_gross_bps': round(statistics.mean(r['gross'] * 10000 for r in traded), 2),
                'mean_excess_bps': round(statistics.mean(ex), 2),
                'positive_excess': sum(1 for v in ex if v > 0)}

    offsets = {k: stats(records[k::HOLD]) for k in range(HOLD)}
    primary = offsets[0]
    traded_series = [r['excess'] * 10000 for r in records if r['traded']]
    low, high = block_lower(traded_series)
    half = len(records) // 2
    halves = [stats(records[:half][0::HOLD]), stats(records[half:][(HOLD - half % HOLD) % HOLD::HOLD])]
    overlapping_halves = [round(statistics.mean(r['excess'] * 10000 for r in part if r['traded']), 2)
                          for part in (records[:half], records[half:])]
    by_year = {}
    for r in records[0::HOLD]:
        if r['traded']:
            by_year.setdefault(r['date'][:4], []).append(r['excess'] * 10000)
    # Survivorship control (reported, not part of the frozen criterion): the basket is today's
    # megacaps, so holding all seven may beat QQQ with no selection at all. The selection edge is
    # the pick's return over the equal-weight basket.
    vs_basket = [r['pick_vs_basket'] * 10000 for r in records if r['traded']]
    vb_low, vb_high = block_lower(vs_basket)
    vb_halves = [round(statistics.mean(r['pick_vs_basket'] * 10000 for r in part if r['traded']), 2)
                 for part in (records[:half], records[half:])]
    control = {
        'basket_minus_qqq_bps_mean': round(statistics.mean(r['basket_excess'] * 10000 for r in records), 2),
        'pick_minus_basket_bps_overlapping': {'mean': round(statistics.mean(vs_basket), 2),
                                              'interval': [round(vb_low, 2), round(vb_high, 2)],
                                              'halves': vb_halves},
        'pick_minus_basket_bps_offset0': round(statistics.mean(
            r['pick_vs_basket'] * 10000 for r in records[0::HOLD] if r['traded']), 2),
    }
    checks = {
        'mean_excess_non_overlapping_gt_hurdle': primary['mean_excess_bps'] > HURDLE_BPS,
        'block_bootstrap_lower_gt_0': low > 0,
        'both_halves_positive': all(h.get('mean_excess_bps', -1) > 0 for h in halves),
    }
    result = {
        'freeze': str(FREEZE.relative_to(ROOT)), 'window': [days[0], days[-1]], 'sessions': len(days),
        'coverage': coverage, 'hurdle_bps': HURDLE_BPS,
        'primary_offset0': primary,
        'overlapping_excess_bps': {'mean': round(statistics.mean(traded_series), 2),
                                   'interval': [round(low, 2), round(high, 2)],
                                   'halves': overlapping_halves},
        'halves_non_overlapping': halves,
        'offsets_mean_excess_bps': {k: v.get('mean_excess_bps') for k, v in offsets.items()},
        'offsets_positive': sum(1 for v in offsets.values() if v.get('mean_excess_bps', 0) > 0),
        'by_year_mean_excess_bps': {y: [len(v), round(statistics.mean(v), 1)] for y, v in sorted(by_year.items())},
        'pick_counts': {s: sum(1 for r in records[0::HOLD] if r['pick'] == s) for s in basket},
        'checks': checks, 'passed': all(checks.values()),
        'survivorship_control': control,
    }
    (args.out / 'result.json').write_text(json.dumps(result, indent=1))
    print(json.dumps(result, indent=1))


if __name__ == '__main__':
    main()
