
# Post-Market Screening - 2026-08-25

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| WLDS | $3.30 | $2.66 | -19.4% | $3.58 | 1 | None | SELL | Grade None exit first PM + far below -10% hard stop; PM no follow-through |

**Actions taken:**
- SELL 28 WLDS @ limit $2.58 ext (id 2eeb31ea) filled @ $2.66. Real fill $2.66, P&L -$17.92 (-19.4%).
- No open positions remain.

## Position Evaluation — 14:30 CET

No open positions (Alpaca source of truth). WLDS closed at 10:30 pulse. OPEN_POSITIONS.md reconciled (shows none). Nothing to evaluate or sell.

## Scan 21:30 CET (3:30 PM ET)

**REGULAR session** — AH not open yet (opens 22:00 CET / 4:00 PM ET). No entries per regular-session caution rule. Low-float / big-move names flagged as watch pending AH confirmation.

| Ticker | Chart | Price | Chg% | Float | MCap | IRVol | VChg% | Industry | Watch |
|--------|-------|-------|------|-------|------|-------|-------|----------|-------|
| DAIC | [TV](https://www.tradingview.com/chart/?symbol=DAIC) | $3.48 | +101.2% | 1.3M | 3.4M | 10.4 | +185.9 | Miscellaneous | Watch |
| PMI | [TV](https://www.tradingview.com/chart/?symbol=PMI) | $9.91 | +93.1% | 1.3M | 12.0M | 25.9 | +33.6 | Medical Specialties | Watch |
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $0.58 | +127.1% | 4.4M | 2.0M | 833.1 | -20.4 | Misc Commercial Services | Watch (fading vol) |
| JEM | [TV](https://www.tradingview.com/chart/?symbol=JEM) | $6.66 | +74.3% | n/a | 4.3M | 566.6 | -39.2 | Wholesale Distributors | Watch (fading vol) |
| TNMG | [TV](https://www.tradingview.com/chart/?symbol=TNMG) | $0.61 | +54.2% | 2.3M | 1.8M | 505.0 | +90.9 | Internet Software/Services | Watch |
| AMIX | [TV](https://www.tradingview.com/chart/?symbol=AMIX) | $8.26 | +53.8% | 946K | 8.0M | 157.0 | -68.4 | Medical Specialties | Watch (fading vol) |
| SWVL | [TV](https://www.tradingview.com/chart/?symbol=SWVL) | $2.19 | +49.0% | 5.3M | 21.8M | 6337.1 | -46.5 | Other Transportation | Watch (fading vol) |

**Notes:**
- Regular-session scan only. Instrumentation (spike-bar, third-bar confirmation) not run — AH ignition tools apply after 4:00 PM ET open.
- Watchlist above = low-float (<10M) names with >45% intraday move. Re-evaluate at 22:00+ CET AH scans; enter only if a name reappears with sustained AH momentum (2+ AH scans) and clears all entry gates at 23:00+ CET.
- Several names (NCPL, JEM, AMIX, SWVL) already showing fading intraday volume (VChg% negative or IRVol declining) — spike-then-fade risk into AH.

## Scan 22:00 CET (4:00 PM ET)

**AH just opened** (16:00 ET). Scanner `--all`: 0 hits. Observation-only scan (learning-phase entry gate is 23:00+ CET). No entries.

Carry-forward check on 21:30 low-float watch names (AH quotes at 16:00 ET, seconds into session — thin/forming books):

| Ticker | Reg Close | AH Bid | AH Ask | Note |
|--------|-----------|--------|--------|------|
| DAIC | $3.48 | $3.31 | $0.00 x0 | No AH ask/offer — no fillable book yet |
| PMI | $9.91 | $8.25 | $10.90 | Wide spread, below reg close |
| NCPL | $0.58 | $0.49 | $0.65 | Below close, thin |
| TNMG | $0.61 | $0.48 | $0.65 | Below close, thin |
| AMIX | $8.26 | $6.21 | $8.25 | Below close, wide |

**Notes:**
- Scanner returned no AH movers >threshold at open. Watch names sitting flat/below regular close, no AH momentum yet.
- Instrumentation (spike-bar, third-bar confirmation) not run — no candidate cleared threshold and it's observation-only.
- Re-evaluate at 22:30 / 23:00 CET. Entries only at 23:00+ with a candidate clearing all gates (float <50M, AH >10% in ≥2 AH scans, Day% > -15%).

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|

No entries — regular-session scan, AH not open.
