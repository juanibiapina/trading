# Trade Log — 2026-07-07

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| EDHL | $4.81 | $5.15 (SIP PM) | +7% | $6.29 (PM open) / $5.83 OVN | 1 | None | SELL | Grade None = exit first premarket at any profit. Sold 20 @ $5.10 (+6.0%) |
| SEER | $2.26 | $2.16 | -4.4% | $2.34 (+3.5%) | 4 | A | HOLD | Within 5-day limit (day 4/5), buyout catalyst intact ($2.45 offer), above -25% hard stop $1.695. Peak never hit +50% so no trail. |

**Actions taken:**
- SELL EDHL 20 @ $5.10 ext (id cdfa66da), filled. P&L +$5.80 (+6.0%). Entry $4.81 → exit $5.10.
- SEER held. Note: tomorrow (07-08) is day 5, the hold limit. Plan to exit next pulse if catalyst unchanged.

**Notes:**
- EDHL: SIP bars confirm PM opened ~$6.25, spiked to $6.29 (opening bar, 184K vol), then faded to ~$5.15 by 04:15 ET. Yahoo peak $6.30 matches SIP. Sold into liquid book (7K sh/min).
- Alpaca `quote` endpoint returned stale data (yesterday 20:00Z close); used SIP 1-min bars for real-time PM price instead.

## Position Evaluation — 14:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| SEER | $2.26 | $2.19 (SIP PM, bid $2.18) | -3.1% | $2.34 (+3.5%) | 4 | A | HOLD | Day 4/5, buyout catalyst intact ($2.45 offer floor), above -25% hard stop $1.695. Peak never hit +50%, no trail. |

**Actions taken:**
- None. SEER held.

**Notes:**
- SEER: SIP PM (07-07) stable $2.12-2.20 through 08:15 ET, currently ~$2.19 (bid $2.18/ask $2.20). Price sits below the $2.45 buyout offer, arb gap intact. No invalidating news.
- Tomorrow 07-08 is day 5 (hold limit). Plan to exit next pulse if still no continuation toward the $2.45 offer.
- Alpaca `quote` again returned stale timestamp (07-06 20:59Z); relied on SIP 5-min bars for live PM price.
