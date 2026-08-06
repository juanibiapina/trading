# Post-Market Screening - 2026-08-06

## Scan 21:30 CET (3:30 PM ET)

Regular-session scan (15:30 ET, before AH opens at 22:00 CET). Per regular-session caution rule: no entries. Candidates flagged as watch — pending AH confirmation. Only enter if they reappear in an AH scan (22:00+ CET) with sustained momentum.

| Ticker | Chart | Price | Day% | 5mVol | AvgVol | IRVol | VChg% | Float | MCap | Industry |
|--------|-------|-------|------|-------|--------|-------|-------|-------|------|----------|
| XHLD | [TV](https://www.tradingview.com/chart/?symbol=XHLD) | $2.07 | +159.6% | 6.5M | 3.4M | 108.6 | +131.6% | 7.8M | $9.5M | Misc Commercial Services |
| BYAH | [TV](https://www.tradingview.com/chart/?symbol=BYAH) | $3.05 | +15.5% | 32K | 26K | 199.1 | -5.2% | 4.2M | $16.8M | Household/Personal Care |
| ALEC | [TV](https://www.tradingview.com/chart/?symbol=ALEC) | $1.88 | +26.2% | 71K | 161K | 16.4 | -74.8% | 77.7M | $208.7M | Biotechnology |
| WLDS | [TV](https://www.tradingview.com/chart/?symbol=WLDS) | $3.69 | +27.9% | 163K | 74K | 1.5 | +861.5% | 1.7M | $8.1M | Electronic Equipment |

**Notes:**
- **XHLD** — biggest mover (+159.6%), real regular-session volume (6.5M on 3.4M avg, VChg +131.6%). Low float 7.8M. Best watch candidate. Already extended (>150% would be a ceiling concern if it carries to AH). Watch for AH continuation.
- **BYAH** — +15.5%, low float 4.2M, sustained relative volume (IRVol 199x). Note: BYAH is the Jun 11 dead-cat-override example ticker; different setup today. Watch for AH.
- **WLDS** — +27.9%, low float 1.7M, huge VChg +861.5% but only 1.5 IRVol (volume fading). Weaker.
- **ALEC** — +26.2% but float 77.7M and volume below average (IRVol declining). Weak.
- Thin/stale movers skipped from watch (CLRO +161.9%, CELZ +104.1%, AZI +52%, PN, PEPG, III — all show VChg near -99% = single-print/stale, no real sustained volume).
- No spike-bar/confirmation instrumentation run — those apply to AH candidates with AH change >10%; AH session not yet open.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|

_No entries — regular-session scan, AH not yet open._

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| CELZ | $0.89 | $0.83 | -6.7% | $0.95 (PM) | 1 | None | SELL | Grade None → exit first PM opportunity. Filled @ $0.83. |
| PAVS | $6.61 | $6.65 | +0.6% | $7.98 (PM) | 1 | None | SELL | Grade None → exit first PM at any profit. Filled @ $6.65. |

**Actions taken:**
- SELL 98 CELZ @ limit $0.80 ext (id 9af1c889) filled @ $0.83 → -$5.88 (-6.7%)
- SELL 14 PAVS @ limit $6.80 ext (id b821a331) did not fill (book faded); canceled, repriced @ $6.50 (id 5c8473a1) filled @ $6.65 → +$0.56 (+0.6%)
- Both positions closed. No open positions remaining.

**Notes:**
- Alpaca quote feed stale for both names (stuck at 2026-08-05 close). Priced sells off live SIP 5Min bars, both liquid (CELZ 6754 trades/first bar, PAVS 11,528 trades/bar).
- CELZ: PM opened $0.87, spiked $0.95, faded to $0.79-0.84 (vwap $0.80-0.87). Textbook spike-and-fade.
- PAVS: PM opened $6.94, spiked $7.98 first bar then chopped $6.66-7.40. Exited near flat.
- Net pulse P&L: -$5.32.

## Position Evaluation — 14:30 CET

No open positions. Alpaca `positions` empty; equity $99,887.56, cash $99,887.56. `OPEN_POSITIONS.md` already shows all closed (CELZ, PAVS exited at 10:30 CET pulse). No reconciliation needed, nothing to evaluate.

**Actions taken:**
- None. Flat book.
