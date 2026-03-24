# Process Review — 2026-03-24

## Sessions Reviewed
- `2026-03-24T09-20` — morning evaluation
- `2026-03-24T09-45` — scanner improvement
- `2026-03-23T23-30` — post-market scan (00:30 CET)
- `2026-03-23T23-00` — post-market scan (00:00 CET)
- `2026-03-23T22-30` — post-market scan (23:30 CET)
- `2026-03-23T21-00` — post-market scan (22:00 CET)
- `2026-03-20T09-20` — morning evaluation (for cross-session pattern comparison)

## Issues Found

### 1. Yahoo Finance curl without User-Agent (recurring)
- **Severity:** Wasteful
- **Sessions affected:** 2 morning evals (Mar 20, Mar 24) — both independently repeat the same discovery
- **Symptom:** Session uses `curl -s "https://query1.finance.yahoo.com/..."` without User-Agent header. Yahoo returns empty body. Python JSON parser throws `JSONDecodeError`. Session debugs, discovers it needs `-H "User-Agent: Mozilla/5.0"`, adds it, retries. Works. On Mar 24 this burned 2 failed calls before the fix. On Mar 20 it burned 3 failed calls plus a debug probe (`curl -o /dev/null -w "%{http_code}"`).
- **Root cause:** `scripts/yahoo-fetch.py` already exists and handles the User-Agent, but no prompt mentioned it. Sessions resort to raw `curl | python3 -c ...` for detailed price action data.
- **Fix:** Added a "Yahoo Finance Data" section to `prompts/morning-evaluation.md` pointing sessions to `yahoo-fetch.py` and explicitly warning against raw `curl`.
- **Status:** Fixed

### 2. Tavily/websearch API quota exhaustion
- **Severity:** Wasteful
- **Sessions affected:** 17 sessions across Mar 11-24 hit HTTP 429 or 432. On Mar 23 evening alone, the 21:00 session (10 websearch calls) and 22:30 session (9 calls) both hit the Tavily plan limit.
- **Symptom:** `websearch search` returns `HTTP 432: This request exceeds your plan's set usage limit` or `HTTP 429: Too Many Requests`. Later sessions in the evening window lose the ability to search for catalysts.
- **Root cause:** Post-market scan prompt instructs a structured 3-step catalyst search (earnings, press releases, SEC filings) per candidate. With 2-3 candidates per scan and 4-5 scans per evening, this generates 20-40 websearch calls per trading day. The Tavily free/basic plan quota is exhausted partway through.
- **Fix:** Needs user action. Options: (a) upgrade Tavily plan, (b) reduce websearch calls per scan by caching catalyst findings across scans (if TICKER was already researched in an earlier scan, skip), (c) use the `-p brave` or `-p exa` provider flags to spread load across providers.
- **Status:** Needs user action

### 3. Inline Python f-string syntax errors
- **Severity:** Minor
- **Sessions affected:** Mar 24 morning eval (2 occurrences)
- **Symptom:** Session writes inline Python like `${h:.2f if h else 0}` which is invalid f-string syntax. Causes `ValueError: Invalid format specifier`. Session self-corrects on next attempt.
- **Root cause:** Complex inline Python snippets for ad-hoc Yahoo data processing are error-prone. The model generates plausible-looking but invalid f-string conditionals.
- **Fix:** Partially addressed by fix #1 (using `yahoo-fetch.py` reduces the need for long inline Python). Remaining occurrences are low-cost self-corrections, not worth further intervention.
- **Status:** Partially addressed

## Non-Issues

- **scan.py `--min-change` argument**: one session tried a non-existent flag, got a clear error, read the script's help, and moved on. Single occurrence, quick recovery, no pattern.
- **ENOENT on `log/2026-03-20/log.md`**: scanner-improvement correctly tried to read recent logs for context. Mar 20 had no trade log (only a process review). Expected behavior, not a bug.
- **Post-market scan sessions (23:00, 23:30)**: ran cleanly with zero errors. Scanner script works reliably.
