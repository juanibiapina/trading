# Morning Evaluation - 2026-06-16

## Morning Evaluation — 10:21 CET

_Pulse 1. PM session only ~20 min old (now 04:21 ET). Peaks below are "so far"; position-evaluation (10:30/14:30 CET) tracks the rest of premarket._

### Today's Winner

**CRVO** — Misc Commercial Services (CervoMed Inc., biotech)
- Catalyst: None fresh. Known items predate the spike — $10.5M private placement (Jun 10, Grade D dilution) and H.C. Wainwright Neuro Summit appearance (Jun 15 AM). Late unexplained AH spike at 17:40 ET.
- Previous Close: $2.45 (Jun 15 regular close $2.48, Day +1.2%)
- AH last night: $3.77 (+53.9%) at 18:20 ET / 00:20 CET — BUILD-and-hold, late new high
- Premarket now: $3.28 (+33.9%), PM peak $3.74 (+52.7%) at 04:10 ET so far
- Hypothetical P&L (AH entry → PM peak): early AH entry ~$3.37 → PM peak $3.74 = **+11%**
- Float: 4.8M | Market Cap: $23.0M | VRatio at entry 5.8x

**Scanner Diagnostic:**
- Detectable at screening time? **YES** — and we acted on it. CRVO appeared in the 00:00 CET scan (+35.9%) and activated on the 2nd AH scan at 00:30 CET (+50.8%), where we entered a paper trade at $3.64.
- BUILD-and-hold pattern: flat all afternoon → spiked +36.7% at 17:40 ET → new AH high $3.77 at 18:20 ET → held +48%. Float 4.8M ideal, VRatio jumped 1.1x→5.8x.
- Scanner gap: none for CRVO. It was caught and traded correctly. The gap is the **PM-only gapper** (see TDIC below), which AH screening structurally cannot catch.

**Biggest raw PM mover (not an AH→PM winner): TDIC** — Dreamland Limited
- PM now ~$11.05 (+92%), PM peak $13.83 (+140.8%) at 04:05 ET, vs prev close ~$5.74.
- **Flat/down in after-hours** ($5.30–$5.50, -4% to -8% all evening). No AH signal whatsoever.
- This is a pure premarket gapper — news likely broke overnight/early AM. Our evening AH scanner could **not** have flagged it; there was nothing to detect. Structural blind spot of the AH→PM strategy.

### Baseline Tracking

- Days tracked: **31** (was 30 + 1)
- Winners detected by scanner: **27/31 (87.1%)** — HIT, SUNE, DRMA, UGRO, NXTT, POLA, BCG, PFSA, MASK, EZGO, AIIO, HTCO, WOK, LNKS, AMST, PHGE (May 20), PHGE (May 26), SNGX, ATPC, PRFX, DXST, TWAV, CHAI, MSW, TMDE, BYAH, **CRVO**
- Winner selected for paper trade: **19/31 (61.3%)** — incremented; we entered CRVO (the AH→PM winner) at $3.64, 00:30 CET
- Target: >80% detection
- Status: **BASELINE MET** (87.1% detection)

### Retrospective Scan Results

- **PM scan (04:20 ET):** 3 hits — TDIC (+100.9%), CRVO (+46.0%), HITI (+21.8%)
- **Forced AH scan (04:20 ET):** 0 hits (overnight TradingView postmarket fields return 0, as expected — use evening live scans as the retrospective source)
- **AH reconstruction (check-prices --ah-history):**
  - CRVO: AH high $3.77 (+53.9%) at 18:20 ET → held +38-40% into close of AH. Clean AH→PM continuation.
  - TDIC: AH $5.30-$5.50 (-4% to -8%). No AH move. PM-only gapper.
  - HITI: AH high $2.74 (+18.6%) → PM $2.83 (+22.5%). Modest, held.
