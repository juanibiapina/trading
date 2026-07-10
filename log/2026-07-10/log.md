# 2026-07-10

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| ELPW | $1.18 | $0.97 | -17.8% | $1.37 (+16%) | 1 | D | SELL | Grade D exit at first PM + below -10% hard stop |
| PMA | $1.66 | $1.48 | -10.8% | $1.96 (pre-entry) | 1 | C | SELL | Grade C exit in first PM pulse + below -10% hard stop |
| YYGH | $1.66 | $1.37 | -17.5% | $2.00 (pre-entry) | 1 | None | SELL | Grade None exit at first PM + below -10% hard stop |

All three entered 2026-07-09; overnight faded, none re-rated above entry. All Grade C/D/None → exit in first premarket pulse per risk rules; all also below -10% hard stops.

**Data notes:**
- Broker `quote` endpoint returned stale bid/ask (timestamped yesterday 20:00Z). Used live SIP 5Min bars (start 08:00Z) for real fillable levels.
- ELPW PM volume healthy (~5M sh across first 4 bars). PMA moderate (~1M sh). YYGH thin (~70K sh, ~8K/bar) — set limit lower ($1.33) to ensure fill in thin book; filled @ $1.37.

**Actions taken:**
- SELL 83 ELPW @ limit $0.92 ext (id 21ed3062) → filled @ **$0.97**. P&L -$17.43 (-17.8%).
- SELL 60 PMA @ limit $1.44 ext (id a40736bf) → filled @ **$1.48**. P&L -$10.80 (-10.8%).
- SELL 58 YYGH @ limit $1.33 ext (id 72970f69) → filled @ **$1.37**. P&L -$16.82 (-17.5%).

**Net realized: -$45.05.** All positions closed. No open positions.

## Position Evaluation — 14:30 CET

No open positions. Alpaca flat (equity $99,953.02, all cash). All three positions (ELPW, PMA, YYGH) closed in the 10:30 pulse. `OPEN_POSITIONS.md` reconciled. Nothing to do.
