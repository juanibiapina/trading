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