- **Data quirk:** Yahoo's Jun 15 daily close is null for several names, so `check-prices.py` defaults its "prev close" to the Jun 12 value. This badly distorts RGNT (shows +386% off a stale $1.50 ref; RGNT actually closed ~$9.40 Jun 15 and is ~$7.30 PM = **down**). `price-timeline.py` also printed impossible "08:00 ET" bars (future data at 04:20 ET) — disregarded; pm-history is the reliable current snapshot.

### Paper Trade P&L

| Ticker | Entry | Entry Total% | Catalyst | Entry Time | PM Peak | Peak Time | Exit | P&L | P&L % | Status |
|--------|-------|--------------|----------|------------|---------|-----------|------|-----|-------|--------|
| HUBC   | $2.06 | +74.6% | None — no catalyst, dilution risk | 23:30 CET | $1.96 | 04:20 ET | — | -€5.28 | -5.3% | 🔴 Open |
| WCT    | $1.94 | +33.8% | D — 1-for-400 reverse consolidation | 23:30 CET | $1.62 | 04:00 ET | — | -€20.91 | -21.1% | 🔴 Open |
| CRVO   | $3.64 | +48.6% | None — late AH spike, Jun 10 dilution | 00:30 CET | $3.74 | 04:10 ET | — | -€9.72 | -9.9% | 🔴 Open |

_PM only 20 min old; peaks are provisional. Exit decisions handled by position-evaluation._

**Total Paper P&L (unrealized, provisional): -€35.91**

### Scanner Effectiveness

- Evening scans ran: 7 times (21:30 - 00:30 CET)
- Candidates found: ~15 unique tickers (HITI, ZNB, AVAT, HUBC, CIIT, WCT, RGNT, SKYA, GELS, CRVO, AHMA, UCAR, GMM, + 21:30 regular-session watch list)
- Retrospective matches: CRVO caught (the AH→PM winner). TDIC missed (PM-only gapper, undetectable in AH).

### Missed Opportunities

| Ticker | AH Change | Why Missed | Would Be Profitable? |
|--------|-----------|------------|---------------------|
| TDIC | Flat/down (-4% to -8%) | PM-only gapper — no AH move to detect; news broke overnight/early AM | Yes as a PM-only play (+140%), but NOT an AH→PM trade — outside strategy scope |

### AH Mover Follow-Through

| Ticker | AH Peak | Peak Time | AH Trajectory | Current PM | From Peak | From Close | Verdict |
|--------|---------|-----------|---------------|------------|-----------|------------|---------|
| HUBC | $2.19 (+85.6%) | 17:30 ET | Build → ease | $1.95 | -11% | +16% (vs $1.68) | Faded; AH was better exit |
| CRVO | $3.77 (+53.9%) | 18:20 ET | Build-and-hold | $3.28 (peak $3.74) | ~flat at peak | +34% (vs $2.45) | Held; PM ≈ AH peak |
| WCT | $1.99 (~+37%) | 17:25 ET | Choppy whipsaw | $1.53 (peak $1.62) | -19% | +5% (vs $1.45) | Faded |
| HITI | $2.74 (+18.6%) | 16:05 ET | Spike → hold | $2.79 (peak $2.83) | +3% | +21% (vs $2.31) | Held/built; PM exceeded AH |
| ZNB | ~$1.58 (+66%) | 16:15 ET | Spike → fade | $0.93 | — | -2% | Faded hard (correctly skipped) |
| RGNT | +599% total | regular blow-off | Regular blow-off | ~$7.30 | down | down vs $9.40 close | Faded (correctly skipped, ceiling) |

**AH-peak-vs-PM-peak check:** HUBC and WCT both peaked in AH and faded into PM (AH was the better exit). CRVO peaked roughly equal AH≈PM. HITI's PM peak slightly exceeded its AH peak. No new clean data point for the extreme-AH-runner (>250% from close) fade hypothesis this session — RGNT's +599% was regular-session driven, not an AH run, but it faded into PM (directionally consistent).

### Price Charts

