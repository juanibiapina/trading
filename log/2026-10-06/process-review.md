# Process Review — 2026-10-06

## Sessions Reviewed

Five most recent completed work sessions, timestamps UTC (scheduled start → actual finish):

- 2026-10-06 08:20 → 10:58 — morning evaluation (`01a1104c`)
- 2026-10-06 09:00 → 10:47 — premarket-open scan (`01a11070`)
- 2026-10-06 09:30 → 11:01 — daily email (`01a1108c`)
- 2026-10-06 12:20 → 12:28 — scanner improvement (`01a11128`)
- 2026-10-06 12:30 → 12:30 — position evaluation (`01a11131`)

Also checked for the outage and initiative progress:

- Oct 6 07:00 feedback check, 08:10 Initiative 6 cohort, 08:30 position evaluation (all resumed at 10:44)
- Oct 5 07:00 feedback check, 08:10 cohort, 09:00 premarket-open scan (completed)
- Oct 5 13:00 and 16:00 strategy advance, and all 13 Oct 5 post-market scans (all failed)
- Oct 2 13:00 and 16:00 strategy advance (latest completed strategy runs)

Excluded this review (started 12:40). Read the Oct 1 and Oct 2 process reviews first; issues they closed are omitted.

## Issues Found

### Expired Anthropic login stopped every scheduled session for 21.7 hours

- **Severity:** Critical
- **Sessions affected:** 15 of 15 sessions from Oct 5 13:00 to 22:30 failed. On Oct 6, 6 of 9 sessions ran 1.5–3.7 hours late.
- **Symptom:** Every session from Oct 5 13:00 failed on its first model call with `OAuth refresh failed for anthropic: invalid_grant, Refresh token expired`. The failures: 0 of 13 post-market scans ran, and both Oct 5 strategy runs ended within 16 seconds. OLOX, the cycle's winner, went +155% in premarket; the email's SIP replay shows it would have passed every gate at 23:00 CEST, with a simulated +63.9%. Oct 6 morning sessions kept retrying until the login was restored at 10:42 and resumed at 10:44.
- **Root cause:** Dotfiles commit `ba155f3c` (Oct 5 11:40 CEST) switched the global pi default from `openai-codex/gpt-6.1-sol` to `anthropic/claude-opus-5-5`. These sessions had last used Anthropic on Sep 16, and its stored refresh token had expired. Nothing tested the provider before the 15:00 CEST strategy run used it.
- **Recurrence:** This is the third provider failure in 14 days to stop scheduled scans: Sep 22 Codex usage limit (7 sessions), Sep 29 OpenAI token invalidated (5 sessions), Oct 5–6 (21 sessions). Earlier reviews called Sep 29 transient and said to escalate if it recurred.
- **Fix (needs user action):** The fix is in bridge or dotfiles code, outside the trading repo:
  1. Treat login errors (`invalid_grant`, `Refresh token expired`, `authentication token has been invalidated`) as permanent. Stop retrying and send one Telegram alert naming the provider and asking for a re-login. Today each retry posts its own warning (`apps/bot/src/session/session.ts`, `auto_retry_start`), which made about 200 warnings on Oct 6.
  2. Let scheduled pulses fall back to the other enabled provider when a login error occurs. `settings.json` already enables both `openai-codex/gpt-6.1-sol` and `anthropic/claude-opus-5-5`. A fallback would have run all 13 Oct 5 scans.
  3. After changing the default provider, make one test call before the next scheduled pulse.
- **Decision for Juan (daily email):** approve items 1–3, or pick a subset. Item 2 decides which model runs the trading pulses during an outage.
- **Status:** Needs user action

### Unlimited retries resume pulses late and all together

- **Severity:** Wasteful, with a trading risk
- **Sessions affected:** 6 of 9 Oct 6 sessions
- **Symptom:** Dotfiles commit `cc5dc639` (Oct 5 17:54 CEST) set `retry.maxRetries: 100000` with a 300-second cap. The six morning sessions made 21–51 failed attempts each (204 in total). They all resumed within the same minute, 10:44 UTC. The effects:
  - The Initiative 6 cohort was lost; its 04:07–04:14 ET guard correctly refused to write at 06:44 ET.
  - The premarket-open scan ran at 06:44 ET instead of about 05:00.
  - The daily email spent five `sleep 50`–`sleep 58` calls waiting for the morning evaluation to finish.
  - Two concurrent `git pull` calls failed (see the next issue).
- **Risk now present:** a post-market pulse caught in an outage could resume the next morning. It would then work out today's date, scan premarket data as if it were after-hours, and could submit orders. Pulses resuming together inside the after-hours window could each enter the same symbol before any of them logs the entry.
- **Fix:** Added a late-start guard to `prompts/post-market-scan.md`. If the ET time is outside 15:25–20:00 on a weekday, the pulse logs a one-line skip and stops without scanning or ordering. Also added a check before each buy: `broker.js positions` and `orders all`, skipping any symbol that already has a position, an open buy, or a buy filled today. This enforces the existing one-entry-per-candidate rule; entry rules are otherwise unchanged. The retry policy itself is covered by item 1 above.
- **Status:** Fixed in the prompt; the policy change needs user action

