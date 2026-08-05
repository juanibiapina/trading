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

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
| — | — | — | — | — | No entries (regular-session scan) |

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
