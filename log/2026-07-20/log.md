# Post-Market Screening - 2026-07-20

## Scan 21:30 CET (3:30 PM ET) — REGULAR session (pre-AH watch)

This scan ran before AH open (16:00 ET / 22:00 CET). No paper trades — regular-session movers flagged as **Watch — pending AH confirmation**. Only names that reappear in AH scans (22:00+ CET) with sustained momentum become entry candidates.

### Watch candidates (low float, big move, real intraday liquidity)

| Ticker | Chart | Price | Chg% | 5mVol | AvgVol5m | IRVol | Float | MCap | Industry | Note |
|--------|-------|-------|------|-------|----------|-------|-------|------|----------|------|
| ADVB | [TV](https://www.tradingview.com/chart/?symbol=ADVB) | $9.03 | +79.4% | 194 | 303K | 2502x | 561K | 14.9M | Biotechnology | Micro-float; late-session vol thin |
| GLVT | [TV](https://www.tradingview.com/chart/?symbol=GLVT) | $0.50 | +792.9% | 904 | 604 | 1.7x | 377K | 2.0M | Advertising/Marketing | Sub-$1, micro-float |
| SINC | [TV](https://www.tradingview.com/chart/?symbol=SINC) | $3.80 | +70.4% | 190 | 63 | 0.9x | 1.7M | 117.2M | Wholesale Distributors | Low float |
| CRNG | [TV](https://www.tradingview.com/chart/?symbol=CRNG) | $2.00 | +263.6% | 4K | 2K | 2.9x | n/a | 31.6M | REIT | Real 5m vol |
| NTRX | [TV](https://www.tradingview.com/chart/?symbol=NTRX) | $0.62 | +73.9% | 3K | 1K | 1.9x | 9.8M | 9.4M | Wholesale Distributors | Sub-$1 |
| ZYBT | [TV](https://www.tradingview.com/chart/?symbol=ZYBT) | $5.20 | +645.0% | 100 | 349K | 15250x | 7.7M | 20.7M | Biotechnology | Vol collapsed to 100 sh — likely halted/faded |
| NATM | [TV](https://www.tradingview.com/chart/?symbol=NATM) | $1.99 | +53.1% | 350 | 386 | 1.1x | 48.3M | 248.1M | Electrical Products | Higher float |

### Notes

- **Illiquid/stale signals:** Most top-% movers (ZYBT +645%, GLVT +793%, LXEIF +844%, SRRCF +3010%, ADVB +79%) show 5-min volume of only 100–900 shares late in the session — moves are early-session and not building into the close. These need AH confirmation before they mean anything.
- **Session context:** 57 hits but the field is dominated by thin sub-$1 names and packaged-software microcaps with negative IRVol (volume fading). No standout BUILD-into-close candidate.
- **Next step:** AH scans at 22:00 / 22:30 / 23:00+ CET decide entries. Per learning-phase rule, no entries before 23:00 CET regardless.

## Scan 22:00 CET (4:00 PM ET) — AH open, observation only

Scanner run at 16:00:16 ET (first minute of AH): **0 hits**. The postmarket feed has not populated yet at the open. No candidates with AH data.

Per learning-phase rule, no entries before 23:00 CET regardless. Watch names carried from the 21:30 regular-session scan (ADVB, GLVT, SINC, CRNG, NTRX, ZYBT, NATM) all showed thin/fading late-session volume — none confirmed in AH yet. Next scans at 22:30 / 23:00+ CET decide entries.

## Scan 22:15 CET (4:15 PM ET) — AH, observation only

Scanner run at 16:15:16 ET: **0 hits**. The postmarket feed still has not populated a screener field 15 min into AH.

SIP cross-check on tracked watch names (feed-lag rescue): only **ADVB** shows real AH volume — first AH bar (16:00-16:05 ET) 280K sh / 3221 trades, VWAP $8.74, but **fading** from the $9.03 close (bar closed $8.37, well below VWAP). CRNG, NTRX, SINC, NATM: no AH bars yet (no AH trades). No confirmation of any watch name building into AH.

Per learning-phase rule, no entries before 23:00 CET regardless. Next scans at 22:30 / 23:00+ CET decide entries.

## Scan 22:30 CET (4:30 PM ET) — AH, observation only

Scanner run at 16:30:16 ET: **4 hits**. AH feed now populated.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| HIHO | [TV](https://www.tradingview.com/chart/?symbol=HIHO) | $0.93 | +19.7% | +49.5% | $1.39 | +78.9% | 6.1M | 751K | 8.1x | 2.8M | Misc Manufacturing |
| GBR | [TV](https://www.tradingview.com/chart/?symbol=GBR) | $0.68 | +6.7% | +6.3% | $0.72 | +13.4% | 600K | 131K | 4.6x | 4.7M | Real Estate Dev |
| SHPH | [TV](https://www.tradingview.com/chart/?symbol=SHPH) | $3.03 | -4.1% | +24.4% | $3.77 | +19.3% | 553K | 7.8M | 0.1x | 596K | Pharmaceuticals |
| GORO | [TV](https://www.tradingview.com/chart/?symbol=GORO) | $1.00 | +7.8% | +218.8% | $3.18 | +243.6% | 13K | 8.1M | 0.0x | 160.0M | Precious Metals |

### Spike-bar instrumentation (log-only, AH >10%)

- `HIHO 2026-07-20 SPIKE 16:04ET +16% $1.08 373 trades / 190k sh (first co-spike bar) (as-of 16:30ET)`
- `SHPH 2026-07-20 SPIKE 16:04ET +22% $3.69 550 trades / 50k sh (first co-spike bar) (as-of 16:30ET)`
- `GORO 2026-07-20 NO-SPIKE flat/faded (peak <= base) (no bar cleared +15% on a volume co-spike) (as-of 16:30ET)`

### Evaluation

- **HIHO** — LEAD CANDIDATE. `tradable=true`. Real BUILD confirmed on SIP: bars 195K → 3.26M → 3.48M → 1.43M sh, thousands of trades/bar, VWAP climbing $1.02 → $1.37. Two-sided book (bid $1.47 x100 / ask $1.50 x100) — real fillable liquidity. Quote ~$1.48 (~+61% vs close), building. Float 2.8M, VRatio 8.1x, Total% +79% (well under +150% ceiling). **Catalyst = Grade B:** reported Q1 FY2027 earnings today (Mon Jul 20) — net sales ~$2.0M **+29.2% YoY**, gross profit +58.4% to $835K, margin +800bps to 42%, return to net-income growth (net-sales turnaround after a weak FY2026). Only gap: this is HIHO's first AH scan appearance — the 2-AH-scan gate is not yet met. **No entry now (22:30, observation-only + gate unmet). Prime entry candidate for 23:00 if it holds/builds.**
- **GBR** — AH +6.3%, below the 10% threshold. Not a candidate.
- **SHPH** — `tradable=false` (matches the recurring broker-block on this name). Qualified-but-untradable; no further workup. Carry as untradable on later scans.
- **GORO** — NO-SPIKE (flat/faded) + `tradable=false` + AH +218.8% on only 13K AH vol against a 160M float. Classic **bad print / illiquid ramp** — no real accumulation, cannot fill. Skip.

Per learning-phase rule, no entries before 23:00 CET. Next scan at 23:00 CET decides entries — HIHO leads pending its second AH confirmation.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
