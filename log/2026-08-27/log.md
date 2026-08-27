
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

## Scan 22:45 CET (4:45 PM ET)

Scanner ran at 16:45:15 ET — **6 hits.** Observation-only (learning phase: no entries before 23:00 CET).

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| AEMD | [TV](https://www.tradingview.com/chart/?symbol=AEMD) | $2.17 | -4.8% | +34.1% | $2.91 | +27.6% | 4.9M | 638K | 7.6x | 695K | Medical Specialties |
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $0.54 | +7.5% | +11.4% | $0.60 | +19.8% | 579K | 61.0M | 0.0x | 4.4M | Misc Commercial Services |
| MI | [TV](https://www.tradingview.com/chart/?symbol=MI) | $2.85 | +4.0% | +20.7% | $3.44 | +25.5% | 477K | 227K | 2.1x | 231K | Internet Software/Services |
| AAME | [TV](https://www.tradingview.com/chart/?symbol=AAME) | $1.57 | +20.8% | +5.1% | $1.65 | +26.9% | 234K | 252K | 0.9x | 3.9M | Multi-Line Insurance |
| MODD | [TV](https://www.tradingview.com/chart/?symbol=MODD) | $3.61 | +9.1% | +6.6% | $3.85 | +16.3% | 222K | 530K | 0.4x | 7.6M | Medical Specialties |
| ACET | [TV](https://www.tradingview.com/chart/?symbol=ACET) | $9.01 | +0.7% | +6.5% | $9.60 | +7.3% | 95K | 97K | 1.0x | 8.2M | Pharmaceuticals |

**Candidates with AH change >10%: AEMD, NCPL, MI.**

- **AEMD** — 2nd AH scan appearance (22:30 +33.6%, 22:45 +34.1%). Real volume-backed spike, SIP accumulating: 283K → 1.12M → 1.09M → 1.48M → 1.10M → 812K → 623K sh/bar, 3-12K trades/bar. SIP high $3.24 (20:15 bar), last bar 20:30 C $3.00 — fading modestly off peak but holding within 20% of high. Low float 695K (ideal). Day% -4.8% (fine). Total% +27.6% (well under +150% ceiling). Would clear 2-AH-scan gate at 23:00 if it holds >10%.
  - `SPIKE 16:03ET +28% $2.77 1139 trades / 100k sh (first co-spike bar)`
  - `CONFIRM-3 YES ignition 16:05ET 4.0x; confirmed 16:15ET $3.06`
  - Catalyst: **no same-day catalyst found** (per 22:30 search). Grade None/D pending. Concern noted.
- **NCPL** — first AH appearance tonight, AH +11.4%. SIP volume choppy: builds to 378K (20:20) then 1.22M sh (20:30) but price round-trips (C $0.57 ≈ open). Float 4.4M. `SPIKE 16:30ET +20% $0.65 703 trades / 379k sh`; `CONFIRM-3 NO no local-volume new-high ignition`. Needs a 2nd AH scan; watch.
- **MI** — first AH appearance, AH +20.7%. Tiny float 231K. SIP spiked to $3.69 (20:25) then collapsed L $2.85, C $3.05 (20:30) — spike→fade forming. `SPIKE 16:19ET +15% $3.28 124 trades / 10k sh`; `CONFIRM-3 PENDING`. Watch.
- **AAME / MODD / ACET** — AH change below 10% threshold. Skip.

Prior 21:30 watch names (WNW day-2, FALFF, CELU, PPCB) not crossing AH threshold. CELU dropped off entirely.

**No entries** — observation-only scan (before 23:00 CET). AEMD is lead for the 23:00 scan (would clear 2-AH-scan gate); NCPL and MI are watch. Prefer AEMD's BUILD-and-hold over MI's spike→fade if both qualify at 23:00.

## Scan 23:00 CET (5:00 PM ET)

Scanner ran at 17:00:10 ET — **5 hits.** Entries allowed (learning phase: ≥23:00 CET).

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| AEMD | [TV](https://www.tradingview.com/chart/?symbol=AEMD) | $2.17 | -4.8% | +49.3% | $3.24 | +42.1% | 7.0M | 894K | 7.8x | 695K | Medical Specialties |
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $0.54 | +7.5% | +10.2% | $0.59 | +18.5% | 2.0M | 61.1M | 0.0x | 4.4M | Misc Commercial Services |
| INHD | [TV](https://www.tradingview.com/chart/?symbol=INHD) | $6.00 | -4.0% | +13.5% | $6.81 | +9.0% | 562K | 278K | 2.0x | 2.5M | Building Products |
| MODD | [TV](https://www.tradingview.com/chart/?symbol=MODD) | $3.61 | +9.1% | +5.8% | $3.82 | +15.4% | 247K | 533K | 0.5x | 7.6M | Medical Specialties |
| ACET | [TV](https://www.tradingview.com/chart/?symbol=ACET) | $9.01 | +0.7% | +5.9% | $9.54 | +6.6% | 103K | 98K | 1.1x | 8.2M | Pharmaceuticals |

**Candidates with AH change >10%: AEMD, NCPL, INHD.**

- **AEMD — ENTERED.** Cleared 2-AH-scan gate (22:30 +33.6% → 22:45 +34.1% → 23:00 +49.3%). Clean BUILD-and-hold: SIP dipped 20:25-20:30 then rebuilt to new highs 20:35-20:45 (last bar 20:45Z C $3.30 H $3.45 vwap $3.35, still building), currently at/near AH high — not a fade. SIP real & accumulating: 1M+ sh/bar, 10K trades/bar; SIP high $3.45/VWAP $3.35 corroborates scanner AH price. Live book (ask $3.38 x100, bid $3.31 x100 — AH-open freeze lifted). Low float 695K (ideal). Day% -4.8% (not dead-cat, above -15%). Total% +42.1% (under +150% ceiling). `tradable=true`.
  - `SPIKE 16:03ET +28% $2.77 1139 trades / 100k sh (first co-spike bar)`
  - `CONFIRM-3 YES ignition 16:05ET 4.0x; confirmed 16:15ET $3.06`
  - Catalyst: **no same-day catalyst found** (4 searches total across scans). Latest events = Aug 13 Q1 earnings, July $4M dilutive follow-on @ $0.7101, undated Long COVID/Hemopurifier preclinical data. Grade None — concern noted, not a skip (learning phase).
  - **MULTI-SESSION check:** fresh day-1 igniter — not in WINNERS_TRACKING, Day% -4.8% (pure AH ignition), no prior up-session run.
  - **CHASE-CAP:** none — filled $3.12 (below ask), Entry Total% +43.8% vs qualifying +42.1% (chase gap +1.7pp). Well below fade zone.
  - **Order:** BUY 29 AEMD @ limit $3.42 ext (id 8d2f09b1) filled @ **$3.12**. Grade None. Position size $90.48.
- **NCPL — Skip: spike→fade / round-trip.** Cleared 2-AH-scan gate on the letter (22:45 +11.4% → 23:00 +10.2%) but declining and barely above threshold. SIP round-trips: spiked to $0.66 H at 20:30Z (16:30 ET) then faded back to $0.59 (C $0.59 ≈ open $0.54). `CONFIRM-3 NO no local-volume new-high ignition`. `SPIKE 16:30ET +20% $0.65 703 trades / 379k sh`. AvgVol 61M (huge, VRatio ~0 — not real AH unusual activity). Not a BUILD.
- **INHD — Watch.** First AH appearance tonight (only 1 AH scan) — 2-AH-scan gate not met. Genuine igniter though: `SPIKE 16:27ET +32% $7.94 599 trades / 20k sh`, `CONFIRM-3 YES ignition 16:25ET 88.8x; confirmed 16:35ET $8.24`. Float 2.5M, Day% -4.0%, Total% +9.0%. Re-check at 23:30 for gate clearance.
- **MODD / ACET** — AH change below 10% threshold. Skip.

Prefer AEMD's BUILD-and-hold over NCPL's spike→fade (trajectory dominates). AEMD entered; NCPL skipped; INHD watch for 23:30.

## Scan 00:00 CET (6:00 PM ET)

Scanner ran at 18:00:13 ET — **6 hits.** Entries allowed (learning phase: ≥23:00 CET).

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| AEMD | [TV](https://www.tradingview.com/chart/?symbol=AEMD) | $2.17 | -4.8% | +47.5% | $3.20 | +40.4% | 11.3M | 1.4M | 8.0x | 695K | Medical Specialties |
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $0.54 | +7.5% | +15.4% | $0.62 | +24.1% | 8.2M | 61.8M | 0.1x | 4.4M | Misc Commercial Services |
| MIMI | [TV](https://www.tradingview.com/chart/?symbol=MIMI) | $1.29 | -28.3% | +7.8% | $1.39 | -22.8% | 491K | 5.5M | 0.1x | 5.8M | Misc Commercial Services |
| BRNX | [TV](https://www.tradingview.com/chart/?symbol=BRNX) | $3.86 | -38.1% | +8.3% | $4.18 | -33.0% | 378K | 2.4M | 0.2x | 684K | Engineering & Construction |
| MODD | [TV](https://www.tradingview.com/chart/?symbol=MODD) | $3.61 | +9.1% | +10.8% | $4.00 | +20.8% | 372K | 548K | 0.7x | 7.6M | Medical Specialties |
| XHLD | [TV](https://www.tradingview.com/chart/?symbol=XHLD) | $8.28 | -3.2% | +8.8% | $9.01 | +5.4% | 369K | 1.8M | 0.2x | 10.4M | Misc Commercial Services |

**Candidates with AH change >10%: AEMD, NCPL, MODD.**

- **AEMD — already entered at 23:00 ($3.12, id 8d2f09b1).** One entry per candidate per night — no re-entry. Still holding: SIP $3.16–3.23 last bars (17:35 ET), live book ask $3.38 x100 / bid $3.31 x100. AH +47.5% / Total% +40.4% — building, not fading. Position intact.
- **NCPL — Skip (repeat): spike→fade / round-trip, no real AH unusual activity.** AH +15.4% but AvgVol 61.8M / VRatio 0.1x = the AH vol is not unusual vs its base. SIP round-trips: peaked $0.72 (17:10 ET) fading to $0.63 (17:35 ET). Quote ask $0.61 x100 / bid $0.45 (wide spread). `SPIKE 16:30ET +20% $0.65`; `CONFIRM-3 NO ignition 17:10ET failed third-bar hold/volume`. No catalyst (prior searches). Skip.
- **MODD — Watch (gate not met).** First AH scan >10% tonight (+10.8%; prior scans +6.6%, +5.8%) — only 1 qualifying AH scan, 2-AH-scan gate not met. Spike→fade with tiny volume: SIP peaked $4.28 (17:15 ET) fading to $4.00 (17:40 ET), 3–29K sh/bar, VRatio 0.7x — not a real igniter. `SPIKE 16:24ET +22% $4.39`; `CONFIRM-3 NO ignition 16:20ET failed third-bar hold/volume`. Catalyst: **no same-day catalyst found** (1 search — insulin-pump device co., latest news Aug 24 analyst "Sell", phased commercial launch late 2026). Watch for a 2nd AH scan >10% at 00:30.
- **MIMI / BRNX — Skip: dead-cat.** Both crashed regular session (MIMI Day -28.3%, BRNX Day -38.1%) and bounce modestly in AH (AH +7.8% / +8.3%, both below 10% and both still well below regular close: Total% -22.8% / -33.0%). Recovering from sell-off, not new momentum. Skip.
- **XHLD — Skip.** AH +8.8% below 10% threshold, VRatio 0.2x. Not an igniter.

**Feed-lag cross-check (tracked pipeline):** INHD (23:00 watch, +13.5% AH) — SIP now shows fade: peaked ~$6.95 dropping to $6.19 (17:45 ET) ≈ +3% over close, below 10% threshold. TradingView correctly dropped it. No rescue. Prior watch names NCPL/MODD handled above.

**No new entries** — NCPL/MODD spike→fade with no real AH accumulation, MIMI/BRNX dead-cat, INHD faded. AEMD position (entered 23:00) is the only trade tonight. One scheduled scan remains (00:30 CET / 18:30 ET).

## Scan 00:30 CET (6:30 PM ET) — final scheduled scan

Scanner ran at 18:30:17 ET — **8 hits.** Entries allowed (learning phase: ≥23:00 CET).

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| AEMD | [TV](https://www.tradingview.com/chart/?symbol=AEMD) | $2.17 | -4.8% | +52.5% | $3.31 | +45.2% | 12.0M | 1.5M | 8.1x | 695K | Medical Specialties |
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $0.54 | +7.5% | +7.0% | $0.58 | +15.1% | 8.8M | 61.8M | 0.1x | 4.4M | Misc Commercial Services |
| RYET | [TV](https://www.tradingview.com/chart/?symbol=RYET) | $0.97 | +2.1% | +26.3% | $1.23 | +28.9% | 3.3M | 793K | 4.2x | 14.3M | Packaged Software |
| INHD | [TV](https://www.tradingview.com/chart/?symbol=INHD) | $6.00 | -4.0% | +8.5% | $6.51 | +4.2% | 942K | 338K | 2.8x | 2.5M | Building Products |
| MIMI | [TV](https://www.tradingview.com/chart/?symbol=MIMI) | $1.29 | -28.3% | +7.0% | $1.38 | -23.3% | 537K | 5.5M | 0.1x | 5.8M | Misc Commercial Services |
| MODD | [TV](https://www.tradingview.com/chart/?symbol=MODD) | $3.61 | +9.1% | +17.5% | $4.24 | +28.1% | 391K | 550K | 0.7x | 7.6M | Medical Specialties |
| AVAT | [TV](https://www.tradingview.com/chart/?symbol=AVAT) | $0.62 | +13.2% | +8.6% | $0.68 | +23.0% | 244K | 677K | 0.4x | 32.8M | Financial Conglomerates |
| WVVIP | [TV](https://www.tradingview.com/chart/?symbol=WVVIP) | $3.43 | -17.3% | +11.1% | $3.81 | -8.2% | 97K | 1.2M | 0.1x | 4.0M | Beverages: Alcoholic |

**Candidates with AH change >10%: AEMD (held), RYET, MODD, WVVIP.**

- **MODD — ENTERED.** Cleared 2-AH-scan gate: crossed 10% at 00:00 (+10.8%) and higher at 00:30 (+17.5%) — a genuine late BUILD, AH% accelerated across the night (22:30 +6.6% → 23:00 +5.8% → 00:00 +10.8% → 00:30 +17.5%). SIP built through the afternoon: $3.80 (20:30Z) → peak $4.28 (~21:00-21:15Z / 17:00-17:15 ET) → $4.00 (21:40Z), real trades accumulating (113-328 trades/bar, 10-29K sh/bar). Current $4.00 vs peak $4.28 = -6.5% off high (holds within 20%, peak after 17:00 ET — not a spike→fade). Float 7.6M (<10M). Day% +9.1% (positive, not dead-cat). Total% +28.1% (well under +150% ceiling). `tradable=true`. Two-sided book (ask $4.31 x100 / bid $2.94 x100, frozen at 20:00Z AH-open artifact — non-zero size, real book).
  - `SPIKE 16:24ET +22% $4.39 570 trades / 65k sh (first co-spike bar)`
  - `CONFIRM-3 NO ignition 16:20ET failed third-bar hold/volume` (early ignition failed, stock rebuilt later in session)
  - Catalyst: **no same-day catalyst found** (prior searches — Modular Medical insulin-pump device co., latest news Aug 24 analyst "Sell", phased commercial launch late 2026). Grade None — concern noted, not a skip (learning phase).
  - **MULTI-SESSION check:** fresh day-1 igniter — not in WINNERS_TRACKING, Day% +9.1% (mild), AH ignition today.
  - **CHASE-CAP:** none — filled $4.18 (below qualifying scanner AH $4.24 / +28.1%). Fill Entry Total% +15.8% vs qualifying +28.1% (negative chase gap). Well below fade zone.
  - **Order:** BUY 23 MODD @ limit $4.20 ext (id 704312eb) filled @ **$4.18**. Grade None. Position size $96.14.
- **RYET — FINAL-SCAN-GATE-BLOCK.** Genuine volume-backed late igniter, but first AH appearance at the final scan — blocked **solely** by the 2-AH-scan gate. Flat/thin all afternoon (1-4 trades/bar to 21:40Z) then EXPLODES at 21:45Z (17:45 ET): 509K sh/2,145 trades → 1.05M sh/6,450 trades → 812K sh/4,433 trades → 474K/450K/354K/345K sh/bar. Price $1.03 → $1.43 H, holding $1.19-1.36. `SPIKE 17:47ET +23% $1.19`; `CONFIRM-3 YES ignition 17:45ET 2036.9x; confirmed 17:55ET $1.27`. Float 14.3M, Day% +2.1% (above -15%), Total% +28.9% (under +150% ceiling), `tradable=true`, two-sided book. Catalyst: none same-day (Ruanyun Edai Technology — recent China Nasdaq IPO, Packaged Software; latest = 1H 2026 interim results ~2 weeks old). Grade None. Ignited 17:45 ET — too late for a 2nd AH scan before the 18:30 final scan. **Do NOT enter (gate stands).** Instrumentation for the morning-eval tracker.
- **WVVIP — Skip: dead-cat / preferred stock.** AH +11.1% but Total% -8.2% (still below regular close), Day% -17.3% (crashed regular session). Willamette Valley Vineyards preferred — thin (AH Vol 97K, VRatio 0.1x). Recovering from sell-off below close, not new momentum. Skip.
- **NCPL — Skip (repeat): faded below 10%.** AH now +7.0% (was +10.2% at 23:00, +15.4% at 00:00) — rolling over. AvgVol 61.8M / VRatio 0.1x = no real AH unusual activity. Spike→fade confirmed. Skip.
- **INHD — Skip: faded.** AH +8.5%, below 10% (was +13.5% at 23:00). SIP faded off $6.95 peak. Gate never met. Skip.
- **MIMI — Skip: dead-cat.** Day -28.3%, AH +7.0%, Total% -23.3% (deep below close). Recovering from crash. Skip.
- **AVAT — Skip.** AH +8.6% below 10% threshold, float 32.8M, VRatio 0.4x. Not an igniter.

**Feed-lag cross-check (tracked pipeline):** NCPL/INHD/MODD all handled above via SIP (INHD/NCPL faded, MODD rescued as real BUILD). No under-reported pipeline name found.

**AEMD** — position from 23:00 ($3.12, id 8d2f09b1) still open, +3.2% (now $3.22, live book ask $3.38 x100). Still building (AH +52.5%). No re-entry (one per candidate per night).

**Entries this scan: MODD.** Two positions open tonight (AEMD, MODD) — both fresh day-1 AH igniters, both Grade None BUILD-and-hold. Final scheduled scan complete.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
| AEMD | $3.12 | 2026-08-27 23:00 CET | 29 | 8d2f09b1 | Grade None. BUILD-and-hold, cleared 2-AH-scan gate, float 695K, CONFIRM-3 YES, Total% +43.8%. No same-day catalyst (concern noted). |
| MODD | $4.18 | 2026-08-27 00:30 CET | 23 | 704312eb | Grade None. Late BUILD, cleared 2-AH-scan gate (00:00 +10.8% → 00:30 +17.5%), float 7.6M, Total% +15.8%. No same-day catalyst (concern noted). |
