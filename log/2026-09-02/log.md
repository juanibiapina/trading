
## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| KITT | $1.02 | $0.87 | -14.7% | $0.99 (-2.9%) | 0 | B | SELL | At -15% hard stop; PM opened $0.92 then faded, no follow-through |
| PXS | $6.26 | $5.98 | -4.5% | $6.68 (+6.7%) | 2 | B | SELL | Grade B day-2 time limit reached; above stop, thin PM book |

**Actions taken:**
- SELL 93 KITT @ limit $0.84 ext (id 58ea9bc1) filled @ $0.87 → -$13.95 (-14.7%)
- SELL 15 PXS @ limit $5.90 ext (id f225e53c) filled @ $5.98 → -$4.20 (-4.5%)
- Both stale Alpaca quotes (KITT bid $0.69, PXS ask $0.00 x0); priced off SIP levels
- No open positions remain

## Position Evaluation — 14:30 CET

No open positions (Alpaca source of truth). Clean slate after 10:30 CET pulse (KITT + PXS exited). OPEN_POSITIONS.md agrees. Nothing to evaluate.

**Actions taken:**
- None

## Scan 21:30 CET (3:30 PM ET)

Regular session — AH opens 22:00 CET (16:00 ET). No entries this scan (regular-session caution). Candidates flagged Watch — pending AH confirmation. Only re-enter evaluation if they reappear in AH scans (22:00+ CET) with sustained momentum.

| Ticker | Chart | Price | Day% | 5mVol | AvgVol | IRVol | Float | MCap | Industry | Note |
|--------|-------|-------|------|-------|--------|-------|-------|------|----------|------|
| TRTI | [TV](https://www.tradingview.com/chart/?symbol=TRTI) | $3.82 | +27.3% | 8K | 9K | 21.4 | 2.1M | 12.6M | Electric Utilities | Watch — low float |
| LHSW | [TV](https://www.tradingview.com/chart/?symbol=LHSW) | $3.76 | +30.6% | 8K | 5K | 5.5 | 1.0M | 12.9M | Computer Processing Hardware | Watch — low float |
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $1.03 | +30.1% | 33K | 50K | 0.5 | 4.4M | 8.1M | Misc Commercial Services | Watch — IRVol fading (0.5) |
| SWVL | [TV](https://www.tradingview.com/chart/?symbol=SWVL) | $5.22 | +36.3% | 313 | 22K | 0.3 | 5.3M | 52.0M | Other Transportation | Watch — vol faded |
| LHAI | [TV](https://www.tradingview.com/chart/?symbol=LHAI) | $1.09 | +32.8% | 100 | 156K | 434.2 | 9.7M | 18.0M | Packaged Software | Watch — vol faded intraday |
| GPRO | [TV](https://www.tradingview.com/chart/?symbol=GPRO) | $1.72 | +39.9% | 1K | 4.6M | 4.0 | 125.1M | 164.0M | Electronics/Appliances | Watch — float 125M (high) |

Other movers (higher price / weaker profile): TRTI leads low-float list. No paper trades — waiting for AH scans to confirm which names carry momentum past 16:00 ET. Most listed names already show fading intraday IRVol (5mVol below Avg5m), a caution sign for AH follow-through.

## Scan 22:00 CET (4:00 PM ET)

No candidates found. Scanner 0 hits at AH open (16:00 ET). SIP shows no AH bars yet for the 21:30 watch names (TRTI, LHSW, LHAI — `no bars`, feed sparse at the open minute). No entries (observation-only before 23:00 CET, and no qualifying candidate anyway). Re-check watch names at 22:30/23:00 for AH carry.

## Scan 22:15 CET (4:15 PM ET)

No candidates found. Scanner 0 hits at 16:15 ET (same as 22:00). Cross-checked 21:30 watch names via SIP first AH bar (16:00-16:05 ET):

| Ticker | AH C | vs Reg | AH Vol | Trades | Note |
|--------|------|--------|--------|--------|------|
| TRTI | — | — | 0 | 0 | no AH bars (no liquidity) |
| LHSW | $3.75 | flat | 12.8K | 6 | flat, 6 trades — thin |
| NCPL | $1.00 | −3% | 96.8K | 151 | fading off close |
| SWVL | $4.90 | −6% | 16.2K | 164 | fading |
| LHAI | $1.12 | flat | 150K | 234 | flat vs close |
| GPRO | $1.64 | −5% | 1.87M | 2147 | fading, float 125M |

None building in AH — all flat or fading off regular close, none igniting. No entries (observation-only before 23:00 CET, and no qualifying candidate). Re-check at 22:30/23:00 for late AH carry.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
| — | — | — | — | — | No entries — regular-session scan, AH not open |
