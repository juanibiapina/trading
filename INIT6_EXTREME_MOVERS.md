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
| 2026-05-14 | EVOL | +300% *ref* | — | — | regular | regular-spike | ? | None | None found ("needs catalyst") | 3.7M | +300% regular session, only in pre-AH watchlist; no AH follow-up captured | — |
| 2026-06-01 | HKIT | +293.8% | +293.8% ($... 16:00 ET) | <+254% | AH | AH-detect | uninvestable | None | None (negative news: investor lawsuits) | 336K | peaked at 16:00 open, faded -40pts from peak (SPIKE->FADE) | fade |
| 2026-06-08 | CHAI | +416% | +416% ($4.29 17:20 ET) | +72% | AH | AH-detect | uninvestable | None | None (generic AI-stock lists only) | 18.3M | VRatio 8.6x real; +233%@16:45 fade -> new AH high +416%@17:20; over ceiling; faded AH->PM to +72% | fade |
| 2026-06-09 | MSW | +292% | +292% ($5.18 ~18:00 ET) | +221% | AH | AH-detect | traded | C | Acquisition close + dilutive convertible notes | 4.6M | VRatio real, BUILD-and-hold, entered $3.24 | fade |
| 2026-06-10 | CIIT | +140% *ref* | +14.9% (flat) | +140% | PM | PM-gapper | holdable | None | None found | — | flat AH; PM held +126-414% across 5h, opened +203% on 53M sh | continue |
| 2026-06-10 | CPOP | +369% (erratic +597%) | +369% | — | regular | regular-spike | uninvestable | ? | None (multi-day blow-off) | 20.4M | +322% regular day, AH total +369%, history erratic prints to +597%; multi-day extension | fade |
| 2026-06-11 | GLXG | +343% | declined | +343% | PM | PM-gapper | holdable | None | None (week-long decline, tiny-float squeeze) | 1.7M | no AH move; PM held +180-380% across 5h, opened +225% on 48M sh | continue |
| 2026-06-11 | EDHL | +225% | +225% ($11.39 19:15 ET late surge) | <+225% | AH | AH-detect | ? | ? | — | — | near-extreme late surge | fade |
| 2026-06-16 | TDIC | +140% *ref* | -4 to -8% | +140% | PM | PM-gapper | uninvestable | None | None fresh | — | no AH move; PM spiked 04:00 then decayed straight to NEG by 05:30, never recovered | fade-from-open |
| 2026-06-23 | ATLN | +220% *ref* | +6% | — | regular | regular-spike | uninvestable | ? | None | 24.4M | +202% regular session, AH <10% (stale prints), no fresh AH momentum | fade |
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
3. **Catalyst tier separates the continuers from the faders among AH runners
   (STRENGTHENED 2026-07-02).** Every AH-detectable extreme runner that *faded*
   lacked a fresh Tier-A catalyst: MSW (Grade C dilution), CHAI (none), HKIT
   (none / negative news), TII (none), EDHL (weak). The only *continuer*, ILLR
   (+760%), had a fresh Tier-A catalyst (SpaceX). Running tally is now **5
   faders / 1 continuer, 100% consistent** with catalyst tier as the
   discriminator: *extreme AH runner + fresh Tier-A catalyst = let it run;
   extreme AH runner on dilution/no catalyst = fade, take AH profit or skip.*
4. **Real AH volume gates investability of AH runners.** Both ILLR (+760%) and
   TII (+110%) printed huge headline AH % but on ZERO real AH liquidity
   (VRatio <0.5x, ask $0.00), so an AH fill was questionable/impossible even
   though the move was "detected." Headline AH % without AH volume is a trap.
5. **Extreme-runner fade tally (AH peak vs PM peak):** 4 fades (MSW, CHAI,
   HKIT, TII/EDHL weak), 1 continue (ILLR), catalyst tier the discriminator
   (pattern 3).

6. **Regular-session spikes are a distinct negative class the AH->PM strategy
   correctly cannot trade (NEW 2026-07-02).** EVOL (+300%), CPOP (+369%), ATLN
   (+220%) all did their move in the *regular* session with AH <10% follow-
   through, so the AH scanner sees no signal and shouldn't — these are not
   AH->PM setups at all. Not every +200% is our pattern; separating regular-
   session blow-offs from PM-only gappers and AH runners keeps the "catch 600%"
   goal from chasing structurally-untradeable moves.

## Decision analysis (2026-07-03) — which proposal to formalize

The census reached the ~15-case threshold, so this run tested the two candidate
proposals (Tier-A-catalyst **hold rule** vs **PM-open scan**) against the data
instead of gathering more.

**Cross-tab of pattern 3 (catalyst tier) against pattern 4 (real-AH-volume
gate), all 6 AH-detectable extreme runners:**

| Ticker | Cat | AH vol | Holdable | Outcome | Hold-rule verdict |
|--------|-----|--------|----------|---------|-------------------|
| MSW | C | real | yes (traded) | fade | no Tier-A -> don't hold -> **correct (PM exit)** |
| CHAI | None | real 8.6x | no (spike-fade) | fade | no Tier-A -> skip -> correct |
| HKIT | None | real | no | fade | no Tier-A -> skip -> correct |
| TII | ? | **zero** (ask $0.00) | no | fade | untradeable anyway |
| EDHL | ? | ? | ? | fade | weak |
| ILLR | **A** | **zero** (VRatio 0.1-0.4x) | — | **continue** | want to hold, but **untradeable in AH** |

