#!/usr/bin/env python3
"""Initiative 7 horizon study: which holding period in the megacap basket clears trading costs?

Reads the SIP 5-minute bars cached by init7-n1-history.py and, for each horizon, measures the
gross return per trade of:
  - momentum: N1's selector (best return relative to QQQ over a lookback equal to the horizon,
    bought only if both its own and its relative return are positive)
  - reversal: the mirror pick (worst relative return), to show whether the sign is stable
  - basket:   equal weight in the seven tradable names (no selection)
  - qqq:      QQQ alone
plus the mean absolute single-stock move, the upper bound on any selection edge.

The hurdle is the frozen base cost per round trip (2 x 6.645 bps = 13.29 bps) and the stress cost
(2 x 26.645 bps). Fills are mid proxies: the bar open at the entry/exit stamp. Means use every
overlapping start; the interval is a moving-block bootstrap with block length = horizon in
sessions (1 for intraday). The sample halves are reported to show stability.

Design-stage research only; it changes no frozen rule and feeds no prospective decision.

Usage:
  init7-horizon-study.py --bars log/2026-10-09/init7-n1-history/bars.json.gz --out DIR
"""
import argparse
import datetime as dt
import gzip
import json
import random
import statistics
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
DESIGN = ROOT / 'docs/investigations/init7-comparison-v1.json'
ET = ZoneInfo('America/New_York')
HALF_SPREAD_BPS = 1.29 / 2


def load(bars_path):
    with gzip.open(bars_path, 'rt') as handle:
        source = json.load(handle)
    index = {}
    for symbol, rows in source['bars'].items():
        for row in rows:
            stamp = dt.datetime.fromisoformat(row['t'].replace('Z', '+00:00')).astimezone(ET)
            index.setdefault(symbol, {})[(stamp.date(), stamp.strftime('%H:%M'))] = row
    days = [dt.date.fromisoformat(r['date']) for r in source['calendar']
            if r['open'] == '09:30' and r['close'] == '16:00']
    return index, days


def block_interval(values, block, draws=2000, seed=11):
    rng = random.Random(seed)
    n = len(values)
    block = max(1, min(block, n))
    starts = n - block + 1
    means = []
    for _ in range(draws):
        sample = []
        while len(sample) < n:
            s = rng.randrange(starts)
            sample.extend(values[s:s + block])
        means.append(statistics.mean(sample[:n]))
    means.sort()
    return means[int(0.025 * draws)], means[int(0.975 * draws) - 1]


def summarize(trades, block, hurdle):
    """trades: list of (period_index, gross_return) with None for no trade."""
    taken = [r for r in trades if r is not None]
    if not taken:
        return {'trades': 0}
    half = len(trades) // 2
    first = [r for r in trades[:half] if r is not None]
    second = [r for r in trades[half:] if r is not None]
    bps = [r * 10000 for r in taken]
    low, high = block_interval(bps, block)
    return {
        'trades': len(taken),
        'opportunities': len(trades),
        'mean_gross_bps': round(statistics.mean(bps), 2),
        'interval_bps': [round(low, 2), round(high, 2)],
        'first_half_bps': round(statistics.mean(first) * 10000, 2) if first else None,
        'second_half_bps': round(statistics.mean(second) * 10000, 2) if second else None,
        'hit_rate': round(sum(1 for r in taken if r > 0) / len(taken), 3),
        'clears_base_hurdle': statistics.mean(bps) > hurdle['base'],
        'interval_clears_base_hurdle': low > hurdle['base'],
        'mean_net_base_bps': round(statistics.mean(bps) - hurdle['base'], 2),
    }


def pick(returns, tradable, mirror=False):
    if any(returns.get(s) is None for s in tradable + ['QQQ']):
        return None
    rel = {s: returns[s] - returns['QQQ'] for s in tradable}
    if mirror:
        best = sorted(tradable, key=lambda s: (rel[s], s))[0]
        return best if returns[best] < 0 and rel[best] < 0 else None
    best = sorted(tradable, key=lambda s: (-rel[s], s))[0]
    return best if returns[best] > 0 and rel[best] > 0 else None