### Concurrent syncs failed with "Cannot rebase onto multiple branches"

- **Severity:** Minor
- **Sessions affected:** 2 of 9 Oct 6 sessions (08:30 position evaluation and 09:00 premarket-open scan, both at 10:44:02)
- **Symptom:** `bash scripts/sync-repo.sh` exited with `fatal: Cannot rebase onto multiple branches`; the position evaluation's plain `git pull --ff-only` failed the same way. Both recovered with a manual `git fetch`. Later sessions quoted the error from the log but did not hit it again.
- **Root cause:** Overlapping `git pull` fetches append to `FETCH_HEAD`, and the global `pull.rebase=true` makes pull refuse multiple heads. In a scratch clone, six concurrent `git pull --ff-only` calls failed 77 of 90 times.
- **Fix:** `scripts/sync-repo.sh` now holds a `flock` on `.git/sync-repo.lock` for the whole sync (waiting up to 120 s). It retries `Cannot rebase onto multiple branches` and `cannot lock ref` like the existing `index.lock` case, and pops a stash only when this run created one.
- **Verification:** Same scratch setup with upstream commits each round: 90 of 90 concurrent syncs exited 0 and reached the remote head. A local edit survived a sync, and an older unrelated stash was left in place. `bash -n` passed.
- **Status:** Fixed

### Python calls to InboxKit get HTTP 403

- **Severity:** Minor
- **Sessions affected:** 3 sessions over 8 days (Sep 29 email, Oct 2 and Oct 5 feedback checks)
- **Symptom:** Each session rewrote the prompt's curl poll in Python `urllib`, got `HTTP Error 403: Forbidden`, then rebuilt the call with curl.
- **Root cause:** Cloudflare blocks Python `urllib`'s default User-Agent (`error code: 1010`). Tested without the API key: the default agent returned 403/1010, while `curl/8.9.1` and a custom agent reached the API (401, missing auth).
- **Fix:** `prompts/check-email-replies.md` now says to use its curl commands and explains the 403, including the need for a `User-Agent` header in Python.
- **Status:** Fixed

## Initiative Progress and Email Coverage

- **Strategy runs:** the Oct 2 15:00 and 18:00 runs both delivered: the Jev shadow classifier, the frozen Initiative 7 comparison, the SGRX full-session closure, and the completed Oct 1 replay. They also finished all Oct 2 process-review handoffs. Both Oct 5 runs failed at their first model call because of the login outage, so none of their work was skipped by choice.
- **Now overdue because of the outage:** the Initiative 7 SEC primary-source archiver and issuer mapping (due Oct 5 15:00), the Initiative 1 sparse-baseline policy against INLF/GIPR/YFOR (due Oct 5 15:00), and Initiative 7 observation orchestration (due Oct 5 18:00). The Initiative 3 later-rebuild comparison (due Oct 6 15:00) was planned to follow these.
- **Latest completed email:** InboxKit message 179, sent `2026-10-06T11:00:54Z`. Its window runs from receipt 178 (`2026-10-02T09:37:06Z`), which the receipt-first lookup found without a session search. It gives dated updates for Initiatives 7, 6, 3 and 4, and names the missed Initiative 1 and 7 deliveries, Initiative 5's dependency and Initiative 2's broker deferral. The Jev section reports 6 calls, 5,471/931 tokens and the estimated cost. No initiative that moved is missing.
- **Gap for the next email:** message 179 says the outage had not yet been reviewed. The next email should report this review's root cause, the fixes, and the decision for Juan above.

## Handoff to Strategy Advance

1. **Oct 6 15:00:** deliver the oldest overdue item, the Initiative 7 SEC archiver and issuer mapping, with a real capture or the actual access failure. Run the Initiative 1 sparse-baseline policy in parallel. If both don't fit, record which one moves to 18:00 and why.
2. **Oct 6 18:00:** Initiative 7 observation orchestration. If the Initiative 3 later-rebuild comparison is displaced again, give it a dated slot.
3. **Initiative 6:** record Oct 6 as a day without a cohort (lost to the outage, not a data result). The Oct 5 cohort's quotes were about 60 hours old (taken Monday). Use the RUBI (Oct 6), SAIQ and QTEX (Oct 5) observations for the discovery and gate check.
4. **Initiative 3:** add the outage record (provider failures on 3 of 8 scheduled nights) and the new late-start guard to the scheduling evidence. The DST loading check before Oct 25 still stands.

Initiative 2's broker test stays deferred per Juan's Sep 22 instruction.

## Additional Checks

- The bounded context reads from the Oct 2 review are in use. Roadmap reads start at the current checkpoint (line 1695) and initiative-log reads stop at 64 lines. Context-file reads were 18–48 KB per session today, against 148–239 KB on Oct 1–2.
- The timeline fixes held: the Oct 6 morning evaluation printed correct ET labels (`[PM] 10-06 05:35 ET`) and committed without whitespace failures.
- Apart from the provider retries, no failing command was retried 3 or more times. The other non-zero exits were expected: empty directory probes, and the scanner improvement's deliberate tests of bad `book-check.js` flags.
