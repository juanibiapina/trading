# Trade Log — 2026-06-11

## Morning Evaluation — 10:20 CET

### Today's Winner

**GLXG** — Galaxy Payroll Group (Misc Commercial Services) — *biggest PM mover, but PM-only*
- Catalyst: **None found.** No same-day press release or 8-K (websearch, freshness week). Stock had *declined* all week (−22% Mon AH, −22% Tue PM). Tiny-float squeeze with no news.
- Previous Close: $1.03
- AH last night: **flat** — AH high $1.08 (+4.9%), chopped $0.96–1.08 the whole session. No after-hours move at all.
- Premarket now: exploded **$4.56 (+343%)** peak at ~04:20 ET, still climbing; ramp began 04:05 ET ($1.94 → $3.46 → $3.76 → $4.56)
- Hypothetical P&L (AH entry → PM peak): **N/A — no AH entry possible** (flat in AH). PM-only move.
- Float: **1.7M** | Market Cap: $2.5M

**Best AH→PM setup: TMDE** — TMD Energy Limited (Wholesale Distributors / marine bunkering)
- Catalyst: **Jun 8 bioenergy MOA extension** with Double Corporate (2-yr extension, EU + Asia green-bioenergy collaboration). A-type partnership but **2 days stale** — Jun 10 AH run was momentum/low-float continuation, no fresh same-day catalyst.
- Previous Close: $0.84
- AH last night: late **BUILD** — flat-to-+37% until 18:30 ET, then ramped to **AH peak $1.66 (+98.6%) at 19:15 ET**
- Premarket now: **PM peak $1.49 (+78%) at 04:00 ET**, faded to ~$1.19 (+42%) by 04:22 ET
- Hypothetical P&L (AH detection entry ~$1.15 at 23:30 CET → AH peak $1.66): **+44%**; → PM peak $1.49: **+30%**
- Float: 16.5M | Market Cap: $21.4M

