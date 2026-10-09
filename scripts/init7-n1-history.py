#!/usr/bin/env python3
"""Historical replay of the frozen Initiative 7 N1 rule (design-stage research).

Replays init7-comparison-v1's N1 selector on past SIP 5-minute bars and models
fills at the open of the 5-minute bar that starts at each slot (a mid proxy),
plus half the median NBBO spread measured for amendment A3 and the frozen
slippage/fee allowances. It answers two questions before the 20-session pilot
calendar is frozen: did N1 beat cash and QQQ over the past year, and how often
would a 20-session window pass the frozen promotion gate.

This is off-schedule development evidence. It never feeds a prospective
decision and does not change the frozen rule.

Usage:
  init7-n1-history.py --start 2025-10-01 --end 2026-10-08 --out DIR      # fetch + replay
  init7-n1-history.py --out DIR --replay                                  # replay cached bars
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
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
DESIGN = ROOT / 'docs/investigations/init7-comparison-v1.json'
ET = ZoneInfo('America/New_York')
HALF_SPREAD_BPS = 1.29 / 2  # median SIP NBBO spread on 64 archived books (amendment A3)


def get(base, path, query):
    headers = {'APCA-API-KEY-ID': os.environ['ALPACA_API_KEY'],
               'APCA-API-SECRET-KEY': os.environ['ALPACA_SECRET_KEY']}
    url = base.rstrip('/') + path + '?' + urllib.parse.urlencode(query)
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=60) as response:
        return json.load(response)


def fetch(design, start, end, out):
    trading = os.environ.get('ALPACA_BASE_URL', 'https://paper-api.alpaca.markets')
    data = os.environ.get('ALPACA_DATA_URL', 'https://data.alpaca.markets')
    calendar = get(trading, '/v2/calendar', {'start': start, 'end': end})
    bars = {symbol: [] for symbol in design['basket']}
    token = None
    pages = 0
    while True:
        query = {'symbols': ','.join(design['basket']), 'timeframe': '5Min', 'feed': 'sip',
                 'adjustment': 'raw', 'start': f'{start}T13:00:00Z', 'end': f'{end}T21:00:00Z',
                 'limit': 10000, 'sort': 'asc'}
        if token:
            query['page_token'] = token
        payload = get(data, '/v2/stocks/bars', query)
        pages += 1
        for symbol, rows in payload.get('bars', {}).items():
            bars[symbol].extend({'t': row['t'], 'o': row['o'], 'c': row['c']} for row in rows)
        token = payload.get('next_page_token')
        if not token:
            break
    source = {'start': start, 'end': end, 'pages': pages,
              'fetched_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
              'calendar': calendar, 'bars': bars}
    with gzip.open(out / 'bars.json.gz', 'wt') as handle:
        json.dump(source, handle)
    return source


def utc(day, hhmm):
    return dt.datetime.combine(day, dt.time.fromisoformat(hhmm), ET).astimezone(dt.timezone.utc)


def replay_session(design, day, index, costs):
    """Return per-arm net USD for $100 starting capital, or None if data is missing."""
    slot = dt.timedelta(minutes=5)
    opened = utc(day, '09:30')
    slots = [utc(day, value) for value in design['observation_times_et']]
    flatten = utc(day, design['future_pilot_execution']['final_flatten_et'])

    def price(symbol, start):
        bar = index[symbol].get(start)
        return bar['o'] if bar else None

    picks = []
    for decision in slots:
        cutoff = decision - dt.timedelta(minutes=design['request_buffer_minutes'])
        latest = opened + slot * (int((cutoff - opened) // slot) - 1)
        required = [latest - slot * i for i in reversed(range(design['required_consecutive_closes']))]
        returns = {}
        for symbol in design['basket']:
            closes = [index[symbol].get(stamp) for stamp in required]
            returns[symbol] = None if None in closes else closes[-1]['c'] / closes[0]['c'] - 1
        if None in returns.values():
            picks.append(None)
            continue
        market = returns['QQQ']
        ranked = sorted(design['tradable_candidates'], key=lambda s: (-(returns[s] - market), s))
        best = ranked[0]
        picks.append(best if returns[best] > 0 and returns[best] - market > 0 else None)

    result = {}
    for name, per_side_bps in costs.items():
        side = per_side_bps / 10000
        equity, trips, missing = 100.0, 0, False
        for i, pick in enumerate(picks):
            if not pick:
                continue
            exit_at = slots[i + 1] if i + 1 < len(slots) else flatten
            buy, sell = price(pick, slots[i]), price(pick, exit_at)
            if buy is None or sell is None:
                missing = True
                continue
            alloc = equity * design['future_pilot_capital']['maximum_equity_fraction_per_position']
            shares = alloc / (buy * (1 + side))
            equity += shares * sell * (1 - side) - alloc
            trips += 1
        q_buy, q_sell = price('QQQ', slots[0]), price('QQQ', flatten)
        if q_buy is None or q_sell is None:
            return None
        alloc = 100 * design['future_pilot_capital']['maximum_equity_fraction_per_position']
        qqq = alloc / (q_buy * (1 + side)) * q_sell * (1 - side) - alloc
        result[name] = {'n1': equity - 100, 'qqq': qqq, 'cash': 0.0, 'trips': trips, 'missing_fill': missing}
    result['picks'] = picks
    return result


def bootstrap_lower(values, draws=10000, seed=7):
    rng = random.Random(seed)
    n = len(values)
    means = sorted(sum(rng.choice(values) for _ in range(n)) / n for _ in range(draws))
    return means[int(0.025 * draws)], means[int(0.975 * draws) - 1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--start')
    parser.add_argument('--end')
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--replay', action='store_true')
    parser.add_argument('--window-step', type=int, default=5)
    args = parser.parse_args()
    design = json.loads(DESIGN.read_text())
    args.out.mkdir(parents=True, exist_ok=True)
    if args.replay:
        with gzip.open(args.out / 'bars.json.gz', 'rt') as handle:
            source = json.load(handle)
    else:
        source = fetch(design, args.start, args.end, args.out)

    index = {s: {dt.datetime.fromisoformat(b['t'].replace('Z', '+00:00')): b for b in rows}
             for s, rows in source['bars'].items()}
    fee = design['cost_accounting']['fee_bps_per_side_assumed']
    costs = {'base': design['cost_accounting']['base_slippage_bps_per_side'] + fee + HALF_SPREAD_BPS,
             'stress': design['cost_accounting']['stress_slippage_bps_per_side'] + fee + HALF_SPREAD_BPS,
             'zero_cost': 0.0}
    sessions, skipped = [], []
    for row in source['calendar']:
        day = dt.date.fromisoformat(row['date'])
        if row['open'] != '09:30' or row['close'] != '16:00':
            skipped.append({'date': row['date'], 'reason': 'half_day'})
            continue
        replay = replay_session(design, day, index, costs)
        if replay is None:
            skipped.append({'date': row['date'], 'reason': 'missing_bars'})
            continue
        sessions.append({'date': row['date'], **replay})

    summary = {'sessions': len(sessions), 'skipped': skipped, 'costs_bps_per_side': costs,
               'first': sessions[0]['date'], 'last': sessions[-1]['date']}
    selected = sum(1 for s in sessions for p in s['picks'] if p)
    summary['selected_observations'] = selected
    summary['observations'] = 6 * len(sessions)
    summary['pick_counts'] = {t: sum(1 for s in sessions for p in s['picks'] if p == t)
                              for t in design['tradable_candidates']}
    for name in costs:
        n1 = [s[name]['n1'] for s in sessions]
        qqq = [s[name]['qqq'] for s in sessions]
        diff_q = [a - b for a, b in zip(n1, qqq)]
        summary[name] = {
            'n1_mean_usd_per_session': statistics.mean(n1),
            'n1_total_usd': sum(n1),
            'n1_positive_sessions': sum(1 for v in n1 if v > 0),
            'qqq_mean_usd_per_session': statistics.mean(qqq),
            'n1_minus_qqq_mean': statistics.mean(diff_q),
            'n1_vs_cash_interval': bootstrap_lower(n1, draws=2000),
            'n1_vs_qqq_interval': bootstrap_lower(diff_q, draws=2000),
            'round_trips_per_session': statistics.mean(s[name]['trips'] for s in sessions),
        }
    # Rolling 20-session windows under the frozen promotion gate (N1 vs cash and QQQ, both cost scenarios).
    window = design['evaluation']['pilot_full_sessions']
    passes, total = 0, 0
    for start in range(0, len(sessions) - window + 1, args.window_step):
        chunk = sessions[start:start + window]
        ok = True
        for name in ('base', 'stress'):
            n1 = [s[name]['n1'] for s in chunk]
            diff = [s[name]['n1'] - s[name]['qqq'] for s in chunk]
            if sum(n1) <= 0 or sum(diff) <= 0 or bootstrap_lower(n1, 2000)[0] <= 0 or bootstrap_lower(diff, 2000)[0] <= 0:
                ok = False
                break
        passes += ok
        total += 1
    summary['rolling_20_session_gate'] = {'windows': total, 'step_sessions': args.window_step,
                                          'passed': passes,
                                          'note': 'A2/A1 legs and coverage gates not modeled; N1 vs cash and QQQ only.'}
    (args.out / 'sessions.json').write_text(json.dumps(sessions, indent=1, default=str))
    (args.out / 'result.json').write_text(json.dumps(summary, indent=1, default=str))
    print(json.dumps({k: v for k, v in summary.items() if k != 'skipped'}, indent=1, default=str))
    print('skipped:', len(skipped), sorted({s['reason'] for s in skipped}))


if __name__ == '__main__':
    main()
