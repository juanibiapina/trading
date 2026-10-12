#!/usr/bin/env python3
"""Point-in-time basket test of the frozen Initiative 7 20-session reversal rule.

The basket definition and pass criterion are frozen in
docs/investigations/init7-reversal20-pit-freeze.json. Each decision day's basket is the seven
US-listed stocks with the highest SIP dollar volume over the prior three complete months, from a
universe that includes delisted names. Signal, selection and hold follow the parent freeze.

Design-stage research only; no order, live rule or prospective decision depends on it.

Usage:
  init7-reversal20-pit.py --out DIR            # fetch universe, monthly and daily bars, then evaluate
  init7-reversal20-pit.py --out DIR --replay   # evaluate cached inputs
"""
import argparse
import csv
import datetime as dt
import gzip
import io
import json
import os
import random
import re
import statistics
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FREEZE = ROOT / 'docs/investigations/init7-reversal20-pit-freeze.json'
PARENT = ROOT / 'docs/investigations/init7-reversal20-freeze.json'
SP500_URL = 'https://raw.githubusercontent.com/fja05680/sp500/master/sp500_ticker_start_end.csv'
HURDLE_BPS = 13.29
START, END = '2016-01-01', '2025-09-30'
MONTHLY_START = '2015-10-01'
HOLD, SIZE = 20, 7
EXCHANGES = {'NASDAQ', 'NYSE', 'AMEX'}
FUND = re.compile(r'\b(ETF|ETN|Fund|Trust|iShares|SPDR|ProShares|Direxion|Invesco|Vanguard|Schwab|Portfolio|Index)\b', re.I)
FOLD = {'GOOG': 'GOOGL', 'BRK.A': 'BRK.B', 'FOX': 'FOXA', 'NWS': 'NWSA'}


def headers():
    return {'APCA-API-KEY-ID': os.environ['ALPACA_API_KEY'],
            'APCA-API-SECRET-KEY': os.environ['ALPACA_SECRET_KEY']}


def get_json(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers()), timeout=120) as response:
        return json.load(response)


def universe():
    assets = []
    for status in ('active', 'inactive'):
        assets += get_json('https://paper-api.alpaca.markets/v2/assets?asset_class=us_equity&status=' + status)
    alpaca = sorted({a['symbol'] for a in assets
                     if a['exchange'] in EXCHANGES and not FUND.search(a.get('name') or '')
                     and re.fullmatch(r'[A-Z]+(\.[A-Z])?', a['symbol'])})
    with urllib.request.urlopen(SP500_URL, timeout=60) as response:
        rows = list(csv.DictReader(io.StringIO(response.read().decode())))
    sp500 = sorted({r['ticker'] for r in rows if not r['end_date'] or r['end_date'] >= START})
    return {'alpaca': alpaca, 'sp500_since_2016': sp500, 'fetched_utc': dt.datetime.now(dt.timezone.utc).isoformat()}


def bars(symbols, timeframe, start, end, fields, batch=200):
    out = {}
    base = os.environ.get('ALPACA_DATA_URL', 'https://data.alpaca.markets').rstrip('/')
    pages = 0
    for k in range(0, len(symbols), batch):
        chunk, token = symbols[k:k + batch], None
        while True:
            query = {'symbols': ','.join(chunk), 'timeframe': timeframe, 'feed': 'sip', 'adjustment': 'all',
                     'start': start, 'end': end, 'limit': 10000, 'sort': 'asc'}
            if token:
                query['page_token'] = token
            payload = get_json(base + '/v2/stocks/bars?' + urllib.parse.urlencode(query))
            pages += 1
            for s, rows in (payload.get('bars') or {}).items():
                out.setdefault(s, []).extend({f: (r['t'][:10] if f == 't' else r.get(f)) for f in fields} for r in rows)
            token = payload.get('next_page_token')
            if not token:
                break
    return out, pages


def save(path, data):
    with gzip.open(path, 'wt') as handle:
        json.dump(data, handle)


