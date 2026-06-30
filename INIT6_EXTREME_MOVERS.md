# Initiative 6 — Extreme-Movers Census

Seed dataset for Initiative 6 (catch the rare +300-600% runners) and the
pattern-extraction goal Juan endorsed (2026-06-26: "+760% is exactly the kind
of stuff we want to catch... extract patterns from those"). Consolidates the
extreme movers already tracked in prose across the daily logs into one
reviewable table so the data can produce reusable entry/skip signals.

Living file — expand it each Init 6 run by mining more daily logs. Threshold for
inclusion: peak >=+200% from prior close (a few notable sub-200% PM-only gappers
kept as reference, marked *ref*).

## Columns

- **Lead:** where the decisive move happened — `AH` (after-hours), `PM`
  (premarket only), or `regular` (regular session).
- **Detect:** could the AH->PM scanner see it? `AH-detect` (>10% AH footprint),
  `PM-gapper` (flat/down in AH, exploded only after 04:00 ET — structurally
  invisible), or `regular-spike`.
- **Invest:** `holdable` (gain held >=2 5-min bars on real volume = exit window
  existed), `uninvestable` (instant crash / thin single-tick peak), `traded`
  (we actually took it), or `?` (not yet classified).
- **Cat:** catalyst tier — A (operational/strategic), B, C, D (dilution),
  None.
- **Outcome:** `fade` (AH peak > PM peak) or `continue` (PM peak > AH peak).

## Census

| Date | Ticker | Peak% | AH peak% | PM peak% | Lead | Detect | Invest | Cat | Catalyst | Float | Vol note | Outcome |
|------|--------|-------|----------|----------|------|--------|--------|-----|----------|-------|----------|---------|
| 2026-06-09 | MSW | +292% | +292% ($5.18 ~18:00 ET) | +221% | AH | AH-detect | traded | C | Acquisition close + dilutive convertible notes | 4.6M | VRatio real, BUILD-and-hold, entered $3.24 | fade |
| 2026-06-10 | CIIT | +140% *ref* | +14.9% (flat) | +140% | PM | PM-gapper | holdable | None | None found | — | flat AH; PM held +126-414% across 5h, opened +203% on 53M sh | continue |
| 2026-06-11 | GLXG | +343% | declined | +343% | PM | PM-gapper | holdable | None | None (week-long decline, tiny-float squeeze) | 1.7M | no AH move; PM held +180-380% across 5h, opened +225% on 48M sh | continue |
| 2026-06-11 | EDHL | +225% | +225% ($11.39 19:15 ET late surge) | <+225% | AH | AH-detect | ? | ? | — | — | near-extreme late surge | fade |
| 2026-06-16 | TDIC | +140% *ref* | -4 to -8% | +140% | PM | PM-gapper | uninvestable | None | None fresh | — | no AH move; PM spiked 04:00 then decayed straight to NEG by 05:30, never recovered | fade-from-open |
| 2026-06-23 | MBRX | +131% *ref* | flat | +131% | PM | PM-gapper | uninvestable | ? | — | — | crashed $6.64->$3.77 in 10 min | continue-then-crash |
| 2026-06-24 | CUPR | +81% *ref* | — | +81% | PM | PM-gapper | uninvestable | — | — | — | $9.74 high was an illiquid single tick | — |
| 2026-06-26 | ILLR | +760% | +446% ($4.20 19:55 ET) | +760% | AH | AH-detect | skipped | A | SpaceX position acquisition (fresh, ongoing news cycle) | — | ZERO real AH volume (VRatio 0.1-0.4x), AH fill questionable | continue |
| 2026-06-26 | TII | +110% *ref* | +110% ($4.56 18:25 ET) | faded -29% | AH | AH-detect | uninvestable | — | — | — | ZERO AH volume (ask $0.00 x0), illiquid ramp trap | fade |

## Patterns observed (running)

1. **Two structurally distinct big-mover classes.** (a) PM-only gappers (CIIT,
   GLXG, TDIC, MBRX, CUPR) are flat/down in AH and explode only after 04:00 ET
   — the AH scanner cannot see them by design. (b) AH-detectable runners (MSW,
   ILLR, EDHL, TII) have an AH footprint the scanner does catch.
2. **PM-only gappers are NOT mostly uninvestable — it is ~50/50, and the
   holdable ones are exactly the targets (UPDATED 2026-06-30).** Classifying the
   three remaining PM-only gappers from their 15m premarket price path flipped
   this pattern: **CIIT (+140%) and GLXG (+343%) were holdable** — both held
   elevated (+126-414% / +180-380%) across the *entire* 04:00-09:15 premarket
   window (20+ consecutive 15m bars, impossible to sustain on a single tick) and
   opened on 48-53M shares, so a multi-hour exit window existed. Only **TDIC was
   uninvestable** (spiked at 04:00, decayed to negative within 90 min). Running
   PM-only tally: **2 holdable (CIIT, GLXG), 3 uninvestable (MBRX, CUPR, TDIC)**.
   The holdable two are precisely the +140%/+343% movers Juan wants. So the
   AH-blind-spot has **real cost**, not low cost — a PM-open scan could have
   caught two large holdable runners in a single week. This raises the priority
   of rollout step 2 (instrument a log-only PM-open scan). Caveat: Yahoo 15m PM
   bars report vol=0, so true premarket *fillability* (vs sustained quotes) still
   needs live NBBO at the moment, the same Init 2 caveat; price persistence + the
   real-volume opens are strong but not conclusive on slippage.
3. **Catalyst tier separates the continuers from the faders among AH runners.**
   ILLR (Tier A, fresh SpaceX news) continued AH->PM to +760%; MSW (Grade C,
   dilutive notes) faded AH->PM. EDHL/TII faded with weak/no catalyst. One
   strong signal forming: *extreme AH runner + fresh Tier-A catalyst = let it
   run; extreme AH runner on dilution/no catalyst = fade, take AH profit.*
4. **Real AH volume gates investability of AH runners.** Both ILLR (+760%) and
   TII (+110%) printed huge headline AH % but on ZERO real AH liquidity
   (VRatio <0.5x, ask $0.00), so an AH fill was questionable/impossible even
   though the move was "detected." Headline AH % without AH volume is a trap.
5. **Extreme-runner fade tally (AH peak vs PM peak):** 1 fade (MSW), 1 continue
   (ILLR), with the catalyst tier as the apparent discriminator (pattern 3).

## Open data gaps (next runs)

- ~~Classify investability for CIIT, GLXG, TDIC via PM bars.~~ **Done
  2026-06-30** (`scripts/init6-pmbars.py`): CIIT & GLXG holdable, TDIC
  uninvestable. Use 15m + `range=1mo` + a `Mozilla/5.0` User-Agent to reach
  historical premarket bars (the `query2` host and a UA are both required;
  `chart.py --range 2d` 5m only reaches ~5 days back).
- Backfill float + catalyst tier for EDHL, TDIC, CIIT, MBRX, CUPR, TII.
- Mine the older logs (Mar-May) for additional +200% cases (EVOL +300%, CCTG,
  CPOP +322%, CHAI +416-438%, PHGE +265%, HKIT +254%, EEIQ +209%, ATLN +220%)
  and tag each — several are regular-session spikes, not AH/PM, which is itself
  a useful negative class.
- Once ~15-20 cases are tagged, test pattern 3 (catalyst-tier discriminator)
  and pattern 2 (PM-gapper investability) for whether they justify (a) a PM-open
  scan workflow and/or (b) a conditional hold rule for Tier-A AH runners.