**Scanner Diagnostic:**
- **GLXG — Detectable at screening time? NO.** It was flat in AH (+4.9% peak, single-digit chop). The entire +343% move is a PM-only squeeze that started at 04:05 ET *this morning*. An evening AH scanner structurally cannot catch a stock that doesn't move until premarket. This is the **2nd PM-only monster in 2 mornings** (CIIT +140% on Jun 10). Like CIIT, it is out of scope for an AH-entry strategy — not a scanner failure so much as a strategy-coverage gap.
- **TMDE — Detectable at screening time? YES** (detected, not acted on). On the board at 23:30 / 00:00 / 00:30 CET, but only at +18–37% AH and choppy — correctly deemed modest (it's on the non-biotech 0/6 loss list). **Its explosive leg (+72% → +98.6%) printed 18:35–19:15 ET — AFTER our last 00:30 CET (18:30 ET) scan.**
- **Scanner gap (recurring):** the last scheduled evening scan is 00:30 CET (18:30 ET); the late-AH window (18:30–20:00 ET) goes **unscanned**. Two winners in a row made their move there — **HWH** (surge 18:45–19:00 ET, Jun 9) and now **TMDE** (18:35–19:15 ET, Jun 10). **Fix: add scans at ~01:00 and ~01:30 CET (19:00 / 19:30 ET)** to catch late-AH BUILD movers. GLXG's gap (PM-only) is a separate, harder problem — only a premarket scan/entry variant would catch it.

### Baseline Tracking

- Days tracked: **29** (was 28 + 1)
- Winners detected by scanner: **25/29 (86.2%)** — HIT, SUNE, DRMA, UGRO, NXTT, POLA, BCG, PFSA, MASK, EZGO, AIIO, HTCO, WOK, LNKS, AMST, PHGE (May 20), PHGE (May 26), SNGX, ATPC, PRFX, DXST, TWAV, CHAI, MSW, **TMDE**
- Winner selected for paper trade: **18/29 (62.1%)** — NOT incremented (we traded SKYQ, not the AH→PM winner TMDE)
- Target: >80% detection
- Status: **BASELINE MET** (86.2%)
- *Footnote:* today's biggest raw PM mover (**GLXG +343%**) was PM-only (flat AH) and is **not counted** as the AH→PM winner — same disposition as CIIT (Jun 10). The detectable AH→PM winner is **TMDE**.

### Retrospective Scan Results

Live premarket scan (04:21 ET, `scan.py --session premarket`): only 4 hits — TMDE +57%, GLXG +57.8% (stale 5m print; prepost shows +265%+), RBNE +18.7%, ELAB +7.8%.

PM reconstruction (`check-prices.py --pm-history`):
- **GLXG** — flat AH, then PM ramp $1.37 (04:00, +33%) → $1.94 → $3.46 → $3.76 → **$4.56 peak (+343%) ~04:20 ET**, still climbing. PM-only squeeze, no catalyst, 1.7M float.
- **TMDE** — AH BUILD to $1.66 (+98.6%, 19:15 ET); PM peak $1.49 (+78%, 04:00 ET), fading to +42%. Best AH→PM pattern. ← AH→PM winner.
- **RBNE** — AH late spike $1.65 (+55.7%, 17:40 ET); PM only $1.33 (+25.6%) → +13%. Faded.

### Paper Trade P&L

| Ticker | Entry | Entry Total% | Catalyst | Entry Time | PM Peak | Peak Time | Exit | P&L | P&L % | Status |
|--------|-------|--------------|----------|------------|---------|-----------|------|-----|-------|--------|
| SKYQ   | $2.28 | +46% | None — macro oil/Iran sector beta | 00:00 CET (18:00 ET) | $1.80 | 04:05 ET | (open) | −€24.94 | −25.4% | 🔴 Open |

SKYQ **round-tripped the entire AH spike**: entered $2.28 (43 sh) at the 18:00 ET base-rebuild, peaked +129% AH earlier ($3.58, before entry), faded overnight to PM **$1.70 (−25% vs entry; +9% vs $1.56 regular close)**. PM high only $1.80. Confirms the Grade-None macro-beta entry (no company catalyst, early +129% AH peak) was a poor setup. **Exit decision handled by position-evaluation.md (10:30 / 14:30 CET) — not this prompt.**

**Total Paper P&L (open): −€24.94**

### Scanner Effectiveness

- Evening scans ran: 7 times (21:30 – 00:30 CET)
- Candidates found: ~25 unique tickers
- Retrospective matches: TMDE caught (detected, not traded; explosive leg after last scan). GLXG never on the board (PM-only). SKYQ traded → faded to a loss.

### Missed Opportunities

| Ticker | AH Change | Why Missed | Would Be Profitable? |
|--------|-----------|------------|---------------------|
| GLXG | flat AH (+4.9%) | **PM-only** — move began 04:05 ET this morning; no AH signal to detect | Yes if PM-entry (+343%), but **out of scope** for an AH-entry strategy |
| TMDE | +98.6% (peak 19:15 ET) | Detected but explosive leg (18:35–19:15 ET) came **after** the 00:30 CET last scan; at scan time only +18–37% and choppy | Yes in AH→AH (+44%); one-position rule (SKYQ open) blocked entry regardless |

### AH Mover Follow-Through

| Ticker | AH Peak | Peak Time | AH Trajectory | Current PM | From Peak | From Close | Verdict |
|--------|---------|-----------|---------------|------------|-----------|------------|---------|
| SKYQ | $3.58 | 17:00 ET | Build→spike→base-hold | $1.70 | −53% | +9% | Round-tripped — our entry $2.28 now −25% (AH was the only exit) |
| TMDE | $1.66 | 19:15 ET | Late BUILD (+18% → +98.6% post-18:30) | ~$1.19 | −28% | +42% | AH→PM winner; **peaked in AH**, PM peak ($1.49) lower |
| BATL | $2.35 | 17:15 ET | Hold on near-zero volume | ~$1.60 | −32% | +22% | Oil/Iran beta; faded, no company catalyst |
| FLYE | $3.45 | 16:15 ET | Spike→fade | $2.10 | −39% | +20% | Early-peak fade confirmed |
| DAIC | $3.28 | 16:10 ET | Spike→fade | $2.41 | −27% | +25% | Reverse-split runner; held some, no catalyst |
| RBNE | $1.65 | 17:40 ET | Late spike | ~$1.20 | −27% | +13% | Shipping beta; faded |
| GLBS | $2.55 | ~18:00 ET | Hold (B-grade earnings) | $2.33 | −9% | +6% | Earnings beat fizzled into PM |

**AH-peak-vs-PM-peak check:** **Every** AH mover above peaked in AH and faded into PM — SKYQ ($3.58 AH ≫ $1.80 PM), TMDE ($1.66 AH > $1.49 PM), BATL/FLYE/DAIC/RBNE all AH > PM. TMDE adds a data point that **even a moderate AH runner (+98.6%, below the +250% "extreme" threshold) peaked in AH, not PM.** Running tally of "AH was the better exit": MSW (Jun 9, AH +292% > PM +221%), now **TMDE (Jun 10, AH +98.6% > PM +78%)** plus the whole Jun 10 board. The "take partial profit in late AH" hypothesis keeps gaining support. GLXG is the lone exception (PM ≫ AH) because it never moved in AH.

### Notes
- **Two scanner gaps exposed tonight, one fixable:**
  1. **Late-AH blind window (FIXABLE):** TMDE (Jun 10) and HWH (Jun 9) both exploded 18:35–19:15 ET, after the 00:30 CET (18:30 ET) last scan. Add 01:00 + 01:30 CET scans to cover 19:00–19:30 ET. This is the highest-value, lowest-cost scanner change available.
  2. **PM-only monsters (HARD):** GLXG (+343%, Jun 11) and CIIT (+140%, Jun 10) both stayed flat in AH and exploded only in premarket. An AH-entry strategy structurally cannot catch these. Two in two mornings — worth flagging whether a premarket-scan/entry variant deserves a learning-phase experiment.
- **SKYQ entry was a mistake the data already warned about:** Grade None (macro oil/Iran beta, no company catalyst) + early +129% AH peak that had already collapsed −36% before entry. It round-tripped to −25%. Reinforces: skip no-catalyst macro-beta names that peaked early, even when float/volume look ideal.
- **No CEILING-OVERRIDE WATCH candidates** were flagged last night (CPOP +369% was a multi-day blow-off, correctly skipped; it has since crashed to $0.36 regular close). Nothing to tally.

### Price Charts

```
GLXG — 2-Day Timeline (5-min)  [PM-only squeeze, no catalyst, 1.7M float]
Prev Close $1.03 | Current ~$4.3–4.56 (+316–343%), still running
AH path:  flat $0.96–1.08 all session (NO after-hours move)
PM path:  $1.37 (04:00) → $1.94 (04:05) → $3.46 (04:10) → $3.76 (04:20) → $4.56 peak (~04:20+)
Verdict:  Pure premarket explosion this morning; uncatchable by evening AH scanner.

TMDE — 2-Day Timeline (5-min)  [AH→PM winner, stale Jun 8 bioenergy MOA, 16.5M float]
Prev Close $0.84 | PM ~$1.19 (+42%)
AH path:  +9% (16:00) → +37.6% peak (17:10) → chop → +29% (18:30, last scan) → +72% (18:35) → +98.6% peak ($1.66, 19:15)
PM path:  $1.49 peak (+78%, 04:00) → faded to $1.18–1.19 (+41%, 04:20)
Verdict:  Late BUILD that peaked in AH; explosive leg came AFTER the 00:30 last scan. AH was the better exit.
```

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| SKYQ | $2.28 | $1.65 | -27.6% | $3.58 (AH, pre-entry) | 1 | None | **SELL** | Stop ($2.05) breached overnight; Grade None = exit at first premarket. Round-tripped entire AH spike, PM high only $1.80 |

**Actions taken:**
- **SOLD SKYQ** @ $1.65 (43 sh) → **-$27.09 (-27.6%)**. Moved to Closed Positions.
- No positions remain open. Evening trade slot is now free.

**Note:** SKYQ confirms the morning diagnosis — Grade None macro-beta entry (no company catalyst) that peaked early in AH (+129% before entry) faded all the way to a -27% loss. Stop losses do not execute in extended hours (known risk), so the -10% stop ($2.05) was blown through overnight to a -27.6% realized loss.
</content>

---

# Post-Market Screening — 2026-06-11

## Scan 21:30 CET (3:30 PM ET)

**Session: REGULAR (pre-AH).** AH opens at 22:00 CET / 4:00 PM ET. Per the regular-session caution rule, **no paper trade entries** — candidates are watch-only pending AH confirmation. Stocks that spike intraday but don't carry into AH tend to fade.

Scanner returned 56 hits; most high-% rows are single-print artifacts (5mVol 100–600 shares with VChg ~−99%, e.g. PPCB +143.7%, GELS +87.1%, ADIL +45.4%, EDHL +91.6%, GLXG +131.5% stale). Filtering for real sustained volume and reasonable float:

| Ticker | Chart | Price | Day% | 5mVol | Avg5m | IRVol | VChg% | Float | MCap | Industry | Note |
|--------|-------|-------|------|-------|-------|-------|-------|-------|------|----------|------|
| RKDA | [TV](https://www.tradingview.com/chart/?symbol=RKDA) | $1.17 | +29.0% | 172K | 108K | 1075 | +167.4% | 2.1M | 2.4M | Chemicals: Agricultural | Real volume building, low float — strongest |
| TMDE | [TV](https://www.tradingview.com/chart/?symbol=TMDE) | $1.07 | +17.6% | 28K | 28K | 20.3 | +23.7% | 16.5M | 25.2M | Wholesale Distributors | Yesterday's AH→PM winner; multi-day continuation |
| FABC | [TV](https://www.tradingview.com/chart/?symbol=FABC) | $3.89 | +15.1% | 29K | 7K | 1.0 | +660.5% | 4.5M | 18.9M | Auto Parts: OEM | Volume building into close; low float |
| RFL | [TV](https://www.tradingview.com/chart/?symbol=RFL) | $2.10 | +17.7% | 26K | 9K | 3.0 | +653.8% | 35.1M | 109.0M | Real Estate Development | Volume building; higher float |
| SBNYL | [TV](https://www.tradingview.com/chart/?symbol=SBNYL) | $2.60 | +14.0% | 78K | 9K | 18.3 | +3825% | 59.6M | 31.5M | Regional Banks | High volume but high float; bank, unlikely AH catalyst |

**Watch assessment:**
- **RKDA** — best profile on the board: 2.1M float, $2.4M MCap, highest IRVol (1075), and *real* sustained volume (172K vs 108K avg, VChg +167%). Agricultural chemicals. First-day unusual activity. Top watch for AH confirmation.
- **TMDE** — yesterday's AH→PM winner (+98.6% AH peak Jun 10), now +17.6% as a multi-day continuation. Fails "first day of unusual activity." Watch only if it builds *fresh* AH volume; stale Jun 8 bioenergy MOA catalyst.
- **FABC** — auto parts, 4.5M float, volume spiking into the close (VChg +660%). Watch for AH follow-through.
- **RFL / SBNYL** — real volume but higher float (35M / 60M); SBNYL is a regional bank preferred share, unlikely to carry an AH momentum catalyst. Lower priority.
- GLXG +131.5% is yesterday's PM-only monster (now stale, 5mVol 441, VChg −99.7%) — multi-day extension, not actionable.
- Remaining rows are single-print artifacts (5mVol 100–600, VChg ~−99%) or down >15% (ATOS −41.6%, NYC −14.9%) — not actionable.

**Decision:** No entries (pre-AH). Re-scan at 22:00+ CET once after-hours opens. Per learning-phase rules, observe-only through the 22:00/22:30 scans; only enter at 23:00+ CET a candidate with fresh sustained AH momentum (float <50M, AH >10% across ≥2 AH scans, Day% > −15%, BUILD/hold pattern, Total% < +150%). Prefer fresh first-day setups (RKDA, FABC) over TMDE's multi-day extension.

## Scan 22:00 CET (4:00 PM ET)

**Session: AFTERHOURS (just opened).** Scanner returned **0 hits** — AH opened at 16:00 ET this minute; post-market prints are still sparse so the scanner has no AH volume/% to work with yet. Observation-only scan per learning-phase rules (no entries before 23:00 CET).

No candidates found. Watch from the 21:30 list to track into AH: RKDA (2.1M float, first-day), FABC (4.5M float), TMDE (multi-day extension). Re-scan at 22:30 once AH volume builds.

## Scan 22:30 CET (4:30 PM ET)

**Session: AFTERHOURS (30 min in).** Scanner returned **7 hits**. AH opened 16:00 ET, so all trajectories are early (16:00–16:30 ET only). Observation-only per learning-phase rules (no entries before 23:00 CET).

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| RITR | [TV](https://www.tradingview.com/chart/?symbol=RITR) | $0.75 | +29.7% | +31.4% | $0.98 | +70.4% | 3.5M | 902K | 3.8x | 17.3M | REIT |
| EDHL | [TV](https://www.tradingview.com/chart/?symbol=EDHL) | $5.98 | +70.9% | +17.1% | $7.00 | +100.0% | 674K | 12.3M | 0.1x | ~0 | Advertising/Marketing |
| SMSI | [TV](https://www.tradingview.com/chart/?symbol=SMSI) | $4.55 | +26.7% | +24.6% | $5.67 | +57.9% | 2.1M | 333K | 6.3x | 5.1M | Packaged Software |
| RKDA | [TV](https://www.tradingview.com/chart/?symbol=RKDA) | $1.07 | +18.4% | +20.6% | $1.29 | +42.8% | 498K | 11.8M | 0.0x | 2.1M | Chemicals: Agricultural |
| ZDGE | [TV](https://www.tradingview.com/chart/?symbol=ZDGE) | $3.31 | +6.1% | +29.6% | $4.29 | +37.5% | 500K | 150K | 3.3x | 10.2M | Packaged Software |
| CPOP | [TV](https://www.tradingview.com/chart/?symbol=CPOP) | $1.05 | −30.9% | +13.3% | $1.19 | −21.7% | 2.4M | 52.7M | 0.0x | 20.4M | Advertising/Marketing |
| STKE | [TV](https://www.tradingview.com/chart/?symbol=STKE) | $1.21 | +3.4% | +5.8% | $1.28 | +9.4% | 55K | 189K | 0.3x | 18.9M | Financial Conglomerates |

**AH trajectory (16:00–16:30 ET, `check-prices.py --ah-history`):**
- **RITR** — +40.9% (16:00) → **+108.7% peak (16:20)** → +84.4% (16:30). Early SPIKE→FADE forming. 17.3M float, REIT.
- **SMSI** — +63.8% (16:00) → **+83.9% peak (16:05)** → hard fade to +28.1% (16:30). Immediate SPIKE→FADE. **Catalyst = 1-for-5 reverse split executed today** (mechanical price move, no operational news; warrant-exercise 13D/A on file → dilution-flavored). Reverse-split runner. 5.1M float.
- **ZDGE** — +6.1% → **+35.6% peak (16:10)** → faded back to +9.6% (near flat). SPIKE→FADE. 10.2M float.
- **RKDA** — +18.4% → **+50% peak (16:15)** → +33.9% (16:30). Mild fade, best float on board (2.1M), ag-chemicals. Watched since 21:30.
- **EDHL** — +116% (16:00) → dip +98.6% → **+175.4% peak (16:25)** → +172.6% (16:30). Only BUILD/hold profile, **but Total% +100–175% breaches the +150% extension ceiling**; Chinese micro-cap advertising name, float ~0/unknown, classic pump shape. Watch, not a candidate.
- **CPOP** — Day **−30.9%** → **DISQUALIFIED** (Day% below −15% = dead-cat bounce).
- **STKE** — AH +5.8% (below 10% threshold), modest. Not actionable.

**Observation assessment:** It's 30 min into AH. Four of five real movers (RITR, SMSI, ZDGE, RKDA) already peaked 16:05–16:20 ET and are fading — early SPIKE→FADE shapes. EDHL is the lone BUILD but is over the extension ceiling with unknown float. No fresh first-day operational catalyst confirmed yet (SMSI = reverse split, the rest unchecked pending 23:00). **No entries (observation-only + pre-23:00).** Re-scan at 23:00 CET: if RITR/RKDA/ZDGE keep fading they're skips; only act on a candidate that builds/holds a fresh AH base, float <50M, AH >10% across ≥2 AH scans, Day% > −15%, Total% < +150%. RKDA (2.1M float) is the float standout to watch if it stops fading.

## Scan 23:00 CET (5:00 PM ET)

**Session: AFTERHOURS (1h in).** Scanner returned **11 hits**. Entries now allowed (23:00+ CET). AH peak times are 16:00–17:00 ET.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| RITR | [TV](https://www.tradingview.com/chart/?symbol=RITR) | $0.75 | +29.7% | +20.7% | $0.90 | +56.5% | 11.2M | 1.7M | 6.5x | 17.3M | REIT |
| BYAH | [TV](https://www.tradingview.com/chart/?symbol=BYAH) | $1.05 | −15.3% | +98.1% | $2.08 | +67.7% | 5.3M | 3.2M | 1.7x | 1.0M | Household/Personal Care |
| RKDA | [TV](https://www.tradingview.com/chart/?symbol=RKDA) | $1.07 | +18.4% | +14.0% | $1.22 | +35.1% | 4.3M | 12.2M | 0.4x | 2.1M | Chemicals: Agricultural |
| EDHL | [TV](https://www.tradingview.com/chart/?symbol=EDHL) | $5.98 | +70.9% | +46.3% | $8.75 | +150.0% | 2.4M | 12.5M | 0.2x | ~0 | Advertising/Marketing |
| RKTO | [TV](https://www.tradingview.com/chart/?symbol=RKTO) | $1.48 | +11.3% | +19.6% | $1.77 | +33.1% | 654K | 12.7M | 0.1x | 21.7M | Pharma: Major |
| MTEN | [TV](https://www.tradingview.com/chart/?symbol=MTEN) | $2.29 | +33.9% | +9.6% | $2.51 | +46.8% | 476K | 12.4M | 0.0x | 843K | Industrial Machinery |
| TOON | [TV](https://www.tradingview.com/chart/?symbol=TOON) | $1.08 | +24.1% | +5.6% | $1.14 | +31.0% | 272K | 3.9M | 0.1x | 55.9M | Movies/Entertainment |
| CPSH | [TV](https://www.tradingview.com/chart/?symbol=CPSH) | $8.59 | +26.1% | +6.9% | $9.18 | +34.8% | 262K | 3.6M | 0.1x | 15.6M | Metal Fabrication |

**AH trajectory (16:00–17:00 ET, `check-prices.py --ah-history`):**
- **RKDA** — +18.4% (16:00) → **+50% peak (16:15)** → holding +39.5% ($1.26) at 17:00, within ~7% of high. **HOLD pattern.** 2.1M float, **116M regular-session volume** (real, not artifact). Catalyst: structured search → QuiverQuant/StocksToTrade both confirm *"no clear new headline catalyst"* — pure low-float speculative pump. No catalyst (concern noted, not a skip in learning phase). Total% +35% (well under ceiling), Day +18.4%. **Best qualifying candidate.**
- **RITR** — +40.9% (16:00) → **+108.7% peak (16:20)** → faded to +39.2% ($0.80) at 17:00. Clear early-peak SPIKE→FADE. 17.3M float. Skip per SPIKE→FADE rule (0/10+).
- **BYAH** — Day **−15.3%** (dead-cat). Flat/down until 16:20, then **+66.9% peak (16:40)** → fading to +31.5% (17:00). Dead-cat bounce + SPIKE→FADE. 1.0M float but disqualified (Day% ≤ −15%, recovering from sell-off).
- **MTEN** — +33.9% → **+55% peak (16:45)** → +35.7% (17:00). 843K float, but catalyst = **$2.26M registered direct offering** priced/closed Jun 9–10 (dilution, **Grade D**). Skip — dilution. Also only 1 AH scan.
- **EDHL** — BUILD/hold to **+178.6% peak (16:30)**, holding +178% (17:00). **Total% +150–178% breaches the +150% extension ceiling.** Ceiling-override check: VRatio 0.2 (<5x) and peak before 17:00 ET → **fails override criteria.** Chinese micro-cap pump shape, float ~0. Skip.
- **RKTO / TOON / CPSH** — AH chg under threshold or float too high (TOON 55.9M); RKTO modest +19.6% but 21.7M float, pharma with no confirmed catalyst. Not actionable.

**Decision: ENTER RKDA** @ $1.26 (79 sh ≈ €100). Only candidate clearing all entry gates: float 2.1M (<50M ✓), AH >10% across 2 AH scans (22:30 +20.6%, 23:00 +14–20% ✓), Day% +18.4% (> −15% ✓), Total% +35% (< +150% ✓), HOLD pattern within ~7% of AH high (not a fade ✓). Catalyst grade **None** — no catalyst found (concern noted); per learning-phase no-catalyst handling, enter with concern, exit at first premarket opportunity. RITR/BYAH SPIKE→FADE and EDHL ceiling-breach correctly skipped; MTEN dilution skipped.

## Scan 23:30 CET (5:30 PM ET)

**Session: AFTERHOURS (1.5h in).** Scanner returned **13 hits**. AH peak times now span 16:00–17:30 ET. **A position is already open (RKDA, entered 23:00 CET) — the one-position rule blocks any new entry tonight.** This scan is for tracking and for confirming the held position's behavior.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| RITR | [TV](https://www.tradingview.com/chart/?symbol=RITR) | $0.75 | +29.7% | +14.1% | $0.85 | +47.9% | 13.3M | 1.9M | 6.9x | 17.3M | REIT |
| BYAH | [TV](https://www.tradingview.com/chart/?symbol=BYAH) | $1.05 | −15.3% | +101.0% | $2.11 | +70.2% | 9.3M | 3.7M | 2.5x | 1.0M | Household/Personal Care |
| RKTO | [TV](https://www.tradingview.com/chart/?symbol=RKTO) | $1.48 | +11.3% | +16.9% | $1.73 | +30.1% | 7.6M | 13.5M | 0.6x | 21.7M | Pharma: Major |
| RKDA | [TV](https://www.tradingview.com/chart/?symbol=RKDA) | $1.07 | +18.4% | +17.3% | $1.25 | +38.9% | 4.7M | 12.3M | 0.4x | 2.1M | Chemicals: Agricultural |
| EDHL | [TV](https://www.tradingview.com/chart/?symbol=EDHL) | $5.98 | +70.9% | +49.2% | $8.92 | +154.9% | 3.2M | 12.7M | 0.3x | ~0 | Advertising/Marketing |
| VSME | [TV](https://www.tradingview.com/chart/?symbol=VSME) | $1.11 | −45.9% | +32.9% | $1.48 | −28.0% | 2.9M | 23.6M | 0.1x | 2.6M | Advertising/Marketing |
| CCHH | [TV](https://www.tradingview.com/chart/?symbol=CCHH) | $0.52 | +50.3% | +15.1% | $0.60 | +72.9% | 2.5M | 16.9M | 0.1x | 4.1M | Restaurants |
| ZDGE | [TV](https://www.tradingview.com/chart/?symbol=ZDGE) | $3.31 | +6.1% | +7.3% | $3.55 | +13.8% | 1.3M | 253K | 5.3x | 10.2M | Packaged Software |
| MTEN | [TV](https://www.tradingview.com/chart/?symbol=MTEN) | $2.29 | +33.9% | +7.0% | $2.45 | +43.3% | 1.2M | 12.5M | 0.1x | 843K | Industrial Machinery |
| SDEV | [TV](https://www.tradingview.com/chart/?symbol=SDEV) | $1.09 | +1.9% | +15.6% | $1.26 | +17.8% | 643K | 211K | 3.0x | 27.1M | Pharma: Major |
| CPSH | [TV](https://www.tradingview.com/chart/?symbol=CPSH) | $8.59 | +26.1% | +5.4% | $9.05 | +32.9% | 297K | 3.6M | 0.1x | 15.6M | Metal Fabrication |
| KMRK | [TV](https://www.tradingview.com/chart/?symbol=KMRK) | $1.44 | −22.6% | +9.0% | $1.57 | −15.6% | 72K | 2.1M | 0.0x | 4.6M | Misc Commercial Services |
| FJET | [TV](https://www.tradingview.com/chart/?symbol=FJET) | $6.75 | −16.7% | +5.9% | $7.15 | −11.7% | 72K | 4.0M | 0.0x | 29.4M | Misc Commercial Services |

**AH trajectory (16:00–17:30 ET, `check-prices.py --ah-history`):**
- **RKDA (HELD)** — +18.4% (16:00) → **+50% peak ($1.35, 16:15)** → tight chop $1.24–1.30, holding **+37.3% ($1.24) at 17:30**, within ~8% of high. **HOLD pattern intact** 2.5h into AH. Entry $1.26 → now $1.24 (−1.6%). Behaving as a base-hold, not a fade. Position thesis unchanged; exit handled by position-evaluation.md in premarket.
- **BYAH** *(new build)* — Day −15.3% dead-cat, flat to 16:20 then **strong BUILD: +66.9% (16:40) → +84.7% (17:20) → +103.9% peak ($2.53, 17:30)**, making new highs. 1.0M float. Best BUILD shape on the board — **but disqualified: Day% −15.3% (dead-cat-bounce rule, recovering from a sell-off).** Track for the retrospective; do not enter.
- **RITR** — still SPIKE→FADE: +108.7% peak (16:20) → faded to +33.9% (17:05), small recovery to +49.6% (17:30). 17.3M float. Skip (0/10+).
- **EDHL** — still over ceiling: holding +144–178% all session, +144% ($8.54) at 17:30. Total% +155% breaches +150% extension ceiling; VRatio 0.3 (<5x) → fails ceiling-override. Chinese micro-cap pump, float ~0. Skip.
- **CCHH** *(new)* — Day +50.3%; held +47–56% then **late spike +108.4% (17:05) → faded to +65% (17:30)**. SPIKE→FADE off the 17:05 high. 4.1M float, Restaurants. Skip (SPIKE→FADE).
- **SDEV** *(new)* — Day +1.9%; clean BUILD +1.9% (16:00) → **+26.6% peak ($1.35, 17:25), holding +26.2% (17:30)**, near high. Only genuine non-disqualified BUILD besides BYAH, but float 27.1M and modest +15.6% AH on one scan. Track; cannot enter (position open).
- **ZDGE** — SPIKE→FADE: +35.6% peak (16:10) → +11.7% (17:24). Skip.
- **VSME (−45.9%) / KMRK (−22.6%) / FJET (−16.7%)** — all Day% ≤ −15% → disqualified (dead-cat / recovering from sell-off).
- **RKTO / MTEN / CPSH** — modest AH (<20%), no fresh catalyst confirmed; not actionable.

**Decision: No new entry — RKDA position already open (one trade per day, one position at a time).** Even absent that block, tonight's fresh BUILD candidates are disqualified or unusable: BYAH (best BUILD, +103.9%) is a Day −15.3% dead-cat; SDEV builds cleanly but is a modest 27.1M-float move; the rest are SPIKE→FADE (RITR, CCHH, ZDGE) or ceiling-breach (EDHL). Held RKDA is holding its base (+37% at 17:30, ~8% off AH high). Next scan continues tracking; entries remain blocked while RKDA is open.

## Scan 00:00 CET (6:00 PM ET)

**Session: AFTERHOURS (2h in).** Scanner returned **14 hits**. AH peak times span 16:00–18:00 ET. **A position is already open (RKDA, entered 23:00 CET) — the one-position rule blocks any new entry tonight.** This scan tracks the held position and logs new movers for the retrospective.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| BYAH | [TV](https://www.tradingview.com/chart/?symbol=BYAH) | $1.05 | −15.3% | +130.4% | $2.42 | +95.1% | 15.4M | 4.4M | 3.5x | 1.0M | Household/Personal Care |
| RITR | [TV](https://www.tradingview.com/chart/?symbol=RITR) | $0.75 | +29.7% | +16.6% | $0.87 | +51.2% | 13.9M | 2.0M | 7.0x | 17.3M | REIT |
| RKTO | [TV](https://www.tradingview.com/chart/?symbol=RKTO) | $1.48 | +11.3% | +29.7% | $1.92 | +44.4% | 9.4M | 13.7M | 0.7x | 21.7M | Pharma: Major |
| VSME | [TV](https://www.tradingview.com/chart/?symbol=VSME) | $1.11 | −45.9% | +94.6% | $2.16 | +5.4% | 5.2M | 23.9M | 0.2x | 2.6M | Advertising/Marketing |
| RKDA | [TV](https://www.tradingview.com/chart/?symbol=RKDA) | $1.07 | +18.4% | +16.8% | $1.25 | +38.4% | 4.9M | 12.3M | 0.4x | 2.1M | Chemicals: Agricultural |
| CCHH | [TV](https://www.tradingview.com/chart/?symbol=CCHH) | $0.52 | +50.3% | +18.9% | $0.62 | +78.7% | 3.5M | 17.1M | 0.2x | 4.1M | Restaurants |
| EDHL | [TV](https://www.tradingview.com/chart/?symbol=EDHL) | $5.98 | +70.9% | +38.8% | $8.30 | +137.1% | 3.5M | 12.7M | 0.3x | ~0 | Advertising/Marketing |
| OTLK | [TV](https://www.tradingview.com/chart/?symbol=OTLK) | $1.10 | +23.6% | +8.2% | $1.19 | +33.7% | 2.0M | 20.9M | 0.1x | 98.7M | Pharma: Major |
| RUBI | [TV](https://www.tradingview.com/chart/?symbol=RUBI) | $0.62 | +32.0% | +17.2% | $0.73 | +54.7% | 1.9M | 22.5M | 0.1x | ~0 | Marine Shipping |
| MTEN | [TV](https://www.tradingview.com/chart/?symbol=MTEN) | $2.29 | +33.9% | +9.2% | $2.50 | +46.2% | 1.4M | 12.5M | 0.1x | 843K | Industrial Machinery |
| SDEV | [TV](https://www.tradingview.com/chart/?symbol=SDEV) | $1.09 | +1.9% | +18.3% | $1.29 | +20.6% | 1.1M | 258K | 4.1x | 27.1M | Pharma: Major |
| CPSH | [TV](https://www.tradingview.com/chart/?symbol=CPSH) | $8.59 | +26.1% | +5.6% | $9.07 | +33.2% | 309K | 3.6M | 0.1x | 15.6M | Metal Fabrication |
| KMRK | [TV](https://www.tradingview.com/chart/?symbol=KMRK) | $1.44 | −22.6% | +7.6% | $1.55 | −16.7% | 100K | 2.1M | 0.0x | 4.6M | Misc Commercial Services |
| FJET | [TV](https://www.tradingview.com/chart/?symbol=FJET) | $6.75 | −16.7% | +6.7% | $7.20 | −11.1% | 98K | 4.0M | 0.0x | 29.4M | Misc Commercial Services |

**AH trajectory (16:00–18:00 ET, `check-prices.py --ah-history`):**
- **RKDA (HELD)** — +18.4% (16:00) → **+50% peak ($1.35, 16:15)** → tight chop $1.18–1.30 for two hours, **+39.5% ($1.26) at 18:00**, within ~7% of high. **HOLD pattern intact** 2h into AH; entry $1.26 → $1.26 (flat, 0.0%). Behaving as a base-hold, not a fade. Thesis unchanged; exit handled by position-evaluation.md in premarket.
- **BYAH** *(building)* — Day −15.3% dead-cat, but the strongest BUILD on the board: +66.9% (16:40) → +103.9% (17:30) → **+130.4% peak ($2.42, ~18:00)**, making new highs late. 1.0M float. **Disqualified: Day% −15.3% (dead-cat-bounce rule).** Track for retrospective only — this is the night's best BUILD shape and a clean test of whether the dead-cat filter is costing winners.
- **RUBI** *(new, late build)* — Day +32%; flat +32% base 16:05–17:20, then **late ramp to +67% peak ($0.79, 17:45)** → holding +53% (18:00). Genuine late BUILD, float ~0/unknown, marine shipping (sector beta — shipping names BATL/RBNE/GLBS all faded recently). Not actionable (position open); modest +17% AH and unknown float anyway.
- **OTLK** *(new)* — Day +23.6%; steady BUILD +23.6% → **+44.7% peak (17:25)** → holding +38% (18:00). 98.7M float (far over the <50M gate), pharma. Track only.
- **RITR** — still SPIKE→FADE off the +108.7% (16:20) peak, now +16.6%. Skip (0/10+).
- **EDHL** — fading off the +178.6% (16:30) peak to +137% (18:00); still over the +150%-ish extension ceiling earlier, VRatio 0.3 (<5x) → fails ceiling-override. Chinese micro-cap pump. Skip.
- **CCHH** — SPIKE→FADE off +108.4% (17:05) high, now +18.9%. Skip.
- **VSME (−45.9%) / KMRK (−22.6%) / FJET (−16.7%)** — Day% ≤ −15% → disqualified (dead-cat).
- **RKTO / MTEN / CPSH / SDEV** — modest AH or float over gate (SDEV 27.1M, RKTO 21.7M); no fresh catalyst confirmed. Not actionable.

**Decision: No new entry — RKDA position already open (one trade per day, one position at a time).** Held RKDA is holding its base (+39.5% at 18:00, ~7% off AH high, entry flat). Tonight's fresh BUILD names are disqualified or unusable anyway: BYAH (best BUILD, +130%) is a Day −15.3% dead-cat; RUBI builds late but is shipping beta with unknown float and only +17% AH; OTLK builds but float 98.7M ≫ gate. The rest are SPIKE→FADE (RITR, CCHH) or ceiling-breach (EDHL). Entries remain blocked while RKDA is open; next scan continues tracking.

## Paper Trades

| Ticker | Entry Price | Entry Time | Shares (~€100) | Catalyst Grade | Reason |
|--------|-------------|------------|-----------------|----------------|--------|
| RKDA | $1.26 | 23:00 CET (17:00 ET) | 79 | None | 2.1M float, HOLD pattern (+50% AH peak 16:15, holding +39.5% within ~7% of high), 116M reg-session vol, Total% +35% under ceiling. No catalyst — speculative low-float pump (concern noted, exit at first premarket). |
