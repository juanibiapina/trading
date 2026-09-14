# Post-Market Screening - 2026-09-14

## Scan 21:30 CET (3:30 PM ET) — REGULAR SESSION (pre-AH watch)

This scan ran during the regular session (15:30 ET, 30 min before close), before after-hours opens at 16:00 ET / 22:00 CET. **No paper trades** per the regular-session caution rule. Candidates below are flagged watch-pending-AH; only names that reappear in AH scans (22:00+ CET) with sustained momentum become entry candidates.

Scanner returned 32 regular-session hits. Filtering out volume-collapse artifacts (`VChg% -99%` = 5m volume far below average, i.e. thin end-of-day prints, not building momentum) and stale/bad-print outliers (BURU +1825.7% on 100 shares — data artifact).

### Watch candidates (small float, live volume, Day% >15%)

| Ticker | Price | Day% | 5mVol | AvgVol | IRVol | Float | MCap | Industry | Note |
|--------|-------|------|-------|--------|-------|-------|------|----------|------|
| VANAF  | $0.75 | +29.3% | 10K | 7K | 11.7 | 5.6M | $12.6M | Financial Conglomerates | Live vol, small float |
| AIXC   | $1.16 | +28.8% | 13K | 36K | 12.9 | 7.1M | $24.4M | Packaged Software | Live vol |
| VSME   | $1.36 | +27.1% | 32K | 44K | 854.1 | 2.6M | $3.8M | Advertising/Marketing | Highest IRVol, tiny float |
| HMR    | $1.75 | +22.7% | 6K | 15K | 10.6 | 6.0M | $103.5M | Oil & Gas Pipelines | Small float |
| MYSE   | $3.10 | +16.3% | 2K | 7K | 4.1 | 4.9M | $15.9M | Packaged Software | Thin |
| PMI    | $6.14 | +15.2% | 200 | 1K | 0.7 | 1.4M | $14.4M | Medical Specialties | Very thin |

### Fading / artifact (excluded from watch)

- **BURU +1825.7%** — 100 shares in 5min, IRVol 0.0. Data artifact / reverse-split print, not a real move.
- **FTFT +187.5%, BMGL +61.4%, VNCE +45.6%, VEEA +34.6%, LHSW +31.9%** — all `VChg% -97% to -99.9%`: volume collapsed into the close. Spike-and-fade end-of-day prints, not building. Watch only if they reappear in AH with real accumulating volume.
- Financial Conglomerates cluster near $9.9–10.0 (IDAC, FWAC, WENC, MYX, TVIV) — flat/near-$10 SPAC-like names, no momentum move.

**Next scan: 22:00 CET (16:00 ET) — AH opens.** Re-check whether any watch name carries into after-hours with real SIP volume. Entries only begin at the 23:00 CET scan per learning-phase rules.

## Scan 22:00 CET (4:00 PM ET) — AH OPEN, observation only

Scanner returned **0 AH hits** — it ran at 16:00:21 ET, ~20 seconds after after-hours opened, before any AH volume had accumulated. Observation-only scan per learning-phase rules (no entries before the 23:00 CET scan).

**Watch-candidate AH book check (21:30 regular-session names):**

| Ticker | AH Quote (16:00 ET) | Read |
|--------|---------------------|------|
| VANAF  | no quote (404) | Not tradable on Alpaca — likely OTC/foreign line. Drop. |
| AIXC   | bid $0.95 x100 / ask $1.20 x500 | Wide spread, closing snapshot only, no AH prints yet |
| VSME   | bid $1.12 x100 / ask $0.00 x0 | No ask book — no fillable AH liquidity |
| HMR    | bid $1.49 x100 / ask $2.08 x100 | Very wide spread, closing snapshot, no AH prints |

No candidate shows a real accumulating AH book this early. Nothing to instrument (no name >10% AH change with live AH volume yet). Next scan 22:30 CET (4:30 PM ET) — re-check whether any 21:30 watch name carries into AH with real SIP volume; entries only begin at the 23:00 CET scan.

