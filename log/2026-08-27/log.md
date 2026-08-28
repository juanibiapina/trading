
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

## Morning Evaluation — 10:20 CET

### Today's Winner

**No real AH→PM winner today.** No name cleared the >100% AH→PM winner bar on accumulating SIP volume.

- **Biggest genuine AH→PM mover: AEMD** (Aethlon Medical, Medical Specialties) — real AH surge that continued into PM but topped at **+76% PM peak**, under the 100% bar. Detected AND entered last night (@ $3.12). Not crowned "winner" (sub-100%), but the baseline diagnostic runs on it.
- **Biggest raw PM mover: WHLR** (Wheeler REIT) — **+155% PM SIP peak** ($1.12 close → $2.86) but a **PM-only gapper** (flat/down in after-hours ~$1.12–1.26, move fired only at 04:00 ET PM open). Structurally undetectable by the AH scanner — **not counted against the detection baseline.**

**AEMD detail:**
- Catalyst: **None** — no same-day PR found (clinical-stage Hemopurifier cancer trial; latest IR news 2 weeks old). Grade None.
- Previous Close: $2.17
- AH last night: SIP peak **$3.46 (+59.4%) @ ~17:05 ET** on accumulating volume (283K → 1.12M → 1.48M sh/bar, 10–12K trades/bar early)
- Premarket now: SIP peak **$3.82 (+76.0%) @ 04:00 ET** on 1.40M sh / 20,091 trades; current ~$3.24
- Hypothetical P&L (AH entry → PM peak): AH ~$2.90 → PM $3.82 = **+31.7%**; actual entry $3.12 → PM peak $3.82 = **+22.4%**
- Float: 695K | Market Cap: ~$1.5M

**WHLR detail:**
- Catalyst: **None** — no fresh PR/8-K found (Aug 10 announcement is old). Grade None.
- Previous Close: $1.12 (Yahoo $1.60 anchor is a stale multi-day figure; the actual last regular close was $1.12, −29.8% that session)
- AH last night: flat/down, SIP $1.12–1.26 all evening (no >10% AH signal)
- Premarket now: SIP peak **$2.86 (+155%) @ 08:05 ET** on 1.74M–2.48M sh/bar, 17K–22K trades/bar — real, holdable
- Float: 772K | Market Cap: ~$4.9M

**Scanner Diagnostic (AEMD):**
- Detectable at screening time? **YES**
- At ~22:15 CET it was a fresh AH igniter (+33.6% AH, VRatio 6.8x, SIP accumulating hard). Cleared the 2-AH-scan gate (22:30 +33.6% → 22:45 +34.1% → 23:00 +49.3%), BUILD-and-hold, low float 695K. **Entered @ $3.12 at 23:00 CET.** Clean detection and selection — nothing to fix.
- Scanner gap: none for AEMD.

**Scanner Diagnostic (WHLR):**
- Detectable at screening time? **NO** — PM-only gapper. Flat in after-hours; the +155% move began only at 04:00 ET PM open on overnight interest. No AH footprint for the evening scanner to catch. Not a scanner failure, not counted vs baseline.

### Baseline Tracking

- Days tracked: **74** (was 73 + 1)
- Winners detected by scanner: **60/69 (87.0%)** — +AEMD (biggest genuine AH→PM mover, detected all AH scans, entered)
- Winner selected for paper trade: **34/67 (50.7%)** — +AEMD (traded @ $3.12)
- Target: >80% detection
- Status: **BASELINE MET** (87.0%)

No baseline gap: previous eval log/2026-08-26 (Aug 26→27 session), today evaluates Aug 27→28 — consecutive trading days.

### Retrospective Scan Results

Live PM scan (04:20 ET) — 3 hits: **WHLR +131.2%** ($2.59, 2.0M PM vol, float 772K), **AEMD +49.8%** ($3.25, 550K vol, float 695K), **NCPL +10.5%** ($0.59).
- WHLR = PM-only gapper (flat AH, exploded at PM open on 2.4M sh/bar / 22K trades) — undetectable AH, not counted vs baseline.
- AEMD = real AH→PM continuation, detected + entered (biggest genuine AH→PM mover, +76% PM peak, under 100% bar).
- NCPL = spike→fade round-trip, correctly skipped all night (VRatio ~0, AvgVol 61M, not real AH unusual activity).

### Open Position P&L (Alpaca)

| Ticker | Entry | Entry Total% | Catalyst | Entry Time | PM Peak | Peak Time | Exit | P&L | P&L % | Status |
|--------|-------|--------------|----------|------------|---------|-----------|------|-----|-------|--------|
| AEMD | $3.12 | +43.8% | None | 23:00 CET | $3.82 (SIP) | 04:00 ET | open | — | +3.8% live (~$3.24) | 🟢 Open, building |
| MODD | $4.18 | +15.8% | None | 00:30 CET | $3.93 (SIP, thin) | 04:00 ET | open | — | −6.2% (~$3.92) | 🔴 Open, faded |

