# 2026-09-15

## Position Evaluation — 14:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| VEEA | $3.38 | $4.05 | +19.8% | $4.43 (+31.1%) | 1 | A | HOLD | Grade A, day 1 of 5, catalyst intact and building. Peak +31% below +50% trail threshold → no trail yet. Price far above -25% hard stop ($2.54). |

**Analysis:**
- **Source of truth:** Alpaca `positions` — VEEA 28 sh @ $3.38, now $4.05, P&L +$18.76 (+19.8%). `OPEN_POSITIONS.md` matches Alpaca.
- **Exit fillability:** quote bid $4.01 x200 / ask $4.05 x100 @ 12:30Z — deep, liquid book. Easy exit if needed.
- **SIP premarket (09-15):** opened 08:00Z $3.77, spiked $4.34, dipped to ~$3.32–3.68 (09:00–10:15Z), then rebuilt hard from 11:00Z on massive volume (5–6.7M sh/15min) to a fresh session high **$4.43** at 11:55Z, now settling ~$4.05. VEEA is +159% from prev close ($1.56).
- **Peak verified against SIP:** $4.43 (11:55Z 5Min bar H) → Peak P&L +31.1%. Below the +50% Grade A trail trigger.
- **Catalyst:** Veea + NovaGen potential-merger term sheet + GeoNova Capital $10M investment (not a fixed-price cash deal → merger-arb→D exclusion does not apply). Intact; price building to fresh highs on heavy volume = the ideal Grade A "operational catalyst drives sustained momentum" pattern (AIIO/UGRO analog).

**Actions taken:**
- None. HOLD VEEA. No stop update (peak +31% below +50% trail trigger; hard stop stays -25% = $2.54).

## Scan 21:30 CET (3:30 PM ET) — Regular session, watch only

**AH not open yet** (opens 16:00 ET / 22:00 CET). No entries this scan per the regular-session caution rule. These are day-session movers flagged as **Watch — pending AH confirmation**; only enter if they reappear in an AH scan (22:00+ CET) with sustained momentum.

