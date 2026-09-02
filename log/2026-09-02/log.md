
## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| KITT | $1.02 | $0.87 | -14.7% | $0.99 (-2.9%) | 0 | B | SELL | At -15% hard stop; PM opened $0.92 then faded, no follow-through |
| PXS | $6.26 | $5.98 | -4.5% | $6.68 (+6.7%) | 2 | B | SELL | Grade B day-2 time limit reached; above stop, thin PM book |

**Actions taken:**
- SELL 93 KITT @ limit $0.84 ext (id 58ea9bc1) filled @ $0.87 → -$13.95 (-14.7%)
- SELL 15 PXS @ limit $5.90 ext (id f225e53c) filled @ $5.98 → -$4.20 (-4.5%)
- Both stale Alpaca quotes (KITT bid $0.69, PXS ask $0.00 x0); priced off SIP levels
- No open positions remain

## Position Evaluation — 14:30 CET

No open positions (Alpaca source of truth). Clean slate after 10:30 CET pulse (KITT + PXS exited). OPEN_POSITIONS.md agrees. Nothing to evaluate.

**Actions taken:**
- None

## Scan 21:30 CET (3:30 PM ET)

Regular session — AH opens 22:00 CET (16:00 ET). No entries this scan (regular-session caution). Candidates flagged Watch — pending AH confirmation. Only re-enter evaluation if they reappear in AH scans (22:00+ CET) with sustained momentum.

