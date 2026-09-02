
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

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
| TLYS | $5.15 | 23:00 CET (5:00 PM ET) | 19 | 921abfa7 | Grade B earnings beat (comp +12.1%); BUILD 4 AH scans, VRatio 4.9x, CONFIRM-3 YES, cleared 2-AH-scan gate |
| CHPT | $6.21 | 23:00 CET (5:00 PM ET) | 16 | 46d8ab1e | Grade B Q2 earnings; holding ~$6.1 within 3% of AH high, cleared 2-AH-scan gate |
