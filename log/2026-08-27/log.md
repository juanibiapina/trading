
## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| WNW | $3.12 | $3.81 | +22.1% | $4.55 PM | 1 | None | SELL | Grade None PM continuation, exit at profit |
| DAIC | $6.09 | $5.81 | -4.6% | $6.42 PM | 1 | None | SELL | Grade None exit first PM opportunity, above -10% stop |

**Actions taken:**
- SELL 29 WNW @ limit $3.72 ext (id 471b5c4a) filled @ $3.81 → +$20.01 (+22.1%)
- SELL 15 DAIC @ limit $5.70 ext (id a0f556e0) filled @ $5.81 → -$4.20 (-4.6%)
- Both Alpaca quotes frozen at 20:00Z prior close; used SIP 5Min bars for exit level
- No open positions after pulse

**Net pulse P&L:** +$15.81

## Position Evaluation — 14:30 CET

No open positions. Alpaca (`PA37U2Y192A7`) `positions` empty; `OPEN_POSITIONS.md` agrees. WNW and DAIC sold at 10:30 pulse. Nothing to evaluate or execute.

**Actions taken:**
- None (no open positions)

## Scan 21:30 CET (3:30 PM ET)

Regular session (15:30 ET, before AH open). No entries per regular-session-caution rule. Candidates below are **Watch — pending AH confirmation**; only entertained if they reappear in a 22:00+ CET AH scan with sustained momentum.

| Ticker | Price | Chg% | IRVol | VChg% | Float | MCap | Industry | Note |
|--------|-------|------|-------|-------|-------|------|----------|------|
| WNW | $3.42 | +37.9% | 436.8 | +463.6 | 26.2M | 90.1M | Internet Retail | Prior AH winner today (entered $3.12, sold +22.1%); day-2 watch |
| FALFF | $0.50 | +109.2% | 11.0 | +1590.8 | 181.7M | 106.9M | Precious Metals | OTC foreign, huge float — low priority |
| CELU | $2.00 | +127.2% | 1610.3 | -100.0 | 16.1M | 25.5M | Misc Commercial Svcs | Volume faded into close (VChg -100%) |
| PPCB | $2.27 | +112.2% | 3033.8 | -100.0 | 2.5M | 3.7M | Biotechnology | Low float, but end-of-day volume collapsed |

Rest of 41 hits are near-flat financial-conglomerate/SPAC $9.99-$10.00 names or faded low-volume movers — not pattern candidates.

## Scan 22:00 CET (4:00 PM ET)

Scanner ran at 16:00:11 ET — AH just opened, volume not yet accumulated. **0 hits.** No candidates found.

Observation-only scan (learning phase: no entries before 23:00 CET). Prior 21:30 watch names (WNW, FALFF, CELU, PPCB) did not cross AH threshold at open. Will re-check at 22:30/23:00 as AH volume builds.

## Scan 22:15 CET (4:15 PM ET)

Scanner ran at 16:15:14 ET — **0 hits.** No candidates found. AH volume still accumulating early. Prior 21:30 watch names (WNW, FALFF, CELU, PPCB) still not crossing AH threshold. Observation-only (learning phase: no entries before 23:00 CET). Re-check at 22:30/23:00.

## Scan 22:30 CET (4:30 PM ET)

Scanner ran at 16:30:12 ET — **4 hits.** Observation-only (learning phase: no entries before 23:00 CET).

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| AEMD | [TV](https://www.tradingview.com/chart/?symbol=AEMD) | $2.17 | -4.8% | +33.6% | $2.90 | +27.2% | 2.0M | 298K | 6.8x | 695K | Medical Specialties |
| CELU | [TV](https://www.tradingview.com/chart/?symbol=CELU) | $2.10 | +138.5% | +5.2% | $2.21 | +150.9% | 4.2M | 21.5M | 0.2x | 16.1M | Misc Commercial Svcs |
| CRE | [TV](https://www.tradingview.com/chart/?symbol=CRE) | $5.90 | -13.4% | +8.0% | $6.37 | -6.5% | 150K | 6.7M | 0.0x | 1.1M | Commercial Printing |
| GNPX | [TV](https://www.tradingview.com/chart/?symbol=GNPX) | $3.61 | -9.1% | +8.0% | $3.90 | -1.8% | 52K | 551K | 0.1x | 817K | Pharmaceuticals |

**Evaluation notes:**

- **AEMD** — only candidate with AH change >10% (+33.6%). Real, volume-backed spike. SIP 5Min bars accumulating hard: 283K → 1.12M → 1.09M → 1.48M sh/bar, ~10-12K trades/bar; SIP high $3.24, VWAP $3.10 corroborates scanner AH price. Low float 695K (ideal). Day% -4.8% (fine). Total% +27.2% (well under +150% ceiling). First AH appearance tonight (22:00/22:15 were 0 hits) — needs to reappear at 23:00+ to clear 2-AH-scan gate.
  - `SPIKE 16:03ET +28% $2.77 1139 trades / 100k sh (first co-spike bar)`
  - `CONFIRM-3 YES ignition 16:05ET 4.0x; confirmed 16:15ET $3.06`
  - Catalyst: **no same-day catalyst found** (2 searches). Latest events = Aug 13 Q1 earnings, July $4M dilutive follow-on @ $0.7101, undated Long COVID Hemopurifier preclinical data. Concern noted — Grade None/D pending.
  - Alpaca `quote` frozen at 20:00Z (`ask $0.00 x0`) — known AH-open freeze, not a real illiquidity read. Re-check book at 23:00.
- **CELU** — AH change only +5.2%; Total% +150.9% is stale regular-session run (Day% +138.5%). VRatio 0.2x = no real AH accumulation. Not an AH igniter. Skip.
- **CRE / GNPX** — AH change +8.0%, below 10% threshold. VRatio ~0. Skip.

Prior 21:30 watch names FALFF/PPCB did not carry into AH. WNW (day-2, sold +22.1% at 10:30) not crossing AH threshold.

**No entries** — observation-only scan. AEMD is the lead candidate for the 23:00 CET scan if it holds >10% AH and reappears.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|

No paper trades — scan ran before AH open (regular-session caution). No entries.
