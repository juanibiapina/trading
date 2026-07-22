# Morning Evaluation - 2026-07-22

## Morning Evaluation — 10:20 CET

Session evaluated: **2026-07-21** after-hours → **2026-07-22** premarket. Pulse 1.

### Today's Winner

**SXTC** — Pharmaceuticals (China SXT Pharmaceuticals, NasdaqCM small-cap)
- Catalyst: **Unverified/None** — no same-day PR located in this environment (no web-search tool available at pulse). China small-cap pharma PM squeeze; treat as no-catalyst until verified.
- Previous Close: $2.45
- AH last night: peaked **$2.85 (+16.3%)** at ~18:25 ET on **negligible volume** (few hundred sh/bar; single 15k-sh bar at the 16:00 ET open). Never a tradeable AH signal.
- Premarket now: **$5.69 (+132%)**; PM peak **$7.91 (+222.9%)** at 04:05 ET (08:05Z)
- Hypothetical P&L: optimistic AH entry ~$2.75 → PM peak $7.91 = **+188%** (but undetectable, see diagnostic). Realistic PM-open re-entry: first PM bar VWAP $5.45 → peak $7.91 = **+45%**.
- Float: 32.2M | Market Cap: $86.3M
- SIP confirmation it cleared the bar: PM open bar 08:00Z **1,282,250 sh / 23,886 trades** (H $6.44), 08:05Z **1,850,080 sh / 38,738 trades** (H $7.91). Real, accumulating, >100% move.

**Scanner Diagnostic:**
- Detectable at screening time (~22:15 CET)? **NO**
- Why: SXTC was only +16% in AH on essentially no volume (a few hundred shares/bar; VRatio far below threshold). It appeared in **zero** of last night's 9 evening scans. The winner-making >100% explosion fired at **PM open (04:00 ET)**, hours after the final 00:30 CET scan.
- Classification: **PM-only gapper — HOLDABLE** (gain sustained across ≥2 consecutive 5-min PM bars on 1.3–1.85M sh; a real exit window exists — still +132% at pulse). Per the PM-only-gapper rule this is **not** a scanner failure and is **not** counted against the detection baseline. The nominal +16% AH tick was sub-detection-threshold noise, not a detectable AH footprint.
- Scanner gap: none actionable in the AH workflow — structurally a PM-only gapper. Only an early-PM scan (a separate, riskier workflow under evaluation via the PM-only-gapper tally) could catch it.

### Baseline Tracking

Carried from 2026-07-21 log (Days tracked 51; 44/49 detected; 25/49 selected). Today's winner (SXTC) is a **PM-only gapper**, so it is excluded from both the detection numerator and denominator (not a valid AH-detection sample) — detection and selection ratios hold at /49. Days tracked increments by 1 for the session evaluated.

- Days tracked: **52** (was 51 + 1)
- Winners detected by scanner: **44/49 (89.8%)** — unchanged (SXTC excluded, PM-only gapper)
- Winner selected for paper trade: **25/49 (51.0%)** — unchanged (SXTC not tradeable via AH workflow; correctly not traded)
- Target: >80% detection
- Status: **BASELINE MET** (89.8%)
- **Baseline gap (carried):** 2026-07-17 and 2026-07-20 morning evals recorded no `Days tracked:` line — those two trading-day retrospectives were not baseline-counted (denominator understates true trading days). The immediately-preceding trading day (07-21) *does* carry a baseline line, so no new gap this cycle.

### Retrospective Scan Results

- Live PM scan (04:21 ET): 5 hits — **SXTC +121% $5.93**, AEHL +39% $0.90, INLF +58% $3.53, SNTG +22% $2.55, KUST +5% $1.01.
- AH reconstruction (SIP + Yahoo `--ah-history`): only AEHL and KUST had real AH volume last night; SXTC's AH was thin (+16%). Winner move was PM-only.

### Open Position P&L (Alpaca)

**No executed positions.** Account is flat — HIHO and PAPL were both sold yesterday (14:30 CET pulse: HIHO @ $1.26 −16.0%, PAPL @ $0.84 −23.6%). `broker.js positions` returns none.

### Scanner Effectiveness

