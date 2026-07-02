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

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
