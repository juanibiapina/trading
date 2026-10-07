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

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
