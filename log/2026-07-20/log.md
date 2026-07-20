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

## Scan 22:45 CET (4:45 PM ET) — AH, observation only

Scanner run at 16:45:20 ET: **5 hits**.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| HIHO | [TV](https://www.tradingview.com/chart/?symbol=HIHO) | $0.93 | +19.7% | +59.2% | $1.48 | +90.5% | 11.4M | 1.3M | 8.6x | 2.8M | Misc Manufacturing |
| SHPH | [TV](https://www.tradingview.com/chart/?symbol=SHPH) | $3.03 | -4.1% | +19.1% | $3.61 | +14.2% | 1.3M | 7.9M | 0.2x | 596K | Pharmaceuticals |
| GBR | [TV](https://www.tradingview.com/chart/?symbol=GBR) | $0.68 | +6.7% | +7.4% | $0.73 | +14.6% | 665K | 139K | 4.8x | 4.7M | Real Estate Dev |
| SLGB | [TV](https://www.tradingview.com/chart/?symbol=SLGB) | $0.51 | -7.3% | +9.6% | $0.56 | +1.6% | 53K | 131K | 0.4x | 3.0M | Air Freight/Couriers |
| GORO | [TV](https://www.tradingview.com/chart/?symbol=GORO) | $1.00 | +7.8% | +228.8% | $3.28 | +254.4% | 14K | 8.1M | 0.0x | 160.0M | Precious Metals |

### Spike-bar instrumentation (log-only, AH >10%)

- `HIHO 2026-07-20 SPIKE 16:04ET +16% $1.08 373 trades / 190k sh (first co-spike bar) (as-of 16:45ET)`
- `SHPH 2026-07-20 SPIKE 16:04ET +22% $3.69 550 trades / 50k sh (first co-spike bar) (as-of 16:45ET)`
- `GORO 2026-07-20 NO-SPIKE flat/faded (peak <= base) (no bar cleared +15% on a volume co-spike) (as-of 16:45ET)`

### Evaluation

- **HIHO** — LEAD CANDIDATE, gate now met. **2nd AH scan appearance** (22:30 +49.5%, 22:45 +59.2%) — clears the 2-AH-scan >10% gate. Still **BUILDING**, not fading: SIP bars 195K → 3.26M → 3.48M → 1.43M → 2.98M → 1.44M → 2.14M sh, thousands of trades/bar, VWAP climbing $1.02 → $1.52, latest 16:30 bar closed $1.56 (new AH high). Real two-sided book: bid $1.50 x300 / ask $1.52 x300 — fillable. `tradable=true`. Float 2.8M (<10M ideal), VRatio 8.6x, Total% +90.5% (under +150% ceiling), Day% +19.7% (well above -15%). Making new AH highs late (16:30 ET) — trajectory is BUILD/hold, not SPIKE→FADE. **Catalyst Grade B:** Q1 FY2027 earnings today — net sales +29.2% YoY, gross profit +58.4%, margin +800bps, return to net-income growth. **No entry now (22:45, observation-only before 23:00 CET). Prime entry at 23:00 if it holds/builds.**
- **SHPH** — untradable (carried, `tradable=false`). AH +19.1% but no fillable book historically. No further workup. Qualified-but-untradable broker-block.
- **GBR** — AH +7.4%, below 10% threshold. Not a candidate.
- **SLGB** — new name, AH +9.6% below threshold, Total% +1.6%, VRatio 0.4x (vol fading), Day% -7.3%. Not a candidate.
- **GORO** — carried skip: NO-SPIKE, `tradable=false`, AH +228.8% on only 14K AH vol vs 160M float = bad print / illiquid ramp. Cannot fill.

Per learning-phase rule, no entries before 23:00 CET. Next scan at 23:00 CET decides entries — **HIHO leads, gate met, pending it holds the build.**

## Scan 23:00 CET (5:00 PM ET) — AH, ENTRY-ELIGIBLE

Scanner run at 17:00:15 ET: **4 hits**.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| HIHO | [TV](https://www.tradingview.com/chart/?symbol=HIHO) | $0.93 | +19.7% | +67.8% | $1.56 | +100.8% | 17.2M | 2.0M | 8.7x | 2.8M | Misc Manufacturing |
| SHPH | [TV](https://www.tradingview.com/chart/?symbol=SHPH) | $3.03 | -4.1% | +18.5% | $3.59 | +13.6% | 1.5M | 7.9M | 0.2x | 596K | Pharmaceuticals |
| HXHX | [TV](https://www.tradingview.com/chart/?symbol=HXHX) | $0.53 | -7.1% | +11.4% | $0.59 | +3.5% | 68K | 48K | 1.4x | 4.0M | Trucking |
| GORO | [TV](https://www.tradingview.com/chart/?symbol=GORO) | $1.00 | +7.8% | +240.9% | $3.40 | +267.4% | 17K | 8.1M | 0.0x | 160.0M | Precious Metals |

### Spike-bar instrumentation (log-only, AH >10%)

- `HIHO 2026-07-20 SPIKE 16:04ET +16% $1.08 373 trades / 190k sh (first co-spike bar) (as-of 17:00ET)`
- `SHPH 2026-07-20 SPIKE 16:04ET +22% $3.69 550 trades / 50k sh (first co-spike bar) (as-of 17:00ET)`
- `GORO 2026-07-20 NO-SPIKE flat/faded (peak <= base) (no bar cleared +15% on a volume co-spike) (as-of 17:00ET)`

### Evaluation

- **HIHO — ENTERED.** Clears every gate. Gate met (3rd AH scan: 22:30 +49.5%, 22:45 +59.2%, 23:00 +67.8% — rising each scan). Float 2.8M (<10M ideal), VRatio 8.7x, Total% +100.8% (under +150% ceiling), Day% +19.7% (well above -15%). `tradable=true`. Real SIP accumulation, not a print: bars 195K → 3.26M → 3.48M → 1.43M → 2.98M → 1.44M → 2.14M → 2.59M → 1.64M → 1.48M sh, thousands of trades/bar, VWAP climbing $1.02 → $1.61, AH high $1.69 at 16:35 ET. Trajectory is BUILD/hold making new highs late (16:35), not SPIKE→FADE; current ~$1.52 within 20% of the $1.69 high. Two-sided fillable book (bid $1.28 x1300 / ask $1.69 x200). **Catalyst Grade B:** Q1 FY2027 earnings today (Mon Jul 20) — net sales ~$2.0M **+29.2% YoY**, gross profit +58.4% to $835K, margin +800bps to 42%, return to net-income growth. **Entered:** BUY 59 @ limit $1.72 ext (id ddf2e698), **filled @ $1.50** (below ask, better fill). ~$88.50 deployed.
- **SHPH** — untradable (carried, `tradable=false`). AH +18.5% but no fillable book; qualified-but-untradable broker-block. No further workup (carried from 22:30/22:45). Morning-eval tally: qualified-but-untradable.
- **HXHX** — new name, AH +11.4% but **1st AH scan appearance** (2-AH-scan gate unmet), Total% +3.5%, VRatio 1.4x. Not an entry this scan; would need a second AH confirmation. `tradable=true`. Watch only.
- **GORO** — carried skip: NO-SPIKE, `tradable=false`, AH +240.9% on only 17K AH vol vs 160M float = bad print / illiquid ramp. Cannot fill.

**Entry taken:** HIHO (Grade B, BUILD, float 2.8M, filled $1.50). This is the last entry-eligible scan of the night per schedule; final feed-lag cross-check on tracked names (SHPH untradable, GORO bad-print, HXHX gate-unmet, GBR/SLGB sub-threshold) surfaced no additional rescue candidate.

## Scan 23:30 CET (5:30 PM ET) — AH, ENTRY-ELIGIBLE

Scanner run at 17:30:10 ET: **7 hits**.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| HIHO | [TV](https://www.tradingview.com/chart/?symbol=HIHO) | $0.93 | +19.7% | +43.1% | $1.33 | +71.2% | 22.1M | 2.5M | 8.9x | 2.8M | Misc Manufacturing |
| SHPH | [TV](https://www.tradingview.com/chart/?symbol=SHPH) | $3.03 | -4.1% | +20.8% | $3.66 | +15.8% | 1.8M | 7.9M | 0.2x | 596K | Pharmaceuticals |
| VCIG | [TV](https://www.tradingview.com/chart/?symbol=VCIG) | $0.61 | -33.5% | +5.7% | $0.65 | -29.7% | 741K | 4.5M | 0.2x | 5.5M | Misc Commercial Svcs |
| LASE | [TV](https://www.tradingview.com/chart/?symbol=LASE) | $1.09 | +17.8% | +5.5% | $1.15 | +24.3% | 408K | 2.8M | 0.1x | 32.6M | Electronic Equipment |
| PAPL | [TV](https://www.tradingview.com/chart/?symbol=PAPL) | $0.88 | -3.6% | +15.1% | $1.01 | +11.0% | 291K | 71K | 4.1x | n/a | Finance/Rental/Leasing |
| CPHI | [TV](https://www.tradingview.com/chart/?symbol=CPHI) | $0.91 | -17.3% | +7.7% | $0.98 | -10.9% | 84K | 13.0M | 0.0x | 37.8M | Pharmaceuticals |
| GORO | [TV](https://www.tradingview.com/chart/?symbol=GORO) | $1.00 | +7.8% | +221.8% | $3.21 | +246.9% | 33K | 8.1M | 0.0x | 160.0M | Precious Metals |

### Spike-bar instrumentation (log-only, AH >10%)

- `HIHO 2026-07-20 SPIKE 16:04ET +16% $1.08 373 trades / 190k sh (first co-spike bar) (as-of 17:30ET)`
- `SHPH 2026-07-20 SPIKE 16:04ET +22% $3.69 550 trades / 50k sh (first co-spike bar) (as-of 17:30ET)`
- `PAPL 2026-07-20 SPIKE 17:09ET +20% $1.06 244 trades / 61k sh (first co-spike bar) (as-of 17:30ET)`
- `GORO 2026-07-20 NO-SPIKE flat/faded (peak <= base) (no bar cleared +15% on a volume co-spike) (as-of 17:30ET)`

### Evaluation

- **HIHO** — already ENTERED at 23:00 ($1.50, 59 sh, id ddf2e698). No re-entry (one entry per candidate per night). Trajectory note: AH now +43.1% ($1.33) vs +67.8% ($1.56) at 23:00 — **fading off the 16:35 ET AH high ($1.69)**. Book bid $1.28 x1300 / ask $1.69 x200 (quote stale ~17:00 ET). Position held; premarket exit handled by position-evaluation. AH volume still accumulating (22.1M total AH vol, VRatio 8.9x).
- **PAPL** — NEW name, **1st AH scan appearance** — the 2-AH-scan >10% gate is unmet, so **no entry this scan** regardless. `tradable=true`. SPIKE fired late (17:09 ET) with real SIP accumulation: bars 5.5K → 121K → 192K → 68K sh, 434/988/323 trades — genuine, building. **Catalyst = earnings:** Pineapple Financial (mortgage brokerage/tech, Canada) reported Q3 FY2026 results today (Mon Jul 20, pre-scheduled) — the AH driver. Grade B pending the actual beat/miss detail (consensus was a loss of ~$0.41 EPS). Float n/a (very small; MCap ~$23M). Quote showed `ask $0.00 x0` but the timestamp was stale (16:00 ET) while SIP shows a live book — not a bad-print reject, staleness artifact. **Watch — needs a 2nd AH confirmation at 00:00/00:30 to become entry-eligible.**
- **SHPH** — untradable (carried, `tradable=false`). AH +20.8% but no fillable book. Qualified-but-untradable broker-block. No further workup.
- **VCIG** — AH +5.7% below threshold; Day% -33.5% (dead-cat territory), Total% -29.7% still deep below close. Not a candidate.
- **LASE** — AH +5.5% below threshold. Not a candidate.
- **CPHI** — AH +7.7% below threshold; Day% -17.3%. Not a candidate.
- **GORO** — carried skip: NO-SPIKE, `tradable=false`, AH +221.8% on only 33K AH vol vs 160M float = bad print / illiquid ramp. Cannot fill.

**No new entry this scan.** HIHO position stands (entered 23:00). PAPL is the only fresh AH >10% mover but is gate-unmet (1st AH scan) — carry to 00:00/00:30 for a possible 2nd confirmation. Next scans at 00:00 / 00:30 CET.

## Scan 00:00 CET (6:00 PM ET) — AH, ENTRY-ELIGIBLE

Scanner run at 18:00:13 ET: **6 hits**.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| HIHO | [TV](https://www.tradingview.com/chart/?symbol=HIHO) | $0.93 | +19.7% | +37.7% | $1.28 | +64.8% | 23.8M | 2.7M | 8.9x | 2.8M | Misc Manufacturing |
| PAPL | [TV](https://www.tradingview.com/chart/?symbol=PAPL) | $0.88 | -3.6% | +39.0% | $1.22 | +34.1% | 3.8M | 471K | 8.2x | n/a | Finance/Rental/Leasing |
| ADVB | [TV](https://www.tradingview.com/chart/?symbol=ADVB) | $8.90 | +76.9% | +38.8% | $12.35 | +145.5% | 2.2M | 5.1M | 0.4x | 561K | Biotechnology |
| SHPH | [TV](https://www.tradingview.com/chart/?symbol=SHPH) | $3.03 | -4.1% | +23.8% | $3.75 | +18.7% | 2.0M | 8.0M | 0.2x | 596K | Pharmaceuticals |
| VCIG | [TV](https://www.tradingview.com/chart/?symbol=VCIG) | $0.61 | -33.5% | +7.0% | $0.65 | -28.8% | 841K | 4.5M | 0.2x | 5.5M | Misc Commercial Svcs |
| GORO | [TV](https://www.tradingview.com/chart/?symbol=GORO) | $1.00 | +7.8% | +212.8% | $3.12 | +237.2% | 39K | 8.1M | 0.0x | 160.0M | Precious Metals |

### Spike-bar instrumentation (log-only, AH >10%)

- `HIHO 2026-07-20 SPIKE 16:04ET +16% $1.08 373 trades / 190k sh (first co-spike bar) (as-of 18:00ET)`
- `PAPL 2026-07-20 SPIKE 17:09ET +20% $1.06 244 trades / 61k sh (first co-spike bar) (as-of 18:00ET)`
- `ADVB 2026-07-20 SPIKE 17:32ET +17% $10.40 2030 trades / 136k sh (first co-spike bar) (as-of 18:00ET)`
- `SHPH 2026-07-20 SPIKE 16:04ET +22% $3.69 550 trades / 50k sh (first co-spike bar) (as-of 18:00ET)`
- `GORO 2026-07-20 NO-SPIKE peak +6% @17:02ET (no bar cleared +15% on a volume co-spike) (as-of 18:00ET)`

### Evaluation

- **PAPL — ENTERED.** Gate now met: **2nd AH scan appearance** (23:30 +15.1%, 00:00 +39.0%) — clears the 2-AH-scan >10% gate. `tradable=true`, Day% -3.6% (well above -15%), Total% +34.1% (far under +150% ceiling), VRatio 8.2x. Real SIP accumulation, not a print: AH built after 17:20 ET — bars 121K → 192K → 68K → 818K → 964K → 787K → 678K → 683K → 675K sh, thousands of trades/bar, VWAP $0.98 → $1.27, AH high ~$1.33 at 17:35 ET (peaked *after* 17:30 — BUILD, not early-fade). Current ~$1.10-1.22 within 20% of high. **Quote was frozen/stale** (`ask $0.00 x0` @ 16:00 ET, not updating across 3 pulls) — per freshness guard this is a staleness artifact, not an empty book (SIP shows 2475 trades in the 17:45 ET bar = live fillable market). Confirmed by the fill. **Catalyst = Grade B:** Pineapple Financial (mortgage brokerage/tech, Canada) reported Q3 FY2026 earnings today (Mon Jul 20) — the AH driver; market reacted +39%. **Entered:** BUY 80 @ limit $1.28 ext (id 4e6d2779), **filled @ $1.10** (well below limit, real market fill). ~$88 deployed.
- **HIHO** — already ENTERED at 23:00 ($1.50, 59 sh). No re-entry. Trajectory note: AH now +37.7% ($1.28) vs peak +67.8% ($1.56) at 23:00 — **fading further off the 16:35 ET AH high ($1.69)**; position now -15.3% (~$1.27). AH volume still accumulating (23.8M total). Premarket exit handled by position-evaluation.
- **ADVB** — strong BUILD but **1st AH scan appearance** (the 21:30 CET showing was regular session, which does not count toward the 2-AH-scan gate) → **gate UNMET, no entry this scan.** `tradable=true`. Real SIP surge: bars climbing $8.99 → $10.77 → $11.40 at 17:30-17:35 ET (409K/527K sh, 6787/9143 trades) — genuine accumulation making new highs late. Micro-float 561K, Day% +76.9%. **Concern:** Total% +145.5% is near the +150% extension ceiling — if it keeps building it may exceed it. **Watch — needs a 2nd AH confirmation at 00:30 to become entry-eligible; watch the ceiling.**
- **SHPH** — untradable (carried, `tradable=false`). AH +23.8% but no fillable book. Qualified-but-untradable broker-block. No further workup.
- **VCIG** — AH +7.0% below threshold; Day% -33.5% (dead-cat territory), Total% -28.8% still deep below close. Not a candidate.
- **GORO** — carried skip: NO-SPIKE (peak +6%), `tradable=false`, AH +212.8% on only 39K AH vol vs 160M float = bad print / illiquid ramp. Cannot fill.

**Entry taken:** PAPL (Grade B, BUILD, filled $1.10). ADVB is the strongest fresh mover but gate-unmet (1st AH scan) — carry to the 00:30 final scan for a possible 2nd confirmation (mind the +150% ceiling). HIHO position stands (entered 23:00), now fading.

## Scan 00:30 CET (6:30 PM ET) — AH, ENTRY-ELIGIBLE (final scheduled scan)

Scanner run at 18:30:14 ET: **10 hits**.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| HIHO | [TV](https://www.tradingview.com/chart/?symbol=HIHO) | $0.93 | +19.7% | +50.6% | $1.40 | +80.2% | 25.1M | 2.8M | 8.9x | 2.8M | Misc Manufacturing |
| PAPL | [TV](https://www.tradingview.com/chart/?symbol=PAPL) | $0.88 | -3.6% | +12.1% | $0.98 | +8.1% | 5.4M | 640K | 8.5x | n/a | Finance/Rental/Leasing |
| ADVB | [TV](https://www.tradingview.com/chart/?symbol=ADVB) | $8.90 | +76.9% | +27.2% | $11.32 | +125.0% | 3.7M | 5.3M | 0.7x | 561K | Biotechnology |
| RDGT | [TV](https://www.tradingview.com/chart/?symbol=RDGT) | $1.58 | +12.1% | +24.7% | $1.97 | +39.7% | 2.7M | 1.1M | 2.5x | 884K | Medical Distributors |
| SHPH | [TV](https://www.tradingview.com/chart/?symbol=SHPH) | $3.03 | -4.1% | +21.5% | $3.68 | +16.5% | 2.0M | 8.0M | 0.3x | 596K | Pharmaceuticals |
| SLGB | [TV](https://www.tradingview.com/chart/?symbol=SLGB) | $0.51 | -7.3% | +8.0% | $0.55 | +0.1% | 570K | 186K | 3.1x | 3.0M | Air Freight/Couriers |
| IVVD | [TV](https://www.tradingview.com/chart/?symbol=IVVD) | $0.69 | -7.7% | +6.3% | $0.73 | -1.8% | 131K | 3.5M | 0.0x | 262.9M | Biotechnology |
| CPHI | [TV](https://www.tradingview.com/chart/?symbol=CPHI) | $0.91 | -17.3% | +6.6% | $0.97 | -11.8% | 117K | 13.0M | 0.0x | 37.8M | Pharmaceuticals |
| CJMB | [TV](https://www.tradingview.com/chart/?symbol=CJMB) | $1.21 | -0.8% | +7.4% | $1.30 | +6.6% | 103K | 6.6M | 0.0x | n/a | Air Freight/Couriers |
| GORO | [TV](https://www.tradingview.com/chart/?symbol=GORO) | $1.00 | +7.8% | +216.8% | $3.16 | +241.5% | 40K | 8.1M | 0.0x | 160.0M | Precious Metals |

### Spike-bar instrumentation (log-only, AH >10%)

- `HIHO 2026-07-20 SPIKE 16:04ET +16% $1.08 373 trades / 190k sh (first co-spike bar) (as-of 18:30ET)`
- `PAPL 2026-07-20 SPIKE 17:09ET +20% $1.06 244 trades / 61k sh (first co-spike bar) (as-of 18:30ET)`
- `ADVB 2026-07-20 SPIKE 17:32ET +17% $10.40 2030 trades / 136k sh (first co-spike bar) (as-of 18:30ET)`
- `RDGT 2026-07-20 SPIKE 18:00ET +17% $1.85 857 trades / 151k sh (first co-spike bar) (as-of 18:30ET)`
- `GORO 2026-07-20 NO-SPIKE peak +6% @17:02ET (no bar cleared +15% on a volume co-spike) (as-of 18:30ET)`

### Final-scan feed-lag cross-check (SIP truth on tracked names)

The TradingView postmarket feed **under-reported ADVB** at this final scan: it showed ADVB flat/stale at $11.32 (+27.2%), but fresh SIP bars run to 18:15 ET showing a **new AH high $13.01** (387K sh / 6105 trades) and Yahoo `--ah-history` confirms $12.91 at 18:30 ET. SIP is truth: ADVB is a live, volume-backed BUILD making new highs late, not the fading $11.32 the scanner printed. Real level ~$12.9-13.05.

### Evaluation

- **ADVB — feed-lag-rescued BUILD, but SKIP on extension ceiling.** Gate now met (2nd AH scan: 00:00 +38.8%, 00:30 rescued to real ~+156%). `tradable=true`, micro-float 561K, Day% +76.9%, genuine SIP accumulation (bars to $13.01 @18:15 ET, 6-17k trades/bar, hundreds-of-K sh). Trajectory is BUILD/hold making new AH highs after 17:00 ET (high $13.05 @18:15 ET, holding $12.91 @18:30 ET, within 20%). **Catalyst = terminated its equity purchase (equity-line) agreement** today — removes a dilution overhang, roughly Grade B/C, up ~50% intraday on it. **BUT the true entry level is ~$12.91-13.05 = +156-158% from the $5.03 base (SIP truth), over the +150% extension ceiling.** The TradingView-printed +125% was stale/understated; the real move is over-ceiling. Extended entries leave no margin for overnight fade (data: ANY +155%→-21%, ATPC +154%→-14%). **Skip the live entry on the ceiling.** **CEILING-OVERRIDE WATCH (data collection):** made AH high after 17:00 ET ✓, holding within 20% across ≥2 AH scans ✓; VRatio fails the >5x condition (scanner 0.7x) but that is an artifact of ADVB's huge 5.3M avg daily volume — real AH accumulation is 3.7M+ sh with tens of thousands of trades. Two of three strict conditions met; recording a **hypothetical entry ~$12.91 at 00:30 CET** (VRatio-metric caveat noted) to collect the BUILD-vs-extension case.
- **RDGT** — NEW name, **1st AH scan appearance at the final scan** → 2-AH-scan gate can never be met tonight. `tradable=true`, micro-float 884K, SPIKE fired late (18:00 ET, 151k sh / 857 trades — real), AH high $2.07, Total% +39.7%. Genuine late build but no second confirmation possible. **No entry (gate unmet).** Morning-eval watch name.
- **HIHO** — already ENTERED at 23:00 ($1.50, 59 sh). No re-entry. Position now **$1.36, -9.3%**. AH still accumulating (25.1M total AH vol, VRatio 8.9x) but faded off the 16:35 ET high ($1.69). Premarket exit handled by position-evaluation.
- **PAPL** — already ENTERED at 00:00 ($1.10, 80 sh). No re-entry. Position **$1.09, -0.9%** (roughly flat). AH +12.1%, still above threshold, VRatio 8.5x. Premarket exit handled by position-evaluation.
- **SHPH** — untradable (carried, `tradable=false`). AH +21.5% but no fillable book. Qualified-but-untradable broker-block. No further workup.
- **GORO** — carried skip: NO-SPIKE (peak +6%), `tradable=false`, AH +216.8% on only 40K AH vol vs 160M float = bad print / illiquid ramp. Cannot fill.
- **SLGB / IVVD / CPHI / CJMB** — all AH <10% (below threshold). Not candidates. CPHI/IVVD also Day%-negative with 0.0x VRatio (vol fading).

**No new entry this final scan.** Both positions stand (HIHO, PAPL). ADVB was rescued from the feed-lag as a genuine live BUILD but skipped on the +150% extension ceiling (real level +156-158%); logged as CEILING-OVERRIDE WATCH with a hypothetical entry for data collection. RDGT is a real late micro-float mover but 1st-AH-appearance at the final scan (gate can't be met). Night complete.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
| HIHO | $1.50 | 2026-07-20 23:01 CET | 59 | ddf2e698 | Grade B (Q1 FY2027 earnings +29.2% YoY sales). Low-float 2.8M AH BUILD, 3rd AH scan, real SIP accumulation, Total% +100.8% under ceiling. |
| PAPL | $1.10 | 2026-07-21 00:01 CET | 80 | 4e6d2779 | Grade B (Pineapple Financial Q3 FY2026 earnings). AH BUILD, 2nd AH scan (+15.1%→+39.0%), real SIP accumulation, Total% +34.1% under ceiling, peaked 17:35 ET. |
