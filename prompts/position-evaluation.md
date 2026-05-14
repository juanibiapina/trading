# Position Evaluation

Evaluate open positions and decide whether to hold or sell based on risk rules.

**Schedule:** Runs at 10:30 CET and 14:30 CET (premarket windows for selling)

## Steps

### 1. Setup

```bash
date
git stash && git pull --ff-only && git stash pop 2>/dev/null || true
```

Read `OPEN_POSITIONS.md` to get current positions.

### 2. Get Current Prices

For each open position:

```bash
python3 scripts/check-prices.py TICKER1 TICKER2 ...
python3 scripts/price-timeline.py TICKER1 TICKER2 ...
```

Calculate for each position:
- **Current P&L %** = (current_price - entry_price) / entry_price
- **Peak P&L %** = (peak_price - entry_price) / entry_price (if tracked)
- **Days held** = today - entry_date

### 3. Apply Risk Rules

For each position, evaluate based on catalyst grade:

#### Grade A (Major operational catalyst)
- **Hold up to 5 days**
- **Trail stop:** If peak P&L > +50%, set stop at peak - 20%
- **Hard stop:** -25% from entry
- **Exit trigger:** Catalyst invalidated by news

#### Grade B (Solid catalyst)
- **Hold up to 2 days**  
- **Trail stop:** If peak P&L > +30%, set stop at peak - 15%
- **Hard stop:** -15% from entry

#### Grade C (Weak catalyst)
- **Exit in first premarket pulse**
- **Hard stop:** -10% from entry

#### Grade D or None (No catalyst)
- **Exit immediately at any profit**
- **Hard stop:** -10% from entry

### 4. Make Decisions

For each position, output one of:
- **HOLD** — Within risk parameters, catalyst intact
- **TRAIL** — Set/update trailing stop at X price
- **SELL** — Exit position (stop hit, time limit, or target reached)

### 5. Execute Sells

For any SELL decisions:
1. Record exit in `OPEN_POSITIONS.md` (move to Closed Positions)
2. Calculate final P&L
3. Log the trade in `log/YYYY-MM-DD/log.md`

### 6. Update Tracking

Update `OPEN_POSITIONS.md`:
- Update current prices
- Update peak prices if new high
- Update trailing stops if applicable
- Move sold positions to Closed Positions table

### 7. Log Summary

Append to today's log (`log/YYYY-MM-DD/log.md`):

```markdown
## Position Evaluation — HH:MM CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| XXXX | $2.50 | $3.20 | +28% | $3.50 | 2 | A | HOLD | Trail stop at $2.80 |

**Actions taken:**
- [List any sells or stop updates]
```

### 8. Commit

```bash
git add log/ OPEN_POSITIONS.md
git commit -m "position evaluation YYYY-MM-DD HH:MM"
git push
```

## Risk Framework

### Why Hold Grade A Positions

From historical data:
- **AIIO** (Grade A - $100M acquisition): +878% over 7 days
- **UGRO** (Grade A - major merger): +62% additional after day 1

Both Grade A positions were multi-day runners. The pattern: **real operational catalysts drive sustained momentum.**

### Why Exit Grade C/D/None Quickly

- **EZGO** (No catalyst): -99% crash
- **WOK** (Unknown catalyst): -87% crash
- **LNKS** (No catalyst): Back to start

No-catalyst moves are often pump-and-dumps or momentum plays that reverse violently.

### Position Sizing for Risk

With €100 positions:
- Max loss on Grade D (quick exit at -10%): €10
- Max loss on Grade A (hold to -25% stop): €25
- Potential gain on Grade A runner (+200%): €200

**Risk/reward ratio for Grade A:** Risk €25 to potentially make €200+ = 8:1

This justifies holding Grade A positions through volatility that would trigger exits on lower-grade positions.
