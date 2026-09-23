# Process Review — 2026-09-23

## Sessions Reviewed

Five completed work sessions immediately before this review, timestamps UTC:

- 2026-09-23 08:30 — position evaluation
- 2026-09-23 09:00 — premarket-open scan
- 2026-09-23 09:30 — daily email
- 2026-09-23 12:20 — scanner improvement
- 2026-09-23 12:30 — position evaluation

Excluded: this process review at 12:40 UTC.

## Issues Found

### Exact-text edit failures caused avoidable retries

- **Severity:** Wasteful
- **Sessions affected:** 2 of 5 reviewed
- **Symptom:** Position evaluation made three edit attempts to remove cosmetic blank lines from `OPEN_POSITIONS.md`; the first two repeated the same stale target and failed. Scanner improvement had two stale exact-text edits fail while updating prompts and the changelog, then recovered with revised targets.
- **Root cause:** The prompts did not say to reread after an exact-text mismatch, avoid repeating unchanged patch text, or skip cosmetic-only edits.
- **Fix:** Added exact-edit recovery guidance to `prompts/position-evaluation.md` and `prompts/scanner-improvement.md`. The guidance requires a reread, a shorter unique target, at most one retry, and skipping cosmetic-only edits.
- **Status:** Fixed

## Additional Checks

- The five sessions made 74 bash calls. No identical bash command ran three or more times.
- One unsupported `node scripts/broker.js --help` probe returned exit code 1; the session did not retry it, and it did not block the task.
- All five sessions completed and pushed their work.
- No recurring missing-tool, permission, broken-path, or API failure appeared in the reviewed sessions.
