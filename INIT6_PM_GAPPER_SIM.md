# Init 6 — PM-only-gapper hypothetical-entry pilot (LOG-ONLY)

Quantifies whether the **holdable PM-only gappers** logged by the `pm-open-scan`
pulse (the AH->PM scanner's structural blind spot) would have made money as
hypothetical paper trades. Answers rollout step 3 for Initiative 6 problem (a):
are these AH-blind names worth proposing as a live pulse to Juan?

Script: `scripts/pm-gapper-sim.js` (no orders, no trading-logic change).

## Model

- **Entry (current):** the `pm-open-scan` cron runs 11:00 CEST = 09:00Z =
  **05:00 ET**. Hypothetical buy at the open of the 09:00Z 5-min bar.
- **Entry (early):** 08:10Z = **04:10 ET**, two bars after the 04:00 ramp
  confirms — models a hypothetical *earlier* PM pulse, to isolate the value of
  detecting sooner.
- **Exits compared:** PM-last (hold to 09:25 ET), RegOpen (sell at 09:30 ET
  open), RegHigh (best-case passive hold, unhittable), RegClose (sell 16:00 ET).
- Population: the 5 `holdable` + `ah_footprint=none` rows in
  `log/pm-open-scan.csv` (SHPH 07-08, BJDX 07-09, MIMI 07-13, EHGO 07-13,
  BJDX 07-14). BJDX 07-14's regular session was still pending at run time.

## Result (2026-07-14, n=4 with a formed regular session)

| date | sym | gap | entry@05:00 | PM-last | RegOpen | RegHigh | RegClose |
|------|-----|-----|------|---------|---------|---------|----------|
| 07-08 | SHPH | +13.8 | $4.13 | -19.9% | -19.1% | -13.6% | -17.2% |
| 07-09 | BJDX | +14.9 | $1.63 | -8.0% | -8.0% | -1.2% | -14.1% |
| 07-13 | MIMI | +68.1 | $3.50 | -11.1% | -11.1% | -1.1% | -15.7% |
| 07-13 | EHGO | +75.0 | $2.30 | -7.8% | -7.4% | +23.5% | -6.5% |

**Mean return, entry at 05:00 ET (current pulse time):**
- PM-last: **-11.7%** · RegOpen: **-11.4%** · RegClose: **-13.4%** ·
  RegHigh (best-case): +1.9%

**Mean return, EARLY entry at 04:10 ET (hypothetical earlier pulse):**
- PM-last: **-8.2%** · RegOpen: **-7.9%** · RegClose: **-9.7%** ·
  RegHigh (best-case): +6.8%

## Findings

- **NEGATIVE. A naive long entry on holdable PM-only gappers loses money at every
  realistic entry and exit.** 12 of 12 realistic entry×exit combinations are
  negative (both entry times × PM-last/RegOpen/RegClose). Only the
  impossible-to-time RegHigh is positive.
- **The "holdable" tag measures exitability, not profitability.** These names
  make their PM high in the first 1-2 bars (04:00-04:35 ET), then "hold within
  20% of high across bars" as a slow bleed. Liquidity to exit exists; a long edge
  does not — by the time price is confirmed holding, it is already fading below
  any tradable entry.
- **Earlier detection helps but does not rescue it.** Moving entry from 05:00 to
  04:10 ET lifts the mean ~3-4 points but stays firmly negative (-8% to -10%).
  So adding an earlier PM pulse (Init 3) would not turn this population
  profitable on its own.
- Consistent with the 07-13 `trailing-sim.js` result on AH->PM exits: these
  microcaps whipsaw to their intraday highs (EHGO's +23.5% RegHigh) but the pops
  are not mechanically harvestable at scale.

## Conclusion

**Do not promote a PM-only-gapper long pilot to a live pulse.** The AH-blind-spot
names, as currently classified, carry no demonstrated long edge at any detectable
or tradable time. Keep `pm-open-scan` as **log-only accumulation** (cheap, one
pulse) rather than escalating to hypothetical orders or proposing a live entry
rule to Juan.

**Caveat / what would change the verdict:** n=4 is small. The one positive-ish
signal is intraday range (RegHigh averaged +1.9% / +6.8%), so any future edge
here would have to come from a *momentum-continuation* rule that re-enters on a
confirmed intraday breakout, not from buying the overnight gap and holding. That
is a different, more complex setup; park it unless the sample grows and the
RegHigh dispersion widens materially.

Re-run: `node scripts/pm-gapper-sim.js` (auto-loads the tracker) as more holdable
PM-only gappers accumulate.
