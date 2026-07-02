# 2026-07-02

## Position Evaluation — 10:30 CET

**Alpaca (source of truth):** No open positions. Account equity $99,997.66, cash $99,997.66.

Reconciliation: `OPEN_POSITIONS.md` still listed ALZN as open. The ALZN SELL (73 @ $1.29 ext, id f7da27e2) submitted in the 2026-07-01 10:30 run filled 2026-07-01 08:33 UTC at $1.29. Moved ALZN to Closed Positions.

| Ticker | Entry | Exit | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|------|-------|------|------|-------|----------|--------|
| ALZN | $1.31 | $1.29 | -1.5% | $1.45 (+10.7%) | 1 | None | CLOSED | SELL filled @ $1.29; Grade None exit-first-PM rule. Real fill −$1.46. |

**Actions taken:**
- Reconciled OPEN_POSITIONS.md against Alpaca; moved ALZN to Closed (real fill $1.29, −$1.46 / −1.5%).
- No open positions to evaluate. Nothing to hold, trail, or sell.

## Position Evaluation — 14:30 CET

**Alpaca (source of truth):** No open positions. Account equity $99,997.63, cash $99,997.63.

`OPEN_POSITIONS.md` already reflects zero open positions (reconciled at 10:30). Nothing to hold, trail, or sell.

**Actions taken:**
- None. No open positions.

## Scan 21:30 CET (3:30 PM ET)

**REGULAR session scan** (pre-AH; after-hours opens 22:00 CET / 4:00 PM ET). No entries per regular-session caution rule — candidates flagged Watch pending AH confirmation.

Top intraday movers (57 hits). Columns: intraday relative-vol (IRVol), volume change %, float, mcap.

| Ticker | Price | Chg% | IRVol | VChg% | Float | MCap | Industry | Note |
|--------|-------|------|-------|-------|-------|------|----------|------|
| SKFG | $0.53 | +367.8% | 44.7 | +738% | 1.6M | 1.1M | Apparel Retail | Watch — low float, live volume |
| SDEV | $1.39 | +33.2% | 104.1 | -39.8% | 1.6M | 69.9M | Pharma | Watch — high IRVol, volume fading |
| CLRO | $6.59 | +104.7% | 1974 | -99.9% | 740K | 8.6M | Electronics | Volume collapsed intraday — likely faded |
| CWD | $1.14 | +75.9% | 3799 | -100% | 8.3M | 10.0M | Investment Mgrs | Volume gone — spike over |
| WMTN | $0.68 | +458.4% | 5.6 | +0.0% | 11.1M | 13.6M | Precious Metals | Watch — big move, modest vol |
| VCBDD | $1.00 | +2089.9% | 0.1 | -95.4% | 297K | 329K | Misc Commercial | Nano-cap, thin |

**Decision:** No paper trades. AH not open. Re-scan at 22:00+ CET to confirm which of these carry into after-hours with sustained momentum. Per plan, learning-phase entries only start at 23:00 CET (5:00 PM ET) scans anyway.

## Scan 22:00 CET (4:00 PM ET)

**AH session scan** (after-hours just opened at 16:00 ET). Scanner returned 0 hits — no symbols meeting AH spike criteria yet. Expected: AH volume/prices take 15-30 min to build after 4:00 PM ET.

No candidates found.

**Decision:** No paper trades (observation-only scan per learning phase; entries start at 23:00 CET). Re-scan at 22:30 and 23:00 to catch AH movers as volume builds. None of the 21:30 regular-session watch names (SKFG, SDEV, WMTN, etc.) surfaced in the AH scan.

## Scan 22:30 CET (4:30 PM ET)