| Ticker | Chart | Price | Day% | 5mVol | IRVol | VChg% | Float | MCap | Industry | Note |
|--------|-------|-------|------|-------|-------|-------|-------|------|----------|------|
| RETO | [TV](https://www.tradingview.com/chart/?symbol=RETO) | $2.87 | +695.7% | 1.5M | 561.7 | -31.8% | 35.8M | 13.3M | Other Metals/Minerals | Huge day move but volume fading; float >10M. Watch AH. |
| MEDS | [TV](https://www.tradingview.com/chart/?symbol=MEDS) | $1.92 | +121.9% | 100 | 209.8 | -100.0% | 1.5M | 2.7M | Medical Distributors | Small float, move already spent (vol collapsed). Watch AH. |
| IPW | [TV](https://www.tradingview.com/chart/?symbol=IPW) | $3.49 | +81.0% | 1K | 869.5 | -99.9% | 945K | 3.3M | Internet Retail | Tiny float, high IRVol; 5m vol dried up. Watch AH. |
| MYSZ | [TV](https://www.tradingview.com/chart/?symbol=MYSZ) | $2.10 | +26.5% | 70K | 428.2 | -25.1% | 646K | 1.5M | Internet Software/Services | Micro float; still trading volume. Watch AH. |

**VEEA** ($5.91, +158.1% day) appears at the top of the scan but is an **open position** (28 sh @ $3.38, held) — handled by position-evaluation, excluded from entries (one entry per candidate per night).

**Other hits noted (lower priority):** MTEN +11.7% (6.1M float), CLNN +26.4% (pharma, 10.6M float), UPLD +23.6%. Most remaining scan hits show VChg% deeply negative (fading, move already spent) or floats well above 10M. No AH data to evaluate yet.

**Next scan:** 22:00 CET (4:00 PM ET) — first true AH scan. Observation only until 23:00 CET (learning-phase entry gate).

## Scan 22:00 CET (4:00 PM ET) — first AH scan, observation only

**Scanner: 0 hits** (ran 16:00:53 ET, 53s into AH — postmarket volume not yet accumulated; zero hits expected this early). Observation only per the learning-phase gate (no entries before 23:00 CET).

**Watch-name AH quote check (early, thin books):**

| Ticker | AH Bid | AH Ask | Note |
|--------|--------|--------|------|
| RETO | $1.20 x200 | $3.49 x200 | Book not settled — huge spread, day move already faded intraday. |
| MEDS | $1.38 x100 | $2.76 x1100 | Wide spread; intraday move already spent. |
| IPW | $2.23 x100 | $3.00 x100 | Wide spread, tiny float. |
| MYSZ | $2.29 x100 | $2.32 x100 | Tight book but flat vs day close (~$2.10-2.30); no AH ignition. |

None show AH ignition. Carry all four forward as watch names; re-check at 22:30/23:00.

**VEEA** — open position (28 sh @ $3.38), handled by position-evaluation; excluded from entries.

**Next scan:** 22:30 CET (4:30 PM ET) — observation. First eligible entry scan is 23:00 CET.

## Scan 22:15 CET (4:15 PM ET) — observation only

**Scanner: 0 hits** (ran 16:15:13 ET). But a watch-name re-check caught **RETO igniting in AH.**

**RETO — real AH igniter, but blocked on extension + first-bar spike (observation only regardless):**
- Quote: bid $4.44 x200 / ask $4.50 x300 @ 16:15 ET — real, two-sided fillable book (vs $1.20/$3.49 at 22:00 — the book has settled and run up).
- SIP first AH bar (16:00 ET): O $2.80 H **$4.73** L $2.47 C $4.58, **vol 5,755,832 / 35,514 trades**, VWAP $3.37 — genuine, massive AH liquidity. Not a bad print (quote corroborates SIP high).
- Context: prev close **$0.36** → regular close $2.87 (Day% +695.7%) → AH ~$4.50. **Total% from prev close = +1150%.**
- Float 35.8M; tradable=true; day 1 of the move (daily bars show only the $0.36 prior close, no multi-session run).
- `SPIKE-BAR: NO-SPIKE peak +11% @16:00ET` · `CONFIRM-3: NO no local-volume new-high ignition as-of 16:15ET`
- **Verdict: skip even at entry time.** Two independent blocks: (1) **Entry extension ceiling** — +1150% total is ~8× the +150% ceiling; no overnight margin. Does NOT qualify for ceiling-override watch (that requires AH high *after* 17:00 ET; RETO's high was the first 16:00 bar). (2) **First-bar spike** — AH high $4.73 printed in the first AH bar, CONFIRM-3 NO.
- **FIRST-BAR-SPIKE WATCH (hypothetical):** entry $4.50 @ 22:15 CET (16:15 ET). Tracks whether the first-bar-spike + extreme-extension skip was correct into PM.

**Other watch names (no AH ignition):**

| Ticker | AH Bid | AH Ask | Note |
|--------|--------|--------|------|
| MEDS | $1.48 x100 | $2.76 x1100 | Bid ticked up but ask is a stale x1100 resting order; still below regular close, no ignition. |
| IPW | $2.23 x100 | $3.00 x100 | Stale (quote 16:00 ET), wide spread, no AH prints. |
| MYSZ | $2.29 x100 | $2.32 x100 | Flat vs day, no AH ignition. |

**VEEA** — open position (28 sh @ $3.38), handled by position-evaluation; excluded from entries.

**Next scan:** 22:30 CET (observation). First eligible entry scan is 23:00 CET — re-check RETO's trajectory and any new igniters then.

## Scan 22:30 CET (4:30 PM ET) — observation only

**Scanner: 4 hits** (ran 16:30:18 ET). Observation only per the learning-phase gate (no entries before 23:00 CET). First eligible entry scan is 23:00 CET.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| RETO | [TV](https://www.tradingview.com/chart/?symbol=RETO) | $2.80 | +676.3% | +62.1% | $4.54 | +1158.7% | 12.0M | 21.0M | 0.6 | 35.8M | Other Metals/Minerals |
| WAFU | [TV](https://www.tradingview.com/chart/?symbol=WAFU) | $1.39 | +1.5% | +90.6% | $2.65 | +93.4% | 5.5M | 662K | 8.4 | 3.0M | Misc Commercial Services |
| TPST | [TV](https://www.tradingview.com/chart/?symbol=TPST) | $0.76 | -3.7% | +25.8% | $0.95 | +21.1% | 907K | 352K | 2.6 | 9.6M | Pharmaceuticals: Major |
| YFOR | [TV](https://www.tradingview.com/chart/?symbol=YFOR) | $1.40 | -2.8% | +10.7% | $1.55 | +7.6% | 348K | 641K | 0.5 | 1.6M | Misc Commercial Services |

**Instrumentation (log-only, no decision impact):**
- RETO — `SPIKE-BAR: NO-SPIKE peak +186% @16:05ET` · `CONFIRM-3: NO no local-volume new-high ignition as-of 16:30ET`
- WAFU — `SPIKE-BAR: SPIKE 16:01ET +29% $1.80 554 trades / 96k sh` · `CONFIRM-3: PENDING ignition 16:10ET; waiting for third bar as-of 16:30ET`
- TPST — `SPIKE-BAR: SPIKE 16:05ET +20% $0.91 40 trades / 14k sh` · `CONFIRM-3: NO ignition 16:05ET failed third-bar hold/volume as-of 16:30ET`
- YFOR — `SPIKE-BAR: SPIKE 16:00ET +16% $1.62 185 trades / 56k sh` · `CONFIRM-3: PENDING ignition 16:15ET; waiting for third bar as-of 16:30ET`

**Candidate evaluation:**

**WAFU — strongest fresh igniter; primary 23:00 entry candidate if it holds (observation only now).**
- Fresh day-1 AH ignition: Day% only +1.5% (regular session flat) → the entire +90.6% move is pure AH. Float **3.0M** (ideal <10M), VRatio **8.4**, Total% **+93.4%** (well under the +150% ceiling), tradable=true.
- SIP bars (16:00–16:15 ET) confirm a **real volume-backed build**, not a bad print:
  - 16:00 O$1.40 H$1.85 C$1.69 — vol 1,021,824 / 5,925 trades — vwap $1.73
  - 16:05 H$2.14 C$1.93 — vol 1,629,758 / 9,730 trades — vwap $1.92
  - 16:10 H**$2.98** C$2.64 — vol 3,689,471 / 26,122 trades — vwap $2.50 (peak bar)
  - 16:15 H$2.80 L$2.10 C$2.49 — vol 1,967,971 / 14,352 trades — vwap $2.37
  - VWAP rising $1.73→$2.50 on accumulating volume; scanner AH $2.65 corroborates SIP (not a bad print). AH high **$2.98 @16:10 ET**, now ~$2.49 (~17% off high — within the ~20% "holding" band, but only 2 bars past peak; too early to call fade).
- Quote at scan is stale (bid $1.16 / ask $1.61 @ 16:00 ET, 30 min behind) — freshness guard: lean on SIP + real-time book at 23:00.
- **Catalyst:** StockTitan — Wah Fu announced its wholly-owned subsidiary Beijing Huaxia Dadi Distance Education signed and began implementing **three AI customization projects** (incl. a Sino-Russian bilingual industrial AI digital human). Chinese small-cap AI operational PR — Grade B/C, plausible momentum driver.
- **Status:** First AH scan appearance (not in 22:00/22:15). Needs to reappear at 23:00 with AH% >10% to satisfy the 2-AH-scan gate. **Watch → likely entry at 23:00 if the build holds within ~20% of the AH high.**

**RETO — carried skip (first-bar spike + extreme extension), fading as thesis predicted.**
- Now bid $2.94 / ask $3.00 @ 16:31 ET (fresh quote) — **faded ~37% off the $4.73 first-bar high** to ~$3.00. Still +733% total extension from prev close ($0.36). Two independent blocks unchanged: (1) extension ~8× the +150% ceiling (no ceiling-override — AH high was the first 16:00 bar, not after 17:00 ET); (2) first-bar spike, CONFIRM-3 NO every scan.
- **FIRST-BAR-SPIKE WATCH** continues (hypothetical entry $4.50 @ 22:15 CET). The fade to ~$3.00 supports the skip.

**TPST — likely skip (thin ignition + weak catalyst).**
- Ignition thin: SPIKE 16:05 ET was only 40 trades / 14k sh; CONFIRM-3 NO (failed third-bar hold/volume). VRatio 2.6, Total +21%, float 9.6M. Quote stale (bid $0.63 / ask $0.88 @ 16:00 ET).
- **Catalyst:** H.C. Wainwright 28th Annual Global conference presentation Sept 15 + next-gen in vivo CAR-T pipeline. A conference presentation is a weak Grade C catalyst, not fresh operational news. Thin volume + weak catalyst → skip candidate.

**YFOR — marginal (borderline threshold, below-avg AH volume).**
- AH Chg +10.7% (barely above threshold), Total +7.6%, VRatio **0.5** (AH vol below its own average — not unusual accumulation). Float 1.6M (small). CONFIRM-3 PENDING. Quote stale (bid $1.20 / ask $1.62 @ 16:00 ET). Low priority; no catalyst searched (marginal signal). Carry as watch.

**VEEA** — open position (28 sh @ $3.38), handled by position-evaluation; excluded from entries.

**Next scan:** 23:00 CET (5:00 PM ET) — **first eligible entry scan.** Re-check WAFU (2-AH-scan gate + hold vs fade), RETO trajectory, and any new igniters.

## Scan 22:45 CET (4:45 PM ET) — observation only

**Scanner: 8 hits** (ran 16:45:20 ET). Observation only per the learning-phase gate (no entries before 23:00 CET). First eligible entry scan is 23:00 CET.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| RETO | [TV](https://www.tradingview.com/chart/?symbol=RETO) | $2.80 | +676.3% | +11.1% | $3.11 | +762.2% | 16.7M | 21.5M | 0.8 | 35.8M | Other Metals/Minerals |
| WAFU | [TV](https://www.tradingview.com/chart/?symbol=WAFU) | $1.39 | +1.5% | +84.9% | $2.57 | +87.6% | 10.5M | 1.2M | 8.5 | 3.0M | Misc Commercial Services |
| TPST | [TV](https://www.tradingview.com/chart/?symbol=TPST) | $0.76 | -3.7% | +52.2% | $1.15 | +46.6% | 7.8M | 1.1M | 7.2 | 9.6M | Pharmaceuticals: Major |
| YFOR | [TV](https://www.tradingview.com/chart/?symbol=YFOR) | $1.40 | -2.8% | +16.4% | $1.63 | +13.2% | 1.5M | 769K | 2.0 | 1.6M | Misc Commercial Services |
| STAK | [TV](https://www.tradingview.com/chart/?symbol=STAK) | $1.14 | -0.9% | +5.3% | $1.20 | +4.3% | 426K | 425K | 1.0 | n/a | Oilfield Services/Equipment |
| WNW | [TV](https://www.tradingview.com/chart/?symbol=WNW) | $2.35 | -1.3% | +6.0% | $2.49 | +4.6% | 362K | 96K | 3.8 | 26.2M | Internet Retail |
| BNGO | [TV](https://www.tradingview.com/chart/?symbol=BNGO) | $1.56 | +17.3% | +9.6% | $1.71 | +28.6% | 130K | 4.1M | 0.0 | 11.1M | Biotechnology |
| EPM | [TV](https://www.tradingview.com/chart/?symbol=EPM) | $3.69 | -0.5% | +7.6% | $3.97 | +7.0% | 124K | 451K | 0.3 | 36.6M | Oil & Gas Production |

**Instrumentation (log-only, no decision impact):**
- RETO — `SPIKE-BAR: NO-SPIKE peak +186% @16:05ET` · `CONFIRM-3: NO no local-volume new-high ignition as-of 16:45ET`
- WAFU — `SPIKE-BAR: SPIKE 16:01ET +29% $1.80 554 trades / 96k sh` · `CONFIRM-3: NO ignition 16:10ET failed third-bar hold/volume as-of 16:45ET`
- TPST — `SPIKE-BAR: SPIKE 16:05ET +20% $0.91 40 trades / 14k sh` · `CONFIRM-3: NO ignition 16:05ET failed third-bar hold/volume as-of 16:45ET`
- YFOR — `SPIKE-BAR: SPIKE 16:00ET +16% $1.62 185 trades / 56k sh` · `CONFIRM-3: NO ignition 16:15ET failed third-bar hold/volume as-of 16:45ET`

**Candidate evaluation:**

**WAFU — primary 23:00 candidate; 2-AH-scan gate already met (22:30 + 22:45).**
- Fresh day-1 AH ignition (Day% +1.5% → entire +84.9% move is AH). Float **3.0M** (ideal), VRatio **8.5**, Total% **+87.6%** (under +150% ceiling), tradable=true.
- SIP bars (16:00–16:30 ET) confirm a **real volume-backed build**, not a bad print — volume accumulating on thousands of trades per bar:
  - 16:00 H$1.85 C$1.69 — vol 1.02M / 5,925 trades — vwap $1.73
  - 16:05 H$2.14 C$1.93 — vol 1.63M / 9,730 trades — vwap $1.92
  - 16:10 H**$2.98** C$2.64 — vol 3.69M / 26,122 trades — vwap $2.50 (peak bar)
  - 16:15 H$2.80 C$2.49 — vol 1.97M / 14,352 trades — vwap $2.37
  - 16:20 H$2.77 C$2.58 — vol 2.10M / 13,923 trades — vwap $2.52
  - 16:25 H$2.79 C$2.59 — vol 1.60M / 11,499 trades — vwap $2.59
  - 16:30 H$2.68 C$2.43 — vol 1.09M / 8,448 trades — vwap $2.53
- AH high **$2.98 @16:10 ET** (before 17:30), now ~$2.43–2.59 (~13–18% off high — inside the ~20% "holding" band, borderline). VWAP has held $2.37–2.59 across six bars = a plateau/hold, not a collapse. Hold-vs-fade is the primary signal; still holding.
- Quote at scan is stale (bid $1.16 / ask $1.61 @ 16:00 ET, 45 min behind) — freshness guard: lean on SIP + real-time book at 23:00.
- **Catalyst:** Wah Fu subsidiary Beijing Huaxia Dadi signed three AI customization projects (Grade B/C, Chinese small-cap AI operational PR).
- **Status:** Gate met. **Watch → likely entry at 23:00 if the build still holds within ~20% of the AH high on a fresh, fillable book.**

**TPST — SPIKE→FADE within AH; likely skip at 23:00 unless it reclaims.**
- SIP shows the ignition built later/bigger than the 22:30 read: spiked to **$1.73 @16:20 ET** on 3.96M sh / 14,344 trades, then immediately faded to ~$1.14–1.15 (16:25 C$1.14, 16:30 C$1.15) — ~33% off the spike high, **beyond the ~20% holding band**. Volume is real and accumulating (2–3M sh/bar), but the price action is a spike-and-fade, not a hold.
- Float 9.6M, VRatio 7.2, Total +46.6% (under ceiling). Quote fresh: bid $0.94 / ask $1.30 @ 16:45 ET (real two-sided book).
- **Catalyst:** H.C. Wainwright 28th Annual Global conference presentation + next-gen in vivo CAR-T pipeline — weak Grade C (conference, not fresh operational news).
- **Status:** Gate met (22:30 +25.8%, 22:45 +52.2%), but peaked 16:20 ET and now 33% off high = fade. Per hold-vs-fade rule, skip at 23:00 unless it rebuilds back within ~20% of $1.73.

**RETO — carried skip (first-bar spike + extreme extension), fading as thesis predicted.**
- Now AH $3.11, +11.1% AH chg — **faded ~34% off the $4.73 first-bar high.** Still +762% total extension from prev close ($0.36). Two independent blocks unchanged: (1) extension ~5× the +150% ceiling (no ceiling-override — AH high was the first 16:00 bar, not after 17:00 ET); (2) first-bar spike, CONFIRM-3 NO every scan.
- **FIRST-BAR-SPIKE WATCH** continues (hypothetical entry $4.50 @ 22:15 CET). The fade to ~$3.11 supports the skip.

**YFOR — marginal, carry as watch.**
- AH Chg +16.4% (above threshold now), Total +13.2%, VRatio 2.0, float 1.6M. CONFIRM-3 NO (ignition 16:15 failed third-bar hold). Low priority; no catalyst searched (marginal signal). Carry as watch.

**New sub-threshold names (all <10% AH, skip):** STAK +5.3%, WNW +6.0%, EPM +7.6% — below the 10% AH threshold. BNGO +9.6% AH but **VRatio 0.0** (130K AH vol vs 4.1M avg — no real AH accumulation; Day% +17.3% is a regular-session move, not AH). None qualify.

**VEEA** — open position (28 sh @ $3.38), handled by position-evaluation; excluded from entries.

**Next scan:** 23:00 CET (5:00 PM ET) — **first eligible entry scan.** Re-check WAFU (hold vs fade + fresh fillable book → enter if holding), TPST (fade vs reclaim), RETO trajectory, and any new igniters.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
| _none yet — regular-session watch scan, AH not open_ | | | | | |
