# Morning Evaluation - 2026-06-18

## Morning Evaluation — 10:25 CET

_Pulse 1. PM session only ~25 min old (now 04:25 ET). Peaks below are "so far"; position-evaluation (10:30/14:30 CET) tracks the rest of premarket and handles the LPA exit._

### Today's Winner

**LNKS** — Linkers Industries (Electronic Production Equipment)
- Catalyst: none verified. Low-float (1.5M) repeat runner — was a prior winner May 13 (faded to $1.35). No fresh PR found; fits the no-catalyst low-float momentum-pump pattern.
- Previous Close: $1.65 (June 17 regular close)
- AH last night: AH peak $2.31 (+40.0%) at **16:05 ET** (very first bar), then faded/chopped $1.76-2.12 the rest of AH — classic SPIKE→FADE, never reclaimed the high
- Premarket now: opened $3.52 (+113.1%) at 04:00 ET, **PM peak $4.70 (+184.7%) at 04:15 ET** (5-min close; intrabar ~$4.97 / +201%), now $4.32
- Hypothetical P&L (AH entry → PM peak): realistic AH entry at the faded base ~$2.00 → PM peak $4.70 = **+135%**
- Float: 1.5M | Market Cap: $2.8M | VRatio (PM) 2.1x

**Scanner Diagnostic:**
- Detectable at screening time? **YES** — LNKS was in every single evening scan (22:30 → 00:30 CET).
- What it looked like at ~22:15 CET (23:00 scan): +16.2% AH, but the AH history showed AH high $2.31 at **16:05 ET** (first bar) with a steady decline to ~$1.78 = **SPIKE→FADE**. Across scans it went 22:30 +38.1% → 23:00 +16.2% (declining). We **correctly skipped it on the SPIKE→FADE rule** (early peak, never made a new AH high, chopping at a base below the high — historically 0/10+ for PM continuation).
- It then re-exploded +184.7% in premarket. This is a **fade-rule false negative** — the 2nd case after CRE (Jun 17, AH +48% faded → PM +90%).
- Scanner gap: none on detection. The gap is in the **entry rule**: the SPIKE→FADE skip misses AH-faders that re-ignite at PM open. Tally these (now CRE + LNKS = 2). A single PM re-check exception is not yet justified — the fade rule correctly skipped ATPC and TGE the same night (both faded, PM stayed below AH peak). Only a recurring pattern (≥4/5) warrants a rule change.

**Biggest raw PM mover:** LNKS itself (+184.7% from close). **Classification: AH→PM continuation** (moved +40% in after-hours, fully detectable and detected). NOT a PM-only gapper. Running PM-only-gapper tally unchanged (CIIT, GLXG, TDIC).

**The winner we DID trade: LPA** — the #2 mover and the clean strategy-fit winner. AH BUILD to $5.59 (+66%) at 16:25 ET, held +50-60% all night, PM opened $6.39 (+90%) at 04:00 ET. Entered $5.21 (Grade B, $145M asset sale). Still open, up ~+6% at current PM price; PM peak gave +22.6% (intrabar $7.77 print = +49%). The scanner + BUILD-and-hold rules picked LPA correctly; it was simply not the single biggest mover of the morning.

### Baseline Tracking

- Days tracked: **33** (was 32 + 1)
- Winners detected by scanner: **29/33 (87.9%)** — HIT, SUNE, DRMA, UGRO, NXTT, POLA, BCG, PFSA, MASK, EZGO, AIIO, HTCO, WOK, LNKS, AMST, PHGE (May 20), PHGE (May 26), SNGX, ATPC, PRFX, DXST, TWAV, CHAI, MSW, TMDE, BYAH, CRVO, LNAI, **LNKS (Jun 18)**
- Winner selected for paper trade: **20/33 (60.6%)** — not incremented. Today's biggest winner (LNKS) was correctly skipped on the SPIKE→FADE rule; we traded LPA (the #2 mover / clean build winner) instead.
- Target: >80% detection
- Status: **BASELINE MET**

