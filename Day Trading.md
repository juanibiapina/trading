---
tags:
  - project
---

# Day Trading

## Trading Plan

### Goal

Catch momentum spikes by entering in after-hours and exiting in premarket before the regular market dump. Any sector — the strategy learns what works through retrospective analysis.

**Key Insight (from BATL trade Jan 2026):** Momentum stocks often peak in premarket, then dump at open. The biggest gains happen *before* regular trading begins.

### The Pattern

1. Stock spikes in after-hours on catalyst (news, squeeze, etc.)
2. Momentum builds overnight as traders discover it
3. FOMO peaks in premarket → price explodes
4. Regular market opens → dump as early buyers take profits

**Pattern confirmed 3/3 times in W05:** Exit in premarket, NOT at open.

### Schedule

| Session | US Eastern (ET) | Berlin (CET) | Action |
|---------|-----------------|--------------|--------|
| After-hours | 4:00 PM - 8:00 PM | 22:00 - 02:00 | **Screen at ~22:15**, buy candidates |
| Overnight | - | - | Hold position |
| Premarket | 4:00 AM - 9:30 AM | 10:00 - 15:30 | Watch for peak, **exit before open** |
| Regular | 9:30 AM - 4:00 PM | 15:30 - 22:00 | (Avoid - this is when dumps happen) |

### Rules

**Position Management:**
- One trade per day, one position at a time
- Stop after winning or losing
- ~100 euros per trade (learning phase)
- Set premarket exit alarm + order right after entry (MNDR W08 miss: forgot to sell premarket, loss expanded)
- Trade on PC

**Learning Phase (started W11 2026):**

The strategy is in a learning phase because we don't yet know what makes a winning trade. Earlier we restricted to biotech-only after going 0/6 on non-biotech trades, but that logic is flawed — restricting to *any* single sector would cut out losses. It doesn't prove biotech is special. The real problem may be that the overall strategy can't yet distinguish good trades from bad ones, and sector filtering just masks that.

**The baseline requirement:** before we can fine-tune any entry rules (sector, price, catalyst type), we need to prove the scanner can even *detect* the winners. Every trading day produces at least one stock that fits the AH→premarket pattern. If our evening scanner consistently misses those stocks, no amount of filtering will make the strategy work. So the first goal is:

1. **Detect** — Can we find yesterday's winner in retrospect? (morning retrospective, Step 0)
2. **Diagnose** — Would our evening scanner have caught it? If not, why?
3. **Fix** — Improve the scanner until it reliably catches winners (target: >80% detection rate)
4. **Refine** — Only then do entry rules (sector, catalyst, price) matter — because now we're choosing among detected winners

Until the baseline is met, we paper trade and focus entirely on scanner accuracy:
- No hard sector or entry-price restrictions — let the data reveal what works
- Every morning, run the retrospective (Step 0) — this is the most important part of the workflow
- Track detection rate weekly: what % of morning winners were detectable the previous evening?

**Observations (from Jan-Feb 2026):**
These are patterns noticed so far, NOT hard rules. They may evolve as more data comes in:
- *Biotech catalysts worked well:* VIVS (+65%), ABP (win) — binary catalysts (FDA, partnerships) drive strong overnight momentum
- *No catalyst = no follow-through:* IFBD had 77x volume but no news → faded. MNDR had 6.8x AH volume, no news, lost -16.5%
- *Chasing extended stocks is risky:* PZG entered at +97%, SER at +69%, both lost. But ABP at +68% won with strong catalyst stack
- *Consolidation entries worked:* VIVS entered after spike consolidated, won +65%
- *FOMO = worst entries:* Anxiety/rushing led to buying at literal tops
- *Non-biotech 0/6:* DRCT, XPON, PZG, IFBD, MNDR, TMDE all lost — but unclear if sector was the cause or other factors (no catalyst, chasing, FOMO)

### Catalyst Ranking

| Tier | Catalyst Type | Example | Result |
|------|---------------|---------|--------|
| A | Operational improvement | BATL gas agreement | +29% |
| A | Partnership/distribution | VIVS Asia deal | +65% |
| B | FDA milestone | SER IND clearance | -18% (faded) |
| C | Analyst price target | ABOS $7 target | Skipped |
| D | Financing/dilution | AGMH equity line | -5% (avoid) |

### Examples (Jan 2026)

| Stock | Entry | PM Peak | After Open | Lesson |
|-------|-------|---------|------------|--------|
| BATL | $1.86 | $7.00 (+276%) | $2.55 (-64%) | Sold at $2.40, missed PM peak |
| MRNO | $2.48 | ~$4.10 | $2.31 (-44%) | Sold at $3.80 PM - perfect exit |
| VIVS | $2.70 | $4.48 | - | Sold at $4.48 PM - perfect exit |

