# Position Evaluation

Evaluate open positions and decide whether to hold or sell based on risk rules.

**Non-interactive:** This pulse runs unattended. Never ask Juan questions or show Telegram buttons here — no one answers. Act on the best available decision and route anything needing his input to the **daily email** (questions go in emails only).

**Schedule:** Runs at 10:30 CET and 14:30 CET (premarket windows for selling)

## Data Sources (read first, every pulse)

Apply this data hierarchy from the start of the pulse:
- **Position state + current price (source of truth):** `node scripts/broker.js positions` (Alpaca `current_price`, real entry). This — not Yahoo — is the P&L basis.
- **Fillable exit price (real-time):** `node scripts/broker.js quote SYM` — set the sell limit off the real bid; `ask $0.00 x0` / thin book means low fillability.
- **Real premarket volume + bad-print detection:** `node scripts/broker.js bars SYM --tf 5Min --start <PM-start-UTC>` — SIP feed (full-market `vol` + `vwap`). PM open 04:00 ET = `08:00:00Z` (EDT) / `09:00:00Z` (EST). Use SIP `H`/`vwap` to sanity-check any peak.
- **Do NOT trust Yahoo for volume or exact levels:** Yahoo ext-hours *volume* is always 0; Yahoo PM *prices* can bad-print on illiquid names and overstate the peak. Yahoo is fine for the timeline shape, not for the exit price or peak level.

## Steps

### 1. Setup

```bash
date
git stash && git pull --ff-only && git stash pop 2>/dev/null || true
```

Get current positions from Alpaca (source of truth), then cross-check `OPEN_POSITIONS.md`:

```bash
node scripts/broker.js account
node scripts/broker.js positions
node scripts/broker.js orders all
```

If `OPEN_POSITIONS.md` disagrees with Alpaca, Alpaca wins. Reconcile the file.

### 2. Get Current Prices

The P&L basis is Alpaca's `current_price` from `broker.js positions` (Step 1), not Yahoo. Use Yahoo only for the premarket timeline *shape*:

```bash
python3 scripts/check-prices.py TICKER1 TICKER2 ...
python3 scripts/price-timeline.py TICKER1 TICKER2 ...
```

**Verify any peak against SIP** before acting on it — Yahoo PM prices bad-print on illiquid names and can overstate the peak. Cross-check with `node scripts/broker.js bars SYM --tf 5Min --start <PM-start-UTC>` (SIP `H`/`vwap`); if Yahoo's peak is far above the SIP high/VWAP, use the SIP level. Before placing a sell, take the real sellable bid from `node scripts/broker.js quote SYM`.

Calculate for each position:
- **Current P&L %** = (current_price - entry_price) / entry_price  (current_price from Alpaca)
- **Peak P&L %** = (peak_price - entry_price) / entry_price (peak verified against SIP)
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

For any SELL decisions, submit a real Alpaca order (extended-hours limit during pre/post market):

```bash
node scripts/broker.js sell SYM QTY --limit PRICE --ext
```

Set the limit a few cents below the bid to ensure a fill in thin pre/post-market books.
Then:
1. Confirm the fill: `node scripts/broker.js orders all` (read `filled_avg_price`)
2. Record exit in `OPEN_POSITIONS.md` (move to Closed Positions) using the **real fill price**
3. Calculate final P&L from the real fill
4. Log the trade in `log/YYYY-MM-DD/log.md`

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

With ~$100 positions:
- Max loss on Grade D (quick exit at -10%): $10
- Max loss on Grade A (hold to -25% stop): $25
- Potential gain on Grade A runner (+200%): $200

**Risk/reward ratio for Grade A:** Risk $25 to potentially make $200+ = 8:1

This justifies holding Grade A positions through volatility that would trigger exits on lower-grade positions.
