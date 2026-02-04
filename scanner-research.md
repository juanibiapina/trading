# Custom Scanner with Polygon/Massive API — Investigation

## Summary

We can build a custom after-hours scanner using the Polygon.io (now Massive.com) API. The key endpoint is **Snapshot - All Tickers**, which returns the entire US stock market state in a single API call — including extended hours data. We'd poll this every 60 seconds during after-hours, filter for biotech micro-caps with unusual activity, and send notifications.

## API: Key Endpoints

### 1. Full Market Snapshot (the scanner core)
```
GET /v2/snapshot/locale/us/markets/stocks/tickers
```
- Returns **10,000+ tickers** in a single response
- Each ticker includes:
  - `day` — today's OHLCV bar (updates during extended hours)
  - `min` — most recent minute bar
  - `prevDay` — previous day's OHLCV
  - `todaysChange` / `todaysChangePerc` — % change from prev close
  - `lastTrade` — most recent trade (price, size, timestamp)
  - `lastQuote` — most recent bid/ask
  - `updated` — last update timestamp
- **Data starts populating at 4:00 AM EST** (premarket), available through 8:00 PM EST (after-hours)
- Cleared daily at 3:30 AM EST

### 2. Top Market Movers
```
GET /v2/snapshot/locale/us/markets/stocks/{direction}
```
- `direction` = `gainers` or `losers`
- Returns top 20 gainers/losers (min 10,000 volume)
- Quick check, but limited to 20 results

### 3. Ticker Overview (for reference data)
```
GET /v3/reference/tickers/{ticker}
```
- Returns: `market_cap`, `sic_code`, `sic_description`, `share_class_shares_outstanding`, `weighted_shares_outstanding`
- Updated daily from SEC filings
- **SIC codes for biotech/pharma:** 2833, 2834, 2835, 2836, 8731

### 4. List All Tickers (for building reference database)
```
GET /v3/reference/tickers?market=stocks&active=true&limit=1000
```
- Paginated, get all active stock tickers
- Use to build a local cache of biotech tickers + their float/market cap

## Pricing

| Plan | Price | Snapshot Data | Rate Limit | Real-time |
|------|-------|---------------|------------|-----------|
| **Free (Basic)** | $0/mo | 15-min delayed | 5 calls/min | ❌ |
| **Stocks Starter** | $29/mo | 15-min delayed | Unlimited REST | ❌ |
| **Stocks Developer** | ~$79/mo | Real-time | Unlimited REST + WebSocket | ✅ |
| **Stocks Advanced** | ~$199/mo | Real-time | Unlimited | ✅ |

**Key finding:** The snapshot endpoint returns **15-min delayed data** on all plans except Developer and above. Free tier gives us 5 calls/minute.

## The 15-Minute Delay Problem

For the free/Starter tier, snapshot data is 15 minutes delayed. But there's a nuance for after-hours:

- After-hours trading is **slow and thin** — a micro-cap might get its first AH trade at 4:05 PM, then nothing for 10-20 minutes
- A 15-minute delay still catches stocks that are building momentum over hours (4 PM → 8 PM)
- For our strategy (AH → hold overnight → sell in premarket), being 15 min late on detection in a 4-hour window is fine
- We don't need to be first — we need to be before the premarket crowd discovers it

**Conclusion: The free tier (5 calls/min, 15-min delayed) is probably sufficient to start.** If it works, we upgrade to Developer ($79/mo) for real-time.

## Architecture

### Phase 1: Simple Polling Scanner (Free Tier)

```
Every 60 seconds during AH (22:00-02:00 Berlin / 4-8 PM ET):
  1. GET /v2/snapshot/locale/us/markets/stocks/tickers
  2. Filter response for:
     - todaysChangePerc > 5%
     - day.volume > 10,000
     - ticker in biotech_watchlist (pre-built from reference data)
  3. Compare with previous scan:
     - NEW tickers appearing = potential alert
     - Volume increasing rapidly = momentum building
  4. Alert via Telegram/desktop notification
```

### Phase 2: Reference Data Cache (run once daily)

```
Before AH session starts:
  1. GET /v3/reference/tickers (paginated, all stocks)
  2. For each ticker, check sic_code in [2833, 2834, 2835, 2836, 8731]
  3. Also filter: market_cap < 100M, share_class_shares_outstanding exists
  4. Save to local JSON: {ticker, name, sic_code, market_cap, shares_outstanding}
  
This gives us ~500-1000 biotech tickers to watch
```

### Phase 3: Smart Alerts

```
Alert when:
  - Biotech ticker with >10% change AND >50,000 AH volume
  - Volume spike: current scan volume >> previous scan volume
  - New entrant: ticker wasn't moving before, now >5% change
  
Alert contains:
  - Ticker, price, % change, volume
  - Previous close for context
  - Link to news search
```

## What We Can't Get from Polygon Free Tier

| Data | Available? | Workaround |
|------|-----------|------------|
| Float (shares in public hands) | ❌ Not directly | Use `shares_outstanding` as proxy, or get float from Yahoo Finance API |
| Sector/Industry | ✅ Via SIC code | Map SIC codes to biotech |
| Real-time prices | ❌ (15-min delay) | Sufficient for AH strategy; upgrade to $79/mo if needed |
| News/catalysts | ❌ | Combine with Finviz news page or free news API |
| Short interest | ❌ | Get from Finviz or other source |

## Implementation Plan

### Step 1: Get API key
- Sign up at polygon.io (or massive.com)
- Free tier, no credit card needed

### Step 2: Build reference database
- Script to fetch all biotech tickers
- Store: ticker, name, sic_code, market_cap, shares_outstanding
- Run once, update weekly

### Step 3: Build scanner script
- Python script using `requests` (or `massive-api-client` / `polygon` package)
- Polls full market snapshot every 60 seconds
- Filters against biotech reference list
- Computes: % change, volume, volume delta from previous scan
- Outputs ranked list of movers

### Step 4: Add notifications
- Desktop notification (macOS `osascript`)
- Optional: Telegram bot for phone alerts

### Step 5: Integrate with trading workflow
- Scanner output feeds into morning analysis log
- Auto-generate candidate analysis template

## Tech Stack

- Python 3 (already have)
- `requests` or `massive-api-client` (`pip install massive-api-client`)
- `schedule` or simple `while True` loop with `time.sleep(60)`
- Local JSON file for biotech reference data
- macOS notifications or Telegram bot for alerts

## Estimated Build Time

| Component | Time |
|-----------|------|
| API signup + test calls | 15 min |
| Reference data builder | 30 min |
| Scanner core (poll + filter) | 1 hour |
| Alert system | 30 min |
| Testing during AH session | 1 evening |
| **Total** | **~3 hours** |

## Next Steps

1. **Sign up** for Polygon.io/Massive.com free API key
2. **Test** the snapshot endpoint with a simple curl call
3. **Build** the scanner
4. **Test** tonight during after-hours (22:00-02:00 Berlin)
