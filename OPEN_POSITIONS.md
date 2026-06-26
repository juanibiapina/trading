# Open Positions

Active paper trade positions, executed on the **Alpaca paper account** (`PA37U2Y192A7`).
Alpaca is the source of truth. This file mirrors `node scripts/broker.js positions`.
Every entry/exit must be a real Alpaca order; do not record trades that were not submitted.

## Current Positions

| Ticker | Entry Date | Entry Price | Shares | Cost Basis | Catalyst Grade | Catalyst | Stop Loss | Target | Peak |
|--------|------------|-------------|--------|------------|----------------|----------|-----------|--------|------|

_No open positions._

## Position Rules

### Entry (after-hours scans)
- Enter when stock meets scanner criteria (float, AH%, catalyst)
- **Multiple concurrent positions allowed** (W24 2026). An open position no longer blocks new entries; enter every qualifying candidate.
- One entry per candidate per night (don't average into the same ticker).
- Position size: ~$100 per trade (learning phase), sized independently per position
- Record catalyst grade at entry (A/B/C/D/None)
- **Execute via Alpaca:** `node scripts/broker.js buy SYM QTY --limit P --ext` (extended-hours limit). Record the real fill price returned by the order, not the quoted/assumed price.

### Holding Rules (based on catalyst grade)
| Grade | Description | Hold Strategy |
|-------|-------------|---------------|
| **A** | Major operational catalyst (acquisition, breakthrough deal) | Hold up to 5 days, trail stop at -20% from peak |
| **B** | Solid catalyst (earnings beat, FDA milestone) | Hold up to 2 days, stop at -15% from entry |
| **C** | Weak catalyst (analyst upgrade, financing) | Exit in premarket, stop at -10% |
| **D/None** | No catalyst or dilution | Exit at first premarket opportunity |

### Exit Triggers
1. **Stop loss hit** — Exit immediately
2. **Target reached** — Trail stop, don't exit all at once
3. **Time limit** — Grade A: 5 days, Grade B: 2 days, Others: premarket
4. **Catalyst invalidated** — News changes thesis → exit

Execute exits via Alpaca: `node scripts/broker.js sell SYM QTY --limit P --ext`. Record the real fill price.

## Risk Calculation

Based on historical data (17 winners tracked):
- Multi-day runners (held = big win): 2/17 = 12%
- Same-day peaks (held = loss): 15/17 = 88%

**Expected value per €100 position if held:**
- 12% chance of +200% avg = +€24
- 88% chance of -50% avg = -€44
- **EV if holding blindly: -€20 per trade**

**But with catalyst filtering:**
- Grade A catalyst runners: 2/2 = 100% (AIIO, UGRO both had real catalysts)
- No-catalyst crashes: 2/2 = 100% (EZGO, WOK)

**Conclusion:** Hold Grade A, exit others quickly.

## Closed Positions

Clean slate as of 2026-06-25. Only real Alpaca paper fills are recorded here going forward.
The pre-Alpaca markdown ledger used assumed prices that were never executed and has been discarded.

| Ticker | Entry | Exit | P&L | P&L % | Hold Days | Catalyst | Notes |
|--------|-------|------|-----|-------|-----------|----------|-------|
| IVF | $1.58 | $2.00 | +$25.20 | +26.6% | 1 | None (Grade None) | Low-float AH build, no fresh catalyst. Sold premarket per Grade None rule (exit at any profit). PM ran to $2.59 peak (+64% from entry); exited at $2.00. |
