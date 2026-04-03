# Process Review - 2026-04-03

## Sessions Reviewed

- `2026-04-03T12-20` - scanner-improvement (5 bash calls, clean)
- `2026-04-03T12-00` - morning-evaluation pulse 3 (17 bash calls, 10 inline python)
- `2026-04-03T10-00` - morning-evaluation pulse 2 (11 bash calls, 2 inline python)
- `2026-04-03T09-30` - daily-email (15 bash calls, 1 grep failure)

## Issues Found

### 1. Inline Python Data Processing (Still Ongoing, Now Fixed)

- **Severity:** Wasteful
- **Sessions affected:** 2 out of 4 (both morning-evaluation sessions)
- **Symptom:** Morning evaluation sessions call `check-prices.py` (default summary mode), find it insufficient for timeline analysis, then fall back to `yahoo-fetch.py | python3 -c "import json, sys; ..."` with 10-40 line inline scripts to parse raw JSON into formatted price timelines.
- **Scale today:**
  - Pulse 3 (12:00): 10 inline python calls out of 17 total (59% of tool calls). Cost: $1.45 total session.
  - Pulse 2 (10:00): 2 inline python calls out of 11 total (18%). Cost: $1.06 total session.
- **Root cause:** The morning-evaluation prompt explicitly said "Pipe output to `python3 -c '...'` for custom processing." Meanwhile, `check-prices.py --ah-history` already provided formatted AH timelines, and no equivalent existed for premarket data.
- **Fix applied:**
  1. Added `--pm-history` flag to `scripts/check-prices.py` (premarket timeline, 04:00-09:30 ET, matching `--ah-history` format)
  2. Updated `prompts/morning-evaluation.md` to direct sessions to `--ah-history` and `--pm-history` instead of inline python parsing
- **Status:** Fixed. Tomorrow's morning sessions should use the built-in modes instead of writing ad-hoc parsers.

### 2. Email Session P&L Grep Failure

- **Severity:** Minor
- **Sessions affected:** 1 out of 4 (daily-email session)
- **Symptom:** `grep -r "Paper Trade|paper trade" log/...` returned exit code 1 (no matches). Session recovered with 2 alternative grep patterns, then computed P&L from matched data.
- **Root cause:** P&L format varies across log files (sometimes "Total Paper P&L", sometimes in tables). The grep pattern didn't match the actual format in the most recent logs.
- **Fix:** Not worth fixing. The session recovered in 2 calls, and P&L formatting naturally evolves. A brittle script would break worse.
- **Status:** Monitoring (no action needed)

## Previously Reported Issues

- **Dirty working tree / stash dance (Apr 2):** Resolved. Working tree is clean, no stash needed. A leftover `stash@{0}` exists but doesn't cause problems.
- **python3 on PATH:** Still resolved. All sessions run python3 directly, zero nix-shell workarounds.
- **check-prices.py timeouts:** Still resolved. Zero timeouts.
- **Email date logic:** Still working correctly.

## Changes Made

1. Added `--pm-history` flag to `scripts/check-prices.py` (premarket timeline matching existing `--ah-history`)
2. Updated `prompts/morning-evaluation.md`: replaced "pipe to python3 -c" guidance with references to `--ah-history` and `--pm-history` modes

## Summary

One fix applied (add `--pm-history` + update prompt) targeting the dominant waste pattern: 12 inline python calls across 2 sessions, consuming 59% of tool calls in the worst case. This was the same issue flagged yesterday but now has a permanent fix rather than just a "needs user action" tag.
