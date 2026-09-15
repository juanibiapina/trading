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

## Scan 23:30 CET (5:30 PM ET) — AH OPEN, entries allowed

Scanner returned **2 AH hits** (ran 17:30:22 ET). Entries allowed per learning-phase rules.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| VEEA | [TV](https://www.tradingview.com/chart/?symbol=VEEA) | $2.29 | +46.8% | +34.1% | $3.07 | +96.8% | 6.9M | 1.3M | 5.1x | 1.6M | Packaged Software |
| HCAI | [TV](https://www.tradingview.com/chart/?symbol=HCAI) | $1.85 | -17.2% | +6.2% | $1.97 | -12.1% | 736K | 443K | 1.7x | 7.3M | Industrial Machinery |

### Evaluation

**VEEA — ENTERED. Grade-A catalyst + real accumulating AH BUILD, cleared the 2-AH-scan gate.**

Instrumentation (AH change +34.1% >10%):
- `SPIKE 16:42ET +17% $2.67 1070 trades / 204k sh (first co-spike bar) (as-of 17:30ET)` — real price+volume co-spike ignition.
- `CONFIRM-3 YES ignition 16:40ET 67.3x; confirmed 16:50ET $2.77 as-of 17:30ET`
- SIP bars (real accumulating volume, not a bad print): flat base 16:00–16:35 ET ($2.18–2.31, 9–86K sh/bar), then **ignition 16:40 ET 892,666 sh / 5,880 tr H $2.74 → 16:45 ET 1,121,423 sh / 8,921 tr H $2.80 → 16:50 ET 1,013,103 sh / 7,039 tr H $2.83 → 16:55 ET 860,979 sh / 6,077 tr H $2.88 → 17:00 ET 1,404,644 sh / 9,819 tr H $3.08 → 17:05 ET 1,482,837 sh / 10,743 tr H $3.29 → 17:10 ET 905,178 sh / 6,981 tr → 17:15 ET 1,314,470 sh / 10,027 tr H $3.38 C $3.31**. 1M+ sh and thousands of trades per bar, still making new highs at scan time — textbook BUILD-and-still-rising.
- Quote frozen at 16:59:47 ET (bid $2.81 / ask $2.85) — free-tier book lag ~30 min; real-time SIP ~$3.31–3.38. `tradable=true`.
- **Catalyst (Grade A):** Veea + NovaGen **potential merger** term sheet to launch an Edge AI-powered Global Health Platform, with a **US$10M investment commitment from GeoNova Capital** (GlobeNewswire, Sep 14 ~16:40 ET — dropped exactly at the ignition bar; StockTitan/Manila Times/GlobeNewswire, 50 min old at scan). Potential/term-sheet merger + fresh capital + new platform → momentum-gradable (NOT a definitive fixed-price cash deal, so the merger-arb→D exclusion does not apply). Can still re-rate. Grade **A**.

  **Gates (all pass):** float 1.6M (ideal <10M); AH >10% in ≥2 AH scans (23:00 +14.5% → 23:30 +34.1%, gate cleared); Day% +46.8% (>−15%); Total% +96.8% (under +150% ceiling — prior close $1.56, ceiling $3.90); real accumulating SIP volume; fillable book; tradable=true; Grade-A catalyst; BUILD-and-still-rising (not fading from a peak).

  **Multi-session-runner check:** fresh day-1 igniter — not in WINNERS_TRACKING as a prior entry; prior daily close $1.56 with no multi-session run-up. Today's move is $1.56 → $2.29 regular close (Day% +46.8%) → AH ignition on a same-day catalyst. Tagged **FRESH DAY-1 IGNITER**.

  **Order:** BUY 28 @ limit $3.45 ext (id `dad1e466`) → **filled @ $3.38**. QTY = floor($100 / ~$3.45) = 28.

  **CHASE-CAP (log-only):** qualifying scan (23:30, gate-clearing) AH price $3.07 / Total% +96.8%; actual fill $3.38 / Entry Total% +116.7% (prior close $1.56); **chase gap +19.9%**. The limit was set to the real-time SIP level (~$3.35–3.40, not the stale $2.85 quote) because the free-tier book lagged ~30 min; the fill landed just below the ~+120% extreme-runner fade zone but under the +150% ceiling. Instrumentation for the morning-eval tracker — did not change the entry decision.

**HCAI — dead-cat + first-bar spike→fade, faded below threshold. Skip (carried, 4th AH scan).** AH Chg now +6.2% (below the 10% threshold), Total% −12.1% (below prior close). SIP tail confirms the roll-over: 16:50 ET C $2.04 → 17:00 ET C $1.99 → 17:15 ET C $1.97 on collapsing volume (26K → 2K sh/bar, 281 → 29 tr). No instrumentation this scan (AH change <10%). Three converging skip signals stand and are now fully confirmed by the fade: (1) dead-cat bounce (Day% −17.2%), (2) first-bar spike→fade (AH high $2.60 @16:05 ET, CONFIRM-3 NO every scan), (3) repeat fader (Sep 9→10 one-bar PM pop in the FIRST-BAR-SPIKE 0/3 dataset). Dead-cat-override does NOT qualify — AH% fell every scan (+22.9% → +19.2% → +18.1% → +6.2%). **FIRST-BAR-SPIKE WATCH update:** hypothetical entry $2.21 @ 16:45 ET is now $1.97 (−11%) — skip tracking correct.

**Entered VEEA (Grade A, real BUILD).** HCAI is a confirmed dead-cat/first-bar-spike fade. Next scan **00:00 CET (6:00 PM ET)** — monitor VEEA's overnight trajectory; watch for any fresh late igniter with accumulating SIP volume and a second AH scan to clear the gate.

## Scan 00:00 CET (6:00 PM ET) — AH OPEN, entries allowed

Scanner returned **4 AH hits** (ran 18:00:37 ET). Entries allowed per learning-phase rules.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| VEEA | [TV](https://www.tradingview.com/chart/?symbol=VEEA) | $2.29 | +46.8% | +59.8% | $3.66 | +134.6% | 11.6M | 1.9M | 6.1x | 1.6M | Packaged Software |
| HCAI | [TV](https://www.tradingview.com/chart/?symbol=HCAI) | $1.85 | -17.2% | +7.3% | $1.99 | -11.2% | 753K | 445K | 1.7x | 7.3M | Industrial Machinery |
| BOXL | [TV](https://www.tradingview.com/chart/?symbol=BOXL) | $5.43 | -4.6% | +7.7% | $5.85 | +2.8% | 205K | 60K | 3.4x | 565K | Computer Peripherals |
| XPON | [TV](https://www.tradingview.com/chart/?symbol=XPON) | $4.59 | -9.5% | +6.3% | $4.88 | -3.7% | 198K | 171K | 1.2x | 680K | Electrical Products |

### Evaluation

**VEEA — OPEN POSITION, still building strongly. No re-entry (one entry per candidate per night).** Entered 23:30 CET @ $3.38; Alpaca now shows **$3.94, P&L +16.6%**.

Instrumentation (AH change +59.8% >10%):
- `SPIKE 16:42ET +17% $2.67 1070 trades / 204k sh (first co-spike bar) (as-of 18:00ET)`
- `CONFIRM-3 YES ignition 16:40ET 67.3x; confirmed 16:50ET $2.77 as-of 18:00ET`
- SIP bars confirm the BUILD is still running, not fading: 17:15 ET 1,314K sh / 10,027 tr H $3.38 → 17:20 ET 851K sh / 7,149 tr H $3.40 → 17:25 ET 548K sh / 4,206 tr H $3.36 → 17:30 ET 917K sh / 7,260 tr H $3.50 → **17:35 ET 1,278K sh / 10,520 tr H $3.83 C $3.80 vwap $3.66** — still making new AH highs on 1M+ sh / 10K+ trades per bar. Textbook continued BUILD.
- Total% now +134.6% (from prior close $1.56), just under the +150% ceiling. Position is up; the entry thesis (Grade-A catalyst + real accumulating BUILD) is playing out. Position management (hold/exit) is handled by the premarket `position-evaluation.md` run, not here.

**HCAI — dead-cat + first-bar spike→fade, faded below threshold. Skip (carried, 5th AH scan).** AH Chg +7.3% (below the 10% threshold), Total% −11.2% (below prior close). SIP continues to confirm the roll-over from the first-bar peak $2.60 @16:05 ET. No instrumentation this scan (AH change <10%). Three converging skip signals stand (dead-cat bounce Day% −17.2%; first-bar spike→fade, CONFIRM-3 NO every scan; repeat fader Sep 9→10). Dead-cat-override does NOT qualify — AH% fell every scan (+22.9% → +19.2% → +18.1% → +6.2% → +7.3%). **FIRST-BAR-SPIKE WATCH update:** hypothetical entry $2.21 @ 16:45 ET is now $1.99 (−10%) — skip tracking correct.

**BOXL — new, below threshold + no AH book. Skip.** AH change +7.7% (below the 10% threshold). Float 565K (ideal) and VRatio 3.4x, but quote `bid $4.66 x100 / ask $0.00 x0` — **no fillable ask book** (illiquid, no AH liquidity). Day% −4.6% (mild down day), Total% only +2.8%. Not a candidate: sub-threshold AH move on an illiquid book. No instrumentation (AH change <10%).

**XPON — carried, still SPIKE→FADE below threshold. Skip.** AH change +6.3% (below threshold, down from +10.0% at 22:45), Total% −3.7%, Day% −9.5%. Quote `bid $3.98 x100 / ask $5.64 x100` — same wide/stale book as earlier. Faded further from its 16:24 ET peak; no catalyst found in prior scan. Not a candidate.

**No new entries at 00:00.** VEEA (open position) is building strongly toward the ceiling; no other name clears the 10% AH threshold. Next scan **00:30 CET (6:30 PM ET) — final scheduled scan.** Priorities: apply the final-scan feed-lag cross-check to tracked pipeline names (VEEA, HCAI, XPON, BOXL, plus 21:30 watch names) against SIP; watch for any late igniter (FINAL-SCAN-GATE-BLOCK instrumentation if one ignites too late for a second AH scan).

## Scan 00:30 CET (6:30 PM ET) — AH OPEN, FINAL scheduled scan

Scanner returned **5 AH hits** (ran 18:30:24 ET). Entries allowed per learning-phase rules. This is the last scheduled scan of the night.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| VEEA | [TV](https://www.tradingview.com/chart/?symbol=VEEA) | $2.29 | +46.8% | +64.6% | $3.77 | +141.7% | 16.0M | 2.4M | 6.6x | 1.6M | Packaged Software |
| HCAI | [TV](https://www.tradingview.com/chart/?symbol=HCAI) | $1.85 | -17.2% | +14.3% | $2.12 | -5.4% | 777K | 448K | 1.7x | 7.3M | Industrial Machinery |
| XPON | [TV](https://www.tradingview.com/chart/?symbol=XPON) | $4.59 | -9.5% | +14.2% | $5.24 | +3.4% | 336K | 191K | 1.8x | 680K | Electrical Products |
| BOXL | [TV](https://www.tradingview.com/chart/?symbol=BOXL) | $5.43 | -4.6% | +6.8% | $5.80 | +1.9% | 243K | 64K | 3.8x | 565K | Computer Peripherals |
| MITQ | [TV](https://www.tradingview.com/chart/?symbol=MITQ) | $0.64 | +6.7% | +9.3% | $0.70 | +16.6% | 220K | 99K | 2.2x | 6.6M | Electronics/Appliances |

### Evaluation

**VEEA — OPEN POSITION, still building strongly. No re-entry (one entry per candidate per night).** Entered 23:30 CET @ $3.38; Alpaca now shows **$3.82, P&L +13.0%**.

Instrumentation (AH change +64.6% >10%):
- `SPIKE 16:42ET +17% $2.67 1070 trades / 204k sh (first co-spike bar) (as-of 18:30ET)`
- `CONFIRM-3 YES ignition 16:40ET 67.3x; confirmed 16:50ET $2.77 as-of 18:30ET`
- Scanner AH Vol 16.0M / VRatio 6.6x — real accumulating book all night. Total% +141.7% (from prior close $1.56), still under the +150% ceiling. The entry thesis (Grade-A catalyst + real accumulating BUILD) is playing out; position up +13.0%. Hold/exit is handled by the premarket `position-evaluation.md` run, not here.

**HCAI — dead-cat + first-bar spike→fade, bounced back above threshold but still a faded spike. Skip (carried, 6th AH scan).** AH Chg back to +14.3% (from +7.3% at 00:00), price $2.12, but Total% still −5.4% (below prior close).
- `SPIKE 16:05ET +26% $2.33 48 trades / 3k sh (first co-spike bar) (as-of 18:30ET)`
- `CONFIRM-3 NO ignition 16:05ET failed third-bar hold/volume as-of 18:30ET`
- The bounce from $1.90 → $2.12 is a rebuild **>18% off the first-bar AH high $2.60** — per the plan's hold-vs-fade rule, a rebuild far below the AH high (>20% off) is a faded spike, not a hold. Three converging skip signals stand: (1) dead-cat bounce (Day% −17.2%); (2) first-bar spike→fade (AH high $2.60 @16:05 ET, CONFIRM-3 NO every scan); (3) repeat fader (Sep 9→10 one-bar PM pop in the FIRST-BAR-SPIKE 0/3 dataset). Dead-cat-override does NOT qualify — AH% has whipsawed (+22.9%→+19.2%→+18.1%→+6.2%→+7.3%→+14.3%), never a sustained rising reclaim above the regular close; Total% remains negative.
- **FIRST-BAR-SPIKE WATCH update:** hypothetical entry $2.21 @ 16:45 ET (22:45 CET) is now $2.12 (−4%) — the first-bar-spike skip is still tracking correct.

**XPON — clears the 2-AH-scan gate on paper, but it's a thin-drift second wave on a SPIKE→FADE first wave. Skip.** AH Chg +14.2% now, and it was +10.0% at 22:45 CET — so numerically it has 2 AH scans >10% (the gate). But the SIP tells the real story:
- `SPIKE 18:02ET +19% $5.48 153 trades / 10k sh (first co-spike bar) (as-of 18:30ET)`
- `CONFIRM-3 NO ignition 16:20ET failed third-bar hold/volume as-of 18:30ET`
- **Wave 1 (real volume, faded):** 16:20 ET 53K sh / 1,154 tr H $5.61 → 16:25 ET 129K sh / 2,084 tr H $5.35 → 16:30 ET 38K sh H $4.80, then bled to ~$4.40–4.70 for over an hour on thin prints.
- **Wave 2 (thin drift, NOT a build):** 17:40 ET 11.5K sh / 129 tr → 17:45 ET 11.8K sh / 152 tr → 17:50 ET 7.5K sh / 167 tr → 18:02 ET spike 10K sh / 153 tr. Price is climbing back toward the $5.61 first-wave high but on a **fraction of the volume** (tens-of-K sh, hundreds of trades per bar). Per the MODD thin-drift rule, a rising Total% on thin per-bar SIP volume is a thin drift, not a build — do NOT read the reclaim toward the high as a BUILD signal.
- Quote `bid $3.98 x100 / ask $5.64 x100` (stale 16:00 ET snapshot, very wide). Down day (Day% −9.5%), no same-day catalyst (searched at 22:45; only stale Aug 24 items). Skip: SPIKE→FADE first wave + thin-drift second wave, no catalyst, down day.

**MITQ — new, below threshold, thin late pop. Skip.** AH change +9.3% (below the 10% threshold). Float 6.6M, VRatio 2.2x, `tradable`-unknown, quote `bid $0.56 x100 / ask $0.79 x100` (stale, wide).
- `SPIKE 17:50ET +17% $0.75 63 trades / 6k sh (first co-spike bar) (as-of 18:30ET)` — thin.
- `CONFIRM-3 NO ignition 16:15ET failed third-bar hold/volume as-of 18:30ET`
- SIP: early AH churn 16:15–16:30 ET ($0.72–0.74 on 15–60K sh), faded to $0.65, then a late pop 18:10 ET H $0.81 (51.7K sh / 241 tr) already back to $0.74. A sub-threshold penny name ($0.70) with a thin late pop and CONFIRM-3 NO. First AH appearance → fails the 2-AH-scan gate. Not a candidate.

**BOXL — carried, below threshold, no AH book. Skip.** AH change +6.8% (below the 10% threshold), Total% +1.9%, Day% −4.6%. Prior scan showed `ask $0.00 x0` (no fillable AH liquidity). Not a candidate.

### Final-scan instrumentation

**FINAL-SCAN-GATE-BLOCK check — none.** No name clears every entry rule except the 2-AH-scan gate. The only fresh first-AH-appearance name is MITQ, but it is **below** the 10% AH threshold (+9.3%), CONFIRM-3 NO, and on thin volume (63 tr / 6k sh spike) — not a genuine volume-backed late igniter. No block to record.

**Final-scan feed-lag cross-check — no rescue needed.** Cross-checked tracked pipeline names against SIP: VEEA (real, in position, 1M+ sh/bar all night), HCAI (real but fading below close), XPON (real but thin second wave), MITQ (thin), BOXL (below threshold). The 21:30 regular-session watch names (AIXC, VSME, HMR, MYSE, PMI) never carried into AH with accumulating SIP volume (all flat/sub-threshold in earlier scans). TradingView is not under-reporting any tracked name above threshold on real volume — no SIP-truth rescue applies.

**No new entries at 00:30.** VEEA remains the sole entry of the night (Grade A, real BUILD, up +13.0%). Night complete — this was the final scheduled scan. HCAI/XPON/MITQ/BOXL are all fades or sub-threshold. VEEA position management moves to the premarket `position-evaluation.md` run.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
| VEEA | $3.38 | 2026-09-14 17:30 ET (23:30 CET) | 28 | dad1e466 | Grade A — Veea+NovaGen potential merger term sheet + GeoNova $10M investment (GlobeNewswire ~16:40 ET at ignition). Real accumulating AH BUILD (1M+ sh/bar, still new highs), cleared 2-AH-scan gate (+14.5%→+34.1%), float 1.6M, VRatio 5.1x, CONFIRM-3 YES 67.3x, Total% +96.8% under ceiling. Fresh day-1 igniter. |

## Morning Evaluation — 10:20 CET (Sep 15, evaluating Sep 14 AH session)

### Today's Winner

**No real winner today.** Nothing cleared the >100% winner bar measured from the correct previous close. Two genuine, volume-backed AH→PM movers both fell just short: **VEEA +89.5%** and **MYSZ +90.8%** (both from their true Monday closes). We entered VEEA — the biggest genuine mover — and it is holding a small gain.

**VEEA** (Veea Inc.) — Packaged Software / AI edge infrastructure — **the biggest genuine mover, DETECTED + ENTERED**
- Catalyst: **Grade A** — Veea + NovaGen **potential merger term sheet** to launch an Edge AI-powered Global Health Platform + a **US$10M investment commitment from GeoNova Capital** (GlobeNewswire, Sep 14 ~16:40 ET — dropped exactly at the ignition bar). Momentum-gradable (potential/term-sheet merger + fresh capital + new platform, not a fixed-price cash deal → no merger-arb→D exclusion).
- **Prev-close basis check (post-nothing, but stale-basis case):** Yahoo `previousClose` = $1.56 is a **stale one-session-old basis** (Friday Sep 11 close). The true last-session close is **Monday Sep 14 = $2.29** (VEEA ran +46.8% in Monday's regular session first). ANCHOR WARNING fired. The scanner/tooling `Total%` used the stale $1.56, inflating the headline to "+178%" at peak — **fictional over-statement**. Corrected from $2.29: AH peak +85.6%, PM peak +89.5%. **Below the +100% winner bar.**
- Previous Close (true, Monday Sep 14): **$2.29** (Yahoo $1.56 = stale Friday close)
- AH last night (SIP): BUILD from $2.26 (16:00 ET) → **$4.25 high at 19:50 ET** = +85.6% from $2.29, on massive accumulating volume (ignition 16:40 ET 892K sh, sustained 500K–1.5M sh/bar & thousands of trades/bar all night). Real book, no bad print (Yahoo AH high $4.25 matched SIP).
- Premarket now (SIP): PM open bar 04:00 ET **H $4.34** on 1.39M sh / 18,364 trades = **+89.5% from $2.29** (Yahoo under-reported the peak at $4.03). Currently ~$3.71.
- Hypothetical P&L (AH entry → PM peak): AH ignition ~$2.56 → PM peak $4.34 = **+69.5%** (we entered later at $3.38 → PM peak = +28.4%).
- SIP peak vs winner bar: $4.34 = **+89.5%** from the true close = **below +100%**.
- Float: 1.6M | Market Cap: ~$7.1M

**MYSZ** (My Size, Inc.) — Internet Software/Services — **comparable secondary mover, NOT DETECTED (feed-lag miss)**
- Catalyst: none same-day verified (AI fashion / body-measurement platform; ultra-low float squeeze).
- Previous Close: $1.73. AH (SIP): thin until an **18:25 ET ignition** (222K sh/1,857 tr → $2.40), AH SIP peak $2.52 (+45.7%) at 19:55 ET. PM (SIP): blast to **$3.30 at 04:05 ET on 1.68M sh / 18,619 trades = +90.8%**.
- MYSZ never appeared in any evening scan despite being >10% AH on 212K sh/bar at the 18:30 ET last scan → **in-window feed-lag miss** (see Notes). Hypo AH $2.25 → PM $3.30 = **+46.7%**.

**Scanner Diagnostic (VEEA, the biggest genuine mover):**
- Detectable at screening time? **YES — detected AND entered.**
- VEEA ignited at 16:40 ET (~1 min after the 22:45 CET scan), first surfaced at the **23:00 CET scan** (+14.5% AH, $2.62), cleared the 2-AH-scan gate at **23:30 CET** (+34.1%) → **ENTERED @ $3.38**. It kept building every scan (23:00 +14.5% → 23:30 +34.1% → 00:00 +59.8% → 00:30 +64.6% AH) on 1M+ sh/bar. Textbook BUILD-and-hold, Grade A catalyst, float 1.6M, fillable two-sided book. Selection was correct — we traded the biggest genuine mover of the night.
- Scanner gap: none for VEEA. The one gap is MYSZ (feed-lag miss, see Notes) — a comparable-size mover the TradingView postmarket feed dropped.

### Baseline Tracking

**Baseline gap:** the immediately-preceding trading day, **Friday Sep 11**, was **never diagnosed** — `log/2026-09-11/log.md` holds only Position Evaluations, no Morning Evaluation and no `Days tracked` line (corroborated by `pm-open-scan.csv`: "the 09-11 Friday log contains no AH scan"). That night's winner was never checked, so a detection miss there could be hidden. Per the rule this is **not back-filled**: the chain jumps 81 → 82 for the Sep 14 session only.

- Days tracked: **82** (was 81 + 1 — Sep 14 session only; Sep 11 Friday NOT back-filled, baseline gap)
- Winners detected by scanner: **68/77 (88.3%)** — +VEEA (biggest genuine mover, detected in 4 scans + entered)
- Winner selected for paper trade: **35/75 (46.7%)** — no >100% winner existed to capture; VEEA (+89.5% PM, the biggest genuine mover) was entered but fell short of the +100% bar
- Target: >80% detection
- Status: **BASELINE MET** (88.3%)

### Retrospective Scan Results

- Live PM scan (04:22 ET): 3 hits — VEEA +65.0% (at scan time; peak +89.5%), MYSZ +85.5% (peak +90.8%), AIIO +9.4% (float 106.7M, small move, not a candidate).
- Forced AH scan: 0 hits (expected — overnight TradingView postmarket fields return stale/0, per the data-hierarchy note; not used as the primary source).
- SIP reconstruction: VEEA and MYSZ both real, heavily-traded movers; HCAI and XPON both faded (see follow-through).

### Open Position P&L (Alpaca)

VEEA is our sole open position. **Quote-freshness note:** the Alpaca `quote` endpoint is stale (VEEA book frozen at 16:59 ET), but the `positions` `current_price` $3.71 matches the live PM tape (Yahoo 04:25 ET $3.73, SIP 08:05Z close $3.84), so the +9.8% is a valid live figure, not a stale artifact.

| Ticker | Entry | Entry Total% | Catalyst | Entry Time | PM Peak | Peak Time | Exit | P&L | P&L % | Status |
|--------|-------|--------------|----------|------------|---------|-----------|------|-----|-------|--------|
| VEEA | $3.38 | +47.6% (from $2.29; scanner tracked +116.7% from stale $1.56) | A — Veea+NovaGen merger term sheet + GeoNova $10M | 2026-09-14 17:30 ET (23:30 CET) | $4.34 (SIP) | 04:00 ET | — (open) | unrealized | **+9.8%** (peak-to-entry was +28.4%) | 🟢 OPEN |

Hold/exit is handled by `position-evaluation.md` (10:30 / 14:30 CET), not here. **Total Realized P&L (Alpaca fills only): €0.00** (no exits).

### Scanner Effectiveness

- Evening scans ran: **7 of 7 scheduled** (21:30, 22:00, 22:30, 23:00, 23:30, 00:00, 00:30 CET) + 2 extra observation scans (22:15, 22:45). Full coverage — entry window (23:00–00:30 CET) fully captured.
- Candidates found: VEEA, HCAI, XPON, BOXL, MITQ, HITI, AIXC, VSME (across scans).
- Retrospective matches: VEEA caught (and traded). MYSZ missed (feed-lag).

### Missed Opportunities

| Ticker | AH Change | Why Missed | Would Be Profitable? |
|--------|-----------|------------|---------------------|
| MYSZ | +35.8% at 18:30 ET (peak +45.7% @19:55 ET) | **In-window feed-lag miss** — ignited 18:25 ET on 222K→212K sh/bar; SIP >10% on accumulating volume at the 18:30 ET last scan, but the TradingView postmarket feed never surfaced it (brand-new name, no pipeline footprint to cross-check) | Yes — hypo AH $2.25 → PM peak $3.30 = **+46.7%** |

### AH Mover Follow-Through

| Ticker | AH Peak | Peak Time | AH Trajectory | Current PM | From Peak | From Close | Verdict |
|--------|---------|-----------|---------------|------------|-----------|------------|---------|
| VEEA | $4.25 (SIP) | 19:50 ET | **Build** (rose every scan +14.5%→+64.6% AH) | ~$3.71 | −12.7% | +62.0% (from $2.29) | **Continued** — PM peak $4.34 > AH peak $4.25 (barely); +89.5%, below the extreme zone. Entered, holding +9.8% |
| HCAI | $2.60 | 16:05 ET (first bar) | **Spike→fade** | ~$1.92 | −26.2% | +3.8% (from $1.85) | **Faded** — AH peak (first bar) was the better exit. Dead-cat + first-bar-spike, correctly skipped |
| XPON | $5.61 | 16:24 ET | **Spike→fade** | ~$4.91 | −12.5% | +7.0% (from $4.59) | **Faded** — AH peak was the better exit. Sub-3M float, correctly skipped |

**AH-peak-vs-PM-peak:** VEEA PM peak ($4.34) slightly EXCEEDED its AH peak ($4.25) = continued, but at +89.5% it is **below the ~+130% extreme-runner zone**, so it does not enter that tally (standing unchanged: 8 fade / 1 continue). HCAI and XPON both had AH peaks above their PM peaks (AH was the exit) but neither is in the extreme zone.

**Chase-cap:** VEEA fill Total% +116.7% (from the stale $1.56 basis; only +47.6% from the true $2.29 close), qualifying-scan Total% +96.8%, chase gap +19.9% — landed just **under** the ~+120% fade zone. **PM reclaimed the fill** (peak $4.34 > $3.38) → a chase that reclaimed = **negative control**. Standing count unchanged: 1 (XOS, never-reclaimed).

### Price Charts

VEEA 2-day timeline (basis Yahoo $1.56 — read peaks from the true $2.29 close: AH $4.25=+85.6%, PM $4.34=+89.5%):

```
Previous Close: $1.56 (stale; true Monday close $2.29)
2-Day Range: $1.50 - $4.34   Peak: $4.34 at 09-15 08:00 ET (04:00 ET)
Flat base $2.2 (16:00–16:35 ET) → ignition 16:40 ET → steady BUILD to $4.25 (19:50 ET)
→ PM open bar $4.34 (04:00 ET) on 1.39M sh → pulled back to ~$3.71
```

### Notes

- **Baseline gap (Fri Sep 11):** no Morning Evaluation exists for the Sep 11 session; retrospective was skipped. Chain jumps 81→82 (Sep 14 only); Sep 11's winner/detection status is unknown and NOT counted. First recorded gap in the recent chain — one-off, likely a missed weekend-morning pulse. Watch for recurrence.
- **Coverage:** 7 of 7 scheduled evening scans ran (+2 extras). No coverage failure.
- **In-window feed-lag miss:** +**MYSZ** (Sep 14→15, surge 18:25 ET, SIP ~$2.35/+35.8% on 212K sh / 1,644 tr at the 18:30 ET last scan, ignited ~5 min before it; hypo AH $2.25 → PM peak $3.30 = **+46.7%**). **Standing count: 5** (BTCT, KUST, WLDS, RAIN, MYSZ) — the ≥3 escalation trigger remains **REACHED**. Route the AH-data-source-verification recommendation (independent whole-universe gainers cross-check at the final scan) to Juan's daily email as a data-reliability decision. No scanner parameter change here.
- **FIRST-BAR-SPIKE skip-validation:** +**HCAI** (Sep 14→15, post-gate WATCH, AH high $2.60 @16:05 ET first bar, CONFIRM-3 NO every scan, hypo entry $2.21 @16:45 ET → PM peak $2.02 = **faded, skip validated, 0 cost**). Standing: **3 pre-gate entries (0 ran: LABT, SUNE, HCAI-Sep10) + 2 post-gate WATCH (XRTX ran, HCAI-Sep15 faded)**. Gate holds (4 of 5 overall fade-or-flat).
- **Fade-rule false-negative (sub-3M):** +**XPON** (Sep 14→15, float 680K, Grade None, AH SIP peak $5.61 @16:24 ET → PM SIP peak $5.20, PM below AH peak = **fell short**). **Standing sub-3M count: 4 of 15** — below the ≥4/5 (≥80%) trigger; exception stays withdrawn.
- **Multi-session-runner tracking:** +**VEEA** (Sep 14→15, **day-1 fresh igniter**, Day% +46.8% same-session, Grade A, entered $3.38 → PM peak $4.34 = **+28.4%, ran**). **Standing: 1 multi-session runner (1 faded) / 20 first-day igniters (7 ran, 6 flat, 7 faded).** First-day run rate 7/20 = 35% — "fresh igniters follow through" stays weak. Data only, no gate change.
- **PM-only gapper:** none today — the biggest raw movers (VEEA +89.5%, MYSZ +90.8%) are both AH→PM continuations, not PM-only gappers. `pm-open-scan.csv` holdable count = **53** (holdable-cluster threshold long exceeded → recurring Initiative-6 early-PM hypothetical-entry pilot routed to Juan's daily email). No 2026-09-15 pm-open row committed yet at eval time.
- **No new cases:** reverse-split-squeeze, broker-block (`tradable=false`), stale-book execution-block, no-fillable-book skip, float-gate skip, final-scan gate-block, dead-cat-override watch, ceiling-override watch. HCAI was a dead-cat but the override did NOT qualify (AH% whipsawed, never a rising reclaim above the close). BOXL/HITI had `ask $0.00 x0` but were below the 10% AH threshold, so they don't reach the no-fillable-book tracker.
- **Prev-close-basis lesson:** VEEA is the textbook stale-basis case — Yahoo prevClose $1.56 (Friday) vs true Monday close $2.29. The tooling's "+178%" headline was fictional; the real AH→PM move is +85.6%/+89.5%, **below the winner bar**. Always recompute % from the true last-session close before crowning.
