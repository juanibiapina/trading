# 2026-07-28

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak (SIP PM) | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|---------------|------|-------|----------|--------|
| INLF | $4.12 | $4.89 | +18.7% | $5.36 (+30.1%) | 1 | None | **SELL** | Grade None → exit at first PM opportunity at any profit. Filled @ $4.89. |
| BZFD | $1.30 | $1.29 | -0.8% | $1.52 (+16.9%) | 0 | C | **SELL** | Grade C → exit in first PM pulse. Filled @ $1.29. |
| DOMO | $3.92 | $3.55 | -9.4% | $4.50 (+14.8%) | 5 | A (mis-graded) | **SELL** | Day 5/5 time limit + exit-flagged 07-24 (merger-arb, price pinned). Order resting, PM untraded. |

### Detail

**INLF** — Best case of the AH-build → PM-continuation pattern working. PM opened at 08:00Z with a real 618K-share bar (10,986 trades), ran $4.20 → $5.36 by 08:10Z, then settled $4.85-4.96 (vwap $4.97). Sold into the settle at $4.89, +18.7%. PM peak was +30% from entry; the Grade-None "exit at first PM opportunity" rule left ~11 points on the table but captured the majority of the move on real liquidity.

**BZFD** — PM opened $1.39, spiked $1.52 in the first bar (288K sh), then bled back to $1.27-1.33 on collapsing volume (29K → 17K → 20K sh/bar). Classic spike-and-fade. Grade C rule fired correctly; the $1.52 print was a first-bar-only level that would not have been fillable at size. Exited flat at $1.29.

**DOMO** — Day 5 of the Grade A window and the exit flag from 07-24 (merger-arb name, Progress Software all-cash $400M pins the price and kills AH→PM momentum). Premarket is effectively dead: one 5Min bar, 550 shares, 5 trades at $3.55. Sell 25 @ limit $3.48 ext submitted (id fadb7c40), resting. Will fill when liquidity arrives. Confirmed -9.4% at last SIP print.

**Actions taken:**
- SELL 22 INLF @ limit $4.88 ext (id e444adb3) → **filled @ $4.89**, +$16.94 (+18.7%)
- SELL 76 BZFD @ limit $1.26 ext (id d19bb119) → **filled @ $1.29**, -$0.76 (-0.8%)
- SELL 25 DOMO @ limit $3.48 ext (id fadb7c40) → **resting**, no PM liquidity yet
- OPEN_POSITIONS.md reconciled with Alpaca (BZFD row had shares/entry-time columns swapped)

**Net realized this pulse:** +$16.18

**Note on stale quotes:** `broker.js quote` returned yesterday's 20:00Z close for all three names (paper IEX feed does not carry premarket). All pricing and limit placement came from SIP 5Min/1Min bars. Yahoo `check-prices.py` returned no PM data either. SIP bars remain the only usable premarket source.

**For the daily email:** DOMO is the last open position and its sell is resting unfilled in a dead premarket book. If it does not fill by the 14:30 pulse, it fills at the open. No decision needed from Juan; noting because it closes out the mis-graded merger-arb trade Juan flagged on 07-24.

## Position Evaluation — 14:30 CET

| Ticker | Entry | Current | P&L % | Peak (SIP PM) | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|---------------|------|-------|----------|--------|
| DOMO | $3.92 | $3.55 | -9.4% | $4.50 (+14.8%) | 5 | A (mis-graded) | **SOLD** | Resting order from 10:30 pulse filled @ $3.55 at 11:00Z. |

**Portfolio is flat.** No open positions.

### Detail

**DOMO** — The 10:30 sell (25 @ limit $3.48 ext, id fadb7c40) rested ~2.5 hours in a near-dead premarket book and filled at **$3.55** at 11:00:00Z, 7 cents above the limit. Final: -$9.25, -9.4%, 5 days held. Premarket volume for the whole session was trivial (550 / 179 / 150 / 906 / 350 / 1000 shares per 5Min bar) in a $3.53-3.59 band — confirming the merger-arb pin.

### Closing the DOMO thesis

Juan flagged this trade on 07-24 and he was right. Domo is being bought for cash ($400M, Progress Software). An all-cash acquisition sets a fixed price, so the stock converges to the deal value and stops moving. That is the opposite of what this strategy needs: the AH→PM pattern depends on price discovery and FOMO, and a deal price removes both. The five-day chart is a flat band between $3.5 and $4.5 with a single 1.98M-share spike on 07-23 that immediately mean-reverted.

**Rule change to propose:** an all-cash acquisition/buyout of the traded company is **not** a Grade A catalyst. Grade A means an operational catalyst that expands the range of future outcomes (partnership, contract, FDA event). A cash buyout collapses that range to one number. Treat cash-buyout targets as Grade D (exit at first PM opportunity) or skip at screening.

**Actions taken:**
- DOMO sell confirmed filled @ $3.55 (order fadb7c40)
- OPEN_POSITIONS.md: DOMO moved to Closed Positions, Current Positions now empty
- Account: equity $99,902.63, cash $99,902.63, no positions

**Realized today (all three exits):** INLF +$16.94, BZFD -$0.76, DOMO -$9.25 → **+$6.93 net**

**For the daily email:**
- Flat going into tonight. All three positions closed; day net +$6.93.
- INLF was the strategy working as designed: AH build → PM continuation → +18.7% on real liquidity.
- The DOMO trade is closed at -9.4%. Recommend adopting the rule above (cash-buyout targets are not Grade A). Juan's 07-24 call was correct and the extra four days of holding cost about 4 points versus selling then.
