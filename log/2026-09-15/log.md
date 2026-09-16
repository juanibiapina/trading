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

## Scan 23:00 CET (5:00 PM ET) — first eligible entry scan

**Scanner: 7 hits** (ran 17:00:27 ET). First eligible entry scan (learning-phase gate). **Entered WAFU and YFOR** — both cleared every entry gate; per the W24 multi-position rule, entered both.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| RETO | [TV](https://www.tradingview.com/chart/?symbol=RETO) | $2.80 | +676.3% | +6.1% | $2.97 | +723.4% | 19.9M | 21.9M | 0.9 | 35.8M | Other Metals/Minerals |
| WAFU | [TV](https://www.tradingview.com/chart/?symbol=WAFU) | $1.39 | +1.5% | +86.1% | $2.59 | +88.8% | 15.1M | 1.8M | 8.5 | 3.0M | Misc Commercial Services |
| TPST | [TV](https://www.tradingview.com/chart/?symbol=TPST) | $0.76 | -3.7% | +31.1% | $0.99 | +26.2% | 12.9M | 1.6M | 7.9 | 9.6M | Pharmaceuticals: Major |
| YFOR | [TV](https://www.tradingview.com/chart/?symbol=YFOR) | $1.40 | -2.8% | +42.1% | $1.99 | +38.2% | 2.8M | 934K | 3.0 | 1.6M | Misc Commercial Services |
| STAK | [TV](https://www.tradingview.com/chart/?symbol=STAK) | $1.14 | -0.9% | +5.3% | $1.20 | +4.3% | 698K | 454K | 1.5 | n/a | Oilfield Services/Equipment |
| WNW | [TV](https://www.tradingview.com/chart/?symbol=WNW) | $2.35 | -1.3% | +15.7% | $2.72 | +14.3% | 591K | 124K | 4.8 | 26.2M | Internet Retail |
| BNGO | [TV](https://www.tradingview.com/chart/?symbol=BNGO) | $1.56 | +17.3% | +6.4% | $1.66 | +24.8% | 515K | 4.1M | 0.1 | 11.1M | Biotechnology |

**Instrumentation (log-only, no decision impact):**
- WAFU — `SPIKE-BAR: SPIKE 16:01ET +29% $1.80 554 trades / 96k sh` · `CONFIRM-3: NO ignition 16:10ET failed third-bar hold/volume as-of 17:00ET`
- YFOR — `SPIKE-BAR: SPIKE 16:00ET +16% $1.62 185 trades / 56k sh` · `CONFIRM-3: NO ignition 16:15ET failed third-bar hold/volume as-of 17:00ET` (note: the real ignition is the 16:40-16:45 volume surge, which the detector's "ignition 16:15" framing missed — trajectory/SIP is truth)
- TPST — `SPIKE-BAR: SPIKE 16:05ET +20% $0.91 40 trades / 14k sh` · `CONFIRM-3: NO ignition 16:05ET failed third-bar hold/volume as-of 17:00ET`
- RETO — `SPIKE-BAR: NO-SPIKE peak +186% @16:05ET` · `CONFIRM-3: NO no local-volume new-high ignition as-of 17:00ET`

**ENTERED — WAFU (Grade None, 38 sh @ $2.21):**
- **All gates cleared:** Float 3.0M (ideal), 2-AH-scan gate met (22:30 +90.6% → 22:45 +84.9% → 23:00 +86.1%, AH% flat/holding across three scans), Total% +88.8% (under +150% ceiling), Day% +1.5% (above -15%), tradable=true.
- **Real volume-backed BUILD** (SIP 16:00-16:45 ET): 16:00 1.02M sh/5,925 tr → 16:10 3.69M sh/26,122 tr (H$2.98) → 16:35 2.76M sh/20,718 tr making a **NEW AH high $3.25** (past the first-bar spike) → 16:40 1.58M sh → 16:45 1.11M sh (C$2.26). Not a bad print (SIP H $3.25 exceeds scanner AH $2.59). VRatio 8.5.
- **Fresh day-1 igniter** (Day% +1.5% → entire move is AH; daily bars show only prev close $1.37; not a multi-session runner. Prior WAFU trade Aug 10 +8.2% was weeks ago).
- **Catalyst: None** — no fresh same-day driver found (3 searches). The "3 AI customization projects" PR is **Aug 10-11 2026** (over a month old), last earnings Jul 30. Prior scans (22:30/22:45) mis-attributed that stale PR as tonight's catalyst — corrected here. No-catalyst handling: enter with concern noted (not a skip reason in learning phase).
- **Concern:** borderline hold — ~20% off the $3.25 high at scan; last SIP bars faded ($2.59→$2.26 on declining volume). At scan level AH% is flat/holding (~+85-90% across 3 scans), which supports entry, but the intra-window fade is a real risk. Grade None → exit at first PM opportunity.
- **Order:** BUY 38 @ limit $2.70 ext (id 4ea8860f) → **filled @ $2.21.** Favorable fill: the real market (~$2.21, matching the 16:45 SIP close) was below the stale scanner $2.59.
- **CHASE-CAP:** N/A (favorable) — qualifying AH $2.59/+88.8%; fill $2.21/+59.0%; chase gap **-29.8%** (filled *below* qualifying, not chased into fade zone). Stale-book artifact worked in our favor.

**ENTERED — YFOR (Grade None, 57 sh @ $1.55):**
- **All gates cleared:** Float 1.6M (ideal, ultra-low), 2-AH-scan gate met (22:30 +10.7% → 22:45 +16.4% → 23:00 +42.1%, **building across all scans**), Total% +38.2% (well under ceiling), Day% -2.8% (above -15%), tradable=true, fresh fillable book (bid $1.63 x100 / ask $1.74 x100 @ 16:59:59 ET).
- **Accelerating volume-backed BUILD** (SIP): quiet 16:00-16:35 (29-500K sh/bar) then **late ignition accelerating** — 16:40 ET 1.37M sh/10,449 tr (H$2.07) → 16:45 ET 1.79M sh/14,879 tr making a **NEW AH high $2.15 in the last bar** (at highs, building), VWAP rising $1.93→$2.06. VRatio 3.0. This is the strongest BUILD trajectory of the night.
- **Fresh day-1 igniter** (Day% -2.8% → pure-AH move; daily bars show one prev close $1.44; not a multi-session runner). YFOR = ex-YYGH (rebrand eff. Sept 2), traded Aug 25 +25.5% / Jul 10 -17.5% under old ticker — weeks ago, not a recent-session run.
- **Catalyst: None** — no fresh same-day driver found (4 searches). Only the Aug 31 rebrand PR (YY Group→YYForce, YYGH→YFOR). No-catalyst handling: enter with concern noted.
- **Order:** BUY 57 @ limit $1.80 ext (id ce1c6258) → **filled @ $1.55.** Favorable fill: real ask ($1.55) below scanner $1.99. Grade None → exit at first PM opportunity.
- **CHASE-CAP:** N/A (favorable) — qualifying AH $1.99/+38.2%; fill $1.55/+10.7%; chase gap **-27.5%** (filled *below* qualifying).

**SKIP — TPST (SPIKE→FADE):** Gate met (22:30 +25.8% → 22:45 +52.2% → 23:00 +31.1%) but SIP shows spike-and-fade: peaked **$1.73 @16:20 ET** (3.96M sh) then faded ~40% to ~$1.00 on **declining volume** (3.96M→2.39M→2.9M→1.59M→0.94M→0.70M sh/bar). Now ~30-40% off the spike high — beyond the ~20% holding band. Weak Grade C catalyst (H.C. Wainwright conference presentation). Per hold-vs-fade rule → skip. Fresh quote bid $0.94 / ask $1.30.

**SKIP (carried) — RETO (first-bar spike + extreme extension):** AH $2.97, +6.1% AH chg — faded ~37% off the $4.73 first-bar high. Still +723% total extension from prev close ($0.36) — ~5× the +150% ceiling. Two independent blocks unchanged: (1) extension far above ceiling (no ceiling-override — AH high was the first 16:00 bar, not after 17:00 ET); (2) first-bar spike, CONFIRM-3 NO every scan. **FIRST-BAR-SPIKE WATCH** continues (hypothetical entry $4.50 @ 22:15 CET). The fade to ~$2.97 supports the skip.

**Sub-threshold / no-accumulation (skip):** STAK +5.3%, WNW +15.7% (but only 1 AH scan >10% — 2-AH-scan gate not met; float 26.2M; carry as watch), BNGO +6.4% (VRatio 0.1 — no real AH accumulation; Day% +17.3% is a regular-session move).

**VEEA** — open position (28 sh @ $3.38, now $5.45, +61.3%), handled by position-evaluation; excluded from entries.

**Next scan:** 23:30 CET (5:30 PM ET) — monitor WAFU (hold vs fade), YFOR (build continuation), and any new igniters. Note: WAFU/YFOR entries are the night's data; position management (exits) is handled by premarket position-evaluation.

## Scan 23:30 CET (5:30 PM ET) — monitor + late-igniter check

**Scanner: 11 hits** (ran 17:30:22 ET). **No new entries.** Only new AH>10% name is PDSB, blocked on the 2-AH-scan gate (first AH appearance) + Grade D dilution catalyst. WAFU and YFOR were entered at 23:00 (excluded from new entries — one entry per candidate per night); trajectory noted below.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| RETO | [TV](https://www.tradingview.com/chart/?symbol=RETO) | $2.80 | +676.3% | +20.7% | $3.38 | +837.1% | 26.0M | 22.6M | 1.2 | 35.8M | Other Metals/Minerals |
| WAFU | [TV](https://www.tradingview.com/chart/?symbol=WAFU) | $1.39 | +1.5% | +59.0% | $2.21 | +61.3% | 18.1M | 2.1M | 8.6 | 3.0M | Misc Commercial Services |
| TPST | [TV](https://www.tradingview.com/chart/?symbol=TPST) | $0.76 | -3.7% | +35.0% | $1.02 | +30.1% | 15.9M | 2.0M | 8.1 | 9.6M | Pharmaceuticals: Major |
| PDSB | [TV](https://www.tradingview.com/chart/?symbol=PDSB) | $0.59 | +46.7% | +15.3% | $0.68 | +69.1% | 6.1M | 97.9M | 0.1 | 55.0M | Pharmaceuticals: Major |
| YFOR | [TV](https://www.tradingview.com/chart/?symbol=YFOR) | $1.40 | -2.8% | +25.0% | $1.75 | +21.5% | 6.1M | 1.3M | 4.6 | 1.6M | Misc Commercial Services |
| STAK | [TV](https://www.tradingview.com/chart/?symbol=STAK) | $1.14 | -0.9% | +6.9% | $1.22 | +6.0% | 743K | 459K | 1.6 | n/a | Oilfield Services/Equipment |
| BNGO | [TV](https://www.tradingview.com/chart/?symbol=BNGO) | $1.56 | +17.3% | +11.5% | $1.74 | +30.8% | 681K | 4.1M | 0.2 | 11.1M | Biotechnology |
| WNW | [TV](https://www.tradingview.com/chart/?symbol=WNW) | $2.35 | -1.3% | +8.9% | $2.56 | +7.6% | 668K | 133K | 5.0 | 26.2M | Internet Retail |
| REED | [TV](https://www.tradingview.com/chart/?symbol=REED) | $0.85 | +14.9% | +7.3% | $0.91 | +23.3% | 500K | 210K | 2.4 | 5.5M | Beverages: Non-Alcoholic |
| MYSZ | [TV](https://www.tradingview.com/chart/?symbol=MYSZ) | $2.32 | +39.8% | +7.8% | $2.50 | +50.6% | 322K | 3.1M | 0.1 | 646K | Internet Software/Services |
| CDZI | [TV](https://www.tradingview.com/chart/?symbol=CDZI) | $3.51 | -2.5% | +9.1% | $3.83 | +6.4% | 56K | 890K | 0.1 | 56.6M | Real Estate Development |

**Instrumentation (log-only, no decision impact):**
- PDSB — `SPIKE-BAR: SPIKE 16:09ET +15% $0.68 371 trades / 128k sh` · `CONFIRM-3: PENDING ignition 17:10ET; waiting for third bar as-of 17:30ET`
- WAFU — `SPIKE-BAR: SPIKE 16:01ET +29% $1.80 554 trades / 96k sh` · `CONFIRM-3: NO ignition 16:10ET failed third-bar hold/volume as-of 17:30ET`
- YFOR — `SPIKE-BAR: SPIKE 16:00ET +16% $1.62 185 trades / 56k sh` · `CONFIRM-3: NO ignition 16:15ET failed third-bar hold/volume as-of 17:30ET`
- TPST — `SPIKE-BAR: SPIKE 16:05ET +20% $0.91 40 trades / 14k sh` · `CONFIRM-3: NO ignition 16:05ET failed third-bar hold/volume as-of 17:30ET`
- RETO — `SPIKE-BAR: NO-SPIKE peak +186% @16:05ET` · `CONFIRM-3: NO no local-volume new-high ignition as-of 17:30ET`
- BNGO — `SPIKE-BAR: SPIKE 16:38ET +18% $1.84 506 trades / 115k sh` · `CONFIRM-3: NO ignition 16:35ET failed third-bar hold/volume as-of 17:30ET`

**Candidate evaluation:**

**PDSB — new AH>10% name, real late build, but SKIP (2-AH-scan gate + Grade D dilution + multi-session runner).**
- First AH scan appearance (not in 22:00–23:00). Day% +46.7% is a regular-session move; AH adds +15.3% on top. Float **55.0M** (high), VRatio **0.1** (6.1M AH vol vs a 97.9M average — AH volume not unusual for this name), Total% +69.1% (under ceiling), tradable=true.
- SIP shows a **real, accelerating late build** at scan time: quiet 16:15–16:40 ET (~$0.58, 50–190K sh/bar), then 16:45 725K sh → 16:50 1.19M sh/1,486 tr → **17:10 ET 1.72M sh/2,766 tr H$0.70** → 17:15 ET 1.42M sh/1,816 tr H$0.70 C$0.68, VWAP $0.68 (new AH high, building at scan). Genuine accumulation, not a bad print.
- Quote stale: bid $0.54 x500 / ask **$0.80 x20000** @ 16:52 ET (~38 min behind at scan) — the x20000 ask is a large resting ceiling. Freshness guard: lean on SIP.
- **Catalyst: Grade D (dilution).** PDS Biotech PIPE financing — up to $22.55M PIPE announced ~1 week ago (shares rocketed 183% to $0.62 then), **initial $11.3M closing PR Sept 14** (GlobeNewswire). Today's move is continued PIPE momentum, not a fresh first-day catalyst. A financing/dilution catalyst is Grade D (exit immediately).
- **Multi-session runner:** already ran +183% ~1 week ago on the same PIPE; not a fresh day-1 igniter ("first day of unusual activity" fails).
- **Verdict: SKIP.** Blocked on three independent counts: (1) 2-AH-scan gate not met (first AH appearance); (2) Grade D dilution catalyst; (3) multi-session runner on a stale catalyst. VRatio 0.1 adds a fourth concern. The late SIP build is real but does not override the gate or the dilution grade. Carry forward; if it reappears at 00:00 with AH>10% the gate would clear, but Grade D keeps it a skip.

**WAFU — open position (entered 23:00 @ $2.21), fading as the intra-window concern predicted.**
- Now $1.97 (Alpaca P&L **-10.9%**). AH Chg fell +86.1% (23:00) → +59.0% (23:30); AH price $2.59 → $2.21 = the borderline-hold flagged at entry has rolled over off the $3.25 AH high. Grade None. Excluded from new entries (one entry per candidate per night); exit handled by premarket position-evaluation.

**YFOR — open position (entered 23:00 @ $1.55), holding above entry.**
- Now $1.74 (Alpaca P&L **+12.3%**). AH Chg +42.1% (23:00) → +25.0% (23:30) — pulled back from the 23:00 peak ($1.99) but still above the $1.55 fill. Grade None. Excluded from new entries; exit handled by premarket position-evaluation.

**RETO — carried skip (first-bar spike + extreme extension).** AH $3.38, +20.7% AH chg — bounced off the ~$2.97 low but still ~29% below the $4.73 first-bar high and +837% total extension from prev close ($0.36), ~5.6× the +150% ceiling. Two blocks unchanged: extension far above ceiling (no ceiling-override — AH high was the first 16:00 bar) + first-bar spike (CONFIRM-3 NO every scan). **FIRST-BAR-SPIKE WATCH** continues (hypothetical entry $4.50 @ 22:15 CET; now $3.38 = -24.9%).

**TPST — carried skip (SPIKE→FADE).** AH $1.02, +35.0% AH chg — bounced off the ~$1.00 low but still ~41% below the $1.73 spike high (16:20 ET); volume was declining into the fade. Weak Grade C catalyst (H.C. Wainwright conference presentation). Skip continues.

**Sub-threshold / no-accumulation (skip):** BNGO +11.5% AH but VRatio 0.2 (681K AH vol vs 4.1M avg — no real AH accumulation; Day% +17.3% is a regular-session move). WNW +8.9% (faded from +15.7% at 23:00; only 1 scan >10%; float 26.2M). MYSZ +7.8%, REED +7.3%, CDZI +9.1%, STAK +6.9% — all below the 10% AH threshold.

**VEEA** — open position (28 sh @ $3.38, now $5.65, +67.2%), handled by position-evaluation; excluded from entries.

**Next scan:** 00:00 CET (6:00 PM ET) — monitor WAFU (fade), YFOR (hold), PDSB (does it reappear + hold, though Grade D keeps it a skip), and any new igniters. WAFU/YFOR exits are handled by premarket position-evaluation.

## Scan 00:00 CET (6:00 PM ET) — monitor + late-igniter check

**Scanner: 13 hits** (ran 18:00:27 ET). **No new entries.** The one strong new AH igniter, MEDS, is blocked on the +150% extension ceiling + the 2-AH-scan gate (first AH scan appearance). WNW clears the 2-AH-scan gate and the ceiling but is skipped on trajectory (early peak + thin drift, CONFIRM-3 NO). WAFU/YFOR were entered at 23:00 (excluded — one entry per candidate per night); trajectory noted below.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| RETO | [TV](https://www.tradingview.com/chart/?symbol=RETO) | $2.80 | +676.3% | +16.1% | $3.25 | +801.0% | 27.5M | 22.8M | 1.2 | 35.8M | Other Metals/Minerals |
| WAFU | [TV](https://www.tradingview.com/chart/?symbol=WAFU) | $1.39 | +1.5% | +43.9% | $2.00 | +46.0% | 19.6M | 2.3M | 8.6 | 3.0M | Misc Commercial Services |
| TPST | [TV](https://www.tradingview.com/chart/?symbol=TPST) | $0.76 | -3.7% | +33.7% | $1.01 | +28.8% | 16.9M | 2.1M | 8.2 | 9.6M | Pharmaceuticals: Major |
| MEDS | [TV](https://www.tradingview.com/chart/?symbol=MEDS) | $1.62 | +87.2% | +56.2% | $2.53 | +192.4% | 7.9M | 6.1M | 1.3 | 1.5M | Medical Distributors |
| YFOR | [TV](https://www.tradingview.com/chart/?symbol=YFOR) | $1.40 | -2.8% | +25.7% | $1.76 | +22.2% | 6.6M | 1.4M | 4.8 | 1.6M | Misc Commercial Services |
| BNGO | [TV](https://www.tradingview.com/chart/?symbol=BNGO) | $1.56 | +17.3% | +13.5% | $1.77 | +33.1% | 747K | 4.1M | 0.2 | 11.1M | Biotechnology |
| WNW | [TV](https://www.tradingview.com/chart/?symbol=WNW) | $2.35 | -1.3% | +11.9% | $2.63 | +10.5% | 727K | 140K | 5.2 | 26.2M | Internet Retail |
| VRA | [TV](https://www.tradingview.com/chart/?symbol=VRA) | $4.09 | +34.5% | +6.4% | $4.35 | +43.1% | 512K | 1.3M | 0.4 | 18.3M | Apparel/Footwear |
| MYSZ | [TV](https://www.tradingview.com/chart/?symbol=MYSZ) | $2.32 | +39.8% | +7.8% | $2.50 | +50.6% | 409K | 3.1M | 0.1 | 646K | Internet Software/Services |
| WWR | [TV](https://www.tradingview.com/chart/?symbol=WWR) | $0.54 | -4.7% | +5.9% | $0.57 | +0.9% | 70K | 938K | 0.1 | 117.5M | Other Metals/Minerals |
| TOPS | [TV](https://www.tradingview.com/chart/?symbol=TOPS) | $0.80 | +13.1% | +5.9% | $0.85 | +19.7% | 58K | 87K | 0.7 | 4.1M | Marine Shipping |
| CDZI | [TV](https://www.tradingview.com/chart/?symbol=CDZI) | $3.51 | -2.5% | +9.1% | $3.83 | +6.4% | 56K | 890K | 0.1 | 56.6M | Real Estate Development |
| VENU | [TV](https://www.tradingview.com/chart/?symbol=VENU) | $1.72 | -1.7% | +5.2% | $1.81 | +3.4% | 51K | 415K | 0.1 | 41.9M | Movies/Entertainment |

**Instrumentation (log-only, no decision impact):**
- MEDS — `SPIKE-BAR: SPIKE 17:22ET +15% $1.87 589 trades / 118k sh` · `CONFIRM-3: YES ignition 17:20ET 14.6x; confirmed 17:30ET $2.58 as-of 18:00ET`
- WNW — `SPIKE-BAR: SPIKE 16:19ET +26% $2.95 212 trades / 98k sh` · `CONFIRM-3: NO ignition 16:15ET failed third-bar hold/volume as-of 18:00ET`
- WAFU — `SPIKE-BAR: SPIKE 16:01ET +29% $1.80 554 trades / 96k sh` · `CONFIRM-3: NO ignition 16:10ET failed third-bar hold/volume as-of 18:00ET`
- YFOR — `SPIKE-BAR: SPIKE 16:00ET +16% $1.62 185 trades / 56k sh` · `CONFIRM-3: NO ignition 16:15ET failed third-bar hold/volume as-of 18:00ET`
- TPST — `SPIKE-BAR: SPIKE 16:05ET +20% $0.91 40 trades / 14k sh` · `CONFIRM-3: NO ignition 16:05ET failed third-bar hold/volume as-of 18:00ET`
- RETO — `SPIKE-BAR: NO-SPIKE peak +186% @16:05ET` · `CONFIRM-3: NO no local-volume new-high ignition as-of 18:00ET`
- BNGO — `SPIKE-BAR: SPIKE 16:38ET +18% $1.84 506 trades / 115k sh` · `CONFIRM-3: NO ignition 16:35ET failed third-bar hold/volume as-of 18:00ET`

**Candidate evaluation:**

**MEDS — genuine late volume-backed BUILD, but SKIP (extension ceiling + 2-AH-scan gate).**
- **The strongest fresh igniter of the night, and the only CONFIRM-3 YES.** Quiet through 17:15 ET, then ignited **17:20 ET** and built hard on massive accumulating volume: SIP 17:20 O$1.65 H$2.24 C$2.20 vol 1.04M / 5,232 tr → 17:25 H$2.43 C$2.40 vol 1.69M / 9,292 tr → **17:30 H$2.69 C$2.58 vol 1.87M / 11,763 tr** (new AH high $2.69, after 17:00 ET) → 17:35 H$2.65 C$2.55 vol 1.02M / 6,298 tr. VWAP $2.03→$2.54 on 5k–12k trades/bar. `CONFIRM-3 YES 14.6x`. Not a bad print (SIP corroborates the scanner $2.53).
- Fresh **day-1 igniter** (daily bars show only prev close $0.87; not a multi-session runner). Float **1.5M** (ideal). tradable=true.
- **Blocks (two independent):** (1) **Entry extension ceiling** — Total% **+192.4%** exceeds the +150% ceiling; extended entries leave no overnight margin (PRFX/VCIG/ATPC/ANY analog). Most of the extension is the +87% regular-session move, with AH adding +56% on top. (2) **2-AH-scan gate not met** — first AH scan appearance at 00:00 (feed-lag: ignited 17:20 ET but the TradingView postmarket feed did not surface it until 18:00 ET; it was absent from the 23:30 scan).
- **No ceiling-override watch:** the override requires VRatio >5x; MEDS VRatio is **1.3** (7.9M AH vol against a high 6.1M average daily volume). The AH high is after 17:00 ET (✓) but only 1 AH scan exists so far (fails the ≥2-scan hold requirement too). **Morning-eval flag:** the VRatio-based ceiling-override guard excludes a genuinely strong late igniter *purely because MEDS has a high average daily volume* (absolute AH accumulation is huge — 7.9M sh, 5k–12k trades/bar). A record for whether the override's VRatio gate should also credit absolute-volume ignition.
- **Catalyst: None found** (3 searches — all results 2024 or older: TRxADE→Scienture name change, SOSRx JV, late 10-K filing). No fresh same-day driver surfaced within budget.
- **Verdict: SKIP** on the +150% ceiling + 2-AH-scan gate. Track into PM to measure whether the ceiling correctly avoided a +192%-extended fade despite the strong build.

**WNW — 2-AH-scan gate met + under ceiling, but SKIP (early peak + thin drift, CONFIRM-3 NO).**
- Gate met (23:00 +15.7% → 00:00 +11.9%, two AH scans >10%) and Total% only +10.5% (well under ceiling), Day% -1.3% (fresh AH move), VRatio 5.2, tradable=true.
- **But the trajectory is a spike-and-drift, not a build.** SIP: AH high **$3.08 @ 16:35 ET** (early, before 17:00) on the 16:15–16:35 spike (~600K sh), then volume **dried up** — 16:50–17:45 ET bars are 2K–48K sh with <300 trades each. That is the textbook **thin drift, not a build** (tens-of-K sh, hundreds not thousands of trades per bar). `CONFIRM-3 NO`. Current ~$2.58–2.65 is ~15% off the $3.08 high (inside the ~20% band) but the hold is on no volume.
- Trajectory dominates: early peak (16:35 ET) + thin declining volume = SPIKE→FADE class (0/6+ for PM continuation). **Verdict: SKIP.**
- **Catalyst: None found** (Meiwu Technology, Chinese online food retail; no fresh same-day PR). Trajectory is the skip regardless.

**WAFU — open position (entered 23:00 @ $2.21), faded as the intra-window concern predicted.** Now $1.82 (Alpaca P&L **-17.6%**); AH Chg $2.59→$2.00. Grade None. Excluded from new entries; exit handled by premarket position-evaluation.

**YFOR — open position (entered 23:00 @ $1.55), holding above entry.** Now $1.82 (Alpaca P&L **+17.4%**); AH $1.76. Grade None. Excluded from new entries; exit handled by premarket position-evaluation.

**RETO — carried skip (first-bar spike + extreme extension).** AH $3.25, +16.1% AH chg — still ~31% below the $4.73 first-bar high and +801% total extension from prev close ($0.36), ~5× the +150% ceiling. Two blocks unchanged: extension far above ceiling (no ceiling-override — AH high was the first 16:00 bar) + first-bar spike (CONFIRM-3 NO every scan). **FIRST-BAR-SPIKE WATCH** continues (hypothetical entry $4.50 @ 22:15 CET; now $3.25 = -27.8%).

**TPST — carried skip (SPIKE→FADE).** AH $1.01, +33.7% AH chg — still ~42% below the $1.73 spike high (16:20 ET); ignition volume declined into the fade. Weak Grade C catalyst (H.C. Wainwright conference presentation). CONFIRM-3 NO. Skip continues.

**Sub-threshold / no-accumulation (skip):** BNGO +13.5% AH but VRatio 0.2 (747K AH vol vs 4.1M avg — no real AH accumulation; Day% +17.3% is a regular-session move). VRA +6.4%, MYSZ +7.8%, WWR +5.9%, TOPS +5.9%, CDZI +9.1%, VENU +5.2% — all below the 10% AH threshold.

**VEEA** — open position (28 sh @ $3.38, now $5.72, +69.2%), handled by position-evaluation; excluded from entries.

**Next scan:** 00:30 CET (6:30 PM ET) — **last scheduled scan.** Re-check MEDS (does it hold near the $2.69 AH high; still ceiling-blocked at +192% regardless), WNW (fade confirmation), WAFU/YFOR trajectory (exits handled by premarket position-evaluation), and any final-scan late igniters (apply the feed-lag cross-check to pipeline names).

## Scan 00:30 CET (6:30 PM ET) — last scheduled scan

**Scanner: 13 hits** (ran 18:30:23 ET). **No new entries.** MEDS technically cleared both of its 00:00 blocks (Total% dropped +192.4% → +148.5%, under the +150% ceiling; 2-AH-scan gate now met with 00:00 + 00:30 appearances) — but it cleared the ceiling *only by fading* ~20% off its $2.69 peak on collapsing volume, so it is skipped on the hold-vs-fade rule. WAFU/YFOR were entered at 23:00 (excluded — one entry per candidate per night); trajectory noted below.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| RETO | [TV](https://www.tradingview.com/chart/?symbol=RETO) | $2.80 | +676.3% | +45.0% | $4.06 | +1025.6% | 30.4M | 23.1M | 1.3 | 35.8M | Other Metals/Minerals |
| WAFU | [TV](https://www.tradingview.com/chart/?symbol=WAFU) | $1.39 | +1.5% | +35.3% | $1.88 | +37.2% | 20.2M | 2.3M | 8.6 | 3.0M | Misc Commercial Services |
| TPST | [TV](https://www.tradingview.com/chart/?symbol=TPST) | $0.76 | -3.7% | +39.2% | $1.05 | +34.1% | 18.3M | 2.2M | 8.3 | 9.6M | Pharmaceuticals: Major |
| PDSB | [TV](https://www.tradingview.com/chart/?symbol=PDSB) | $0.59 | +46.7% | +6.5% | $0.62 | +56.2% | 11.1M | 98.4M | 0.1 | 55.0M | Pharmaceuticals: Major |
| MEDS | [TV](https://www.tradingview.com/chart/?symbol=MEDS) | $1.62 | +87.2% | +32.7% | $2.15 | +148.5% | 10.6M | 6.4M | 1.7 | 1.5M | Medical Distributors |
| YFOR | [TV](https://www.tradingview.com/chart/?symbol=YFOR) | $1.40 | -2.8% | +27.9% | $1.79 | +24.3% | 7.1M | 1.4M | 4.9 | 1.6M | Misc Commercial Services |
| WNW | [TV](https://www.tradingview.com/chart/?symbol=WNW) | $2.35 | -1.3% | +13.2% | $2.66 | +11.8% | 757K | 143K | 5.3 | 26.2M | Internet Retail |
| GWAV | [TV](https://www.tradingview.com/chart/?symbol=GWAV) | $2.66 | -16.2% | +23.7% | $3.29 | +3.6% | 5K | 40K | 0.1 | 219K | Misc Commercial Services |
| STAK | [TV](https://www.tradingview.com/chart/?symbol=STAK) | $1.14 | -0.9% | +6.1% | $1.21 | +5.2% | 818K | 467K | 1.8 | n/a | Oilfield Services/Equipment |
| BURU | [TV](https://www.tradingview.com/chart/?symbol=BURU) | $1.20 | -11.1% | +5.0% | $1.26 | -6.7% | 224K | 950K | 0.2 | 8.4M | Electronic Components |
| WWR | [TV](https://www.tradingview.com/chart/?symbol=WWR) | $0.54 | -4.7% | +7.2% | $0.58 | +2.1% | 73K | 938K | 0.1 | 117.5M | Other Metals/Minerals |
| TOPS | [TV](https://www.tradingview.com/chart/?symbol=TOPS) | $0.80 | +13.1% | +5.2% | $0.84 | +19.0% | 61K | 87K | 0.7 | 4.1M | Marine Shipping |
| CDZI | [TV](https://www.tradingview.com/chart/?symbol=CDZI) | $3.51 | -2.5% | +9.1% | $3.83 | +6.4% | 56K | 890K | 0.1 | 56.6M | Real Estate Development |

**Instrumentation (log-only, no decision impact):**
- MEDS — `SPIKE-BAR: SPIKE 17:22ET +15% $1.87 589 trades / 118k sh` · `CONFIRM-3: YES ignition 17:20ET 14.6x; confirmed 17:30ET $2.58 as-of 18:30ET`
- WNW — `SPIKE-BAR: SPIKE 16:19ET +26% $2.95 212 trades / 98k sh` · `CONFIRM-3: NO ignition 16:15ET failed third-bar hold/volume as-of 18:30ET`
- TPST — `SPIKE-BAR: SPIKE 16:05ET +20% $0.91 40 trades / 14k sh` · `CONFIRM-3: NO ignition 16:05ET failed third-bar hold/volume as-of 18:30ET`
- RETO — `SPIKE-BAR: NO-SPIKE peak +186% @16:05ET` · `CONFIRM-3: NO no local-volume new-high ignition as-of 18:30ET`
- GWAV — `SPIKE-BAR: SPIKE 16:37ET +21% $3.22 22 trades / 1k sh` · `CONFIRM-3: NO no local-volume new-high ignition as-of 18:30ET`

**Candidate evaluation:**

**MEDS — both 00:00 blocks technically cleared, but SKIP (cleared the ceiling only by fading; hold-vs-fade dominates).**
- **Gates now cleared:** Total% **+148.5%** (was +192.4% at 00:00 — under the +150% ceiling now); 2-AH-scan gate met (00:00 +56.2% → 00:30 +32.7%, both AH scans >10%); Day% +87.2% (above -15%); float **1.5M** (ideal); tradable=true; `CONFIRM-3 YES 14.6x` (the night's only YES — real, volume-backed ignition after 17:00 ET).
- **But the trajectory is now a FADE, not a hold.** SIP (forced-recent, to 18:15 ET): peaked **$2.69 @ 17:30 ET** (1.87M sh / 11,763 tr), then 17:45 dropped to $2.03–2.23 (938K sh), bounced to $2.54 @ 18:00 ET (741K sh), then settled $2.08–2.15 as **volume collapsed** — 18:05 373K → 18:10 246K → 18:15 **110K sh**. Yahoo 18:20–18:31 ET: $2.05–$2.18. Current ~$2.15 is **~20% off the $2.69 high** (right at the boundary); the **live quote bid $1.74** (ask $3.50 stale/wide) is ~35% off — real sell pressure. AH price declined across both scans it appeared in ($2.53 → $2.15).
- **The reason it dropped under the ceiling is the fade itself** (price $2.53 → $2.15 = -15%). Entering a name that cleared +150% only by fading is the anti-signal — at +148.5% it sits exactly in the ATPC (+154%→-14.1%) / ANY (+155%→-21.3%) loss zone. Grade None (no catalyst — 3 searches at 00:00 returned only 2024-or-older results).
- **No ceiling-override watch:** VRatio **1.7** (<5x required) — fails the override's volume gate (10.6M AH vol against a high 6.4M avg daily volume).
- **Verdict: SKIP** on hold-vs-fade + extension-at-ceiling. **FADE-SKIP WATCH (hypothetical):** entry ~$2.15 @ 00:30 CET (18:30 ET) — recorded so morning-eval can measure whether skipping the night's only CONFIRM-3 YES (a genuine post-17:00 igniter that faded ~20% and slipped under the ceiling) was correct. This is the key data point of the night: a name whose ceiling + 2-AH-scan blocks *cleared by fading*.

**WNW — 3 AH scans >10% + under ceiling, but SKIP (thin drift, early peak, CONFIRM-3 NO).**
- 2-AH-scan gate met (23:00 +15.7% → 00:00 +11.9% → 00:30 +13.2%), Total% only +11.8% (well under ceiling), Day% -1.3% (fresh AH move), VRatio 5.3, tradable=true, float 26.2M (high).
- **But it is a spike-and-drift, not a build.** AH high **$3.08 @ 16:35 ET** (early, before 17:00) on the 16:15–16:35 spike, then volume **dried up**: recent SIP bars (17:00–18:15 ET) are 657–41K sh / 10–216 trades each — textbook thin drift (tens-of-K sh, tens–low-hundreds of trades). Total AH vol crept 591K → 727K → 757K over the last hour (barely any new volume). Current ~$2.62–2.66 holds within ~14% of $3.08 but on essentially no volume. `CONFIRM-3 NO`.
- Trajectory dominates: early peak (16:35 ET) + thin declining volume = SPIKE→FADE class (0/6+ for PM continuation). **Verdict: SKIP.** Catalyst: none found earlier; trajectory is the skip regardless.

**GWAV — new AH>10% name, SKIP (illiquid / no AH book + dead-cat + thin print).**
- First AH appearance. Day% **-16.2%** (below the -15% threshold → dead-cat territory). AH vol **5K** / VRatio 0.1 (40K avg) — no real AH accumulation. SPIKE-BAR reads only 22 trades / 1k sh (thin/bad print). Quote **stale** (bid $2.25 / ask $4.34 @ 16:00 ET, 2.5h behind) — huge spread, no fillable AH book. Float 219K (micro). No dead-cat-override (only 1 AH scan, illiquid — not a volume-backed reclaim). **Verdict: SKIP** as illiquid + dead-cat + thin.

**RETO — carried skip (first-bar spike + extreme extension).** AH $4.06, +45.0% AH chg — bounced back toward the $4.73 first-bar high (~14% off) but still **+1025.6% total extension** from prev close ($0.36), ~7× the +150% ceiling. Two blocks unchanged: extension far above ceiling (no ceiling-override — AH high was the first 16:00 bar) + first-bar spike (CONFIRM-3 NO every scan). **FIRST-BAR-SPIKE WATCH** continues (hypothetical entry $4.50 @ 22:15 CET; now $4.06 = -9.8%).

**TPST — carried skip (SPIKE→FADE).** AH $1.05, +39.2% AH chg — bounced but still ~39% below the $1.73 spike high (16:20 ET); ignition volume declined into the fade. Weak Grade C catalyst (H.C. Wainwright conference presentation). CONFIRM-3 NO. Skip continues.

**PDSB — carried skip (Grade D dilution + multi-session runner), now sub-threshold.** AH +6.5% (fell below the 10% threshold; was +15.3% at 23:30). Grade D PIPE financing, multi-session runner (+183% ~1 week ago on the same PIPE), float 55.0M, VRatio 0.1. Skip stands on every count.

**Open positions (entered 23:00; excluded from new entries — exits handled by premarket position-evaluation):**
- **WAFU** — entered $2.21, now $1.73 (Alpaca P&L **-21.7%**). AH Chg $2.59 → $1.88; faded hard off the $3.25 AH high, as the intra-window borderline-hold concern flagged at entry. Grade None.
- **YFOR** — entered $1.55, now $1.71 (Alpaca P&L **+10.3%**). AH $1.79; holding above entry. Grade None.

**Sub-threshold / no-accumulation (skip):** STAK +6.1%, BURU +5.0% (Day -11.1%, Total -6.7%), WWR +7.2%, TOPS +5.2%, CDZI +9.1% — all below the 10% AH threshold or no AH accumulation.

**Final-scan feed-lag cross-check (pipeline names):** All tracked AH names this night (RETO, WAFU, TPST, MEDS, YFOR, WNW, PDSB) are present in the 18:30 ET scan — no TradingView under-report/omission to rescue. MEDS surfaced at 00:00 (feed-lag from its 17:20 ET ignition) and is present again here. No new omitted igniter on SIP. **No FINAL-SCAN-GATE-BLOCK:** the only first-appearance name (GWAV) fails multiple entry rules (illiquid, Day% <-15%, thin) — it is not a genuine late igniter blocked solely by the gate.

**VEEA** — open position (28 sh @ $3.38, now $5.57, +64.8%), handled by position-evaluation; excluded from entries.

**End of scheduled scans.** Tonight's entries: WAFU (23:00, $2.21, now -21.7%) and YFOR (23:00, $1.55, now +10.3%). Exits handled by premarket position-evaluation. Morning-eval to check the FADE-SKIP WATCH on MEDS (skipped the night's only CONFIRM-3 YES on the hold-vs-fade + extension-at-ceiling rules) and the RETO FIRST-BAR-SPIKE WATCH.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
| WAFU | $2.21 | 23:00 CET (17:00 ET) | 38 | 4ea8860f | Grade None. Float 3.0M, VRatio 8.5, 2-AH-scan gate met, real volume-backed BUILD (new AH high $3.25 @16:35 ET), Total% +88.8% under ceiling, fresh day-1 igniter. No fresh catalyst (AI PR is Aug 10-11). Favorable fill below stale scanner $2.59. |
| YFOR | $1.55 | 23:00 CET (17:00 ET) | 57 | ce1c6258 | Grade None. Float 1.6M, VRatio 3.0, 2-AH-scan gate met (building +10.7%→+42.1%), accelerating BUILD (1.79M sh/14.9k tr @16:45 making new high $2.15), Total% +38.2%, fresh day-1 igniter. No fresh catalyst (only Aug 31 rebrand). Favorable fill below scanner $1.99. |

## Morning Evaluation — 10:20 CET (Sep 16, evaluating Sep 15 AH session)

### Today's Winner

**RETO** — Other Metals/Minerals (ReTo Eco-Solutions, Chinese eco/construction-materials micro-cap)
- Catalyst: **None verified** — QuiverQuant: "heavy speculative trading with no clear fresh catalyst." Ran +676% in the regular Sep 15 session ($0.361→$2.80) with no company-specific driver. Grade None.
- Previous Close (regular Sep 15): **$2.80** (correct basis). Yahoo `previousClose` $0.36 is the **stale Friday close** — RETO's +676% regular-session run made it diverge; measuring from $0.36 gives a fictional "+1150-2079%." All AH→PM math below uses $2.80.
- AH last night: **SIP high $8.00 @ 16:05 ET (22:05 CET)** on **5.5M sh / 45,900 trades** = **+185.7% from $2.80** (16:05 bar VWAP $5.97 = +113%). Faded to ~$2.80 by 16:35 ET, rebuilt to ~$4.58 by end of AH.
- Premarket now: **SIP high $5.52 @ 04:00 ET = +97.1%** (2.57M sh / 35,716 trades), now fading ~$3.86–4.39.
- Hypothetical P&L (AH entry → PM peak): realistic post-spike AH entry ~$3.00–3.13 (16:35–17:00 ET) → PM peak $5.52 = **+76–84%**; the 16:05 first-bar spike itself hit $8.00 = +186% intra-AH. **AH peak ($8.00) exceeded the PM peak ($5.52)** → AH was the better exit (extreme-runner fade).
- Float: 35.8M | Market Cap: $103.2M
- Winner-bar check: **CLEARED** — AH high $8.00 = +185.7% on massive accumulating SIP volume (5.5M sh, 45,900 trades in one 5-min bar). Capturable — genuine two-sided fillable book (bid $4.44 x200 / ask $4.50 x300 @ 16:15 ET), not a phantom. Note SIP high $8.00 > Yahoo $6.06 — Yahoo under-reported the peak; SIP used.

**Scanner Diagnostic:**
- Detectable at screening time? **YES** — RETO was in **every scan** (21:30 → 00:30 CET). At 22:15 CET (16:15 ET) it was explicitly flagged as a real AH igniter with the SIP first bar (5.76M sh / 35,514 trades) and a fresh two-sided book. Detection was perfect.
- Why we didn't act (two independent, correct blocks): (1) **Extreme extension** — Total% far above the +150% ceiling (even from the true $2.80 close, RETO layered an AH spike on top of a +676% regular-session run; no overnight margin). (2) **First-bar spike** — AH high printed in the first 16:00–16:05 bar, CONFIRM-3 NO every scan. It was logged as a **FIRST-BAR-SPIKE WATCH** (hypothetical entry $4.50 @ 22:15 CET).
- Scanner gap: **NONE.** The scanner detected the winner flawlessly. This is a *detected + correctly-skipped* winner (BTCT/DAIC/WVVIP class), not a detection failure. RETO's AH $8.00 → PM $5.52 fade validates the extension skip; the first-bar-spike WATCH did run modestly (see tracker).

**Winner selected for paper trade?** No. We entered WAFU and YFOR (both Grade None day-1 igniters); RETO — the >100% winner — was correctly un-enterable per our rules (first-bar spike + extreme extension). No other >100% capturable-and-ruleable winner existed.

**Broker-block tracking:** No new case. RETO/WAFU/YFOR/MEDS all `tradable=true`. Standing unchanged (SHPH ×2).

**Stale-book execution-block tracking:** No new case. WAFU/YFOR filled; no `tradable=true` name was blocked solely by a stale quote through the final scan. **Standing count: 3** (NUWE, KUST, CLRO), all profitable — unchanged.

**No-fillable-book skip tracking:** No new case tonight (RETO had a real fillable book; it was skipped on extension/first-bar-spike, not liquidity). **Standing count: 2** (OFAL, BIVI), both faded — unchanged.

**Float-gate skip tracking:** No new case (no name blocked purely on float >50M). **Standing count: 1** (CAPR ran) — unchanged.

**Final-scan gate-block tracking:** No new case — the only final-scan first-appearance name (GWAV) failed multiple rules (illiquid, Day% −16.2%, thin), not a genuine late igniter blocked solely by the 2-scan gate. **Standing count: 2** (TRUG, UPC, both ran) — unchanged.

**Multi-session-runner outcome tracking:** Two entries tonight, both **fresh first-day igniters**:
- **WAFU** (day 1, Day% +1.5% pure-AH ignition, Grade None, entered $2.21 → PM peak $1.93 SIP = **−12.7%, faded** below entry).
- **YFOR** (day 1, Day% −2.8% pure-AH ignition, Grade None, entered $1.55 → PM peak $1.87 SIP = **+20.6%, ran**).
**Standing: 1 multi-session runner (1 faded: DAIC) / 22 first-day igniters (8 ran: WNW, AEMD, GPRO, PETZ, SSM, PLAG, VEEA, YFOR; 6 flat: PXS, TLYS, CHPT, SUNE, CULP, HCAI; 8 faded: MODD, LABT, KITT, UFG(Sep2), GELS, GIPR, UFG(Sep9), WAFU).** First-day run rate 8/22 (36%) — "fresh igniters follow through" stays weak. Data collection only; no gate change.

**First-bar-spike skip-validation tracking:** **RETO** post-gate WATCH — first-bar spike (AH high $8.00 @16:05 ET, CONFIRM-3 NO every scan), hypothetical entry $4.50 @ 22:15 CET → PM SIP peak $5.52 = **+22.7%, ran** (above the $4.73 first-bar 16:00-bar high; below the $8.00 16:05 spike). **Routed to Juan's daily email** per the tracker rule (a WATCH that ran). Caveat: RETO's dominant, co-equal block was the **extreme extension ceiling** — relaxing the first-bar-spike gate alone would not have entered it, and the AH $8.00 → PM $5.52 fade shows the extension skip was right. **Standing: 3 pre-gate entries (0 ran: LABT, SUNE, HCAI-Sep10) + 3 post-gate WATCH (2 ran: XRTX, RETO; 1 faded: HCAI-Sep15).** Overall 4 of 6 fade-or-flat — gate holds; the two runs (XRTX, RETO) are both extension/dead-cat co-blocked, not clean first-bar-spike-only misses. Record + route, no gate change.

### Baseline Tracking

- Days tracked: **83** (was 82 + 1 — Sep 15 session only; Sep 11 Friday still NOT back-filled, prior baseline gap unchanged)
- Winners detected by scanner: **69/78 (88.5%)** — +RETO (detected in all 9 scans; correctly skipped on first-bar-spike + extreme extension)
- Winner selected for paper trade: **35/76 (46.1%)** — RETO (the >100% winner) was correctly un-enterable per rules; WAFU/YFOR entered but are not the winner
- Target: >80% detection
- Status: **BASELINE MET** (88.5% detection)

### Retrospective Scan Results

- **Live PM scan (04:20 ET):** 6 hits — RETO +70.7% ($4.78), TPST +49.5% ($1.13), WAFU +21.6% ($1.69), YFOR +20.7% ($1.69), MEDS +9.3% ($1.77), PDSB +5.7% ($0.62). All had AH footprints last night — no PM-only gapper dominates.
- **Forced AH scan (secondary diagnostic):** 0 hits (expected — TradingView postmarket feed returns 0 overnight).
- **AH reconstruction (SIP):** RETO the clear winner (AH $8.00 → PM $5.52, both on multi-million-share bars). WAFU/YFOR/TPST/MEDS all faded AH→PM.

### Open Position P&L (Alpaca)

Real Alpaca fills. VEEA carried from the Sep 14 session (handled by position-evaluation); WAFU/YFOR are Sep 15 entries. Exits are NOT made here.

| Ticker | Entry | Entry Total% | Catalyst | Entry Time | PM Peak | Peak Time | Exit | P&L | P&L % | Status |
|--------|-------|--------------|----------|------------|---------|-----------|------|-----|-------|--------|
| VEEA | $3.38 | — (Sep 14) | A — Veea+NovaGen merger term sheet + GeoNova $10M | Sep 14 23:00 CET | $5.84 | 04:00 ET | (open) | +$51.21 | +54.1% | 🟢 Open (carried) |
| WAFU | $2.21 | +59.0% | None | 23:00 CET | $1.93 | 04:00 ET | (open) | −$20.14 | −24.0% | 🔴 Open, PM never reclaimed entry |
| YFOR | $1.55 | +10.7% | None | 23:00 CET | $1.87 | 04:00 ET | (open) | +$7.98 | +9.0% | 🟢 Open, above entry |

PM peaks verified against SIP 5-min bars (Sep 16 08:00Z). VEEA `current_price` $5.21 matches live SIP PM (~$5.26) — not stale. WAFU ($1.68) and YFOR ($1.69) match SIP PM — fresh.

**Total Realized P&L (Alpaca fills only): €0.00** (no exits this session — all positions open, exits handled by position-evaluation at 10:30/14:30 CET).

### Scanner Effectiveness

- Evening scans ran: **7 of 7 scheduled** (21:30, 22:00, 22:30, 23:00, 23:30, 00:00, 00:30 CET) + 2 extra observation scans (22:15, 22:45) = 9 total. **Full coverage of the entry window.**
- Candidates found: ~13 unique tickers across the night (RETO, WAFU, TPST, YFOR, MEDS, PDSB, WNW, BNGO, STAK, VRA, MYSZ, GWAV, others).
- Retrospective matches: every PM mover (RETO, TPST, WAFU, YFOR, MEDS, PDSB) was in the evening scans. 6/6.

### Missed Opportunities

No significant missed opportunities. Every PM mover was detected in the evening scans. The winner (RETO) was detected in all 9 scans and correctly skipped on entry rules.

### AH Mover Follow-Through

Stocks in 2+ evening scans with AH change >10%:

| Ticker | AH Peak | Peak Time | AH Trajectory | Current PM | From Peak | From Close | Verdict |
|--------|---------|-----------|---------------|------------|-----------|-----------|---------|
| RETO | $8.00 (+185.7%) | 16:05 ET | Spike→fade→rebuild | $5.52 PM peak / ~$3.86 now | −31% | +97.1% (PM peak) | **AH was better exit** (extreme-runner fade) |
| WAFU | $3.25 (+133.8%) | 16:35 ET | Spike→fade | $1.93 PM peak | −41% | +38.8% (PM peak) | **AH was better exit** (borderline extreme-zone fade) |
| TPST | $1.73 (+127.6%) | 16:20 ET | Spike→fade | $1.28 PM peak | −26% | +68.4% (PM peak) | **AH was better exit** |
| YFOR | $2.15 (+53.6%) | 16:45 ET | Build→fade | $1.87 PM peak | −13% | +33.6% (PM peak) | AH was better exit (modest) |
| MEDS | $2.69 (+66.0%) | 17:30 ET | Late build→fade | $1.92 PM peak | −29% | +18.5% (PM peak) | AH was better exit |

**AH-peak-vs-PM-peak check (extreme-runner fade tally):** RETO (AH +185.7% > PM +97.1%) is a clean extreme-zone (>+130%) fade; WAFU (AH +133.8% > PM +38.8%) is a borderline extreme-zone fade. **Standing: 10 fade (MSW, DSY, AQB, XOS, BTCT, LOOP, DAIC, AMIX, RETO, WAFU) / 1 continue (BAOS)** = 11 cases, 91% fade. Routing trigger (≥9 cases at ≥85% fade) remains **REACHED** — partial-profit-on-extreme-runners recommendation already routed to Juan's daily email; exit rule is his domain, unchanged here.

**MEDS FADE-SKIP WATCH outcome:** hypothetical entry $2.15 @ 00:30 CET (18:30 ET) → PM SIP peak $1.92 = **−10.7%, faded. Skip validated (0 cost).** Skipping the night's only CONFIRM-3 YES on the hold-vs-fade + extension-at-ceiling rules was correct.

**Chase-cap / entry-extension outcome tracking:** No new case. WAFU (fill +59.0% vs qualifying +88.8%) and YFOR (fill +10.7% vs qualifying +38.2%) both filled *below* the qualifying scan price (favorable stale-book artifact), not chased into the >+120% fade zone. **Standing count: 1** (XOS, never-reclaimed) — unchanged. Note WAFU's fill was never reclaimed in PM (−24%), but that is entry-into-a-fader, not a chase.

### Notes

- **Winner is a detected-and-correctly-skipped case.** RETO cleared +185.7% AH on 5.5M sh/45,900 trades (real, liquid) but was a first-bar spike layered on a +676% regular-session run — extension ~5-8× the ceiling. The scanner's detection is perfect; the entry rules correctly avoided chasing it, and the AH $8.00 → PM $5.52 fade confirms the skip. Detection baseline stays healthy at 88.5%.
- **Prev-close basis correction applied (recurring guard).** Yahoo/`price-timeline.py` used the stale $0.36 Friday close for RETO, inflating the move to "+2079%." True basis is the $2.80 regular Sep 15 close (confirmed by the SIP AH first-bar open $2.80). All winner math uses $2.80. This is the post-run analog of the BNC post-weekend basis case — a hard-running regular session leaves Yahoo's `previousClose` stale.
- **PM-only gapper:** none dominates today; the biggest raw PM mover (RETO +70.7%) is an AH→PM continuation the scanner detected. Holdable PM-only count in `log/pm-open-scan.csv` = **54** (cluster long past the ≥3–4 threshold; already routed as the Initiative-6 early-PM pilot decision to Juan's email).
- **Coverage:** 7 of 7 scheduled scans ran (+2 extra) — no coverage failure. Coverage-failure tally unchanged.
- **In-window feed-lag miss tally:** no new case (RETO surged in-window at AH open and was surfaced). **Standing count: 5** (BTCT, KUST, WLDS, RAIN, MYSZ) — trigger REACHED, AH-data-source cross-check already routed to Juan's email.
- **Routed to Juan's daily email this pulse:** (1) RETO first-bar-spike WATCH that ran (+22.7%), with the extension-co-block caveat; (2) re-statement of the standing extreme-runner-fade (10/11) and in-window feed-lag (5) recommendations already open.

### Price Charts

**RETO** (basis note: `price-timeline.py` uses stale $0.36; true basis $2.80):
- 2-Day Range: $0.35 – $7.86 (Yahoo; SIP AH high $8.00). Peak $7.86 @ 09-15 16:05 ET (the AH-open first-bar spike). PM 04:00 ET $4.66 → faded to $3.49 → ~$3.78.
- Shape: massive AH-open spike to $8.00, faded to ~$2.80 by 16:35 ET, choppy $3.80–4.40 all overnight, PM re-poke to $5.52 then fade. Classic extreme first-bar spike + overnight fade.

**WAFU** (prev close $1.37): range $1.32–$3.25, peak $3.25 (+137.2%) @ 16:35 ET, now ~$1.72. Spiked AH then faded below the $2.21 entry.

**YFOR** (prev close $1.44): range $1.36–$2.15, peak $2.15 (+49.3%) @ 16:45 ET, now ~$1.68. Built into the entry, PM held above the $1.55 fill.
