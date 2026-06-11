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
</content>
