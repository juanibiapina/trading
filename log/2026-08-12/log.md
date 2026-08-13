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

## Scan 23:30 CET (5:30 PM ET)

6 hits. GXAI still leading and building; two new >10% AH names (OFAL, USIO) appear for the first time this scan.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| GXAI | [TV](https://www.tradingview.com/chart/?symbol=GXAI) | $0.87 | -1.7% | +70.1% | $1.48 | +67.2% | 21.2M | 2.6M | 8.3x | 10.5M | Packaged Software |
| OFAL | [TV](https://www.tradingview.com/chart/?symbol=OFAL) | $0.73 | +90.7% | +17.6% | $1.60 | +124.3% | 2.9M | 16.3M | 0.2x | n/a | Engineering & Construction |
| USIO | [TV](https://www.tradingview.com/chart/?symbol=USIO) | $2.38 | +6.7% | +18.9% | $2.83 | +26.9% | 770K | 404K | 1.9x | 19.0M | Finance/Rental/Leasing |
| CURI | [TV](https://www.tradingview.com/chart/?symbol=CURI) | $2.80 | +0.0% | +14.6% | $3.21 | +14.6% | 1.3M | 420K | 3.2x | 40.2M | Movies/Entertainment |

Sub-threshold (AH <10%, not evaluated): GCDT +7.3%, RNXT +8.9%.

**Instrumentation (log-only, no decision impact):**
- GXAI: `SPIKE 16:10ET +26% $1.10 475 trades / 161k sh (first co-spike bar)` | `CONFIRM-3 YES ignition 16:10ET 1883.7x; confirmed 16:20ET $1.33`
- OFAL: `SPIKE 16:58ET +22% $1.66 952 trades / 257k sh (first co-spike bar)` | `CONFIRM-3 YES ignition 16:55ET 11.0x; confirmed 17:05ET $1.66`
- USIO: `SPIKE 17:07ET +24% $2.94 142 trades / 26k sh (first co-spike bar)` | `CONFIRM-3 NO ignition 17:05ET failed third-bar hold/volume`

**GXAI (open position) — HOLD, no new entry** (one entry per candidate per night). Entered 23:00 @ $1.42. Still BUILD: AH +66.6%→+70.1%, SIP last bars 21:10Z 1.30M sh/4848 tr, 21:15Z 1.86M sh/7891 tr, VWAP back to $1.53, high $1.58 — making new highs on rising volume. Live book bid $1.37 x200 / ask $1.56 x300 (quote @16:59 ET). Position now $1.43, +0.7%. Position management handled by premarket eval.

**Skips / watches (both new names fail the 2-AH-scan gate — first AH-scan appearance this scan; not enterable regardless):**
- **OFAL — watch (real surge, but 1 AH scan + no confirmable book).** Real accumulating SIP: 20:55Z 550K sh/2304 tr, 21:00Z 445K/2023, 21:05Z 678K/3007, 21:10Z 211K/1335 — genuine late-starting AH ignition (16:55 ET, after the 23:00 scan), VWAP $1.57→$1.67, CONFIRM-3 YES. Not stale/bad-print. But: (1) first AH-scan appearance → fails 2-AH-scan gate; (2) `quote ask $0.00 x0` timestamped 16:00 ET (stale) — no confirmable live two-sided book; (3) Day% +90.7% (intraday +172% per StocksToTrade) with **no same-day company catalyst** (recent PRs: 1-for-10 reverse split Jul 27, domestic-issuer status May 21) — low-float day-trader momentum runner. Re-evaluate at 00:00 CET: needs a 2nd AH scan >10% + a fillable book.
- **USIO — watch/skip.** AH +18.9% but CONFIRM-3 NO (ignition 17:05ET failed third-bar hold), VRatio 1.9x, `quote ask $0.00 x0` (stale 16:00 ET) — no confirmable book. First AH-scan appearance → fails 2-AH-scan gate. Not enterable.
- **CURI — skip: illiquid (no AH book), carried.** AH +14.6%, VRatio 3.2x but book was `ask $0.00 x0` at 23:00; CONFIRM-3 NO, float 40.2M. Same as prior scans.

**No new entries this scan.** GXAI position held from 23:00. OFAL/USIO watch for the 00:00 CET scan (need 2nd AH scan + fillable book).

## Scan 00:00 CET (6:00 PM ET)

7 hits. GXAI still leading (open position). OFAL now on its 2nd AH scan >10%; BIVI appears for the first time.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| GXAI | [TV](https://www.tradingview.com/chart/?symbol=GXAI) | $0.87 | -1.7% | +62.0% | $1.41 | +59.2% | 25.3M | 3.0M | 8.4x | 10.5M | Packaged Software |
| BIVI | [TV](https://www.tradingview.com/chart/?symbol=BIVI) | $1.56 | +22.8% | +21.2% | $1.89 | +48.8% | 1.9M | 13.8M | 0.1x | 7.2M | Biotechnology |
| CURI | [TV](https://www.tradingview.com/chart/?symbol=CURI) | $2.80 | +0.0% | +20.4% | $3.37 | +20.4% | 1.5M | 437K | 3.4x | 40.2M | Movies/Entertainment |
| OFAL | [TV](https://www.tradingview.com/chart/?symbol=OFAL) | $1.36 | +90.7% | +16.2% | $1.58 | +121.5% | 3.4M | 16.3M | 0.2x | n/a | Engineering & Construction |
| FGI | [TV](https://www.tradingview.com/chart/?symbol=FGI) | $4.73 | +4.0% | +9.1% | $5.16 | +13.4% | 753K | 119K | 6.3x | 522K | Building Products |

Sub-threshold (AH <10%, not evaluated): FGI +9.1%, LGCL +5.6% (faded further), RNXT +7.1%.

**Instrumentation (log-only, no decision impact):**
- GXAI: `SPIKE 16:10ET +26% $1.10 475 trades / 161k sh (first co-spike bar)` | `CONFIRM-3 YES ignition 16:10ET 1883.7x; confirmed 16:20ET $1.33`
- OFAL: `SPIKE 16:58ET +22% $1.66 952 trades / 257k sh (first co-spike bar)` | `CONFIRM-3 YES ignition 16:55ET 11.0x; confirmed 17:05ET $1.66`
- BIVI: `SPIKE 17:39ET +21% $1.89 840 trades / 212k sh (first co-spike bar)` | `CONFIRM-3 NO ignition 17:35ET failed third-bar hold/volume`
- CURI: `SPIKE 16:21ET +25% $3.50 221 trades / 32k sh (first co-spike bar)` | `CONFIRM-3 NO ignition 16:20ET failed third-bar hold/volume`

**GXAI (open position) — HOLD, no new entry** (one entry per candidate per night). Entered 23:00 @ $1.42, Grade C. Still leading the scan at AH +62.0%. Position management handled by premarket eval, out of scope here.

**Skips:**
- **OFAL — skip: illiquid (no AH book).** Momentum gates now pass — 2nd AH scan >10% (23:30 +17.6%, 00:00 +16.2%), Total% +121.5% under the 150 ceiling, Day% +90.7% (a real intraday runner, not a dead-cat), CONFIRM-3 YES, and SIP is real & accumulating (ignition 16:55 ET, holding $1.55-1.70 across bars, VWAP $1.57→$1.63 corroborates the scanner AH price, last bar 17:35 ET). **But the Alpaca book has no fillable ask:** `quote bid $1.15 x100 / ask $0.00 x0`, frozen at 16:00 ET across two re-pulls — no live two-sided AH book to lift. Per the AH-liquidity sanity check, skip as illiquid; a limit buy would sit unfilled with no offer. Record as **qualified-but-no-fillable-book** for the morning-eval tally (still no same-day company catalyst; recent PRs are the Jul 27 1-for-10 reverse split and May 21 domestic-issuer status — low-float day-trader runner).
- **BIVI — skip: fails 2-AH-scan gate + no confirmable book.** First AH-scan appearance this scan (ignition 17:35 ET, late) → cannot clear the 2-AH-scan gate. CONFIRM-3 NO (third-bar hold failed). `quote bid $1.36 x100 / ask $2.50 x1000` @16:59 ET — the $2.50 ask sits far above the $1.89 AH price (wide/thin offer), not a clean fillable book. Watch for a 2nd AH scan; Day +22.8%, float 7.2M, Biotech.
- **CURI — skip: illiquid (no AH book), carried.** AH +20.4%, VRatio 3.4x but book has been `ask $0.00 x0` all night; CONFIRM-3 NO, float 40.2M. Same as prior scans.
- **FGI — sub-threshold (AH +9.1%).** Not evaluated; low float 522K, VRatio 6.3x — note for later scan if it pushes >10%.

**No new entries this scan.** GXAI position held from 23:00. OFAL clears the momentum gate but has no fillable Alpaca AH book (skip, recorded). No other candidate clears both the 2-AH-scan gate and a fillable-book check.

## Scan 00:30 CET (6:30 PM ET) — final scheduled scan

11 hits. GXAI still leading (open position). BIVI now on its 2nd AH scan >10% (clears the 2-AH-scan gate); HXHX appears for the first time.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| GXAI | [TV](https://www.tradingview.com/chart/?symbol=GXAI) | $0.87 | -1.7% | +59.7% | $1.39 | +57.0% | 27.0M | 3.2M | 8.5x | 10.5M | Packaged Software |
| BIVI | [TV](https://www.tradingview.com/chart/?symbol=BIVI) | $1.56 | +22.8% | +29.5% | $2.02 | +59.1% | 4.9M | 14.1M | 0.3x | 7.2M | Biotechnology |
| HXHX | [TV](https://www.tradingview.com/chart/?symbol=HXHX) | $0.54 | +11.8% | +43.4% | $0.78 | +60.3% | 2.2M | 4.2M | 0.5x | 4.0M | Trucking |
| OFAL | [TV](https://www.tradingview.com/chart/?symbol=OFAL) | $1.36 | +90.7% | +14.0% | $1.55 | +117.3% | 3.8M | 16.4M | 0.2x | n/a | Engineering & Construction |
| CURI | [TV](https://www.tradingview.com/chart/?symbol=CURI) | $2.80 | +0.0% | +22.5% | $3.43 | +22.5% | 1.6M | 445K | 3.5x | 40.2M | Movies/Entertainment |

Sub-threshold (AH <10%, not evaluated): USIO +9.7%, CYCU +10.7% (VRatio 0.0 — no real AH vol), FGI +9.9%, BBLG -22.6% (dead-cat), RNXT +8.0%, CDIO +6.5%.

**Instrumentation (log-only, no decision impact):**
- GXAI: `SPIKE 16:10ET +26% $1.10 475 trades / 161k sh (first co-spike bar)` | `CONFIRM-3 YES ignition 16:10ET 1883.7x; confirmed 16:20ET $1.33`
- BIVI: `SPIKE 17:39ET +21% $1.89 840 trades / 212k sh (first co-spike bar)` | `CONFIRM-3 NO ignition 17:35ET failed third-bar hold/volume`
- HXHX: `SPIKE 18:08ET +19% $0.64 307 trades / 134k sh (first co-spike bar)` | `CONFIRM-3 YES ignition 18:05ET 370.7x; confirmed 18:15ET $0.71`

**Final-scan feed-lag cross-check:** pulled BIVI SIP directly (below) — scanner is reporting all tracked movers on real levels, no under-reporting. GXAI remains the live leader on the feed.

**GXAI (open position) — HOLD, no new entry** (one entry per candidate per night). Entered 23:00 @ $1.42, Grade C. Still the scan leader at AH +59.7% on 27.0M AH vol / VRatio 8.5x. Position management handled by premarket eval, out of scope here.

**Skips:**
- **BIVI — skip: no fillable book** (qualified-but-no-fillable-book, recorded for morning eval). Momentum gates now pass: 2nd AH scan >10% (00:00 +21.2%, 00:30 +29.5%), Day% +22.8% (positive, not a dead-cat), Total% +59.1% (under the 150 ceiling), float 7.2M. SIP is real & accumulating on a genuine re-ignition — early spike to $1.62 (16:20 ET) → hour-long fade to a $1.32-1.40 base → fresh **new high** $1.89 at 17:35 ET on 519k sh / 1804 trades (last SIP bar). Not stale/bad-print (scanner $2.02 vs SIP high $1.89 is a ~55-min free-tier lag, not a bad print). **But the Alpaca book is frozen at bid $1.36 x100 / ask $2.50 x1000 @16:59 ET across two re-pulls** — the $2.50 ask sits 25-33% above the $1.89-2.02 traded price. No clean fillable two-sided book: a limit near $2.00 sits unfilled behind the $2.50 offer, and lifting the ask would buy ~33% above where it trades. Per the AH-liquidity sanity check, skip. CONFIRM-3 NO. No same-day catalyst found (4 searches — all results 2021-2023; BioVie is a clinical-stage Alzheimer's/liver neuro biopharma, driver unknown).
- **HXHX — skip: fails 2-AH-scan gate + no book.** First AH-scan appearance this scan (ignition 18:05 ET, late) → cannot clear the 2-AH-scan gate. `quote bid $0.45 x100 / ask $0.00 x0` @16:00 ET (stale) — no fillable ask. Day +11.8%, float 4.0M, VRatio 0.5x, CONFIRM-3 YES. Watch only; not enterable.
- **CYCU — skip: no real book / VRatio 0.0.** `quote bid $0.53 / ask $20.00 x100` — absurd ask, no fillable market. VRatio 0.0 = no real AH volume behind the +10.7% print.
- **OFAL — skip: illiquid (no AH book), carried.** Day +90.7%, Total% +117.3%, but book has been `ask $0.00 x0` all night. Low-float day-trader runner, no same-day company catalyst. Same as prior scans.
- **CURI — skip: illiquid (no AH book), carried.** AH +22.5%, VRatio 3.5x but `ask $0.00 x0` all night; float 40.2M. Same as prior scans.

**No new entries this scan.** GXAI position held from 23:00. BIVI clears the momentum gates but has no fillable Alpaca AH book (skip, recorded for morning-eval tally). This concludes tonight's scheduled scans: **1 entry (GXAI @ $1.42), 1 qualified-but-no-fillable-book (BIVI), plus OFAL carried no-book.**

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

## Morning Evaluation — 10:20 CET

### Today's Winner

**No real winner today.** Nothing cleared the >100% winner bar on accumulating SIP volume. The biggest genuine movers:

**GXAI** — Packaged Software / AI-gaming (biggest AH→PM continuation, detected + traded)
- Catalyst: same-day GlobeNewswire PR ~16:10 ET — revenue/ad-efficiency operational update. **Grade C**
- Previous Close: $0.89
- AH last night: SIP peak **$1.58 (+77.5%)** at 17:15 ET (23:15 CET), on millions of sh/bar (20:15Z 3.02M sh/11.8k tr)
- Premarket now: ~$1.29–1.37 (SIP PM high $1.53 = +72%), faded from AH peak
- Hypothetical P&L (AH entry → PM peak): AH entry $1.42 → PM peak $1.53 = **+7.7%**; the AH peak $1.58 was the better exit
- Float: 10.5M | Market Cap: $9.4M
- **Sub-100%** → not a "winner," but the strongest AH→PM name and the one we entered.

**FRGT** — Freight Technologies (biggest raw PM mover, PM-only gapper)
- Previous Close: $2.57 | AH flat (SIP AH ~$2.50, few hundred sh/bar)
- PM explosion at 04:00 ET: SIP PM high **$4.77 (+85.6%)** on 1.28M sh / 20,832 trades at 08:05Z — real, liquid
- No verified fresh catalyst (strategic-alternatives story ongoing) → **Grade None**
- Float 563K. **PM-only gapper** (AH flat, move began only at 04:00 ET) — structurally undetectable by the AH scanner, NOT a detection miss.

**Scanner Diagnostic (GXAI):**
- Detectable at screening time? **YES**
- What it looked like: ignited 16:10 ET on the same-day PR, +28.7% AH at the 22:30 scan, built to +66.6% by 23:00 on 15.8M AH vol / VRatio 8.0x, real two-sided book. Textbook BUILD.
- We acted: **entered 64 GXAI @ $1.42 at 23:00 CET.** Right stock traded.
- Scanner gap: none. GXAI was caught and entered. It simply faded AH→PM (sub-100%, AH was the better exit).

### Baseline Tracking

- Days tracked: **65** (was 64 + 1)
- Winners detected by scanner: **52/61 (85.2%)** — GXAI detected and added.
- Winner selected for paper trade: **30/61 (49.2%)** — GXAI entered @ $1.42. Right stock traded.
- Target: >80% detection
- Status: **BASELINE MET** (85.2%)
- Baseline chain: 08-10 (63) → 08-11 (64) → 08-12 (65). Sequential, no gap.

### Retrospective Scan Results
Live PM scan (04:20 ET): GXAI +58%, FRGT +66%, CURI +31%, CPHI +21%, FRGT the biggest raw mover.
- GXAI AH SIP peak $1.58 (+77.5%) 17:15 ET → PM SIP $1.53 (+72%). AH→PM continuation, faded modestly.
- FRGT PM-only gapper +85.6% (AH flat). OFAL/BIVI faded in PM (OFAL $1.59→$1.37; BIVI $1.83→$1.60).
- No name >100%.

### Open Position P&L (Alpaca)

| Ticker | Entry | Entry Total% | Catalyst | Entry Time | PM Peak | Peak Time | Exit | P&L | P&L % | Status |
|--------|-------|--------------|----------|------------|---------|-----------|------|-----|-------|--------|
| GXAI | $1.42 | +59.6% | C — rev/ad-efficiency PR | 23:00 CET | $1.53 (SIP) | 04:00 ET | open | -€6.40 | -7.0% | Open |

GXAI Alpaca `current_price` $1.32 is roughly live (SIP PM $1.29–1.37), so the −7% is real, not a stale figure. Exit is handled by position-evaluation (10:30 CET), not here.

**Total Realized P&L (Alpaca fills only): €0.00** (no exits this pulse)

### Scanner Effectiveness

- Evening scans ran: **7 of 7** scheduled (21:30, 22:00, 22:30, 23:00, 23:30, 00:00, 00:30 CET) + 2 bonus (22:15, 22:45) = 9 total. Full coverage.
- Candidates found: GXAI, LGCL, CURI, OFAL, USIO, BIVI, HXHX, PRHI, FGI
- Retrospective matches: GXAI (entered), LGCL, CURI, OFAL all surfaced. No in-window mover missed.

### Missed Opportunities

No significant missed opportunities. FRGT (+85.6%) was a PM-only gapper (AH flat) — structural blind spot, not a detection miss.

### AH Mover Follow-Through

| Ticker | AH Peak | Peak Time | AH Trajectory | Current PM | From Peak | From Close | Verdict |
|--------|---------|-----------|---------------|------------|-----------|------------|---------|
| GXAI | $1.58 (+77.5%) | 17:15 ET | Build→hold | $1.29–1.37 | −13% | +45–54% | AH peak > PM peak (AH better exit) |
| LGCL | $2.17 (+52.8%) | 16:10 ET | Spike→fade | $1.36 | −37% | −4% | Faded further, correctly skipped |
| CURI | $3.98 (+42%) | 19:55 ET | Build (late) | $3.68 | −8% | +31% | Held most of gain, no book |
| OFAL | $1.60 (+124% total) | AH | Day-runner tail | $1.37 | −14% | +88% | Faded in PM, no book all night |

**AH-peak-vs-PM-peak check:** GXAI AH peak (+77.5%) > PM peak (+72%) — AH was the marginally better exit, consistent with the fade-into-PM tendency (though below the ~+130% extreme zone). LGCL AH peak (+52.8%) >> PM peak (~0%) — clean fade, fade rule correct.

### Notes

- **Coverage:** 7 of 7 scheduled scans ran. No coverage failure.
- **Fade-rule false-negative tracking:** LGCL (Aug 12→13, float **1.6M** sub-3M, Grade None, AH SIP peak $2.17 +52.8% @16:10 ET → PM SIP high $1.41 = **fell short**, PM well below AH peak). Correctly skipped. **Standing sub-3M count: 4 of 12** (LGCL added as fell-short). ≥4/5 (80%) trigger NOT met (33%). Hypothesis weakening further — do not wire the PM-open re-check exception.
- **PM-only gapper tracking:** biggest raw PM mover = FRGT +85.6% (SIP), classified **PM-only gapper** (AH flat, move began 04:00 ET), liquid at PM open (1.28M sh/20.8k trades). Not found in `log/pm-open-scan.csv` yet — flag for the pm-open pulse. Holdable PM-only-gapper count in the csv = **21** (cluster threshold already exceeded; standing action: route to Juan's daily email as Initiative-6 early-PM pilot decision). PM-only gapper is not a detection miss.
- **No ceiling-override or dead-cat-override watches** flagged last night.
- **No in-window feed-lag miss, no price-floor exclusion, no late-AH-tail surge, no reverse-split entry** this session. OFAL (1-for-10 reverse split ~Jul 27, weeks-old, no fresh catalyst) surfaced but was skipped all night on no fillable book (not entered) — not added to the reverse-split-entry tally (tracks entered names).
- **AH-fade pattern:** GXAI (the night's leader) topped in AH and faded into PM (+77.5% → +72%), the AH peak being the marginally better exit. Consistent with prior evidence that AH runners tend to peak before PM.

