# Init 3 — Ignition timing vs the AH scan grid

Research artifact for Initiative 3 (adaptive scheduling / faster ignition
detection). Init 1 falsified the volume-*lead* hypothesis and reframed "we catch
spikes late" as a **scan-timing** problem: ignition is a single-minute
price+volume co-spike (IVF 16:53 ET), so the lever is how fast our scan grid
sees that minute. This audit quantifies the ignition-vs-grid gap across winners.

**Tool:** `scripts/ignition-timing.js` (log-only, no orders). For a ticker +
AH-evening date D it pulls real Alpaca SIP **1-min** bars for the AH session
(D 16:00–20:00 ET), baseline = the D regular-session daily close, and finds the
**ignition bar** = first 1-min bar that both (a) highs ≥ +15% vs base and (b)
carries a real volume co-spike (≥20 trades and ≥5× the running median trades).
It then maps the ignition minute onto the current AH scan grid and reports the
first scan at/after ignition and the lag.

**Current AH scan grid (ET):** 15:30, 16:00, 16:30, 17:00, 17:30, 18:00, 18:30
(= 21:30…00:30 CET, 30-min spacing; summer CET = ET + 6h).

## Batch (2026-07-16, IGN≥+15%, MINTR=20, K=5×)

| sym  | AH-eve date | ignition ET | ign % | trades/sh at ign | first scan ≥ ign | lag   | note                    |
|------|-------------|-------------|-------|------------------|------------------|-------|-------------------------|
| XCUR | 2026-07-14  | 16:08       | +41%  | 182 / 48k        | 16:30            | +22m  | open cluster            |
| ATPC | 2026-07-15  | 16:09       | +24%  | 453 / 46k        | 16:30            | +21m  | open cluster            |
| EDHL | 2026-07-06  | 16:12       | +25%  | 74 / 3.5k        | 16:30            | +18m  | open cluster            |
| TGHL | 2026-07-15  | 16:21       | +40%  | 1491 / 728k      | 16:30            | +9m   | open cluster            |
| VTAK | 2026-06-23  | 16:47       | +17%  | 208 / 77k        | 17:00            | +13m  | open cluster            |
| IVF  | 2026-06-25  | 16:53       | +19%  | 72 / 25k         | 17:00            | +7m   | open cluster            |
| VMAR | 2026-07-13  | 17:01       | +17%  | 1154 / 220k      | 17:30            | +29m  | mid-AH                  |
| GMM  | 2026-07-09  | 18:05       | +16%  | 21 / 2.4k        | 18:30            | +25m  | tail                    |
| KUST | 2026-07-14  | 18:25       | +19%  | 93 / 16k         | 18:30            | +5m   | tail                    |
| MSW  | 2026-06-08  | 19:01       | +33%  | 461 / 78k        | none (past 18:30)| MISS  | tail — grid never sees  |

## Findings

1. **Ignition is not before the grid — the grid is too coarse.** The earlier
   framing ("our 16:15 ET scan runs before IVF's 16:53 ignition") was too
   narrow: every winner here except MSW ignites *inside* the grid window, but
   the 30-min spacing means the first scan to see the move fires **7–29 min
   after ignition** (median ~+18 min), by which point the name is already partway
   up. The lever is **cadence, not phase**.

2. **The dominant cluster is the AH open, 16:08–16:53 ET (6 of 10).** These
   ignite in the first hour and wait up to +22 min for the 16:30/17:00 scan. A
   denser cadence in the first ~75 min of AH (e.g. add 16:15 and 16:45 ET scans,
   i.e. 22:15 and 22:45 CET) would cut the worst-case lag from ~22 min to ~7 min
   and catch the open igniters closer to the ignition price.

