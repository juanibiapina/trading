# Process Review — 2026-07-14

## Sessions Reviewed
Covers the window since the last review (07-10 14:40 CEST, which closed at 07-10 14:30).
07-11 (Sat) and 07-12 (Sun) had no sessions (markets closed). 18 sessions
(times CEST; session files are UTC):

- 2026-07-10 15:00 — strategy-roadmap (Init 6(b) exit-cost writeup)
- 2026-07-13 09:00 — email-reply check
- 2026-07-13 11:00 — (pre-market / setup)
- 2026-07-13 15:00 — strategy-roadmap
- 2026-07-13 21:30, 22:00, 22:30, 23:00, 23:30, 00:00, 00:30 — 7 post-market scans
  (LVLU entered 23:01 @ $11.03)
- 2026-07-14 09:00 — email-reply check
- 2026-07-14 10:20 — morning evaluation (88.6% detection, baseline MET)
- 2026-07-14 10:30 — position evaluation
- 2026-07-14 11:00 — pm-open scan (4 gappers, 0 orders)
- 2026-07-14 11:30 — daily email
- 2026-07-14 14:20 — scanner improvement (broker-blocked gating)
- 2026-07-14 14:30 — position evaluation (LVLU HOLD)

(Excluded this 07-14 14:40 process-review session.)

## Method
- Parsed each session JSONL, linking `toolResult` (`isError:true`) back to its
  originating `toolCall` via `toolCallId` to separate real bash/edit failures from
  benign chained-command exit codes and doc quotes.
- Inspected every `isError` result's command and output.
- Counted bash calls per session; checked for any identical full-command string issued
  3+ times (real-retry detection). Zero found.
- Verified prompt-referenced scripts exist and spot-checked session completion/commits.

## Issues Found

### `broker.js clock` — non-existent subcommand, re-discovered workaround (FIXED)
- **Severity:** Wasteful
- **Sessions affected:** recurring — 07-14 14:30 this window, plus 07-03 (x2), 07-07,
  07-08, 07-09 in prior windows. Never referenced by any prompt; it's an ad-hoc pattern
  sessions keep reaching for when they need the market phase / server time.
- **Symptom:** Sessions run `node scripts/broker.js clock`. broker.js had no `clock`
  subcommand, so it printed the usage header and exited nonzero. The command was always
  chained as `broker.js clock 2>/dev/null || curl <yahoo chart> | python3 -c ...`, so it
  fell through to a Yahoo fallback that threw a `Traceback` (the "Yahoo ||-fallback
  traceback class" flagged as dormant in prior reviews — it recurred here). The 07-14
  14:30 position eval recovered by deriving the phase from SIP bars and completed (LVLU
  HOLD), but every occurrence burns a failed command + a failing fallback.
- **Root cause:** Alpaca exposes a `/v2/clock` endpoint (is_open, next_open, next_close,
  timestamp) but broker.js never wrapped it. Sessions assumed the subcommand existed and
  re-invented a brittle Yahoo workaround each time instead of a permanent tool.
- **Fix:** Added a `clock` subcommand to `scripts/broker.js` wrapping Alpaca `/v2/clock`
  (with `--json`). Verified: `node scripts/broker.js clock` →
  `now <ts> | is_open=false | next_open ... | next_close ...`, exit 0. Sessions now get
  the market clock in one reliable call; no Yahoo fallback, no traceback.
- **Status:** Fixed

### Edit-slips — 2 slips in 1 session (steady, below threshold)
- **Severity:** Minor
- **Sessions affected:** 1 of 18 reviewed
- **Symptom:** Two schema rejections on `edit` (`edits.0` / `edits.1: must not have
  additional properties`), both in the 07-10 15:00 strategy session on
  `INIT6_EXIT_COST.md`. Each was a distinct edit; both retried clean on first attempt.
  Session completed and committed.
- **Root cause:** Agent-side schema serialization on edit payloads — the recurring
  edit-slip class tracked since 06-10, plain additional-properties flavor.
- **Context:** Watch threshold is "escalate if the *same* edit fails twice, or slips
  cluster within a normal-length automated session." Neither happened; both
  self-corrected with no token blowup. Slip count 6 → 2 → 2 over the last three reviews;
  the evening post-market log.md-append cluster did not recur this window. Below
  threshold, not actionable.
- **Fix:** None. Self-corrected. Keep watching.
- **Status:** No action (self-corrected)

## Health Checks
- **No blocking errors.** All 18 sessions completed and committed/pushed where expected
  (strategy advances, 7 post-market scans with LVLU entered, email checks, morning eval,
  both position evals, pm-open scan, daily email, scanner improvement).
- **No real retries.** Zero sessions issued any identical full-command string 3+ times.
- **Three benign bash `isError` results (not real failures):**
  - 07-13 09:00 email-reply — `for t in EHGO MIMI SKYQ AURE; do rg -l "$t" ...; done`.
    Last ticker had no match so the loop's final `rg` returned 1; headers printed fine.
    Expected grep-no-match exit code.
  - 07-14 10:20 morning eval — `grep -l "Days tracked:" ... | tail -1 | xargs grep -E ...;
    ls -d ...; ls log`. Baseline extracted correctly; a trailing chained `ls`/`grep`
    returned nonzero. Benign.
  - 07-14 11:30 daily email — `ls -la log/2026-07-13/process-review.md 2>&1 && ...`.
    That file legitimately doesn't exist (07-13 was Sunday, no review ran), so `ls`
    returned 2 and the chained CHANGELOG read was skipped; the session re-fetched and
    completed. Benign existence probe.
- **No command-not-found / permission errors.** Zero across the window.
- **No stale references.** All seven prompt-referenced scripts exist (broker.js, chart.py,
  check-prices.py, price-timeline.py, scan.py, send-email-inboxkit.js, yahoo-fetch.py).
- **No cron gaps.** 07-13 evening ran the full 7-scan post-market block; 07-14 ran the
  complete morning-through-midday pipeline. 07-11/07-12 idle as expected (weekend).
- **python3/nix-shell loop stays closed.** Resolved 2026-03-24 (commit `2638c3b`).
  Not re-verified.
- **Orphan file (cosmetic, unchanged):** `scripts/send-email.js` remains unreferenced by
  any prompt (pipeline uses `send-email-inboxkit.js`). Dead but harmless.

## Summary
One real fix this window: `broker.js` gained a `clock` subcommand wrapping Alpaca
`/v2/clock`. Sessions had been reaching for a non-existent `broker.js clock` and
re-inventing a brittle Yahoo curl fallback (which threw a traceback) across at least five
prior sessions — a re-discovered workaround, exactly the class this review hunts for. Now
a permanent one-call tool. Otherwise clean: two self-correcting edit slips in one strategy
session (below threshold, log.md-append cluster did not recur), three benign
chained-command exit codes, no blocking errors, no real retries, no missing scripts, no
cron gaps.
