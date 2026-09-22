# Process Review — 2026-09-22

## Sessions Reviewed

Five completed sessions immediately before this review, timestamps UTC:

- 2026-09-22 08:30 — position evaluation
- 2026-09-22 09:00 — premarket-open scan
- 2026-09-22 09:30 — daily email
- 2026-09-22 12:20 — scanner improvement
- 2026-09-22 12:30 — position evaluation

Excluded: this process review at 12:40 UTC.

## Issues Found

### Sessions reused an out-of-range log offset

- **Severity:** Wasteful
- **Sessions affected:** 2 of 5 reviewed
- **Symptom:** The daily-email and scanner-improvement sessions tried to read `log/2026-09-22/log.md` at offset 318 while the file had only 13 lines. Both reads failed, then the sessions recovered by reading the correct cycle log and completed.
- **Root cause:** The prompts did not require cycle-date confirmation or a current line-count check before using a nonzero read offset. The agents reused an offset from a longer prior log and initially selected the current partial log instead of the completed overnight-cycle log.
- **Fix:** Updated `prompts/daily-email.md` to use the resolved cycle date, read the cycle log from the start, and validate offsets. Updated `prompts/scanner-improvement.md` to select the log updated by morning evaluation and apply the same offset guard.
- **Status:** Fixed

## Additional Checks

- The five sessions made 72 bash calls. No identical bash command ran three or more times.
- One exact-text edit failed in scanner improvement and self-corrected with a shorter target; it did not create a retry loop or block completion.
- No missing required tool, permission error, stale prompt path, or unresolved user-action issue appeared in the reviewed sessions.
- All five sessions completed and pushed their work.
