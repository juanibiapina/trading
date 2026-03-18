# Process Review — 2026-03-18

## Sessions Reviewed
- `2026-03-18T09-45` — scanner-improvement
- `2026-03-18T09-20` — morning-evaluation
- `2026-03-17T23-30` — post-market-scan
- `2026-03-17T23-00` — post-market-scan

Also spot-checked 6 older sessions (Mar 16-17) to confirm patterns.

## Issues Found

### 1. websearch defaults to Tavily but only Brave API key is configured
- **Severity:** Wasteful
- **Sessions affected:** 4 out of 4 reviewed (and 6/6 older sessions checked)
- **Symptom:** Every session's first `websearch search` call fails with `Error: TAVILY_API_KEY is not set`. The session then discovers it needs `-p brave` and retries. Some sessions also probe `-p exa` and `-p websearchapi`, which also fail (no keys set). This wastes 1-3 tool calls per session.
- **Root cause:** The `websearch` CLI defaults to Tavily as the search provider. Only `BRAVE_API_KEY` is set in the environment. The env var `WEBSEARCH_DEFAULT_PROVIDER` (which overrides the default) is not set.
- **Fix:** Set `WEBSEARCH_DEFAULT_PROVIDER=brave` in the shell environment (e.g., in NixOS config or `.bashrc`). This makes `websearch search` use Brave by default, eliminating the Tavily error entirely.
- **Status:** Needs user action — environment variable needs to be set system-wide so pi sessions inherit it.

### 2. Parallel websearch calls hit Brave rate limit
- **Severity:** Minor
- **Sessions affected:** 3 out of 4 reviewed
- **Symptom:** Sessions fire 2-3 `websearch search -p brave` calls in parallel. The Brave free plan limits to 1 request/second, so concurrent calls get `HTTP 429: Too Many Requests`. Sessions then retry individually, wasting calls and time.
- **Root cause:** The agent sends independent search queries in parallel (which is normally efficient), but the Brave free tier rate limit is 1 req/sec.
- **Fix:** This is a model behavior issue. Once Issue #1 is fixed (Brave becomes default), the pattern should stay the same but at least the first failed-then-retried batch won't compound. No prompt change needed since the rate limit errors are recoverable and the agent handles them.
- **Status:** Low priority — recoverable errors, minimal waste after Issue #1 is fixed.

### 3. Yahoo Finance curl calls missing User-Agent header
- **Severity:** Wasteful
- **Sessions affected:** 2 out of 4 reviewed (the two evening sessions)
- **Symptom:** Evening sessions use raw `curl -s "https://query1.finance.yahoo.com/..."` without a User-Agent header. Yahoo returns `Edge: Too Many Requests` (plain text, not JSON). When piped to `python3 -c "json.load(sys.stdin)"`, this causes `JSONDecodeError`. The session then discovers it needs `-H "User-Agent: Mozilla/5.0"` and retries.
- **Root cause:** The morning session uses `python3 scripts/check-prices.py` (which includes User-Agent), but evening sessions make ad-hoc curl calls without it. The Day Trading.md Yahoo API docs don't mention the User-Agent requirement.
- **Fix:** The scripts (`scan.py`, `check-prices.py`) already handle this correctly with `urllib.request` + User-Agent header. The issue is only with ad-hoc curl usage. No code fix needed since prompts already point to the scripts. Sessions using inline curl is just model improvisation.
- **Status:** No action needed — the scripts handle it correctly. Would only recur if sessions use raw curl instead of the provided scripts.

### 4. Stale brave-search reference in post-market SKILL.md
- **Severity:** Minor
- **Sessions affected:** 0 (no session used this code path, but it's a latent bug)
- **Symptom:** `.pi/skills/post-market/SKILL.md` references `~/.agents/skills/brave-search/search.js` for news searching, but that file doesn't exist (the directory only contains `node_modules/`). If a session followed this instruction, it would fail.
- **Root cause:** The brave-search skill was apparently replaced by the `websearch` CLI, but the post-market SKILL.md wasn't updated.
- **Fix:** Updated SKILL.md to use `websearch search` instead.
- **Status:** Fixed

## Summary

| # | Issue | Severity | Status |
|---|-------|----------|--------|
| 1 | websearch defaults to unconfigured Tavily | Wasteful | Needs user action: set `WEBSEARCH_DEFAULT_PROVIDER=brave` |
| 2 | Parallel websearch hits Brave rate limit | Minor | No action needed (recoverable) |
| 3 | Yahoo curl missing User-Agent | Wasteful | No action needed (scripts handle it) |
| 4 | Stale brave-search ref in SKILL.md | Minor | Fixed |
