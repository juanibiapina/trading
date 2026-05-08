Run a morning evaluation of the overnight scanning session.

**Schedule awareness:** This prompt runs as a premarket pulse at 10:20, 12:00, and 14:00 CET (3 pulses). Check `date` to determine which pulse this is.
- **Pulse 1 (10:20 CET):** Full evaluation — find today's winner, diagnose scanner, check paper trade P&L.
- **Pulse 2 (12:00 CET):** Update paper trade P&L, note any significant price changes since pulse 1.
- **Pulse 3 (14:00 CET) — LAST PULSE:** Update paper trade P&L and **close all positions**. Sell any open paper trade at the current premarket price. Record the exit in the log. An open position blocks the next evening trade.

**Scope by pulse:**
- **Pulse 1:** Run the full retrospective workflow.
- **Pulse 2:** Reuse pulse 1's winner and scanner diagnostic. Do **not** rerun `python3 scripts/scan.py --all --session afterhours` or a full winner search unless pulse 1 is missing or clearly incomplete.
- **Pulse 3:** Same as pulse 2, then close positions.
- This is a morning retrospective, not an evening post-market workflow. Ignore any post-market entry guidance if that skill loads.

**Primary goal on pulse 1: find today's winner and diagnose the scanner.** On pulses 2 and 3, the goal is to update prices, P&L, and any notable changes since pulse 1.

The most important question is: what stock IS exploding in premarket right now? There is almost always one. Find it first — independently, without looking at last night's watchlist — then check if our evening scanner would have caught it. This is the baseline test: if the scanner can't even detect the winners, no entry rules will make the strategy work. See "Learning Phase" in Day Trading.md for the full reasoning.

## Steps

### 1. Setup

- Run `date` to get the current time
- Determine yesterday's US trading date (the AH session we're evaluating)
- Set `LOG_FILE=log/YYYY-MM-DD/log.md` using that date
- Pull latest changes: `git stash && git pull --ff-only && git stash pop 2>/dev/null || true`
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

### 3. Check Paper Trade P&L

If there are paper trades in the log, check their current prices:

```bash
python3 scripts/check-prices.py TICKER1 TICKER2 ...
```

For each paper trade:
- Get current premarket price (or latest available price)
- Calculate unrealized P&L: `(current_price - entry_price) * shares`
- Calculate P&L percentage: `((current_price - entry_price) / entry_price) * 100`

### 4. Scanner Diagnostic

Run this full section on **pulse 1**. On **pulse 2 and 3**, reuse the existing scanner diagnostic unless new evidence changes the conclusion.

**For today's winner (from Step 2), answer:**
- Was it detectable at evening screening time (~22:15 CET)? YES / NO
- If YES: what did it look like then? (price, volume, % gain) — why didn't we act on it?
- If NO: why not? (news came later, AH move started after midnight, no volume yet, etc.)
- What scanner change would have caught it?

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

- Days tracked: X
- Winners detected by scanner: X/Y (**X%**)
- Winner selected for paper trade: X/Y (**X%**) — did we trade the right stock?
- Target: >80% detection
- Status: **BASELINE MET / NOT MET**

### Retrospective Scan Results
[results from AH reconstruction via `check-prices.py --ah-history`, optional forced AH scan diagnostic, and PM scan]

### Paper Trade P&L

| Ticker | Entry | Entry Total% | Catalyst | Entry Time | Current | P&L | P&L % | Status |
|--------|-------|--------------|----------|------------|---------|-----|-------|--------|
| XXXX   | $2.50 | +35.0% | A — breakthrough data | 23:00 CET  | $3.10   | +€24.00 | +24.0% | ✅ Win |

**Entry Total%** = total change from **previous close** (not just AH change). Calculate as: `(entry_price - prev_close) / prev_close`. This combines Day% + AH% into one number showing how extended the stock is at entry. Example: if prev close was $4.10 and you enter at $6.86, Entry Total% = +67.3%.

**Catalyst** = tier from Day Trading.md catalyst ranking + brief label. Use: **A** (operational improvement, partnership, breakthrough data), **B** (FDA milestone), **C** (analyst target), **D** (financing/dilution), or **None** (no catalyst found/unverified). This tracks whether catalyst quality predicts PM follow-through.

**Total Paper P&L: +€XX.XX**

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

### Notes
[any observations about scanner performance, threshold adjustments needed, etc.]
```

### 6. Commit

```bash
git add log/
git commit -m "morning evaluation YYYY-MM-DD"
git push
```
