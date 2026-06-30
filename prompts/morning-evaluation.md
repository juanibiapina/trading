Run a morning evaluation of the overnight scanning session.

**Schedule awareness:** This prompt runs once in early premarket at 10:20 CET.

**Focus:** Find today's winner for baseline tracking and diagnose scanner effectiveness. This is a retrospective analysis prompt, NOT a position management prompt.

**Position management is separate:** Hold/sell decisions are handled by `position-evaluation.md` which runs at 10:30 and 14:30 CET. This prompt does NOT close positions.

**Primary goal on pulse 1: find today's winner and diagnose the scanner.** On pulses 2 and 3, the goal is to update prices, P&L, and any notable changes since pulse 1.

The most important question is: what stock IS exploding in premarket right now? There is almost always one. Find it first — independently, without looking at last night's watchlist — then check if our evening scanner would have caught it. This is the baseline test: if the scanner can't even detect the winners, no entry rules will make the strategy work. See "Learning Phase" in Day Trading.md for the full reasoning.

## Steps

### 1. Setup

- Run `date` to get the current time
- Determine yesterday's US trading date (the AH session we're evaluating)
- Set `LOG_FILE=log/YYYY-MM-DD/log.md` using that date
- Pull latest changes: `git stash && git pull --ff-only && git stash pop 2>/dev/null || true`
- **Get cumulative baseline** (pulse 1 only): Find the most recent previous log with baseline tracking and extract the counts:
  ```bash
  # Find most recent log with baseline tracking (excluding today)
  grep -l "Days tracked:" log/2026-*/log.md | sort | tail -1 | xargs grep -E "Days tracked:|Winners detected"
  ```
  Save these values — you'll increment them in Step 5.
- If this is **pulse 1**, do **not** read `LOG_FILE` yet. Step 2 must happen first.
- If this is **pulse 2 or 3**, read the existing log now so you can reuse pulse 1's winner, scanner diagnostic, and paper trades

### 2. Find Today's Winner (Pulse 1 only, or fallback if pulse 1 is missing)

**Pulse 1:** Do this BEFORE looking at last night's log. Search fresh for what is exploding in premarket right now.

**Pulse 2 and 3:** Skip this full step if pulse 1 already logged a winner and scanner diagnostic. Reuse the existing winner, then update only the current PM price, P&L, and any important follow-through changes.

Run a live premarket scan, then reconstruct the prior AH session with Yahoo history for the strongest PM names:

```bash
python3 scripts/scan.py --all --session premarket
python3 scripts/check-prices.py --ah-history TICKER1 TICKER2 ...
```

A forced `python3 scripts/scan.py --all --session afterhours` can still be logged as a secondary diagnostic, but do **not** rely on it as the primary retrospective source. Overnight TradingView postmarket fields often return 0 hits even when the live evening scans clearly found AH movers.

From the results, identify the **best AH→premarket trade** — the stock that:
- Spiked in after-hours yesterday
- Is still running or peaking in premarket now
- Would have given the best return if bought in AH and sold now

This is "today's winner." Document it with: sector, catalyst, float, AH entry price, current PM price, hypothetical P&L.

**Then** go back and read last night's log. Was this stock on our radar? This is the scanner diagnostic.

### Price Timeline Data

For AH and PM price timelines (5-min intervals), use these built-in modes:

```bash
# After-hours timeline (16:00-20:00 ET)
python3 scripts/check-prices.py --ah-history TICKER1 TICKER2 ...

# Premarket timeline (04:00-09:30 ET)
python3 scripts/check-prices.py --pm-history TICKER1 TICKER2 ...
```

These output formatted tables with time, price, volume, and change%. Use these instead of piping yahoo-fetch.py through inline python.

For raw JSON data (rare cases only):
```bash
python3 scripts/yahoo-fetch.py TICKER --interval 5m --range 2d --prepost
```
Do NOT use raw `curl` to Yahoo Finance (it will fail without the User-Agent header).

### 3. Check Open Position P&L (Alpaca)

Open positions live on the **Alpaca paper account** (source of truth), not in the log. Pull them read-only for context:

```bash
node scripts/broker.js positions
```

For each open position, note the unrealized P&L Alpaca reports (entry = the real `filled_avg_price`). **Do not place hold/sell orders here** — exits are handled by `position-evaluation.md` (10:30 / 14:30 CET). If there are no open positions, state that and move on. The hand-maintained markdown ledger was discarded 2026-06-25; do **not** reconstruct P&L from assumed/quoted prices for stocks that never filled on Alpaca.

### 4. Scanner Diagnostic

Run this full section on **pulse 1**. On **pulse 2 and 3**, reuse the existing scanner diagnostic unless new evidence changes the conclusion.

