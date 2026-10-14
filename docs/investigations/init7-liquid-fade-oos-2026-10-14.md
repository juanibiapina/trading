# Initiative 7 — Out-of-sample fade of liquid AH up movers (2026-10-14)

**Result: fails.** Shorting liquid after-hours up movers at the next open and covering 20 sessions later loses -0.56% per trade net of the benchmark and a 10 bps round trip, interval [-3.30, +2.65], halves +1.52 / -2.62 (n=578). The in-sample reversal from the October 13 drift test does not replicate on the prior year. Initiative 7 has no candidate left on liquid names.

## Freeze

`docs/investigations/init7-liquid-fade-oos-freeze.json`, written 2026-10-14 13:15 UTC before any bar for the window was fetched. One cell: short every up mover (move of at least +3% by 16:55 ET with the census volume spike) at the split-adjusted D+1 open, cover at the D+20 close. Net = -(event return - equal-weight top-1,000 return over the same days) - 10 bps. Month-clustered bootstrap, 4,000 draws, seed 13, two-sided 95%. Pass: mean > 0, lower bound > 0, both chronological halves > 0.

## Data

- Window: events dated 2024-10-01 to 2025-09-30, disjoint from the in-sample October 2025 – September 2026.
- Fetch: `scripts/init7-liquid-ah-census.py --first 2024-10-01 --last 2025-09-30 --bars-only` (gob job `XCM`, started in the 15:00 run, exit 0). 1,222 symbols were ever in the point-in-time top 1,000. Cache: `log/2026-10-14/init7-liquid-fade-oos/census/`.
- Events: 579 up movers, 688 down movers, 0 split drops; 1 up mover lacked bars, leaving 578. Last daily bar 2025-11-14, so no 20-session hold was truncated.

## Result (frozen cell)

| Measure | Value |
|---|---|
| Net per trade, base | **-0.555%** [-3.296, +2.646] |
| Net per trade, +20 bps stress | -0.755% |
| Median / win rate | +0.37% / 51.7% |
| Halves (by event date) | +1.521% / **-2.616%** |
| Raw up-mover return vs benchmark | +1.42% vs +0.97% |

Up movers beat the benchmark by +0.46 points over 20 sessions in this year, the opposite sign from the in-sample -1.76.

## Descriptive only (cannot rescue the failed pass)

- By move size, fade net: 3-6% -2.64% (n=294), 6-10% +0.05% (n=150), >10% +3.34% [-3.01, +9.19] (n=134). The in-sample 6-10% bucket (long -5.1%) is flat here; the >10% bucket now carries the fade, so the bucket pattern flips between years.
- The other seven drift cells on this window (rows in `result.json`): long up movers +0.26% to +0.70% net, no lower bound above zero; shorting down movers -0.99% to -3.11%. The in-sample year had long up movers negative in all four cells. Neither direction is stable across the two years.
- April 2025 holds 150 of 688 down-mover events (tariff selloff).

## Verification

`scripts/init7-liquid-fade-oos.py` reproduces `fade-result.json` from `rows.json.gz`. ZETA 2024-10-08: D+1 open $32.72 (2024-10-09), D+20 close $29.02 (2024-11-05), -11.31%, matching the row.

## Limits

Borrow cost and short availability are ignored; both would make the fade worse. The universe uses the 2026-10-12 symbol list including delisted names, ranked by trailing three-month SIP dollar volume.

## Decision

Per the freeze: report that Initiative 7 has no candidate left on liquid names. Five frozen tests have now failed (hourly megacap rotation, point-in-time 20-session reversal, liquid AH→PM census, liquid drift, this fade). No order, live rule, size or pulse timing changed.

Artifacts: `log/2026-10-14/init7-liquid-fade-oos/fade-result.json`, `result.json`, `rows.json.gz`.
