# Process Review — 2026-07-28

## Sessions Reviewed
Covers the window since the last review (07-24 14:40 CEST, which closed at 07-24 14:30).
20 workload sessions (times CEST; session files are UTC):

- 2026-07-24 15:00 — strategy-advance (Init 6 mechanical-exit sim, negative at 5-min cadence)
- 2026-07-27 09:00 — email-reply/feedback check (InboxKit queue empty, nothing to log)
- 2026-07-27 11:00 — pm-open scan (3 gappers logged)
- 2026-07-27 15:00 — strategy-advance (Init 3 day-movers census; Init 6 exit-sim refresh)
- 2026-07-27 21:30, 22:00, 22:15, 22:30, 22:45, 23:00, 23:30, 00:00, 00:30 CEST — 9 post-market scans
- 2026-07-28 09:00 — email-reply/feedback check (queue empty)
- 2026-07-28 10:20 — morning evaluation
- 2026-07-28 10:30 — position evaluation
- 2026-07-28 11:00 — pm-open scan (7 gappers logged)
- 2026-07-28 11:30 — daily email (charts committed, email sent — inboxkit id 70, status "sent")
- 2026-07-28 14:20 — scanner improvement (price-floor exclusion tracker + sub-3M fade seed, WLDS)
- 2026-07-28 14:30 — position evaluation

(Excluded this 07-28 14:40 process-review session.)

## Method
- Parsed each session JSONL with the correct schema: `toolResult` is a **message role**, not
  a content block (`message.role == "toolResult"`, with `isError` and `toolCallId` on the
  message). The two prior reviews described a different shape; a block-level scan returns
  nothing, so results were linked back to their `toolCall` by id at message level.
- Counted `isError:true` across the 20 sessions: **4** (2 edit-slips, 1 git lock, 1 benign
  tool-help probe). Each inspected below.
- Grepped every tool output for `command not found` / `Permission denied` / `Traceback` /
  `nix-shell` / `No such file` / `unknown command` / `429`, then separated executions from
  prior-review text quoted in context.
- Widened the `websearch` and `index.lock` counts across all of July to test whether the
  hits are one-offs or a standing pattern.
- Checked cron coverage against four weeks of session timestamps, verified every task has a
  matching commit in `git log`, working tree clean, all 8 prompt-referenced scripts exist.

## Issues Found

### `websearch` invoked without its subcommand, then re-discovered from scratch
- **Severity:** Wasteful
- **Sessions affected:** 11 days in July (31 failed calls + 33 tool-discovery probes ≈ 64
  wasted tool calls); 3 failed calls and 3 probes in this window alone (07-27 22:30, 07-27
  00:00, 07-28 10:20)
- **Symptom:** sessions run `websearch "TICKER news July 27 2026"` and get
  `error: unknown command '...'`. They then probe for the tool — `which websearch ddgr`,
  `websearch --help`, `mcpli`, `cat ~/.agents/skills/web-search/SKILL.md` — before landing
  on the working form. Some also try `mcpli glean search "text"`, which fails with
  `invalid JSON arguments` (glean is Contentful-internal knowledge, not web search).
- **Root cause:** the prompts prescribe catalyst searches but never state the invocation.
  `websearch` requires a subcommand (`websearch search "query"`). Every session that needs
  a news lookup guesses, fails, and re-derives the same answer — the exact "workaround
  never made permanent" class this review exists to catch. Prior reviews missed it because
  the failing calls exit 0 through `2>&1 | head` pipes and so never set `isError`.
- **Fix:** pinned the exact command (with the `-p tavily` retry for HTTP 429) into the three
  prompts that order news lookups:
  - `prompts/post-market-scan.md` — new "Search tool — exact invocation" block above the
    existing search budget
  - `prompts/pm-open-scan.md` — inline syntax on the `catalyst` field
  - `prompts/morning-evaluation.md` — inline syntax on the winner's catalyst lookup
- **Status:** Fixed

### `STRATEGY_ROADMAP.md` edits keep missing their `oldText`
- **Severity:** Wasteful (small)
- **Sessions affected:** 3 of the last 3 strategy-advance runs (07-23, 07-24, 07-27)
- **Symptom:** `Could not find oldText in .../STRATEGY_ROADMAP.md`. Always the **second**
  consecutive edit to that file in the run. Each slip costs a `rg` + a re-read + a re-issued
  edit (3 extra calls); all three self-corrected and the content landed.
