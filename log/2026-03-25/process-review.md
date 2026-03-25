# Process Review - 2026-03-25

## Sessions Reviewed
- `2026-03-25T09-45` - scanner improvement
- `2026-03-25T09-20` - morning evaluation
- `2026-03-24T23-30` - post-market scan (00:30 CET)
- `2026-03-24T23-00` - post-market scan (00:00 CET)
- `2026-03-24T22-30` - post-market scan (23:30 CET)
- `2026-03-24T22-00` - post-market scan (23:00 CET)
- `2026-03-24T21-30` - post-market scan (22:30 CET)
- `2026-03-24T21-00` - post-market scan (22:00 CET)
- `2026-03-24T20-30` - post-market scan (21:30 CET)

## Issues Found

### 1. Yahoo Finance raw curl in post-market sessions (incomplete fix from Mar 24)
- **Severity:** Wasteful
- **Sessions affected:** 3 of 7 post-market sessions (21:00, 21:30, 23:30)
- **Symptom:** Sessions use `curl -s "https://query1.finance.yahoo.com/..."` without User-Agent header. Yahoo returns HTML consent page instead of JSON. Python JSON parser throws `JSONDecodeError`. Session debugs, discovers it needs `-H "User-Agent: Mozilla/5.0"`, retries. In the 23:30 session, even the retry failed with a `ValueError` in inline Python formatting.
- **Root cause:** The Mar 24 process review fixed this in `prompts/morning-evaluation.md` only. Post-market sessions use `prompts/post-market-scan.md` and `.pi/skills/post-market/SKILL.md`, neither of which mentioned `yahoo-fetch.py` or `check-prices.py`.
- **Wasted calls:** ~9 failed/retried commands across the 3 sessions
- **Fix:** Added Yahoo Finance data helper section to both `prompts/post-market-scan.md` and `.pi/skills/post-market/SKILL.md`, pointing to `yahoo-fetch.py` and `check-prices.py` with explicit warning against raw `curl`.
- **Status:** Fixed

### 2. websearch extract fails on financial sites
- **Severity:** Minor
- **Sessions affected:** 1 of 9 (23:30 session)
- **Symptom:** `websearch extract "https://www.marketbeat.com/..."` returns HTTP 403. `websearch extract "https://finviz.com/..."` returns "document is not defined" (JS-rendered page).
- **Root cause:** These sites block scraping or require JavaScript rendering. Not fixable from our side.
- **Fix:** None needed. Sessions quickly moved on to alternative data sources. Single occurrence, low cost.
- **Status:** Non-actionable

### 3. Inline Python fragility (continuing from Mar 24 review)
- **Severity:** Minor
- **Sessions affected:** 2 of 9 (21:00, 23:30)
- **Symptom:** Inline `python3 -c "..."` one-liners for Yahoo data parsing hit `ValueError: Unknown format code 'f' for object of type 'str'` when Yahoo returns string values instead of floats.
- **Root cause:** Ad-hoc inline Python is fragile. Yahoo Finance API sometimes returns values as strings.
- **Fix:** Addressed by fix #1 above. Sessions that use `yahoo-fetch.py` and `check-prices.py` avoid writing inline Python for basic data fetching. Remaining edge cases (custom analysis) are low-cost self-corrections.
- **Status:** Partially addressed (by fix #1)

## Improvements Since Last Review

- **python3 / nix-shell workaround:** Zero occurrences. Fully resolved.
- **Morning evaluation sessions:** The 09:20 session used `yahoo-fetch.py` for all 7 Yahoo calls and `check-prices.py` for 2 calls. Zero raw curls. The Mar 24 fix worked.
- **Tavily quota (HTTP 429/432):** Zero occurrences across 9 sessions. Total websearch calls: 32 across the evening window. Either the quota was increased or usage stayed within limits.
- **Scanner script (`scan.py`):** Ran cleanly in all sessions. No argument errors or failures.

## Observations

- Post-market sessions from 22:30 and 23:00 CET ran cleanly with zero errors (6 and 9 tool calls respectively). These sessions only ran the scanner and committed. The heavier sessions (21:00, 21:30, 23:30) that did deeper candidate analysis are where Yahoo curl issues appeared.
- The pattern is clear: fixes applied to one prompt don't propagate to other prompts that need the same information. When fixing a tool usage issue, check all prompts that might use that tool.
