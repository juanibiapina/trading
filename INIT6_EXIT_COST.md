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
- **Pilot (needs Juan — changes the "never hold through the day" rule):** on a
  position that is **green and still making higher highs at the premarket-exit
  check**, hold a **partial** (e.g. half) into the regular session with a trailing
  stop, exit the rest in premarket as usual. Compare the held-partial P&L to the
  baseline all-out-premarket exit. Start with 1 position at a time for
  attribution (pilot-serialized).

**Open question before piloting:** what signal at the premarket-exit check best
separates the IVF-type regular-session runners from the DCX-type open-dumpers?
Candidates: still-green + higher-highs into 09:00 ET, sustained real volume,
fresh Tier-A catalyst. Needs a few more logged cases to test.

**Needs from Juan:** approval to pilot a partial-hold variant (it edits the
`Day Trading.md` premarket-exit rule). Until then this stays log-only research.
