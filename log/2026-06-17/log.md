# Morning Evaluation - 2026-06-17

## Morning Evaluation — 10:25 CET

_Pulse 1. PM session only ~25 min old (now 04:25 ET). Peaks below are "so far"; position-evaluation (10:30/14:30 CET) tracks the rest of premarket and handles exits._

### Today's Winner

**LNAI** — Lunai Bioworks (Biotechnology)
- Catalyst: 8-K filed ~16:35 ET Jun 16 — regained Nasdaq $1.00 minimum bid-price compliance (1-year Panel monitor). Grade C (administrative, removes delisting overhang on a 2.9M float).
- Previous Close: $2.61
- AH last night: AH peak $6.42 (+146.0%) at 17:15 ET / 23:15 CET — clean BUILD from +12% (16:00) → +100% (17:00) → +146% (17:15), then held +90-115% through the rest of AH
- Premarket now: $6.82 (+161%), PM peak (5-min close) $7.12 (+172.9%) at 04:00 ET; intrabar touched ~$7.90
- Hypothetical P&L (AH entry → PM peak): realistic strategy entry $5.80 → PM peak $7.12 = **+22.8%**; earliest-AH hypothetical ($3.44 first appearance 23:00) → $7.12 = **+107%**
- Float: 2.9M | Market Cap: $12.9M | VRatio at entry 6.6x

**Co-winner: NIVF** — NewGenIvf Group (Medical/Nursing Services). Also detected and traded. Entry $0.81 → PM peak $1.55 (+91% from entry, +166.5% from close). 568K float, note/warrant buyback catalyst (Grade C). Late AH spike→hold ($0.96 +65% at 17:45 ET) carried into a much higher PM.

**Scanner Diagnostic:**
- Detectable at screening time? **YES** — and we acted on both. LNAI was the only BUILD candidate of the night; it cleared the 2-AH-scan gate at 23:30 CET (23:00 +20.9% → 23:30 +103.9%) and we entered $5.80. NIVF cleared the gate at 00:30 CET (00:00 +18.8% → 00:30 +16.4%) and we entered $0.81.
- LNAI at ~22:15 CET (23:00 scan): +20.9% AH on its 1st qualifying scan, BUILD trajectory climbing to new AH highs at 17:00 ET. Correctly held for a 2nd scan rather than chasing — it exploded to +103.9% at 23:30, confirming the BUILD before entry.
- Scanner gap: none. Both winners were caught and traded with the BUILD-and-hold + 2-scan logic working exactly as designed. Best-case night for the scanner.

**Biggest raw PM mover:** LNAI itself (+172.9% from close). **Classification: AH→PM continuation** (moved +146% in after-hours, fully detectable). NOT a PM-only gapper — today's single biggest mover was a continuation the AH scanner caught and traded. Running PM-only-gapper tally unchanged (CIIT, GLXG, TDIC).

### Baseline Tracking

- Days tracked: **32** (was 31 + 1)
- Winners detected by scanner: **28/32 (87.5%)** — HIT, SUNE, DRMA, UGRO, NXTT, POLA, BCG, PFSA, MASK, EZGO, AIIO, HTCO, WOK, LNKS, AMST, PHGE (May 20), PHGE (May 26), SNGX, ATPC, PRFX, DXST, TWAV, CHAI, MSW, TMDE, BYAH, CRVO, **LNAI** (NIVF also detected + traded)
- Winner selected for paper trade: **20/32 (62.5%)** — incremented; we entered LNAI (the winner) at $5.80 plus NIVF at $0.81
- Target: >80% detection
- Status: **BASELINE MET**

### Retrospective Scan Results

Live PM scan (04:21 ET, 6 hits): LNAI +153.4%, NIVF +77.1%, MCRP +42.8%, CREG +34.1%, GDHG +31.9%, OTLK +5.1%. AH reconstruction (`check-prices.py --ah-history`) confirms LNAI AH peak $6.42 (+146%) at 17:15 ET and NIVF AH peak $0.96 (+65%) at 17:45 ET. Both top PM movers map directly to last night's two paper-trade entries.

