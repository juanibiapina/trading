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

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