**Result — the Tier-A hold rule has zero tradeable supporting cases.** The only
*continuer* (ILLR) was untradeable in AH (zero real volume, pattern 4), and every
*tradeable* AH runner faded (so the current premarket-exit discipline was
correct on each). Pattern 3 is a real statistical discriminator, but pattern 4
neutralizes its only actionable instance: no case exists where a Tier-A-catalyst
AH runner was tradeable *and* holding past the premarket exit would have earned
more. Formalizing the hold rule now would act on an untradeable pattern. **Shelve
it** until a tradeable Tier-A AH runner (real AH volume + holdable) appears; keep
logging the catalyst tag on extreme AH runners so that case is captured if it
comes.

**Higher-value lever is pattern 2 (PM-open scan).** Its holdable targets — CIIT
(+140%) and GLXG (+343%), both held elevated across the full 5h premarket on
48-53M-share opens — are real, tradeable-looking, and structurally missed by the
AH scanner today. That is where the reachable +200-600% money is, not in the AH
hold rule. So the PM-open scan (rollout step 2), not the hold rule, is the
proposal to advance. Gate remains: 2 holdable gappers so far; want 1-2 more (or a
live-fillability check) before wiring even a log-only pulse, since a single
illiquid tick can masquerade as a holdable 15m bar (Yahoo PM bars report vol=0).

## Fillability check (2026-07-06) — gate MET, PM-open scan justified

The one caveat blocking the PM-open-scan proposal was that Yahoo 15m PM bars
report `vol=0`, so the "holdable" CIIT/GLXG classification rested on price
persistence alone — a single illiquid tick could masquerade as a sustained 15m
bar. Ran the **live-fillability check** the gate asked for using Alpaca SIP
historical minute bars (`broker.js bars <SYM> --tf 5Min --feed sip`, times UTC =
ET+4):

- **CIIT 2026-06-10 (holdable):** deep, real premarket liquidity the *entire*
  ramp — 418K sh / 3,803 trades in the 04:00 ET bar, rising to **3.18M sh /
  55,293 trades** at 04:20 ET, **2.98M sh / 53,926 trades** at 04:35 ET
  ($7.68 area), and 0.4–2.2M sh/bar sustained through 05:00+ ET. Not a tick.
- **GLXG 2026-06-11 (holdable):** thin only in the first 04:00 ET bar (12.8K sh),
  then **2.28M sh / 18,819 trades** at 04:05, **3.60M sh / 57,279 trades** at
  04:10, staying 0.4–3.6M sh/bar as price built $1.94 -> $5.39 by 05:00 ET.
- **TDIC 2026-06-16 (uninvestable control):** *also* had deep liquidity (632K sh
  / 18,718 trades in the first bar), so uninvestability is a **price-path**
  property (peaked $16.23 in the opening bar, decayed straight down), not a
  liquidity one.

**Verdict:** Yahoo's `vol=0` was a data gap, not reality. Both holdable gappers
were genuinely fillable across a multi-hour premarket window on millions of
shares and tens of thousands of trades per 5-min bar — a real exit window
existed. The pattern-2 caveat is closed and the gate to advance the **log-only
PM-open scan** (rollout step 2) is **met**. Bonus: **Alpaca SIP is a validated
premarket data source** (`broker.js bars ... --feed sip`) the scan can use for
live-ish liquidity/price-path reads, where Yahoo is blind. Note: SIP historical
blocks the most recent ~15 min on the free tier, so a live PM-open scan reads a
slightly delayed tape — fine for a log-only observation pulse.

## Open data gaps (next runs)

- ~~Classify investability for CIIT, GLXG, TDIC via PM bars.~~ **Done
  2026-06-30** (`scripts/init6-pmbars.py`): CIIT & GLXG holdable, TDIC
  uninvestable. Use 15m + `range=1mo` + a `Mozilla/5.0` User-Agent to reach
  historical premarket bars (the `query2` host and a UA are both required;
  `chart.py --range 2d` 5m only reaches ~5 days back).
- Backfill float + catalyst tier for EDHL, TDIC, CIIT, MBRX, CUPR, TII.
- ~~Mine the older logs for additional +200% cases (EVOL, CPOP, CHAI, HKIT,
  ATLN).~~ **Done 2026-07-02** — added 5 (census now 14). EVOL/CPOP/ATLN are
  regular-session spikes (negative class, pattern 6); CHAI/HKIT are catalyst-less
  AH spike-fades (support pattern 3). Still open: CCTG, PHGE +265%, EEIQ (log
  shows only +64%, likely mis-noted). Census is at the ~15-case analytic
  threshold; pattern 3 and pattern 2 can now be tested.
- Once ~15-20 cases are tagged, test pattern 3 (catalyst-tier discriminator)
  and pattern 2 (PM-gapper investability) for whether they justify (a) a PM-open
  scan workflow and/or (b) a conditional hold rule for Tier-A AH runners.
