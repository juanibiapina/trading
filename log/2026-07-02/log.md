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

## Scan 00:00 CET (6:00 PM ET)

**AH session scan** (6:00 PM ET). Scanner returned 13 hits. New vs prior scans: RDGT, HLP, UFG, RAYA, NCT, ALZN, GNLN. Prior names ZCMD, SEER, CLRO, UPC, CRE, ILAG still present.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| ZCMD | [TV](https://www.tradingview.com/chart/?symbol=ZCMD) | $1.11 | -0.9% | +404.5% | $5.60 | +400.0% | 10.6M | 4.7M | 2.3x | 1.1M | Misc Commercial |
| SEER | [TV](https://www.tradingview.com/chart/?symbol=SEER) | $1.62 | -0.6% | +34.6% | $2.18 | +33.8% | 4.6M | 805K | 5.7x | 36.2M | Biotechnology |
| RDGT | [TV](https://www.tradingview.com/chart/?symbol=RDGT) | $1.53 | +5.5% | +6.5% | $1.63 | +12.4% | 4.0M | 10.5M | 0.4x | 884K | Medical Distributors |
| CLRO | [TV](https://www.tradingview.com/chart/?symbol=CLRO) | $6.48 | +101.2% | +11.9% | $7.25 | +125.2% | 4.0M | 8.7M | 0.5x | 740K | Electronics/Appliances |
| UPC | [TV](https://www.tradingview.com/chart/?symbol=UPC) | $6.32 | +13.7% | +16.0% | $7.33 | +31.8% | 2.8M | 8.1M | 0.3x | 326K | Pharmaceuticals: Major |
| HLP | [TV](https://www.tradingview.com/chart/?symbol=HLP) | $0.75 | +34.4% | +6.6% | $0.80 | +43.3% | 988K | 5.7M | 0.2x | 44.4M | Metal Fabrication |
| CRE | [TV](https://www.tradingview.com/chart/?symbol=CRE) | $2.49 | +1.6% | +9.6% | $2.73 | +11.4% | 574K | 141K | 4.1x | 1.1M | Commercial Printing |
| UFG | [TV](https://www.tradingview.com/chart/?symbol=UFG) | $0.69 | -6.4% | +14.8% | $0.79 | +7.4% | 325K | 156K | 2.1x | 9.8M | Wholesale Distributors |
| RAYA | [TV](https://www.tradingview.com/chart/?symbol=RAYA) | $2.79 | +1.1% | +7.0% | $2.98 | +8.1% | 262K | 82K | 3.2x | 975K | Electrical Products |
| ILAG | [TV](https://www.tradingview.com/chart/?symbol=ILAG) | $3.49 | -3.6% | +5.2% | $3.67 | +1.4% | 109K | 35K | 3.1x | 987K | Tools & Hardware |
| NCT | [TV](https://www.tradingview.com/chart/?symbol=NCT) | $3.25 | +3.5% | +6.8% | $3.47 | +10.5% | 79K | 80K | 1.0x | 321K | Marine Shipping |
| ALZN | [TV](https://www.tradingview.com/chart/?symbol=ALZN) | $1.16 | +3.6% | +5.2% | $1.22 | +8.9% | 69K | 595K | 0.1x | 3.2M | Pharmaceuticals: Major |
| GNLN | [TV](https://www.tradingview.com/chart/?symbol=GNLN) | $2.27 | -3.4% | +21.3% | $2.75 | +17.2% | 9K | 12K | 0.7x | 608K | Wholesale Distributors |

**Two-AH-scan gate (>10% AH in ≥2 AH scans, 22:00+ CET):** SEER (23:30 +31.5% → 00:00 +34.6% — **qualifies**), UPC (4 scans, faded), ZCMD (23:30 +450.5% → 00:00 +404.5% — now 2nd AH scan), CLRO (extended +101% Day), CRE (fading below threshold). RDGT, HLP, UFG, RAYA, NCT, GNLN all first AH scan and/or below the 10% AH threshold.

**SIP verification (bars fresh to 17:45 ET / 21:45Z; quotes returned stale IEX 16:00 ET on free tier):**
- **SEER** — **ENTERED.** Real accumulation: 1.09M → 1.12M → 779K → 364K → 415K → 202K → 711K (2nd push 17:30 ET) → 334K → 242K → 226K sh/bar, 890–7.2K trades/bar. AH peak $2.33 at **17:05 ET**, second push to $2.29 at 17:30, now holding $2.21 (−5% off high) = **HOLD pattern** (within 20% of high, like CHAI/MSW; early peak not disqualifying when holding). SIP $2.16–$2.21 corroborates scanner AH $2.18 (no bad print). Quote stale (16:00 ET, ask=$1.62=regular close) — freshness guard: stale-not-contradicting, real live liquidity confirmed by fresh SIP bars. Gates: 2-AH-scan ✓, Day% -0.6% ✓, Total% +33.8% <150% ✓, VRatio 5.7x ✓. **Catalyst (Grade A):** unsolicited **CEO buyout proposal at $2.45/share** + active activist proxy contest ($2.40 cash+CVR). AH $2.21 sits below the $2.45 offer (deal-risk discount) — room to entry.
- **ZCMD** — Now 2nd AH scan (23:30 +450.5% → 00:00 +404.5%), genuine +400% on 10M+ real AH shares. **Still skip:** Total% +400% massively exceeds the +150% ceiling; VRatio 2.3x fails the >5x ceiling-override gate. Real mover, logged for retrospective; too extended to enter.
- **UPC / CLRO / CRE** — UPC fading (peaked $9.69 16:20 ET, now $7.33, −24% off high), extended multi-day run, no fresh catalyst — SPIKE→FADE skip. CLRO +101% Day extended regular continuation, fading. CRE +9.6% AH now below threshold, −35% off its $4.37 high — SPIKE→FADE skip.
- **RDGT, HLP, UFG, RAYA, NCT, ALZN, GNLN** — all first AH scan, below 10% AH threshold (except GNLN +21.3% but only 9K AH vol / VRatio 0.7x — no real accumulation, skip-tier). ALZN is yesterday's closed position bouncing +5.2% AH on thin volume — skip.

**Decision: ENTERED SEER** — 43 shares @ **$2.26** real fill (order 1a03c698), $97.18. First entry of the night. SEER is the only candidate clearing all gates: 2-AH-scan qualifier, HOLD pattern near AH high, VRatio 5.7x on real SIP accumulation, Grade A acquisition catalyst (CEO $2.45 buyout proposal) with AH price below the offer. ZCMD is a real +400% mover but ceiling-blocked (VRatio fails override). All other qualifiers SPIKE→FADE or extended. No dead-cat-override (no Day% ≤ -15% candidate). Grade A hold: up to 5 days, trail stop -20% from peak — position management runs in premarket.

## Scan 00:30 CET (6:30 PM ET)

**AH session scan** (6:30 PM ET). Scanner returned 13 hits. New vs prior scans: RENX, MGNX, FXHO, HDSN. Prior names ZCMD, SEER, LHSW, UFG, CLRO, UPC, HLP, CRE, ILAG still present. SEER is the open position entered at 00:00.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| ZCMD | [TV](https://www.tradingview.com/chart/?symbol=ZCMD) | $1.11 | -0.9% | +378.4% | $5.31 | +374.1% | 13.6M | 5.2M | 2.6x | 1.1M | Misc Commercial |
| SEER | [TV](https://www.tradingview.com/chart/?symbol=SEER) | $1.62 | -0.6% | +36.4% | $2.21 | +35.6% | 5.4M | 897K | 6.0x | 36.2M | Biotechnology |
| LHSW | [TV](https://www.tradingview.com/chart/?symbol=LHSW) | $1.80 | +1.7% | +8.4% | $1.95 | +10.2% | 4.7M | 1.2M | 3.8x | 147K | Computer Proc Hardware |
| UFG | [TV](https://www.tradingview.com/chart/?symbol=UFG) | $0.69 | -6.4% | +21.6% | $0.84 | +13.8% | 4.4M | 612K | 7.3x | 9.8M | Wholesale Distributors |
| CLRO | [TV](https://www.tradingview.com/chart/?symbol=CLRO) | $6.48 | +101.2% | +19.2% | $7.73 | +139.9% | 4.3M | 8.8M | 0.5x | 740K | Electronics/Appliances |
| UPC | [TV](https://www.tradingview.com/chart/?symbol=UPC) | $6.32 | +13.7% | +11.6% | $7.05 | +26.8% | 2.9M | 8.1M | 0.4x | 326K | Pharmaceuticals: Major |
| HLP | [TV](https://www.tradingview.com/chart/?symbol=HLP) | $0.75 | +34.4% | +6.4% | $0.80 | +42.9% | 1.1M | 5.7M | 0.2x | 44.4M | Metal Fabrication |
| CRE | [TV](https://www.tradingview.com/chart/?symbol=CRE) | $2.49 | +1.6% | +5.2% | $2.62 | +6.9% | 590K | 143K | 4.1x | 1.1M | Commercial Printing |
| RENX | [TV](https://www.tradingview.com/chart/?symbol=RENX) | $2.00 | +2.6% | +7.5% | $2.15 | +10.3% | 151K | 126K | 1.2x | 2.3M | Real Estate Dev |
| ILAG | [TV](https://www.tradingview.com/chart/?symbol=ILAG) | $3.49 | -3.6% | +16.0% | $4.05 | +11.9% | 116K | 36K | 3.2x | 987K | Tools & Hardware |
| MGNX | [TV](https://www.tradingview.com/chart/?symbol=MGNX) | $4.71 | +1.9% | +5.2% | $4.95 | +7.2% | 109K | 2.0M | 0.1x | 61.3M | Pharmaceuticals: Major |
| FXHO | [TV](https://www.tradingview.com/chart/?symbol=FXHO) | $7.20 | -25.0% | +168.1% | $19.30 | +101.0% | 79K | 95K | 0.8x | 97K | Telecom Equipment |
| HDSN | [TV](https://www.tradingview.com/chart/?symbol=HDSN) | $5.99 | +5.6% | +5.3% | $6.31 | +11.3% | 74K | 550K | 0.1x | 36.2M | Wholesale Distributors |

**Two-AH-scan gate (>10% AH in ≥2 AH scans, 22:00+ CET):** SEER (qualified at 00:00, entered), UPC (5 scans, faded), ZCMD (23:30/00:00/00:30, ceiling-blocked). All four new names (RENX, MGNX, FXHO, HDSN) are on their **first AH scan** — fail the 2-AH gate regardless of trajectory.

**SIP verification (new names; bars fresh to ~18:15 ET / 22:15Z; quotes returned stale IEX 16:00 ET on free tier):**
- **FXHO** — **Real +168% AH spike, NOT a bad print.** SIP shows genuine accumulation igniting late: flat ~$7.20–7.44 through 22:00Z, then 22:05Z 26.8K sh / 921 trades, 22:10Z **173.6K sh / 7,789 trades** peaking $19.30, 22:15Z 86.5K sh / 4,645 trades ($16.00 close). SIP high $19.30 corroborates the scanner AH price exactly. The scanner's AH Vol 79K / VRatio 0.8x is **stale TradingView lag** — real move is ~287K sh in the last 15 min. **Skip (live entry):** Day% **-25.0%** ≤ -15% → dead-cat gate; and this is the **first AH scan** (fails 2-AH gate). The spike DOES reclaim far above the $7.20 regular close (dead-cat-override territory), but the override watch requires AH% rising across **≥2 AH scans** — only 1 scan so far. Nano float 97K, MCap $1.4M. **Strong watch for the 01:00 scan:** if it holds/builds and posts a 2nd AH scan above close, it becomes a **DEAD-CAT-OVERRIDE WATCH** (record hypothetical entry then). No live entry now.
- **RENX** — AH +7.5%, Total +10.3%, AH Vol 151K, VRatio 1.2x — below the 10% AH threshold, no real accumulation. Skip-tier.
- **MGNX** — AH +5.2%, VRatio 0.1x (109K vs 2.0M avg). Below threshold, no unusual AH volume. Skip.
- **HDSN** — AH +5.3%, VRatio 0.1x. Below threshold. Skip.

**Prior-name status:** ZCMD still a genuine +374% mover (13.6M real AH sh) but ceiling-blocked (Total% +374% ≫ 150%, VRatio 2.6x fails >5x override) — logged for retrospective. UPC/CLRO/CRE/UPC continue fading / extended regular continuations — SPIKE→FADE skips. LHSW faded to +8.4% (below threshold). ILAG/HLP sub-threshold.

**Decision: No new paper trades.** No new candidate clears the gates: RENX/MGNX/HDSN are sub-threshold with low VRatio; FXHO is a real +168% AH spike but blocked by the -25% Day% dead-cat gate and its first-AH-scan status (flagged as strong dead-cat-override watch for 01:00). SEER remains the night's only entry (position management runs in premarket, not here). No ceiling-override (ZCMD VRatio fails) applies.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
| SEER | $2.26 | 2026-07-03 00:03 CET (18:03 ET) | 43 | 1a03c698 | Grade A: CEO $2.45/sh buyout proposal + activist proxy contest. 2-AH-scan qualifier, HOLD near AH high, VRatio 5.7x real SIP vol. |
