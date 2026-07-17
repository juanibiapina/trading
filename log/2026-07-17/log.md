# Trade Log — 2026-07-17

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| BIYA | $4.55 | $3.94 | -13.6% | $5.03 (+51%) | 1 | None | SELL | Grade None exit at first PM opportunity + below -10% hard stop. Filled $3.92. |
| CJMB | $1.01 | $1.39 | +37.6% | $1.58 (+56%) | 1 | B | HOLD | Grade B, day 1 of 2, catalyst intact. Trail stop $1.34 (peak-15%). |

**Actions taken:**
- SELL 22 BIYA @ limit $3.85 ext (id 9445ec9a) → filled @ $3.92. Final P&L -$13.86 (-13.8%). Moved to Closed Positions.
- CJMB HOLD. Trail stop set at $1.34 (peak $1.58 -15%). Current $1.39 above stop. Re-evaluate at 14:30 CET pulse.

**Notes:**
- PM window ~04:30 ET at pulse time. Both names liquid on SIP (BIYA 198K sh/bar, CJMB 2.6M sh first bar).
- BIYA quote endpoint returned stale (yesterday close); used SIP 5Min bars + Alpaca current_price for exit level.

## Position Evaluation — 14:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| CJMB | $1.01 | $1.21 | +19.8% | $1.58 (+56%) | 1 | B | SELL | Trail stop $1.34 hit. Faded steadily from PM peak toward open. Filled $1.21. |

**Actions taken:**
- SELL 95 CJMB @ limit $1.18 ext (id 30aff93a) → filled @ $1.21. Final P&L +$19.00 (+19.8%). Moved to Closed Positions.

**Notes:**
- CJMB peaked $1.58 (+56%) at PM open (08:00Z), then faded monotonically: $1.58→$1.40→$1.30→$1.22 by 12:15Z. Liquid throughout (bid $1.21 x500). Trail stop from 10:30 pulse ($1.34) breached; Grade B trail rule executed. Classic PM-peak-then-fade pattern; captured most of the run above entry.
- No open positions after this pulse.
