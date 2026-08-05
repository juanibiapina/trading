# Post-Market Screening - 2026-08-05

## Scan 21:30 CET (3:30 PM ET)

Regular-session scan (before AH open at 16:00 ET). No entries — regular-session caution rule. Watch candidates flagged for AH confirmation at 22:00+ CET.

| Ticker | Chart | Price | Day% | Float | MCap | IRVol | Industry | Note |
|--------|-------|-------|------|-------|------|-------|----------|------|
| ZYBT | [TV](https://www.tradingview.com/chart/?symbol=ZYBT) | $2.72 | +112.5% | 7.7M | 38.0M | 57.1 | Biotechnology | Watch — pending AH confirmation |
| INLF | [TV](https://www.tradingview.com/chart/?symbol=INLF) | $6.38 | +100.6% | 1.0M | 3.3M | 6.8 | Industrial Machinery | Watch — low float |
| BJDX | [TV](https://www.tradingview.com/chart/?symbol=BJDX) | $1.41 | +40.5% | 936K | 1.5M | 299.3 | Medical Specialties | Watch — very low float |
| VRM | [TV](https://www.tradingview.com/chart/?symbol=VRM) | $9.71 | +38.0% | 5.1M | 50.8M | 20.8 | Specialty Stores | Watch |
| ASTC | [TV](https://www.tradingview.com/chart/?symbol=ASTC) | $9.23 | +27.5% | 1.7M | 18.5M | 67.4 | Aerospace & Defense | Watch — low float |
| FLZH | [TV](https://www.tradingview.com/chart/?symbol=FLZH) | $1.49 | +25.8% | 48.0M | 79.5M | 67.7 | Movies/Entertainment | Watch — float high |
| CSAI | [TV](https://www.tradingview.com/chart/?symbol=CSAI) | $5.00 | +26.9% | n/a | 4.2M | 3.0 | Packaged Software | Watch |
| ABTS | [TV](https://www.tradingview.com/chart/?symbol=ABTS) | $1.46 | +15.9% | 2.1M | 4.3M | 10.7 | Data Processing | Watch — low float |
| SHPH | [TV](https://www.tradingview.com/chart/?symbol=SHPH) | $4.37 | +19.6% | 596K | 2.8M | 2.6 | Pharma: Major | Watch — untradable on Alpaca (carried, tradable=false historically) |

23 total hits. Others (SUJA, NCO, TYGO, KLTR, CTXR, USDE, PPCB, CDTG, ZTG, ANPA, NEOV, SMRT, CTOR) either negative-day, high float, or no clear low-float momentum profile — tracked but not on the AH watchlist.

No paper trades this scan (regular session, entries only permitted at 23:00+ CET AH scans per learning-phase default).

## Scan 22:00 CET (4:00 PM ET)

Scanner ran one minute into AH open (16:00 ET) — `postmarket_volume` hasn't accumulated yet, so the screener returned **0 hits**. Observation-only scan (learning-phase default: no entries before 23:00 CET). Cross-checked the 21:30 regular-session watch names against live Alpaca AH books:

| Ticker | Prev Close | AH Book (16:00 ET) | Note |
|--------|-----------|--------------------|------|
| ZYBT | $2.72 | bid $2.01 / ask $2.67 x100 | Two-sided book, ask below close — early AH softness, watch |
| ASTC | $9.23 | bid $7.74 / ask $10.40 x100 | Two-sided book (wide spread) |
| INLF | $6.38 | bid $5.30 / ask $0.00 x0 | No AH ask (no fillable book) |
| BJDX | $1.41 | bid $1.22 / ask $0.00 x0 | No AH ask (no fillable book) |
| VRM | $9.71 | bid $9.19 / ask $0.00 x0 | No AH ask (no fillable book) |

No spike-bar / confirmation instrumentation run — scanner produced no AH candidates above threshold this early. Re-scan at 22:30 CET once real AH volume accumulates.

No paper trades this scan (observation-only, entries permitted at 23:00+ CET).

## Scan 22:15 CET (4:15 PM ET)

Scanner returned **0 hits** (early AH, `postmarket_volume` still thin). Observation-only scan (learning-phase default: no entries before 23:00 CET). Cross-checked the 21:30 watch names against live SIP bars + Alpaca AH books — all softening off their regular-session close, none building:

| Ticker | Prev Close | AH (16:15 ET) | Book | Note |
|--------|-----------|---------------|------|------|
| ZYBT | $2.72 | $2.11 (VWAP $2.20, 306K sh / 1932 tr) | bid $2.23 / ask $0.00 x0 | Fading off close, ask pulled |
| ASTC | $9.23 | $8.65 (VWAP $8.99, 21K sh / 136 tr) | bid $7.74 / ask $10.40 x100 | Softening, wide spread |
| INLF | $6.38 | — | bid $5.30 / ask $0.00 x0 | No fillable ask |
| BJDX | $1.41 | — | bid $1.25 / ask $1.27 x100 | Two-sided but faded below close |
| VRM | $9.71 | — | bid $9.19 / ask $0.00 x0 | No fillable ask |
| ABTS | $1.46 | — | bid $1.19 / ask $1.76 x100 | Faded below close |

No candidate is building in AH; all watch names are below their regular close. No spike-bar / confirmation instrumentation run (no name above threshold). Re-scan at 22:30 / 23:00 CET.

No paper trades this scan (observation-only, entries permitted at 23:00+ CET).

## Scan 22:30 CET (4:30 PM ET)

Scanner returned **2 AH hits** as real post-market volume accumulated. Observation-only scan (learning-phase default: no entries before 23:00 CET).

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| CELZ | [TV](https://www.tradingview.com/chart/?symbol=CELZ) | $0.67 | +1.9% | +36.1% | $0.91 | +38.6% | 11.0M | 1.4M | 8.1x | 4.7M | Medical Specialties |
| FRGT | [TV](https://www.tradingview.com/chart/?symbol=FRGT) | $3.42 | -1.4% | +31.6% | $4.50 | +29.7% | 180K | 48K | 3.7x | 563K | Financial Conglomerates |

**Instrumentation (log-only, no decision impact):**
- CELZ: `SPIKE 16:01ET +34% $0.90 1343 trades / 466k sh (first co-spike bar)` · `CONFIRM-3 NO no local-volume new-high ignition as-of 16:30ET`
- FRGT: `SPIKE 16:08ET +24% $4.23 135 trades / 8k sh (first co-spike bar)` · `CONFIRM-3 NO no local-volume new-high ignition as-of 16:30ET`

**CELZ** — real, liquid AH move. SIP bars accumulating hard: 20:00Z 3.45M sh / 10,537 tr, 20:05Z 4.86M sh / 16,553 tr (H $1.06), 20:10Z 3.47M sh / 11,819 tr, 20:15Z 2.06M sh / 6,458 tr. VWAP $0.89–0.96 corroborates the scanner AH price (no bad print). Book two-sided: bid $1.00 x100 / ask $1.03 x100. `tradable=true`. Float 4.7M (low). Clinical-stage biotech. Peaked ~$1.06 at 16:05 ET, now softening to $0.89 (16:15 close), trades-per-bar declining — early-peak, mild fade profile so far. **No catalyst found** (earnings Aug 10 post-market, latest PR January ADAPT data; nothing same-day). Track into 23:00 scan for build-vs-fade; qualifies on the 2-AH-scan gate only if it reappears >10% at 23:00+.

**FRGT** — SPIKE→FADE + illiquid. SIP: spiked 20:05–20:10Z to H $4.99 (2,793 tr peak bar) then collapsed 20:15Z to L $2.80 / C $2.99. Quote `bid $2.68 / ask $0.00 x0` — no fillable AH ask (book pulled). Very low float 563K but no real two-sided liquidity and already round-tripping off the spike. **No catalyst found** (earnings Aug 17). Skip: illiquid (no AH book) + SPIKE→FADE.

21:30 watch names (ZYBT, ASTC, INLF, BJDX, VRM, ABTS) remain below their regular-session close, none building — dropped from active AH watch. SHPH carried as untradable (`tradable=false` historically).

No paper trades this scan (observation-only, entries permitted at 23:00+ CET).

## Scan 22:45 CET (4:45 PM ET)

Scanner returned **6 AH hits**. Observation-only scan (learning-phase default: no entries before 23:00 CET).

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| CELZ | [TV](https://www.tradingview.com/chart/?symbol=CELZ) | $0.67 | +1.9% | +33.9% | $0.90 | +36.4% | 16.6M | 2.0M | 8.4x | 4.7M | Medical Specialties |
| PAVS | [TV](https://www.tradingview.com/chart/?symbol=PAVS) | $4.91 | +0.2% | +35.3% | $6.64 | +35.6% | 490K | 2.2M | 0.2x | 856K | Pharmaceuticals: Other |
| CNEY | [TV](https://www.tradingview.com/chart/?symbol=CNEY) | $0.64 | +3.8% | +10.1% | $0.70 | +14.3% | 127K | 227K | 0.6x | 7.6M | Electrical Products |
| LESL | [TV](https://www.tradingview.com/chart/?symbol=LESL) | $1.36 | +3.0% | +11.0% | $1.51 | +14.4% | 100K | 1.4M | 0.1x | 8.8M | Specialty Stores |
| FCHL | [TV](https://www.tradingview.com/chart/?symbol=FCHL) | $1.26 | +5.0% | +8.7% | $1.37 | +14.2% | 63K | 446K | 0.1x | 1.3M | Misc Commercial Services |
| OPRT | [TV](https://www.tradingview.com/chart/?symbol=OPRT) | $6.06 | +0.8% | +5.1% | $6.37 | +6.0% | 51K | 400K | 0.1x | 39.3M | Finance/Rental/Leasing |

**Instrumentation (log-only, no decision impact):**
- CELZ: `SPIKE 16:01ET +34% $0.90 1343 trades / 466k sh (first co-spike bar)` · `CONFIRM-3 NO no local-volume new-high ignition as-of 16:45ET`
- PAVS: `SPIKE 16:20ET +32% $6.48 385 trades / 28k sh (first co-spike bar)` · `CONFIRM-3 NO ignition 16:20ET failed third-bar hold/volume as-of 16:45ET`
- CNEY: `SPIKE 16:24ET +16% $0.74 174 trades / 54k sh (first co-spike bar)` · `CONFIRM-3 NO no local-volume new-high ignition as-of 16:45ET`
- LESL: `SPIKE 16:27ET +17% $1.59 57 trades / 19k sh (first co-spike bar)` · `CONFIRM-3 PENDING ignition 16:25ET; waiting for third bar as-of 16:45ET`

**CELZ** — lead candidate, real + liquid + BUILD/reclaim profile. Now in its **2nd AH scan >10%** (22:30 +36%, 22:45 +34%) → clears the 2-AH-scan gate. SIP bars sustained/rebuilding: 20:00Z 3.45M sh/10,537 tr (VWAP $0.90), 20:05Z peak H $1.06 (4.86M/16,553 tr), dip to L $0.86 at 20:20Z (−19% off high), then **rebuilt** 20:25Z→20:30Z C $0.98 (2.34M sh/7,625 tr) making a run at the high. Live quote 16:38 ET bid $1.00 / ask $1.02 x100 — fresh, two-sided, liquid (not stale). VWAP $0.88–0.96 corroborates scanner AH (no bad print). `tradable=true`. Float 4.7M (low). Day% +1.9% (not a dead-cat). Total% ~+49% at bid $1.00 — well under the 150% ceiling. **No catalyst found** (earnings Aug 10 post-market, latest PR January ADAPT data). No-catalyst = concern noted, not a skip. Holding within ~20% of AH high on real volume → BUILD pattern. **Qualifies for entry at the 23:00 CET scan** if it holds >10% AH.
- PAVS — VRatio 0.2x (AH vol 490K vs 2.2M avg = thin), spike 16:20ET already failed third-bar hold, quote stale bid $4.05/ask $5.70 wide. SPIKE→FADE + thin relative volume. Skip.
- CNEY / LESL / FCHL / OPRT — AH change ≤11%, VRatio <1x (below-average relative volume), thin trade counts. Below the momentum threshold. Skip.

21:30 watch names remain below their regular close; SHPH carried untradable (`tradable=false` historically).

No paper trades this scan (observation-only; CELZ flagged for entry at 23:00 CET pending a hold above threshold).

## Scan 23:00 CET (5:00 PM ET)

Scanner returned **8 AH hits**. Entry-eligible scan (learning-phase default: entries permitted at 23:00+ CET).

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| CELZ | [TV](https://www.tradingview.com/chart/?symbol=CELZ) | $0.67 | +1.9% | +30.9% | $0.88 | +33.4% | 23.8M | 2.7M | 8.7x | 4.7M | Medical Specialties |
| AZI | [TV](https://www.tradingview.com/chart/?symbol=AZI) | $1.01 | -9.8% | +14.9% | $1.16 | +3.6% | 1.6M | 272K | 6.0x | 4.4M | Specialty Stores |
| PAVS | [TV](https://www.tradingview.com/chart/?symbol=PAVS) | $4.91 | +0.2% | +21.2% | $5.95 | +21.4% | 799K | 2.2M | 0.4x | 856K | Pharmaceuticals: Other |
| RECT | [TV](https://www.tradingview.com/chart/?symbol=RECT) | $1.28 | +4.5% | +21.1% | $1.55 | +26.5% | 291K | 49K | 5.9x | 2.5M | Wholesale Distributors |
| LESL | [TV](https://www.tradingview.com/chart/?symbol=LESL) | $1.36 | +3.0% | +14.7% | $1.56 | +18.2% | 194K | 1.5M | 0.1x | 8.8M | Specialty Stores |
| CNEY | [TV](https://www.tradingview.com/chart/?symbol=CNEY) | $0.64 | +3.8% | +5.1% | $0.67 | +9.1% | 175K | 232K | 0.8x | 7.6M | Electrical Products |
| MYO | [TV](https://www.tradingview.com/chart/?symbol=MYO) | $1.06 | -1.9% | +10.4% | $1.17 | +8.3% | 93K | 287K | 0.3x | 35.2M | Medical Distributors |
| OPRT | [TV](https://www.tradingview.com/chart/?symbol=OPRT) | $6.06 | +0.8% | +6.3% | $6.44 | +7.2% | 55K | 401K | 0.1x | 39.3M | Finance/Rental/Leasing |

**Instrumentation (log-only, no decision impact):**
- CELZ: `SPIKE 16:01ET +34% $0.90 1343 trades / 466k sh (first co-spike bar)` · `CONFIRM-3 NO no local-volume new-high ignition as-of 17:00ET`
- PAVS: `SPIKE 16:20ET +32% $6.48 385 trades / 28k sh (first co-spike bar)` · `CONFIRM-3 NO ignition 16:20ET failed third-bar hold/volume as-of 17:00ET`
- LESL: `SPIKE 16:27ET +17% $1.59 57 trades / 19k sh (first co-spike bar)` · `CONFIRM-3 NO ignition 16:25ET failed third-bar hold/volume as-of 17:00ET`
- AZI: `SPIKE 16:30ET +24% $1.25 280 trades / 37k sh (first co-spike bar)` · `CONFIRM-3 NO ignition 16:30ET failed third-bar hold/volume as-of 17:00ET`
- RECT: `SPIKE 16:35ET +37% $1.75 372 trades / 41k sh (first co-spike bar)` · `CONFIRM-3 YES ignition 16:25ET 32.0x; confirmed 16:35ET $1.45 as-of 17:00ET`
- MYO: `SPIKE 16:43ET +23% $1.30 34 trades / 5k sh (first co-spike bar)` · `CONFIRM-3 PENDING ignition 16:40ET; waiting for third bar as-of 17:00ET`

**CELZ — ENTERED.** Clears every entry gate. Now on its **3rd AH scan >10%** (22:30 +36%, 22:45 +34%, 23:00 +31%) → 2-AH-scan gate met. SIP bars real + liquid + BUILD/hold: 20:00Z 3.45M sh/10,537 tr (VWAP $0.90), peak H $1.06 at 20:05Z (4.86M/16,553 tr), dip to L $0.83 at 20:15–20:20Z, then **rebuilt** to touch $1.06 again at 20:35Z (3.31M sh/10,145 tr, VWAP $1.00), C $0.90 at 20:45Z. Current price within ~15% of AH high $1.06 → holding, not faded. Live quote 16:38 ET bid $1.00 / ask $1.02 x100 — fresh, two-sided, liquid. VWAP $0.88–1.00 corroborates scanner AH (no bad print). `tradable=true`. Float 4.7M (low). Day% +1.9% (not a dead-cat). Total% ~+33% (well under the 150% ceiling). **No same-day catalyst found** (3 searches: latest PR is Jun 30 warrant-exercise dilution; earnings Aug 10 post-market; nothing today). No-catalyst = concern noted, not a skip (learning phase). BUILD-and-hold on real volume → entered. **BUY 98 CELZ @ limit $1.05 ext (id 520c6223) filled @ $0.89** (price improvement below ask). Catalyst Grade **None** — exit at first premarket opportunity.
- **PAVS** — 2nd AH scan >10% (22:45 +35%, 23:00 +21%) so it clears the 2-scan gate, but VRatio 0.4x (AH vol 799K vs 2.2M avg = below-average relative volume), spike 16:20ET already failed third-bar hold, quote stale/wide. SPIKE→FADE + thin relative volume. **Skip.**
- **LESL** — 2nd AH scan >10% (22:45 +11%, 23:00 +14.7%), but VRatio 0.1x (AH 194K vs 1.5M avg = far below average), CONFIRM-3 NO, spike failed. Thin, not a real momentum book. **Skip.**
- **AZI** — 1st AH scan (+14.9%), does not clear the 2-AH-scan gate yet. Day% -9.8%. VRatio 6.0x decent but spike failed third-bar hold. Watch for a 2nd AH appearance; no entry.
- **RECT** — 1st AH scan (+21.1%), does not clear the 2-AH-scan gate yet. Notable: CONFIRM-3 **YES** (ignition 16:25ET 32x, confirmed 16:35ET). VRatio 5.9x, float 2.5M low. Watch for a 2nd AH appearance at 23:30/00:00 — would qualify for entry then if it holds >10%.
- **CNEY / MYO / OPRT** — AH change ≤10.4%, VRatio <1x (below-average relative volume), thin trade counts. Below the momentum threshold. Skip.

21:30 watch names (ZYBT, ASTC, INLF, BJDX, VRM, ABTS) remain below their regular close; SHPH carried untradable (`tradable=false` historically).

## Scan 23:30 CET (5:30 PM ET)

Scanner returned **6 AH hits**. Entry-eligible scan.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| CELZ | [TV](https://www.tradingview.com/chart/?symbol=CELZ) | $0.67 | +1.9% | +33.4% | $0.89 | +35.9% | 27.2M | 3.1M | 8.7x | 4.7M | Medical Specialties |
| PAVS | [TV](https://www.tradingview.com/chart/?symbol=PAVS) | $4.91 | +0.2% | +39.1% | $6.83 | +39.4% | 2.0M | 2.4M | 0.8x | 856K | Pharmaceuticals: Other |
| AZI | [TV](https://www.tradingview.com/chart/?symbol=AZI) | $1.01 | -9.8% | +6.9% | $1.08 | -3.6% | 1.9M | 307K | 6.3x | 4.4M | Specialty Stores |
| LESL | [TV](https://www.tradingview.com/chart/?symbol=LESL) | $1.36 | +3.0% | +16.8% | $1.59 | +20.3% | 287K | 1.5M | 0.2x | 8.8M | Specialty Stores |
| MYO | [TV](https://www.tradingview.com/chart/?symbol=MYO) | $1.06 | -1.9% | +6.6% | $1.13 | +4.6% | 171K | 296K | 0.6x | 35.2M | Medical Distributors |
| OPRT | [TV](https://www.tradingview.com/chart/?symbol=OPRT) | $6.06 | +0.8% | +6.3% | $6.44 | +7.2% | 66K | 402K | 0.2x | 39.3M | Finance/Rental/Leasing |

**Instrumentation (log-only, no decision impact):**
- CELZ: `SPIKE 16:01ET +34% $0.90 1343 trades / 466k sh (first co-spike bar)` · `CONFIRM-3 NO no local-volume new-high ignition as-of 17:30ET`
- PAVS: `SPIKE 16:20ET +32% $6.48 385 trades / 28k sh (first co-spike bar)` · `CONFIRM-3 NO ignition 16:20ET failed third-bar hold/volume as-of 17:30ET`

**CELZ — held (already entered 23:00).** Still on AH >10% (+33.4%, 4th scan). Position now $0.92 vs $0.89 entry (+3.3%). Grade None — premarket exit handled by position-evaluation.

**PAVS — ENTERED.** Re-evaluated after prior scans skipped it on a thin VRatio reading. On its **3rd AH scan >10%** (22:45 +35.3%, 23:00 +21.2%, 23:30 +39.1%) → clears the 2-AH-scan gate. SIP bars are real + liquid, contradicting the scanner's lagging 0.8x VRatio: 20:20Z 366K sh/5779 tr (H $6.79), 20:25Z 370K sh/6791 tr (H $6.95), dip to $5.36 at 20:30Z, then **rebuilt to new AH high $7.55 at 20:45Z** (602K sh/9389 tr), holding $6.5–7.2 since; 21:15Z C $7.10 (159K sh/2470 tr). Total AH volume ~3.1M sh **exceeds** the 2.4M avg — the spike is genuinely liquid, not thin. VWAP $6.5–7.1 corroborates the scanner AH price (no bad print). Peaked 16:45 ET (after 16:30), holding within ~6% of AH high → BUILD-and-hold, not SPIKE→FADE. Float 856K (ultra-low). Day% +0.2% (not a dead-cat). Total% ~+45% (under the 150% ceiling). `tradable=true`. **Alpaca quote stuck stale at 16:00 ET** (bid $4.05/ask $5.70, 90 min behind the scan) — freshness guard applies: SIP is fresh (last bar 15 min behind) and liquid, so this is a feed artifact, not a "no book" / bad-print skip. **No same-day catalyst found** (4 searches: latest news is a Jun 15 non-binding LOI for Jabanero and a March registered direct offering; nothing today). No-catalyst = concern noted, not a skip (learning phase). **BUY 14 PAVS @ limit $7.30 ext (id 49c34e12) filled @ $6.61** (price improvement below the current level). Catalyst Grade **None** — exit at first premarket opportunity.
- **RECT** — dropped off the scanner this pulse. Cross-checked SIP (had CONFIRM-3 YES at 23:00): spiked to H $1.75 at 20:35ET then **faded to $1.24 by 21:00ET, below its $1.28 close**, volume died (597 sh last bar). The ignition confirmation did not hold. **Skip: faded below close, dead.**
- **AZI** — fell to +6.9% AH (below the 10% threshold), Day% -9.8%. Below threshold. Skip.
- **LESL** — 3rd AH scan >10% (+16.8%) but VRatio 0.2x (AH 287K vs 1.5M avg = far below average), CONFIRM-3 NO. Thin, not a real momentum book. Skip.
- **MYO / OPRT** — AH change <7%, VRatio <1x. Below threshold. Skip.

21:30 watch names (ZYBT, ASTC, INLF, BJDX, VRM, ABTS) remain below their regular close; SHPH carried untradable (`tradable=false` historically).

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
| CELZ | $0.89 | 2026-08-05 23:00 CET | 98 | 520c6223 | 3rd AH scan >10%, float 4.7M, real liquid SIP BUILD/hold, Total% +33% (under ceiling), Day% +1.9% (not dead-cat). Grade None (no catalyst). |
| PAVS | $6.61 | 2026-08-05 23:30 CET | 14 | 49c34e12 | 3rd AH scan >10%, float 856K, real liquid SIP BUILD/hold (rebuilt to new AH high $7.55 @16:45ET), Total% ~+45% (under ceiling), Day% +0.2% (not dead-cat). Grade None (no catalyst). |

## Position Evaluation — 10:30 CEST

No open positions in Alpaca. `OPEN_POSITIONS.md` agrees with the broker state.

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| — | — | — | — | — | — | — | — | No positions to evaluate |

**Actions taken:**
- No sells or stop updates.

## Position Evaluation — 14:30 CEST

No open positions in Alpaca. `OPEN_POSITIONS.md` agrees with the broker state.

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| — | — | — | — | — | — | — | — | No positions to evaluate |

**Actions taken:**
- No sells or stop updates.