**Quote-freshness note:** Alpaca reported AEMD $3.15 / +1.0% — slightly stale vs the live PM SIP ~$3.24 (+3.8%). AEMD PM peak $3.82 = +22.4% from entry. MODD PM is thin (5,708 sh first bar) at ~$3.92, below the $4.18 entry. No exits placed here — position-evaluation.md (10:30 CET) owns hold/sell.

**Total Realized P&L (Alpaca fills only): €0.00** (no exits yet)

### Scanner Effectiveness

- Evening scans ran: **6 of 7 scheduled** (21:30, 22:00, 22:30, 23:00, 00:00, 00:30 ran; **23:30 missing**; plus 2 bonus scans 22:15 & 22:45). Entry window (23:00–00:30 CET) fully covered — not a coverage failure.
- Candidates found: AEMD (all scans), MODD, NCPL, INHD, MI, MIMI, BRNX, RYET, WVVIP, CELU, MODD
- Retrospective matches: AEMD caught (entered); WHLR is a PM-only gapper (not an AH candidate).

### Missed Opportunities

No AH→PM detection miss. WHLR (+155% PM) was a PM-only gapper — structurally undetectable by the AH scanner, not a miss.

### AH Mover Follow-Through

| Ticker | AH Peak | Peak Time | AH Trajectory | Current PM | From Peak | From Close | Verdict |
|--------|---------|-----------|---------------|------------|-----------|------------|---------|
| AEMD | $3.46 (+59%) | 17:05 ET | Build | ~$3.24 (peak $3.82) | PM peak > AH peak | +49% | **Continued** — PM exceeded AH peak, entered @ $3.12 |
| MODD | $4.28 (+18%) | 17:15 ET | Late Build | ~$3.92 | −8% | +8% | **Faded** — AH peak was the better exit; entered @ $4.18, PM below entry |
| NCPL | ~$0.72 (+15%) | 17:10 ET | Spike→fade | $0.59 | −18% | +10% | **Faded** — correctly skipped all night |

**AH-peak-vs-PM-peak check:** AEMD PM peak ($3.82) **exceeded** its AH peak ($3.46) — a continuation, not a fade; not in the extreme (>~+130%) zone. MODD PM ($3.93) **fell short** of its AH peak ($4.28) — AH was the better exit (thin PM). Neither is an extreme-zone case. Extreme-zone tally unchanged: **8 fade / 1 continue**.

### Notes

- **PM-only gapper tracking:** WHLR = today's biggest raw mover, **+155% PM SIP** ($1.12 → $2.86), classification **PM-only gapper**, investability **holdable** (2.48M/1.74M sh across the first two 5-min bars, 22K/17K trades, sustained above +140% across bars — genuine liquid window). Not yet in `log/pm-open-scan.csv` (the Aug 28 pm-open pulse had not logged it by 04:20 ET). Standing holdable PM-only-gapper count in `pm-open-scan.csv`: **32** — well past the ≥3–4 threshold. Standing action unchanged: the holdable-PM-only-gapper cluster routes to Juan's daily email as an Initiative-6 decision (early-PM hypothetical-entry pilot), not applied here. Not a scanner failure, not counted vs baseline.
- **Multi-session-runner tracking:** both entries were **fresh first-day AH igniters** (AEMD Day% −4.8%, MODD Day% +9.1% — neither a prior-day runner). AEMD **ran** (PM peak +22.4% from entry); MODD **faded** (PM below entry, thin). Updated standing: **1 multi-session runner (1 faded: DAIC) / 3 first-day igniters (2 ran: WNW, AEMD; 1 faded: MODD).** Data collection only.
- **Fade-rule / reverse-split / broker-block / stale-book / float-gate / final-scan trackers:** no new cases tonight. MODD faded post-entry but float 7.6M (above the 3M sub-float bucket) and was entered, not skipped — not a fade-rule case. Sub-3M fade-rule count unchanged at 4 of 14 (below the ≥80% trigger). No reverse-split names entered.
- **In-window feed-lag miss** standing count unchanged at **4** (trigger REACHED — AH-data-source-verification recommendation stays routed to Juan's email). No new case tonight.
- **Scanner health:** clean night — AEMD detected across every AH scan and entered at the right level; the one detection-relevant name that exploded (WHLR) is a PM-only gapper outside the AH scanner's reach. 6 of 7 scheduled scans ran (23:30 dropped, entry window intact).

### Price Charts

```
AEMD  Prev Close $2.17 (Yahoo anchor $2.28) | 2-Day Range $2.18–$3.82
      AH SIP peak $3.46 (+59.4%) @17:05 ET → PM SIP peak $3.82 (+76.0%) @04:00 ET | Current ~$3.24
      Entered $3.12 → PM peak +22.4%. Continuation (PM > AH peak).

WHLR  Prev Close $1.12 (Yahoo $1.60 anchor stale) | 2-Day Range $1.08–$2.86
      AH flat $1.12–1.26 (no signal) → PM SIP peak $2.86 (+155%) @08:05 ET on 1.7–2.5M sh/bar
      PM-only gapper, holdable. Undetectable AH — not counted vs baseline.
```