3. **A real tail exists past the grid end (18:30 ET).** MSW ignited at 19:01 ET
   and the grid **never sees it live** (last scan 18:30 ET / 00:30 CET). GMM
   (18:05) and KUST (18:25) sit at the tail edge with +25m / +5m lag. Juan
   pre-authorized 1–2 late scans (~01:00/01:30 CET = 19:00/19:30 ET) once the
   18:30–20:00 ET tail shows ≥3–4 winners; this batch adds MSW to that count
   (GMM/KUST are just before 18:30). Tail evidence is building but not yet at the
   trigger.

## Proposed schedule change (for Juan to veto — touches trading-scan timing)

**Do not apply silently.** Two cadence changes, ranked by expected value:

- **(A) Densify the AH-open hour.** Add scans at **22:15 and 22:45 CET
  (16:15 / 16:45 ET)** so the first hour is 15-min spaced. Rationale: 6 of 10
  winners ignite 16:08–16:53 ET and currently wait 7–22 min for a scan; this
  halves the median catch-lag on the dominant cluster. Cost: +2 scan rounds/day.
- **(B) Extend into the tail.** Add **01:00 and 01:30 CET (19:00 / 19:30 ET)**
  scans (Juan pre-authorized these). Rationale: MSW-type tail igniters are
  invisible today. Cost: +2 rounds/day. Weaker than (A) until the tail count
  reaches the 3–4 trigger — MSW is 1.

**Caveats:** n=10 winners, SIP 1-min historical (no NBBO). Entry is still banned
before 23:00 CET / 17:00 ET in the current rules, so (A)'s 16:15/16:45 scans
would be *observation* scans (catch + log the ignition) feeding a faster entry
decision at 17:00 ET, not new entry windows — consistent with Juan's 2026-07-16
"catch the first volume spike bar" ask, whose blocker is exactly this detection
latency.

## Out-of-sample validation (2026-07-20) — 3 fresh AH names, new 15-min grid

After the 2026-07-17 cadence change the AH-open hour is 15-min spaced. New grid
(ET): **15:30, 16:00, 16:15, 16:30, 16:45, 17:00, 17:30, 18:00, 18:30** (the
16:15/16:45 scans = 22:15/22:45 CET are new). Ran `scripts/spike-bar.js` (same
co-spike detector) on 3 AH names from the 07-16 session that were **not** in the
original batch, to test (a) that the detector generalizes and (b) whether the new
scans reduce catch-lag.

| sym  | AH-eve date | ignition ET | ign % | trades/sh   | first scan ≥ ign | lag  | outcome                          |
|------|-------------|-------------|-------|-------------|------------------|------|----------------------------------|
| BIYA | 2026-07-16  | 16:28       | +17%  | 85 / 12k    | 16:30            | +2m  | held/built (+48% AH), entered     |
| GCTK | 2026-07-16  | 16:57       | +30%  | 730 / 603k  | 17:00            | +3m  | **SPIKE→faded**, skipped (correct) |
| CJMB | 2026-07-16  | 17:33       | +22%  | 262 / 79k   | 18:00            | +27m | late-BUILD, **our traded winner** (+19.8%) |

**Findings:**

1. **Detector generalizes (3/3).** Every fresh AH mover fired SPIKE at a minute
   consistent with the daily-log narrative (BIYA building from the open → 16:28;
   GCTK early pump → 16:57; CJMB "dead until 17:30 then exploded" → 17:33). No
   false negatives on real movers.

2. **GCTK is a SPIKE-then-fade** (ignited 16:57 +30%, then declined and was
   correctly skipped). Confirms the spike bar alone is **not** an entry green
   light — continuation/BUILD gating is still required. Tempers the eventual
   entry-trigger design: "first co-spike bar" marks ignition, not a buy.

3. **New open-hour scans didn't help these 3** — but not a negative result. The
   16:15/16:45 scans benefit igniters landing in 16:00–16:14 and 16:31–16:44;
   these three ignited at 16:28 / 16:57 / 17:33, just after existing scan points.
   Benefit awaits a live igniter in the new sub-windows (first real test is the
   next AH sessions, now that the scans are wired).

