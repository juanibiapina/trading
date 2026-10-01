# Trading Log — 2026-10-01

## Position Evaluation — 10:30 CEST

**Result:** No open positions and no open orders on Alpaca paper account `PA37U2Y192A7`. `OPEN_POSITIONS.md` matches the broker.

**Broker checks:** `account`, `positions --json`, `orders all --json`, `orders all`, and `orders open`. Equity and cash: **$99,721.90**; buying power: **$398,887.60**. Account active, trading not blocked. Latest fill: TOPS sell, 64 shares at $0.70 on 2026-09-23 (order `b732f236`), already recorded in Closed Positions.

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|

No position rows to evaluate. Position prices, SIP peaks, holding periods, and risk triggers are not applicable.

**Actions taken:**

- Created today's log and reconciled the empty position table against Alpaca.
- No sells or stop updates required.
- No items requiring Juan's input for the daily email.

Time: 10:30 CEST (08:30 UTC); today's premarket opened at 08:00 UTC.

## Position Evaluation — 14:30 CEST

**Result:** No open positions and no open orders on Alpaca paper account `PA37U2Y192A7`. `OPEN_POSITIONS.md` matches the broker.

**Broker checks:** `account`, `positions`, `positions --json` (returned `[]`), `orders all`, and `orders open`. Equity and cash: **$99,721.90**; buying power: **$398,887.60**. Account active, trading not blocked. Latest listed fill: TOPS sell, 64 shares at $0.70 (order `b732f236`), already recorded in Closed Positions.

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|

No position rows to evaluate. Position prices, SIP peaks, holding periods, and risk triggers are not applicable.

**Actions taken:**

- Verified the empty Current Positions table against Alpaca; no reconciliation edits required.
- No sells or stop updates required.
- No items requiring Juan's input for the daily email.

Time: 14:30 CEST (12:30 UTC / 08:30 EDT); today's premarket opened at 08:00 UTC.

## Scan 21:30 CEST (3:30 PM ET)

**Decision:** Watch — pending AH confirmation. No paper orders submitted; this scan precedes the 16:00 ET AH open and the 23:00 CEST entry window.

`python3 scripts/scan.py --all` ran at 15:30:30 ET (21:30:30 CEST / 19:30:30 UTC), in the REGULAR session, and returned 28 candidates. The US trading date is 2026-10-01. This is today's first discovery scan; regular-session appearances add zero qualifying AH scans. Prices and volumes below are regular-session scanner readings; AH change, AH volume, and AH VRatio are not available yet.

