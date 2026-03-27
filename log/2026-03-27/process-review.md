# Process Review — 2026-03-27

## Sessions Reviewed
- 2026-03-27T09:45 (scanner-improvement)
- 2026-03-27T09:20 (morning-evaluation)
- 2026-03-26T23:30 (post-market-scan)
- 2026-03-26T23:00 (post-market-scan)
- 2026-03-26T22:30 (post-market-scan)

Plus 5 additional sessions (20:30-22:00) scanned for timeout patterns.

## Issues Found

### check-prices.py --ah-history timeouts
- **Severity:** Wasteful (sometimes Critical when data is lost entirely)
- **Sessions affected:** 7 out of 10 reviewed
- **Symptom:** `check-prices.py --ah-history TICKER1 TICKER2 ...` hits pi's bash timeout (15-20s) and returns no data. Sessions then waste time retrying with background jobs, direct curl calls, or individual yahoo-fetch.py invocations.
- **Root cause:** The script fetched tickers sequentially, each with a 10s HTTP timeout. With 5-9 tickers, worst case was 50-90 seconds of sequential requests. Pi's bash tool kills the process at 15-20s.
- **Fix:** Added `concurrent.futures.ThreadPoolExecutor` to fetch all tickers in parallel. Total time is now bounded by the slowest single ticker (~10s) regardless of count. Both `--ah-history` and default modes parallelized.
- **Status:** Fixed (scripts/check-prices.py)

### Redundant cd prefixes in bash commands
- **Severity:** Minor
- **Sessions affected:** 4 out of 5 reviewed (8-9 occurrences each)
- **Symptom:** Sessions prepend `cd /home/juan/workspace/juanibiapina/trading &&` to every bash command despite the working directory already being set.
- **Root cause:** LLM behavior, not prompt-driven. The agent doesn't trust the cwd.
- **Fix:** N/A. This is cosmetic token waste (~50 tokens/session). Not worth a prompt instruction that would likely be ignored.
- **Status:** Accepted (minor)

### One-off /dev/stdin coding mistake
- **Severity:** Minor
- **Sessions affected:** 1 out of 10 (2026-03-26T22:30 only)
- **Symptom:** Agent wrote `python3 -c "...open('/dev/stdin')..."` without piping input, causing a JSON parse error. Recovered on next attempt by piping yahoo-fetch output.
- **Root cause:** One-time agent coding error. Not systemic.
- **Fix:** N/A. Not reproducible.
- **Status:** Accepted (one-off)