CRVO AH→PM (from check-prices, ET):
```
AH:  16:00 $2.48 (flat) → 17:40 $3.35 (+36.7% spike) → 18:20 $3.77 (+53.9% high) → held +38-40% to 19:55
PM:  04:00 $3.62 (+47.8%) → 04:10 $3.74 (+52.7% peak so far) → 04:20 $3.28 (+33.9%)
```

TDIC PM-only gapper (ET):
```
AH:  16:00-19:55 $5.30-$5.50 (-4% to -8%, no move)
PM:  04:00 $10.64 (+85%) → 04:05 $13.83 (+140.8% peak) → 04:20 $11.05 (+92%)
```

_(price-timeline.py output omitted — its post-04:20 ET timestamps are a timezone artifact and not real data at this hour.)_

### Notes

- **Clean detection day for the AH→PM strategy:** CRVO was caught, activated on the 2-scan gate, and traded. Detection rate ticks to 87.1% (27/31), and we selected the right stock (19/31 selected).
- **The real story is TDIC** (+140% PM, pure gapper). This is the recurring PM-only blind spot: a stock with no AH footprint that explodes after 04:00 ET on overnight news. AH screening cannot catch these by design. Worth tracking how often the morning's *biggest* mover is a PM-only gapper vs an AH→PM continuation — if PM-only gappers dominate, a separate early-PM scan workflow may be warranted.
- **Open positions are red so far**, but PM is only 20 min old. HUBC and WCT both faded from AH (no fresh catalyst / reverse-split overhang — the weak-catalyst names underperforming again). CRVO holding near its AH level.
- No ceiling-override or dead-cat-override watch candidates were flagged last night, so no override-watch outcomes to tally.
</content>
</invoke>

## Position Evaluation — 10:30 CET

PM prices at 04:30 ET (via check-prices --pm-history, the reliable snapshot).

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| HUBC | $2.06 | $1.98 | -3.9% | $2.11 (PM) | 1 | None | SELL | Grade None — exit at first premarket pulse; faded from AH |
| WCT | $1.94 | $1.53 | -21.1% | $1.62 (PM) | 1 | D | SELL | Hard stop ($1.65) breached + Grade D premarket exit |
| CRVO | $3.64 | $3.19 | -12.4% | $3.74 (PM) | 1 | None | SELL | Grade None — exit at first premarket pulse; PM peak $3.74 faded |

**Actions taken:**
- SELL HUBC at $1.98 (48 sh) → -$3.84 (-3.9%)
- SELL WCT at $1.53 (51 sh) → -$20.91 (-21.1%)
- SELL CRVO at $3.19 (27 sh) → -$12.15 (-12.4%)
- **Total realized P&L: -$36.90**

All three were Grade None/D, all exit in first premarket per risk rules. None had a fresh catalyst to justify a hold. WCT's hard stop was breached overnight. CRVO's PM peak ($3.74, +52.7% from close) was the best exit window but it faded to $3.19 by 04:30 ET; entry at $3.64 left no profit. Consistent pattern: weak/no-catalyst AH movers fade overnight.

## Position Evaluation — 14:30 CET

No open positions. All three positions (HUBC, WCT, CRVO) were closed in the 10:30 CET evaluation. Nothing to evaluate.

**Actions taken:** None.

---

## Post-Market Screening

## Scan 21:30 CET (3:30 PM ET)

_Regular-session scan (before AH opens at 22:00 CET / 4:00 PM ET). No entries per regular-session caution rule. Candidates flagged **Watch — pending AH confirmation**; only enter if they reappear in an AH scan (22:00+ CET) with sustained momentum. 61 hits total; notable low-float / high-move names below._

