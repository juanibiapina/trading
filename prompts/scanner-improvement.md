Review recent scanning results and make incremental improvements to the scanner and process.

This runs daily after the morning evaluation. The goal is continuous, data-driven improvement.

## Rules

- **One or two small changes per day.** Never rewrite a whole file. Surgical edits only.
- **Every change must have a hypothesis.** "I expect this will..." with measurable criteria.
- **Evaluate previous changes first.** Check if yesterday's changes helped before making new ones.
- **Don't change strategy.** Entry rules, sector discipline, position sizing — those are the user's domain. You improve the *scanner and process* that feeds into those decisions.
- **Be conservative.** A missed improvement is fine. A broken scanner is not.

## What You Can Change

- Scanner thresholds and filters (`scripts/scan.py`)
- Scanner output columns and formatting (`scripts/scan.py`)
- Price checking utility (`scripts/check-prices.py`)
- Evening scan prompt logic (`prompts/post-market-scan.md`)
- Morning evaluation prompt logic (`prompts/morning-evaluation.md`)
- Add new utility scripts in `scripts/`

## What You Must NOT Change

- `Day Trading.md` (trading plan — user-maintained)
- `AGENTS.md` (agent instructions)
- `scheduler.json` (schedule — managed separately)
- This file (`prompts/scanner-improvement.md`)
- Core trading rules (sector discipline, position sizing, entry/exit rules)

## Steps

### 1. Read Context

- Read `SCANNER_CHANGELOG.md` — understand what changes have been made and what's pending evaluation
- Read today's morning evaluation log (`log/YYYY-MM-DD/log.md` — determine the date: if before 06:00 CET, use yesterday's CET date)
- Read the last 3-5 days of logs for patterns (check `log/` directory)
- Read `Day Trading.md` for current rules and lessons

### 2. Evaluate Previous Changes

For each recent changelog entry that has a hypothesis:
- Check if there's enough data to evaluate it
- If yes: did it help? Add an `**Evaluation:**` note to the changelog entry
- If no: note "insufficient data" and move on

### 3. Identify Improvements

Look for patterns in recent logs:
- Are we missing stocks that would have been profitable? → adjust thresholds
- Are we getting too many false positives? → tighten filters
- Is the paper trading logic making bad entries? → improve evaluation criteria
- Is data missing that would help decisions? → add scanner output columns
- Are there repeated patterns the prompts don't catch? → update prompt logic

### 4. Implement Changes

For each change:
1. State the hypothesis clearly
2. Make the edit (small, surgical)
3. Verify the file still works (e.g., `python3 scripts/scan.py --help` for syntax check)

### 5. Update Changelog

Prepend a new entry to `SCANNER_CHANGELOG.md` (before the previous entries, after the header sections):

```markdown
### YYYY-MM-DD — [Brief Title]

**Context:** [What recent data prompted this]

**Evaluation of previous changes:**
- [Change from YYYY-MM-DD]: [helped / didn't help / insufficient data]. [Evidence.]

**Changes:**
1. **[File]** — [What changed]
   - Why: [reasoning from data]
   - Hypothesis: [expected measurable impact]

**Updated parameters:** (if scanner params changed)
```

Also update the "Current Scanner Parameters" or "Current Process" sections at the top of the changelog if those values changed.

### 6. Commit

```bash
git add -A
git commit -m "scanner improvement YYYY-MM-DD: [brief description]"
git push
```

### 7. Send Daily Summary Email

Send an email summarizing the full overnight cycle to `juanibiapina@gmail.com`.

```bash
gmcli juanibiapina@gmail.com send \
  --to juanibiapina@gmail.com \
  --subject "Trading Scanner Report — YYYY-MM-DD" \
  --body "..."
```

The email body should be a concise, readable summary covering:

1. **Post-Market Scans** — How many scans ran, how many unique tickers found, any notable movers
2. **Paper Trades** — Any positions entered, entry price and reasoning
3. **Morning Evaluation** — Paper P&L (€ and %), scanner catch rate, missed opportunities
4. **Improvements Made Today** — What was changed, the hypothesis, and what we're evaluating
5. **Key Takeaway** — One sentence: the single most important thing from this cycle

Keep it short — aim for something scannable on a phone in under 30 seconds.
