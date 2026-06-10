# Trade Log — 2026-06-10

## Morning Evaluation — 10:20 CET

### Today's Winner

**MSW** — Ming Shing Group Holdings (Engineering & Construction)
- Catalyst: GlobeNewswire — "Closing of the Acquisition of PMA Nano Carbon Tech Limited and Issuance of Unsecured Convertible Promissory Notes." Operational acquisition close (A-type) paired with dilutive convertible notes (D-type). Net **Grade C**.
- Previous Close: $1.32
- AH last night: peaked **$5.18 (+292%)** at ~18:00 ET (00:00 CET); verified 5m AH high $4.93 (+273.5%) at 18:05 ET
- Premarket now: **$3.51 (+166%)** at 04:21 ET; PM high $4.24 (+221%) at 04:00 ET (10:00 CET), now fading
- Hypothetical P&L (AH scanner-detection entry ~$2.18 at 23:00 CET → AH peak $5.18): **+138%**; → PM peak $4.24: **+94%**
- Float: 4.6M | Market Cap: $17.1M

**Scanner Diagnostic:**
- Detectable at screening time? **YES**
- The scanner not only detected MSW — **we entered it** ($3.24, 30 shares, 23:30 CET). It was caught at the 23:00 CET (17:00 ET) entry-eligible scan at +25.8%, confirmed its 2nd AH scan at 23:30 (+65.2%, peak +145%), and qualified the full entry gate (float <50M, AH >10% across 2 scans, Day +0.0%, BUILD-and-hold making new highs).
- Note on the literal 22:15 CET screening: MSW was still flat ($1.32) at 16:15 ET — the AH move only began at 16:30 ET (+28%). A single 22:15 snapshot would have missed it; the **recurring evening scans caught it cleanly** the moment volume built. This is exactly what the multi-scan cadence is for.
- Scanner gap: **none** — this is a textbook detection + selection success.

**Key deviation from the usual pattern:** MSW peaked in **after-hours** ($5.18), and the PM peak ($4.24) was *lower*. The strategy's core thesis (AH spike → PM continuation/peak) did NOT hold here — the best exit was last night in AH, not premarket. Track whether late-BUILD names that peak >250% in AH tend to fade rather than continue into PM.

### Baseline Tracking

