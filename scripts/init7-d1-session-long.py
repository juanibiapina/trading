#!/usr/bin/env python3
"""Initiative 7: D+1 regular-session long on micro-cap AH movers, per docs/investigations/init7-d1-session-long-freeze.json.

Buy each short-fade scan event at the D+1 official open (+50 bps) and sell at the D+1 or D+2 close (-50 bps).
Uses only the daily bars and events cached by scripts/init7-microcap-short-fade.py; no fetch.

  init7-d1-session-long.py --out DIR
"""
import argparse
import importlib.util
import json
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location('lc', ROOT / 'scripts/init7-liquid-ah-census.py')
lc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lc)

FREEZE = ROOT / 'docs/investigations/init7-d1-session-long-freeze.json'
SRC = ROOT / 'log/2026-10-16/init7-short-fade'
BUY, SELL, STRESS = 1 + 50 / 1e4, 1 - 50 / 1e4, 0.01
EXITS, SUBSETS, TAIL = ('close1', 'close2'), ('all', 'gap_up'), 0.025 / 4


def rows():
    cal = [d['date'] for d in json.loads((SRC / 'calendar.json').read_text()) if d['close'] == '16:00']
    after = {a: b for a, b in zip(cal, cal[1:])}
    daily = {s: {r['t'][:10]: r for r in v} for s, v in lc.load(SRC / 'daily-raw.json.gz').items()}
    splitc = {s: {r['t'][:10]: r['c'] for r in v} for s, v in lc.load(SRC / 'daily-split.json.gz').items()}
    out, dropped = [], {'missing_bar': 0, 'split': 0}
    for e in lc.load(SRC / 'events.json.gz'):
        s, d0, d1 = e['symbol'], e['date'], e['next']
        d2 = after.get(d1)
        bars, sc = daily.get(s, {}), splitc.get(s, {})
        if not (d0 in bars and d1 in bars and d2 in bars and bars[d1]['o'] > 0):
            dropped['missing_bar'] += 1
            continue
        ratios = [bars[d]['c'] / sc[d] for d in (d0, d2) if sc.get(d)]
        if len(ratios) < 2 or abs(ratios[1] / ratios[0] - 1) > 0.01:
            dropped['split'] += 1
            continue
        o1, c1, c2 = bars[d1]['o'], bars[d1]['c'], bars[d2]['c']
        entry = o1 * BUY
        out.append({'key': e['key'], 'symbol': s, 'date': d0, 'etb': bool(e.get('etb')), 'move': e['move'],
                    'gap': o1 / e['close'] - 1, 'all': True, 'gap_up': o1 > e['close'],
                    'close1': c1 * SELL / entry - 1, 'close2': c2 * SELL / entry - 1,
                    'gross_close1': c1 / o1 - 1, 'gross_close2': c2 / o1 - 1,
                    'short_close1': 1 - c1 * BUY / (o1 * SELL)})
    return out, dropped


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', required=True)
    out = Path(ap.parse_args().out)
    out.mkdir(parents=True, exist_ok=True)
    data, dropped = rows()
    summ = lambda sub, k, stress=0.0: lc.summary(sub, k, stress, tail=TAIL)
    res = {'freeze': str(FREEZE.relative_to(ROOT)), 'events': 872, 'scored': len(data), 'dropped': dropped,
           'cells': {}, 'gross': {}, 'descriptive': {}}
    for sub in SUBSETS:
        rs = [r for r in data if r[sub]]
        for k in EXITS:
            res['cells'][f'{sub}/{k}'] = {'base': summ(rs, k), 'stress': summ(rs, k, STRESS)}
            res['gross'][f'{sub}/{k}'] = summ(rs, 'gross_' + k)
    desc = res['descriptive']
    desc['etb/close1'] = summ([r for r in data if r['etb']], 'close1')
    desc['etb/close2'] = summ([r for r in data if r['etb']], 'close2')
    for label, lo, hi in (('gap<0', -9, 0), ('gap0-20', 0, .2), ('gap20-50', .2, .5), ('gap>50', .5, 99)):
        desc[f'{label}/close1'] = summ([r for r in data if lo <= r['gap'] < hi], 'close1')
    desc['short_mirror/close1'] = summ(data, 'short_close1')
    desc['short_mirror_etb/close1'] = summ([r for r in data if r['etb']], 'short_close1')
    res['passed_cells'] = [c for c, v in res['cells'].items() if v['base'].get('passed')]
    res['passed'] = bool(res['passed_cells'])
    srt = sorted(data, key=lambda r: r['close1'])
    res['bottom5_close1'] = [(r['key'], round(r['close1'] * 100, 1)) for r in srt[:5]]
    res['top5_close1'] = [(r['key'], round(r['close1'] * 100, 1)) for r in srt[-5:]]
    lc.save(out / 'rows.json.gz', data)
    (out / 'result.json').write_text(json.dumps(res, indent=2) + '\n')
    print(json.dumps({k: res[k] for k in ('scored', 'dropped', 'cells', 'passed_cells')}, indent=1))


if __name__ == '__main__':
    main()