## Scan 22:15 CET (4:15 PM ET) — AH OPEN, observation only

Scanner returned **0 AH hits** (ran 16:15:17 ET). Still early in after-hours; scanner sees no name clearing the AH threshold. Observation-only per learning-phase rules (no entries before the 23:00 CET scan).

**Watch-candidate SIP + book check (tracked 21:30 names):** AH-start `2026-09-14T20:00:00Z` (EDT).

| Ticker | Close | AH 1st-bar (16:00 ET) | AH Chg | Quote (16:00 ET) | Read |
|--------|-------|-----------------------|--------|------------------|------|
| AIXC   | $1.16 | C $1.15, 16.3K sh, 85 tr | −0.9% | bid $0.95 x100 / ask $1.20 x500 | Flat, wide spread, no build |
| VSME   | $1.36 | C $1.33, 33.7K sh, 85 tr | −2.2% | bid $1.12 x100 / ask $0.00 x0 | No ask book — no fillable AH liquidity |
| HMR    | $1.75 | C $1.71, 4.8K sh, 24 tr | −2.3% | bid $1.49 x100 / ask $2.08 x100 | Thin, very wide spread |
| MYSE   | $3.10 | C $3.08, 2.9K sh, 4 tr | −0.6% | bid $2.63 x100 / ask $3.53 x100 | 4 trades — dead |
| PMI    | $6.14 | C $6.15, 4.9K sh, 22 tr | +0.2% | bid $5.36 x100 / ask $7.13 x100 | Thin, wide spread |

Every tracked name is flat-to-slightly-down vs its regular close on thin, single-bar volume — no candidate carried its regular-session move into after-hours with real accumulating SIP volume. No name >10% AH change, so no spike-bar / CONFIRM-3 instrumentation applies. **No entries** (also pre-23:00 CET). Next scan 22:30 CET (4:30 PM ET) — re-check whether any name ignites in AH with real SIP volume; entries begin at the 23:00 CET scan.

## Scan 22:30 CET (4:30 PM ET) — AH OPEN, observation only

