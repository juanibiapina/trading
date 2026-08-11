
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
