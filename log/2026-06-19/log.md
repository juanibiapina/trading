# Morning Evaluation - 2026-06-19

## Morning Evaluation — 10:25 CET

_Pulse 1. Evaluating the Jun 18 after-hours → Jun 19 premarket transition. Live read at 04:22 ET (PM ~22 min old). Yahoo's 5m prepost feed is still showing Jun 18 sessions (documented overnight lag), so AH/PM reconstruction relies on the live TradingView scan plus Jun 17 daily anchors._

### ⚠️ Headline: evening scanner failed after 22:00 CET

The post-market scanner ran only **2 of 7** scheduled scans last night:
- ✅ 21:30 CET (regular session, pre-close watch)
- ✅ 22:00 CET (AH open, 0 hits as usual)
- ❌ 22:30, 23:00, 23:30 CET (Jun 18) — did not run
- ❌ 00:00, 00:30 CET (Jun 19) — did not run

Git history confirms: after `post-market scan 2026-06-18 22:00 CET` (22:00:48), no scan committed until an unrelated commit at 09:01 Jun 19. **The entire entry window (23:00–00:30 CET) was missed.** No AH BUILD data was captured, no candidate could be evaluated for entry, and no paper trade was possible last night. This is an infrastructure/process failure, not a detection-threshold issue. The scanner binary works (manual runs at 04:22–04:24 ET returned 22 PM / 20 AH hits), so the cron executions silently failed or were skipped.

### Today's Winner

Weak, ambiguous morning — no dramatic fresh AH→PM explosion. The PM movers are low-float multi-day continuations that were already on yesterday's pre-close watchlist. Best liquid AH→PM continuation by reliable gain from the Jun 18 close:

**CDT** — CDT Equity Inc. (Pharmaceuticals: Major)
- Catalyst: none verified. Low-float (1.6M) momentum name; ran +48% on Jun 18 (intraday peak $1.96 at 12:40 ET) and is popping again in PM.
- Previous Close (Jun 18): ~$1.02 (Jun 17 close was $0.69; ran +48% Jun 18)
- Premarket now (04:22 ET): $1.34 = **+31% from Jun 18 close** (scanner shows +93.4% but that is measured off the stale Jun 17 $0.69 anchor — Yahoo has not posted the Jun 18 daily close yet)
- Hypothetical P&L (AH entry ~$1.02 → PM $1.34): **+31%**
- Float: 1.6M | Market Cap: $5.0M | VRatio (PM) 3.1x

**Scanner Diagnostic:**
- Detectable at screening time? **YES (partial)** — CDT was on the 21:30 CET regular-session watchlist ($1.17, +68.8% day, fading into close) and carried over to the 22:00 CET watch. So even the truncated scanner flagged it.
- But the scanner died before the AH/entry window, so CDT (like every name) could not be evaluated for an AH BUILD entry. Detection of the candidate is not the gap today; **scan coverage is.**
- Scanner gap: fix the cron reliability so the 22:30–00:30 CET scans actually run. Detection thresholds are not the problem this morning.

_Caveat: all "winner" calls today are low-confidence. Moves are modest (~+30% top liquid), Yahoo 5m AH/PM data is lagged, and the scanner never recorded the AH session._

### Baseline Tracking

- Days tracked: **34** (was 33 + 1)
- Winners detected by scanner: **30/34 (88.2%)** — …, LNAI, LNKS (Jun 18), **CDT (Jun 19)** (CDT was on the 21:30/22:00 CET watch)
- Winner selected for paper trade: **20/34 (58.8%)** — not incremented. No entry possible: the scanner failed before the 23:00+ CET entry window.
- Target: >80% detection
- Status: **BASELINE MET** (detection), but **COVERAGE FAILED** last night

### Retrospective Scan Results

Live PM scan (04:22 ET, 22 hits, top by Jun 18-close gain): CDT $1.34 (+31%), WKSP $0.96 (+30%), BYAH $1.67 (+27%), LPA $4.37 (+22%), LNKS $2.98 (+11%), CRVO $4.66 (+10%), APWC $1.91 (-4%). WOK $5.69 (+78%) excluded — 9K float, untradeable. Forced AH scan (04:24 ET, 20 hits): top SAGT +82.4% AH ($1.81, 6.7M float), ATPC +9.5%. These are *next* session's AH building, not last night's. AH/PM 5m reconstruction unavailable (Yahoo feed still on Jun 18 sessions). The scanner's PM Chg% column is inflated this morning because it anchors to the last Yahoo daily close (Jun 17 $0.69 for CDT) rather than the Jun 18 close.