- Evening scans ran: **7 of 7** scheduled (21:30, 22:00, 22:30, 23:00, 23:30, 00:00, 00:30 CET), plus 2 bonus (22:15, 22:45) = 9 total. **Full coverage — entry window fully captured.**
- Candidates found: AEHL (night's deepest AH mover), KUST, DFNS, NVVE, SNTG (all AH movers logged).
- Retrospective matches: winner SXTC = PM-only gapper, not an AH candidate. AH movers (AEHL, KUST) all faded — correctly skipped.

### Missed Opportunities

| Ticker | AH Change | Why Missed | Would Be Profitable? |
|--------|-----------|------------|---------------------|
| SXTC | +16% AH (thin) | PM-only gapper — real +100% move fired at PM open, no AH volume | Yes on PM re-entry (+45% VWAP→peak), but structurally undetectable by AH scanner — not a scanner miss |

No AH→PM continuation was missed. Every real AH mover was detected and correctly skipped (all faded).

### AH Mover Follow-Through

| Ticker | AH Peak | Peak Time | AH Trajectory | Current PM | From Peak | From Close | Verdict |
|--------|---------|-----------|---------------|------------|-----------|------------|---------|
| AEHL | $1.38 (SIP, +112%) | 16:40 ET | Spike→fade | $0.90 (+38%) | −35% | +38% | Faded; **AH peak > PM peak $1.14 → AH was the better exit**. Correctly gate-blocked (SPIKE→FADE, 1st-scan). Float 15.6M = higher-float negative control. |
| KUST | $1.32 (AH) | ~17:00 ET | Spike→fade | $1.01 (−21% vs $1.27 Yahoo close) | −24% | fade | Dead-cat-override watch (hypo $1.24). SIP PM peak $1.35 first bar (578k sh) then collapsed to $1.01. Reclaim faded instantly. |

**AH-peak-vs-PM-peak:** AEHL AH peak ($1.38) > PM peak ($1.14) — another "AH was the better exit" case (but AH peak only +112%, not an extreme >250% runner, so not a new MSW-class data point).

### Price Charts

```
SXTC — 2-Day Timeline
Prev Close: $2.45 | Range: $2.50–$7.91 | Current: $5.69 (+132.3%)
Peak: $7.91 (+222.9%) at 07-22 08:05 ET
AH 07-21: flat +6–16% on a few hundred sh/bar (non-tradeable)
PM 07-22 04:00 ET: EXPLODES $3.39 → $7.91 on 1.3–1.85M sh/bar (24k–39k trades) → PM-only gapper
```

### Notes

- **Winner is a rare HOLDABLE PM-only gapper.** SXTC's +223% peak came entirely at PM open on 1.3–1.85M sh/bar (24k–39k trades) and held above +130% through the pulse — a genuine, liquid exit window, unlike most PM-only gappers which are instant crashes. Adds to the PM-only-gapper tally as a *holdable* case (see tally). One holdable case does not flip the "AH-blind-spot has low real cost" hypothesis, but it is the strongest holdable PM-only example to date.

- **PM-only gapper tally (updated):** CIIT (Jun 10 +140%), GLXG (Jun 11 +343%, uninvestable), TDIC (Jun 16 +140%), MBRX (Jun 23 +131%, uninvestable), CUPR (Jun 24 +81%, thin), **SXTC (Jul 22 +223%, HOLDABLE — sustained ≥2 PM bars on 1.3–1.85M sh)**. Holdable count now 1 clear + a few borderline; still not a cluster justifying a separate early-PM workflow.

- **Dead-cat-override watch outcome (KUST, 07-21 → 22):** hypo entry $1.24 @ 23:00 CET → SIP PM peak $1.35 (first PM bar, 578k sh) = **+8.9%**, then collapsed to $1.01 within one bar. The reclaim-above-close faded near-instantly — **dead-cat filter roughly validated** (only a thin one-bar +8.9% window, gone immediately). Note: this is a *different* KUST event from the 2026-07-15 winner (577K-float repeat pump name).

- **Broker-block tally (updated):** SHPH (07-21, tradable=false across AH scans, Grade None, AH +18–24%). PM follow-through: PM peak only **$3.22 (+6.3%)** vs $3.03 close — faded from its AH level, so the untradability **cost ≈ nil this time** (would have lost). Prior cases: SHPH Jun 25 (Grade C, hypo untradable), SHPH Jul 13 (hypo +29%/+70%). Recurring low-float-pharma broker-block persists; cumulative cost still modest and this instance was a non-event.

- **Fade-rule false-negative tally (unchanged): sub-3M count 3 of 5, ≥4/5 trigger NOT met.** Tonight's faders were higher-float negative controls: **AEHL float 15.6M** faded (AH peak $1.38 > PM peak $1.14) exactly as the fade rule predicts — corroborates trajectory-over-catalyst, does not count toward the sub-3M trigger. No new sub-3M fader re-exploded. Live-flip exception stays withdrawn pending one more clean sub-3M SIP-verified blow-past.

- **No reverse-split entries** last night (no entries at all — clean no-trade night). Reverse-split recency tally unchanged (this-week splits 3/3 faded).

- **No ceiling-override or late-AH-tail winner cases** this cycle. AEHL's AH peak (16:40 ET) was well inside the scanned window, not a tail surge.

- **Coverage:** full 7/7 (no coverage failure to add to the tally).

- **Active Watch check:** HIHO (entered $1.50, sold $1.26) crashed further to $0.93 day 2 — no-catalyst-grade-B pump fully unwinding. CJMB flat at $1.21 (day 5 → moved to Historical).

## Position Evaluation — 10:30 CET

**No open positions.** Alpaca `broker.js positions` returns none; `OPEN_POSITIONS.md` shows `_(none)_`. Source of truth and mirror agree — no reconciliation needed.

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| _(none)_ | | | | | | | — | Account flat |

**Actions taken:**
- None. Nothing to sell, no stops to update. Account flat since 07-21 14:30 CET pulse (HIHO, PAPL both closed).

## Position Evaluation — 14:30 CET

**No open positions.** Alpaca `broker.js positions` returns none (equity $99,877.41, all cash); `OPEN_POSITIONS.md` shows `_(none)_`. Source of truth and mirror agree — no reconciliation needed.

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| _(none)_ | | | | | | | — | Account flat |

**Actions taken:**
- None. Nothing to sell, no stops to update. Account flat since 07-21 14:30 CET pulse (HIHO, PAPL both closed).
