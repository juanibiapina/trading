# Process Review — 2026-10-07

## Sessions Reviewed

All 23 work sessions since the Oct 6 review, timestamps UTC:

- 2026-10-06 13:00 and 16:00 — strategy advance (`01a1114c`, `01a111f1`)
- 2026-10-06 19:30 → 22:30 — 13 post-market scans (21:30 CEST regular-session pass, then 22:00–00:30 CEST)
- 2026-10-07 07:00 feedback check, 08:10 Initiative 6 cohort, 08:20 morning evaluation, 08:30 position evaluation, 09:00 premarket-open scan, 09:30 daily email, 12:20 scanner improvement, 12:30 position evaluation

For recurrence I also compared the Oct 1 post-market scans, the morning evaluations since Sep 24, and every session since Sep 28 that read `OPEN_POSITIONS.md`. This review (12:40) is excluded. I read the Sep 29 to Oct 6 process reviews first; issues they closed are omitted.

All 23 sessions finished and pushed. No provider errors occurred in this window.

## Issues Found

### Volume metric fetch fails with HTTP 403, so every pulse builds the SIP archive by hand

- **Severity:** Wasteful
- **Sessions affected:** 8 of 8 Oct 6 post-market pulses that had >10% candidates (22:20 to 00:30 CEST)
- **Symptom:** Each pulse spent 4–10 tool calls on the shared volume measurement (48 in total). The 22:20 pulse read the script's help, its source, the spec and `broker.js` before writing an archive script. The 22:25 and 22:30 pulses first tried `volume_metric.py --save-input`, got `HTTP Error 403: Forbidden`, and fell back to a script of their own. Every later pulse wrote a new Python script that wraps `broker.js bars --json` in the archive format.
- **Root cause:** `fetch_sip` requested bars through 20:00 ET of the current day. During a live session that end time falls inside the free SIP plan's 15-minute delay, and Alpaca rejects it with `subscription does not permit querying recent SIP data`. The same request with its end at least 15 minutes in the past succeeds. The prompt worked around the bug by telling sessions to assemble the archive themselves.
- **Fix:** `scripts/volume_metric.py` now caps the request's end at 15 minutes 10 seconds before now. `prompts/post-market-scan.md` uses `--save-input` for the fetch and archive in one call, and keeps `--input` for replays.
- **Verification:** For BIYA (as-of 08:47 ET today, current session still open), the old code returned 403 and the new code exited 0. Its archive held the same 103 bars, field for field, as the `broker.js` fetch the pulses used. Replays of `BIYA-2300-volume-sip.json` give byte-identical v1 and v2 output from the old and new code. `ah-5m-confirmation.js` read the new output.
- **Status:** Fixed

### A concurrent pulse committed another pulse's temporary files

- **Severity:** Minor
- **Sessions affected:** 1 of 13 post-market pulses
- **Symptom:** The 22:20 pulse's `git add log/` committed three empty `*-2225-volume-metric.json.tmp` files. They came from the 22:25 pulse's 403 failures. The 22:20 pulse removed them in a follow-up commit (`2f007c2`).
- **Root cause:** The 22:20 and 22:25 pulses ran 6.8 and 8.8 minutes, past the next 5-minute start, and nothing ignored temporary files.
- **Fix:** Added `*.tmp` to `.gitignore`. A test `.tmp` file under `log/` stayed out of `git status`. The volume fix above also removes the failure that left these files, which should shorten the pulses.
- **Status:** Fixed

### Post-market pulses read the whole day's log every run

- **Severity:** Wasteful
- **Sessions affected:** the last 6 of 13 Oct 6 pulses read 41–79 KB of the log each; on Oct 1 the matching 6 pulses read 42–117 KB
- **Symptom:** "Read the existing log" led pulses to `cat` or page through the full `log.md`. By 23:00 CEST it held about 50 KB of earlier scan notes, and the read stayed in context for 20–30 turns.
- **Root cause:** The prompt did not say which part of the log answers its question.
- **Fix:** `prompts/post-market-scan.md` now lists the log's sections, reads the Paper Trades table and the latest `## Scan` section, and searches for a ticker by name when an earlier note is needed.
- **Status:** Fixed in the prompt; adoption shows from tonight's pulses

### Full reads of OPEN_POSITIONS.md

