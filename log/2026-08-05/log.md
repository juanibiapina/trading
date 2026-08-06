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

## Scan 00:00 CET (6:00 PM ET)

Scanner returned **9 AH hits**. Entry-eligible scan.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| CELZ | [TV](https://www.tradingview.com/chart/?symbol=CELZ) | $0.67 | +1.9% | +37.6% | $0.92 | +40.2% | 33.4M | 3.8M | 8.8x | 4.7M | Medical Specialties |
| PAVS | [TV](https://www.tradingview.com/chart/?symbol=PAVS) | $4.91 | +0.2% | +24.4% | $6.11 | +24.7% | 2.3M | 2.5M | 1.0x | 856K | Pharmaceuticals: Other |
| CLRO | [TV](https://www.tradingview.com/chart/?symbol=CLRO) | $3.68 | -8.7% | +56.5% | $5.76 | +42.9% | 1.1M | 189K | 5.8x | 740K | Electronics/Appliances |
| AZI | [TV](https://www.tradingview.com/chart/?symbol=AZI) | $1.01 | -9.8% | +7.9% | $1.09 | -2.7% | 2.0M | 317K | 6.4x | 4.4M | Specialty Stores |
| BJDX | [TV](https://www.tradingview.com/chart/?symbol=BJDX) | $1.24 | +24.0% | +5.7% | $1.31 | +31.0% | 1.3M | 11.6M | 0.1x | 936K | Medical Specialties |
| HYFM | [TV](https://www.tradingview.com/chart/?symbol=HYFM) | $1.62 | -15.6% | +14.8% | $1.86 | -3.1% | 794K | 15.8M | 0.1x | 4.1M | Trucks/Construction/Farm Machinery |
| VMAR | [TV](https://www.tradingview.com/chart/?symbol=VMAR) | $0.66 | +1.4% | +7.5% | $0.71 | +9.0% | 932K | 5.4M | 0.2x | 6.4M | Recreational Products |
| LESL | [TV](https://www.tradingview.com/chart/?symbol=LESL) | $1.36 | +3.0% | +10.3% | $1.50 | +13.6% | 320K | 1.5M | 0.2x | 8.8M | Specialty Stores |
| FGL | [TV](https://www.tradingview.com/chart/?symbol=FGL) | $0.83 | -3.2% | +10.5% | $0.92 | +7.0% | 135K | 1.1M | 0.1x | 854K | Engineering & Construction |

**Instrumentation (log-only, no decision impact):**
- CELZ: `SPIKE 16:01ET +34% $0.90 1343 trades / 466k sh (first co-spike bar)` · `CONFIRM-3 NO no local-volume new-high ignition as-of 18:00ET`
- PAVS: `SPIKE 16:20ET +32% $6.48 385 trades / 28k sh (first co-spike bar)` · `CONFIRM-3 NO ignition 16:20ET failed third-bar hold/volume as-of 18:00ET`
- CLRO: `SPIKE 17:28ET +23% $4.51 313 trades / 37k sh (first co-spike bar)` · `CONFIRM-3 YES ignition 17:25ET 867.1x; confirmed 17:35ET $5.30 as-of 18:00ET`

**CELZ — held (already entered 23:00).** Still on AH >10% (+37.6%, 5th scan). Position $0.93 vs $0.89 entry (+5.0%). Grade None — premarket exit handled by position-evaluation.

**PAVS — held (already entered 23:30).** Still on AH >10% (+24.4%, 4th scan). Position $6.61 vs $6.61 entry (flat). Grade None — premarket exit handled by position-evaluation.

**CLRO — WATCH (1st AH scan, does not clear the 2-AH-scan gate).** Fresh late-igniting BUILD. SIP bars confirm real + liquid accumulation building into new highs: move started ~21:25Z (17:25 ET) 110K sh/989 tr H$5.50, 21:30Z 443K sh/6114 tr, 21:35Z 436K sh/6185 tr, 21:40Z 578K sh/9716 tr H$6.00, 21:45Z 457K sh/7431 tr C$5.85 H$6.15 — accumulating hard, making new highs late. CONFIRM-3 **YES** (ignition 17:25ET 867x, confirmed 17:35ET). Float 740K (ultra-low). Day% -8.7% (not a dead-cat, above -15%). Total% +42.9% (under the 150% ceiling). `tradable=true`. Alpaca quote stale at 16:00 ET (bid $3.08/ask $4.50, ~2h behind scan) — freshness guard: SIP is fresh (last bar 17:45 ET, ~15 min behind) and liquid, so this is a feed artifact, not a "no book." Late-building/late-peak (17:40 ET) profile is favorable. **Only its 1st AH scan >10%** — fails the 2-AH-scan gate. No entry this scan; **watch for the 00:30 CET final scan** — qualifies for entry then if it holds >10% AH (strong BUILD candidate).
- **HYFM** — Day% -15.6% (dead-cat territory), AH +14.8% but Total% -3.1% (still below its regular close, not reclaiming). VRatio 0.1x thin. Dead-cat bounce, no override. Skip.
- **AZI** — AH +7.9% (below threshold), Day% -9.8%. Skip.
- **BJDX** — AH +5.7% (below threshold); a 21:30 regular-session watch name, faded in AH. Skip.
- **LESL** — AH +10.3% but VRatio 0.2x (far below average), thin. Skip.
- **FGL / VMAR** — AH ≤10.5%, VRatio ≤0.2x thin. Below threshold. Skip.

21:30 watch names (ZYBT, ASTC, INLF, VRM, ABTS) remain below their regular close; SHPH carried untradable (`tradable=false` historically).

No new paper trades this scan (CELZ + PAVS held; CLRO flagged for entry at 00:30 CET pending a 2nd AH appearance >10%).

## Scan 00:30 CET (6:30 PM ET) — final scan

Scanner returned **9 AH hits**. Entry-eligible scan (final scheduled scan of the night).

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| CELZ | [TV](https://www.tradingview.com/chart/?symbol=CELZ) | $0.67 | +1.9% | +46.5% | $0.98 | +49.2% | 35.3M | 4.0M | 8.9x | 4.7M | Medical Specialties |
| CLRO | [TV](https://www.tradingview.com/chart/?symbol=CLRO) | $3.68 | -8.7% | +72.8% | $6.36 | +57.8% | 2.8M | 444K | 6.4x | 740K | Electronics/Appliances |
| PAVS | [TV](https://www.tradingview.com/chart/?symbol=PAVS) | $4.91 | +0.2% | +34.4% | $6.60 | +34.7% | 2.5M | 2.5M | 1.0x | 856K | Pharmaceuticals: Other |
| AZI | [TV](https://www.tradingview.com/chart/?symbol=AZI) | $1.01 | -9.8% | +12.9% | $1.14 | +1.8% | 2.1M | 321K | 6.4x | 4.4M | Specialty Stores |
| HYFM | [TV](https://www.tradingview.com/chart/?symbol=HYFM) | $1.62 | -15.6% | +13.0% | $1.83 | -4.7% | 850K | 15.8M | 0.1x | 4.1M | Trucks/Construction/Farm Machinery |
| LESL | [TV](https://www.tradingview.com/chart/?symbol=LESL) | $1.36 | +3.0% | +11.0% | $1.51 | +14.4% | 352K | 1.5M | 0.2x | 8.8M | Specialty Stores |
| MYO | [TV](https://www.tradingview.com/chart/?symbol=MYO) | $1.06 | -1.9% | +9.4% | $1.16 | +7.4% | 181K | 297K | 0.6x | 35.2M | Medical Distributors |
| NAUT | [TV](https://www.tradingview.com/chart/?symbol=NAUT) | $0.93 | -5.6% | +10.8% | $1.03 | +4.5% | 73K | 1.2M | 0.1x | 63.5M | Biotechnology |
| EVGN | [TV](https://www.tradingview.com/chart/?symbol=EVGN) | $0.63 | -2.9% | +6.2% | $0.67 | +3.1% | 62K | 137K | 0.5x | 12.0M | Biotechnology |

**Instrumentation (log-only, no decision impact):**
- CLRO: `SPIKE 17:28ET +23% $4.51 313 trades / 37k sh (first co-spike bar)` · `CONFIRM-3 YES ignition 17:25ET 867.1x; confirmed 17:35ET $5.30 as-of 18:30ET`

**CELZ — held (already entered 23:00).** Still on AH >10% (+46.5%, 6th scan). Position $0.99 vs $0.89 entry (+10.7%). Grade None — premarket exit handled by position-evaluation.

**PAVS — held (already entered 23:30).** Still on AH >10% (+34.4%, 5th scan). Position $6.41 vs $6.61 entry (-3.0%). Grade None — premarket exit handled by position-evaluation.

**CLRO — QUALIFIED, but NO FILL (broker no-fill).** Clears every entry gate on its **2nd AH scan >10%** (00:00 +56.5%, 00:30 +72.8%) → 2-AH-scan gate met. SIP bars fresh, real, liquid, and BUILDING to new highs: 21:25Z ignition (110K sh/989 tr H$5.50), sustained 200K–670K sh/bar through 22:15Z (18:15 ET, ~15 min behind scan), peak **H $6.76 at 22:05Z (18:05 ET)**, C $6.37 at 22:15Z. VWAP $6.0–6.4 corroborates scanner AH $6.36 (no bad print). CONFIRM-3 **YES** (ignition 17:25ET 867x, confirmed 17:35ET). Float 740K (ultra-low). Day% -8.7% (above -15%, not a dead-cat). Total% +57.8% (under the 150% ceiling). Late-building/late-peak (18:05 ET) → favorable BUILD profile. `tradable=true`. **No same-day catalyst found** (4 searches: only the July 2 stock-for-stock Cortigent reverse-merger, rebrand to CRGT — not fresh, and stock-for-stock so not a fixed-cash merger-arb exclusion; nothing same-day). No-catalyst = concern noted, not a skip. **Alpaca AH book would not fill:** quote stuck stale at 16:00 ET (bid $3.08/ask $4.50, 2.5h behind scan). Submitted BUY 15 CLRO limit $6.70 ext (id 2e5dadee) — sat `new`, no fill after ~50s; cancelled, re-submitted at limit $7.10 ext (id 9a420abd) — again no fill after ~50s; cancelled. Despite real SIP volume on the consolidated feed, Alpaca's own AH venue had no fillable ask. **No fill = no position.** Recorded as a qualified-but-unfillable broker no-fill for the morning-eval tally (a strong BUILD candidate the broker could not execute).
- **AZI** — AH +12.9% but Total% only +1.8% (Day -9.8%, still barely above prev close). Never built above close across scans; recovering from a down day, not a new-momentum breakout. Skip.
- **HYFM** — Day% -15.6% (dead-cat territory), Total% -4.7% (still below regular close, not reclaiming). VRatio 0.1x thin. Dead-cat bounce, no override. Skip.
- **NAUT** — AH +10.8% but VRatio 0.1x (73K vs 1.2M avg = far below average), float 63.5M (high), Total% +4.5%. Thin, no real momentum book. Skip.
- **LESL / MYO / EVGN** — AH ≤11%, VRatio ≤0.6x (below-average relative volume), thin trade counts. Below the momentum threshold. Skip.

**Final-scan feed-lag cross-check (pipeline names):** RECT (CONFIRM-3 YES at 23:00) died — faded below its $1.28 close by 23:30, confirmed dead, not rescued. AZI covered above (below-momentum). No tracked name is under-reported by the TradingView feed relative to SIP this scan; the two real movers (CELZ, PAVS) are already held and CLRO is present in the feed (no-fill, not feed-lag). 21:30 watch names (ZYBT, ASTC, INLF, BJDX, VRM, ABTS) remain below their regular close; SHPH carried untradable (`tradable=false` historically).

No new fills this scan — CELZ + PAVS held; CLRO qualified but the broker could not fill it.

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

---

## Morning Evaluation — 10:20 CEST

### Today's Winner

**CLRO** (ClearOne) — Electronics/Appliances (audio/AV conferencing)
- Catalyst: **Grade None (same-day).** Backdrop is the July 2 stock-for-stock Cortigent reverse-merger (rebrand to CRGT); no fresh same-day PR found. Ultra-low-float momentum squeeze.
- Previous Close (Aug 5 regular): **$3.68** (Aug 5 was a −8.7% red regular day on 8.5M sh)
- AH last night: SIP peak **$8.07** (+119.3%) at 18:35 ET / 00:35 CET, on accumulating volume (400K–700K sh/bar, 5K–11K trades/bar)
- Premarket now: **$7.07** (+92.1%) at 04:20 ET; **PM SIP peak $9.00** (+144.6%) at 04:00 ET open on 895K sh / 20,524 trades
- Hypothetical P&L (qualified AH entry $6.70 → PM peak $9.00): **+34.3%**
- Float: **740K** (ultra-low) | Market Cap: ~$9.8M

Clears the winner bar: **>100% (both AH +119% and PM +145%) on high, accumulating SIP volume.** Real, liquid explosion — not a thin ramp or bad print.

**Scanner Diagnostic:**
- Detectable at screening time? **YES**
- The scanner **caught it.** Move ignited 17:25 ET (21:25Z), within the scanned window. Flagged **WATCH** at 00:00 CET (1st AH scan >10%, +56.5%), then **QUALIFIED** at the 00:30 CET final scan on its 2nd AH scan >10% (+72.8%). CONFIRM-3 YES, float 740K, Day% −8.7% (not a dead-cat), Total% +57.8% (under ceiling), tradable=true.
- **Why we didn't hold it: broker no-fill / stale-book execution block.** Alpaca's AH quote was stuck stale at 16:00 ET (bid $3.08/ask $4.50, 2.5h behind the scan). Orders at $6.70 and $7.10 ext both sat `new` with no fill despite real SIP volume on the consolidated feed. No fillable ask on Alpaca's own venue → no position.
- Scanner gap: **none — this is not a detection or selection failure, it is an execution-data (stale extended-hours quote) failure.** Same class as NUWE (Jul 29→30) and KUST (Jul 30→31).

### Baseline Tracking

- Days tracked: **61** (was 60 + 1)
- Winners detected by scanner: **49/58 (84.5%)** — CLRO detected (WATCH → QUALIFIED)
- Winner selected for paper trade: **27/58 (46.6%)** — CLRO qualified but was a stale-book no-fill; per the execution-block rule this is not counted as a selection (numerator held), denominator +1
- Target: >80% detection
- Status: **BASELINE MET** (84.5% > 80%)

### Retrospective Scan Results

Live PM scan (04:20 ET) top hits: CLRO +92.1% ($7.07), CLRO the standout; PAVS +36.5% ($6.70), CELZ +25.6% ($0.84), AZI +11.4%, LIDR +9.5%. Biggest raw PM mover = **CLRO** (an AH→PM continuation, detectable — not a PM-only gapper). SIP reconstruction confirms CLRO AH ignition 17:25 ET → AH peak $8.07 (18:35 ET) → PM peak $9.00 (04:00 ET open). PAVS PM SIP peak $7.98; CELZ PM SIP peak $0.95.

### Open Position P&L (Alpaca)

Two positions carried from last night's entries (CELZ entered 23:00, PAVS entered 23:30). Standalone `quote` endpoint is stale (CELZ 16:38 ET, PAVS 16:00 ET) but the `positions` `current_price` is live and matches the PM SIP tape, so P&L below is reported against the live PM price. **This is a diagnostic — no exits here; position-evaluation.md (10:30 CET) manages hold/sell.**

| Ticker | Entry | Entry Total% | Catalyst | Entry Time | PM Peak (SIP) | Peak Time | Exit | P&L | P&L % | Status |
|--------|-------|--------------|----------|------------|---------------|-----------|------|-----|-------|--------|
| CELZ | $0.89 | +33% | None | 23:00 CET | $0.95 | 04:00 ET | open | — | −2.9% | 🟡 Open (live $0.86) |
| PAVS | $6.61 | +45% | None | 23:30 CET | $7.98 | 04:00 ET | open | — | +4.5% | 🟢 Open (live $6.91) |

**Total Realized P&L (Alpaca fills only): €0.00** (no exits yet)

### Scanner Effectiveness

- Evening scans ran: **9** (21:30, 22:00, 22:15, 22:30, 22:45, 23:00, 23:30, 00:00, 00:30 CET) — **all 7 scheduled scans ran + 2 bonus. Coverage: 7 of 7.** Entry window fully captured.
- Candidates found: CELZ, PAVS, CLRO (all real, liquid movers surfaced); FRGT/RECT/HYFM/BJDX correctly skipped
- Retrospective matches: 3/3 real movers detected (CELZ, PAVS, CLRO)

### Missed Opportunities

No significant missed opportunities. The three real AH→PM movers (CLRO, PAVS, CELZ) were all detected. CLRO was the only >100% winner and it was caught; the loss was execution (stale book), not detection.

### AH Mover Follow-Through

| Ticker | AH Peak (SIP) | Peak Time | AH Trajectory | Current PM | From Peak | From Close | Verdict |
|--------|---------------|-----------|---------------|------------|-----------|-----------|---------|
| CLRO | $8.07 | 18:35 ET | Build (late-igniting, +17% at 17:25 → +119% by 18:35) | $7.07 (PM peak $9.00) | −12% off PM peak | +92% (peak +145%) | PM peak > AH peak → continued |
| PAVS | $7.55 | 16:45 ET | Build-and-hold | $6.91 (PM peak $7.98) | −13% off PM peak | +41% (peak +62.5%) | PM peak > AH peak → continued |
| CELZ | $1.06 | 16:05 ET | Spike→hold/reclaim | $0.86 (PM peak $0.95) | −19% off PM peak | +17% | PM peak < AH peak (AH was better exit) |

**AH-peak-vs-PM-peak check:** CLRO and PAVS both extended past their AH peaks into PM (continuation). CELZ's AH peak $1.06 exceeded its PM peak $0.95 — AH was the better exit for CELZ (early-peak name). No extreme-AH-runner (>250%) fade case today.

### Notes

- **Stale-book execution-block tracking:** CLRO (Aug 5→6) adds to the tally. Quote frozen at 16:00 ET (`bid $3.08/ask $4.50`) through the final scan; SIP bars were fresh, real, liquid (400K–700K sh/bar); qualified ~$6.70 → PM peak $9.00 = **+34.3%**. **Standing count: 3, all three detected winners, all profitable hypotheticals** (NUWE +82.4%, KUST +45.9%, CLRO +34.3%). This is the third night in ~8 sessions where a detected, qualifying winner was lost solely to a stale Alpaca extended-hours quote. Cumulative hypothetical cost is now material — **route the repeated stale extended-hours quote problem (3 lost winners) to Juan's daily email as a paper-data/execution-feed decision.** Keep the live-book safety gate unchanged here.
- **Reverse-split tracking:** PAVS is a known reverse-split name (1-for-100, Jun 25, now ~6 weeks old / weeks-old bucket), though last night's entry thesis was momentum, not the split (catalyst noted None). Entered $6.61 → PM peak $7.98 = **+20.7%, continue** (PM peak above entry). Weeks/months-old bucket now 3 non-fade (EDHL, LGCL, PAVS-continue) vs earlier PAVS fade (Jul 23→24) — older-split bucket stays mixed. This-week-split bucket unchanged at 3/3 fade.
- **Fade-rule false-negative tracking:** no new sub-3M AH-fader re-explosion today. FRGT (SPIKE→FADE, illiquid) and RECT (faded below close) both stayed dead into PM — fade rule correct. Standing sub-3M count unchanged at 4 of 11 (below the ≥80% trigger).
- **In-window feed-lag miss tracking:** none today — CLRO was surfaced by the feed (no-fill, not feed-lag). Standing count unchanged at 4 (≥3 escalation trigger remains REACHED; AH-data-source-verification recommendation already routed).
- **PM-only gapper / late-AH-tail / price-floor exclusion:** none today. Biggest PM mover (CLRO) was an in-window, detected AH→PM continuation.
- **Coverage:** full 7/7. No coverage-failure tally entry.
- **Baseline chain:** no gap — Aug 4 log (Days 60) is the immediately-preceding trading day; this eval is Aug 5 session → Days 61.

### Price Charts

```
CLRO — 2-day, base $3.68 (Aug 5 regular close)
AH ignition 17:25 ET → AH SIP peak $8.07 (+119%) 18:35 ET → PM SIP peak $9.00 (+145%) 04:00 ET → faded to $7.07 (+92%) by 04:20 ET
Volume: 400K–700K sh/bar in AH, 895K sh/20.5K trades on the PM-open peak bar — real, accumulating, liquid.
```