Scanner returned **2 AH hits** (ran 16:30:25 ET). Observation-only per learning-phase rules (no entries before the 23:00 CET scan).

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| HCAI | [TV](https://www.tradingview.com/chart/?symbol=HCAI) | $1.85 | -17.2% | +22.9% | $2.28 | +1.8% | 323K | 393K | 0.8x | 7.3M | Industrial Machinery |
| HITI | [TV](https://www.tradingview.com/chart/?symbol=HITI) | $2.63 | +4.0% | +5.3% | $2.77 | +9.5% | 725K | 726K | 1.0x | 76.6M | Specialty Stores |

### Evaluation

**HITI — not a candidate.** AH change +5.3% is below the 10% threshold. Large float (76.6M), VRatio 1.0x (no unusual AH volume). Quote `bid $2.63 x100 / ask $0.00 x0` — no fillable ask book. Skip.

**HCAI — dead-cat bounce + first-bar spike→fade, skip.** Only >10% AH mover, so instrumented:
- `SPIKE 16:05ET +26% $2.33 48 trades / 3k sh (first co-spike bar) (as-of 16:30ET)`
- `CONFIRM-3 NO ignition 16:05ET failed third-bar hold/volume as-of 16:30ET`
- SIP bars (real volume, not a bad print, but **fading**): 16:05 ET 218K sh / 2,264 tr H $2.60 vwap $2.33 → 16:10 ET 185K sh / 1,772 tr H $2.38 vwap $2.28 → 16:15 ET 123K sh / 964 tr H $2.32 vwap $2.23. Peak in the first bar, declining volume and highs since.
- Quote `bid $1.48 x100 / ask $2.18 x100` (16:00 ET snapshot, wide spread).

  **Why skip (three converging skip signals):**
  1. **Dead-cat bounce** — Day% -17.2% (crashed >15% in regular session), bouncing in AH. Recovering from a sell-off, not building new momentum.
  2. **First-bar spike→fade** — AH high $2.60 printed in the first 15-min AH window (16:05 ET), CONFIRM-3 NO, volume/highs declining every bar since. Single-bar pop, not a build.
  3. **Repeat fader** — HCAI one-bar PM pop Sep 9→10 ($5.32 → faded $4.73) is in the plan's FIRST-BAR-SPIKE 0/3 dataset.

  **Dead-cat-override check:** Does NOT qualify. The override requires AH% *rising* across ≥2 AH scans while reclaiming above the regular close. HCAI is on its first AH appearance and is *fading* within AH (peak 16:05, declining since), not building. No override watch warranted.

No entry (also pre-23:00 CET). Next scan 23:00 CET (5:00 PM ET) — entries begin. Re-check whether any fresh name ignites with real accumulating SIP volume and a BUILD pattern; HCAI's fade trajectory makes continuation unlikely, but re-verify if it reappears building.

## Scan 22:45 CET (4:45 PM ET) — AH OPEN, observation only

Scanner returned **4 AH hits** (ran 16:45:19 ET). Observation-only per learning-phase rules (no entries before the 23:00 CET scan).

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| HCAI | [TV](https://www.tradingview.com/chart/?symbol=HCAI) | $1.85 | -17.2% | +19.2% | $2.21 | -1.3% | 588K | 425K | 1.4x | 7.3M | Industrial Machinery |
| AIXC | [TV](https://www.tradingview.com/chart/?symbol=AIXC) | $1.19 | +32.7% | +5.0% | $1.25 | +39.4% | 192K | 521K | 0.4x | 7.1M | Packaged Software |
| XPON | [TV](https://www.tradingview.com/chart/?symbol=XPON) | $4.59 | -9.5% | +10.0% | $5.05 | -0.4% | 132K | 162K | 0.8x | 680K | Electrical Products |
| VSME | [TV](https://www.tradingview.com/chart/?symbol=VSME) | $1.30 | +21.5% | +5.4% | $1.37 | +28.0% | 79K | 2.8M | 0.0x | 2.6M | Advertising/Marketing |

### Evaluation

**AIXC / VSME — below threshold, watch only.** Both AH change <10% (AIXC +5.0%, VSME +5.4%). VRatio near zero (AIXC 0.4x, VSME 0.0x) — no unusual accumulating AH volume. Their Total% (AIXC +39.4%, VSME +28.0%) is regular-session gain carried in, not an AH build. Not candidates.

**XPON — new, tiny float, but SPIKE→FADE with no catalyst. Skip.** Float 680K (ideal), `tradable=true`. Only the second name >10% AH change, so instrumented:
- `NO-SPIKE peak +22% @16:24ET (no bar cleared +15% on a volume co-spike) (as-of 16:45ET)`
- `CONFIRM-3 NO ignition 16:20ET failed third-bar hold/volume as-of 16:45ET`
- SIP bars (real volume, not a bad print, but **fading**): 16:20 ET 53K sh / 1,154 tr H $5.61 vwap $5.29 → 16:25 ET 129K sh / 2,084 tr H $5.35 vwap $5.14 → 16:30 ET 38K sh / 590 tr H $5.10 C $4.80 vwap $4.92. Ignited 16:20, peaked ~$5.61 @16:24, declining price and volume since.
- Quote `bid $3.98 x100 / ask $5.64 x100` — very wide spread; ask $5.64 is stale near the peak while SIP has faded to $4.80.
- **Catalyst search (4 calls budget, 2 used):** no same-day catalyst found. Most recent items are stale — Aug 24 definitive agreement (potential $91M investments), June RV/OEM news, an oil & gas exploration acquisition. Nothing dated Sep 14.

  **Why skip:** SPIKE→FADE (peaked 16:24 ET, fading since) — 0/10+ for PM continuation regardless of float/catalyst. Day% -9.5% (down day). First AH appearance, so fails the 2-AH-scan gate. No same-day catalyst. Illiquid wide book. Observation-only anyway (pre-23:00 CET).

**HCAI — dead-cat + first-bar spike→fade, skip (carried from 22:30).** Now on its second >10% AH scan (+22.9% at 22:30 → +19.2% now), AH Vol up to 588K / VRatio 1.4x, but still fading:
- `SPIKE 16:05ET +26% $2.33 48 trades / 3k sh (first co-spike bar) (as-of 16:45ET)`
- `CONFIRM-3 NO ignition 16:05ET failed third-bar hold/volume as-of 16:45ET`
- SIP bars: 16:05 ET 218K sh / 2,264 tr H $2.60 → 16:10 H $2.38 → 16:15 H $2.32 → 16:20 H $2.40 → 16:25 H $2.31 → 16:30 H $2.26 C $2.23. AH high $2.60 in the first bar, declining highs and volume (218K→21K) every bar since.
- Quote `bid $1.48 x100 / ask $2.18 x100` (wide spread).
- **Catalyst search:** no same-day HCAI-specific catalyst found (results were generic HCA Healthcare AI items).

  **Why skip (three converging signals):** (1) **Dead-cat bounce** — Day% -17.2%, bouncing in AH, not building new momentum; (2) **First-bar spike→fade** — AH high $2.60 printed in the first AH bar (16:05 ET), CONFIRM-3 NO every scan, volume/highs declining since; (3) **Repeat fader** — HCAI's one-bar PM pop Sep 9→10 ($5.32 → $4.73) is already in the plan's FIRST-BAR-SPIKE 0/3 dataset.

  **Dead-cat-override check:** Does NOT qualify — AH% is *falling* across scans (+22.9% → +19.2%) and price sits below the regular close context; the override requires a *rising* AH% reclaim above the regular close.

  **FIRST-BAR-SPIKE WATCH (data collection):** AH high $2.60 @16:05 ET (first AH bar), CONFIRM-3 NO across both scans, current $2.21 sits within ~15% of that high. Recording hypothetical entry **$2.21 @ 16:45 ET (22:45 CET)** for the morning-eval tracker to measure whether the first-bar-spike skip was correct (overlaps the dead-cat skip).

**No entries** — observation-only (pre-23:00 CET), and no candidate shows a BUILD pattern (HCAI and XPON both spike→fade). Next scan 23:00 CET (5:00 PM ET) — entries begin. Re-check whether any fresh name ignites with real accumulating SIP volume and a BUILD-and-hold pattern.

## Scan 23:00 CET (5:00 PM ET) — AH OPEN, entries begin

Scanner returned **2 AH hits** (ran 17:00:26 ET). Entries are allowed from this scan per learning-phase rules.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| VEEA | [TV](https://www.tradingview.com/chart/?symbol=VEEA) | $2.29 | +46.8% | +14.5% | $2.62 | +68.0% | 976K | 654K | 1.5x | 1.6M | Packaged Software |
| HCAI | [TV](https://www.tradingview.com/chart/?symbol=HCAI) | $1.85 | -17.2% | +18.1% | $2.19 | -2.2% | 638K | 431K | 1.5x | 7.3M | Industrial Machinery |

### Evaluation

**VEEA — genuine BUILD with Grade-A catalyst, but blocked by the 2-AH-scan gate (first AH appearance). GATE-PENDING for 23:30, no entry at 23:00.**

Instrumentation:
- `SPIKE 16:42ET +17% $2.67 1070 trades / 204k sh (first co-spike bar) (as-of 17:00ET)` — real price+volume co-spike ignition.
- `CONFIRM-3 PENDING ignition 16:40ET; waiting for third bar as-of 17:00ET`
- SIP bars (real accumulating volume, not a bad print): flat base 16:00–16:35 ET ($2.18–2.32, 9–86K sh/bar), then ignition — **16:40 ET 892,666 sh / 5,880 tr H $2.74 vwap $2.56 → 16:45 ET 1,121,423 sh / 8,921 tr H $2.80 vwap $2.65 C $2.75**. Nearly 1M+ sh and thousands of trades per bar = real book, still building at scan time.
- Quote `bid $2.81 x100 / ask $2.85 x100` (17:00 ET) — real two-sided fillable book, tight 4¢ spread. `tradable=true`.
- **Catalyst (Grade A):** Veea + NovaGen **potential merger** to launch an Edge AI-powered Global Health Platform, with a **US$10M investment commitment from GeoNova Capital** (GlobeNewswire, Sep 14, ~16:40 ET — dropped exactly at the ignition bar). Term-sheet/potential merger + fresh capital + new platform → momentum-gradable (NOT a definitive fixed-price cash deal, so the merger-arb→D exclusion does not apply). This can still re-rate. Grade **A**.

  **Why no entry at 23:00:** VEEA fails the **2-AH-scan gate** — this is its *first* AH scan >10% (it ignited at 16:40 ET, ~1 min after the 22:45 CET scan window, so it did not appear in any of the 22:00/22:15/22:30/22:45 scans). The gate requires AH change >10% in ≥2 after-hours scans. Every *other* gate passes: float 1.6M (ideal), Day% +46.8% (>−15%), Total% +68.0% (well under the +150% ceiling), real accumulating SIP volume, fillable book, tradable, Grade-A catalyst, BUILD-and-hold pattern (price $2.75→$2.83 rising, not fading). This is a fresh day-1 igniter that just needs one more AH scan.

  **GATE-PENDING (real pending entry, not a hypothetical watch):** If VEEA still shows >10% AH change at the 23:30 CET scan, it clears the 2-AH-scan gate and should be **entered** (assuming Total% still under +150% and the book still fillable). This is not the final scan (00:30), so the FINAL-SCAN-GATE-BLOCK instrumentation does not apply — the gate legitimately stands and VEEA has 3 more scans (23:30/00:00/00:30) to confirm. Multi-session check: VEEA spiked intraday too (Day% +46.8%), but its AH ignition is a fresh same-day catalyst move, not a prior-session runner (not in WINNERS_TRACKING as a prior entry) — treat as day-1 igniter.

**HCAI — dead-cat + first-bar spike→fade, now breaking down. Skip (carried, 3rd AH scan).**
- `SPIKE 16:05ET +26% $2.33 48 trades / 3k sh (first co-spike bar) (as-of 17:00ET)`
- `CONFIRM-3 NO ignition 16:05ET failed third-bar hold/volume as-of 17:00ET`
- SIP bars now show a clear breakdown: peak $2.60 in the first bar (16:05 ET, 218K sh), declining highs and volume every bar since, and the **16:45 ET bar collapsed to C $1.90 (L $1.90), vol 48K** — now trading *below* its regular close $1.85 context and far below the AH high. The dead-cat bounce is rolling over.
- Quote `bid $1.48 x100 / ask $2.18 x100` (stale 16:00 snapshot, wide spread).

  **Why skip (three converging signals, all now confirmed by the fade):** (1) **Dead-cat bounce** — Day% −17.2%, bouncing then rolling over; (2) **First-bar spike→fade** — AH high $2.60 in the first AH bar (16:05 ET), CONFIRM-3 NO all three scans, now broken down to $1.90; (3) **Repeat fader** — HCAI's one-bar PM pop Sep 9→10 ($5.32 → $4.73) is already in the plan's FIRST-BAR-SPIKE 0/3 dataset. **Dead-cat-override check:** does NOT qualify — AH% is falling across scans (+22.9% → +19.2% → +18.1%) and price has now dropped below the regular close, the opposite of a rising reclaim.

  **FIRST-BAR-SPIKE WATCH update:** hypothetical entry recorded $2.21 @ 16:45 ET (22:45 CET) is now $1.90 (−14%) — the first-bar-spike skip is tracking correct so far. Continue recording for the morning-eval tracker.

**No entries at 23:00.** VEEA is a strong GATE-PENDING candidate (enter at 23:30 if it holds >10% AH); HCAI is a confirmed dead-cat/first-bar-spike fade. Next scan **23:30 CET (5:30 PM ET)** — priority: re-check VEEA for the second AH scan to clear the gate; watch for any fresh igniter with accumulating SIP volume.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
