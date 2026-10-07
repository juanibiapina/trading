# Initiative 7 orchestration, Initiative 3 later-rebuild test, Initiative 5 check — 2026-10-07

Strategy advance, October 7 15:00 CEST. Log-only: no order, trading rule, size or trading-pulse time changed.

## Initiative 7 — observation orchestration

`scripts/init7-observe.py` (SHA-256 `f0527781efeb7da41ede7e3ce8d299957e4074bf2fd529819699b07e77552fba`) runs the frozen design end to end for one scheduled slot:

1. Capture today's delayed SIP five-minute bars for the eight-symbol basket and the latest IEX books, with the October 1 census request shapes.
2. Select N1 with the pinned selector `init7-comparison-features.py`.
3. If N1 picks a ticker, run the pinned SEC archiver for that ticker.
4. If the source is eligible, make the single Jev call with the pinned classifier.
5. Write A1 (design v1) and A2 (amendment) to `decision.json` before any outcome is read.

Output goes to `log/<ET date>/init7-observe/<HHMM>/`. Every stage creates its files exclusively, so a slot cannot be run twice.

**Timing rule (orchestration v1).** The common decision cutoff is the scheduled time plus the design's 120-second observation deadline. Market and SEC inputs count only if received by then, and the archiver uses that cutoff. Market inputs received later make every arm cash. A mismatch with any hash pinned by the A2 amendment also makes every arm cash.

**Verification.**

| Check | Result |
|---|---|
| Pinned hashes (design, archiver, classifier, amendment) | all match |
| A2 amendment decision vectors | **12/12** reproduce A1, A2 and the A2 reason |
| Offline rehearsal on `log/2026-10-01/init7-data-census.json` | `features.json` is identical to the October 2 reference; N1 cash (`no_positive_absolute_and_relative_return`) |
| Live SEC capture, all seven tickers, cutoff 13:07:51 UTC | 7/7 `no_8k_within_window`; A1 cash, A2 holds N1 (`no_source`) |
| Jev glue, archived AAPL 8-K (accession 0000320193-26-000018, Q3 results) with receipt flags overridden | `earnings_guidance`, confidence 1.0, dilutive financing 0.03; A1 and A2 keep AAPL |
| Refusals | outside the slot window and a non-frozen slot both exit 1 |

The Jev glue check made **1 development call: 5,914 input / 157 output tokens, $0.000248 estimated** at $0.042 per million input tokens; the billed charge is unavailable. It is excluded from the trial. Artifacts: `log/2026-10-07/init7-observe-dev/`.

**First scheduled capture.** The scheduler only runs agent prompts and loads jobs at bridge startup. Instead, gob job `SFm` runs `python3 scripts/init7-observe.py daemon --sessions 5`. It started at 13:06 UTC, before today's 10:30 ET slot. It sleeps until each frozen slot (10:30–15:30 ET), skips half-days, and stops after five full sessions: October 7, 8, 9, 12 and 13 if none is missed. No agent session or bridge restart is needed. If a reboot or a gob restart kills it, `gob list` and `python3 scripts/init7-observe.py status` show the gap; restart it before the next 10:30 ET.

## Initiative 3 — later-rebuild comparison with the screener lag

`scripts/init3-rebuild-eval.py` replays the October 6 archive of all 89 real AH entries offline. It reuses the October 1 confirmation gate unchanged (ignition: +10% over the regular close, a green new AH high, ≥20 trades, ≥2x local volume; confirmation: closes hold ≥80% of the running high, and the confirming bar is at least the ignition's close and volume). Entry is the first bar opening at least 15 minutes after the confirming bar closes, the measured screener and free-SIP delay. Exit is each trade's realized exit price, so a variant changes only selection and entry price.

| Variant (15-minute lag) | Admits | Later rebuilds | Mean | Median | Wins | $ at $100 each | Same names, real entry | Selection p |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Base: all real entries | 89 | — | -3.2% | -7.7% | 28 | -$285 | — | — |
| First ignition, 2-bar | 41 | 0 | -0.2% | -9.8% | 17 | -$7 | -1.9% | 0.67 |
| Re-arm (rebuild allowed), 2-bar | 49 | 8 | -2.4% | -9.9% | 18 | -$118 | -3.8% | 0.81 |
| First ignition, 3-bar | 42 | 0 | -2.7% | -10.3% | 15 | -$112 | -3.6% | 0.89 |
| Re-arm, 3-bar | 45 | 3 | -3.7% | -11.5% | 15 | -$167 | -4.4% | 0.69 |

**Later rebuilds lose.** The eight rebuild admits average **-13.9% (median -13.2%, 1 win: YFOR +8.4%)**: VEEE, TGHL, PAPL, ANY, ONMD, ONFO, XOS. Re-arming is worse than the first-ignition rule at every confirmation length and both lags tested (0 and 15 minutes).

**The first-ignition rule does not beat the base rate reliably.** Its -0.2% mean on 41 names has a -9.8% median. Its selection is no better than chance (permutation p 0.67), and its +1.7-point entry-price gain is within the spread that bar opens omit. Entries at or after 17:00 ET average +10.0% on 19 names (median +3.0%), but BAOS (+143%) and VEEA (+77%) carry it: without them the mean is -1.8%. This split was found after the fact.

**Decision:** no timing or rebuild rule is proposed. AMOD's open question is closed: allowing a later rebuild adds losers.

**Limits.** Bar opens carry no spread while real fills crossed it, so variant returns lean optimistic. The regular close is the last regular-session five-minute bar, not the closing auction. The 89 names were chosen by the live scan, so this tests timing within that selection, not discovery.

## Initiative 5 — shared rows beside charts (October 6 cycle)

`generate-html-report.py --date 2026-10-06` renders both charts (BIYA, MTEN) and **43 volume sections with 578 rows, all matching** `log/2026-10-06/*-volume-metric.json` field by field (bar time, shares, baseline, both ratios, status).

The published October 6 page returned **404**. The Pages workflow built only the newest dated log on each push, so the 10:00 CEST premarket scan's `log/2026-10-07` replaced it before the 11:30 email. The email does not link the report, so nothing visible broke. `.github/workflows/pages.yml` now rebuilds the seven newest dated logs; the loop ran locally for October 7 back to September 29 with exit 0. Initiative 1's October 8 v2 switch must teach the generator to accept `sip-ah-volume-v2`; it currently raises on any other version, which would now fail the whole build.

## Initiative 3 — DST loading check

The bridge process started **2026-10-05 11:22:21 CEST**. `scheduler.json` was last written **2026-09-29 18:05**, and it parses with all 37 jobs. The three DST cohort jobs added on September 29 are therefore loaded before October 25.

## Reproduce

```bash
python3 scripts/init7-observe.py verify
python3 scripts/init7-observe.py observe --market-input log/2026-10-01/init7-data-census.json \
  --at 2026-10-01T16:04:00Z --out /tmp/init7-rehearsal
python3 scripts/init7-observe.py status
python3 scripts/init3-rebuild-eval.py            # offline; full rows in log/2026-10-07/init3-rebuild/result.json
python3 scripts/generate-html-report.py --date 2026-10-06
```
