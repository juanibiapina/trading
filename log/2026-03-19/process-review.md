# Process Review — 2026-03-19

## Sessions Reviewed

9 sessions from 2026-03-18T20:30 through 2026-03-19T09:45 (excluding the current review session):

- `2026-03-19T09-45` — scanner-improvement (clean)
- `2026-03-19T09-20` — morning-evaluation (6 wasted calls)
- `2026-03-18T23-30` — post-market-scan (clean)
- `2026-03-18T23-00` — post-market-scan (1 wasted call)
- `2026-03-18T22-30` — post-market-scan (5 wasted calls)
- `2026-03-18T22-00` — post-market-scan (clean)
- `2026-03-18T21-30` — post-market-scan (3 wasted calls)
- `2026-03-18T21-00` — post-market-scan (8 wasted calls)
- `2026-03-18T20-30` — post-market-scan (9 wasted calls)

**Aggregate waste: 29 failed tool calls out of 127 total bash calls (22%).**

## Issues Found

### 1. WEBSEARCH_DEFAULT_PROVIDER still not set (repeat from 2026-03-18)
- **Severity:** Wasteful
- **Sessions affected:** 6 out of 9
- **Symptom:** `websearch search` defaults to Tavily, fails with "TAVILY_API_KEY is not set" (14 wasted calls). Sessions then retry with `-p brave`.
- **Root cause:** Only `BRAVE_API_KEY` is set. `WEBSEARCH_DEFAULT_PROVIDER` env var is unset.
- **Fix:** Set `WEBSEARCH_DEFAULT_PROVIDER=brave` in NixOS config or shell profile.
- **Status:** Needs user action (flagged yesterday, not yet resolved)
- **Impact:** This is the single biggest source of waste. It alone accounts for 14/29 (48%) of wasted calls.

### 2. Brave free tier rate limits (429)
- **Severity:** Minor
- **Sessions affected:** 5 out of 9
- **Symptom:** Parallel `websearch search -p brave` calls hit 1 req/sec rate limit (9 wasted calls). Sessions then retry with `sleep` delays.
- **Root cause:** Brave free plan allows 1 request/second. Sessions fire parallel search calls after failing Tavily. This compounds Issue #1: once sessions switch to Brave, they send a burst of requests that triggers 429s.
- **Fix:** Fixing Issue #1 would reduce the burst pattern. Upgrading Brave plan or setting up Tavily would eliminate it. Sessions already learn to add `sleep` delays, so it's self-correcting within a session.
- **Status:** Low priority (self-correcting, worsened by Issue #1)

### 3. Yahoo Finance curl missing User-Agent header
- **Severity:** Wasteful
- **Sessions affected:** 3 out of 9 (morning-eval + two evening sessions)
- **Symptom:** Sessions construct inline `curl -s "https://query1.finance.yahoo.com/..."` without User-Agent. Yahoo returns non-JSON response, causing `json.load()` to throw a Traceback (5 wasted calls). Sessions then discover they need `-H "User-Agent: Mozilla/5.0"` and retry.
- **Root cause:** Sessions copy the URL pattern from Day Trading.md examples and build curl commands from scratch. The existing scripts (`check-prices.py`, `pm-volume-check.py`) already handle this correctly with User-Agent headers, but sessions don't always use them for ad-hoc queries.
- **Fix:** Cannot modify Day Trading.md (user-maintained). However, sessions that need ad-hoc Yahoo data beyond what scripts provide will keep hitting this. A helper script (`scripts/yahoo-chart.py TICKER [interval] [range]`) would give sessions a reliable tool instead of improvising curl.
- **Status:** Candidate for fix (see below)

### 4. websearch extract broken
- **Severity:** Wasteful
- **Sessions affected:** 1 out of 9 (morning-eval), but 100% failure rate when used
- **Symptom:** `websearch extract URL` fails with "document is not defined" for every URL. This is a JS runtime error in the websearch CLI's Readability parser.
- **Root cause:** Broken dependency in the websearch CLI (likely `linkedom` or `jsdom` not working in the current Node.js environment).
- **Fix:** Debug/fix the websearch CLI's extract command, or use an alternative for page extraction (e.g., `curl + python3 html.parser`).
- **Status:** Needs user action (system-level tool is broken)

### 5. Session hallucinated scripts/news.py
- **Severity:** Minor
- **Sessions affected:** 1 out of 9 (21:00 post-market)
- **Symptom:** Session called `python3 scripts/news.py SER MDAI SUNE EONR TPET` which does not exist and has never existed. Got "No such file or directory".
- **Root cause:** The post-market prompt instructs "structured catalyst search" but doesn't specify which tool to use. The session invented a script name.
- **Fix:** The post-market prompt could be more explicit about using `websearch search -p brave` for news lookups. However, this is a one-off hallucination and not worth a prompt change.
- **Status:** No action needed (isolated incident)

## Changes Since Yesterday's Review

Yesterday's review (2026-03-18) identified 4 issues. Status:
1. **WEBSEARCH_DEFAULT_PROVIDER** — NOT fixed (still needs user action)
2. **Brave rate limits** — unchanged (low priority, self-correcting)
3. **Yahoo curl User-Agent** — unchanged (still happening)
4. **Stale brave-search ref in SKILL.md** — Fixed yesterday

New issue today: **websearch extract broken** (#4 above).

## Waste Summary

| Issue | Wasted Calls | % of Total Waste |
|-------|-------------|-----------------|
| Tavily missing key | 14 | 48% |
| Brave 429 rate limit | 9 | 31% |
| Yahoo no User-Agent | 5 | 17% |
| websearch extract broken | 1 | 3% |
| **Total** | **29 / 127** | **22% waste rate** |

## Recommendations (Priority Order)

1. **Set `WEBSEARCH_DEFAULT_PROVIDER=brave`** — eliminates 48% of waste immediately, reduces Brave 429s by eliminating the post-Tavily burst pattern. One line in NixOS config.
2. **Fix `websearch extract`** — or accept it's broken and stop using it. Sessions that need article content can use `curl + python3` instead.
3. **Yahoo helper script** — optional. Would prevent ad-hoc curl improvisation. Low priority since the existing scripts cover most use cases.
