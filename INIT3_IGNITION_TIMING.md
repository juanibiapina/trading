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
