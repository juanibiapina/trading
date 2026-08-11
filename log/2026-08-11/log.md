
## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| WAFU | $1.94 | $2.10 | +8.2% | $2.60 | 1 | None | SELL | Grade None exit first PM at profit; filled $2.10 |
| MTEN | $1.39 | $1.35 | -2.9% | $1.55 | 1 | None | SELL | Grade None exit first PM; filled $1.35 |
| MGIH | $2.12 | $2.02 | -4.7% | $2.22 | 1 | None | SELL | Grade None exit first PM; filled $2.02 |
| FF | $6.28 | $6.07 | -3.3% | $6.45 | 1 | B | HOLD | Day 1, above -15% stop ($5.34), Q2 earnings catalyst intact |

**Actions taken:**
- SELL 43 WAFU @ $2.10 (id 3ee7b7e8), +$6.88 / +8.2%
- SELL 64 MTEN @ $1.35 (id c0ff8507), -$2.56 / -2.9%
- SELL 47 MGIH @ $2.02 (id c8a5fc8e), -$4.70 / -4.7%
- HOLD FF (Grade B, day 1). Trail not active (peak +2.7% below +30% threshold). Hard stop -15% = $5.34.
- Net on 3 sells: -$0.38. All filled with price improvement over limit.

**Data notes:** Alpaca IEX quotes were stale (prior-close, 20:xx UTC). Used SIP 5Min bars for fillable levels. price-timeline.py labels UTC as "ET"; PM bars 08:00-08:15 UTC = 04:00-04:15 ET premarket open.

## Position Evaluation — 14:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| FF | $6.28 | $6.20 | -1.3% | $6.45 (+2.7%) | 1 | B | HOLD | Day 1 of 2, above -15% stop ($5.34), no trail triggered (never hit +30%), earnings catalyst intact. PM flat $6.04-6.30, no momentum spike to sell into. |

**Actions taken:**
- None. FF held. Alpaca (source of truth) and OPEN_POSITIONS.md reconciled — FF only open position.
- Quote bid $6.19 was stale (yesterday 20:40Z); confirmed live PM ~$6.15-6.23 via SIP 5Min bars.
