# Position Evaluation

Sell every open position at the first premarket evaluation, and resell anything left unfilled at 14:30 CET.

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
bash scripts/sync-repo.sh
TODAY=$(date +%F)
mkdir -p "log/$TODAY"
touch "log/$TODAY/log.md"
```

Create today's log before trying to read or search it. Get current positions from Alpaca (source of truth), then cross-check `OPEN_POSITIONS.md`:

```bash
node scripts/broker.js account
node scripts/broker.js positions
node scripts/broker.js orders all
```

If `OPEN_POSITIONS.md` disagrees with Alpaca, Alpaca wins. Reconcile the file.

Read only the file's open section (current positions and rules, about 3 KB):

```bash
sed -n '1,/^## Closed Positions/p' OPEN_POSITIONS.md
```

The Closed Positions table below it is history (about 45 KB, newest first). Do not read it whole. To record an exit, insert the new row directly under the table's header and separator lines, which `rg -n -A1 '^\| Ticker \| Entry \| Exit \|' OPEN_POSITIONS.md` prints; use those two lines as the edit anchor.

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

### 3. Apply the Exit Rule

**Sell every open position at the first premarket evaluation (10:30 CET / 04:30 ET), whatever its grade.** No position is held past that pulse for a later premarket or a later day. (Applied 2026-10-14 by `strategy-advance` under Juan's standing apply-and-report directive; retroactive veto. Basis: on the 89 real Alpaca AH entries, the 26 held past the 04:30 evaluation under the old Grade A/B hold rules returned -11.9% against -3.1% if sold at the 04:30 open; 21 of 26 were worse, p 0.038, both chronological halves negative. Selling all at 04:30 would have moved the per-trade mean from -3.2% to -1.0%. See `docs/investigations/init3-exec-gap-2026-10-09.md`.)

- **10:30 CET pulse:** SELL every position. Price the limit off the real bid (Step 5).
- **14:30 CET pulse:** any position still open means the 10:30 order did not fill. Cancel the stale order, take a fresh bid, and SELL again.
- **Catalyst grade (A/B/C/D/None)** is still recorded at entry and in the exit row for pattern analysis. It no longer changes the exit time. The fixed-price cash buyout rule (grade D, not A) still applies to grading.
- If the book has no bid at all (`bid $0.00`), rest the limit at the last SIP vwap and log it; the 14:30 pulse reprices.

### 4. Make Decisions

For each position, output **SELL** (first premarket evaluation) or **RESELL** (14:30 pulse, unfilled 10:30 order). Record the grade and the peak in the log for analysis.

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
- Move sold positions to Closed Positions table

Only edit content needed to reconcile positions or record the evaluation; skip cosmetic whitespace changes. If an exact-text edit fails, reread the current file, choose a shorter unique target, and retry once. Do not repeat the unchanged `oldText`.

### 7. Log Summary

Append to today's log (`log/YYYY-MM-DD/log.md`):

```markdown
## Position Evaluation — HH:MM CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| XXXX | $2.50 | $3.20 | +28% | $3.50 | 1 | A | SELL | First premarket evaluation |

**Actions taken:**
- [List sells, fills and any reprices]
```

### 8. Commit

```bash
git add log/ OPEN_POSITIONS.md
git commit -m "position evaluation YYYY-MM-DD HH:MM"
git push
```

## Risk Framework

### Why Every Position Exits at the First Premarket Evaluation

The old rules held Grade A positions up to 5 days and Grade B up to 2, citing AIIO (+878% over 7 days) and UGRO (+62% after day 1) from the pre-Alpaca ledger. On real Alpaca fills since 2026-06-25 the holds lost: 26 held trades returned -11.9% against -3.1% at the 04:30 open. The two big hold winners (CHPT +50.9 points, VEEA +46.2) did not offset the losers (DARE -39.9, TOPS -44.6, ONFO -28.3). The 63 trades sold at 04:30-05:00 ET beat the modeled 04:30 open by 0.58 points. `Day Trading.md` already says to sell every position in premarket before the open.

### Why Exit No-Catalyst Names Quickly

- **EZGO** (No catalyst): -99% crash
- **WOK** (Unknown catalyst): -87% crash
- **LNKS** (No catalyst): Back to start

No-catalyst moves are often pump-and-dumps or momentum plays that reverse violently.
