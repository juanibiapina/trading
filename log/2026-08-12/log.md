# Post-Market Screening - 2026-08-12

## Scan 21:30 CET (3:30 PM ET)

**Regular session — before AH open (16:00 ET / 22:00 CET). No entries; candidates flagged Watch pending AH confirmation** (per regular-session caution: intraday spikes that don't carry into AH tend to fade).

Notable intraday movers with real volume (most scanner hits show huge negative VChg% = fading, tiny 5mVol = stale prints):

| Ticker | Chart | Price | Chg% | 5mVol | IRVol | Float | MCap | Industry | Note |
|--------|-------|-------|------|-------|-------|-------|------|----------|------|
| DOGZ | [TV](https://www.tradingview.com/chart/?symbol=DOGZ) | $1.30 | +40.3% | 13K | 1243.9 | 4.3M | 18.9M | Consumer Sundries | Watch — VChg -10% (fading) |
| BANL | [TV](https://www.tradingview.com/chart/?symbol=BANL) | $5.40 | +30.6% | 16K | 82.4 | 407K | 11.4M | Air Freight/Couriers | Watch — low float 407K, VChg +92.6% |
| GRWG | [TV](https://www.tradingview.com/chart/?symbol=GRWG) | $1.84 | +23.6% | 16K | 14.7 | 54.7M | 110.6M | Wholesale Dist | Watch — high float |
| DRMA | [TV](https://www.tradingview.com/chart/?symbol=DRMA) | $1.33 | +23.1% | 16K | 103.7 | 2.7M | 5.3M | Pharma | Already traded today, position closed -19.1% |
| BCG | [TV](https://www.tradingview.com/chart/?symbol=BCG) | $1.50 | +15.1% | 5K | 16.3 | 3.6M | 25.3M | Investment Managers | Watch |

Remaining hits (BOXL, RMCF, OFAL, BQ, CHOW, XHLD, etc.) show VChg% near -100% with sub-1K 5mVol = stale/regular-session artifacts, not live spikes. BAOS and BOXL were traded and closed this morning (see Position Evaluation).

**No paper trades this scan** — regular session, AH not yet open. Real AH screening begins at the 22:00 CET scan.

## Scan 22:00 CET (4:00 PM ET)

No candidates found. Scanner returned 0 AH hits at AH open (16:00 ET). None of the 21:30 regular-session watch names (DOGZ, BANL, GRWG, BCG) carried into the AH feed above threshold at this scan. Nothing to evaluate; no entries (learning-phase default holds entries until the 23:00 CET scan regardless).

## Scan 22:15 CET (4:15 PM ET)

No candidates found. Scanner returned 0 AH hits 15 min into the after-hours session. None of the 21:30 regular-session watch names (DOGZ, BANL, GRWG, BCG) surfaced in the AH feed above threshold. Nothing to evaluate; no entries (learning-phase default holds entries until the 23:00 CET scan regardless).

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| BAOS | $0.90 | $2.24 | +148.9% | $2.19 (PM) | 1 | None | SELL | Grade None — exit at any profit. PM ran $1.70→$2.19H on 2.6M sh/20k trades. Filled $2.24 (price improvement). |
| BOXL | $4.01 | $5.83 | +45.4% | $6.50 (PM) | 1 | None | SELL | Grade None — exit at any profit. PM ran $4.35→$6.50H on 1.2M sh/22k trades. Filled $5.83. |
| DRMA | $1.52 | $1.43 | -5.9% | $1.59 (PM) | 1 | B | HOLD | Above -15% stop ($1.29), day 1 of 2. Peak +4.6% never hit +30% trail. PM $1.40-1.59, VWAP $1.45. |
| FF | $6.28 | $6.20 | -1.3% | $6.45 | 2 | B | SELL | Grade B day-2 time limit reached. Flat, thin PM. Filled $6.20. |

**Actions taken:**
- SELL 102 BAOS @ limit $1.98 ext (id 40fe100d) filled @ $2.24 → +$136.68 (+148.9%)
- SELL 24 BOXL @ limit $5.75 ext (id 742fee8e) filled @ $5.83 → +$43.68 (+45.4%)
- SELL 16 FF @ limit $6.00 ext (id f2d3ab05) filled @ $6.20 → -$1.28 (-1.3%)
- HOLD DRMA (Grade B, day 1, within risk)
- **Pulse net realized: +$179.08.** BAOS Grade-None exit captured a rare +149% overnight runner.


## Position Evaluation — 14:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| DRMA | $1.52 | $1.23 | -19.1% | $1.59 (PM) | 1 | B | SELL | Below -15% Grade B hard stop ($1.29). PM faded monotonically $1.59→$1.35; live bid $1.21 x100. Filled $1.23 (price improvement). |

**Actions taken:**
- SELL 66 DRMA @ limit $1.18 ext (id fcf9ca9f) filled @ $1.23 → -$19.14 (-19.1%)
- No open positions remain.
