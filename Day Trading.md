---
tags:
  - project
---

# Day Trading

## Trading Plan

- The goal is to catch the start of the day bumps that some biotech companies get.
- I'll use the screener in the beginning of the day to figure out what to buy.
- I'll sell in less than 15 minutes.
- I'll trade "warrior stocks" as set in my screener.
- I will trade only once per day.
- I'll stop after winning or losing either way.
- Only one position at a time.
- I'll trade in the PC.
- I'll keep the amount around 100 euros per trade since this is a learning time.
- **Sector discipline:** Biotech/pharma only. Non-biotech trades (DRCT advertising, XPON industrials, PZG gold) all lost in W05.
- **Scanner:** Use custom TradingView screener script (`scanner/scan.py`) to detect volume spikes. Run with `--all` to scan all sectors, then verify catalyst manually. See [TradingView Screener API](#tradingview-screener-api-free) in Resources.

## Scanner Learnings (Feb 5, 2026)

**Key insight: `relative_volume_intraday` beats `relative_volume_10d_calc`.**
- `relative_volume_10d_calc|5` compares current 5m bar to the overall 10-day average 5m bar — useless because open/close bars skew the average, making normal mid-day bars look like spikes.
- `relative_volume_intraday|5` compares to what's typical *for this specific time of day* — much more accurate for detecting real unusual activity.

**Catalyst verification is critical.**
- Scanner finds volume spikes, but not all spikes are tradeable.
- No-news pumps (GDTC — Discord pump by "Grandmaster-Obi") spike and fade fast.
- Real catalysts (AIM — Phase 2 clinical data, CISS — ownership filing + fleet expansion, TRUG — product launch partnership) have more follow-through.
- Always check news before entering.

**Consider expanding beyond biotech.**
- CISS (shipping, 194K float) and TRUG (software/gaming) both had real catalysts and big moves.
- Ultra-low float (<500K) produces the most violent moves regardless of sector.
- Run scanner with `--all` flag, then filter by catalyst quality manually.

## Trading Plan Requirements

These questions are useful to ask when defining or updating the Trading Plan.

- Schedule for daily or weekly research and trade review

- List of patterns and ideas to trade

- Target activity and risk levels.
  - How many trades a day/week/month will you allow?
  - How many positions can you have on at the same time?
  - What is the maximum percentage of your capital that can be at risk at any time?
  - How and when will you use margin?
  - Is there a loss level at which you will stop trading for the day/week/month?  

- A clear plan for trade management.
  - Will you enter all at once or scale in?
  - Will you take partial profits? If so, where and how?  

- How often will you make trading decisions? Are you able to make decisions in the middle of the day, or do you prefer to create a plan the night before and simply execute it as faithfully as possible during the trading day?

## After-Hours → Premarket Strategy

**Key Insight (from BATL trade Jan 2026):** Momentum stocks often peak in premarket, then dump at open. The biggest gains happen *before* regular trading begins.

**The Pattern:**
1. Stock spikes in after-hours on catalyst (news, squeeze, etc.)
2. Momentum builds overnight as traders discover it
3. FOMO peaks in premarket → price explodes
4. Regular market opens → dump as early buyers take profits

**Examples (Jan 2026):**

| Stock | Entry | PM Peak | After Open | Lesson |
|-------|-------|---------|------------|--------|
| BATL | $1.86 | $7.00 (+276%) | $2.55 (-64%) | Sold at $2.40, missed PM peak |
| MRNO | $2.48 | ~$4.10 | $2.31 (-44%) | Sold at $3.80 PM - perfect exit |
| VIVS | $2.70 | $4.48 | - | Sold at $4.48 PM - perfect exit |

**Pattern confirmed 3/3 times in W05:** Exit in premarket, NOT at open.

**Trading Hours:**
| Session | US Eastern (ET) | Berlin (CET) |
|---------|-----------------|--------------|
| Premarket | 4:00 AM - 9:30 AM | 10:00 - 15:30 |
| Regular | 9:30 AM - 4:00 PM | 15:30 - 22:00 |
| After-hours | 4:00 PM - 8:00 PM | 22:00 - 02:00 |

**Strategy:**
1. **22:00-02:00 Berlin / 4:00-8:00 PM ET:** Screen for AH volume spikes
   - [TradingView AH Gainers](https://www.tradingview.com/markets/stocks-usa/market-movers-after-hours-gainers/)
   - [Finviz Screener](https://finviz.com/screener.ashx) - filter by after-hours change
   - Look for unusual volume increases after market close
2. **Identify catalyst:** Real news > no news. Check PR, SEC filings.
   
   **Catalyst Ranking (best to worst):**
   | Tier | Catalyst Type | Example | Result |
   |------|---------------|---------|--------|
   | A | Operational improvement | BATL gas agreement | +29% |
   | A | Partnership/distribution | VIVS Asia deal | +65% |
   | B | FDA milestone | SER IND clearance | -18% (faded) |
   | C | Analyst price target | ABOS $7 target | Skipped |
   | D | Financing/dilution | AGMH equity line | -5% (avoid) |
3. **Buy in after-hours:** Enter position after spotting the move
4. **Hold overnight**
5. **10:00-15:30 Berlin / 4:00-9:30 AM ET:** Watch for momentum peak, exit before regular open

**Risks:**
- Extended hours have wider spreads and lower liquidity
- **CRITICAL: Stop losses DO NOT execute in extended hours** - PZG (Jan 29) had SL at $2.49, stock crashed to $1.70, SL never triggered. Accept full loss potential or size smaller.
- Can gap against you overnight
- Need broker that supports extended hours trading

**Entry Rules (learned Jan 2026):**
- **Never chase >50% above previous close** - PZG entered at +97%, SER at +69%, both lost
- **Wait for consolidation** - VIVS entered after spike consolidated, won +65%
- **FOMO = worst entries** - Anxiety/rushing led to buying at literal tops

**TODO:** Track win rate of this strategy vs regular session trading.

---

## Weekly Review Workflow

Run this workflow at the end of each trading week to assess performance and refine the strategy.

### Steps

1. **Create review** - Document in `log/weekly/YYYY-WNN/review.md`
2. **Analyze trades** - Fill out the template below
3. **Update trading plan** - Extract learnings and update this document:
   - Add new examples to existing patterns
   - Add new rules based on repeated mistakes
   - Update catalyst rankings with real results
   - Document what worked/didn't work with specific trades

### Review Template

```markdown
# Weekly Review: [Date Range]

## Summary

| Metric | Value |
|--------|-------|
| Trading Days | X |
| Total Trades | X |
| Wins | X (X%) |
| Losses | X (X%) |
| Net P&L | $X |

## Trade Breakdown

| Date | Ticker | Entry | Exit | P&L | Notes |
|------|--------|-------|------|-----|-------|

## Rule Violations

1. [List any trading plan violations]

## Key Lessons

1. [What patterns emerged?]

## What Worked

| Pattern | Example | Result |
|---------|---------|--------|

## What Didn't Work

| Pattern | Example | Result |
|---------|---------|--------|

## Recommendations

1. [Action items for next week]

## Trading Plan Updates

[List changes made to Day Trading.md based on this week's learnings]
```

### Key Metrics to Track

- Win rate (target: >50%)
- Average win vs average loss (target: wins > losses)
- Rule compliance (target: 100%)
- Sector discipline (target: biotech only)

---

## Morning Analysis Workflow

Run this workflow between 7:00-9:30 AM ET to find premarket gappers before market open.

Document the analysis in `log/YYYY-MM-DD/log.md`.

### Step 1: Screen for Candidates (7:00-8:00 AM)

Use Finviz screener with these filters:
- Sector: Healthcare (Biotechnology focus)
- Market Cap: < $100M (micro-cap)
- Float: < 10M (low float = bigger moves)
- Relative Volume: > 2 (unusual activity)
- Gap: Up > 5%
- Price: $0.50 - $10

This should return 5-20 candidates on an active day.

### Step 2: For Each Candidate, Analyze (8:00-9:00 AM)

For each stock that passes the screener:

**A. Check the fundamentals:**
| Metric | Ideal | Why |
|--------|-------|-----|
| Float | < 5M | Easier to move |
| Market Cap | < $50M | More volatile |
| Sector | Biotech/Pharma | News-driven |
| Short Float | > 10% | Squeeze potential |

**B. Check for news:**
- Look on Finviz news section
- Check if there's a PR/catalyst (partnership, FDA, earnings)
- If unusual premarket activity but NO news yet, keep watching - news might drop

**C. Analyze premarket price action (use Yahoo Finance API):**
```
https://query1.finance.yahoo.com/v8/finance/chart/TICKER?interval=1m&range=1d&includePrePost=true
```

Look for:
| Signal | Bullish | Bearish |
|--------|---------|---------|
| Premarket trend | Higher lows, building | Spike then dump |
| Volume pattern | Increasing into open | Fading |
| Price vs news time | Moving before/after news | No reaction to news |

**D. Capture chart (using browse):**
```bash
browse tab.new "https://www.tradingview.com/chart/?symbol=TICKER"
browse wait 3
browse screenshot
cp /tmp/browse-snap-*.png log/YYYY-MM-DD/TICKER-HHMM.png
```

Link in daily log with `![TICKER](TICKER-HHMM.png)`.

### Step 3: Build Watchlist (9:00-9:30 AM)

Rank candidates by conviction:

**A-Grade (High conviction):**
- Low float (< 2M)
- Fresh news catalyst
- Premarket volume > 10x average
- Price holding gains or building

**B-Grade (Medium conviction):**
- Low float (< 5M)
- News or unusual activity
- Some premarket volume

**C-Grade (Watch only):**
- Meets basic criteria but something off
- No clear catalyst
- Choppy premarket action

### Step 4: Trade Decision (9:30 AM)

At market open:
- Focus on A-Grade candidates first
- Watch the first 1-2 minutes for confirmation
- Look for: high volume, price holding or pushing higher
- Avoid: immediate dump on open, no follow-through

### Analysis Template

When analyzing a stock, format it like this:

```
## [TICKER] - [Date]

**Setup:**
- Float: X
- Market Cap: $X
- Sector: X
- Previous Close: $X
- Premarket High: $X (+X%)

**Catalyst:**
- [News headline and time]

**Premarket Action:**
| Time | Price | Volume | Notes |
|------|-------|--------|-------|
| 4:00 AM | $X | X | First trade |
| 8:00 AM | $X | X | News released |
| 9:00 AM | $X | X | Ramping into open |

**Grade:** A/B/C
**Decision:** Buy / Watch / Skip
**Reason:** [Why]
```

### Key Insight: Early Movers

Stocks often move BEFORE official news (see SXTP example - spiked to +60% at 4:50 AM, news came at 8:06 AM). Watch for:
- Unusual premarket volume with no apparent news
- Multiple spikes and recoveries (accumulation)
- Price holding above previous close despite volatility

This could indicate news is coming. Monitor closely.

## Resources

- ~~[My Screener](https://elite.finviz.com/screener.ashx?v=150&f=cap_microunder,sh_float_u100,sh_price_u10,sh_relvol_o10,ta_change_u20&ft=4&o=-change)~~ - **Free trial expired, don't use Finviz Elite**
- [After-Hours Gainers (TradingView)](https://www.tradingview.com/markets/stocks-usa/market-movers-after-hours-gainers/) - Shows stocks gaining in after-hours trading
- https://finviz.com
- https://www.financialdatasets.ai/ (account available but no credits yet. for now yahoo works)

### Yahoo Finance API (Free)

Free historical stock data via undocumented API:

```
https://query1.finance.yahoo.com/v8/finance/chart/TICKER?period1=START&period2=END&interval=INTERVAL
```

**Parameters:**
- `TICKER`: Stock symbol (e.g., AEHL)
- `period1` / `period2`: Unix timestamps for date range
- `interval`: See table below

**Alternative syntax (for recent data):**
```
https://query1.finance.yahoo.com/v8/finance/chart/TICKER?interval=INTERVAL&range=RANGE
```

**Available intervals and ranges:**

| Interval | Max Range | Notes |
|----------|-----------|-------|
| `1m` | `1d` | 1-minute bars, last trading day only |
| `5m` | `5d` | 5-minute bars, last 5 days |
| `15m` | ~1 month | 15-minute bars |
| `30m` | ~1 month | 30-minute bars |
| `1h` | ~2 years | Hourly bars |
| `1d` | Full history | Daily OHLCV (most useful for backtesting) |
| `1wk` | Full history | Weekly bars |
| `1mo` | Full history | Monthly bars |

**Returns JSON with:**
- Open, High, Low, Close, Volume (OHLCV)
- Timestamps (Unix)

**Metadata included in response:**
- `regularMarketPrice`: Current price
- `fiftyTwoWeekHigh` / `fiftyTwoWeekLow`: 52-week range
- `regularMarketVolume`: Today's volume
- `regularMarketDayHigh` / `regularMarketDayLow`: Today's range
- `longName`: Full company name
- `exchangeName`: Exchange (e.g., NCM = NasdaqCM)
- `currentTradingPeriod`: Pre-market, regular, post-market times

**Example (daily data for specific dates):**
```
https://query1.finance.yahoo.com/v8/finance/chart/AEHL?period1=1743638400&period2=1744502400&interval=1d
```

**Example (5-min intraday, last 5 days):**
```
https://query1.finance.yahoo.com/v8/finance/chart/AEHL?interval=5m&range=5d
```

**Example (with pre-market and post-market data):**
```
https://query1.finance.yahoo.com/v8/finance/chart/AEHL?interval=1m&range=1d&includePrePost=true
```

**Trading periods (EST):**
- Pre-market: 4:00 AM - 9:30 AM
- Regular: 9:30 AM - 4:00 PM
- Post-market: 4:00 PM - 8:00 PM

**Note:** Some endpoints (v7/quote, v10/quoteSummary) require authentication.

### TradingView Screener API (Free)

Undocumented API for scanning the entire US stock market. No API key needed. Can filter by sector, market cap, float, volume, and extended hours data. Python package available: `pip install tradingview-screener`.

- [tradingview-screener PyPI](https://pypi.org/project/tradingview-screener/)
- [GitHub](https://github.com/shner-elmo/TradingView-Screener)
- [All available fields](https://shner-elmo.github.io/TradingView-Screener/fields/stocks.html)
- [Pre-built screeners](https://shner-elmo.github.io/TradingView-Screener/screeners/stocks/america.html) (includes `postmarket_gainers`, `premarket_gainers`, etc.)

**Key fields for our strategy:**

| Field | Description | Timeframes |
|-------|-------------|------------|
| `relative_volume_intraday\|5` | Volume vs same time-of-day average (5m) | Best for detecting unusual activity |
| `volume\|5` | Current 5-min bar volume | `\|1`, `\|5`, `\|15`, `\|30`, `\|60` |
| `volume_change\|5` | Volume change % from previous bar | Same timeframes |
| `average_volume_10d_calc\|5` | Average 5-min volume (10-day) | Same timeframes |
| `postmarket_volume` | Post-market volume | Daily only |
| `postmarket_change` | Post-market change % | Daily only |
| `premarket_volume` | Pre-market volume | Daily only |
| `premarket_change` | Pre-market change % | Daily only |
| `float_shares_outstanding` | Shares float | — |
| `market_cap_basic` | Market cap | — |
| `sector` | e.g., "Health Technology" | — |
| `industry` | e.g., "Biotechnology", "Pharmaceuticals: Major" | — |

**Biotech volume spike screener (during regular hours):**

```bash
curl -s -X POST "https://scanner.tradingview.com/america/scan" \
  -H "Content-Type: application/json" \
  -d '{
    "columns": ["name", "close", "volume|5", "average_volume_10d_calc|5", "relative_volume_10d_calc|5", "relative_volume_intraday|5", "volume_change|5", "change", "sector", "industry", "market_cap_basic"],
    "filter": [
      {"left": "relative_volume_intraday|5", "operation": "greater", "right": 10},
      {"left": "market_cap_basic", "operation": "in_range", "right": [0, 100000000]},
      {"left": "close", "operation": "in_range", "right": [0.5, 10]},
      {"left": "sector", "operation": "equal", "right": "Health Technology"},
      {"left": "volume|5", "operation": "greater", "right": 5000}
    ],
    "sort": {"sortBy": "relative_volume_intraday|5", "sortOrder": "desc"},
    "markets": ["america"],
    "symbols": {"query": {"types": ["stock"]}},
    "options": {"lang": "en"},
    "range": [0, 20]
  }'
```

**Key insight:** `relative_volume_intraday|5` compares the current 5-min bar to what's typical for that specific time of day (not the daily average). This avoids false positives from normal open/close volume spikes. Use `volume|5 > 5000` as absolute floor to filter out noise from ultra-thin stocks.