| Ticker | Chart | Price | Day% | 5mVol | Avg5m | IRVol | VChg% | Float | Industry |
|--------|-------|-------|------|-------|-------|-------|-------|-------|----------|
| EVOL | [TV](https://www.tradingview.com/chart/?symbol=EVOL) | $0.60 | +0.0% | 11K | 1K | 40.9 | +3564.0% | 3.7M | Information Technology Services |
| GBLRF | [TV](https://www.tradingview.com/chart/?symbol=GBLRF) | $0.71 | +146.4% | 40K | 0 | 32.7 | +8788.9% | 135.3M | Other Metals/Minerals |
| LONA | [TV](https://www.tradingview.com/chart/?symbol=LONA) | $4.41 | +23.5% | 8K | 9K | 30.3 | -73.1% | 6.4M | Biotechnology |
| MHUAF | [TV](https://www.tradingview.com/chart/?symbol=MHUAF) | $7.00 | +0.0% | 5K | 631 | 28.7 | +4955.0% | 613K | Medical Specialties |
| MTNE | [TV](https://www.tradingview.com/chart/?symbol=MTNE) | $9.90 | -0.2% | 27K | 4K | 23.0 | +27088.0% | 22.0M | Financial Conglomerates |
| CRMZ | [TV](https://www.tradingview.com/chart/?symbol=CRMZ) | $2.10 | -2.3% | 12K | 6K | 13.5 | -16.3% | 4.7M | Packaged Software |
| FNFI | [TV](https://www.tradingview.com/chart/?symbol=FNFI) | $9.15 | -2.9% | 15K | 2K | 13.3 | +3972.0% | 1.0M | Savings Banks |
| SGRP | [TV](https://www.tradingview.com/chart/?symbol=SGRP) | $0.65 | -7.0% | 7K | 4K | 11.3 | +30.9% | 12.3M | Advertising/Marketing Services |
| LTCEF | [TV](https://www.tradingview.com/chart/?symbol=LTCEF) | $2.77 | +1.6% | 14K | 2K | 10.4 | +7075.5% | 33.7M | Integrated Oil |
| KUST | [TV](https://www.tradingview.com/chart/?symbol=KUST) | $4.65 | +998.8% | 100 | 782 | 0.4 | -87.4% | 625K | Miscellaneous Commercial Services |
| MYPS | [TV](https://www.tradingview.com/chart/?symbol=MYPS) | $4.64 | +877.0% | 2K | 3K | 0.2 | -6.9% | 8.2M | Packaged Software |
| NXL | [TV](https://www.tradingview.com/chart/?symbol=NXL) | $7.24 | +69.0% | 100 | 120K | 3199.1 | -99.9% | 652K | Medical Specialties |
| SSM | [TV](https://www.tradingview.com/chart/?symbol=SSM) | $1.76 | +57.1% | 555 | 618K | 11.8 | -100.0% | 1.1M | Motor Vehicles |
| VEEA | [TV](https://www.tradingview.com/chart/?symbol=VEEA) | $3.37 | +55.3% | 150 | 226K | 35.8 | -100.0% | 1.6M | Packaged Software |
| SDEV | [TV](https://www.tradingview.com/chart/?symbol=SDEV) | $3.54 | +36.5% | 700 | 231K | 3.3 | -99.6% | 1.8M | Pharmaceuticals: Major |
| BIRD | [TV](https://www.tradingview.com/chart/?symbol=BIRD) | $3.53 | +35.2% | 100 | 56K | 15.7 | -99.8% | 6.7M | Data Processing Services |
| GIPR | [TV](https://www.tradingview.com/chart/?symbol=GIPR) | $0.53 | +31.6% | 963 | 159K | 3.8 | -99.4% | 2.8M | Real Estate Investment Trusts |
| SES | [TV](https://www.tradingview.com/chart/?symbol=SES) | $0.78 | +30.2% | 2K | 701K | 4.8 | -99.7% | 250.0M | Electrical Products |
| NAMM | [TV](https://www.tradingview.com/chart/?symbol=NAMM) | $1.25 | +30.1% | 269 | 699K | 44.9 | -99.9% | 6.7M | Precious Metals |
| CMCT | [TV](https://www.tradingview.com/chart/?symbol=CMCT) | $3.76 | +28.5% | 450 | 17K | 0.3 | -98.8% | 2.8M | Real Estate Investment Trusts |
| EJH | [TV](https://www.tradingview.com/chart/?symbol=EJH) | $1.80 | +26.8% | 200 | 2K | 161.0 | -90.2% | 2.5M | Other Consumer Services |
| AISP | [TV](https://www.tradingview.com/chart/?symbol=AISP) | $2.32 | +25.0% | 2K | 53K | 253.4 | -95.0% | 24.5M | Packaged Software |
| MEDS | [TV](https://www.tradingview.com/chart/?symbol=MEDS) | $3.88 | +22.6% | 240 | 33K | 3.2 | -98.4% | 1.5M | Medical Distributors |
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $1.51 | +21.8% | 100 | 37K | 0.2 | -99.7% | 4.4M | Miscellaneous Commercial Services |
| BTTC | [TV](https://www.tradingview.com/chart/?symbol=BTTC) | $0.63 | +21.2% | 100 | 70K | 2.3 | -99.7% | 10.8M | Packaged Software |
| DMRC | [TV](https://www.tradingview.com/chart/?symbol=DMRC) | $6.93 | +19.1% | 100 | 4K | 2.8 | -99.1% | 19.3M | Packaged Software |
| INSG | [TV](https://www.tradingview.com/chart/?symbol=INSG) | $4.34 | +18.6% | 100 | 7K | 11.7 | -97.3% | 12.8M | Telecommunications Equipment |
| ATOS | [TV](https://www.tradingview.com/chart/?symbol=ATOS) | $2.28 | +16.9% | 1K | 2K | 1.9 | -5.1% | 9.8M | Pharmaceuticals: Major |

### Evaluation notes

**Watch — pending AH confirmation (20 names):** LONA, MTNE, KUST, MYPS, NXL, SSM, VEEA, SDEV, BIRD, GIPR, SES, NAMM, CMCT, AISP, MEDS, NCPL, BTTC, DMRC, INSG, ATOS. `broker.js tradable` returned `tradable=true` for each. Float and industry are recorded for pattern tracking; SES's 250.0M float does not independently disqualify it in the learning phase.

**Untradable — carry forward (8 names):** EVOL, GBLRF, MHUAF, CRMZ, FNFI, SGRP, LTCEF, EJH each returned `tradable=false`. The first seven are OTC; EJH is active on Nasdaq but still untradable on Alpaca. Carry these broker blocks into later scans without repeating SIP verification or catalyst searches. None is yet an AH-qualified-but-untradable entry; this scan records regular-session discovery only.

**Trajectory observations:** NXL (+69.0%), SSM (+57.1%), and VEEA (+55.3%) lead the listed day movers after KUST and MYPS. Their displayed latest five-minute volumes are 100, 555, and 150 shares, with VChg -99.9%, -100.0%, and -100.0%. These regular-session fields do not establish real AH accumulation or an AH BUILD/HOLD. LONA's VChg is -73.1%; MTNE's is +27088.0%. Both require AH confirmation. All displayed Day% values exceed -15% at this checkpoint; recheck the completed regular close before any entry.

**Price-basis verification pending:** KUST (+998.8%) and MYPS (+877.0%) show extreme scanner day gains. No corporate-action adjustment or prior-close basis has been verified. Preserve the readings as discovery evidence and verify that basis if either becomes an AH candidate; no entry grade is assigned from these percentages.

**AH evidence:** The regular-session scanner did not emit `Supplementary AH-change-only` or `AH >10% at this snapshot (unrounded)` lines. There is no >10% AH appearance to count and no AH candidate requiring catalyst, SIP, spike-bar, or CONFIRM-3 instrumentation at this scan. Any later entry requires >10% AH in at least two AH scans, the entry window, trajectory and extension checks, real SIP accumulation, and a current two-sided fillable book. No-catalyst results are a concern to document, not a learning-phase skip reason.

**Carry forward:** Retain all 28 names in tonight's pipeline, including the eight untradable broker blocks, for later scans and the 00:30 CEST final-scan feed-lag cross-check. The AH session starts at `2026-10-01T20:00:00Z` (16:00 EDT / 22:00 CEST).

**Daily email:** No item from this scan requires Juan's input.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|

No entries from the 21:30 CEST scan: observation only before AH opens.
