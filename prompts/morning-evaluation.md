Run a morning evaluation of last night's post-market scanning session.

**Primary goal: find today's winner and diagnose the scanner.**

The most important question is: what stock IS exploding in premarket right now? There is almost always one. Find it first — independently, without looking at last night's watchlist — then check if our evening scanner would have caught it. This is the baseline test: if the scanner can't even detect the winners, no entry rules will make the strategy work. See "Learning Phase" in Day Trading.md for the full reasoning.

## Steps

### 1. Setup

- Run `date` to get the current time
- Determine yesterday's US trading date (the AH session we're evaluating)
- Set `LOG_FILE=log/YYYY-MM-DD/log.md` using that date
- Pull latest changes
- Read the existing log to understand what was found and any paper trades

### 2. Find Today's Winner

**Do this BEFORE looking at last night's log.** Search fresh for what is exploding in premarket right now.

Run both a forced after-hours scan and a live premarket scan:

```bash
python3 scripts/scan.py --all --session afterhours
python3 scripts/scan.py --all --session premarket
```

From the results, identify the **best AH→premarket trade** — the stock that:
- Spiked in after-hours yesterday
- Is still running or peaking in premarket now
- Would have given the best return if bought in AH and sold now

This is "today's winner." Document it with: sector, catalyst, float, AH entry price, current PM price, hypothetical P&L.

**Then** go back and read last night's log. Was this stock on our radar? This is the scanner diagnostic.

### 3. Check Paper Trade P&L

If there are paper trades in the log, check their current prices:

```bash
python3 scripts/check-prices.py TICKER1 TICKER2 ...
```

For each paper trade:
- Get current premarket price (or latest available price)
- Calculate unrealized P&L: `(current_price - entry_price) * shares`
- Calculate P&L percentage: `((current_price - entry_price) / entry_price) * 100`

### 4. Scanner Diagnostic

**For today's winner (from Step 2), answer:**
- Was it detectable at evening screening time (~22:15 CET)? YES / NO
- If YES: what did it look like then? (price, volume, % gain) — why didn't we act on it?
- If NO: why not? (news came later, AH move started after midnight, no volume yet, etc.)
- What scanner change would have caught it?

**Then compare all retrospective results with evening scans:**
- **Caught**: stocks in both evening scans and retrospective
- **Missed**: stocks in retrospective that evening scans never found
- For each missed stock, analyze WHY:
  - Appeared too late (after our last scan)?
  - Below our volume/change thresholds at scan time?
  - Sector filtered out?

### 5. Update Log

Append a `## Morning Evaluation` section to the log:

```markdown
## Morning Evaluation — HH:MM CET

### Today's Winner

**[TICKER]** — [sector]
- Catalyst: [what drove it]
- Previous Close: $X
- AH last night: $X (+X%) at HH:MM CET
- Premarket now: $X (+X%)
- Hypothetical P&L (AH entry → PM peak): +X%
- Float: X | Market Cap: $X

**Scanner Diagnostic:**
- Detectable at screening time? **YES / NO**
- [If YES: what it looked like at ~22:15 CET, why we did/didn't act]
- [If NO: why — news timing, volume below threshold, etc.]
- Scanner gap: [what would need to change to catch this]

[If no clear winner today: "No stock showed the AH→PM pattern today. Reason: [market conditions, etc.]"]

### Baseline Tracking

- Days tracked: X
- Winners detected by scanner: X/Y (**X%**)
- Winner selected for paper trade: X/Y (**X%**) — did we trade the right stock?
- Target: >80% detection
- Status: **BASELINE MET / NOT MET**

### Retrospective Scan Results
[results from forced AH + PM scans]

### Paper Trade P&L

| Ticker | Entry | Entry Time | Current | P&L | P&L % | Status |
|--------|-------|------------|---------|-----|-------|--------|
| XXXX   | $2.50 | 23:00 CET  | $3.10   | +€24.00 | +24.0% | ✅ Win |

**Total Paper P&L: +€XX.XX**

### Scanner Effectiveness

- Evening scans ran: X times (HH:MM - HH:MM CET)
- Candidates found: X unique tickers
- Retrospective matches: X/Y

### Missed Opportunities

| Ticker | AH Change | Why Missed | Would Be Profitable? |
|--------|-----------|------------|---------------------|

[or "No significant missed opportunities."]

### AH Mover Follow-Through

How did last night's top AH movers perform into premarket? Include every stock that appeared in 2+ evening scans with AH change >10%.

| Ticker | AH Peak | AH Peak Time | Current PM | From Peak | From Prev Close | Verdict |
|--------|---------|-------------|------------|-----------|-----------------|---------|

This tracks whether AH momentum carries into premarket (the core trading hypothesis).

### Notes
[any observations about scanner performance, threshold adjustments needed, etc.]
```

### 6. Commit

```bash
git add log/
git commit -m "morning evaluation YYYY-MM-DD"
git push
```
