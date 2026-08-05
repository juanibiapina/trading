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
