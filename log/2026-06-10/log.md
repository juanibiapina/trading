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

---

# Post-Market Screening — 2026-06-10

## Scan 21:30 CET (3:30 PM ET)

**Session: REGULAR (pre-AH).** AH opens at 22:00 CET / 4:00 PM ET. Per the regular-session caution rule, **no paper trade entries** — candidates are watch-only pending AH confirmation. Stocks that spike intraday but don't carry into AH tend to fade.

Scanner returned 62 hits, but most high-% rows are single-print artifacts (5mVol 100–500 shares with VChg ~−99%, e.g. DSY +411%, VSME +189%, CPOP +401%, CNET +42%). Filtering for real sustained volume and reasonable float:

| Ticker | Chart | Price | Day% | 5mVol | Avg5m | IRVol | Float | MCap | Industry | Note |
|--------|-------|-------|------|-------|-------|-------|-------|------|----------|------|
| CIIT | [TV](https://www.tradingview.com/chart/?symbol=CIIT) | $1.92 | +60.0% | 41K | 57K | 1025 | 1.3M | 6.9M | Air Freight/Couriers | Stale — ran in 06-09 AH; multi-day runner |
| HWH | [TV](https://www.tradingview.com/chart/?symbol=HWH) | $1.69 | +38.0% | 18K | 21K | 461 | 1.5M | 12.6M | Financial Conglomerates | Stale — +210% in 06-09 AH; multi-day runner |
| WCT | [TV](https://www.tradingview.com/chart/?symbol=WCT) | $1.92 | +46.6% | 11K | 61K | 6.5 | 849K | 5.9M | Packaged Software | Vol fading (−89% VChg); low float |
| HXHX | [TV](https://www.tradingview.com/chart/?symbol=HXHX) | $0.79 | +55.5% | 7K | 69K | 10.0 | 4.0M | 10.9M | Trucking | Vol fading (−80% VChg) |
| GLAI | [TV](https://www.tradingview.com/chart/?symbol=GLAI) | $0.90 | +50.0% | 2K | 2K | 6.4 | 14.4M | 139.4M | Misc Commercial Svcs | High float/MCap; thin vol |
| MSW | [TV](https://www.tradingview.com/chart/?symbol=MSW) | $1.57 | +19.3% | 2K | 31K | 81.2 | 4.6M | 20.4M | Engineering & Construction | Already traded last night; faded from $5.18 AH peak |

**Watch assessment:**
- **CIIT** — low float (1.3M), highest IRVol on the board, but already ran in 06-09 AH (peak +12.5% then PM-only continuation). Today's +60% is a multi-day extension, fails "first day of unusual activity." Watch only if it builds *fresh* AH volume tonight.
- **HWH** — surged +210% in 06-09 AH (late, 18:45–19:00 ET), faded into PM. Today +38% is a continuation. Same stale-runner concern. Watch for fresh AH build.
- **WCT / HXHX** — both fading volume into the close; unlikely AH follow-through. Low priority.
- Remaining rows are single-print artifacts or high-float/MCap — not actionable.

**Decision:** No entries (pre-AH). Re-scan at 22:00+ CET once after-hours opens; only enter a candidate that shows *fresh* sustained AH momentum (float <50M, AH >10% across ≥2 AH scans, Day% > −15%, BUILD/hold pattern). Prefer fresh first-day setups over CIIT/HWH multi-day extensions.

## Scan 22:00 CET (4:00 PM ET)

**Session: AFTERHOURS (just opened, 16:00 ET).** Observation-only per learning-phase default — no entries before 23:00 CET.

`scan.py --all`: **0 hits.** AH session opened seconds ago (16:00:19 ET); no after-hours bars have printed yet, so nothing to evaluate.

**Prior watch candidates (21:30) — regular-session outcome:** all faded into the close, confirming the regular-session caution. None carried momentum to support AH follow-through:

| Ticker | Prev Close | Day High | Reg Close | Verdict |
|--------|-----------|----------|-----------|---------|
| CIIT | $1.20 | $4.65 | $1.61 (+34%) | Spiked intraday to $4.65, dumped to close near lows — faded |
| HWH | $1.22 | $2.60 | $1.42 (+16%) | Faded from $2.60 high to close |
| WCT | $1.31 | $3.90 | $1.71 (+30%) | Big intraday spike to $3.90, gave it all back |
| MSW | $1.32 | $2.18 | $1.35 (+2%) | Yesterday's trade — dead, back near flat |

**Decision:** No entries (AH just opened, 0 scanner hits). Re-scan at 22:30 / 23:00 CET once after-hours volume builds. Watch for *fresh* first-day AH momentum (float <50M, AH >10% across ≥2 AH scans, Day% > −15%, BUILD/hold). The stale multi-day runners (CIIT, HWH) and the faded intraday spikers (WCT) are low priority unless they build genuinely new AH volume.

## Scan 22:30 CET (4:30 PM ET)

**Session: AFTERHOURS (16:30 ET, 30 min in).** Observation-only per learning-phase default — no entries before 23:00 CET.

`scan.py --all`: **3 hits.** All three are *new* (not in 21:30 / 22:00 scans). The stale runners CIIT/HWH/WCT did not reappear.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| DAIC | [TV](https://www.tradingview.com/chart/?symbol=DAIC) | $1.85 | -4.1% | +77.8% | $3.29 | +70.5% | 2.1M | 3.8M | 0.5x | 721K | Miscellaneous |
| FLYE | [TV](https://www.tradingview.com/chart/?symbol=FLYE) | $2.00 | +14.3% | +44.0% | $2.88 | +64.6% | 237K | 52K | 4.5x | 1.5M | Motor Vehicles |
| SCKT | [TV](https://www.tradingview.com/chart/?symbol=SCKT) | $0.95 | +12.8% | +6.3% | $1.01 | +19.9% | 94K | 344K | 0.3x | 5.4M | Computer Peripherals |

**AH trajectory (check-prices --ah-history):**
- **DAIC** — spiked to +69.9% ($3.28) at **16:10 ET**, faded to +40%, chopped back to +60%, now +54.6% at 16:30. Early peak, choppy. Float 721K (very low). VRatio 0.5x (AH vol below avg — weak). SPIKE→chop so far.
- **FLYE** — spiked to +97% ($3.45) at **16:15 ET**, faded hard to +56-57% and flat since. Early peak, SPIKE→FADE so far. Float 1.5M, VRatio 4.5x (genuine fresh AH volume). Day +14.3%.
- **SCKT** — only +6.3% AH (below 10% threshold), VRatio 0.3x. Not actionable.

**Catalyst search (DAIC, FLYE — both >10% AH):**
- **FLYE** — next earnings Jun 30, 2026 (not today). No same-day press release or 8-K surfaced (tavily/brave, freshness day). **No catalyst found so far.** EV bike maker; the +14.3% regular Day% + AH spike with 4.5x VRatio suggests a real driver but none located within search budget.
- **DAIC** — CID HoldCo. **No catalyst found** (no results on tavily/brave). Day% -4.1% (was red in regular session, then AH spike — possible dead-cat character given the red day). Very low float (721K).

**Decision:** No entries (observation-only, before 23:00 CET). Both DAIC and FLYE peaked very early (16:10-16:15 ET) and are fading from their AH highs — early-peak-fading is 0/7 for PM continuation. Will re-evaluate at 23:00 CET: re-run catalyst search (PRs often appear 15-30 min after 4:00 PM ET) and check whether either rebuilds toward its AH high or keeps fading. FLYE has the better volume profile (4.5x VRatio, green Day%); DAIC's red Day% + sub-1x VRatio is a dead-cat/weak-volume concern.

## Scan 23:00 CET (5:00 PM ET)

**Session: AFTERHOURS (17:00 ET, 1h in). Entry-eligible scan.** `scan.py --all`: **10 hits.**

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| DAIC | [TV](https://www.tradingview.com/chart/?symbol=DAIC) | $1.85 | -4.1% | +61.1% | $2.98 | +54.4% | 5.3M | 4.2M | 1.2x | 721K | Miscellaneous |
| FLYE | [TV](https://www.tradingview.com/chart/?symbol=FLYE) | $2.00 | +14.3% | +24.0% | $2.48 | +41.7% | 2.7M | 362K | 7.4x | 1.5M | Motor Vehicles |
| HWH | [TV](https://www.tradingview.com/chart/?symbol=HWH) | $1.42 | +15.9% | +21.8% | $1.73 | +41.2% | 828K | 3.5M | 0.2x | 1.5M | Financial Conglomerates |
| EDHL | [TV](https://www.tradingview.com/chart/?symbol=EDHL) | $3.50 | +12.9% | +22.0% | $4.27 | +37.7% | 680K | 6.5M | 0.1x | 0 | Advertising/Marketing |
| WCT | [TV](https://www.tradingview.com/chart/?symbol=WCT) | $1.71 | +30.5% | +29.8% | $2.22 | +69.5% | 341K | 17.7M | 0.0x | 849K | Packaged Software |
| IPW | [TV](https://www.tradingview.com/chart/?symbol=IPW) | $3.29 | -12.7% | +27.4% | $4.19 | +11.1% | 340K | 524K | 0.6x | 570K | Internet Retail |
| TGHL | [TV](https://www.tradingview.com/chart/?symbol=TGHL) | $0.55 | +6.9% | +15.7% | $0.64 | +23.7% | 618K | 14.4M | 0.0x | 12.7M | IT Services |
| GLBS | [TV](https://www.tradingview.com/chart/?symbol=GLBS) | $2.14 | -0.9% | +12.6% | $2.41 | +11.6% | 751K | 173K | 4.4x | 13.9M | Marine Shipping |
| NVNI | [TV](https://www.tradingview.com/chart/?symbol=NVNI) | $0.91 | -8.7% | +10.6% | $1.01 | +1.0% | 106K | 2.5M | 0.0x | 7.8M | Financial Conglomerates |
| TANH | [TV](https://www.tradingview.com/chart/?symbol=TANH) | $0.51 | +11.1% | +6.6% | $0.54 | +18.5% | 71K | 333K | 0.2x | 14.1M | Chemicals: Specialty |

**AH trajectory (check-prices --ah-history):**
- **DAIC** — peaked **+69.9% ($3.28) at 16:10 ET**, faded steadily to +28.5% at 17:01. Early peak, SPIKE→FADE. Float 721K. Day -4.1% (red).
- **FLYE** — peaked **+97% ($3.45) at 16:15 ET**, faded hard to +32.6% at 17:01. Early peak, SPIKE→FADE. Float 1.5M, VRatio 7.4x (real volume). Day +14.3%.
- **EDHL** — peaked **+64.2% ($5.09) at 16:30 ET**, settled and holding a base ~+36–39% for 30 min. Early peak but holding, not actively fading. Recent IPO.
- **GLBS** — peaked +23.1% at 16:15, dipped to +7.6%, **recovered to +20.4% (16:55)**, now +17.6%. Hold/recover pattern. Float 13.9M, MCap 46.2M (higher).
- **HWH** — peaked +54.9% at 16:35, holding +43%. **Stale multi-day runner** (ran +210% on 06-09 AH) — fails first-day-of-unusual-activity.
- **IPW** — peaked +11.7% at 16:40, now **-15.3% (below close)**. Day -12.7%. Dead/dead-cat.
- **TGHL / NVNI / TANH / WCT** — single-print spikes or below 10% sustained; faded to flat/red. Not actionable.

**Catalyst search (>10% AH movers):**
- **GLBS** — **Q1 2026 earnings beat** reported after close: $0.05 EPS vs -$0.05 consensus (beat +$0.10). **B-grade catalyst.** Driver identified.
- **EDHL** — recent **IPO** (began Nasdaq trading after IPO pricing/closing); flagged on metaverse-stock watchlists. No same-day operational catalyst. Recent-IPO momentum, **no fresh catalyst**.
- **DAIC** — **1-for-25 reverse split** (corporate action, not a bullish operational catalyst). Multi-day runner (+47% Tue, +98% Wed premarket per Benzinga). **No catalyst found** + fails first-day.
- **FLYE** — re-ran search (was no-catalyst at 22:30); searches return Firefly Aerospace (FLY), not Fly-E (FLYE). **No catalyst found** within budget. EV bike maker.

**Decision: NO ENTRY (skip-all).**
- The only candidates meeting the full entry gate (float <50M, AH >10% across ≥2 AH scans 22:00+, Day% > −15%) are **DAIC** and **FLYE** (both seen at 22:30 + 23:00). **Both are clear SPIKE→FADE** — peaked at 16:10/16:15 ET and have declined steadily across both scans. Per the SPIKE→FADE-only-night rule, skip all rather than entering the least-bad option (SPIKE→FADE is 0/10+ for PM continuation regardless of float/catalyst/AH%). Neither has a catalyst anyway.
- **EDHL** (holding base, recent IPO, no catalyst) and **GLBS** (earnings beat B-grade, hold/recover) are the more interesting *trajectories* but each has only **1 AH scan** so far — they don't meet the ≥2-scan requirement. **Watch both at 23:30**: confirm whether EDHL holds its ~+37% base / GLBS rebuilds toward its AH high. GLBS's earnings catalyst + recover pattern makes it the better B-grade watch despite higher float and modest AH%.
- **HWH** — stale multi-day runner, fails first-day. Skip.
- No CEILING-OVERRIDE WATCH candidates (nothing exceeds +150% Total% with a BUILD-and-hold profile).

## Scan 23:30 CET (5:30 PM ET)

**Session: AFTERHOURS (17:30 ET, 1.5h in). Entry-eligible scan.** `scan.py --all`: **12 hits.**

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| BATL | [TV](https://www.tradingview.com/chart/?symbol=BATL) | $2.06 | +57.3% | +10.7% | $2.28 | +74.0% | 8.0M | 27.7M | 0.3x | 17.9M | Oil & Gas Production |
| SKYQ | [TV](https://www.tradingview.com/chart/?symbol=SKYQ) | $1.56 | +22.4% | +66.0% | $3.17 | +103.2% | 7.7M | 3.1M | 2.5x | 3.6M | Integrated Oil |
| DAIC | [TV](https://www.tradingview.com/chart/?symbol=DAIC) | $1.85 | -4.1% | +34.1% | $2.48 | +28.5% | 6.0M | 4.3M | 1.4x | 721K | Miscellaneous |
| FLYE | [TV](https://www.tradingview.com/chart/?symbol=FLYE) | $2.00 | +14.3% | +14.0% | $2.28 | +30.3% | 2.9M | 392K | 7.4x | 1.5M | Motor Vehicles |
| WCT | [TV](https://www.tradingview.com/chart/?symbol=WCT) | $1.71 | +30.5% | +8.2% | $1.85 | +41.2% | 2.1M | 17.9M | 0.1x | 849K | Packaged Software |
| TMDE | [TV](https://www.tradingview.com/chart/?symbol=TMDE) | $0.91 | +8.9% | +26.4% | $1.15 | +37.6% | 1.1M | 1.2M | 1.0x | 16.5M | Wholesale Distributors |
| HWH | [TV](https://www.tradingview.com/chart/?symbol=HWH) | $1.42 | +15.9% | +19.0% | $1.69 | +38.0% | 974K | 3.5M | 0.3x | 1.5M | Financial Conglomerates |
| GLBS | [TV](https://www.tradingview.com/chart/?symbol=GLBS) | $2.14 | -0.9% | +11.7% | $2.39 | +10.6% | 907K | 190K | 4.8x | 13.9M | Marine Shipping |

_(Lower rows — SCKT +6.8%, SEGG -14.3%, MTEN +6.4%, ANNA +6.7% — below the 10% AH threshold or red; not actionable.)_

**AH trajectory (check-prices --ah-history):**
- **SKYQ** — flat ~+20% until 16:45, then ramped: +67.8% (16:50) → +92.3% (16:55) → **peak +129.5% ($3.58) at 17:00 ET** → faded hard: +106% (17:05), +76% (17:15), +41% (17:20), now **+40% ($2.19) at 17:30**. Late BUILD then SPIKE→FADE off the 17:00 peak. Float 3.6M (ideal), VRatio 2.5x (genuine volume). Day +22.4%. **New — only 1 AH scan.**
- **BATL** — opened +58.8%, chopped +48–79%, **peak +79.4% ($2.35) at 17:15 ET**, now +68.7%. HOLD/range pattern near its high. But VRatio 0.3x (AH vol well below avg — weak). Float 17.9M, Day +57.3% (already extended in regular session). **New — only 1 AH scan.**
- **DAIC** — **peak +69.9% ($3.28) at 16:10 ET**, faded to +22.3% at 17:30. Clean SPIKE→FADE, declining across all 3 scans (22:30/23:00/23:30). Float 721K, Day -4.1%.
- **FLYE** — **peak +97% ($3.45) at 16:15 ET**, faded to +17.1% at 17:30. Clean SPIKE→FADE across all 3 scans. Float 1.5M, VRatio 7.4x, Day +14.3%.
- **GLBS** — peak +23.1% (16:15), faded to base, recovered +20% (16:55), back to **+9.9% at 17:30**. Early-peak → decaying to the +10% threshold. Float 13.9M. Earnings beat (B-grade).
- **TMDE** — peak +37.6% (17:10), choppy, now +23%. Float 16.5M. On the non-biotech 0/6 loss list. Modest.
- **HWH/WCT** — stale multi-day runners (ran in 06-09 AH). Fail first-day-of-unusual-activity. Skip.

**Catalyst search:**
- **SKYQ** — only news is the **June 8 SAF MOU** (non-binding multi-party MOU with Southern Energy Renewables + DevvStream re: sustainable aviation fuel at the Foreland refinery) — **2 days stale**. No same-day (June 10) press release or 8-K found within budget (tavily week, brave day, tavily 8-K day). The move looks like a multi-day continuation/momentum run on the SAF story (stock already +22.4% in regular session). **No fresh same-day catalyst found.**
- **GLBS** — Q1 2026 **earnings beat** (carried from 23:00 search). **B-grade.**
- **DAIC** — 1-for-25 reverse split (corporate action, not bullish operational). No catalyst.
- **FLYE** — searches return Firefly Aerospace, not Fly-E. No catalyst found.

**Decision: NO ENTRY (skip-all).**
- **The strongest movers (SKYQ +129% peak, BATL +79%) are new this scan — only 1 AH scan each**, so they fail the ≥2-AH-scan (22:00+) entry requirement. They cannot be entered tonight; they become **00:00 CET watches.** SKYQ additionally is *fading hard* from its 17:00 peak (BUILD→SPIKE→FADE, +129%→+40%); BATL holds near its high but has weak AH volume (VRatio 0.3x) and is already +57% on the regular day.
- **The gate-qualifying candidates (≥2 AH scans) are all weak/fading:** DAIC and FLYE are clean SPIKE→FADE (peaked 16:10/16:15 ET, declining across all 3 scans) → 0/10+ for PM continuation, skip. GLBS qualifies on its B-grade earnings beat but its AH move has *decayed to the +10% threshold* and it peaked early (16:15) — not building, marginal. Per "skip-all when no candidate sustains >10% AH across multiple scans," GLBS is too weak to anchor an entry.
- **SPIKE→FADE / weak night** → skip all rather than entering the least-bad option.
- No CEILING-OVERRIDE WATCH candidates (nothing exceeds +150% Total% with a BUILD-and-hold profile; SKYQ peaked at +129% and is fading).
- **00:00 CET watch:** SKYQ (priority — float 3.6M, VRatio 2.5x) — re-evaluate if it stabilizes/rebuilds toward its $3.58 high and prints a 2nd AH scan; BATL (secondary) — confirm it holds its range on improving volume.

## Scan 00:00 CET (6:00 PM ET)

**Session: AFTERHOURS (18:00 ET, 2h in). Entry-eligible scan.** `scan.py --all`: **15 hits.**

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| SKYQ | [TV](https://www.tradingview.com/chart/?symbol=SKYQ) | $1.91 | +22.4% | +8.9% | $2.08 | +33.3% | 13.1M | 3.7M | 3.6x | 3.6M | Integrated Oil |
| BATL | [TV](https://www.tradingview.com/chart/?symbol=BATL) | $2.06 | +57.3% | +5.8% | $2.18 | +66.3% | 10.7M | 28.0M | 0.4x | 17.9M | Oil & Gas Production |
| DAIC | [TV](https://www.tradingview.com/chart/?symbol=DAIC) | $1.85 | -4.1% | +16.8% | $2.16 | +11.9% | 6.2M | 4.3M | 1.4x | 721K | Miscellaneous |
| TMDE | [TV](https://www.tradingview.com/chart/?symbol=TMDE) | $0.91 | +8.9% | +20.9% | $1.10 | +31.6% | 2.1M | 1.3M | 1.7x | 16.5M | Wholesale Distributors |
| HWH | [TV](https://www.tradingview.com/chart/?symbol=HWH) | $1.42 | +15.9% | +22.2% | $1.74 | +41.7% | 1.6M | 3.6M | 0.4x | 1.5M | Financial Conglomerates |
| TGHL | [TV](https://www.tradingview.com/chart/?symbol=TGHL) | $0.55 | +6.9% | +16.7% | $0.65 | +24.7% | 1.5M | 14.5M | 0.1x | 12.7M | IT Services |
| RBNE | [TV](https://www.tradingview.com/chart/?symbol=RBNE) | $1.07 | +0.9% | +54.2% | $1.65 | +55.7% | 1.3M | 470K | 2.7x | 7.3M | Marine Shipping |
| EONR | [TV](https://www.tradingview.com/chart/?symbol=EONR) | $0.62 | +9.0% | +12.0% | $0.69 | +22.0% | 991K | 1.6M | 0.6x | 39.8M | Integrated Oil |
| GLBS | [TV](https://www.tradingview.com/chart/?symbol=GLBS) | $2.14 | -0.9% | +19.2% | $2.55 | +18.1% | 942K | 194K | 4.9x | 13.9M | Marine Shipping |
| FATE | [TV](https://www.tradingview.com/chart/?symbol=FATE) | $1.87 | -1.6% | +5.9% | $1.98 | +4.2% | 319K | 4.2M | 0.1x | 110.5M | Biotechnology |
| SCKT | [TV](https://www.tradingview.com/chart/?symbol=SCKT) | $0.95 | +12.8% | +7.4% | $1.02 | +21.1% | 231K | 358K | 0.6x | 5.4M | Computer Peripherals |
| SEGG | [TV](https://www.tradingview.com/chart/?symbol=SEGG) | $1.39 | -20.6% | +9.4% | $1.52 | -13.1% | 183K | 1.6M | 0.1x | 10.8M | Movies/Entertainment |
| INDO | [TV](https://www.tradingview.com/chart/?symbol=INDO) | $2.84 | +7.2% | +5.6% | $3.00 | +13.2% | 133K | 836K | 0.2x | 9.9M | Integrated Oil |
| HCWB | [TV](https://www.tradingview.com/chart/?symbol=HCWB) | $1.21 | +2.5% | +9.9% | $1.33 | +12.7% | 95K | 1.6M | 0.1x | 4.2M | Biotechnology |
| AGIG | [TV](https://www.tradingview.com/chart/?symbol=AGIG) | $1.17 | +0.9% | +6.0% | $1.24 | +6.9% | 94K | 175K | 0.5x | 12.4M | Oil & Gas Production |

**Macro driver — oil-sector rally:** The board is dominated by oil & integrated-oil names (SKYQ, BATL, EONR, INDO, AGIG) plus shipping (RBNE, GLBS). Catalyst search confirms **BATL "surges 78%+ on Trump Iran comments"** (Reddit/news, Jun 10) and **SKYQ "as energy momentum flips into domestic oil and refinery plays"** (Instagram/news). This is a **sector-wide macro move (Trump/Iran → oil), not company-specific catalysts.** EONR +19%, INDO +11% in AH confirm the sector beta. No individual operational catalyst on any name.

**AH trajectory (check-prices --ah-history):**
- **SKYQ** — flat ~+20% until 16:45, ramped on genuine volume (1M+ share 5m prints) to **peak +129.5% ($3.58) at 17:00 ET**, collapsed to +33% (17:30), then *rebuilt a base* +33→+47→+40→+44→**+46.2% ($2.28) at 18:00**. Float 3.6M (ideal), VRatio 3.6x (genuine fresh AH volume). Day +22.4%. **2nd AH scan** (23:30 +40% → 00:00 +46%, holding/rebuilding across scans). Early peak (17:00) but NOT declining across scans.
- **BATL** — opened +58.8%, chopped, **peak +79.4% ($2.35) at 17:15 ET**, holding +71.8% ($2.25) at 18:00 — near its high. BUT **VRatio 0.4x** and AH history shows ~0 volume after the 16:00 open (72K) — the "hold" is stale quotes, **not genuine AH trading**. Day +57.3% (already extended in regular session). Float 17.9M.
- **RBNE** — flat ~+5% until 17:35, then **late spike to +55.7% ($1.65) at 17:40 ET**, settled +29% by 18:00. **New — only 1 AH scan.** Late spike, float 7.3M, VRatio 2.7x. Shipping (sector beta).
- **DAIC** — clean SPIKE→FADE, **peak +69.9% at 16:10 ET**, declined to +14% across 4 scans. 1-for-25 reverse split, no catalyst. Skip.
- **GLBS** — peaked +23.1% (16:15), chopping ~+14%. Q1 earnings beat (B-grade) but AH decayed/modest. Float 13.9M.
- **TMDE** — peaked +37.6% (17:10), choppy +30%. Float 16.5M. On non-biotech 0/6 loss list.
- **HWH** — stale multi-day runner (ran +210% on 06-09 AH). Fails first-day. Skip.
- **EONR/INDO/AGIG** — oil-sector beta, low AH% (+22/+13/+7), thin volume. SEGG red (-13% total, dead-cat). Not actionable.

**Decision: ENTER SKYQ** (paper). Per the 23:00+ baseline rule, SKYQ is the **best available gate-qualifier**: float 3.6M (ideal), VRatio 3.6x (the only candidate with both ideal float AND genuine fresh AH volume), AH >10% across 2 scans (23:30 +40% → 00:00 +46%, holding/rebuilding — not declining), Day +22.4% (not over-extended), Total% +46% (well under the 150 ceiling, lots of overnight room).
- **Why SKYQ over BATL:** BATL "holds near high" but on **near-zero AH volume** (VRatio 0.4x, stale quotes) and is already **+57% on the regular day** — a no-volume hold of an extended regular-session mover, not genuine AH momentum. SKYQ has real volume and ideal float with room under the ceiling.
- **Concerns noted:** (1) SKYQ spiked to +129% at 17:00 ET and collapsed -36% to its base — early-peak character (mitigant: it is *holding/rebuilding* across the last two scans, like the CHAI "held base despite early peak" case, not declining). (2) Catalyst is **macro oil-sector (Trump/Iran), not company-specific** → **Grade None** (exit at first premarket opportunity).
- This is a learning-phase data-collection entry: macro-sector AH spike + early-peak-then-base-hold + low-float genuine-volume oil name. Skip everything else (DAIC/FLYE SPIKE→FADE, GLBS decayed, HWH stale, RBNE only 1 scan).
- No CEILING-OVERRIDE WATCH candidates (nothing exceeds +150% Total% with a BUILD-and-hold profile).

## Scan 00:30 CET (6:30 PM ET)

**Session: AFTERHOURS (18:30 ET, 2.5h in). Entry-eligible scan, but SKYQ is OPEN → one-position rule blocks new entries.** `scan.py --all`: **20 hits.**

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| SKYQ | [TV](https://www.tradingview.com/chart/?symbol=SKYQ) | $1.91 | +22.4% | +22.0% | $2.33 | +49.4% | 15.1M | 3.9M | 3.9x | 3.6M | Integrated Oil |
| CPOP | [TV](https://www.tradingview.com/chart/?symbol=CPOP) | $1.52 | +322.2% | +11.2% | $1.69 | +369.4% | 14.8M | 39.8M | 0.4x | 20.4M | Advertising/Marketing |
| BATL | [TV](https://www.tradingview.com/chart/?symbol=BATL) | $2.06 | +57.3% | +9.7% | $2.26 | +72.5% | 12.5M | 28.1M | 0.4x | 17.9M | Oil & Gas Production |
| DAIC | [TV](https://www.tradingview.com/chart/?symbol=DAIC) | $1.85 | -4.1% | +15.1% | $2.13 | +10.4% | 6.4M | 4.3M | 1.5x | 721K | Miscellaneous |
| RBNE | [TV](https://www.tradingview.com/chart/?symbol=RBNE) | $1.07 | +0.9% | +30.9% | $1.40 | +32.2% | 4.7M | 851K | 5.5x | 7.3M | Marine Shipping |
| TMDE | [TV](https://www.tradingview.com/chart/?symbol=TMDE) | $0.91 | +8.9% | +18.7% | $1.08 | +29.2% | 2.3M | 1.3M | 1.8x | 16.5M | Wholesale Distributors |
| VIVK | [TV](https://www.tradingview.com/chart/?symbol=VIVK) | $0.64 | +15.6% | +39.0% | $0.89 | +60.8% | 1.4M | 4.7M | 0.3x | 4.2M | Chemicals: Specialty |
| HWH | [TV](https://www.tradingview.com/chart/?symbol=HWH) | $1.42 | +15.9% | +14.8% | $1.63 | +33.1% | 1.8M | 3.6M | 0.5x | 1.5M | Financial Conglomerates |
| BQ | [TV](https://www.tradingview.com/chart/?symbol=BQ) | $0.89 | +7.6% | +14.6% | $1.02 | +23.3% | 987K | 5.7M | 0.2x | 3.9M | Internet Retail |
| GLBS | [TV](https://www.tradingview.com/chart/?symbol=GLBS) | $2.14 | -0.9% | +10.7% | $2.37 | +9.7% | 966K | 197K | 4.9x | 13.9M | Marine Shipping |

_(Lower rows — EONR +12%, SCKT +9.5%, MTEN +7.6%, SEGG -10.3% total, ANNA +5.3%, AGIG, HCWB, NCT, MSW +6.7% — below the 10% AH threshold, red, or stale. Not actionable.)_

**AH trajectory (check-prices --ah-history):**
- **SKYQ (OPEN)** — peaked +129.5% ($3.58) at 17:00 ET, collapsed to +33% base, now **rebuilt to +48.7% ($2.33) at 18:30** — third consecutive scan holding/building above the base (23:30 +40% → 00:00 +46% → 00:30 +49%). VRatio 3.9x (genuine, climbing). Above our $2.28 entry (+2.2%). Thesis intact: low-float oil name holding its base, not fading.
- **RBNE** — late spike to +55.7% ($1.65) at 17:40 ET, settled, choppy ~+32% ($1.40) now. **2nd AH scan** (00:00 +55% snapshot → 00:30 +32%). Float 7.3M, VRatio 5.5x (real volume). Shipping — part of the same macro oil/shipping rally, not a company catalyst.
- **CPOP** — **+322% regular day**, AH total +369% (history shows erratic prints to +597%). Multi-day blow-off / extreme extension. **Skip — far above the +150% ceiling.**
- **BQ** — peaked +28% at 16:50, faded, holding ~+22% ($1.02). Float 3.9M, VRatio 0.2x (thin). Modest.
- **VIVK** — +60.8% total, +39% AH, float 4.2M but VRatio 0.3x (thin AH volume). Specialty chemicals.
- **BATL** — holds +72% but VRatio 0.4x (stale quotes, no genuine AH volume) and already +57% regular day. Same no-volume-hold concern as prior scans.
- **DAIC** — clean SPIKE→FADE (peak 16:10 ET), decayed to +10% across 5 scans. Reverse split, no catalyst. Skip.

**Decision: NO NEW ENTRY.**
- **SKYQ is open → one-position rule blocks any new entry**, and SKYQ is behaving well (holding/building above entry across 3 scans). No reason to consider a swap.
- Even absent the open position, tonight's fresh strong movers are weak fits: CPOP is far over the +150% ceiling (+369%), RBNE/BATL/VIVK are macro oil-shipping beta with no company catalyst (RBNE only choppy 2nd scan; BATL/VIVK thin AH volume), and DAIC is a confirmed SPIKE→FADE.
- No CEILING-OVERRIDE WATCH candidates (CPOP exceeds +150% but is a multi-day blow-off, not a post-17:00 BUILD-and-hold within ~20% of high; it spiked +369%→erratic).
- **This is the last scheduled evening scan (00:30 CET).** SKYQ carries overnight; exit decision handled by position-evaluation.md in premarket.

## Paper Trades

| Ticker | Entry Price | Entry Time | Shares (~€100) | Catalyst Grade | Reason |
|--------|-------------|------------|-----------------|----------------|--------|
| SKYQ | $2.28 | 00:00 CET (18:00 ET) | 43 | None | Best gate-qualifier: float 3.6M (ideal), VRatio 3.6x (genuine AH vol), AH +46% holding across 2 scans, Total% +46% (room under ceiling), Day +22.4%. Concerns: early-peak spike +129%→base; macro oil-sector catalyst (Trump/Iran), not company-specific |