4. **NEW gap — the late window (17:00–18:30 ET) is still coarse, and it caught
   the actual traded winner late.** CJMB (the name we entered and won +19.8% on)
   ignited at 17:33 ET and waited **+27 min** for the 18:00 scan; we didn't enter
   until the 18:30 final scan. This is the first case of a **late-BUILD igniter**
   (17:00–18:30 ET) undercaught by the current 30-min late spacing — the
   densification so far only covers the open hour. **Watch:** if 2–3 late-BUILD
   winners accumulate in the 17:00–18:30 ET window, propose 15-min spacing there
   too (add 23:45 + 00:15 CET = 17:45 + 18:15 ET). Late-BUILD tally: CJMB = 1.

---

## First live out-of-sample AH session (2026-07-20, the wired scans firing)

The 22:15/22:45 CET (16:15/16:45 ET) observation scans fired live for the first
time on the Mon 07-20 AH session (they are Mon–Thu). The spike-bar column also
ran live in every entry-eligible scan. Three findings, from `log/2026-07-20/log.md`.

### 1. Spike-bar column validated live end-to-end (6 names)

The log-only column populated on every AH >10% candidate across the 22:30–00:30
CET scans, with verdicts consistent with the SIP price path:

| sym  | verdict   | ignition ET | ign detail                    | outcome (morning eval)              |
|------|-----------|-------------|-------------------------------|-------------------------------------|
| HIHO | SPIKE     | 16:04       | +16% $1.08 373 tr / 190k sh   | winner, entered $1.50; PM peak $1.89 |
| SHPH | SPIKE     | 16:04       | +22% $3.69 550 tr / 50k sh    | untradable (broker-block)            |
| PAPL | SPIKE     | 17:09       | +20% $1.06 244 tr / 61k sh    | entered $1.10; faded, exit $0.84     |
| ADVB | SPIKE     | 17:32       | +17% $10.40 2030 tr / 136k sh | skipped on ceiling; PM faded -16%    |
| RDGT | SPIKE     | 18:00       | +17% $1.85 857 tr / 151k sh   | gate-blocked (1st AH at final scan)  |
| GORO | NO-SPIKE  | —           | peak +6%, no co-spike bar     | **correctly skipped** (bad print)    |

The detector runs in the cron environment and reproduces on replay
(`node scripts/spike-bar.js HIHO:2026-07-20 --now 17:00` → SPIKE 16:04;
`GORO:2026-07-20` → NO-SPIKE). **GORO NO-SPIKE = correct skip** (AH +240% on 17K
sh vs a 160M float = bad print). But **SPIKE ≠ winner**: PAPL and ADVB both fired
SPIKE and then faded — so the column confirms *ignition*, not *outcome*.
Continuation/BUILD gating stays required before any spike-bar entry trigger.

### 2. The screener feed is BLIND before ~16:30 ET — the 22:00/22:15 densification
adds nothing via the screener; only the SIP cross-check reaches the open window

