# Post-Market Screening - 2026-07-13

## Scan 21:30 CET (3:30 PM ET) — REGULAR session, pre-AH

Scanner ran during regular session (AH opens 4:00 PM ET / 22:00 CET). **No entries — regular-session caution rule.** Candidates flagged for AH confirmation; only enter if they reappear in a 22:00+ CET AH scan with sustained momentum.

Notable movers (regular-session, IRVol = intraday relative volume):

| Ticker | Price | Chg% | IRVol | Float | MCap | Industry | Note |
|--------|-------|------|-------|-------|------|----------|------|
| MIMI | $3.04 | +41.4% | 179x | 1.5M | 8.4M | Misc Commercial | Low float, high IRVol — watch AH |
| SOBR | $1.31 | +202.1% | high | 2.3M | 1.2M | Electronic Equip | Big % move, low float — watch AH |
| ACTU | $1.46 | +20.7% | 17x | 10.3M | 34.9M | Pharma Major | Watch AH |
| AURE | $1.68 | +13.5% | 95x | 10.9M | 65.0M | IT Services | Watch AH |
| EHGO | $2.24 | +36.6% | 3.7x | 2.2M | 7.2M | Wholesale Dist | Low float — watch AH |
| GEDC | $0.78 | +94.9% | 3.8x | 7.3M | 10.3M | Eng & Construction | Watch AH |
| SKYQ | $4.09 | +28.7% | 1.2x | 3.8M | 19.6M | Integrated Oil | Fading IRVol — watch AH |

Many other small % movers with negligible real volume (VChg% -99% type = stale). Full scan had 62 hits, mostly illiquid.

**Decision:** No paper trades. Regular-session scan only. Reassess at 22:00+ CET AH scans for entries.

## Scan 22:00 CET (4:00 PM ET) — AH open

Scanner (`scan.py --all`): **0 AH hits.** Observation-only scan (learning phase: no entries before 23:00 CET).

Early-AH quotes on the 21:30 watchlist (scan hit ~30s after AH open, books still forming):

| Ticker | Bid | Ask | Note |
|--------|-----|-----|------|
| MIMI | $2.51 x100 | $3.36 x100 | Wide spread, thin |
| SOBR | $0.61 x500 | $1.70 x1100 | Very wide spread, unstable |
| SKYQ | $3.43 x100 | $0.00 x0 | No AH ask (no fillable book) |
| EHGO | $1.82 x100 | $2.46 x100 | Wide spread, thin |

**Decision:** No paper trades. No scanner AH hits; watchlist books thin/unstable seconds into AH. Reassess at 22:30 / 23:00 CET.

## Scan 22:30 CET (4:30 PM ET) — AH observation

Scanner (`scan.py --all`): **3 AH hits.** Observation-only scan (learning phase: no entries before 23:00 CET).

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| JEM | [TV](https://www.tradingview.com/chart/?symbol=JEM) | $0.50 | -7.0% | +22.9% | $0.62 | +14.3% | 6.5M | 26.4M | 0.2x | 0 | Wholesale Distributors |
| SHPH | [TV](https://www.tradingview.com/chart/?symbol=SHPH) | $2.96 | +1.4% | +16.2% | $3.44 | +17.8% | 211K | 435K | 0.5x | 596K | Pharmaceuticals: Major |
| LVLU | [TV](https://www.tradingview.com/chart/?symbol=LVLU) | $8.32 | -3.7% | +27.2% | $10.58 | +22.5% | 123K | 25K | 5.0x | 1.2M | Internet Retail |

**SIP verification (bars from 20:00Z / 16:00 ET):**
- **JEM** — real high volume (1.7M→3.6M→1.6M→629K sh/bar, thousands of trades), VWAP ~$0.60 corroborates AH price. **SPIKE→FADE**: peaked 20:05 ($0.69), fading to $0.57. Catalyst: **1-for-12 reverse split effective Jul 14** (Grade D, compliance/dilution). Sub-penny, Day -7%. Skip-lean.
- **SHPH** — **BUILD** volume (2.7K→68K→194K→174K, accumulating), VWAP $3.43-3.51 corroborates. Float 596K (very low). Pharma. **No catalyst found** (latest news 07/07 insider trades; reverse-split microcap near lows). Note for 23:00.
- **LVLU** — real SIP volume, VWAP ~$10.9 corroborates AH $10.58. Float 1.2M (low). Peaked 20:05 ($11.90), mild fade to ~$11.10 but **holding within 20% of high**. Volume fading after first bar (116K→69K→59K). Catalyst: **strategic-alternatives review** announced ~16:06 ET (24 min before scan) — special committee to evaluate options to maximize stockholder value (**Grade B**, solid news, can precede acquisition). Total +22.5%, well under 150% ceiling. **Strongest candidate for 23:00 if it holds/builds.**

**Decision:** No paper trades (observation-only window). At 23:00 CET, re-evaluate: LVLU (Grade B, low float, holding) is the lead; SHPH (build, no catalyst) secondary; JEM (Grade D split, fading) skip-lean. Watch whether LVLU holds/builds vs continues fading, and whether it stays within 20% of its AH high.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
