# Initiative Log

Daily progress on the strategy roadmap (`STRATEGY_ROADMAP.md`), one initiative
at a time. Written by the `strategy-advance` pulse. Newest first.

This is the strategy-level analog of `SCANNER_CHANGELOG.md` (which logs surgical
scanner tweaks). Each entry evaluates the previous step, records the step taken
today, and sets the hypothesis/next step for the following run.

---

### 2026-08-13 — Initiative 3: peak-ceiling gap is mostly UNCAPTURABLE by a fixed second pulse

**Evaluated:** The 2026-08-12 step **worked** (9th seed GXAI is again a positive post-exit premarket peak, so the peak ceiling holds 9/9) **but its core hypothesis — "add a second premarket exit pulse to capture the gap" — is now substantially weakened by today's own analysis.** The prior runs reported a growing peak-ceiling tally (+229% over 8) as if a second pulse would capture it. That conflates the *perfect intrabar peak* with what a *fixed second decision time* actually gets.

**Step taken:** **Pilot / Initiative 3 (execution pivot):** (1) seeded GXAI (Grade C, sold at the 08-13 04:30 ET exit) into `premarket-exit-gap.js`; (2) built `scripts/premarket-exit-pulse-sweep.js` (log-only) to measure the *realistic capturable* gain — the bar-close price at each candidate fixed second-pulse time (05:00–09:00 ET) vs our actual 04:30 ET exit, summed across all 9 seeded names. Verified the GXAI peak bar is genuine (1.8M sh / 7.5k trades, not a bad print). No orders, no schedule change.

**Result:** GXAI exit $1.28 -> PM peak $1.56 at 05:35 ET (+21.9%) then faded to PM-last $1.33 (+3.9%); 9/9 seeds positive at the peak (peak-ceiling tally +251.1%). **The sweep is the decisive finding: the best fixed second-pulse time (06:00 ET / 12:00 CET) captures only +25.0% total across 9 names (~+2.8%/name), dominated by one outlier (PAVS +25.4%); without PAVS it is ~0.** Every other time is worse (05:00 ET -4.3%, 05:30 ET +1.1%, 07:00 ET +13.6%, 08:00 ET +10.7%). The early peakers (BAOS -21% by 06:00, BOXL, GXAI, WAFU) dump before any reasonable second pulse fires, so a hold-to-a-fixed-later-time rule gives back nearly all of the peak. The +251% is a **peak ceiling, not a capturable edge.**

**Hypothesis / next step:** A blind second exit pulse is **not** supported — it would not reliably beat the 04:30 ET exit net of the fade. Capturing the gap needs a *peak-seeking* mechanism (a resting sell-limit above entry, or a trailing stop set at entry) that sells early spikes into strength, not a second fixed decision time. Next run: simulate a resting limit / trailing-stop exit set at entry over the 9 seeded names (log-only) to size what a peak-seeking rule actually captures vs the 04:30 ET exit, before proposing anything to Juan. Keep `CONFIRM-3` and both instruments log-only. Init 6 still waits for admitted PM-only-gapper n>=12 before the deferred 1-minute exit test.

**Needs from Juan:** **softened proposal (evidence changed the ask):** the earlier "add a second premarket exit pulse" is weakened by the sweep; the better-evidenced candidate is a **peak-seeking premarket exit** (resting limit / trailing stop above entry) so early spikes sell into strength. Still to be proposed once the peak-seeking sim quantifies the capture — not applied. Also still open from 08-07: the Initiative 2 broker/feed decision for the ~203% fill gap (Alpaca SIP ~$99/mo, IBKR paper, or modeled SIP fills).

### 2026-08-12 — Initiative 3: exit-timing gap holds a third session (n=8)

**Evaluated:** The 2026-08-11 step **worked and its hypothesis held again.** It confirmed the exit-timing gap out-of-sample (5/5 held names with a positive post-exit premarket peak) and set this run to keep seeding held names. Today's 08-12 10:30 CET position eval sold three held names (BAOS Grade-None +148.9%, BOXL Grade-None +45.4%, FF Grade-B day-2) at the 04:31 ET exit — three fresh seeds.

**Step taken:** **Pilot / Initiative 3 (execution pivot):** pulled the three exit fills from `broker.js orders all --json` (all filled ~08:30:5xZ = 04:31 ET), ran `premarket-exit-gap.js` on each, and appended all three to `log/premarket-exit-gap.csv`. Log-only, no orders.

**Result:** **BAOS** exit $2.24 -> PM peak $2.51 at 04:35 ET (+12.1%) then crashed to PM-last $1.16 (-48%); **BOXL** $5.83 -> $6.80 at 05:05 ET (+16.6%) then faded to $4.52 (-22%); **FF** $6.20 -> $6.43 at 06:30 ET (+3.7%), held to PM-last $6.25 (+0.8%). New three-name gap +32.4%; running tally **+229.2% over 8 held names**, all 8 with a positive premarket peak after our 04:31 ET exit. **Nuance sharpens:** these three peaked EARLY (04:35–06:30 ET) and BAOS/BOXL then dumped hard to PM-last, so the +229.2% is a peak ceiling needing a peak-seeking exit, not hold-to-PM-last. The accumulated sample is now bimodal: early peakers (BAOS 04:35, BOXL 05:05, WAFU 05:05, MTEN 05:40 ET) vs later peakers (FF 06:30, PAVS 06:55, MGIH 07:30, CELZ 08:00 ET).

**Hypothesis / next step:** The exit-timing gap is robust (8/8 positive across three sessions), so the second-premarket-exit-pulse proposal stands. But the bimodal peak distribution means a single fixed second pulse misses one cluster; a ~06:00–07:00 ET (12:00–13:00 CET) time captures the larger/later spikes (FF, PAVS, MGIH, CELZ) at the cost of the four early ones. Next run: keep seeding; once (if) the second pulse is approved, sweep the accumulated sample for the single time that captures the most total gap. Keep `CONFIRM-3` and this instrument log-only. Init 6 unchanged (waits for admitted PM-only-gapper n>=12 before the deferred 1-minute exit test; 08-11/08-12 logged new holdable PM-only gappers — ELPW, DOGZ, WXM, HUDI — but the admitted-set recount is deferred to a dedicated run).

**Needs from Juan:** **one proposal (unchanged, evidence now +229.2% over 8 held names)** — add a second premarket position-eval pulse (~12:00–14:00 CET / 06:00–08:00 ET), ideally ~06:00–07:00 ET to catch the larger/later premarket peaks, so held names can catch the peak rather than selling at the 04:31 ET floor. Veto window; not applied. Also still open from 08-07: the Initiative 2 broker/feed decision for the ~203% fill gap (Alpaca SIP ~$99/mo, IBKR paper, or modeled SIP fills).

### 2026-08-11 — Initiative 3: premarket exit-timing gap confirmed out-of-sample

**Evaluated:** The 2026-08-10 step **worked and its hypothesis held out-of-sample.** It sized the exit-timing gap at +146.2% over PAVS/CELZ and set this run to seed 1–2 more held names to confirm persistence. The 08-11 10:30 CET position eval sold three Grade-None held names (WAFU, MTEN, MGIH) at the 04:31 ET exit — ideal fresh seeds. All three show a positive premarket peak *after* our exit, so the gap is not a two-name artifact.

**Step taken:** **Pilot / Initiative 3 (execution pivot):** pulled the three exit fills from `broker.js orders all` (all filled 08:31Z = 04:31 ET), ran `premarket-exit-gap.js` on each, verified MGIH's peak is genuine (not a bad print), and appended all three to `log/premarket-exit-gap.csv`. Log-only, no orders.

**Result:** **WAFU** exit $2.10 -> PM peak $2.30 at 05:05 ET (+9.5%); **MTEN** $1.35 -> $1.45 at 05:40 ET (+7.4%); **MGIH** $2.02 -> a **genuine liquid spike to $2.70 at 07:30 ET (+33.7%)** on 2.9M sh / 23,710 trades (VWAP $2.47), then a crash to $1.61 the next bar. New three-name gap +50.6%; running tally **+196.8% over 5 held names**, every peak (05:05–08:00 ET) after our 04:31 ET exit and inside premarket. **Nuance:** PAVS/CELZ held their gains to PM-last (+39%/+38%) but WAFU/MTEN/MGIH faded to PM-last (-21%/-3%/-26%), so the +196.8% is the peak ceiling, not a hold-to-PM-last figure — capturing it needs a peak-seeking exit at a second decision point, not just holding longer. MGIH's 07:30 ET spike lands squarely inside the proposed 06:00–08:00 ET second-pulse window.

**Hypothesis / next step:** The exit-timing gap is real and persistent (5/5 names positive premarket peak after exit), so the second-premarket-exit-pulse proposal to Juan stands. But it is timing-dependent: WAFU/MTEN peaked early (05:05/05:40 ET) while PAVS/MGIH/CELZ peaked later (06:55–08:00 ET), so one fixed second pulse can't catch every peak — a mid-window time (~07:00 ET / 13:00 CET) catches the larger/later spikes (PAVS, MGIH, CELZ) but misses the two smaller early ones. Next run: keep seeding held names; once the second pulse is (or isn't) approved, if approved test which single time captures the most gap across the accumulated sample. Keep `CONFIRM-3` and this instrument log-only. Init 6 unchanged (waits for admitted PM-only-gapper n>=12 before the deferred 1-minute exit test).

**Needs from Juan:** **one proposal (unchanged, now stronger evidence)** — add a second premarket position-eval pulse (~12:00–14:00 CET / 06:00–08:00 ET) so held names can catch the later premarket peak rather than selling at the 04:31 ET floor (evidence now +196.8% premarket upside across 5 held names). Veto window; not applied. Also still open from 08-07: the Initiative 2 broker/feed decision for the ~203% fill gap (pay Alpaca SIP ~$99/mo, IBKR paper, or modeled SIP fills).

### 2026-08-10 — Initiative 3: premarket exit-timing gap sized from real SIP bars

**Evaluated:** The 2026-08-07 step **worked and its hypothesis holds up under scrutiny.** It predicted the exit-timing slice was the largest gap fixable without Juan or a broker change and set this run to size it from real bars. Doing so confirms it: measured strictly from our actual exit fills and capped at the premarket open, the two held names left **+146.2%** of premarket upside on the table — corroborating (and slightly exceeding) the 08-07 tally's 137%, which had used entry references and reached past the open. My initial partial bar pull looked like CELZ topped at only ~$0.97 (+9%); pulling the full premarket window showed CELZ actually ran to **$1.37 at 08:00 ET** on 6.9M sh / 17,237 trades — the gap is real and liquid, not a print artifact.

**Step taken:** **Pilot / Initiative 3 (execution pivot):** built `scripts/premarket-exit-gap.js` + `log/premarket-exit-gap.csv` (log-only, no orders). For each held name it pulls SIP 5-min bars, takes our real exit fill (price + UTC time from `broker.js`), finds the highest premarket HIGH *strictly after* that exit, and **caps the window at 09:30 ET / 13:30Z** so it never counts regular-session prices our rules forbid holding into. Seeded with PAVS and CELZ (the two `exit_timing` names from the execution-gap tally), using verified exit fills (both filled 08:31Z = 04:31 ET, the 10:30 CET pulse).

**Result:** `node --check` passes and the tool runs. **PAVS** exit $6.65 -> premarket peak **$12.10 at 06:55 ET = +82.0%**; **CELZ** exit $0.834 -> premarket peak **$1.37 at 08:00 ET = +64.3%** (verified genuine: the peak bar carried 6.9M sh / 17,237 trades, VWAP $1.29). Summed premarket exit-timing gap = **+146.2%** over 2 held names, entirely inside premarket, entirely after our single 04:31 ET exit. This is the strongest evidence yet that the single 10:30 CET (04:31 ET) exit pulse is far too early for overnight-AH holds: the real premarket peaks fired 06:55–08:00 ET (12:55–14:00 CET), 2.5–3.5h after we sold.

**Hypothesis / next step:** A second premarket position-eval pulse around **12:00–14:00 CET (06:00–08:00 ET)** would let Grade-None holds catch the later premarket peak instead of exiting at the 04:31 ET floor. This changes live exit timing, so it is **proposed to Juan, not applied** (routed to the daily email + roadmap open-asks). Next run: seed 1–2 more held names as they occur to confirm the +146% gap persists out-of-sample; only propose wiring the second exit pulse once the gap holds across more sessions. Keep `CONFIRM-3` and this instrument log-only. Init 6 unchanged: waits for admitted PM-only-gapper n>=12 before the deferred 1-minute exit test.

**Needs from Juan:** **one proposal** — add a second premarket exit-eval pulse (~12:00–14:00 CET / 06:00–08:00 ET) so held names can catch the true premarket peak rather than selling at the 04:31 ET floor (evidence: +146.2% premarket upside left on the table across PAVS + CELZ). Veto window; not applied. Also still open from 08-07: the Initiative 2 broker/feed decision for the 203% fill gap (pay Alpaca SIP ~$99/mo, IBKR paper, or modeled SIP fills).

### 2026-08-07 — Initiative 3: execution-gap tally (pivot to execution)

**Evaluated:** The 2026-08-06 step **worked** and its hypothesis is confirmed. It predicted the fill/exit-timing gap would be the larger money-fast lever; quantifying it today bears that out. Added the fourth live outcome set first (08-06 AH -> 08-07 PM): only DSY qualified (CONFIRM-3 **NO**, entered at $7.10 on other grounds), and it faded — PM peak $6.96 below entry, a clean entry-price loss, not a selection or exit-timing miss. `node scripts/ah-5m-confirmation.js` still reproduces recorded verdicts.

**Step taken:** **Pilot / Initiative 3 (execution pivot):** built `scripts/execution-gap.js` + `log/execution-gap.csv` — a log-only tally of the 10 CONFIRM-3 YES / held rows across four live sessions, classifying each by where the detected PM upside was lost (fill / exit_timing / blocked_saved / selection / none). Appended the fourth outcome table and the tally writeup to `INIT3_IGNITION_TIMING.md`. No orders, entry rule, grade, or schedule changed.

