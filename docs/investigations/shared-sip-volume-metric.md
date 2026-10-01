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

## Next step — October 1 18:00 CEST

Add opt-in log-only consumption of these JSON rows to the confirmation output and chart/report annotations. Keep existing verdicts and decision rules intact, then check the same bar timestamp and ratio appear in both consumers. Expand the verification to one fresh volume-backed winner and one additional negative control before proposing any threshold or cross-session entry rule.

No input from Juan blocks instrumentation. The daily email should report the distinction between local ignition and prior-session magnitude and link the YFOR artifact.