def load(path):
    with gzip.open(path, 'rt') as handle:
        return json.load(handle)


def interval(values, block=HOLD, draws=4000, seed=13):
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


def month_add(ym, k):
    y, m = map(int, ym.split('-'))
    m += k
    y, m = y + (m - 1) // 12, (m - 1) % 12 + 1
    return f'{y:04d}-{m:02d}'


def rankings(monthly):
    """Top SIZE names per decision month by dollar volume over the three prior complete months."""
    # Same company under two symbols (e.g. FB and META before the 2022 rename) shows the same volume
    # with different dividend adjustment, so duplicates match on volume; the longer history wins.
    dv, seen = {}, {}
    for s, rows in sorted(monthly.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        for r in rows:
            if not r.get('v') or not r.get('vw'):
                continue
            ym = r['t'][:7]
            key = (ym, r['v'])
            if key in seen:
                continue
            seen[key] = s
            dv.setdefault(ym, {})[FOLD.get(s, s)] = dv.get(ym, {}).get(FOLD.get(s, s), 0) + r['v'] * r['vw']
    top = {}
    month = START[:7]
    while month <= END[:7]:
        prior = [month_add(month, -k) for k in (1, 2, 3)]
        # SIP history starts 2016-01, so the first decision month with three complete months is 2016-04.
        names = set.intersection(*(set(dv.get(p, {})) for p in prior))
        score = {s: sum(dv[p][s] for p in prior) for s in names}
        top[month] = sorted(score, key=lambda s: (-score[s], s))[:SIZE]
        month = month_add(month, 1)
    return top


def evaluate(top, daily):
    closes = {s: {r['t']: r['c'] for r in rows} for s, rows in daily.items()}
    days = sorted(closes['QQQ'])
    dates_by_symbol = {s: sorted(c) for s, c in closes.items()}

    def close_on_or_before(s, d):
        ds = dates_by_symbol.get(s, [])
        lo, hi = 0, len(ds)
        while lo < hi:
            mid = (lo + hi) // 2
            if ds[mid] <= d:
                lo = mid + 1
            else:
                hi = mid
        return (ds[lo - 1], closes[s][ds[lo - 1]]) if lo else (None, None)

    records, dropped, stale = [], 0, 0
    for i in range(HOLD, len(days) - HOLD):
        d0, d1, d2 = days[i - HOLD], days[i], days[i + HOLD]
        if not top[d1[:7]]:
            continue
        members = [s for s in top[d1[:7]] if d0 in closes.get(s, {}) and d1 in closes.get(s, {})]
        dropped += SIZE - len(members)
        back = {s: closes[s][d1] / closes[s][d0] - 1 for s in members}
        qqq_back = closes['QQQ'][d1] / closes['QQQ'][d0] - 1
        rel = {s: back[s] - qqq_back for s in members}
        worst = sorted(members, key=lambda s: (rel[s], s))[0]
        pick = worst if back[worst] < 0 and rel[worst] < 0 else None
        fwd = {}
        for s in members:
            when, price = close_on_or_before(s, d2)
            stale += when != d2
            fwd[s] = price / closes[s][d1] - 1
        qqq_fwd = closes['QQQ'][d2] / closes['QQQ'][d1] - 1
        basket_fwd = statistics.mean(fwd.values())
        records.append({'date': d1, 'basket': members, 'pick': pick, 'traded': pick is not None,
                        'gross': fwd[pick] if pick else 0.0,
                        'excess': (fwd[pick] - qqq_fwd) if pick else -qqq_fwd,
                        'vs_basket': (fwd[pick] - basket_fwd) if pick else None,
                        'basket_excess': basket_fwd - qqq_fwd})
    return days, records, dropped, stale


def criterion(records, key):
    half = len(records) // 2
    primary = [r[key] * 10000 for r in records[0::HOLD] if r['traded']]
    overlapping = [r[key] * 10000 for r in records if r['traded']]
    low, high = interval(overlapping)
    halves = [[r[key] * 10000 for r in part if r['traded']]
              for part in (records[:half][0::HOLD], records[half:][(HOLD - half % HOLD) % HOLD::HOLD])]
    checks = {'mean_non_overlapping_gt_hurdle': statistics.mean(primary) > HURDLE_BPS,
              'block_bootstrap_lower_gt_0': low > 0,
              'both_halves_positive': all(h and statistics.mean(h) > 0 for h in halves)}
    offsets = [statistics.mean(r[key] * 10000 for r in records[k::HOLD] if r['traded']) for k in range(HOLD)]
    return {'trades_non_overlapping': len(primary), 'mean_bps': round(statistics.mean(primary), 2),
            'positive': sum(1 for v in primary if v > 0),
            'overlapping_mean_bps': round(statistics.mean(overlapping), 2),
            'interval_bps': [round(low, 2), round(high, 2)],
            'halves_bps': [round(statistics.mean(h), 2) if h else None for h in halves],
            'offsets_positive': sum(1 for v in offsets if v > 0),
            'checks': checks, 'passed': all(checks.values())}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--replay', action='store_true')
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    parent = json.loads(PARENT.read_text())
    if args.replay:
        uni = load(args.out / 'universe.json.gz')
        monthly = load(args.out / 'monthly.json.gz')
        daily = load(args.out / 'daily.json.gz')
    else:
        uni = universe()
        save(args.out / 'universe.json.gz', uni)
        symbols = sorted(set(uni['alpaca']) | set(uni['sp500_since_2016']))
        monthly, pages = bars(symbols, '1Month', MONTHLY_START, END, ('t', 'c', 'v', 'vw'))
        save(args.out / 'monthly.json.gz', monthly)
        members = sorted({s for names in rankings(monthly).values() for s in names} | {'QQQ'})
        daily, _ = bars(members, '1Day', START, END, ('t', 'c'), batch=50)
        save(args.out / 'daily.json.gz', daily)

    top = rankings(monthly)
    days, records, dropped, stale = evaluate(top, daily)
    original = set(parent['rule']['basket'])
    traded = [r for r in records[0::HOLD] if r['traded']]
    members = sorted({s for r in records for s in r['basket']})
    vs_qqq, vs_basket = criterion(records, 'excess'), criterion(records, 'vs_basket')
    by_year = {}
    for r in traded:
        by_year.setdefault(r['date'][:4], []).append(r['excess'] * 10000)
    result = {
        'freeze': str(FREEZE.relative_to(ROOT)), 'window': [days[0], days[-1]], 'sessions': len(days),
        'universe_size': len(set(uni['alpaca']) | set(uni['sp500_since_2016'])),
        'symbols_with_monthly_bars': len(monthly),
        'basket_members_ever': members,
        'member_share_of_days': {s: round(sum(s in r['basket'] for r in records) / len(records), 3) for s in members},
        'original_seven_share_of_slots': round(sum(s in original for r in records for s in r['basket'])
                                               / sum(len(r['basket']) for r in records), 3),
        'basket_by_year_start': {m: top[m] for m in sorted(top) if m.endswith('-01')},
        'dropped_member_slots': dropped, 'stale_forward_prices': stale,
        'basket_minus_qqq_bps_mean': round(statistics.mean(r['basket_excess'] * 10000 for r in records), 2),
        'vs_qqq': vs_qqq, 'vs_basket': vs_basket,
        'pick_counts': {s: n for s, n in sorted(
            ((s, sum(1 for r in traded if r['pick'] == s)) for s in members), key=lambda x: -x[1]) if n},
        'by_year_excess_bps': {y: [len(v), round(statistics.mean(v), 1)] for y, v in sorted(by_year.items())},
        'passed': vs_qqq['passed'] and vs_basket['passed'],
    }
    (args.out / 'result.json').write_text(json.dumps(result, indent=1))
    print(json.dumps(result, indent=1))


if __name__ == '__main__':
    main()
