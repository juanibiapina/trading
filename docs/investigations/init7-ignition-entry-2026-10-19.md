# Initiative 7: ignition-bar entry census (2026-10-19)

Juan's October 19 point on XXII ("entry way too late") asked whether entering on the volume ignition bar beats entering at the 17:00+ scans after a second >10% AH scan. This census tests that on the prior year, frozen before the data was fetched.

- Freeze: `docs/investigations/init7-ignition-entry-freeze.json` (16:10 UTC, before any regular-session bar or ignition-time quote was fetched)
- Script: `scripts/init7-ignition-entry.py` (gob `U8t`, 10 minutes)
- Output: `log/2026-10-19/init7-ignition-entry/result.json`, `rows.json.gz`, `quotes.json.gz`, `rth-peak.json.gz`

## Result: fails in all four cells

Events: the first 5-minute bar from 16:00 to 18:25 ET with volume of at least 10x the day's largest regular-session bar, a close 10–150% above the regular close, and at least 100k shares and $100k traded since 16:00. Universe: the same micro-caps as the October 15 censuses (outside the point-in-time top 1,000, $0.50–$10). The trade buys at the SIP ask 1 minute after the bar closes. October 2024 – September 2025: 547 events, 544 scored.

| Cell | n | Net mean | Interval (Bonferroni /4) | Halves | Stress (-100 bps) | Mid to mid |
|---|---|---|---|---|---|---|
| all / 04:30 bid | 544 | **-8.01%** | [-12.08, -2.61] | -11.04 / -4.97 | -9.01% | -5.73% |
| all / open | 544 | -11.82% | [-14.81, -8.45] | -14.75 / -8.88 | -12.82% | -10.73% |
| early (bar ≤16:40) / 04:30 | 400 | **-10.25%** | [-13.66, -6.76] | -11.66 / -8.86 | -11.25% | -8.02% |
| early / open | 400 | -12.32% | [-15.81, -8.73] | -15.57 / -9.11 | -13.32% | -11.26% |

Every interval sits below zero. The early cell, which matches Juan's 16:30–16:45 ET window, loses the most.

## The scan confirmation is a filter that helps

On the 364 symbol-days that are also among the 872 scan-time events, the ignition entry loses -5.12% at the 04:30 bid and the scan entry loses -3.31%. The ignition entry is worse by -1.82 points [-4.05, +0.30], and both halves are negative. The other 180 ignitions never reached a scan entry, and they lose about -13.8% on average. So waiting for a second >10% scan removes spikes that fail before 17:00. Entering earlier buys those failures, and the lower entry price on the survivors does not make up for them.

## Descriptive (cannot rescue the result)

- By ignition time at the 04:30 bid: 16:00–16:25 -10.3% (n=325), 16:30–16:40 -10.1% (75), 16:45–17:25 -8.2% (99), 17:30–18:25 +12.5% mean but -13.4% median (45). That mean comes from one outlier, DSY 2025-09-08 (+937%, unverified). The medians are negative in every bucket.
- By ignition-bar ratio: 10–30x -10.8%, 30–100x -4.4%, >100x -3.3%. Larger spikes lose less, but every bucket is negative.
- ETB names -10.5% (n=51), others -7.7%. The median entry spread is 114 bps.
- Spot check: ESYN 2024-10-01, 16:35 bar closes at $1.43; the quote at 16:40:59 ET is $1.35 x $1.36; the 04:30 bid is $1.22, so the result is -10.3%, which matches the row.

## Decision (fixed in the freeze)

No tested entry timing gives the long AH→PM micro-cap trade an edge. This census covers ignition-bar entry; the earlier ones covered 17:00 ET, 17:30–18:30 ET, take-profit exits and the short side on Alpaca. The scanner-improvement item that would replace the second scan with an ignition-bar confirmation is closed as unsupported. The stop-or-replace ask to Juan stands, with this result added. No live rule, order or pulse changed.

## Limits

Alpaca SIP bars stand in for the live TradingView screen, and live detection lag beyond 1 minute is not modelled. Quoted size is ignored. ETB is today's flag. Survivorship is limited to assets Alpaca still lists.
