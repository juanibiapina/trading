# Initiative 7 — Small-cap monthly reversal (2026-10-20 18:00 CEST)

**Result: fail on all four checks.** From 2016-04 to 2025-09, buying last month's bottom decile of point-in-time dollar-volume ranks 1001–3000 and holding for one month trails the equal-weight band by **-1.27% a month** after 50 bps, with a 95% interval of [-2.08, -0.43]. Halves are -0.04 and -2.49, and stress (100 bps) is -1.77. Only 38 of 114 months are positive. Losers keep losing, so the sign is momentum rather than reversal, and the drag has grown every year since 2022 (-2.5%, -2.7%, -3.1%, -4.6%). The candidate is dropped.

## Test

Frozen in `docs/investigations/init7-smallcap-reversal-freeze.json` (16:15 UTC) and pushed in commit 2e3825e before any return was computed. Inputs: the cached October 12 monthly SIP bars (adjusted, 2016–2025, active and inactive symbols). No fetch.

- About 1,778 eligible names a month; the decile is about 178 names.
- 60 long-side exits (539 across the band) had no next-month bar and were scored at -30%. Dropping them instead gives -1.25%, so delistings do not drive the result.

## Descriptive (cannot rescue the test)

| Measure | % a month |
|---|---|
| Bottom decile, raw | -0.25 |
| Band benchmark, raw | +0.51 |
| Bottom decile net of 50 bps, against cash | -0.75 |
| Bottom minus top decile, gross | -0.07 |

**Bias found after the run:** the bars are adjusted for later reverse splits (TOP shows $541 in April 2023), so the frozen $5 floor admits names that traded below $5 at the time. With no floor, the excess is -0.59% [-1.56, +0.44] with halves +0.59 and -1.78. That is still a fail, so the conclusion does not depend on the floor.

## Decision

Drop small-cap monthly reversal. Combined with the megacap reversal (Oct 12) and the liquid fade (Oct 14), reversal is now rejected in three universes. No order, live rule, size or pulse timing changed.

## Verification

`python3 scripts/init7-smallcap-reversal.py` runs offline in about 7 seconds and writes `log/2026-10-20/init7-smallcap-reversal/result.json` and `rows.json.gz`. Spot check for June 2023: TOP's April to May signal is 46.05 / 541.05 - 1 = -91.49%, and its June return is 46.95 / 46.05 - 1 = +1.95%. BANL's are -79.87% and +6.46%. Both match the script.
