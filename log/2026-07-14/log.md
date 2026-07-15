# Trade Log — 2026-07-14

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| VMAR | $1.57 | $2.22 (fill) | +41.4% | $3.35 (+114%) | 1 | None | SELL | Grade None = exit at any profit. PM peaked $3.35 then dumping. |
| LVLU | $11.03 | $10.01 | -9.2% | $11.99 (+8.7%) | 1 | B | HOLD | Day 1 of 2; above -15% stop ($9.38); peak <+30% so no trail; catalyst intact. |

**Actions taken:**
- SELL 62 VMAR @ limit $2.15 ext (id edb17587) → filled **$2.22**. P&L +$40.30 (+41.4%).
- VMAR verified real via SIP: 4.5M sh in first PM bar, 37,981 trades on a 670K-float name. Peaked $3.35 at PM open, faded fast ($3.35→$2.94→$2.62→$2.23). Classic PM peak-then-dump — exited into the fade.
- LVLU held: Grade B, day 1 of 2, -9.2% is above the -15% hard stop. PM liquidity thin (7.3K sh in first PM bar). Re-evaluate at 14:30 CET pulse.

## Position Evaluation — 14:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| LVLU | $11.03 | $9.44 | -14.4% | $11.99 (+8.7%) | 1 of 2 | B | HOLD | Above -15% hard stop ($9.38); day 1 of 2; catalyst intact |

**Actions taken:**
- No sells. LVLU held per Grade B rule (hold up to 2 days).
- Data reconcile: Alpaca quote feed stale (07-13 20:00Z close, wide $6.55/$10.36 book). Used Alpaca `current_price` $9.44 (-14.4%) as P&L basis; SIP PM bars show latest ~$9.75-9.80 (-11.6%). SIP feed latest 11:55Z (07:55 ET) confirms premarket.
- LVLU never gave a PM spike above entry to exit into profit (OVN peak only +8.7%). Faded from $11.50 PM open to ~$9.75. Now sitting just above the hard stop.
- **Flag for next pulse:** if LVLU prints below $9.38, sell per Grade B hard-stop rule.

## Scan 21:30 CET (3:30 PM ET) — REGULAR session, pre-AH

AH not open yet (opens 22:00 CET / 4:00 PM ET). No paper entries per regular-session caution rule. Candidates below are **Watch — pending AH confirmation**; only actionable if they reappear in a 22:00+ CET AH scan with sustained momentum.

| Ticker | Price | Chg% | 5mVol | IRVol | Float | MCap | Industry | Note |
|--------|-------|------|-------|-------|-------|------|----------|------|
| CNEY | $0.66 | +38.2% | 278K | 293.9 | 5.0M | 3.7M | Electrical Products | Real vol + low float — watch AH |
| CRMT | $4.16 | +37.7% | 43K | 9.8 | 7.6M | 34.5M | Specialty Stores | Real vol — watch AH |
| SHPH | $4.09 | +38.3% | 11K | 180.4 | 596K | 2.6M | Pharma: Major | Untradable on Alpaca (carried, `tradable=false` all prior nights) — skip |
| NIXX | $1.47 | +28.9% | 63K | 1.2 | 24.1M | 42.8M | Personnel Services | Watch AH |
| LOOP | $1.03 | +21.6% | 25K | 5.6 | 26.5M | 49.8M | Chemicals: Specialty | Watch AH |
| NXTC | $6.04 | +176.8% | 100 | 639.9 | 2.4M | 7.9M | Pharma: Major | Thin (100 sh/5m) — likely halt artifact, monitor AH |
| LEDS | $2.17 | +42.8% | 300 | 4918.6 | 3.4M | 17.9M | Semiconductors | Thin print — monitor AH |

Rest of the 63-hit scan was thin regular-session prints (single/low-hundred share 5m vol) or downside movers (SPRO -20%). LVLU (+7.9%, $8.98) appears but is an open managed position (Grade B, day 1 of 2) handled by position-evaluation. No action here.

**Next AH scan ~22:15 CET** will re-run with real extended-hours volume/VRatio and evaluate entries.

## Scan 22:00 CET (4:00 PM ET) — AH open

**No candidates found.** Scanner returned 0 hits with real extended-hours volume.

