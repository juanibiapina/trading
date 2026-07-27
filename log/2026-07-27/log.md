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

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
| INLF | $4.12 | 2026-07-27 23:00 CET | 22 | 76dc5a7d | BUILD/hold, float 1.0M, +35% Total (under ceiling), 3 AH scans >10%, real SIP volume. Catalyst: None (concern noted). |
