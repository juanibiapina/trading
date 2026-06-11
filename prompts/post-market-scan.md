Run a post-market scan and update the daily log with results and paper trade decisions.

**Focus:** This prompt finds ENTRIES only. Position management (hold/sell decisions) is handled by `position-evaluation.md` which runs separately in premarket.

## Steps

### 1. Setup

- Run `date` to get the current time
- Determine the US trading date: if current CET time is before 06:00, the trading date is yesterday (CET). Otherwise it's today.
- Set `LOG_DIR=log/YYYY-MM-DD` and `LOG_FILE=log/YYYY-MM-DD/log.md` using the trading date
- Pull latest changes: `git stash && git pull --ff-only && git stash pop 2>/dev/null || true`

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
  4. If none of the above finds a catalyst, note "no catalyst found" — see "No-catalyst handling" below.
  **Search budget:** Steps 1-3 should take at most 4 websearch calls per ticker. If no catalyst is found after 4 searches, stop and record "no catalyst found." Do not try additional search providers, alternative query phrasings, or `websearch extract` on financial sites (Finviz, Benzinga, MarketBeat return JS errors). More searches rarely uncover what 4 targeted searches missed.
- Volume not fading, first day of unusual activity
- Note sector and characteristics for pattern tracking (observations in Day Trading.md are NOT skip criteria)