| Ticker | Chart | Price | Day% | 5mVol | AvgVol | IRVol | Float | MCap | Industry | Note |
|--------|-------|-------|------|-------|--------|-------|-------|------|----------|------|
| TRTI | [TV](https://www.tradingview.com/chart/?symbol=TRTI) | $3.82 | +27.3% | 8K | 9K | 21.4 | 2.1M | 12.6M | Electric Utilities | Watch — low float |
| LHSW | [TV](https://www.tradingview.com/chart/?symbol=LHSW) | $3.76 | +30.6% | 8K | 5K | 5.5 | 1.0M | 12.9M | Computer Processing Hardware | Watch — low float |
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $1.03 | +30.1% | 33K | 50K | 0.5 | 4.4M | 8.1M | Misc Commercial Services | Watch — IRVol fading (0.5) |
| SWVL | [TV](https://www.tradingview.com/chart/?symbol=SWVL) | $5.22 | +36.3% | 313 | 22K | 0.3 | 5.3M | 52.0M | Other Transportation | Watch — vol faded |
| LHAI | [TV](https://www.tradingview.com/chart/?symbol=LHAI) | $1.09 | +32.8% | 100 | 156K | 434.2 | 9.7M | 18.0M | Packaged Software | Watch — vol faded intraday |
| GPRO | [TV](https://www.tradingview.com/chart/?symbol=GPRO) | $1.72 | +39.9% | 1K | 4.6M | 4.0 | 125.1M | 164.0M | Electronics/Appliances | Watch — float 125M (high) |

Other movers (higher price / weaker profile): TRTI leads low-float list. No paper trades — waiting for AH scans to confirm which names carry momentum past 16:00 ET. Most listed names already show fading intraday IRVol (5mVol below Avg5m), a caution sign for AH follow-through.

## Scan 22:00 CET (4:00 PM ET)

No candidates found. Scanner 0 hits at AH open (16:00 ET). SIP shows no AH bars yet for the 21:30 watch names (TRTI, LHSW, LHAI — `no bars`, feed sparse at the open minute). No entries (observation-only before 23:00 CET, and no qualifying candidate anyway). Re-check watch names at 22:30/23:00 for AH carry.

## Scan 22:15 CET (4:15 PM ET)

No candidates found. Scanner 0 hits at 16:15 ET (same as 22:00). Cross-checked 21:30 watch names via SIP first AH bar (16:00-16:05 ET):

| Ticker | AH C | vs Reg | AH Vol | Trades | Note |
|--------|------|--------|--------|--------|------|
| TRTI | — | — | 0 | 0 | no AH bars (no liquidity) |
| LHSW | $3.75 | flat | 12.8K | 6 | flat, 6 trades — thin |
| NCPL | $1.00 | −3% | 96.8K | 151 | fading off close |
| SWVL | $4.90 | −6% | 16.2K | 164 | fading |
| LHAI | $1.12 | flat | 150K | 234 | flat vs close |
| GPRO | $1.64 | −5% | 1.87M | 2147 | fading, float 125M |

None building in AH — all flat or fading off regular close, none igniting. No entries (observation-only before 23:00 CET, and no qualifying candidate). Re-check at 22:30/23:00 for late AH carry.

## Scan 22:30 CET (4:30 PM ET)

Two hits — both fresh AH igniters on today's earnings. First AH appearance for each (need 2nd AH scan to clear the 2-scan gate). Observation-only (before 23:00 CET), no entries.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| TLYS | [TV](https://www.tradingview.com/chart/?symbol=TLYS) | $3.81 | -3.8% | +24.7% | $4.75 | +19.9% | 336K | 202K | 1.7x | 22.2M | Apparel/Footwear Retail |
| CHPT | [TV](https://www.tradingview.com/chart/?symbol=CHPT) | $5.19 | -2.1% | +17.5% | $6.10 | +15.1% | 172K | 420K | 0.4x | 22.7M | Electrical Products |

**Catalysts (both earnings, Grade B):**
- **TLYS** — Q2 fiscal 2026 earnings after close (scheduled Sept 2). Beat: net income $8.4M, comp sales +12.1%, e-commerce +20.9%. Earnings beat = Grade B.
- **CHPT** — Q2 earnings reported after close Sept 2. Grade B (earnings report). Confirm beat/miss at next scan.

**Instrumentation (log-only):**
- TLYS: SPIKE 16:05ET +19% $4.55 58 trades / 6k sh. CONFIRM-3 YES ignition 16:05ET 12.4x; confirmed 16:15ET $5.05.
- CHPT: SPIKE 16:11ET +19% $6.20 272 trades / 34k sh. CONFIRM-3 PENDING (waiting third bar).

**SIP volume (real, accumulating):**
- TLYS bars 16:00→16:15 ET: vol 6k→80k→334k→562k, trades 8→504→2764→6080, vwap $3.81→$4.96, C $5.05. Strong BUILD, still rising.
- CHPT bars 16:00→16:15 ET: vol 80k→8k→108k→66k, trades 77→141→1179→626, vwap $5.19→$6.03, C $6.07. Ignition bar 16:10 ET, holding ~$6.

Both under +150% ceiling, Day% above -15%, float 22M (recorded, not a gate). No entries (observation-only). Re-check at 23:00 CET for 2nd-scan confirmation and entry evaluation.

## Scan 22:45 CET (4:45 PM ET)

Three hits. TLYS and CHPT carried from 22:30 (2nd AH scan — clears the 2-AH-scan gate). BRNX new (+13.9% AH), thin. Observation-only (before 23:00 CET), no entries.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| TLYS | [TV](https://www.tradingview.com/chart/?symbol=TLYS) | $3.81 | -3.8% | +35.9% | $5.18 | +30.8% | 1.5M | 338K | 4.4x | 22.2M | Apparel/Footwear Retail |
| CHPT | [TV](https://www.tradingview.com/chart/?symbol=CHPT) | $5.19 | -2.1% | +17.3% | $6.09 | +14.9% | 354K | 442K | 0.8x | 22.7M | Electrical Products |
| BRNX | [TV](https://www.tradingview.com/chart/?symbol=BRNX) | $3.16 | -10.2% | +13.9% | $3.60 | +2.3% | 52K | 3.1M | 0.0x | 684K | Engineering & Construction |

**Progress vs 22:30:**
- **TLYS** — building: AH +24.7%→+35.9%, VRatio 1.7x→4.4x, AH Vol 336K→1.5M. Strong accumulation, real BUILD. Grade B (earnings beat: net income $8.4M, comp sales +12.1%).
- **CHPT** — flat/holding: AH +17.5%→+17.3%, holding ~$6.1. Grade B (earnings).
- **BRNX** — new, thin: VRatio 0.0x, AH Vol 52K vs AvgVol 3.1M. Was down -18.9% Sept 1. **No catalyst found** (BrenX Ltd, formerly Brenmiller Energy). NO-SPIKE, peak +16% @16:27ET.

**Instrumentation (log-only):**
- TLYS: SPIKE 16:05ET +19% $4.55 58 trades / 6k sh. CONFIRM-3 YES ignition 16:05ET 12.4x; confirmed 16:15ET $5.05.
- CHPT: SPIKE 16:11ET +19% $6.20 272 trades / 34k sh. CONFIRM-3 NO ignition 16:10ET failed third-bar hold/volume.
- BRNX: NO-SPIKE peak +16% @16:27ET. CONFIRM-3 PENDING (waiting third bar).

**SIP volume:**
- TLYS: accumulating strongly per 22:30 read (vol 6k→80k→334k→562k, trades to 6080), building.
- BRNX bars 16:00→16:30 ET: vol 21k→16k→4k→5k→4k→13k→6k, trades 282→175→52→38→55→140→111. Thin, not accumulating. Quote `bid $2.72 ask $3.63` (stale open-minute). Thin drift, not a build.

Both TLYS and CHPT now clear the 2-AH-scan gate. TLYS is the standout (BUILD + Grade B earnings + rising VRatio); CHPT holding but CONFIRM-3 NO. BRNX thin/no-catalyst — skip regardless. No entries this scan (observation-only before 23:00 CET). Enter evaluation at 23:00 CET.

## Scan 23:00 CET (5:00 PM ET) — ENTRY SCAN

8 hits. Entries allowed (23:00+ CET). Two names clear the 2-AH-scan gate and all entry rules: **TLYS** and **CHPT** — both entered (multiple positions allowed, W24 2026).

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| TLYS | [TV](https://www.tradingview.com/chart/?symbol=TLYS) | $3.81 | -3.8% | +27.5% | $4.86 | +22.7% | 2.1M | 416K | 4.9x | 22.2M | Apparel/Footwear Retail |
| CHPT | [TV](https://www.tradingview.com/chart/?symbol=CHPT) | $5.19 | -2.1% | +19.1% | $6.18 | +16.6% | 532K | 464K | 1.1x | 22.7M | Electrical Products |
| NCT | [TV](https://www.tradingview.com/chart/?symbol=NCT) | $4.90 | -6.1% | +11.4% | $5.46 | +4.6% | 605K | 2.4M | 0.2x | 8.5M | Marine Shipping |
| UFG | [TV](https://www.tradingview.com/chart/?symbol=UFG) | $0.56 | +3.8% | +10.7% | $0.62 | +14.9% | 543K | 697K | 0.8x | 9.8M | Wholesale Distributors |
| BIAF | [TV](https://www.tradingview.com/chart/?symbol=BIAF) | $9.75 | +48.0% | +7.5% | $10.48 | +59.1% | 510K | 9.3M | 0.1x | 573K | Medical Specialties |
| NYXH | [TV](https://www.tradingview.com/chart/?symbol=NYXH) | $1.51 | +1.3% | +11.2% | $1.68 | +12.7% | 358K | 149K | 2.4x | 81.3M | Medical Specialties |
| XTIA | [TV](https://www.tradingview.com/chart/?symbol=XTIA) | $0.95 | -17.4% | +6.3% | $1.01 | -12.2% | 68K | 943K | 0.1x | 38.4M | IT Services |
| BRNX | [TV](https://www.tradingview.com/chart/?symbol=BRNX) | $3.16 | -10.2% | +8.9% | $3.44 | -2.3% | 62K | 3.1M | 0.0x | 684K | Engineering & Construction |

**ENTERED — TLYS (Grade B earnings beat):**
- 4th AH appearance (22:30 +24.7%, 22:45 +35.9%, 23:00 +27.5% AH) — cleared 2-AH-scan gate.
- Day% -3.8% (above -15%), Total% +22.7% (under +150% ceiling), float 22.2M (recorded).
- BUILD confirmed. SIP 16:00→16:45 ET: vol 6k→80k→334k→562k→336k→483k→415k→159k→159k→286k, trades to 6080/bar, holding $4.8-5.2, vwap $4.96-5.10. Real, sustained accumulation.
- SPIKE 16:05ET +19% $4.55 58 trades / 6k sh. CONFIRM-3 YES ignition 16:05ET 12.4x; confirmed 16:15ET $5.05.
- tradable=true, fillable. Catalyst Grade B: Q2 FY2026 earnings beat (net income $8.4M, comp sales +12.1%, e-commerce +20.9%).
- **Fill: 19 @ $5.15** (limit $5.15 ext, id 921abfa7).
- **CHASE-CAP:** qualifying 23:00 AH $4.86/+22.7%; first limit $4.95 rested unfilled (Alpaca book stale @16:12 ET, SIP real ~$5.05-5.10); repriced $5.15, filled $5.15/+35.2%. Chase gap +12.5% (fill Total% − qualifying Total%). Well under the +120% fade zone.
- **MULTI-SESSION check:** fresh day-1 igniter (Day% -3.8%, pure AH earnings pop, not in WINNERS_TRACKING).

**ENTERED — CHPT (Grade B earnings):**
- 3rd AH appearance (22:30 +17.5%, 22:45 +17.3%, 23:00 +19.1% AH) — cleared 2-AH-scan gate.
- Day% -2.1% (above -15%), Total% +16.6% (under ceiling), float 22.7M (recorded).
- Holding ~$6.1-6.2 within 3% of AH high $6.42 (hold, not fade). SIP 16:00→16:45 ET: real volume 80k/8k/108k/66k/137k/19k/118k/82k/19k/29k sh, vwap climbing $5.19→$6.17, C $6.20. Real, thinning into later bars but holding.
- SPIKE 16:11ET +19% $6.20 272 trades / 34k sh. CONFIRM-3 **NO** ignition 16:10ET failed third-bar hold/volume (instrumentation only, not a gate).
- tradable=true. Catalyst Grade B: Q2 earnings reported after close.
- **Fill: 16 @ $6.21** (limit $6.30 ext, id 46d8ab1e).
- **CHASE-CAP:** qualifying 23:00 AH $6.18/+16.6%; fill $6.21/+19.7%. Chase gap +3.1% (minimal).
- **MULTI-SESSION check:** fresh day-1 igniter (Day% -2.1%, pure AH earnings pop, not in WINNERS_TRACKING).

**Skipped:**
- **NCT** — VRatio 0.2x, AH Vol 605K vs AvgVol 2.4M, thin/not accumulating. Skip.
- **UFG** — first AH appearance, no 2nd AH scan yet (2-scan gate). Re-check 23:30/00:00.
- **BIAF** — Day% +48% already ran regular session (not fresh first-day AH ignition), AH chg only +7.5%, VRatio 0.1x thin. Skip.
- **NYXH** — first AH appearance (2-scan gate), float 81.3M. Re-check next scan.
- **XTIA** — Day% -17.4% below the -15% floor, Total% negative. Skip.
- **BRNX** — carried, thin (VRatio 0.0x), no catalyst found. Skip.

## Scan 23:30 CET (5:30 PM ET) — ENTRY SCAN

11 hits. TLYS and CHPT already entered at 23:00 (managed by premarket position-evaluation, not re-entered). Two names newly clear the 2-AH-scan gate: **UFG** (entered) and **NYXH** (skipped).

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| UFG | [TV](https://www.tradingview.com/chart/?symbol=UFG) | $0.56 | +3.8% | +26.7% | $0.71 | +31.5% | 7.0M | 1.4M | 5.1x | 9.8M | Wholesale Distributors |
| GELS | [TV](https://www.tradingview.com/chart/?symbol=GELS) | $0.70 | +31.6% | +11.7% | $0.78 | +47.0% | 3.1M | 5.8M | 0.5x | n/a | Pharmaceuticals: Major |
| TLYS | [TV](https://www.tradingview.com/chart/?symbol=TLYS) | $3.81 | -3.8% | +31.5% | $5.01 | +26.5% | 2.8M | 508K | 5.5x | 22.2M | Apparel/Footwear Retail |
| NCT | [TV](https://www.tradingview.com/chart/?symbol=NCT) | $4.90 | -6.1% | +6.3% | $5.21 | -0.2% | 719K | 2.4M | 0.3x | 8.5M | Marine Shipping |
| BIAF | [TV](https://www.tradingview.com/chart/?symbol=BIAF) | $9.75 | +48.0% | +6.2% | $10.35 | +57.1% | 653K | 9.3M | 0.1x | 573K | Medical Specialties |
| CHPT | [TV](https://www.tradingview.com/chart/?symbol=CHPT) | $5.19 | -2.1% | +18.7% | $6.16 | +16.2% | 596K | 471K | 1.3x | 22.7M | Electrical Products |
| NYXH | [TV](https://www.tradingview.com/chart/?symbol=NYXH) | $1.51 | +1.3% | +12.6% | $1.70 | +14.1% | 502K | 167K | 3.0x | 81.3M | Medical Specialties |
| XTIA | [TV](https://www.tradingview.com/chart/?symbol=XTIA) | $0.95 | -17.4% | +7.4% | $1.02 | -11.3% | 113K | 948K | 0.1x | 38.4M | IT Services |
| MIMI | [TV](https://www.tradingview.com/chart/?symbol=MIMI) | $0.64 | -10.2% | +7.7% | $0.69 | -3.3% | 91K | 6.2M | 0.0x | 3.7M | Misc Commercial Services |
| BRNX | [TV](https://www.tradingview.com/chart/?symbol=BRNX) | $3.16 | -10.2% | +9.8% | $3.47 | -1.4% | 70K | 3.1M | 0.0x | 684K | Engineering & Construction |
| BIVI | [TV](https://www.tradingview.com/chart/?symbol=BIVI) | $2.03 | -9.4% | +6.6% | $2.16 | -3.4% | 52K | 7.7M | 0.0x | 8.1M | Biotechnology |

**ENTERED — UFG (Grade None, no catalyst found):**
- Uni-Fuels Holdings (marine fuel trader, Singapore). 2nd AH appearance (23:00 +10.7% → 23:30 +26.7% AH) — cleared 2-AH-scan gate.
- Float 9.8M (ideal <10M), Day% +3.8% (fresh day-1 igniter), Total% +31.5% (under +150% ceiling), VRatio 5.1x.
- **Night's strongest, realest BUILD.** SIP 16:00→17:15 ET: vol ramp to 441K→1.09M→1.0M→1.38M→680K→1.83M→842K→963K sh/bar, thousands of trades/bar (to 6273), vwap $0.56→$0.77. Massive sustained accumulation.
- Yahoo AH: peaked $0.75 @17:05 ET (+39.6%), dipped to $0.61 @17:20, recovering $0.64→$0.66 @17:30-17:31. Current ~12% off AH high = holding within 20%.
- SPIKE 16:43 ET +27% $0.71 257 trades / 119K sh. CONFIRM-3 **YES** ignition 16:40 ET 11.1x; confirmed 16:50 ET $0.73.
- tradable=true. Alpaca quote stale (`ask $0.00 x0` @16:00 ET open minute; re-pull returned same stale timestamp) — SIP shows real fillable liquidity (963K sh last bar), so limit rested and filled.
- **No same-day catalyst found** (3 searches): Nasdaq bid-noncompliance notice July 31, Q1 results May 26, FY guidance raise May — nothing dated Sept 2. Grade None, entered with concern noted (learning-phase rule).
- **Fill: 147 @ $0.64** (limit $0.68 ext, id 144bcf15).
- **CHASE-CAP:** qualifying 23:30 scanner AH $0.71/+31.5% (30-min lagged); fill $0.64/+14.3%. Chase gap −17.2% (filled BELOW the lagged scanner price — bought the real-time dip, no chase into fade zone).
- **MULTI-SESSION check:** fresh day-1 igniter (Day% +3.8%, pure AH ignition, not in WINNERS_TRACKING).

**Skipped:**
- **NYXH** — 2nd AH scan (cleared gate) but early single-bar spike: SIP $1.93 @16:30 ET on one 320K-sh bar, then volume thinned hard (per-bar 6K-73K sh, hundreds of trades). Holding ~$1.70 (12% off high) but that is thin drift after an early spike, not a build. SPIKE 16:33 ET, CONFIRM-3 **NO**. Float 81.3M. Skip: early-peak thin-drift + CONFIRM-3 NO.
- **GELS** — Day% +31.6% already ran regular session (not fresh first-day AH ignition), VRatio 0.5x thin, Total% +47%, float n/a. Skip.
- **TLYS / CHPT** — already entered at 23:00 (position management handled in premarket).
- **NCT** — carried, VRatio 0.3x, AH Chg +6.3%, thin/not accumulating. Skip.
- **BIAF** — Day% +48% already ran, AH chg +6.2%, VRatio 0.1x thin. Skip.
- **XTIA** — Day% -17.4% below the -15% floor, Total% negative. Skip.
- **MIMI / BIVI** — new, VRatio 0.0x thin, Day% negative. Skip.
- **BRNX** — carried, VRatio 0.0x thin, no catalyst found. Skip.

## Scan 00:00 CET (6:00 PM ET)

12 hits. No new qualifying candidates. TLYS, CHPT, UFG already entered (managed in premarket, not re-entered). All names with AH Chg >10% are already handled; new names this scan (GYGY, JLHL, LHAI) are below the 10% AH threshold and thin.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| UFG | [TV](https://www.tradingview.com/chart/?symbol=UFG) | $0.56 | +3.8% | +18.1% | $0.66 | +22.5% | 8.7M | 1.6M | 5.6x | 9.8M | Wholesale Distributors |
| GELS | [TV](https://www.tradingview.com/chart/?symbol=GELS) | $0.70 | +31.6% | +37.2% | $0.96 | +80.5% | 8.5M | 6.4M | 1.3x | n/a | Pharmaceuticals: Major |
| TLYS | [TV](https://www.tradingview.com/chart/?symbol=TLYS) | $3.81 | -3.8% | +33.9% | $5.10 | +28.8% | 3.0M | 530K | 5.6x | 22.2M | Apparel/Footwear Retail |
| LHAI | [TV](https://www.tradingview.com/chart/?symbol=LHAI) | $1.10 | +34.0% | +5.5% | $1.16 | +41.3% | 1.9M | 9.3M | 0.2x | 9.7M | Packaged Software |
| NCT | [TV](https://www.tradingview.com/chart/?symbol=NCT) | $4.90 | -6.1% | +6.5% | $5.22 | +0.0% | 738K | 2.4M | 0.3x | 8.5M | Marine Shipping |
| BIAF | [TV](https://www.tradingview.com/chart/?symbol=BIAF) | $9.75 | +48.0% | +7.0% | $10.43 | +58.3% | 704K | 9.3M | 0.1x | 573K | Medical Specialties |
| CHPT | [TV](https://www.tradingview.com/chart/?symbol=CHPT) | $5.19 | -2.1% | +20.0% | $6.23 | +17.5% | 642K | 477K | 1.3x | 22.7M | Electrical Products |
| NYXH | [TV](https://www.tradingview.com/chart/?symbol=NYXH) | $1.51 | +1.3% | +15.2% | $1.74 | +16.8% | 544K | 172K | 3.2x | 81.3M | Medical Specialties |
| GYGY | [TV](https://www.tradingview.com/chart/?symbol=GYGY) | $1.73 | +25.4% | +5.8% | $1.83 | +32.6% | 294K | 7.9M | 0.0x | 17K | Packaged Software |
| MIMI | [TV](https://www.tradingview.com/chart/?symbol=MIMI) | $0.64 | -10.2% | +7.7% | $0.69 | -3.3% | 91K | 6.2M | 0.0x | 3.7M | Misc Commercial Services |
| BRNX | [TV](https://www.tradingview.com/chart/?symbol=BRNX) | $3.16 | -10.2% | +12.0% | $3.54 | +0.6% | 78K | 3.1M | 0.0x | 684K | Engineering & Construction |
| JLHL | [TV](https://www.tradingview.com/chart/?symbol=JLHL) | $6.33 | +12.6% | +5.7% | $6.69 | +19.0% | 52K | 1.3M | 0.0x | 1.3M | Misc Commercial Services |

**Positions (Alpaca, entered earlier tonight):**
- TLYS 19 @ $5.15 → now $5.15 (+0.0%); AH +33.9%, VRatio 5.6x, still building.
- CHPT 16 @ $6.21 → now $6.18 (-0.5%); AH +20.0%, holding ~$6.2.
- UFG 147 @ $0.64 → now $0.68 (+5.7%); AH +18.1%, VRatio 5.6x, still the night's strongest BUILD.

**New/other names — all skip:**
- **GYGY** — AH Chg +5.8% (below 10% gate), Day% +25.4% already ran regular session, VRatio 0.0x thin, float 17K. Skip.
- **JLHL** — AH Chg +5.7% (below 10% gate), VRatio 0.0x thin, AH Vol 52K. Skip.
- **LHAI** — AH Chg +5.5% (below 10% gate), Day% +34% already ran regular, VRatio 0.2x thin. Skip.
- **GELS** — Day% +31.6% already ran regular (not fresh AH ignition), VRatio 1.3x, Total% +80.5%, float n/a. Skip (carried).
- **NYXH** — early-peak thin-drift + CONFIRM-3 NO, float 81.3M (carried skip).
- **NCT / BIAF / MIMI / BRNX** — thin (VRatio ≤0.3x) / already-ran / no-catalyst (carried skips).

No entries this scan (no new candidate clears the 2-AH-scan gate with >10% AH). Final scheduled scan at 00:30 CET.

## Scan 00:30 CET (6:30 PM ET) — FINAL SCAN

10 hits. Final scheduled scan. TLYS, CHPT, UFG already entered (managed in premarket). Final-scan feed-lag cross-check on pipeline names revealed **GELS** as a real, volume-backed BUILD that had been skipped 3× on a weak "already ran regular session" reason — re-evaluated and **entered**.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| GELS | [TV](https://www.tradingview.com/chart/?symbol=GELS) | $0.70 | +31.6% | +42.3% | $1.00 | +87.3% | 10.3M | 6.6M | 1.6x | n/a | Pharmaceuticals: Major |
| UFG | [TV](https://www.tradingview.com/chart/?symbol=UFG) | $0.56 | +3.8% | +17.4% | $0.66 | +21.8% | 9.6M | 1.7M | 5.8x | 9.8M | Wholesale Distributors |
| TLYS | [TV](https://www.tradingview.com/chart/?symbol=TLYS) | $3.81 | -3.8% | +35.4% | $5.16 | +30.3% | 3.1M | 545K | 5.7x | 22.2M | Apparel/Footwear Retail |
| NYXH | [TV](https://www.tradingview.com/chart/?symbol=NYXH) | $1.51 | +1.3% | +33.1% | $2.01 | +34.9% | 1.5M | 284K | 5.2x | 81.3M | Medical Specialties |
| NCT | [TV](https://www.tradingview.com/chart/?symbol=NCT) | $4.90 | -6.1% | +8.6% | $5.32 | +1.9% | 758K | 2.4M | 0.3x | 8.5M | Marine Shipping |
| CHPT | [TV](https://www.tradingview.com/chart/?symbol=CHPT) | $5.19 | -2.1% | +17.7% | $6.11 | +15.3% | 660K | 479K | 1.4x | 22.7M | Electrical Products |
| GYGY | [TV](https://www.tradingview.com/chart/?symbol=GYGY) | $1.73 | +25.4% | +5.8% | $1.83 | +32.6% | 325K | 7.9M | 0.0x | 17K | Packaged Software |
| XTIA | [TV](https://www.tradingview.com/chart/?symbol=XTIA) | $0.95 | -17.4% | +6.3% | $1.01 | -12.2% | 131K | 950K | 0.1x | 38.4M | IT Services |
| BRNX | [TV](https://www.tradingview.com/chart/?symbol=BRNX) | $3.16 | -10.2% | +10.4% | $3.49 | -0.9% | 81K | 3.1M | 0.0x | 684K | Engineering & Construction |
| VIDA | [TV](https://www.tradingview.com/chart/?symbol=VIDA) | $2.56 | -0.4% | +6.6% | $2.73 | +6.2% | 55K | 98K | 0.6x | 5.4M | Packaged Software |

**Positions (Alpaca, entered earlier tonight):**
- TLYS 19 @ $5.15 → now $5.11 (-0.7%); AH +35.4%, VRatio 5.7x, holding/building.
- CHPT 16 @ $6.21 → now $6.11 (-1.6%); AH +17.7%, holding ~$6.1.
- UFG 147 @ $0.64 → now $0.68 (+5.6%); AH +17.4%, VRatio 5.8x, still holding its BUILD.

**ENTERED — GELS (Grade None, no catalyst found):**
- Gelteq Ltd (gel-based drug delivery, ASX/Nasdaq). Cleared the 2-AH-scan gate (23:30 +11.7% → 00:00 +37.2% → 00:30 +42.3% AH, all >10%). Skipped 3× earlier on "already ran regular session" — but that reasoning was weak: GELS is a fresh single-day mover (regular +31.6% then AH +42% same day), not a multi-session runner, and the AH leg is a real accelerating volume-backed BUILD, not the thin already-ran case (unlike BIAF).
- Day% +31.6% positive (no dead-cat concern), Total% +87.3% (under +150% ceiling), float n/a (recorded, not a gate).
- **Real, massive SIP accumulation.** Bars 16:55→17:35 ET: vol 757K→1.25M→510K→240K→1.03M→1.33M→712K→1.10M→1.07M sh/bar, 2094-4275 trades/bar, vwap $0.82→$1.00, new high $1.03 @17:30 ET. Late peak (after 17:00 ET), holding $0.99-1.02 within ~4% of high = hold/build, not fade.
- SPIKE 16:58ET +24% $0.87 757 trades / 302k sh (real co-spike ignition). CONFIRM-3 **NO** ignition 16:55ET failed third-bar hold/volume (instrumentation only, not a gate).
- tradable=true. Alpaca quote stale (`bid $0.58 ask $0.80 @16:00 ET` open minute, ask well below current SIP ~$1.00) — same stale-open-quote pattern as UFG; limit rested and filled against the real book.
- **No same-day catalyst found** (2 searches): latest Gelteq PR Jun 12 2026, nothing dated Sept 2. Grade None, entered with concern noted (learning-phase rule).
- **Fill: 95 @ $1.02** (limit $1.05 ext, id 40539152).
- **CHASE-CAP:** qualifying gate-clear scan 00:00 AH $0.96/+80.5%; fill $1.02/+91.7%. Chase gap +11.2% (fill Total% − qualifying Total%). Under the +120% fade zone.
- **MULTI-SESSION check:** fresh day-1 igniter (single-day regular+AH move, not in WINNERS_TRACKING).

**Skipped:**
- **UFG / TLYS / CHPT** — already entered (position management handled in premarket).
- **NYXH** — cleared gate but confirmed thin-drift: SIP shows one 320K-sh spike bar @16:35 ET (vwap $1.76), then per-bar volume collapsed to 3K-73K sh (hundreds of trades). Holding ~$1.74 is thin drift after an early spike, not a build. Float 81.3M. SPIKE 16:33 ET, CONFIRM-3 NO. Skip.
- **GELS's row is the only new qualifier;** the rest are carried skips:
- **NCT** — VRatio 0.3x, AH +8.6%, thin/not accumulating. Skip.
- **GYGY** — AH +5.8% (below 10% gate), Day% +25.4% already ran, VRatio 0.0x, float 17K. Skip.
- **XTIA** — Day% -17.4% below the -15% floor, Total% negative. Skip.
- **BRNX** — carried, VRatio 0.0x thin, no catalyst found. Skip.
- **VIDA** — new, AH +6.6% (below 10% gate), VRatio 0.6x thin. Skip.

No FINAL-SCAN-GATE-BLOCK this scan (no late igniter met every rule except the 2-AH-scan gate — GELS already had 3 AH appearances so the gate was satisfied).

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
| TLYS | $5.15 | 23:00 CET (5:00 PM ET) | 19 | 921abfa7 | Grade B earnings beat (comp +12.1%); BUILD 4 AH scans, VRatio 4.9x, CONFIRM-3 YES, cleared 2-AH-scan gate |
| CHPT | $6.21 | 23:00 CET (5:00 PM ET) | 16 | 46d8ab1e | Grade B Q2 earnings; holding ~$6.1 within 3% of AH high, cleared 2-AH-scan gate |
| UFG | $0.64 | 23:30 CET (5:30 PM ET) | 147 | 144bcf15 | Grade None (no catalyst); night's strongest BUILD, float 9.8M, VRatio 5.1x, CONFIRM-3 YES, cleared 2-AH-scan gate |
| GELS | $1.02 | 00:30 CET (6:30 PM ET) | 95 | 40539152 | Grade None (no catalyst); real accelerating BUILD (757K-1.33M sh/bar, vwap $0.82→$1.00), new high $1.03 @17:30 ET, cleared 2-AH-scan gate, float n/a |
