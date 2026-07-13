# Init 6 (b) — Cost of the premarket-exit rule ("let winners run")

Research artifact for Initiative 6, rollout problem **(b)**: the
`Day Trading.md` rule *"Never hold positions through the day. Sell every position
in premarket before open"* caps gains. Juan's 2026-07-07 steer ("catch BIG wins,
not a clean 6%") pushes directly on this. This measures how much the rule costs
vs how much it saves, using real Alpaca paper fills.

**Method:** `scripts/exit-cost.js` pairs every closed round-trip (FIFO) and
compares the **premarket exit price** to the **same regular session** that
followed it. Alpaca daily bars are regular-session-only, so the daily High/Close
bound "what if we had held through the open." `vsExit%H` = regular high vs our
exit (upside we left), `vsExit%C` = regular close vs our exit, `nextH%` = next
session high vs exit (overnight-hold proxy). Verdict: **LEFT** = regular high
>=+8% above exit (clipped a runner); **SAVED** = regular close <=-5% below exit
(dodged a dump); **flat** = neither. Re-run any time to refresh as trades
accumulate.

## Result (2026-07-10 refresh, 11 round-trips since 2026-06-23)

SUNE (exited 2026-07-09) closed as a 4th **LEFT** case (exit $2.44, regular high
$2.83 = +16.0%). Tally now **4 LEFT / 5 SAVED / 2 flat; avg upside missed on the
LEFT trades = +29.7%.** (Three more round-trips closed 2026-07-10 — YYGH, PMA,
ELPW — but their regular session has not formed yet, so they are excluded until
the next refresh.)

## Result (2026-07-09, 10 round-trips since 2026-06-23)

| sym  | exit day   | P&L% | regHigh vs exit | regClose vs exit | nextH% | verdict |
|------|------------|------|-----------------|------------------|--------|---------|
| VTAK | 2026-06-23 | -0.9 | +2.7            | -18.6            | +58.4  | SAVED   |
| VTAK | 2026-06-24 | -0.7 | +33.6           | -11.2            | -6.7   | LEFT    |
| IVF  | 2026-06-26 | +26.6| **+55.5**       | +22.5            | +20.5  | LEFT    |
| CTNT | 2026-06-30 | -7.3 | -7.9            | -12.6            | -1.6   | SAVED   |
| GANX | 2026-06-30 | -17.6| +13.7           | +3.0             | +9.1   | LEFT    |
| ALZN | 2026-07-01 | -1.5 | +2.3            | -13.2            | -7.8   | SAVED   |
| EDHL | 2026-07-07 | +6.0 | +7.1            | -3.1             | -3.9   | flat    |
| VEEE | 2026-07-08 | -1.8 | -2.8            | -24.8            | -      | SAVED   |
| DCX  | 2026-07-08 | +3.7 | -11.5           | -30.9            | -      | SAVED   |
| SEER | 2026-07-08 | -2.7 | +0.9            | -0.9             | -      | flat    |

**Tally:** 3 LEFT (clipped a runner) · 5 SAVED (dodged a dump) · 2 flat.
**Avg upside missed on LEFT trades: +34.3%** (regular-session high vs exit).

## Findings

1. **The rule dodges dumps more often than it clips runners (5 vs 3), so on
   average it protects capital** — but every SAVED case was a *loser or a
   small-gainer* (VTAK, CTNT, ALZN, VEEE, DCX), where in the learning phase the
   downside is capped at ~$100/position anyway.
2. **When it clips, it clips big.** The single biggest winner, **IVF (+26.6%
   realized), traded to +55.5% above our exit in the *regular* session** — its
   $3.11 high hit at **14:55 ET (midday)**, ~10h after our 04:30 ET premarket
   exit at $2.00. This is a direct counter-example to the core "peaks in PM,
   dumps at open" thesis: IVF's real peak was mid-regular-session the next day,
   exactly the window `Day Trading.md` tells us to avoid.
3. **Asymmetry favors letting the strongest run.** Missing a +34% avg runner
   hurts compounding more than dodging a -10-30% dump on a size-capped loser
   helps. This is the mechanism behind Juan's "catch BIG wins" critique.
4. **A blanket rule change is NOT justified** — 2 of 3 dumps (DCX -31%, VEEE
   -25% to close) show holding all positions through the open would bleed the
   faders badly. The edge is in *selectively* holding the movers that are still
   green and rising at the premarket-exit check, not holding everything.

## Proposed pilot for Juan (touches `Day Trading.md` — NOT applied)

Instrument-first, then a small conditional-hold pilot:

- **Instrument (log-only, can apply now):** keep running `exit-cost.js` (and/or
  log the regular-session high/close for each exited position in the daily
  eval) so the LEFT/SAVED tally accumulates on live trades. Zero risk.
- **Pilot (needs Juan — changes the "never hold through the day" rule):** on any
  position that is **green at the premarket-exit check**, hold a **partial**
  (e.g. half) into the regular session under a **trailing stop** (the stop, not a
  predictive filter, sorts runners from faders — see the 2026-07-10 negative
  result above), and exit the rest in premarket as usual. Compare the
  held-partial P&L to the baseline all-out-premarket exit. Start with 1 position
  at a time for attribution (pilot-serialized). *Note the earlier "still making
  higher highs" gate was dropped: the data shows runners and dumpers are
  indistinguishable at the exit check, so the trailing stop must do the work.*

**Open question before piloting:** what signal at the premarket-exit check best
separates the IVF-type regular-session runners from the DCX-type open-dumpers?
Candidates: still-green + higher-highs into 09:00 ET, sustained real volume,
fresh Tier-A catalyst.

