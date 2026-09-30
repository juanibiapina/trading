# Post-Market Screening - 2026-09-30

## Scan 21:30 CEST (3:30 PM ET)

Regular-session checkpoint before the 16:00 ET after-hours open. `python3 scripts/scan.py --all` ran at 15:30:57 ET; the saved refresh at 15:31:52 ET returned the 23 names below. These are regular-session prices and five-minute volumes. After-hours change, volume, and VRatio are not available yet.

| Ticker | Chart | Price | Day% | 5mVol | Avg5m | IRVol | VChg% | Float | Industry |
|--------|-------|-------|------|-------|-------|-------|-------|-------|----------|
| TGE | [TV](https://www.tradingview.com/chart/?symbol=TGE) | $1.49 | +79.5% | 75K | 527K | 9968.4 | -74.3% | 44.2M | Financial Conglomerates |
| CMCT | [TV](https://www.tradingview.com/chart/?symbol=CMCT) | $2.85 | +48.4% | 39K | 263K | 1311.2 | -69.2% | 2.8M | Real Estate Investment Trusts |
| CHGA | [TV](https://www.tradingview.com/chart/?symbol=CHGA) | $2.30 | +17.3% | 33K | 42K | 781.1 | +25.4% | 1.1M | Biotechnology |
| GOW | [TV](https://www.tradingview.com/chart/?symbol=GOW) | $3.30 | +82.3% | 234K | 517K | 129.9 | -85.1% | n/a | Financial Conglomerates |
| TNON | [TV](https://www.tradingview.com/chart/?symbol=TNON) | $4.01 | +46.9% | 30K | 98K | 99.9 | -81.2% | 899K | Medical/Nursing Services |
| CNTB | [TV](https://www.tradingview.com/chart/?symbol=CNTB) | $1.20 | +21.0% | 144K | 156K | 58.8 | +49.7% | 17.0M | Pharmaceuticals: Major |
| GBLRF | [TV](https://www.tradingview.com/chart/?symbol=GBLRF) | $0.71 | +146.4% | 40K | 0 | 32.7 | +8788.9% | 135.3M | Other Metals/Minerals |
| MHUAF | [TV](https://www.tradingview.com/chart/?symbol=MHUAF) | $7.00 | +0.0% | 5K | 631 | 28.7 | +4955.0% | 613K | Medical Specialties |
| SFES | [TV](https://www.tradingview.com/chart/?symbol=SFES) | $0.50 | +9.9% | 10K | 16K | 26.9 | +3965.0% | 12.1M | Investment Managers |
| VBIO | [TV](https://www.tradingview.com/chart/?symbol=VBIO) | $2.72 | -3.9% | 24K | 54K | 25.6 | -91.1% | 886K | Medical Specialties |
| WTLLF | [TV](https://www.tradingview.com/chart/?symbol=WTLLF) | $4.45 | +6.7% | 24K | 5K | 18.2 | +20.0% | 7.0M | Engineering & Construction |
| BMNM | [TV](https://www.tradingview.com/chart/?symbol=BMNM) | $2.70 | -1.6% | 8K | 1K | 15.6 | +1016.4% | 5.4M | Financial Conglomerates |
| RFL | [TV](https://www.tradingview.com/chart/?symbol=RFL) | $1.28 | -36.9% | 8K | 6K | 15.2 | -4.3% | 35.0M | Real Estate Development |
| FNFI | [TV](https://www.tradingview.com/chart/?symbol=FNFI) | $9.15 | -2.9% | 15K | 2K | 13.3 | +3972.0% | 1.0M | Savings Banks |
| FFR | [TV](https://www.tradingview.com/chart/?symbol=FFR) | $1.41 | +39.1% | 8K | 62K | 0.0 | -79.5% | 7.1M | Packaged Software |
| SOTK | [TV](https://www.tradingview.com/chart/?symbol=SOTK) | $6.02 | +20.9% | 159 | 578 | 14.0 | -47.0% | 13.2M | Industrial Machinery |
| MSGY | [TV](https://www.tradingview.com/chart/?symbol=MSGY) | $5.35 | +20.5% | 19K | 16K | 1.8 | -6.4% | 1.5M | Engineering & Construction |
| FBDT | [TV](https://www.tradingview.com/chart/?symbol=FBDT) | $1.04 | +18.1% | 475 | 7K | 1.3 | -98.1% | 26.9M | Aerospace & Defense |
| ACTU | [TV](https://www.tradingview.com/chart/?symbol=ACTU) | $0.80 | +17.0% | 1K | 7K | 1.8 | -87.5% | 10.2M | Pharmaceuticals: Major |
| PMVP | [TV](https://www.tradingview.com/chart/?symbol=PMVP) | $1.67 | +16.8% | 2K | 27K | 6.4 | -98.6% | 68.1M | Biotechnology |
| TLSA | [TV](https://www.tradingview.com/chart/?symbol=TLSA) | $1.11 | +16.4% | 6K | 30K | 2.1 | -40.3% | 65.4M | Pharmaceuticals: Major |
| MWYN | [TV](https://www.tradingview.com/chart/?symbol=MWYN) | $1.15 | +15.6% | 3K | 1K | 1.1 | +202.5% | 14.2M | Home Improvement Chains |
| EPOW | [TV](https://www.tradingview.com/chart/?symbol=EPOW) | $4.38 | +15.6% | 2K | 2K | 1.6 | +157.4% | 1.8M | Packaged Software |

### Evaluation notes

**Watch — pending AH confirmation:** TGE, CMCT, CHGA, GOW, TNON, CNTB, VBIO, RFL, FFR, SOTK, MSGY, FBDT, ACTU, PMVP, TLSA, MWYN, EPOW. Alpaca returned `tradable=true` for each. Float and sector are recorded for pattern tracking; GOW's float is unknown. Regular-session appearances contribute zero qualifying AH scans.

**Untradable — carry forward:** GBLRF, MHUAF, SFES, WTLLF, BMNM, FNFI each returned `tradable=false` on Alpaca (OTC). Carry these broker blocks into later scans without repeating SIP verification or catalyst searches. None is yet an AH-qualified-but-untradable entry; this checkpoint records discovery only.

**Additional initial-scan watch:** SGRX appeared at 15:30:57 ET ($1.68, Day +11.2%, 5mVol 6K, Avg5m 4K, IRVol 10.9, VChg +117.3%, float 800K, Food: Meat/Fish/Dairy), then dropped out of the refresh. Alpaca `tradable=true`; retain it in tonight's pipeline. Total unique names across the two snapshots: 24.

**Trajectory observations:** TGE and GOW lead the refreshed listed names at +79.5% and +82.3% on the day. Their five-minute volume changes are -74.3% and -85.1%; CMCT and TNON are also slowing (-69.2% / -81.2%). CHGA and CNTB have rising five-minute volume (+25.4% / +49.7%). These intraday observations require AH rechecks before any BUILD/HOLD classification. RFL is down 36.9% intraday; if its closing Day% remains at or below -15%, the dead-cat entry skip applies. Check any subsequent rising reclaim for a hypothetical DEAD-CAT-OVERRIDE WATCH.

**Decision:** Observation only; no paper orders submitted. It is before the AH open and before the 23:00 CEST entry window. Entry requires >10% AH on at least two AH scans plus the per-candidate trajectory, extension, real SIP volume, and current fillable-book checks. Recheck the 24 tracked names at the 00:30 CEST final-scan feed-lag cross-check; carry the six untradable broker blocks. No item from this scan requires Juan's input.

## Scan 22:00 CEST (4:00 PM ET)

`python3 scripts/scan.py --all` ran at 16:00:57 ET (22:00:57 CEST), in the AFTERHOURS session. No candidates found.

  Supplementary AH-change-only (>15%, not in volume pass): none

### Evaluation notes

**Decision:** Observation only; no paper orders submitted. Entries begin at the 23:00 CEST scan and require >10% AH change in at least two AH scans plus all entry gates. This snapshot is less than one minute after the AH open; empty scanner results do not establish that the regular-session watch names have faded.

**Carry forward:** The 24 names tracked at 21:30 remain in tonight's pipeline for later AH scans and the 00:30 final-scan feed-lag cross-check. GBLRF, MHUAF, SFES, WTLLF, BMNM, and FNFI remain untradable (carried). No new >10% AH candidate was discovered, so no candidate catalyst, SIP, spike-bar, or CONFIRM-3 workup was triggered by this scan.

**Daily email:** No item from this scan requires Juan's input.

## Scan 22:05 CEST (4:05 PM ET)

`python3 scripts/scan.py --all` ran at 16:05:42 ET (22:05:42 CEST), in the AFTERHOURS session. No candidates found.

  Supplementary AH-change-only (>15%, not in volume pass): none

### Evaluation notes

**Decision:** Observation only; no paper orders submitted. Entries begin at the 23:00 CEST scan and require >10% AH change in at least two AH scans plus all entry gates. Both opening AH scans (22:00 and 22:05) returned no candidates. Neither scan adds a qualifying AH appearance to any name.

**Carry forward:** The 24 names tracked at 21:30 remain in tonight's pipeline for later AH scans and the 00:30 final-scan feed-lag cross-check. GBLRF, MHUAF, SFES, WTLLF, BMNM, and FNFI remain untradable (carried). Empty discovery results five minutes after the AH open do not establish their current AH trajectory. No new >10% AH candidate was discovered, so no candidate catalyst, SIP, spike-bar, or CONFIRM-3 workup was triggered by this scan.

**Daily email:** No item from this scan requires Juan's input.

## Scan 22:10 CEST (4:10 PM ET)

`python3 scripts/scan.py --all` ran at 16:10:41 ET (22:10:41 CEST), in the AFTERHOURS session. No candidates found.

  Supplementary AH-change-only (>15%, not in volume pass): none

### Evaluation notes

**Decision:** Observation only; no paper orders submitted. Entries begin at the 23:00 CEST scan and require >10% AH change in at least two AH scans plus all entry gates. All three opening AH scans (22:00, 22:05, and 22:10) returned no candidates; no name has a qualifying AH appearance from these scans.

**Carry forward:** The 24 names tracked at 21:30 remain in tonight's pipeline for later AH scans and the 00:30 final-scan feed-lag cross-check. GBLRF, MHUAF, SFES, WTLLF, BMNM, and FNFI remain untradable (carried). Empty discovery results ten minutes after the AH open do not establish the watch names' current AH trajectory. No >10% AH candidate was discovered, so this scan triggered no catalyst, SIP, spike-bar, or CONFIRM-3 workup.

**Daily email:** No item from this scan requires Juan's input.

## Scan 22:15 CEST (4:15 PM ET)

`python3 scripts/scan.py --all` ran at 16:15:26 ET (22:15:26 CEST), in the AFTERHOURS session. No candidates found.

  Supplementary AH-change-only (>15%, not in volume pass): none

### Evaluation notes

**Decision:** Observation only; no paper orders submitted. Entries begin at the 23:00 CEST scan and require >10% AH change in at least two AH scans plus all entry gates. All four opening AH scans (22:00, 22:05, 22:10, and 22:15) returned no candidates; no name has a qualifying AH appearance from these scans.

**Carry forward:** The 24 names tracked at 21:30 remain in tonight's pipeline for later AH scans and the 00:30 final-scan feed-lag cross-check. GBLRF, MHUAF, SFES, WTLLF, BMNM, and FNFI remain untradable (carried). Empty discovery results fifteen minutes after the AH open do not establish the watch names' current AH trajectory. No >10% AH candidate was discovered, so this scan triggered no catalyst, SIP, spike-bar, or CONFIRM-3 workup.

**Daily email:** No item from this scan requires Juan's input.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|

## Position Evaluation — 10:30 CEST

Alpaca paper account PA37U2Y192A7 reports no open positions. `OPEN_POSITIONS.md` matches.

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|

**Actions taken:** None; no positions to evaluate or sell.

## Position Evaluation — 14:30 CEST

Alpaca paper account PA37U2Y192A7 reports no open positions. `OPEN_POSITIONS.md` matches; no open orders appeared in the order list.

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|

**Actions taken:** None; no positions to evaluate or sell.
