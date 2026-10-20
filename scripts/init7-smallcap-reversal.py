#!/usr/bin/env python3
"""Initiative 7: small-cap monthly reversal test, frozen in
docs/investigations/init7-smallcap-reversal-freeze.json. Offline, cached bars only; no orders.

Usage: init7-smallcap-reversal.py [--out log/2026-10-20/init7-smallcap-reversal]
"""
import argparse
import gzip
import json
import random
import re
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / 'log/2026-10-12/init7-reversal20-pit'
FIRST, LAST = '2016-04', '2025-09'
BAND = (1001, 3000)
PRICE_FLOOR = 5.0
DECILE = 0.10
MISSING = -0.30
BASE, STRESS = 0.0050, 0.0100


def month_add(ym, k):
    y, m = map(int, ym.split('-'))
    m += k
    y, m = y + (m - 1) // 12, (m - 1) % 12 + 1
    return f'{y:04d}-{m:02d}'


def load(path):
    with gzip.open(path, 'rt') as handle:
        return json.load(handle)


def boot_low(values, draws=4000, seed=13):
    rng = random.Random(seed)
    n = len(values)
    means = sorted(statistics.mean(rng.choice(values) for _ in range(n)) for _ in range(draws))
    return means[int(0.025 * draws)], means[int(0.975 * draws) - 1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default=str(ROOT / 'log/2026-10-20/init7-smallcap-reversal'))
    args = ap.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    monthly = load(CACHE / 'monthly.json.gz')
    allowed = set(load(CACHE / 'universe.json.gz')['alpaca'])
    keep = lambda s: s in allowed and '.' not in s and not (len(s) == 5 and s[-1] in 'UWR')

    bars, seen = {}, set()
    for s, rows in sorted(monthly.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        if not keep(s):
            continue
        for r in rows:
            if not r.get('v') or not r.get('vw') or not r.get('c'):
                continue
            key = (r['t'][:7], r['v'])
            if key in seen:
                continue
            seen.add(key)
            bars.setdefault(s, {})[r['t'][:7]] = r

    months, rows = [], []
    m = FIRST
    while m <= LAST:
        prior = [month_add(m, -k) for k in (1, 2, 3)]
        score = {s: sum(b[p]['v'] * b[p]['vw'] for p in prior)
                 for s, b in bars.items() if all(p in b for p in prior)}
        ranked = sorted(score, key=lambda s: (-score[s], s))[BAND[0] - 1:BAND[1]]
        p1, p2 = prior[0], prior[1]
        elig = [s for s in ranked if bars[s][p1]['c'] >= PRICE_FLOOR]
        sig = {s: bars[s][p1]['c'] / bars[s][p2]['c'] - 1 for s in elig}
        fwd, missing = {}, set()
        for s in elig:
            if m in bars[s]:
                fwd[s] = bars[s][m]['c'] / bars[s][p1]['c'] - 1
            else:
                fwd[s], _ = MISSING, missing.add(s)
        k = max(1, int(round(DECILE * len(elig))))
        order = sorted(elig, key=lambda s: (sig[s], s))
        low, high = order[:k], order[-k:]
        bench = statistics.mean(fwd.values())
        long_raw = statistics.mean(fwd[s] for s in low)
        long_nomiss = [fwd[s] for s in low if s not in missing]
        bench_nomiss = [fwd[s] for s in elig if s not in missing]
        months.append(m)
        rows.append({'month': m, 'n_eligible': len(elig), 'k': k, 'missing_long': sum(s in missing for s in low),
                     'missing_all': len(missing), 'long_raw': long_raw, 'bench': bench,
                     'excess_base': long_raw - bench - BASE, 'excess_stress': long_raw - bench - STRESS,
                     'excess_base_nomiss': statistics.mean(long_nomiss) - statistics.mean(bench_nomiss) - BASE,
                     'long_short': long_raw - statistics.mean(fwd[s] for s in high),
                     'worst5': [[s, round(sig[s], 4), round(fwd[s], 4)] for s in low[:5]]})
        m = month_add(m, 1)

    ex = [r['excess_base'] for r in rows]
    half = len(rows) // 2
    h1, h2 = statistics.mean(ex[:half]), statistics.mean(ex[half:])
    lo, hi = boot_low(ex)
    stress = statistics.mean(r['excess_stress'] for r in rows)
    checks = {'mean_excess_base_gt_0': statistics.mean(ex) > 0, 'bootstrap_95_lower_gt_0': lo > 0,
              'both_halves_gt_0': h1 > 0 and h2 > 0, 'stress_mean_gt_0': stress > 0}
    pct = lambda v: round(100 * v, 3)
    by_year = {}
    for r in rows:
        by_year.setdefault(r['month'][:4], []).append(r['excess_base'])
    result = {
        'freeze': 'docs/investigations/init7-smallcap-reversal-freeze.json', 'months': len(rows),
        'first': months[0], 'last': months[-1],
        'mean_eligible': round(statistics.mean(r['n_eligible'] for r in rows), 1),
        'mean_excess_base_pct': pct(statistics.mean(ex)), 'interval_95_pct': [pct(lo), pct(hi)],
        'halves_pct': [pct(h1), pct(h2)], 'mean_excess_stress_pct': pct(stress),
        'positive_months': sum(v > 0 for v in ex), 'checks': checks, 'passed': all(checks.values()),
        'descriptive': {
            'long_raw_mean_pct': pct(statistics.mean(r['long_raw'] for r in rows)),
            'bench_mean_pct': pct(statistics.mean(r['bench'] for r in rows)),
            'long_raw_net_base_mean_pct': pct(statistics.mean(r['long_raw'] - BASE for r in rows)),
            'excess_base_missing_dropped_pct': pct(statistics.mean(r['excess_base_nomiss'] for r in rows)),
            'long_short_gross_pct': pct(statistics.mean(r['long_short'] for r in rows)),
            'missing_long_total': sum(r['missing_long'] for r in rows),
            'missing_all_total': sum(r['missing_all'] for r in rows),
            'excess_base_by_year_pct': {y: pct(statistics.mean(v)) for y, v in sorted(by_year.items())},
        },
    }
    (out / 'result.json').write_text(json.dumps(result, indent=2) + '\n')
    with gzip.open(out / 'rows.json.gz', 'wt') as handle:
        json.dump(rows, handle)
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
