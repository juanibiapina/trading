# Initiative 7: late-entry micro-cap census (2026-10-15)

Freeze: [init7-microcap-late-census-freeze.json](init7-microcap-late-census-freeze.json) (16:05 UTC, before any 17:00–18:30 ET bar or quote was fetched). Script: [init7-microcap-late-census.py](../../scripts/init7-microcap-late-census.py). Data and result: `log/2026-10-15/init7-microcap-late/` (`result.json`, `events.json.gz`; `--replay` reproduces it).

## Verdict

**Fails in all eight cells.** Micro-cap AH ignitions that were not 17:00 events, bought at the SIP ask at the first of the 17:30, 18:00 or 18:30 ET scans where they pass the live gate, lose money at both exits. Every interval lies entirely below zero. With the 17:00 census, the whole live entry window (17:00–18:30 ET) has now failed a frozen test, so the proposal to stop or replace AH→PM is unconditional.

| Cell | n | 04:30 bid | interval | halves | open | interval |
|---|---:|---:|---|---|---:|---|
| all | 604 | **-3.91%** | [-5.99, -1.44] | -5.99 / -1.86 | **-5.61%** | [-8.12, -2.95] |
| build | 326 | -5.28% | [-8.16, -1.93] | -7.26 / -3.29 | -7.30% | [-10.63, -3.02] |
| fresh | 521 | -3.52% | [-5.78, -0.95] | -6.13 / -0.91 | -5.40% | [-7.88, -2.41] |
| build∩fresh | 280 | -4.44% | [-7.58, -1.18] | -6.95 / -1.92 | -6.58% | [-9.97, -2.13] |

Intervals are date-clustered bootstraps with a Bonferroni tail of 0.025/8.

## Detail

- **Counts:** 609 events, 604 scored (4 had no entry quote, 1 was a split). 10 exits used the open fallback.
- **Shape:** the win rate is 27% and the median trade loses 6.4%. With +100 bps stress the mean is -4.91% at 04:30.
- **Before costs:** mid to mid loses -2.24% at 04:30 [-4.33, +0.25] and -4.60% at the open [-7.12, -1.92]. The median entry spread is 74 bps.
- **By scan (04:30):** 17:30 -3.81% (226), 18:00 -3.28% (203), 18:30 -4.77% (175).
- **By move (04:30):** 10–25% -2.01%, 25–50% -6.53%, 50–150% -8.43%. Bigger moves fade harder. No price or dollar-volume bucket is positive.
- **Hand check:** CIGL 2025-10-01: close $2.57, ask $4.93 at 17:29:59 ET, 04:30 bid $4.39, -10.95%.

## Descriptive only (cannot rescue the failed pass)

- **Real entries:** the census scores 32 of the 44 real entries that the 17:00 census missed. They return +3.80% at 04:30 (95% interval -3.72 to +12.46; median -3.21%; 12 of 32 win). Without the best trade (BAOS +85%) the mean is +1.18%. Unselected late events on the same dates lose -8.08% (51). The live agent's late picks beat the pool, but that rests on one trade, and its early picks (45 trades, -3.45%) did not. All 89 real entries together still model negative.
- **Short side:** the long loss is larger than the spread, so the mirror trade is the next candidate. Only 161 of the 671 census names (201 of 1,103 events, both censuses) are easy to borrow on Alpaca today. On the 100 late events among them, mid to mid falls -4.01% by 04:30 and -4.28% by the open (median spread 74 bps). This is in-sample and uses today's borrow flags (a look-ahead), so it only motivates a frozen test on the prior year.

## Limits

Consecutive half-hour checkpoints approximate the live two-scan gate. The census has no catalyst grading and no first-bar-spike or spike-fade skips. Survivorship is limited to assets Alpaca still lists. It models no borrow, fees or partial fills, and it ignores quoted size.
