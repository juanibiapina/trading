# Process Review — 2026-07-29

## Sessions Reviewed
Window since the last review (07-28 14:40 CEST, which closed at 07-28 14:30).
16 workload sessions (times UTC as in the session files; CEST = UTC+2):

- 2026-07-28 19:30, 20:00, 20:15, 20:30, 20:45, 21:00, 21:30, 22:00 — 8 post-market scans
- 2026-07-29 07:00 — email-reply/feedback check (queue empty, no commit)
- 2026-07-29 08:20 — morning evaluation
- 2026-07-29 08:30 — position evaluation
- 2026-07-29 09:00 — pm-open scan (4 gappers logged)
- 2026-07-29 09:30 — daily email (sent — inboxkit id 73, status "sent")
- 2026-07-29 12:20 — scanner improvement (Yahoo prev-close anchoring flag in check-prices.py)
- 2026-07-29 12:30 — position evaluation

(Excluded this 12:40 process-review session.)

## Method
- Parsed each JSONL with the correct schema: `assistant` messages carry `toolCall`
  blocks (`{type, id, name, arguments}`); separate `toolResult` messages hold the output
  and `isError`. Linked results to calls by `toolCallId`.
- Counted `isError:true` across the 16 sessions: **0**.
- Grepped every tool output for `command not found` / `Permission denied` / `Traceback` /
  `nix-shell` / `No such file` / `403 Forbidden` / `429` / `Could not find oldText` /
  `index.lock`, then split executions from prior-review text read into context. The
  daily-email (09:30) and this process-review session both read 07-28's process-review.md,
  which is why the nix-shell/traceback/permission strings appear — all **quoted, not run**.
- Verified every workload task has a matching commit in `git log` and the daily email sent.

## Issues Found

### `spike-bar.js` forces `--feed sip`, killing broker.js's IEX auto-fallback (opaque 403)
- **Severity:** Wasteful
- **Sessions affected:** every early-AH post-market scan. The 07-28 20:00 scan (16:00 ET,
  AH open) diagnosed it from scratch and wrote the analysis into that day's log; the 403
  recurs in 8 of the sessions this window (20:00 ×4 then ×1 across the later scans, plus the
  08:20 morning eval and 09:30 daily email).
- **Symptom:** during the first ~15-20 min of after-hours, `spike-bar.js` returns
  `SYM DATE: ERROR Command failed: node .../broker.js bars ... --feed sip`. The real cause
  (`403 Forbidden: subscription does not permit querying recent SIP data`) is buried on a
  later stderr line, so the surfaced message hides why it failed and a session re-diagnoses
  it each early-AH scan.
- **Root cause:** the Alpaca free tier blocks the most recent ~15 min of SIP, which at
  16:00 ET is the entire AH window. `broker.js bars` already auto-falls back to IEX on that
  exact 403 — **but only when `--feed` is not passed** (`if (feed === "sip" && !flags.feed
  && /recent SIP data/i.test(...))`). `spike-bar.js`'s `bars()` helper hard-coded
  `feed = "sip"` and always appended `--feed sip`, which set `flags.feed` and suppressed the
  fallback, turning a recoverable condition into an opaque throw.
- **Fix:** changed `spike-bar.js` `bars()` to default `feed = null` and only append `--feed`
  when a non-default feed is explicitly requested. broker.js still defaults to SIP, so
  historical reads are unchanged, but recent-window calls now auto-fall back to IEX. Verified:
  before, `broker.js bars AAPL --start <-5min> --feed sip` → 403; without `--feed` → IEX bars
  returned. After the edit, `spike-bar.js` on a live recent window no longer emits the opaque
  `Command failed`, and the historical regression (`AMIX:2026-07-28 --now 20:00`) still
  reports `SPIKE 16:03ET +24% $3.40` unchanged.
- **Status:** Fixed

### `websearch` HTTP 429 on the default provider (mitigation holds)
- **Severity:** Minor
- **Sessions affected:** every search-heavy scan (10 of the reviewed sessions hit ≥1 429).
- **Symptom:** `Error: HTTP 429: Too Many Requests` (`"plan":"Free","rate_limit":1`) on
  back-to-back `websearch search` calls.
- **Root cause:** the default provider's free tier allows one request/sec; scans fire several
  catalyst lookups in a row.
- **Fix:** none needed this window. The 07-28 fix (correct `websearch search "…"` syntax plus
  a `-p tavily` retry) is working: every session used the right subcommand and retried
  through the 429 with `-p tavily`, then continued. Cost is ~1-2 wasted default-provider
  calls per search-heavy session. A future option is to pin `-p tavily` as the default in the
  prompt syntax blocks, but that risks moving the rate limit onto tavily and would churn
  prompts one day after the last change — not acting.
- **Status:** No action (documented mitigation holds)

## Health Checks
- **No blocking errors.** All 16 sessions completed. Every task has a matching commit/push
  (8 post-market scans, morning eval, 2 position evals, pm-open, scanner improvement) and the
  daily email sent (`send-email-inboxkit.js` → `{"id":73,"status":"sent"}`). The feedback
  pulse correctly made no commit (unread queue empty).
- **No real retries.** No session issued any identical full-command string 3+ times.
- **`websearch` subcommand fix (07-28) holds.** Every lookup used `websearch search "…"`;
  no bare-`websearch` `unknown command` executions and no tool-hunting probes. The only
  `unknown command` string matches are the warning text now baked into the scan prompts.
- **`403 Forbidden` on `--feed sip` was the spike-bar issue above** — no other 403s. broker.js
  itself falls back correctly when called without `--feed`.
- **No command-not-found / permission / nix-shell / traceback executions.** All such matches
  are 07-28 process-review text quoted into the daily-email and this session's context.
- **All prompt scripts exist (8):** broker.js, chart.py, check-prices.py, price-timeline.py,
  scan.py, send-email-inboxkit.js, spike-bar.js, yahoo-fetch.py.
- **python3/nix-shell loop stays closed.** Resolved 2026-03-24. Not re-verified.
- **Orphan file (cosmetic, unchanged):** `scripts/send-email.js` remains unreferenced by any
  prompt. Dead but harmless.

## Needs From Juan
Nothing. The one real defect was fixable in `scripts/spike-bar.js`; no system packages,
PATH, or NixOS changes required.

## Summary
One real process defect, fixed: `spike-bar.js` hard-coded `--feed sip`, which disabled the
IEX auto-fallback broker.js already implements for the free-tier recent-SIP 403, so every
early-after-hours run failed with an opaque `Command failed` that a session then
re-diagnosed. Dropping the forced `--feed` restores the fallback; historical spike detection
is unchanged. The 07-28 `websearch` subcommand fix holds cleanly, and its 429 retry
mitigation carries every session through the free-tier rate limit. Commits, scripts, cron
coverage and the daily email (id 73) are all clean.
