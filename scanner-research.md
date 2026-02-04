# Stock Scanner Research

## The Problem

TradingView's after-hours gainers page shows stocks that have *already* moved significantly. By the time a stock appears on that page, much of the initial move has happened. For the AH→PM strategy, we need to catch stocks **as they start moving** in after-hours, not after the move is established.

## What We Need

| Requirement | Why |
|-------------|-----|
| **Real-time AH/PM coverage** (4:00 PM - 9:30 AM ET) | Our strategy lives in extended hours |
| **Volume spike detection** | First sign of unusual activity |
| **Low float / micro-cap filtering** | Biotech micro-caps are our targets |
| **News/catalyst integration** | Need to verify the catalyst quickly |
| **Price: ideally <$30/mo** | Trading €100 positions, can't justify $200/mo tools |
| **Alerts/notifications** | Need to be notified, not staring at screen all night |

---

## Scanner Options Ranked

### Tier 1: Best Fit (Recommended)

#### 1. 🏆 MOMO Pro (mometic.com) — $27/mo (free trial available)
- **Full premarket AND after-hours coverage** (4:00 AM - 8:00 PM ET)
- Real-time scanning with sub-second updates
- Filter by: float, price change %, unusual volume, VWAP delta
- Conditional alerts with sound notifications (e.g., "Price change > 3% AND Low Float < 30M AND Unusual Vol > 50%")
- TradingView integration
- Works on any device (web-based PWA)
- **Push notifications** for custom alert conditions
- Active subreddit: r/MOMOStockScanner
- **Why it's #1:** Purpose-built for exactly our use case — momentum scanning during all sessions including extended hours. Cheapest dedicated scanner. Users on Reddit confirm it catches moves early.

#### 2. Stock Titan Argus (stocktitan.net) — Free / $19.99-$89.99/mo
- Momentum scanner covering **premarket, regular, and after-hours**
- Filters: price range, market cap, float, volume, relative volume, 5-min delta %
- Automatically correlates price movements with news ("Why is this moving?")
- AI sentiment & impact scoring on news
- **Free tier:** 15-min delay (useless for our strategy)
- **Silver ($19.99/mo):** 30-sec delay (still not ideal)
- **Gold ($59.99/mo):** Real-time + full filters
- **Why it's good:** News correlation is killer — instantly tells you WHY something moved. But real-time requires Gold ($60/mo).

#### 3. Realtime Stock Screener App (iOS/Android) — Free / $19.99-$49.99/mo
- **Premarket (4:00 AM-9:30 AM), After-hours (4:15 PM-8:00 PM)**
- Low float stock list built-in (shares float < 5M)
- Real-time movers with news, charts, fundamentals
- Alerts and trade ideas
- App Store: 4.7/5 (717 ratings)
- **Why it's good:** Free tier works during extended hours with real-time data. Great for phone alerts when away from computer.

---

### Tier 2: Powerful but Expensive

#### 4. Trade Ideas — $89-$178/mo
- Industry gold standard for day trading scanners
- "Holly" AI assistant runs dozens of strategies
- 500+ filters including float, gap%, premarket volume
- Dedicated premarket and after-hours scanning
- Channel bar includes biotech-specific channels
- Backtesting included
- **Why not #1:** Very expensive ($89-$178/mo). Makes no sense for €100 positions. Also Windows-only desktop app with dated UI. But if you scale up position sizes, this becomes worth it.

#### 5. Benzinga Pro — ~$197/mo (14-day free trial)
- **Breaking news 5-15 min before Bloomberg/CNBC** — this is their killer feature
- Scanner integrated with news feed
- Filter news by: ticker, price range, float, market cap, sector
- Keyword filters like "Phase 1 approval", "FDA", "partnership"
- Audio squawk (live voice reading headlines)
- **Why it's interesting:** For catalyst-driven trading, getting news FIRST matters more than seeing price move first. A stock might not show on any scanner yet, but Benzinga shows the PR. However, $197/mo is too much for current position sizes.

#### 6. StocksToTrade — ~$179/mo
- All-in-one platform with scanner, charts, news
- Low-float and penny stock focused
- Alpha Scanner (AI-driven alerts)
- Good premarket scanning
- **Why not:** Expensive, overlaps with what we can do cheaper.

---

### Tier 3: DIY / Build Your Own

#### 7. 🔧 TradingView Screener Python API (tradingview-screener) — FREE
- Python package: `pip install tradingview-screener`
- Query TradingView's scanner API programmatically
- 3000+ fields, filter by market cap, relative volume, MACD, etc.
- Can run on a cron job every 1-5 minutes during AH/PM
- With TradingView account cookies: real-time streaming data
- **Extended hours columns available** in screener
- **Limitation:** Still uses TradingView's data, so same delay issue. But the advantage is we can **automate it** and add notification logic (Telegram, email, etc.).