**Result:** **340.4% of detected next-PM upside was lost, none of it to selection.** Two buckets dominate: **fill gap 203.4%** (CLRO +147.7, BJDX +43.5, INLF +12.2 — real winners with no fillable Alpaca AH ask; 55.7% even excluding the CLRO outlier) and **exit-timing gap 137.0%** (CELZ +53.9, PAVS +83.1 — held names whose PM spikes fired ~06:55/08:00 ET, after our 10:30 CET / 04:30 ET exit but still inside premarket). The fill gap is Initiative 2 (feed/broker), root-caused and awaiting Juan's fix call. The exit-timing gap is self-inflicted and fixable in our own process. This confirms Init 3's original selection-gate hypothesis is **not** the money-fast lever — execution is. `node --check` and the tally run pass.

**Hypothesis / next step:** The exit-timing slice is the largest gap fixable without Juan or a broker change. Next run: instrument the intra-premarket exit path (log-only) — for each held name, record the full premarket SIP trajectory and the best premarket exit vs our actual 10:30 CET exit, to size the gap out-of-sample. Only after several rows show a persistent gap should an exit-pulse retiming be **proposed to Juan** (trading-pulse change, not applied unilaterally). Keep CONFIRM-3 log-only; stop treating it as a promotion candidate.

**Needs from Juan:** nothing blocking today. **Two flags routed to the daily email:** (1) the 203.4% fill gap needs the Initiative 2 broker/feed decision (pay Alpaca SIP ~$99/mo, IBKR paper, or modeled SIP fills); (2) the 10:30 CET single exit pulse looks too early for multi-day holds — CELZ/PAVS ran >50% in *later* premarket after we had exited. A later or second premarket exit check is a candidate change, to be proposed once instrumented.

### 2026-08-06 — Initiative 3: third live third-bar outcome set

**Evaluated:** The 2026-08-05 second-set step **worked mechanically** but the gate remains **insufficient/now weakening**. The 08-05 AH -> 08-06 PM session added a third out-of-sample set and, for the first time, the gate's separation clearly **broke down**: `CONFIRM-3 YES` CLRO ran +147.7% to its next-PM high but Alpaca had no fillable AH ask (uninvestable), the other `YES` RECT died (-6.2%), and both `CONFIRM-3 NO` names had the day's largest PM excursions (PAVS +83.1%, CELZ +53.9%). The gate would have rejected the two biggest movers.

**Step taken:** **Pilot / Initiative 3:** re-ran `ah-5m-confirmation.js` on the four labelled 08-05 AH candidates (RECT, CLRO, CELZ, PAVS), pulled their 08-06 SIP 5-minute PM highs (high-trade bars only, no bad prints), and appended the third verdict-to-PM-outcome table to `INIT3_IGNITION_TIMING.md`.

**Result:** Combined live `YES` n=7 = +12.2, +43.5, +147.7, +0.9, -2.8, -6.2, -19.9 (mean +25.1% is CLRO-outlier-driven, median +0.9%); `NO` n=7 now holds two >50% PM runs. `node scripts/ah-5m-confirmation.js RECT:2026-08-05 CLRO:2026-08-05 CELZ:2026-08-05 PAVS:2026-08-05` reproduced every recorded verdict. **Emerging conclusion:** across three sessions the third-bar gate does not cleanly separate next-PM winners from fades; the recurring bottleneck is **execution, not selection** — the biggest edges were unfillable (CLRO no AH ask; INLF/BANL/ZJYL broker-blocked) or ran only after our early 10:30 CET exit (CELZ/PAVS). Init 6 stays blocked at n=11 admitted PM-only gappers (08-05 produced AH-open names, no new PM-only gapper), one short of the n>=12 one-minute-exit trigger.

**Hypothesis / next step:** Stop treating the selection gate as the primary lever. Next run should quantify the **fill/exit-timing gap**: how much of the CONFIRM-3 YES + qualified edge is lost to unfillable AH asks vs premature PM exits. Build a log-only tally of qualified/YES names that (a) had no fillable Alpaca AH ask and (b) spiked in PM after our exit pulse. If the gap is large, that reframes Initiative 3 toward execution/exit-timing rather than scan cadence. Keep CONFIRM-3 log-only. Run Init 6's one-minute exit test only when admitted n reaches 12.

**Needs from Juan:** nothing blocking. **Flag for awareness:** repeated real edges (CLRO +148%, INLF, BANL, ZJYL) are unfillable in Alpaca's after-hours book — the paper broker's AH liquidity, not our selection, is now the main thing capping captured P&L. Raising in the daily email as a strategic constraint to weigh (e.g. entering a portion at PM open instead of AH, or a different broker for live).

### 2026-08-05 — Initiative 3: second live third-bar outcome set

**Evaluated:** The 2026-08-04 first-live-outcome step **worked mechanically but remains insufficient for a decision**. The next AH session supplied five more out-of-sample rows. `CONFIRM-3 YES` INLF reached +12.2% to its next-PM SIP high and BJDX +43.5%, but BANL lost -19.9% and ZJYL was only +0.9%; `NO` TRUG was flat. Combined live YES n=5 has two meaningful excursions, one near-flat result, and two losses. Peak returns omit spread, INLF had no fillable AH ask, and BJDX had faded in AH, so this does not establish executable edge.

**Step taken:** **Pilot / Initiative 3:** re-ran `ah-5m-confirmation.js` on all five 2026-08-04 AH candidates, pulled their 2026-08-05 SIP 5-minute PM bars, and appended the verdict-to-PM-outcome table to `INIT3_IGNITION_TIMING.md`.

**Result:** The first live YES loss (JELD) was not representative, but the broader n=10 live sample is still too small and mixed to change selection or add five-minute pulses. `node scripts/ah-5m-confirmation.js INLF:2026-08-04 BJDX:2026-08-04 BANL:2026-08-04 ZJYL:2026-08-04 TRUG:2026-08-04` reproduced every recorded verdict. Initiative 3 remains the highest expected dollars-per-time lever because a validated selection gate would improve every AH trade without added pulse cost. Parallel Init 6 remains blocked at n=11 admitted PM-only gappers, one short of its deferred one-minute exit test; its 5-minute exits remain negative after spread.

**Hypothesis / next step:** Collect more distinct live `CONFIRM-3` verdicts and next-PM outcomes. Do not change entry logic or scan timing unless the out-of-sample separation persists net of realistic fill and spread constraints. Run Initiative 6's one-minute exit test only when admitted n reaches 12.

**Needs from Juan:** nothing.

### 2026-08-04 — Initiative 3: first live third-bar outcomes; Initiative 6 sample refresh

**Evaluated:** The 2026-08-03 instrumentation step **worked mechanically**: every eligible 08-03 AH candidate received a `CONFIRM-3` verdict, and the 08-04 morning evaluation supplied next-PM outcomes. Evidence is still insufficient to judge the gate: the sole YES (JELD) reached only $1.71 versus its $1.76 confirmed close (-2.8%); three of four recorded NO rows failed outright (ABTS -9.5%, BRCC flat, CSAI -3.0%), while IPW rose +24.1% but remained below its ~$0.90 AH peak. The prior replay result does not yet generalize from this n=5 live sample.

**Step taken:** **Pilot / Initiative 3:** appended the first out-of-sample verdict-to-next-PM table to `INIT3_IGNITION_TIMING.md` and updated the roadmap. **Parallel research / Initiative 6:** re-ran the continuation-gate and causal mechanical-exit simulations after the 08-04 VGAS row.

**Result:** Initiative 3 remains the highest expected dollars-per-time lever because a real selection filter could improve every AH trade without new pulses, but no gate or cadence change is justified. Initiative 6 advanced cheaply in parallel: VGAS raised its admitted set from n=10 to **n=11**, still below the n>=12 one-minute-exit trigger; 5-minute exits remain negative after the 1-3% spread (best trail12 mean -0.2%, median -2.5%). `node --check scripts/ah-5m-confirmation.js` and the live JELD/IPW replay passed.

**Hypothesis / next step:** Collect distinct `CONFIRM-3` candidates and their next-PM outcomes until the live sample can test whether YES rejects fades or finds continuations. Do not change entry logic or scan timing. For Initiative 6, accumulate one more admitted PM-only gapper, then run the deferred 1-minute exit test.

**Needs from Juan:** nothing.

### 2026-08-03 — Initiative 3: third-bar confirmation instrumented

**Evaluated:** The 2026-07-31 replay **worked** as research: its third-bar local-volume gate admitted all 3 labelled winners and no 6 labelled fades, while showing that denser five-minute trading scans would pay 6.1% worse entries on average. There has been no new AH session since the replay, so live out-of-sample evidence remains insufficient. Init 6 also remains insufficient at n=10 admitted PM-only gappers, below its n>=12 one-minute-exit trigger.

**Step taken:** Added `scripts/ah-5m-confirmation.js` and wired it into `prompts/post-market-scan.md` as a log-only `CONFIRM-3` scanner column for every >10% AH candidate. The tool applies the replay's local-volume ignition and third-bar hold test, returning YES, NO, or PENDING. The prompt prohibits it from affecting entries, skips, grades, rankings, or schedules.

**Result:** `node --check` passed. A historical run reproduced YES for AMIX, NUWE, and KUST, and NO for ONMD and BOOM. This is the highest expected dollars-per-time step because it turns the only recent gate that separated winners from fades into an out-of-sample measurement without risking paper capital or adding scan cost.

**Hypothesis / next step:** Live `CONFIRM-3` rows should keep rejecting BOOM/ONMD-shaped fades while retaining high-volume AH continuations. Record each candidate's next-PM outcome, then test the separation after a meaningful out-of-sample sample before proposing an entry gate. Do not add five-minute pulses from the current evidence.

**Needs from Juan:** nothing.

### 2026-07-31 — Initiative 3: five-minute confirmation replay

**Evaluated:** The 2026-07-30 Init 3 retirement **worked**: all seven scheduled
AH scans plus both observation scans ran on 07-30 without the discarded pre-seed
calls, and the daily cycle remained intact. The parallel Init 5 p95 volume-scale
change also **worked** on its first live email charts: KUST's AH/PM volume bars
are readable despite a 2.4M outlier, with the 0.8M display cap and true maximum
label visible; BOOM's smaller bars are also visible. Init 6 remains
**insufficient data**: the refreshed exit sim has n=10 admitted PM-only gappers,
below the n>=12 trigger for the deferred one-minute test.

**Step taken:** **Research / Init 3:** built
`scripts/ah-5m-confirmation-replay.js` and replayed Juan's second/third 5-minute
price-plus-volume confirmation on 10 recent AH-open cases. This was the top
money-fast step because a causal volume gate that rejects fades while preserving
explosive continuations can improve selection expectancy on every AH cycle.
The gate compares each bar with that ticker's immediately preceding volume,
uses BOOM as a named negative control, enters hypothetically at the next 5-minute
open, and compares the result with the current legal scan grid. Added the full
result to `INIT3_IGNITION_TIMING.md`. No orders, entry rule, or schedule changed.

**Result:** The third-bar gate admitted **3/3 winners (AMIX, NUWE, KUST) and 0/6
fades**, rejected BOOM as Juan expected, and produced a +30.0% mean next-PM-open
return in the admitted set. The second-bar version caught 2/3 winners but falsely
admitted ONMD. Crucially, the third-bar entries were **6.1% worse than the first
currently legal grid price on average**, so the replay supports a selection
filter, not more 5-minute trading pulses. The sample is hand-labelled and small,
returns omit spread, and discovery is assumed, so this is evidence to instrument,
not promote. `node --check` and the full live-data replay both pass.

**Hypothesis / next step:** Add the third-bar local-volume verdict as a log-only
scanner column and collect out-of-sample candidates. It should continue to reject
BOOM-shaped modest-volume spikes and fades while retaining high-volume winners;
only propose an entry gate if live results preserve that separation. Do not add
5-minute pulses from this replay. Init 6 waits for admitted n>=12.

**Needs from Juan:** nothing. No trading-pulse schedule change is proposed.

---

### 2026-07-30: Init 3 pre-seed retired after second zero-lead night; Init 5 volume scale fixed

**Evaluated:** Prior Init 3 step (keep the day-movers pre-seed for 1–2 more
nights and look for an early SPIKE that the 22:30 screener misses): **didn't
work.** Night 2 repeated zero actionable lead: all pre-seed names were NO-SPIKE
at 22:15 CET; the 22:30 screener then found DCX/CRE/SXTP without an early flag,
and the real winner NUWE (+147% PM peak from close) was outside the pre-seed.
DCX was on the list, but its live 16:15 SIP check missed the ignition that replay
later placed at 16:03, showing bar-arrival lag rather than a watch-source edge.
Across two nights the pre-seed surfaced no useful name before the main screener.

**Step taken:** **Pilot / Init 3:** retired the pre-seed instrumentation block
from `prompts/post-market-scan.md`; this cuts dozens of low-value SIP calls from
each 22:00/22:15 run while preserving `scan.py --day-movers` for research and
the regular scan. This is the best money-fast pilot step because the experiment
showed no entry-price edge and consumed scan time that can move to the 5-minute
confirmation test. **Parallel / Init 5:** changed `scripts/chart.py` to cap only
strong volume outliers at the nonzero-bar p95, label the display cap and true
maximum, and mark clipped bars. This directly fixes Juan's ONMD review problem:
one regular-open print no longer flattens the AH/PM bars used to judge entries.

**Result:** No schedule, entry rule, or live trading logic changed. The retired
instrument had zero measured benefit over two live sessions. `chart.py` passes
`py_compile` and rendered ONMD with **232 Alpaca SIP extended-hours bars
backfilled**, a **0.5M display cap**, and the honest **14.0M true maximum**
visible; clipped bars carry triangle markers. Initiative 3 remains the highest
expected dollars/time lever because catching ignition on a second/third 5-minute
bar could improve entry by tens of percent, while the pre-seed could not reach
post-close igniters or beat the 22:30 screener.

**Hypothesis / next step:** Build a log-only replay over recent AH-open winners
and fades (including AMIX, NUWE, DCX, CRE) that enters hypothetically after the
second and third confirmed 5-minute price-plus-volume bar. Compare entry price,
PM return, false positives, and added pulse rounds against the current 15-minute
observation grid before proposing any trading-scan schedule change. Also check
the next daily email chart for whether the p95 cap makes AH volume readable
without hiding true outliers.

