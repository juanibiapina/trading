## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| BIYA | $1.91 | $2.44 | +27.8% | $2.86 (+49.7%) | 1 | None | SELL | Grade None exit at first PM opportunity at any profit. Filled $2.41 (+26.2%). |
| MTEN | $1.39 | $1.48 | +6.5% | $1.79 (+28.8%) | 1 | B | HOLD | Day 1 of 2. Peak +28.8% is under the +30% trail trigger ($1.81). Hard stop $1.18 not hit. Catalyst intact (MTEN is the acquirer in a completed $15M cash acquisition, so the fixed-price buyout re-grade does not apply). |

**Actions taken:**

- SELL BIYA 52 @ limit $2.25 ext (id 12241ef6) filled @ $2.41. +$26.00 (+26.2%). The 08:10Z PM spike to $2.86 was a single heavy bar (4.2M sh, vwap $2.31); the book settled $2.17–2.24 by 08:15Z, and the fill came in above that on the Alpaca mark.
- MTEN held. No order placed. If a new SIP peak clears $1.81 (+30%), set trail at peak × 0.85. Time-limit exit at the 2026-10-08 PM pulse.

**Data notes:** IEX quotes for both names were stale (prior-day 20:46–20:54Z timestamps, BIYA bid $1.88, MTEN bid $1.00), and IEX returned no PM bars. Levels come from SIP 5Min bars (latest complete bar 08:15Z) and the Alpaca position mark. Both books were liquid at the PM open: BIYA 6.5K–29.5K trades per bar, MTEN 2.5K–18.5K. MTEN printed a spike and fade: $1.79 at 08:05Z, then $1.38 by 08:15Z on 1.0M shares. That fade is the risk for the 14:30 pulse.

## Position Evaluation — 14:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| MTEN | $1.39 | $1.32 mark / $1.20 bid | -5.0% mark, -13.7% bid | $1.79 (+28.8%) | 1 | B | SELL | Hard stop $1.18 (-15%) breached on SIP: low $1.12 at 11:30Z, 5Min closes $1.15–1.20 from 11:30Z to 12:15Z. Pulse-time bounce was fading. Filled $1.21 (-12.9%). |

**Actions taken:**

- SELL MTEN 70 @ limit $1.16 ext (id ad6671de) filled @ $1.21 at 12:31Z. -$12.60 (-12.9%). No open positions remain.

**Why sell above the stop line:** The Alpaca mark ($1.32) sat above the stop, but the verified SIP tape spent 45 minutes at or below $1.18 before the pulse (11:30Z bar L $1.12 / C $1.15 on 661K sh, 1987 trades). The mark came from a 12:21Z spike on IEX ($1.20 → $1.60 → $1.02 within two minutes, 181 trades) with no new SEC filing (EDGAR shows only the 10-06 6-K). The live bid fell from $1.29 to $1.20 in 36 seconds during the pulse. Stops do not execute in extended hours, so the pulse is the stop; holding to the 10-08 time limit would have meant carrying a breached Grade B stop through a regular session.

**Data notes:** The SIP 5Min feed lagged about 15 minutes (latest bar 12:15Z at 12:30Z), so the 12:20Z+ bars came from IEX 1Min. The Alpaca quote was live this pulse (12:30Z timestamps, 700 x 700). The PM shape: open spike to $1.79 (08:05Z), $1.41–1.55 range through 10:50Z, then a heavy break at 10:55–11:00Z (864K + 997K sh) to $1.20–1.27 and a second leg to $1.12 at 11:30Z. Yahoo's timeline matched the SIP shape.

# Post-Market Screening - 2026-10-07

## Scan 21:30 CEST (3:30 PM ET)

**Decision:** Watch — pending AH confirmation. No paper orders submitted; this scan precedes the 16:00 ET AH open and the 23:00 CEST entry window.

`python3 scripts/scan.py --all` ran at 15:30:20 ET (21:30:20 CEST) in the REGULAR session and returned 35 hits. The US trading date is 2026-10-07. Regular-session appearances add zero qualifying AH scans. AH change, AH volume, and AH VRatio are not available yet, so the scanner printed no `Supplementary AH-change-only` or `AH >10% at this snapshot (unrounded)` line.

