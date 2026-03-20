# Process Review — 2026-03-20

## Sessions Reviewed

4 sessions from 2026-03-19T23:00 through 2026-03-20T09:45:

- `2026-03-20T09-45` — scanner-improvement (25 tool calls, 0 errors)
- `2026-03-20T09-20` — morning-evaluation (29 tool calls, 3 errors + 2 workaround calls)
- `2026-03-19T23-30` — post-market-scan (16 tool calls, 0 errors)
- `2026-03-19T23-00` — post-market-scan (10 tool calls, 0 errors)

**Aggregate waste: 5 wasted calls out of 80 total (6%).**

Down from 22% waste rate yesterday (29/127). Most improvement came from Tavily API key being configured.

## Issues Found

### 1. Yahoo Finance curl still missing User-Agent (repeat from 2026-03-18, 2026-03-19)
- **Severity:** Wasteful
- **Sessions affected:** 1 out of 4 (morning-evaluation)
- **Symptom:** Session constructs `curl -s "https://query1.finance.yahoo.com/..."` without User-Agent header. Yahoo returns non-JSON, causing `json.load()` Traceback. Session then spends 2 calls discovering it needs `-H "User-Agent: Mozilla/5.0"`. Total: 5 wasted calls.
- **Root cause:** Morning eval uses `check-prices.py` (which handles User-Agent) for basic price checks, but then improvises with raw curl for detailed 5m/2d analysis that the script doesn't support. The inline curl always forgets User-Agent.
- **Fix:** Created `scripts/yahoo-fetch.py` - a thin wrapper that fetches Yahoo Finance data with User-Agent and outputs JSON to stdout. Sessions can now pipe this to custom `python3 -c` processing:
  ```
  python3 scripts/yahoo-fetch.py DRMA --interval 5m --range 2d --prepost | python3 -c "..."
  ```
  This replaces the fragile `curl ... | python3 -c "..."` pattern.
- **Status:** Fixed (scripts/yahoo-fetch.py created)

### 2. websearch extract still broken (repeat from 2026-03-19)
- **Severity:** Minor (no session used it today, but still broken)
- **Sessions affected:** 0 out of 4 (not attempted)
- **Symptom:** `websearch extract URL` fails with "Error: document is not defined" for every URL.
- **Root cause:** JS runtime error in the websearch CLI's Readability parser (likely linkedom/jsdom issue).
- **Fix:** Needs debugging of the websearch CLI's Node.js dependencies.
- **Status:** Needs user action (carried forward from 2026-03-19)

### 3. Tavily API key issue — RESOLVED
- **Severity:** Was Wasteful, now fixed
- **Sessions affected:** 0 out of 4 (was 6/9 yesterday)
- **Details:** `TAVILY_API_KEY` is now set. The 23:30 post-market session used `websearch search` without specifying a provider and it worked. This was the single biggest source of waste (48% of wasted calls yesterday). Fully resolved.

## Changes Made

1. **Created `scripts/yahoo-fetch.py`** - Thin wrapper for Yahoo Finance API that includes User-Agent header. Outputs raw JSON to stdout. Supports `--interval`, `--range`, and `--prepost` flags. Sessions that need custom data processing can pipe this to `python3 -c` instead of using raw curl.

## Changes Since Yesterday's Review

| # | Issue | Yesterday | Today |
|---|-------|-----------|-------|
| 1 | Tavily missing API key | 14 wasted calls (48% of waste) | **Resolved** (user set TAVILY_API_KEY) |
| 2 | Brave 429 rate limits | 9 wasted calls | **Not seen** (likely resolved by Tavily fix) |
| 3 | Yahoo curl User-Agent | 5 wasted calls | 5 wasted calls — **Fixed** (yahoo-fetch.py) |
| 4 | websearch extract broken | Broken | Still broken (needs user action) |

## Waste Trend

| Date | Wasted Calls | Total Calls | Waste Rate |
|------|-------------|-------------|------------|
| 2026-03-19 | 29 | 127 | 22% |
| 2026-03-20 | 5 | 80 | 6% |

## No Action Needed

- Post-market sessions (23:00, 23:30) ran cleanly with zero errors
- Scanner-improvement session ran cleanly
- No prompt confusion observed: all sessions followed their prompts correctly
- No stale references found in prompts