### 2026-07-10 — the at-exit signal test came back NEGATIVE

Built `scripts/exit-signal.js` (log-only): for each closed round-trip it pulls
the exit-day premarket 5-min SIP bars up to the exit moment and measures four
candidate signals at the exit check — `green%` (vs entry), `momo%` (last-bar
high vs ~30 min earlier), `offHigh%` (exit vs PM high so far), `volTrend%`
(trades/bar building vs fading) — then groups the means by verdict.

Means by verdict (n=11):

| signal    | LEFT (runners) | SAVED (dumpers) | separates? |
|-----------|----------------|-----------------|------------|
| green%    | +0.9           | -1.5            | no (IVF +26.6 and DCX +3.7 both green, opposite outcomes) |
| momo%     | -5.7           | -11.3           | weak/noisy (both fading into the exit) |
| offHigh%  | -20.7          | -19.2           | no (both exit ~20% off the PM high) |
| volTrend% | -0.9           | +16.2           | inverted (SAVED had *rising* volume) |

**None of the at-exit signals cleanly separate the two classes.** The runners
look the same as the dumpers at 04:30 ET: all fading ~5-12% off a PM high they
had already made, all near-flat green. The standout **IVF was fading -11.6% into
its exit** and still ran to +55% mid-regular-session — the separating event is a
*next-session* move, not observable at the premarket-exit check. This **kills
the "hold if still-green + making higher highs" filter** in the pilot above: the
runners were NOT making higher highs at exit.

**Implication for the pilot.** Since no exit-time filter picks the winners, a
smart conditional hold is not supported by the data. What survives is a
**trailing-stop partial hold applied to every green exit**, where the *stop*, not
a predictive signal, does the sorting: it stays out of the way while a runner
climbs and caps the loss when a fader rolls over. Rough asymmetry: LEFT trades
run +29.7% avg above exit; SAVED trades close ~-20% below exit, but a trailing
stop exits a fader far above its close (near -8 to -10%), not at the close. With
roughly even LEFT/SAVED frequency, a trailing stop that gives up ~half the LEFT
upside while capping SAVED losses near -10% is plausibly net positive — but the
exact capture depends on the intraday path and can only be measured by running
it. That is what the pilot is for.

**Needs from Juan:** approval to pilot a partial-hold variant (it edits the
`Day Trading.md` premarket-exit rule). Until then this stays log-only research.

### 2026-07-13 — the trailing-stop simulation came back NEGATIVE — the partial-hold pilot does NOT beat the premarket-exit baseline

Before proposing the trailing-stop pilot to Juan, simulated it on real fills.
`scripts/trailing-sim.js` (log-only) takes each closed round-trip's premarket
exit as the hypothetical hold-start, walks the exit-day **regular-session
(09:30-16:00 ET) 5-min SIP bars**, and simulates a trailing stop at 8/12/15/20%
widths (peak starts at the exit price; exit at the stop, at the open if it gaps
through, or at the session close). It reports the held partial's capture vs the
all-out-premarket exit, for the green-at-exit population (the pilot's gate) and
for hold-all. Refreshed tally first: **14 round-trips, 6 LEFT / 6 SAVED / 2
flat, avg +29.1% upside missed on LEFT** (the three 07-10 exits YYGH/PMA/ELPW
formed their regular sessions; ELPW closed as a 6th SAVED at -64.9%).

**Result — every width, every gate, LOSES vs the baseline:**

| config | 8% | 12% | 15% | 20% |
|--------|----|-----|-----|-----|
| green-gate avg capture% | -10.2 | -6.4 | -7.3 | -9.0 |
| green-gate added return/trade @50% partial | -5.1 | -3.2 | -3.7 | -4.5 |
| hold-all avg capture% | -8.2 | -8.2 | -8.3 | -9.9 |
| hold-all added return/trade @50% partial | -4.1 | -4.1 | -4.2 | -5.0 |

Two reasons the trailing stop fails:
1. **The green-at-exit gate is the wrong population.** Only **3 of 14** exits
   were green (IVF, EDHL, DCX), and 2 of those 3 (EDHL, DCX) faded. Most of the
   big regular-session runners were **RED at premarket exit** — VTAK 06-24
   (regHigh +33.6%), GANX (+13.7%), SUNE (+16.0%), PMA (+41.9%), YYGH (+13.9%)
   — so the gate that seemed "safe" excludes the very runners we wanted. This
   confirms the 2026-07-10 finding (runners ≠ green at exit) with real cost.
2. **The +29% "upside left" is not mechanically harvestable.** These microcaps
   whipsaw to their highs, so a tight trail (8-12%) gets knocked out early
   (IVF's +55.5% high came at 14:55 ET but an 8% trail stops at -8.0%) while a
   wide trail (20%) gives back too much on the faders. Best single capture is
   PMA +15.4% at ts15, drowned by ELPW -66% and a wall of -8 to -15% stop-outs.

**Conclusion: the trailing-stop partial-hold pilot is WITHDRAWN.** On this
sample no mechanical hold rule (any width, gated or not) beats the all-out-
premarket exit; the premarket-exit discipline is validated by the data. The
+29% avg "upside left" on LEFT trades is real but the choppy path there makes it
uncapturable by a trailing stop. **Problem (b) has no demonstrated mechanical
edge** — do not propose it as a live change. Init 6's reachable money is in
**problem (a)**: the holdable PM-only gappers (SHPH, BJDX, MIMI, EHGO), whose
tally just hit the rollout-step-3 trigger. Re-run `trailing-sim.js` if the
sample grows a lot; a genuine smooth-trending runner could shift it, but 14
trades pointing uniformly negative is a strong signal to stop here.
