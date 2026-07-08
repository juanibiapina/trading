Advance the strategy roadmap by one concrete step. Runs daily.

This is the strategy-level twin of `scanner-improvement.md`. That loop makes
surgical scanner/process tweaks inside the daily cycle. This loop moves the
**bigger initiatives** in `STRATEGY_ROADMAP.md` forward with evidence
discipline. Only the **pilot** stage is serialized (one live experiment at a
time, for attribution); research / instrument / build work runs in parallel, so
each run advances the active pilot **and** clears ready low-risk items instead
of queuing them.

## North Star

The objective is **making the most money, fast** = maximizing account-growth
rate, per the North Star section of `STRATEGY_ROADMAP.md`. Detection rate,
baseline, and clean process are proxies, not the goal. The core AH->PM strategy
is a hypothesis that can be replaced if another approach compounds faster. Every
run, sanity-check that the active initiative is still the highest expected
dollars-per-unit-time lever; if a bigger lever has appeared (including changing
the core strategy or universe), surface it. Strategy pivots that touch
`Day Trading.md` or live trading are *proposed to Juan*, not applied alone, but
they are always in scope to raise.

## Rules

- **Serialize pilots only.** Never run two initiatives in the *pilot* stage at
  once (keeps P&L attributable). Research, instrument (log-only), and
  build/delivery work carry no attribution conflict, so advance them in
  parallel: each run does the top pilot step **plus** up to ~1-2 ready low-risk
  non-pilot items. Cap it so runs stay focused and never break the daily cycle.
- **Smallest next step.** Walk each initiative through Research -> Instrument ->
  Pilot -> Promote. Do the next smallest step that produces evidence, not a
  whole stage in one day.
- **Evaluate the last step first.** Did yesterday's step do what its hypothesis
  said? Record the result before taking a new step.
- **Evidence before promotion.** Never promote an initiative to the live cycle
  without data showing an edge over the current baseline.
- **Be conservative.** A slow roadmap is fine. A broken daily cycle is not.
  Prefer shadow/log-only changes over anything that alters live paper trading.

## What You Can Change

- `STRATEGY_ROADMAP.md` (this loop owns it — update status, notes, progress)
- `INITIATIVE_LOG.md` (prepend a dated entry each run)
- Add/edit scripts in `scripts/` (e.g. `broker.js`, backtests, analyses)
- Add **instrumentation** to existing prompts (log-only flags/columns), the same
  way the scanner trackers were added
- **Pulses/crons (Initiative 3 territory):** you MAY add new shadow or
  instrumentation pulses, and you MAY retire/retime pulses as part of executing
  Initiative 3. BUT any change to the timing of an existing **trading scan or
  evaluation** pulse must be *proposed in the run report for Juan to veto*, not
  silently applied. Adding a new log-only pulse is fine to apply directly.

## What You Must NOT Change

- `Day Trading.md` (trading plan — user-maintained)
- `AGENTS.md`
- Core trading rules (position sizing, learning-phase parameters)
- `prompts/scanner-improvement.md`, `prompts/morning-evaluation.md` trading
  logic (instrumentation columns are fine; decision rules are not)
- This file

## Steps

### 1. Read Context

- `STRATEGY_ROADMAP.md` — the source of truth for initiatives and their stage
- `INITIATIVE_LOG.md` — what was done on prior runs and what is pending eval
- `FEEDBACK_LOG.md` — recent Juan feedback that may re-prioritise
- Skim the last few daily logs if the active step needs market data

### 2. Evaluate the Previous Step

Find the most recent `INITIATIVE_LOG.md` entry with a hypothesis. Is there
enough evidence to judge it? If yes, record `did it work` with the evidence. If
no, note "insufficient data" and continue.

### 3. Select Today's Active Initiative

Advance the active **pilot** (if any) first, then clear ready low-risk
non-pilot items, all ranked by the North Star (expected dollars per unit time =
edge size x frequency x scalability, discounted by effort and uncertainty):
1. If an initiative is in the *pilot* stage, continue it (only one pilot at a
   time).
2. Then advance up to ~1-2 unblocked Research/Instrument/build items with the
   highest expected money-fast impact (these run in parallel with the pilot).
   Skip any whose `Needs from Juan` is unmet (note it as blocked).
3. If the highest-impact lever is not on the roadmap (e.g. a core-strategy or
   universe change looks like it would compound faster), add it as a new
   initiative and, if it touches live trading, flag it for Juan.

State which initiatives you advanced and why (the money-fast rationale) in one
sentence each.

### 4. Take the Next Smallest Step

Examples by stage:
- **Research:** run a backtest/census, pull data, answer one open question.
- **Instrument:** add a log-only flag/column/script; verify it runs.
- **Pilot:** mirror in shadow mode (e.g. Alpaca paper orders, hypothetical
  rows) and capture the first comparison.
- **Promote:** only with accumulated evidence; if promoting touches live pulses
  or rules, propose it for Juan rather than applying unilaterally.

Verify anything you build actually runs before logging it.

### 5. Update the Roadmap and Log

- Update the active initiative's **Status** and add a dated progress note in
  `STRATEGY_ROADMAP.md`. Refresh the consolidated "Open asks for Juan" if an
  ask opened or closed.
- Prepend an entry to `INITIATIVE_LOG.md`:

```markdown
### YYYY-MM-DD — [Initiative N: short title]

**Evaluated:** [prior step — worked / didn't / insufficient data, with evidence]

**Step taken:** [the concrete thing done today]

**Result:** [what came out of it — data, file built, decision]

**Hypothesis / next step:** [what the next run should check or do]

**Needs from Juan:** [anything blocking, or "nothing"]
```

### 6. Commit

```bash
git add -A
git commit -m "strategy advance YYYY-MM-DD: [initiative + brief]"
git push
```

### 7. Report

One line: which initiative moved, what step, and any new ask for Juan. If a
trading-pulse schedule change is being proposed, surface it clearly so Juan can
veto before the next run.