- Days tracked: **28** (was 27 + 1)
- Winners detected by scanner: **24/28 (85.7%)** — HIT, SUNE, DRMA, UGRO, NXTT, POLA, BCG, PFSA, MASK, EZGO, AIIO, HTCO, WOK, LNKS, AMST, PHGE (May 20), PHGE (May 26), SNGX, ATPC, PRFX, DXST, TWAV, CHAI, **MSW**
- Winner selected for paper trade: **18/28 (64.3%)** — incremented (MSW: detected AND traded as the actual day's winner)
- Target: >80% detection
- Status: **BASELINE MET** (85.7%)

### Retrospective Scan Results

Live premarket scan (04:20 ET): MSW +222%, HWH +165.8%, CIIT +140%, PAVS +45.1%, AZI +29.7%, GMEX +27.8%.

AH reconstruction (`check-prices.py --ah-history`):
- **MSW** — AH high $4.93 (+273.5%) at 18:05 ET. Built late: flat until 16:30, ramped steadily through the session. BUILD. ← winner, traded.
- **HWH** — AH high $3.78 (+223%) at 19:00 ET. Flat (~+17%) until 18:45, then a **late surge** to +223%. Main move came at 18:45–19:00 ET (00:45–01:00 CET), *after* our 00:30 last scan.
- **CIIT** — AH essentially flat (peak +14.9%). Its +140% PM move was **PM-only**, not an AH→PM pattern.

### Paper Trade P&L

| Ticker | Entry | Entry Total% | Catalyst | Entry Time | PM Peak | Peak Time | Exit | P&L | P&L % | Status |
|--------|-------|--------------|----------|------------|---------|-----------|------|-----|-------|--------|
| MSW    | $3.24 | +145.5% | C — acquisition close + dilutive notes | 23:30 CET | $4.24 | 04:00 ET (10:00 CET) | (open) | +€8.10 | +8.3% | 🟢 Open |

Current price $3.51 (+8.3% over entry, +€8.10 unrealized on 30 sh). PM peak $4.24 was +30.9% over entry; AH peak $5.18 was +59.9% over entry (best exit window was AH last night). **Exit decision handled by position-evaluation.md (10:30 / 14:30 CET) — not this prompt.**

**Total Paper P&L (open): +€8.10**

### Scanner Effectiveness

- Evening scans ran: 7 times (21:30 – 00:30 CET)
- Candidates found: ~16 unique tickers
- Retrospective matches: winner MSW caught and traded; HWH partially caught (late surge after last scan); CIIT was PM-only.

### Missed Opportunities

| Ticker | AH Change | Why Missed | Would Be Profitable? |
|--------|-----------|------------|---------------------|
| HWH | +223% (peak 19:00 ET) | Main surge at 18:45–19:00 ET, **after** the 00:30 CET last scan; earlier scans showed only +10–12% (below conviction threshold) | Yes in AH→AH, but one-position rule (MSW open) blocked entry regardless |
| CIIT | flat AH (+14.9%) | Not an AH→PM pattern — move was PM-only | N/A — would not qualify |

No missed AH→PM winner: the night's clear winner (MSW) was caught and traded.

### AH Mover Follow-Through

| Ticker | AH Peak | Peak Time | AH Trajectory | Current PM | From Peak | From Close | Verdict |
|--------|---------|-----------|---------------|------------|-----------|------------|---------|
| MSW | $5.18 | 18:00 ET | Build (25.8→65→170→262%) | $3.51 | -32% | +166% | Peaked in AH; fading into PM (AH was the better exit) |
| HWH | $3.78 | 19:00 ET | Late surge (flat +17% → +223% at 18:45+) | ~$2.37 | -37% | +102% | Late surge, faded into PM but still well above close |
| AZI | $2.40 | — | Spike→hold (microstructure/Nasdaq-compliance) | $3.03 | +26% | +64% | Re-accelerated in PM; non-operational catalyst |
| UK | $3.78 | 17:10 ET | Spike→fade (dead-cat, Day -12.2%, no catalyst) | $2.69 | -29% | -9% | **Dead-cat confirmed** — no follow-through, below close |

### Notes
- **Textbook night for the scanner:** the day's biggest AH→PM mover (MSW) was detected through the recurring evening cadence and traded at $3.24. Baseline holds at 85.7%.
- **Pattern flag — AH peak vs PM peak:** MSW peaked in AH (+292%) and the PM peak was *lower* (+221%). When a late-BUILD name runs extremely hot in AH (>250%), the PM continuation may be weaker than the AH high. Collect more cases before promoting; if it recurs, it argues for taking partial profit in late AH rather than waiting for PM.
- **UK dead-cat case** played out as expected: Day -12.2% recovery with no catalyst → faded below prev close in PM. Validates the dead-cat skip rule.
- No CEILING-OVERRIDE WATCH candidates were flagged in last night's log (CHAI was referenced only as the prior Jun 8 case). Nothing to tally this morning.

### Price Charts

```
MSW — 2-Day Timeline (5-min)
Prev Close $1.32 | Current $3.51 (+166%)
AH path:  $1.32 (flat to 16:30) → $2.66 (16:50) → $3.24 entry (17:30) → $4.93–5.18 peak (18:00–18:05) → drifted $3.7–4.3 into 20:00
PM path:  $4.24 (04:00, PM high) → $3.98 → $3.76 → $3.56 → $3.42 → $3.51 (04:21)  [fading]
Verdict:  BUILD-and-hold that peaked in AH; PM opened near $4.24 then faded.
```

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| MSW | $3.24 | $3.53 | +9.0% | $5.72 | 1 | C | SELL | Grade C = exit in first premarket pulse; in profit and fading from peak ($4.93 AH → $4.24 → $3.53) |

**Actions taken:**
- SOLD MSW: 30 sh @ $3.53, realized **+$8.70 (+9.0%)**, 1 day held. Locked gain per Grade C premarket-exit rule.
- Moved MSW to Closed Positions; dropped BIYA from the last-10 table.
- No open positions remaining.

**Note:** Confirms the morning pattern flag — MSW peaked in AH ($5.18 / +60% over entry), not PM. PM peak only $4.24 (+31%), then steady fade. The Grade C "exit in premarket" rule captured a smaller but positive gain; the best exit was last night in AH.

## Position Evaluation — 14:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| _(none)_ | | | | | | | | No open positions |

**Actions taken:**
- No open positions to evaluate (MSW closed at 10:30 CET). No action.
