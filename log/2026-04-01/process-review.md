# Process Review - 2026-04-01

## Sessions Reviewed

- `2026-04-01T08-20` - morning evaluation (17 bash, 16 turns, $1.12)
- `2026-04-01T08-45` - scanner-improvement (6 bash, 15 turns, $1.53)
- `2026-04-01T09-10` - process-review [CRASHED] (4 bash, 4 turns, $0.13)
- `2026-04-01T09-30` - daily-email (8 bash, 7 turns, $0.43)
- Also checked Mar 31 sessions (morning + 7 evening post-market scans) and 5 historical email sessions (Mar 19-26).

## Issues Found

### Email Prompt Date Logic Wrong
- **Severity:** Wasteful
- **Sessions affected:** 4 out of 6 email sessions reviewed (Mar 19, 20, 24, 25, Apr 1). Pattern confirmed across 2+ weeks.
- **Symptom:** Email session tries to read `log/YYYY-MM-DD/log.md` using today's calendar date, gets ENOENT, then spends 2-3 extra tool calls listing directories to discover the correct date.
- **Root cause:** The email prompt said "Determine today's trading date (if before 06:00 CET, use yesterday)." But the morning evaluation writes to *yesterday's* US trading date (the AH session being reviewed). The email runs after the morning eval and should use the same date, not "today."
- **Example:** On April 1, morning eval wrote to `log/2026-03-31/log.md`. Email tried `log/2026-04-01/log.md` (ENOENT), then had to search for the right directory.
- **Fix:** Changed `prompts/daily-email.md` date instruction to: "Determine yesterday's US trading date. This is the date the morning evaluation used."
- **Status:** Fixed

### Process-Review Session Crashed (API Error)
- **Severity:** Minor (one-off)
- **Sessions affected:** 1 of 1 (2026-04-01T09-10)
- **Symptom:** Session hit `stopReason: error` with zero tokens on the third assistant turn. Made 4 tool calls, then died. Did not produce a process-review log.
- **Root cause:** Transient API error (zero-token response). Not a tooling or prompt issue.
- **Fix:** Not needed. The task was retried in a later session (this one). Transient API errors are expected occasionally.
- **Status:** No action needed

### Minor: Scanner-Improvement Read Error (Missing log.md)
- **Severity:** Minor
- **Sessions affected:** 1 of 1 scanner-improvement session (2026-04-01T08-45)
- **Symptom:** Tried to read `log/2026-03-27/log.md`, got ENOENT. That date only has `process-review.md` (no trading happened).
- **Root cause:** Same as reported in Mar 31 review. The scanner-improvement prompt reads recent logs to analyze results. Not every date directory has a `log.md`.
- **Fix:** Not needed. Session recovered gracefully (moved to other dates). This is benign.
- **Status:** No action needed

## Previously Reported Issues

- **python3 on PATH:** Still resolved. Zero nix-shell workarounds across all sessions.
- **check-prices.py timeouts:** Still resolved. Zero timeouts since the Mar 27 parallelization fix.
- **Inline python3 -c quoting errors:** Not observed in recent sessions.

## Summary

One systemic issue found and fixed: the email prompt's date logic was wrong, causing ENOENT errors in 4 out of 6 email sessions over the past 2 weeks. Each occurrence wasted 2-3 tool calls on directory discovery. The fix aligns the email's date determination with the morning evaluation's.
