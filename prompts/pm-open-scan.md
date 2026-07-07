Run a **log-only** premarket-open scan for extreme overnight gappers that the
after-hours scanner structurally cannot see, and record each one's live price
path + liquidity. **This pulse places NO orders and changes no trading logic.**
It exists to accumulate evidence for Initiative 6 (catch the +300-600% runners):
are holdable PM-only gappers (CIIT +140%, GLXG +343%) frequent enough in real
time to justify piloting hypothetical entries?

See `STRATEGY_ROADMAP.md` Initiative 6 and `INIT6_EXTREME_MOVERS.md` for context.
The AH->PM scanner (`post-market-scan.md`) only sees stocks with an after-hours
footprint. The biggest raw morning movers keep being **PM-only gappers**: flat or
down in after-hours, exploding only after 04:00 ET on overnight news. This pulse
watches that blind spot.

## Data Sources

- **Discovery (whole-market PM gainers):** `python3 scripts/scan.py --all` —
  during premarket it auto-detects the session and screens `premarket_change` /
  `premarket_volume` across all symbols. VRatio here is a first-pass signal.
- **Real premarket price-path + liquidity:** `node scripts/broker.js bars SYM
  --tf 5Min --feed sip`. SIP consolidated feed gives real `vol`, `vwap`, and
  `trades` per 5-min bar. Free-tier SIP blocks only the most recent ~15 min, so a
  scan at ~05:00 ET reads the 04:00-04:45 ramp cleanly. **Bar timestamps are
  UTC** = ET + 4 (EDT) or + 5 (EST); 04:00 ET = `08:00Z` (EDT).
- **Do NOT trust Yahoo for premarket volume** — it reports `vol=0` for every
  ticker in extended hours, which is exactly why this pulse uses SIP.

## Steps

### 1. Setup

- Run `TZ=America/New_York date` to get the current ET time. This pulse is meant
  to run ~04:00-05:00 ET (premarket). If it is not premarket, run the scan
  anyway and note the session (still useful; classify whatever gappers exist).
- Set `TRACKER=log/pm-open-scan.csv` (create with the header row below if
  missing).
- Pull latest: `git stash && git pull --ff-only && git stash pop 2>/dev/null || true`

### 2. Discover PM gappers

```bash
python3 scripts/scan.py --all
```

Keep the candidates that look like **big overnight gappers**: PM Chg% high (focus
on the largest movers; there is no fixed cutoff, but prioritise anything >+50%,
and always classify at least the top 3 by PM Chg%). Skip obvious dupes of names
already holding as open positions.

### 3. Classify each gapper (price path + liquidity)

For each selected gapper, pull the real premarket tape:

```bash
node scripts/broker.js bars SYM --tf 5Min --feed sip
```

Read the bars from ~04:00 ET (`08:00Z` EDT) onward and determine:

- **AH footprint?** Did this stock move in after-hours last night? Check the
  prior night's `log/YYYY-MM-DD/log.md` scan sections (or note "unknown" if no
  log). A PM-only gapper has **no** AH footprint — that is the blind-spot class
  this pulse targets. Names that DID appear in last night's AH scan are already
  covered by `post-market-scan.md`; tag them `ah-detected` and deprioritise.
- **PM high + time** (ET) and **ramp-start time** (first 5-min bar with real
  volume, i.e. thousands of trades / hundreds of K+ shares).
- **Liquidity:** peak `vol` and `trades` per 5-min bar during the elevated
  period. Real = millions of shares and thousands of trades per bar. Thin = a
  handful of trades / tiny volume (a single illiquid tick).
- **Classification** (mechanical, mirrors the census heuristic):
  - `holdable` — price held within ~20% of its PM high across **>=2 consecutive
    5-min bars** on real, sustained volume (rising/steady `vol` and `trades`). A
    multi-hour exit window existed. (CIIT, GLXG, SUGP profile.)
  - `uninvestable` — peaked in the first 1-2 bars then decayed straight down
    below the mid-point of the gap, never recovering. (TDIC, MBRX profile.)
  - `thin` — no real volume (single-tick print, `trades` in the low tens or
    less); not fillable regardless of price path. (CUPR profile.)

### 4. Log to the tracker (NO orders)

Create `log/pm-open-scan.csv` with this header if it does not exist, then append
one row per classified gapper:

```
date,ticker,pm_gap_pct,ah_footprint,pm_high,pm_high_time_et,ramp_start_et,peak_vol_per_bar,peak_trades_per_bar,classification,catalyst,notes
```

- `date` = US trading date (YYYY-MM-DD)
- `ah_footprint` = `none` (PM-only gapper), `ah-detected`, or `unknown`
- `pm_gap_pct` = PM Chg% at scan time
- `peak_vol_per_bar` / `peak_trades_per_bar` = the busiest 5-min bar's `vol` /
  `trades` during the ramp
- `catalyst` = one-line catalyst if quickly found (optional; do not spend more
  than 1-2 searches — this is a log-only observation pulse), else `-`
- `notes` = short price-path description (e.g. "held $1.00-1.10 across 6 bars")

**Do not submit any Alpaca order. Do not touch `OPEN_POSITIONS.md`.** This pulse
is instrumentation only.

### 5. Commit

```bash
git add log/pm-open-scan.csv
git commit -m "pm-open scan YYYY-MM-DD: N gappers logged"
git push
```

### 6. Report

One line: how many PM-only gappers were found and how many classified holdable
vs uninvestable vs thin. Over several weeks this tally decides whether to propose
a hypothetical-entry pilot (rollout step 3) to Juan.