**Scan coverage check (run first):** Before diagnosing detection, verify how many of the scheduled evening scans actually ran last night. There are **7 scheduled evening scans** (21:30, 22:00, 22:30, 23:00, 23:30, 00:00, 00:30 CET). Count the `## Scan HH:MM CET` sections in last night's `LOG_FILE` (or `git log` commits matching `post-market scan`). Record `Evening scans ran: X of 7` in the Scanner Effectiveness section, and keep a running **coverage-failure tally** in Notes (date + how many scans ran) whenever fewer than 7 ran. A coverage failure means the entry window (23:00–00:30 CET) may have been partly or fully uncaptured. **Critical:** on a night where the scanner did not run during the entry window, do **not** count that night's winner as a detection *miss* and do **not** increment the selection count against us — there was no opportunity to detect or trade. Note it as a coverage failure instead. Founding case: Jun 18–19 (only 2 of 7 scans ran; entry window lost). If coverage failures recur (≥2 within ~10 sessions), flag in Notes that the scheduler/bridge reliability needs investigation (a infra decision left to the user) — a one-off is likely transient.

**For today's winner (from Step 2), answer:**
- Was it detectable at evening screening time (~22:15 CET)? YES / NO
- If YES: what did it look like then? (price, volume, % gain) — why didn't we act on it?
- If NO: why not? (news came later, AH move started after midnight, no volume yet, etc.)
- What scanner change would have caught it?

**Ceiling-override watch outcomes:** If last night's log flagged any **CEILING-OVERRIDE WATCH** candidates (BUILD-and-hold stocks skipped only on the +150% ceiling), look up each one's PM follow-through and record the hypothetical P&L (skipped entry price → PM peak) in the Notes section. Tally these over time — they are the dataset for deciding whether the extension ceiling should become conditional for genuine BUILD-and-hold patterns.

**Dead-cat-override watch outcomes:** If last night's log flagged any **DEAD-CAT-OVERRIDE WATCH** candidates (Day% ≤ -15% stocks that reclaimed above their regular close on a multi-scan AH BUILD, skipped only by the dead-cat filter), look up each one's PM follow-through and record the hypothetical P&L (skipped entry price → PM peak) in Notes. Tally these over time — they are the dataset for deciding whether the dead-cat filter should become conditional for AH builds that reclaim above the regular close. (Founding case: BYAH Jun 11, hypothetical +72%.)

**Fade-rule false-negative tracking:** If last night's log skipped any candidate on the **SPIKE→FADE / early-peak-fade rule** (faded in after-hours, correctly skipped from live entry) that then **re-exploded in premarket** (PM peak materially above its AH peak and above a profitable hypothetical entry), record it in a running tally in Notes with its AH peak, PM peak, **float**, and hypothetical AH-entry→PM-peak P&L. These are false negatives of the fade-skip rule. Known cases so far: CRE (Jun 17, AH peak $4.65 +48% faded → PM peak $5.99 +90%); LNKS (Jun 18, AH peak $2.31 +40% faded → PM peak $4.70 +185%, float 1.5M). **Also record the float of the same-night faders the rule *correctly* skipped** (PM stayed below AH peak) for contrast — e.g. Jun 18 TGE faded as predicted on a 44.2M float. Hypothesis under test: AH-faders that re-explode in PM are distinguished by very low float (<~3M); if so, the eventual exception should be a conditional low-float PM-open re-check rather than a blanket one. This tally is the dataset for deciding whether the SPIKE→FADE skip needs a PM-open re-check exception. A single case does not justify relaxing the rule — the fade rule correctly skipped MYSE/FLZH/GDHG the same night; only a recurring pattern (≥4/5 AH-faders re-exploding) would warrant a change.

**PM-only gapper tracking:** Identify the morning's single **biggest raw PM mover** (highest % from previous close, regardless of strategy fit). Classify it as either (a) an **AH→PM continuation** the evening scanner could detect (moved >10% in after-hours), or (b) a **PM-only gapper** (flat/down in after-hours, move began only after 04:00 ET on overnight news — structurally undetectable by the AH scanner). Record the classification and maintain a running tally in Notes. Known cases so far: PM-only gappers — CIIT (Jun 10, +140%), GLXG (Jun 11, +343%), TDIC (Jun 16, +140%), MBRX (Jun 23, +131%, uninvestable — crashed $6.64→$3.77 in 10 min), CUPR (Jun 24, +81%, thin print — $9.74 high was an illiquid tick). **For each PM-only gapper, also classify its investability:** check the `--pm-history` 5-min bars and label it **holdable** (the gain was sustained for ≥2 consecutive 5-min bars on real volume, giving a plausible exit window) or **uninvestable** (instant crash within ~10 min, or the peak was a single thin/illiquid tick). Record the label beside each case. This tally is the dataset for deciding whether the morning's biggest movers are dominated by PM-only gappers — but the blind spot only matters if those gappers are *holdable*. Hypothesis under test: most PM-only gappers are uninvestable spikes, so the AH-scanner blind spot has low real cost and does **not** justify a separate (and risky) early-PM scan workflow; only a cluster of *holdable* PM-only gappers would. A PM-only gapper is **not** a scanner failure — do not count it against detection baseline.