### Paper Trade P&L

| Ticker | Entry | Entry Total% | Catalyst | Entry Time | PM Peak | Peak Time | Exit | P&L | P&L % | Status |
|--------|-------|--------------|----------|------------|---------|-----------|------|-----|-------|--------|
| LNAI | $5.80 | +122.2% | C — 8-K Nasdaq bid-price compliance | 23:30 CET | $7.12 | 04:00 ET | — | +€17.34 | +17.6% | 🟢 Open |
| NIVF | $0.81 | +39.7% | C — note/warrant buyback (anti-dilution) | 00:30 CET | $1.55 | 04:10 ET | — | +€76.26 | +76.5% | 🟢 Open |

P&L shown at current PM prices (LNAI $6.82, NIVF $1.43, 04:24 ET). At PM peaks: LNAI +€22.44 (+22.8%), NIVF +€91.02 (+91.4%). PM is 25 min old — peaks are preliminary; exits handled by position-evaluation at 10:30/14:30 CET.

**Total Paper P&L (current): +€93.60** | at PM peaks: +€113.46

### Scanner Effectiveness

- Evening scans ran: 7 times (21:30 - 00:30 CET)
- Candidates found: ~25 unique tickers across the night
- Retrospective matches: **2/2** — both morning winners (LNAI, NIVF) were in the evening scans and both were entered

### Missed Opportunities

| Ticker | AH Change | Why Missed | Would Be Profitable? |
|--------|-----------|------------|---------------------|
| CRE | AH peak $4.65 (+48%) at 17:30, faded to $3.87 | Skipped on SPIKE→FADE rule | YES — PM peaked $5.99 (+90%); PM exceeded AH peak |
| CREG | 00:00 +8.7% (below 10%) → 00:30 +45.4% | Failed ≥2-AH-scan gate by one scan | YES — PM peaked $3.15 (+64%) |

CRE is a SPIKE→FADE-rule false negative: it faded in AH (correct skip per rule) but gapped to +90% in PM. CREG missed the 2-scan gate by a hair (8.7% vs 10% at 00:00) then surged. Both single cases; the fade rule still worked on MYSE/FLZH/GDHG (all faded). Track CRE-type cases — AH faders that re-explode in PM — to test whether the fade-skip rule needs a PM-gap exception.

### AH Mover Follow-Through

| Ticker | AH Peak | Peak Time | AH Trajectory | Current PM | From Peak | From Close | Verdict |
|--------|---------|-----------|---------------|------------|-----------|------------|---------|
| LNAI | $6.42 (+146%) | 17:15 ET | Build | $6.82 (+161%) | +6% | +161% | ✅ Continuation, PM>AH — traded, winning |
| NIVF | $0.96 (+65%) | 17:45 ET | Late surge→hold | $1.43 (+146%) | +49% | +146% | ✅ Continuation, PM>>AH — traded, winning |
| CRE | $4.65 (+48%) | 17:30 ET | Spike→fade | $5.67 (+80%) | +22% | +80% | ⚠️ PM>AH — ran despite AH fade; skipped on fade rule |
| CREG | ~$3.01 (+45%) | 18:30 ET | Late surge (1 scan) | $2.78 (+45%) | — | +64% | Continuation; watched, failed 2-scan gate |
| GDHG | $2.55 (+59%) | 16:40 ET | Spike→fade | $2.15 (+34%) | -16% | +34% | Partial PM bounce; AH faded, skipped (thin vol) |
| MYSE | $3.17 (+57%) | 16:25 ET | Spike→fade | $1.90 (-2.5%) | -40% | -2.5% | Faded — correctly skipped |
| FLZH | $6.19 (+93%) | 16:10 ET | Spike→fade | $3.30 (+3%) | -47% | +3% | Faded — correctly skipped |
| TDIC | $8.84 (+16%) | early AH | Spike→fade | $8.90 (+64%) | +1% | +64% | Yesterday's PM gapper, multi-day runner |
| SDOT | dead-cat (Total neg) | — | Bounce | $16.85 (-28%) | — | -28% | Far below close — correctly skipped |

