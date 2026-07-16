# 2026-07-16

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|

## Scan 22:00 CET (4:00 PM ET) — AFTERHOURS open

Scanner returned 0 hits. AH just opened; observation-only scan (learning phase blocks entries before 23:00 CET).

No candidates found.

**Decision:** No entries. First AH scan of the night, no movers detected. Re-scan at 22:30/23:00 CET.

## Scan 21:30 CET (3:30 PM ET) — REGULAR session

AH not open yet (opens 16:00 ET / 22:00 CET). Regular-session caution: no entries, watch only pending AH confirmation. Scanner returned 55 regular-session hits; notable low-float movers below.

| Ticker | Chart | Price | Chg% | Float | MCap | IRVol | VChg% | Industry | Note |
|--------|-------|-------|------|-------|------|-------|-------|----------|------|
| ATPC | [TV](https://www.tradingview.com/chart/?symbol=ATPC) | $4.12 | +63.5% | 475K | 4.1M | 1588x | -99.3% | Pharma: Other | Vol fading (5mVol 500) |
| STAK | [TV](https://www.tradingview.com/chart/?symbol=STAK) | $3.80 | +78.4% | 0 | 38.0M | 242x | -99.9% | Oilfield Svc | Vol fading |
| DXST | [TV](https://www.tradingview.com/chart/?symbol=DXST) | $2.72 | +30.8% | 1.2M | 4.9M | 54x | -99.3% | Env Svc | Prior winner name; vol fading |
| TGHL | [TV](https://www.tradingview.com/chart/?symbol=TGHL) | $1.49 | +82.9% | 12.7M | 37.7M | 28x | -99.9% | IT Svc | Already traded+sold today (-18.6%) |
| CLIK | [TV](https://www.tradingview.com/chart/?symbol=CLIK) | $1.77 | +19.7% | 724K | 5.8M | 122x | -86.1% | Personnel Svc | Vol fading |
| CRNG | [TV](https://www.tradingview.com/chart/?symbol=CRNG) | $2.00 | +263.6% | 0 | 35.3M | 1.5x | +485% | REIT | Low rel-vol |

**Decision:** No entries. This is a pre-AH regular-session scan; per the regular-session caution rule, candidates are watch-only pending AH confirmation (22:00+ CET). Most notable movers show VChg -99% (regular-session volume already fading, not building into AH). Learning-phase policy also blocks entries before the 23:00 CET scan. Re-scan at 22:00 CET when AH opens.

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| TGHL | $1.33962 | $1.09 | -18.6% | $1.33 (PM) | 1 | None | SELL | Grade None: exit first PM opportunity + below -10% hard stop |

**Actions taken:**
- SELL 79 TGHL @ limit $1.04 ext (id e56b50df) → filled @ $1.09. Final P&L -$19.72 (-18.6%).
- No open positions remain.

**Notes:**
- TGHL faded from PM open $1.15; 5Min SIP bars $1.33H→$1.08C on 5.6M sh, vwap $1.07-1.20 (liquid book). Sold into the fade per Grade None rule.
- Broker quote endpoint returned a stale close-print bid ($1.18 @ prior 20:59Z); used live SIP bars for pricing instead.

## Position Evaluation — 14:30 CET

No open positions. Alpaca `positions` returns empty; `OPEN_POSITIONS.md` already reconciled (shows none). TGHL was the last position, sold in the 10:30 pulse @ $1.09. Nothing to evaluate.

**Actions taken:**
- None.
