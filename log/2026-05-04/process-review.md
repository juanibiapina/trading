# Process Review - 2026-05-04

## Sessions Reviewed

- `2026-05-05T12-20` - scanner-improvement
- `2026-05-05T12-00` - morning-evaluation pulse 3
- `2026-05-05T10-00` - morning-evaluation pulse 2
- `2026-05-05T09-30` - daily-email

## Issues Found

### 1. Morning Evaluation Pulse Scope Confusion
- **Severity:** Wasteful
- **Sessions affected:** 2 out of 4 reviewed
- **Symptom:** Pulse 2 and pulse 3 reran a full retrospective workflow instead of reusing pulse 1. Both sessions ran fresh `scan.py` scans, and both started with `python3 scripts/scan.py --all --session afterhours` even though the prompt said the live premarket scan should be primary and later pulses should only update P&L and changes.
- **Root cause:** `prompts/morning-evaluation.md` mixed pulse-specific update tasks with a general "find today's winner" instruction. It also referred to the prior "post-market scanning session," which pulled in evening workflow guidance that does not fit the morning pulses.
- **Fix:** Updated `prompts/morning-evaluation.md` to:
  - rename the task as an overnight evaluation
  - state pulse-specific scope at the top
  - forbid rerunning `--session afterhours` or a full winner search on pulses 2 and 3 unless pulse 1 is missing
  - tell the agent to ignore post-market entry guidance if that skill loads
- **Status:** Fixed

### 2. Optional Process Review File Was Treated as Required
- **Severity:** Minor
- **Sessions affected:** 1 out of 4 reviewed
- **Symptom:** The daily-email session tried to read `log/2026-05-04/process-review.md` before it existed and hit `ENOENT`.
- **Root cause:** `prompts/daily-email.md` said the file was optional, but it did not explicitly tell the agent to check for existence before reading it.
- **Fix:** Updated `prompts/daily-email.md` to require an existence check and to treat a missing file as normal for that cycle.
- **Status:** Fixed

### 3. One-Off AWK Retry During Pulse 3 P&L Closeout
- **Severity:** Minor
- **Sessions affected:** 1 out of 4 reviewed
- **Symptom:** Pulse 3 used `awk` with `exit` as a variable name, hit a syntax error, then retried with a different variable name and succeeded.
- **Root cause:** Ad-hoc shell arithmetic, not a prompt or environment failure.
- **Fix:** None. The retry succeeded immediately, and this does not show a cross-session pattern.
- **Status:** Monitoring

## Summary

Two prompt fixes were applied. The bigger one targets repeated morning pulse waste by stopping pulse 2 and pulse 3 from redoing the full retrospective and from falling back to forced after-hours scans. The email prompt fix removes a noisy optional-file error.