### Paper Trade P&L

| Ticker | Entry | Entry Total% | Catalyst | Entry Time | PM Peak | Peak Time | Exit | P&L | P&L % | Status |
|--------|-------|--------------|----------|------------|---------|-----------|------|-----|-------|--------|
| _none — scanner failed before the 23:00+ CET entry window; no trade possible_ | | | | | | | | | | |

**Total Paper P&L: €0.00** (no open positions; LPA was closed yesterday Jun 18 at $4.21, -19.2%)

### Scanner Effectiveness

- Evening scans ran: **2 of 7 scheduled** (21:30, 22:00 CET only) — coverage failure
- Candidates found: ~10 unique (21:30 watch); 0 AH hits at 22:00 (normal this early)
- Retrospective matches: today's PM movers (CDT, LNKS, WKSP, APWC) were all on the 21:30 watchlist — detection held, but no AH/entry data was collected

### Missed Opportunities

| Ticker | AH Change | Why Missed | Would Be Profitable? |
|--------|-----------|------------|---------------------|
| (all) | unknown | Scanner did not run 22:30–00:30 CET — entire AH session uncaptured | Indeterminate |

No *detection* miss identified, but the AH session was entirely uncaptured, so any AH BUILD setup that formed after 22:00 CET would have been missed by default.

### AH Mover Follow-Through

No AH scan data exists for Jun 18 evening beyond the 22:00 CET (0-hit) snapshot, and Yahoo 5m AH bars for Jun 18 are not yet posted. Follow-through table cannot be reconstructed this morning. The names that carried from the 21:30 CET pre-close watch into Jun 19 PM:

| Ticker | Jun 18 Close | Current PM (04:22 ET) | From Close | Note |
|--------|--------------|------------------------|------------|------|
| CDT | ~$1.02 | $1.34 | +31% | Low-float continuation; ran Jun 18 intraday |
| WKSP | $0.74 | $0.96 | +30% | Low-float continuation |
| BYAH | $1.32 | $1.67 | +27% | No-catalyst pump (Jun 12 winner, faded) bouncing again |
| LPA | $3.57 | $4.37 | +22% | Yesterday's trade; bounced after -19% stop-out |
| APWC | $1.99 | $1.91 | -4% | Faded |

### Notes

- **Process failure is the story today.** 5 of 7 evening scans did not run; the entry window was lost. Flag to the 14:20 scanner-improvement / 14:40 process-review runs: investigate why the 22:30/23:00/23:30/00:00/00:30 CET crons silently skipped on Jun 18. The scanner binary itself is healthy (manual runs work). Check cron daemon / pi bridge availability during 22:30–00:30 CET.
- **No CEILING-OVERRIDE / DEAD-CAT-OVERRIDE / fade-rule watch candidates** could be flagged last night — the scanner never reached the AH window. Fade-rule false-negative tally unchanged (CRE Jun 17, LNKS Jun 18 = 2). PM-only-gapper tally unchanged (CIIT, GLXG, TDIC).
- **Biggest raw PM mover:** WOK (+78% from $3.20) but 9K float = untradeable artifact (was the May 12 winner that crashed -87%). Excluding it, CDT (+31%) is the biggest liquid mover and an **AH→PM continuation** the scanner detects (on the 21:30 watch). Not a PM-only gapper.
- **Multi-day check (Active Watch):**
  - CRVO (Jun 16, Day 3): $4.66 PM (+10% from $4.24 close) — still elevated, low-float multi-day runner continuing.
  - LNKS (Jun 18, Day 1→2): $2.98 PM, holding ~$2.7–3.0 after its $4.70 PM peak yesterday — typical day-2 fade-from-peak.
  - LNAI / NIVF (Jun 17): below scan thresholds, ~$4.0 / ~$0.8 — faded as logged.
- **Data caveat:** Yahoo daily and 5m prepost feeds both lag ~1 day at 04:22 ET; the live TradingView scan is the only current source. All gain figures are computed against the Jun 18 close where derivable.
