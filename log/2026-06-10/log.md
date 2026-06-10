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

## Paper Trades

| Ticker | Entry Price | Entry Time | Shares (~€100) | Catalyst Grade | Reason |
|--------|-------------|------------|-----------------|----------------|--------|
| _(none yet — pre-AH watch scan)_ | | | | | |