| Ticker | Chart | Price | Day% | 5mVol | Avg5m | IRVol | VChg% | Float | Industry |
|--------|-------|-------|------|-------|-------|-------|-------|-------|----------|
| IRIX | [TV](https://www.tradingview.com/chart/?symbol=IRIX) | $0.78 | +14.7% | 9K | 33K | 379.6 | -75.6% | 10.9M | Medical Specialties |
| SXTC | [TV](https://www.tradingview.com/chart/?symbol=SXTC) | $4.12 | +229.6% | 774K | 914K | 214.5 | +4.0% | 1.0M | Pharmaceuticals: Major |
| NXTS | [TV](https://www.tradingview.com/chart/?symbol=NXTS) | $1.05 | -24.5% | 8K | 14K | 56.7 | +50.2% | 1.1M | Household/Personal Care |
| NXAT | [TV](https://www.tradingview.com/chart/?symbol=NXAT) | $0.68 | -9.2% | 13K | 14K | 53.9 | +158.1% | 2.0M | Financial Conglomerates |
| ENSIF | [TV](https://www.tradingview.com/chart/?symbol=ENSIF) | $1.25 | +8.6% | 10K | 14K | 48.8 | -84.2% | 60.9M | Semiconductors |
| EVOL | [TV](https://www.tradingview.com/chart/?symbol=EVOL) | $0.60 | +0.0% | 11K | 1K | 40.9 | +3564.0% | 3.7M | Information Technology Services |
| QNCRF | [TV](https://www.tradingview.com/chart/?symbol=QNCRF) | $1.22 | -14.1% | 7K | 3K | 39.9 | +43.9% | 28.3M | Semiconductors |
| XSLL | [TV](https://www.tradingview.com/chart/?symbol=XSLL) | $10.00 | -0.1% | 129K | 69K | 25.1 | +0.9% | 20.9M | Financial Conglomerates |
| VCIG | [TV](https://www.tradingview.com/chart/?symbol=VCIG) | $0.78 | -44.6% | 15K | 22K | 22.1 | +40.9% | 1.0M | Miscellaneous Commercial Services |
| APMC | [TV](https://www.tradingview.com/chart/?symbol=APMC) | $9.97 | +0.1% | 25K | 12K | 21.1 | +0.1% | 16.0M | Financial Conglomerates |
| AMEGF | [TV](https://www.tradingview.com/chart/?symbol=AMEGF) | $0.72 | -2.8% | 24K | 6K | 19.1 | +75.4% | 121.4M | Precious Metals |
| ENAFF | [TV](https://www.tradingview.com/chart/?symbol=ENAFF) | $7.00 | +7.7% | 8K | 2K | 11.0 | +7620.0% | 8.3M | Semiconductors |
| KHDHF | [TV](https://www.tradingview.com/chart/?symbol=KHDHF) | $2.33 | +3.6% | 8K | 1K | 10.9 | +866.3% | 5.5M | Construction Materials |
| THEO | [TV](https://www.tradingview.com/chart/?symbol=THEO) | $9.90 | +0.0% | 40K | 16K | 10.5 | -20.0% | 14.0M | Financial Conglomerates |
| PFAI | [TV](https://www.tradingview.com/chart/?symbol=PFAI) | $5.16 | +120.5% | 101 | 561K | 13267.1 | -100.0% | 3.6M | Trucks/Construction/Farm Machinery |
| SBFM | [TV](https://www.tradingview.com/chart/?symbol=SBFM) | $0.77 | +92.8% | 179 | 893K | 440.4 | -100.0% | 4.2M | Pharmaceuticals: Major |
| BIYA | [TV](https://www.tradingview.com/chart/?symbol=BIYA) | $2.17 | +59.0% | 150 | 151K | 52.5 | -99.9% | 2.7M | Personnel Services |
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $1.57 | +44.0% | 116K | 423K | 1.0 | -23.5% | 4.4M | Miscellaneous Commercial Services |
| CPHI | [TV](https://www.tradingview.com/chart/?symbol=CPHI) | $0.86 | +34.0% | 600 | 1.1M | 160.6 | -99.9% | 40.3M | Pharmaceuticals: Major |
| MNDR | [TV](https://www.tradingview.com/chart/?symbol=MNDR) | $1.61 | +33.1% | 700 | 65K | 25.3 | -99.6% | 429K | Medical/Nursing Services |
| LGCL | [TV](https://www.tradingview.com/chart/?symbol=LGCL) | $2.99 | +32.3% | 200 | 34K | 399.4 | -99.5% | 49K | Personnel Services |
| FFR | [TV](https://www.tradingview.com/chart/?symbol=FFR) | $1.82 | +31.9% | 300 | 39K | 3.7 | -97.4% | 7.1M | Packaged Software |
| MI | [TV](https://www.tradingview.com/chart/?symbol=MI) | $1.57 | +27.6% | 20K | 51K | 0.9 | -38.7% | 542K | Internet Software/Services |
| SMXT | [TV](https://www.tradingview.com/chart/?symbol=SMXT) | $4.34 | +26.9% | 200 | 5K | 2.7 | -98.5% | 3.5M | Engineering & Construction |
| DKI | [TV](https://www.tradingview.com/chart/?symbol=DKI) | $1.72 | +26.5% | 100 | 68K | 245.6 | -99.7% | 1.2M | Packaged Software |
| MTEN | [TV](https://www.tradingview.com/chart/?symbol=MTEN) | $1.18 | +23.1% | 150 | 53K | 194.3 | -99.7% | 6.1M | Industrial Machinery |
| ELOG | [TV](https://www.tradingview.com/chart/?symbol=ELOG) | $0.68 | +19.5% | 264 | 4K | 30.3 | -93.8% | 6.8M | Air Freight/Couriers |
| CCG | [TV](https://www.tradingview.com/chart/?symbol=CCG) | $5.91 | +18.9% | 100 | 2K | 1.5 | -96.3% | 943K | Packaged Software |
| JVA | [TV](https://www.tradingview.com/chart/?symbol=JVA) | $4.72 | +18.3% | 1K | 3K | 9.5 | +200.8% | 5.0M | Food: Specialty/Candy |
| INLX | [TV](https://www.tradingview.com/chart/?symbol=INLX) | $5.70 | +17.5% | 2K | 708 | 3.8 | +105.6% | 2.9M | Packaged Software |
| XTIA | [TV](https://www.tradingview.com/chart/?symbol=XTIA) | $0.85 | +17.5% | 35K | 12K | 3.9 | +467.2% | 36.5M | Information Technology Services |
| NXTC | [TV](https://www.tradingview.com/chart/?symbol=NXTC) | $6.60 | +16.1% | 396 | 2K | 1.1 | -91.6% | 3.8M | Pharmaceuticals: Major |
| CANG | [TV](https://www.tradingview.com/chart/?symbol=CANG) | $3.49 | +15.5% | 2K | 13K | 3.8 | -96.8% | 38.3M | Wholesale Distributors |
| LICN | [TV](https://www.tradingview.com/chart/?symbol=LICN) | $1.05 | +15.4% | 2K | 927 | 3.6 | +509.7% | 16.2M | Miscellaneous Commercial Services |
| FMST | [TV](https://www.tradingview.com/chart/?symbol=FMST) | $0.57 | +15.1% | 1K | 7K | 40.5 | -79.3% | 13.2M | Other Metals/Minerals |

### Evaluation notes

**Watch — pending AH confirmation (29 names):** IRIX, SXTC, NXTS, NXAT, XSLL, VCIG, APMC, THEO, PFAI, SBFM, BIYA, NCPL, CPHI, MNDR, LGCL, FFR, MI, SMXT, DKI, MTEN, ELOG, CCG, JVA, INLX, XTIA, NXTC, CANG, LICN, FMST. `broker.js tradable` returned `tradable=true` for each. Float and industry are recorded for pattern tracking only.

**Untradable — carry forward (6 names):** ENSIF, EVOL, QNCRF, AMEGF, ENAFF, KHDHF returned `tradable=false` (all OTC, status inactive). Carry these into later scans without repeating SIP verification or catalyst searches.

**Stale scanner rows:** EVOL, XSLL, APMC and KHDHF show the same price, 5mVol, Avg5m, IRVol and VChg% as the 2026-10-06 21:30 scan. These are stale TradingView rows, so their IRVol readings carry no information about today.

**Trajectory observations:** SXTC (+229.6%, 774K latest 5-min volume, VChg +4.0%) is the only big mover still trading heavily into the close; it is already above the +150% entry ceiling from its prior close. XTIA (+17.5%, VChg +467.2%), JVA (+18.3%, +200.8%) and LICN (+15.4%, +509.7%) show rising volume on small absolute bars (1K–35K). The largest day movers (PFAI +120.5%, SBFM +92.8%, BIYA +59.0%, CPHI +34.0%, MNDR +33.1%, LGCL +32.3%) show VChg of -99.5% to -100.0% on 100–700 share latest bars. These regular-session fields do not establish AH accumulation or an AH BUILD/HOLD.

**Day% guard:** VCIG (-44.6%) and NXTS (-24.5%) are below -15%; an AH bounce on either is a dead-cat skip unless it reclaims above its regular close and builds across ≥2 AH scans (DEAD-CAT-OVERRIDE WATCH). QNCRF (-14.1%) is untradable. Recheck every Day% against the completed regular close before any entry.

**Multi-session context (for MULTI-SESSION-RUNNER tagging if they qualify in AH):** BIYA is the 2026-10-06 AH→PM winner (`WINNERS_TRACKING.md`, PM peak $2.86 at 04:14 ET today) and was sold this morning at $2.41; today's +59.0% is day 2 of that move. MTEN was entered 2026-10-06 and stopped out today at $1.21. SXTC, NCPL and VCIG were tracked AH candidates on 2026-10-06, so any AH move tonight is day 2+.

## Scan 22:00 CEST (4:00 PM ET)

No candidates found.

`python3 scripts/scan.py --all` ran at 16:00:15 ET (22:00:15 CEST) in the AFTERHOURS session and returned 0 hits.

Supplementary AH-change-only (>15%, not in volume pass): none
AH >10% at this snapshot (unrounded): none

### Evaluation notes

**Decision:** Observation only; no paper orders. This scan precedes the 23:00 CEST entry window, and no name was above 10% AH, so no spike-bar, CONFIRM-3, SIP volume or book checks applied. The scan ran 15 seconds after the AH open, so the TradingView postmarket fields had little or no AH data yet. This scan counts as zero qualifying AH appearances for every 21:30 watch name (SXTC, PFAI, SBFM, BIYA, CPHI, MNDR, LGCL and the rest).

## Scan 22:05 CEST (4:05 PM ET)

No candidates found.

`python3 scripts/scan.py --all` ran at 16:05:17 ET (22:05:17 CEST) in the AFTERHOURS session and returned 0 hits.

Supplementary AH-change-only (>15%, not in volume pass): none
AH >10% at this snapshot (unrounded): none

### Evaluation notes

**Decision:** Observation only; no paper orders. This scan precedes the 23:00 CEST entry window, and no name was above 10% AH, so no spike-bar, CONFIRM-3, SIP volume or book checks applied. SIP bars for 16:00–16:05 ET fall inside the free tier's 15-minute delay, so no SIP cross-check of the 21:30 watch names was possible yet. This scan adds zero qualifying AH appearances for every 21:30 watch name.

## Scan 22:10 CEST (4:10 PM ET)

No candidates found.

`python3 scripts/scan.py --all` ran at 16:10:12 ET (22:10:12 CEST) in the AFTERHOURS session and returned 0 hits.

Supplementary AH-change-only (>15%, not in volume pass): none
AH >10% at this snapshot (unrounded): none

### Evaluation notes

**Decision:** Observation only; no paper orders. This scan precedes the 23:00 CEST entry window, and no name was above 10% AH, so no spike-bar, CONFIRM-3, SIP volume or book checks applied. SIP bars for 16:00–16:10 ET still fall inside the free tier's 15-minute delay, so no SIP cross-check of the 21:30 watch names was possible. This is the third consecutive empty AH scan, which suggests the TradingView postmarket fields have not populated yet; later scans should confirm whether the 21:30 movers (SXTC, PFAI, SBFM, BIYA) carry into AH. This scan adds zero qualifying AH appearances for every 21:30 watch name.

## Scan 22:15 CEST (4:15 PM ET)

No candidates found.

`python3 scripts/scan.py --all` ran at 16:15:15 ET (22:15:15 CEST) in the AFTERHOURS session and returned 0 hits.

Supplementary AH-change-only (>15%, not in volume pass): none
AH >10% at this snapshot (unrounded): none

### Evaluation notes

**Decision:** Observation only; no paper orders. This scan precedes the 23:00 CEST entry window, and the scanner reported no name above 10% AH, so no spike-bar, CONFIRM-3, SIP volume or book checks applied. This is the fourth consecutive empty AH scan.

**SIP cross-check of the top 21:30 watch names (first AH bar now outside the 15-minute delay):** The scanner's empty result does not match SIP for at least one name. Close below is the 15:55 ET bar close, an approximation of the official close.

| Ticker | 15:55 bar C | 16:00 bar (O/H/L/C) | 16:00 bar vol / trades | 16:00 C vs 15:55 C |
|--------|-------------|---------------------|------------------------|--------------------|
| PFAI | $5.00 | $5.07 / $6.18 / $5.04 / $5.53 | 1,024,894 / 13,995 | +10.6% (H +23.6%) |
| SXTC | $2.81 | $2.83 / $2.85 / $2.30 / $2.42 | 678,816 / 4,969 | -13.9% |
| SBFM | $0.70 | $0.70 / $0.70 / $0.63 / $0.63 | 258,038 / 495 | -10.0% |
| BIYA | $2.29 | $2.18 / $2.30 / $2.08 / $2.13 | 152,118 / 737 | -7.0% |

PFAI traded about 1.0M shares on 14K trades in the 16:00 ET bar and closed it about 10% above the regular close, while TradingView listed nothing. One SIP bar is not a qualifying AH scan appearance; the next scans should check whether TradingView picks PFAI up and whether SIP volume keeps accumulating after the first bar. SXTC fell from $4.12 at the 21:30 scan to $2.81 by the close and lost another 14% in the first AH bar. SBFM and BIYA are fading in AH.

## Scan 22:20 CEST (4:20 PM ET)

`python3 scripts/scan.py --all` ran at 16:20:13 ET (22:20:13 CEST) in the AFTERHOURS session and returned 2 hits.

Supplementary AH-change-only (>15%, not in volume pass): none
AH >10% at this snapshot (unrounded): MVIS

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| PFAI | [TV](https://www.tradingview.com/chart/?symbol=PFAI) | $5.07 | +116.7% | +9.3% | $5.54 | +136.9% | 717K | 2.9M | 0.2x | 3.6M | Trucks/Construction/Farm Machinery |
| MVIS | [TV](https://www.tradingview.com/chart/?symbol=MVIS) | $1.52 | -3.8% | +11.8% | $1.70 | +7.6% | 661K | 1.1M | 0.6x | 27.9M | Semiconductors |

### Evaluation notes

**Decision:** Observation only; no paper orders. This scan precedes the 23:00 CEST entry window. This is the first AH scan with any hits, so MVIS has 1 qualifying AH appearance and PFAI has 0 (+9.3%, below 10%).

**MVIS** (new, `tradable=true`, float 27.9M, Semiconductors/lidar):

- Spike bar: `MVIS 2026-10-07  SPIKE  16:01ET  +22%  $1.85  367 trades / 64k sh  (first co-spike bar) (as-of 16:20ET)`
- Third bar: `MVIS 2026-10-07  CONFIRM-3  NO no local-volume new-high ignition as-of 16:20ET`
- SIP bars: 16:00 ET O $1.52 H $1.86 L $1.52 C $1.66, 716,315 sh / 3,566 trades, vwap $1.72; 16:05 ET O $1.70 H $1.70 L $1.40 C $1.41, 547,866 sh / 2,190 trades, vwap $1.52. The 16:05 bar closed 7% below the regular close. The scanner's $1.70 at 16:20 sits between the two bars and is newer than the latest SIP bar, so it is not a bad print, but SIP shows a first-bar high and a full round trip in the second bar.
- Shared SIP volume context:
  ```
  # MVIS shared SIP volume sip-ah-volume-v2; prior 2026-10-06 10+38zero/48 slots; floor 100; log-only
  # reconstructed as-of 2026-10-07T20:20:13+00:00; source fetched 2026-10-07T20:20:37.875192+00:00
  MVIS 2026-10-07  VOLUME-CONTEXT 16:00ET start=2026-10-07T20:00:00+00:00 shares=716315 local=unknown prior-peak=71.2893x status=warmup
  MVIS 2026-10-07  VOLUME-CONTEXT 16:05ET start=2026-10-07T20:05:00+00:00 shares=547866 local=unknown prior-peak=54.5249x status=warmup
  ```
- Book:
  ```
  MVIS BOOK iex bid $1.30 x100 / ask $1.74 x100 @ 2026-10-07 16:00:01 ET age 20m38s two-sided spread 25.29% of ask
  MVIS BOOK sip-15m bid $1.51 x900 / ask $1.52 x2000 @ 2026-10-07 16:05:39 ET age 15m00s two-sided spread 0.66% of ask
  MVIS BOOK refresh +15s iex unchanged @ 2026-10-07 16:00:01 ET
  MVIS BOOK verdict: IEX STALE 20m38s; SIP-15m TWO-SIDED (observed 2026-10-07 16:20:39 ET; log-only)
  ```
- Catalyst (3 searches): MicroVision scheduled a video business update for 2026-10-07 at 4:00 PM ET (ACCESS Newswire, October 2, 2026, moved from 1:00 PM ET). StockTitan says the update covers commercial progress and revenue and operating expense expectations. The event is dated today and matches the 16:00 ET spike, but I found no write-up of what was said, so the catalyst content is unverified. Provisional grade: None until a dated release or 8-K with the content appears. Re-check at the next scan if MVIS stays above 10% AH.
- Pattern: first AH bar holds the high ($1.86), CONFIRM-3 NO. If this persists across scans, MVIS fits the first-bar-spike skip. Day% -3.8% and Total% +7.6% are far below the extension ceiling.

**PFAI** (21:30 watch name, +9.3% AH): SIP 16:00 ET bar H $6.18 on 1.02M sh / 13,995 trades, then 16:05 ET bar L $4.42 / C $4.64 on 474K sh / 6,724 trades, below the $5.07 close. The scanner's $5.54 at 16:20 is newer than SIP. Below 10%, so no instrumentation run; first-bar high, same shape as MVIS.

## Scan 22:25 CEST (4:25 PM ET)

`python3 scripts/scan.py --all` ran at 16:25:11 ET (22:25:11 CEST) in the AFTERHOURS session and returned 3 hits.

Supplementary AH-change-only (>15%, not in volume pass): KUST, VNTG
AH >10% at this snapshot (unrounded): KUST, VNTG

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| IRIX | [TV](https://www.tradingview.com/chart/?symbol=IRIX) | $0.88 | +29.2% | +8.0% | $0.95 | +39.6% | 163K | 1.3M | 0.1x | 10.9M | Medical Specialties |
| VNTG | [TV](https://www.tradingview.com/chart/?symbol=VNTG) | $0.63 | -4.0% | +18.2% | $0.74 | +13.5% | 20K | 367K | 0.1x | 10.6M | Marine Shipping |
| KUST | [TV](https://www.tradingview.com/chart/?symbol=KUST) | $4.50 | -1.6% | +15.5% | $5.19 | +13.6% | 15K | 44K | 0.3x | 625K | Miscellaneous Commercial Services |

### Evaluation notes

**Decision:** Observation only; no paper orders. This scan precedes the 23:00 CEST entry window. Qualifying AH appearances so far: KUST 1, VNTG 1, MVIS 1 (dropped out of this scan), PFAI 0, IRIX 0. SIP bars through 16:10 ET were available at 16:25 ET.

**KUST** (new, `tradable=true`, float 625K, Kustom Entertainment, live entertainment/ticketing):

- Spike bar: `KUST 2026-10-07  SPIKE  16:09ET  +22%  $5.50  164 trades / 18k sh  (first co-spike bar) (as-of 16:25ET)`
- Third bar: `KUST 2026-10-07  CONFIRM-3  PENDING ignition 16:05ET; waiting for third bar as-of 16:25ET`
- SIP bars: 16:00 ET $4.50 on 259 sh / 4 trades; 16:05 ET O $4.61 H $5.50 C $5.24, 17,804 sh / 164 trades, vwap $5.15; 16:10 ET O $5.19 H $5.75 L $4.93 C $5.19, 169,039 sh / 3,481 trades, vwap $5.34. Volume rose about 10x into the 16:10 bar, and the 16:10 high ($5.75, +27.8%) came after the 16:05 ignition, so this is not a first-bar spike so far. The scanner's $5.19 matches the SIP 16:10 close.
- Shared SIP volume context:
  ```
  # KUST shared SIP volume sip-ah-volume-v2; prior 2026-10-06 2+46zero/48 slots; floor 100; log-only
  # reconstructed as-of 2026-10-07T20:25:11+00:00; source fetched 2026-10-07T20:25:50.248841+00:00
  KUST 2026-10-07  VOLUME-CONTEXT 16:00ET start=2026-10-07T20:00:00+00:00 shares=259 local=unknown prior-peak=0.4752x status=warmup
  KUST 2026-10-07  VOLUME-CONTEXT 16:05ET start=2026-10-07T20:05:00+00:00 shares=17804 local=unknown prior-peak=32.6679x status=warmup
  KUST 2026-10-07  VOLUME-CONTEXT 16:10ET start=2026-10-07T20:10:00+00:00 shares=169039 local=unknown prior-peak=310.1633x status=warmup
  ```
- Book:
  ```
  KUST BOOK iex bid $3.57 x100 / ask $5.17 x100 @ 2026-10-07 16:00:02 ET age 25m52s two-sided spread 30.95% of ask
  KUST BOOK sip-15m bid $5.32 x100 / ask $5.43 x400 @ 2026-10-07 16:10:53 ET age 15m00s two-sided spread 2.03% of ask
  KUST BOOK refresh +15s iex unchanged @ 2026-10-07 16:00:02 ET
  KUST BOOK verdict: IEX STALE 25m52s; SIP-15m TWO-SIDED (observed 2026-10-07 16:25:53 ET; log-only)
  ```
- Catalyst (2 searches): no catalyst found dated today. Background only: 1-for-10 reverse split effective 2026-10-01 (StockTitan, about a week old) and the TFL (Tickets For Less) acquisition agreement of 2026-09-01. Neither is fresh. Provisional grade: None. Re-search at the next scan if KUST stays above 10% AH.
- Multi-session context: `WINNERS_TRACKING.md` lists KUST runs on 2026-07-15 and 2026-07-31, both months old. Day% -1.6% today, so tonight is a fresh first-day AH move. The reverse split was on 2026-10-01, before the 2026-10-06 prior session, so the prior-session volume comparison is on a split-adjusted basis.

**VNTG** (new, `tradable=true`, float 10.6M, Vantage Corp, Singapore tanker shipbroking):

- Spike bar: `VNTG 2026-10-07  SPIKE  16:09ET  +21%  $0.76  36 trades / 16k sh  (first co-spike bar) (as-of 16:25ET)`
- Third bar: `VNTG 2026-10-07  CONFIRM-3  PENDING ignition 16:05ET; waiting for third bar as-of 16:25ET`
- SIP bars: 16:00 ET C $0.68, 6,101 sh / 14 trades; 16:05 ET H $0.76 C $0.74, 21,451 sh / 87 trades; 16:10 ET O $0.74 L $0.63 C $0.64, 20,745 sh / 64 trades, vwap $0.65. The 16:10 bar gave back the whole move to roughly the $0.63 close, on tens of K shares and under 100 trades per bar. The scanner's $0.74 is the 16:05 close and is behind SIP. This is thin and already faded.
- Shared SIP volume context:
  ```
  # VNTG shared SIP volume sip-ah-volume-v2; prior 2026-10-06 3+45zero/48 slots; floor 100; log-only
  # reconstructed as-of 2026-10-07T20:25:11+00:00; source fetched 2026-10-07T20:25:52.157870+00:00
  VNTG 2026-10-07  VOLUME-CONTEXT 16:00ET start=2026-10-07T20:00:00+00:00 shares=6101 local=unknown prior-peak=0.5916x status=warmup
  VNTG 2026-10-07  VOLUME-CONTEXT 16:05ET start=2026-10-07T20:05:00+00:00 shares=21451 local=unknown prior-peak=2.0802x status=warmup
  VNTG 2026-10-07  VOLUME-CONTEXT 16:10ET start=2026-10-07T20:10:00+00:00 shares=20745 local=unknown prior-peak=2.0117x status=warmup
  ```
- Book: not run; SIP volume is not accumulating.
- Catalyst (2 searches): no catalyst found dated today. Most recent items are the OpsWiz commercialization PR (2026-09-21) and FY2026 results; both are background.

**IRIX** (21:30 watch name, +8.0% on the scanner, below 10%): SIP is ahead of the scanner. The 16:10 ET bar ran O $0.95 H $1.03 C $1.00 on 1,371,285 sh / 4,226 trades (vwap $0.99), which is +13.6% over the $0.88 close and about +58% on the day. This is the largest AH bar of the session so far. It does not count as a qualifying AH appearance until the scanner shows it above 10%; cross-check it against SIP at the next scans.

**Faded 22:20 names:** MVIS dropped off the scanner; SIP 16:10 ET C $1.37 on 164K sh, about 10% below the $1.52 close, after the first-bar high of $1.86. PFAI SIP 16:10 ET C $4.10 (L $4.00), about 19% below the $5.07 close, after the $6.18 first-bar high. Both follow the first-bar-spike shape and are now below their regular closes.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