**Needs from Juan:** nothing. No new schedule proposal. Existing proposal (C),
the 23:45 + 00:15 CET entry-eligible scans, remains unapplied and available for
veto through the daily email.

---

### 2026-07-29 — Init 3: day-movers pre-seed evaluated (first live night) — zero entry-lead

**Evaluated:** Prior step (2026-07-28 Init 3: wire `scan.py --day-movers` as an
additive 22:00/22:15 CET pre-seed; check whether any day-mover SPIKEs before the
same name hits the 22:30+ screener) — **ran live 07-28 and produced zero lead.**
Of the four real AH ignitions that fired at the 22:30 CET screener (AMIX 16:03 ET,
YIBO 16:06, IOTR 16:08, EGG 16:06), **only EGG was on the day-movers watch list,
and it was the worst behaving (faded).** AMIX/YIBO/IOTR had no regular-session
footprint (Day% −1.4/−2.5/+3.0%) — pure post-close ignitions the pre-seed is
structurally blind to. AMIX went on to be paper-entered 07-28 AH and ran to **PM
+63% (07-29 winner)**, caught by the screener+spike-bar path, invisible to the
pre-seed. (The 07-28 spike-bar 403 tooling note was already fixed by the process
review pulse, commit 467c854 — not re-done here.)

**Step taken (pilot / Init 3):** Ran the extended winner census the roadmap
calls for — pulled AH-eve regular-session Day% (Alpaca daily bars vs prior close)
for the six most recent ah-detected *holdable* PM winners and scored each against
the pre-seed's ≥15% reach. Appended the table + first-night write-up to
`INIT3_IGNITION_TIMING.md`.

**Result:** **Only 2 of 6 recent winners (STFS +19.4%, BIYA +116.1% reg) are
reachable by the day-movers pre-seed;** the other 4 — AMIX (−1.4%), GMM (−8.5%),
INLF (+2.8%), POLA (+1.4%) — ignite post-close with no regular footprint. Across
the combined census the split is ~even (5 reg-day-movers / 5 post-close
ignitions), but the biggest/cleanest winners (AMIX +63% paper win, LGCL +114%)
both fall in the pre-seed's blind class. Decisive conclusion: **the pre-seed
gives no actionable entry-lead** — it surfaces ~half of winners, and even those
are already on the 16:30 ET (22:30 CET) screener a full 30 min before the 23:00
CET entry window opens. Its only theoretical edge is a name it flags at
22:00–22:15 that the 22:30 screener misses; that did not occur night 1.

**Hypothesis / next step:** Keep the pre-seed as cheap log-only for 1–2 more
nights and watch for the one thing that would justify it — an early-window
(22:00–22:15 CET) day-mover that SPIKEs and that the 22:30 screener does *not*
surface. If nights 2–3 also show no such name, trim the pre-seed instruction from
`post-market-scan.md` to save scan-time effort (an Init-3 cost cut, not a schedule
or trading-rule change). (Init 6) unchanged: build the 1-min-bar exit test once
the gate-admitted set reaches ~12 (at n=8). (Catalyst grading) watch the next
merger-arb candidate grade D at entry.

**Needs from Juan:** nothing blocking. No pulse-schedule change proposed this run;
Init 3 proposal (C) (23:45 + 00:15 CET entry-eligible scans) still sits unapplied
in its veto window.

---

### 2026-07-28 — Init 3: day-movers pre-seed WIRED (log-only); catalyst taxonomy split APPLIED (merger-arb ≠ Grade A)

**Evaluated:** Prior step (2026-07-27 Init 3: wire `scan.py --day-movers` as an
additive 22:00/22:15 CET watch source running `spike-bar.js` log-only) —
**executed today, and the build surfaced one thing the census missed.** The
census assumed the day-movers list was usable as-is; it is not. Run against the
whole market sorted by day%, the filter returns **39 of 50 rows on OTC**
(EDEYF +42400%, GRWC +1017%, dead tickers on 150-1,200 share average volume) —
untradable on Alpaca and enough to push every real NASDAQ name out of the 50-row
window. So the census's "3 of 7 clear the threshold" understated the practical
problem: without an exchange filter the list is mostly noise.

**Step taken (pilot / Init 3):** Added `--day-movers` to `scripts/scan.py`. The
day% filter used to be reachable only in the regular-session code path; it now
short-circuits `build_filters` in **any** session (during after-hours the
`change` column still carries the regular-session day%), sorts by `change`, and
restricts to `NASDAQ/NYSE/AMEX`. Wired it into `prompts/post-market-scan.md` as
an **early-window pre-seed for the 22:00 and 22:15 CET scans only**: run the
watch list, run `spike-bar.js` on each name, log ticker / Day% / verdict under a
`Day-movers pre-seed (log-only)` bullet. Explicitly instrumentation — no entries,
no gates, additive to the screener, with the LGCL counter-example written into
the prompt so no future run mistakes it for a replacement.

**Result:** Verified end to end. `scan.py --day-movers --session afterhours`
returns **26 listed hits** (down from 50 with 39 OTC); the default regular and
after-hours scan paths are unchanged (regular still merges its day-movers
supplement, now OTC-free); `spike-bar.js BIYA:2026-07-27 --now 17:00` and
`CNET:2026-07-27 --now 18:30` both return clean NO-SPIKE verdicts, so the
per-name leg works. This gives the 22:00/22:15 CET scans something to watch in
the window where the TradingView `postmarket_*` fields are still empty (0 hits
before ~16:30 ET) and the 16:08-16:53 ET ignition cluster is live.

**Step taken (parallel / catalyst grading):** Applied the 07-27 merger-arb
proposal. It drew no veto and DOMO has since **closed at -9.4%** — it held the
full 5-day Grade-A window, peaked +14.8%, and never left a $3.5-4.5 band, which
is exactly what a fixed cash deal price does. Under Juan's standing "apply,
don't ask" directive: a **definitive fixed-price cash buyout / asset purchase /
merger agreement is graded D (exit at first premarket opportunity)**, never
Grade-A-hold; rumored / competing-bid / unfixed-ratio M&A can still re-rate and
stays momentum-gradable. Written into the grading table in
`prompts/post-market-scan.md`, the Grade-A rules in
`prompts/position-evaluation.md` (re-grade an open position to D if its catalyst
is a fixed-price cash deal, regardless of the entry grade), and the holding-rules
table in `OPEN_POSITIONS.md`. `Day Trading.md` was not touched — it holds no
grade table.

**Hypothesis / next step:** (Init 3) the pre-seed should produce its first live
rows tonight; the hypothesis to check on the next run is whether any day-mover
shows a `SPIKE` verdict at 22:00/22:15 CET **before** the same name reaches the
22:30+ screener — that lag, if it appears, is the measured value of the pre-seed
and the input to any eventual entry use. Keep the caught/missed tally growing
(currently 3 caught: HIHO, CJMB, JEM / 1 miss: LGCL). (Init 6) unchanged: at
gate-admitted n>=12 build the 1-min-bar exit test. (Catalyst grading) watch the
next merger-arb candidate get graded D at entry instead of A.

