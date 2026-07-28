# Post-Market Screening - 2026-07-27

## Scan 21:30 CET (3:30 PM ET)

**Session: REGULAR** (before AH opens at 4:00 PM ET / 22:00 CET). No paper trades this scan — candidates flagged as "Watch — pending AH confirmation." Only enter if a name reappears in a 22:00+ CET AH scan with sustained momentum.

Scanner returned 52 regular-session hits. Top low-float movers to watch into after-hours:

| Ticker | Price | Chg% | 5mVol | IRVol | VChg% | Float | MCap | Industry | Note |
|--------|-------|------|-------|-------|-------|-------|------|----------|------|
| SUIC   | $0.69 | +576.5% | 30K | 138.3 | -61.0 | 3.3M | 1.2M | Data Processing | Huge move but volume fading |
| APHD   | $1.70 | +213.4% | 100 | 0.3 | -50.0 | 15.6M | 30.4M | Advertising | Thin 5mVol |
| GFLT   | $2.00 | +162.3% | 500 | 2.2 | -17.9 | 4.5M | 26.2M | Misc Commercial Svcs | Low float |
| BIYA   | $4.20 | +117.6% | 258 | 11.3 | -99.9 | 2.7M | 12.2M | Personnel Services | Volume collapsed |
| ENTX   | $3.81 | +85.9% | 321 | 301.1 | -99.7 | 39.9M | 187.8M | Pharma: Major | High IRVol |
| NTRX   | $0.62 | +73.9% | 3K | 1.9 | +379.2 | 9.8M | 9.4M | Wholesale Dist | Volume rising |
| KIDZ   | $0.70 | +66.0% | 100 | 14.6 | -100.0 | 2.0M | 1.4M | Internet Software | Volume gone |
| GLVT   | $0.50 | +792.9% | 904 | 1.7 | +322.4 | 377K | 2.0M | Advertising | Tiny float, volume rising |
| RBRS   | $1.20 | +500.0% | 639 | 0.7 | +59.8 | 327K | 1.7M | Integrated Oil | Tiny float |

**Watch — pending AH confirmation.** Most strong movers show fading intraday volume (VChg negative). Names with rising volume into the close (NTRX +379%, GLVT +322%, RBRS +60%) are the ones most likely to carry momentum into AH. Re-evaluate all at the 22:00+ CET AH scans; enter only on sustained AH momentum (>10% AH change across 2 AH scans, per learning-phase gates).

## Scan 22:00 CET (4:00 PM ET)

**Session: AFTERHOURS** (AH just opened). Scanner returned **0 hits** at 16:00 ET. Observation-only scan (learning phase: no entries before 23:00 CET).

No candidates found.

**Watch-name AH cross-check** (21:30 movers via Yahoo `--ah-history`): none showing real accumulating AH prints at this minute. Yahoo returns stale prior-session dates (07-23/07-24) for SUIC, ENTX, NTRX, GLVT, RBRS, BIYA, GFLT — no fresh AH liquidity. The 21:30 leaders were volume-fading intraday spikes (VChg negative) that are not carrying into after-hours. Re-check at 22:30/23:00 in case any name builds real AH volume.

## Scan 22:15 CET (4:15 PM ET)

**Session: AFTERHOURS.** Scanner returned **0 hits** at 16:15 ET. Observation-only scan (learning phase: no entries before 23:00 CET).

Watch-name AH cross-check (21:30 movers via Yahoo `--ah-history` + SIP):

- **ENTX** (Entera Bio, Pharma: Major) — the one name with real fresh AH liquidity. AH holding $3.93–4.00 across 16:00–16:15 ET; SIP first bar 511K sh / 2,353 trades / VWAP $3.95; real two-sided book (bid $3.89 x100 / ask $3.96 x100). **But the +85.9% move happened in the regular session** (21:30 scan had it at $3.81). AH is only ~+3% above the $3.81 regular close, not a fresh AH spike. Scanner missed it because MCap $187.8M exceeds the <$100M cap. Float 39.9M. Does not meet the AH-change >10% gate (AH move off regular close is ~+3%). Regular-session mover holding flat in AH — track at 23:00 to see if it builds; per regular-session caution, intraday spikes that go flat in AH tend to fade.
- NTRX, GLVT, RBRS, SUIC — Yahoo still returns stale prior-session dates (07-23/07-24), no fresh AH liquidity. The 21:30 intraday leaders are not carrying into after-hours.

No qualifying AH candidates. Re-check at 22:30/23:00.

## Scan 22:30 CET (4:30 PM ET)