**Learning phase default:** During the learning phase (see Day Trading.md), the purpose of paper trades is data collection. **Do not enter paper trades before the 23:00 CET scan (5:00 PM ET).** The 22:00 and 22:30 scans are for observation only — track how candidates behave but do not enter. At 23:00+ CET, if at least one candidate has float <50M, AH change >10% in at least 2 after-hours scans (22:00+ CET — regular session appearances don't count toward this requirement), and Day% above -15%, paper trade the best available candidate. Skip dead-cat bounces: stocks that crashed >15% during regular session and bounce in AH are recovering from a sell-off, not building new momentum (3+ observations: all lost or went dead in PM). When choosing among candidates, prefer those showing a build or hold AH pattern over those that spiked early and are now fading from their peak. **Trajectory overrides catalyst when patterns clearly diverge:** if one candidate shows BUILD pattern and another shows SPIKE→FADE, prefer the BUILD candidate even if the BUILD candidate lacks a catalyst and the SPIKE→FADE has one. Early-peak-fading stocks are 0/7 for PM continuation regardless of catalyst quality (data: VCIG, TRNR, BNZI, CODX, plus 4 from May 11-13). BUILD patterns are 5/5 including no-catalyst winners (SNGX, PHGE ×2, AMST, NXTT). **AH peak timing matters, but trajectory dominates:** at later scans (00:00+ CET), compare each candidate's current price to their AH peak and peak TIME. Early-peaking stocks that are *also fading* are 0/6+ for PM continuation (OCG 16:35, CNET 16:45, FOXX 18:20→-15.7%, ANY 17:15). Stocks that peaked after 18:30 ET are 4/4 for PM follow-through (DXST 18:35, LNKS 18:50, WOK 19:05, TWAV 19:50). **However, a before-18:30 peak does NOT disqualify a candidate that is holding/building rather than fading:** CHAI (peak 17:20 ET) and MSW (peak 18:00 ET) both peaked before 18:30 yet held their base across scans and followed through (MSW +31% over entry at PM peak). Hold-vs-fade is the primary signal; absolute peak time is a secondary tiebreaker. At later scans, strongly prefer candidates still building or holding near their AH high; only treat an early peak as a disqualifier when the stock is *also* declining across scans. **"Holding" requires the current price to be within ~20% of the AH high (or making new highs) — a deep collapse that stabilizes at a much lower base is still a fade, not a hold.** CHAI made a *new* AH high at 17:20 and held within 20% of it; MSW was entered while still building toward its peak. By contrast, SKYQ (Jun 10) peaked +129% ($3.58) at 17:00 ET, collapsed -64% off that high, and "rebuilt" only to +46% ($2.28) — that low-rebuild base was misread as a CHAI-style hold and lost -27.6%. A rebuild to a base far below the AH high (>20% off), especially on a Grade-None macro/sector-beta name with no company catalyst, is a faded spike — skip it. **SPIKE→FADE-only nights:** If all qualifying candidates at entry time show SPIKE→FADE pattern (peaked before 17:30 ET and now declining), skip all rather than entering the 'least bad' option. SPIKE→FADE stocks are 0/10+ for PM continuation regardless of float, catalyst, or AH% — entering one still loses. A skip on a SPIKE→FADE-only night is not lost data; it's avoiding a predictable loss. Wait for nights with BUILD patterns. Reserve "skip all" also for nights when no candidate sustains >10% AH across multiple scans. **Entry extension ceiling:** Skip candidates with Entry Total% above +150% (total move from previous close). Extended entries leave no margin for overnight fade. Data: PRFX +439%→-28.8%, VCIG +194%→-7.9%, ATPC +154%→-14.1%, ANY +155%→-21.3% all lost; lower-extension entries (AMST +76%→+124%, NXTT +23%→+19%, DXST +57%→+75%) won. **If the only candidate at 23:00 exceeds 150%, wait for later scans (23:30, 00:00).** Late-building candidates often appear with better entry points — DXST emerged at 00:30 with +57% vs ANY at 23:00 with +155%. Only enter above 150% extension if it's past 00:00 CET and no lower-extension alternatives have appeared across all scans. **Ceiling-override watch (data collection):** When a candidate exceeds +150% Total% but shows a genuine BUILD-and-hold profile — made its AH high *after 17:00 ET*, is *holding within ~20% of that high* across ≥2 AH scans, and has *VRatio >5x* — still skip the actual entry, but flag it as **CEILING-OVERRIDE WATCH** in the evaluation notes and record a hypothetical entry (price + scan time). This collects the BUILD-vs-extension cases needed to decide whether the ceiling should become conditional, without risking capital. (Basis: CHAI Jun 8 +212%→held $2.8–3.4 base→PM +72% was skipped purely on the ceiling, while early-peak fades OCG/CNET/BGI correctly died.)

**No-catalyst handling (learning phase):** If structured search finds no catalyst, **enter with concern noted**. "No catalyst" is a concern to document, not a skip reason. Float is tracked for pattern analysis but is not a filter during learning phase. (Data: OCG 1.9M +14.9%, LNKS 633K +61%, PHGE 5.9M +19.3%, PHGE 7.4M +170% — all no-catalyst winners across different float ranges.)

**Regular session caution (21:30 CET / before 4:00 PM ET):** If this scan is running before AH opens, do NOT enter paper trades yet. Flag candidates as "Watch — pending AH confirmation" in the evaluation notes. Only enter a paper trade if the stock reappears in a subsequent AH scan (22:00+ CET) with sustained momentum. Stocks that spike intraday but don't carry into AH tend to fade (e.g., SPRC -18.6%, AEMD -4.6% on March 12).

If a candidate passes (and it's an AH scan), add a paper trade entry to the `## Paper Trades` table:
- Entry Price = current AH price
- Shares = ~€100 / entry price (round down)
- Catalyst Grade = A/B/C/D/None (see below)
- Reason = brief justification

**Catalyst Grading (determines hold strategy):**
| Grade | Type | Examples | Hold Strategy |
|-------|------|----------|---------------|
| **A** | Major operational | Acquisition, major partnership, breakthrough deal | Hold up to 5 days |
| **B** | Solid news | Earnings beat, FDA approval, contract win | Hold up to 2 days |
| **C** | Weak news | Financing, analyst upgrade, minor PR | Exit in premarket |
| **D** | Dilution | Stock offering, warrant exercise | Exit immediately |
| **None** | No catalyst found | Unknown driver | Exit at first opportunity |

**Also add the position to `OPEN_POSITIONS.md`** with the entry details and catalyst grade.

If a candidate fails, note briefly why in the scan section (e.g., "Skip: no catalyst", "Skip: float too high").

For candidates already seen in prior scans, note any significant changes (price movement, volume increase/decrease). **If a prior candidate was skipped for "no catalyst" and still shows >10% AH change, re-run the structured catalyst search** — don't just repeat the prior skip. Press releases and news articles frequently appear 15-30 minutes after AH opens (4:00 PM ET), so catalysts often become findable at the 22:30 or 23:00 scans that weren't available at 22:00.

### 5. Commit

```bash
git add log/
git commit -m "post-market scan YYYY-MM-DD HH:MM CET"
git push
```