**AH-peak-vs-PM-peak check:** LNAI ($7.12 PM > $6.42 AH), NIVF ($1.55 > $0.96), CRE ($5.99 > $4.65) all had PM peaks exceeding AH peaks = continuations, PM was the better exit. The fade names (MYSE, FLZH, GDHG) had AH peaks above PM = AH was the better exit, but they faded overall and were correctly skipped. No extreme AH runner (>250% from close) tonight, so no new MSW-pattern data point.

### Price Charts

**LNAI** — prev close $2.61, AH built to $6.42 (+146%) at 17:15 ET, held +90-115% overnight, PM opened $7.12 (+173%), now $6.82.
```
$   7.12 │                                                          █ 
         │                                                        ██ █
         │                                                     █ █    
         │                                                   ██       
         │                                            ███████         
$   2.50 │████████████████████████████████████████████                
         AH build 16:00→17:15 ($2.9→$6.4) ... hold ~$5 ... PM $7.1
```

**NIVF** — prev close $0.58, AH flat ~+20% then late spike $0.96 (+65%) at 17:45 ET, PM exploded to $1.55 (+166%), now $1.43.
```
$   1.55 │                                              (PM open)     
         │         █              █                                   
         │        █ ████        █ ████  ████████████ ████████         
$   0.55 │███████          ██                                         
         AH flat ~$0.70 → spike $0.96 → PM gap $1.5
```

### Notes

- **Best scanner night on record: 2/2 winners detected AND both traded.** The two biggest PM movers of the morning are exactly the two stocks we entered. The BUILD-and-hold + 2-AH-scan + hold-vs-fade logic selected both correctly and rejected every fade (MYSE, FLZH, GDHG all faded into PM as predicted).
- **CRVO multi-day runner:** yesterday's winner (sold in PM) is now $4.05 (+63% from $2.48) on Day 2 — kept running after our PM exit. Adds to the UGRO/AIIO multi-day-runner pattern (catalyst-light but low-float). Tracking in WINNERS_TRACKING.
- **CRE fade-rule false negative:** the one notable miss. AH faded (skip per rule) then PM-gapped +90%. First clear case of an AH-fader re-exploding in PM. Watch for repeats — if the pattern recurs, the SPIKE→FADE skip may need a "but re-check at PM open" exception.
- **PM-only-gapper tally unchanged** (CIIT, GLXG, TDIC). Today's biggest mover was an AH→PM continuation — a point in favor of the AH strategy being competitive with PM-only gappers.
- No CEILING-OVERRIDE or DEAD-CAT-OVERRIDE watch candidates were flagged last night (LNAI Total% +122% was under the +150% ceiling; SDOT never reclaimed above its close). Nothing to follow up on those datasets today.

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| LNAI | $5.80 | $6.43 | +10.9% | $7.12 | 1 | C | SELL | Grade C premarket exit at profit; PM pulse, +$10.71 |
| NIVF | $0.81 | $1.36 | +67.9% | $1.55 | 1 | C | SELL | Grade C premarket exit at profit; PM pulse, +$67.65 |

**Actions taken:**
- SELL LNAI 17 sh @ $6.43 → +$10.71 (+10.9%). Cost $98.60 → proceeds $109.31. Grade C premarket exit.
- SELL NIVF 123 sh @ $1.36 → +$67.65 (+67.9%). Cost $99.63 → proceeds $167.28. Grade C premarket exit.
- Both moved to Closed Positions. No open positions remaining.

**Session realized P&L: +$78.36** (LNAI +$10.71, NIVF +$67.65)

## Position Evaluation — 14:30 CET

No open positions. LNAI and NIVF both closed at the 10:30 CET evaluation (Grade C premarket exits at profit). Nothing to evaluate.

---

# Post-Market Screening - 2026-06-17

## Paper Trades

