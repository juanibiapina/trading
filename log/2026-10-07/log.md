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

## Scan 23:30 CEST (5:30 PM ET)

`python3 scripts/scan.py --all` ran at 17:30:20 ET (23:30:20 CEST) in the AFTERHOURS session and returned 8 hits.

Supplementary AH-change-only (>15%, not in volume pass): none
AH >10% at this snapshot (unrounded): CPHI, IPW, PROF

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| CPHI | [TV](https://www.tradingview.com/chart/?symbol=CPHI) | $0.85 | +32.6% | +10.5% | $0.94 | +46.5% | 3.3M | 6.4M | 0.5x | 40.3M | Pharmaceuticals: Major |
| IPW | [TV](https://www.tradingview.com/chart/?symbol=IPW) | $1.04 | -8.0% | +21.0% | $1.26 | +11.4% | 1.6M | 592K | 2.7x | 1.2M | Internet Retail |
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $1.59 | +45.9% | +7.2% | $1.71 | +56.4% | 1.2M | 13.3M | 0.1x | 4.4M | Miscellaneous Commercial Services |
| MTEN | [TV](https://www.tradingview.com/chart/?symbol=MTEN) | $1.10 | +14.7% | +5.5% | $1.16 | +21.0% | 534K | 7.7M | 0.1x | 6.1M | Industrial Machinery |
| ERNA | [TV](https://www.tradingview.com/chart/?symbol=ERNA) | $2.39 | +6.9% | +8.8% | $2.60 | +16.3% | 390K | 89K | 4.4x | 1.1M | Pharmaceuticals: Major |
| BFRG | [TV](https://www.tradingview.com/chart/?symbol=BFRG) | $0.71 | +2.8% | +5.1% | $0.74 | +8.1% | 275K | 7.3M | 0.0x | 16.0M | Packaged Software |
| LGCL | [TV](https://www.tradingview.com/chart/?symbol=LGCL) | $2.82 | +24.8% | +9.6% | $3.09 | +36.7% | 201K | 4.6M | 0.0x | 49K | Personnel Services |
| PROF | [TV](https://www.tradingview.com/chart/?symbol=PROF) | $5.68 | -6.6% | +17.1% | $6.65 | +9.4% | 118K | 155K | 0.8x | 35.4M | Medical Specialties |

### Evaluation notes

**Decision:** Enter IPW; skip PROF; watch CPHI. IPW and PROF now have 2 qualifying AH scans (23:00 and 23:30). CPHI is a first AH appearance above 10%. Before the buy, `positions` returned no open positions and `orders all` showed no IPW order today. SIP bars through 17:15 ET were available at 17:30 ET.

**IPW — ENTER (order working, unfilled at log time)** (float 1.2M, iPower, Internet Retail):

- Spike bar: `IPW 2026-10-07  SPIKE  16:44ET  +25%  $1.30  149 trades / 23k sh  (first co-spike bar) (as-of 17:30ET)`
- Third bar: `IPW 2026-10-07  CONFIRM-3  YES ignition 16:40ET 83.2x; confirmed 16:50ET $1.29 as-of 17:30ET`
- SIP bars: ignition 16:40, then 16:45 461K sh / 3,822 trades, 16:50 433K / 3,502, 16:55 368K / 2,117 (AH high $1.37), 17:00 363K / 2,108 (dip to $1.16, close $1.21), then 87K / 504, 111K / 803, 65K / 446 holding $1.24–$1.27. Real volume; per-bar volume is easing after 17:00, but price holds a $1.21–$1.30 base. The 17:15 close of $1.27 is 7% below the $1.37 high, and SIP corroborates the scanner's $1.26. Trajectory: spike at 16:45, then a hold within 20% of the high. The high came in the 16:55 bar, so the first-bar-spike rule does not apply.
- Shared SIP volume context:
  ```
  # IPW shared SIP volume sip-ah-volume-v2; prior 2026-10-06 12+36zero/48 slots; floor 100; log-only
  # reconstructed as-of 2026-10-07T21:30:20+00:00; source fetched 2026-10-07T21:31:38.326704+00:00
  IPW 2026-10-07  VOLUME-CONTEXT 16:00ET start=2026-10-07T20:00:00+00:00 shares=21000 local=unknown prior-peak=10.5000x status=warmup
  IPW 2026-10-07  VOLUME-CONTEXT 16:05ET start=2026-10-07T20:05:00+00:00 shares=150 local=unknown prior-peak=0.0750x status=warmup
  IPW 2026-10-07  VOLUME-CONTEXT 16:10ET start=2026-10-07T20:10:00+00:00 shares=300 local=unknown prior-peak=0.1500x status=warmup
  IPW 2026-10-07  VOLUME-CONTEXT 16:15ET start=2026-10-07T20:15:00+00:00 shares=302 local=1.0067x prior-peak=0.1510x status=ok
  IPW 2026-10-07  VOLUME-CONTEXT 16:35ET start=2026-10-07T20:35:00+00:00 shares=165 local=1.6500x prior-peak=0.0825x status=floored
  IPW 2026-10-07  VOLUME-CONTEXT 16:40ET start=2026-10-07T20:40:00+00:00 shares=24954 local=249.5400x prior-peak=12.4770x status=floored
  IPW 2026-10-07  VOLUME-CONTEXT 16:45ET start=2026-10-07T20:45:00+00:00 shares=460704 local=2792.1455x prior-peak=230.3520x status=ok
  IPW 2026-10-07  VOLUME-CONTEXT 16:50ET start=2026-10-07T20:50:00+00:00 shares=433447 local=17.3698x prior-peak=216.7235x status=ok
  IPW 2026-10-07  VOLUME-CONTEXT 16:55ET start=2026-10-07T20:55:00+00:00 shares=368119 local=0.8493x prior-peak=184.0595x status=ok
  IPW 2026-10-07  VOLUME-CONTEXT 17:00ET start=2026-10-07T21:00:00+00:00 shares=362713 local=0.8368x prior-peak=181.3565x status=ok
  IPW 2026-10-07  VOLUME-CONTEXT 17:05ET start=2026-10-07T21:05:00+00:00 shares=87466 local=0.2376x prior-peak=43.7330x status=ok
  IPW 2026-10-07  VOLUME-CONTEXT 17:10ET start=2026-10-07T21:10:00+00:00 shares=111180 local=0.3065x prior-peak=55.5900x status=ok
  IPW 2026-10-07  VOLUME-CONTEXT 17:15ET start=2026-10-07T21:15:00+00:00 shares=65130 local=0.5858x prior-peak=32.5650x status=ok
  ```
- Book:
  ```
  IPW BOOK iex bid $1.35 x100 / ask $1.36 x100 @ 2026-10-07 16:59:57 ET age 31m53s two-sided spread 0.74% of ask
  IPW BOOK sip-15m bid $1.27 x1000 / ask $1.28 x300 @ 2026-10-07 17:16:50 ET age 15m01s two-sided spread 0.78% of ask
  IPW BOOK refresh +15s iex unchanged @ 2026-10-07 16:59:57 ET
  IPW BOOK verdict: IEX STALE 31m53s; SIP-15m TWO-SIDED (observed 2026-10-07 17:31:50 ET; log-only)
  ```
- Catalyst (re-run, 2 searches): nothing dated 2026-10-07. Search turned up an ad-hoc-news item, "iPower stock gained 8.93 percent after fiscal 2026 results" (fiscal 2026 revenue $19.96M, down 68.4%; net loss $11.62M). It was listed as 1 day old, but its exact release date is unverified, so it is background. Other items: the July AI hardware leasing plan and the August 1-for-9 reverse split. Grade: None. Entering with the no-catalyst concern noted.
- Multi-session context: not in `WINNERS_TRACKING.md`. Day% −8.0% and previous close $1.13, so this is a fresh day-1 AH igniter.
- Gates: 2 AH scans >10% (+17.3% at 23:00, +21.0% at 23:30), float 1.2M, Day% −8.0%, Total% +11.4% (under the +150% ceiling), `tradable=true`, two-sided book.
- Order: the first limit of 76 sh @ $1.31 (SIP-15m ask $1.28 + 3¢) rested unfilled for about 1.5 minutes and was canceled (`75f1e6ad`). It was resubmitted as 72 sh @ $1.38 (`825706f4`), 2¢ above the stale IEX ask of $1.36. The order was still `new` with 0 filled at 17:37 ET. The IEX quote has not updated since 16:59:57 ET, and the paper engine appears to need a fresh quote to fill. The order stays working with an extended-hours day TIF (expires 20:00 ET). The next pulse must check `orders all` and record any fill in Paper Trades and `OPEN_POSITIONS.md`.
- CHASE-CAP: qualifying $1.26 / +11.4%; limit $1.38 / +22.1% from the $1.13 close; gap +10.7 pts if filled at the limit. Well below the fade zone (>~+120%).

**PROF — SKIP: thin, not accumulating** (float 35.4M, Profound Medical; catalyst B, preliminary Q3 revenue on GlobeNewswire 2026-10-07 ~16:15 ET):

- Spike bar: `PROF 2026-10-07  SPIKE  16:36ET  +21%  $6.87  69 trades / 2k sh  (first co-spike bar) (as-of 17:30ET)`
- Third bar: `PROF 2026-10-07  CONFIRM-3  NO ignition 16:35ET failed third-bar hold/volume as-of 17:30ET`
- SIP bars: the 16:35 peak bar ($7.51 high) had 51.8K sh / 659 trades. Since then: 40.5K / 447, 7.5K / 201, 15.2K / 174, 8.7K / 70, 4.8K / 48, 4.6K / 36, 6.0K / 40, 2.0K / 29. The price drifts at $6.62–$6.80 (11% off the high). AH% slipped from +21.3% to +17.1% across the two scans. Per-bar volume is single-digit K shares with tens of trades, which fails the SIP volume confirmation. This is a thin drift off an early 16:35 peak.
- Shared SIP volume context:
  ```
  # PROF shared SIP volume sip-ah-volume-v2; prior 2026-10-06 1+47zero/48 slots; floor 100; log-only
  # reconstructed as-of 2026-10-07T21:30:20+00:00; source fetched 2026-10-07T21:31:42.005592+00:00
  PROF 2026-10-07  VOLUME-CONTEXT 16:00ET start=2026-10-07T20:00:00+00:00 shares=2919 local=unknown prior-peak=4.2121x status=warmup
  PROF 2026-10-07  VOLUME-CONTEXT 16:25ET start=2026-10-07T20:25:00+00:00 shares=500 local=5.0000x prior-peak=0.7215x status=floored
  PROF 2026-10-07  VOLUME-CONTEXT 16:30ET start=2026-10-07T20:30:00+00:00 shares=4110 local=41.1000x prior-peak=5.9307x status=floored
  PROF 2026-10-07  VOLUME-CONTEXT 16:35ET start=2026-10-07T20:35:00+00:00 shares=51786 local=103.5720x prior-peak=74.7273x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 16:40ET start=2026-10-07T20:40:00+00:00 shares=40539 local=9.8635x prior-peak=58.4978x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 16:45ET start=2026-10-07T20:45:00+00:00 shares=7528 local=0.1857x prior-peak=10.8629x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 16:50ET start=2026-10-07T20:50:00+00:00 shares=15162 local=0.3740x prior-peak=21.8788x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 16:55ET start=2026-10-07T20:55:00+00:00 shares=8667 local=0.5716x prior-peak=12.5065x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 17:00ET start=2026-10-07T21:00:00+00:00 shares=4761 local=0.5493x prior-peak=6.8701x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 17:05ET start=2026-10-07T21:05:00+00:00 shares=4604 local=0.5312x prior-peak=6.6436x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 17:10ET start=2026-10-07T21:10:00+00:00 shares=5952 local=1.2502x prior-peak=8.5887x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 17:15ET start=2026-10-07T21:15:00+00:00 shares=2019 local=0.4241x prior-peak=2.9134x status=ok
  ```
- No book check: SIP volume is not accumulating.

**CPHI — Watch (first AH scan >10%)** (float 40.3M, China Pharma Holdings; 21:30 watch name, +7.1% at 22:45):

- Spike bar: `CPHI 2026-10-07  SPIKE  17:02ET  +16%  $0.99  513 trades / 170k sh  (first co-spike bar) (as-of 17:30ET)`
- Third bar: `CPHI 2026-10-07  CONFIRM-3  NO ignition 17:00ET failed third-bar hold/volume as-of 17:30ET`
- SIP bars: second leg at 17:00 (652K sh / 1,822 trades, close $0.99) and 17:05 (610K / 2,454, high $1.04), then 204K / 750 and 185K / 559 easing to $0.94–$0.95. Real volume, 10% off the $1.04 high.
- Shared SIP volume context:
  ```
  # CPHI shared SIP volume sip-ah-volume-v2; prior 2026-10-06 15+33zero/48 slots; floor 100; log-only
  # reconstructed as-of 2026-10-07T21:30:20+00:00; source fetched 2026-10-07T21:31:47.537734+00:00
  CPHI 2026-10-07  VOLUME-CONTEXT 16:00ET start=2026-10-07T20:00:00+00:00 shares=356426 local=unknown prior-peak=10.0021x status=warmup
  CPHI 2026-10-07  VOLUME-CONTEXT 16:05ET start=2026-10-07T20:05:00+00:00 shares=325964 local=unknown prior-peak=9.1473x status=warmup
  CPHI 2026-10-07  VOLUME-CONTEXT 16:10ET start=2026-10-07T20:10:00+00:00 shares=68702 local=unknown prior-peak=1.9279x status=warmup
  CPHI 2026-10-07  VOLUME-CONTEXT 16:15ET start=2026-10-07T20:15:00+00:00 shares=58420 local=0.1792x prior-peak=1.6394x status=ok
  CPHI 2026-10-07  VOLUME-CONTEXT 16:20ET start=2026-10-07T20:20:00+00:00 shares=38957 local=0.5670x prior-peak=1.0932x status=ok
  CPHI 2026-10-07  VOLUME-CONTEXT 16:25ET start=2026-10-07T20:25:00+00:00 shares=441505 local=7.5574x prior-peak=12.3896x status=ok
  CPHI 2026-10-07  VOLUME-CONTEXT 16:30ET start=2026-10-07T20:30:00+00:00 shares=206395 local=3.5330x prior-peak=5.7919x status=ok
  CPHI 2026-10-07  VOLUME-CONTEXT 16:35ET start=2026-10-07T20:35:00+00:00 shares=263320 local=1.2758x prior-peak=7.3894x status=ok
  CPHI 2026-10-07  VOLUME-CONTEXT 16:40ET start=2026-10-07T20:40:00+00:00 shares=88456 local=0.3359x prior-peak=2.4823x status=ok
  CPHI 2026-10-07  VOLUME-CONTEXT 16:45ET start=2026-10-07T20:45:00+00:00 shares=57116 local=0.2767x prior-peak=1.6028x status=ok
  CPHI 2026-10-07  VOLUME-CONTEXT 16:50ET start=2026-10-07T20:50:00+00:00 shares=84055 local=0.9502x prior-peak=2.3588x status=ok
  CPHI 2026-10-07  VOLUME-CONTEXT 16:55ET start=2026-10-07T20:55:00+00:00 shares=112461 local=1.3379x prior-peak=3.1559x status=ok
  CPHI 2026-10-07  VOLUME-CONTEXT 17:00ET start=2026-10-07T21:00:00+00:00 shares=652217 local=7.7594x prior-peak=18.3027x status=ok
  CPHI 2026-10-07  VOLUME-CONTEXT 17:05ET start=2026-10-07T21:05:00+00:00 shares=610375 local=5.4274x prior-peak=17.1285x status=ok
  CPHI 2026-10-07  VOLUME-CONTEXT 17:10ET start=2026-10-07T21:10:00+00:00 shares=204110 local=0.3344x prior-peak=5.7278x status=ok
  CPHI 2026-10-07  VOLUME-CONTEXT 17:15ET start=2026-10-07T21:15:00+00:00 shares=184928 local=0.3030x prior-peak=5.1895x status=ok
  ```
- Book:
  ```
  CPHI BOOK iex bid $0.7403 x100 / ask $0.9897 x100 @ 2026-10-07 16:00:00 ET age 1h31m two-sided spread 25.20% of ask
  CPHI BOOK sip-15m bid $0.9106 x800 / ask $0.9176 x2000 @ 2026-10-07 17:16:50 ET age 15m00s two-sided spread 0.76% of ask
  CPHI BOOK refresh +15s iex unchanged @ 2026-10-07 16:00:00 ET
  CPHI BOOK verdict: IEX STALE 1h31m; SIP-15m TWO-SIDED (observed 2026-10-07 17:31:50 ET; log-only)
  ```
- Catalyst (2 searches): nothing dated today. Background: the 2026-07-15 "no known events" unusual-activity statement and the 2026-07-23 $5.0M registered direct offering close. Grade: None.
- Multi-session context: not in `WINNERS_TRACKING.md`; previous close $0.64, so today's +32.6% regular session is day 1. `tradable=true`. Total% +46.5%. It needs a second AH scan above 10% at 00:00 to qualify.

**Dropped below 10%:** NCPL (+7.2%, from +10.1%), ERNA (+8.8%, from +16.3%). MTEN, BFRG, and LGCL are under threshold.

## Scan 00:00 CEST (6:00 PM ET)

`python3 scripts/scan.py --all` ran at 18:00:11 ET (00:00:11 CEST) in the AFTERHOURS session and returned 8 hits.

Supplementary AH-change-only (>15%, not in volume pass): none
AH >10% at this snapshot (unrounded): BFRG, CPHI, IPW, LGCL, PROF

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| CPHI | [TV](https://www.tradingview.com/chart/?symbol=CPHI) | $0.85 | +32.6% | +24.7% | $1.06 | +65.3% | 6.8M | 6.8M | 1.0x | 40.3M | Pharmaceuticals: Major |
| IPW | [TV](https://www.tradingview.com/chart/?symbol=IPW) | $1.04 | -8.0% | +24.0% | $1.29 | +14.2% | 2.9M | 732K | 3.9x | 1.2M | Internet Retail |
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $1.59 | +45.9% | +8.2% | $1.72 | +57.8% | 1.4M | 13.3M | 0.1x | 4.4M | Miscellaneous Commercial Services |
| VCIG | [TV](https://www.tradingview.com/chart/?symbol=VCIG) | $0.77 | -45.3% | +7.8% | $0.83 | -41.1% | 1.0M | 5.4M | 0.2x | 1.0M | Miscellaneous Commercial Services |
| BFRG | [TV](https://www.tradingview.com/chart/?symbol=BFRG) | $0.71 | +2.8% | +15.3% | $0.82 | +18.6% | 879K | 7.4M | 0.1x | 16.0M | Packaged Software |
| FMST | [TV](https://www.tradingview.com/chart/?symbol=FMST) | $0.56 | +13.2% | +6.0% | $0.59 | +20.0% | 726K | 627K | 1.2x | 13.2M | Other Metals/Minerals |
| LGCL | [TV](https://www.tradingview.com/chart/?symbol=LGCL) | $2.82 | +24.8% | +10.6% | $3.12 | +38.1% | 262K | 4.6M | 0.1x | 49K | Personnel Services |
| PROF | [TV](https://www.tradingview.com/chart/?symbol=PROF) | $5.68 | -6.6% | +18.5% | $6.73 | +10.7% | 129K | 157K | 0.8x | 35.4M | Medical Specialties |

### Evaluation notes

**Decision:** Enter CPHI (filled 94 sh @ $0.9978). IPW's 23:30 order filled at 17:38:57 ET (72 sh @ $1.38) and is now recorded. Skip PROF again (thin). Watch BFRG and LGCL (first AH scan above 10%). Before the CPHI buy, `positions` showed only IPW and `orders open` was empty; no CPHI order today. SIP bars through 17:45 ET were available at 18:00 ET.

**IPW — entered at 23:30, fill confirmed** (float 1.2M, Grade None):

- Order `825706f4` filled 72 sh @ $1.38 at 17:38:57 ET (21:38:57Z). Fill Total% +22.1% from the $1.13 previous close; CHASE-CAP gap +10.7 pts vs the qualifying $1.26 / +11.4%, far below the fade zone.
- Spike bar: `IPW 2026-10-07  SPIKE  16:44ET  +25%  $1.30  149 trades / 23k sh  (first co-spike bar) (as-of 18:00ET)`
- Third bar: `IPW 2026-10-07  CONFIRM-3  YES ignition 16:40ET 83.2x; confirmed 16:50ET $1.29 as-of 18:00ET`
- SIP bars: second leg at 17:30 (410K sh / 2,319 trades, high $1.48) and 17:35 (528K / 2,892, new AH high $1.52), then 278K / 1,384 down to $1.30 and 183K / 1,059 closing $1.36. Still building on real volume; the 17:45 close is 11% off the new high. Position at 18:02 ET: now $1.35, −2.2%.
- Shared SIP volume context:
  ```
  # IPW shared SIP volume sip-ah-volume-v2; prior 2026-10-06 12+36zero/48 slots; floor 100; log-only
  # reconstructed as-of 2026-10-07T22:00:11+00:00; source fetched 2026-10-07T22:01:03.631946+00:00
  IPW 2026-10-07  VOLUME-CONTEXT 16:00ET start=2026-10-07T20:00:00+00:00 shares=21000 local=unknown prior-peak=10.5000x status=warmup
  IPW 2026-10-07  VOLUME-CONTEXT 16:05ET start=2026-10-07T20:05:00+00:00 shares=150 local=unknown prior-peak=0.0750x status=warmup
  IPW 2026-10-07  VOLUME-CONTEXT 16:10ET start=2026-10-07T20:10:00+00:00 shares=300 local=unknown prior-peak=0.1500x status=warmup
  IPW 2026-10-07  VOLUME-CONTEXT 16:15ET start=2026-10-07T20:15:00+00:00 shares=302 local=1.0067x prior-peak=0.1510x status=ok
  IPW 2026-10-07  VOLUME-CONTEXT 16:35ET start=2026-10-07T20:35:00+00:00 shares=165 local=1.6500x prior-peak=0.0825x status=floored
  IPW 2026-10-07  VOLUME-CONTEXT 16:40ET start=2026-10-07T20:40:00+00:00 shares=24954 local=249.5400x prior-peak=12.4770x status=floored
  IPW 2026-10-07  VOLUME-CONTEXT 16:45ET start=2026-10-07T20:45:00+00:00 shares=460704 local=2792.1455x prior-peak=230.3520x status=ok
  IPW 2026-10-07  VOLUME-CONTEXT 16:50ET start=2026-10-07T20:50:00+00:00 shares=433447 local=17.3698x prior-peak=216.7235x status=ok
  IPW 2026-10-07  VOLUME-CONTEXT 16:55ET start=2026-10-07T20:55:00+00:00 shares=368119 local=0.8493x prior-peak=184.0595x status=ok
  IPW 2026-10-07  VOLUME-CONTEXT 17:00ET start=2026-10-07T21:00:00+00:00 shares=362713 local=0.8368x prior-peak=181.3565x status=ok
  IPW 2026-10-07  VOLUME-CONTEXT 17:05ET start=2026-10-07T21:05:00+00:00 shares=87466 local=0.2376x prior-peak=43.7330x status=ok
  IPW 2026-10-07  VOLUME-CONTEXT 17:10ET start=2026-10-07T21:10:00+00:00 shares=111180 local=0.3065x prior-peak=55.5900x status=ok
  IPW 2026-10-07  VOLUME-CONTEXT 17:15ET start=2026-10-07T21:15:00+00:00 shares=65130 local=0.5858x prior-peak=32.5650x status=ok
  IPW 2026-10-07  VOLUME-CONTEXT 17:20ET start=2026-10-07T21:20:00+00:00 shares=31702 local=0.3624x prior-peak=15.8510x status=ok
  IPW 2026-10-07  VOLUME-CONTEXT 17:25ET start=2026-10-07T21:25:00+00:00 shares=98760 local=1.5164x prior-peak=49.3800x status=ok
  IPW 2026-10-07  VOLUME-CONTEXT 17:30ET start=2026-10-07T21:30:00+00:00 shares=409810 local=6.2922x prior-peak=204.9050x status=ok
  IPW 2026-10-07  VOLUME-CONTEXT 17:35ET start=2026-10-07T21:35:00+00:00 shares=528173 local=5.3480x prior-peak=264.0865x status=ok
  IPW 2026-10-07  VOLUME-CONTEXT 17:40ET start=2026-10-07T21:40:00+00:00 shares=278175 local=0.6788x prior-peak=139.0875x status=ok
  IPW 2026-10-07  VOLUME-CONTEXT 17:45ET start=2026-10-07T21:45:00+00:00 shares=183046 local=0.4467x prior-peak=91.5230x status=ok
  ```
- Book:
  ```
  IPW BOOK iex bid $1.35 x100 / ask $1.36 x100 @ 2026-10-07 16:59:57 ET age 1h01m two-sided spread 0.74% of ask
  IPW BOOK sip-15m bid $1.29 x600 / ask $1.30 x600 @ 2026-10-07 17:46:34 ET age 15m03s two-sided spread 0.77% of ask
  IPW BOOK refresh +15s iex unchanged @ 2026-10-07 16:59:57 ET
  IPW BOOK verdict: IEX STALE 1h01m; SIP-15m TWO-SIDED (observed 2026-10-07 18:01:37 ET; log-only)
  ```

**CPHI — ENTER, filled 94 sh @ $0.9978** (float 40.3M, China Pharma Holdings, Pharmaceuticals):

- Spike bar: `CPHI 2026-10-07  SPIKE  17:02ET  +16%  $0.99  513 trades / 170k sh  (first co-spike bar) (as-of 18:00ET)`
- Third bar: `CPHI 2026-10-07  CONFIRM-3  NO ignition 17:00ET failed third-bar hold/volume as-of 18:00ET`
- SIP bars: after the 17:00–17:05 leg (high $1.04) and a dip to $0.90, a third leg at 17:20 (515K sh / 1,735 trades, close $1.08), 17:25 (1.28M / 4,615), 17:30 (776K / 3,499, new AH high $1.16), 17:35 (541K / 2,321, close $1.13), then 393K / 1,566 and 318K / 1,286 easing to $1.05. Real, accumulating volume (hundreds of K shares, thousands of trades per bar). SIP vwap $1.05 corroborates the scanner's $1.06. Trajectory: BUILD, with successive higher highs ($1.04 → $1.16) after 17:00 ET; the 17:45 close is 9.5% off the high, inside the 20% hold band. The AH high was not in the first AH bar, so the first-bar-spike rule does not apply.
- Shared SIP volume context:
  ```
  # CPHI shared SIP volume sip-ah-volume-v2; prior 2026-10-06 15+33zero/48 slots; floor 100; log-only
  # reconstructed as-of 2026-10-07T22:00:11+00:00; source fetched 2026-10-07T22:00:48.340913+00:00
  CPHI 2026-10-07  VOLUME-CONTEXT 16:00ET start=2026-10-07T20:00:00+00:00 shares=356426 local=unknown prior-peak=10.0021x status=warmup
  CPHI 2026-10-07  VOLUME-CONTEXT 16:05ET start=2026-10-07T20:05:00+00:00 shares=325964 local=unknown prior-peak=9.1473x status=warmup
  CPHI 2026-10-07  VOLUME-CONTEXT 16:10ET start=2026-10-07T20:10:00+00:00 shares=68702 local=unknown prior-peak=1.9279x status=warmup
  CPHI 2026-10-07  VOLUME-CONTEXT 16:15ET start=2026-10-07T20:15:00+00:00 shares=58420 local=0.1792x prior-peak=1.6394x status=ok
  CPHI 2026-10-07  VOLUME-CONTEXT 16:20ET start=2026-10-07T20:20:00+00:00 shares=38957 local=0.5670x prior-peak=1.0932x status=ok
  CPHI 2026-10-07  VOLUME-CONTEXT 16:25ET start=2026-10-07T20:25:00+00:00 shares=441505 local=7.5574x prior-peak=12.3896x status=ok
  CPHI 2026-10-07  VOLUME-CONTEXT 16:30ET start=2026-10-07T20:30:00+00:00 shares=206395 local=3.5330x prior-peak=5.7919x status=ok
  CPHI 2026-10-07  VOLUME-CONTEXT 16:35ET start=2026-10-07T20:35:00+00:00 shares=263320 local=1.2758x prior-peak=7.3894x status=ok
  CPHI 2026-10-07  VOLUME-CONTEXT 16:40ET start=2026-10-07T20:40:00+00:00 shares=88456 local=0.3359x prior-peak=2.4823x status=ok
  CPHI 2026-10-07  VOLUME-CONTEXT 16:45ET start=2026-10-07T20:45:00+00:00 shares=57116 local=0.2767x prior-peak=1.6028x status=ok
  CPHI 2026-10-07  VOLUME-CONTEXT 16:50ET start=2026-10-07T20:50:00+00:00 shares=84055 local=0.9502x prior-peak=2.3588x status=ok
  CPHI 2026-10-07  VOLUME-CONTEXT 16:55ET start=2026-10-07T20:55:00+00:00 shares=112461 local=1.3379x prior-peak=3.1559x status=ok
  CPHI 2026-10-07  VOLUME-CONTEXT 17:00ET start=2026-10-07T21:00:00+00:00 shares=652217 local=7.7594x prior-peak=18.3027x status=ok
  CPHI 2026-10-07  VOLUME-CONTEXT 17:05ET start=2026-10-07T21:05:00+00:00 shares=610375 local=5.4274x prior-peak=17.1285x status=ok
  CPHI 2026-10-07  VOLUME-CONTEXT 17:10ET start=2026-10-07T21:10:00+00:00 shares=204110 local=0.3344x prior-peak=5.7278x status=ok
  CPHI 2026-10-07  VOLUME-CONTEXT 17:15ET start=2026-10-07T21:15:00+00:00 shares=184928 local=0.3030x prior-peak=5.1895x status=ok
  CPHI 2026-10-07  VOLUME-CONTEXT 17:20ET start=2026-10-07T21:20:00+00:00 shares=514727 local=2.5218x prior-peak=14.4444x status=ok
  CPHI 2026-10-07  VOLUME-CONTEXT 17:25ET start=2026-10-07T21:25:00+00:00 shares=1281472 local=6.2783x prior-peak=35.9610x status=ok
  CPHI 2026-10-07  VOLUME-CONTEXT 17:30ET start=2026-10-07T21:30:00+00:00 shares=776055 local=1.5077x prior-peak=21.7779x status=ok
  CPHI 2026-10-07  VOLUME-CONTEXT 17:35ET start=2026-10-07T21:35:00+00:00 shares=541391 local=0.6976x prior-peak=15.1927x status=ok
  CPHI 2026-10-07  VOLUME-CONTEXT 17:40ET start=2026-10-07T21:40:00+00:00 shares=393245 local=0.5067x prior-peak=11.0354x status=ok
  CPHI 2026-10-07  VOLUME-CONTEXT 17:45ET start=2026-10-07T21:45:00+00:00 shares=317506 local=0.5865x prior-peak=8.9099x status=ok
  ```
- Book:
  ```
  CPHI BOOK iex bid $0.7403 x100 / ask $0.9897 x100 @ 2026-10-07 16:00:00 ET age 2h01m two-sided spread 25.20% of ask
  CPHI BOOK sip-15m bid $1.05 x12900 / ask $1.06 x1000 @ 2026-10-07 17:46:37 ET age 15m00s two-sided spread 0.94% of ask
  CPHI BOOK refresh +15s iex unchanged @ 2026-10-07 16:00:00 ET
  CPHI BOOK verdict: IEX STALE 2h01m; SIP-15m TWO-SIDED (observed 2026-10-07 18:01:37 ET; log-only)
  ```
- Catalyst (re-run, 2 searches; 4 total tonight): nothing dated 2026-10-07. Background only: the 2026-07-15 "no known events" unusual-activity statement and the 2026-07-23 $5.0M registered direct offering close (PR Newswire). Grade: None. Entering with the no-catalyst concern noted.
- Multi-session context: not in `WINNERS_TRACKING.md`; previous close $0.64, today's +32.6% regular session is day 1 of the move.
- Gates: 2 AH scans >10% (+10.5% at 23:30, +24.7% at 00:00), float 40.3M (<50M), Day% +32.6%, Total% +65.3% (under the +150% ceiling), `tradable=true`, two-sided book (IEX ask $0.99 x100, SIP-15m ask $1.06 x1000).
- Order `58102d51`: 94 sh, limit $1.09 (SIP-15m ask $1.06 + 3¢), filled @ $0.9978 at 18:02:02 ET. The paper engine filled against the stale 16:00 ET IEX ask ($0.99), about 6% below the SIP-15m ask, so the fill price is optimistic versus the real market. Fill Total% +55.7% from the $0.641 previous close. CHASE-CAP: qualifying $0.94 / +46.5% at 23:30; fill $0.9978 / +55.7%; gap +9.2 pts. Well below the fade zone.

**PROF — SKIP: thin, not accumulating (3rd AH scan >10%)** (float 35.4M, catalyst B):

- Spike bar: `PROF 2026-10-07  SPIKE  16:36ET  +21%  $6.87  69 trades / 2k sh  (first co-spike bar) (as-of 18:00ET)`
- Third bar: `PROF 2026-10-07  CONFIRM-3  NO ignition 16:35ET failed third-bar hold/volume as-of 18:00ET`
- SIP bars 17:20–17:45: 3.8K, 1.8K, 1.5K, 2.6K, 0.2K, 1.6K sh with 7–14 trades per bar, pinned at $6.73–$6.85 (10% off the $7.51 high). Volume keeps thinning; same skip as 23:30.
- Shared SIP volume context:
  ```
  # PROF shared SIP volume sip-ah-volume-v2; prior 2026-10-06 1+47zero/48 slots; floor 100; log-only
  # reconstructed as-of 2026-10-07T22:00:11+00:00; source fetched 2026-10-07T22:00:58.838715+00:00
  PROF 2026-10-07  VOLUME-CONTEXT 16:00ET start=2026-10-07T20:00:00+00:00 shares=2919 local=unknown prior-peak=4.2121x status=warmup
  PROF 2026-10-07  VOLUME-CONTEXT 16:25ET start=2026-10-07T20:25:00+00:00 shares=500 local=5.0000x prior-peak=0.7215x status=floored
  PROF 2026-10-07  VOLUME-CONTEXT 16:30ET start=2026-10-07T20:30:00+00:00 shares=4110 local=41.1000x prior-peak=5.9307x status=floored
  PROF 2026-10-07  VOLUME-CONTEXT 16:35ET start=2026-10-07T20:35:00+00:00 shares=51786 local=103.5720x prior-peak=74.7273x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 16:40ET start=2026-10-07T20:40:00+00:00 shares=40539 local=9.8635x prior-peak=58.4978x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 16:45ET start=2026-10-07T20:45:00+00:00 shares=7528 local=0.1857x prior-peak=10.8629x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 16:50ET start=2026-10-07T20:50:00+00:00 shares=15162 local=0.3740x prior-peak=21.8788x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 16:55ET start=2026-10-07T20:55:00+00:00 shares=8667 local=0.5716x prior-peak=12.5065x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 17:00ET start=2026-10-07T21:00:00+00:00 shares=4761 local=0.5493x prior-peak=6.8701x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 17:05ET start=2026-10-07T21:05:00+00:00 shares=4604 local=0.5312x prior-peak=6.6436x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 17:10ET start=2026-10-07T21:10:00+00:00 shares=5952 local=1.2502x prior-peak=8.5887x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 17:15ET start=2026-10-07T21:15:00+00:00 shares=2019 local=0.4241x prior-peak=2.9134x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 17:20ET start=2026-10-07T21:20:00+00:00 shares=3761 local=0.8169x prior-peak=5.4271x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 17:25ET start=2026-10-07T21:25:00+00:00 shares=1810 local=0.4813x prior-peak=2.6118x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 17:30ET start=2026-10-07T21:30:00+00:00 shares=1506 local=0.7459x prior-peak=2.1732x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 17:35ET start=2026-10-07T21:35:00+00:00 shares=2611 local=1.4425x prior-peak=3.7677x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 17:40ET start=2026-10-07T21:40:00+00:00 shares=178 local=0.0983x prior-peak=0.2569x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 17:45ET start=2026-10-07T21:45:00+00:00 shares=1572 local=1.0438x prior-peak=2.2684x status=ok
  ```

**BFRG — Watch (first AH scan >10%)** (float 16.0M, Bullfrog AI, Packaged Software; `tradable=true`):

- Spike bar: `BFRG 2026-10-07  SPIKE  17:27ET  +15%  $0.82  135 trades / 51k sh  (first co-spike bar) (as-of 18:00ET)`
- Third bar: `BFRG 2026-10-07  CONFIRM-3  NO no local-volume new-high ignition as-of 18:00ET`
- SIP bars: flat $0.72–$0.76 until 17:15 (255K sh / 434 trades, high $0.80), then 17:25 (169K / 479, high $0.82); after that 57K / 136, 111K / 179, 16K / 65, 78K / 98 holding $0.79–$0.82. Tens to low hundreds of K shares and only tens to hundreds of trades per bar: borderline-thin. SIP corroborates the scanner's $0.82. Catalyst search deferred to the next scan if it holds >10%. No book check (volume not clearly accumulating).
- Shared SIP volume context:
  ```
  # BFRG shared SIP volume sip-ah-volume-v2; prior 2026-10-06 48+0zero/48 slots; floor 100; log-only
  # reconstructed as-of 2026-10-07T22:00:11+00:00; source fetched 2026-10-07T22:00:43.781206+00:00
  BFRG 2026-10-07  VOLUME-CONTEXT 16:00ET start=2026-10-07T20:00:00+00:00 shares=37935 local=unknown prior-peak=0.3961x status=warmup
  BFRG 2026-10-07  VOLUME-CONTEXT 16:05ET start=2026-10-07T20:05:00+00:00 shares=6770 local=unknown prior-peak=0.0707x status=warmup
  BFRG 2026-10-07  VOLUME-CONTEXT 16:10ET start=2026-10-07T20:10:00+00:00 shares=18596 local=unknown prior-peak=0.1942x status=warmup
  BFRG 2026-10-07  VOLUME-CONTEXT 16:15ET start=2026-10-07T20:15:00+00:00 shares=3623 local=0.1948x prior-peak=0.0378x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 16:20ET start=2026-10-07T20:20:00+00:00 shares=12785 local=1.8885x prior-peak=0.1335x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 16:25ET start=2026-10-07T20:25:00+00:00 shares=1794 local=0.1403x prior-peak=0.0187x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 16:30ET start=2026-10-07T20:30:00+00:00 shares=19557 local=5.3980x prior-peak=0.2042x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 16:35ET start=2026-10-07T20:35:00+00:00 shares=92266 local=7.2167x prior-peak=0.9634x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 16:40ET start=2026-10-07T20:40:00+00:00 shares=29291 local=1.4977x prior-peak=0.3059x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 16:45ET start=2026-10-07T20:45:00+00:00 shares=8289 local=0.2830x prior-peak=0.0866x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 16:50ET start=2026-10-07T20:50:00+00:00 shares=2089 local=0.0713x prior-peak=0.0218x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 16:55ET start=2026-10-07T20:55:00+00:00 shares=15435 local=1.8621x prior-peak=0.1612x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 17:00ET start=2026-10-07T21:00:00+00:00 shares=8740 local=1.0544x prior-peak=0.0913x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 17:05ET start=2026-10-07T21:05:00+00:00 shares=1908 local=0.2183x prior-peak=0.0199x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 17:10ET start=2026-10-07T21:10:00+00:00 shares=25567 local=2.9253x prior-peak=0.2670x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 17:15ET start=2026-10-07T21:15:00+00:00 shares=255072 local=29.1844x prior-peak=2.6634x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 17:20ET start=2026-10-07T21:20:00+00:00 shares=11668 local=0.4564x prior-peak=0.1218x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 17:25ET start=2026-10-07T21:25:00+00:00 shares=169118 local=6.6147x prior-peak=1.7659x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 17:30ET start=2026-10-07T21:30:00+00:00 shares=56583 local=0.3346x prior-peak=0.5908x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 17:35ET start=2026-10-07T21:35:00+00:00 shares=111222 local=1.9656x prior-peak=1.1614x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 17:40ET start=2026-10-07T21:40:00+00:00 shares=16265 local=0.1462x prior-peak=0.1698x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 17:45ET start=2026-10-07T21:45:00+00:00 shares=78390 local=1.3854x prior-peak=0.8185x status=ok
  ```

**LGCL — Watch (first AH scan >10%)** (float 49K, Lucas GC, Personnel Services; `tradable=true`; +9.6% at 23:30):

- Spike bar: `LGCL 2026-10-07  NO-SPIKE  peak +15% @16:59ET  (no bar cleared +15% on a volume co-spike) (as-of 18:00ET)`
- Third bar: `LGCL 2026-10-07  CONFIRM-3  NO ignition 16:55ET failed third-bar hold/volume as-of 18:00ET`
- SIP bars: high $3.24 at 16:55 (38K sh / 401 trades), since then $3.00–$3.19 on 4–43K sh and 72–438 trades per bar; 17:45 close $3.12, 4% off the high. Thin drift: tens of K shares and hundreds of trades per bar. Fails the SIP accumulation check if it qualifies at 00:30.
- Shared SIP volume context:
  ```
  # LGCL shared SIP volume sip-ah-volume-v2; prior 2026-10-06 16+32zero/48 slots; floor 100; log-only
  # reconstructed as-of 2026-10-07T22:00:11+00:00; source fetched 2026-10-07T22:00:53.420591+00:00
  LGCL 2026-10-07  VOLUME-CONTEXT 16:00ET start=2026-10-07T20:00:00+00:00 shares=29711 local=unknown prior-peak=14.7522x status=warmup
  LGCL 2026-10-07  VOLUME-CONTEXT 16:05ET start=2026-10-07T20:05:00+00:00 shares=6291 local=unknown prior-peak=3.1236x status=warmup
  LGCL 2026-10-07  VOLUME-CONTEXT 16:10ET start=2026-10-07T20:10:00+00:00 shares=9623 local=unknown prior-peak=4.7781x status=warmup
  LGCL 2026-10-07  VOLUME-CONTEXT 16:15ET start=2026-10-07T20:15:00+00:00 shares=911 local=0.0947x prior-peak=0.4523x status=ok
  LGCL 2026-10-07  VOLUME-CONTEXT 16:20ET start=2026-10-07T20:20:00+00:00 shares=13815 local=2.1960x prior-peak=6.8595x status=ok
  LGCL 2026-10-07  VOLUME-CONTEXT 16:25ET start=2026-10-07T20:25:00+00:00 shares=3125 local=0.3247x prior-peak=1.5516x status=ok
  LGCL 2026-10-07  VOLUME-CONTEXT 16:30ET start=2026-10-07T20:30:00+00:00 shares=8376 local=2.6803x prior-peak=4.1589x status=ok
  LGCL 2026-10-07  VOLUME-CONTEXT 16:35ET start=2026-10-07T20:35:00+00:00 shares=9341 local=1.1152x prior-peak=4.6380x status=ok
  LGCL 2026-10-07  VOLUME-CONTEXT 16:40ET start=2026-10-07T20:40:00+00:00 shares=9023 local=1.0772x prior-peak=4.4801x status=ok
  LGCL 2026-10-07  VOLUME-CONTEXT 16:45ET start=2026-10-07T20:45:00+00:00 shares=22312 local=2.4728x prior-peak=11.0785x status=ok
  LGCL 2026-10-07  VOLUME-CONTEXT 16:50ET start=2026-10-07T20:50:00+00:00 shares=15303 local=1.6383x prior-peak=7.5983x status=ok
  LGCL 2026-10-07  VOLUME-CONTEXT 16:55ET start=2026-10-07T20:55:00+00:00 shares=37895 local=2.4763x prior-peak=18.8158x status=ok
  LGCL 2026-10-07  VOLUME-CONTEXT 17:00ET start=2026-10-07T21:00:00+00:00 shares=42655 local=1.9118x prior-peak=21.1792x status=ok
  LGCL 2026-10-07  VOLUME-CONTEXT 17:05ET start=2026-10-07T21:05:00+00:00 shares=13521 local=0.3568x prior-peak=6.7135x status=ok
  LGCL 2026-10-07  VOLUME-CONTEXT 17:10ET start=2026-10-07T21:10:00+00:00 shares=13067 local=0.3448x prior-peak=6.4881x status=ok
  LGCL 2026-10-07  VOLUME-CONTEXT 17:15ET start=2026-10-07T21:15:00+00:00 shares=29562 local=2.1864x prior-peak=14.6783x status=ok
  LGCL 2026-10-07  VOLUME-CONTEXT 17:20ET start=2026-10-07T21:20:00+00:00 shares=4441 local=0.3285x prior-peak=2.2051x status=ok
  LGCL 2026-10-07  VOLUME-CONTEXT 17:25ET start=2026-10-07T21:25:00+00:00 shares=6407 local=0.4903x prior-peak=3.1812x status=ok
  LGCL 2026-10-07  VOLUME-CONTEXT 17:30ET start=2026-10-07T21:30:00+00:00 shares=8781 local=1.3705x prior-peak=4.3600x status=ok
  LGCL 2026-10-07  VOLUME-CONTEXT 17:35ET start=2026-10-07T21:35:00+00:00 shares=16539 local=2.5814x prior-peak=8.2120x status=ok
  LGCL 2026-10-07  VOLUME-CONTEXT 17:40ET start=2026-10-07T21:40:00+00:00 shares=9764 local=1.1119x prior-peak=4.8481x status=ok
  LGCL 2026-10-07  VOLUME-CONTEXT 17:45ET start=2026-10-07T21:45:00+00:00 shares=12491 local=1.2793x prior-peak=6.2021x status=ok
  ```

**Below 10%:** NCPL (+8.2%), VCIG (+7.8%, Day −45.3%, dead-cat profile), FMST (+6.0%).

## Scan 00:30 CEST (6:30 PM ET)

`python3 scripts/scan.py --all` ran at 18:30:16 ET (00:30:16 CEST) in the AFTERHOURS session and returned 9 hits.

Supplementary AH-change-only (>15%, not in volume pass): none
AH >10% at this snapshot (unrounded): BFRG, CPHI, DKI, IPSC, IPW, PROF, SBFM, WHLR

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| CPHI | [TV](https://www.tradingview.com/chart/?symbol=CPHI) | $0.85 | +32.6% | +11.8% | $0.95 | +48.2% | 7.9M | 6.9M | 1.1x | 40.3M | Pharmaceuticals: Major |
| SBFM | [TV](https://www.tradingview.com/chart/?symbol=SBFM) | $0.70 | +75.9% | +20.3% | $0.84 | +111.6% | 5.1M | 18.2M | 0.3x | 4.2M | Pharmaceuticals: Major |
| IPW | [TV](https://www.tradingview.com/chart/?symbol=IPW) | $1.04 | -8.0% | +25.0% | $1.30 | +15.0% | 3.3M | 788K | 4.2x | 1.2M | Internet Retail |
| DKI | [TV](https://www.tradingview.com/chart/?symbol=DKI) | $1.67 | +22.8% | +37.1% | $2.29 | +68.4% | 1.9M | 5.3M | 0.4x | 1.2M | Packaged Software |
| BFRG | [TV](https://www.tradingview.com/chart/?symbol=BFRG) | $0.71 | +2.8% | +12.3% | $0.80 | +15.5% | 1.1M | 7.4M | 0.1x | 16.0M | Packaged Software |
| FMST | [TV](https://www.tradingview.com/chart/?symbol=FMST) | $0.56 | +13.2% | +5.4% | $0.59 | +19.2% | 729K | 627K | 1.2x | 13.2M | Other Metals/Minerals |
| WHLR | [TV](https://www.tradingview.com/chart/?symbol=WHLR) | $0.69 | -24.3% | +14.7% | $0.79 | -13.2% | 501K | 4.3M | 0.1x | 568K | Real Estate Investment Trusts |
| PROF | [TV](https://www.tradingview.com/chart/?symbol=PROF) | $5.68 | -6.6% | +19.0% | $6.76 | +11.2% | 136K | 157K | 0.9x | 35.4M | Medical Specialties |
| IPSC | [TV](https://www.tradingview.com/chart/?symbol=IPSC) | $1.28 | -3.0% | +13.3% | $1.45 | +9.8% | 52K | 801K | 0.1x | 122.9M | Biotechnology |

### Evaluation notes

**Decision:** No new entries at the final scan. BFRG is the only new name with 2 AH scans >10%, and its SIP volume is a thin drift. DKI and SBFM ignited after 17:50 ET on real volume but have only this one AH scan; DKI gets a FINAL-SCAN-GATE-BLOCK note. IPW (+25.0%) and CPHI (+11.8%, off its $1.16 high) are already held. All SIP bars below run through 18:15 ET (the latest bar outside the 15-minute delay at 18:30 ET), so the verification data is fresh.

**DKI — FINAL-SCAN-GATE-BLOCK (first AH scan >10%)** (DarkIris, float 1.2M, Packaged Software, `tradable=true`):

- FINAL-SCAN-GATE-BLOCK: DKI, float 1.2M, Grade None, ignition 17:50 ET, qualified at the final scan at $2.29 / +68.4% Total% from the $1.36 previous close; SIP 17:50–18:15 ET 170K / 264K / 669K / 485K / 413K / 298K sh on 1,185 / 2,491 / 4,814 / 4,170 / 2,964 / 1,900 trades, vwap $2.03 → $2.38 → $2.23; CONFIRM-3 YES 6.8x; ask book SIP-15m $2.20 x2300. Blocked only by the 2-AH-scan gate.
- Spike bar: `DKI 2026-10-07  SPIKE  17:53ET  +19%  $1.99  181 trades / 27k sh  (first co-spike bar) (as-of 18:30ET)`
- Third bar: `DKI 2026-10-07  CONFIRM-3  YES ignition 17:50ET 6.8x; confirmed 18:00ET $2.48 as-of 18:30ET`
- SIP: flat $1.61–$1.79 on 5–31K sh until 17:45, then the 17:50 ignition to $2.21 and an AH high of $2.70 at 18:00. 18:15 close $2.30 (15% off the high, inside the 20% hold band). SIP close matches the scanner's $2.29.
- Catalyst (2 searches): nothing dated 2026-10-07. Background only: the 2026-10-06 report of the extraordinary meeting vote (share structure and supervoting changes) and an undated AIGC video platform launch. Grade None.
- Multi-session context: not in `WINNERS_TRACKING.md`; previous close $1.36, today's +22.8% regular session is day 1.
- Shared SIP volume context:
  ```
  # DKI shared SIP volume sip-ah-volume-v2; prior 2026-10-06 3+45zero/48 slots; floor 100; log-only
  # reconstructed as-of 2026-10-07T22:30:16+00:00; source fetched 2026-10-07T22:31:50.906660+00:00
  DKI 2026-10-07  VOLUME-CONTEXT 16:00ET start=2026-10-07T20:00:00+00:00 shares=26120 local=unknown prior-peak=77.9701x status=warmup
  DKI 2026-10-07  VOLUME-CONTEXT 16:05ET start=2026-10-07T20:05:00+00:00 shares=18361 local=unknown prior-peak=54.8090x status=warmup
  DKI 2026-10-07  VOLUME-CONTEXT 16:10ET start=2026-10-07T20:10:00+00:00 shares=15263 local=unknown prior-peak=45.5612x status=warmup
  DKI 2026-10-07  VOLUME-CONTEXT 16:15ET start=2026-10-07T20:15:00+00:00 shares=10293 local=0.5606x prior-peak=30.7254x status=ok
  DKI 2026-10-07  VOLUME-CONTEXT 16:20ET start=2026-10-07T20:20:00+00:00 shares=14482 local=0.9488x prior-peak=43.2299x status=ok
  DKI 2026-10-07  VOLUME-CONTEXT 16:25ET start=2026-10-07T20:25:00+00:00 shares=7201 local=0.4972x prior-peak=21.4955x status=ok
  DKI 2026-10-07  VOLUME-CONTEXT 16:30ET start=2026-10-07T20:30:00+00:00 shares=14534 local=1.4120x prior-peak=43.3851x status=ok
  DKI 2026-10-07  VOLUME-CONTEXT 16:35ET start=2026-10-07T20:35:00+00:00 shares=20396 local=1.4084x prior-peak=60.8836x status=ok
  DKI 2026-10-07  VOLUME-CONTEXT 16:40ET start=2026-10-07T20:40:00+00:00 shares=14359 local=0.9880x prior-peak=42.8627x status=ok
  DKI 2026-10-07  VOLUME-CONTEXT 16:45ET start=2026-10-07T20:45:00+00:00 shares=11038 local=0.7595x prior-peak=32.9493x status=ok
  DKI 2026-10-07  VOLUME-CONTEXT 16:50ET start=2026-10-07T20:50:00+00:00 shares=12092 local=0.8421x prior-peak=36.0955x status=ok
  DKI 2026-10-07  VOLUME-CONTEXT 16:55ET start=2026-10-07T20:55:00+00:00 shares=9799 local=0.8104x prior-peak=29.2507x status=ok
  DKI 2026-10-07  VOLUME-CONTEXT 17:00ET start=2026-10-07T21:00:00+00:00 shares=5880 local=0.5327x prior-peak=17.5522x status=ok
  DKI 2026-10-07  VOLUME-CONTEXT 17:05ET start=2026-10-07T21:05:00+00:00 shares=5961 local=0.6083x prior-peak=17.7940x status=ok
  DKI 2026-10-07  VOLUME-CONTEXT 17:10ET start=2026-10-07T21:10:00+00:00 shares=7982 local=1.3390x prior-peak=23.8269x status=ok
  DKI 2026-10-07  VOLUME-CONTEXT 17:15ET start=2026-10-07T21:15:00+00:00 shares=7338 local=1.2310x prior-peak=21.9045x status=ok
  DKI 2026-10-07  VOLUME-CONTEXT 17:20ET start=2026-10-07T21:20:00+00:00 shares=4671 local=0.6365x prior-peak=13.9433x status=ok
  DKI 2026-10-07  VOLUME-CONTEXT 17:25ET start=2026-10-07T21:25:00+00:00 shares=3849 local=0.5245x prior-peak=11.4896x status=ok
  DKI 2026-10-07  VOLUME-CONTEXT 17:30ET start=2026-10-07T21:30:00+00:00 shares=4719 local=1.0103x prior-peak=14.0866x status=ok
  DKI 2026-10-07  VOLUME-CONTEXT 17:35ET start=2026-10-07T21:35:00+00:00 shares=31458 local=6.7347x prior-peak=93.9045x status=ok
  DKI 2026-10-07  VOLUME-CONTEXT 17:40ET start=2026-10-07T21:40:00+00:00 shares=10709 local=2.2693x prior-peak=31.9672x status=ok
  DKI 2026-10-07  VOLUME-CONTEXT 17:45ET start=2026-10-07T21:45:00+00:00 shares=25118 local=2.3455x prior-peak=74.9791x status=ok
  DKI 2026-10-07  VOLUME-CONTEXT 17:50ET start=2026-10-07T21:50:00+00:00 shares=170084 local=6.7714x prior-peak=507.7134x status=ok
  DKI 2026-10-07  VOLUME-CONTEXT 17:55ET start=2026-10-07T21:55:00+00:00 shares=263595 local=10.4943x prior-peak=786.8507x status=ok
  DKI 2026-10-07  VOLUME-CONTEXT 18:00ET start=2026-10-07T22:00:00+00:00 shares=668842 local=3.9324x prior-peak=1996.5433x status=ok
  DKI 2026-10-07  VOLUME-CONTEXT 18:05ET start=2026-10-07T22:05:00+00:00 shares=484630 local=1.8385x prior-peak=1446.6567x status=ok
  DKI 2026-10-07  VOLUME-CONTEXT 18:10ET start=2026-10-07T22:10:00+00:00 shares=413351 local=0.8529x prior-peak=1233.8836x status=ok
  DKI 2026-10-07  VOLUME-CONTEXT 18:15ET start=2026-10-07T22:15:00+00:00 shares=298130 local=0.6152x prior-peak=889.9403x status=ok
  ```
- Book:
  ```
  DKI BOOK iex bid $1.44 x100 / ask $1.97 x100 @ 2026-10-07 16:00:00 ET age 2h32m two-sided spread 26.90% of ask
  DKI BOOK sip-15m bid $2.19 x100 / ask $2.20 x2300 @ 2026-10-07 18:17:01 ET age 15m01s two-sided spread 0.45% of ask
  DKI BOOK refresh +15s iex unchanged @ 2026-10-07 16:00:00 ET
  DKI BOOK verdict: IEX STALE 2h32m; SIP-15m TWO-SIDED (observed 2026-10-07 18:32:02 ET; log-only)
  ```

**SBFM — Watch, gate-blocked (first AH scan >10%)** (Sunshine Biopharma, float 4.2M, Pharmaceuticals, `tradable=true`):

- Spike bar: `SBFM 2026-10-07  SPIKE  17:56ET  +19%  $0.83  372 trades / 149k sh  (first co-spike bar) (as-of 18:30ET)`
- Third bar: `SBFM 2026-10-07  CONFIRM-3  NO ignition 17:55ET failed third-bar hold/volume as-of 18:30ET`
- SIP: $0.68–$0.74 until 17:50, then 17:55 957K sh / 2,172 trades (high $0.88), followed by 600K / 1,586, 783K / 2,375, 710K / 1,803 and 396K / 1,025, capped at $0.88–$0.89 and closing $0.83 at 18:15. Real volume, but no new high after the ignition bar, so CONFIRM-3 NO and it does not meet the FINAL-SCAN-GATE-BLOCK definition. Total% +111.6% from the $0.40 previous close; Day% +75.9%.
- Catalyst (2 searches): nothing dated 2026-10-07; the Rivaroxaban Canadian approval (June 2026) is background. Grade None.
- Shared SIP volume context:
  ```
  # SBFM shared SIP volume sip-ah-volume-v2; prior 2026-10-06 40+8zero/48 slots; floor 100; log-only
  # reconstructed as-of 2026-10-07T22:30:16+00:00; source fetched 2026-10-07T22:31:52.934729+00:00
  SBFM 2026-10-07  VOLUME-CONTEXT 16:00ET start=2026-10-07T20:00:00+00:00 shares=258038 local=unknown prior-peak=5.0310x status=warmup
  SBFM 2026-10-07  VOLUME-CONTEXT 16:05ET start=2026-10-07T20:05:00+00:00 shares=115401 local=unknown prior-peak=2.2500x status=warmup
  SBFM 2026-10-07  VOLUME-CONTEXT 16:10ET start=2026-10-07T20:10:00+00:00 shares=89254 local=unknown prior-peak=1.7402x status=warmup
  SBFM 2026-10-07  VOLUME-CONTEXT 16:15ET start=2026-10-07T20:15:00+00:00 shares=182391 local=1.5805x prior-peak=3.5561x status=ok
  SBFM 2026-10-07  VOLUME-CONTEXT 16:20ET start=2026-10-07T20:20:00+00:00 shares=57387 local=0.4973x prior-peak=1.1189x status=ok
  SBFM 2026-10-07  VOLUME-CONTEXT 16:25ET start=2026-10-07T20:25:00+00:00 shares=359720 local=4.0303x prior-peak=7.0135x status=ok
  SBFM 2026-10-07  VOLUME-CONTEXT 16:30ET start=2026-10-07T20:30:00+00:00 shares=228132 local=1.2508x prior-peak=4.4479x status=ok
  SBFM 2026-10-07  VOLUME-CONTEXT 16:35ET start=2026-10-07T20:35:00+00:00 shares=256839 local=1.1258x prior-peak=5.0076x status=ok
  SBFM 2026-10-07  VOLUME-CONTEXT 16:40ET start=2026-10-07T20:40:00+00:00 shares=108997 local=0.4244x prior-peak=2.1251x status=ok
  SBFM 2026-10-07  VOLUME-CONTEXT 16:45ET start=2026-10-07T20:45:00+00:00 shares=42898 local=0.1880x prior-peak=0.8364x status=ok
  SBFM 2026-10-07  VOLUME-CONTEXT 16:50ET start=2026-10-07T20:50:00+00:00 shares=32710 local=0.3001x prior-peak=0.6377x status=ok
  SBFM 2026-10-07  VOLUME-CONTEXT 16:55ET start=2026-10-07T20:55:00+00:00 shares=113139 local=2.6374x prior-peak=2.2059x status=ok
  SBFM 2026-10-07  VOLUME-CONTEXT 17:00ET start=2026-10-07T21:00:00+00:00 shares=34421 local=0.8024x prior-peak=0.6711x status=ok
  SBFM 2026-10-07  VOLUME-CONTEXT 17:05ET start=2026-10-07T21:05:00+00:00 shares=44590 local=1.2954x prior-peak=0.8694x status=ok
  SBFM 2026-10-07  VOLUME-CONTEXT 17:10ET start=2026-10-07T21:10:00+00:00 shares=43185 local=0.9685x prior-peak=0.8420x status=ok
  SBFM 2026-10-07  VOLUME-CONTEXT 17:15ET start=2026-10-07T21:15:00+00:00 shares=30298 local=0.7016x prior-peak=0.5907x status=ok
  SBFM 2026-10-07  VOLUME-CONTEXT 17:20ET start=2026-10-07T21:20:00+00:00 shares=65739 local=1.5223x prior-peak=1.2817x status=ok
  SBFM 2026-10-07  VOLUME-CONTEXT 17:25ET start=2026-10-07T21:25:00+00:00 shares=47584 local=1.1019x prior-peak=0.9277x status=ok
  SBFM 2026-10-07  VOLUME-CONTEXT 17:30ET start=2026-10-07T21:30:00+00:00 shares=55343 local=1.1631x prior-peak=1.0790x status=ok
  SBFM 2026-10-07  VOLUME-CONTEXT 17:35ET start=2026-10-07T21:35:00+00:00 shares=13906 local=0.2513x prior-peak=0.2711x status=ok
  SBFM 2026-10-07  VOLUME-CONTEXT 17:40ET start=2026-10-07T21:40:00+00:00 shares=45901 local=0.9646x prior-peak=0.8949x status=ok
  SBFM 2026-10-07  VOLUME-CONTEXT 17:45ET start=2026-10-07T21:45:00+00:00 shares=111125 local=2.4210x prior-peak=2.1666x status=ok
  SBFM 2026-10-07  VOLUME-CONTEXT 17:50ET start=2026-10-07T21:50:00+00:00 shares=91379 local=1.9908x prior-peak=1.7816x status=ok
  SBFM 2026-10-07  VOLUME-CONTEXT 17:55ET start=2026-10-07T21:55:00+00:00 shares=956924 local=10.4720x prior-peak=18.6571x status=ok
  SBFM 2026-10-07  VOLUME-CONTEXT 18:00ET start=2026-10-07T22:00:00+00:00 shares=599538 local=5.3952x prior-peak=11.6892x status=ok
  SBFM 2026-10-07  VOLUME-CONTEXT 18:05ET start=2026-10-07T22:05:00+00:00 shares=782801 local=1.3057x prior-peak=15.2623x status=ok
  SBFM 2026-10-07  VOLUME-CONTEXT 18:10ET start=2026-10-07T22:10:00+00:00 shares=710112 local=0.9071x prior-peak=13.8450x status=ok
  SBFM 2026-10-07  VOLUME-CONTEXT 18:15ET start=2026-10-07T22:15:00+00:00 shares=395818 local=0.5574x prior-peak=7.7173x status=ok
  ```
- Book:
  ```
  SBFM BOOK iex bid $0.9374 x100 / ask $1.09 x1400 @ 2026-10-07 11:59:26 ET age 6h32m two-sided spread 14.00% of ask
  SBFM BOOK sip-15m bid $0.8250 x100 / ask $0.8276 x700 @ 2026-10-07 18:17:02 ET age 15m00s two-sided spread 0.31% of ask
  SBFM BOOK refresh +15s iex unchanged @ 2026-10-07 11:59:26 ET
  SBFM BOOK verdict: IEX STALE 6h32m; SIP-15m TWO-SIDED (observed 2026-10-07 18:32:02 ET; log-only)
  ```

**BFRG — SKIP: thin drift (2nd AH scan >10%: +15.3% at 00:00, +12.3% now)** (float 16.0M, `tradable=true`):

- Spike bar: `BFRG 2026-10-07  SPIKE  17:27ET  +15%  $0.82  135 trades / 51k sh  (first co-spike bar) (as-of 18:30ET)`
- Third bar: `BFRG 2026-10-07  CONFIRM-3  NO no local-volume new-high ignition as-of 18:30ET`
- SIP 17:50–18:15: 18K, 25K, 25K, 16K, 32K, 39K sh on 21–64 trades per bar, pinned at $0.79–$0.82. VRatio 0.1x. This meets the thin, not accumulating skip.
- Catalyst (1 search, re-run): the 2026-10-06 collaboration milestone with a global pharma partner is from the previous trading date, so it is background. Grade None.
- Shared SIP volume context:
  ```
  # BFRG shared SIP volume sip-ah-volume-v2; prior 2026-10-06 48+0zero/48 slots; floor 100; log-only
  # reconstructed as-of 2026-10-07T22:30:16+00:00; source fetched 2026-10-07T22:31:54.906794+00:00
  BFRG 2026-10-07  VOLUME-CONTEXT 16:00ET start=2026-10-07T20:00:00+00:00 shares=37935 local=unknown prior-peak=0.3961x status=warmup
  BFRG 2026-10-07  VOLUME-CONTEXT 16:05ET start=2026-10-07T20:05:00+00:00 shares=6770 local=unknown prior-peak=0.0707x status=warmup
  BFRG 2026-10-07  VOLUME-CONTEXT 16:10ET start=2026-10-07T20:10:00+00:00 shares=18596 local=unknown prior-peak=0.1942x status=warmup
  BFRG 2026-10-07  VOLUME-CONTEXT 16:15ET start=2026-10-07T20:15:00+00:00 shares=3623 local=0.1948x prior-peak=0.0378x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 16:20ET start=2026-10-07T20:20:00+00:00 shares=12785 local=1.8885x prior-peak=0.1335x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 16:25ET start=2026-10-07T20:25:00+00:00 shares=1794 local=0.1403x prior-peak=0.0187x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 16:30ET start=2026-10-07T20:30:00+00:00 shares=19557 local=5.3980x prior-peak=0.2042x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 16:35ET start=2026-10-07T20:35:00+00:00 shares=92266 local=7.2167x prior-peak=0.9634x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 16:40ET start=2026-10-07T20:40:00+00:00 shares=29291 local=1.4977x prior-peak=0.3059x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 16:45ET start=2026-10-07T20:45:00+00:00 shares=8289 local=0.2830x prior-peak=0.0866x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 16:50ET start=2026-10-07T20:50:00+00:00 shares=2089 local=0.0713x prior-peak=0.0218x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 16:55ET start=2026-10-07T20:55:00+00:00 shares=15435 local=1.8621x prior-peak=0.1612x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 17:00ET start=2026-10-07T21:00:00+00:00 shares=8740 local=1.0544x prior-peak=0.0913x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 17:05ET start=2026-10-07T21:05:00+00:00 shares=1908 local=0.2183x prior-peak=0.0199x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 17:10ET start=2026-10-07T21:10:00+00:00 shares=25567 local=2.9253x prior-peak=0.2670x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 17:15ET start=2026-10-07T21:15:00+00:00 shares=255072 local=29.1844x prior-peak=2.6634x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 17:20ET start=2026-10-07T21:20:00+00:00 shares=11668 local=0.4564x prior-peak=0.1218x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 17:25ET start=2026-10-07T21:25:00+00:00 shares=169118 local=6.6147x prior-peak=1.7659x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 17:30ET start=2026-10-07T21:30:00+00:00 shares=56583 local=0.3346x prior-peak=0.5908x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 17:35ET start=2026-10-07T21:35:00+00:00 shares=111222 local=1.9656x prior-peak=1.1614x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 17:40ET start=2026-10-07T21:40:00+00:00 shares=16265 local=0.1462x prior-peak=0.1698x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 17:45ET start=2026-10-07T21:45:00+00:00 shares=78390 local=1.3854x prior-peak=0.8185x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 17:50ET start=2026-10-07T21:50:00+00:00 shares=18453 local=0.2354x prior-peak=0.1927x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 17:55ET start=2026-10-07T21:55:00+00:00 shares=25492 local=1.3815x prior-peak=0.2662x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 18:00ET start=2026-10-07T22:00:00+00:00 shares=24577 local=0.9641x prior-peak=0.2566x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 18:05ET start=2026-10-07T22:05:00+00:00 shares=15673 local=0.6377x prior-peak=0.1637x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 18:10ET start=2026-10-07T22:10:00+00:00 shares=31905 local=1.2982x prior-peak=0.3331x status=ok
  BFRG 2026-10-07  VOLUME-CONTEXT 18:15ET start=2026-10-07T22:15:00+00:00 shares=39213 local=1.5955x prior-peak=0.4095x status=ok
  ```

**WHLR — SKIP: dead-cat bounce (first AH scan >10%)** (float 568K, REIT, `tradable=true`): Day% −24.3%, AH +14.7% still leaves it 13.2% below the previous close, so it does not qualify for DEAD-CAT-OVERRIDE WATCH. SIP: 17:55–18:00 spike to $0.84 on 92K / 128K sh, then 17–38K sh per bar at $0.76–$0.80.

- Spike bar: `WHLR 2026-10-07  SPIKE  17:59ET  +22%  $0.84  233 trades / 61k sh  (first co-spike bar) (as-of 18:30ET)`
- Third bar: `WHLR 2026-10-07  CONFIRM-3  NO ignition 17:55ET failed third-bar hold/volume as-of 18:30ET`
- Shared SIP volume context:
  ```
  # WHLR shared SIP volume sip-ah-volume-v2; prior 2026-10-06 48+0zero/48 slots; floor 100; log-only
  # reconstructed as-of 2026-10-07T22:30:16+00:00; source fetched 2026-10-07T22:31:56.884975+00:00
  WHLR 2026-10-07  VOLUME-CONTEXT 16:00ET start=2026-10-07T20:00:00+00:00 shares=59055 local=unknown prior-peak=0.2044x status=warmup
  WHLR 2026-10-07  VOLUME-CONTEXT 16:05ET start=2026-10-07T20:05:00+00:00 shares=21243 local=unknown prior-peak=0.0735x status=warmup
  WHLR 2026-10-07  VOLUME-CONTEXT 16:10ET start=2026-10-07T20:10:00+00:00 shares=12400 local=unknown prior-peak=0.0429x status=warmup
  WHLR 2026-10-07  VOLUME-CONTEXT 16:15ET start=2026-10-07T20:15:00+00:00 shares=7990 local=0.3761x prior-peak=0.0277x status=ok
  WHLR 2026-10-07  VOLUME-CONTEXT 16:20ET start=2026-10-07T20:20:00+00:00 shares=11127 local=0.8973x prior-peak=0.0385x status=ok
  WHLR 2026-10-07  VOLUME-CONTEXT 16:25ET start=2026-10-07T20:25:00+00:00 shares=3015 local=0.2710x prior-peak=0.0104x status=ok
  WHLR 2026-10-07  VOLUME-CONTEXT 16:30ET start=2026-10-07T20:30:00+00:00 shares=19111 local=2.3919x prior-peak=0.0662x status=ok
  WHLR 2026-10-07  VOLUME-CONTEXT 16:35ET start=2026-10-07T20:35:00+00:00 shares=16003 local=1.4382x prior-peak=0.0554x status=ok
  WHLR 2026-10-07  VOLUME-CONTEXT 16:40ET start=2026-10-07T20:40:00+00:00 shares=7682 local=0.4800x prior-peak=0.0266x status=ok
  WHLR 2026-10-07  VOLUME-CONTEXT 16:45ET start=2026-10-07T20:45:00+00:00 shares=15112 local=0.9443x prior-peak=0.0523x status=ok
  WHLR 2026-10-07  VOLUME-CONTEXT 16:50ET start=2026-10-07T20:50:00+00:00 shares=15698 local=1.0388x prior-peak=0.0543x status=ok
  WHLR 2026-10-07  VOLUME-CONTEXT 16:55ET start=2026-10-07T20:55:00+00:00 shares=6123 local=0.4052x prior-peak=0.0212x status=ok
  WHLR 2026-10-07  VOLUME-CONTEXT 17:00ET start=2026-10-07T21:00:00+00:00 shares=3583 local=0.2371x prior-peak=0.0124x status=ok
  WHLR 2026-10-07  VOLUME-CONTEXT 17:05ET start=2026-10-07T21:05:00+00:00 shares=9821 local=1.6040x prior-peak=0.0340x status=ok
  WHLR 2026-10-07  VOLUME-CONTEXT 17:10ET start=2026-10-07T21:10:00+00:00 shares=2356 local=0.3848x prior-peak=0.0082x status=ok
  WHLR 2026-10-07  VOLUME-CONTEXT 17:15ET start=2026-10-07T21:15:00+00:00 shares=735 local=0.2051x prior-peak=0.0025x status=ok
  WHLR 2026-10-07  VOLUME-CONTEXT 17:20ET start=2026-10-07T21:20:00+00:00 shares=2360 local=1.0017x prior-peak=0.0082x status=ok
  WHLR 2026-10-07  VOLUME-CONTEXT 17:25ET start=2026-10-07T21:25:00+00:00 shares=9932 local=4.2156x prior-peak=0.0344x status=ok
  WHLR 2026-10-07  VOLUME-CONTEXT 17:30ET start=2026-10-07T21:30:00+00:00 shares=9336 local=3.9559x prior-peak=0.0323x status=ok
  WHLR 2026-10-07  VOLUME-CONTEXT 17:35ET start=2026-10-07T21:35:00+00:00 shares=8633 local=0.9247x prior-peak=0.0299x status=ok
  WHLR 2026-10-07  VOLUME-CONTEXT 17:40ET start=2026-10-07T21:40:00+00:00 shares=10191 local=1.0916x prior-peak=0.0353x status=ok
  WHLR 2026-10-07  VOLUME-CONTEXT 17:45ET start=2026-10-07T21:45:00+00:00 shares=3128 local=0.3350x prior-peak=0.0108x status=ok
  WHLR 2026-10-07  VOLUME-CONTEXT 17:50ET start=2026-10-07T21:50:00+00:00 shares=8667 local=1.0039x prior-peak=0.0300x status=ok
  WHLR 2026-10-07  VOLUME-CONTEXT 17:55ET start=2026-10-07T21:55:00+00:00 shares=91837 local=10.5962x prior-peak=0.3179x status=ok
  WHLR 2026-10-07  VOLUME-CONTEXT 18:00ET start=2026-10-07T22:00:00+00:00 shares=127842 local=14.7504x prior-peak=0.4426x status=ok
  WHLR 2026-10-07  VOLUME-CONTEXT 18:05ET start=2026-10-07T22:05:00+00:00 shares=20173 local=0.2197x prior-peak=0.0698x status=ok
  WHLR 2026-10-07  VOLUME-CONTEXT 18:10ET start=2026-10-07T22:10:00+00:00 shares=37789 local=0.4115x prior-peak=0.1308x status=ok
  WHLR 2026-10-07  VOLUME-CONTEXT 18:15ET start=2026-10-07T22:15:00+00:00 shares=17248 local=0.4564x prior-peak=0.0597x status=ok
  ```

**IPSC — SKIP: thin (first AH scan >10%)** (float 122.9M, Biotechnology, `tradable=true`): SIP shows 3 AH bars after 16:00, totalling 8.8K sh on 13 trades, last print $1.35 (below the scanner's $1.45). Total% +9.8%.

- Spike bar: `IPSC 2026-10-07  NO-SPIKE  peak +14% @18:08ET  (no bar cleared +15% on a volume co-spike) (as-of 18:30ET)`
- Third bar: `IPSC 2026-10-07  CONFIRM-3  NO no local-volume new-high ignition as-of 18:30ET`
- Shared SIP volume context:
  ```
  # IPSC shared SIP volume sip-ah-volume-v2; prior 2026-10-06 4+44zero/48 slots; floor 100; log-only
  # reconstructed as-of 2026-10-07T22:30:16+00:00; source fetched 2026-10-07T22:31:58.884707+00:00
  IPSC 2026-10-07  VOLUME-CONTEXT 16:00ET start=2026-10-07T20:00:00+00:00 shares=43510 local=unknown prior-peak=0.7530x status=warmup
  IPSC 2026-10-07  VOLUME-CONTEXT 18:05ET start=2026-10-07T22:05:00+00:00 shares=8000 local=80.0000x prior-peak=0.1385x status=floored
  IPSC 2026-10-07  VOLUME-CONTEXT 18:10ET start=2026-10-07T22:10:00+00:00 shares=515 local=5.1500x prior-peak=0.0089x status=floored
  IPSC 2026-10-07  VOLUME-CONTEXT 18:15ET start=2026-10-07T22:15:00+00:00 shares=240 local=0.4660x prior-peak=0.0042x status=ok
  ```

**PROF — SKIP: thin (4th AH scan >10%)**: SIP 17:55–18:15 at 200–2.9K sh per bar.

- Spike bar: `PROF 2026-10-07  SPIKE  16:36ET  +21%  $6.87  69 trades / 2k sh  (first co-spike bar) (as-of 18:30ET)`
- Third bar: `PROF 2026-10-07  CONFIRM-3  NO ignition 16:35ET failed third-bar hold/volume as-of 18:30ET`
- Shared SIP volume context:
  ```
  # PROF shared SIP volume sip-ah-volume-v2; prior 2026-10-06 1+47zero/48 slots; floor 100; log-only
  # reconstructed as-of 2026-10-07T22:30:16+00:00; source fetched 2026-10-07T22:32:00.849810+00:00
  PROF 2026-10-07  VOLUME-CONTEXT 16:00ET start=2026-10-07T20:00:00+00:00 shares=2919 local=unknown prior-peak=4.2121x status=warmup
  PROF 2026-10-07  VOLUME-CONTEXT 16:25ET start=2026-10-07T20:25:00+00:00 shares=500 local=5.0000x prior-peak=0.7215x status=floored
  PROF 2026-10-07  VOLUME-CONTEXT 16:30ET start=2026-10-07T20:30:00+00:00 shares=4110 local=41.1000x prior-peak=5.9307x status=floored
  PROF 2026-10-07  VOLUME-CONTEXT 16:35ET start=2026-10-07T20:35:00+00:00 shares=51786 local=103.5720x prior-peak=74.7273x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 16:40ET start=2026-10-07T20:40:00+00:00 shares=40539 local=9.8635x prior-peak=58.4978x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 16:45ET start=2026-10-07T20:45:00+00:00 shares=7528 local=0.1857x prior-peak=10.8629x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 16:50ET start=2026-10-07T20:50:00+00:00 shares=15162 local=0.3740x prior-peak=21.8788x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 16:55ET start=2026-10-07T20:55:00+00:00 shares=8667 local=0.5716x prior-peak=12.5065x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 17:00ET start=2026-10-07T21:00:00+00:00 shares=4761 local=0.5493x prior-peak=6.8701x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 17:05ET start=2026-10-07T21:05:00+00:00 shares=4604 local=0.5312x prior-peak=6.6436x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 17:10ET start=2026-10-07T21:10:00+00:00 shares=5952 local=1.2502x prior-peak=8.5887x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 17:15ET start=2026-10-07T21:15:00+00:00 shares=2019 local=0.4241x prior-peak=2.9134x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 17:20ET start=2026-10-07T21:20:00+00:00 shares=3761 local=0.8169x prior-peak=5.4271x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 17:25ET start=2026-10-07T21:25:00+00:00 shares=1810 local=0.4813x prior-peak=2.6118x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 17:30ET start=2026-10-07T21:30:00+00:00 shares=1506 local=0.7459x prior-peak=2.1732x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 17:35ET start=2026-10-07T21:35:00+00:00 shares=2611 local=1.4425x prior-peak=3.7677x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 17:40ET start=2026-10-07T21:40:00+00:00 shares=178 local=0.0983x prior-peak=0.2569x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 17:45ET start=2026-10-07T21:45:00+00:00 shares=1572 local=1.0438x prior-peak=2.2684x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 17:50ET start=2026-10-07T21:50:00+00:00 shares=312 local=0.1985x prior-peak=0.4502x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 17:55ET start=2026-10-07T21:55:00+00:00 shares=2545 local=8.1571x prior-peak=3.6724x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 18:00ET start=2026-10-07T22:00:00+00:00 shares=2883 local=1.8340x prior-peak=4.1602x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 18:05ET start=2026-10-07T22:05:00+00:00 shares=403 local=0.1583x prior-peak=0.5815x status=ok
  PROF 2026-10-07  VOLUME-CONTEXT 18:15ET start=2026-10-07T22:15:00+00:00 shares=200 local=0.4963x prior-peak=0.2886x status=ok
  ```

**Final-scan feed-lag cross-check:** LGCL (>10% at 00:00) dropped from the scan. SIP shows a spike to $3.39 at 17:50 (79K sh / 557 trades), then a fade to $2.99 at 18:15, +6% over the $2.82 close: below threshold, so TradingView is not under-reporting it. `LGCL 2026-10-07  SPIKE  17:52ET  +20%  $3.39  211 trades / 31k sh  (first co-spike bar) (as-of 18:30ET)`; `LGCL 2026-10-07  CONFIRM-3  NO ignition 16:55ET failed third-bar hold/volume as-of 18:30ET`. Other 21:30 watch names are not in the scan and had no prior AH footprint above 10%.

**Below 10%:** FMST (+5.4%).

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
| IPW | $1.38 | 17:38:57 ET (23:38 CEST) | 72 | 825706f4 | 2 AH scans >10%, real SIP ignition (CONFIRM-3 YES), hold near high; float 1.2M; Grade None |
| CPHI | $0.9978 | 18:02:02 ET (00:02 CEST) | 94 | 58102d51 | 2 AH scans >10%, late BUILD to $1.16 on 0.3–1.3M sh/bar; float 40.3M; Grade None |

## Morning Evaluation — 10:20 CEST (04:20 ET, October 8)

**Pulse 1: DKI is today's winner. The scanner detected it at the final scan, and the 2-AH-scan gate blocked the entry.** DKI reached a SIP PM high of **$3.72 (+122.8%)** at 04:21 ET from its **$1.67** October 7 close, on **2.34M + 1.47M shares / 23,158 + 16,082 trades** in the 04:15 and 04:20 bars. Both bars closed above +100% ($3.47, $3.46). The 00:30 CEST scan logged it at **$2.29** with CONFIRM-3 YES and a two-sided SIP book, and blocked it only because it had one AH scan. Hypothetical final-scan entry → PM peak: **+62.4%**. Our two entries did not reach the bar: IPW peaked at $2.00 (+92.3% from close, +44.9% on the $1.38 fill) and CPHI never reclaimed its fill. Position-evaluation sold both at 10:30 CEST for **−$14.88** net.

Discovery ran before reading this log: `scan.py --all --session premarket` at 04:20 ET (QTEX, IPW, WHLR, DKI) and `pm-sweep.py` (18 listed names above +10%, no price or cap limit). All levels below are **Alpaca SIP** daily closes or 5-minute/1-minute bars through the **04:22 ET** minute (captured 04:38 ET). Yahoo was used for timeline shape and the latest print only. October 7 is a normal Wednesday, so every PM % uses the October 7 SIP close; entry Total% uses the October 6 SIP close, as the scan did.

### Today's Winner

**DKI — DarkIris Inc. (packaged software / digital game storefronts, Hong Kong), Nasdaq**

- Catalyst: **Grade None.** The October 6 6-K reported the extraordinary meeting results: Class B shares raised to 200 votes each, and two **conditional** 50-for-1 share consolidations that apply only if the Class A price falls below $1.00. Benzinga ran "DarkIris shares jump 16% after hours" on the vote overnight. No operational news. No split has been effected, so it does not enter the reverse-split tally.
- Previous close: **$1.67** (SIP, October 7). October 7's regular session ran $1.27 → $3.64 intraday on 41.7M shares and closed $1.67 (+22.8% from the $1.36 October 6 close). `price-timeline.py` uses the same $1.67 basis.
- AH last night: flat $1.53–$1.79 on 5–60K shares per bar until 17:45 ET. It ignited at **17:50 ET** (170K → 264K → 669K shares) to an AH high of **$2.70 (+61.7%) at 18:00 ET** (4,814 trades). The 00:30 CEST scan showed **$2.29 (+37.1% AH)**. It then faded to **$1.82** (18:45 bar low) and closed AH at **$1.94**.
- Premarket: opened $2.04, dipped to $1.86, then ran from 04:13. The **04:15 bar** went to **$3.59** on 2,342,884 / 23,158 (close $3.47), the **04:20 bar** to **$3.72 at 04:21** on 1,472,817 / 16,082 (close $3.46). Yahoo shows $3.22 at 04:25 and $3.19 (+91.0%) at 04:28.
- Hypothetical P&L: final-scan $2.29 → $3.72 = **+62.4%**. Holding overnight meant a drawdown to $1.82 (−20.5%) first, and the PM opened at $2.04, below that entry. PM-open 04:00 VWAP $1.96 → $3.72 = +89.8%.
- Float **1.2M** | Market cap **~$3.5M** (TradingView; Class A only).
- Capturable: **yes.** `tradable=true`. The 00:30 scan logged a two-sided SIP book ($2.19 x100 / $2.20 x2300 at 18:17 ET). The PM SIP book at 04:10 ET was $2.01 / $2.06 (2.4%). The IEX quote was frozen at the 16:00 ET close, as usual.
- Winner bar: **clears.** +122.8% from the true last-session close, two consecutive 5-minute closes above +100%, 3.8M shares / 39K trades across the two peak bars.

**Scanner Diagnostic:**

- Detectable at screening time (~22:15 CEST)? **NO.** At 16:15 ET DKI was $1.55 (−7%). The AH move began at 17:50 ET (23:50 CEST). It was detected at the first scan after the ignition: the **00:30 CEST final scan**, +37.1% AH, $2.29. It was also on the 21:30 regular-session watch list.
- Why we did not act: the **2-AH-scan gate**. It was logged as a FINAL-SCAN-GATE-BLOCK with CONFIRM-3 YES (6.8x) and a fillable SIP ask.
- Scanner gap: **none in detection.** The gap is the entry gate on late igniters; see the final-scan gate-block tracker in Notes. A late scan would not have added a second qualifying AH scan, because DKI faded to +16% by 20:00 ET.

**Also notable (not the headline):**

- **IPW — iPower (internet retail), our first entry.** Fresh day-1 AH igniter (Day −8.0%). It ignited at 16:40 ET on 461K shares per bar, built through four AH scans (+17.3 → +21.0 → +24.0 → +25.0%), and extended in the unscanned tail to **$1.68 at 19:55 ET**. PM SIP high **$2.00 (+92.3%)** in the 04:10 bar on 3,411,595 / 23,113, which closed $1.71; then $1.65 and $1.55. Below the bar. Entered $1.38, sold $1.43.
- **MRNO — Murano Global (hotels, Mexico), close $0.2361. Below the $0.50 floor.** October 7 6-K: strategic review, debt-restructuring update, and a second 180-day Nasdaq bid-price extension (no deal; Grade None). It ignited at **16:30 ET** to $0.42 (+78%) on **9.8M shares / 19,376 trades** in that 15-minute bar. It held $0.35–$0.41 for the rest of AH on 0.7–12M shares per 15 minutes, and the SIP book at 18:30 ET was $0.3752 / $0.3756 (0.1% spread). PM high **$0.46 (+94.8%)** in the 04:00 bar on 8.68M / 19,985, closing $0.38; $0.39 since. Below the >100% bar.

### Baseline Tracking

Source: the October 6 log (Days tracked 95), which is the immediately preceding trading day. **No new baseline gap.** Existing gaps stay **Sep 11, Sep 18, Sep 25, Oct 2**.

- Days tracked: **96** (95 + October 7 only).
- Winners detected by scanner: **74/85 (87.1%)**. DKI is added as detected (+1/+1). MRNO is a price-floor exclusion but peaked at +94.8%, below the >100% winner bar, so it does not enter the denominator.
- Winner selected for paper trade: **37/81 (45.7%)**. DKI was not entered (+0/+1).
- Target: >80% detection. Status: **BASELINE MET.** Coverage failures, the four skipped retrospectives, and the floor exclusions limit what the rate means.
- **Correction 2026-10-09 (Juan's reply to the Oct 7 email):** "DKI is NOT a winner. There is no volume spike compared to the previous day." Oct 7's regular session printed 5m SIP bars up to 4.0M shares; DKI's AH ignition bars peaked at 669K and its PM peak bars at 2.34M/1.47M. DKI comes out of the denominator: **no real winner for Oct 7→8.** Corrected carry-forward: detected **73/84 (86.9%)**, selected **37/80 (46.3%)**, days tracked 96. The final-scan gate-block tally stays **2 (TRUG, UPC)**; DKI is excluded.

### Retrospective Scan Results

`scan.py --all --session premarket` (04:20 ET): QTEX (+5.4%, 0.0x), IPW (+49.0%), WHLR (+5.8%), DKI (+19.8% at the time). `pm-sweep.py` added MRNO, SDST and OLB (all below $0.50) plus thin names: PROF 2,950 PM shares, LUCD 1,122, NXXT 1,058, UPC 1,486, LZMH 939, EDSA 4,339, CMTL 168, SKIN 598, AMBP 972, BGL 594. WOLF (+14%, $1.66B cap) is outside the strategy. No forced AH scan was run; the postmarket fields reset overnight.

| Ticker | Oct 7 SIP close | AH SIP high / ET | PM SIP high / ET | PM high vs close | Peak-bar shares / trades | Latest | Classification |
|--------|-----------------|------------------|------------------|------------------|--------------------------|--------|----------------|
| DKI | $1.67 | $2.70 / 18:00 | $3.72 / 04:21 | **+122.8%** | 1,472,817 / 16,082 (04:20 bar) | $3.19 (+91.0%, Yahoo 04:28) | AH→PM continuation; **winner**; detected at final scan, gate-blocked |
| MRNO | $0.2361 | $0.44 / 16:45 | $0.46 / 04:00 | +94.8% | 8,675,929 / 19,985 | $0.39 (+65%) | Below $0.50 floor; in-window AH +78% on 9.8M shares |
| IPW | $1.04 | $1.68 / 19:55 | $2.00 / 04:10 | +92.3% | 3,411,595 / 23,113 | $1.55 (+49.0%) | AH→PM continuation; detected + entered |
| SDST | $0.075 | $0.08 (flat) | $0.1273 / 04:00 | +69.7% | 23,123,875 / 12,956 | $0.10 (+33%) | Below floor; PM-only (flat AH) |
| OLB | $0.387 | $0.52 / 19:45 | $0.55 / 04:05 | +42.1% | 2,712,683 / 4,299 | $0.48 (+24%) | Below floor; late-AH tail (+1% at 18:30 ET) |
| PROF | $5.68 | $7.51 / 16:35 | $6.92 / 04:00 | +21.8% | 11,263 / 229 | $6.82 | Detected, thin; AH better |
| SBFM | $0.70 | $0.89 / 18:05 | $0.85 / 04:00 | +21.4% | 986,224 / 10,841 | $0.70 (0%) | Final-scan first sighting, CONFIRM-3 NO; AH better |
| WHLR | $0.69 | $0.84 / 17:55 | $0.77 / 04:00 | +11.6% | 161,242 / 1,354 | $0.71 | Dead-cat skip; AH better |
| CPHI | $0.85 | $1.16 / 17:30 | $0.96 / 04:00 | +12.9% | 394,740 / 2,733 | $0.84 | Detected + entered; faded below fill |

### Open Position P&L (Alpaca)

No positions remain open. Position-evaluation (10:30 CEST, `log/2026-10-08/log.md`) sold both fills at 04:30 ET. Prices are `filled_avg_price` from `broker.js orders all`.

| Ticker | Entry | Entry Total% | Catalyst | Entry Time | PM Peak | Peak Time | Exit | P&L | P&L % | Status |
|--------|-------|--------------|----------|------------|---------|-----------|------|-----|-------|--------|
| IPW | $1.38 | +22.1% (vs $1.13) | None — no catalyst found | 23:38 CEST (17:38 ET) | $2.00 (SIP) | 04:10 ET | $1.43 | +$3.60 | +3.6% | ✅ Win (peak +44.9% on fill) |
| CPHI | $0.9978 | +55.9% (vs $0.64) | None — no catalyst found | 00:02 CEST (18:02 ET) | $0.96 (SIP) | 04:00 ET | $0.8012 | −$18.48 | −19.7% | ❌ Loss (never reclaimed fill) |

**Total Realized P&L (Alpaca fills only, this session): −$14.88.** IPW was sold 28.5% below its $2.00 SIP peak, which printed in the 04:10 bar and was already fading when the 10:30 pulse ran.

### Scanner Effectiveness

- Evening scans ran: **7 of 7** scheduled checkpoints (21:30, 22:00, 22:30, 23:00, 23:30, 00:00, 00:30 CEST), plus six extra observations (22:05, 22:10, 22:15, 22:20, 22:25, 22:45). The entry window was fully covered.
- Candidates found: **16 unique tickers** with a >10% AH appearance (IPW 4, PROF 4, CPHI 3, KUST 2, BFRG 2, ERNA 1, NCPL 1, IRIX 1, SUGP 1, VNTG 1, MVIS 1, LGCL 1, DKI 1, SBFM 1, WHLR 1, IPSC 1), plus a 29-name regular-session watch list.
- Retrospective matches: **all in-universe AH→PM movers detected** (DKI, IPW, plus the faders). MRNO, SDST and OLB sit below the floor.
- Supplementary AH-change-only pass: the line is present in all 12 AH scans. **4 unique tickers, 1 continuation / 3 faded / 0 unassessed.**
  - **IPW: continuation, sustained.** Latest logged AH price $1.30 (00:30) → PM SIP high $2.00 (+53.8%) on 3,411,595 / 23,113; the next bar closed $1.65, above $1.30.
  - **ERNA: faded.** $2.60 (23:30) → PM high $2.46 (−5.4%) on 6,159 / 88.
  - **KUST: faded.** $5.25 (22:30) → PM high $4.19 (−20.2%) on 1,613 / 29.
  - **VNTG: faded.** $0.74 (22:25) → PM high $0.71 (−4.1%) on 357 / 5.

### Missed Opportunities

| Ticker | AH Change | Why Missed | Would Be Profitable? |
|--------|-----------|------------|---------------------|
| DKI | +37.1% at 00:30 (first and only appearance); AH high +61.7% at 18:00 ET | 2-AH-scan gate (ignited 17:50 ET; FINAL-SCAN-GATE-BLOCK) | **Yes**: $2.29 → $3.72 **+62.4%**, after an overnight dip to $1.82 (−20.5%) |
| MRNO | +78% at 16:30 ET on 9.8M shares; +59% at 18:30 | Below `MIN_PRICE = $0.50` | Modest: 18:30 ask $0.3756 → $0.46 **+22.5%** peak; +3.8% to the latest $0.39 |

### AH Mover Follow-Through

Every name with two or more >10% AH scans. Current = latest SIP 5-minute close (04:15–04:20 ET).

| Ticker | AH Peak | Peak Time | AH Trajectory | Current PM | From Peak | From Close | Verdict |
|--------|---------|-----------|---------------|------------|-----------|------------|---------|
| IPW | $1.68 | 19:55 | **Build** (+17.3 → 21.0 → 24.0 → 25.0%) | $1.55 | −7.7% | +49.0% | PM peak $2.00 **exceeded AH by 19.0%**, transient (one bar) |
| PROF | $7.51 | 16:35 | **Spike→hold**, thin (+21.3 → 17.1 → 18.5 → 19.0%) | $6.82 | −9.2% | +20.1% | PM peak $6.92 **fell short (−7.9%)**; AH better |
| CPHI | $1.16 | 17:30 | **Late surge → fade** (+10.5 → 24.7 → 11.8%) | $0.84 | −27.6% | −1.2% | PM peak $0.96 **fell short (−17.2%)**; AH better |
| KUST | $5.95 | 16:15 | **Spike→fade** (+15.5 → 16.8%, then off the scan) | $4.19 | −29.6% | −6.9% | PM peak $4.19 **fell short (−29.6%)**; AH better |
| BFRG | $0.82 | 17:25 | **Spike→hold**, thin (+15.3 → 12.3%) | $0.68 | −17.1% | −4.2% | PM peak $0.72 **fell short (−12.2%)**; AH better |

DKI (one scan) is the reverse shape: AH spike→fade to $1.94, then a PM peak 37.8% above the $2.70 AH high.

**Chase-cap check:** IPW filled at +22.1% Total (qualifying +11.4%, +10.7 pts) and CPHI at +55.9% (qualifying +65.3%). Neither is near the ~+120% zone. PM reclaimed IPW's fill and never reclaimed CPHI's. No new chase case; standing **1 (XOS), never reclaimed**.

### Notes

- **Coverage, last 10 completed sessions (Sep 24–Oct 7):** **Sep 25 0/7, Sep 29 3/7, Oct 2 0/7, Oct 5 0/7.** Sep 24, 28, 30, Oct 1, Oct 6 and **Oct 7 ran 7/7.** That is **4 failures in 10 sessions**, still above the ≥2 trigger, so the scheduler/bridge investigation stays routed to the email.
- **CEILING-OVERRIDE / DEAD-CAT-OVERRIDE / FIRST-BAR-SPIKE WATCH:** none flagged last night. WHLR was a dead-cat skip that did not meet the watch condition (PM $0.77 < AH $0.84). Standings unchanged: dead-cat **3 positive / 4 negative**; first-bar **11 valid (2 ran / 9 faded-flat), 1 pending (ICMB)**. ICMB is still pending: no SIP PM prints again.
- **Fade-rule tally:** no SPIKE→FADE skips in the entry window. KUST (2 AH scans before 23:00) and ERNA (1 scan) faded before they could be considered. Sub-3M sample stays **4/23 (17.4%)**.
- **Final-scan gate-block: 2 → 3, all 3 ran.** New row **DKI** (Oct 7→8): float 1.2M, Grade None, ignition 17:50 ET, CONFIRM-3 YES 6.8x, fillable SIP ask, qualified at the final scan at $2.29 → PM SIP peak **$3.72 = +62.4%**. Caveat: the path went through $1.82 (−20.5%) overnight and a $2.04 PM open, so the result depends on holding through that dip. Previous rows: TRUG +47%, UPC +11.9%. Three of three late igniters ran, so this pulse routes a **final-scan-ignition exception proposal** to the daily email (CONFIRM-3 YES + accumulating SIP volume + fillable book, under the ceiling). The gate is unchanged here.
- **Raw PM leader / PM-only tracking:** the biggest raw PM mover is **DKI (+122.8%)**, an **AH→PM continuation** the scanner detected (AH +62% at 18:00 ET). The only PM-only gapper is **SDST** (below the floor, +69.7% in the 04:00 bar on 23M shares, then $0.10, +33%). `log/pm-open-scan.csv` has **no October 8 rows yet** at 04:38 ET. The CSV holdable PM-only count is **62**. Carry the Initiative-6 cluster to the email.
- **Price-floor exclusions: 11 → 12 observations across 8 → 9 nights; confirmed >100%-and-holdable stays 1 (TOPP).** New row **MRNO Oct 7→8**: close $0.2361, `tradable=true`, float 1.75M, Grade None (strategic-review 6-K). In-window AH +78% at 16:30 ET on 9.8M shares / 19,376 trades per 15 minutes, +59% at 18:30 ET. PM peak $0.46 (+94.8%). Hypothetical 18:30 ask $0.3756 → $0.46 = **+22.5%**. Verdict: **holdable on a tight book** (SIP spread 0.1% at 18:30 ET and 0.2% at 04:10 ET; AH held +50–75% for 3+ hours on millions of shares), **but not >100%**, so it does not count toward the trigger (**1 of 3, not met**). SDST (PM-only) and OLB (late tail, +1% at 18:30 ET) are not added.
- **Late-AH-tail tracking:** DKI's surge was at 17:50 ET, inside the window. IPW's tail climb to $1.68 at 19:55 ET continued a detected build, so it is not added (BIYA convention). Standing **2 true-tail (ORIS, GNS) / 1 feed-lag (BTCT)**, unchanged.
- **In-window feed-lag: 7, unchanged.** Every in-universe in-window mover above +10% on real volume was surfaced. Carry the whole-universe AH verification recommendation to the email.
- **Execution and selection trackers:** broker-block **2**, stale-book-only **6**, no-fillable-book **4**, float-only **1**, all unchanged. Both fills executed against frozen IEX quotes with SIP-priced limits again: IPW at 17:38 ET against a 16:59 quote, and CPHI at 18:02 ET against the 16:00 quote. CPHI's paper fill ($0.9978) came at the stale IEX ask, about 6% below the live SIP ask of $1.06. That is a paper-engine artifact in our favour; it belongs with the stale-book feed decision.
- **Actual-entry trackers:** both entries are **day-1 fresh igniters** (IPW Day −8.0%, CPHI Day +32.6%). IPW **ran** ($1.38 → $2.00, +44.9%); CPHI **faded** ($0.9978 → $0.96 peak, −3.8%). First-day igniters **29 → 31 entries (12 ran / 8 flat / 11 faded) = 38.7% ran**; multi-session **1, faded**, unchanged. IPW's August 7 reverse split is background, not the catalyst note, so the reverse-split tally stays **4/5 this-week faded / 4/6 older continued**.
- **Extreme-runner tally: 15 fades / 2 continues (88.2%), unchanged.** No AH peak reached the ~+130% zone: DKI +61.7% from $1.67 (+98.5% from the $1.36 October 6 close), SBFM about +124% Total from its $0.398 October 6 close, IPW +61.5%. The partial-profit routing trigger stays reached.
- **SIP basis checks:** October 7 closes DKI $1.67, IPW $1.04, CPHI $0.85, MRNO $0.2361 (SIP rounds to $0.24), SBFM $0.70, WHLR $0.69, PROF $5.68, KUST $4.50, ERNA $2.39, BFRG $0.71, OLB $0.387. October 6 closes for Entry Total%: IPW $1.13, CPHI $0.64. `price-timeline.py` uses the correct $1.67 / $1.04 October 7 basis this morning.
- **Tooling:** `broker.js bars --end` is ignored with `--tf 5Min` (AH queries returned PM bars). Use `--limit 48` from the AH start and filter by date.

### Daily Email Routing

- Headline: **DKI is today's winner. It was detected at the 00:30 final scan and blocked by the 2-AH-scan gate.** SIP PM peak $3.72 (+122.8%) at 04:21 ET on 3.8M shares in two bars; final-scan $2.29 → +62.4% hypothetical, after a −20.5% overnight dip. Our entries: IPW +$3.60 (+3.6%; peak +44.9% on the fill), CPHI −$18.48 (−19.7%). Net **−$14.88**. Detection **74/85 (87.1%)**, selection **37/81 (45.7%)**, 96 days tracked.
- **Decision for Juan — final-scan-ignition exception:** three late igniters blocked only by the 2-AH-scan gate (TRUG +47%, UPC +11.9%, DKI +62.4%) all ran into PM. Should a final-scan entry be allowed when CONFIRM-3 is YES, SIP volume is accumulating, the book is fillable and Total% is under the ceiling? DKI shows the cost: an overnight dip to −20.5% before the run.
- **Scheduler/bridge reliability (decision for Juan):** 4 coverage failures in the last 10 sessions (Sep 25, Sep 29, Oct 2, Oct 5). October 6 and 7 ran 7/7.
- **Stale-quote feed:** both fills again executed on frozen IEX quotes with SIP-priced limits; CPHI filled 6% below the live SIP ask.
- Carry forward: 7 feed-lag observations → whole-universe AH verification; 62-row holdable PM-only cluster → Initiative 6; 15/17 extreme-runner fades → partial-profit decision; reverse-split recency recommendation; sub-$0.50 floor question (TOPP 1 of 3; MRNO holdable but +94.8%). The sub-3M fade (4/23), price-floor (1 of 3) and first-bar (no new run) triggers are not met.

### Price Charts

Excerpts from `python3 scripts/price-timeline.py DKI IPW CPHI MRNO` at ~04:28 ET. Yahoo's 5-minute closes; the SIP tables above set the levels. The block charts are omitted.

```text
DKI   Previous Close: $1.67 (regular close 2026-10-07) | 2-Day Range: $1.38 - $3.72 | Current: $3.19 (+91.0%) | Peak: $3.72 (+122.8%) at 10-08 04:20 ET
  [REG] 10-07 12:40 ET: $2.27 (+35.9%)   [REG] 14:45: $1.57 (-6.0%)   [REG] 15:55: $1.71 (+2.4%)
  [PM]  10-08 04:00 ET: $1.91 (+14.4%)   [PM] 04:05: $2.06 (+23.4%)   [PM] 04:10: $2.53 (+51.5%)
  [PM]  10-08 04:15 ET: $3.48 (+108.4%)  [PM] 04:20: $3.46 (+107.2%)  [PM] 04:25: $3.22 (+92.8%)  [PM] 04:28: $3.19 (+91.0%)

IPW   Previous Close: $1.04 (regular close 2026-10-07) | Current: $1.46 (+40.3%) | Peak: $1.99 (+91.4%) at 10-08 04:10 ET
  [PM]  10-08 04:00 ET: $1.57   [PM] 04:05: $1.65   [PM] 04:10: $1.71   [PM] 04:15: $1.65   [PM] 04:20: $1.59

CPHI  [PM] 10-08 04:00 ET: $0.83   [PM] 04:05: $0.86   [PM] 04:10: $0.85   [PM] 04:20: $0.84

MRNO  [PM] 10-08 04:00 ET: $0.38   [PM] 04:05: $0.39   [PM] 04:15: $0.40   [PM] 04:21: $0.39
```