**Late-AH-tail surge tracking:** Separate from the PM-only case above, check whether today's winner (or the biggest AH→PM mover) had its **defining AH surge *after* the last scheduled scan** — i.e. the move that set up the PM continuation fired after 18:30 ET / 00:30 CET but before premarket opened (04:00 ET), in the unscanned 18:30–20:00 ET after-hours tail. If so, classify it as a **late-AH-tail surge** and add a row to a running tally in Notes (date, ticker, surge time ET, hypothetical AH-tail-entry → PM-peak P&L). This is distinct from a PM-only gapper: the stock *did* have an after-hours footprint, but the decisive move happened in the ~90-minute tail the 7-scan schedule does not cover (last scan 00:30 CET / 18:30 ET). It is **not** a detection-threshold miss (during the scanned window the stock was correctly under the 10% AH threshold) and is **not** counted against the detection baseline. Founding case: ORIS (Jun 22, pure-AH surge $2.49→$3.28 +32% at 19:25 ET, after the 00:30 CET last scan, then PM peak $3.93; hypothetical AH-tail entry ~$2.55 → PM peak +54%). **Sub-classify each late-AH-tail case as feed-lag vs true-tail:** using the `--ah-history` reconstruction, check the stock's AH change *at the 18:30 ET / 00:30 CET last-scan timestamp*. If it was already over the 10% AH threshold then but the live 00:30 scan did not surface it (TradingView postmarket feed lag), label it **feed-lag** — a late scan would not have helped; the fix is data-source verification (e.g. cross-check Yahoo AH at the last scan). If it was genuinely under threshold at 18:30 ET and the decisive surge fired after, label it **true-tail** — only these argue for an added late scan. Known: ORIS (true-tail; +22–28% at 18:30 ET, surged 19:25 ET), BTCT (Jun 29→30, **feed-lag**; already +67.6% at 18:30 ET but the 00:30 scan's feed showed it flat, peaked +139% at 18:50 ET; hypo AH-tail entry ~$1.20 → AH peak +47%). This tally is the dataset for deciding whether to add 1–2 late scans (~01:00/01:30 CET) covering the 18:30–20:00 ET tail — a scheduling decision left to the user. A single case does not justify it; a recurring pattern (≥3–4 **true-tail** winners surging in this tail) would. A **feed-lag** cluster instead points at fixing the AH data source, not the schedule.

**Then compare all retrospective results with evening scans:**
- **Caught**: stocks in both evening scans and retrospective
- **Missed**: stocks in retrospective that evening scans never found
- For each missed stock, analyze WHY:
  - Appeared too late (after our last scan)?
  - Below our volume/change thresholds at scan time?
  - Sector filtered out?

### 5. Update Log

Append a `## Morning Evaluation` section to the log.
- **Pulse 1:** use the full template below.
- **Pulse 2 and 3:** append a shorter update that reuses pulse 1's winner and scanner diagnostic, then refreshes P&L, follow-through, and exit status.

```markdown
## Morning Evaluation — HH:MM CET

### Today's Winner

**[TICKER]** — [sector]
- Catalyst: [what drove it]
- Previous Close: $X
- AH last night: $X (+X%) at HH:MM CET
- Premarket now: $X (+X%)
- Hypothetical P&L (AH entry → PM peak): +X%
- Float: X | Market Cap: $X

**Scanner Diagnostic:**
- Detectable at screening time? **YES / NO**
- [If YES: what it looked like at ~22:15 CET, why we did/didn't act]
- [If NO: why — news timing, volume below threshold, etc.]
- Scanner gap: [what would need to change to catch this]

[If no clear winner today: "No stock showed the AH→PM pattern today. Reason: [market conditions, etc.]"]

### Baseline Tracking

**Use the cumulative values from Step 1.** Increment "Days tracked" by 1. If today's winner was detectable, increment the detected count and add ticker to the list.

- Days tracked: [previous + 1]
- Winners detected by scanner: X/Y (**X%**) — [list of tickers]
- Winner selected for paper trade: X/Y (**X%**) — did we trade the right stock?
- Target: >80% detection
- Status: **BASELINE MET / NOT MET**

### Retrospective Scan Results
[results from AH reconstruction via `check-prices.py --ah-history`, optional forced AH scan diagnostic, and PM scan]

### Open Position P&L (Alpaca)

Only real Alpaca fills go in this table (entry/exit = `filled_avg_price` from `broker.js`). Candidates that were tracked but never filled belong in the Scanner Diagnostic as *hypothetical* (AH entry → PM peak), **not** here. If there were no Alpaca fills, write "No executed positions."

| Ticker | Entry | Entry Total% | Catalyst | Entry Time | PM Peak | Peak Time | Exit | P&L | P&L % | Status |
|--------|-------|--------------|----------|------------|---------|-----------|------|-----|-------|--------|
| XXXX   | $2.50 | +35.0% | A — breakthrough data | 23:00 CET  | $3.20 | 06:15 ET | $3.10 | +€24.00 | +24.0% | ✅ Win |

**PM Peak** = highest premarket price observed. **Peak Time** = when that peak occurred (ET). Track this to identify optimal exit windows. Use `check-prices.py --pm-history TICKER` to find the peak.

**Entry Total%** = total change from **previous close** (not just AH change). Calculate as: `(entry_price - prev_close) / prev_close`. This combines Day% + AH% into one number showing how extended the stock is at entry. Example: if prev close was $4.10 and you enter at $6.86, Entry Total% = +67.3%.

**Catalyst** = tier from Day Trading.md catalyst ranking + brief label. Use: **A** (operational improvement, partnership, breakthrough data), **B** (FDA milestone), **C** (analyst target), **D** (financing/dilution), or **None** (no catalyst found/unverified). This tracks whether catalyst quality predicts PM follow-through.

**Total Realized P&L (Alpaca fills only): +€XX.XX**

### Scanner Effectiveness

- Evening scans ran: X times (HH:MM - HH:MM CET)
- Candidates found: X unique tickers
- Retrospective matches: X/Y

### Missed Opportunities

| Ticker | AH Change | Why Missed | Would Be Profitable? |
|--------|-----------|------------|---------------------|

[or "No significant missed opportunities."]

### AH Mover Follow-Through

How did last night's top AH movers perform into premarket? Include every stock that appeared in 2+ evening scans with AH change >10%.

| Ticker | AH Peak | Peak Time | AH Trajectory | Current PM | From Peak | From Close | Verdict |
|--------|---------|-----------|---------------|------------|-----------|------------|---------|

**AH Trajectory** — classify the AH price action from evening scan data:
- **Build**: AH% increased across scans (e.g., +6% → +13% → +20%)
- **Spike→fade**: peaked early in AH, declined in later scans
- **Spike→hold**: spiked then held steady across scans
- **Late surge**: flat in early AH, jumped in later scans (23:30+ CET)

This tracks whether AH momentum carries into premarket and which AH patterns predict follow-through.

**AH-peak-vs-PM-peak check:** For each mover, note whether the PM peak *exceeded* or *fell short of* the AH peak. When the AH peak was higher (AH was the better exit), flag it. We are testing the hypothesis that extreme AH runners (AH peak >250% from close) tend to peak in after-hours and fade into PM rather than continuing — MSW (Jun 9: AH +292% > PM +221%) is the first data point. Tally these cases in Notes; if the pattern recurs, it argues for taking partial profit in late AH on extreme runners.

### Notes
[any observations about scanner performance, threshold adjustments needed, etc.]
```

### 6. Generate Price Charts (Pulse 1 only)

For today's winner and any strong candidates, generate ASCII price timelines:

```bash
python3 scripts/price-timeline.py WINNER_TICKER CANDIDATE1 CANDIDATE2
```

This shows:
- 2-day price range and current position
- Peak price and timing
- Session-by-session breakdown (AH, PM, REG)

Include the chart output in the log under a `### Price Charts` section.

### 7. Multi-Day Tracking (Pulse 1 only)

Update `WINNERS_TRACKING.md`:

1. **Add today's winner** to the "Active Watch" table
2. **Check previous winners** still in Active Watch:
   ```bash
   python3 scripts/check-prices.py PREV_WINNER1 PREV_WINNER2 ...
   ```
3. **Move to Historical** any winners that are 5+ days old
4. **Note any runners** (stocks that kept going after day 1)

This catches multi-day runners like AIIO (+878% over 7 days) that we'd miss with premarket-only exits.

### 8. Commit

```bash
git add log/ WINNERS_TRACKING.md
git commit -m "morning evaluation YYYY-MM-DD"
git push
```