| Ticker | Price | Day% | IRVol | Float | MCap | Industry | Note |
|--------|-------|------|-------|-------|------|----------|------|
| SEAC | $5.00 | +100.0% | 2.6 | 1.8M | $12.9M | Packaged Software | Ideal float, big move — Watch |
| RBLK | $1.60 | +110.1% | 0.8 | 596K | $956K | Packaged Software | Tiny float, but IRVol fading — Watch |
| CCTG | $1.44 | +84.1% | 45.7 | 3.0M | $5.6M | Electronic Components | Low float, high IRVol — Watch |
| CRVO | $4.72 | +90.3% | 1377.8 | 4.8M | $23.0M | Misc Commercial Svcs | Last night's AH→PM winner; already traded+closed today — Watch for re-spike |
| TDIC | $8.27 | +52.3% | 2.1 | 0/14.1M | $14.1M | Misc Commercial Svcs | This morning's PM-only gapper (+140% PM); now regular-session — Watch |
| VIIQ | $1.00 | +376.2% | 0.9 | 2.1M | $2.1M | Financial Conglomerates | Huge % but low IRVol (0.9), thin — Watch with caution |
| CFOR | $2.00 | +300.0% | 0.9 | 3.6M | $24.4M | Misc Commercial Svcs | Big % but low IRVol — Watch |
| OBAI | $1.07 | +100.2% | 588.9 | 14.7M | $13.1M | Packaged Software | Float >10M, very high IRVol — Watch |
| NMRA | $1.52 | +66.2% | 11.8 | 78.5M | $281.6M | Pharma: Major | Float too high — low priority |

**Assessment:** Regular-session only. No AH price action yet — TradingView postmarket fields are 0 until 22:00 CET. All names above are observation-only until they confirm in an AH scan. The 22:00 and 22:30 AH scans are also observation-only per learning-phase rules (no entries before 23:00 CET / 5:00 PM ET).

## Scan 22:00 CET (4:00 PM ET)

_AH just opened. Scanner returned 0 hits — TradingView postmarket fields are still settling at the open and no candidate cleared the filter. Observation-only scan per learning phase (no entries before 23:00 CET). Regular-session watch names from 21:30 (SEAC, CCTG, CRVO, TDIC, etc.) need to reappear in a later AH scan with sustained AH momentum before they qualify._

No candidates found.

## Scan 22:30 CET (4:30 PM ET)