| Ticker | Entry Price | Entry Time | Shares (~€100) | Catalyst Grade | Reason |
|--------|-------------|------------|-----------------|----------------|--------|
| LPA | $5.21 | 23:00 CET | 19 | B | $145M asset sale (Lima logistics park to FIBRA Prime); cleared 2-AH-scan gate, holding within ~7% of AH high, float 5.1M, VRatio 6.4-7.7x |

## Scan 23:00 CET (5:00 PM ET)

**AH open ~1h. First entry-eligible scan of the night** (learning-phase rule: no entries before 23:00 CET).

Scanner returned **9 AH hits**:

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| LPA | [TV](https://www.tradingview.com/chart/?symbol=LPA) | $3.14 | -6.5% | +65.9% | $5.21 | +55.1% | 4.9M | 641K | 7.7x | 5.1M | Real Estate Development |
| BYAH | [TV](https://www.tradingview.com/chart/?symbol=BYAH) | $1.20 | -20.0% | +54.2% | $1.85 | +23.4% | 979K | 17.2M | 0.1x | 1.0M | Household/Personal Care |
| ATPC | [TV](https://www.tradingview.com/chart/?symbol=ATPC) | $2.73 | -3.5% | +17.6% | $3.21 | +13.4% | 2.3M | 543K | 4.3x | 475K | Pharmaceuticals: Other |
| LNKS | [TV](https://www.tradingview.com/chart/?symbol=LNKS) | $1.60 | -3.0% | +16.2% | $1.86 | +12.7% | 6.0M | 1.2M | 5.2x | 1.5M | Electronic Production Equipment |
| NXGL | [TV](https://www.tradingview.com/chart/?symbol=NXGL) | $0.61 | +15.1% | +15.9% | $0.71 | +33.3% | 218K | 243K | 0.9x | 7.1M | Chemicals: Specialty |
| SPRO | [TV](https://www.tradingview.com/chart/?symbol=SPRO) | $2.11 | -23.8% | +8.5% | $2.29 | -17.3% | 181K | 1.9M | 0.1x | 42.9M | Biotechnology |
| FTHM | [TV](https://www.tradingview.com/chart/?symbol=FTHM) | $1.11 | +75.4% | +6.3% | $1.18 | +86.4% | 1.2M | 9.0M | 0.1x | 19.3M | Packaged Software |
| WHLR | [TV](https://www.tradingview.com/chart/?symbol=WHLR) | $0.82 | -3.6% | +6.2% | $0.87 | +2.3% | 271K | 1.3M | 0.2x | 549K | Real Estate Investment Trusts |
| CHGG | [TV](https://www.tradingview.com/chart/?symbol=CHGG) | $1.03 | -11.2% | +5.8% | $1.09 | -6.0% | 58K | 1.2M | 0.0x | 101.9M | Misc Commercial Services |

**Gate check (float<50M, >10% AH in ≥2 AH scans [22:00+ CET], Day% >-15%):**
- **LPA ✅ ENTERED** — 22:30 +59.2%, 23:00 +65.9% (2 AH scans >10%). Float 5.1M, Day% -6.5%, Total% +55.1% (under +150% ceiling). AH peak $5.59 (+66%) at 16:25 ET, dipped to $4.65 (16:45) then rebuilt to $4.98 (17:00); current $5.21 = within ~7% of high and UP across the two AH scans ($5.00 → $5.21). Holding/building, not fading. Real volume (VRatio 6.4-7.7x). **Catalyst: $145M asset sale** — divesting Parque Logístico Lima Sur (Peru logistics park) to FIBRA Prime REIT, ~$85M net proceeds after debt, pending regulatory approval. Material for a $99M mcap company. **Grade B** (solid operational deal, pending approval — hold up to 2 days). Early-peak (16:25, before 17:30) is the one caution, but hold-vs-fade dominates and LPA is holding within 20% of high.
  - **Entry: $5.21, 19 sh, cost $98.99.**
- **LNKS — Skip (SPIKE→FADE).** Peaked $2.31 (+40%) at 16:05 ET, declined steadily to ~$1.78 then weak bounce to $1.86. Across AH scans: 22:30 +38.1% → 23:00 +16.2% = decline. Early peak + declining across scans = fade. SPIKE→FADE 0/10+ for PM continuation regardless of its 1.5M float / prior-winner status.
- **BYAH — Skip (dead-cat bounce, stale catalyst).** Day% -20.0% (below -15% gate). Started AH at -20%, spiked to +27% (16:45) then faded to +5% by 17:00. Only 1 AH scan, faded — does NOT meet dead-cat-override criteria (needs AH% rising across ≥2 AH scans while reclaiming above close). Catalyst is the June 12 Star Plus Action AI partnership = 5 days stale, not today's driver. No override flag.
- **ATPC — Skip.** Fails 2-scan gate (22:30 +8.9% below 10%, only 23:00 +17.6% qualifies) AND SPIKE→FADE (peaked $4.29 +51.6% at 16:20, faded to $3.11 by 17:00).
- **NXGL — Skip/watch.** Fails 2-scan gate (22:30 +6.4% below 10%, only 23:00 +15.9%). Thin AH volume (VRatio 0.9). Holding +22% but needs a 2nd qualifying scan.
- **SPRO, FTHM, WHLR, CHGG — Skip.** SPRO Total% -17.3% (negative, dead-cat, 42.9M float). FTHM AH only +6.3% (regular-session runner Day +75%, 19.3M float). WHLR/CHGG AH <7%, CHGG 101.9M float.

**Entered LPA only.** One BUILD/hold candidate cleared all gates; everything else was a fade, failed the 2-scan gate, or below the Day% floor. Not a skip-all night (LPA qualified).

## Scan 22:30 CET (4:30 PM ET)

**AH open ~30 min.** Observation-only per learning-phase rule (no entries before 23:00 CET).

Scanner returned **5 AH hits**:

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| LPA | [TV](https://www.tradingview.com/chart/?symbol=LPA) | $3.14 | -6.5% | +59.2% | $5.00 | +48.8% | 493K | 78K | 6.4x | 5.1M | Real Estate Development |
| LNKS | [TV](https://www.tradingview.com/chart/?symbol=LNKS) | $1.60 | -3.0% | +38.1% | $2.21 | +33.9% | 4.2M | 957K | 4.4x | 1.5M | Electronic Production Equipment |
| TGE | [TV](https://www.tradingview.com/chart/?symbol=TGE) | $1.08 | +12.5% | +18.5% | $1.28 | +33.3% | 2.9M | 1.4M | 2.1x | 44.2M | Financial Conglomerates |
| NXGL | [TV](https://www.tradingview.com/chart/?symbol=NXGL) | $0.61 | +15.1% | +6.4% | $0.65 | +22.4% | 51K | 226K | 0.2x | 7.1M | Chemicals: Specialty |
| ATPC | [TV](https://www.tradingview.com/chart/?symbol=ATPC) | $2.73 | -3.5% | +8.9% | $2.97 | +5.0% | 116K | 264K | 0.4x | 475K | Pharmaceuticals: Other |

**AH trajectory check (check-prices.py --ah-history):**
- **LPA** — $3.14 → jumped to $5.00 at 16:10, peaked **$5.60 (+66.7%) at 16:25 ET**, holding $5.59. **BUILD pattern**, real volume (VRatio 6.4), 5.1M float. Best candidate of the night so far — watch for 23:00 confirmation.
- **LNKS** — peaked $2.31 (+40%) at 16:05 ET, faded to $2.06 (+24.9%) by 16:30. **SPIKE→FADE** so far. Prior winner (May), 1.5M float — watch whether it rebuilds.
- **TGE** — peaked $1.40 (+45.8%) at 16:05 ET, faded to $1.25 (+30.2%) by 16:30. **SPIKE→FADE**, 44.2M float (high).
- **NXGL / ATPC** — thin AH volume (VRatio 0.2-0.4x), small AH change. Noise unless volume builds.

No entries (observation-only). LPA is the lone BUILD candidate; need a 2nd qualifying AH scan (≥10% AH) before any entry at 23:00+. Re-evaluate at 23:00 CET.

## Scan 22:00 CET (4:00 PM ET)

**AH open.** First after-hours scan of the night. Observation-only per learning-phase rule (no entries before 23:00 CET).

Scanner returned **0 AH hits**. None of the 21:30 regular-session watch candidates (EHGO, CIIT, ICCM, VIIQ, CFOR, EMSKF, YMAT, RBLK) carried into the after-hours scan with qualifying volume/change at AH open. The thin-print names (ICCM, VIIQ, CFOR, EMSKF, YMAT, RBLK) appear to have been illiquid regular-session prints that didn't continue. EHGO and CIIT (the two real-volume names) also did not register in the AH scan.

No candidates. Re-evaluate at 22:30 and 23:00 CET.

## Scan 21:30 CET (3:30 PM ET)

**Regular session still open** (AH opens 22:00 CET / 4:00 PM ET). Watch-only per regular-session caution rule — no entries. Candidates flagged below only enter if they reappear in an AH scan (22:00+ CET) with sustained momentum.

Scanner returned 55 regular-session hits. Most high-% movers have tiny 5-min volume (thin/illiquid prints — ICCM 170 sh, VIIQ 300 sh, CFOR 400 sh, EMSKF 500 sh, YMAT 650 sh) and are not reliable signals. Notable candidates with real volume or extreme moves:

| Ticker | Chart | Price | Day% | 5mVol | Avg5m | IRVol | Float | MCap | Industry |
|--------|-------|-------|------|-------|-------|-------|-------|------|----------|
| EHGO | [TV](https://www.tradingview.com/chart/?symbol=EHGO) | $2.58 | +95.5% | 47K | 113K | 780.5 | 1.3M | $2.7M | Wholesale Distributors |
| CIIT | [TV](https://www.tradingview.com/chart/?symbol=CIIT) | $0.64 | +45.2% | 54K | 70K | 3.0 | 1.3M | $2.3M | Air Freight/Couriers |
| ICCM | [TV](https://www.tradingview.com/chart/?symbol=ICCM) | $6.47 | +203.8% | 170 | 328K | 1313.6 | 1.2M | $6.0M | Medical Specialties |
| VIIQ | [TV](https://www.tradingview.com/chart/?symbol=VIIQ) | $1.00 | +376.2% | 300 | 432 | 0.9 | 2.1M | $2.1M | Financial Conglomerates |
| CFOR | [TV](https://www.tradingview.com/chart/?symbol=CFOR) | $2.00 | +300.0% | 400 | 408 | 0.9 | 3.7M | $24.4M | Misc Commercial Services |
| EMSKF | [TV](https://www.tradingview.com/chart/?symbol=EMSKF) | $0.50 | +233.3% | 500 | 1K | 1.0 | 11.4M | $1.9M | Precious Metals |
| YMAT | [TV](https://www.tradingview.com/chart/?symbol=YMAT) | $0.94 | +143.9% | 650 | 1.6M | 43.5 | 7.9M | $7.7M | Electrical Products |
| RBLK | [TV](https://www.tradingview.com/chart/?symbol=RBLK) | $1.60 | +110.1% | 500 | 530 | 0.8 | 596K | $956K | Packaged Software |

**Watch — pending AH confirmation:**
- **EHGO** ($2.58, +95.5%, 1.3M float) — best regular-session signal: real volume (47K 5m), low float, strong move. Watch for AH carry-through.
- **CIIT** ($0.64, +45.2%, 1.3M float) — real volume (54K 5m), low float. Note: CIIT was a prior PM-only gapper in earlier retrospectives; watch AH behavior.
- **ICCM** ($6.47, +203.8%) — huge IRVol but VChg -100% (fading) and only 170 sh in last 5m. Likely halt/thin print. Watch only if AH shows real volume.
- **VIIQ / CFOR / EMSKF / YMAT / RBLK** — extreme % moves on negligible volume (300-650 sh). Treat as noise unless AH brings genuine volume.

No paper trades entered (regular session). Re-evaluate at 22:00+ CET AH scans.
