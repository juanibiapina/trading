Run a morning evaluation of last night's post-market scanning session.

The goal is to assess scanner effectiveness: did we catch the right stocks? What did we miss?

## Steps

### 1. Setup

- Run `date` to get the current time
- Determine yesterday's US trading date (the AH session we're evaluating)
- Set `LOG_FILE=log/YYYY-MM-DD/log.md` using that date
- Pull latest changes
- Read the existing log to understand what was found and any paper trades

### 2. Retrospective Scan

Run both a forced after-hours scan and a live premarket scan to get the fullest picture of what moved overnight. Use `--all` to scan ALL sectors — don't limit to biotech. We want to catch anything that would have been worth buying.

```bash
python3 scripts/scan.py --all --session afterhours
python3 scripts/scan.py --all --session premarket
```

The AH scan may still show yesterday's post-market movers. The premarket scan shows what's moving right now — stocks up in premarket often continued from an AH spike, so this catches movers our evening scans may have missed.

### 3. Check Paper Trade P&L

If there are paper trades in the log, check their current prices:

```bash
python3 scripts/check-prices.py TICKER1 TICKER2 ...
```

For each paper trade:
- Get current premarket price (or latest available price)
- Calculate unrealized P&L: `(current_price - entry_price) * shares`
- Calculate P&L percentage: `((current_price - entry_price) / entry_price) * 100`

### 4. Find Missed Opportunities

Compare the retrospective scan results with what our evening scans caught:

- **Caught**: stocks that appeared in both evening scans and retrospective scan
- **Missed**: stocks in the retrospective scan that our evening scans never found
- For each missed stock, analyze WHY it was missed:
  - Appeared too late (after our last scan)?
  - Below our volume/change thresholds at scan time?
  - Different sector filtered out?

Also check if any missed stocks would have been profitable (i.e., they're still up in premarket).

### 5. Update Log

Append a `## Morning Evaluation` section to the log:

```markdown
## Morning Evaluation — HH:MM CET

### Retrospective Scan
[results from forced AH scan, if any]

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
