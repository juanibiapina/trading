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
