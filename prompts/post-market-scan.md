Run a post-market scan and update the daily log with results and paper trade decisions.

## Steps

### 1. Setup

- Run `date` to get the current time
- Determine the US trading date: if current CET time is before 06:00, the trading date is yesterday (CET). Otherwise it's today.
- Set `LOG_DIR=log/YYYY-MM-DD` and `LOG_FILE=log/YYYY-MM-DD/log.md` using the trading date
- Make sure the repository is clean (stash if needed)
- Pull latest changes

### 2. Run Scanner

```bash
python3 scripts/scan.py --all
```

### 3. Update Log

- If `LOG_FILE` doesn't exist, create it with the header:
  ```markdown
  # Post-Market Screening - YYYY-MM-DD

  ## Paper Trades

  | Ticker | Entry Price | Entry Time | Shares (~€100) | Reason |
  |--------|-------------|------------|-----------------|--------|
  ```

- Append a timestamped scan section **before** the `## Paper Trades` section:
  ```markdown
  ## Scan HH:MM CET (H:MM PM ET)

  [results table or "No candidates found."]
  ```

- If there ARE results, format them as:
  ```markdown
  | Ticker | Chart | Close | Day% | AH Chg | AH Price | AH Vol | AvgVol | VRatio | Float | Industry |
  |--------|-------|-------|------|--------|----------|--------|--------|--------|-------|----------|
  | TICK   | [TV](https://www.tradingview.com/chart/?symbol=TICK) | $X | +X% | +X% | $X | XK | XK | Xx | XM | Industry |
  ```

### 4. Paper Trade Decisions

Read the existing log to see which tickers were already found in previous scans today.

For each **new** candidate (not in prior scans), evaluate against the entry criteria from the trading plan:
- Biotech/pharma preferred (non-biotech has 0% win rate historically)
- Price < 50% above previous close (for AH scans, check Day% + AH Chg% = total move from previous close)
- Float < 10M ideal
- Has a clear catalyst (search for news if needed)
- Volume not fading, first day of unusual activity

If a candidate passes, add a paper trade entry to the `## Paper Trades` table:
- Entry Price = current AH price
- Shares = ~€100 / entry price (round down)
- Reason = brief justification

If a candidate fails, note briefly why in the scan section (e.g., "Skip: no catalyst", "Skip: float too high").

For candidates already seen in prior scans, note any significant changes (price movement, volume increase/decrease).

### 5. Commit

```bash
git add log/
git commit -m "post-market scan YYYY-MM-DD HH:MM CET"
git push
```
