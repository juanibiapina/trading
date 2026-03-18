---
name: post-market
description: Post-market screening and trade execution workflow for after-hours trading (4:00-8:00 PM ET / 22:00-02:00 CET). Use when the user says "post-market", "after hours", "AH screening", or asks to find stocks moving after market close. Triggers on evening screening sessions, after-hours gainer analysis, and overnight hold candidates.
---

# Post-Market Workflow

Screen for after-hours momentum stocks and identify overnight hold candidates.

**Session:** 4:00-8:00 PM ET (22:00-02:00 Berlin)

## Step 0: Create today's log directory and file

- Run `date`
- Create directory and file: `log/YYYY-MM-DD/log.md`

## Step 1: Run Scanner

Run the scanner script to get candidates:

```bash
python3 scripts/scan.py --all
```

The scanner auto-detects the after-hours session and returns stocks with:
- All sectors — no sector filter (learning phase, see Day Trading.md)
- Market cap < $100M
- Price $0.50-$10
- AH volume > 50K
- AH change > 5%

Present the results to the user in a table with clickable TradingView links:

```
| Ticker | Chart | Close | AH Chg | AH Price | AH Vol | Float | Industry |
|--------|-------|-------|--------|----------|--------|-------|----------|
| TICKER | [TV](https://www.tradingview.com/chart/?symbol=TICKER) | $X | +X% | $X | XK | XM | Industry |
```

Ask which tickers to analyze further.

## Step 2: Analyze Each Candidate

For each selected candidate:

1. **Check catalyst** — Search for recent news:
   ```bash
   websearch search "TICKER COMPANY_NAME stock news" --freshness day -n 5
   ```
   Look for: partnerships, FDA news, earnings, offerings (dilution = bad)

2. **Open chart in TradingView** for visual analysis:
   ```bash
   browse tab.new "https://www.tradingview.com/chart/?symbol=TICKER"
   ```

3. **Assess setup** — Based on scanner data + news, determine catalyst tier and decision

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

**Buy criteria (learning phase — paper trade only):**
- Any sector (no sector restriction — learning phase)
- Good catalyst (news, partnership, FDA, earnings — not just volume)
- Float < 10M
- Volume confirming:
  - volume not fading
  - today is the first day of unexpected volume (reject tickers that had unexpected volume in the previous days)
- Note: previous hard rules (biotech only, never >50% above close) are now observations under review — see Day Trading.md Learning Phase

**Entry rules:**
- ~€100 position size (learning phase)
- Accept full loss potential — stop losses do NOT execute in extended hours
- Plan to exit in premarket (before 9:30 AM ET / 15:30 CET)
