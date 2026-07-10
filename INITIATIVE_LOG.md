# Initiative Log

Daily progress on the strategy roadmap (`STRATEGY_ROADMAP.md`), one initiative
at a time. Written by the `strategy-advance` pulse. Newest first.

This is the strategy-level analog of `SCANNER_CHANGELOG.md` (which logs surgical
scanner tweaks). Each entry evaluates the previous step, records the step taken
today, and sets the hypothesis/next step for the following run.

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
