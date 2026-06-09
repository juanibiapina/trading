# Open Positions

Active paper trade positions. Updated by evening scans (entries) and position evaluation (exits).

## Current Positions

| Ticker | Entry Date | Entry Price | Shares | Cost Basis | Catalyst Grade | Catalyst | Stop Loss | Target | Peak |
|--------|------------|-------------|--------|------------|----------------|----------|-----------|--------|------|
| MSW | 2026-06-09 | $3.24 | 30 | $97.20 | C | Acquisition close (PMA Nano Carbon Tech) + dilutive convertible notes | $2.92 (-10%) | Premarket exit | $3.57 |

## Position Rules

### Entry (after-hours scans)
- Enter when stock meets scanner criteria (float, AH%, catalyst)
- Position size: €100 per trade (learning phase)
- Record catalyst grade at entry (A/B/C/D/None)

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

## Closed Positions (Last 10)

| Ticker | Entry | Exit | P&L | P&L % | Hold Days | Catalyst | Notes |
|--------|-------|------|-----|-------|-----------|----------|-------|
| ANY | $4.84 | $3.81 | -$20.60 | -21.3% | 2 | A - Cathedra Bitcoin acquisition | Stop breached overnight (low $3.54), peaked at $5.50 (+13.6%) |
| PRFX | $7.28 | $5.18 | -$27.30 | -28.8% | 1 | B - DeepSolar Predict™ launch | Hard stop breached, peaked at $9.30 (+27.7%) then overnight fade |
| ATPC | $7.23 | $6.21 | -$13.26 | -14.1% | 1 | None | Hard stop breached, peaked at $8.30 (+14.8%) then faded |
| VCIG | $3.91 | $3.60 | -$7.75 | -7.9% | 2 | B - CEO insider buy | Day 2 exit per Grade B rules, peak +21.5% |
| BNZI | $4.61 | $3.53 | -$24.84 | -23.4% | 2 | B - Debt elimination | Hard stop breached, overnight gap down |
| CODX | $2.50 | $1.77 | -$29.20 | -29.2% | 2 | B - Ebola testing strategy | Hard stop breached, collapsed in premarket |
| AMST | $1.17 | $2.62 | +$123.25 | +124% | 1 | B - Enterprise customer win | Trail stop hit at $2.89 after $3.40 peak |
| TRNR | $1.31 | $1.07 | -$19.68 | -18.3% | 1 | B - Q1 earnings beat | Hard stop breached, faded from $1.64 AH peak |
| FOXX | $5.62 | $4.74 | -$14.96 | -15.7% | 1 | None | Hard stop breached, peaked at $6.10 (+8.5%) then overnight fade |
| BIYA | $1.12 | $1.16 | +$3.56 | +3.6% | 1 | None | Exited at profit per rules, avoided fade from $1.41 peak |
