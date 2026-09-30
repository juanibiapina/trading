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

## Scan 22:25 CEST (4:25 PM ET)

`python3 scripts/scan.py --all` ran at 16:25:26 ET (22:25:26 CEST), in the AFTERHOURS session. Five candidates were discovered; BENF and FLNA are new tonight. HIT and DKI each have two >10% AH appearances, at 22:20 and 22:25. Entries begin at 23:00 CEST.

  Supplementary AH-change-only (>15%, not in volume pass): none

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| HIT | [TV](https://www.tradingview.com/chart/?symbol=HIT) | $0.82 | -3.7% | +13.3% | $0.93 | +9.1% | 1.6M | 221K | 7.1x | 20.5M | Information Technology Services |
| DKI | [TV](https://www.tradingview.com/chart/?symbol=DKI) | $1.57 | -38.4% | +42.1% | $2.23 | -12.5% | 960K | 304K | 3.2x | 1.2M | Packaged Software |
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $1.24 | +1.6% | +8.9% | $1.35 | +10.7% | 204K | 40.8M | 0.0x | 4.4M | Miscellaneous Commercial Services |
| BENF | [TV](https://www.tradingview.com/chart/?symbol=BENF) | $1.36 | -3.5% | +5.1% | $1.43 | +1.4% | 87K | 42.7M | 0.0x | 2.1M | Investment Managers |
| FLNA | [TV](https://www.tradingview.com/chart/?symbol=FLNA) | $0.89 | -4.2% | +10.0% | $0.97 | +5.4% | 52K | 10.8M | 0.0x | 47.3M | Biotechnology |

### Evaluation notes

**Decision:** Observation only; no paper orders submitted. HIT and DKI clear the two-AH-scan count but still require the entry window and all other gates. No filled position was added to the paper-trade table or `OPEN_POSITIONS.md`. Float and sector remain pattern-tracking data, not learning-phase skip reasons.

**Tradability:** BENF and FLNA returned `tradable=true` before their SIP workup. Carry the earlier `tradable=true` results for HIT, DKI, and NCPL. MCDIF dropped out of this snapshot and remains **untradable (carried)**; its verification and catalyst searches were not repeated.

**SIP evidence:** All five bar requests used `--tf 5Min --start 2026-09-30T20:00:00Z` and returned `feed=sip`. The latest available bar starts at 16:10 ET, 15 minutes behind this scan, covering trades through 16:15. These delayed bars confirm opening activity; they do not establish the price at 16:25. No bad-print rejection is supported by a price difference against this incomplete coverage.

| Ticker | Bar start ET | High | Close | VWAP | Shares | Trades |
|--------|--------------|------|-------|------|--------|--------|
| HIT | 16:10 | $1.08 | $1.03 | $1.03 | 1,596,712 | 7,553 |
| DKI | 16:10 | $2.35 | $2.16 | $2.17 | 398,562 | 4,121 |
| NCPL | 16:10 | $1.47 | $1.43 | $1.42 | 191,674 | 770 |
| BENF | 16:00 | $1.36 | $1.36 | $1.36 | 86,756 | 4 |
| BENF | 16:05 | $1.43 | $1.43 | $1.43 | 724 | 1 |
| BENF | 16:10 | $1.41 | $1.41 | $1.40 | 1,900 | 3 |
| FLNA | 16:00 | $0.98 | $0.98 | $0.93 | 29,987 | 52 |
| FLNA | 16:05 | $0.99 | $0.98 | $0.96 | 23,133 | 84 |
| FLNA | 16:10 | $0.98 | $0.94 | $0.97 | 17,133 | 90 |

- **HIT — Watch; opening high still unreclaimed.** Scanner AH +18.2% → +13.3%, price $0.97 → $0.93; discovery volume 1.0M → 1.6M and VRatio 6.4x → 7.1x. SIP totals 3,289,636 shares / 13,432 trades across three bars. The third bar regained volume and VWAP after the second-bar dip, but its $1.08 high remains below the $1.12 opening high at 16:00 ET. Scanner price is 17.0% below that high. **FIRST-BAR-SPIKE WATCH (provisional): hypothetical $0.93 at 16:25 ET / 22:25 CEST.** CONFIRM-3 is NO on both scans; if the opening high remains unreclaimed with NO on every scan at entry time, apply the first-bar-spike skip. Later-bar coverage remains incomplete, so do not classify an established BUILD from discovery volume alone. Grade **None**; InsurTech / IT services.
- **DKI — Skip live entry: Day -38.4%, dead-cat gate. DEAD-CAT-OVERRIDE WATCH: hypothetical $2.23 at 16:25 ET / 22:25 CEST.** Scanner AH +27.4% → +42.1% and price $2.00 → $2.23 across two AH scans, both above the $1.57 regular close. This meets the rising-reclaim watch condition while retaining the live-entry skip. SIP totals 1,562,669 shares / 14,038 trades; the third bar is liquid but slowed from 932K shares / 8,477 trades to 399K / 4,121, with VWAP $2.25 → $2.17. Available high $2.37 at 16:05 ET; scanner price is 5.9% below it. Grade **None**; mobile gaming / packaged software.
- **NCPL — Watch; scanner remains below threshold.** AH +7.3% → +8.9%, price $1.33 → $1.35; discovery volume 144K → 204K. SIP totals 412,699 shares / 1,332 trades; the third bar improved to 192K / 770 trades and a new available high of $1.47. Its earlier 16:10-bar close $1.43 was approximately +15.3% above the rounded regular close, exceeding the delayed scanner reading. Retain this discrepancy for later verification; it does not establish a second current >10% AH scan. A sustained volume-backed BUILD and current fillable book remain unconfirmed. Sector: capital-raising services. Run the structured catalyst search if it qualifies above threshold in a later scan.
- **BENF — Skip current setup: below AH threshold and sparse trading.** Only eight SIP trades / 89,380 shares across three bars; 86,756 shares were concentrated in four opening trades, followed by 724 and 1,900 shares. This is not sustained liquid accumulation. The zero-ask snapshot is stale and cannot support sizing. Sector: investment managers.
- **FLNA — Watch below the verified threshold; thin volume.** The original scanner rounded AH change to +10.0%; that alone does not verify the strict >10% gate. A separate unrounded scanner check at 16:27:45 ET returned +9.503386%, AH price $0.9702, regular close $0.886. Do not count that check as another scheduled scan or infer the original unrounded value from it. SIP totals 70,253 shares / 226 trades, with shares declining 29,987 → 23,133 → 17,133; this is thin trading, not a volume-backed BUILD. Grade **None**; Filana Therapeutics, formerly Cassava Sciences, epilepsy biotechnology. The 47.3M float is recorded for pattern tracking.

**Book freshness:** HIT returned bid $1.00 x100 / ask $1.04 x100 at 16:10:50 ET; DKI bid $1.29 x100 / ask $0.00 x0 at 16:00:02 ET. One re-pull returned the same timestamps. NCPL returned bid $1.23 x100 / ask $0.00 x0 at 16:00:41 ET; BENF bid $1.20 x100 / ask $0.00 x0 at 16:00:02 ET; FLNA bid $0.76 x100 / ask $1.08 x100 at 16:00:00 ET. All are stale relative to the scan. No current two-sided fillable book is established; no order can be sized from these snapshots. SIP confirms real AH trades, so stale zero asks do not prove the observed volume is fictitious. Recheck books at any eligible entry scan.

**Spike-bar and third-bar instrumentation (verbatim; log only):** HIT and DKI exceed the scanner threshold. FLNA was also instrumented because the displayed percentage was at the rounding boundary; NCPL was instrumented because its available SIP bars exceeded +10% despite the lower scanner reading.

```text
HIT 2026-09-30  SPIKE  16:00ET  +37%  $1.12  221 trades / 67k sh  (first co-spike bar) (as-of 16:25ET)
HIT 2026-09-30  CONFIRM-3  NO no local-volume new-high ignition as-of 16:25ET
DKI 2026-09-30  SPIKE  16:01ET  +20%  $1.89  256 trades / 43k sh  (first co-spike bar) (as-of 16:25ET)
DKI 2026-09-30  CONFIRM-3  PENDING ignition 16:05ET; waiting for third bar as-of 16:25ET
FLNA 2026-09-30  NO-SPIKE  peak +11% @16:09ET  (no bar cleared +15% on a volume co-spike) (as-of 16:25ET)
FLNA 2026-09-30  CONFIRM-3  NO no local-volume new-high ignition as-of 16:25ET
NCPL 2026-09-30  SPIKE  16:13ET  +18%  $1.46  213 trades / 79k sh  (first co-spike bar) (as-of 16:25ET)
NCPL 2026-09-30  CONFIRM-3  NO no local-volume new-high ignition as-of 16:25ET
```

DKI's third ignition bar starts at 16:15 ET and is outside the available SIP coverage; PENDING remains expected. The instrumentation does not grade or rank entries; HIT's provisional watch records the separately specified persistent-opening-high rule.

**Catalyst freshness:** Three Tavily `websearch search` calls each refreshed HIT and DKI earnings, same-day press releases, and material SEC filings (8-K / 6-K for DKI). FLNA received four calls covering earnings, press releases, and SEC filings; the initial earnings query included unrelated company names, which were discarded, and the fourth call checked the correctly identified Filana Therapeutics. No catalyst with a verified current-trading-date or preceding-overnight publication date/time was found. Grades remain **None**; absence of a catalyst is a concern, not a learning-phase entry skip.

- **HIT:** [Earnings history](https://www.wallstreetzen.com/stocks/us/nasdaq/hit/earnings) returned August 13, 2026 results. The [company release index](https://healthintech.investorroom.com/Press-Releases?l=50) returned older announcements; the [company SEC index](https://healthintech.investorroom.com/SEC-Filings) returned August 13 8-Ks, and other filing results returned September 15–16 insider tax-withholding disclosures. These dates are background, not fresh catalysts; no publication time was used for grading.
- **DKI:** [Earnings history](https://www.marketbeat.com/stocks/NASDAQ/DKI/earnings) returned August 13, 2026 results. PR searches found no verified same-day company release; other results showed an August 14 AI/gaming update. The [SEC index](https://www.stocktitan.net/sec-filings/DKI) returned September 18 filings and the October 6 meeting notice. These are background; no fresh publication time was verified or used for grading.
- **FLNA:** The [company release index](https://www.filanatx.com/press-releases) and [investor page](https://www.filanatx.com) returned July 29, 2026 Q2 earnings and September 22, 2026 FDA clinical-hold clearance news. The [filing overview](https://www.stocktitan.net/overview/FLNA) returned September 22 as its latest filing. All predate this trading date; the FDA headline is not used to assign a fresh Grade B.

**Carry forward:** Thirty unique names are now in tonight's pipeline: the previous 28 plus BENF and FLNA. Carry seven untradable names: GBLRF, MHUAF, SFES, WTLLF, BMNM, FNFI, MCDIF. At 00:30 CEST, cross-check all tracked tradable names for final-scan feed lag. Before any later entry, check recent daily bars and `WINNERS_TRACKING.md` for MULTI-SESSION-RUNNER instrumentation. Chase-cap and final-scan gate-block instrumentation do not apply to this observation scan.

**Daily email:** No item from this scan requires Juan's input.

## Scan 22:30 CEST (4:30 PM ET)

`python3 scripts/scan.py --all` ran at 16:30:26 ET (22:30:26 CEST), in the AFTERHOURS session. Six candidates were discovered. HIT and DKI have three scanner appearances above +10% AH (22:20, 22:25, and 22:30); NCPL and LPA each have their first. FLNA and USBC remain below threshold. The scanner snapshot requires fresh broker confirmation before any entry. The 22:25 pulse committed during this workup; its results are included in the histories below.

  Supplementary AH-change-only (>15%, not in volume pass): none

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| HIT | [TV](https://www.tradingview.com/chart/?symbol=HIT) | $0.82 | -3.7% | +25.5% | $1.03 | +20.8% | 3.0M | 381K | 7.9x | 20.5M | Information Technology Services |
| DKI | [TV](https://www.tradingview.com/chart/?symbol=DKI) | $1.57 | -38.4% | +37.6% | $2.16 | -15.3% | 1.3M | 345K | 3.7x | 1.2M | Packaged Software |
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $1.24 | +1.6% | +15.3% | $1.43 | +17.2% | 381K | 40.8M | 0.0x | 4.4M | Miscellaneous Commercial Services |
| LPA | [TV](https://www.tradingview.com/chart/?symbol=LPA) | $2.86 | +1.4% | +12.9% | $3.23 | +14.5% | 204K | 50K | 4.0x | 5.2M | Real Estate Development |
| FLNA | [TV](https://www.tradingview.com/chart/?symbol=FLNA) | $0.89 | -4.2% | +6.1% | $0.94 | +1.7% | 67K | 10.8M | 0.0x | 47.3M | Biotechnology |
| USBC | [TV](https://www.tradingview.com/chart/?symbol=USBC) | $0.54 | +0.8% | +7.6% | $0.59 | +8.4% | 53K | 325K | 0.2x | 14.8M | Electronic Equipment/Instruments |

### Evaluation notes

**Decision:** Observation only; no paper orders submitted. Entries begin at the 23:00 CEST scan. HIT's opening-spike evidence and DKI's dead-cat gate also block entry on the current evidence. NCPL and LPA need a second qualifying AH scan and all remaining entry checks. No filled position was added to the paper-trade table or `OPEN_POSITIONS.md`.

**Tradability:** HIT, DKI, and NCPL retain their earlier verified `tradable=true` results. New candidates LPA and USBC each returned `tradable=true` before further workup; FLNA also returned true before the concurrent 22:25 result was read. Carry BENF's verified `tradable=true` result from 22:25. Float and industry are recorded for pattern tracking.

**SIP volume and freshness:** `broker.js bars --tf 5Min --start 2026-09-30T20:00:00Z` returned consolidated SIP for HIT, DKI, NCPL, and LPA. The latest available bar starts at 16:15 ET, consistent with the approximately 15-minute free-tier delay; the unserved later bars cannot establish the current high or liquidity. All four scanner prices fall within the available SIP traded ranges. No bad-print rejection is supported by these bars.

| Ticker | Bar start ET | High | Close | VWAP | Shares | Trades |
|--------|--------------|------|-------|------|--------|--------|
| HIT | 16:00 | $1.12 | $0.97 | $0.99 | 1,065,934 | 3,505 |
| HIT | 16:05 | $1.02 | $0.91 | $0.95 | 626,990 | 2,374 |
| HIT | 16:10 | $1.08 | $1.03 | $1.03 | 1,596,712 | 7,553 |
| HIT | 16:15 | $1.04 | $0.92 | $0.98 | 930,280 | 4,078 |
| DKI | 16:00 | $2.20 | $2.04 | $1.86 | 231,693 | 1,440 |
| DKI | 16:05 | $2.37 | $2.25 | $2.25 | 932,414 | 8,477 |
| DKI | 16:10 | $2.35 | $2.16 | $2.17 | 398,562 | 4,121 |
| DKI | 16:15 | $2.26 | $2.25 | $2.12 | 249,617 | 2,235 |
| NCPL | 16:00 | $1.36 | $1.33 | $1.28 | 147,135 | 212 |
| NCPL | 16:05 | $1.38 | $1.34 | $1.34 | 73,890 | 350 |
| NCPL | 16:10 | $1.47 | $1.43 | $1.42 | 191,674 | 770 |
| NCPL | 16:15 | $1.43 | $1.35 | $1.37 | 192,636 | 467 |
| LPA | 16:00 | $2.86 | $2.86 | $2.86 | 152 | 4 |
| LPA | 16:10 | $3.50 | $3.21 | $3.32 | 273,176 | 3,655 |
| LPA | 16:15 | $3.25 | $3.14 | $3.17 | 142,321 | 1,461 |

- **HIT — FIRST-BAR-SPIKE WATCH; skip live entry on the available opening-spike evidence. Hypothetical $1.03 at 16:30 ET / 22:30 CEST.** Scanner AH +18.2% → +13.3% → +25.5%, AH Vol 1.0M → 1.6M → 3.0M. SIP confirms 4,219,916 shares / 17,510 trades, including a second volume surge at 16:10, but no new high above the opening 16:00 bar's $1.12. CONFIRM-3 is NO in all three scans. The scanner price is 8.0% below that high; proximity alone does not remove the first-bar-spike rule. The 16:15 bar lost the second surge, closing $0.92 with lower VWAP and volume. Yahoo's timeline checked through 16:31 suggests continued fading after 16:10, so rising delayed scanner AH% does not establish a current BUILD. Verify the later SIP bars at the eligible scan before carrying the opening-high classification forward. Grade **None**; InsurTech / IT services.
- **DKI — Skip live entry: Day -38.4%, dead-cat gate. DEAD-CAT-OVERRIDE WATCH (carried): hypothetical $2.23 at 16:25 ET / 22:25 CEST.** The prior scan recorded the rising reclaim +27.4% → +42.1% above the $1.57 regular close. This scan eased to +37.6% / $2.16, so it does not establish a new rising reclaim; retain the original hypothetical for morning evaluation. SIP confirms 1,812,286 shares / 16,273 trades. Its available high remains $2.37 in the 16:05 opening bar, with volume falling 932K → 399K → 250K. The fresh 16:30:57 quote is bid $1.87 x100 / ask $1.91 x100, below the delayed scanner $2.16; Yahoo's timeline also suggests fading after the opening move. The hypothetical captures the scanner reclaim, not a verified current BUILD. CONFIRM-3 changed from PENDING to NO; do not use that transition to grade or rank it. Grade **None**, with unverified same-day commentary noted below; mobile gaming / packaged software.
- **NCPL — Watch; first >10% AH scan, thin volume and stale zero-ask book.** Scanner AH +7.3% → +8.9% → +15.3%, AH Vol 144K → 204K → 381K. SIP confirms 605,335 shares / 1,799 trades, but only 212–770 trades per five-minute bar; this does not establish the thousands-of-trades sustained accumulation required for a BUILD entry. The available high is $1.47 at 16:10; the next bar closed $1.35 with VWAP falling $1.42 → $1.37. Yahoo's timeline suggests the move subsequently eased. VRatio 0.0x is rounded discovery data. Recheck accumulation and a current two-sided book before sizing. Grade **None**; fintech / capital-raising services.
- **LPA — Watch; first >10% AH scan, real ignition but incomplete follow-through and stale zero-ask book.** SIP confirms 415,649 shares / 5,120 trades, with a 273,176-share / 3,655-trade surge at 16:10 followed by 142,321 shares / 1,461 trades at 16:15. Its available high is $3.50 at 16:10, and the scanner $3.23 is 7.7% below it. Yahoo's later timeline suggests a rebound after 16:25; exact levels and any new high require SIP confirmation. CONFIRM-3 remains PENDING and has no independent decision impact. Grade **None**; Latin American logistics real estate. A second qualifying scan and fresh book are required.
- **FLNA — Watch; AH +6.1%, below >10% entry threshold.** The 22:25 scanner displayed +10.0% at the rounding boundary; this scan eased to +6.1%, price $0.97 → $0.94, while discovery volume rose 52K → 67K. It still has no verified >10% scheduled-scan appearance. Float 47.3M; Filana Therapeutics, formerly Cassava Sciences, epilepsy biotechnology. Carry Grade **None** and the 22:25 thin-volume/catalyst findings; no new >10% workup is triggered.
- **USBC — Watch; AH +7.6%, below >10% entry threshold.** First discovery; float 14.8M, electronic equipment/instruments. No >10% catalyst or spike-bar workup is triggered.

**Book checks and stale data:** HIT returned bid $1.00 x100 / ask $1.04 x100 at 16:10:50 ET; NCPL returned bid $1.23 x100 / ask $0.00 x0 at 16:00:41; LPA returned bid $2.46 x100 / ask $0.00 x0 at 16:00:01. One re-pull of each returned the same timestamps. These snapshots do not verify current fillable liquidity, and NCPL/LPA cannot be sized from zero asks. Their consolidated SIP trades establish real AH activity; the stale quotes do not support calling the volume a stale regular-session artifact. DKI's two-sided quote is fresh, but its other entry gates still fail. Yahoo was used only for timeline shape, with zero extended-hours volume ignored and no precise entry/high levels taken from it.

**Spike-bar and third-bar instrumentation (verbatim; log only):**

```text
HIT 2026-09-30  SPIKE  16:00ET  +37%  $1.12  221 trades / 67k sh  (first co-spike bar) (as-of 16:30ET)
DKI 2026-09-30  SPIKE  16:01ET  +20%  $1.89  256 trades / 43k sh  (first co-spike bar) (as-of 16:30ET)
NCPL 2026-09-30  SPIKE  16:13ET  +18%  $1.46  213 trades / 79k sh  (first co-spike bar) (as-of 16:30ET)
LPA 2026-09-30  SPIKE  16:12ET  +22%  $3.50  1174 trades / 89k sh  (first co-spike bar) (as-of 16:30ET)
HIT 2026-09-30  CONFIRM-3  NO no local-volume new-high ignition as-of 16:30ET
DKI 2026-09-30  CONFIRM-3  NO ignition 16:05ET failed third-bar hold/volume as-of 16:30ET
NCPL 2026-09-30  CONFIRM-3  NO no local-volume new-high ignition as-of 16:30ET
LPA 2026-09-30  CONFIRM-3  PENDING ignition 16:10ET; waiting for third bar as-of 16:30ET
```

CONFIRM-3 is recorded for observation; only the explicitly specified first-bar-spike rule combines a persistent opening high with repeated NO readings. PENDING on LPA reflects delayed SIP coverage.

**Structured catalyst searches:** Four `websearch search` calls per >10% ticker: earnings on September 30, one identical Tavily retry after the default provider returned a rate-limit error, same-day wire releases, and SEC material filings (8-K, plus 6-K for foreign issuers DKI/LPA). HIT and DKI were searched again for newly indexed news. Budgets are exhausted for this pulse. **HIT, DKI, NCPL, LPA: no verified fresh catalyst found; grades None.** No catalyst remains a documented concern, not a learning-phase skip. No unverified headline is used to assign an operational-news grade.

- **HIT:** The [company release index](https://healthintech.investorroom.com/Press-Releases) points to August 13 Q2 results; the [filing index](https://www.stocktitan.net/sec-filings/HIT) returned September 15 tax-withholding transactions. No fresh earnings, release, or material filing was found. Older news remains background.
- **DKI:** Earnings search returned August 13 results and a [GuruFocus article](https://www.gurufocus.com/news/9103534/darkiris-dki-advances-ai-video-platform-and-expands-in-north-america-amid-challenging-valuation) alleging a same-day Cine3.AI / North America update. Its page metadata verifies publication **September 30, 2026 at 09:57:07 ET (13:57:07Z)**. This verifies the article's timestamp, not the underlying company announcement. The wire search returned the [August 14 operational update](https://www.globenewswire.com/news-release/2026/08/14/3345600/0/en/darkiris-inc-updates-strategic-and-operational-progress-on-ai-initiatives-and-gaming-business.html), published **August 14 at 16:05 ET**, and the [filing index](https://www.stocktitan.net/sec-filings/DKI) returned September 18. Direct retrieval of the older wire page timed out. No fresh primary announcement was verified; retain **None** with the same-day commentary as an unconfirmed lead.
- **NCPL:** Earnings search returned older results and an estimated October 2 reporting date, not a September 30 earnings release. The wire search found the [September 25 Nasdaq delayed-filing notice](https://www.globenewswire.com/news-release/2026/09/25/3369339/0/en/netcapital-inc-receives-nasdaq-notice-related-to-delayed-quarterly-report-on-form-10-q.html); [SEC searches](https://www.stocktitan.net/sec-filings/NCPL/8-k.html) found the same notice and older financing. These are background; no fresh catalyst was verified.
- **LPA:** Earnings search returned Q2 results released August 12. News searches returned the [September 21 Costa Rica asset sale](https://lpamericas.com/logistic-properties-of-the-americas-advances-capital-reallocation-strategy-with-costa-rica-asset-sale), distributed at **16:30 ET on September 21** per the news index, and September 11 Peru-sale approval. SEC search returned September 21 as the latest indexed filing. These older asset-sale items do not establish a fresh September 30 catalyst and are not used for grading.

**Carry forward:** Add LPA and USBC to the 30-name pipeline established at 22:25 (32 unique names total). BENF dropped out of this snapshot; retain its 22:25 below-threshold, sparse-trading watch and tradability result for the final cross-check. MCDIF remains **untradable (carried)** with GBLRF, MHUAF, SFES, WTLLF, BMNM, and FNFI; no repeated workup was performed on those seven broker blocks. At the 00:30 CEST final scan, cross-check tracked tradable names against SIP for feed-lag omissions. Before any later entry, verify recent daily activity for MULTI-SESSION-RUNNER instrumentation and the current sustained AH trajectory. No fill occurred, so CHASE-CAP instrumentation does not apply; this is not the final scan, so FINAL-SCAN-GATE-BLOCK instrumentation does not apply.

**Daily email:** No item from this scan requires Juan's input. Include the stale-book limitations and DKI's unverified commentary lead in the daily scan summary.

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
