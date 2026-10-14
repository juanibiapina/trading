#!/usr/bin/env python3
"""Initiative 7: out-of-sample fade test, per docs/investigations/init7-liquid-fade-oos-freeze.json.

Shorts liquid after-hours up movers at the D+1 open and covers at the D+20 close, net of the equal-weight
point-in-time top 1000 and a 10 bps round trip, on October 2024 - September 2025.

Prerequisites (run from the repo root):
  python3 scripts/init7-liquid-ah-census.py --out log/2026-10-14/init7-liquid-fade-oos/census \
      --first 2024-10-01 --last 2025-09-30 --bars-only
  python3 scripts/init7-liquid-drift.py --census $PWD/log/2026-10-14/init7-liquid-fade-oos/census \
      --out $PWD/log/2026-10-14/init7-liquid-fade-oos --first 2024-10-01 --last 2025-09-30 --tail 0.025
Then:
  python3 scripts/init7-liquid-fade-oos.py
Writes fade-result.json next to the drift rows.
"""
import gzip
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'log/2026-10-14/init7-liquid-fade-oos'
spec = importlib.util.spec_from_file_location('drift', ROOT / 'scripts/init7-liquid-drift.py')
drift = importlib.util.module_from_spec(spec)
spec.loader.exec_module(drift)
drift.TAIL = 0.025                      # single frozen cell, two-sided 95%

cells = json.load(gzip.open(OUT / 'rows.json.gz', 'rt'))
# drift rows hold (raw - bench) - cost for up movers; the fade is the opposite side, also paying the cost
rows = [dict(r, fade=-(r['raw'] - r['bench']) - drift.COST) for r in cells['long_open_20']]
drops = json.loads((OUT / 'result.json').read_text())
result = {
    'freeze': 'docs/investigations/init7-liquid-fade-oos-freeze.json',
    'cell': 'short up movers, open D+1 to close D+20',
    'window': drops['window'],
    'base': drift.summary(rows, 'fade'),
    'stress': drift.summary(rows, 'fade', drift.STRESS),
    'raw_event_mean_pct': round(sum(r['raw'] for r in rows) / len(rows) * 100, 3),
    'bench_mean_pct': round(sum(r['bench'] for r in rows) / len(rows) * 100, 3),
    'dropped': {'split': drops['counts']['split'], 'missing_bars': drops['missing_bars']['long_open_20'],
                'truncated': drops['truncated']['long_open_20']},
    'by_move': {label: drift.summary([r for r in rows if lo <= r['move'] < hi], 'fade')
                for label, lo, hi in (('3-6%', .03, .06), ('6-10%', .06, .10), ('>10%', .10, 99))},
}
result['passed'] = result['base'].get('passed', False)
(OUT / 'fade-result.json').write_text(json.dumps(result, indent=1))
json.dump({k: result[k] for k in ('base', 'passed')}, sys.stdout)
print()