The 22:00 (16:00 ET) and 22:15 (16:15 ET) scans both returned **0 screener
hits**: the TradingView postmarket field does not populate until ~16:30 ET. So
15-min-spacing the *open* hour with **screener** scans cannot catch the dominant
16:08–16:53 ET ignition cluster — the screener is empty there. What *did* reach
the early window was the **SIP cross-check** (feed-lag rescue) already in
`post-market-scan.md`: at 22:15 it pulled real SIP bars on the carried watch
names and flagged ADVB's live AH volume while the screener showed nothing.
HIHO ignited 16:04 ET but the screener didn't surface it until the 22:30 scan
(16:30 ET) — a ~26 min screener lag. Entry is banned before 23:00 CET, so this
cost no entry (HIHO had 3 populated AH scans before the 23:00 entry), but it
means the open-hour densification's value comes from the **SIP path, not the
screener**. Implication for a future step: to actually shrink open-window
catch-lag, the 22:00/22:15 scans should run the SIP spike-bar check on the
regular-session watch list by default (the screener won't help there).

### 3. Late-window (17:00–18:30 ET) densification case strengthened — RDGT joins CJMB

RDGT ignited **18:00 ET** (SPIKE, 151k sh / 857 trades, real micro-float 884K
build) but **first appeared at the 00:30 CET / 18:30 ET final scan**, so the
2-AH-scan gate can never be met and it was structurally un-enterable. RDGT then
continued to a **PM peak $2.33 (+47%)**. An **18:15 ET scan (00:15 CET) would
have surfaced RDGT at 18:15 AND 18:30 = gate met → entry-eligible at 18:30.** This
is the same late-window gap CJMB exposed (07-16: ignited 17:33, caught +27m late).

**Late-window support tally now 2:** CJMB (07-16, traded winner +19.8%, caught
late) and RDGT (07-20, PM +47%, gate-blocked, an 18:15 scan rescues it). This
reaches the low end of the "2–3 cases" trigger for proposing 15-min spacing in
the 17:00–18:30 ET window (add 23:45 + 00:15 CET = 17:45 + 18:15 ET). These are
*entry-eligible* scan points (after the 23:00 CET ban), so unlike the open-hour
observation scans they change live entry behavior → **propose to Juan for veto,
do not apply silently.**

---

## Watch-list source test for the pre-16:30-ET open window (2026-07-22, strategy-advance)

Finding 2 above showed the screener is **blind before ~16:30 ET**, so the only
way to shrink open-window catch-lag is to run the SIP spike-bar check on a
**pre-seeded watch list** at 22:00/22:15 CET. The open question that gates
building that: **does a "regular-session day-movers" list actually contain the
AH igniters we care about?** Fresh post-close-news igniters (earnings dropped at
16:00 ET) may be flat in the regular session and absent from any day-movers list.

Tested it directly from Alpaca daily bars (regular-session-only OHLC): for each
recent AH igniter, computed the regular-session day% (prior close → that day's
regular close, and → regular high) and checked it against scan.py's
`MIN_DAY_CHANGE_REGULAR = 15` day-mover threshold.

| Ticker | AH-eve | Prior C | Reg C | Reg C% | Reg H% | Day-mover (>15%)? | AH/PM outcome |
|--------|--------|---------|-------|--------|--------|-------------------|----------------|
| HIHO   | 07-20  | 0.78    | 0.93  | +19.2% | +20.5% | **YES**           | traded winner (+26% hypo; entered) |
| ADVB   | 07-20  | 5.03    | 8.90  | +76.9% | +87.3% | **YES**           | SPIKE→fade (skipped) |
| CJMB   | 07-16  | 0.74    | 0.86  | +16.2% | +24.3% | **YES**           | traded winner +19.8% |
| RDGT   | 07-20  | 1.41    | 1.58  | +12.1% | +13.5% | no (borderline)   | PM +47%, gate-blocked |
| AEHL   | 07-21  | 0.67    | 0.65  | −3.0%  | +14.9% | no (borderline)   | SPIKE→fade (skipped) |
| PAPL   | 07-20  | 0.91    | 0.88  | −3.3%  | 0%     | **no**            | entered, faded −23.6% |
| KUST   | 07-21  | 1.27    | 0.96  | −24.4% | 0%     | **no**            | fade/dead-cat (skipped) |

**Result: 3 of 7 clear the day-mover threshold — but both traded WINNERS
(HIHO, CJMB) are in the caught set, and the misses skew to faders/losers.** The
names a regular-session day-movers pre-seed would **miss** (PAPL −23.6%, KUST
dead-cat, AEHL fade; RDGT the one profitable miss) are dominated by names we
either lost on or correctly skipped. The two AH→PM continuations we actually made
money detecting were **already +16–19% in the regular session** before their AH
ignition, so a 16:00 ET day-movers list surfaces them, letting the 22:00/22:15
SIP spike-bar check catch the ignition bar 15–30 min ahead of the ~16:30 ET
screener (HIHO ignited 16:04, screener surfaced it only at 22:30).

**Design conclusion.** The regular-session day-movers list is a **useful but
partial** early-watch source: it rescues the profitable subset (AH igniters that
were already regular-session movers) and its blind spot (flat/down-regular
post-close-news names) skews toward faders in this n=7 sample. It cannot help a
genuinely flat-regular igniter like PAPL — those depend on the external ~16:30 ET
screener population, which we can't beat. **Next step: wire scan.py's
`--day-movers` regular list as the 22:00/22:15 CET watch source and run
spike-bar.js on each (log-only), then measure over more sessions whether the
"winners are already day-movers" pattern holds before proposing any entry use.**
Small sample — treat the "both winners caught" as promising, not proven.

### Census extension (2026-07-27, strategy-advance) — n=7 → n=9, and a clean counter-example

Added the two AH→PM **continuers** from the 07-22/07-23 sessions (both bigger PM
moves than anything in the original 7) to test whether the "winners are already
regular-session day-movers" pattern holds. Regular-session-only OHLC from Alpaca
daily bars; LGCL's regular-session volume cross-checked against its 5-min bars.

| Ticker | AH-eve | Prior C | Reg C | Reg C% | Reg H% | Reg vol vs prior | Day-mover (>15%)? | AH/PM outcome |
|--------|--------|---------|-------|--------|--------|------------------|-------------------|----------------|
| JEM    | 07-23  | 3.53    | 4.74  | +34.3% | +58.4% | huge             | **YES**           | AH→PM continuer, PM +48% (winner) |
| LGCL   | 07-22  | 0.98    | 0.95  | −3.1%  | +9.2%  | **78.6k ≈ prior 94k (flat)** | **no** | AH→PM continuer, **PM +114%** (biggest recent winner) |
| PLAG   | 07-22  | 0.54    | 0.59  | +9.3%  | +20.4% | huge             | no (borderline)   | PM faded (uninvestable) |

**Result: the pattern half-holds and gains a decisive counter-example.** JEM
(+34.3% regular) confirms the "already a day-mover" path — caught, and a real
+48% PM winner. But **LGCL breaks the "both winners caught" claim**: it was
**flat and low-volume in the regular session** (−3.1% close, +9.2% high, only
78.6k regular-session shares vs ~94k the prior *full* day), then ignited entirely
**post-close** (AH high $1.58 at 18:15 ET) and ran to **PM +114%** — the single
biggest PM winner in this whole sample. A regular-session day-movers **or**
relative-volume pre-seed misses it completely: there is no regular-session
footprint to surface it. It is the same flat-regular class as PAPL, except LGCL
proves that class contains some of the **biggest** PM winners, not just faders.

**Refined design conclusion.** The day-movers watch source is worth wiring — it
rescues the "already-moving" AH→PM continuers (HIHO, CJMB, JEM) and lets the
22:00/22:15 SIP spike-bar check catch their ignition bar 15–30 min ahead of the
~16:30 ET screener — but it is **structurally incomplete**: flat-regular
post-close igniters (PAPL fader, **LGCL +114% winner**) have no regular-session
signal (neither %change nor relative volume) and can only be reached through the
external ~16:30 ET screener feeding the tighter AH scan grid. So the two detection
paths are complementary, not substitutes: (1) day-movers watch source for
already-moving names (pre-16:30 ET head start), (2) the 16:30 ET screener + 15-min
AH grid for the flat-regular igniters. Wire the watch source as an *additive*
log-only pre-seed, not a replacement for the screener. Running tally on the
"winners are already day-movers" question: **3 caught (HIHO, CJMB, JEM) / 1 clear
miss (LGCL, and the biggest winner at that)** — promising for the moving subset,
but do not assume it catches the whole winner set.

---

## Day-movers pre-seed — first live night (2026-07-28) + extended winner census (2026-07-29)

The pre-seed went live in the 21:30/22:00/22:15 CET scans on 2026-07-28. The
hypothesis for this run: does any day-mover show a `SPIKE` verdict in the early
window **before** the same name reaches the 22:30+ screener (measured lead-time)?

**First-night result: zero lead. The pre-seed predicted 0 of 4 real ignitions.**
At 22:30 CET (16:30 ET) the screener populated and the spike-bar detector fired
real ignition bars on **four** names — AMIX (16:03 ET), YIBO (16:06), IOTR
(16:08), EGG (16:06). Of those, **only EGG was on the day-movers watch list, and
it was the worst-behaving one** (faded on collapsing volume). AMIX, YIBO and IOTR
had no regular-session footprint (Day% −1.4%, −2.5%, +3.0%) — pure post-close
ignitions, the LGCL-shaped class the pre-seed is structurally blind to. AMIX went
on to be paper-entered 07-28 AH and ran to **PM +63% (07-29 winner)** — caught by
the screener+spike-bar path, invisible to the pre-seed.

**Extended winner census (6 recent ah-detected holdable PM winners).** Regular-
session Day% on the AH-eve (Alpaca daily bars, vs prior close):

| Ticker | PM date | AH-eve | reg Day% | >=15% (pre-seed reach) | PM result |
|--------|---------|--------|----------|------------------------|-----------|
| AMIX   | 07-29   | 07-28  | −1.4%    | **MISS**               | PM +63% (paper-entered winner) |
| STFS   | 07-29   | 07-28  | +19.4%   | HIT                    | PM +44% holdable |
| GMM    | 07-29   | 07-28  | −8.5%    | **MISS**               | PM +42% holdable |
| INLF   | 07-28   | 07-27  | +2.8%    | **MISS**               | PM +49% holdable |
| POLA   | 07-28   | 07-27  | +1.4%    | **MISS**               | PM +37% holdable |
| BIYA   | 07-28   | 07-27  | +116.1%  | HIT                    | PM +30% holdable |

**Only 2 of 6 recent winners are reachable by the day-movers pre-seed** (STFS,
BIYA); the other 4 — including the biggest, AMIX — ignite post-close with no
regular-session footprint. Combined with the prior census the split is ~even
(reg day-movers: HIHO, CJMB, JEM, STFS, BIYA = 5; post-close ignitions: LGCL,
AMIX, GMM, INLF, POLA = 5), but the cleanest/biggest winners (AMIX +63% paper
win, LGCL +114%) are both in the pre-seed's blind class.

**Decisive conclusion — the pre-seed provides no actionable entry-lead.** Two
independent reasons: (1) it surfaces only ~half of AH→PM winners; (2) even for
those, the 16:30 ET screener already carries them at 22:30 CET, a full 30 min
before entries are allowed at 23:00 CET — so the pre-seed's only theoretical edge
is a name it flags in the 22:00–22:15 window that the 22:30 screener misses, which
did **not** happen on night 1. It stays cheap log-only for a couple more nights to
confirm the zero-lead across sessions; if night 2–3 also show no early-window
name that the screener misses, trim the pre-seed instruction to save scan-time
effort (an Init-3 cost-reduction, not a schedule or trading-rule change).

### Second live night and retirement (2026-07-30)

The 2026-07-29 AH session repeated the zero-lead result. At 22:15 CET every
pre-seed name was `NO-SPIKE`. The 22:30 main screener then found DCX, CRE, and
SXTP; none had been flagged early. DCX was present in the pre-seed but its live
16:15 ET SIP check still read `NO-SPIKE`, while the later replay located its
ignition at 16:03 ET. That is a bar-arrival lag, so more pre-seed symbols would
not have fixed it. The night's real winner, NUWE (+147% PM peak from close), had
no pre-seed signal and first surfaced through the main screener at 22:45 CET.

**Decision: retire the pre-seed after two live nights with zero actionable
lead.** It reached only part of the winner universe, never surfaced a useful
name before the 22:30 screener, and added up to dozens of SIP calls to each early
scan. Removed the instrumentation block from `prompts/post-market-scan.md`; the
`scan.py --day-movers` option remains available for research and the regular
21:30 scan. No schedule, entry rule, or live trading logic changed.

The next Init 3 test follows Juan's 2026-07-29 feedback: replay recent AH-open
ignitions on a 5-minute grid and measure a second/third-bar price-plus-volume
confirmation against the current 15-minute observation cadence. AMIX alone is
not enough to justify more live scans; the replay must compare entry-price gain,
false positives, and pulse cost across winners and fades.

## Five-minute second/third-bar replay (2026-07-31)

Built `scripts/ah-5m-confirmation-replay.js` (log-only, no orders) and ran it on
10 recent AH-open cases: three winners (AMIX, NUWE, KUST), one moderate
continuation (DCX), and six fades/non-winners (CRE, BOOM, ONMD, YIBO, IOTR,
EGG). The causal ignition gate requires a green new-high 5-minute close at least
10% above the regular close, at least 20 trades, and volume at least 2x the
median of up to three immediately preceding active bars. Confirmation must hold
every intervening close within 80% of the running high and finish with close and
volume at least as high as the ignition bar. Entry is the next bar's open.

| Rule | Admitted | Winners caught | Fade false positives | Mean PM-open return | Mean entry-price edge vs current legal grid |
|------|----------|----------------|----------------------|---------------------|---------------------------------------------|
| Second bar | 3/10 | 2/3 | 1/6 (ONMD) | +13.6% | **-4.6%** |
| Third bar | 3/10 | **3/3** | **0/6** | **+30.0%** | **-6.1%** |

The local-volume gate behaves as Juan expected on the named control: **BOOM is
rejected** because its opening price spike did not come with a volume increase
versus its own preceding bar, and its later volume increase did not make a new
AH high. CRE, IOTR, and DCX also fail to produce a qualifying local-volume
new-high ignition. YIBO and EGG ignite but fail continuation. ONMD is the second-
bar rule's only fade false positive; waiting for the third bar rejects it. The
third-bar rule admits AMIX at $4.61, NUWE at $2.40, and KUST at $1.54; their
next-morning SIP-open returns are -9.5%, +65.8%, and +33.8% respectively.

**Decision:** the third-bar local-volume gate is a promising **selection**
signal, but this replay does **not** justify adding 5-minute trading pulses. On
these cases, waiting for confirmation buys 6.1% worse on average than the first
currently legal scheduled-grid price; the gain comes from rejecting fades, not
from cadence. The sample is small and hand-labelled, PM-open returns omit spread,
and the replay assumes the ticker is already discoverable. Next step: add the
third-bar verdict as a log-only scanner column and collect out-of-sample results
before considering an entry gate or schedule change.

## First live third-bar outcomes (2026-08-03 AH -> 2026-08-04 PM)

The first instrumented AH session produced one `YES` and four `NO` candidates
with a recorded next-PM outcome. These are observations, not an entry test: no
orders, grades, rankings, or schedules used the verdict.

| Ticker | CONFIRM-3 | Reference price | Next-PM high | Return | Outcome |
|--------|-----------|-----------------|--------------|--------|---------|
| JELD | YES, confirmed 16:40 ET | $1.76 confirmed close | $1.71 | -2.8% | PM fell short; stale-book / volume-fade skip was prudent |
| ABTS | NO | ~$1.16 first sighting | $1.05 | -9.5% | early spike-fade |
| IPW | NO | ~$0.58 latest liquid AH level | $0.72 | +24.1% | bounced in PM but remained below ~$0.90 AH peak |
| BRCC | NO | $1.15 | $1.15 | 0.0% | thin, no AH book |
| CSAI | NO | $4.05 hypothetical watch | $3.93 | -3.0% | thin dead-cat override watch |

**Reading:** the one live `YES` did not continue, while three of four recorded
`NO` rows failed outright. IPW is a non-winner exception, not a clean false
negative: its PM bounce stayed below its AH peak. The sample is far too small to
change selection or cadence. Keep collecting distinct candidate outcomes.

## Second live third-bar outcomes (2026-08-04 AH -> 2026-08-05 PM)

Re-ran the instrument against the final AH bars, then measured the next-PM SIP high from each verdict's confirmed close (or final liquid AH level for `NO`). These remain observations only: none was entered, and stale books / broker blocks still independently prevented several fills.

| Ticker | CONFIRM-3 | Reference price | Next-PM SIP high | Return | Outcome |
|--------|-----------|-----------------|------------------|--------|---------|
| INLF | YES, confirmed 16:15 ET | $4.50 | $5.05 | +12.2% | PM opening pop, then faded; no fillable AH ask |
| BJDX | YES, confirmed 16:45 ET | $1.24 | $1.78 | +43.5% | liquid PM re-explosion after the AH fade |
| BANL | YES, confirmed 17:10 ET | $5.68 | $4.55 | -19.9% | fade; broker-blocked |
| ZJYL | YES, confirmed 17:50 ET | $3.46 | $3.49 | +0.9% | flat before fading; broker-blocked |
| TRUG | NO | $0.82 final liquid AH level | $0.82 | 0.0% | illiquid flatline |

**Reading:** Across the two live sessions, `YES` is now 5 rows: two meaningful positive PM excursions (INLF +12.2%, BJDX +43.5%), one near-flat result (+0.9%), and two losses (JELD -2.8%, BANL -19.9%). `NO` is five rows: three outright failures, one flatline, and IPW's +24.1% bounce that remained below its AH peak. This is not a tradable sample: the positive `YES` rows include a stale/unfillable book (INLF) and a later fade pattern (BJDX), returns are peak ceilings rather than executable exits, and no spread is charged. It does show the first live `YES` was not representative, so keep the column log-only and collect more outcomes rather than change cadence or selection.

## Third live third-bar outcomes (2026-08-05 AH -> 2026-08-06 PM)

Re-ran the instrument on the 08-05 AH candidates and measured each verdict's
next-PM SIP high (04:00-09:30 ET window, high-trade bars only). `YES` reference
is the confirmed close; `NO` reference is the actionable AH fill/level. Still
observations only: CLRO could not be filled (no AH ask), and CELZ/PAVS were held
from 08-05 and exited early at the 10:30 CET pulse, before their PM spikes.

| Ticker | CONFIRM-3 | Reference price | Next-PM SIP high | Return | Outcome |
|--------|-----------|-----------------|------------------|--------|---------|
| CLRO | YES, confirmed 17:35 ET | $5.30 | $13.13 | +147.7% | huge PM re-explosion; **Alpaca had no fillable AH ask** |
| RECT | YES, confirmed 16:35 ET | $1.45 | $1.36 | -6.2% | faded below close in AH, never recovered |
| CELZ | NO | $0.89 AH fill | $1.37 | +53.9% | held from 08-05, PM spike at 14:00 CET after our 10:30 exit |
| PAVS | NO | $6.61 AH fill | $12.10 | +83.1% | held from 08-05, PM spike at 12:55 CET after our 10:30 exit |

**Reading:** this is the first live session where the gate's separation clearly
**breaks down**. One `YES` was a monster (CLRO +147.7%) but unfillable; the other
`YES` (RECT) died. Both `NO` names (PAVS +83.1%, CELZ +53.9%) had large next-PM
excursions — the gate would have *rejected* the day's two biggest PM movers as a
selection filter. Combined live `YES` (n=7) is now +12.2, +43.5, +147.7, +0.9,
-2.8, -6.2, -19.9 (mean +25.1% but CLRO-outlier-driven, median +0.9%); `NO`
(n=7) now includes two >50% PM runs. **Emerging conclusion:** across three
out-of-sample sessions the third-bar gate does *not* cleanly separate next-PM
winners from fades, and the recurring bottleneck is **execution, not selection** —
the biggest edges (CLRO, INLF, BANL, ZJYL) were unfillable or broker-blocked, and
CELZ/PAVS ran only after we had already exited. Keep the column log-only; the
selection-gate hypothesis is weakening while the fill/exit-timing problem looks
like the larger money-fast lever.