- **Severity:** Wasteful
- **Sessions affected:** 37 sessions since Sep 28 read the full 47–49 KB file: both position evaluations each day plus post-market pulses (11 on Sep 30, 10 on Oct 1). In this window: the 08:30 and 12:30 position evaluations and the Oct 6 00:00 CEST entry pulse.
- **Symptom:** The current positions and rules fill the first 55 lines (2.9 KB). The rest is the closed-trade history.
- **Fix:** `prompts/position-evaluation.md` and `prompts/post-market-scan.md` now read only the open section with `sed -n '1,/^## Closed Positions/p'`. The position prompt also gives the Closed table's header and separator lines as the anchor for inserting an exit row; both commands were checked on the current file.
- **Status:** Fixed in the prompts

### Morning evaluations write their own uncapped premarket sweep

- **Severity:** Wasteful
- **Sessions affected:** 5 of 8 morning evaluations since Sep 24 (Sep 29, Sep 30, Oct 2, Oct 6, Oct 7); today's premarket-open scan did it once too
- **Symptom:** The sessions read `scan.py` help or source (up to 3 calls), then wrote 1–3 inline TradingView queries for premarket gainers with no price or market-cap cap.
- **Root cause:** `prompts/morning-evaluation.md` requires an "independent whole-market PM sweep (no price/mcap cap)" for price-floor tracking but names no tool, and `scan.py` always applies its $0.50–$10 and $300M caps.
- **Fix:** Added `scripts/pm-sweep.py` (listed exchanges by default; `--min-change`, `--limit`, `--include-otc`), and the morning prompt now names it in the retrospective step and the price-floor section. A live run returned 13 names, including sub-$0.50 TOPP and GIPR and the $2.6B NEOG, which `scan.py` excludes. Its help notes that TradingView's premarket high can be a bad print: it showed BIYA at $37.10, while the SIP high was $2.99. Scanner parameters are unchanged.
- **Status:** Fixed

## Initiative Progress and Email Coverage

- **Strategy runs:** both Oct 6 runs delivered. At 15:00 the Initiative 7 SEC archiver, the oldest overdue handoff item, ran with seven real captures. The same run did the Initiative 6 latency study that ended the pilot and added the Initiative 3 outage record. At 18:00 came Initiative 1's v2 metric, the 89-entry volume-gate test and the Initiative 7 A2 freeze. There were no runs with only unchanged reruns.
- **Moved work, with dated reasons:** Initiative 7 observation orchestration moved from Oct 6 18:00 to Oct 7 15:00 because A2 had to be frozen first. The Initiative 3 later-rebuild comparison has moved twice (the Oct 5 outage, then Oct 6 priorities) and is set for Oct 7 15:00.
- **Latest completed email:** InboxKit message 180, sent `2026-10-07T09:35:30Z`. Its window starts at receipt 179 (`2026-10-06T11:00:54Z`). It carries dated updates for Initiatives 1, 3, 6 and 7, the four that moved. It also reports the Oct 6 review's outage root cause, the repo fixes and the open provider decision, Initiative 5's pending check and Initiative 2's broker deferral. No moved initiative is missing.
- **Ready work without an owner or date:** Initiative 5's check of the shared volume rows beside charts. The roadmap set it for "the next chart-bearing cycle". The Oct 6 cycle was the first with both charts (BIYA, MTEN) and volume-metric files, yet the email, the scanner improvement and the roadmap each list it as waiting.

## Handoff to Strategy Advance

1. **Oct 7 15:00:** deliver the dated items: Initiative 7 observation orchestration that reproduces the 12 A2 vectors, and the Initiative 3 later-rebuild comparison. The comparison has moved twice; if it moves again, record why.
2. **Initiative 5:** run the check on the Oct 6 cycle. Generate the 2026-10-06 report and confirm that the BIYA and MTEN volume rows match `log/2026-10-06/*-volume-metric.json`. Give it a slot if 15:00 is full.
3. **Initiative 1, Oct 8:** the post-market prompt's volume command now uses `--save-input`. The v2 switch adds `--metric-version sip-ah-volume-v2` to that same command.

Initiative 2's broker test stays deferred per Juan's Sep 22 instruction. Nothing from this review needs Juan's input. The provider-error decision from the Oct 6 review is still open in the daily email.

## Additional Checks

- The Oct 6 fixes held. The 23:00 and 00:00 CEST entry pulses ran `broker.js positions` and `orders all` before each buy. No sync failed, and no late start happened.
- The scheduled InboxKit check used curl and finished in two calls.
- Apart from the 403s above, no failing command was retried 3 or more times. Other non-zero exits were expected: `ls *.tmp` checks with no matches (exit 2), empty `ps | rg` probes, and one strategy probe run from `/tmp` that could not import `scan`.