**AH session scan** (4:30 PM ET). Scanner returned 3 hits — all new (22:00 had 0). SIP verified.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| UPC | [TV](https://www.tradingview.com/chart/?symbol=UPC) | $6.32 | +13.7% | +42.4% | $9.00 | +61.9% | 1.0M | 7.8M | 0.1x | 326K | Pharma: Major |
| ICON | [TV](https://www.tradingview.com/chart/?symbol=ICON) | $1.04 | +0.0% | +22.1% | $1.27 | +22.1% | 631K | 138K | 4.6x | 0 | Marine Shipping |
| UK | [TV](https://www.tradingview.com/chart/?symbol=UK) | $2.07 | +0.0% | +8.7% | $2.25 | +8.7% | 118K | 73K | 1.6x | 665K | Real Estate Dev |

**SIP verification (bars from 20:00Z):**
- **UPC** — Real accumulation: 143K → 763K → 601K → 272K sh/bar, 2.2K–16.5K trades/bar. Peaked $9.36 at 16:10 ET, now bid $8.86 / ask $9.19 x100 (real two-sided book). Holding within ~5% of AH high. BUILD pattern, Total +62% (under 150% ceiling), float 326K nano. **Strong watch for 23:00.**
- **ICON** — Building hard: 636 → 4.5K → 670K → 1.78M sh/bar, making new AH high ($1.43 at 16:15 ET). Book bid $1.40 / ask $1.41 x100. BUILD, Total +22% (low extension). **Strong watch for 23:00.**
- **UK** — Only +8.7% AH (below 10% threshold). Spiked $2.48 (16:10 ET) → fading $2.16. Quote wide/stale (bid $1.76 / ask $2.34 @ 16:00 ET). SPIKE→FADE, sub-threshold. **Skip-tier.**

**Decision:** No paper trades (observation-only per learning phase; entries start at 23:00 CET / 5:00 PM ET). UPC and ICON both show BUILD patterns with real SIP volume and fillable books — primary watch names for the 23:00 scan. Need each to hold >10% AH across the 23:00 scan and clear entry gates (Day% > -15%, Total% < 150%, not a fade). No catalyst search yet — will run at 23:00 for any that clear.

## Scan 23:00 CET (5:00 PM ET)

**AH session scan** (5:00 PM ET). Scanner returned 5 hits. This is the first entry-eligible scan of the night (learning-phase entries start at 23:00).

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| ICON | [TV](https://www.tradingview.com/chart/?symbol=ICON) | $1.04 | +0.0% | +35.6% | $1.41 | +35.6% | 6.5M | 783K | 8.3x | ~3.3M mcap | Marine Shipping |
| CLRO | [TV](https://www.tradingview.com/chart/?symbol=CLRO) | $6.48 | +101.2% | +18.2% | $7.66 | +137.9% | 2.7M | 8.6M | 0.3x | 740K | Electronics/Appliances |
| UPC | [TV](https://www.tradingview.com/chart/?symbol=UPC) | $6.32 | +13.7% | +31.2% | $8.29 | +49.1% | 2.3M | 8.0M | 0.3x | 326K | Pharmaceuticals: Major |
| CRE | [TV](https://www.tradingview.com/chart/?symbol=CRE) | $2.49 | +1.6% | +17.3% | $2.92 | +19.2% | 399K | 117K | 3.4x | 1.1M | Commercial Printing |
| SLGB | [TV](https://www.tradingview.com/chart/?symbol=SLGB) | $0.63 | -4.5% | +6.3% | $0.67 | +1.6% | 54K | 273K | 0.2x | 3.0M | Air Freight/Couriers |

**Two-AH-scan qualifiers (>10% AH in ≥2 AH scans, 22:00+ CET):** ICON (22:30 +22% → 23:00 +35.6%) and UPC (22:30 +42.4% → 23:00 +31.2%). CLRO appeared in the 21:30 regular scan only (regular appearances don't count) — first AH scan tonight. CRE new. SLGB below 10% threshold.

**SIP verification + live book (bars to 16:45 ET, quotes fresh at ~16:57-16:59 ET):**
- **ICON** — Real accumulation: 670K → 1.78M → 1.18M → 1.06M → 811K → 341K → 1.33M → 1.40M sh/bar, 2K–8.8K trades/bar. AH peak $1.49 at **16:40 ET**. Live quote bid $1.19 / ask $1.20 x300 @ 16:59 (fresh) — now **-19.5% off the AH high, rolling over**. Peaked before 17:30 and declining = SPIKE→FADE. **Catalyst:** Icon Energy Corp (Greek LNG shipping); 4 searches (earnings, PR, 8-K) found **no ticker-specific catalyst** → no catalyst found.
- **UPC** — Real volume (143K–763K sh/bar early), AH peak $9.69 at **16:20 ET** (very early), steady decline since: $8.85 → $8.30 → $8.10 by 16:45. Quote bid $8.02 / ask $8.17 @ 16:42, ~-16% off high. Clear SPIKE→FADE. **Catalyst:** Universe Pharmaceuticals (China pharma); already in a multi-day run — $2.96 close Jun 26 → $6.32 close Jul 2 (+113% over the week). No fresh Jul 2 PR/earnings surfaced in searches. Extended, no new catalyst.
- **CLRO** — Holding best: dipped to $6.15, ramped $7.34 → $8.20 (peak 16:40 ET), live bid $7.59 / ask $7.70 @ 16:57 (only -6% off high). BUT Day% **+101.2%** — already exploded in the regular session; Total% +137.9% is an extended regular-session-continuation, not a fresh AH spike. Only **1 AH scan** (fails the 2-AH-scan gate).
- **CRE** — AH peaked $4.37 at 16:30 ET, faded to $2.94–3.05 (**-30% off high**). Book bid $2.14 / ask $2.98 wide/stale @ 16:00. SPIKE→FADE, 1 AH scan.
- **SLGB** — AH +6.3%, Total +1.6%, below the 10% threshold. Skip-tier.

**Decision: No paper trades.** Both two-AH-scan qualifiers (ICON, UPC) peaked before 17:30 ET and are declining at entry time — a **SPIKE→FADE-only night among qualifiers**. Per the SPIKE→FADE rule, skip all rather than enter the least-bad option (SPIKE→FADE stocks are 0/10+ for PM continuation). CLRO holds better but fails the 2-AH-scan gate and is an extended (+101% Day) regular-session continuation. CRE faded -30%; SLGB sub-threshold. No dead-cat-override (no Day% ≤ -15% candidate) or ceiling-override (all under +150% Total%) flags apply. A skip here avoids a predictable loss; will re-scan at 23:30 / 00:00 for BUILD/hold patterns as later movers emerge.

## Scan 23:30 CET (5:30 PM ET)

**AH session scan** (5:30 PM ET). Scanner returned 9 hits. New vs prior scans: ZCMD, LHSW, SEER, ILAG, YYGH. Prior names ICON/UPC/CLRO/CRE still present but fading.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| ZCMD | [TV](https://www.tradingview.com/chart/?symbol=ZCMD) | $1.11 | -0.9% | +450.5% | $6.11 | +445.5% | 6.6M | 4.1M | 1.6x | 1.1M | Misc Commercial |
| SEER | [TV](https://www.tradingview.com/chart/?symbol=SEER) | $1.62 | -0.6% | +31.5% | $2.13 | +30.7% | 2.6M | 581K | 4.5x | 36.2M | Biotechnology |
| LHSW | [TV](https://www.tradingview.com/chart/?symbol=LHSW) | $1.80 | +1.7% | +25.6% | $2.26 | +27.7% | 3.6M | 1.1M | 3.2x | 147K | Computer Proc Hardware |
| ICON | [TV](https://www.tradingview.com/chart/?symbol=ICON) | $1.04 | +0.0% | +9.6% | $1.14 | +9.6% | 9.4M | 1.1M | 8.5x | ~3.3M mcap | Marine Shipping |
| CLRO | [TV](https://www.tradingview.com/chart/?symbol=CLRO) | $6.48 | +101.2% | +10.8% | $7.18 | +123.1% | 3.6M | 8.7M | 0.4x | 740K | Electronics/Appliances |
| UPC | [TV](https://www.tradingview.com/chart/?symbol=UPC) | $6.32 | +13.7% | +14.9% | $7.26 | +30.6% | 2.7M | 8.1M | 0.3x | 326K | Pharmaceuticals: Major |
| CRE | [TV](https://www.tradingview.com/chart/?symbol=CRE) | $2.49 | +1.6% | +13.7% | $2.83 | +15.5% | 530K | 135K | 3.9x | 1.1M | Commercial Printing |
| ILAG | [TV](https://www.tradingview.com/chart/?symbol=ILAG) | $3.49 | -3.6% | +5.2% | $3.67 | +1.4% | 109K | 35K | 3.1x | 987K | Tools & Hardware |
| YYGH | [TV](https://www.tradingview.com/chart/?symbol=YYGH) | $1.25 | -3.8% | +8.7% | $1.36 | +4.5% | 53K | 1.1M | 0.0x | 133K | Misc Commercial |

**Two-AH-scan gate (>10% AH in ≥2 AH scans, 22:00+ CET):** UPC (3 scans), ICON (22:30/23:00 qualified, now faded to +9.6%), CLRO (23:00 +18.2%, 23:30 +10.8% — but +101% Day extended regular continuation), CRE (23:00 +17.3%, 23:30 +13.7%). All three new movers (ZCMD, SEER, LHSW) are on their **first AH scan** — fail the 2-AH-scan gate regardless of trajectory.

**SIP verification (bars to 21:15Z / 17:15 ET — fresh, ~15 min lag; quotes returned stale IEX 16:00–16:59 ET, so trajectory read off SIP bars):**
- **ZCMD** — **Real explosive move.** SIP accumulation 418K → 1.05M → 2.6M → 2.13M → 2.08M → 1.74M sh/bar, 2.7K–25K trades/bar. Peaked $6.57 at **17:15 ET**, holding $6.06 (within 8% of high) = BUILD/hold. Genuine +445% on 10M+ real AH shares. **Skip:** Total% +445% massively exceeds the +150% ceiling; VRatio 1.6x (real ~2.4x vs avg) fails the >5x ceiling-override gate; and first AH scan (fails 2-AH gate). Not a ceiling-override watch (VRatio gate fails). **Notable real mover for tomorrow's retrospective** — came late (first surfaced 17:30 ET) and too extended to enter.
- **SEER** — Real volume, peaked $2.33 at **17:00 ET**, holding $2.17 (within ~7% of high) but volume fading across bars (1.1M → 1.12M → 779K → 364K sh/bar). Biotech, float 36.2M. First AH scan → fails 2-AH gate. Watch for 00:00.
- **LHSW** — Peaked $3.40 at **16:55 ET**, faded to $2.31 = **−32% off high** (>20%). SPIKE→FADE. Low float 147K. First AH scan. Skip-tier.
- **UPC** — Continues fading: peaked $9.69 at 16:20 ET, now $7.26 (−25% off high). SPIKE→FADE, extended multi-day run, no fresh catalyst. Skip.
- **ICON** — Faded below threshold (+35.6% at 23:00 → +9.6% now). SPIKE→FADE confirmed, rolling over. Skip.
- **CLRO** — +101% Day extended regular-session continuation, fading in AH ($8.20 peak → $7.18). Skip.
- **CRE** — Still holding low base $2.83 far below its $4.37 AH high (16:30 ET), −35% off high. SPIKE→FADE. Skip.
- **ILAG / YYGH** — AH +5.2% / +8.7%, both below the 10% threshold. Skip-tier.

**Decision: No paper trades.** No candidate clears all entry gates. The three fresh BUILD/mover candidates (ZCMD, SEER, LHSW) are all on their first AH scan and fail the 2-AH-scan requirement. The two-AH-scan qualifiers (UPC, ICON, CRE, CLRO) are all SPIKE→FADE or extended regular-session continuations — a SPIKE→FADE-only night among qualifiers, skip all per the 0/10+ rule. ZCMD is a genuine +445% AH explosion on 10M+ real shares but exceeds the +150% ceiling with VRatio too low for override; logged for tomorrow's retrospective. No dead-cat-override (no Day% ≤ -15% candidate) applies. Re-scan at 00:00 CET — if ZCMD/SEER hold and post a 2nd qualifying AH scan, re-evaluate (ZCMD would still need VRatio >5x to clear the ceiling-override).

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
