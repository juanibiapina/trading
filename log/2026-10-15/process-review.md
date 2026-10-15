# Process Review — 2026-10-15

## Sessions Reviewed

All 23 work sessions since the Oct 14 review, timestamps UTC:

- 2026-10-14 13:00 and 16:00 — strategy advance
- 2026-10-14 19:30 → 22:30 — 13 post-market scans
- 2026-10-15 07:00 feedback check, 08:10 Initiative 6 cohort, 08:20 morning evaluation, 08:30 position evaluation, 09:00 premarket-open scan, 09:30 daily email, 12:20 scanner improvement, 12:30 position evaluation

This review (12:40) is excluded. I read the Oct 13 and Oct 14 reviews first; issues they closed are omitted. 22 sessions finished and pushed; the 13:00 strategy run died mid-call (first issue). No provider errors.

## Issues Found

### Strategy run died inside a 28-minute wait and lost its log entry

- **Severity:** Wasteful
- **Sessions affected:** 1 of 2 strategy runs (Oct 14 13:00)
- **Symptom:** the run applied Initiative 3's hold retirement, froze the Initiative 7 fade test, committed and pushed (77991ce), then started one bash call that looped `sleep 60` up to 28 times waiting for gob `XCM`. The session stopped at 13:19 with that call unanswered. The `INITIATIVE_LOG.md` entry was never written; the 16:00 run reconstructed it from the commit.
- **Root cause:** the prompt says nothing about long jobs, so the run put its log entry after a long blocking wait. The kill cause is not visible in the session file. The Oct 13 run waited 48 minutes in short polls and survived.
- **Fix:** [prompts/strategy-advance.md](../../prompts/strategy-advance.md) step 4 now says to start long jobs with `gob add`, write the log entry and commit before waiting, poll in calls of 5 minutes or less, and leave a job that outlasts the run for the next run.
- **Status:** Fixed

### Final-scan feed-lag cross-check is rebuilt by hand and truncated by the bar limit

- **Severity:** Wasteful
- **Sessions affected:** 5 of the last 6 final (22:30) scans built a shell loop over tracked names; Oct 13 and Oct 14 each needed a second loop
- **Symptom:** the prompt tells the final scan to check every tracked name with `broker.js bars SYM --tf 5Min --start <AH-start-UTC>`. `bars` defaults to `--limit 20`, so a loop starting at 16:00 ET stops at 17:35 ET, an hour before the 18:30 ET scan. Oct 13 and Oct 14 printed "lastAH (21:35Z)" and re-ran the loop with a later start. The Oct 14 loop also piped to `bc`, which is not installed, so its volume column came out empty.
- **Root cause:** no script for the check, and `broker.js bars` gave no sign that it had cut off bars.
- **Fix:**
  - New [scripts/ah-crosscheck.js](../../scripts/ah-crosscheck.js): `node scripts/ah-crosscheck.js SYM ...` prints close, latest SIP AH bar and time, AH high, AH%, AH volume, last-4-bar volume and trades. It pages through all bars from 16:00 ET (DST-aware). Tested on the Oct 14 names: it reaches 23:55Z and matches `broker.js bars`.
  - [scripts/broker.js](../../scripts/broker.js) `bars` now prints `# truncated at --limit N; more bars exist after <time>` when the API has more pages.
  - [prompts/post-market-scan.md](../../prompts/post-market-scan.md) cross-check paragraph now points at the script and names the 17:35 ET cutoff.
- **Status:** Fixed

### `grep -A7`-style flags fail under the `grg` wrapper

- **Severity:** Minor
- **Sessions affected:** Oct 15 08:20; also Sep 22 08:20, Oct 6 08:20, Oct 6 13:00, Oct 7 08:20 (5 work sessions in 4 weeks, one extra call each)
- **Symptom:** `grep -A7 …` fails with `rg: error parsing flag -A: value is not a valid number`. Same for `-B2`, `-C3`, `-m1`. `-A 7` with a space works, and plain `rg -A7` works.
- **Root cause:** in agent shells `grep` calls `grg` from greprip (`kaofelix/greprip-rs`, pinned at the latest upstream commit 234c03c, Mar 4) through Juan's dotfiles `nix/modules/greprip.nix`. `grg` passes an attached numeric value to `rg` incorrectly. The Sep 15 review logged the wrapper's regex differences as tracking only; this flag bug is separate and keeps recurring.
- **Fix:** needs a greprip change: split `-A7`/`-B2`/`-C3`/`-m1` into flag and value before calling `rg`. Upstream has no fix. No prompt uses this form, so the trading repo has nothing to change.
- **Status:** Needs user action (low priority)

## One-off Errors

- Oct 14 13:00: an inline Python patch printed a `diff` that exited 1; the run continued.
- Oct 14 16:00: a trailing `rg -c` found no match while checking a byte pattern.
- Oct 15 09:00: two `ls … | rg` checks exited 1 and 2 when no sweep file existed yet.

## Previous Fixes Checked

- **Initiative 3 hold retirement (Oct 14 handoff):** applied at 15:00 CEST. NCPL and YYAI, entered on Oct 14 night, were sold at the Oct 15 10:30 evaluation (orders `ff6523b9`, `44de789a`); `OPEN_POSITIONS.md` and Alpaca are both empty.
- **AH-open pulse (Oct 14 fix):** the Oct 14 20:00 scan ran 5 calls in 27 seconds and did not sleep.

## Initiative Progress and Email Coverage

- **Strategy runs:** both Oct 14 runs produced new results: Initiative 3's applied rule change and Initiative 7's failed out-of-sample fade test, which closes the liquid lane. No run had only unchanged reruns.
- **Latest email:** Gmail message `1a13ee7e9a66b9f8`, sent `2026-10-15T09:32:28Z`, window from `2026-10-14T09:32:21Z`. `initiative_updates` lists 3, 7 and 4, the three initiatives that moved in the window (4 through the Oct 14 process review). Initiative 6 is under monitoring and Initiative 2's deferral is carried.
- **Ready work:** Initiative 7's micro-cap census is the next step, set for today's 15:00 run. Nothing has been skipped.

## Handoff to Strategy Advance

- **Initiative 7 micro-cap census (today 15:00 CEST):** the fetch is likely long. Follow the new long-job rule: start it with `gob add`, write the log entry and commit before waiting, and poll in short calls.
- Keep Initiative 2's broker test deferred per Juan's Sep 22 instruction.

## Needs User Action

- **greprip attached numeric flags** (low priority): `grg` should accept `-A7`, `-B2`, `-C3` and `-m1` like grep does. Fix it in greprip or patch it in `dotfiles/nix/modules/greprip.nix`.
- The scheduler reliability note and the provider login-error decision stay open in the daily email.