None of the 21:30 regular-session watch candidates (CNEY, CRMT, NIXX, LOOP, NXTC, LEDS) reappeared in the AH scan — their intraday spikes did not carry into after-hours with sustained volume. Per regular-session caution rule, no entries.

First AH scan of the night; observation only per learning-phase default (no entries before 23:00 CET). Next scan ~22:30 CET.

## Scan 22:30 CET (4:30 PM ET) — AH

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| XCUR | [TV](https://www.tradingview.com/chart/?symbol=XCUR) | $1.72 | +4.2% | +39.0% | $2.39 | +44.8% | 1.2M | 179K | 6.6x | 4.2M | Biotechnology |
| BTTC | [TV](https://www.tradingview.com/chart/?symbol=BTTC) | $0.80 | +5.9% | +8.7% | $0.87 | +15.1% | 145K | 51K | 2.8x | 1.9M | Packaged Software |

**Observation only (before 23:00 CET) — no entries this scan.**

**XCUR (Exicure, Inc.) — strong watch for 23:00 entry scan:**
- **Verified real via SIP:** AH bars show genuine accumulation — 20:05Z 164K sh/1,040 trades, 20:10Z 1.27M sh/10,369 trades, 20:15Z 1.45M sh/12,099 trades. Real two-sided book (bid $2.37 x100 / ask $2.40 x100). `tradable=true`. SIP VWAP $2.36 / high $2.50 corroborates scanner AH price $2.39. Not a stale VRatio or bad print.
- **Trajectory: BUILD** — $1.72 → $2.09 → $2.39, peaked $2.50 at 20:15Z, now ~$2.38. Building across the first three AH bars, not a spike-fade. Day% +4.2% (positive — not a dead-cat bounce).
- **Total% +44.8%** — well under the +150% extension ceiling.
- **Float 4.2M** (ideal <10M range).
- **Catalyst: NONE found (4-search budget exhausted).** Distressed biotech: 66% workforce reduction + halted R&D (June), Nasdaq minimum-equity ($2.5M) non-compliance notice (June 5), plan-to-regain-compliance deadline **July 20, 2026**. No same-day PR/8-K found driving the +39% move. The looming July 20 deadline raises dilution/reverse-split risk → Grade None (exit at first opportunity) if entered. Per no-catalyst handling, enter with concern noted at 23:00+ if it holds the build.
- **Plan:** if XCUR reappears at 23:00 CET still building/holding within ~20% of its AH high, it clears all entry gates (float <50M, AH >10% across 2 AH scans, Day% > -15%, Total% < 150%, real SIP liquidity) — enter a paper trade then.

**BTTC — skip:** no fillable AH book (`ask $0.00 x0`) and AH chg only +8.7% (below the 10% threshold). Illiquid ramp.

Next scan ~23:00 CET — first entry-eligible scan of the night.

## Scan 23:00 CET (5:00 PM ET) — AH, first entry-eligible scan

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| XCUR | [TV](https://www.tradingview.com/chart/?symbol=XCUR) | $1.72 | +4.2% | +33.1% | $2.29 | +38.8% | 5.9M | 744K | 7.9x | 4.2M | Biotechnology |
| CRDF | [TV](https://www.tradingview.com/chart/?symbol=CRDF) | $1.31 | -3.0% | +5.3% | $1.38 | +2.2% | 77K | 827K | 0.1x | 62.5M | Medical Specialties |

**XCUR (Exicure) — ENTERED paper trade. Filled 41 sh @ $2.40 (id 13d1b6bb).**
- All entry gates cleared: float 4.2M (<50M ✓), AH >10% across 2 AH scans (22:30 +39%, 23:00 +33.1% ✓), Day% +4.2% (> -15% ✓, positive = not dead-cat), Total% +38.8% (< 150% ceiling ✓), real SIP liquidity ✓.
- **Verified fresh & real:** `tradable=true`; live two-sided book bid $2.39 x100 / ask $2.42 x100 @ 20:59:57Z (fresh vs scan). SIP bars show sustained accumulation across the whole AH session — 20:25Z 1.60M sh/10,996 trades ($2.55 H), 20:45Z 1.09M sh/7,818 trades ($2.52 H). Volume not fading; rebuilding toward highs. VWAP $2.43.
- **Trajectory: BUILD-and-hold.** Built $1.72→$2.50 (20:15), pulled to $2.22, rebuilt to $2.55 (20:25), consolidated $2.26-2.29, pushed back to $2.52 (20:45). Current ~$2.40 = within ~6% of AH high $2.55 → holding qualifies.
- **Catalyst: NONE found** (4-search budget exhausted at 22:30 scan). Distressed biotech: 66% workforce cut + halted R&D (June), Nasdaq min-equity non-compliance notice, regain-compliance deadline **July 20, 2026**. No same-day PR/8-K driving the +33% move. Looming July 20 deadline raises dilution/reverse-split risk. **Grade None → exit at first premarket opportunity.** Entered with concern noted per no-catalyst learning-phase handling.
- QTY = floor(100 / 2.42) = 41 sh. Limit $2.46 (above ask for thin AH book), filled $2.40.

**CRDF — skip:** AH chg +5.3% (below 10% threshold), VRatio 0.1x (no real AH volume — 77K vs 827K avg), float 62.5M, wide illiquid book (bid $1.07 / ask $1.54, quote stale @ 20:00Z). Not a real AH spike.

Next scan ~23:30 CET.

## Scan 23:30 CET (5:30 PM ET) — AH

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| XCUR | [TV](https://www.tradingview.com/chart/?symbol=XCUR) | $1.72 | +4.2% | +31.4% | $2.26 | +37.0% | 8.7M | 1.1M | 8.1x | 4.2M | Biotechnology |
| VTAK | [TV](https://www.tradingview.com/chart/?symbol=VTAK) | $0.56 | -13.9% | +31.8% | $0.74 | +13.5% | 2.8M | 24.2M | 0.1x | 2.0M | Medical Specialties |
| TGHL | [TV](https://www.tradingview.com/chart/?symbol=TGHL) | $0.66 | +3.9% | +18.6% | $0.78 | +23.2% | 675K | 992K | 0.7x | 12.7M | IT Services |
| BTTC | [TV](https://www.tradingview.com/chart/?symbol=BTTC) | $0.80 | +5.9% | +10.0% | $0.88 | +16.4% | 290K | 68K | 4.3x | 1.9M | Packaged Software |

**No new entries this scan.** VTAK and TGHL are fresh real spikes but both fail the 2-AH-scan entry gate (first AH appearance). Watches for 00:00 CET.

**XCUR (open position, entered 23:00 @ $2.40) — update:** now $2.23 bid $2.39 / ask $2.42 (fresh @ 20:59:57Z), P&L -7.1%. AH price faded $2.29 (23:00) → $2.26 (23:30) off the $2.55 AH high. Grade None, managed by position-evaluation (premarket exit). No action here.

**VTAK (VirTra? — Medical Specialties) — WATCH for 00:00, not entered:**
- **Verified real via SIP:** fresh spike began 17:00 ET (21:00Z). Real accumulation across bars — 21:00Z 326K sh/814 trades, 21:05Z **1.40M sh/3,572 trades**, 21:10Z 1.11M sh/3,073 trades, 21:15Z 801K sh/2,093 trades. VWAP $0.70-0.77, high $0.80 corroborates scanner AH price $0.74. Not stale/bad print — the low VRatio (0.1x) is an artifact of a very high 24.2M avg volume, not thin AH liquidity.
- **Entry gate not met:** first AH-scan appearance (not in 22:00/22:30/23:00 AH scans) → fails the "AH >10% in ≥2 AH scans" requirement. Cannot enter this scan.
- Float 2.0M (ideal). Day% -13.9% (above -15%, and AH reclaims well above today's close — not a dead-cat bounce). Total% +13.5% (well under ceiling). Trajectory: BUILD (spike just starting, elevated at last bar). Catalyst: not yet searched (defer to 00:00 if it holds).
- **Plan:** if VTAK reappears at 00:00 CET still holding/building (2nd AH appearance), it clears the 2-scan gate — run catalyst search + book check and enter.

**TGHL (Ted Global Holdings — IT Services) — WATCH for 00:00, not entered:**
- **Verified real via SIP:** fresh spike began 17:00 ET (21:00Z). 21:05Z 199K sh/644 trades, 21:10Z **478K sh/1,552 trades**, 21:15Z 134K sh/606 trades. VWAP $0.73-0.80, high $0.86 corroborates scanner AH price $0.78. Real but smaller book than VTAK.
- **Entry gate not met:** first AH-scan appearance → fails 2-AH-scan requirement. Cannot enter this scan.
- Float 12.7M, Day% +3.9%, Total% +23.2% (under ceiling). Trajectory: BUILD. Quote book still wide ($0.56/$0.80, stale @ 20:00Z) — recheck live book at 00:00.
- **Plan:** if TGHL reappears at 00:00 CET holding/building, run catalyst search + confirm a real two-sided book, then enter.

**BTTC — skip (carried):** AH chg +10.0% marginal; still an illiquid ramp pattern (VRatio 4.3x on tiny 290K vol). No fresh two-sided book demonstrated. Same skip as 22:30.

Next scan ~00:00 CET.

## Scan 00:00 CET (6:00 PM ET) — AH

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| XCUR | [TV](https://www.tradingview.com/chart/?symbol=XCUR) | $1.72 | +4.2% | +32.0% | $2.27 | +37.6% | 9.3M | 1.1M | 8.2x | 4.2M | Biotechnology |
| VTAK | [TV](https://www.tradingview.com/chart/?symbol=VTAK) | $0.56 | -13.9% | +41.1% | $0.79 | +21.5% | 7.2M | 24.6M | 0.3x | 2.0M | Medical Specialties |
| GCTK | [TV](https://www.tradingview.com/chart/?symbol=GCTK) | $0.53 | +14.1% | +9.6% | $0.58 | +25.1% | 1.4M | 2.0M | 0.7x | 6.2M | Medical Specialties |
| TGHL | [TV](https://www.tradingview.com/chart/?symbol=TGHL) | $0.66 | +3.9% | +11.4% | $0.74 | +15.8% | 1.2M | 1.0M | 1.1x | 12.7M | IT Services |
| TOON | [TV](https://www.tradingview.com/chart/?symbol=TOON) | $0.59 | +0.3% | +6.9% | $0.63 | +7.2% | 239K | 3.2M | 0.1x | 56.0M | Movies/Entertainment |
| BCDA | [TV](https://www.tradingview.com/chart/?symbol=BCDA) | $0.80 | -11.9% | +9.0% | $0.87 | -3.9% | 52K | 554K | 0.1x | 10.2M | Biotechnology |

**VTAK (Catheter Precision) — ENTERED paper trade. Filled 125 sh @ $0.72 (id 3dbb0e53).**
- All entry gates cleared: float 2.0M (<50M ✓, ideal), AH >10% across 2 AH scans (23:30 +31.8%, 00:00 +41.1% ✓), Day% -13.9% (> -15% ✓; AH reclaims well above $0.56 close = not a dead-cat bounce), Total% +21.5% (< 150% ceiling ✓), real SIP liquidity ✓, tradable=true ✓.
- **Verified fresh & real via SIP:** spike began 17:00 ET (21:00Z) with sustained accumulation across every bar — 21:05Z 1.40M sh/3,572 trades, 21:10Z 1.11M/3,073, 21:30Z 1.37M/3,869, and still 677K/1,885 (21:40Z) and 466K/1,659 (21:45Z, latest). Volume NOT fading. VWAP $0.75-0.81, high $0.84 corroborates scanner AH price $0.79. The 0.3x VRatio is an artifact of the very high 24.6M avg regular volume, not thin AH liquidity. Alpaca quote feed stale (@ 20:00Z) but book shows non-zero sized ask ($0.70 x100) — passes liquidity sanity check.
- **Trajectory: BUILD-and-hold.** $0.56 → $0.72 → new high $0.84 at 17:30 ET (21:30Z), holding $0.72-0.81 across the last four bars. Current ~$0.72-0.76 within ~10-14% of the AH high → holding qualifies. Peaked 17:30 (before 18:30) but building/holding, not fading — hold-vs-fade is the primary signal.
- **Catalyst: NONE fresh (4-search budget used).** Flyte/LifeVac partnership + patent news drove the stock July 6-8, but no same-day (July 14) PR/8-K/earnings found driving the +41% AH move. **Notable squeeze setup:** short interest up 606% in June on a 2.0M float — today's spike is a squeeze/continuation, not fresh news. **Grade None → exit at first premarket opportunity.** Entered with concern noted per no-catalyst learning-phase handling.
- QTY = floor(100 / 0.80) ≈ 125 sh. Limit $0.82 (above real ~$0.76 price for thin AH book), filled $0.72.

**TGHL (Ted Global Holdings) — skip: SPIKE→FADE.** 2nd AH appearance (23:30 +18.6%, 00:00 +11.4%) clears the 2-scan gate, but trajectory disqualifies. SIP: peaked $0.86 at 17:10 ET (21:10Z, 478K sh/1,552 trades), then volume faded hard — 134K (17:15), 60K (17:20), 30K (17:25), a secondary push to $0.85 at 17:30 on lower 145K vol, then back down to 36-58K/bar and price $0.73. Declining volume + pre-17:30 peak + fading price = SPIKE→FADE (0/10+ for PM continuation). Skip rather than enter the weaker of the two candidates. Float 12.7M.

**GCTK, TOON, BCDA — skip:** AH chg below the 10% threshold (+9.6%, +6.9%, +9.0%). Not entry-eligible.

**XCUR (open position, entered 23:00 @ $2.40) — update:** now ~$2.13, P&L -11.3%. AH faded $2.29 (23:00) → $2.27 (00:00) off the $2.55 AH high. Grade None, managed by position-evaluation (premarket exit). No action here.

Next scan ~00:30 CET.

## Scan 00:30 CET (6:30 PM ET) — AH

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| GCTK | [TV](https://www.tradingview.com/chart/?symbol=GCTK) | $0.53 | +14.1% | +77.7% | $0.94 | +102.8% | 17.9M | 3.8M | 4.7x | 6.2M | Medical Specialties |
| XCUR | [TV](https://www.tradingview.com/chart/?symbol=XCUR) | $1.72 | +4.2% | +20.3% | $2.07 | +25.5% | 9.8M | 1.2M | 8.2x | 4.2M | Biotechnology |
| VTAK | [TV](https://www.tradingview.com/chart/?symbol=VTAK) | $0.56 | -13.9% | +23.2% | $0.69 | +6.1% | 8.7M | 24.8M | 0.4x | 2.0M | Medical Specialties |
| VMAR | [TV](https://www.tradingview.com/chart/?symbol=VMAR) | $1.32 | -6.4% | +8.3% | $1.43 | +1.4% | 1.5M | 15.5M | 0.1x | 670K | Recreational Products |
| TGHL | [TV](https://www.tradingview.com/chart/?symbol=TGHL) | $0.66 | +3.9% | +7.4% | $0.71 | +11.5% | 1.3M | 1.1M | 1.2x | 12.7M | IT Services |
| BTTC | [TV](https://www.tradingview.com/chart/?symbol=BTTC) | $0.80 | +5.9% | +6.2% | $0.85 | +12.5% | 305K | 69K | 4.4x | 1.9M | Packaged Software |
| BCDA | [TV](https://www.tradingview.com/chart/?symbol=BCDA) | $0.80 | -11.9% | +8.8% | $0.87 | -4.1% | 52K | 554K | 0.1x | 10.2M | Biotechnology |

**GCTK (Glucotrack) — ENTERED paper trade. Filled 101 sh @ $0.87 (id 1afba3d0).**
- All entry gates cleared: float 6.2M (<50M ✓, ideal <10M ✓), Day% +14.1% (> -15% ✓, positive = not dead-cat), Total% +102.8% (< 150% ceiling ✓), real SIP liquidity ✓, tradable=true ✓.
- **AH >10% across scans — substance met via SIP despite scanner lag:** GCTK appeared at 00:00 at scanner +9.6% ($0.58) and 00:30 at +77.7% ($0.94). The 00:00 reading was **feed-lag** — SIP 22:00Z bar (18:00 ET = the 00:00 scan window) already showed real price $0.80-0.85 (+51% AH). Real AH% was >10% at both the 00:00 and 00:30 windows. Per the freshness guard (USDE basis), do not skip a real fresh building spike on a scanner-lag technicality.
- **Verified fresh & real via SIP:** massive accelerating accumulation — 21:40Z 1.39M sh/3,990 trades, 21:45Z 1.99M/4,922, 21:50Z 2.98M/8,022, 21:55Z 2.85M/7,702, 22:00Z 2.91M/8,273, 22:05Z 3.55M/9,324, 22:10Z 3.66M/10,401, 22:15Z (latest, 18:15 ET) 3.16M/9,166 @ $0.96, VWAP $0.96, high $0.99. Volume NOT fading — accelerating into the latest bar. SIP high $0.99 corroborates scanner AH $0.94.
- **Trajectory: strong BUILD** — $0.55 → $0.99, making new highs at the latest bar (18:15 ET). Spike began 17:40 ET, still building into the 18:30 scan. Not a spike-fade.
- **Quote stale (freshness artifact, not illiquid):** Alpaca quote `ask $0.00 x0 @ 20:00:02Z` (16:00 ET) on two pulls — free-tier quote feed not updating for GCTK in AH. Fresh SIP (18:15 ET, 3.6M sh/bar, 10K trades/bar) proves a live fillable book. Not an illiquid ramp.
- **Catalyst: Grade A — completed strategic business combination.** GlobeNewswire same-day (July 14 AH): *"Glucotrack and Lōkahi Therapeutics Complete Strategic Business Combination, Establishing Lōkahi-Controlled Public Platform."* Major operational/structural event (reverse-merger-style combination) driving the +100% AH move on huge volume. Concern noted: reverse-merger structure carries dilution/control-change risk — managed by position-evaluation.
- QTY = floor(100 / 0.99) = 101 sh. Limit $1.03 (above SIP last for thin AH book), filled **$0.87** (book better than SIP last).

**XCUR (open position, entered 23:00 @ $2.40) — update:** AH faded further to +20.3% ($2.07), off the $2.55 AH high. Grade None, managed by position-evaluation (premarket exit). No action here.

**VTAK (open position, entered 00:00 @ $0.72) — update:** AH +23.2% ($0.69 scanner), holding above entry. Grade None, managed by position-evaluation. No action here.

**TGHL — skip (carried): SPIKE→FADE confirmed.** AH faded to +7.4% ($0.71), below threshold. Declining across scans (23:30 +18.6% → 00:00 +11.4% → 00:30 +7.4%). Same skip.

**VMAR, BTTC, BCDA — skip:** AH chg below the 10% threshold (+8.3%, +6.2%, +8.8%). VMAR is a prior sold position (fully exited 10:30 CET); BTTC illiquid ramp (carried); BCDA below threshold. Not entry-eligible.

Next scan ~01:00 CET.

## Morning Evaluation — 10:26 CET

### Today's Winner

**KUST** — Kustom Entertainment (Miscellaneous Commercial Services)
- Catalyst: **unverified** — sharp AH volume spike at 18:25 ET (445K→812K sh/bar, 3.5–4.5K trades/bar) points to a fresh news/PR drop; no evening research (never surfaced in scans).
- Previous Close: $0.97
- AH last night: peaked **$1.34 SIP (+38%)** at 19:50 ET; surge fired 18:25 ET (00:25 CET)
- Premarket now: peaked **$1.95 (+101.7%)** at 08:10 ET; currently ~$1.75–1.79 (+81–85%)
- Hypothetical P&L (AH entry $1.30 @ 18:30 ET → PM peak $1.95): **+50%**
- Float: 577K (ultra-low) | Market Cap: ~$633K (scan artifact)
- **SIP-verified real:** PM 08:00Z bar 4.10M sh / 30,537 trades, vwap $1.74; AH 18:30 ET bar 812K sh / 4,463 trades. Genuine liquidity both sessions, not a phantom ramp.

**Scanner Diagnostic:**
- Detectable at screening time (~22:15 CET)? At 16:15 ET KUST was +5.5% — **below threshold**. It crossed 10% only at 18:20–18:25 ET (00:20–00:25 CET) and hit **+34% at 18:30 ET = the 00:30 CET last scan**.
- Detectable at the final scan window? **YES (feed-lag).** At the 00:30 CET / 18:30 ET last scan KUST was already +34% on 812K sh of real SIP volume, but the TradingView postmarket feed did not surface it — same failure mode as GCTK the same night (GCTK we *did* rescue via SIP cross-check).
- Could it have been **entered**? **No.** It was above threshold in only the single last scan (fails the 2-AH-scan gate) and the surge was 5 min before that scan. Feed-lag, not a schedule gap — a later scan would not have helped.
- Scanner gap: at the final scan, cross-check the top raw AH movers against a second data source (Yahoo/SIP AH) to catch feed-lagged spikes. This is the recurring fix (KUST today, GCTK/BTCT before).

### Baseline Tracking

- Days tracked: **48** (was 47 + 1)
- Winners detected by scanner: **41/46 (89.1%)** — KUST added (detected, feed-lag substance at last scan). GMM still excluded (late-AH-tail).
- Winner selected for paper trade: **23/46 (50.0%)** — KUST not entered (feed-lag + single-scan, unenterable). We entered XCUR/VTAK/GCTK, none the top winner.
- Target: >80% detection
- Status: **BASELINE MET** (89.1%)

### Retrospective Scan Results

Live PM scan (04:20 ET, 6 hits): KUST +63.4% ($1.65), VTAK +56.4% ($0.88), GCTK +42.3% ($0.75), XCUR +15.1% ($1.98), VMAR +7.6%, BJDX +8.0%. AH reconstruction (SIP + Yahoo) identifies KUST as the best AH→PM trade: only name that both spiked in AH *and* made a fresh PM high on heavy real volume. GCTK peaked in AH (+106%) and faded to +42% PM (AH was the better exit). VTAK modest AH (+23%) → re-exploded PM (+42%).

### Open Position P&L (Alpaca)

Open positions only (managed by `position-evaluation.md` at 10:30/14:30 CET — **not** closed here). All `quote` endpoints returned stale 20:00Z books; `positions current_price` aligns with live PM levels (used below). LVLU has no PM trades — $8.89 is its last regular close.

| Ticker | Entry | Entry Total% | Catalyst | Entry Time | Current (live) | PM/AH Peak | P&L % | Status |
|--------|-------|--------------|----------|------------|----------------|------------|-------|--------|
| VTAK | $0.72 | +28.6% | None (squeeze, 2.0M float) | 00:00 CET | ~$0.85 | **PM $1.27 (SIP)** | **+17.6%** | 🟢 OPEN |
| XCUR | $2.40 | +39.5% | None (distressed biotech) | 23:00 CET | ~$2.05 | AH $2.55 > PM | −14.6% | 🔴 OPEN |
| GCTK | $0.87 | +64.2% | A — business combination | 00:30 CET | ~$0.70 | AH $0.99 > PM $0.75 | −19.5% | 🔴 OPEN |
| LVLU | $11.03 | carried | B — carried from 07-13 | 07-13 | $8.89 (last reg close) | OVN peak +8.7% | −19.4% | 🔴 OPEN (day 2) |

No exits taken here. XCUR and GCTK both peaked in AH and faded into PM (AH was the better exit); VTAK is the one continuation winner. **Total realized P&L (Alpaca fills today): €0.00** (no exits this pulse).

### Scanner Effectiveness

- Evening scans ran: **7 of 7** (21:30–00:30 CET). Full coverage, no coverage failure.
- Candidates found: XCUR, CRDF, VTAK, TGHL, BTTC, GCTK, TOON, BCDA, VMAR (+ regular-session watch CNEY/CRMT/SHPH/NIXX/LOOP/NXTC/LEDS).
- Retrospective matches: winner KUST **missed** (feed-lag at last scan). Entered names VTAK/GCTK/XCUR all caught.

### Missed Opportunities

| Ticker | AH Change | Why Missed | Would Be Profitable? |
|--------|-----------|------------|---------------------|
| KUST | +34% @ 18:30 ET | Feed-lag — real +34% mover on 812K sh at the 00:30 scan, TradingView PM feed did not surface it; surge fired 18:25 ET (5 min pre-scan), single scan only | Yes — hypo AH $1.30 → PM peak $1.95 = +50% (but unenterable: fails 2-scan gate) |

### AH Mover Follow-Through

| Ticker | AH Peak | Peak Time | AH Trajectory | Current PM | From Peak | From Close | Verdict |
|--------|---------|-----------|---------------|------------|-----------|------------|---------|
| VTAK | $0.84 (SIP) | 17:30 ET | Build→hold | $1.27 PM peak (SIP) | +51% | +95% | ✅ PM >> AH — big continuation |
| GCTK | $0.99 (SIP, +106%) | 18:15 ET | Spike→hold | $0.75 | −24% | +42% | ⚠️ AH peak > PM — AH was better exit |
| XCUR | $2.55 (SIP) | 20:15 ET | Build→fade | ~$2.05 | −20% | +19% | ⚠️ AH peak > PM — AH was better exit |
| TGHL | $0.86 (SIP) | 17:10 ET | Spike→fade | no PM trades | — | ~flat | Faded as predicted (correctly skipped) |

**AH-peak-vs-PM-peak check:** GCTK (AH +106% > PM +42%) and XCUR (AH peak > PM) both peaked in after-hours and faded into PM — two more data points for the "extreme AH runner fades into PM" pattern (though GCTK's +106% is below the >250% extreme-runner threshold from MSW). VTAK is the counter-case (PM > AH on a 2.0M float). Note: GCTK is Grade A yet still faded PM — strong catalyst did not prevent the AH→PM fade.

### Notes

- **VTAK PM peak under-reported by Yahoo (DCX pattern):** Yahoo `--pm-history` showed VTAK PM high $0.92, but SIP shows a real **$1.27** print at 04:05 ET on **6.13M sh / 27,277 trades** (vwap $1.04) — a genuine, liquid peak Yahoo missed. Our VTAK entry $0.72 → PM peak $1.27 = **+76% available** (currently faded back to $0.85, +17%). Flag for the 10:30 position-eval: VTAK already printed its optimal exit; it is fading off the peak.
- **KUST feed-lag miss (data-source fix, not schedule):** the winner was a real +34% / 812K-sh mover at the 00:30 CET last scan that TradingView's postmarket feed missed. This is the recurring feed-lag failure (KUST today, GCTK same-night rescued via SIP, BTCT Jun 29–30). The fix remains: at the final scan, cross-check top raw movers against a second AH source. KUST would still have been unenterable (single scan above threshold, surge 5 min pre-scan), so it costs detection cleanliness, not a tradeable entry.
- **PM-only gapper tracking:** biggest raw PM mover today = KUST (+63% PM), an **AH→PM continuation** (moved >10% in AH) — not a PM-only gapper. No PM-only gapper this session.
- **Late-AH-tail tally:** KUST logged as **feed-lag** (already +34% at 18:30 ET last-scan timestamp, feed missed it) — not a true-tail. Does not argue for an added late scan; argues for data-source verification. Joins BTCT (Jun 29–30) on the feed-lag side vs ORIS (true-tail).
- **Fade-rule false-negative tracking:** no sub-3M AH-fader was skipped-then-re-exploded tonight. VTAK (2.0M, AH build→hold) was **entered**, not skipped. TGHL (12.7M) faded as predicted. Standing sub-3M count unchanged at **3 of 4**.
- **Reverse-split-squeeze tracking:** none of tonight's entries (XCUR/VTAK/GCTK) had a reverse-split catalyst. No new row.
- **Broker-block tracking:** SHPH again flagged `tradable=false` in the 21:30 regular watch but never cleared AH gates (did not reappear in AH), so no qualifier this night. No new row.
- **Catalyst vs trajectory:** GCTK was the only Grade A entry and it faded PM (AH $0.99 → PM $0.75); the no-catalyst BUILD-and-hold VTAK (2.0M float) was the only PM winner. Continued weak support for "trajectory/float over catalyst grade."
- **Coverage:** 7/7 evening scans ran. No coverage failure.

### Price Charts

```
KUST — Previous Close $0.97 | 2-Day Range $0.92–$1.95
  Flat $1.00–1.06 (16:00–18:20 ET) → surge 18:25 ET → AH peak $1.34 (19:50 ET)
  → PM open $1.50 → PM peak $1.95 (+101.7%) at 04:10 ET on 3.2M sh/19K trades
  Current ~$1.79 (+85%). Clean AH build → PM continuation to fresh high.

GCTK — Previous Close $0.46 | 2-Day Range $0.44–$0.99
  AH spike to peak $0.99 (+113.6%) at 18:15 ET → held ~$0.90 → PM faded to $0.71–0.75.
  AH was the better exit (Grade A, still faded PM).

VTAK — Previous Close $0.65 | 2-Day Range $0.55–$1.27
  AH peak $0.84 (17:30 ET) → faded → PM re-explode to $1.27 (+95%) at 04:05 ET
  on 6.1M sh/27K trades → faded to $0.85. PM >> AH (2.0M float continuation).
```