- **Root cause:** the second edit's `oldText` is drafted from the stale pre-edit read of a
  long file, as a multi-line block that no longer matches.
- **Fix:** `prompts/strategy-advance.md` now tells the run to batch roadmap changes into one
  edit call and anchor `oldText` on a single short grep-verified line.
- **Status:** Fixed

### Transient `.git/index.lock` collision
- **Severity:** Minor
- **Sessions affected:** 1 (07-27 11:00 pm-open scan)
- **Symptom:** `git stash && git pull --ff-only` failed with
  `Unable to create '.git/index.lock': File exists`.
- **Root cause:** a short-lived external git process (likely an interactive lazygit) held the
  index. The `gitwatch` daemon the session found in `ps` is **not** the culprit — its cwd is
  `/home/juan/Sync/notes`, not this repo.
- **Fix:** none needed. The session probed, saw the lock already gone, retried once and
  proceeded; the scan committed and pushed normally (`1d58440`). Single occurrence in July.
- **Status:** No action

### `websearch` HTTP 429 rate limit
- **Severity:** Minor
- **Sessions affected:** 1 this window (07-28 10:20 morning eval); ~1-2 per active day
  across July
- **Symptom:** `Error: HTTP 429: Too Many Requests` — `"plan":"Free","rate_limit":1`, i.e.
  one request/sec on the default provider, not a quota exhaustion (quota 2000, current ~1).
- **Root cause:** back-to-back searches on the free tier of the default provider.
- **Fix:** the retry instruction (`-p tavily`, then move on) is folded into the search-syntax
  blocks added above, so a 429 no longer ends the lookup or triggers provider hunting. All
  five provider keys (brave, tavily, exa, serpapi, websearchapi) are present in the
  environment — verified `websearch search` works.
- **Status:** Fixed (mitigation)

## Health Checks
- **No blocking errors.** All 20 sessions completed; every task has a matching commit and
  push (strategy-advance ×2, 9 post-market scans, 2 pm-open scans, morning eval, 2 position
  evals, scanner improvement, daily email). Both feedback pulses correctly made no commit —
  the InboxKit unread queue returned `{"messages":[],"nextCursor":null}` on both days.
- **No real retries.** No session issued any identical full-command string 3+ times.
- **Daily email sent.** `send-email-inboxkit.js` returned `{"id":70,"status":"sent"}` to
  juanibiapina@gmail.com in the 07-28 11:30 session.
- **All prompt scripts exist (8):** broker.js, chart.py, check-prices.py, price-timeline.py,
  scan.py, send-email-inboxkit.js, spike-bar.js, yahoo-fetch.py.
- **No cron gaps.** The absences in this window are the standing schedule, not failures: no
  Friday-evening post-market block (07-03, 07-10, 07-17, 07-24 all identical) and a
  Monday shape of feedback + pm-open + strategy-advance only (07-06, 07-13, 07-20, 07-27 all
  identical — Monday has no prior-night AH session to evaluate). 07-27 evening ran the full
  9-scan block; 07-28 ran the full morning-through-midday pipeline.
- **No command-not-found / permission / nix-shell / traceback executions.** The only such
  string matches are prior-review text this session read into context.
- **`scheduler.json` path fix (07-21) holds.** No session re-hunted for it.
- **python3/nix-shell loop stays closed.** Resolved 2026-03-24. Not re-verified.
- **Orphan file (cosmetic, unchanged):** `scripts/send-email.js` remains unreferenced by any
  prompt (pipeline uses `send-email-inboxkit.js`). Dead but harmless.

## Needs From Juan
Nothing. All four findings were fixable inside the prompts; no system packages, PATH, or
NixOS changes required.

## Summary
Two real process defects, both fixed in prompts. The `websearch` one is the significant
find: ~64 tool calls burned across 11 days of July on a missing subcommand and the
tool-hunting that followed it, invisible to the last two reviews because the failures exit 0
through pipes. Correct syntax and the 429 retry are now written into the three prompts that
order news lookups. The `STRATEGY_ROADMAP.md` edit-slip has hit three consecutive
strategy-advance runs and now has a named avoidance in that prompt. The git lock was a
one-off external collision (not gitwatch, which watches a different repo) and needs no fix.
Cron coverage, commits, scripts and the daily email are all clean.