**Needs from Juan:** nothing blocking. Two applied changes he can veto
retroactively: the merger-arb grading split, and the OTC exclusion on the
day-movers watch list (which also drops OTC names from the 21:30 CET regular
scan's supplementary merge — they were never tradable on Alpaca). No pulse
schedule change proposed this run; Init 3 proposal (C) (23:45 + 00:15 CET
entry-eligible scans) still sits in its veto window, unapplied.

---

### 2026-07-27 — Init 3: day-movers watch-source census extended (LGCL counter-example); Init 6 exit-sim refresh still NEGATIVE at n=8; DOMO merger-arb grading fix proposed to Juan

**Evaluated:** Prior step (2026-07-24 Init 6: build the 1-min exit test only once
the gate-admitted sample reaches ~12; keep `pm-open-scan` accumulating) —
**insufficient sample to advance, conclusion holds.** Re-ran
`pm-gapper-exit-sim.js`: the holdable PM-only tally reached 11 and the
continuation-gate admitted set grew from 7 to **n=8** (adds EHGO 07-23, a clean
holdable that *held* +59% to PM-last, and BIYA 07-27 +16% held). Even with those,
**every mechanical exit still has a negative median** (trail12 mean +2.4%/med
−2.0%, N1 mean +7.5%/med −1.3%, 1stLH mean +3.8%/med −2.0%); wins stay
INLF-outlier-driven and the gate still admits the uninvestable WLDS
false-positive. Admitted 8 < the ~12 threshold, so the deferred 1-min exit test
stands — the 07-24 "NEGATIVE at 5-min cadence" close is unchanged.

**Step taken (pilot / Init 3):** Extended the day-movers watch-source census
(the 07-22 n=7 test that gates wiring scan.py `--day-movers` as the 22:00/22:15
CET pre-seed) with the two AH→PM continuers from the 07-22/07-23 sessions — both
bigger PM moves than anything in the original 7. Pulled regular-session-only
Alpaca daily bars for JEM/LGCL/PLAG, computed each one's regular-session day%,
and cross-checked LGCL's regular-session volume against its 5-min bars. Wrote the
extension into `INIT3_IGNITION_TIMING.md`.

**Result:** The "winners are already regular-session day-movers" pattern
**half-holds and gains a decisive counter-example.** JEM (+34.3% reg close, PM
+48% winner) confirms the caught path. But **LGCL breaks the "both winners
caught" claim**: it was flat and low-volume in the regular session (−3.1% close,
+9.2% high, **78.6k reg-session sh ≈ prior day's 94k**), ignited entirely
post-close (AH high $1.58 at 18:15 ET), and ran to **PM +114% — the biggest PM
winner in the whole sample.** A regular-session day-movers *or* relative-volume
pre-seed misses it completely (no regular footprint). Refined design: wire the
day-movers list as an **additive log-only pre-seed** (rescues already-moving
AH→PM continuers 15–30 min ahead of the 16:30 ET screener) but treat it as
**structurally incomplete** — flat-regular post-close igniters (PAPL fader, LGCL
+114% winner) still depend on the 16:30 ET screener + the tight AH grid, so the
two detection paths are complementary, not substitutes. Tally on the question:
3 caught (HIHO, CJMB, JEM) / 1 clear miss (LGCL).

**Step taken (route to Juan / catalyst grading):** Surfaced Juan's fresh 07-24
DOMO feedback ("I have no idea why you're holding that") as a concrete proposal
in the roadmap open-asks: **split the catalyst taxonomy so a definitive cash
buyout / fixed-price merger agreement is graded None/exit-premarket, never
Grade-A-hold.** An all-cash deal pins the price near deal value and kills the
AH→PM momentum the strategy needs (DOMO sat dead $3.92→$3.71 for days). This
edits the `Day Trading.md`/`OPEN_POSITIONS.md` holding-rules table — outside this
pulse's write scope — so it is **proposed, not applied.** DOMO itself is already
exit-flagged for the next premarket eval (still open at −5.4%; AH book ~30%
spread, so exit waits for premarket).

**Hypothesis / next step:** (Init 3) wire scan.py `--day-movers` as an additive
22:00/22:15 CET watch source running `spike-bar.js` log-only, and keep the
day-movers-vs-winner tally growing to see whether the "already-moving" subset is
worth an eventual entry signal. Verify it live on the first AH session where a
day-mover ignites in the pre-16:30-ET window. (Init 6) at admitted n≥12, build
the 1-min-bar exit test (peak is intrabar); also consider tightening the gate so
uninvestable wick names like WLDS aren't admitted. (Catalyst grading) if Juan
doesn't veto, a future run applies the merger-arb taxonomy split once it has a
write path (Juan edit or scanner-improvement scope).

**Needs from Juan:** **one proposal** — approve (or veto) splitting cash
buyouts/definitive mergers out of Grade-A-hold into None/exit-premarket
(prevents holding dead merger-arb money like DOMO). Nothing else blocking; the
Init 3 census and Init 6 refresh are log-only.

---

### 2026-07-24 — Init 6: mechanical-exit sim — problem (a) NEGATIVE at 5-min cadence, no live PM-gapper scalp pulse justified

**Evaluated:** Prior step (2026-07-23: simulate a mechanical exit on the
continuation-gate-admitted set to measure the capturable slice of the +28.5%
PMHigh ceiling) — **worked; the answer is decisively NEGATIVE.** The admitted set
also grew to n=7 (WBUY + EHGO logged 07-23, both PMHigh winners), so the ceiling
mean rose to +31.1%, but the mechanical-exit test shows it is not capturable.

**Step taken (pilot / Init 6):** Built `scripts/pm-gapper-exit-sim.js` (log-only,
no orders). It reuses the exact continuation gate to fix the entry (R+3 open),
then walks the premarket 5-min bars from entry applying **causal, close-based**
exits with no lookahead: trailing stop 8/12/15/20%, N-bars hold 1/2/3, and
first-lower-high. Benchmarks printed alongside: PMHigh (perfect ceiling) and
PM-last (hold-to-09:25 floor). Ran it on all footprint=none gappers; wrote up
"Mechanical-exit sim (2026-07-24)" in `INIT6_PM_GAPPER_SIM.md`.

**Result:** **No mechanical exit converts the admitted set to positive expectancy
after spread.** PMHigh ceiling mean +31.1% but **median only +11.0%** — the mean
is an INLF (+96%) outlier. Every exit rule: trail8 mean -0.0%/med -3.9%/1-of-7
wins, trail12 +0.3%/-3.9%/2, trail20 -8.8%/-11.2%/2, N1 +8.8%/-1.1%/3 (the +8.8%
is *entirely* INLF +83.5%), N2 +6.1%/-1.7%/2, first-lower-high +4.5%/-2.9%/1.
Every rule's median is negative *before* the ~1-3% micro-cap PM round-trip spread,
so after spread the admitted set is a loser and no rule reliably beats even the
flat PM-last floor. Root cause: the peak prints **inside the entry bar** (INLF
08:15Z open $3.76 -> $7.19 high, close $6.13), uncapturable by a rule that only
sees 5-min closes. Also surfaced a gate false-positive: WLDS (07-24, classified
*uninvestable*) was admitted and loses on every exit. **Conclusion: do not
propose a live PM-gapper scalp pulse** — the gate is a decent wick *filter* but
yields no tradable edge at 5-min cadence.

**Hypothesis / next step:** The binding constraint is exit *cadence*, not exit
*logic* — the peak is intrabar, so the only untested angle is a **1-min-bar exit**
(finer trailing stop / limit-on-spike) that could sell the intrabar spike. But
n=7 is tiny and outlier-dominated (drop INLF and every rule is flatly negative),
and a 1-min exit means a near-continuous monitoring pulse for a rare setup — high
cost for thin evidence. **Conservative call: keep `pm-open-scan` accumulating
gappers; build the 1-min exit test only once the admitted sample reaches ~12** so
the result doesn't hinge on one INLF. Problem (a) stays log-only; no
`Day Trading.md` change, no live pulse. Also worth a later pass: tighten the gate
so uninvestable names like WLDS don't get admitted.

**Needs from Juan:** nothing blocking (log-only research under his standing
no-approval directive). No live-trading change proposed this run.

---

### 2026-07-23 — Init 6: continuation-gate sim reopens problem (a) positively — gate rejects 7/7 wick-fades, admitted names reach +28.5% PM peak (but hold still loses)

**Evaluated:** Prior step (2026-07-22 Init 3: test whether a regular-session
day-movers list contains the AH igniters, to justify a pre-16:30-ET SIP watch
source) — **worked (n=7, promising not proven).** 3/7 cleared the day-mover
threshold and both traded winners (HIHO, CJMB) were caught; misses skewed to
faders. Not advanced further this run because Juan's 2026-07-23 directive
("make changes so we can catch the winner of today ... don't ask for approvals")
re-opened Init 6 problem (a) as the explicit top priority, so this run took the
Init 6 step his feedback routed to `strategy-advance`.

**Step taken (pilot-track / Init 6, per Juan's directive):** Built
`scripts/pm-gapper-continuation-sim.js` (log-only, no orders) — the
continuation-gated PM-only-gapper entry the 2026-07-23 feedback asked for. It is
a **causal** gate (uses only bars available at decision time): ignition = first
PM bar with >= 3000 trades; enter at R+3 only if R+1 and R+2 each close >= 80% of
the running high and VWAP is non-declining; else skip. Ran it on all 18 PM-only
gappers (footprint=none) in `pm-open-scan.csv`; added a PMHigh-after-entry
(peak-scalp) exit column. Wrote up the result in `INIT6_PM_GAPPER_SIM.md`.

**Result:** **The gate reopens problem (a) positively.** (1) It **rejects 7/7
wick-fades** — SXTC (R+1 close 6.06 < 80% of its 7.91 wick), LICN, ZCMD, UONEK,
DXST + 2 thin — the 80%-of-high hold rule is the discriminator the earlier
fixed-time sim lacked. It false-rejects 5 holdables (SHPH, EHGO, SLGB +76.5%…),
mostly on the VWAP rule (a tuning knob). (2) On the 6 admitted names, holding to
PM-last/RegOpen still loses **-9%**, but the **PMHigh reachable after entry is
positive on every one**: mean **+28.5%**, median +15.7% (INLF +96%, WBUY +31%,
EHGO +21%, MIMI +11%, SKYQ +10%, BJDX +3%). So the gated entry lands near the
ramp base and a positive peak exists — the 07-14 "12/12 combos lose" close was an
artifact of fixed-time entry held to a fixed exit. **The gate is a scalp rule,
not a hold rule.** No live orders; no `Day Trading.md` change.

**Hypothesis / next step:** PMHigh (+28.5%) is the optimistic ceiling (perfect
exit) and PM-last (-9%) the pessimistic floor; the truth is what a mechanical
exit captures between them. **Next run: simulate a mechanical exit** on the
admitted set — trailing stop (8/12%), fixed N-bars-after-entry, or
exit-on-first-lower-high — to measure the capturable slice. If a simple exit
clears the spread and beats flat, that is the evidence to propose a live
PM-gapper scalp pulse to Juan (a live-trading change → propose, don't apply).
Also test relaxing the VWAP-non-declining rule (it false-rejected SLGB/EHGO, two
big holdables). Keep `pm-open-scan` accumulating gappers to grow n.

**Needs from Juan:** nothing blocking (log-only research under his standing
no-approval directive). A live PM-gapper scalp pulse would be proposed once the
mechanical-exit sim shows a capturable edge — not yet.

---

### 2026-07-22 — Init 3: watch-list source for the pre-16:30-ET open window tested — regular-session day-movers catches both traded winners, misses skew to faders

**Evaluated:** Prior step (2026-07-21: after the next 1–2 AH sessions, if
proposal (C) draws no veto, wire the late-window scans; keep accumulating
SPIKE/NO-SPIKE) — **worked / no trigger to act yet.** The 07-21 AH session ran
(evaluated in `log/2026-07-22/log.md`): the spike-bar column kept working (AEHL
flagged SPIKE→FADE, correctly gate-blocked; KUST dead-cat), the winner **SXTC was
a PM-only gapper** (+223% at PM open, no AH footprint — not an AH-detection
sample), and **no late-window (17:00–18:30 ET) igniter appeared**, so proposal
(C)'s late-window tally holds at 2 (CJMB, RDGT). One session passed with no veto,
tally not firmed → **hold (C) one more session** (conservative; don't wire an
entry-eligible schedule change on a soft tally).

**Step taken (pilot / Init 3, step b):** Tested the open question that gates
building the "SIP spike-bar on a pre-seeded watch list" mechanism (needed because
the screener is blind before ~16:30 ET): **does a regular-session day-movers list
actually contain the AH igniters we care about?** Pulled Alpaca daily
(regular-session-only) bars for 7 recent AH igniters and computed each one's
regular-session day% vs scan.py's `MIN_DAY_CHANGE_REGULAR=15` threshold. Wrote
the census table + design conclusion into `INIT3_IGNITION_TIMING.md`.

**Result:** **3 of 7 clear the day-mover threshold — but both traded WINNERS are
in the caught set** (HIHO +19.2% reg close, CJMB +16.2% reg close), and the
misses skew to faders/losers (PAPL −23.6%, KUST dead-cat, AEHL fade; RDGT the one
profitable miss at +12% borderline). The AH→PM continuations we make money on
were **already +16–19% in the regular session** before their AH ignition, so a
16:00 ET day-movers list surfaces them and lets the 22:00/22:15 SIP spike-bar
check catch the ignition bar 15–30 min ahead of the ~16:30 ET screener (HIHO
ignited 16:04, screener surfaced it only at 22:30). The list's blind spot
(flat/down-regular post-close-news names like PAPL) can't be beaten by SIP — no
symbol to check until the screener populates at 16:30 ET. So the day-movers list
is a **useful but partial** early-watch source, and its blind spot skews toward
names we lose on or correctly skip (n=7, promising not proven).

**Hypothesis / next step:** (a) Wire scan.py `--day-movers` (regular-session
high-change list) as the 22:00/22:15 CET watch source and run `spike-bar.js` on
each name **log-only**, so the tighter grid accumulates ignition-bar timing on
day-movers before the screener wakes up. (b) Over more sessions, test whether the
"AH→PM winners were already regular-session day-movers" pattern holds — if it
does, an early SIP-caught day-mover ignition becomes a candidate entry signal (a
future proposal). (c) Re-check proposal (C) after the next AH session: if a third
late-window igniter appears or the window stays quiet with no veto, wire the
23:45/00:15 CET late-window scans.

**Needs from Juan:** nothing new. Proposal (C) veto window (add 23:45 + 00:15 CET
entry-eligible late-window scans) stays open — silence = wire a future run once
the tally firms; say the word to veto.

---

### 2026-07-21 — Init 3: first live wired-scan session — spike-bar column validated end-to-end; screener blind before 16:30 ET; late-window densification proposed (C)

**Evaluated:** Prior step (2026-07-20: after the 07-20 AH session, evaluate the
wired 22:15/22:45 scans' live catch-lag and confirm the spike-bar column
populated on real candidates) — **worked, with two decision-relevant findings.**
The 07-20 AH session ran (`log/2026-07-20/log.md`). **The spike-bar column
populated live on 6 real names** (HIHO/SHPH SPIKE 16:04, PAPL SPIKE 17:09, ADVB
SPIKE 17:32, RDGT SPIKE 18:00, GORO NO-SPIKE) — validated end-to-end in the cron
and reproduces on replay. **GORO NO-SPIKE was a correct skip** (AH +240% on 17K
sh / 160M float = bad print). But SPIKE ≠ winner: PAPL and ADVB fired SPIKE then
faded, so the column marks ignition, not outcome — continuation gating stays
required. **On catch-lag:** the 22:00/22:15 scans returned **0 screener hits** —
the TradingView postmarket field doesn't populate until ~16:30 ET, so the
open-hour densification adds nothing via the *screener*; only the SIP cross-check
reached the early window (rescued ADVB at 22:15). HIHO ignited 16:04 but wasn't
surfaced by the screener until 22:30 (~26 min lag; cost no entry — entry banned
before 23:00 CET).

**Step taken (pilot / Init 3):** Wrote up the first live wired-scan session in
`INIT3_IGNITION_TIMING.md` (new "First live out-of-sample AH session" section):
the 6-name column-validation table, the screener-blind-before-16:30-ET finding,
and a strengthened late-window densification case. Verified `spike-bar.js`
reproduces (`HIHO:2026-07-20 --now 17:00` → SPIKE 16:04; `GORO:2026-07-20` →
NO-SPIKE). Updated the roadmap Init 3 status, Needs-from-Juan, and consolidated
open-asks with proposal (C).

**Result:** Two carry-forward findings and one Juan proposal. (1) The spike-bar
instrument is live-validated (6/6 names, correct NO-SPIKE skip). (2) The open-hour
densification is defeated by the screener's ~16:30 ET population lag — the
next step is to run the SIP spike-bar check on the regular-session watch list in
the 22:00/22:15 scans, since the screener is empty there. (3) **Late-window
densification proposal (C):** RDGT (07-20, ignited 18:00 ET, first-seen at the
18:30 final scan so the 2-AH-scan gate was un-meetable, ran to PM +47%) joins
CJMB (07-16 traded winner +19.8%, caught +27m late) — an 18:15 ET scan (00:15
CET) would have made RDGT entry-eligible. Late-window support tally = 2 (low end
of the 2–3 trigger). Proposed adding 23:45 + 00:15 CET (17:45 + 18:15 ET)
entry-eligible scans; since these change live entry behavior, **Juan veto window,
not applied**.

**Hypothesis / next step:** (a) After the next 1–2 AH sessions, if proposal (C)
draws no veto, wire the 23:45/00:15 CET late-window scans. (b) Prototype the
SIP-spike-bar check on the regular-session watch list inside the 22:00/22:15
scans (the screener is blind <16:30 ET, so SIP is the only path to shrink open-
window catch-lag) — log-only first. (c) Keep accumulating SPIKE/NO-SPIKE
readings toward the two live tests: does NO-SPIKE reliably precede a fade (skip
filter), and does the SPIKE-bar price beat our current late entry (this session:
HIHO SPIKE $1.08 vs our $1.50 entry = 39% cheaper, but HIHO faded to a -16% exit,
so entry-price gain ≠ trade win — need more cases).

**Needs from Juan:** **veto window on proposal (C)** — add 23:45 + 00:15 CET
(17:45 + 18:15 ET) entry-eligible late-window scans. Silence = wire a future run
once the tally firms; say the word to veto. Nothing else blocking.

---

### 2026-07-20 — Init 3: spike-bar detector validated out-of-sample; new late-BUILD detection gap surfaced (CJMB winner ignited in the coarse late window)

**Evaluated:** Prior step (2026-07-17 2nd: build + wire the log-only spike-bar
column; then next AH session confirm the 22:15/22:45 scans fire and the column
populates) — **insufficient data to evaluate live yet.** No post-market scan has
run since 07-17: the new 22:15/22:45 crons are Mon–Thu (`1-4`) and were added on
Fri 07-17, so their first fire is tonight (Mon 07-20). No log dir exists for
07-18/07-20. Confirmed the crons are in `scheduler.json` (22:15/22:45 present,
Mon–Thu). Live catch-lag evaluation carries to the next run.

**Step taken (pilot / Init 3 + Init 1):** Rather than idle until tonight's data,
strengthened the pilot's evidence base **out-of-sample**: ran `scripts/spike-bar.js`
on 3 AH names from the 07-16 session that were NOT in the original 10-name
ignition audit (BIYA, GCTK, CJMB — including CJMB, the name we actually entered
and won +19.8% on). Appended the results + the new-grid lag mapping to
`INIT3_IGNITION_TIMING.md`.

**Result:** Three findings. (1) **Detector generalizes 3/3** — SPIKE fired at a
minute consistent with each daily-log narrative (BIYA building from open →
16:28ET; GCTK early pump → 16:57ET; CJMB "dead until 17:30 then exploded" →
17:33ET). No false negatives on real movers. (2) **GCTK is a SPIKE→fade**
(ignited 16:57 +30%, then declined, correctly skipped): the first co-spike bar
marks ignition, **not** a buy — continuation/BUILD gating stays required before
any spike-bar entry trigger. (3) **New gap — the 17:00–18:30 ET late window is
still 30-min-coarse and it caught our actual traded winner late.** CJMB ignited
17:33 ET but the first scan to see it was 18:00 (+27 min lag) and we didn't enter
until the 18:30 final scan. The 07-17 densification only covers the open hour
(16:15/16:45), so late-BUILD igniters remain undercaught. The 3 fresh cases also
didn't fall in the new open-hour scans' benefit sub-windows (16:00–16:14 /
16:31–16:44), so those scans' payoff still awaits a live igniter there.

**Hypothesis / next step:** (1) After tonight's AH session, evaluate the wired
22:15/22:45 scans' live catch-lag and confirm the spike-bar column populated on
real candidates. (2) Track a **late-BUILD tally** (17:00–18:30 ET igniters);
CJMB = 1. If it reaches 2–3, propose densifying the late window (add 23:45 +
00:15 CET = 17:45 + 18:15 ET) — a trading-scan timing change, so propose to Juan
for veto, don't apply silently. (3) Once ~1–2 weeks of live SPIKE/NO-SPIKE
readings accumulate, test whether NO-SPIKE reliably precedes a fade (skip filter)
and whether the SPIKE-bar price beats our current late entry (entry-trigger
proposal). Keep the column log-only until then.

**Needs from Juan:** nothing. Out-of-sample validation is log-only; no schedule
or live-rule change made this run.


### 2026-07-17 (2nd step) — Init 3/1: log-only spike-bar detector built + wired as a scan column (Juan's "catch the first volume spike bar")

**Evaluated:** Prior step (2026-07-17 1st run: wire the 22:15/22:45 CET AH-open
observation scans; withdraw the premature sub-3M live-flip after CRE was found to
be a Yahoo bad print) — **worked; the scans are in `scheduler.json` and the
sub-3M trigger correctly sits at 3/5.** The just-wired scans have not fired yet
(next AH session), so their catch-lag improvement is **insufficient data** to
judge — evaluate after the next AH cycle. The stated next step (add a log-only
spike-bar detection column so the tighter grid surfaces the ignition bar) was
actionable and verifiable now, so this run took it.

**Step taken (instrument / Init 3 + Init 1):** Built `scripts/spike-bar.js`
(log-only, no orders) — the live counterpart of `ignition-timing.js`. For a
`SYM:YYYY-MM-DD` (AH-eve) + optional `--now HH:MM` ET cutoff it pulls real Alpaca
SIP 1-min AH bars and reports whether the first price+volume **co-spike**
(ignition) bar has fired as-of that scan minute (same detector as the audit tool:
high ≥ +15% vs the regular-session close AND trades ≥ 20 and ≥ 5× the running
median trades). Output is one line: `SPIKE 16:53ET +19% $1.48 72 trades / 25k sh`
or `NO-SPIKE flat/faded`. Wired it into `prompts/post-market-scan.md` as a
**log-only column** (run per >10% AH candidate, record the verdict; explicitly
NOT an entry gate yet).

**Result:** Verified consistent with the validated `ignition-timing.js` audit on
every test: IVF 16:53ET +19%, TGHL 16:21ET +40%, XCUR 16:08ET +41%. The negative
filter also reads correctly — **LVLU** (Juan's "clearly terrible: no volume
spike" example) returns **NO-SPIKE**, and IVF as-of 16:30 ET (before its 16:53
ignition) returns NO-SPIKE, flipping to SPIKE as-of 17:00 ET. So the tool cleanly
separates real igniters from no-spike names and is time-aware (won't fabricate an
ignition the scan couldn't yet have seen). This is the missing detection signal
for Juan's 2026-07-16 "catch the first volume spike bar" ask; the 15-min AH-open
grid + this column will now accumulate live ignition-bar timing.

**Hypothesis / next step:** Next AH session, confirm the 22:15/22:45 scans fire
and the spike-bar column populates on live candidates (evaluate the wired scans'
catch-lag then). Once ~1–2 weeks of live SPIKE/NO-SPIKE readings accumulate,
test two things: (1) does NO-SPIKE reliably precede a fade (a candidate skip
filter, per Juan), and (2) does the SPIKE bar price make a viable entry vs our
current late entry — which would justify proposing a spike-bar entry trigger
(touches live trading → propose to Juan). Keep the column log-only until then.

**Needs from Juan:** nothing. The AH-open scan-timing change (proposal A) was the
prior run's veto item and is now applied (no objection); this step is log-only
instrumentation.

---

### 2026-07-17 — Init 3: AH-open observation scans WIRED; sub-3M fade-exception (b) validated → CRE was a bad print, trigger drops to 3/5 (live flip held)

**Evaluated:** Prior step (2026-07-16: propose AH cadence change (A) — add 22:15
+ 22:45 CET observation scans — with a Juan veto window, "silence = wire it next
run") — **veto window passed with no objection; wired.** Both new scans fire
before the 23:00 CET entry ban, so they are observation/log-only (no new entry
window), which the strategy-advance rules allow applying directly.

**Step taken (pilot / Init 3):** Added crons `trading-post-market-2215` (`15 22
* * 1-4`) and `trading-post-market-2245` (`45 22 * * 1-4`) to `scheduler.json`,
both pointing at `post-market-scan.md`. JSON re-validated (24 jobs). The AH-open
hour is now 15-min-spaced (22:00/22:15/22:30/22:45/23:00 CET), halving catch-lag
on the dominant 16:08–16:53 ET ignition cluster. Updated `STRATEGY_ROADMAP.md`
Init 3 status + schedule + Open-asks.

**Step taken (parallel / Init 1 — validate the sub-3M fade exception the
morning-eval handed off):** The 07-16 morning eval said the ≥4/5 sub-3M-float
PM-open re-check trigger was "REACHED" and handed the live `Day Trading.md`
entry-rule flip to this pulse. Before flipping a live rule I pulled real Alpaca
SIP 5-min bars for each sub-3M fader's PM session to measure the **(b) realistic
PM-open re-entry** economics (the number the proposed rule actually earns):
- **LNKS** (1.5M, Jun 18 PM): real SIP peak **$4.98** on 2.9M sh/bar, 32k
  trades. (b) first-bar VWAP $2.97 → $4.98 = **+68%**. Genuine liquid re-explode.
- **RPGL** (1.1M, Jul 9 PM): peak **$3.05** *in the first PM bar*, then fades.
  (b) first-bar VWAP $2.76 → $3.05 = **+11%**, thin and hard to catch.
- **ATPC** (475K): (b) **+22%** (already on file).
- **CRE** (1.1M, Jun 18 PM): real SIP peak **$4.04**, *below* its AH peak $4.65
  — CRE **faded further, did NOT re-explode**. The tally's "PM peak $5.99 +90%"
  is a **Yahoo bad print**.

**Result:** **CRE was a false member of the trigger** (bad print). Removing it,
the sub-3M count is **3 of 5 blew past** (LNKS, RPGL, ATPC), CRE + IOTR fell
short — the ≥4/5 trigger is **NOT met**. So the live-flip handoff was **premature
and is withdrawn this cycle** (corrected in `prompts/morning-evaluation.md`). But
the exception is **not a mirage**: the (b) economics on the genuine cases are
positive (LNKS +68%, ATPC +22%; RPGL +11% thin). It needs **one more clean,
SIP-verified sub-3M blow-past to reach ≥4/5**, then strategy-advance applies it
(sized to the realistic (b), not the optimistic (a)). The prospective (a)/(b)
recording already added to the morning eval collects that live.

**Hypothesis / next step:** (Init 3) add a log-only **spike-bar detection
column** to the scan output so the now-tighter AH-open grid actually surfaces the
ignition bar (Juan's "catch the first volume spike bar" ask) — the scans are in
place; the detection signal is the missing piece. (Init 1) watch for the 4th
clean sub-3M PM-open re-explosion on SIP-verified peaks; flip the live exception
when the count reaches ≥4/5. Guard morning-eval tally figures against Yahoo bad
prints — CRE shows a single bad print can fabricate a trigger.

**Needs from Juan:** nothing blocking. The two AH-open observation scans are
wired (retroactive veto still fine). No live entry-rule change was made.

---

### 2026-07-16 — Init 3: ignition-vs-grid audit done (grid too coarse, not mis-phased) — AH-cadence change proposed to Juan; Init 5 render-race 200-check shipped

**Evaluated:** Prior step (2026-07-15: advance Init 3 with the timing audit —
find each recent winner's ignition minute from 1-min SIP bars and tabulate
against the AH scan grid to quantify how often scans fire before vs after
ignition) — **worked; produced a decisive, actionable table.**

**Step taken (research / Init 3):** Built `scripts/ignition-timing.js` (log-only,
no orders): for a ticker + AH-evening date it pulls real Alpaca SIP **1-min**
bars for the AH session, finds the ignition bar (first bar ≥ +15% vs the daily
close *and* carrying a volume co-spike: ≥20 trades and ≥5× running median
trades), then maps that minute onto the current AH scan grid (15:30–18:30 ET /
21:30–00:30 CET). Ran it on 10 AH winners; wrote up `INIT3_IGNITION_TIMING.md`.

**Step taken (parallel / Init 5):** Added a post-push raw-URL **HTTP-200 poll**
to `prompts/daily-email.md` — after committing/pushing charts, poll each
`raw.githubusercontent` URL until 200 (short retries) before sending, and drop
any image still not live. Closes the 07-09 Gmail render race (RPGL didn't show
while SUNE did because the proxy cached a 404 before the CDN propagated).

**Result (Init 3):** **The grid is too coarse, not mis-phased** — the earlier
"our 16:15 ET scan runs before IVF's 16:53 ignition" framing was too narrow. 9
of 10 winners ignite *inside* the grid window, but the 30-min spacing means the
first scan sees the move **7–29 min after ignition (median ~+18m)**, already
partway up. Two gaps: (1) **AH-open cluster** — 6 of 10 ignite 16:08–16:53 ET
and wait up to +22m for the 16:30/17:00 scan (XCUR 16:08, ATPC 16:09, EDHL
16:12, TGHL 16:21, VTAK 16:47, IVF 16:53); (2) **tail past the 18:30 ET grid
end** — MSW ignited 19:01 ET and the grid never sees it live (GMM 18:05 / KUST
18:25 sit at the edge). **Proposed to Juan (touches trading-scan timing — veto,
don't apply silently):** (A) add 22:15 + 22:45 CET (16:15/16:45 ET) observation
scans to 15-min-space the open hour (halves catch-lag on the dominant cluster;
no new entry window, entry still banned before 17:00 ET); (B) add 01:00/01:30
CET tail scans (Juan pre-authorized, but tail count MSW=1 is below the 3–4
trigger, so held). (A) is the enabler for Juan's 07-16 "catch the first volume
spike bar" ask — its blocker is exactly this detection latency.

**Hypothesis / next step:** If Juan doesn't veto (A), wire the two AH-open
observation scans (16:15/16:45 ET) — a schedule change, applied only after the
veto window. If he vetoes or wants a different cadence, adjust. Either way, the
tradeable form of the co-spike entry (Init 1 reopened angle) then needs a
spike-bar detection rule in the scan output (log-only first). In parallel, the
last Init 5 follow-on is GitHub Pages HTML reports.

**Needs from Juan:** **veto window on proposal (A)** — add 22:15 + 22:45 CET
observation scans (log/detect only, no new entry window). Silence = wire it next
run. Evidence in `INIT3_IGNITION_TIMING.md`.

---

### 2026-07-15 — Init 1: volume-lead hypothesis FALSIFIED (ignition is a single-minute co-spike); roadmap re-ranked, Init 3 promoted

**Evaluated:** Prior step (2026-07-14: Init 6 problem-(a) PM-gapper entry pilot,
plus re-rank the roadmap since Init 6's two tested hypotheses failed) — **worked;
both Init 6 levers are confirmed negative.** With no active pilot and Init 6
exhausted, this run re-ranked by the North Star and advanced the top *untested*
money lever, Init 1 (earlier volume-lead entries — Juan: "we catch spikes late,
once +50-100%").

**Step taken (research / Init 1):** Built `scripts/volume-lead.js` (log-only, no
orders): for a ticker + AH-evening date it pulls real Alpaca SIP 5-min bars
across the AH + next-morning PM sessions and measures when per-bar volume crosses
a relative threshold vs when price crosses +20%/+50% (LEAD = t(price+20%) −
t(volSurge); positive => volume leads). Ran it on 7 winners; zoomed the clearest
(IVF) to 1-min bars. Wrote up `INIT1_VOLUME_LEAD.md`.

**Result:** **Hypothesis falsified.** On every real AH mover (IVF, VTAK, EDHL,
MSW) price reaches +20% at or before the volume threshold (LEAD ≈ 0 or negative)
— volume does not lead. At 1-min resolution IVF was dead (100-300 sh, 1 trade/min,
flat $1.24) until **16:53 ET, when a single bar carried both a +19% price jump
and a 25k-share / 72-trade volume spike** — no quiet volume ramp to front-run.
The two PM-only gappers (GLXG/CIIT) flagged a big "lead" but it is a false
positive on thin AH prints (hundreds of shares, <40 trades); their real move is a
news-driven 04:00 ET PM explosion with no tradeable AH precursor. **Reframe:**
"we catch late" is real, but the fix is faster ignition detection / scan timing —
our AH scan runs ~22:15 CET / 16:15 ET, ~38 min *before* IVF's ignition — which
is **Initiative 3**, not a volume-lead entry rule. Init 1 folds into Init 3 and
is effectively closed. Re-ranked the roadmap: Init 3 promoted to the top research
lever; Init 6 demoted (no active pilot, both levers negative); Init 1 marked
falsified.

**Hypothesis / next step:** Advance Init 3 with the timing audit — for each
recent winner, find the ignition minute (ET) from 1-min SIP bars and tabulate it
against the current AH scan grid (21:30–00:30 CET) to quantify how often our
scans fire *before* vs *after* ignition. If winners systematically ignite in a
window our grid misses, that justifies a concrete retimed/added AH observation
scan — a trading-scan timing change, so **propose to Juan for veto, don't apply
silently**. In parallel, Init 5 has two ready low-risk items (post-push raw-URL
200-check; GitHub Pages HTML reports).

**Needs from Juan:** nothing this run. A scan-timing change proposal is likely
next run once the ignition-vs-scan-grid audit quantifies the miss.

---

### 2026-07-14 — Init 6: PM-only-gapper entry pilot is NEGATIVE (problem a closed); Init 5 AH/PM volume blank fixed in chart.py

**Evaluated:** Prior step (2026-07-13: design a log-only hypothetical-entry
pilot for the 4 holdable PM-only gappers) — **done, and it came back decisively
NEGATIVE.** The tracker now holds 5 holdable + no-AH-footprint gappers (SHPH
07-08, BJDX 07-09, MIMI 07-13, EHGO 07-13, BJDX 07-14).

**Step taken (pilot / Init 6):** Built `scripts/pm-gapper-sim.js` (log-only, no
orders). For each holdable PM-only gapper it hypothetically buys at the 05:00 ET
pulse time (09:00Z bar open) and, as a separate scenario, at an earlier 04:10 ET
pulse (08:10Z, two bars after the 04:00 ramp), then exits at PM-last (09:25 ET),
regular-open (09:30 ET), regular-high (best-case), and regular-close, off real
Alpaca SIP 5-min bars. Verified end-to-end; wrote up `INIT6_PM_GAPPER_SIM.md`.

**Step taken (parallel / Init 5):** Added `backfill_ext_volume()` to
`scripts/chart.py` — after the Yahoo fetch (vol=0 for all pre/post bars) it
pulls Alpaca SIP 5m bars via `broker.js` and fills the missing extended-hours
volume by timestamp. Verified on MIMI: **170 ext-hours bars backfilled**, the
premarket volume panel now renders. Closes Juan's escalated 07-10 ask ("the
chart still has no volume in AH... how can we even enter?").

**Result:** **Init 6 problem (a) is NEGATIVE.** Mean return, entry at 05:00 ET:
PM-last -11.7%, RegOpen -11.4%, RegClose -13.4% (n=4); the earlier 04:10 entry
is -8.2 / -7.9 / -9.7%. **12 of 12 realistic entry×exit combinations lose;** only
the untradeable best-case RegHigh is positive (+1.9% / +6.8%). The "holdable"
tag measures exitability, not profitability — these names peak in the first 1-2
bars then bleed, so by the time holding is confirmed the entry has already
faded, and earlier detection helps only a few points. **No PM-only-gapper long
pulse is proposed; `pm-open-scan` stays cheap log-only.** With both problem (a)
and problem (b, trailing-stop, 07-13) now negative, the AH->PM core strategy
stands unchallenged by the extreme-mover work, and the review surface's AH/PM
volume blind spot is closed.

**Hypothesis / next step:** Init 6's two structured levers are answered (both
negative). The only surviving thread is a possible **intraday momentum-
continuation re-entry** (buy a confirmed intraday breakout, not the overnight
gap) — a different, harder setup; park it until the holdable-gapper sample grows
and the RegHigh dispersion justifies the build. Next run: re-rank the roadmap by
the North Star (Init 6's active-initiative claim is weaker now that its two
tested hypotheses failed — Init 1 earlier-volume-lead or Init 3 scheduling may
outrank it), and take the top Init 5 follow-up (post-push raw-URL 200-check or
GitHub Pages). Keep `pm-gapper-sim.js` accumulating as gappers log.

**Needs from Juan:** nothing. Both Init 6 asks (problem a and b) are now closed
with documented negative results; the Init 5 AH-volume ask is closed by the
chart.py fix.

---

### 2026-07-13 — Init 6: trailing-stop simulation is NEGATIVE — the partial-hold pilot is withdrawn; PM-only-gapper tally hit the rollout-3 trigger (4 holdable)

**Evaluated:** Prior step (2026-07-10: extend the analysis to pull each
LEFT/SAVED trade's full regular-session 5-min SIP path and simulate trailing-
stop widths so the pilot proposal carries an expected-capture number) — **done,
and it came back decisively NEGATIVE.** First refreshed `exit-cost.js`: the three
07-10 exits (YYGH, PMA, ELPW) formed their regular sessions, so the tally is now
**14 round-trips, 6 LEFT / 6 SAVED / 2 flat, avg +29.1% upside missed on LEFT**
(ELPW closed a 6th SAVED at -64.9%).

**Step taken:** Built `scripts/trailing-sim.js` (log-only, no orders). For every
closed round-trip it takes the premarket exit as the hypothetical hold-start,
walks the exit-day **regular-session (09:30-16:00 ET) 5-min SIP bars**, and
simulates a trailing stop at 8/12/15/20% widths (exit at the stop, at the open
if it gaps through, or at the session close), for both the green-at-exit gate
(the pilot's population) and hold-all. Reports the held partial's capture vs the
all-out-premarket baseline. Verified end-to-end.

**Result:** **Every stop width and both gate configs LOSE vs the baseline.**
Green-gate added return -3.2 to -5.1%/trade; hold-all -4.1 to -5.0%/trade. Two
reasons: (1) only **3 of 14** exits were green (IVF, EDHL, DCX) and 2 of those
faded — the big regular-session runners (VTAK +33.6% regHigh, GANX, SUNE, PMA
+41.9%, YYGH) were **RED at premarket exit**, so the "safe" green gate excludes
them, confirming the 07-10 finding with real cost; (2) the +29% "upside left" is
**not mechanically harvestable** — these microcaps whipsaw to their highs (IVF's
+55.5% high at 14:55 ET but an 8% trail stops at -8.0%), so a tight trail is
knocked out early and a wide one gives back too much, drowned by ELPW -66%.
**The trailing-stop partial-hold pilot is withdrawn; the premarket-exit rule is
validated by the data.** Full write-up appended to `INIT6_EXIT_COST.md`.
Separately, today's PM-open scan (commit d674f98) logged **MIMI (+68%) and EHGO
(+75%) as holdable PM-only gappers with no AH footprint**, taking the holdable
PM-only-gapper tally to **4 (SHPH, BJDX, MIMI, EHGO)** — the ~3-4 trigger for
rollout step 3.

**Hypothesis / next step:** Problem (b) is closed (no mechanical edge; re-run
`trailing-sim.js` only if the sample grows a lot). Init 6 pivots to **problem
(a)**: with 4 holdable PM-only gappers logged, the next run should design a
**log-only hypothetical-entry pilot** for PM-only gappers — hypothetical buy at
PM-open-scan detection, hypothetical exit at the premarket-exit window and at
regular open, P&L logged against the current strategy. This is shadow/log-only
(no live orders, no `Day Trading.md` edit), so it needs no Juan gate; it just
quantifies whether the AH-blind-spot names are worth a live-pulse proposal.

**Needs from Juan:** nothing. The problem-(b) partial-hold ask is withdrawn (the
sim shows it loses), so that open ask is now closed.

---

### 2026-07-10 — Init 6: the at-exit signal test came back NEGATIVE — no filter separates runners from dumpers; pilot pivots to a trailing-stop partial hold

**Evaluated:** Prior step (2026-07-09: keep `exit-cost.js` accumulating on live
trades; work the open question of what signal separates IVF-type runners from
DCX-type dumpers) — **worked, and produced a decisive result.** Re-ran
`exit-cost.js`: SUNE (exited 07-09) closed as a 4th **LEFT** case (exit $2.44,
regular high $2.83 = +16% left), so the tally grew to **4 LEFT / 5 SAVED / 2
flat, avg +29.7% upside missed** on the clipped runners — evidence accumulating
on live trades as hypothesized.

**Step taken:** Built `scripts/exit-signal.js` (log-only, no orders) to answer
the open question head-on. For each closed round-trip it pulls the exit-day
premarket 5-min SIP bars up to the exit moment and measures four candidate
“hold?” signals at the exit check — green% (vs entry), momentum (last-bar high vs
~30 min earlier), off-PM-high%, and volume-trend — then groups the means by the
LEFT/SAVED verdict. Wrote the result into `INIT6_EXIT_COST.md` and updated the
pilot proposal + roadmap.

**Result:** **NEGATIVE — none of the at-exit signals separate the two classes**
(LEFT vs SAVED means: green +0.9/-1.5, momo -5.7/-11.3, offHigh -20.7/-19.2,
volTrend -0.9/+16.2). At the 04:30 ET exit the runners look identical to the
dumpers: all fading ~5-12% off a PM high they already made, all near-flat green.
**IVF, the +55% mid-session runner, was itself fading -11.6% into its exit** —
the separating event happens *next session*, not at the exit check. This kills
the “hold if still-green + making higher highs” gate in the prior pilot
proposal. The pilot now pivots to a **trailing-stop partial hold on every green
exit**, where the stop (not a predictive filter) sorts runners from faders. All
scripts verified end-to-end.

**Hypothesis / next step:** The exit-time-filter question is answered (no edge
there). Next run: (1) keep `exit-cost.js` / `exit-signal.js` accumulating (three
07-10 exits — YYGH, PMA, ELPW — refresh into the tally once their regular
session forms); (2) to firm up the trailing-stop asymmetry with real numbers,
extend the analysis to pull each LEFT/SAVED trade’s *full regular-session* 5-min
SIP path and simulate a few trailing-stop widths (e.g. 8/12/15%) so the pilot
proposal carries an expected-capture estimate instead of a hand-wave. PM-open
holdable-PM-only-gapper tally unchanged at 2 (SHPH, BJDX); no new PM-only gapper
today (GMM was AH-detected, ELPW/ELAB uninvestable).

**Needs from Juan:** same open ask, refined — approve the **partial-hold pilot**
(now a trailing-stop hold on green exits, gate dropped) that edits the
`Day Trading.md` no-hold rule. Evidence in `INIT6_EXIT_COST.md`. Until approved,
log-only research only.

---

### 2026-07-09 — Init 6: quantified the premarket-exit rule's cost (problem b); IVF ran +55% mid-regular-session after exit

**Evaluated:** Prior step (2026-07-08: watch the holdable PM-only-gapper tally
climb; confirm the next PM-open scan fired) — **worked.** Today's 11:00 CET pulse
ran (commit 4a12663) and logged 5 more gappers, including a second holdable
PM-only gapper **BJDX (+14.9%, no AH footprint)** — tally now **2 holdable**
(SHPH, BJDX); ELPW was thin. Init 5's inline-chart confirmation is still
**insufficient data** (no Juan reply since 07-08).

**Step taken:** Advanced Init 6 **problem (b)** (let winners run vs premarket
exit), the lever Juan's 07-07 steer points at. Built `scripts/exit-cost.js`
(log-only, no orders): pairs every closed Alpaca round-trip FIFO and compares the
premarket exit to the *same regular session's* high/close (daily bars =
regular-session only). Ran it over all 10 round-trips; wrote up
`INIT6_EXIT_COST.md` with the table, findings, and a proposed pilot.

**Result:** **3 LEFT (rule clipped a runner) / 5 SAVED (dodged a dump) / 2 flat;
avg upside missed on the 3 LEFT trades = +34.3%.** Standout: **IVF**, our biggest
realized winner (+26.6%), traded to **+55.5% above our exit in the regular
session** — its $3.11 high hit **14:55 ET (midday)**, ~10h after our 04:30 ET
premarket exit — a direct counter-example to the core "peaks in PM, dumps at
open" thesis and exactly the BIG win Juan wants. But a blanket change is NOT
justified: every SAVED case was a loser/small-gainer (downside size-capped),
and DCX (-31% to close) / VEEE (-25%) show holding everything would bleed the
faders. The edge is *selectively* holding movers still green + making higher
highs at the exit check, not holding all. Verified the script runs end-to-end.

**Hypothesis / next step:** The exit-rule cost is now evidenced. Next run: (1)
keep `exit-cost.js` accumulating (re-run to grow the LEFT/SAVED tally on live
trades); (2) work the open question — what signal at the premarket-exit check
separates IVF-type regular-session runners from DCX-type open-dumpers (still-
green + higher-highs into 09:00 ET, sustained volume, Tier-A catalyst)? A few
more logged cases sharpen the partial-hold pilot proposal. PM-open tally keeps
collecting toward 3-4 holdable PM-only gappers.

**Needs from Juan:** **new ask** — approve a **partial-hold pilot** that edits
the `Day Trading.md` "never hold through the day" rule (hold a partial into the
regular session on a position still green + rising at the premarket-exit check,
trailing stop, exit the rest in premarket; 1 position at a time for
attribution). Evidence in `INIT6_EXIT_COST.md`. Until approved, log-only
research only — nothing applied to live trading.

---

### 2026-07-08 — Init 5: inline charts shipped to the email; Init 6 first scheduled PM-open run logged 4 gappers

**Evaluated:** Prior step (2026-07-07 Init 6: confirm the first scheduled PM-open
run fired and logged rows) — **worked.** The 11:00 CET pulse ran today (commit
a59fccc) and appended **4 rows** to `log/pm-open-scan.csv`, all classified
holdable: IOTR (+62.7%), DCX (+36.3%), BATL (+18.3%) — all AH-detected — and
**SHPH (+13.8%), a genuine PM-only gapper with no AH footprint** (DOGE-mining
acquisition catalyst), held $3.65-4.13 within 20% of its $4.34 PM high across 6+
bars. SHPH is the blind-spot target class. The pulse runs end-to-end in the cron
environment.

**Step taken:** Two moves this run. (1) **Init 6 (active):** recorded the first
scheduled run's result and started the running real-time holdable PM-only-gapper
tally at **1 (SHPH)** — the trigger to propose a hypothetical-entry pilot
(rollout step 3) is ~3-4, so keep collecting. (2) **Init 5 (parallel, ready,
Juan-requested):** switched `prompts/daily-email.md` from GitHub **blob links**
(which 404'd for Juan on 06-30, private-repo era) to **inline
`<img src="https://raw.githubusercontent.com/...">` images**, now that the repo
is public. Added a **commit + push charts BEFORE sending the email** step so the
raw URL is live when Gmail's image proxy fetches it (avoids Gmail caching a 404).

**Result:** Init 5's email-charts delivery is rebuilt on the path Juan asked for
(image in the body, not a link). Verified: a `raw.githubusercontent.com` chart
URL returns **HTTP 200** on the public repo, and `chart.py SHPH --range 2d`
still renders (45 KB PNG). First live use is the next daily-email run. Init 6
continues accumulating gappers with no code change needed.

**Hypothesis / next step:** (Init 5) confirm the next daily email actually
displays the inline chart in Juan's Gmail; if yes, the email-charts half is DONE
and focus shifts to GitHub Pages HTML reports + data-source quality. (Init 6)
watch the holdable PM-only-gapper tally climb toward 3-4, then draft the
hypothetical-entry pilot proposal for Juan.

**Needs from Juan:** nothing blocking. The premarket-exit / let-winners-run
question (Juan's 07-07 "catch BIG wins, not clean 6%" steer) remains a
live-trading proposal to raise once the PM-open data or a hold-rule backtest
justifies it; not proposed this run (still gathering evidence).

---

### 2026-07-07 — Init 6: log-only PM-open scan pulse built + scheduled (rollout step 2 done)

**Evaluated:** Prior step (2026-07-06 Init 6: gate met, so next run *draft the
log-only PM-open scan pulse*) — **worked.** The gate (live-fillability via Alpaca
SIP) held, and this run executed the drafting step: the pulse is built, the
discovery + classification pipeline runs end-to-end on a live gapper, and it is
scheduled.

**Step taken:** Built `prompts/pm-open-scan.md` — a log-only pulse that (1)
discovers whole-market PM gappers via `scan.py` (which auto-detects the premarket
session and screens `premarket_change`/`premarket_volume`), (2) classifies each
gapper holdable / uninvestable / thin from real Alpaca-SIP 5-min bars
(`broker.js bars --feed sip`, the source validated on 07-06), using the census
heuristic (held within ~20% of PM high across >=2 bars on real volume =
holdable), and (3) appends to a new tracker `log/pm-open-scan.csv`. **No orders,
no `OPEN_POSITIONS.md` touch, no change to any existing trading-scan timing.**
Added cron `trading-pm-open-scan-1100` (11:00 CET / 05:00 ET, Mon-Fri).

**Result:** Rollout step 2 (instrument a log-only PM-open scan) is **done**.
Verified the full pipeline live at 09:01 ET: `scan.py --all` returned 11
premarket hits; classified today's top gapper **SUGP** via SIP bars — it ramped
at 07:00 ET on **3.4-5.8M shares / 14-18K trades per 5-min bar** and held
$1.00-1.10 across 6+ bars = **holdable**, seeded as the first tracker row (marked
pipeline-verification). Both halves (discovery, SIP classification) run in the
cron environment. First scheduled run: tomorrow 11:00 CET.

**Hypothesis / next step:** Let the pulse accumulate real-time gappers for a few
weeks. Next run(s): confirm the first scheduled run fired and logged rows, then
watch the holdable-vs-uninvestable tally build. **Trigger for rollout step 3
(propose a hypothetical-entry pilot to Juan):** ~3-4 real-time *holdable* PM-only
gappers logged, showing they recur often enough to be worth piloting. Until then,
just collect.

**Needs from Juan:** nothing blocking. **Heads-up / veto window:** the new
log-only PM-open scan pulse was applied directly (permitted for log-only pulses)
and first runs tomorrow 11:00 CET. It places no orders and retimes no existing
trading scan. Say the word to remove it before then.

---

### 2026-07-06 — Init 6: PM-open-scan gate MET (live-fillability confirmed via Alpaca SIP)

**Evaluated:** Prior step (2026-07-03 Init 6: advance the PM-open-scan case via
either (a) mine more holdable gappers or (b) a live-fillability check) —
**worked, and the fillability check was decisive.** Chose (b) because it directly
kills the one caveat holding the proposal back (Yahoo PM bars report `vol=0`, so
"holdable" rested on price persistence alone).

**Step taken:** Ran the live-fillability check on the two holdable PM-only
gappers (CIIT 2026-06-10, GLXG 2026-06-11) plus TDIC (uninvestable control)
using Alpaca SIP historical 5-min bars (`node scripts/broker.js bars <SYM> --tf
5Min --feed sip`). Recorded results as a "Fillability check (2026-07-06)" section
in `INIT6_EXTREME_MOVERS.md` and updated Init 6 status in the roadmap.

**Result:** **Gate met.** Both holdable gappers had deep, real premarket
liquidity across the entire 04:00-05:00 ET ramp — CIIT: 0.4-3.2M sh and
3.8K-55K trades per 5-min bar ($1.49->$7.68); GLXG: 2-3.6M sh and 18K-58K trades
per bar ($1.94->$5.39). Not single ticks; a multi-hour exit window genuinely
existed. TDIC (uninvestable) *also* had deep liquidity (632K sh / 18.7K trades
first bar) but peaked $16.23 in the opening bar and decayed straight down —
confirming uninvestability is a **price-path** property, not a liquidity one.
Yahoo's `vol=0` was a data gap. Bonus finding: **Alpaca SIP** (`broker.js bars
--feed sip`) is a validated premarket data source where Yahoo is blind (free-tier
SIP blocks only the most recent ~15 min, fine for a log-only pulse).

**Hypothesis / next step:** The gate to instrument rollout step 2 is now met, so
next run should **draft the log-only PM-open scan pulse**: a prompt (~04:00-05:00
ET / 10:00-11:00 CET) that lists overnight gappers with no AH footprint, pulls
their Alpaca-SIP premarket price-path + liquidity, tags each holdable vs
uninvestable, and logs to a tracker CSV — **no orders, no change to existing
trading-scan timing.** Expectation: a few weeks of shadow logging shows whether
real-time holdable gappers recur often enough to justify piloting hypothetical
entries.

**Needs from Juan:** nothing blocking. Heads-up (repeat): the next step adds a
*new log-only PM-open scan pulse* (instrumentation only, no orders, no retiming
of any existing trading scan). Log-only pulses can be added directly, but it will
be flagged here for veto before applying.

---

### 2026-07-03 — Init 6: hold rule shelved (no tradeable case); PM-open scan is the lever

**Evaluated:** Prior step (2026-07-02 Init 6: expand census to ~15, firm up
patterns, then next run shift to *decision* and lead with the Tier-A hold-rule
proposal) — **worked, and the decision test flipped the recommendation.** The
census (14 cases) and patterns 3/6 held. Executing the "draft the proposal" step
by first cross-checking it against pattern 4 (real-AH-volume gate) showed the
hold rule should NOT be led with.

**Step taken:** Cross-tabbed pattern 3 (catalyst tier) against pattern 4 (real
AH volume) across all 6 AH-detectable extreme runners to test whether the
Tier-A-catalyst hold rule has any *tradeable* supporting case, before proposing
it to Juan. Recorded the table + verdict as a "Decision analysis (2026-07-03)"
section in `INIT6_EXTREME_MOVERS.md` and updated Init 6 status in the roadmap.

**Result:** **The Tier-A hold rule has zero tradeable supporting cases, so it is
shelved (not proposed).** The only AH *continuer* (ILLR +760%) had zero real AH
volume (untradeable, ask $0.00 / VRatio 0.1-0.4x); every *tradeable* AH runner
(MSW holdable-traded, CHAI, HKIT) faded, meaning the current premarket-exit
discipline was correct on each. Pattern 3 is a real statistical discriminator but
pattern 4 neutralizes its only actionable instance — no case exists where a
Tier-A AH runner was tradeable *and* holding past the PM exit would have earned
more. This redirects Init 6: the reachable +200-600% money is in pattern 2's
**holdable PM-only gappers** (CIIT +140%, GLXG +343%), not the AH hold rule. The
**log-only PM-open scan** (rollout step 2) is now the proposal to advance, gated
on 1-2 more holdable gappers or a live-fillability check.

**Hypothesis / next step:** Next run should advance the PM-open-scan case, not
the hold rule. Two options: (a) mine remaining older-log +200% cases (CCTG, PHGE
+265%) and classify any new PM-only gappers' premarket paths to push the holdable
tally past ~3-4 (the trigger to draft the pulse); or (b) if the tally is judged
sufficient at 2, draft the log-only PM-open scan pulse (~04:00-05:00 ET /
10:00-11:00 CET, instrumentation only, no orders) and flag it for Juan before
applying. Expectation: one more holdable gapper makes the case decisive, so lean
(a) first, then (b).

**Needs from Juan:** nothing yet. Heads-up: the likely next proposal is a *new
log-only PM-open scan pulse* (no orders, no change to existing trading-scan
timing). Log-only pulses can be added directly, but it will be flagged here for
veto before applying since it touches scan cadence.

---

### 2026-07-02 — Init 6: census expanded to 14; pattern 3 strengthened, pattern 6 added

**Evaluated:** Prior step (2026-06-30 Init 6: classify PM-only gappers, then
mine older logs toward ~15-20 cases and classify new gappers) — **worked.** The
PM-gapper classification held; this run executed the second half (mine older
logs). No new PM-only gappers appeared in the mined set, so the holdable-gapper
tally is unchanged (still 2 holdable / 3 uninvestable) — the PM-open-scan
proposal stays pending more gapper evidence, not triggered yet.

**Step taken:** Mined the pre-Jun-9 daily logs for the +200% candidates flagged
in the census open-gaps (EVOL, CPOP, CHAI, HKIT, EEIQ, ATLN) and characterized
each from its log entry (peak %, AH vs PM vs regular lead, catalyst, outcome).
Added 5 to `INIT6_EXTREME_MOVERS.md` (census now **14 cases**); dropped EEIQ (log
shows only +64%, below the +200% threshold — the "+209%" note was wrong).

**Result:** Two pattern updates, both decision-relevant:
- **Pattern 3 (catalyst tier) strengthened to 5 faders / 1 continuer, 100%
  consistent.** The two new AH runners CHAI (+416%, no catalyst) and HKIT
  (+293%, negative news) both faded AH->PM, joining MSW/TII/EDHL. Every faded
  extreme AH runner lacked a fresh Tier-A catalyst; the only continuer (ILLR
  +760%) had one. This is now a strong enough signal to consider drafting a
  conditional hold/skip rule (Tier-A AH runner = let run; no/dilution catalyst =
  take AH profit or skip) — but that touches live trading, so it is a *proposal
  to Juan*, not applied.
- **New pattern 6: regular-session spikes are a distinct untradeable negative
  class.** EVOL (+300%), CPOP (+369%), ATLN (+220%) all moved in the regular
  session with AH <10% follow-through — the AH->PM scanner sees nothing and
  correctly shouldn't. Confirms "catch 600%" must not chase these; the reachable
  targets are AH runners (pattern 3) and holdable PM-only gappers (pattern 2).

**Hypothesis / next step:** The census is at the ~15-case analytic threshold and
two patterns are now firm. Next run should shift from data-gathering to
*decision*: draft the two candidate proposals for Juan and pick the higher-value
one to formalize — (i) a conditional **Tier-A-catalyst hold rule** for extreme AH
runners (pattern 3, touches live trading -> propose only), or (ii) a **log-only
PM-open scan** for holdable gappers (pattern 2; needs 1-2 more holdable gappers
to justify). Expectation: pattern 3 has more cases behind it and a clearer edge,
so lead with (i) as a written proposal, framed as instrument-first (log the
catalyst-tier tag on extreme AH runners before acting).

**Needs from Juan:** nothing yet. Heads-up: a proposal to add catalyst-tier
hold/skip logic for extreme AH runners (a live-trading rule) is likely next run.

---

### 2026-06-30 — Init 6: PM-only gappers classified; pattern 2 flipped (real cost)

**Evaluated:** Prior step (2026-06-29 Init 6: build the extreme-movers census,
seed 9 cases, extract patterns) — **worked.** `INIT6_EXTREME_MOVERS.md` exists
with the 9-case table and 5 patterns; it gave a concrete, prioritised next
question (classify the unlabeled PM-only gappers), which this run answered.

**Step taken:** Took the highest-decision-value next step from the census: pull
the premarket price path for the three unclassified PM-only gappers (CIIT Jun 10,
GLXG Jun 11, TDIC Jun 16) and label each holdable vs uninvestable. Built
`scripts/init6-pmbars.py` (Yahoo 15m + `range=1mo` + a `Mozilla/5.0` UA reaches
~1 month of historical premarket bars; the `chart.py --range 2d` 5m path only
goes ~5 days back, so it couldn't reach mid-June). Verified it runs.

**Result:** **Pattern 2 flipped — PM-only gappers are NOT mostly uninvestable.**
CIIT (+140%) held +126-414% across the *entire* 04:00-09:15 premarket (20+
consecutive 15m bars) and opened +203% on 53M shares; GLXG (+343%) held
+180-380% all premarket and opened +225% on 48M shares — both clearly
**holdable** (a multi-hour exit window existed). Only TDIC was **uninvestable**
(spiked 04:00, decayed to negative within 90 min). PM-only tally is now 2
holdable (CIIT, GLXG) / 3 uninvestable (MBRX, CUPR, TDIC), and the two holdable
ones are exactly the +140%/+343% movers Juan wants. So the AH-blind-spot has
**real cost**: a PM-open scan could have caught two large holdable runners in one
week. Census + roadmap updated. Caveat: Yahoo 15m PM bars report vol=0, so true
premarket fillability still needs live NBBO (the Init 2 caveat).

**Hypothesis / next step:** The holdable-PM-gapper evidence (2/5 and growing)
raises rollout step 2. Next run: mine Mar-May logs for more +200% cases toward
the ~15-20 threshold AND classify any new PM-only gappers' premarket paths; if
the holdable count keeps climbing, draft a proposal to Juan for a **log-only
PM-open scan** (~04:00-05:00 ET / 10:00-11:00 CET, instrumentation only, no
orders) to start capturing these structurally-missed runners. A new log-only
pulse is allowed to apply directly, but flag it for Juan first since it touches
the scan cadence.

**Needs from Juan:** nothing yet (research uses existing logs + Yahoo). Heads-up:
a log-only PM-open scan proposal is likely within a few runs.

---

### 2026-06-29 — Init 6: extreme-movers census seeded; pattern extraction started

**Evaluated:** Prior step (2026-06-26 Init 5: wire chart.py PNGs + repo links
into the daily-email pulse, path b; confirm links resolve) — **mechanism
verified, works.** The chart PNGs (ILLR, IVF) are committed and pushed in
`origin/main` (b79a276); the daily-email prompt has the "Generate Charts" step +
"Charts (5m + volume)" link section. The blob/raw URLs 404 to an unauthenticated
curl, but so does the repo root page — the repo is **private**, so the 404 is
expected gating, not a broken link (Juan is authenticated). Init 5's email-charts
rollout step is mechanically done; full live confirmation waits on the first
trading day that runs the wired pulse end-to-end (no log dir since Fri 06-26).

**Step taken:** With the pilot slot free and Juan's strong 2026-06-26
endorsement of the +760% target, switched the active initiative to **Init 6**
(highest expected $/time lever). Took the cheapest research step (rollout 1/1b):
built `INIT6_EXTREME_MOVERS.md`, a structured census consolidating the extreme
movers already tracked in prose across daily logs into one reviewable table with
the pattern-extraction columns Juan asked for (catalyst tier, float, AH-vs-PM
timing, volume, price path, detectability, investability, outcome). Mined logs
for Jun 9-26 cases.

**Result:** 9 cases seeded (MSW, CIIT, GLXG, EDHL, TDIC, MBRX, CUPR, ILLR, TII)
with 5 extracted patterns. Strongest signals: (3) **catalyst tier separates AH
continuers from faders** — ILLR (Tier A, fresh SpaceX news) ran AH->PM to +760%
while MSW (Grade C, dilutive notes) faded AH->PM; (4) **headline AH % on zero AH
volume is an untradeable trap** — ILLR and TII both printed huge AH % on
VRatio <0.5x / ask $0.00, so no real fill; (2) the two PM-only gappers
classified so far (MBRX, CUPR) were both uninvestable, supporting the low-cost
blind-spot hypothesis. `chart.py` verified available for the next classification
step.

**Hypothesis / next step:** Expand the census toward ~15-20 cases (the analytic
threshold to test the patterns): mine Mar-May logs for more +200% movers (EVOL,
CCTG, CPOP, CHAI, PHGE, HKIT, EEIQ, ATLN already spotted) and classify
investability (holdable vs uninvestable) for the unlabeled PM-only gappers
(CIIT, GLXG, TDIC) via their PM 5-min bars. Then test whether pattern 3
(catalyst-tier discriminator) is strong enough to justify a conditional
hold/skip rule for Tier-A AH runners (proposal to Juan, not applied).

**Needs from Juan:** nothing (research uses existing logs + chart.py).

---

### 2026-06-26 — Init 5: charts wired into the daily email (path b)

**Evaluated:** Prior step (2026-06-25 Init 5: default to path (b) and wire
chart.py PNGs + repo links into the daily-email pulse if Juan doesn't object) —
**proceeded; Juan didn't object.** No new feedback touched chart delivery (the
only feedback since, 2026-06-24, was the scheduler approval), so the (b)
recommendation stands and was applied.

**Step taken:** (1) Proved the chart pipeline end-to-end on today's *real*
reported tickers, not just old samples: `chart.py ILLR --range 2d` and
`chart.py IVF --range 2d` rendered into `log/2026-06-26/` (49 KB / 44 KB PNGs).
Visually confirmed the ILLR PNG shows the full AH->PM pattern (regular climb ->
after-hours build to ~$4.20 amber -> premarket spike to ~$7 then fade blue, with
the early volume surge). (2) Wired path (b) into `prompts/daily-email.md`: a new
"Generate Charts" step runs `chart.py` for the winner + each open Alpaca position
into `log/YYYY-MM-DD/`, and a "Charts (5m + volume)" email section links each PNG
via its GitHub blob URL. Log-only change; no trading logic touched.

**Result:** The daily email now has an auditable chart surface with zero new
infra (no host, no attachment API). `convert` (ImageMagick) is present, so the
pipeline runs in the cron environment. Charts ride the existing
`log/YYYY-MM-DD/TICKER-HHMM.png` convention and are committed by the cycle's git
step, so the email links resolve for Juan (authenticated to the private repo).

**Hypothesis / next step:** Tomorrow's daily email is the first live use. Next
run: confirm the email actually rendered a Charts section and that the GitHub
blob link displays the committed PNG when opened (resolves only after the
cycle's push). If links work, Init 5's email-charts rollout step is done and the
focus shifts to data-source quality (the second half of Init 5) or hands the
pilot slot to Init 6 (the +200%-mover census, now surfaceable through these
charts).

**Needs from Juan:** nothing blocking. Optional: if he'd rather not click into
the repo, he can ask for inline hosted images (path a) instead.

---

### 2026-06-25 — Init 2 promoted to live paper; Init 5 attachment path resolved

**Evaluated:** Prior step (2026-06-24 Init 2: decide shadow-pulse vs wire-into-pulses
to capture fills at entry/exit) — **overtaken by events, resolved.** The
scanner-improvement loop already wired `broker.js` directly into the trading
pulses (commits `0c43af9` "switch to Alpaca paper execution; clean break from
fictional ledger" and `a508bfe`): `post-market-scan.md` now submits real
ext-hours Alpaca paper buys, `position-evaluation.md` submits real sells, and
`morning-evaluation.md` / `OPEN_POSITIONS.md` treat Alpaca as the source of
truth. Real fills are captured natively at entry/exit — exactly what the
shadow-fills comparison (rollout steps 3-4) was meant to achieve, so that
approach is moot. **Init 2 is effectively promoted to the live paper cycle;
only step 5 (real money, tiny size) remains, gated on a proven edge + Juan.**
Account `PA37U2Y192A7` verified flat at $99,998.41 (no open positions; two old
VTAK validation round-trips paid ~$1.59 total spread).

**Step taken:** With the single pilot slot freed, switched the active initiative
to **Init 5** (next by priority; Juan needs a review surface to steer the now-
live paper P&L). Resolved Init 5's blocking question — whether InboxKit supports
attachments — by reading the authoritative OpenAPI spec
(`https://inboxkit.cc/api/openapi.json`), then re-verified the chart renderer on
today's winner AZI.

**Result:**
- **InboxKit `POST /api/messages` supports only `to`, `subject`, `text`, `html`
  — NO attachment/multipart field.** The "attach PNG to the daily email" plan
  is dead. (Spec is the source of truth; no guessing against the live sender.)
- `chart.py AZI --range 2d` renders the full AH->PM pattern (flat ~$1.25 ->
  after-hours spike to ~$2.34 -> premarket fade to ~$1.79, volume panel intact),
  50 KB PNG. The renderer is healthy on current data; only delivery is blocked.
- Two delivery paths survive: (a) inline `<img src="https://...">` with a hosted
  PNG (Gmail proxies remote https images; base64 data URIs are stripped, so no);
  (b) commit charts to the daily log dir (existing `TICKER-HHMM.png` convention)
  and link from the email — Juan is authenticated to the repo, zero hosting.
  Leaning (b).

**Hypothesis / next step:** If Juan confirms (b) (or doesn't object), wire the
daily-email pulse to generate `chart.py` PNGs for the reported winner + any open
positions into `log/YYYY-MM-DD/` and add repo links in the email body — a
log-only change to `daily-email.md`, no trading-logic impact. Verify the links
resolve before relying on them.

**Needs from Juan:** confirm chart delivery preference — (b) committed charts +
email link (recommended, no hosting) vs (a) inline images needing a public host.
Not blocking; will default to (b) next run if no objection.

---

### 2026-06-24 — Init 2: second ext-hours round-trip + shadow-fills ledger

**Evaluated:** Prior step (first VTAK ext-hours round-trip, buy@ask/sell@bid) —
**worked and now replicated.** A second VTAK round-trip this morning filled the
same way: BUY 86 @ **$1.35 (ask)**, SELL 86 @ **$1.34 (bid)**, flat. The fill
model holds on a second occasion.

**Step taken:** It's 09:00 ET (US premarket), account flat. Ran a fresh VTAK
ext-hours shadow round-trip (86 sh, mirroring today's real paper size), checked
EPOW (today's other paper name) for ext-hours fill viability, and started a
persistent ledger `log/shadow-fills.csv` to accumulate assumed-vs-real fill
comparisons. Then applied the fill model to today's two closed paper trades.

**Result:**
- VTAK BUY @ $1.35 = ask, SELL @ $1.34 = bid. Spread held at **1c** even at the
  higher price, so relative round-trip cost shrank to **0.74%** (vs 0.88% at
  $1.14 yesterday). Cheaper the name, bigger the relative spread bite.
- EPOW ($0.52, sub-$1) had **no fresh ext-hours quote** (ask $0.00, stale
  06-23 20:00 ET close) — would **not** have filled in extended hours. Coverage
  gap is worst on the cheapest names (matches yesterday's EHGO caveat).
- Spread cost on today's real paper trades (1c/leg): VTAK (+70.7%) loses only
  ~1-2% of its gain — survives easily. EPOW (-10.1%) would have its loss widened
  ~29% and might not have filled at all. **Spread is a rounding error on big
  winners but meaningfully erodes small losers; sub-$1 names carry non-fill
  risk.**

**Hypothesis / next step:** Free-tier Alpaca has no historical NBBO, so past
fills can't be reconstructed — a real assumed-vs-real comparison needs fills
captured *at the moment* of each paper entry/exit. Next run: decide between (a)
a log-only shadow pulse that mirrors open paper positions to Alpaca at the
entry/exit windows, or (b) wiring a shadow order into the scan/eval pulses.
Option (b) changes pulse behavior and must be proposed to Juan; option (a) is a
new log-only pulse and can be built directly. Lean toward (a). Keep appending
to `log/shadow-fills.csv`.

**Needs from Juan:** nothing blocking. Heads-up for the next step: if we mirror
live paper entries/exits automatically, it will place real (paper) Alpaca orders
during scan/eval windows — still paper, no real money.

---

### 2026-06-23 — Init 2: first live extended-hours shadow fill

**Evaluated:** Prior step (build broker.js + chart.py) — **worked.** broker.js
runs against the live paper account; chart.py renders. This run advanced the
Init 2 next step (the one pilot slot).

**Step taken:** Added `--ext` (extended_hours) limit-order support to
`scripts/broker.js`, then ran a live premarket shadow round-trip on VTAK
(mirroring today's closed 67-share paper trade). It's 09:00 ET, US premarket.

**Result:** Real fills captured.
- Ext-hours marketable limit BUY 67 VTAK filled at **$1.14 (the ask)**.
- Ext-hours limit SELL 67 VTAK filled at **$1.13 (the bid)**. Position flat, no
  leftover exposure.
- **Core Init 2 question answered: Alpaca paper DOES fill our micro-float
  sub-$10 names in extended hours, at the NBBO bid/ask.** Realistic fill model
  = buy@ask / sell@bid; spread is the real slippage (~1c, ~0.9% round trip on
  VTAK at $1.14). This means our assumed paper "wins" are not pure fiction, but
  each round trip pays the spread.
- Coverage caveat: VTAK and SKYQ had fresh 09:00 ET premarket IEX quotes; EHGO's
  quote was stale (prior close) — some names may not fill in extended hours.

**Hypothesis / next step:** Over the next sessions with open paper positions,
mirror real entries/exits as Alpaca ext-hours orders and tabulate assumed price
vs ask(entry)/bid(exit) to measure how much paper P&L survives realistic fills.
If the spread routinely eats a big share of the edge on the cheapest names, that
reshapes entry sizing/price selection.

**Needs from Juan:** nothing blocking. (Heads-up: the Init 2 pilot places real
paper orders on Alpaca during market/extended hours — still paper, no real
money. Today's test round-tripped one position and left the account flat.)

---

### 2026-06-23 — Init 2 broker + Init 5 chart prototype built

**Evaluated:** Re-rank (same day) — acted on it by working the top two priorities.

**Step taken:** Two next steps, both log-only / paper (no live-trading or pulse
rule changes, so no Juan sign-off needed):
- **Init 2:** built `scripts/broker.js` (Alpaca paper CLI, no deps) and tested
  the full path against the live paper account — account/positions, order
  submit -> new -> cancel, live quote, asset tradable lookup.
- **Init 5:** built `scripts/chart.py` (dependency-free 5m+volume candlestick,
  Yahoo data, AH/PM shading, SVG -> PNG) and verified on ORIS and VTAK.

**Result:**
- Micro-float names are tradable on Alpaca (VTAK, ORIS `tradable=true`) — the
  universe is not blocked. De-risks Init 2.
- Alpaca free IEX bars are sparse; Yahoo stays the history/5m source, Alpaca is
  for live quotes + real fills. Settled the data-source question for Init 5.
- ORIS chart visibly shows the AH->PM pattern (build in after-hours, premarket
  spike to ~$5.85 then fade) — a usable review surface.

**Hypothesis / next step:**
- Init 2 pilot: shadow-mirror paper entries/exits as Alpaca paper orders during
  market hours; compare assumed vs real fills (this is the one pilot slot).
- Init 5: confirm InboxKit attachment API, then attach charts to the daily
  email so Juan reviews them in-channel.

**Needs from Juan:** nothing blocking. (Heads-up: the Init 2 pilot will place
real paper orders on Alpaca during market hours — still paper, no real money.)

---

### 2026-06-23 — Roadmap re-ranked by money-fast + enablers

**Evaluated:** Loop bootstrap (same day) — done; this is the first prioritisation pass.

**Step taken:** Re-ranked the roadmap under the North Star, weighting Juan's
steer that working Alpaca paper (path to real money) and a better data/review
surface (graphs + sources) are high-value enablers. Added a "Priority order"
section to `STRATEGY_ROADMAP.md` and broadened Init 5 from "charts in email" to
"better data + review surface (charts, sources)."

**Result:** Order is 2 (Alpaca, foundation) -> 5 (data + graphs to review/steer)
-> 6 (extreme runners, biggest raw lever) -> 1 (earlier entries) -> 3 (adaptive
scheduling, ongoing). Init 4 done. Juan put 5 before 6 (2026-06-23) so the
census and big-mover work land as something he can review. Key insight driving
#1: Alpaca shadow fills will reveal whether our micro-float paper "wins" are real.

**Hypothesis / next step:** Next run starts Init 2 — build `scripts/broker.js`
against the live paper account (submit/track orders, read fills), then shadow
the existing paper entries/exits to compare assumed vs real fills.

**Needs from Juan:** nothing blocking.

---

### 2026-06-23 — Loop bootstrapped

**Evaluated:** n/a — first entry.

**Step taken:** Created the `strategy-advance` daily pulse (`prompts/strategy-advance.md`)
and this log. The loop walks `STRATEGY_ROADMAP.md` one initiative at a time
(Research -> Instrument -> Pilot -> Promote), one small step per day.

**Result:** A daily mechanism now exists to move strategy initiatives, mirroring
the scanner-improvement loop. Current roadmap state: Init 2 (Alpaca) unblocked
and ready to build; Init 6 (catch extreme runners) at research; Init 1, 3, 5 at
research/backlog.

**Hypothesis / next step:** First real run should pick the active initiative.
Likely order: (1) Init 2 — build `scripts/broker.js` against the live paper
account; then (2) Init 6 — the +200%-mover census. Init 3 (adaptive scheduling)
is the loop's own domain and can retime pulses as evidence accrues.

**Needs from Juan:** confirm the pulse cadence/time (proposed: daily 15:00
Berlin, after process-review).