def legs(index, tradable, entries, signals):
    """entries: list of (entry_key, exit_key); signals: list of (from_key, to_key) on closes."""
    out = {'momentum': [], 'reversal': [], 'basket': [], 'qqq': [], 'abs_move': [],
           'momentum_vs_qqq': [], 'reversal_vs_qqq': [], 'picks_momentum': [], 'picks_reversal': []}
    for (entry, exit_), (sig_from, sig_to) in zip(entries, signals):
        def open_at(symbol, key):
            row = index[symbol].get(key)
            return row['o'] if row else None

        def close_at(symbol, key):
            row = index[symbol].get(key)
            return row['c'] if row else None

        fwd, back = {}, {}
        for s in tradable + ['QQQ']:
            a, b = open_at(s, entry), open_at(s, exit_)
            fwd[s] = b / a - 1 if a and b else None
            c0, c1 = close_at(s, sig_from), close_at(s, sig_to)
            back[s] = c1 / c0 - 1 if c0 and c1 else None
        if any(v is None for v in fwd.values()):
            for k in out:
                out[k].append(None)
            continue
        m, r = pick(back, tradable), pick(back, tradable, mirror=True)
        out['momentum'].append(fwd[m] if m else None)
        out['reversal'].append(fwd[r] if r else None)
        out['basket'].append(statistics.mean(fwd[s] for s in tradable))
        out['qqq'].append(fwd['QQQ'])
        out['abs_move'].append(statistics.mean(abs(fwd[s]) for s in tradable))
        out['momentum_vs_qqq'].append(fwd[m] - fwd['QQQ'] if m else None)
        out['reversal_vs_qqq'].append(fwd[r] - fwd['QQQ'] if r else None)
        out['picks_momentum'].append(m)
        out['picks_reversal'].append(r)
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bars', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    design = json.loads(DESIGN.read_text())
    tradable = design['tradable_candidates']
    fee = design['cost_accounting']['fee_bps_per_side_assumed']
    hurdle = {'base': 2 * (design['cost_accounting']['base_slippage_bps_per_side'] + fee + HALF_SPREAD_BPS),
              'stress': 2 * (design['cost_accounting']['stress_slippage_bps_per_side'] + fee + HALF_SPREAD_BPS)}
    index, days = load(args.bars)

    horizons = {}
    # Intraday: 1 hour (N1's own horizon, signal = prior hour) at the six N1 slots.
    slots = ['10:30', '11:30', '12:30', '13:30', '14:30', '15:30']
    entries, signals = [], []
    for d in days:
        for i, s in enumerate(slots):
            exit_ = slots[i + 1] if i + 1 < len(slots) else '15:55'
            hh, mm = map(int, s.split(':'))
            back = f'{hh - 1:02d}:{mm - 10:02d}' if mm >= 10 else None
            entries.append(((d, s), (d, exit_)))
            signals.append(((d, back), (d, f'{hh:02d}:{mm - 10:02d}')))
    horizons['1h_intraday'] = (legs(index, tradable, entries, signals), 6)
    # Rest of day: signal = open to 10:25 close, hold 10:30 -> 15:55.
    entries = [((d, '10:30'), (d, '15:55')) for d in days]
    signals = [((d, '09:30'), (d, '10:25')) for d in days]
    horizons['10:30_to_close'] = (legs(index, tradable, entries, signals), 1)
    # Overnight: signal = today's 09:30 bar close to 15:50 close; hold 15:55 -> next 09:30 open.
    entries = [((days[i], '15:55'), (days[i + 1], '09:30')) for i in range(len(days) - 1)]
    signals = [((days[i], '09:30'), (days[i], '15:50')) for i in range(len(days) - 1)]
    horizons['overnight'] = (legs(index, tradable, entries, signals), 1)
    # Multi-session: signal = return over the previous k sessions (15:50 closes); hold k sessions
    # from 15:55 to 15:55.
    for k in (1, 5, 20):
        entries, signals = [], []
        for i in range(k, len(days) - k):
            entries.append(((days[i], '15:55'), (days[i + k], '15:55')))
            signals.append(((days[i - k], '15:50'), (days[i], '15:50')))
        horizons[f'{k}d_close_to_close'] = (legs(index, tradable, entries, signals), k)

    result = {'sessions': len(days), 'first': str(days[0]), 'last': str(days[-1]),
              'hurdle_bps_round_trip': {k: round(v, 3) for k, v in hurdle.items()},
              'fill_proxy': 'bar open at entry and exit stamps (mid proxy), raw prices',
              'horizons': {}}
    for name, (out, block) in horizons.items():
        result['horizons'][name] = {leg: summarize(values, block, hurdle) for leg, values in out.items()
                                    if not leg.startswith('picks_')}
        for leg in ('momentum', 'reversal'):
            picks = [p for p in out[f'picks_{leg}'] if p]
            result['horizons'][name][leg]['pick_counts'] = {t: picks.count(t) for t in tradable}
            if block > 1:
                # Non-overlapping trades (one start every `block` sessions, offset 0) and their mean.
                values = [v for v in out[leg][::block] if v is not None]
                excess = [v for v in out[f'{leg}_vs_qqq'][::block] if v is not None]
                result['horizons'][name][leg]['non_overlapping'] = {
                    'trades': len(values),
                    'mean_gross_bps': round(statistics.mean(values) * 10000, 2) if values else None,
                    'mean_vs_qqq_bps': round(statistics.mean(excess) * 10000, 2) if excess else None,
                    'positive_vs_qqq': sum(1 for v in excess if v > 0)}
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / 'result.json').write_text(json.dumps(result, indent=1, default=str))
    print(f"sessions {result['sessions']} ({result['first']}..{result['last']}), "
          f"hurdle base {hurdle['base']:.2f} bps, stress {hurdle['stress']:.2f} bps per round trip")
    print(f"{'horizon':20} {'leg':9} {'n':>5} {'mean':>8} {'interval':>18} {'1st':>8} {'2nd':>8} {'hit':>6}")
    for name, legs_ in result['horizons'].items():
        for leg, s in legs_.items():
            if not s.get('trades'):
                continue
            print(f"{name:20} {leg:9} {s['trades']:5} {s['mean_gross_bps']:8.2f} "
                  f"{str(s['interval_bps']):>18} {s['first_half_bps']!s:>8} {s['second_half_bps']!s:>8} {s['hit_rate']:6}")


if __name__ == '__main__':
    main()
