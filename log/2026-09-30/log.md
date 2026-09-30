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

## Scan 22:20 CEST (4:20 PM ET)

`python3 scripts/scan.py --all` ran at 16:20:27 ET (22:20:27 CEST), in the AFTERHOURS session. Four new candidates were discovered; HIT and DKI each have their first >10% AH appearance. The four earlier AH scans were empty, and regular-session appearances do not count toward the two-AH-scan gate.

  Supplementary AH-change-only (>15%, not in volume pass): none

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| HIT | [TV](https://www.tradingview.com/chart/?symbol=HIT) | $0.82 | -3.7% | +18.2% | $0.97 | +13.8% | 1.0M | 156K | 6.4x | 20.5M | Information Technology Services |
| DKI | [TV](https://www.tradingview.com/chart/?symbol=DKI) | $1.57 | -38.4% | +27.4% | $2.00 | -21.6% | 208K | 207K | 1.0x | 1.2M | Packaged Software |
| MCDIF | [TV](https://www.tradingview.com/chart/?symbol=MCDIF) | $4.10 | +2.5% | +9.8% | $4.50 | +12.5% | 200K | 183K | 1.1x | n/a | Engineering & Construction |
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $1.24 | +1.6% | +7.3% | $1.33 | +9.0% | 144K | 40.8M | 0.0x | 4.4M | Miscellaneous Commercial Services |

### Evaluation notes

**Decision:** Observation only; no paper orders submitted. Entries begin at the 23:00 CEST scan. HIT and DKI have only one qualifying AH scan each; MCDIF and NCPL are below the >10% AH threshold in this snapshot. No filled position was added to the paper-trade table or `OPEN_POSITIONS.md`.

**Tradability:** Alpaca returned `tradable=true` for HIT, DKI, and NCPL. MCDIF returned `tradable=false`, OTC, inactive. Carry MCDIF as **untradable (carried)** on subsequent scans without repeating its SIP verification or catalyst searches. It is not yet an AH-qualified-but-untradable entry because this scan is below threshold and before the entry window.

**SIP volume and freshness:** `broker.js bars --tf 5Min --start 2026-09-30T20:00:00Z` returned consolidated SIP bars, not IEX. The newest available bar starts at 16:05 ET, 15 minutes before the scan; coverage remains incomplete for the later opening bars. Volume and prices below are SIP evidence; TradingView AH Vol is discovery data.

| Ticker | Bar start ET | High | Close | VWAP | Shares | Trades |
|--------|--------------|------|-------|------|--------|--------|
| HIT | 16:00 | $1.12 | $0.97 | $0.99 | 1,065,934 | 3,505 |
| HIT | 16:05 | $1.02 | $0.91 | $0.95 | 626,990 | 2,374 |
| DKI | 16:00 | $2.20 | $2.04 | $1.86 | 231,693 | 1,440 |
| DKI | 16:05 | $2.37 | $2.25 | $2.25 | 932,414 | 8,477 |
| NCPL | 16:00 | $1.36 | $1.33 | $1.28 | 147,135 | 212 |
| NCPL | 16:05 | $1.38 | $1.34 | $1.34 | 73,890 | 350 |

- **HIT — Watch; opening spike with fading volume.** SIP confirms 1,692,924 shares / 5,879 trades across two bars and corroborates the scanner's $0.97. Both volume and VWAP fell in the second bar. The available AH high is $1.12 at 16:00 ET; the scanner price is 13.4% below it. **FIRST-BAR-SPIKE WATCH (provisional): hypothetical $0.97 at 16:20 ET / 22:20 CEST.** Its only CONFIRM-3 observation is NO, and available SIP coverage is still limited to opening bars. Track whether a later volume-backed new high develops; a persistent opening-bar high with NO on every scan triggers the first-bar-spike entry skip. No sustained BUILD/HOLD is established yet. Float 20.5M; the company operates an InsurTech platform despite the scanner's IT-services label.
- **DKI — Skip live entry: Day -38.4%, dead-cat gate.** The opening move is real: 1,164,107 SIP shares / 9,917 trades, with volume, VWAP, and highs rising into 16:05 ET. This does not remove the regular-session-loss gate. The scanner's $2.00 is below the already-observed SIP $2.25 close; do not call this a bad print. Only one qualifying AH scan exists, so DEAD-CAT-OVERRIDE WATCH is not established yet; flag a hypothetical reclaim if AH% rises across at least two AH scans. Sector: mobile gaming / packaged software.
- **MCDIF — Skip: untradable.** AH +9.8%; no further workup. Float unknown; engineering and construction.
- **NCPL — Watch; below AH threshold and current book unverified.** Scanner AH +7.3%, with no qualifying AH appearance. SIP shows 221,025 shares / 562 trades across two bars, and volume fell from 147K to 74K. This is not an established volume-backed BUILD. VRatio 0.0x is the scanner's rounded value, not proof of zero AH volume. Sector: capital-raising services.

**Book checks:** HIT returned bid $1.00 x100 / ask $1.04 x100, timestamp 16:10:50 ET. DKI returned bid $1.29 x100 / ask $0.00 x0 at 16:00:02 ET; NCPL returned bid $1.23 x100 / ask $0.00 x0 at 16:00:41 ET. One re-pull returned the same timestamps. These are stale snapshots; none establishes a current fillable book at 16:20. DKI and NCPL cannot be sized from a zero-ask snapshot. Their SIP bars show real AH trades, so the stale quotes do not justify claiming their AH volume is fictitious. Recheck current two-sided prices and sizes at any eligible entry scan.

**Spike-bar and third-bar instrumentation (verbatim; log only):**

```text
HIT 2026-09-30  SPIKE  16:00ET  +37%  $1.12  221 trades / 67k sh  (first co-spike bar) (as-of 16:20ET)
DKI 2026-09-30  SPIKE  16:01ET  +20%  $1.89  256 trades / 43k sh  (first co-spike bar) (as-of 16:20ET)
HIT 2026-09-30  CONFIRM-3  NO no local-volume new-high ignition as-of 16:20ET
DKI 2026-09-30  CONFIRM-3  PENDING ignition 16:05ET; waiting for third bar as-of 16:20ET
```

CONFIRM-3 PENDING on DKI reflects the available bars; the newest SIP bar is still 16:05 ET. The instrumentation does not establish an entry grade or independently qualify a trade.

**Structured catalyst searches:** Four `websearch search` calls per >10% ticker: earnings on September 30, one Tavily retry after the default provider was rate limited, same-day press releases, and SEC material filings (8-K, plus 6-K for foreign issuer DKI). Search budgets are exhausted for this pulse. **HIT and DKI: no catalyst found.** No fresh release with a verified September 30 or immediately preceding overnight publication date/time was found; both grades are **None**. No catalyst is a documented concern, not a learning-phase entry skip.

- **HIT:** Earnings search returned August 13, 2026 Q2 results; the [company release index](https://healthintech.investorroom.com/Press-Releases?l=50) and [SEC index](https://healthintech.investorroom.com/SEC-Filings) returned older items. Search also surfaced the September 9 Newsweek award and September 15–16 insider tax-withholding filings. These are background; no publication time is verified or used for grading.
- **DKI:** [Earnings history](https://www.marketbeat.com/stocks/NASDAQ/DKI/earnings) returned August 13, 2026 results. The PR search returned a [February 17, 2026 shareholder letter](https://www.sec.gov/Archives/edgar/data/2058584/000149315226006949/ex99-1.htm). The [filing index](https://www.stocktitan.net/sec-filings/DKI) returned a September 18 filing and an October 6 meeting notice, not a verified fresh announcement. These are background; no publication time is verified or used for grading.

**Carry forward:** Add HIT, DKI, MCDIF, and NCPL to tonight's 24-name regular-session pipeline (28 unique names total). Carry seven untradable names: GBLRF, MHUAF, SFES, WTLLF, BMNM, FNFI, MCDIF. Recheck tracked tradable names at the 00:30 CEST final-scan feed-lag cross-check. Before any later fill, check recent daily bars and prior winner history for MULTI-SESSION-RUNNER instrumentation; the HIT winner record found so far is from March 17, not a recent prior session.

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