### Retrospective Scan Results

Live PM scan (04:22 ET, 6 hits): LNKS +131.9% ($3.71), BYAH +56.7% ($1.88), SPRO +20.4%, CAST +19.4%, LPA +79.9% ($5.65), CTNT +11.7%. Forced AH scan (04:23 ET): **0 hits** (expected — overnight TradingView postmarket fields return empty, as documented). AH reconstruction (`check-prices.py --ah-history`) confirms LNKS AH peak $2.31 (+40%) at 16:05 (faded) and LPA AH peak $5.59 (+66%) at 16:25 (build/hold). The two top PM movers map to last night's skip (LNKS, fade rule) and entry (LPA).

### Paper Trade P&L

| Ticker | Entry | Entry Total% | Catalyst | Entry Time | PM Peak | Peak Time | Exit | P&L | P&L % | Status |
|--------|-------|--------------|----------|------------|---------|-----------|------|-----|-------|--------|
| LPA | $5.21 | +65.9% | B — $145M asset sale (Lima logistics park) | 23:00 CET | $6.39 | 04:00 ET | — | +€6.27 | +6.3% | 🟢 Open |

P&L at current PM price (LPA $5.54, 04:25 ET). At PM peak $6.39: +€22.42 (+22.6%); intrabar $7.77 print would have been +€48.64 (+49.1%). PM is 25 min old — exit handled by position-evaluation at 10:30/14:30 CET.

**Total Paper P&L (current): +€6.27** | at PM peak: +€22.42

### Scanner Effectiveness

- Evening scans ran: 7 times (21:30 - 00:30 CET)
- Candidates found: ~25 unique tickers across the night
- Retrospective matches: **2/2** — both top PM movers (LNKS, LPA) were in the evening scans. LPA entered; LNKS skipped on fade rule.

### Missed Opportunities

| Ticker | AH Change | Why Missed | Would Be Profitable? |
|--------|-----------|------------|---------------------|

No scanner-missed opportunities — every PM mover (LNKS, LPA, BYAH, ATPC) was in the evening scans. LNKS was skipped by the SPIKE→FADE **rule**, not missed by the scanner (tracked as a fade-rule false negative below).

### AH Mover Follow-Through

| Ticker | AH Peak | Peak Time | AH Trajectory | Current PM | From Peak | From Close | Verdict |
|--------|---------|-----------|---------------|------------|-----------|------------|---------|
| LPA | $5.59 (+66%) | 16:25 ET | Build→hold | $5.54 (+76%) | -1% | +76% | ✅ Continuation, PM>AH — traded, open +6% |
| LNKS | $2.31 (+40%) | 16:05 ET | Spike→fade | $4.32 (+162%) | +87% | +162% | ⚠️ Fade-rule false negative — skipped, PM>>AH |
| BYAH | $1.91 (+27%) | 16:45 ET | Spike→fade | $1.80 (+50%) | -6% | +50% | Dead-cat skip (Day -20%) bounced in PM; PM≈AH |
| ATPC | $4.29 (+52%) | 16:20 ET | Spike→fade | $3.73 (+32%) | -13% | +32% | ✅ Fade rule worked — PM stayed below AH peak |
| TGE | $1.40 (+46%) | 16:05 ET | Spike→fade | $1.15 (+6%) | -18% | +6% | Faded — correctly skipped (44.2M float) |

**AH-peak-vs-PM-peak check:** LNKS ($4.70 PM > $2.31 AH) and LPA ($6.39 > $5.59) had PM peaks above AH = continuations, PM the better exit. ATPC ($3.73 < $4.29) and TGE ($1.15 < $1.40) had AH peaks above PM = fades, AH was the better exit and both were correctly skipped. BYAH PM≈AH. No extreme AH runner (>250% from close) tonight, so no new MSW-pattern data point.

### Price Charts

