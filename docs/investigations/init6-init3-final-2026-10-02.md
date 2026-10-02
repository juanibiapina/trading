# Initiative 6 and Initiative 3 — October 2 completed-window checks

## Decision

The 15:00 incomplete-window hypothesis is resolved. **SGRX had no qualifying PM ignition, and the AH replay's admissions and displayed returns did not change.** Neither result supports promotion. Initiative 7's frozen alternative comparison supplies the parallel strategy progress.

## Initiative 6 — active pilot

[The 18:00 SGRX archive](../../log/2026-10-02/init6-SGRX-audit-1800.json) records the explicit SIP request and receipt, its raw response, complete-slot audit and a later quote. Requested at **16:03:12 UTC / 12:03:12 ET**, it has **66/66** unique five-minute PM slots from 04:00 through the 09:25 ET bar. The last bar ends at 09:30, before request time minus the 16-minute buffer. No pagination remains.

Maximum trades per bar remained **2,651**, below the unchanged **3,000-trade ignition**. There was no later qualifying bar. PM high was **$2.08** and PM-last close **$1.775**; neither is a pilot entry or realized return. SGRX adds no modeled admission regardless of its early retrospective class label. The stored holdable ledger remains **26 rows**, and the all-class liquidity audit remains **35**, both ending September 29. The broader historical ledger was not fetched again because the named new case cannot qualify.

The frozen cohort still captured **0/1 selected PM-only case**: SGRX was absent at 04:10:23 ET. Its 17 names had zero positive-size asks no more than 60 seconds old. This is one discovery miss in a selected tracker, not whole-universe recall; untracked cohort outcomes remain unresolved.

The later regular-session quote was **$1.67 x100 bid / $1.68 x100 ask**, **16.693 seconds** old at receipt. It demonstrates a later fresh IEX book and cannot reconstruct a PM entry or order fill.

**Evaluation:** the earlier maximum-trade/no-entry result held through the complete PM window. The completed modeled edge and execution hypothesis still have insufficient new positive evidence. This run closes a pending result; it does not add a trade or profitable case.

**Next check:** October 5's pre-entry cohort and next genuine PM-only observation. Compare discovery, all causal gate observations, quote availability and the complete outcome; record missing evidence before any execution claim. Keep this as the sole log-only pilot. The existing hardcoded UTC seasonal bounds require correction before winter data.

## Initiative 3 — parallel research

[The completed replay archive](../../log/2026-10-02/init3-opening-replay-1800.json) records the command, request/receipt times, full CLI output and the 15:00 per-case reference. All **13 selected-case lines match exactly** after the completed October 2 PM window:

| Variant | Admits | Completed result |
|---|---:|---|
| Second bar | 0 | No timing comparison |
| Third bar | 1, IPW | Modeled $1.40 at 17:30 ET, identical legal-grid price; −18.6% to PM open and −10.7% to the PM-high ceiling |

AMOD's first-ignition confirmations remain rejected; this version does not reconsider its later rebuild. TARA still has only two AH bars and is insufficient data. The original CLI fixture denominators are excluded from the selected-cohort claims. Active-bar baselines, rounded CLI prices and modeled next-open prices do not prove causal source availability, fillable books or P&L. The earlier 12/12 scan-completion result needs no repeat session audit.

**Evaluation:** finishing the outcome window did not reveal an earlier-entry advantage. No scan timing or entry-rule change follows. The later-rebuild question is a distinct next study, not a reason to relabel the rejected first signal as a win.

**Next delivery:** October 6 15:00, compare one later rebuild causally using the shared volume measurements, following October 5's primary-source and sparse-baseline deliveries. Exit research waits for a new actual fill. Verify DST cohort jobs loaded in the bridge before October 25; preserve the pending scan-retirement/exit proposals and Juan's broker-test deferral.

## Account and reporting

The read-only account and positions checks at approximately 18:03 CEST returned **$99,721.90**, down **$278.10**, and no positions. Commands were `node scripts/broker.js account` and `node scripts/broker.js positions`; no order was submitted.

The next daily email should report separate Initiative 7 design/selector/eligibility and Initiative 3 completed-replay deliveries, plus this Initiative 6 closed result. Jev had no additional calls in this run; the six-call batch remains in its prior dated manifest. The existing liquid-session/core-universe proposal remains for that email. Nothing new requires Juan's input.
