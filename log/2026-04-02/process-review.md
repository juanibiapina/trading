# Process Review - 2026-04-02

## Sessions Reviewed

- `2026-04-02T12-20` - scanner-improvement (33 calls, 61 lines)
- `2026-04-02T12-00` - morning-evaluation pulse 3 (12 calls, 26 lines)
- `2026-04-02T10-00` - morning-evaluation pulse 2 (12 calls, 28 lines)
- `2026-04-02T09-30` - daily-email (9 calls, 21 lines)
- `2026-04-02T08-20` - morning-evaluation pulse 1 (33 calls, 28 lines)
- `2026-04-01T22-30` - post-market scan 00:30 CET (11 calls)
- `2026-04-01T22-00` - post-market scan 00:00 CET (12 calls)
- `2026-04-01T21-30` - post-market scan 23:30 CET (16 calls)
- `2026-04-01T21-00` - post-market scan 23:00 CET (23 calls)

## Issues Found

### 1. Dirty Working Tree Causes Stash Dance in Every Session

- **Severity:** Wasteful
- **Sessions affected:** 7 out of 7 non-email sessions
- **Symptom:** Every session runs `git stash && git pull && git stash pop` (or the 3-step variant). This adds 1-2 extra tool calls per session, ~14 wasted calls across the 9 sessions reviewed.
- **Root cause:** Two files have uncommitted local changes:
  - `prompts/morning-evaluation.md` — pulse schedule instructions added by a session but never committed. Every morning eval session depends on these instructions.
  - `Day Trading.md` — one-line addition ("Never hold positions through the day").
- **Fix:**
  - **morning-evaluation.md:** Committed now. The pulse schedule is actively used by all 3 morning sessions and should be in the repo.
  - **Day Trading.md:** Needs user action. This file is user-maintained. Either commit the change or revert it. Until resolved, sessions will continue stashing around it.
- **Status:** Partially fixed (morning-evaluation.md committed). Day Trading.md needs user action.

### 2. check-prices.py Output Insufficient for Morning Evaluations

- **Severity:** Wasteful
- **Sessions affected:** 3 out of 3 morning sessions, 2 out of 4 evening sessions
- **Symptom:** Sessions call `check-prices.py`, find the output inadequate, then redo the work:
  - Pulse 3 (12:00): "The check-prices script isn't showing PM data. Let me fetch live data directly."
  - 23:00 scan: "The check-prices data is sparse. Let me get more detailed AH data."
- **What happens next:** Sessions fall back to `yahoo-fetch.py | python3 -c "..."` with 10-40 line inline python scripts to parse the raw JSON. The morning eval (08:20) used 8 yahoo-fetch calls + 5 inline python scripts = 13 extra tool calls.
- **Root cause:** `check-prices.py` shows a summary row per ticker (close, PM price, PM%, AH price, AH%). Agents need the AH/PM price *timeline* (progression over hours) to assess momentum and trajectories. The `--ah-history` mode exists but shows sparse data points.
- **Fix:** Needs script improvement. Either enhance `check-prices.py --ah-history` to show a denser timeline, or add a `--timeline` mode that outputs key price points at 30-min intervals. This would eliminate the need for inline python parsing.
- **Status:** Needs user action (script improvement)

### 3. Inline Python Data Processing (Token Waste)

- **Severity:** Wasteful
- **Sessions affected:** 5 out of 9 sessions
- **Symptom:** 12 total `python3 -c` invocations across 9 sessions. These are 10-40 line scripts embedded in bash commands, parsing yahoo-fetch JSON output into human-readable tables.
- **Root cause:** Same as issue #2. yahoo-fetch.py outputs raw JSON. Agents need formatted summaries.
- **Token cost:** Each inline script burns ~200-500 output tokens just for the code, plus the JSON input tokens. The morning eval session (08:20) spent roughly 30-40% of its tool calls on data formatting.
- **Fix:** Same as #2. Better scripts = no inline python needed.
- **Status:** Needs user action (linked to issue #2)

## Previously Reported Issues

- **python3 on PATH:** Still resolved. Zero nix-shell workarounds.
- **check-prices.py timeouts:** Still resolved. Zero timeouts.
- **Email date logic (fixed Apr 1):** Working. Email session (09:30) read the correct log file on first try.

## Changes Made

- Committed `prompts/morning-evaluation.md` with pulse schedule instructions that sessions depend on but were never committed.

## Summary

One direct fix (commit morning-evaluation.md), two items needing user action:
1. Commit or revert the Day Trading.md local change to eliminate the remaining stash workaround.
2. Improve check-prices.py output to eliminate the inline python data processing pattern (12 wasted calls across 9 sessions).
