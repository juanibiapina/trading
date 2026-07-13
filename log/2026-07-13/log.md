# Post-Market Screening - 2026-07-13

## Scan 21:30 CET (3:30 PM ET) — REGULAR session, pre-AH

Scanner ran during regular session (AH opens 4:00 PM ET / 22:00 CET). **No entries — regular-session caution rule.** Candidates flagged for AH confirmation; only enter if they reappear in a 22:00+ CET AH scan with sustained momentum.

Notable movers (regular-session, IRVol = intraday relative volume):

| Ticker | Price | Chg% | IRVol | Float | MCap | Industry | Note |
|--------|-------|------|-------|-------|------|----------|------|
| MIMI | $3.04 | +41.4% | 179x | 1.5M | 8.4M | Misc Commercial | Low float, high IRVol — watch AH |
| SOBR | $1.31 | +202.1% | high | 2.3M | 1.2M | Electronic Equip | Big % move, low float — watch AH |
| ACTU | $1.46 | +20.7% | 17x | 10.3M | 34.9M | Pharma Major | Watch AH |
| AURE | $1.68 | +13.5% | 95x | 10.9M | 65.0M | IT Services | Watch AH |
| EHGO | $2.24 | +36.6% | 3.7x | 2.2M | 7.2M | Wholesale Dist | Low float — watch AH |
| GEDC | $0.78 | +94.9% | 3.8x | 7.3M | 10.3M | Eng & Construction | Watch AH |
| SKYQ | $4.09 | +28.7% | 1.2x | 3.8M | 19.6M | Integrated Oil | Fading IRVol — watch AH |

Many other small % movers with negligible real volume (VChg% -99% type = stale). Full scan had 62 hits, mostly illiquid.

**Decision:** No paper trades. Regular-session scan only. Reassess at 22:00+ CET AH scans for entries.

## Scan 22:00 CET (4:00 PM ET) — AH open

Scanner (`scan.py --all`): **0 AH hits.** Observation-only scan (learning phase: no entries before 23:00 CET).

Early-AH quotes on the 21:30 watchlist (scan hit ~30s after AH open, books still forming):

| Ticker | Bid | Ask | Note |
|--------|-----|-----|------|
| MIMI | $2.51 x100 | $3.36 x100 | Wide spread, thin |
| SOBR | $0.61 x500 | $1.70 x1100 | Very wide spread, unstable |
| SKYQ | $3.43 x100 | $0.00 x0 | No AH ask (no fillable book) |
| EHGO | $1.82 x100 | $2.46 x100 | Wide spread, thin |

**Decision:** No paper trades. No scanner AH hits; watchlist books thin/unstable seconds into AH. Reassess at 22:30 / 23:00 CET.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
