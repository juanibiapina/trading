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
  | Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
  |--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
  | TICK   | [TV](https://www.tradingview.com/chart/?symbol=TICK) | $X | +X% | +X% | $X | +X% | XK | XK | Xx | XM | Industry |
  ```

### Yahoo Finance Data

For price history and AH price action data, use the helper scripts:

```bash
python3 scripts/check-prices.py --ah-history TICKER1 TICKER2 ...
python3 scripts/yahoo-fetch.py TICKER --interval 5m --range 2d --prepost
```

Do NOT use raw `curl` to Yahoo Finance (it fails without the User-Agent header that these scripts handle).

### 4. Paper Trade Decisions

Read the existing log to see which tickers were already found in previous scans today.

For each **new** candidate (not in prior scans), evaluate against the entry criteria from the trading plan:
- Any sector — do NOT skip stocks for being outside biotech/pharma. The "non-biotech 0/6" observation in Day Trading.md is a hypothesis under investigation, not a filter. Note the sector for pattern tracking.
- Float < 10M ideal
- Has a clear catalyst — for every stock with AH change >10%, do a structured catalyst search:
  1. **Earnings**: check if the company reported earnings today (Yahoo Finance or search "[TICKER] earnings"). Earnings released after close are the most common AH catalyst and the most commonly missed.
  2. **Press releases**: search GlobeNewswire, PRNewswire, or BusinessWire for same-day releases (search "[TICKER] press release" or "[company name] announcement"). PRs often drop at exactly 4:00-4:05 PM ET and may not appear in general news searches immediately.
  3. **SEC filings**: check for 8-K filings (material events) on the same day.
  4. If none of the above finds a catalyst, THEN note "no catalyst found" as a skip reason.
  **Search budget:** Steps 1-3 should take at most 4 websearch calls per ticker. If no catalyst is found after 4 searches, stop and record "no catalyst found." Do not try additional search providers, alternative query phrasings, or `websearch extract` on financial sites (Finviz, Benzinga, MarketBeat return JS errors). More searches rarely uncover what 4 targeted searches missed.
- Volume not fading, first day of unusual activity
- Note sector and characteristics for pattern tracking (observations in Day Trading.md are NOT skip criteria)

**Learning phase default:** During the learning phase (see Day Trading.md), the purpose of paper trades is data collection. **Do not enter paper trades before the 23:00 CET scan (5:00 PM ET).** The 22:00 and 22:30 scans are for observation only — track how candidates behave but do not enter. At 23:00+ CET, if at least one candidate has float <10M and AH change >10% in at least 2 after-hours scans (22:00+ CET — regular session appearances don't count toward this requirement), paper trade the best available candidate. When choosing among candidates, prefer those showing a build or hold AH pattern over those that spiked early and are now fading from their peak. Document concerns (extension, weak catalyst, no catalyst on ultra-low float) but enter anyway. A paper trade with noted concerns generates data; a skip generates nothing. Reserve "skip all" for nights when NO candidate sustains >10% AH across multiple scans.

**Regular session caution (21:30 CET / before 4:00 PM ET):** If this scan is running before AH opens, do NOT enter paper trades yet. Flag candidates as "Watch — pending AH confirmation" in the evaluation notes. Only enter a paper trade if the stock reappears in a subsequent AH scan (22:00+ CET) with sustained momentum. Stocks that spike intraday but don't carry into AH tend to fade (e.g., SPRC -18.6%, AEMD -4.6% on March 12).

If a candidate passes (and it's an AH scan), add a paper trade entry to the `## Paper Trades` table:
- Entry Price = current AH price
- Shares = ~€100 / entry price (round down)
- Reason = brief justification

If a candidate fails, note briefly why in the scan section (e.g., "Skip: no catalyst", "Skip: float too high").

For candidates already seen in prior scans, note any significant changes (price movement, volume increase/decrease). **If a prior candidate was skipped for "no catalyst" and still shows >10% AH change, re-run the structured catalyst search** — don't just repeat the prior skip. Press releases and news articles frequently appear 15-30 minutes after AH opens (4:00 PM ET), so catalysts often become findable at the 22:30 or 23:00 scans that weren't available at 22:00.

### 5. Commit

```bash
git add log/
git commit -m "post-market scan YYYY-MM-DD HH:MM CET"
git push
```