**LNKS** — prev close $1.65, AH spiked $2.31 (+40%) at 16:05 (first bar) then faded/chopped $1.76-2.12 all night, PM gapped to $3.52 (+113%) and ran to $4.70 (+185%) at 04:15 ET.
```
$   4.70 │                                                    █        
         │                                                  ██ █       
         │                                                 █           
         │    █                                          ██            
         │   █ ████████   ██   ████  ███████████████████              
$   1.65 │███          ███  ███    ██                                  
         AH: spike $2.31 → fade/chop ~$1.9 ... PM gap $3.5 → $4.7
```

**LPA** — prev close $3.36, AH built to $5.59 (+66%) at 16:25, held $5.0-5.4 all night, PM opened $6.39 (+90%, intrabar $7.77) then settled ~$5.5.
```
$   6.39 │                                            █                
         │                                        ████ ███            
         │      ███████████████████████████████████                   
         │     █                                                       
$   3.14 │█████                                                        
         AH build 16:10→16:25 ($3.1→$5.6) ... hold ~$5.2 ... PM $6.4
```

### Notes

- **Fade-rule false negative #2: LNKS.** AH spiked +40% at the first bar (16:05 ET) and faded — a textbook SPIKE→FADE skip — then PM-exploded to +184.7%. This follows CRE (Jun 17, AH +48% faded → PM +90%). **Running AH-fader-re-explode tally: CRE, LNKS = 2.** Still below the ≥4/5 threshold to add a PM-open re-check exception. Same night, the fade rule correctly skipped ATPC (PM +32% < AH +52%) and TGE (PM +6% < AH +46%), so the rule is still net-correct. Keep tracking; if it hits 4/5, add a "re-check AH-faders at PM open" exception.
- **LPA (our trade) is the clean win.** AH build-and-hold → PM continuation, exactly the strategy pattern. Open and green; position-eval handles the PM exit. PM intrabar touched $7.77 (a thin opening print) but the reliable 5-min PM peak is $6.39 (+90%).
- **BYAH dead-cat skip bounced +50% in PM.** It was correctly skipped (Day% -20%, below the -15% gate, and it never reclaimed above its close across AH scans, so no dead-cat-override flag). The PM bounce is noise on a no-catalyst low-float name — not a strategy miss. No override-watch tally entry (it never met the reclaim-above-close criterion).
- **No CEILING-OVERRIDE or DEAD-CAT-OVERRIDE watch candidates** were flagged last night. Nothing to follow up on those datasets today.
- **PM-only-gapper tally unchanged** (CIIT, GLXG, TDIC). Today's biggest mover (LNKS) was an AH→PM continuation the scanner detected.
- **Multi-day check:** LNAI faded $7.12 PM peak → $2.85 close (PM bounce to $3.66) and NIVF $1.55 → $0.70 (PM $0.78) — both faded hard after our Jun 17 PM exits, confirming the premarket-exit discipline. CRVO Day 3: ~$3.8 PM (off its $4.52 close but still +50% above its $2.48 origin) — low-float multi-day runner continuing.
</content>
</invoke>

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| LPA | $5.21 | $5.26 | +1.0% | $6.39 (+22.6%) | 1 | B | HOLD | Within Grade B 2-day window; peak +22.6% below +30% trail trigger; hard stop $4.43 not hit; catalyst intact |

**Actions taken:**
- Updated LPA peak to $6.39 (PM high 08:00 ET, above prior $5.59 AH high)
- No sells, no trail stop activated (peak P&L +22.6% < +30% threshold)

## Position Evaluation — 14:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| LPA | $5.21 | $4.21 | -19.2% | $7.77 (+49%) | 1 | B | SELL | Hard stop ($4.43) breached |

**Actions taken:**
- SOLD LPA @ $4.21 (19 sh) → -$19.00 (-19.2%). Hard stop -15% ($4.43) breached. PM spiked to $7.77 (+49% from entry) at 08:00 ET but evaluation windows missed the peak; faded below stop by midday.
- No remaining open positions.
