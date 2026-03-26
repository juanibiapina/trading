# Process Review — 2026-03-26

## Sessions Reviewed
- `2026-03-26T09-45` — scanner improvement (31 tool calls)
- `2026-03-26T09-20` — morning evaluation (26 tool calls)
- `2026-03-25T23-30` — post-market scan 00:30 CET (10 tool calls)
- `2026-03-25T23-00` — post-market scan 00:00 CET (15 tool calls)
- `2026-03-25T22-30` — post-market scan 23:30 CET (25 tool calls)
- `2026-03-25T22-00` — post-market scan 23:00 CET (19 tool calls)
- `2026-03-25T21-30` — post-market scan 22:30 CET (20 tool calls)
- `2026-03-25T21-00` — post-market scan 22:00 CET (31 tool calls)
- `2026-03-25T20-30` — post-market scan 21:30 CET (18 tool calls)

## Issues Found

### 1. Excessive websearch depth per ticker
- **Severity:** Wasteful
- **Sessions affected:** 3 of 7 post-market sessions (21:00, 22:00, 22:30)
- **Symptom:** Sessions perform 6-9 websearch calls for a single ticker when the structured 3-step catalyst search doesn't find results. The 22:30 session did 9 searches for SLND alone, trying progressively more obscure queries (globenewswire, exa provider, brave provider, SEC filings). The 21:00 session did 18 websearch calls across 3 tickers (6 each for ADVB, FCHL, HCTI).
- **Root cause:** The prompt's structured catalyst search (earnings, PRs, SEC filings) is clear, but there was no guidance on when to stop. Sessions escalate to speculative queries and alternative providers after the structured steps fail.
- **Wasted calls:** ~20 extra searches across the evening (59 total, ~35-40 would have been sufficient)
- **Fix:** Added search budget to `prompts/post-market-scan.md` and `.pi/skills/post-market/SKILL.md`: max 4 websearch calls per ticker, no `websearch extract` on financial sites, stop after structured steps fail.
- **Status:** Fixed

### 2. websearch extract fails on JS-rendered sites (continuing)
- **Severity:** Minor
- **Sessions affected:** 2 of 7 post-market sessions (21:00, 22:30)
- **Symptom:** `websearch extract` on Finviz (3 calls), minichart.com.sg (1 call), and Benzinga (1 call) returns "Error: document is not defined." Sessions recover quickly but waste 1-3 calls per incident.
- **Root cause:** These sites require JavaScript rendering. `websearch extract` can't handle them.
- **Fix:** Addressed by fix #1 above (explicit note not to use `websearch extract` on financial sites). Previously marked "non-actionable" in Mar 25 review, but sessions kept trying it because the prompt didn't say not to.
- **Status:** Fixed

## Improvements Since Last Review

- **Raw curl to Yahoo Finance:** Zero occurrences across all 9 sessions. The fix from Mar 24 (helper scripts + prompt update) is fully propagated.
- **python3 / nix-shell workaround:** Zero occurrences. Fully resolved since Mar 24.
- **Inline Python fragility:** Zero ValueError occurrences. Sessions consistently use helper scripts for Yahoo data.
- **Scanner script:** Ran cleanly in all sessions. No failures.
- **Later post-market sessions are efficient:** The 23:00 and 23:30 sessions (4 and 0 websearch calls respectively) show that sessions with fewer new tickers are appropriately lightweight.

## Observations

- Total websearch calls across the 7 evening sessions: 59. With the search budget (4 per ticker), this should drop to ~35-40.
- The morning evaluation and scanner-improvement sessions were clean: no errors, no retries, no wasted calls.
- The pattern from yesterday's review holds: fixes applied to one prompt must be applied to all prompts that use the same tool. The search budget was added to both `post-market-scan.md` and `SKILL.md`.
