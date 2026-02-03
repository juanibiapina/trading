---
name: post-market
description: Post-market screening and trade execution workflow for after-hours trading (4:00-8:00 PM ET / 22:00-02:00 CET). Use when the user says "post-market", "after hours", "AH screening", or asks to find stocks moving after market close. Triggers on evening screening sessions, after-hours gainer analysis, and overnight hold candidates.
---

# Post-Market Workflow

Screen for after-hours momentum stocks and identify overnight hold candidates.

**Session:** 4:00-8:00 PM ET (22:00-02:00 Berlin)

## Step 0: Create today's log directory and file

- Run `date`
- Create directory and file: `log/YYYY-MM-DD/log.md`:

## Step 1: Screen for AH Gainers

- Browse in new tab: https://www.tradingview.com/markets/stocks-usa/market-movers-after-hours-gainers/
- Take a screenshot and extract tickers and available information
- Filter for tickers that have gains

## Step 2: Analyze Each Candidate

For each candidate:

1. **Check catalyst** — Look for news on Finviz (`https://finviz.com/quote.ashx?t=TICKER`)

2. **Check fundamentals** via Yahoo Finance API:
   ```
   https://query1.finance.yahoo.com/v8/finance/chart/TICKER?interval=1m&range=1d&includePrePost=true
   ```
   - Float, market cap, volume vs average
   - Current AH price vs close

3. **Assess price action**

## Step 3: Log Candidates

```markdown
# Post-Market Screening - YYYY-MM-DD

## Candidates

### TICKER
- **AH Price:** $X (+X%)
- **Previous Close:** $X
- **Float:** X
- **Market Cap:** $X
- **Catalyst:** [description + tier]
- **Volume:** X (Xx average)
- **Decision:** Buy / Watch / Skip
- **Reason:** [why]
```

## Step 4: Entry Decision

**Buy criteria (all or most must be true):**
- Biotech/pharma sector
- Good catalist
- Price < 50% above previous close
- Float < 10M
- Volume confirming:
  - volume not fading
  - today is the first day of unexpected volume (reject tickers that had unexpected volume in the previous days)

**Entry rules:**
- ~€100 position size (learning phase)
- Accept full loss potential — stop losses do NOT execute in extended hours
- Plan to exit in premarket (before 9:30 AM ET / 15:30 CET)
