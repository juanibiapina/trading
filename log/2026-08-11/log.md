
## Scan 21:30 CET (3:30 PM ET)

**Session: REGULAR** (AH opens 22:00 CET / 4:00 PM ET). Watch-only — no entries before AH confirmation.

Top regular-session movers (pending AH confirmation):

| Ticker | Chart | Price | Chg% | IRVol | Float | MCap | Industry |
|--------|-------|-------|------|-------|-------|------|----------|
| PLAG | [TV](https://www.tradingview.com/chart/?symbol=PLAG) | $5.00 | +783.9% | 696x | 11.6M | $8.1M | Food: Specialty/Candy |
| WXM | [TV](https://www.tradingview.com/chart/?symbol=WXM) | $8.84 | +120.9% | 405x | 577K | $4.5M | Wholesale Distributors |
| MSGY | [TV](https://www.tradingview.com/chart/?symbol=MSGY) | $3.59 | +55.0% | 242x | 6.5M | $39.2M | Engineering & Construction |
| STIM | [TV](https://www.tradingview.com/chart/?symbol=STIM) | $3.10 | +43.1% | 22x | 24.0M | $216.1M | Medical Specialties |
| FF | [TV](https://www.tradingview.com/chart/?symbol=FF) | $6.39 | +23.8% | 15x | 26.1M | $280.3M | Chemicals: Specialty (open position, Grade B) |
| DOMH | [TV](https://www.tradingview.com/chart/?symbol=DOMH) | $3.22 | +14.2% | 15x | 9.1M | $72.8M | Investment Banks/Brokers |

**Notes:**
- Scan ran at 15:30 ET (regular session), so all volume/change figures are intraday, not after-hours. AH liquidity and continuation unknown until the 22:00+ CET scans.
- PLAG (+783%), WXM (+120%), MSGY (+55%) are the standout small-float movers to watch for AH follow-through. Spike-bar / confirmation instrumentation and catalyst searches deferred to AH scans (spike detector keys off AH bars).
- FF is the existing Grade-B open position (Q2 earnings), managed by premarket position-evaluation, not re-entered here.
- No paper trades entered — regular-session caution rule. Re-evaluate at 22:00 CET (AH open).

## Scan 22:00 CET (4:00 PM ET)

**Session: AFTERHOURS.** `scan.py --all` ran at 16:00:14 ET (AH open) — **0 hits**. Postmarket volume has not accumulated yet at the open, so VRatio-based discovery returns nothing this early. Observation-only scan per learning phase (no entries before 23:00 CET).

Pipeline cross-check (21:30 regular-session watch names) via SIP/quote:

| Ticker | AH Book (quote) | SIP AH bars | Read |
|--------|-----------------|-------------|------|
| PLAG | bid $6.65 x1000 / **ask $0.00 x0** | none yet | No fillable ask; +783% regular spike, AH liquidity unconfirmed |
| WXM | bid $6.68 / ask $9.12 x100 | none yet | Two-sided but no AH prints yet |
| MSGY | bid $2.99 / ask $3.98 x100 | none yet | Two-sided but no AH prints yet |

**Notes:**
- No AH 5Min bars available for any pipeline name yet (feed sparse at the open). Nothing to instrument (no candidate with confirmed AH change >10%).
- PLAG shows `ask $0.00 x0` — no fillable book right now; watch whether a real two-sided AH market forms.
- No paper trades — observation-only (pre-23:00 CET) and scanner has no AH candidates. Re-scan at 22:30 / 23:00 CET.

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| WAFU | $1.94 | $2.10 | +8.2% | $2.60 | 1 | None | SELL | Grade None exit first PM at profit; filled $2.10 |
| MTEN | $1.39 | $1.35 | -2.9% | $1.55 | 1 | None | SELL | Grade None exit first PM; filled $1.35 |
| MGIH | $2.12 | $2.02 | -4.7% | $2.22 | 1 | None | SELL | Grade None exit first PM; filled $2.02 |
| FF | $6.28 | $6.07 | -3.3% | $6.45 | 1 | B | HOLD | Day 1, above -15% stop ($5.34), Q2 earnings catalyst intact |

**Actions taken:**
- SELL 43 WAFU @ $2.10 (id 3ee7b7e8), +$6.88 / +8.2%
- SELL 64 MTEN @ $1.35 (id c0ff8507), -$2.56 / -2.9%
- SELL 47 MGIH @ $2.02 (id c8a5fc8e), -$4.70 / -4.7%
- HOLD FF (Grade B, day 1). Trail not active (peak +2.7% below +30% threshold). Hard stop -15% = $5.34.
- Net on 3 sells: -$0.38. All filled with price improvement over limit.

**Data notes:** Alpaca IEX quotes were stale (prior-close, 20:xx UTC). Used SIP 5Min bars for fillable levels. price-timeline.py labels UTC as "ET"; PM bars 08:00-08:15 UTC = 04:00-04:15 ET premarket open.

## Position Evaluation — 14:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| FF | $6.28 | $6.20 | -1.3% | $6.45 (+2.7%) | 1 | B | HOLD | Day 1 of 2, above -15% stop ($5.34), no trail triggered (never hit +30%), earnings catalyst intact. PM flat $6.04-6.30, no momentum spike to sell into. |

**Actions taken:**
- None. FF held. Alpaca (source of truth) and OPEN_POSITIONS.md reconciled — FF only open position.
- Quote bid $6.19 was stale (yesterday 20:40Z); confirmed live PM ~$6.15-6.23 via SIP 5Min bars.

## Scan 22:15 CET (4:15 PM ET)

**Session: AFTERHOURS.** `scan.py --all` ran at 16:15 ET — **0 hits**. Observation-only (pre-23:00 CET).

Pipeline cross-check (21:30 watch names) via SIP AH bars + quote (quotes lag ~15 min on free tier):

| Ticker | Reg Close | AH C (SIP) | AH% | AH Vol / trades | Book (quote) | Read |
|--------|-----------|------------|-----|-----------------|--------------|------|
| PLAG | $5.00 | $4.30 | -14% | 2.0M / 22,106 | bid $6.65 / **ask $0.00 x0** | Spiked then faded ($6.03→$4.30 in first AH bar); no fillable ask. Skip. |
| WXM | $8.84 | $7.64 | -13.6% | 63K / 931 | bid $6.68 / ask $9.12 | Fading below close, two-sided but stale quote. No AH momentum. |
| MSGY | $3.59 | $3.46 | -3.6% | 31K / 212 | bid $2.99 / ask $3.98 | Flat-to-down, thin AH. No momentum. |
| STIM | $3.10 | — | — | — | **ask $0.00 x0** | No fillable AH book. |
| DOMH | $3.22 | — | — | — | **ask $0.00 x0** | No fillable AH book. |

**Notes:**
- Real AH volume now printing (first 5Min bar). Every pipeline name is FADING in AH (negative AH% vs regular close) — none reaches the +10% AH threshold. PLAG's huge +783% regular spike is unwinding (first AH bar $6.03→$4.30) with no fillable ask, classic illiquid spike→fade.
- No candidate with AH change >10%, so no spike-bar / third-bar-confirmation instrumentation this scan.
- No paper trades — observation-only (pre-23:00 CET) and no qualifying candidate. Re-scan at 22:30 / 23:00 CET.

## Scan 22:30 CET (4:30 PM ET)

**Session: AFTERHOURS.** `scan.py --all` ran at 16:30 ET — **4 hits**. Observation-only (pre-23:00 CET, learning phase). First scan with real AH candidates tonight.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| GTEC | [TV](https://www.tradingview.com/chart/?symbol=GTEC) | $0.55 | +2.7% | +28.3% | $0.71 | +31.8% | 7.2M | 836K | 8.6x | 14.1M | Industrial Machinery |
| SINT | [TV](https://www.tradingview.com/chart/?symbol=SINT) | $1.77 | +4.1% | +35.0% | $2.39 | +40.6% | 1.2M | 177K | 6.8x | 5.3M | Medical Specialties |
| DRMA | [TV](https://www.tradingview.com/chart/?symbol=DRMA) | $1.08 | -3.6% | +18.5% | $1.28 | +14.3% | 379K | 118K | 3.2x | 2.7M | Pharmaceuticals: Major |
| SND | [TV](https://www.tradingview.com/chart/?symbol=SND) | $4.65 | +1.3% | +9.7% | $5.10 | +11.1% | 87K | 302K | 0.3x | 30.2M | Construction Materials |

**Instrumentation (log-only, no decision impact):**
- GTEC `SPIKE 16:00ET +16% $0.64 79 trades / 14k sh` · `CONFIRM-3 NO no local-volume new-high ignition as-of 16:30ET`
- SINT `SPIKE 16:06ET +29% $2.29 48 trades / 8k sh` · `CONFIRM-3 NO ignition 16:05ET failed third-bar hold/volume as-of 16:30ET`
- DRMA `SPIKE 16:09ET +16% $1.25 97 trades / 22k sh` · `CONFIRM-3 YES ignition 16:05ET 215.0x; confirmed 16:15ET $1.46 as-of 16:30ET`

**SIP AH bars (20:00-20:20Z) + book:**
| Ticker | Trajectory | AH Vol/bar | Book (quote) | Read |
|--------|-----------|------------|--------------|------|
| GTEC | $0.55→$0.78 high (20:10), holding $0.69-0.71 | 1.7-3.2M sh, 5.5-11k trades | bid $0.55 / ask $0.72 x500 | Real heavy volume, BUILD-and-hold. Small- cap $14.7M, float 14.1M. Fillable book. |
| SINT | $1.80→$2.48 high (20:05), now $2.20-2.33 | 0.5-1.0M sh, 4.4-7.4k trades | bid $1.47 / ask $2.08 x100 | Real volume, spiked then holding near peak. Float 5.3M. Wide spread. |
| DRMA | $1.08→$1.52 high, rising each bar | 35k→1.4M sh, up to 8k trades | bid $1.42 / ask $1.44 x100 | Clean BUILD, tight ask spread, smallest float 2.7M. CONFIRM-3 YES. |
| SND | — | — | **ask $0.00 x0** | No fillable AH book; +9.7% below threshold. Skip. |

**Notes:**
- Three real, volume-backed AH candidates (GTEC, SINT, DRMA) — first live movers of the night. All accumulating on real SIP trades (not stale VRatio / bad prints); DRMA and GTEC show tight two-sided books, SINT wider.
- DRMA is the cleanest BUILD (rising each bar, tightest spread, smallest float, CONFIRM-3 YES). GTEC holding after a sharp spike on the heaviest volume. SINT spiked then holding near peak.
- No entries — observation-only per learning phase (pre-23:00 CET). All three need a 2nd AH scan appearance at 23:00+ CET to clear the entry gate. Re-scan and evaluate for entry at 23:00 CET.
- Prior pipeline names (PLAG, WXM, MSGY) all faded below close in AH (see 22:15 scan) — dropped.

## Scan 22:45 CET (4:45 PM ET)

**Session: AFTERHOURS.** `scan.py --all` ran at 16:45 ET — **7 hits**. Observation-only (pre-23:00 CET, learning phase). Candidates with AH change >10%: DRMA, CIGL, OWLT (SINT dropped to +9%, GTEC dropped off scanner).

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| DRMA | [TV](https://www.tradingview.com/chart/?symbol=DRMA) | $1.08 | -3.6% | +34.3% | $1.45 | +29.5% | 4.7M | 608K | 7.8x | 2.7M | Pharmaceuticals: Major |
| CIGL | [TV](https://www.tradingview.com/chart/?symbol=CIGL) | $0.60 | +32.5% | +33.7% | $0.80 | +77.1% | 2.1M | 17.5M | 0.1x | 35.0M | Misc Commercial Services |
| OWLT | [TV](https://www.tradingview.com/chart/?symbol=OWLT) | $5.44 | +0.4% | +20.4% | $6.55 | +20.8% | 79K | 136K | 0.6x | 15.7M | Electronics/Appliances |
| SINT | [TV](https://www.tradingview.com/chart/?symbol=SINT) | $1.77 | +4.1% | +9.0% | $1.93 | +13.4% | 2.5M | 311K | 7.9x | 5.3M | Medical Specialties |
| SMRT | [TV](https://www.tradingview.com/chart/?symbol=SMRT) | $1.41 | +3.7% | +5.9% | $1.49 | +9.8% | 104K | 1.8M | 0.1x | 175.0M | Computer Communications |
| EPOW | [TV](https://www.tradingview.com/chart/?symbol=EPOW) | $0.56 | +0.9% | +7.2% | $0.59 | +8.1% | 103K | 495K | 0.2x | 38.1M | Packaged Software |
| SND | [TV](https://www.tradingview.com/chart/?symbol=SND) | $4.65 | +1.3% | +7.5% | $5.00 | +8.9% | 90K | 302K | 0.3x | 30.2M | Construction Materials |

**Instrumentation (log-only, no decision impact):**
- DRMA `SPIKE 16:09ET +16% $1.25 97 trades / 22k sh` · `CONFIRM-3 YES ignition 16:05ET 215.0x; confirmed 16:15ET $1.46 as-of 16:45ET`
- CIGL `SPIKE 16:27ET +30% $0.78 1624 trades / 558k sh` · `CONFIRM-3 PENDING ignition 16:25ET; waiting for third bar as-of 16:45ET`
- OWLT `SPIKE 16:10ET +21% $6.60 68 trades / 9k sh` · `CONFIRM-3 NO ignition 16:10ET failed third-bar hold/volume as-of 16:45ET`
- SINT `SPIKE 16:06ET +29% $2.29 48 trades / 8k sh` · `CONFIRM-3 NO ignition 16:05ET failed third-bar hold/volume as-of 16:45ET`
- GTEC `SPIKE 16:00ET +16% $0.64 79 trades / 14k sh` · `CONFIRM-3 NO no local-volume new-high ignition as-of 16:45ET`

**SIP AH bars (20:00-20:30Z / 16:00-16:30 ET, ~15 min behind scan) + book:**
| Ticker | Trajectory | AH Vol/bar | Book (quote) | Read |
|--------|-----------|------------|--------------|------|
| DRMA | $1.08→$1.56, **rising each bar** (H $1.59) | 1.4-2.0M sh, 8-10k trades | **fresh** bid $1.63 / ask $1.67 (20:45Z) | Clean BUILD, tightest fresh book, smallest float 2.7M, CONFIRM-3 YES. Lead candidate. |
| CIGL | Reg +32.5% mover; AH spike 16:25 to $0.87 then C $0.70 | 2.0-2.7M sh late bars | stale bid $0.48 / ask $0.68 (20:00Z) | Late AH spike already fading off $0.87 high; large float 35M, MCap $135M. SPIKE→FADE forming. |
| OWLT | $5.44→$6.84, holding $6.5-6.8 | thin 5-36k sh, 100-500 trades | stale ask $6.67 (20:00Z) | Building/holding but **thin** AH volume; float 15.7M. |
| SINT | Spiked $2.48 @16:05, faded to $1.92-1.98 | 0.2-1.0M sh | stale bid $1.47 / ask $2.08 | -20%+ off AH high. SPIKE→FADE. |
| GTEC | Peaked $0.78 @16:10, collapsed to $0.56 | 1.1-3.1M sh, fading | fresh bid $0.55 / ask $0.64 | -27% off AH high. Fading hard. SPIKE→FADE. |

**Notes:**
- **DRMA is the clear lead:** only name showing a clean BUILD (rising every SIP bar $1.08→$1.56), heavy accumulating volume, a fresh tight two-sided book, smallest float (2.7M), and CONFIRM-3 YES. 2nd AH-scan appearance (22:30 +18.5% → 22:45 +34.3%, building). Total% ~+53% at quote $1.65 — under the +150% ceiling. Pharmaceuticals sector (no catalyst searched yet — will run at 23:00).
- SINT and GTEC (last scan's BUILD-and-hold candidates) both rolled into SPIKE→FADE — faded 20-27% off their AH highs. Dropped from lead consideration.
- CIGL is a regular-session runner (+32.5% day) that spiked late in AH and is already fading; stale quote, 35M float. OWLT holding but thin. SMRT/EPOW/SND below the 10% AH threshold.
- **No paper trades — observation-only per learning phase (pre-23:00 CET).** DRMA has now cleared the 2-AH-scan gate (22:30 + 22:45, both >10%, both building) and is the entry candidate for the 23:00 CET scan pending catalyst search and a still-live BUILD read. Re-scan and evaluate for entry at 23:00 CET.

## Scan 23:00 CET (5:00 PM ET)

**Session: AFTERHOURS.** `scan.py --all` ran at 17:00 ET — **5 hits**. **First entry-eligible scan** (23:00 CET+, learning phase). Candidates with AH change >10%: DRMA, OWLT, SND, GTEC.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| DRMA | [TV](https://www.tradingview.com/chart/?symbol=DRMA) | $1.08 | -3.6% | +49.0% | $1.61 | +43.7% | 9.9M | 1.2M | 8.4x | 2.7M | Pharmaceuticals: Major |
| OWLT | [TV](https://www.tradingview.com/chart/?symbol=OWLT) | $5.44 | +0.4% | +21.2% | $6.59 | +21.6% | 135K | 143K | 0.9x | 15.7M | Electronics/Appliances |
| GTEC | [TV](https://www.tradingview.com/chart/?symbol=GTEC) | $0.55 | +2.7% | +10.1% | $0.61 | +13.0% | 11.7M | 1.3M | 8.9x | 14.1M | Industrial Machinery |
| SND | [TV](https://www.tradingview.com/chart/?symbol=SND) | $4.65 | +1.3% | +10.8% | $5.15 | +12.2% | 93K | 302K | 0.3x | 30.2M | Construction Materials |
| LENZ | [TV](https://www.tradingview.com/chart/?symbol=LENZ) | $5.21 | -2.8% | +8.2% | $5.64 | +5.1% | 82K | 685K | 0.1x | 27.4M | Pharmaceuticals: Major |

**Instrumentation (log-only, no decision impact):**
- DRMA `SPIKE 16:09ET +16% $1.25 97 trades / 22k sh` · `CONFIRM-3 YES ignition 16:05ET 215.0x; confirmed 16:15ET $1.46 as-of 17:00ET`
- GTEC `SPIKE 16:00ET +16% $0.64 79 trades / 14k sh` · `CONFIRM-3 NO no local-volume new-high ignition as-of 17:00ET`
- OWLT `SPIKE 16:10ET +21% $6.60 68 trades / 9k sh` · `CONFIRM-3 NO ignition 16:10ET failed third-bar hold/volume as-of 17:00ET`
- SND `NO-SPIKE peak +11% @16:41ET` · `CONFIRM-3 NO no local-volume new-high ignition as-of 17:00ET`

**SIP AH bars (20:00-20:45Z / 16:00-16:45 ET) + book:**
| Ticker | Trajectory | AH Vol/bar | Book (quote) | Read |
|--------|-----------|------------|--------------|------|
| DRMA | $1.08→$1.72H (20:35Z), holding $1.60 | 1.1-2.3M sh, 6-12k trades | **fresh** bid $1.50 / ask $1.51 (20:59Z) | Clean BUILD, tight fresh book, smallest float 2.7M, VWAP rose $1.08→$1.64, CONFIRM-3 YES. **ENTRY.** |
| OWLT | $5.44→$6.84H (20:30Z), holding $6.5-6.6 | thin 5-38k sh, 86-525 trades, **fading** | stale bid $4.73 / ask $6.67 (20:00Z) | Earnings mover but AH vol thin + fading, VRatio 0.9x (below avg), CONFIRM-3 NO. Fails SIP volume-accumulation gate. Skip. |
| GTEC | Peaked $0.78 @16:10, rebuilt to ~$0.61 | 1-3M sh, choppy | fresh bid $0.55 / ask $0.64 | -22% off AH high, rebuild base >20% below high = faded spike (SKYQ rule). Skip. |
| SND | Peak +11% @16:41, thin | 5-90k sh | ask $0.00 x0 earlier | NO-SPIKE, only 1 AH scan >10% (fails 2-scan gate). Skip. |

**Catalyst searches:**
- **DRMA:** Q2 2026 earnings + corporate update released after close 08-11; announced launch date of first commercial product (Tome Foundational Treatment, expected Aug 25, 2026). GlobeNewswire/PR-Inside 08-11. **Grade B** (concrete operational/product-launch milestone + earnings).
- **OWLT:** Q2 2026 earnings released after close 08-11 (confirmed). Earnings catalyst present but candidate fails the AH-volume-accumulation gate (thin/fading, VRatio 0.9x) — not entered.

**Paper trade:**
- **DRMA — BUY 66 @ limit $1.54 ext → filled @ $1.52** (order id 66c1614c). Grade B. QTY = floor($100/$1.51)=66. Entry Total% +40.7% (under 150 ceiling). Rationale: only candidate clearing all gates — float 2.7M (<50M), AH >10% across 3 AH scans (22:30 +18.5% → 22:45 +34.3% → 23:00 +49%, building), Day% -3.6% (above -15%, not a dead-cat: never crashed), clean BUILD holding within 20% of $1.72 AH high, heavy accumulating SIP volume (1-2M sh/bar, 8-12k trades), fresh tight two-sided book, real (not bad print — SIP high $1.72 corroborates), CONFIRM-3 YES, catalyst Grade B. Added to OPEN_POSITIONS.md.
- **OWLT — Skip:** earnings catalyst but thin, non-accumulating AH volume (5-38k sh/bar, fading 36k→8k, VRatio 0.9x below average). Fails SIP volume-accumulation confirmation.
- **GTEC — Skip:** faded spike (rebuild base >20% below AH high, SKYQ rule), CONFIRM-3 NO.
- **SND — Skip:** NO-SPIKE, only 1 AH scan >10% (fails 2-AH-scan gate).
- **LENZ — Skip:** +8.2% AH, below 10% threshold.

**Notes:**
- One entry tonight: DRMA (Grade B, clean BUILD, smallest float, real volume). This is the textbook detect→select→BUILD profile the strategy targets. Set premarket exit for Grade B (hold up to 2 days, -15% stop $1.29, trail at -15% from peak if +30% reached).
- Prior BUILD candidates SINT and GTEC both rolled to SPIKE→FADE; DRMA is the only one that kept building into the entry scan.

## Scan 23:30 CET (5:30 PM ET)

**Session: AFTERHOURS.** `scan.py --all` ran at 17:30 ET — **12 hits**. Entry-eligible window. Candidates with AH change >10%: DRMA (held), BAOS, BOXL, PRSO, OFAL, NOMA, WAFU(+21% total but AH +5.7%).

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| DRMA | [TV](https://www.tradingview.com/chart/?symbol=DRMA) | $1.08 | -3.6% | +41.7% | $1.53 | +36.6% | 13.8M | 1.6M | 8.6x | 2.7M | Pharmaceuticals: Major |
| BAOS | [TV](https://www.tradingview.com/chart/?symbol=BAOS) | $0.73 | +3.2% | +26.2% | $0.92 | +30.1% | 6.3M | 1.9M | 3.2x | 1.0M | Advertising/Marketing Services |
| BOXL | [TV](https://www.tradingview.com/chart/?symbol=BOXL) | $2.93 | -1.3% | +32.9% | $3.90 | +31.1% | 96K | 45K | 2.1x | 564K | Computer Peripherals |
| PRSO | [TV](https://www.tradingview.com/chart/?symbol=PRSO) | $0.72 | +1.1% | +13.7% | $0.82 | +15.0% | 154K | 329K | 0.5x | 14.8M | Semiconductors |
| NOMA | [TV](https://www.tradingview.com/chart/?symbol=NOMA) | $2.73 | -13.3% | +20.9% | $3.30 | +4.8% | 2K | 7K | 0.3x | 5.6M | Movies/Entertainment |
| OFAL | [TV](https://www.tradingview.com/chart/?symbol=OFAL) | $0.71 | -10.5% | +10.8% | $0.79 | -0.9% | 288K | 1.2M | 0.2x | n/a | Engineering & Construction |

**Instrumentation (log-only, no decision impact):**
- DRMA `SPIKE 16:09ET +16% $1.25 97 trades / 22k sh` · `CONFIRM-3 YES ignition 16:05ET 215.0x; confirmed 16:15ET $1.46 as-of 17:30ET`
- BAOS `SPIKE 16:51ET +22% $0.89 229 trades / 169k sh` · `CONFIRM-3 YES ignition 16:50ET 1060.5x; confirmed 17:00ET $0.90 as-of 17:30ET`
- BOXL `SPIKE 17:13ET +26% $3.69 185 trades / 35k sh` · `CONFIRM-3 PENDING ignition 17:10ET; waiting for third bar as-of 17:30ET`
- PRSO `SPIKE 16:54ET +15% $0.83 45 trades / 21k sh` · `CONFIRM-3 NO ignition 16:50ET failed third-bar hold/volume as-of 17:30ET`
- NOMA `NO-SPIKE peak +34% @16:54ET` · `CONFIRM-3 NO no local-volume new-high ignition as-of 17:30ET`

**SIP AH bars (20:00-21:15Z / 16:00-17:15 ET) + book:**
| Ticker | Trajectory | AH Vol/bar | Book (quote) | Read |
|--------|-----------|------------|--------------|------|
| DRMA | Held ~$1.53 vs $1.72 AH high | sustained | (held position) | Still building/holding, within 20% of high. Position from 23:00, not re-entered. |
| BAOS | $0.73→$1.03H (20:55Z), faded to $0.80 (21:15Z, L $0.77) | 0.9-2.2M sh, 2.6-7.8k trades | bid $0.98 / ask $3.20 (bad-print ask) | Real heavy volume but -20% off AH high = SPIKE→FADE forming. Tiny 1.0M float. 1st AH scan. |
| BOXL | $2.93→$4.25H (21:10Z), holding $3.9-3.95 | 123k-527k sh, 1.6-8.6k trades | **ask $0.00 x0** (stale) | Late emerge (17:10 ET), small 564K float, real volume, holding. No fillable book. 1st AH scan. |
| PRSO | Peaked $0.83, faded | thin 21k sh | bid $0.72 / ask $1.04 | CONFIRM-3 NO. 1st AH scan. |
| NOMA | Spiked, only 2K AH vol | 2K sh total | bid $2.31 / ask $3.72 | Illiquid (7 trades), Day -13.3% dead-cat, NO-SPIKE. Skip. |
| OFAL | Total% -0.9% (below close) | thin | bid $0.57 / ask $0.82 | Below regular close, Day -10.5%. Not a real AH mover. Skip. |

**Paper trade:**
- **No new entries.** DRMA already entered at 23:00 (one entry per candidate/night); holding at +41.7% AH ($1.53), above entry $1.52.
- **BAOS, BOXL, PRSO, NOMA, OFAL — Skip (1st AH-scan appearance, fail 2-AH-scan gate).** All are first-time hits this scan; the gate requires AH >10% across ≥2 after-hours scans. None qualify yet.
  - BAOS (float 1.0M, CONFIRM-3 YES, real volume) and BOXL (float 564K, late build, real volume) are the two worth tracking — both small-float with genuine SIP accumulation. BAOS is already fading -20% off its AH high (SPIKE→FADE forming); BOXL just spiked at 17:10 ET with no fillable book yet. Re-evaluate both at 00:00 CET if they hold >10% AH for a 2nd scan.
  - PRSO CONFIRM-3 NO / thin. NOMA illiquid + dead-cat (Day -13.3%). OFAL below regular close.

**Notes:**
- One position tonight remains DRMA (entered 23:00, Grade B). No qualifying new entry this scan — all new >10% movers are first appearances.
- BAOS and BOXL are the names to watch for a 2nd-scan confirmation at 00:00 CET; both tiny float with real volume, but BAOS is fading and BOXL has no fillable AH book.

## Scan 00:00 CET (6:00 PM ET)

**Session: AFTERHOURS.** `scan.py --all` ran at 18:00 ET — **13 hits**. Entry-eligible window. Candidates with AH change >10%: DRMA (position), BOXL, BAOS (both 2nd AH scan), XHLD, PETZ, PRSO, OWLT, NOMA. **Final scheduled scan of the night.**

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| DRMA | [TV](https://www.tradingview.com/chart/?symbol=DRMA) | $1.08 | -3.6% | +53.7% | $1.66 | +48.2% | 16.3M | 1.9M | 8.6x | 2.7M | Pharmaceuticals: Major |
| BAOS | [TV](https://www.tradingview.com/chart/?symbol=BAOS) | $0.73 | +3.2% | +18.2% | $0.86 | +21.9% | 8.5M | 2.2M | 3.9x | 1.0M | Advertising/Marketing Services |
| BOXL | [TV](https://www.tradingview.com/chart/?symbol=BOXL) | $2.93 | -1.3% | +34.8% | $3.95 | +33.0% | 2.1M | 339K | 6.1x | 564K | Computer Peripherals |
| XHLD | [TV](https://www.tradingview.com/chart/?symbol=XHLD) | $3.57 | +14.8% | +19.6% | $4.27 | +37.3% | 520K | 14.5M | 0.0x | 7.8M | Misc Commercial Services |
| PETZ | [TV](https://www.tradingview.com/chart/?symbol=PETZ) | $1.54 | -8.9% | +16.9% | $1.80 | +6.5% | 372K | 101K | 3.7x | 6.8M | Food: Specialty/Candy |
| PRSO | [TV](https://www.tradingview.com/chart/?symbol=PRSO) | $0.72 | +1.1% | +11.4% | $0.80 | +12.7% | 176K | 331K | 0.5x | 14.8M | Semiconductors |
| OWLT | [TV](https://www.tradingview.com/chart/?symbol=OWLT) | $5.44 | +0.4% | +10.3% | $6.00 | +10.7% | 197K | 150K | 1.3x | 15.7M | Electronics/Appliances |
| NOMA | [TV](https://www.tradingview.com/chart/?symbol=NOMA) | $2.73 | -13.3% | +20.9% | $3.30 | +4.8% | 2K | 7K | 0.3x | 5.6M | Movies/Entertainment |

**Instrumentation (log-only, no decision impact):**
- BOXL `SPIKE 17:13ET +26% $3.69 185 trades / 35k sh` · `CONFIRM-3 YES ignition 17:10ET 191.4x; confirmed 17:20ET $4.10 as-of 18:00ET`
- BAOS `SPIKE 16:51ET +22% $0.89 229 trades / 169k sh` · `CONFIRM-3 YES ignition 16:50ET 1060.5x; confirmed 17:00ET $0.90 as-of 18:00ET`
- PRSO `SPIKE 16:54ET +15% $0.83 45 trades / 21k sh` · `CONFIRM-3 NO ignition 16:50ET failed third-bar hold/volume as-of 18:00ET`
- XHLD `SPIKE 17:32ET +22% $4.34 843 trades / 71k sh` · `CONFIRM-3 NO ignition 17:25ET failed third-bar hold/volume as-of 18:00ET`
- PETZ `SPIKE 16:56ET +17% $1.80 24 trades / 4k sh` · `CONFIRM-3 NO ignition 17:00ET failed third-bar hold/volume as-of 18:00ET`

**SIP AH bars (20:00-21:45Z / 16:00-17:45 ET, ~15 min behind scan) + book:**
| Ticker | Trajectory | AH Vol/bar | Book (quote) | Read |
|--------|-----------|------------|--------------|------|
| DRMA | Held/rebuilt to $1.75H (21:35Z) vs $1.72 prior high | 200K-1M sh, sustained | (held position) | Still building/holding, new AH high. Position from 23:00, not re-entered. |
| BOXL | Ignited 17:10 ET → $4.77H @17:30 ET, holding $4.11 (17:45 ET) | 100-680K sh, 1.5-11k trades | stale ask $0.00 @16:00Z (predates 17:10 ignition = freshness artifact) | Real heavy volume BUILD, holding within 14% of high, tiny 564K float, CONFIRM-3 YES. **ENTRY.** |
| BAOS | Peaked $1.03 @17:00 ET, faded to $0.79, rebuilt to $0.98 near-high (17:45 ET) | 200K-2.2M sh, up to 7.8k trades | stale bid $0.98/ask $3.20 @16:59Z | V-recovery to within 5% of high on 1.1M-sh bar, tiny 1.0M float, CONFIRM-3 YES. **ENTRY.** |
| PRSO | Peaked $0.83, thin, now $0.79 | mostly <30K sh/bar | bid $0.72/ask $1.04 | CONFIRM-3 NO, fails volume-accumulation gate. Skip. |
| XHLD | Reg +14.8% mover; AH spike 17:25 to $4.34 then faded $3.77 | 130-200K sh spike bars | bid $3.02/ask $4.04 | 1st AH scan (fails 2-scan gate), CONFIRM-3 NO, fading off spike. Skip. |
| PETZ | Thin spike (24 trades/4k sh) | tiny | bid $1.16/ask $1.87 | 1st AH scan, thin, Day -8.9%, CONFIRM-3 NO. Skip. |
| OWLT | Thin/fading (carried) | thin 5-38K sh | stale | Earnings mover but thin non-accumulating vol, fails volume gate all night. Skip (carried). |
| NOMA | 2K AH vol total | illiquid | — | Illiquid + Day -13.3% dead-cat. Skip (carried). |

**Catalyst searches:**
- **BOXL:** structured search found no confirmed same-day catalyst. Q2 2026 earnings fall in the report window (analysts expected the quarter) but a same-day release was not confirmed; the 17:10 ET ignition on heavy volume is consistent with a delayed earnings/PR drop. Recorded as **no catalyst found → Grade None** (enter-with-concern, learning phase).
- **BAOS:** structured search (Yahoo/StockTitan/GlobeNewswire/Nasdaq PR) found no same-day catalyst. **No catalyst found → Grade None.**

**Paper trades (2 entries):**
- **BOXL — BUY 24 @ limit $4.30 ext → filled @ $4.01** (order id 4f304cb5). Grade None. QTY = floor($100/$4.11)=24. Entry Total% +36.9% (under 150 ceiling). Clears all gates: float 564K (<50M), AH >10% across 2 AH scans (23:30 +32.9% → 00:00 +34.8%), Day% -1.3% (above -15%, not dead-cat), holding within 14% of $4.77 AH high, real accumulating SIP volume (100-680K sh/bar, up to 11k trades), CONFIRM-3 YES, real (not bad print — SIP corroborates). Stale ask $0.00 @16:00Z was a freshness artifact (predates the 17:10 ET ignition) — order filled with price improvement, confirming real liquidity. Added to OPEN_POSITIONS.md.
- **BAOS — BUY 102 @ limit $1.03 ext → filled @ $0.90** (order id 4a36133c). Grade None. QTY = floor($100/$0.98)=102. Entry Total% +23.3% (under ceiling). Clears all gates: float 1.0M, AH >10% across 2 AH scans (23:30 +26.2% → 00:00 +18.2%), Day% +3.2%, V-recovery to within 5% of $1.03 AH high on a 1.1M-sh bar, real accumulating SIP volume, CONFIRM-3 YES. Filled with price improvement (real liquidity). Added to OPEN_POSITIONS.md.
- **PRSO — Skip:** CONFIRM-3 NO, thin AH volume (<30K sh/bar), fails volume-accumulation gate.
- **XHLD — Skip:** 1st AH scan (fails 2-scan gate), CONFIRM-3 NO, fading off 17:25 ET spike.
- **PETZ — Skip:** 1st AH scan, thin (24 trades), Day -8.9%, CONFIRM-3 NO.
- **OWLT — Skip (carried):** thin non-accumulating AH volume all night, fails SIP volume gate.
- **NOMA — Skip (carried):** illiquid (2K AH vol), Day -13.3% dead-cat.

**Notes:**
- Two entries tonight at the final scan: BOXL and BAOS (both Grade None, ultra-low float, real accumulating SIP volume, CONFIRM-3 YES, both cleared the 2-AH-scan gate at 00:00). Multiple-positions policy (W24) applied — both qualifying candidates entered independently.
- Open positions now: DRMA (Grade B, from 23:00, building to new AH high $1.75), BOXL, BAOS (both Grade None), plus FF (Grade B, day 1). Grade None names exit at first PM opportunity; premarket position-evaluation handles exits.
- BAOS and BOXL had faded/no-book reads at 23:30 but both firmed into 00:00: BAOS rebuilt to near-high, BOXL held within 14% of high on heavy volume. The stale zero-book quotes were confirmed as freshness artifacts by real filled orders (price improvement on both).
- No feed-lag rescue needed — all tracked pipeline names accounted for; PLAG/WXM/MSGY faded out earlier and stayed dead.

## Scan 00:30 CET (6:30 PM ET)

**Session: AFTERHOURS.** `scan.py --all` ran at 18:30 ET — **12 hits**. **Last scheduled scan of the night** (final-scan feed-lag cross-check applied). Candidates with AH change >10%: DRMA (position), BOXL (position), BAOS (position), XHLD, PETZ, OFAL, SND, NOMA.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| DRMA | [TV](https://www.tradingview.com/chart/?symbol=DRMA) | $1.08 | -3.6% | +54.3% | $1.67 | +48.7% | 18.3M | 2.1M | 8.7x | 2.7M | Pharmaceuticals: Major |
| BAOS | [TV](https://www.tradingview.com/chart/?symbol=BAOS) | $0.73 | +3.2% | +30.2% | $0.95 | +34.3% | 10.8M | 2.4M | 4.5x | 1.0M | Advertising/Marketing Services |
| BOXL | [TV](https://www.tradingview.com/chart/?symbol=BOXL) | $2.93 | -1.3% | +51.9% | $4.45 | +49.8% | 2.7M | 430K | 6.2x | 564K | Computer Peripherals |
| XHLD | [TV](https://www.tradingview.com/chart/?symbol=XHLD) | $3.57 | +14.8% | +15.7% | $4.13 | +32.8% | 761K | 14.6M | 0.1x | 7.8M | Misc Commercial Services |
| PETZ | [TV](https://www.tradingview.com/chart/?symbol=PETZ) | $1.54 | -8.9% | +12.3% | $1.73 | +2.4% | 374K | 101K | 3.7x | 6.8M | Food: Specialty/Candy |
| OFAL | [TV](https://www.tradingview.com/chart/?symbol=OFAL) | $0.71 | -10.5% | +12.1% | $0.80 | +0.3% | 359K | 1.2M | 0.3x | n/a | Engineering & Construction |
| SND | [TV](https://www.tradingview.com/chart/?symbol=SND) | $4.65 | +1.3% | +10.8% | $5.15 | +12.2% | 94K | 303K | 0.3x | 30.2M | Construction Materials |
| NOMA | [TV](https://www.tradingview.com/chart/?symbol=NOMA) | $2.73 | -13.3% | +20.9% | $3.30 | +4.8% | 2K | 7K | 0.3x | 5.6M | Movies/Entertainment |

**Instrumentation (log-only, no decision impact):**
- XHLD `SPIKE 17:32ET +22% $4.34 843 trades / 71k sh` · `CONFIRM-3 NO ignition 17:25ET failed third-bar hold/volume as-of 18:30ET`
- PETZ `SPIKE 16:56ET +17% $1.80 24 trades / 4k sh` · `CONFIRM-3 NO ignition 17:00ET failed third-bar hold/volume as-of 18:30ET`
- OFAL `SPIKE 16:52ET +20% $0.85 149 trades / 68k sh` · `CONFIRM-3 NO ignition 16:50ET failed third-bar hold/volume as-of 18:30ET`
- SND `NO-SPIKE peak +11% @16:41ET` · `CONFIRM-3 NO no local-volume new-high ignition as-of 18:30ET`
- NOMA `NO-SPIKE peak +34% @16:54ET` · `CONFIRM-3 NO no local-volume new-high ignition as-of 18:30ET`

**SIP AH bars + book (final-scan cross-check):**
| Ticker | Trajectory (SIP) | AH Vol/bar | Book (quote) | Read |
|--------|-----------|------------|--------------|------|
| DRMA | Held/building, AH high $1.75, quote $1.50/$1.51 | sustained 1-2M sh | **fresh** bid $1.50 / ask $1.51 (20:59Z) | Position from 23:00, still holding within 20% of high. Not re-entered. |
| BAOS | Rebuilt near AH high $1.03; quote bid $0.98 | 0.9-2.2M sh | bid $0.98 / ask $3.20 (bad-print ask) | Position from 00:00. Not re-entered. |
| BOXL | Ignited 17:10 ET → $4.77 high, holding; scanner AH $4.45 | 100-680K sh | stale ask $0.00 @20:00Z (predates ignition) | Position from 00:00. Not re-entered. |
| XHLD | Spike 17:25 ET → $4.34 high @17:30, faded to $3.77 (17:35 ET) | 133K/200K spike bars, then thinning | bid $3.02 / ask $4.04 (stale 20:00Z) | 2nd AH scan (00:00 +19.6% → 00:30 +15.7%, fading both), peaked 17:30 ET then declining, CONFIRM-3 NO. SPIKE→FADE. Skip. |
| PETZ | Spike 17:00 ET → $2.25 high, faded hard to $1.72-1.74 (18:15 ET) | 88K-224K spike then <30K | bid $1.16 / ask $1.87 | -23% off AH high, Day -8.9%, CONFIRM-3 NO. SPIKE→FADE. Skip. |
| OFAL | Spike 16:50 ET → $0.85 high, faded to $0.77 base (18:00 ET) | 138K spike then thinning | bid $0.57 / ask $0.82 | Total% +0.3% (at/below prior close), Day -10.5%, faded off high, CONFIRM-3 NO. Skip. |
| SND | NO-SPIKE, peak +11% @16:41, thin | 5-94K sh | **ask $0.00 x0** | No fillable book, NO-SPIKE. Skip. |
| NOMA | 2K AH vol total, illiquid | 2K sh | bid $2.31 / ask $3.72 | Illiquid (7 trades), Day -13.3% dead-cat. Skip (carried). |

**Paper trades:**
- **No new entries.** All three qualifying AH movers tonight (DRMA, BAOS, BOXL) are already open positions and are not re-entered (one entry per candidate per night).
- **XHLD — Skip:** SPIKE→FADE (peaked $4.34 @17:30 ET, faded to $3.77), fading across both AH scans (00:00 +19.6% → 00:30 +15.7%), CONFIRM-3 NO. Early-peak fade, 0/x for PM continuation.
- **PETZ — Skip:** SPIKE→FADE (-23% off $2.25 high), Day -8.9%, thin trailing volume, CONFIRM-3 NO.
- **OFAL — Skip:** Total% +0.3% (at/below prior close), Day -10.5%, faded off $0.85 high, CONFIRM-3 NO.
- **SND — Skip:** NO-SPIKE, no fillable AH book (ask $0.00 x0).
- **NOMA — Skip (carried):** illiquid (2K AH vol / 7 trades), Day -13.3% dead-cat.

**Final-scan feed-lag cross-check:** All tracked pipeline names accounted for. No name under-reported by TradingView while surging on SIP — XHLD is the only new regular-session runner and SIP confirms it faded (spike→fade), not an under-reported live surge. Earlier pipeline names (PLAG, WXM, MSGY, SINT, GTEC, CIGL) faded out in prior scans and stayed dead. No SIP-truth rescue needed.

**Notes:**
- No new entries at the final scan. Three positions entered earlier tonight remain: DRMA (Grade B, 23:00), BOXL + BAOS (Grade None, 00:00), plus FF (Grade B, day 1).
- Current paper P&L (Alpaca): BAOS +56.4%, DRMA +6.6%, BOXL +5.2%, FF +1.4% — all green at last mark. Premarket position-evaluation handles exits (Grade None names exit at first PM opportunity; DRMA/FF Grade B hold up to 2 days).
- Night summary: DRMA/BAOS/BOXL were the clean BUILD + real-SIP-volume candidates that cleared all gates; the rest of the field (XHLD, PETZ, OFAL, SND, NOMA, SINT, GTEC, CIGL, PLAG, WXM, MSGY) was SPIKE→FADE, thin, illiquid, or dead-cat.

## Morning Evaluation — 10:20 CET

### Today's Winner

**BAOS** — Baosheng Media Group (China online-marketing ADR)
- Catalyst: Blockchain/crypto business pivot — "Hires Project Lead and Purchases 1,000 Mining Machines to start blockchain & cryptocurrency business" (8-11 6-K) + a share subscription agreement (financing). Classic low-float China-ADR crypto-pivot pump. **Grade D** (financing/dilution + narrative pivot, no organic operational catalyst).
- Previous Close: $0.73 (Yahoo $0.71)
- AH last night: SIP peak **$1.97** (+170%) at 23:40 CET (19:40 ET), on 1.6M sh / 5,715 trades in the peak bar — heavy accumulating SIP volume all evening (0.9-2.7M sh/bar, 3-11k trades)
- Premarket now: ~$2.07 (+184%); SIP PM peak **$2.18** at 08:05Z (04:05 ET) on 1.7M sh / 12,513 trades, Yahoo peak $2.19 @ 08:15 ET
- Hypothetical P&L (AH entry → PM peak): entered $0.90 → PM peak $2.19 = **+143%** (real fill, see position table)
- Float: 1.0M | Market Cap: $1.1M
- **Clears the winner bar:** >100% (peaked ~+200%) on high, accumulating SIP volume (20,862 trades in the first PM bar). Real explosion, not a thin ramp.

**Scanner Diagnostic:**
- Detectable at screening time? **YES**
- At the nominal 22:15 CET screen (16:15 ET) BAOS was flat — the move ignited at 16:50 ET (22:50 CET) with a 901K-sh bar. It surfaced on the 17:30 ET scan (1st AH scan, +26.2%) and the 18:00 ET final scan (2nd AH scan, +18.2%), cleared the 2-AH-scan gate, and **we entered it at $0.90 at the 00:00 CET final scan** (Grade None, ultra-low 1.0M float, real accumulating SIP volume, CONFIRM-3 YES).
- Scanner gap: none. This is a textbook detect→select→run. The scanner caught it and we hold it at +123%. The only nuance: at 23:30 CET BAOS briefly read SPIKE→FADE (-20% off its AH high) and was correctly deferred; it firmed into the 00:00 scan and qualified. The 2-AH-scan gate delayed entry from ~$1.03 to $0.90 (better price via the fade), no cost.

### Baseline Tracking

- Days tracked: **64** (was 63 + 1)
- Winners detected by scanner: **51/60 (85.0%)** — BAOS detected and added.
- Winner selected for paper trade: **29/60 (48.3%)** — BAOS entered @ $0.90. Right stock traded.
- Target: >80% detection
- Status: **BASELINE MET** (85.0%)

No baseline gap: prior baseline log (08-10, Days tracked 63) is the immediately-preceding trading day.

### Retrospective Scan Results

- Live PM scan (`scan.py --all --session premarket`, 04:20 ET): 4 hits — BAOS +183.8%, BOXL +88.4%, DRMA +32.4%, MXCT +14.5%. BAOS and BOXL are last night's entries continuing; DRMA is last night's Grade-B entry, faded.
- AH reconstruction (`check-prices.py --ah-history` + SIP bars) confirms BAOS built cleanly through the AH on heavy accumulating volume, PM SIP peak $2.18 exceeds the AH SIP peak $1.97 → genuine continuation.

### Open Position P&L (Alpaca)

Real Alpaca fills. Alpaca per-symbol `quote` timestamps are stale (20:59 ET prior close); positions `current_price` read live PM and match the SIP/PM tape, so P&L is reported against those live marks. FF's mark ($6.28 = entry, bid $6.07) looks stale — flagged.

| Ticker | Entry | Entry Total% | Catalyst | Entry Time | PM Peak | Peak Time | Exit | P&L | P&L % | Status |
|--------|-------|--------------|----------|------------|---------|-----------|------|-----|-------|--------|
| BAOS | $0.90 | +23.3% | D — crypto pivot + financing | 00:00 CET | $2.19 | 04:15 ET | open | +€113.21 | +123.3% | ✅ Open win |
| BOXL | $4.01 | +36.9% | None | 00:00 CET | $5.99 | 04:00 ET | open | +€42.48 | +44.1% | ✅ Open win |
| DRMA | $1.52 | +40.7% | B — earnings + product launch | 23:00 CET | $1.59 | 04:00 ET | open | −€4.69 | −4.7% | 🔻 Open (faded) |
| FF | $6.28 | — | B — Q2 earnings | prior day | $6.45 | — | open | +€0.00 | +0.0%* | ⏸ Open (day 2, mark stale) |

*FF mark likely stale (prior 20:59 ET close). Exits handled by position-evaluation (10:30 / 14:30 CET), not here.

**Total Realized P&L (Alpaca fills only): €0.00** (no exits this pulse).

### Scanner Effectiveness

- Evening scans ran: **7 of 7** scheduled (21:30, 22:00, 22:30, 23:00, 23:30, 00:00, 00:30 CET) — plus 2 extra (22:15, 22:45). Full coverage.
- Candidates found: DRMA, BAOS, BOXL cleared all gates and were entered; wide field of SPIKE→FADE/thin/dead-cat names skipped.
- Retrospective matches: winner (BAOS) and both other real movers (BOXL, DRMA) all caught. 3/3.

### Missed Opportunities

No significant missed opportunities. The three real volume-backed AH movers (BAOS, BOXL, DRMA) were all detected and entered.

### AH Mover Follow-Through

| Ticker | AH Peak | Peak Time | AH Trajectory | Current PM | From Peak | From Close | Verdict |
|--------|---------|-----------|---------------|------------|-----------|------------|---------|
| BAOS | $1.97 (+170%) | 19:40 ET | Build | $2.07 | +5% | +184% | PM > AH — continuation ✅ |
| BOXL | $4.77 (+63%) | 17:10 ET | Spike→hold→build | $5.52 | +16% | +88% | PM > AH — continuation ✅ |
| DRMA | $1.75 (+62%) | 21:35 ET | Build | $1.45 | −17% | +32% | PM < AH — AH was better exit ⚠️ |

**AH-peak-vs-PM-peak check:** BAOS and BOXL both extended in PM above their AH peaks (continuation). DRMA topped in AH ($1.75) and PM fell short ($1.59), so the AH was the better exit — but DRMA never hit an extreme (+62% AH), so it's outside the ~+130%+ fade cluster (MSW/DSY/AQB). No new extreme-runner fade data point.

### Notes

- **Clean detect→select→run night.** All three volume-backed AH movers were caught and entered; the winner (BAOS) is a +123% open position. No scanner miss, no feed-lag miss, no broker block, no stale-book block. Nothing to escalate on detection this pulse.
- **PM-only gapper tracking:** morning's biggest raw PM mover is BAOS (+184%), an **AH→PM continuation** (moved >10% AH, scanner-detectable) — NOT a PM-only gapper. No new gapper case. `log/pm-open-scan.csv` holdable count stands at 20 (cluster already exceeds the ≥3-4 threshold; Initiative-6 early-PM pilot remains routed to Juan's email, not applied here).
- **Reverse-split tracking:** no entry tonight has a reverse-split catalyst (DRMA earnings, BOXL none, BAOS crypto-pivot/financing). No new case. This-week-split bucket stays 3/3 fade; awaiting the next this-week reverse split to resolve the recency signal.
- **Standing escalation tallies unchanged:** in-window feed-lag misses 4 (≥3 trigger REACHED — AH-data-source cross-check still routed to Juan's email); price-floor exclusions 5 across 2 nights, 0 holdable; stale-book execution-blocks 3. No additions this pulse.
- **Grade-vs-outcome note:** the +123% winner (BAOS) is Grade D and the +44% BOXL is Grade None, while the Grade-B DRMA faded −5%. Consistent with the learning-phase finding that trajectory/float/real-volume, not catalyst grade, drive PM follow-through on these ultra-low-float names.

### Price Charts

```
BAOS — Previous Close $0.71 | 2-Day Range $0.62-$2.19 | Current $2.07 (+193%)
Peak $2.19 (+210%) at 08-12 08:15 ET
AH build: 16:50 ET ignition $0.89 → 19:40 ET SIP peak $1.97 → PM 04:15 ET peak $2.19
Trajectory: clean multi-hour BUILD, PM extended above AH peak (continuation).

BOXL — Previous Close $2.93 | Current $5.52 (+88%)
AH: 17:10 ET ignition → $4.77 high, held → PM SIP peak $5.99 (+104%) at 04:00 ET (1.24M sh/22k trades)
Trajectory: spike→hold→PM continuation above AH peak.

DRMA — Previous Close $1.08 | Current $1.45 (+32%)
AH: BUILD $1.08→$1.75 high (21:35 ET) → PM SIP high $1.59, faded to $1.45
Trajectory: AH BUILD topped, PM fell short of AH peak (AH was better exit).
```