#### 8. 🔧 Polygon.io / Massive.com API — Free tier / $29/mo (Stocks Starter)
- **Full tick-level data during pre-market and after-hours**
- WebSocket streaming for real-time trades and quotes (4:00 AM - 8:00 PM ET)
- REST API for snapshots of all tickers
- Free tier: 5 API calls/min, delayed data
- Starter ($29/mo): Real-time WebSocket, unlimited REST calls
- **Build a custom scanner:** Poll all stock snapshots every minute, compare volume to historical average, alert when unusual activity detected on biotech micro-caps
- Python client library available
- **Why it's interesting:** Full control. We define exactly what "unusual" means. Could detect first AH trades on a ticker that normally has zero AH volume.

#### 9. 🔧 Databento — $125 free credit, then usage-based (~$5-50/mo)
- Professional-grade real-time data from all 15 US exchanges
- Pre-market data from 4:00 AM ET
- Python client, blog post with exact scanner tutorial code
- Sub-millisecond latency (overkill for us, but data is great)
- Usage-based pricing: pay for what you consume
- **Best for:** If you want to build the fastest possible custom scanner

#### 10. 🔧 Yahoo Finance API (free, already in use) + Custom Script
- Already using this for chart analysis
- `includePrePost=true` gives extended hours data
- **Limitation:** Need to poll individual tickers (no "scan all" endpoint). Only useful for monitoring a watchlist, not discovering new movers.

#### 11. 🔧 UnusualVolumeDetector (GitHub) — FREE
- Open source Python script (github.com/SamPom100/UnusualVolumeDetector)
- Scans every ticker, gets 5 months volume history
- Alerts when volume exceeds 10 standard deviations from mean
- Could be adapted for AH monitoring
- **Limitation:** Uses batch API calls, not truly real-time. Good for end-of-day scanning.

---

## Comparison Matrix

| Scanner | AH Coverage | PM Coverage | Real-time | Alerts | Float Filter | News | Price/mo |
|---------|-------------|-------------|-----------|--------|--------------|------|----------|
| **MOMO Pro** | ✅ | ✅ | ✅ | ✅ Push | ✅ | ❌ | $27 |
| **Stock Titan Argus** | ✅ | ✅ | ✅ (Gold) | ✅ | ✅ | ✅ Auto | $60 |
| **RT Stock Screener App** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Free-$50 |
| **Trade Ideas** | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | $89-178 |
| **Benzinga Pro** | ❌ Scanner | ✅ | ✅ | ✅ Audio | ✅ | ✅✅✅ | $197 |
| **TradingView Python** | ✅ | ✅ | ⚠️ (cookies) | 🔧 Build | ✅ | ❌ | Free |
| **Polygon/Massive API** | ✅ | ✅ | ✅ ($29) | 🔧 Build | 🔧 Build | ❌ | Free-$29 |
| **Yahoo API** | ✅ | ✅ | ❌ (delayed) | 🔧 Build | ❌ | ❌ | Free |

---

## Recommended Strategy

### Quick Win (start tonight): MOMO Pro free trial
1. Sign up at mometic.com (free trial, no CC needed reportedly)
2. Set up a stream with these filters:
   - Price: $0.50 - $10
   - Float: < 10M
   - Unusual Volume: > 50%
   - Price Change: > 5%
3. Enable push notifications
4. Test during tonight's after-hours session (22:00-02:00 Berlin)

### Medium Term: Build custom scanner with Polygon/Massive API
1. Sign up for free tier at polygon.io/massive.com
2. Use their "Snapshot - All Tickers" endpoint to get real-time data for entire market
3. Build a Python script that:
   - Runs every 60 seconds during AH (4:00 PM - 8:00 PM ET)
   - Compares current volume to historical average
   - Filters: biotech/healthcare sector, market cap < $100M, float < 10M
   - Sends Telegram/push notification when anomaly detected
4. Upgrade to $29/mo Starter for real-time WebSocket if polling isn't fast enough

### Also Consider: Realtime Stock Screener App
- Install on phone as a backup/complement
- Free tier covers AH and PM
- Get alerts on phone even when away from computer

---

## Key Insight: News vs. Price Scanning

There are two fundamentally different approaches:

1. **Price/Volume scanning** (MOMO, Trade Ideas, TradingView): Detect the MOVE as it happens
2. **News scanning** (Benzinga Pro, Stock Titan): Detect the CATALYST before/as the move happens

For our strategy, **news scanning catches things even earlier** because:
- A PR drops at 4:05 PM → Benzinga shows it immediately
- First trades happen at 4:10 PM → Price scanners detect it
- Volume builds → TradingView AH page shows it at 4:30 PM

But news scanners are expensive ($197/mo for Benzinga). The sweet spot is **price/volume scanning** (MOMO at $27/mo or DIY) because:
- We still catch the move early enough (within 5-10 min of first trades)
- We don't need to be first — we need to be before the crowd
- The AH→PM strategy has hours of runway, not minutes