_First AH scan with hits (22:00 returned 0). Observation-only per learning phase (no entries before 23:00 CET / 5:00 PM ET). All 5 names are new vs prior scans. To qualify for entry at 23:00+, a candidate needs float <50M, AH change >10% in ≥2 AH scans (22:00+ CET), and Day% above -15%. This is only their 1st AH appearance, so none can qualify yet._

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| FLZH | [TV](https://www.tradingview.com/chart/?symbol=FLZH) | $3.85 | +22.2% | +61.0% | $6.20 | +96.8% | 2.4M | 0 | 0.0x | 1.6M | Wholesale Distributors |
| SDOT | [TV](https://www.tradingview.com/chart/?symbol=SDOT) | $8.67 | -63.1% | +44.9% | $12.56 | -46.5% | 117K | 7.7M | 0.0x | 741K | Restaurants |
| GDHG | [TV](https://www.tradingview.com/chart/?symbol=GDHG) | $1.60 | -1.8% | +31.2% | $2.10 | +28.8% | 56K | 1.6M | 0.0x | 18.6M | Engineering & Construction |
| MYSE | [TV](https://www.tradingview.com/chart/?symbol=MYSE) | $2.30 | +13.9% | +24.3% | $2.86 | +41.6% | 3.4M | 614K | 5.5x | 4.8M | Packaged Software |
| LNAI | [TV](https://www.tradingview.com/chart/?symbol=LNAI) | $2.85 | +9.0% | +8.6% | $3.09 | +18.4% | 54K | 58K | 0.9x | 2.9M | Biotechnology |

**Observations (no entries — observation-only scan):**
- **FLZH** — Float 1.6M (ideal), AH +61% on 2.4M AH vol. Strongest mover. Watch for re-appearance + sustained build at 23:00.
- **SDOT** — Day **-63.1%** regular-session crash, AH bounce +44.9% but Total% still **-46.5%** (well below regular close). Classic **dead-cat bounce** — recovering from a sell-off, not new momentum. Day% < -15% → fails entry gate. Would only flag DEAD-CAT-OVERRIDE WATCH if it reclaims *above* its regular close, which it is far from doing. Skip-track.
- **GDHG** — AH +31% but float 18.6M (above 10M ideal, under 50M cap). Watch.
- **MYSE** — Float 4.8M, AH +24%, VRatio 5.5x (only name with real volume ratio). Watch for build.
- **LNAI** — AH +8.6% (below 10% threshold), low AH vol 54K. Marginal; low priority.

Catalyst searches deferred to 23:00+ scan when candidates can actually qualify for entry (need 2nd AH appearance first). No entries this scan.

## Scan 23:00 CET (5:00 PM ET)

_First entry-eligible AH scan (entries allowed at 23:00+ CET). 7 hits. Three names now have ≥2 AH scans >10% (FLZH, GDHG, MYSE) and clear the numeric gates, but all three peaked before 17:00 ET and are declining = SPIKE→FADE/early-peak-fading. LNAI is the only BUILD candidate (new AH highs at 17:00) but has just 1 qualifying AH scan. **Decision: skip all entries — SPIKE→FADE-only night among qualifiers; watch LNAI for 23:30.**_

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| MYSE | [TV](https://www.tradingview.com/chart/?symbol=MYSE) | $2.30 | +13.9% | +27.8% | $2.94 | +45.5% | 8.9M | 1.3M | 6.9x | 4.8M | Packaged Software |
| FLZH | [TV](https://www.tradingview.com/chart/?symbol=FLZH) | $3.85 | +22.2% | +36.4% | $5.25 | +66.7% | 5.1M | 0 | 0.0x | 1.6M | Wholesale Distributors |
| GDHG | [TV](https://www.tradingview.com/chart/?symbol=GDHG) | $1.60 | -1.8% | +59.3% | $2.55 | +56.4% | 596K | 1.7M | 0.3x | 18.6M | Engineering & Construction |
| STEX | [TV](https://www.tradingview.com/chart/?symbol=STEX) | $0.99 | -2.2% | +5.3% | $1.04 | +3.0% | 478K | 1.5M | 0.3x | 67.5M | Investment Banks/Brokers |
| SDOT | [TV](https://www.tradingview.com/chart/?symbol=SDOT) | $8.67 | -63.1% | +84.7% | $16.01 | -31.8% | 257K | 7.7M | 0.0x | 741K | Restaurants |
| TDIC | [TV](https://www.tradingview.com/chart/?symbol=TDIC) | $7.60 | +40.0% | +16.3% | $8.84 | +62.8% | 237K | 4.4M | 0.1x | 0/14.1M | Misc Commercial Services |
| LNAI | [TV](https://www.tradingview.com/chart/?symbol=LNAI) | $2.85 | +9.0% | +20.9% | $3.44 | +31.8% | 147K | 69K | 2.1x | 2.9M | Biotechnology |

**Per-candidate evaluation:**

- **FLZH** — Float 1.6M (ideal), Day +22.2%, 2nd AH scan >10% (22:30 +61% → 23:00 +36.4%). Clears numeric gates. **Trajectory: SPIKE→FADE.** AH peaked $6.19 (+93%) at **16:10 ET** (early), now $4.65, **-25% off high**, declining every bar since. Current price >20% below AH high = fade, not hold. No same-day catalyst found (Seeking Alpha/TipRanks only general listings). **SKIP — SPIKE→FADE, 0/10+ for PM continuation.**
- **GDHG** — Float 18.6M (above ideal, under 50M cap), Day -1.8%, 2nd AH scan >10% (+31% → +59%). Clears gates. **Trajectory: early peak + fading.** Peaked $2.55 (+59%) at **16:40 ET**, now $2.13 (+33%), -16.5% off high, declining last 20 min. VRatio 0.3 (596K AH vs 1.7M avg — thin volume, no conviction). **SKIP — early-peak fade on thin volume.**
- **MYSE** — Float 4.8M (ideal), Day +13.9%, 2nd AH scan >10% (+24% → +28%), VRatio 6.9 (real volume, 8.9M AH). Best volume profile of the night. **Trajectory: early peak + fading.** Peaked $3.17 (+57%) at **16:25 ET**, now $2.74 (+36%), -13.6% off high, drifting down 30 min. No same-day catalyst found (latest news Apr 2026). The "least bad" option, but it peaked early and is fading. **SKIP — per SPIKE→FADE-only-night rule, do not enter the least-bad.**
- **LNAI** — Float 2.9M (ideal), Day +9.0%, VRatio 2.1. **Trajectory: BUILD — the only one tonight.** Built from +12% (16:00) to new AH high $4.36/$4.57 (+67%/+75%) at **17:00 ET**, still climbing on the last bar. Late peak, holding/building. **But only 1 qualifying AH scan** (22:30 reading was +8.6%, below 10%). Fails the ≥2 AH scans >10% gate. No same-day catalyst found (prior catalysts: Mar 2026 $20M CNS acquisition, all old). **WATCH for 23:30 — if it logs a 2nd AH scan >10% and holds the build, it's the entry candidate.**
- **SDOT** — Day **-63.1%** regular crash; AH bounce +84.7% but Total% **-31.8%** (still well below regular close). Classic **dead-cat bounce** — recovering from a sell-off, far below close, no override (would need to reclaim *above* close). **SKIP.**
- **TDIC** — This morning's PM-only gapper (+140% PM), now AH +16.3%. Only 1 AH scan >10%. Float 0/14.1M. **Watch.**
- **STEX** — AH +5.3% (below 10% threshold). **SKIP.**

**Decision: No entries.** All numeric qualifiers (FLZH, GDHG, MYSE) are SPIKE→FADE/early-peak-fading — a SPIKE→FADE-only night among qualifiers, where the rule is skip-all rather than enter the least-bad (0/10+ historical). The only BUILD pattern (LNAI) doesn't yet clear the 2-scan gate. Watch LNAI at 23:30 for a qualifying 2nd AH scan while still building.

## Scan 23:30 CET (5:30 PM ET)

_Entry-eligible AH scan. 8 hits. **LNAI exploded from +20.9% AH (23:00) to +103.9% AH (23:30)** — the BUILD candidate I was watching now clears the 2-scan gate (23:00 +20.9%, 23:30 +103.9%) and all numeric gates with a clean BUILD/hold trajectory. **ENTERED LNAI.** The prior SPIKE→FADE qualifiers (MYSE, FLZH, GDHG) continue to fade — skipped._

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| LNAI | [TV](https://www.tradingview.com/chart/?symbol=LNAI) | $2.85 | +9.0% | +103.9% | $5.80 | +122.2% | 6.0M | 914K | 6.6x | 2.9M | Biotechnology |
| MYSE | [TV](https://www.tradingview.com/chart/?symbol=MYSE) | $2.30 | +13.9% | +15.6% | $2.66 | +31.7% | 10.7M | 1.5M | 7.1x | 4.8M | Packaged Software |
| FLZH | [TV](https://www.tradingview.com/chart/?symbol=FLZH) | $3.85 | +22.2% | +19.0% | $4.58 | +45.4% | 5.8M | 0 | 0.0x | 1.6M | Wholesale Distributors |
| GDHG | [TV](https://www.tradingview.com/chart/?symbol=GDHG) | $1.60 | -1.8% | +47.5% | $2.36 | +44.8% | 938K | 1.8M | 0.5x | 18.6M | Engineering & Construction |
| SDOT | [TV](https://www.tradingview.com/chart/?symbol=SDOT) | $8.67 | -63.1% | +75.8% | $15.24 | -35.1% | 347K | 7.7M | 0.0x | 741K | Restaurants |
| FLD | [TV](https://www.tradingview.com/chart/?symbol=FLD) | $0.56 | -14.6% | +6.4% | $0.60 | -9.1% | 514K | 13.1M | 0.0x | 7.4M | Packaged Software |
| STEX | [TV](https://www.tradingview.com/chart/?symbol=STEX) | $0.99 | -2.2% | +6.3% | $1.05 | +4.0% | 478K | 1.5M | 0.3x | 67.5M | Investment Banks/Brokers |
| REI | [TV](https://www.tradingview.com/chart/?symbol=REI) | $1.12 | -4.3% | +5.3% | $1.18 | +0.8% | 68K | 3.9M | 0.0x | 228.1M | Integrated Oil |

**Per-candidate evaluation:**

- **LNAI — ✅ ENTER.** Float 2.9M (ideal). Day +9.0% (above -15%). **2nd AH scan >10%:** 23:00 +20.9% → 23:30 +103.9%, clears the ≥2-AH-scan gate. VRatio 6.6 (real volume, 6.0M AH). **Trajectory: clean BUILD** — climbed 16:00 +11.9% → 17:00 +100.4% → AH high $6.42 (+146%) at **17:15 ET**, pulled to $5.50, then **rebuilding** $5.50→$5.65→$5.78 on the last 3 bars. Current $5.78 is -10% off the AH high = within 20% → holding/building, not fading. Peak at 17:15 ET is before 18:30, but hold-vs-fade is the primary signal (CHAI/MSW precedent) and LNAI is rebuilding toward its high. **Total% +122%** — under the +150% extension ceiling. **Catalyst (Grade C):** 8-K filed today (~16:35 ET) — regained Nasdaq $1.00 minimum bid-price compliance, under 1-year Panel monitor. Removing the delisting overhang on a 2.9M float is a plausible squeeze driver. Administrative/minor PR → Grade C (exit premarket). Older items (Feb oncology pilot, Geneial LOI) predate the move. **ENTER $5.80, 17 sh.**
- **MYSE** — Float 4.8M, VRatio 7.1 (best volume). But AH faded from +27.8% (23:00) to +15.6% now. Peaked $3.17 (+56.9%) at **16:25 ET**, now $2.67 (+32%), declining. **SKIP — early-peak fade.**
- **FLZH** — Float 1.6M (ideal) but AH faded from +36.4% to +19.0%. Peaked $6.19 (+93.4%) at **16:10 ET**, now $4.35-$4.58 (+36-47%), >20% off high. **SKIP — SPIKE→FADE.**
- **GDHG** — Float 18.6M (above ideal), VRatio 0.5 (thin, 938K AH vs 1.8M avg). Early peak fade. **SKIP — thin volume + early-peak fade.**
- **SDOT** — Day **-63.1%** regular crash; AH bounce +75.8% but Total% **-35.1%** (far below regular close). Classic dead-cat bounce, no reclaim above close → no override. **SKIP.**
- **FLD** — Day -14.6%, AH +6.4% (below 10%). **SKIP.**
- **STEX / REI** — AH +6.3% / +5.3% (below 10%), high floats. **SKIP.**

**Decision: 1 entry — LNAI $5.80, 17 sh, Grade C.** First BUILD candidate of the night to clear the 2-scan gate, ideal float, real volume, holding within 10% of its AH high, same-day 8-K catalyst, extension under ceiling. The SPIKE→FADE names (MYSE/FLZH/GDHG) correctly skipped per the early-peak-fade rule.

## Paper Trades

| Ticker | Entry Price | Entry Time | Shares (~€100) | Catalyst Grade | Reason |
|--------|-------------|------------|-----------------|----------------|--------|
| LNAI | $5.80 | 23:30 CET | 17 | C | BUILD pattern, float 2.9M, 2nd AH scan >10% (+20.9%→+103.9%), VRatio 6.6, holding within 10% of AH high, Total +122% under ceiling; 8-K Nasdaq bid-compliance regain |
