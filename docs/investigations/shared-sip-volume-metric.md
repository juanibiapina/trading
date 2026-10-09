# Shared SIP volume metric — Initiatives 1 and 5

## Delivered October 1, 2026

`scripts/volume_metric.py` computes `sip-ah-volume-v1` and renders a Markdown review from the same rows returned as JSON. The archived [YFOR report](../../log/2026-10-01/YFOR-volume-audit.md) satisfies the process-review handoff for a log-only review surface. Its [SIP input](../../log/2026-10-01/YFOR-volume-sip.json) supports an offline replay.

The original volume-lead hypothesis remains falsified. This deliverable measures a completed volume spike and its prior-session context. Adoption into existing scanner columns and daily charts is the next instrumentation step.

## Calculation

For each completed five-minute AH bar with raw SIP shares `V[t]`:

- `baseline[t] = median(V[t-5m], V[t-10m], V[t-15m])`.
- `local_ratio[t] = V[t] / baseline[t]`, when the baseline is known and positive.
- `prior_peak_ratio[t] = V[t] / max(V in previous completed AH session)`, when all previous-session slots are observed and that maximum is positive.

The local window contains three exact preceding slots in the same 16:00–20:00 America/New_York session. It does not search backward across missing bars or overnight. The first three bars have a `warmup` local status. Require a caller-supplied previous **trading** date checked against the exchange calendar; weekends and holidays are not the prior session. `ZoneInfo` supplies the date-specific UTC offset.

Explicitly reported zero-share bars count in the median. An absent bar stays unknown: Alpaca can omit a no-trade interval, and an absent interval also cannot prove that a data request captured the complete tape. Any missing baseline slot yields `missing-baseline`; a median of zero yields `zero-baseline`. Both return null ratios and null threshold flags. Do not divide by an epsilon or classify an infinite ratio as a spike.

A complete normal AH session has 48 slots. When a previous session has fewer observed slots, report the observed peak and coverage, but leave `prior_peak_ratio` unknown. An early-close session needs calendar-specific bounds before this version can compare it; do not call it a complete normal session. Splits and other share-changing corporate actions also need a separate review before comparing raw shares across dates.

Input must identify SIP, five-minute aggregation and raw adjustment. The fetch uses an explicit end time and consumes every page. It fails on a SIP error; there is no IEX substitution. A bar starting at `t` only enters the output after `t+5m <= as_of`. Free historical SIP access can publish bars about 15 minutes late, so a completed historical bar is not proof of availability at its close. Archive `source_observed_utc` and use the data actually returned at each live observation for future attribution.

## Meaning of the columns

`local_ge_10` describes Juan's quantified 10x measurement on **that bar**, not on another bar's ignition. Keep it log-only in this delivery. The 20x upper part of his stated range is not an exclusion ceiling.

`prior_peak_ratio` supplies the missing cross-session context. A value below 1 means the current bar is smaller than the largest observed bar of the complete prior AH session. It does not establish a new hard rejection threshold. Price continuation, trade count, corporate-action context and executable quotes remain separate observations.

## YFOR verification

The input includes all 48 AH slots on both September 15 and 16. The prior-session maximum was **1,793,140 shares** at 16:45 ET on September 15.

| September 16 bar | Shares | Three-slot median | Local ratio | Prior AH maximum ratio |
|---|---:|---:|---:|---:|
| 17:15 ignition | 154,414 | 36,929 | 4.1814x | 0.0861x |
| 17:20 large bar | 941,842 | 36,929 | 25.5041x | 0.5252x |

The old `CONFIRM-3 4.2x` referred to the **17:15 ignition**, not the 941,842-share 17:20 bar. The latter clears 10x locally while remaining below the prior-session peak. A local 10x filter on any later bar therefore does not reproduce Juan's cross-session objection by itself. This resolves a metric-scope ambiguity in the September 17 roadmap note; it does not authorize a different entry.

## Reproduce

```bash
python3 scripts/volume_metric.py YFOR 2026-09-16 \
  --prior-date 2026-09-15 --as-of 2026-09-16T17:35:00-04:00 \
  --input log/2026-10-01/YFOR-volume-sip.json \
  --report /tmp/YFOR-volume-audit.md
```

Omit `--input` to fetch SIP and use `--save-input PATH` to archive it. JSON and the report consume the same `calculate()` result.

The network run, archived CLI replay and Python compilation passed. Verification reproduced both YFOR ratios and the report, kept output identical after changing future volumes, and returned unknown on missing slots, zero baselines and incomplete prior-session coverage. November and September AH bounds used the correct differing UTC offsets.

## Consumer delivery — October 1 18:00 CEST

Opt-in confirmation and HTML report consumption is complete. [The delivery report](shared-sip-volume-consumers-2026-10-01.md) records the matching rows, preserved verdict, and additional INLF/GIPR controls. It also records the missing-baseline and local-threshold limits that prevent promotion.

The next chart-bearing cycle should verify daily publication beside charts. Research sparse-slot interpretation and prior-session coverage before proposing a gate. No input from Juan blocks instrumentation; the next daily email should report both Initiative 1 and Initiative 5 deliveries.

## Same-date regular-session ratio — October 9, 2026

`sip-ah-volume-v2` output now adds `rth_peak_shares` (largest 5-minute SIP bar of the AH date's 09:30–16:00 ET regular session, with the v2 zero-slot and 100-share floor rules) and a per-row `rth_peak_ratio`. This is the "previous day" in Juan's DKI feedback: on the next morning's chart, the AH date's regular session is the previous day. The field is additive; files written before October 9 show `unknown`. Replay on the 89 real AH entries matches the October 6 study's `ah_vs_rth_max` on every entry and does not separate realized returns (≥1x: 75 entries, mean −2.8%; <1x: 14, mean −5.5%), so it stays log-only. Controls: DKI Oct 7 0.17x (Juan: no spike), OLB Oct 8 0.15x, VEEA Oct 8 3.5x, TRUG Aug 25 18.4x, UPC Sep 1 94.7x.
