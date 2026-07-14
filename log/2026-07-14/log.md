# Trade Log — 2026-07-14

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| VMAR | $1.57 | $2.22 (fill) | +41.4% | $3.35 (+114%) | 1 | None | SELL | Grade None = exit at any profit. PM peaked $3.35 then dumping. |
| LVLU | $11.03 | $10.01 | -9.2% | $11.99 (+8.7%) | 1 | B | HOLD | Day 1 of 2; above -15% stop ($9.38); peak <+30% so no trail; catalyst intact. |

**Actions taken:**
- SELL 62 VMAR @ limit $2.15 ext (id edb17587) → filled **$2.22**. P&L +$40.30 (+41.4%).
- VMAR verified real via SIP: 4.5M sh in first PM bar, 37,981 trades on a 670K-float name. Peaked $3.35 at PM open, faded fast ($3.35→$2.94→$2.62→$2.23). Classic PM peak-then-dump — exited into the fade.
- LVLU held: Grade B, day 1 of 2, -9.2% is above the -15% hard stop. PM liquidity thin (7.3K sh in first PM bar). Re-evaluate at 14:30 CET pulse.

## Position Evaluation — 14:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| LVLU | $11.03 | $9.44 | -14.4% | $11.99 (+8.7%) | 1 of 2 | B | HOLD | Above -15% hard stop ($9.38); day 1 of 2; catalyst intact |

**Actions taken:**
- No sells. LVLU held per Grade B rule (hold up to 2 days).
- Data reconcile: Alpaca quote feed stale (07-13 20:00Z close, wide $6.55/$10.36 book). Used Alpaca `current_price` $9.44 (-14.4%) as P&L basis; SIP PM bars show latest ~$9.75-9.80 (-11.6%). SIP feed latest 11:55Z (07:55 ET) confirms premarket.
- LVLU never gave a PM spike above entry to exit into profit (OVN peak only +8.7%). Faded from $11.50 PM open to ~$9.75. Now sitting just above the hard stop.
- **Flag for next pulse:** if LVLU prints below $9.38, sell per Grade B hard-stop rule.