**Session: AFTERHOURS.** Scanner returned **2 hits** at 16:30 ET. Observation-only scan (learning phase: no entries before 23:00 CET). Both are new (first AH appearance) — neither meets the 2-AH-scan gate yet.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| INLF | [TV](https://www.tradingview.com/chart/?symbol=INLF) | $3.28 | +2.8% | +23.5% | $4.05 | +27.0% | 460K | 5.4M | 0.1x | 1.0M | Industrial Machinery |
| WLDS | [TV](https://www.tradingview.com/chart/?symbol=WLDS) | $3.18 | -9.9% | +13.2% | $3.60 | +2.0% | 1.2M | 6.9M | 0.2x | 2.0M | Electronic Equip/Instruments |

**Spike-bar instrumentation (log-only):**
- INLF: `SPIKE 16:09ET +28% $4.20 1411 trades / 95k sh (first co-spike bar)` — ignition bar fired.
- WLDS: `NO-SPIKE peak +37% @16:10ET (no bar cleared +15% on a volume co-spike)` — no genuine ignition.

**INLF (INLIF Limited, industrial automation/robotics, China small-cap):**
- Tradable=true. Real SIP AH accumulation: 20:00Z 4K sh → 20:05Z 180K → 20:10Z 436K → 20:15Z 445K, thousands of trades/bar. VWAP $3.76→$3.95→$4.26, corroborates scanner AH price. Real book (bid $2.73 x100 / ask $3.82 x100 @16:00 ET quote, ~30 min stale).
- **Trajectory: BUILD** — $3.28→$4.20→$4.04→$4.20 (H $4.50 on last bar), holding near AH high, still building. Ignition bar 16:09 ET.
- Float 1.0M (tiny). Day +2.8% (not a dead-cat).
- **Catalyst: none found** — latest news Oct-Nov 2025 (new-energy sector pivot, Nasdaq bid-price deficiency) + Jun 2026; nothing same-day. Low-float runner with no fresh news.
- Entry Total% +27% (well under 150% ceiling). Verdict: **strongest watch into 23:00** — genuine BUILD on real low-float AH volume, but no catalyst and only 1 AH scan so far. Re-check at 23:00; needs 2nd AH scan >10% to qualify.

**WLDS (Wearable Devices, Mudra neural wristband):**
- Tradable=true. Real SIP AH: 20:00Z 357K → 20:05Z 644K → 20:10Z 431K → 20:15Z 133K — **volume fading**. Peaked $4.28 @16:05 ET, now $3.61-3.79.
- **Trajectory: SPIKE→FADE** — early peak, fading volume and price, NO-SPIKE (no ignition co-spike bar). Day -9.9%, Total% only +2.0%.
- Float 2.0M. Catalyst stale (Jul 25 Mudra partnership news, 2 days old; 1-for-3 reverse split Jun 22).
- Verdict: **skip-track** — SPIKE→FADE with fading volume, stale catalyst, minimal net move. Not a candidate.

**Assessment:** INLF is the one name worth watching into the 23:00 entry window (BUILD, tiny float, real volume). WLDS is a fading spike. No entries this scan (observation-only). Re-check both at 23:00; INLF needs a 2nd AH scan >10% to clear the gate.

## Scan 22:45 CET (4:45 PM ET)

**Session: AFTERHOURS.** Scanner returned **4 hits** at 16:45 ET. Observation-only scan (learning phase: no entries before 23:00 CET).

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| INLF | [TV](https://www.tradingview.com/chart/?symbol=INLF) | $3.28 | +2.8% | +35.4% | $4.44 | +39.2% | 1.3M | 5.6M | 0.2x | 1.0M | Industrial Machinery |
| WLDS | [TV](https://www.tradingview.com/chart/?symbol=WLDS) | $3.18 | -9.9% | +11.6% | $3.55 | +0.6% | 1.4M | 7.0M | 0.2x | 2.0M | Electronic Equip/Instruments |
| BYRN | [TV](https://www.tradingview.com/chart/?symbol=BYRN) | $4.13 | +16.7% | +6.5% | $4.40 | +24.3% | 132K | 858K | 0.2x | 17.8M | Aerospace & Defense |
| AUUD | [TV](https://www.tradingview.com/chart/?symbol=AUUD) | $1.07 | +0.0% | +6.5% | $1.14 | +6.5% | 95K | 240K | 0.4x | 4.8M | Packaged Software |

**Spike-bar instrumentation (log-only, AH Chg >10%):**
- INLF: `SPIKE 16:09ET +28% $4.20 1411 trades / 95k sh (first co-spike bar)` — ignition bar fired (carried from 22:30).
- WLDS: `NO-SPIKE peak +37% @16:10ET (no bar cleared +15% on a volume co-spike)` — no genuine ignition (carried).

BYRN and AUUD below the +10% AH threshold — no spike-bar / catalyst workup.

**INLF (INLIF Limited, industrial automation/robotics, China small-cap) — now clears the 2-AH-scan gate:**
- 2nd AH scan >10% (22:30 +23.5% → 22:45 +35.4%). Float 1.0M, Day +2.8% (not dead-cat), Total% +39% (well under 150% ceiling).
- **Trajectory: BUILD, still climbing.** SIP AH accumulation sustained and rising across every bar: 20:05Z 180K sh/2249 tr → 20:10Z 436K/5685 → 20:15Z 445K/6158 → 20:20Z 215K/2555 → 20:25Z 497K/7136 → 20:30Z 337K/4457. VWAP climbing $3.76→$4.42, corroborates scanner AH price. Price near AH high ($4.65), holding within 20%. Real low-float volume, not a bad print. (Quote endpoint stale at 16:00 ET on free tier; SIP bars are the live confirmation.)
- Catalyst: none found (searched at 22:30 — latest news Oct-Nov 2025 + Jun 2026, nothing same-day). No-catalyst concern noted; not a skip during learning phase.
- Verdict: **prime entry candidate for the 23:00 scan** — genuine BUILD on real accumulating low-float AH volume, clears all gates except the pre-23:00 timing hold.

**WLDS:** SPIKE→FADE confirmed (carried from 22:30). Day -9.9%, Total% +0.6% (barely above prior close), NO-SPIKE, fading volume. Not a candidate.

**Assessment:** No entries (observation-only, before 23:00 CET). INLF is the standout — tiny float, real sustained AH volume, BUILD pattern, under the extension ceiling. It qualifies on all entry gates and should be entered at the 23:00 scan if the BUILD holds. WLDS remains a fading spike.

## Scan 23:00 CET (5:00 PM ET)

**Session: AFTERHOURS. Entry window open** (learning phase: entries allowed at 23:00+ CET). Scanner returned **4 hits** at 17:00 ET. INLF is the only name above the +10% AH threshold.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| INLF | [TV](https://www.tradingview.com/chart/?symbol=INLF) | $3.28 | +2.8% | +31.7% | $4.32 | +35.4% | 1.8M | 5.6M | 0.3x | 1.0M | Industrial Machinery |
| PFSA | [TV](https://www.tradingview.com/chart/?symbol=PFSA) | $1.22 | -28.7% | +6.6% | $1.30 | -24.0% | 1.5M | 929K | 1.6x | 526K | Semiconductors |
| WLDS | [TV](https://www.tradingview.com/chart/?symbol=WLDS) | $3.18 | -9.9% | +7.5% | $3.42 | -3.1% | 1.5M | 7.0M | 0.2x | 2.0M | Electronic Equipment/Instruments |
| OTLK | [TV](https://www.tradingview.com/chart/?symbol=OTLK) | $1.06 | -24.2% | +6.1% | $1.13 | -19.6% | 366K | 16.6M | 0.0x | 151.9M | Pharmaceuticals: Major |

**Spike-bar instrumentation (log-only, AH Chg >10%):**
- INLF: `SPIKE 16:09ET +28% $4.20 1411 trades / 95k sh (first co-spike bar)` — ignition bar fired (carried, confirmed at 17:00 ET).

PFSA, WLDS, OTLK all below the +10% AH threshold — no workup. PFSA (-28.7%) and OTLK (-24.2%) are dead-cat bounces off deep regular-session sell-offs; WLDS is the fading spike carried from prior scans (now +7.5% AH, below threshold).

**INLF (INLIF Limited, industrial automation/robotics, China small-cap) — ENTERED:**
- Clears all gates: 3rd AH scan >10% (22:30 +23.5% → 22:45 +35.4% → 23:00 +31.7%). Float 1.0M (tiny), Day +2.8% (not dead-cat), Total% +35% (well under 150% ceiling). Tradable=true.
- **Trajectory: BUILD/HOLD.** SIP AH accumulation real and sustained across every bar through 16:45 ET (last SIP bar 142K sh / 1835 trades; earlier bars 180K–497K sh). VWAP climbed $3.76→$4.42, corroborates scanner AH price — not a bad print. Peaked $4.65 @16:25 ET, holding $4.20-4.35 (within ~6% of AH high) — a hold, not a fade. Peak before 18:30 ET but stock is holding, not declining, so peak-time is not a disqualifier (hold-vs-fade dominates).
- **Catalyst: none found** (structured search at 22:30 — latest news Oct-Nov 2025 + Jun 2026, nothing same-day). No-catalyst concern documented; not a skip in learning phase. No-catalyst winners span the float range (LNKS 633K, OCG 1.9M).
- **Entry: filled 22 sh @ $4.12** (limit $4.50 --ext, order 76dc5a7d). Book quote stale at 16:00 ET ($3.82 ask); SIP bars are the live confirmation. Catalyst Grade **None** → exit at first premarket opportunity.

**Assessment:** One entry (INLF). Genuine BUILD on real accumulating low-float AH volume, tiny 1.0M float, under the extension ceiling. No catalyst is the one concern. PFSA/OTLK are dead-cat bounces (skip); WLDS is a fading spike (below threshold).

## Scan 23:30 CET (5:30 PM ET)

**Session: AFTERHOURS. Entry window open.** Scanner returned **7 hits** at 17:30 ET. Only INLF (+17.4% AH) and WLDS (+11.3% AH) clear the +10% AH threshold. INLF is already an open position (entered 23:00); WLDS is a confirmed skip. **No new entries this scan.**

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| INLF | [TV](https://www.tradingview.com/chart/?symbol=INLF) | $3.28 | +2.8% | +17.4% | $3.85 | +20.7% | 2.5M | 5.7M | 0.4x | 1.0M | Industrial Machinery |
| WLDS | [TV](https://www.tradingview.com/chart/?symbol=WLDS) | $3.18 | -9.9% | +11.3% | $3.54 | +0.3% | 1.6M | 7.0M | 0.2x | 2.0M | Electronic Equipment/Instruments |
| BIYA | [TV](https://www.tradingview.com/chart/?symbol=BIYA) | $4.17 | +116.1% | +6.2% | $4.43 | +129.5% | 865K | 20.4M | 0.0x | 2.7M | Personnel Services |
| OTLK | [TV](https://www.tradingview.com/chart/?symbol=OTLK) | $1.06 | -24.2% | +8.0% | $1.15 | -18.1% | 535K | 16.6M | 0.0x | 151.9M | Pharmaceuticals: Major |
| JZXN | [TV](https://www.tradingview.com/chart/?symbol=JZXN) | $1.35 | +13.4% | +5.9% | $1.43 | +20.2% | 220K | 5.5M | 0.0x | 1.4M | Specialty Stores |
| BYRN | [TV](https://www.tradingview.com/chart/?symbol=BYRN) | $4.13 | +16.7% | +6.1% | $4.38 | +23.7% | 201K | 866K | 0.2x | 17.8M | Aerospace & Defense |
| BRCC | [TV](https://www.tradingview.com/chart/?symbol=BRCC) | $0.99 | -8.3% | +5.0% | $1.04 | -3.7% | 54K | 628K | 0.1x | 103.1M | Food: Specialty/Candy |

**Spike-bar instrumentation (log-only, AH Chg >10%):**
- INLF: `SPIKE 16:09ET +28% $4.20 1411 trades / 95k sh (first co-spike bar)` — ignition bar fired (carried, confirmed at 17:30 ET).
- WLDS: `NO-SPIKE peak +37% @16:10ET (no bar cleared +15% on a volume co-spike)` — no genuine ignition (carried, confirmed at 17:30 ET).

**INLF (open position, entered 23:00 @ $4.12) — trajectory update:** SIP shows a new AH high **$4.69 @16:55 ET** (above the $4.12 entry), then a fade to $3.80–4.02 by 17:15 ET. Scanner AH $3.85 (+17.4%) at 17:30 ET matches the fade. Volume still real and accumulating (16:50Z 320K sh/3717 tr, tapering to 17:15Z 87K sh/1057 tr). Position remains up ~+17% off close on genuine low-float volume; the AH high printed *after* entry. Fade is off the peak, not a collapse — still holding well above close. Hold/sell decision belongs to the premarket position-evaluation pass; noted here for trajectory tracking only.

**WLDS:** SPIKE→FADE / NO-SPIKE confirmed again. Day −9.9%, Total% +0.3% (barely above prior close), fading. Not a candidate. Skip.

**Below-threshold names:** BIYA (+129.5% Total but only +6.2% AH — regular-session mover gone flat in AH), OTLK (−24.2% dead-cat), JZXN, BYRN, BRCC all under +10% AH — no workup.

**Assessment:** No new entries. INLF (already held) is the only real AH mover and it is fading off its post-entry high on still-real volume. WLDS remains a fading spike. Everything else is below threshold or a dead-cat bounce.

## Scan 00:00 CET (6:00 PM ET)

**Session: AFTERHOURS. Entry window open.** Scanner returned **7 hits** at 18:00 ET. Above the +10% AH threshold: INLF (+25.0%, open position), BIYA (+14.9%), BZFD (+13.3%, new). **No new entries this scan** — both new >10% names fail the 2-AH-scan gate.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| INLF | [TV](https://www.tradingview.com/chart/?symbol=INLF) | $3.28 | +2.8% | +25.0% | $4.10 | +28.5% | 2.7M | 5.7M | 0.5x | 1.0M | Industrial Machinery |
| WLDS | [TV](https://www.tradingview.com/chart/?symbol=WLDS) | $3.18 | -9.9% | +9.7% | $3.49 | -1.1% | 1.6M | 7.0M | 0.2x | 2.0M | Electronic Equipment/Instruments |
| BIYA | [TV](https://www.tradingview.com/chart/?symbol=BIYA) | $4.17 | +116.1% | +14.9% | $4.79 | +148.2% | 1.2M | 20.5M | 0.1x | 2.7M | Personnel Services |
| OTLK | [TV](https://www.tradingview.com/chart/?symbol=OTLK) | $1.06 | -24.2% | +7.0% | $1.14 | -18.9% | 622K | 16.6M | 0.0x | 151.9M | Pharmaceuticals: Major |
| BZFD | [TV](https://www.tradingview.com/chart/?symbol=BZFD) | $1.13 | +1.8% | +13.3% | $1.28 | +15.3% | 246K | 659K | 0.4x | 11.9M | Internet Software/Services |
| BYRN | [TV](https://www.tradingview.com/chart/?symbol=BYRN) | $4.13 | +16.7% | +6.0% | $4.38 | +23.7% | 214K | 867K | 0.2x | 17.8M | Aerospace & Defense |
| BRCC | [TV](https://www.tradingview.com/chart/?symbol=BRCC) | $0.99 | -8.3% | +6.3% | $1.05 | -2.6% | 54K | 628K | 0.1x | 103.1M | Food: Specialty/Candy |

**Spike-bar instrumentation (log-only, AH Chg >10%):**
- INLF: `SPIKE 16:09ET +28% $4.20 1411 trades / 95k sh (first co-spike bar)` — ignition bar fired (carried, confirmed at 18:00 ET).
- BIYA: `SPIKE 17:43ET +16% $4.84 878 trades / 76k sh (first co-spike bar)` — late ignition, but this is a regular-session runner (Day +116%).
- BZFD: `SPIKE 17:41ET +20% $1.36 57 trades / 18k sh (first co-spike bar)` — ignition on thin trade count (57 trades / 18k sh).

**INLF (open position, entered 23:00 @ $4.12) — trajectory update:** SIP full night: peak **$4.69 @16:55 ET** (above entry), faded to $3.80–4.02 by 17:25 ET, then rebuilt to $4.13–4.20 (21:30–21:35Z bars). Scanner AH $4.10 (+25.0%) at 18:00 ET matches. Volume tapering off the peak (26K sh last bar vs 300K–500K at 16:25–16:55 ET) but still real. Position now $4.00 (P&L −2.9%). AH high printed after entry; current price ~holding near entry. Hold/sell belongs to the premarket position-evaluation pass; tracked here only.

**BIYA (Baiya Intl., Personnel Services, China small-cap) — skip (fails 2-AH-scan gate):** This is its **first AH scan above +10%** (was +6.2% AH at 23:30, below threshold). The +116% move was the **regular session**; AH is a fade off the $4.70 @17:05 ET peak down to $4.37 (21:35Z). Total% +148.2% sits right at the +150 extension ceiling. Regular-session runner fading in AH, no 2-AH-scan confirmation. Skip.

**BZFD (BuzzFeed, Internet Software/Services) — skip (fails 2-AH-scan gate):**
- Tradable=true. **First AH appearance** — fails the 2-AH-scan >10% gate (this is scan #1 above threshold).
- **Catalyst found: 35% workforce layoffs announced today** (post Byron Allen $120M majority-stake takeover; restructuring/cost-cut, ~Grade C). Q2 earnings are Aug 4, not today.
- SIP AH volume is **thin** — single-digit trades most bars (20:40–21:15Z: 3–6 trades/bar), only picking up in the last two bars (21:40Z 273 trades/81K sh, 21:45Z 164 trades/40K sh). Not sustained accumulation. Float 11.9M, Day +1.8% (not a dead-cat).
- Verdict: skip tonight (fails 2-AH-scan gate, thin volume). Watch at 00:30 — if it holds >10% AH on building volume it becomes a 2nd-scan candidate.

**Below-threshold names:** WLDS (+9.7% AH, SPIKE→FADE / NO-SPIKE carried, Total −1.1%), OTLK (−24.2% dead-cat), BYRN (+6.0%), BRCC (−8.3% dead-cat) — no workup.

**Assessment:** No new entries. INLF (already held) is the only confirmed multi-scan AH mover; holding near entry on tapering-but-real volume. BIYA and BZFD both fail the 2-AH-scan gate (first AH scans >10%); BIYA is a fading regular-session runner near the ceiling, BZFD has a real catalyst (35% layoffs) but thin volume. Re-check BZFD at the 00:30 final scan for a possible 2nd AH scan.

## Scan 00:30 CET (6:30 PM ET) — FINAL SCAN

**Session: AFTERHOURS. Entry window open. Final scheduled scan.** Scanner returned **8 hits** at 18:30 ET. Above the +10% AH threshold: INLF (+25.6%, open position), BIYA (+17.0%), BZFD (+12.4%). BIYA and BZFD both now have 2 AH scans >10% — evaluated for entry. **1 new entry: BZFD.**

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| BIYA | [TV](https://www.tradingview.com/chart/?symbol=BIYA) | $4.17 | +116.1% | +17.0% | $4.88 | +152.8% | 3.6M | 20.8M | 0.2x | 2.7M | Personnel Services |
| INLF | [TV](https://www.tradingview.com/chart/?symbol=INLF) | $3.28 | +2.8% | +25.6% | $4.12 | +29.2% | 2.8M | 5.8M | 0.5x | 1.0M | Industrial Machinery |
| WLDS | [TV](https://www.tradingview.com/chart/?symbol=WLDS) | $3.18 | -9.9% | +9.7% | $3.49 | -1.1% | 1.6M | 7.0M | 0.2x | 2.0M | Electronic Equipment/Instruments |
| OTLK | [TV](https://www.tradingview.com/chart/?symbol=OTLK) | $1.06 | -24.2% | +5.6% | $1.12 | -19.9% | 705K | 16.6M | 0.0x | 151.9M | Pharmaceuticals: Major |
| BZFD | [TV](https://www.tradingview.com/chart/?symbol=BZFD) | $1.13 | +1.8% | +12.4% | $1.27 | +14.4% | 373K | 673K | 0.6x | 11.9M | Internet Software/Services |
| BYRN | [TV](https://www.tradingview.com/chart/?symbol=BYRN) | $4.13 | +16.7% | +5.1% | $4.34 | +22.6% | 223K | 868K | 0.3x | 17.8M | Aerospace & Defense |
| ANGI | [TV](https://www.tradingview.com/chart/?symbol=ANGI) | $5.93 | +7.2% | +8.1% | $6.41 | +15.9% | 65K | 516K | 0.1x | 28.6M | Internet Software/Services |
| BRCC | [TV](https://www.tradingview.com/chart/?symbol=BRCC) | $0.99 | -8.3% | +5.0% | $1.04 | -3.7% | 56K | 628K | 0.1x | 103.1M | Food: Specialty/Candy |

**Spike-bar instrumentation (log-only, AH Chg >10%):**
- INLF: `SPIKE 16:09ET +28% $4.20 1411 trades / 95k sh (first co-spike bar)` — ignition bar fired (carried, confirmed 18:30 ET).
- BIYA: `SPIKE 17:43ET +16% $4.84 878 trades / 76k sh (first co-spike bar)` — late ignition, regular-session runner.
- BZFD: `SPIKE 17:41ET +20% $1.36 57 trades / 18k sh (first co-spike bar)` — thin ignition (57 trades / 18k sh).

**BZFD (BuzzFeed, Internet Software/Services) — ENTERED:**
- Clears the 2-AH-scan gate: 00:00 +13.3% → 00:30 +12.4% AH. Float 11.9M (<50M), Day +1.8% (not dead-cat), Total% +14.4% (well under 150% ceiling). Tradable=true.
- **Trajectory: BUILD/HOLD.** SIP shows real accumulation building through the last hour: 21:20Z 22K sh/15 tr → 21:25Z 21K → 21:30Z 31K → 21:35Z 50K → 21:40Z 81K sh/273 tr → 21:45Z 40K/164 → 21:50Z 32K → 22:00Z 19K/127 tr. Price built $1.13→$1.37 peak @17:40 ET, holding $1.26-1.30 (within ~8% of AH high). VWAP $1.28-1.31 corroborates scanner AH price — not a bad print. Peak after 17:30 ET, holding not fading. (Quote endpoint stale at 16:00 ET on free tier; SIP bars are the live confirmation.)
- **Catalyst: 35% workforce layoffs announced today** (cost-cut/restructuring after Byron Allen $120M majority-stake takeover). Market read it bullish. ~Grade **C** (weak news/restructuring). Q2 earnings Aug 4, not today.
- **Entry: filled 76 sh @ $1.30** (limit $1.38 --ext, order abb707e6). Catalyst Grade **C** → exit in premarket.

**BIYA (Baiya Intl., Personnel Services, China small-cap) — skip (extension ceiling):**
- 2 AH scans >10% (00:00 +14.9% → 00:30 +17.0%), but **Total% +152.8% exceeds the +150 extension ceiling.** Ceiling-override watch requires VRatio >5x — BIYA is 0.2x, fails the override. No hypothetical entry recorded (fails override criteria).
- Regular-session runner (+116% Day). SIP shows AH peak $4.70 @17:05 ET, fading to $4.37 (21:35Z). Fading spike off a huge intraday move — exactly the extended-entry profile the ceiling protects against (ANY +155%→-21%, ATPC +154%→-14%). Skip.

**INLF (open position, entered 23:00 @ $4.12) — trajectory update:** SIP full night: peak $4.69 @16:55 ET (above entry), faded to $3.80-4.02 by 17:25 ET, rebuilt to $4.13-4.20 (21:30-21:35Z). Scanner AH $4.12 (+25.6%) at 18:30 ET matches — position ~flat to entry. Volume tapering off the peak (26K sh last bar vs 300K-500K at 16:25-16:55 ET) but still real. AH high printed after entry; holding near entry. Hold/sell belongs to the premarket position-evaluation pass; tracked here only.

**Final-scan feed-lag cross-check:** Tracked names this night (INLF, WLDS, BIYA, BZFD) plus 21:30 watch names (ENTX, NTRX, GLVT, RBRS, SUIC, GFLT). The three real >10% AH movers (INLF, BIYA, BZFD) are all captured by the scanner at 18:30 ET on real accumulating SIP volume — no under-reported name to rescue. Below-threshold names (WLDS +9.7% SPIKE→FADE, OTLK -24.2% dead-cat, BYRN, ANGI, BRCC) show no SIP surge above threshold. No feed-lag rescue needed.

**Assessment:** 1 new entry (BZFD — BUILD/hold, float 11.9M, real catalyst 35% layoffs Grade C, low extension +14.4%, building volume last hour). BIYA skipped on the +150% ceiling (VRatio 0.2x fails override). INLF (held) holding near entry on tapering-but-real volume. Two positions carried into premarket: INLF (Grade None) and BZFD (Grade C) — both exit in the premarket position-evaluation pass.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
| INLF | $4.12 | 2026-07-27 23:00 CET | 22 | 76dc5a7d | BUILD/hold, float 1.0M, +35% Total (under ceiling), 3 AH scans >10%, real SIP volume. Catalyst: None (concern noted). |
| BZFD | $1.30 | 2026-07-28 00:30 CET | 76 | abb707e6 | BUILD/hold, float 11.9M, +14.4% Total (low extension), 2 AH scans >10%, building SIP volume last hour. Catalyst: 35% layoffs (Grade C). |

---

## Morning Evaluation — 10:20 CET (04:20 ET), Pulse 1

### Today's Winner

**No clean winner today.** The only mover clearing the >100% bar was **CISS**, and it is a dilution-crash dead-cat bounce, not a tradeable AH→PM explosion. Reported below as the mechanical winner with the disqualifying context. The best *strategy-fit* mover was **INLF** at +58.5% — real and liquid, but below the 100% bar.

**CISS** — C3is Inc. (marine shipping, Nasdaq) — *mechanical winner, disqualified in practice*
- Catalyst: **Grade D — $6.0M underwritten public offering priced at $0.52/unit (11,535,000 units + Class F warrants), announced Jul 27.** Massive dilution on a tiny share count.
- Previous Close: **$0.1024** (Jul 27 close after a **−80% single-day collapse** from $0.52 on 42.9M sh / 53,263 trades)
- AH last night: SIP high **$0.14 @ 17:15 ET** (+37% AH) on 2.95M sh / 2,611 trades in one bar; held $0.12–0.13 through the AH tail
- Premarket now: SIP PM high **$0.27 @ 04:00 ET** = **+164% from close**, on **18.1M sh / 25,932 trades** in a single 5-min bar; second bar 7.9M sh / 10,598 trades holding $0.21 (+105%). Now fading — $0.20 at 04:20 ET, $0.16 at 04:25 ET.
- Hypothetical P&L (AH entry $0.13 → PM peak $0.27): **+108%**
- Float: 529K (post-offering, manufactured) | Market Cap: $281K
- **Why this is not a real winner:** the +164% is measured off a crash-day close. The stock is $0.27 against $0.52 two days ago and $1.68 ten days ago — a −80% dilution collapse bouncing, not a momentum explosion. Sub-penny ($0.10 tick regime), live book bid $0.10 / ask $0.14 = **~40% spread**. Any realistic fill destroys the paper gain. Day% −80% is the archetype our dead-cat filter exists to block.

**Best strategy-fit mover: INLF** — INLIF Limited (industrial automation/robotics, China small-cap) — **our position**
- Catalyst: **None found** (searched at 22:30 CET; latest news Oct–Nov 2025 + Jun 2026)
- Previous Close: $3.28 | AH SIP peak **$4.69 @ 16:55 ET** (+43%) on sustained 180K–497K sh/bar, 2.2k–7.1k trades/bar
- Premarket now: SIP PM high **$5.20 @ 04:00 ET** (+58.5% from close) on 618K sh / 10,986 trades; currently $4.96–5.02
- Hypothetical P&L (AH first sighting $4.05 → PM peak $5.20): **+28%**. Actual entry $4.12 → **+21.8% to +26.2%**
- Float: 1.0M | Market Cap: $3.4M
- Does **not** clear the >100% winner bar.

**Scanner Diagnostic (CISS):**
- Detectable at screening time? **NO — structurally excluded by our own price floor.**
- The data was there: CISS traded +27% to +37% above its close from 17:15 ET onward on 2.95M sh / 2,611 trades in a single bar — squarely inside the scanned window (23:15 CET), on volume far above anything else that night.
- It never appeared in any of the 9 evening scans because `scan.py` enforces `MIN_PRICE = $0.50`. CISS closed at $0.1024. The screener never queried it.
- Second gate it would also have failed: the dead-cat filter (Day% ≤ −15%; CISS was −80%). That gate would have been **correct** — the bounce is already unwinding ($0.27 → $0.16 in 25 minutes).
- **Scanner gap:** a **price-floor exclusion**, a category we have not tracked before. New tally opened in Notes. Alpaca reports `CISS tradable=true`, so the floor is our constraint, not the broker's.

**Scanner Diagnostic (INLF — the tradeable mover):**
- Detectable at screening time? **YES — detected, entered, and currently profitable.**
- First surfaced at the 22:30 CET scan (+23.5% AH, $4.05), confirmed across 22:45 (+35.4%), 23:00 (+31.7%), 23:30 (+17.4%), 00:00 (+25.0%), 00:30 (+25.6%). Entered 23:00 CET @ $4.12 on a BUILD with real accumulating SIP volume.
- Scanner worked exactly as designed on this name.

### Baseline Tracking

- Days tracked: **55** (was 54 + 1)
- Winners detected by scanner: **45/51 (88.2%)** — CISS counted as a **miss** (price-floor exclusion; the AH signal was real, in-window, and volume-backed, but our universe filter never queried it)
- Winner selected for paper trade: **26/51 (51.0%)** — unchanged (CISS not entered; correctly so on the dead-cat gate)
- Target: >80% detection
- Status: **BASELINE MET** (88.2%)
- **Baseline gap (carried):** 2026-07-17 and 2026-07-20 morning evals recorded no `Days tracked:` line — those two trading-day retrospectives were never baseline-counted (denominator understates true trading days). The immediately-preceding trading day (07-24) *does* carry a baseline line, so **no new gap this cycle**.

### Retrospective Scan Results

**Live PM scan (04:20 ET, `scan.py --session premarket`) — 3 hits:**

| Ticker | Close | PM Chg% | PM Price | PM Vol | VRatio | Float | MCap |
|--------|-------|---------|----------|--------|--------|-------|------|
| INLF | $3.28 | +47.0% | $4.82 | 329K | 0.1x | 1.0M | $3.4M |
| POLA | $1.47 | +35.4% | $1.99 | 899K | 2.3x | 2.8M | $5.4M |
| BZFD | $1.13 | +16.8% | $1.32 | 102K | 0.1x | 11.9M | $45.2M |

**Forced AH scan (`--session afterhours`): 0 hits** — expected overnight; TradingView postmarket fields are stale by morning. Not used as a retrospective source.

**Independent whole-market PM sweep (TradingView, `premarket_change > 25`, no price/mcap cap) — 5 hits:**

| Ticker | Close | PM Chg% | PM Vol | Float | In our universe? |
|--------|-------|---------|--------|-------|------------------|
| CISS | $0.1024 | +95.9% (SIP peak +164%) | 15.7M | 529K | **No — below $0.50 floor** |
| INLF | $3.28 | +42.1% (SIP peak +58.5%) | 463K | 1.0M | Yes — detected + entered |
| OMH | $0.1454 | +40.5% (SIP peak +65%) | 4.2M | 22.2M | **No — below $0.50 floor** (also `tradable=false`) |
| POLA | $1.47 | +35.7% (SIP peak +64%) | 966K | 2.8M | Yes — but late-AH-tail surge |
| GOSS | $0.1994 | +28.5% (SIP peak +45%) | 2.7M | 449M | **No — below $0.50 floor** (float 449M anyway) |

**Three of the five biggest PM movers were sub-$0.50 and structurally invisible to the scanner.** All three had real, volume-backed AH footprints above the +10% threshold inside the scanned window.

### Open Position P&L (Alpaca)

| Ticker | Entry | Entry Total% | Catalyst | Entry Time | PM Peak | Peak Time | Exit | P&L | P&L % | Status |
|--------|-------|--------------|----------|------------|---------|-----------|------|-----|-------|--------|
| INLF | $4.12 | +25.6% | None | 2026-07-27 23:00 CET | **$5.20 (SIP)** | 04:00 ET | open | +$22.80 | **+25.2%** | 🟢 Open |
| BZFD | $1.30 | +15.0% | C — 35% workforce layoffs | 2026-07-28 00:30 CET | $1.34 | 04:05 ET | open | −$0.78 | −0.8% | 🟡 Open |
| DOMO | $3.92 | +14.2% | A — $400M asset sale | 2026-07-23 23:32 CET | $4.50 (07-24) | 07:55 ET | open | −$9.25 | −9.4% | 🔴 Open (day 4/5) |

**Quote-freshness check:** Alpaca `current_price` verified against live data for all three.
- INLF $5.16 — **live** (Yahoo PM $5.02–5.15 at 04:20–04:23 ET, SIP PM high $5.20). P&L +25.2% is real.
- BZFD $1.29 — **live** (Yahoo PM $1.30 at 04:23 ET, TV scan $1.32). Roughly flat to entry.
- DOMO $3.55 — **live** (SIP Jul 27 daily close $3.57; no PM trades yet this morning). −9.4% is real, not stale.

**Total Realized P&L (Alpaca fills only): €0.00 this session** — no exits. Exits belong to the 10:30 / 14:30 CET position-evaluation pass; this prompt closes nothing.

**Peak verification:** INLF Yahoo `--pm-history` reported PM high $5.15; SIP reports **$5.20** on 618K sh / 10,986 trades. SIP peak used (Yahoo under-reported by $0.05, consistent with the known low-float under-count).

### Scanner Effectiveness

- **Evening scans ran: 9 (21:30 → 00:30 CET)** — all **7 of 7** scheduled scans ran (21:30, 22:00, 22:30, 23:00, 23:30, 00:00, 00:30) plus 2 extra (22:15, 22:45). **No coverage failure.**
- Candidates found: 13 unique tickers across the night (INLF, WLDS, BIYA, BZFD, BYRN, AUUD, PFSA, OTLK, JZXN, BRCC, ANGI + 21:30 regular-session watch names)
- Retrospective matches: **1 of 2 relevant movers caught** — INLF caught and entered; POLA missed (late-AH-tail); CISS/OMH/GOSS outside the price universe.

### Missed Opportunities

| Ticker | AH Change | Why Missed | Would Be Profitable? |
|--------|-----------|------------|---------------------|
| CISS | +37% (17:15 ET, 2.95M sh/bar) | **Price-floor exclusion** ($0.1024 < $0.50 `MIN_PRICE`). Also blocked by dead-cat gate (Day −80%) | On paper +108% (AH $0.13 → PM $0.27); in practice **no** — ~40% bid/ask spread, bounce unwound to $0.16 in 25 min |
| POLA | 0% at 18:30 ET, +49% by 18:55 ET | **True-tail surge** — $25M equity facility PR dropped ~18:30–18:45 ET, after the 00:30 CET final scan. Zero AH prints before 18:45 ET | AH-tail entry ~$1.56 → PM peak $2.38 = **+53%** |
| OMH | +27% (AH, 128K sh) | Price-floor exclusion ($0.1454). Also `tradable=false` on Alpaca | Not fillable |
| GOSS | +45% (AH, 725K–1.07M sh/bar) | Price-floor exclusion ($0.1994). Float 449M is far outside profile anyway | AH $0.29 → PM peak $0.29 = flat |

### AH Mover Follow-Through

| Ticker | AH Peak (SIP) | Peak Time | AH Trajectory | Current PM | From Peak | From Close | Verdict |
|--------|---------------|-----------|---------------|------------|-----------|------------|---------|
| INLF | $4.69 | 16:55 ET | **Build** ($4.05→$4.44→$4.32→$3.85→$4.10→$4.12) | $5.02 | +7.0% | **+53%** | ✅ PM **exceeded** AH peak — continuation confirmed |
| BIYA | **$6.11** | 17:55 ET | Late surge then fade | $4.31 | −29.5% | +3.4% (from $4.17) | ❌ PM **fell short** — AH was the better exit. Ceiling skip vindicated |
| WLDS | $4.35 | 16:10 ET | **Spike→fade** | $3.07 | −29.4% | −3.5% | ❌ PM **fell short** — fade rule correct |
| BZFD | $1.37 | 17:40 ET | Build/hold | $1.30 | −5.1% | +15.0% | ➖ PM roughly flat to AH peak |
| POLA | $2.22 | 19:00 ET | **Late surge** (no AH prints until 18:45 ET) | $2.05 | −7.7% | +41.2% | ✅ PM peak $2.38 **exceeded** AH peak |

**AH-peak-vs-PM-peak:** 2 exceeded (INLF, POLA), 2 fell short (BIYA, WLDS), 1 flat (BZFD).

**Extreme-AH-runner check (AH peak >250% from close):** BIYA's AH peak $6.11 vs its prior close $1.93 = **+217% Total** — just under the 250% band, and it faded −29.5% into PM. Consistent with the hypothesis that heavily-extended AH runners peak in after-hours. The +150% extension ceiling correctly skipped it at Total% +152.8%.

### Price Charts

**INLF** — clean AH build → PM continuation (the pattern we hunt):
```
Previous Close: $3.28  |  Peak: $5.20 (+58.5%) at 07-28 04:00 ET
  [AH]  07-27 16:09 ET: $4.20 (+28%)  SPIKE ignition, 1,411 trades / 95k sh
  [AH]  07-27 16:25 ET: $4.65 (+42%)  497k sh / 7,136 trades
  [AH]  07-27 16:55 ET: $4.69 (+43%)  AH high
  [AH]  07-27 17:15 ET: $4.02 (+23%)  fade off peak
  [AH]  07-27 18:30 ET: $4.12 (+26%)  rebuilt — final scan
  [AH]  07-27 19:55 ET: $4.40 (+34%)  AH tail climbing
  [PM]  07-28 04:00 ET: $5.20 (+58%)  PM high, 619k sh / 10,986 trades
  [PM]  07-28 04:25 ET: $4.96 (+51%)  holding
```

**POLA** — flat all AH, then a vertical late-tail surge on the equity-facility PR:
```
Previous Close: $1.45  |  Peak: $2.38 (+64.2%) at 07-28 04:00 ET
  [AH]  07-27 16:00 ET: $1.47 (+1.4%)   142 sh / 3 trades — dead
  [AH]  07-27 16:00-18:40 ET: NO PRINTS
  [AH]  07-27 18:45 ET: $2.00 (+37.9%)  540k sh / 4,876 trades — ignition
  [AH]  07-27 18:55 ET: $2.16 (+49.0%)  530k sh / 4,617 trades
  [AH]  07-27 19:00 ET: $2.22 (+53.1%)  AH high
  [AH]  07-27 19:55 ET: $2.08 (+43.6%)  holding
  [PM]  07-28 04:00 ET: $2.38 (+64.2%)  PM high, 1.66M sh / 14,305 trades
  [PM]  07-28 04:25 ET: $2.05 (+41.2%)  fading
```
Final scan was 18:30 ET. The first POLA print was 18:45 ET.

**CISS** — the −80% dilution collapse and its bounce (why the "+164%" is an artifact):
```
  07-15  $1.68     07-22  $1.63     07-23  $0.96 (−41%, 931k sh)
  07-24  $0.52 (−46%, 5.2M sh)     07-27  $0.10 (−80%, 42.9M sh / 53,263 trades)
  [AH]  07-27 17:15 ET: $0.14 (+37% off the $0.1024 crash close), 2.95M sh / 2,611 trades
  [PM]  07-28 04:00 ET: $0.27 (+164%), 18.1M sh / 25,932 trades
  [PM]  07-28 04:05 ET: $0.21 (+105%), 7.9M sh / 10,598 trades
  [PM]  07-28 04:20 ET: $0.20 (+96%)
  [PM]  07-28 04:25 ET: $0.16 (+56%)  ← unwinding
```

### Notes

**NEW TALLY — Price-floor exclusion misses (opened 2026-07-28).** A category we have not tracked: real, in-window, volume-backed AH movers that no scan ever surfaced because `scan.py` sets `MIN_PRICE = $0.50`. This is distinct from a feed-lag miss (data-source failure), a PM-only gapper (structurally undetectable), and a late-tail surge (schedule gap) — here the scanner is deliberately not looking.

| Date | Ticker | Close | AH signal (in-window) | PM peak | Hypo AH→PM | Alpaca tradable | Verdict |
|------|--------|-------|------------------------|---------|------------|-----------------|---------|
| 2026-07-28 | CISS | $0.1024 | +37% @17:15 ET, 2.95M sh / 2,611 trades | $0.27 (+164%) | +108% | **true** | Uninvestable — ~40% spread, dilution dead-cat, unwound to $0.16 in 25 min |
| 2026-07-28 | OMH | $0.1454 | +27% @AH, 128K sh | $0.24 (+65%) | +33% | **false** | Broker-blocked regardless |
| 2026-07-28 | GOSS | $0.1994 | +45% @AH, 725K–1.07M sh/bar | $0.29 (+45%) | ~0% | true | Flat AH→PM; float 449M, outside profile |

**Standing count: 3 (all 2026-07-28, all on one night).** Hypothesis under test: sub-$0.50 names produce frequent >100% headline moves but are uninvestable (spreads wide relative to tick, moves are dilution/crash bounces). Tonight's evidence supports the hypothesis — the only one clearing 100% (CISS) had a ~40% spread and unwound within 25 minutes, and one of three is not even tradeable on Alpaca. **Do not change `MIN_PRICE` on one night's data.** The escalation is a *question* for Juan (routed to the daily email), not a parameter change: should the scanner *observe* sub-$0.50 names in log-only mode to build the dataset, without making them entry-eligible? Threshold to propose an actual floor change: ≥3 sub-$0.50 names on separate nights that are both >100% **and** holdable on tight spreads.

**Fade-rule false-negative tally — WLDS added as a sub-3M NEGATIVE case.** WLDS (float **2.0M**, sub-3M) was skipped on SPIKE→FADE / NO-SPIKE at 22:30 CET: AH SIP peak $4.35 @16:10 ET, faded all night to $3.16, PM peak only **$3.10 on 31K sh / 345 trades** — well below its AH peak and below the prior close. **Fade rule correct.**
**Standing sub-3M count: 3 of 6 — the ≥4/5 trigger has MOVED FURTHER AWAY.**
- Blew past: LNKS 1.5M, RPGL 1.1M, ATPC 475K
- Fell short: CRE 1.1M, IOTR 644K, **WLDS 2.0M (new)**
The live-flip handoff remains **withdrawn**. Do not wire the `Day Trading.md` entry-rule exception. Two consecutive cycles have now added negative cases (CRE reclassified on SIP correction 07-17, WLDS tonight); the float-conditional hypothesis is weakening, not strengthening.
**Catalyst-override annotation:** WLDS carried a stale Grade C catalyst (Jul 25 Mudra partnership, 2 days old) — not a strong-catalyst case, so it does not enter the strong-catalyst fader bucket. That bucket stays at ALGS (Jul 6, Grade A, −5%): strong catalysts still have not rescued a fade.

**Late-AH-tail surge tally — POLA added (TRUE-TAIL).** POLA had **zero AH prints between 16:00 and 18:40 ET** (142 sh / 3 trades in the entire 16:00 bar, then nothing). The $25M Committed Equity Facility PR (Roth Principal Investments) dropped ~18:30–18:45 ET; ignition bar 18:45 ET at 540K sh / 4,876 trades. At the 18:30 ET final scan POLA was at **+1.4%**, genuinely far below the +10% threshold — **true-tail**, not feed-lag.

| Date | Ticker | Surge time ET | Sub-class | At 18:30 ET | Hypo AH-tail → PM peak |
|------|--------|---------------|-----------|-------------|------------------------|
| 2026-06-22 | ORIS | 19:25 | true-tail | +22–28% | +54% |
| 2026-06-29 | BTCT | 18:50 | feed-lag | +67.6% (feed showed flat) | +47% |
| 2026-07-28 | POLA | 18:45 | **true-tail** | **+1.4%** | ~$1.56 → $2.38 = **+53%** |

**Standing true-tail count: 2 (ORIS, POLA).** Threshold to propose added late scans (~01:00/01:30 CET) is ≥3–4 true-tail winners. Not reached — **no schedule change recommended**. Worth noting that POLA's catalyst was **Grade D (equity facility / dilution)**, historically our worst tier, so the +53% would have been a low-conviction trade even if scanned. Route as an FYI in the daily email, not a request.

**In-window feed-lag miss tally: UNCHANGED at 3** (BTCT, KUST, WLDS Jul 23–24). No new case tonight. The 00:30 CET final-scan feed-lag cross-check ran and correctly found nothing to rescue among tracked names. **However, one partial discrepancy: BIYA's SIP price at 18:00 ET was $5.62 while the 00:00 CET scan reported $4.79 (−15%).** By the 18:30 ET scan the feed had caught up ($4.88 vs SIP $4.93). BIYA was already surfaced and correctly skipped on the ceiling, so no trade was affected — logged as a data-quality observation, not a new miss. **The ≥3 escalation trigger remains REACHED** and the AH-data-source-verification recommendation (independent gainers cross-check of the whole scan universe at the final scan) stays on the daily email.

**PM-only gapper tally: UNCHANGED.** Today's biggest raw PM mover (CISS, +164%) is **not** a PM-only gapper — it had a real AH footprint (+37% at 17:15 ET on 2.95M sh). It is classified as a price-floor exclusion instead. **Standing holdable count remains 1 clear (SXTC) of 6 tracked** — no cluster, no early-PM workflow recommendation.

**Reverse-split-squeeze fade tally: UNCHANGED.** No entered or notable candidate last night carried a reverse-split catalyst. (WLDS had a 1-for-3 reverse split Jun 22, ~5 weeks old, but it was a skip-track name with a stale partnership catalyst, not a split-squeeze entry — not added to the tally.) Recency split stands at: this-week splits **3/3 faded** (ELPW, YYGH, BIYA); weeks/months-old splits **2/3 non-fade** (EDHL, LGCL continue; PAVS faded).

**Ceiling-override watch: none flagged last night.** BIYA was skipped on the +150% ceiling (Total% +152.8%) but explicitly failed the VRatio >5x override criterion at 0.2x, so no hypothetical was recorded. **Outcome check anyway, for the ceiling dataset: the skip was correct.** BIYA's SIP AH peak was $6.11 @17:55 ET (Total +217% from its $1.93 base); PM peaked at only $4.76 and settled $4.31. An entry at the 00:30 scan price ($4.88) would be **−11.7%** at the current PM level. Second consecutive ceiling-skip vindication.

**Dead-cat-override watch: none flagged.** PFSA (−28.7%) and OTLK (−24.2%) both stayed well below their regular closes (Total% −24.0% and −19.9%), so neither met the reclaim condition. **CISS is a near-miss case worth noting**: Day −80%, and its AH *did* reclaim +27% above the regular close on a multi-scan-equivalent build — the exact dead-cat-override profile. It then ran +164% in PM before unwinding to +56% within 25 minutes. This is a **cautionary** data point for the dead-cat-override hypothesis, not a supporting one: the reclaim was real, the PM spike was real, and it was still uninvestable.

**Broker-block tally: UNCHANGED.** All qualified candidates (INLF, BZFD) filled normally. OMH was `tradable=false` but never qualified (below the price floor and outside the AH threshold path), so it is not a broker-block case.

**Session assessment.** Full scan coverage (7/7 scheduled + 2 extra), one clean win in progress (INLF +25% and above its AH peak — the AH-build→PM-continuation pattern working exactly as intended), one flat (BZFD), one aging Grade A hold underwater (DOMO −9.4%, day 4/5). No real >100% winner existed tonight in our tradeable universe. The two rules that fired defensively — the +150% extension ceiling on BIYA and the SPIKE→FADE skip on WLDS — were both vindicated by PM follow-through. The single genuine new finding is the price-floor blind spot, and the evidence so far argues the blind spot is cheap rather than costly.

**For the daily email (questions/decisions for Juan):**
1. **Price-floor blind spot.** Three of the five biggest PM movers were sub-$0.50 and invisible to the scanner by design. Tonight's evidence says they are uninvestable (CISS: ~40% spread, unwound in 25 min; OMH: not tradeable on Alpaca; GOSS: flat AH→PM). Question: add a *log-only* sub-$0.50 observation pass to build the dataset without making them entry-eligible?
2. **AH-data-source verification** (carried, trigger reached at 3 in-window feed-lag misses): add an independent gainers cross-check of the whole scan universe at the final scan.
3. **DOMO** is day 4 of 5 on the Grade A multi-day hold at −9.4%. The 10:30 position-evaluation pass owns the decision; flagging that the 5-day clock expires tomorrow.
