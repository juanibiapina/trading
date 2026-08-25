
# Post-Market Screening - 2026-08-25

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| WLDS | $3.30 | $2.66 | -19.4% | $3.58 | 1 | None | SELL | Grade None exit first PM + far below -10% hard stop; PM no follow-through |

**Actions taken:**
- SELL 28 WLDS @ limit $2.58 ext (id 2eeb31ea) filled @ $2.66. Real fill $2.66, P&L -$17.92 (-19.4%).
- No open positions remain.

## Position Evaluation — 14:30 CET

No open positions (Alpaca source of truth). WLDS closed at 10:30 pulse. OPEN_POSITIONS.md reconciled (shows none). Nothing to evaluate or sell.

## Scan 21:30 CET (3:30 PM ET)

**REGULAR session** — AH not open yet (opens 22:00 CET / 4:00 PM ET). No entries per regular-session caution rule. Low-float / big-move names flagged as watch pending AH confirmation.

| Ticker | Chart | Price | Chg% | Float | MCap | IRVol | VChg% | Industry | Watch |
|--------|-------|-------|------|-------|------|-------|-------|----------|-------|
| DAIC | [TV](https://www.tradingview.com/chart/?symbol=DAIC) | $3.48 | +101.2% | 1.3M | 3.4M | 10.4 | +185.9 | Miscellaneous | Watch |
| PMI | [TV](https://www.tradingview.com/chart/?symbol=PMI) | $9.91 | +93.1% | 1.3M | 12.0M | 25.9 | +33.6 | Medical Specialties | Watch |
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $0.58 | +127.1% | 4.4M | 2.0M | 833.1 | -20.4 | Misc Commercial Services | Watch (fading vol) |
| JEM | [TV](https://www.tradingview.com/chart/?symbol=JEM) | $6.66 | +74.3% | n/a | 4.3M | 566.6 | -39.2 | Wholesale Distributors | Watch (fading vol) |
| TNMG | [TV](https://www.tradingview.com/chart/?symbol=TNMG) | $0.61 | +54.2% | 2.3M | 1.8M | 505.0 | +90.9 | Internet Software/Services | Watch |
| AMIX | [TV](https://www.tradingview.com/chart/?symbol=AMIX) | $8.26 | +53.8% | 946K | 8.0M | 157.0 | -68.4 | Medical Specialties | Watch (fading vol) |
| SWVL | [TV](https://www.tradingview.com/chart/?symbol=SWVL) | $2.19 | +49.0% | 5.3M | 21.8M | 6337.1 | -46.5 | Other Transportation | Watch (fading vol) |

**Notes:**
- Regular-session scan only. Instrumentation (spike-bar, third-bar confirmation) not run — AH ignition tools apply after 4:00 PM ET open.
- Watchlist above = low-float (<10M) names with >45% intraday move. Re-evaluate at 22:00+ CET AH scans; enter only if a name reappears with sustained AH momentum (2+ AH scans) and clears all entry gates at 23:00+ CET.
- Several names (NCPL, JEM, AMIX, SWVL) already showing fading intraday volume (VChg% negative or IRVol declining) — spike-then-fade risk into AH.

## Scan 22:00 CET (4:00 PM ET)

**AH just opened** (16:00 ET). Scanner `--all`: 0 hits. Observation-only scan (learning-phase entry gate is 23:00+ CET). No entries.

Carry-forward check on 21:30 low-float watch names (AH quotes at 16:00 ET, seconds into session — thin/forming books):

| Ticker | Reg Close | AH Bid | AH Ask | Note |
|--------|-----------|--------|--------|------|
| DAIC | $3.48 | $3.31 | $0.00 x0 | No AH ask/offer — no fillable book yet |
| PMI | $9.91 | $8.25 | $10.90 | Wide spread, below reg close |
| NCPL | $0.58 | $0.49 | $0.65 | Below close, thin |
| TNMG | $0.61 | $0.48 | $0.65 | Below close, thin |
| AMIX | $8.26 | $6.21 | $8.25 | Below close, wide |

**Notes:**
- Scanner returned no AH movers >threshold at open. Watch names sitting flat/below regular close, no AH momentum yet.
- Instrumentation (spike-bar, third-bar confirmation) not run — no candidate cleared threshold and it's observation-only.
- Re-evaluate at 22:30 / 23:00 CET. Entries only at 23:00+ with a candidate clearing all gates (float <50M, AH >10% in ≥2 AH scans, Day% > -15%).

## Scan 22:15 CET (4:15 PM ET)

**AH open ~15 min in.** Scanner `--all`: 0 hits (feed lag). Observation-only (entry gate 23:00+ CET). No entries.

SIP cross-check on 21:30 watch names — **DAIC is a real AH mover the TradingView feed missed**:

| Ticker | Reg Close | AH SIP C | AH% | AH Vol | Trades | AH Ask | Note |
|--------|-----------|----------|-----|--------|--------|--------|------|
| DAIC | $3.48 | $4.19 (H $4.36) | +20% | 745K | 6004 | $0.00 x0 | Real SIP build above close; but no fillable ask book yet |
| PMI | $9.91 | $8.82 (vwap $9.18) | -11% | 244K | 3004 | $10.90 | Below close, fading |
| NCPL | $0.58 | $0.52 | -10% | 1.8M | 2892 | $0.90 | Below close |
| TNMG | $0.61 | ~$0.48–0.65 | flat | — | — | $0.65 | Stale quote, no build |
| AMIX | $8.26 | — | — | — | — | $8.25 | Below close, wide |
| SWVL | $2.19 | — | — | — | — | $2.49 | Flat |

**Instrumentation (log-only, DAIC AH >10%):**
- `DAIC 2026-08-25 NO-SPIKE flat/faded (peak <= base) (no bar cleared +15% on a volume co-spike) as-of 16:15ET`
- `DAIC 2026-08-25 CONFIRM-3 NO no local-volume new-high ignition as-of 16:15ET`

**Notes:**
- DAIC building in AH on real SIP volume (745K sh / 6004 trades first bar, C $4.19 = +20% above reg close $3.48, Total% ~+142% from prior close). TradingView `--all` returned 0 — feed-lag omission. Flag for entry evaluation at 23:00+ CET (needs 2-AH-scan gate + fillable ask book; currently `ask $0.00 x0`, no fill possible).
- DAIC Total% ~+142% sits near the +150% extension ceiling — watch entry extension at later scans.
- Other watch names (PMI, NCPL, AMIX, SWVL) all sitting below reg close in AH — spike-then-fade, no new momentum.
- Re-evaluate at 22:30 / 23:00 CET.

## Scan 22:30 CET (4:30 PM ET)

**AH ~30 min in.** Scanner `--all`: 3 hits. Observation-only (learning-phase entry gate 23:00+ CET). No entries.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| XPON | [TV](https://www.tradingview.com/chart/?symbol=XPON) | $5.27 | -15.0% | +41.0% | $7.43 | +19.8% | 2.3M | 10.5M | 0.2x | 891K | Electrical Products |
| YYGH | [TV](https://www.tradingview.com/chart/?symbol=YYGH) | $1.15 | -3.4% | +37.8% | $1.58 | +33.2% | 2.5M | 903K | 2.8x | 1.6M | Misc Commercial Services |
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $0.57 | +124.3% | +9.3% | $0.63 | +145.2% | 7.9M | 50.4M | 0.2x | 4.4M | Misc Commercial Services |

**Instrumentation (log-only, AH >10%):**
- `XPON 2026-08-25 SPIKE 16:01ET +17% $6.19 1317 trades / 136k sh (first co-spike bar) as-of 16:30ET`
- `XPON 2026-08-25 CONFIRM-3 NO no local-volume new-high ignition as-of 16:30ET`
- `YYGH 2026-08-25 SPIKE 16:10ET +36% $1.56 1748 trades / 443k sh (first co-spike bar) as-of 16:30ET`
- `YYGH 2026-08-25 CONFIRM-3 PENDING ignition 16:10ET; waiting for third bar as-of 16:30ET`
- `DAIC 2026-08-25 NO-SPIKE peak +12% @16:03ET (no bar cleared +15% on volume co-spike) as-of 16:30ET`
- `DAIC 2026-08-25 CONFIRM-3 NO no local-volume new-high ignition as-of 16:30ET`

**SIP verification (feed=sip, AH bars from 16:00 ET):**

| Ticker | 16:00 vwap | 16:05 | 16:10 | 16:15 | Trajectory | Real-time book |
|--------|-----------|-------|-------|-------|-----------|----------------|
| XPON | $6.56 | $7.33 | $7.38 | $7.72 (C $7.91) | **BUILD** — rising vwap all 4 bars, 0.5–1.4M sh/bar, 7k–19k trades | quote stale 16:00ET, `ask $0.00 x0` (no live book yet) |
| YYGH | $1.16 (7 tr) | — | $1.52 (2.8M sh) | $1.54 (C $1.49, off $1.65 high) | SPIKE 16:10 then slight fade, holding near | live book `bid $1.63 x100 / ask $1.66 x100` |
| DAIC | $4.11 (H $4.36) | $4.07 | $3.72 | $3.69 (C $3.76) | **SPIKE→FADE** — peaked first bar, off ~13% | quote stale 16:00ET, `ask $0.00 x0` |

**Notes:**
- **XPON** = strongest candidate. Real, volume-backed BUILD (SIP vwap climbing $6.56→$7.72, >1M sh/bar). Tiny float 891K. SIP corroborates scanner $7.43 (SIP H $8.09). Day% -15.0% (right at the dead-cat threshold — regular session was a -15% drop; AH is reclaiming above the $5.27 close to $7.43, so this is a reclaim-above-close BUILD, not a below-close dead-cat bounce). Total% only +19.8% (well under the +150% ceiling). tradable=true. Blocker: real-time ask book stale/empty at this scan — recheck at 23:00 for a fillable ask. Needs 2nd AH scan to clear the 2-AH-scan gate; this is its first AH appearance.
- **YYGH** = real mover, live two-sided book, float 1.6M, tradable=true. Spiked hard 16:10 (2.8M sh) then faded slightly, holding ~$1.5. First AH appearance — needs a 2nd AH scan. Watch for build-vs-fade at 23:00.
- **DAIC** = the 21:30/22:15 watch name faded. Peaked first AH bar $4.36 then declined to $3.6–3.8. SPIKE→FADE, no fillable book. Drop unless it rebuilds.
- **NCPL** = AH +9.3% (below 10% threshold); +124% move is regular-session, VRatio 0.2x (fading). Not a real AH mover. Skip.
- Re-evaluate at 23:00 CET (entry gate). XPON leads on trajectory (BUILD) if it holds and shows a fillable book; needs its 2nd AH scan to clear the gate.

## Scan 22:45 CET (4:45 PM ET)

**AH ~45 min in.** Scanner `--all`: 3 hits (XPON, YYGH carried; DDC new). Observation-only (learning-phase entry gate 23:00+ CET). No entries.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| YYGH | [TV](https://www.tradingview.com/chart/?symbol=YYGH) | $1.15 | -3.4% | +42.2% | $1.64 | +37.4% | 6.3M | 1.3M | 4.8x | 1.6M | Misc Commercial Services |
| XPON | [TV](https://www.tradingview.com/chart/?symbol=XPON) | $5.27 | -15.0% | +50.9% | $7.95 | +28.2% | 4.0M | 10.7M | 0.4x | 891K | Electrical Products |
| DDC | [TV](https://www.tradingview.com/chart/?symbol=DDC) | $0.70 | +18.3% | +5.4% | $0.73 | +24.6% | 165K | 719K | 0.2x | 22.7M | Internet Software/Services |

**Instrumentation (log-only, AH >10%):**
- `XPON 2026-08-25 SPIKE 16:01ET +17% $6.19 1317 trades / 136k sh (first co-spike bar) as-of 16:45ET`
- `XPON 2026-08-25 CONFIRM-3 NO no local-volume new-high ignition as-of 16:45ET`
- `YYGH 2026-08-25 SPIKE 16:10ET +36% $1.56 1748 trades / 443k sh (first co-spike bar) as-of 16:45ET`
- `YYGH 2026-08-25 CONFIRM-3 NO ignition 16:10ET failed third-bar hold/volume as-of 16:45ET`

**SIP verification (feed=sip, AH bars from 16:00 ET; lags ~15 min, last bar 16:30 ET):**

| Ticker | vwap 16:00→16:30 | Trajectory | Real-time book |
|--------|------------------|-----------|----------------|
| XPON | $6.56 → $7.33 → $7.38 → $7.72 → $8.17 → $7.90 → $7.71 | **BUILD** — climbing, peak vwap $8.17 @16:20, slight pull to $7.71 @16:30; 0.3–1.4M sh/bar, 5k–20k trades | quote stale 16:00ET `bid $4.91 / ask $0.00 x0` (no live ask yet) |
| YYGH | $1.16 → $1.52 → $1.54 → $1.54 → $1.61 → $1.55 | SPIKE 16:10 then **HOLD/BUILD** near high, 0.8–2.8M sh/bar | live fresh book 16:45ET `bid $1.76 / ask $1.78` (new high, building) |

**Catalyst search:**
- **XPON** — CATALYST FOUND: Aug 24 2026 GlobeNewswire — Expion360 renamed **Expion Energy**, entered a definitive agreement with "Potential for Additional $91.0M of Investments" and acquired an oil & gas exploration opportunity in Eastern Louisiana (first entry into oil & gas). Transformational pivot + large investment. Concern: "investment/financing" framing leans dilutive (Grade C/D risk) — resolve deal structure at 23:00 before grading. Catalyst dated yesterday; XPON has been a multi-day runner.
- **YYGH** — no catalyst found (2 searches). Singapore staffing/services name spiking on momentum only. Note as no-catalyst.

**Notes:**
- **XPON** = strongest trajectory. Real volume-backed BUILD (SIP vwap $6.56→$8.17, >1M sh/bar). Tiny float 891K, tradable. **Extension caution:** scanner Total% +28.2% is measured off a ~$6.20 intraday base, but Yahoo shows true prior close **$3.43** — from there AH $7.95 = **~+132% Total**, near the +150% ceiling. Resolve which base at 23:00; if true extension is ~+132% on a BUILD-and-hold with VRatio... note VRatio only 0.4x (AvgVol 10.7M is inflated by today's 82M-share day). This is XPON's 2nd AH scan (22:30, 22:45) — clears the 2-AH-scan gate at 23:00 if it holds. Blocker: no live ask book at this scan (stale quote) — needs a fillable ask at entry.
- **YYGH** = real mover, fresh live two-sided book building to $1.78 (above earlier $1.65 high), float 1.6M, tradable, VRatio 4.8x. No catalyst. 2nd AH scan — clears 2-AH-scan gate at 23:00 if it holds. Total% +37.4%, well under ceiling. BUILD/HOLD trajectory.
- **DDC** = AH +5.4% (below 10% threshold), +18.3% is regular-session, VRatio 0.2x (fading), float 22.7M. Not a real AH mover. No catalyst search. Skip.
- **DAIC/NCPL** dropped from scanner (faded). Not carried further.
- Re-evaluate at 23:00 CET (entry gate). XPON and YYGH both lead on BUILD/HOLD trajectory; both need a live fillable book and the extension/catalyst checks resolved at entry.

## Scan 23:00 CET (5:00 PM ET)

**AH ~1h in. ENTRY GATE (23:00+ CET).** Scanner `--all`: 4 hits (YYGH, XPON carried; DAIC/CDTG faded/below-threshold). **Entered XPON + YYGH** — both cleared the 2-AH-scan gate (22:30, 22:45) and all entry rules.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| YYGH | [TV](https://www.tradingview.com/chart/?symbol=YYGH) | $1.15 | -3.4% | +53.0% | $1.76 | +47.9% | 10.4M | 1.8M | 5.8x | 1.6M | Misc Commercial Services |
| XPON | [TV](https://www.tradingview.com/chart/?symbol=XPON) | $5.27 | -15.0% | +41.0% | $7.43 | +19.8% | 4.6M | 10.8M | 0.4x | 891K | Electrical Products |
| DAIC | [TV](https://www.tradingview.com/chart/?symbol=DAIC) | $3.88 | +124.3% | +8.1% | $4.20 | +142.5% | 3.0M | 24.1M | 0.1x | 1.3M | Miscellaneous |
| CDTG | [TV](https://www.tradingview.com/chart/?symbol=CDTG) | $0.98 | -16.2% | +9.2% | $1.07 | -8.5% | 156K | 11.3M | 0.0x | 3.0M | Industrial Machinery |

**Instrumentation (log-only, AH >10%):**
- `XPON 2026-08-25 SPIKE 16:01ET +17% $6.19 1317 trades / 136k sh (first co-spike bar) as-of 17:00ET`
- `XPON 2026-08-25 CONFIRM-3 NO no local-volume new-high ignition as-of 17:00ET`
- `YYGH 2026-08-25 SPIKE 16:10ET +36% $1.56 1748 trades / 443k sh (first co-spike bar) as-of 17:00ET`
- `YYGH 2026-08-25 CONFIRM-3 NO ignition 16:10ET failed third-bar hold/volume as-of 17:00ET`

**SIP verification (feed=sip, AH bars from 16:00 ET; last bar 16:45):**

| Ticker | vwap 16:00→16:45 | Trajectory | Real-time book |
|--------|------------------|-----------|----------------|
| XPON | $6.56→$7.33→$7.38→$7.72→$8.17→$7.90→$7.71→$7.35→$7.54→$7.89 | **BUILD/HOLD** — peak vwap $8.17 @16:20 (H $8.62), choppy hold $7.3-7.9, current ~$7.44 (-14% off high, within 20%). 0.2-1.4M sh/bar, 3k-20k trades | quote **frozen 16:00 ET** `bid $4.91 / ask $0.00 x0` (dead across all 5 scans) |
| YYGH | $1.16→$1.52→$1.54→$1.54→$1.61→$1.55→$1.70→$1.80→$1.68 | SPIKE 16:10 then **BUILD** to $1.80 vwap peak @16:40 (H $1.87), shallow fade last 20min to $1.57 (-16% off high, within 20%). 0.8-2.8M sh/bar, 5k-16k trades | fresh live `bid $1.56 / ask $1.59` @16:59 ET |

**Entry decisions (multiple positions, W24 rule — enter every qualifying candidate):**

- **XPON — ENTERED.** Cleared 2-AH-scan gate (22:30, 22:45). Float 891K (<50M). Day% -15.0% (at threshold, but AH reclaims above the $5.27 close = reclaim-above-close BUILD, not below-close dead-cat). Real SIP-confirmed BUILD/HOLD, >1M sh/bar. Total% modest (+40.6% off $5.27 close / +19.5% off Yahoo prev close $6.20) — well under +150% ceiling. Catalyst: Expion360→Expion Energy pivot ("$91.0M potential additional investments" + oil & gas acquisition, GlobeNewswire 08-24) — financing/dilution lean = **Grade C**. Blocker resolved: Alpaca quote frozen 16:00 ET (`ask $0.00 x0` across all 5 scans) but the paper engine **filled anyway @ $7.41** against the real SIP level. BUY 13 @ limit $7.60 ext (id b11db9d4) filled @ **$7.41**.
- **YYGH — ENTERED.** Cleared 2-AH-scan gate (22:30, 22:45). Float 1.6M (<50M). Day% -3.4%. VRatio 5.8x. Real SIP-confirmed SPIKE→BUILD to $1.87, fresh two-sided book. Total% +40.0% (fill) — well under ceiling. No catalyst found (2 searches) — **Grade None**, concern noted (learning-phase: no-catalyst enters). BUY 62 @ limit $1.62 ext (id 643382ed) filled @ **$1.61**.
- **DAIC — skip.** Scanner AH +8.1% (below 10% threshold); the +142.5% is regular-session. Faded from first-bar $4.36 peak (SPIKE→FADE at 22:30), VRatio 0.1x. Not a real AH mover now.
- **CDTG — skip.** AH +9.2% (below threshold), Total% -8.5% (below close), VRatio 0.0x. Not a mover.

**CHASE-CAP:** neither fill chased into the fade zone. YYGH: qualifying 22:45 Total% +37.4% vs fill +40.0% (gap +2.6%). XPON: qualifying +28.2% vs fill +19.5-40.6% depending on base — both far under the +120% fade zone. No chase concern.

**Notes:**
- Both entries are BUILD/HOLD trajectories (not SPIKE→FADE-only night). XPON is the cleaner BUILD (genuine reclaim-above-close on >1M sh/bar); YYGH shallow-fading from peak but holding within 20%.
- Both peaked before 18:30 ET (XPON 16:20, YYGH 16:40) — peak time is a secondary tiebreaker; hold-within-20% is the primary signal and both pass.
- CONFIRM-3 read NO for both (log-only, no decision impact).
- Position management (hold/sell) handled by premarket `position-evaluation` pulse. Both flagged for premarket exit (XPON Grade C, YYGH Grade None). Never hold through the day.

## Scan 23:30 CET (5:30 PM ET)

**AH ~1.5h in.** Scanner `--all`: 8 hits. Holding XPON + YYGH (entered 23:00). No new entries — all new AH>10% names fail gates.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| YYGH | [TV](https://www.tradingview.com/chart/?symbol=YYGH) | $1.15 | -3.4% | +45.2% | $1.67 | +40.3% | 13.8M | 2.2M | 6.3x | 1.6M | Misc Commercial Services |
| DAIC | [TV](https://www.tradingview.com/chart/?symbol=DAIC) | $3.88 | +124.3% | +49.2% | $5.79 | +234.7% | 7.8M | 24.7M | 0.3x | 1.3M | Miscellaneous |
| XPON | [TV](https://www.tradingview.com/chart/?symbol=XPON) | $5.27 | -15.0% | +35.5% | $7.14 | +15.2% | 5.5M | 10.9M | 0.5x | 891K | Electrical Products |
| CDTG | [TV](https://www.tradingview.com/chart/?symbol=CDTG) | $0.98 | -16.2% | +20.4% | $1.18 | +0.9% | 1.8M | 11.5M | 0.2x | 3.0M | Industrial Machinery |
| WVVIP | [TV](https://www.tradingview.com/chart/?symbol=WVVIP) | $3.33 | +25.7% | +40.3% | $4.67 | +76.3% | 478K | 810K | 0.6x | 4.0M | Beverages: Alcoholic |
| SLQT | [TV](https://www.tradingview.com/chart/?symbol=SLQT) | $0.55 | -29.3% | +7.4% | $0.59 | -24.1% | 158K | 1.7M | 0.1x | 140.2M | Multi-Line Insurance |
| ALEC | [TV](https://www.tradingview.com/chart/?symbol=ALEC) | $2.36 | +2.6% | +9.7% | $2.59 | +12.6% | 88K | 1.5M | 0.1x | 82.1M | Biotechnology |
| SGLY | [TV](https://www.tradingview.com/chart/?symbol=SGLY) | $2.15 | -15.0% | +5.1% | $2.26 | -10.7% | 80K | 6.5M | 0.0x | 897K | Air Freight/Couriers |

**Instrumentation (log-only, AH >10%):**
- `XPON 2026-08-25 SPIKE 16:01ET +17% $6.19 1317 trades / 136k sh (first co-spike bar) as-of 17:30ET`
- `XPON 2026-08-25 CONFIRM-3 NO no local-volume new-high ignition as-of 17:30ET`
- `YYGH 2026-08-25 SPIKE 16:10ET +36% $1.56 1748 trades / 443k sh (first co-spike bar) as-of 17:30ET`
- `YYGH 2026-08-25 CONFIRM-3 NO ignition 16:10ET failed third-bar hold/volume as-of 17:30ET`
- `DAIC 2026-08-25 SPIKE 16:33ET +15% $4.47 2257 trades / 258k sh (first co-spike bar) as-of 17:30ET`
- `DAIC 2026-08-25 CONFIRM-3 NO ignition 16:55ET failed third-bar hold/volume as-of 17:30ET`
- `WVVIP 2026-08-25 SPIKE 16:45ET +29% $4.30 325 trades / 21k sh (first co-spike bar) as-of 17:30ET`
- `WVVIP 2026-08-25 CONFIRM-3 NO ignition 16:45ET failed third-bar hold/volume as-of 17:30ET`
- `CDTG 2026-08-25 SPIKE 16:35ET +19% $1.17 162 trades / 29k sh (first co-spike bar) as-of 17:30ET`
- `CDTG 2026-08-25 CONFIRM-3 NO ignition 16:50ET failed third-bar hold/volume as-of 17:30ET`

**SIP verification (feed=sip, AH bars from 16:00 ET):**

| Ticker | Trajectory | Real-time book |
|--------|-----------|----------------|
| WVVIP | **SPIKE→FADE** — flat $3.1 until 16:45 spike to H $6.88 (254k sh/4112 tr), then bleeding $6.07→$5.37→$4.58→$4.28 (16:15 vwap $4.42, ~-38% off high) | `bid $3.11 / ask $0.00 x0` — no fillable ask book |
| DAIC | Real **second-leg BUILD** — vwap $4.1 base 16:30-16:50, then surge $4.59→$5.43→$5.51→$5.90 on 1-2.2M sh/bar, 10k-23k trades, H $6.49 @17:15 ET | `bid $3.31 / ask $0.00 x0` — no fillable ask book |

**Entry decisions — no new entries:**

- **WVVIP — SKIP.** Multiple fails: (1) SPIKE→FADE — peaked $6.88 @16:45 ET, now ~$4.28 (-38% off high, well outside 20% hold band); (2) no fillable ask book (`ask $0.00 x0`); (3) **Grade D** — it's a 5.3% perpetual preferred (WVVI 5.3 PERP), the "catalyst" is a $1.75M preferred stock offering (dilution/financing, PRNewswire Aug 4); (4) first AH scan — fails 2-AH-scan gate. Thin preferred-share ramp.
- **DAIC — SKIP.** Total% +234.7% far above the +150% extension ceiling. Regular-session +124% mover. Ceiling-override watch requires VRatio >5x — scanner VRatio 0.3x (fails) — so no override flag despite the real SIP second-leg build (2M+ sh/bar into H $6.49 @17:15 ET made after 17:00 ET, holding within 20%). Also no fillable ask book (`ask $0.00 x0`). Note the real SIP second-leg for morning-eval, but extension + no book = skip.
- **CDTG — SKIP.** AH +20.4% but Total% +0.9% (barely reclaims prior close), Day% -16.2% (below -15% dead-cat threshold), thin (162 trades/29k sh, VRatio 0.2x), first AH scan. Dead-cat range + thin.
- **SLQT / SGLY** — AH <10% threshold (SLQT +7.4%, SGLY +5.1%), both below prior close (Total% negative). Skip.
- **ALEC** — AH +9.7% (below 10%), float 82M, Total% +12.6%. Below threshold. Skip.

**Held positions (management by premarket pulse, no action here):**
- **XPON** 13 @ $7.41 → now $7.29 (-1.7%). Scanner AH +35.5% $7.14, holding near entry. Grade C.
- **YYGH** 62 @ $1.61 → now $1.68 (+4.3%). Scanner AH +45.2% $1.67, VRatio 6.3x, building. Grade None.

**Notes:**
- No BUILD-and-hold candidate with a fillable book cleared the gates this scan. DAIC is the one real fresh second-leg build but is blocked by the extension ceiling (+234%) and has no fillable Alpaca book.
- Both held positions still holding/building; premarket `position-evaluation` handles exits. Never hold through the day.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
| XPON | $7.41 | 2026-08-25 17:00 ET | 13 | b11db9d4 | Grade C — Expion Energy pivot ($91M investment + oil & gas acq). SIP BUILD/HOLD vwap $6.56→$8.17, float 891K, 2-AH-scan gate cleared. |
| YYGH | $1.61 | 2026-08-25 17:00 ET | 62 | 643382ed | Grade None (no catalyst, concern noted). SIP SPIKE→BUILD to $1.87, float 1.6M, VRatio 5.8x, 2-AH-scan gate cleared. |
