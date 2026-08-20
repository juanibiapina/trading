# Post-Market Screening - 2026-08-20

## Scan 21:30 CET (3:30 PM ET) — REGULAR session, watch only

AH not open yet (opens 22:00 CET / 16:00 ET). No entries this scan per regular-session caution rule. Candidates flagged Watch — pending AH confirmation. Names with near-zero 5mVol / VChg −100% (faded, dead) excluded from watch.

| Ticker | Chart | Price | Day% | 5mVol | AvgVol | IRVol | VChg% | Float | MCap | Industry | Note |
|--------|-------|-------|------|-------|--------|-------|-------|-------|------|----------|------|
| USDE | [TV](https://www.tradingview.com/chart/?symbol=USDE) | $3.95 | +27.8% | 32K | 14K | 5.6 | +246% | 21.7M | 107.4M | Packaged Software | Watch — live vol, prior AH winner history |
| BTMD | [TV](https://www.tradingview.com/chart/?symbol=BTMD) | $1.53 | +12.5% | 30K | 6K | 12.9 | +296% | 25.9M | 55.0M | Hospital/Nursing Mgmt | Watch — rising vol |
| SUGRF | [TV](https://www.tradingview.com/chart/?symbol=SUGRF) | $9.47 | +14.4% | 15K | 3K | 11.8 | +271% | 4.6M | 219.0M | Wholesale Distributors | Watch — low float |
| ARBB | [TV](https://www.tradingview.com/chart/?symbol=ARBB) | $4.83 | +20.4% | 2K | 6K | 39.0 | +207% | 1.2M | 8.5M | IT Services | Watch — low float, thin vol |
| NXTT | [TV](https://www.tradingview.com/chart/?symbol=NXTT) | $7.90 | +19.0% | 5K | 16K | 46.4 | −27% | 1.5M | 11.6M | Packaged Software | Watch — low float, prior winner |

Excluded (faded/thin, VChg −100% or sub-1K 5mVol at scan): BRLS, BTCT, INDP, MMA, BIVI, XOS, GNLN, IDAI, FRTT, RETO, JWEL, ACTU, CBAT, AIFC. CATO −19.7% (down day, not a spike). EWAV/ALPX/SHOT Financial Conglomerate noise.

## Scan 22:00 CET (4:00 PM ET) — AH open, observation only

Scanner 0 hits at 16:00:17 ET (right at AH open, postmarket feed empty). Observation-only scan per learning-phase rule (no entries before 23:00 CET).

Feed-lag cross-check on prior 21:30 watch names via SIP + quote:
- USDE: no SIP AH bars yet; quote bid $3.37 / ask $4.61 (wide, no surge). Live book, no ignition.
- NXTT: no SIP AH bars yet; quote bid $6.87 / ask $9.41 (wide). No surge.
- BTMD: no SIP AH bars yet; quote bid $1.24 / ask $1.78 (wide). No surge.

No candidate above 10% AH threshold on real accumulating volume this scan. Nothing to enter. Watch names carried to next scan.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| BTOG | $1.25 | $0.76 | -39.2% | $1.25 | 1 | D | SELL | Grade D exit first PM + far below -10% stop; PM dumped $0.95→$0.76 |
| LOOP | $1.36 | $1.11 | -18.4% | $1.47 | 1 | None | SELL | Grade None exit first PM + below -10% stop; PM faded $1.34→$1.11 |

**Actions taken:**
- SELL 86 BTOG @ limit $0.70 ext (id 1646c658) filled @ $0.76 → -$42.14 (-39.2%)
- SELL 73 LOOP @ limit $1.07 ext (id 7f09ba1f) filled @ $1.11 → -$18.25 (-18.4%)
- Both positions closed. No open positions remaining.
- Quotes stale (prior-close IEX); used SIP PM bars for sell levels. Both got price improvement over limit.

## Position Evaluation — 14:30 CET

No open positions (Alpaca source of truth). BTOG + LOOP already closed in 10:30 pulse. OPEN_POSITIONS.md reconciled, in agreement. Nothing to evaluate.

**Actions taken:**
- None.
