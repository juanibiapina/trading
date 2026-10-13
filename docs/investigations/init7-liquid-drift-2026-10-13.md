# Initiative 7 — Multi-day drift after liquid AH ignitions (2026-10-13 18:00 CEST)

**Result: fail. No cell passes; every base mean is negative.** Liquid after-hours ignitions bought (or shorted) in the regular session do not beat the equal-weight top 1,000 over 5 or 20 sessions. The liquid-event lane is closed.

## Test

Frozen in `docs/investigations/init7-liquid-drift-freeze.json` before any multi-day or benchmark return was computed. Inputs are the October 13 census cache (`log/2026-10-13/init7-liquid-ah-census`, daily SIP bars through 2026-10-09); no new fetch.

- **Events:** all 1,420 ignitions from the census rule (783 up movers, 637 down movers, Oct 2025 – Sep 2026). The 17:00 quote is not needed, so the 62 events the census dropped for lack of a quote are included. No splits.
- **Entries:** next-session open or next-session close (split-adjusted). **Holds:** 5 and 20 sessions.
- **Unit:** event return minus the equal-weight return of the point-in-time top 1,000 over the same window, minus 10 bps round trip (sign flipped for shorts).
- **Pass:** mean > 0, lower bound of a 99.375% month-clustered bootstrap interval (Bonferroni over 8 cells) > 0, both chronological halves > 0.

## Results (net of benchmark and cost, % per trade)

| Cell | n | Mean | Interval | Halves | Win rate | Event raw | Benchmark |
|---|---|---|---|---|---|---|---|
| Long, open, 5 | 782 | -0.65 | [-3.25, +0.92] | +0.30 / -1.59 | 46% | -0.21 | +0.34 |
| Long, open, 20 | 766 | -1.76 | [-8.10, +3.55] | -0.59 / -2.92 | 41% | -1.37 | +0.29 |
| Long, close, 5 | 782 | -0.53 | [-4.63, +1.42] | +0.74 / -1.81 | 46% | +0.10 | +0.53 |
| Long, close, 20 | 766 | -1.16 | [-8.32, +4.28] | +0.23 / -2.55 | 44% | -0.51 | +0.55 |
| Short, open, 5 | 637 | -0.08 | [-1.52, +1.13] | +1.16 / -1.25 | 52% | +0.03 | +0.04 |
| Short, open, 20 | 632 | -0.55 | [-4.15, +2.97] | +1.95 / -2.94 | 50% | +0.15 | -0.31 |
| Short, close, 5 | 637 | -0.10 | [-1.66, +1.27] | +1.29 / -1.40 | 50% | -0.09 | -0.09 |
| Short, close, 20 | 630 | -0.34 | [-3.41, +2.68] | +1.67 / -2.28 | 50% | -0.13 | -0.37 |

Stress (+20 bps) lowers each mean by 0.20. Excluded: 16 long and 5–7 short events whose 20-session exit falls after 2026-10-09; one long event lacked bars.

**Reading:** the sign is the opposite of drift. Up movers lag the market by 1–2 points over 20 sessions, and down movers roughly keep pace with it. The intervals are wide (12 monthly clusters), so the reversal is not established either.

**Descriptive only (cannot rescue the test):** for the 20-session open entry, long 6–10% movers lose -5.1% [-11.1, -0.4] with both halves negative (n=195); shorting >10% down movers loses -2.9% [-5.9, +0.2], both halves negative (n=117). Both point to reversal after the event. This was found in the same sample, so it can only become a hypothesis for a different period.

## Decision

Close the liquid-event lane: liquid AH ignitions carry no tradable edge overnight (October 13 census) or over 5–20 sessions in the regular session (this test). No order, live rule, size or pulse timing changed.

**Next candidate (out of sample):** the fade. Frozen from this year's descriptive buckets, test on the prior year (October 2024 – September 2025): short up movers at the next open, hold 20 sessions, against the same benchmark and cost. It needs the census fetch rerun for that year (about 55 minutes).

## Verification

`python3 scripts/init7-liquid-drift.py` runs offline in about 65 seconds and writes `log/2026-10-13/init7-liquid-drift/result.json` and `rows.json.gz`. Spot check: USAR (2025-10-02) open on 2025-10-03 to close on 2025-10-09 is +19.09% in both the script and a hand computation. A first draft dropped benchmark returns beyond ±500% as bad data; the guard was not in the freeze, so it was removed, and the results are identical to three decimals.
