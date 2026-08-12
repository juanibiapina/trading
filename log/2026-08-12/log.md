# Post-Market Screening - 2026-08-12

## Scan 21:30 CET (3:30 PM ET)

**Regular session — before AH open (16:00 ET / 22:00 CET). No entries; candidates flagged Watch pending AH confirmation** (per regular-session caution: intraday spikes that don't carry into AH tend to fade).

Notable intraday movers with real volume (most scanner hits show huge negative VChg% = fading, tiny 5mVol = stale prints):

| Ticker | Chart | Price | Chg% | 5mVol | IRVol | Float | MCap | Industry | Note |
|--------|-------|-------|------|-------|-------|-------|------|----------|------|
| DOGZ | [TV](https://www.tradingview.com/chart/?symbol=DOGZ) | $1.30 | +40.3% | 13K | 1243.9 | 4.3M | 18.9M | Consumer Sundries | Watch — VChg -10% (fading) |
| BANL | [TV](https://www.tradingview.com/chart/?symbol=BANL) | $5.40 | +30.6% | 16K | 82.4 | 407K | 11.4M | Air Freight/Couriers | Watch — low float 407K, VChg +92.6% |
| GRWG | [TV](https://www.tradingview.com/chart/?symbol=GRWG) | $1.84 | +23.6% | 16K | 14.7 | 54.7M | 110.6M | Wholesale Dist | Watch — high float |
| DRMA | [TV](https://www.tradingview.com/chart/?symbol=DRMA) | $1.33 | +23.1% | 16K | 103.7 | 2.7M | 5.3M | Pharma | Already traded today, position closed -19.1% |
| BCG | [TV](https://www.tradingview.com/chart/?symbol=BCG) | $1.50 | +15.1% | 5K | 16.3 | 3.6M | 25.3M | Investment Managers | Watch |

Remaining hits (BOXL, RMCF, OFAL, BQ, CHOW, XHLD, etc.) show VChg% near -100% with sub-1K 5mVol = stale/regular-session artifacts, not live spikes. BAOS and BOXL were traded and closed this morning (see Position Evaluation).

**No paper trades this scan** — regular session, AH not yet open. Real AH screening begins at the 22:00 CET scan.

## Scan 22:00 CET (4:00 PM ET)

No candidates found. Scanner returned 0 AH hits at AH open (16:00 ET). None of the 21:30 regular-session watch names (DOGZ, BANL, GRWG, BCG) carried into the AH feed above threshold at this scan. Nothing to evaluate; no entries (learning-phase default holds entries until the 23:00 CET scan regardless).

## Scan 22:15 CET (4:15 PM ET)

No candidates found. Scanner returned 0 AH hits 15 min into the after-hours session. None of the 21:30 regular-session watch names (DOGZ, BANL, GRWG, BCG) surfaced in the AH feed above threshold. Nothing to evaluate; no entries (learning-phase default holds entries until the 23:00 CET scan regardless).

## Scan 22:30 CET (4:30 PM ET)

First AH scan with real hits tonight. 7 hits; two clear >10% AH movers on real accumulating SIP volume:

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| LGCL | [TV](https://www.tradingview.com/chart/?symbol=LGCL) | $1.42 | +2.2% | +42.3% | $2.02 | +45.3% | 2.3M | 522K | 4.5x | 1.6M | Personnel Services |
| GXAI | [TV](https://www.tradingview.com/chart/?symbol=GXAI) | $0.87 | -1.7% | +28.7% | $1.12 | +26.5% | 1.6M | 457K | 3.5x | 10.5M | Packaged Software |

Sub-threshold hits (AH <10%, not evaluated): RKDA +5.7%, LESL +9.8%, LNAI +8.5%, CURI +8.2%. BBLG +8.7% AH but Day -27.6% (dead-cat, sub-threshold anyway).

**Observation-only scan** — learning-phase default holds entries until the 23:00 CET scan. No entries.

**Instrumentation (log-only, no decision impact):**
- LGCL: `SPIKE 16:05ET +23% $1.75 750 trades / 82k sh (first co-spike bar)` | `CONFIRM-3 NO ignition 16:05ET failed third-bar hold/volume`
- GXAI: `SPIKE 16:10ET +26% $1.10 475 trades / 161k sh (first co-spike bar)` | `CONFIRM-3 PENDING ignition 16:10ET; waiting for third bar`

**SIP volume (both real, accumulating, not stale/bad-print):**
- LGCL: 20:05Z 1.04M sh/7958 tr, 20:10Z 1.71M sh/14062 tr, 20:15Z 1.00M sh/7231 tr. VWAP $1.83→$2.03→$1.91, corroborates scanner AH price. Peaked $2.17 at 20:10Z, pulling back to $1.93.
- GXAI: 20:10Z 1.74M sh/6796 tr, 20:15Z 3.02M sh/11812 tr. VWAP $1.08→$1.19, building. High $1.28.

**Catalyst:**
- LGCL: no same-day catalyst found (3 searches). Recent PRs are financing-plan updates (Jul 2) and 1H results (Oct 2025). AI/PaaS HR + insurance name, float 1.6M. No-catalyst — note only.
- GXAI: **same-day GlobeNewswire press release timestamped Aug 12, 2026 16:10 ET** — exactly matches the ignition bar. Content not retrieved within search budget; grade TBD at 23:00. Gaxos.ai, AI/gaming, float 10.5M.

**Trajectory watch for 23:00:** LGCL peaked early (20:10Z) and is fading off its high ($2.17→$1.93, ~11% off) but still holding within 20%; CONFIRM-3 NO. GXAI still building toward its high on rising volume with a real PR catalyst. Re-evaluate both at 23:00 CET against the 2-AH-scan gate (each has only 1 AH scan so far), extension ceiling, and hold-vs-fade.

## Scan 22:45 CET (4:45 PM ET)

5 hits. GXAI now the clear leader, building hard across two AH scans; LGCL fading off its high.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| GXAI | [TV](https://www.tradingview.com/chart/?symbol=GXAI) | $0.87 | -1.7% | +56.1% | $1.36 | +53.5% | 9.6M | 1.3M | 7.2x | 10.5M | Packaged Software |
| LGCL | [TV](https://www.tradingview.com/chart/?symbol=LGCL) | $1.42 | +2.2% | +14.1% | $1.62 | +16.6% | 4.6M | 782K | 5.9x | 1.6M | Personnel Services |
| CURI | [TV](https://www.tradingview.com/chart/?symbol=CURI) | $2.80 | +0.0% | +14.3% | $3.20 | +14.3% | 236K | 290K | 0.8x | 40.2M | Movies/Entertainment |

Sub-threshold / skipped: BBLG +5.5% AH but Day -27.6% (dead-cat, sub-threshold anyway); RNXT +6.2% AH.

**Instrumentation (log-only, no decision impact):**
- GXAI: `SPIKE 16:10ET +26% $1.10 475 trades / 161k sh (first co-spike bar)` | `CONFIRM-3 YES ignition 16:10ET 1883.7x; confirmed 16:20ET $1.33`
- LGCL: `SPIKE 16:05ET +23% $1.75 750 trades / 82k sh (first co-spike bar)` | `CONFIRM-3 NO ignition 16:05ET failed third-bar hold/volume`
- CURI: `SPIKE 16:21ET +25% $3.50 221 trades / 32k sh (first co-spike bar)` | `CONFIRM-3 NO ignition 16:20ET failed third-bar hold/volume`

**SIP volume (GXAI real, accumulating, not stale/bad-print):** 20:10Z 1.74M sh/6796 tr, 20:15Z 3.02M sh/11812 tr, 20:20Z 2.27M sh/10011 tr, 20:25Z 3.35M sh/13953 tr, 20:30Z 2.74M sh/12134 tr. VWAP climbing $1.08→$1.19→$1.27→$1.39→$1.43, corroborates scanner AH price. High $1.49. Live book: **bid $1.44 x300 / ask $1.46 x300** (real two-sided AH liquidity). `tradable=true`.

**Catalyst (GXAI):** same-day GlobeNewswire PR Aug 12 2026 ~16:10 ET (matches ignition bar) — "Revenue growth significantly outpaces advertising expense growth as revenue generated per advertising dollar improves." Business/metrics efficiency update, not acquisition/FDA/contract. **Grade C** (weak operational PR).

**Trajectory:** GXAI = textbook BUILD — up +28.7%→+56.1% across two AH scans, price making new highs on rising SIP volume, CONFIRM-3 YES, real book, live PR. LGCL = SPIKE→FADE (peaked $2.17 @20:10Z, now $1.62, ~25% off high, CONFIRM-3 NO) — disqualified as a fade. CURI = VRatio 0.8x (AH vol below avg), CONFIRM-3 NO — not a real spike.

**No entries this scan** — 22:45 CET is before the 23:00 learning-phase entry gate; observation only. GXAI now clears the 2-AH-scan gate (22:30 + 22:45), Total% +53.5% (well under the 150% ceiling), Day% -1.7%, float 10.5M, real book, Grade-C catalyst. **Primed to enter at the 23:00 CET scan** if it holds/builds. Re-verify book and price then.

## Scan 23:00 CET (5:00 PM ET)

Entry gate scan. 6 hits; GXAI is the clear BUILD leader across three AH scans.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| GXAI | [TV](https://www.tradingview.com/chart/?symbol=GXAI) | $0.87 | -1.7% | +66.6% | $1.45 | +63.7% | 15.8M | 2.0M | 8.0x | 10.5M | Packaged Software |
| CURI | [TV](https://www.tradingview.com/chart/?symbol=CURI) | $2.80 | +0.0% | +25.9% | $3.52 | +25.9% | 808K | 358K | 2.3x | 40.2M | Movies/Entertainment |
| LGCL | [TV](https://www.tradingview.com/chart/?symbol=LGCL) | $1.42 | +2.2% | +13.5% | $1.61 | +15.9% | 5.5M | 883K | 6.2x | 1.6M | Personnel Services |
| PRHI | [TV](https://www.tradingview.com/chart/?symbol=PRHI) | $4.16 | -9.4% | +38.9% | $5.78 | +25.9% | 1K | 5K | 0.3x | 2.5M | Property/Casualty Insurance |

Sub-threshold (AH <10%, not evaluated): GCDT +5.1%, RNXT +8.9%.

**Instrumentation (log-only, no decision impact):**
- GXAI: `SPIKE 16:10ET +26% $1.10 475 trades / 161k sh (first co-spike bar)` | `CONFIRM-3 YES ignition 16:10ET 1883.7x; confirmed 16:20ET $1.33`
- CURI: `SPIKE 16:21ET +25% $3.50 221 trades / 32k sh (first co-spike bar)` | `CONFIRM-3 NO ignition 16:20ET failed third-bar hold/volume`
- LGCL: `SPIKE 16:05ET +23% $1.75 750 trades / 82k sh (first co-spike bar)` | `CONFIRM-3 NO ignition 16:05ET failed third-bar hold/volume`

**GXAI — ENTER.** Clears every gate:
- 2-AH-scan gate: 3 AH scans >10% (22:30 +28.7%, 22:45 +56.1%, 23:00 +66.6%) — textbook BUILD.
- SIP volume real & accumulating (not stale/bad-print): 20:10Z 1.74M sh/6796 tr → 20:15Z 3.02M/11812 → 20:20Z 2.27M/10011 → 20:25Z 3.35M/13953 → 20:30Z 2.74M/12134 → 20:35Z 2.32M/9144 → 20:40Z 1.56M/7161 → 20:45Z 1.40M/6150. VWAP climbed $1.08→$1.46, corroborates scanner AH price. High $1.53 (20:35Z). Last two bars pulled back C$1.44→$1.38 (~10% off high, within 20% = holding, not a fade). Last SIP bar 16:45 ET vs 17:00 scan = ~15 min free-tier lag, expected.
- Live book: **bid $1.37 x200 / ask $1.56 x300** (quote @16:59 ET, fresh) — real two-sided AH liquidity. `tradable=true`.
- Day% -1.7%, float 10.5M, Total% +63.7% (well under 150 ceiling), CONFIRM-3 YES.
- Catalyst: same-day GlobeNewswire PR ~16:10 ET (matches ignition) — revenue/advertising-efficiency operational update. **Grade C** (weak operational PR). No-catalyst-quality concern is moot; enter on BUILD + real book.
- **Entered:** BUY 64 GXAI @ limit $1.59 ext (id c99e8f14) **filled @ $1.42** (price improvement).

**Skips:**
- **CURI — skip: illiquid (no AH book).** `quote` shows `ask $0.00 x0` (timestamped 16:00 ET, stale) — no fillable AH book behind the +25.9% scanner print. VRatio 2.3x, float 40.2M, CONFIRM-3 NO. Not enterable.
- **LGCL — skip: SPIKE→FADE.** Peaked $2.17 @20:10Z early, now $1.61 (~26% off high, >20% = fade, not hold). AH% +42.3%→+14.1%→+13.5% across scans. CONFIRM-3 NO. Early-peak fade, 0/10+ for PM continuation.
- **PRHI — skip: thin/illiquid.** AH Vol 1K, AvgVol 5K, VRatio 0.3x — the +38.9% is a stale/thin print, not real AH liquidity. Day -9.4%.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
| GXAI | $1.42 | 23:00 CET (17:00 ET) | 64 | c99e8f14 | AH BUILD 3 scans (+28.7→+56.1→+66.6%), real SIP vol (M sh/K trades/bar), real book, CONFIRM-3 YES, Grade C PR, Total% +63.7% under ceiling, float 10.5M |

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| BAOS | $0.90 | $2.24 | +148.9% | $2.19 (PM) | 1 | None | SELL | Grade None — exit at any profit. PM ran $1.70→$2.19H on 2.6M sh/20k trades. Filled $2.24 (price improvement). |
| BOXL | $4.01 | $5.83 | +45.4% | $6.50 (PM) | 1 | None | SELL | Grade None — exit at any profit. PM ran $4.35→$6.50H on 1.2M sh/22k trades. Filled $5.83. |
| DRMA | $1.52 | $1.43 | -5.9% | $1.59 (PM) | 1 | B | HOLD | Above -15% stop ($1.29), day 1 of 2. Peak +4.6% never hit +30% trail. PM $1.40-1.59, VWAP $1.45. |
| FF | $6.28 | $6.20 | -1.3% | $6.45 | 2 | B | SELL | Grade B day-2 time limit reached. Flat, thin PM. Filled $6.20. |

**Actions taken:**
- SELL 102 BAOS @ limit $1.98 ext (id 40fe100d) filled @ $2.24 → +$136.68 (+148.9%)
- SELL 24 BOXL @ limit $5.75 ext (id 742fee8e) filled @ $5.83 → +$43.68 (+45.4%)
- SELL 16 FF @ limit $6.00 ext (id f2d3ab05) filled @ $6.20 → -$1.28 (-1.3%)
- HOLD DRMA (Grade B, day 1, within risk)
- **Pulse net realized: +$179.08.** BAOS Grade-None exit captured a rare +149% overnight runner.


## Position Evaluation — 14:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| DRMA | $1.52 | $1.23 | -19.1% | $1.59 (PM) | 1 | B | SELL | Below -15% Grade B hard stop ($1.29). PM faded monotonically $1.59→$1.35; live bid $1.21 x100. Filled $1.23 (price improvement). |

**Actions taken:**
- SELL 66 DRMA @ limit $1.18 ext (id fcf9ca9f) filled @ $1.23 → -$19.14 (-19.1%)
- No open positions remain.