### Risks

- Extended hours have wider spreads and lower liquidity
- **CRITICAL: Stop losses DO NOT execute in extended hours** - PZG (Jan 29) had SL at $2.49, stock crashed to $1.70, SL never triggered. Accept full loss potential or size smaller.
- Can gap against you overnight
- Need broker that supports extended hours trading

### Baseline Status

**Detection rate:** not yet measured (start tracking W11 2026)
**Target:** >80% of morning winners should have been detectable at evening screening time
**Status:** Learning — collecting data through daily retrospectives

Once the baseline is met (scanner reliably detects winners), the strategy graduates from learning phase to live trading with data-driven entry rules.

### Emerging Patterns (from retrospectives)

_This section gets updated as retrospective analyses reveal what ideal trades have in common. After 2 weeks of daily retrospectives (target: W13 2026), review all findings and promote consistent patterns to strategy rules._

**Patterns confirmed so far:**
- (none yet — start collecting from W11 retrospectives)

**Patterns under investigation:**
- Strong catalyst presence (seen in BATL, VIVS, ABP wins)
- AH consolidation before PM continuation
- Volume sustainability through overnight

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

- **Scanner detection rate (THE baseline):** what % of morning winners were detectable at evening screening time? (target: >80%)
- Win rate (target: >50%) — only meaningful after baseline is met
- Average win vs average loss (target: wins > losses)
- Pattern consistency: are the same characteristics appearing in ideal trades?

---

## Morning Analysis Workflow

Run this workflow between 7:00-9:30 AM ET. Document in `log/YYYY-MM-DD/log.md`.

### Step 0: Retrospective — Find Today's Winners (7:00-7:30 AM)

**This is the most important step.** Before looking at today's candidates, independently find what IS exploding in premarket RIGHT NOW. Don't look at last night's watchlist — search fresh. There is almost always a stock that spiked in AH and is peaking in premarket this morning.

**Why this matters:**
The retrospective is a diagnostic tool for the evening scanner. If a stock is a clear winner this morning but wasn't on our radar last night, our scanner is broken. The strategy can only work if the scanner reliably catches winners. The baseline requirement is: **every morning winner should have been detectable the previous evening.**

**How to find it:**
1. Search broadly for stocks exploding in premarket RIGHT NOW (any sector):
   - Premarket gainers lists, volume leaders, unusual activity
   - Use Yahoo Finance API with `includePrePost=true` to check AH + PM action
   - Look for the pattern: spiked in AH yesterday → still running or peaking in PM now
2. Identify the best one — the stock with the clearest AH entry → premarket peak pattern
3. Then go back and check: **was this stock visible in after-hours last night?** What did it look like at screening time (~22:15 CET)?

**Document it:**
```
## Retrospective: [Date]

**Today's Winner:** [TICKER]
- Sector: [sector]
- Previous Close: $X
- AH action last night: $X at [time] (+X% from close), volume Xm
- Premarket now: $X (+X% from close)
- Hypothetical P&L (AH entry → PM peak): +X%

**Catalyst:**
- [What news/event drove it, and when did it drop]

**Scanner Diagnostic:**
- Was this detectable at screening time (~22:15 CET)? YES / NO
- If YES: what did it look like? (price, volume, % gain at that time)
- If NO: why not? (news came later, AH move started after midnight, no volume yet, etc.)
- **Scanner gap:** [what would need to change to catch this]

**Stock characteristics:**
- Float: X
- Market Cap: $X
- AH volume vs normal: Xx
- Price action pattern: [consolidation? steady climb? spike and hold?]
```

**This builds two things:**
1. A library of "what winning trades actually look like" → evolves the strategy
2. A diagnostic log for the scanner → if it keeps missing winners, we know exactly what to fix

**After 2 weeks of daily retrospectives (target: W13 2026),** review all findings:
- What patterns do winners share?
- How often did the scanner catch them? What's the detection rate?
- What scanner changes would improve detection?

### Step 1: Screen for Candidates (7:00-8:00 AM)

Use Finviz screener with these filters:
- Market Cap: < $100M (micro-cap)
- Float: < 10M (low float = bigger moves)
- Relative Volume: > 2 (unusual activity)
- Gap: Up > 5%
- Price: $0.50 - $10
- **No sector filter** — let retrospective analysis guide what sectors work

This should return 5-20 candidates on an active day.

### Step 2: For Each Candidate, Analyze (8:00-9:00 AM)

For each stock that passes the screener:

**A. Check the fundamentals:**
| Metric | Ideal | Why |
|--------|-------|-----|
| Float | < 5M | Easier to move |
| Market Cap | < $50M | More volatile |
| Sector | Any (note it for pattern tracking) | Learning phase |
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
