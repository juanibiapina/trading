# Open Positions

Active paper trade positions, executed on the **Alpaca paper account** (`PA37U2Y192A7`).
Alpaca is the source of truth. This file mirrors `node scripts/broker.js positions`.
Every entry/exit must be a real Alpaca order; do not record trades that were not submitted.

## Current Positions

| Ticker | Entry | Shares | Cost | Entry Time | Catalyst | Grade | Hold Strategy |
|--------|-------|--------|------|-----------|----------|-------|---------------|
| PMA | $1.66 | 60 | $99.60 | 2026-07-09 17:00 ET | Ticker change MSW→PMA (rebrand to PMA Nano Carbon Tech) + prior dilutive convertible notes | C | Exit in premarket (weak/dilutive catalyst) |
| ELPW | $1.18 | 83 | $97.94 | 2026-07-09 17:30 ET | Low-float squeeze after $6M discounted public offering + 1-for-80 reverse split (dilution) | D | Exit at first premarket opportunity |
| YYGH | $1.66 | 58 | $96.28 | 2026-07-09 18:30 ET | Low-float squeeze (133K float), 30-for-1 reverse split; no fresh same-day catalyst | None | Exit at first premarket opportunity |

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
| GANX | $2.39 | $1.97 | -$17.22 | -17.6% | 1 | B (Phase 1b Parkinson's data) | Hard stop hit. Held overnight; PM faded from $2.17 to $1.97, below -15% stop ($2.03). Sold per Grade B hard-stop rule. Real fill $1.97. Peak $2.59 (AH 06-29). |
| IVF | $1.58 | $2.00 | +$25.20 | +26.6% | 1 | None (Grade None) | Low-float AH build, no fresh catalyst. Sold premarket per Grade None rule (exit at any profit). PM ran to $2.59 peak (+64% from entry); exited at $2.00. |
| CTNT | $2.05 | $1.90 | -$7.20 | -7.3% | 1 | None (Grade None) | Low-float squeeze, no catalyst. Sold first premarket opportunity per Grade None rule. AH peaked $2.21; faded to $1.94 PM. Exited at $1.90 (real fill). |
| ALZN | $1.31 | $1.29 | -$1.46 | -1.5% | 1 | None (Grade None) | No catalyst (earnings due 7/19; no same-day PR). Sold first PM opportunity per Grade None rule. OVN peak $1.45 (+10.7%); faded overnight. SELL 73 @ $1.29 ext (id f7da27e2) filled 2026-07-01 08:33 UTC. Real fill $1.29. |
| EDHL | $4.81 | $5.10 | +$5.80 | +6.0% | 1 | None (Grade None) | Low-float double-pump momentum, no catalyst. Sold first PM opportunity per Grade None rule. OVN peak $5.83 (+21% from entry); PM opened $6.29 spike then faded to ~$5.15. SELL 20 @ $5.10 ext (id cdfa66da) filled 2026-07-07. Real fill $5.10. |
| DCX | $1.34 | $1.39 | +$3.30 | +3.7% | 1 | None (Grade None) | Low-float AH BUILD, no catalyst. Sold first PM opportunity per Grade None rule. PM 07-08 opened strong ($1.63 H, 2.5M sh/bar) then faded; peak +10% (~$1.48). Exited on the fade. SELL 66 @ $1.39 ext (id a10d862b) filled 2026-07-08. Real fill $1.39. |
| VEEE | $6.28 | $6.17 | -$1.65 | -1.8% | 1 | C (DoD LYNX Platform registration) | Grade C — exit in first PM pulse. AH high $7.31; PM opened $6.97 then faded to $6.30/vwap $6.45. Sold in first PM pulse per Grade C rule, small loss (above -10% stop). SELL 15 @ $6.17 ext (id 590df196) filled 2026-07-08. Real fill $6.17. |
| SEER | $2.26 | $2.20 | -$2.58 | -2.65% | 5 | A (CEO $2.45/share buyout proposal + activist proxy contest) | Grade A held full 5-day window (entry 07-03). Catalyst intact ($2.45 floor) but never re-rated above entry; peak $2.34 (+3.5%, OVN 07-02). Sold on day-5 time limit at 14:30 CET pulse. SELL 43 @ limit $2.12 ext (id 34b9f54e), filled @ $2.20 (real bid). |
| SUNE | $2.56 | $2.44 | -$4.32 | -4.7% | 1 | None | No same-day catalyst (SUNation Energy solar). Sold first PM opportunity per Grade None rule. OVN peak ~$2.67 (+4.3%); PM opened $2.72 spike (single-bar) then faded to $2.41/vwap $2.39. SELL 36 @ limit $2.35 ext (id 54d1a663) filled 2026-07-09. Real fill $2.44. |
