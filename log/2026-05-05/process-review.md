# Process Review — 2026-05-05

## Sessions Reviewed
- 2026-05-06T12-20 (scanner-improvement)
- 2026-05-06T12-00 (morning eval pulse 2)
- 2026-05-06T10-00 (morning eval pulse 2 — ran at wrong time?)
- 2026-05-06T09-30 (daily email)
- 2026-05-06T08-20 (morning eval pulse 1)
- 2026-05-05T22-30 (post-market scan)
- 2026-05-05T22-00 (post-market scan)
- 2026-05-05T21-30 (post-market scan)
- 2026-05-05T21-00 (post-market scan)

## Issues Found

### 1. Uncommitted edits from interactive session cause git pull failures
- **Severity:** Wasteful
- **Sessions affected:** 2 out of 9 reviewed (10:00 and 12:00 morning evals)
- **Symptom:** `git pull` fails with "cannot pull with rebase: You have unstaged changes"
- **Root cause:** The daily-email session (09:30) was used interactively by the user to change the float threshold. It edited `SCANNER_CHANGELOG.md` and `prompts/post-market-scan.md` but had no commit step (it's a read-and-send task). Subsequent sessions found a dirty working tree.
- **Fix:** Made `morning-evaluation.md` pull step resilient: `git stash && git pull --ff-only && git stash pop`. This handles dirty trees gracefully regardless of cause.
- **Status:** Fixed

### 2. Morning eval Finviz news scraping via inline Python (repeated discovery)
- **Severity:** Minor (wasteful but not blocking)
- **Sessions affected:** 1 out of 9 (08:20 pulse 1)
- **Symptom:** Session writes 3+ inline Python scripts trying different regex patterns to scrape Finviz news, eventually falls back to Google News RSS. 97 total bash commands, ~$0.60 cost.
- **Root cause:** No dedicated news/catalyst lookup utility in `scripts/`. Sessions improvise with inline code. The `websearch` CLI works but the session tried Finviz first.
- **Fix:** Not fixing now — the `websearch` tool works for catalyst lookups and later sessions use it correctly. If this recurs (inline Finviz scraping in multiple sessions), consider adding a `scripts/news.py` utility.
- **Status:** Monitoring

### 3. "Offset beyond end of file" on log re-reads
- **Severity:** Minor
- **Sessions affected:** 3 out of 9 (22:30, 22:00 post-market; 10:00 morning eval)
- **Symptom:** Session tries to re-read a log file with an offset that exceeds the file's current line count (e.g., offset=120 on a 118-line file).
- **Root cause:** Sessions estimate offsets based on prior reads, but the file hasn't grown as much as expected. The `read` tool returns a clear error and sessions self-correct on next attempt.
- **Fix:** No fix needed — self-correcting, costs 1 wasted tool call (trivial).
- **Status:** Acceptable

## Summary

One actionable fix made (resilient git pull). No critical issues. Total daily cost across all 9 sessions: ~$3.86.
