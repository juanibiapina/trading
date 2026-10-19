# Initiative 3: take-profit power check on the census events (2026-10-19)

Frozen in `docs/investigations/init3-take-profit-census-freeze.json` (13:20 UTC) before any post-entry bar high was fetched. Script `scripts/init3-take-profit-census.py`, gob `XwA` (4.5 minutes, exit 0). Result: `log/2026-10-19/init3-take-profit-census/result.json`; rows in `rows.json.gz`.

## Question

Juan, Oct 15: "YYAI good entry, late exit." The October 16 replay on 103 live fills found +1.2 to +2.2 points from a resting limit, with intervals spanning zero. This run repeats it on the 872 prior-year micro-cap census events for more power.

## Result

Buy at the scan ask; baseline sells at the 04:30 ET bid (19 open fallbacks); limits fill if a 1-minute SIP high from the scan minute to 20:00 ET, or 04:00–04:29 ET, trades above them. Bonferroni over 3.

| Exit | Fill rate | Mean return | Interval | Paired gain vs 04:30 | Interval | Halves |
|---|---|---|---|---|---|---|
| 04:30 bid (live) | — | -3.47% | [-5.58, -0.95] | — | — | — |
| +10% limit | 44% | -2.50% | [-3.78, -1.35] | +0.97 | [-1.13, +2.58] | +1.51 / +0.43 |
| +15% limit | 33% | -2.53% | [-3.95, -1.29] | +0.95 | [-1.11, +2.48] | +1.06 / +0.84 |
| +20% limit | 25% | -2.53% | [-4.13, -0.95] | +0.95 | [-0.62, +2.22] | +0.96 / +0.93 |

No variant beats the 04:30 exit under the frozen rule, and none makes the long side profitable. Median peak after entry is +8.0%; the top decile peaks above +39%.

Spot check: HKD 2024-10-02, entry ask $5.29, 04:30 bid $4.20 (-20.6%), peak +13.4%, so only the +10% limit fills.

## Decision

`decision_if_fail`: no exit change; the take-profit line of Initiative 3 is closed. Both samples (103 live fills, 872 census events) agree on a gain of about one point, too small and too noisy to pass, and the strategy loses either way.
