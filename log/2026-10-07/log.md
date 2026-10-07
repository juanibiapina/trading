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

## Scan 22:30 CEST (4:30 PM ET)

`python3 scripts/scan.py --all` ran at 16:30:15 ET (22:30:15 CEST) in the AFTERHOURS session and returned 3 hits.

Supplementary AH-change-only (>15%, not in volume pass): none
AH >10% at this snapshot (unrounded): IRIX, KUST, SUGP

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| IRIX | [TV](https://www.tradingview.com/chart/?symbol=IRIX) | $0.88 | +29.2% | +13.5% | $1.00 | +46.6% | 1.5M | 1.5M | 1.0x | 10.9M | Medical Specialties |
| KUST | [TV](https://www.tradingview.com/chart/?symbol=KUST) | $4.50 | -1.6% | +16.8% | $5.25 | +14.9% | 114K | 61K | 1.9x | 625K | Miscellaneous Commercial Services |
| SUGP | [TV](https://www.tradingview.com/chart/?symbol=SUGP) | $2.64 | +8.2% | +12.5% | $2.97 | +21.7% | 85K | 1.6M | 0.1x | 1.4M | Miscellaneous Commercial Services |

### Evaluation notes

**Decision:** Observation only; no paper orders. This scan precedes the 23:00 CEST entry window. Qualifying AH appearances so far: KUST 2 (22:25, 22:30), IRIX 1, SUGP 1, VNTG 1 (dropped out of this scan), MVIS 1 (dropped out at 22:25). All three hits are `tradable=true`. SIP bars through 16:15 ET were available at 16:30 ET.

**IRIX** (21:30 watch name, first scanner appearance above 10%, float 10.9M, IRIDEX, ophthalmic lasers):

- Spike bar: `IRIX 2026-10-07  SPIKE  16:13ET  +16%  $1.02  1503 trades / 533k sh  (first co-spike bar) (as-of 16:30ET)`
- Third bar: `IRIX 2026-10-07  CONFIRM-3  PENDING ignition 16:10ET; waiting for third bar as-of 16:30ET`
- SIP bars: 16:10 ET O $0.95 H $1.03 C $1.00, 1,371,285 sh / 4,226 trades, vwap $0.99; 16:15 ET O $1.00 H $1.01 L $0.94 C $0.95, 883,786 sh / 2,976 trades, vwap $0.98. Volume is real and sustained across two bars (hundreds of K shares, thousands of trades). The scanner's $1.00 matches the SIP range and sits within 3% of the $1.03 AH high, so it is holding. The AH high came in the third AH bar, after two flat bars, so this is not a first-bar spike.
- Shared SIP volume context:
  ```
  # IRIX shared SIP volume sip-ah-volume-v2; prior 2026-10-06 1+47zero/48 slots; floor 100; log-only
  # reconstructed as-of 2026-10-07T20:30:15+00:00; source fetched 2026-10-07T20:30:40.503967+00:00
  IRIX 2026-10-07  VOLUME-CONTEXT 16:00ET start=2026-10-07T20:00:00+00:00 shares=87036 local=unknown prior-peak=364.1674x status=warmup
  IRIX 2026-10-07  VOLUME-CONTEXT 16:05ET start=2026-10-07T20:05:00+00:00 shares=82288 local=unknown prior-peak=344.3013x status=warmup
  IRIX 2026-10-07  VOLUME-CONTEXT 16:10ET start=2026-10-07T20:10:00+00:00 shares=1371285 local=unknown prior-peak=5737.5941x status=warmup
  IRIX 2026-10-07  VOLUME-CONTEXT 16:15ET start=2026-10-07T20:15:00+00:00 shares=883786 local=10.1543x prior-peak=3697.8494x status=ok
  ```
- Book:
  ```
  IRIX BOOK iex bid $0.9920 x100 / ask $1.01 x100 @ 2026-10-07 16:26:48 ET age 3m57s two-sided spread 1.78% of ask
  IRIX BOOK sip-15m bid $0.9712 x300 / ask $0.9731 x200 @ 2026-10-07 16:15:46 ET age 15m00s two-sided spread 0.20% of ask
  IRIX BOOK refresh +15s iex unchanged @ 2026-10-07 16:26:48 ET
  IRIX BOOK verdict: IEX STALE 3m57s; SIP-15m TWO-SIDED (observed 2026-10-07 16:30:46 ET; log-only)
  ```
- Catalyst (2 searches): no company release, earnings or 8-K found dated today. The only dated item is a Defense World article of 2026-10-07 reporting that major shareholder Shih-Yao David Lin bought 17,526 shares (a Form 4 insider purchase, small size). That is weak background and does not explain a +46% total move. Grade: None.
- Multi-session context: not in `WINNERS_TRACKING.md`. Day% +29.2% came from the regular session (21:30 watch at +14.7%), so tonight is day 1 of the move, extending into AH.

**KUST** (second qualifying AH appearance, float 625K):

- Spike bar: `KUST 2026-10-07  SPIKE  16:09ET  +22%  $5.50  164 trades / 18k sh  (first co-spike bar) (as-of 16:30ET)`
- Third bar: `KUST 2026-10-07  CONFIRM-3  NO ignition 16:05ET failed third-bar hold/volume as-of 16:30ET`
- SIP bars: 16:15 ET O $5.25 H $5.95 L $4.13 C $4.36, 254,335 sh / 4,337 trades, vwap $5.11. Volume kept rising (17.8K → 169K → 254K sh), and the bar made a new high at $5.95 (+32%), then closed at $4.36, 3% below the $4.50 regular close. The scanner's $5.25 at 16:30 is newer than this bar, so the swing range is $4.13–$5.95 on real trades. CONFIRM-3 turned NO because the third bar failed to hold.
- Shared SIP volume context:
  ```
  # KUST shared SIP volume sip-ah-volume-v2; prior 2026-10-06 2+46zero/48 slots; floor 100; log-only
  # reconstructed as-of 2026-10-07T20:30:15+00:00; source fetched 2026-10-07T20:30:42.557562+00:00
  KUST 2026-10-07  VOLUME-CONTEXT 16:00ET start=2026-10-07T20:00:00+00:00 shares=259 local=unknown prior-peak=0.4752x status=warmup
  KUST 2026-10-07  VOLUME-CONTEXT 16:05ET start=2026-10-07T20:05:00+00:00 shares=17804 local=unknown prior-peak=32.6679x status=warmup
  KUST 2026-10-07  VOLUME-CONTEXT 16:10ET start=2026-10-07T20:10:00+00:00 shares=169039 local=unknown prior-peak=310.1633x status=warmup
  KUST 2026-10-07  VOLUME-CONTEXT 16:15ET start=2026-10-07T20:15:00+00:00 shares=254335 local=14.2853x prior-peak=466.6697x status=ok
  ```
- Book:
  ```
  KUST BOOK iex bid $3.57 x100 / ask $5.17 x100 @ 2026-10-07 16:00:02 ET age 30m44s two-sided spread 30.95% of ask
  KUST BOOK sip-15m bid $5.42 x100 / ask $5.52 x200 @ 2026-10-07 16:15:46 ET age 15m00s two-sided spread 1.81% of ask
  KUST BOOK refresh +15s iex unchanged @ 2026-10-07 16:00:02 ET
  KUST BOOK verdict: IEX STALE 30m44s; SIP-15m TWO-SIDED (observed 2026-10-07 16:30:46 ET; log-only)
  ```
- Catalyst re-search (1 search, 3 total): still no catalyst dated today. Newest items are the 1-for-10 reverse split and recapitalization effective 2026-10-01 (TipRanks, 2 days old) and a 2026-10-06 article on shareholder votes. Both are background. Grade: None.
- Pattern: KUST clears the 2-AH-scan count, but the 16:15 bar's $5.95 → $4.36 reversal and CONFIRM-3 NO make it a volatile swing, not a clean build. Re-check the trajectory at 23:00.

**SUGP** (new, float 1.4M, SU Group Holdings, Hong Kong security services):

- Spike bar: `SUGP 2026-10-07  SPIKE  16:13ET  +17%  $3.08  471 trades / 48k sh  (first co-spike bar) (as-of 16:30ET)`
- Third bar: `SUGP 2026-10-07  CONFIRM-3  PENDING ignition 16:10ET; waiting for third bar as-of 16:30ET`
- SIP bars: 16:10 ET O $2.71 H $3.08 C $2.98, 100,189 sh / 1,063 trades; 16:15 ET O $2.97 H $3.37 L $2.57 C $2.66, 411,416 sh / 4,854 trades, vwap $2.95. Volume is accumulating, but the 16:15 bar swung from a $3.37 high (+28%) to a $2.66 close (+0.8%). The scanner's $2.97 is newer than this bar and matches the 16:15 vwap.
- Shared SIP volume context:
  ```
  # SUGP shared SIP volume sip-ah-volume-v2; prior 2026-10-06 28+20zero/48 slots; floor 100; log-only
  # reconstructed as-of 2026-10-07T20:30:15+00:00; source fetched 2026-10-07T20:30:44.699244+00:00
  SUGP 2026-10-07  VOLUME-CONTEXT 16:00ET start=2026-10-07T20:00:00+00:00 shares=1206 local=unknown prior-peak=0.0672x status=warmup
  SUGP 2026-10-07  VOLUME-CONTEXT 16:05ET start=2026-10-07T20:05:00+00:00 shares=3676 local=unknown prior-peak=0.2048x status=warmup
  SUGP 2026-10-07  VOLUME-CONTEXT 16:10ET start=2026-10-07T20:10:00+00:00 shares=100189 local=unknown prior-peak=5.5806x status=warmup
  SUGP 2026-10-07  VOLUME-CONTEXT 16:15ET start=2026-10-07T20:15:00+00:00 shares=411416 local=111.9195x prior-peak=22.9163x status=ok
  ```
  Prior-session comparison unverified: SUGP's 1-for-6 reverse split took effect at 12:01 AM ET today (PRNewswire, 2026-10-02), so the 2026-10-06 session traded pre-split share counts. The `prior-peak` ratio compares post-split shares against pre-split shares. The scanner's 1.6M AvgVol is likely on the pre-split basis too, which would understate VRatio.
- Book:
  ```
  SUGP BOOK iex bid $2.25 x100 / ask $3.06 x100 @ 2026-10-07 16:00:00 ET age 30m46s two-sided spread 26.47% of ask
  SUGP BOOK sip-15m bid $2.92 x100 / ask $2.95 x500 @ 2026-10-07 16:15:45 ET age 15m01s two-sided spread 1.02% of ask
  SUGP BOOK refresh +15s iex unchanged @ 2026-10-07 16:00:00 ET
  SUGP BOOK verdict: IEX STALE 30m46s; SIP-15m TWO-SIDED (observed 2026-10-07 16:30:46 ET; log-only)
  ```
- Catalyst (2 searches): no catalyst dated today. Background: the 1-for-6 reverse split effective today (announced 2026-10-02), a Nasdaq staff delisting determination with a hearing request, and a 2026-09-15 subsidiary announcement with an acquisition agreement deadline of 2026-10-31. A reverse split is not a fresh catalyst. Grade: None.
- Multi-session context: not in `WINNERS_TRACKING.md`; Day% +8.2% on the first post-split session.

**Dropped names:** VNTG and MVIS are off the scanner. Not re-pulled; both had faded below their regular closes on SIP at 22:25.

## Scan 22:45 CEST (4:45 PM ET)

`python3 scripts/scan.py --all` ran at 16:45:20 ET (22:45:20 CEST) in the AFTERHOURS session and returned 2 hits, neither above 10% AH.

Supplementary AH-change-only (>15%, not in volume pass): none
AH >10% at this snapshot (unrounded): none

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| CPHI | [TV](https://www.tradingview.com/chart/?symbol=CPHI) | $0.85 | +32.6% | +7.1% | $0.91 | +42.0% | 1.2M | 6.2M | 0.2x | 40.3M | Pharmaceuticals: Major |
| FMST | [TV](https://www.tradingview.com/chart/?symbol=FMST) | $0.56 | +13.2% | +8.5% | $0.61 | +22.8% | 587K | 613K | 1.0x | 13.2M | Other Metals/Minerals |

### Evaluation notes

**Decision:** Observation only; no paper orders. This scan precedes the 23:00 CEST entry window, and no name is above 10% AH. Spike-bar, CONFIRM-3, volume-metric and book checks apply only to >10% candidates, so none ran. Qualifying AH appearance counts are unchanged: KUST 2, IRIX 1, SUGP 1, VNTG 1, MVIS 1.

**Tracked names, SIP bars through 16:30 ET:** all three 22:30 qualifiers faded off the scanner.

- **IRIX** (close $0.88): made a new AH high of $1.08 in the 16:20 bar (1.35M sh / 4,673 trades), then sold off on heavy volume: 16:25 C $0.89 (1.22M sh), 16:30 C $0.81 (1.05M sh / 2,420 trades, vwap $0.85). Now about 8% below the regular close and 25% off the AH high. Spike→fade.
- **KUST** (close $4.50): after the 16:15 swing to $5.95, it fell to $3.93 at 16:20 and has sat at $3.95–$4.13 since on thin volume (4–5K sh, 62–125 trades per bar). About 12% below the regular close. Fade; it no longer qualifies.
- **SUGP** (close $2.64): fell from the 16:15 $3.37 high to $2.50–$2.74 on thin volume (10–14K sh per bar). 16:30 C $2.71, about +2.7% AH. Fade.

**New names (below the 10% threshold):**

- **CPHI** (float 40.3M): +7.1% AH. The 16:25 bar carried 441K sh / 1,578 trades up to $0.93, then 16:30 eased to $0.84 (206K sh). Watch only.
- **FMST** (float 13.2M): +8.5% AH on thin volume (22–112K sh, 37–151 trades per bar). Watch only.

## Scan 23:00 CEST (5:00 PM ET)

`python3 scripts/scan.py --all` ran at 17:00:13 ET (23:00:13 CEST) in the AFTERHOURS session and returned 5 hits.

Supplementary AH-change-only (>15%, not in volume pass): ERNA, IPW
AH >10% at this snapshot (unrounded): ERNA, IPW, NCPL, PROF

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $1.59 | +45.9% | +10.1% | $1.75 | +60.6% | 1.1M | 13.3M | 0.1x | 4.4M | Miscellaneous Commercial Services |
| FMST | [TV](https://www.tradingview.com/chart/?symbol=FMST) | $0.56 | +13.2% | +7.1% | $0.60 | +21.3% | 630K | 617K | 1.0x | 13.2M | Other Metals/Minerals |
| PROF | [TV](https://www.tradingview.com/chart/?symbol=PROF) | $5.68 | -6.6% | +21.3% | $6.89 | +13.3% | 81K | 151K | 0.5x | 35.4M | Medical Specialties |
| IPW | [TV](https://www.tradingview.com/chart/?symbol=IPW) | $1.04 | -8.0% | +17.3% | $1.22 | +8.0% | 45K | 409K | 0.1x | 1.2M | Internet Retail |
| ERNA | [TV](https://www.tradingview.com/chart/?symbol=ERNA) | $2.39 | +6.9% | +16.3% | $2.78 | +24.4% | 29K | 41K | 0.7x | 1.1M | Pharmaceuticals: Major |

### Evaluation notes

**Decision:** No paper orders. The entry window is open, but no name has the required 2 qualifying AH scans. All four >10% names (NCPL, PROF, IPW, ERNA) are first AH appearances above 10%; NCPL was a 21:30 regular-session watch name, which does not count. The earlier AH qualifiers (KUST 2, IRIX 1, SUGP 1, VNTG 1, MVIS 1) are all off the scanner and had faded on SIP by 22:45. All four new names are `tradable=true`; no open positions. SIP bars through 16:45 ET were available at 17:00 ET.

**NCPL** (float 4.4M, Netcapital, fintech capital platform; 21:30 watch name):

- Spike bar: `NCPL 2026-10-07  SPIKE  16:32ET  +17%  $1.86  1076 trades / 280k sh  (first co-spike bar) (as-of 17:00ET)`
- Third bar: `NCPL 2026-10-07  CONFIRM-3  NO ignition 16:30ET failed third-bar hold/volume as-of 17:00ET`
- SIP bars: flat $1.58–$1.65 on 8–70K sh per bar until 16:30, then 16:30 O $1.65 H $1.86 C $1.77 on 576K sh / 2,476 trades; 16:35 C $1.73 (196K sh / 1,153 trades); 16:40 C $1.75 (205K sh / 1,140 trades); 16:45 C $1.66 (94K sh / 475 trades). Real volume, but fading from the 16:30 bar, and price is 11% off the $1.86 high. The scanner's $1.75 matches the 16:40 SIP range.
- Shared SIP volume context:
  ```
  # NCPL shared SIP volume sip-ah-volume-v2; prior 2026-10-06 43+5zero/48 slots; floor 100; log-only
  # reconstructed as-of 2026-10-07T21:00:13+00:00; source fetched 2026-10-07T21:00:55.777593+00:00
  NCPL 2026-10-07  VOLUME-CONTEXT 16:00ET start=2026-10-07T20:00:00+00:00 shares=70160 local=unknown prior-peak=0.9746x status=warmup
  NCPL 2026-10-07  VOLUME-CONTEXT 16:05ET start=2026-10-07T20:05:00+00:00 shares=8245 local=unknown prior-peak=0.1145x status=warmup
  NCPL 2026-10-07  VOLUME-CONTEXT 16:10ET start=2026-10-07T20:10:00+00:00 shares=27620 local=unknown prior-peak=0.3837x status=warmup
  NCPL 2026-10-07  VOLUME-CONTEXT 16:15ET start=2026-10-07T20:15:00+00:00 shares=29276 local=1.0600x prior-peak=0.4067x status=ok
  NCPL 2026-10-07  VOLUME-CONTEXT 16:20ET start=2026-10-07T20:20:00+00:00 shares=27482 local=0.9950x prior-peak=0.3818x status=ok
  NCPL 2026-10-07  VOLUME-CONTEXT 16:25ET start=2026-10-07T20:25:00+00:00 shares=18556 local=0.6718x prior-peak=0.2578x status=ok
  NCPL 2026-10-07  VOLUME-CONTEXT 16:30ET start=2026-10-07T20:30:00+00:00 shares=576193 local=20.9662x prior-peak=8.0041x status=ok
  NCPL 2026-10-07  VOLUME-CONTEXT 16:35ET start=2026-10-07T20:35:00+00:00 shares=195535 local=7.1150x prior-peak=2.7163x status=ok
  NCPL 2026-10-07  VOLUME-CONTEXT 16:40ET start=2026-10-07T20:40:00+00:00 shares=204701 local=1.0469x prior-peak=2.8436x status=ok
  NCPL 2026-10-07  VOLUME-CONTEXT 16:45ET start=2026-10-07T20:45:00+00:00 shares=93757 local=0.4580x prior-peak=1.3024x status=ok
  ```
- Book:
  ```
  NCPL BOOK iex bid $1.64 x100 / ask $1.70 x100 @ 2026-10-07 16:51:26 ET age 9m40s two-sided spread 3.53% of ask
  NCPL BOOK sip-15m bid $1.68 x2300 / ask $1.69 x400 @ 2026-10-07 16:46:05 ET age 15m01s two-sided spread 0.59% of ask
  NCPL BOOK refresh +15s iex unchanged @ 2026-10-07 16:51:26 ET
  NCPL BOOK verdict: IEX STALE 9m40s; SIP-15m TWO-SIDED (observed 2026-10-07 17:01:06 ET; log-only)
  ```
- Catalyst (3 searches): nothing dated today. Newest items are the 2026-06-04 non-binding LOI to buy Resmac mortgage assets from RezyFi (GlobeNewswire) and an August Nasdaq deficiency notice with a compliance plan due 2026-10-23. Both are background. Grade: None.
- Multi-session context: not in `WINNERS_TRACKING.md`. Day% +45.9% came in today's regular session; day 1 of the move.

**PROF** (float 35.4M, Profound Medical, MRI-guided prostate ablation):

- Spike bar: `PROF 2026-10-07  SPIKE  16:36ET  +21%  $6.87  69 trades / 2k sh  (first co-spike bar) (as-of 17:00ET)`
- Third bar: `PROF 2026-10-07  CONFIRM-3  NO ignition 16:35ET failed third-bar hold/volume as-of 17:00ET`
- SIP bars: near-empty until 16:30; 16:35 O $6.50 H $7.51 C $6.59 on 51.8K sh / 659 trades; 16:40 C $6.89 (40.5K sh / 447 trades); 16:45 C $6.82 (7.5K sh / 201 trades). Tens of K shares, hundreds of trades, falling volume: moderate and thinning. Price is 9% off the $7.51 high; the scanner's $6.89 matches SIP.
- Shared SIP volume context:
  ```
  # PROF shared SIP volume sip-ah-volume-v2; prior 2026-10-06 1+47zero/48 slots; floor 100; log-only
  # reconstructed as-of 2026-10-07T21:00:13+00:00; source fetched 2026-10-07T21:00:58.583786+00:00
  PROF 2026-10-07  VOLUME-CONTEXT 16:00ET start=2026-10-07T20:00:00+00:00 shares=2919 local=unknown prior-peak=4.2121x status=warmup
  PROF 2026-10-07  VOLUME-CONTEXT 16:25ET start=2026-10-07T20:25:00+00:00 shares=500 local=5.0000x prior-peak=0.7215x status=floored
  PROF 2026-10-07  VOLUME-CONTEXT 16:30ET start=2026-10-07T20:30:00+00:00 shares=4110 local=41.1000x prior-peak=5.9307x status=floored
  PROF 2026-10-07  VOLUME-CONTEXT 16:35ET start=2026-10-07T20:35:00+00:00 shares=51786 local=103.5720x prior-peak=74.7273x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 16:40ET start=2026-10-07T20:40:00+00:00 shares=40539 local=9.8635x prior-peak=58.4978x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 16:45ET start=2026-10-07T20:45:00+00:00 shares=7528 local=0.1857x prior-peak=10.8629x status=ok
  ```
- Book:
  ```
  PROF BOOK iex bid $7.10 x100 / ask $7.87 x100 @ 2026-10-07 16:37:16 ET age 23m50s two-sided spread 9.78% of ask
  PROF BOOK sip-15m bid $6.70 x1200 / ask $6.82 x200 @ 2026-10-07 16:46:04 ET age 15m01s two-sided spread 1.76% of ask
  PROF BOOK refresh +15s iex unchanged @ 2026-10-07 16:37:16 ET
  PROF BOOK verdict: IEX STALE 23m50s; SIP-15m TWO-SIDED (observed 2026-10-07 17:01:06 ET; log-only)
  ```
- Catalyst (1 search): GlobeNewswire 2026-10-07, "Profound Medical Reports Strong Preliminary Third Quarter 2026 Revenue" (preliminary unaudited Q3 revenue). The search showed it as 47 minutes old at about 17:02 ET, so it was released around 16:15 ET; the exact timestamp is unverified. Fresh, same-day. Grade: B (revenue beat type).
- Multi-session context: not in `WINNERS_TRACKING.md`; Day% −6.6%, so this is a fresh AH reaction.

**IPW** (float 1.2M, iPower, digital treasury and supply chain):

- Spike bar: `IPW 2026-10-07  SPIKE  16:44ET  +25%  $1.30  149 trades / 23k sh  (first co-spike bar) (as-of 17:00ET)`
- Third bar: `IPW 2026-10-07  CONFIRM-3  PENDING ignition 16:40ET; waiting for third bar as-of 17:00ET`
- SIP bars: dead until 16:40 (single trades at $1.05–$1.07); 16:40 O $1.09 H $1.30 C $1.21 on 25K sh / 160 trades; 16:45 O $1.22 H $1.36 C $1.30 on 461K sh / 3,822 trades, vwap $1.28. Real and accelerating ignition; the 16:45 close is at +25% and near the $1.36 high. The IEX quote at 16:59:57 ET ($1.35/$1.36) shows it still near the high. The scanner's $1.22 lags SIP.
- Shared SIP volume context:
  ```
  # IPW shared SIP volume sip-ah-volume-v2; prior 2026-10-06 12+36zero/48 slots; floor 100; log-only
  # reconstructed as-of 2026-10-07T21:00:13+00:00; source fetched 2026-10-07T21:01:01.487237+00:00
  IPW 2026-10-07  VOLUME-CONTEXT 16:00ET start=2026-10-07T20:00:00+00:00 shares=21000 local=unknown prior-peak=10.5000x status=warmup
  IPW 2026-10-07  VOLUME-CONTEXT 16:05ET start=2026-10-07T20:05:00+00:00 shares=150 local=unknown prior-peak=0.0750x status=warmup
  IPW 2026-10-07  VOLUME-CONTEXT 16:10ET start=2026-10-07T20:10:00+00:00 shares=300 local=unknown prior-peak=0.1500x status=warmup
  IPW 2026-10-07  VOLUME-CONTEXT 16:15ET start=2026-10-07T20:15:00+00:00 shares=302 local=1.0067x prior-peak=0.1510x status=ok
  IPW 2026-10-07  VOLUME-CONTEXT 16:35ET start=2026-10-07T20:35:00+00:00 shares=165 local=1.6500x prior-peak=0.0825x status=floored
  IPW 2026-10-07  VOLUME-CONTEXT 16:40ET start=2026-10-07T20:40:00+00:00 shares=24954 local=249.5400x prior-peak=12.4770x status=floored
  IPW 2026-10-07  VOLUME-CONTEXT 16:45ET start=2026-10-07T20:45:00+00:00 shares=460704 local=2792.1455x prior-peak=230.3520x status=ok
  ```
- Book:
  ```
  IPW BOOK iex bid $1.35 x100 / ask $1.36 x100 @ 2026-10-07 16:59:57 ET age 1m08s two-sided spread 0.74% of ask
  IPW BOOK sip-15m bid $1.21 x1400 / ask $1.23 x100 @ 2026-10-07 16:46:05 ET age 15m00s two-sided spread 1.63% of ask
  IPW BOOK refresh +15s iex unchanged @ 2026-10-07 16:59:57 ET
  IPW BOOK verdict: IEX STALE 1m08s; SIP-15m TWO-SIDED (observed 2026-10-07 17:01:06 ET; log-only)
  ```
- Catalyst (2 searches): nothing dated today. Background: 1-for-9 reverse split effective 2026-08-07, a July AI computing hardware leasing plan, and Public.com listing next earnings on 2026-10-08 (tomorrow, not today). Grade: None.
- Multi-session context: not in `WINNERS_TRACKING.md`; Day% −8.0%, pure AH ignition. Strongest live build tonight; it needs a second qualifying AH scan at 23:30 to be eligible.

**ERNA** (float 1.1M, Ernexa Therapeutics, cell therapy):

- Spike bar: `ERNA 2026-10-07  SPIKE  16:36ET  +19%  $2.84  26 trades / 3k sh  (first co-spike bar) (as-of 17:00ET)`
- Third bar: `ERNA 2026-10-07  CONFIRM-3  NO ignition 16:35ET failed third-bar hold/volume as-of 17:00ET`
- SIP bars: 16:35 O $2.78 H $2.84 C $2.79 on 17.8K sh / 132 trades; 16:40 13.1K sh / 83 trades; 16:45 8.3K sh / 56 trades, pinned at $2.78–$2.79. Thin and shrinking: tens of K shares, under 150 trades per bar. Not an accumulating spike, so no book check.
- Shared SIP volume context:
  ```
  # ERNA shared SIP volume sip-ah-volume-v2; prior 2026-10-06 7+41zero/48 slots; floor 100; log-only
  # reconstructed as-of 2026-10-07T21:00:13+00:00; source fetched 2026-10-07T21:01:04.130774+00:00
  ERNA 2026-10-07  VOLUME-CONTEXT 16:00ET start=2026-10-07T20:00:00+00:00 shares=750 local=unknown prior-peak=0.2341x status=warmup
  ERNA 2026-10-07  VOLUME-CONTEXT 16:30ET start=2026-10-07T20:30:00+00:00 shares=147 local=1.4700x prior-peak=0.0459x status=floored
  ERNA 2026-10-07  VOLUME-CONTEXT 16:35ET start=2026-10-07T20:35:00+00:00 shares=17820 local=178.2000x prior-peak=5.5618x status=floored
  ERNA 2026-10-07  VOLUME-CONTEXT 16:40ET start=2026-10-07T20:40:00+00:00 shares=13135 local=89.3537x prior-peak=4.0996x status=ok
  ERNA 2026-10-07  VOLUME-CONTEXT 16:45ET start=2026-10-07T20:45:00+00:00 shares=8289 local=0.6311x prior-peak=2.5871x status=ok
  ```
- Catalyst (2 searches): nothing dated today. Background: 2026-09-29 selection for the Cell & Gene Meeting on the Mesa (Oct 5–7) and earlier ERNA-101 manufacturing updates. Grade: None.

**FMST** (float 13.2M): +7.1% AH, below threshold. Watch only.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
