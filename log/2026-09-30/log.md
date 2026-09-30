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

## Scan 22:45 CEST (4:45 PM ET)

`python3 scripts/scan.py --all` ran at 16:45:32 ET (22:45:32 CEST), in the AFTERHOURS session. Seven candidates were discovered. DKI has its fourth scanner appearance above +10% AH; LPA has its second (22:30 and 22:45). SES, WETO, and IMCC are new tonight. HIT dropped out; NCPL and FLNA are below threshold.

  Supplementary AH-change-only (>15%, not in volume pass): none

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| DKI | [TV](https://www.tradingview.com/chart/?symbol=DKI) | $1.57 | -38.4% | +24.8% | $1.96 | -23.1% | 2.0M | 431K | 4.6x | 1.2M | Packaged Software |
| SES | [TV](https://www.tradingview.com/chart/?symbol=SES) | $0.60 | +12.3% | +6.7% | $0.64 | +19.8% | 739K | 19.2M | 0.0x | 250.0M | Electrical Products |
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $1.24 | +1.6% | +6.8% | $1.32 | +8.5% | 621K | 40.9M | 0.0x | 4.4M | Miscellaneous Commercial Services |
| LPA | [TV](https://www.tradingview.com/chart/?symbol=LPA) | $2.86 | +1.4% | +12.6% | $3.22 | +14.2% | 445K | 80K | 5.6x | 5.2M | Real Estate Development |
| WETO | [TV](https://www.tradingview.com/chart/?symbol=WETO) | $1.01 | -8.2% | +5.9% | $1.07 | -2.7% | 210K | 9.3M | 0.0x | 915K | Other Transportation |
| IMCC | [TV](https://www.tradingview.com/chart/?symbol=IMCC) | $2.25 | -8.2% | +6.5% | $2.40 | -2.2% | 162K | 16.9M | 0.0x | 1.5M | Agricultural Commodities/Milling |
| FLNA | [TV](https://www.tradingview.com/chart/?symbol=FLNA) | $0.89 | -4.2% | +9.5% | $0.97 | +4.9% | 87K | 10.8M | 0.0x | 47.3M | Biotechnology |

### Evaluation notes

**Decision:** Observation only; no paper orders submitted. This is the 22:45 scan, before the 23:00 CEST entry window. LPA clears the two-AH-scan count but still needs a current fillable book and a trajectory recheck at the eligible scan. DKI remains blocked by the dead-cat gate. The other five scanner names are below the strict >10% AH threshold. No filled position was added to the paper-trade table or `OPEN_POSITIONS.md`.

**Tradability:** New names SES, WETO, and IMCC each returned `tradable=true` before their SIP workup. Carry the earlier true results for DKI, LPA, NCPL, FLNA, and HIT. Float and industry remain pattern-tracking data, not learning-phase skip reasons.

**SIP volume and freshness:** All seven bar requests used `--tf 5Min --start 2026-09-30T20:00:00Z` and returned `feed=sip`. The latest available bar starts at 16:30 ET, 15 minutes before this scan, consistent with the historical-feed delay. Later bars and the current AH high remain unverified. DKI and LPA scanner prices are corroborated by the available traded ranges; no bad-print rejection is supported. Scanner AH Vol and VRatio are discovery data, not fillable-liquidity evidence.

| Ticker | Available SIP shares | Trades | Latest bar start ET | Latest high | Latest close | Latest VWAP | Latest shares | Latest trades |
|--------|----------------------|--------|---------------------|-------------|--------------|-------------|---------------|---------------|
| DKI | 2,764,814 | 23,883 | 16:30 | $1.97 | $1.68 | $1.82 | 342,185 | 2,511 |
| LPA | 1,074,446 | 12,997 | 16:30 | $3.49 | $3.34 | $3.40 | 505,055 | 6,315 |
| HIT | 5,175,334 | 20,845 | 16:30 | $0.89 | $0.87 | $0.86 | 138,855 | 478 |
| NCPL | 674,690 | 2,104 | 16:30 | $1.36 | $1.32 | $1.33 | 8,689 | 48 |
| SES | 1,305,813 | 322 | 16:30 | $0.64 | $0.64 | $0.64 | 1,741 | 7 |
| WETO | 242,407 | 792 | 16:30 | $1.09 | $1.06 | $1.07 | 24,898 | 125 |
| IMCC | 198,192 | 1,608 | 16:30 | $2.35 | $2.29 | $2.32 | 4,513 | 41 |

- **LPA — Watch; two qualifying scans, renewed real volume, current book unconfirmed.** Scanner AH +12.9% → +12.6%, price $3.23 → $3.22, AH Vol 204K → 445K, VRatio 4.0x → 5.6x. SIP shows a renewed 16:30 surge of 505,055 shares / 6,315 trades, versus 40,829 / 601 at 16:20 and 112,913 / 961 at 16:25. VWAP rose $3.15 → $3.21 → $3.40. This is real accumulation after the opening dip. The available AH high remains $3.50 at 16:10 ET; the later $3.49 high nearly retested it, and the scanner price is 8.0% below it. **FIRST-BAR-SPIKE WATCH (provisional): hypothetical $3.22 at 16:45 ET / 22:45 CEST.** CONFIRM-3 changed from PENDING to its first NO verdict; the earlier scans were PENDING, so a persistent NO history has not yet been established. Recheck whether later volume-backed highs replace the opening high before applying the first-bar-spike skip. The CONFIRM-3 verdict does not independently grade or rank the candidate. Grade **None (provisional; fresh 6-K contents unverified)**; Latin American logistics real estate. Recheck current two-sided liquidity before sizing at 23:00 or later.
- **DKI — Skip live entry: Day -38.4%, dead-cat gate; opening move is fading.** Scanner AH +42.1% → +37.6% → +24.8% across the last three scans; price $2.23 → $2.16 → $1.96 despite AH Vol rising 960K → 1.3M → 2.0M. SIP confirms real trading but VWAP fell $2.23 → $2.06 → $1.82 in the last three available bars, and the 16:30 close $1.68 is 29.1% below the $2.37 opening high at 16:05. The scanner price is only 17.3% below that high, illustrating the delayed view. **DEAD-CAT-OVERRIDE WATCH (carried): hypothetical $2.23 at 16:25 ET / 22:25 CEST.** Retain the original rising-reclaim hypothetical; this declining scan creates no new override. Grade **None**; mobile gaming / packaged software.
- **NCPL — Watch below threshold; fade with sharply falling volume.** Scanner AH +15.3% → +6.8%, price $1.43 → $1.32, while cumulative discovery volume rose 381K → 621K. Available SIP volume fell 192,636 → 41,647 → 19,019 → 8,689 shares; trades fell 467 → 164 → 93 → 48. VWAP fell $1.37 → $1.35 → $1.33 → $1.33. Cumulative volume growth does not establish a BUILD here. It retains only one qualifying scanner appearance, at 22:30. Grade **None** carried; fintech / capital-raising services.
- **FLNA — Watch below threshold.** Scanner AH +6.1% → +9.5%, price $0.94 → $0.97, AH Vol 67K → 87K. No verified >10% scheduled-scan appearance exists; the earlier +10.0% display was at the rounding boundary. Carry the previous thin-volume findings and Grade **None**. Biotechnology; float 47.3M.
- **SES — Watch below threshold; sparse trades after the opening volume.** First discovery, AH +6.7%. Of 1,305,813 available SIP shares, 1,082,473 were in the opening bar with only 71 trades. The latest bar has 1,741 shares / seven trades; sustained liquid accumulation is not established. Float 250.0M is recorded, not used to skip it. Electrical products / battery technology. No >10% catalyst workup is triggered.
- **WETO — Watch below threshold; thin activity.** First discovery, AH +5.9%; available SIP bars have 7,906–100,449 shares and 54–170 trades each. The latest bar has 24,898 shares / 125 trades, not thousands of trades with hundreds of K shares. Other transportation; float 915K. No >10% catalyst workup is triggered.
- **IMCC — Watch below threshold; brief spike followed by fading volume.** First discovery, AH +6.5%. The 16:15 SIP bar reached $2.80 on 155,652 shares / 1,275 trades, but subsequent volume fell to 24,012 → 9,646 → 4,513 shares and VWAP to $2.39 → $2.34 → $2.32. The available close is $2.29. Agricultural commodities/milling label; cannabis company, float 1.5M. No >10% catalyst workup is triggered by the current scanner reading.

**Dropped prior candidate — HIT:** Its absence from discovery is supported by a faded SIP trajectory: available closes $0.92 → $0.91 → $0.86 → $0.87, with the last two VWAPs $0.87 → $0.86 and only 478 trades in the latest bar. The latest available close is 22.3% below the unchanged $1.12 opening high, so stabilization here does not qualify as holding near the high. Carry the **FIRST-BAR-SPIKE WATCH** hypothetical $1.03 at 16:30 ET / 22:30 CEST and Grade **None**. Retain HIT in the pipeline for the final feed-lag cross-check; dropping from the scanner does not itself establish the current price.

**Book freshness:** LPA returned bid $2.46 x100 / ask $0.00 x0 at 16:00:01 ET; NCPL bid $1.23 x100 / ask $0.00 x0 at 16:00:41; HIT bid $1.00 x100 / ask $1.04 x100 at 16:10:50; DKI bid $1.89 x100 / ask $1.94 x100 at 16:32:05. One re-pull of each returned identical timestamps. These are stale snapshots, especially LPA, NCPL, and HIT; none verifies the instantaneous book at 16:45. LPA/NCPL cannot be sized from zero asks. Their SIP trades confirm real AH activity, so these stale snapshots do not support a hard bad-print or fictitious-volume conclusion. Recheck a current two-sided book at any eligible entry scan. No book was requested for the new below-threshold names.

**Spike-bar and third-bar instrumentation (verbatim; log only):**

```text
DKI 2026-09-30  SPIKE  16:01ET  +20%  $1.89  256 trades / 43k sh  (first co-spike bar) (as-of 16:45ET)
DKI 2026-09-30  CONFIRM-3  NO ignition 16:05ET failed third-bar hold/volume as-of 16:45ET
LPA 2026-09-30  SPIKE  16:12ET  +22%  $3.50  1174 trades / 89k sh  (first co-spike bar) (as-of 16:45ET)
LPA 2026-09-30  CONFIRM-3  NO ignition 16:10ET failed third-bar hold/volume as-of 16:45ET
```

**Structured catalyst searches:** DKI received three Tavily `websearch search` calls covering September 30 earnings, same-day wire releases, and SEC material filings (8-K / 6-K). LPA received the same three checks plus one targeted search for the newly surfaced September 30 6-K, reaching its four-call budget. No verified fresh operational catalyst was found. No catalyst is a documented concern, not a learning-phase entry skip.

- **DKI — Grade None:** [Earnings history](https://www.marketbeat.com/stocks/NASDAQ/DKI/earnings) points to August 13 results. The [wire release](https://www.globenewswire.com/news-release/2026/08/14/3345600/0/en/darkiris-inc-updates-strategic-and-operational-progress-on-ai-initiatives-and-gaming-business.html) is dated **August 14, 2026 at 16:05 ET**; the [TMX release index](https://money.tmx.com/en/quote/DKI:US/news) also dates the earnings release **August 13 at 08:00 ET**. The [filing index](https://www.stocktitan.net/sec-filings/DKI) returned September 18 as its latest filing. All are background. The prior scan's September 30 commentary lead remains unverified as a fresh underlying company announcement; no headline-only grade is assigned.
- **LPA — Grade None, provisional:** [Earnings searches](https://ir.lpamericas.com/news-events/news/news-details/2026/Logistic-Properties-of-the-Americas-Announces-Second-Quarter-2026-Earnings-Results/default.aspx) returned the August 12 Q2 release. The [news index](https://marketchameleon.com/Overview/LPA/Summary) dates the Costa Rica sale release **September 21 at 16:30 ET** and Peru regulatory approval **September 11 at 09:25 ET**; these are background. The [MarketBeat filing search](https://www.marketbeat.com/stocks/NYSEAMERICAN/LPA/sec-filings) surfaced a same-day 6-K, contrary to the older September 21 index snapshot. Direct [SEC submissions](https://data.sec.gov/submissions/CIK0001997711.json) confirmed **filing date September 30, 2026**, accession **0001997711-26-000172**, acceptance timestamp **2026-09-30T16:14:00.000Z (12:14 ET)**, primary document `latampropertiesoftheameric.htm`. Retrieval of the [primary 6-K](https://www.sec.gov/Archives/edgar/data/1997711/000199771126000172/latampropertiesoftheameric.htm) and the [official IR filing page](https://ir.lpamericas.com/financials/sec-filings/default.aspx) each returned HTTP 403. The filing is fresh, but its contents and any attached release time are unverified. Recheck its contents at the next eligible scan before assigning an operational or dilution grade; freshness alone does not establish a catalyst type.

**Carry forward:** Add SES, WETO, and IMCC to the 32-name pipeline (35 unique names total). Carry seven **untradable (carried)** broker blocks: GBLRF, MHUAF, SFES, WTLLF, BMNM, FNFI, MCDIF; no repeated verification or catalyst search was performed on them. BENF and USBC are absent but remain tracked. At 00:30 CEST, cross-check the 28 tracked tradable names against SIP for feed-lag omissions. Before any later entry, check recent daily bars and `WINNERS_TRACKING.md` for MULTI-SESSION-RUNNER instrumentation. No fill occurred, so CHASE-CAP does not apply; this is not the final scan, so FINAL-SCAN-GATE-BLOCK does not apply.

**Daily email:** Include LPA's renewed SIP surge, stale zero-ask quote, and confirmed September 30 6-K with contents unverified due to HTTP 403. No item from this scan requires Juan's input.

## Scan 23:00 CEST (5:00 PM ET)

`python3 scripts/scan.py --all` ran at 17:00:27 ET (23:00:27 CEST), in the AFTERHOURS session, and returned nine candidates. LPA has three scanner appearances above +10% AH (22:30, 22:45, 23:00). PARA and WETO each have their first. PARA and SDEV are new tonight; CNTB was already tracked at the regular-session checkpoint.

  Supplementary AH-change-only (>15%, not in volume pass): none

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| HIT | [TV](https://www.tradingview.com/chart/?symbol=HIT) | $0.82 | -3.7% | +5.3% | $0.86 | +1.3% | 5.0M | 598K | 8.4x | 20.5M | Information Technology Services |
| PARA | [TV](https://www.tradingview.com/chart/?symbol=PARA) | $0.65 | -5.4% | +16.3% | $0.75 | +10.0% | 1.5M | 1.4M | 1.0x | 3.4M | Packaged Software |
| LPA | [TV](https://www.tradingview.com/chart/?symbol=LPA) | $2.86 | +1.4% | +10.8% | $3.17 | +12.4% | 1.1M | 170K | 6.6x | 5.2M | Real Estate Development |
| CNTB | [TV](https://www.tradingview.com/chart/?symbol=CNTB) | $1.10 | +10.9% | +5.5% | $1.16 | +16.9% | 1.0M | 17.7M | 0.1x | 17.0M | Pharmaceuticals: Major |
| SES | [TV](https://www.tradingview.com/chart/?symbol=SES) | $0.60 | +12.3% | +6.7% | $0.64 | +19.8% | 752K | 19.2M | 0.0x | 250.0M | Electrical Products |
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $1.24 | +1.6% | +8.1% | $1.34 | +9.8% | 655K | 40.9M | 0.0x | 4.4M | Miscellaneous Commercial Services |
| WETO | [TV](https://www.tradingview.com/chart/?symbol=WETO) | $1.01 | -8.2% | +14.8% | $1.16 | +5.4% | 491K | 9.3M | 0.1x | 915K | Other Transportation |
| SDEV | [TV](https://www.tradingview.com/chart/?symbol=SDEV) | $2.59 | -20.8% | +6.6% | $2.76 | -15.6% | 352K | 26.3M | 0.0x | 1.8M | Pharmaceuticals: Major |
| FLNA | [TV](https://www.tradingview.com/chart/?symbol=FLNA) | $0.89 | -4.2% | +8.2% | $0.96 | +3.7% | 89K | 10.8M | 0.0x | 47.3M | Biotechnology |

### Evaluation notes

**Decision: no paper entries.** The entry window is open, but no candidate clears every gate on the available evidence. LPA clears the scan-count gate but has no verified current fillable ask; PARA and WETO have only one qualifying AH scan. PARA's available bars also show a spike followed by a retreat. The remaining scanner names are below +10% AH. Alpaca reports no open positions, and the order history shows no new entry fills or open orders. No order was submitted; the paper-trade table and `OPEN_POSITIONS.md` contain no new positions.

**Tradability:** New names PARA and SDEV returned `tradable=true` before further workup. Carry the earlier verified true results for the other seven scanner names. Alpaca identifies PARA as **Banzai International, Inc. Class A Common Stock**, operating as Parabolic; catalyst searches used this issuer identity. WETO is **Wetour Robotics**, formerly Webus, despite its transportation screener label. Float and sector are pattern-tracking data; neither is a skip reason here.

**SIP volume and freshness:** Bar requests used `--tf 5Min --start 2026-09-30T20:00:00Z` and returned `feed=sip`. The newest available bar starts at 16:45 ET and covers trades through 16:50, consistent with the historical-feed delay at this scan. It cannot establish the current price or a later new high. The three >10% scanner prices are within available SIP traded ranges; none warrants a bad-print rejection. TradingView AH Vol/VRatio remain discovery signals.

| Ticker | Available SIP shares | Trades | Latest bar start ET | Latest high | Latest close | Latest VWAP | Latest shares | Latest trades |
|--------|----------------------|--------|---------------------|-------------|--------------|-------------|---------------|---------------|
| LPA | 1,520,978 | 18,058 | 16:45 | $3.24 | $3.24 | $3.17 | 44,116 | 514 |
| PARA | 2,132,638 | 7,382 | 16:45 | $0.76 | $0.70 | $0.72 | 577,039 | 1,802 |
| WETO | 926,408 | 3,325 | 16:45 | $1.24 | $1.20 | $1.19 | 411,454 | 1,556 |
| HIT | 5,525,354 | 21,610 | 16:45 | $0.86 | $0.83 | $0.84 | 64,115 | 198 |
| NCPL | 713,897 | 2,209 | 16:45 | $1.34 | $1.33 | $1.33 | 9,971 | 29 |
| DKI | 3,139,676 | 26,646 | 16:45 | $1.63 | $1.47 | $1.51 | 124,480 | 825 |

- **LPA — Skip entry this scan: current fillable liquidity unconfirmed; opening high persists in available SIP.** Scanner AH +12.9% → +12.6% → +10.8%, price $3.23 → $3.22 → $3.17, while discovery volume rose 204K → 445K → 1.1M. The genuine 16:30 surge of 505,055 shares / 6,315 trades was followed by 327,858 / 3,557, 74,558 / 990, then 44,116 / 514. VWAP fell $3.40 → $3.18 → $3.17 → $3.17. Cumulative volume growth alone does not establish continuing accumulation. The available AH high remains $3.50 at 16:10 ET; scanner price is 9.4% below it. **FIRST-BAR-SPIKE WATCH (carried, provisional): hypothetical $3.17 at 17:00 ET / 23:00 CEST.** Both completed confirmation verdicts (16:45 and 17:00) are NO; earlier readings were PENDING. Retain the opening-high watch and recheck later SIP coverage before treating that history as a confirmed persistent single-bar pop. Yahoo's later timeline suggests a rebound, which requires SIP confirmation of any new high and sustained volume. The stale zero-ask quote independently prevents sizing now. Grade **None, provisional** because the same-day 6-K's contents remain unverified.
- **PARA — Skip entry: only one qualifying AH scan, retreat from spike, and stale zero-ask book.** Real ignition began at 16:35: 298,312 shares / 1,109 trades, high $0.80, close $0.78, VWAP $0.76. At 16:40, 1,251,360 shares / 4,467 trades reached $0.82 but closed $0.75; the next bar closed $0.70 with VWAP $0.72 and reduced volume. The latest available close is 14.6% below the 16:40 high and declining. Yahoo's subsequent timeline also shows continued retreat; its precise levels are not used for the decision. This is real traded volume, with incomplete current coverage, rather than evidence of a bad print. Grade **None**; AI/marketing software, float 3.4M. A second appearance alone would still require a renewed sustained trajectory and a current two-sided book.
- **WETO — Watch: first qualifying AH scan; real late ignition needs a second scan and current book.** Scanner AH +5.9% → +14.8%, price $1.07 → $1.16, AH Vol 210K → 491K since 22:45. SIP improved from 30,015 shares / 100 trades at 16:35 to 242,532 / 877 at 16:40, then 411,454 / 1,556 at 16:45; VWAP rose $1.07 → $1.14 → $1.19, with successive highs $1.09 → $1.17 → $1.24. This is a volume-backed late surge, despite low discovery VRatio. The scanner price is 6.5% below the available $1.24 high. Yahoo's later timeline suggests a pullback after that surge; verify the next SIP bars before classifying current BUILD/HOLD. Grade **None**; physical AI/wearable robotics, float 915K. CONFIRM-3 PENDING has no entry or ranking impact.
- **HIT — Skip: current AH +5.3%, below threshold, with a faded opening spike.** It reappeared after dropping out at 22:45, but discovery volume 5.0M / VRatio 8.4x does not restore its price trajectory. Available close $0.83 is 25.9% below the $1.12 opening high; latest volume is only 64K shares / 198 trades. Carry Grade **None** and the existing FIRST-BAR-SPIKE WATCH hypothetical $1.03 at 16:30 ET. InsurTech / IT services.
- **NCPL — Watch below threshold; thin fading activity.** Scanner AH +6.8% → +8.1%, price $1.32 → $1.34, discovery volume 621K → 655K. Latest available bars have only 13,894 / 37 trades, 15,342 / 39, and 9,971 / 29; no sustained liquid BUILD is established. It retains one qualifying scanner appearance, at 22:30. Grade **None** carried; capital-raising services.
- **CNTB — Watch below threshold; regular-session appearance contributes no AH confirmation.** AH +5.5%. Its 16:35 SIP bar reached $1.21 on 197,374 shares / 617 trades; subsequent bars slowed to 78,795 / 306 and 67,432 / 141, closing $1.17. The available high alone does not add a current qualifying scan. Pharmaceuticals; float 17.0M.
- **SES — Watch below threshold.** AH remains +6.7%; discovery volume 739K → 752K. Carry the 22:45 sparse-trade observation; no new >10% workup is triggered. Battery technology / electrical products; float 250.0M is recorded without applying a float skip.
- **SDEV — Skip entry: AH +6.6% below threshold and Day -20.8% fails the dead-cat gate.** New discovery, `tradable=true`. Available SIP bars contain 18K–74K shares / 99–346 trades each; latest close $2.70 / VWAP $2.73 on 26,618 shares / 140 trades. This is thin activity. Only one below-threshold AH appearance exists, so no rising-reclaim DEAD-CAT-OVERRIDE WATCH is established. Pharmaceuticals; float 1.8M. The quote is stale at 15:59:59 ET (bid $2.52 x100 / ask $3.98 x500), not evidence of a current entry book.
- **FLNA — Watch below threshold; volume has nearly stopped.** Scanner AH +9.5% → +8.2%, price $0.97 → $0.96, discovery volume 87K → 89K. The latest SIP bars contain 1,258 shares / 13 trades, 210 / 4, then 977 / 10. No verified >10% scheduled-scan appearance exists. Grade **None** carried; epilepsy biotechnology, float 47.3M.

**Dropped prior candidate — DKI:** Retain the dead-cat skip (Day -38.4%) and **DEAD-CAT-OVERRIDE WATCH** hypothetical $2.23 at 16:25 ET. Available SIP now closed $1.47, below the $1.57 regular close and 38.0% below the $2.37 opening high; the last three VWAPs fell $1.67 → $1.63 → $1.51. This supports continued fading rather than a new reclaim. Grade **None** carried. Other absent tracked names remain in the final-scan pipeline.

**Book freshness and entry limitation:** LPA returned bid $2.46 x100 / ask $0.00 x0 at 16:00:01 ET; PARA bid $0.55 x100 / ask $0.00 x0 at 16:00:02; WETO bid $0.88 x100 / ask $1.17 x100 at 16:00:00. One re-pull returned identical timestamps. These snapshots are about an hour behind the scan, including WETO's nominally two-sided book. LPA/PARA have no current verified fillable ask, and WETO's stale book cannot size a later entry. SIP establishes real AH trades; stale quotes do not prove fictitious volume or justify a bad-print label. Recheck current liquidity at subsequent eligible scans. Yahoo was used only for timeline shape; its extended-hours volume and precise prices were not used to establish liquidity or entry/high levels.

**Spike-bar and third-bar instrumentation (verbatim; log only):**

```text
LPA 2026-09-30  SPIKE  16:12ET  +22%  $3.50  1174 trades / 89k sh  (first co-spike bar) (as-of 17:00ET)
LPA 2026-09-30  CONFIRM-3  NO ignition 16:10ET failed third-bar hold/volume as-of 17:00ET
PARA 2026-09-30  SPIKE  16:38ET  +20%  $0.78  197 trades / 73k sh  (first co-spike bar) (as-of 17:00ET)
PARA 2026-09-30  CONFIRM-3  NO ignition 16:35ET failed third-bar hold/volume as-of 17:00ET
WETO 2026-09-30  SPIKE  16:42ET  +16%  $1.17  249 trades / 56k sh  (first co-spike bar) (as-of 17:00ET)
WETO 2026-09-30  CONFIRM-3  PENDING ignition 16:40ET; waiting for third bar as-of 17:00ET
```

**Structured catalyst searches:** Three Tavily `websearch search` calls per >10% ticker covered September 30 earnings, same-day wire releases, and SEC material filings (8-K; also 6-K for LPA/WETO). LPA received a fourth accession-specific search; PARA received a fourth date-specific 8-K search after the first filing search returned unrelated issuers. Search budgets were respected. **No verified fresh catalyst found** for any of the three. No-catalyst status is a documented concern, not an entry skip. No older or undated headline is used to assign an operational-news grade.

- **LPA — Grade None, provisional:** Earnings searches returned the [August 12 Q2 release](https://ir.lpamericas.com/news-events/news/news-details/2026/Logistic-Properties-of-the-Americas-Announces-Second-Quarter-2026-Earnings-Results/default.aspx); wire searches found older items. The [September 21 Costa Rica asset-sale release](https://lpamericas.com/logistic-properties-of-the-americas-advances-capital-reallocation-strategy-with-costa-rica-asset-sale), distributed at 16:30 ET, remains background. The [filing index](https://www.marketbeat.com/stocks/NYSEAMERICAN/LPA/sec-filings) again shows a September 30 6-K. Carry the prior primary-source verification: accession **0001997711-26-000172**, accepted **September 30 at 12:14 ET (16:14Z)**. Its contents remain unverified after the fourth targeted search. The newly retrieved [IR-hosted September PDF](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001997711/b5e6881e-b15f-4289-b0bb-253dae66db5e.pdf) was inspected in full and is actually signed **September 14**, concerning the September 22–23 conference; it is not the September 30 filing or a fresh catalyst. No grade is inferred from filing freshness alone. Recent daily closes (Yahoo daily bars) show September 28 $2.87 → September 29 $2.82 → September 30 $2.86, without a recent prior-session large run; `WINNERS_TRACKING.md` has no LPA match. This does not affect the failed liquidity gate.
- **PARA — Grade None:** [Official IR](https://ir.banzai.io/investor-relations) dates the Q2 results August 14 and the Parabolic/agentic-platform announcement August 6. The [wire offering release](https://www.globenewswire.com/news-release/2026/07/14/3326988/0/en/banzai-international-inc-announces-closing-of-0-9-million-underwritten-public-offering.html) is July 14. A [release index](https://seekingalpha.com/symbol/BNZI/press-releases) surfaced an annualized-cost-savings headline without a verified publication date/time; it is not used for grading. Both filing searches failed to identify a verified September 30 material event. Older releases and undated headlines remain background; no fresh publication time was verified.
- **WETO — Grade None:** Earnings search found a [Q2 financial summary](https://www.quiverquant.com/news/Webus+International+LTD+(WETO)+stock+falls+on+Q2+2026+Earnings) without a verified release date/time, so it is not graded as fresh earnings. Wire search returned the [July 23 Qualcomm-network release](https://www.globenewswire.com/news-release/2026/07/23/3331989/0/en/wetour-robotics-nasdaq-weto-joins-qualcomm-partner-network-advancing-orchestra-physical-ai-toward-commercial-scale.html) and [July 29 share-consolidation announcement](https://www.globenewswire.com/news-release/2026/07/29/3335680/0/en/wetour-robotics-announces-share-consolidation.html), plus a September 1 demonstration headline in related-news snippets. The [filing index](https://www.stocktitan.net/sec-filings/WETO) lists September 18 as its latest filing and older financing. These are background; no fresh publication time was verified or used for grading.

**Carry forward:** Add PARA and SDEV to the prior 35-name pipeline: **37 unique names**, comprising 30 tradable names and seven **untradable (carried)** broker blocks (GBLRF, MHUAF, SFES, WTLLF, BMNM, FNFI, MCDIF). No repeated SIP verification or catalyst search was performed on those broker blocks. At 00:30 CEST, cross-check tracked tradable names against SIP for final-scan feed lag, including the regular-session watches and names absent from discovery. WETO needs a second qualifying AH scan and sustained real volume/current liquidity; PARA needs those checks plus a trajectory recovery; LPA needs fresh later-bar and book verification. No fill occurred, so CHASE-CAP does not apply. This is not the final scan, so FINAL-SCAN-GATE-BLOCK does not apply. Before any later entry, check that candidate's recent daily bars and winner history for MULTI-SESSION-RUNNER instrumentation.

**Daily email:** Include the no-entry decision, LPA's stale zero-ask book and unresolved September 30 6-K, WETO's late volume surge pending a second scan, and PARA's real spike followed by fading. No item from this scan requires Juan's input.

## Scan 23:30 CEST (5:30 PM ET)

`python3 scripts/scan.py --all` ran at 17:30:38 ET (23:30:38 CEST), in the AFTERHOURS session, and returned eight candidates. LPA has four scanner appearances above +10% AH (22:30, 22:45, 23:00, 23:30). TGE has its first qualifying AH appearance; its regular-session appearance does not count. ACH and RCON are new tonight. WETO's initial +10.0% display is at the rounding boundary; the unrounded verification within this pulse is recorded below.

  Supplementary AH-change-only (>15%, not in volume pass): none

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| TGE | [TV](https://www.tradingview.com/chart/?symbol=TGE) | $1.55 | +86.7% | +10.3% | $1.71 | +106.0% | 6.8M | 19.0M | 0.4x | 44.2M | Financial Conglomerates |
| LPA | [TV](https://www.tradingview.com/chart/?symbol=LPA) | $2.86 | +1.4% | +15.8% | $3.31 | +17.4% | 1.9M | 262K | 7.1x | 5.2M | Real Estate Development |
| WETO | [TV](https://www.tradingview.com/chart/?symbol=WETO) | $1.01 | -8.2% | +10.0% | $1.11 | +1.0% | 1.3M | 9.4M | 0.1x | 915K | Other Transportation |
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $1.24 | +1.6% | +8.9% | $1.35 | +10.7% | 829K | 40.9M | 0.0x | 4.4M | Miscellaneous Commercial Services |
| SDEV | [TV](https://www.tradingview.com/chart/?symbol=SDEV) | $2.59 | -20.8% | +5.0% | $2.72 | -16.8% | 456K | 26.3M | 0.0x | 1.8M | Pharmaceuticals: Major |
| ACH | [TV](https://www.tradingview.com/chart/?symbol=ACH) | $0.56 | -8.1% | +6.6% | $0.60 | -2.0% | 261K | 1.8M | 0.1x | 69.7M | Medical Specialties |
| FLNA | [TV](https://www.tradingview.com/chart/?symbol=FLNA) | $0.89 | -4.2% | +8.2% | $0.96 | +3.7% | 95K | 10.8M | 0.0x | 47.3M | Biotechnology |
| RCON | [TV](https://www.tradingview.com/chart/?symbol=RCON) | $1.29 | +4.9% | +5.4% | $1.36 | +10.6% | 52K | 321K | 0.2x | 933K | Electronics Distributors |

### Evaluation notes

**Decision: no paper entries.** TGE needs a second qualifying AH scan and a current book. LPA's persistent opening high with repeated completed CONFIRM-3 NO readings meets the FIRST-BAR-SPIKE skip, and its zero-ask quote still cannot establish fillable liquidity. WETO's late surge has retreated with sharply reduced per-bar volume; a positive confirmation verdict does not remove that failure. The other five scanner names are below +10% AH. Alpaca reports no open positions; its order history shows no new entry or open order. No order was submitted, and no filled position was added to the paper-trade table or `OPEN_POSITIONS.md`.

**Tradability:** ACH and RCON returned `tradable=true` before SIP workup. SDEV also returned true; retain the earlier true results for TGE, LPA, WETO, NCPL, and FLNA. The seven previously recorded false results remain **untradable (carried)** without repeated SIP verification or catalyst searches. Float and sector are recorded for pattern tracking, without a float or sector skip.

**SIP evidence and freshness:** All 11 requests (the eight scanner names plus dropped prior candidates PARA, HIT, and DKI) used `broker.js bars --tf 5Min --start 2026-09-30T20:00:00Z --limit 1000` and returned `feed=sip`. The latest bars for the liquid names start at 17:15 ET and cover through 17:20, consistent with the approximately 15-minute historical-feed delay. The later ten minutes remain unserved. Sparse names have earlier last trades, recorded below. The scanner's qualifying prices are within the available consolidated traded ranges; no bad-print rejection is supported. Discovery AH Vol and VRatio do not establish current fillable liquidity. Yahoo was used only for timeline shape; its printed AH volumes, exact highs, and previous-close-based change percentages were not used for entry verification.

| Ticker | Available SIP shares | Trades | Latest bar start ET | Latest high | Latest close | Latest VWAP | Latest shares | Latest trades |
|--------|----------------------|--------|---------------------|-------------|--------------|-------------|---------------|---------------|
| TGE | 7,602,216 | 25,882 | 17:15 | $1.75 | $1.69 | $1.71 | 404,367 | 2,203 |
| LPA | 2,416,724 | 26,711 | 17:15 | $3.33 | $3.32 | $3.31 | 28,841 | 320 |
| WETO | 1,439,747 | 5,823 | 17:15 | $1.14 | $1.13 | $1.12 | 24,541 | 103 |
| NCPL | 887,135 | 2,433 | 17:15 | $1.35 | $1.33 | $1.33 | 8,095 | 36 |
| SDEV | 507,039 | 2,525 | 17:15 | $2.75 | $2.70 | $2.72 | 11,802 | 97 |
| ACH | 368,028 | 16 | 17:10 | $0.60 | $0.60 | $0.60 | 450 | 1 |
| FLNA | 99,986 | 389 | 17:10 | $0.96 | $0.96 | $0.95 | 1,017 | 5 |
| RCON | 60,188 | 319 | 17:15 | $1.36 | $1.30 | $1.34 | 3,265 | 31 |

- **TGE — Watch; first qualifying AH scan, real later surge, current book unverified.** The scanner shows Day +86.7%, AH +10.3%, Total +106.0%, below the +150% ceiling. SIP shows a later-volume surge at 17:05: 1,510,542 shares / 5,432 trades, high $1.85, close/VWAP $1.76. Subsequent bars eased to 801,152 / 3,507 and 404,367 / 2,203, with VWAP $1.74 → $1.71. This is real liquid activity, but volume and price are retreating from the later high. The scanner $1.71 is 7.6% below that high; the latest available close $1.69 is 8.6% below. Yahoo's later shape suggests a rebound requiring the next SIP check. An unrounded discovery refresh around 17:31 returned AH +12.2580645%, $1.74, Total +109.6%; it is verification within this pulse, not an additional independent AH scan. Recheck a second scheduled appearance, trajectory, recent daily bars/winner history, and current book before any entry. **Grade B**, fresh interim earnings verified below. Actual business: media, entertainment, and hospitality; scanner label: financial conglomerates. Float 44.2M.
- **LPA — Skip: FIRST-BAR-SPIKE and no verified current fillable ask. FIRST-BAR-SPIKE WATCH: hypothetical $3.31 at 17:30 ET / 23:30 CEST.** Scanner AH +10.8% → +15.8%, price $3.17 → $3.31, discovery volume 1.1M → 1.9M, VRatio 6.6x → 7.1x since 23:00. SIP confirms renewed real trading at 16:50–17:00 (237K / 2,631 trades, 196K / 1,683, 220K / 2,301), followed by 109K / 820, 105K / 898, then 29K / 320. The AH high remains $3.50 in the 16:10 opening bar; subsequent highs reached $3.49 at 16:30 and $3.46 at 17:00 without reclaiming it. The scanner price is 5.4% below the opening high. Every completed CONFIRM-3 verdict is NO (16:45, 17:00, 17:30); earlier readings were PENDING. Holding within 20% alone does not remove the persistent-opening-high skip. The latest SIP coverage still excludes any event after 17:20, and the next scan should recheck later highs. **Catalyst correction: Grade D under the fixed-price cash asset-purchase exclusion**, replacing the earlier provisional None after verifying the September 30 property-sale closing release. Logistics real estate; float 5.2M. The hypothetical is for morning evaluation, not a position.
- **WETO — Skip current setup: fading late spike, thin subsequent volume, and stale book.** Scanner AH +14.8% → displayed +10.0%, price $1.16 → $1.11, despite cumulative discovery volume 491K → 1.3M. An unrounded verification around 17:31 returned AH **+10.7920792%**, $1.119, Total +1.7%. This confirms an above-threshold reading within the 23:30 pulse; it does not recover the initial unrounded snapshot or create a separate scheduled scan. WETO was definitely above threshold at 23:00, but the trajectory/volume/book failures decide this scan regardless of the boundary count. SIP high $1.24 at 16:45 ET has not been reclaimed; VWAP fell $1.19 → $1.18 → $1.15 and later $1.12 → $1.11 → $1.12. Volume fell from 411,454 shares / 1,556 trades at the peak to 22,475 / 119 and 24,541 / 103 in the latest two bars. This is a faded surge with thin subsequent activity, not a sustained BUILD. CONFIRM-3 changed from PENDING to YES; that observation has no entry, grading, or ranking impact. **Grade None**; physical AI/wearable robotics, float 915K.
- **NCPL — Watch below threshold; thin activity persists.** AH +8.1% → +8.9%, price $1.34 → $1.35, discovery volume 655K → 829K. Latest SIP bars have 63,479 shares / 35 trades, 15,563 / 26, and 8,095 / 36. It retains one qualifying scanner appearance, at 22:30; cumulative volume growth does not establish sustained liquid accumulation. Grade None carried; capital-raising services, float 4.4M.
- **SDEV — Skip: AH +5.0% below threshold and Day -20.8% fails the dead-cat gate.** AH eased from +6.6%; latest SIP has 11,802 shares / 97 trades, close $2.70. No rising multi-scan reclaim or DEAD-CAT-OVERRIDE WATCH is established. Pharmaceuticals; float 1.8M.
- **ACH — Watch below threshold; sparse trades.** First discovery, AH +6.6%. SIP totals 368,028 shares but only 16 trades; 301,302 shares are in 13 opening trades, 65,916 in a single 16:25 trade, and just 450 in the latest 17:10 trade. No sustained liquid accumulation exists. Medical specialties; float 69.7M is recorded without a float skip.
- **FLNA — Watch below threshold; very little ongoing trading.** AH remains +8.2%, price $0.96, discovery volume 89K → 95K. Latest available SIP bar contains 1,017 shares / five trades at 17:10. It still has no verified >10% scheduled-scan appearance. Grade None carried; epilepsy biotechnology, float 47.3M.
- **RCON — Watch below threshold; small brief surge then retreat.** First discovery, AH +5.4%. SIP reached $1.38 at 17:05 on 31,747 shares / 136 trades; the next bars slowed to 15,457 / 96 and 3,265 / 31, closing $1.30. This is thin activity. Electronics-distributor scanner label; float 933K.

**Dropped prior candidates:** PARA's available SIP close is $0.64, 22.0% below its $0.82 high at 16:40, with only 26,192 shares / 66 trades in the latest bar; carry the spike→fade skip and its single qualifying scanner appearance. HIT's close is $0.82, 26.8% below the $1.12 opening high; carry the first-bar-spike skip and hypothetical $1.03 at 16:30 ET. DKI's close is $1.56, still below its $1.57 regular close and 34.2% below the $2.37 opening high; carry the Day -38.4% dead-cat skip and DEAD-CAT-OVERRIDE WATCH hypothetical $2.23 at 16:25 ET. Each has sharply reduced volume. These delayed bars support the observed fades; they do not establish instantaneous levels. Retain all three and the other absent watches in the final-scan pipeline.

**Book freshness:** LPA returned bid $2.46 x100 / ask $0.00 x0 at **16:00:01 ET**; TGE bid $1.49 x500 / ask $1.65 x400 at **16:59:31 ET**; WETO bid $0.88 x100 / ask $1.17 x100 at **16:00:00 ET**. One re-pull of each returned the same timestamp. None establishes a current book at 17:30; LPA cannot be sized from a zero ask. Consolidated trades establish real AH volume on all three, so these stale quotes do not support a fictitious-volume or bad-print conclusion. No order was sized from them.

**Spike-bar and third-bar instrumentation (verbatim; log only):** TGE and LPA exceed +10% in the discovery snapshot; WETO was instrumented at the rounding boundary and its unrounded reading exceeded +10% during verification.

```text
TGE 2026-09-30  SPIKE  17:06ET  +16%  $1.80  1372 trades / 379k sh  (first co-spike bar) (as-of 17:30ET)
TGE 2026-09-30  CONFIRM-3  NO ignition 17:05ET failed third-bar hold/volume as-of 17:30ET
LPA 2026-09-30  SPIKE  16:12ET  +22%  $3.50  1174 trades / 89k sh  (first co-spike bar) (as-of 17:30ET)
LPA 2026-09-30  CONFIRM-3  NO ignition 16:10ET failed third-bar hold/volume as-of 17:30ET
WETO 2026-09-30  SPIKE  16:42ET  +16%  $1.17  249 trades / 56k sh  (first co-spike bar) (as-of 17:30ET)
WETO 2026-09-30  CONFIRM-3  YES ignition 16:40ET 8.1x; confirmed 16:50ET $1.15 as-of 17:30ET
```

CONFIRM-3 does not independently enter, skip, grade, or rank a candidate. LPA's decision applies the separately specified persistent-opening-high rule; WETO's skip comes from its declining trajectory, thin subsequent bars, and stale book.

**Structured catalyst searches and corrections:** TGE received four `websearch search` calls: earnings, one identical Tavily retry after default-provider rate limiting, same-day wire releases, and SEC material filings. The initial earnings query included an incorrect expanded company name; issuer identity was corrected to The Generation Essentials Group and confirmed from its SEC filing. LPA and WETO each received three Tavily calls covering earnings, same-day press releases, and material SEC filings (8-K / 6-K). All stayed within the four-call budget. The SEC submissions endpoint and the primary 6-K documents/exhibits were retrieved directly for TGE and LPA; both returned HTTP 200, resolving LPA's earlier HTTP 403 limitation. Search-index dates were stale and did not reliably identify these same-day filings.

- **TGE — Grade B, fresh interim earnings.** [SEC 6-K](https://www.sec.gov/Archives/edgar/data/2053456/000121390026104923/ea0307190-6k_generation.htm), accession **0001213900-26-104923**, filed September 30 and accepted **September 30 at 05:14:02 ET (09:14:02Z)**. The [attached interim results](https://www.sec.gov/Archives/edgar/data/2053456/000121390026104923/ea030719001ex99-1.htm) were read beyond the headline: customer-contract revenue +35.8% to $30.8M, hospitality revenue +59.8%, EPS $0.12 → $0.56, and net profit $2.093M → $22.848M. Concern: total reported revenue including investment gains fell $87.429M → $65.864M, and the prior-year $58.878M one-off share-based expense was absent this year, helping the profit comparison. No analyst-consensus beat is claimed. The filing time is verified; a separate wire-release publication time is not. This is current-date morning news, not a new after-close earnings release.
- **LPA — Grade D, fresh fixed-price cash asset-sale completion; earlier provisional None corrected.** [SEC 6-K](https://www.sec.gov/Archives/edgar/data/1997711/000199771126000172/latampropertiesoftheameric.htm), accession **0001997711-26-000172**, filed September 30 and accepted **September 30 at 12:14 ET (16:14Z)**. The [attached September 30 release](https://www.sec.gov/Archives/edgar/data/1997711/000199771126000172/ex991lpacompletesplssalepr.htm) confirms completion of the previously disclosed **$145M Parque Logístico Lima Sur sale to FIBRA Prime**: $85M received at closing, $60M payable in two $30M installments after 12/24 months, and a $55M BTG Pactual credit facility at 8.5% against those deferred proceeds. LPA retains property-management fee income and intends to redeploy proceeds in Mexico. Apply the prompt's fixed-price cash asset-purchase exclusion from Grade A; record D rather than treating filing freshness as an operational Grade A. This is the sale of a property within LPA's portfolio; no fixed per-share buyout value is claimed. The filing time is verified; a separate wire-release publication time is not. The September 11 approval and September 21 Costa Rica sale remain older background, distinct from today's Peru closing.
- **WETO — Grade None; no fresh catalyst found.** Earnings checks returned no verified September 30 report. [Wire searches](https://www.globenewswire.com/news-release/2026/07/22/3331270/0/en/wetour-robotics-enters-into-us-20-million-north-american-multi-site-commercial-agreement-for-orchestra-robotics-services.html) returned July announcements and September 1 related-news snippets; the [filing index](https://www.stocktitan.net/sec-filings/WETO) still lists September 18 as latest. A [same-day trading commentary](https://www.timothysykes.com/news/wetour-robotics-limited-weto-news-2026_09_30-2) is timestamped **September 30 at 08:32:28 ET**, but its claimed AI breakthrough lacks a verified fresh underlying announcement; it is not graded from the headline. No fresh primary release time was verified. No catalyst is a learning-phase concern, not an entry skip.

**Carry forward:** Add ACH and RCON to the prior 37-name pipeline: **39 unique names**, 32 tradable and seven **untradable (carried)** (GBLRF, MHUAF, SFES, WTLLF, BMNM, FNFI, MCDIF). At the 00:30 CEST final scan, cross-check tracked tradable names against SIP for feed-lag omissions, including regular-session watches and absent discovery names. TGE needs a second qualifying scheduled scan and sustained trajectory/current book; LPA needs a later volume-backed high and fillable book to revisit the opening-spike skip; WETO needs renewed sustained accumulation/current liquidity. No fill occurred, so CHASE-CAP does not apply. This is not the final scan, so FINAL-SCAN-GATE-BLOCK does not apply. Before any later entry, check recent daily bars and `WINNERS_TRACKING.md` for MULTI-SESSION-RUNNER instrumentation; no entry was made on an assumed first-day classification.

**Daily email:** Include the no-entry decision, TGE's verified morning interim earnings and first qualifying AH appearance, LPA's resolved September 30 filing/catalyst correction and FIRST-BAR-SPIKE WATCH at $3.31, WETO's faded surge despite CONFIRM-3 YES, and stale quote timestamps limiting executable-book verification. No item from this scan requires Juan's input.

## Scan 00:00 CEST (6:00 PM ET)

`python3 scripts/scan.py --all` ran at 18:00:26 ET on September 30 (00:00:26 CEST on October 1), in the AFTERHOURS session, and returned 11 candidates. TGE has its second >10% AH scanner appearance (23:30, 00:00); LPA has its fifth. WETO is above threshold again after its 23:00 appearance and above-threshold verification within the 23:30 pulse. QSI and KRMD have their first qualifying AH appearance; GURE and BURU are also new tonight but below threshold. Regular-session appearances do not count toward the two-AH-scan gate.

  Supplementary AH-change-only (>15%, not in volume pass): KRMD

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| TGE | [TV](https://www.tradingview.com/chart/?symbol=TGE) | $1.55 | +86.7% | +10.3% | $1.71 | +106.0% | 9.2M | 19.2M | 0.5x | 44.2M | Financial Conglomerates |
| LPA | [TV](https://www.tradingview.com/chart/?symbol=LPA) | $2.86 | +1.4% | +16.4% | $3.33 | +18.1% | 2.1M | 288K | 7.2x | 5.2M | Real Estate Development |
| WETO | [TV](https://www.tradingview.com/chart/?symbol=WETO) | $1.01 | -8.2% | +10.9% | $1.12 | +1.8% | 1.5M | 9.4M | 0.2x | 915K | Other Transportation |
| QSI | [TV](https://www.tradingview.com/chart/?symbol=QSI) | $1.07 | +11.7% | +11.2% | $1.19 | +24.2% | 947K | 5.1M | 0.2x | 171.3M | Packaged Software |
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $1.24 | +1.6% | +7.7% | $1.33 | +9.4% | 872K | 40.9M | 0.0x | 4.4M | Miscellaneous Commercial Services |
| SES | [TV](https://www.tradingview.com/chart/?symbol=SES) | $0.60 | +12.3% | +6.5% | $0.64 | +19.5% | 822K | 19.2M | 0.0x | 250.0M | Electrical Products |
| CHGA | [TV](https://www.tradingview.com/chart/?symbol=CHGA) | $2.40 | +22.4% | +5.4% | $2.53 | +29.1% | 403K | 3.3M | 0.1x | 1.1M | Biotechnology |
| GURE | [TV](https://www.tradingview.com/chart/?symbol=GURE) | $3.06 | -4.4% | +7.5% | $3.29 | +2.8% | 319K | 369K | 0.9x | 1.3M | Chemicals: Specialty |
| FLNA | [TV](https://www.tradingview.com/chart/?symbol=FLNA) | $0.89 | -4.2% | +7.2% | $0.95 | +2.7% | 95K | 10.8M | 0.0x | 47.3M | Biotechnology |
| BURU | [TV](https://www.tradingview.com/chart/?symbol=BURU) | $0.99 | +4.9% | +9.5% | $1.08 | +14.9% | 58K | 1.1M | 0.1x | 8.4M | Electronic Components |
| KRMD | [TV](https://www.tradingview.com/chart/?symbol=KRMD) | $2.93 | -2.5% | +15.1% | $3.37 | +12.3% | 31K | 366K | 0.1x | 43.1M | Medical Specialties |

### Evaluation notes

**Decision: no paper entries.** TGE clears the scan-count gate but lacks a verified current book. LPA retains the first-bar-spike skip and a zero-ask snapshot. WETO's recent bars are thin after its earlier surge. QSI needs a second qualifying AH scan and sustained follow-through; KRMD has almost no ongoing trading and no verified fillable ask. The other six scanner names are below +10% AH. Alpaca reports no open positions, and its order history has no new entry or open order. No order was submitted; no fill was added to the paper-trade table or `OPEN_POSITIONS.md`.

**Tradability:** QSI and KRMD returned `tradable=true` before SIP and catalyst workup. New below-threshold names GURE and BURU also returned true. Carry earlier verified true results for the seven other scanner names. Float and sector are recorded for pattern tracking; QSI's 171.3M float is not an entry skip.

**SIP evidence and freshness:** All five >10% names were checked with `broker.js bars --tf 5Min --start 2026-09-30T20:00:00Z --limit 1000`; all returned `feed=sip`. TGE, LPA, WETO, and QSI have bars starting at 17:45 ET, covering through 17:50, consistent with the approximately 15-minute historical-feed delay. KRMD's last available trade bar starts at 17:40 ET. These bars corroborate the scanner's prices but do not establish instantaneous levels or activity in the unserved final ten minutes. No candidate is rejected as a bad print. TradingView AH Vol and VRatio remain discovery signals.

| Ticker | Available SIP shares | Trades | Latest bar start ET | Latest high | Latest close | Latest VWAP | Latest shares | Latest trades |
|--------|----------------------|--------|---------------------|-------------|--------------|-------------|---------------|---------------|
| TGE | 9,905,955 | 34,767 | 17:45 | $1.76 | $1.73 | $1.73 | 165,374 | 754 |
| LPA | 2,660,877 | 29,302 | 17:45 | $3.36 | $3.34 | $3.34 | 8,934 | 153 |
| WETO | 1,591,398 | 6,626 | 17:45 | $1.12 | $1.11 | $1.11 | 7,387 | 54 |
| QSI | 1,263,555 | 2,230 | 17:45 | $1.25 | $1.23 | $1.22 | 287,048 | 883 |
| KRMD | 31,306 | 11 | 17:40 | $3.37 | $3.37 | $3.37 | 101 | 2 |

- **TGE — Wait for the next scan: current fillable book unconfirmed; holding gains with slowing volume.** Scanner AH +10.3% and price $1.71 are unchanged from 23:30, while discovery volume rose 6.8M → 9.2M and VRatio 0.4x → 0.5x. SIP confirms liquid trading: 17:20–17:40 bars have 237K–724K shares and 1,106–2,659 trades each. Available closes since 17:20 are $1.76 → $1.73 → $1.80 → $1.75 → $1.71 → $1.73, holding a range below the $1.85 high at 17:05. The scanner price is 7.6% below that high, and the latest available close is 6.5% below. Volume declined 415K → 300K → 237K → 165K in the last four bars; this is a concern to recheck, not proof of a vanished AH spike. Its before-18:30 peak alone does not disqualify this near-high hold. The book re-pull is still timestamped 16:59:31, so no order can be sized from a current verified ask. **Grade B**, verified current-date interim earnings. Sector: media/entertainment/hospitality, despite the financial-conglomerates label. Recent daily closes are September 24 $0.833, September 25 $0.820, September 28 $0.844, September 29 $0.830, September 30 $1.550; no prior-session large run or `WINNERS_TRACKING.md` match was found. No MULTI-SESSION-RUNNER tag is supported. Qualifying-scan price $1.71 / Total +106.0%; there is no fill for CHASE-CAP measurement.
- **LPA — Skip: FIRST-BAR-SPIKE, declining recent volume, and no verified current fillable ask. FIRST-BAR-SPIKE WATCH: hypothetical $3.33 at 18:00 ET / 00:00 CEST.** Scanner AH +15.8% → +16.4%, price $3.31 → $3.33, VRatio 7.1x → 7.2x since 23:30. The consolidated AH high remains $3.50 in the 16:10 opening bar; later highs have not reclaimed it. Every completed CONFIRM-3 verdict remains NO; earlier PENDING readings do not count as NO. The scanner price is 4.9% below the opening high, which does not remove the explicit first-bar-spike skip. Recent shares/trades fell 78,582/852 → 47,977/426 → 17,498/197 → 8,934/153; rising cumulative discovery volume does not establish a renewed liquid BUILD. **Grade D carried** under the specified fixed-price cash asset-purchase exclusion, from the verified September 30 property-sale completion. Logistics real estate; float 5.2M. The hypothetical is for morning evaluation, not a position.
- **WETO — Skip current setup: thin activity after the earlier spike and stale book.** Scanner AH is +10.9%, price $1.12, discovery volume 1.3M → 1.5M since 23:30. The 16:45 high remains $1.24; scanner price is 9.7% below it. This has stabilized below the earlier surge, but ongoing volume does not support a liquid BUILD: the last four bars contain 63,619/313 → 28,703/149 → 17,716/90 → 7,387/54 shares/trades. Latest VWAPs declined $1.15 → $1.14 → $1.12 → $1.11. CONFIRM-3 YES remains log-only and does not remove the thin-volume or current-book failures. **Grade None**, no fresh catalyst found; physical AI/wearable robotics, float 915K.
- **QSI — Watch; first qualifying AH scan, emerging late volume surge, current book unconfirmed.** The 17:45 SIP bar accelerated to 287,048 shares / 883 trades from 22,518 / 131 at 17:40, reaching an available new AH high of $1.25 with close $1.23 and VWAP $1.22. Earlier bars were mostly tens of K shares and tens/hundreds of trades. This is a new surge requiring follow-through, not established sustained accumulation across liquid bars. Scanner $1.19 / AH +11.2% is corroborated by SIP; the later available close is about +15.0% above the rounded $1.07 regular close. Neither an intrabar high nor a second verification within this pulse supplies another independent qualifying AH scan. **Grade None**, no fresh catalyst found; actual business is proteomics/protein-sequencing technology despite the software scanner label. Float 171.3M is tracked without a float skip. NO-SPIKE and CONFIRM-3 PENDING are instrumentation only.
- **KRMD — Skip: sparse AH trading, no verified fillable ask, and only one qualifying scan.** Added solely by the supplementary change-ranked pass. Of 31,306 SIP shares / 11 trades, 31,097 shares / eight trades are in the 16:00 closing bar; the only subsequent available bars contain 108 shares / one trade at 17:30 and 101 shares / two trades at 17:40. Those tiny trades corroborate $3.36–$3.37 but cannot establish real accumulating liquidity. This is a thin print, not a sustained volume-backed ramp; the quoted ask remains $0.00 x0 on a stale snapshot. **Grade None**, no fresh catalyst found; subcutaneous infusion devices / medical specialties, float 43.1M. Record discovery for retrospective coverage without treating the supplementary pass as entry qualification.

**Below-threshold names:** NCPL eased AH +8.9% → +7.7% since 23:30 and retains its single qualifying appearance at 22:30; carry the thin-activity concern and Grade None. SES is +6.5% and retains the earlier sparse-trading concern. CHGA reappears at +5.4% AH after its regular-session watch; no qualifying AH appearance is established. FLNA eased +8.2% → +7.2%, with displayed discovery volume unchanged at 95K; carry Grade None and the sparse-trading observation. New GURE (+7.5% AH) and BURU (+9.5%) are watches below threshold. No >10% catalyst or instrumentation workup is triggered for these six names.

**Book timestamps, including one re-pull per >10% name:** All re-pulls returned the identical quotes below. These are stale snapshots, not current contradictory evidence. SIP shows actual trades; zero asks on old snapshots do not establish that all AH volume is fictitious. LPA and KRMD cannot be sized from a zero ask; the nominal two-sided books for TGE, WETO, and QSI also fail current-book verification. Recheck at the next scheduled scan; no order was sized from these quotes.

| Ticker | Bid | Ask | Quote time ET |
|--------|-----|-----|---------------|
| TGE | $1.49 x500 | $1.65 x400 | 16:59:31 |
| LPA | $2.46 x100 | $0.00 x0 | 16:00:01 |
| WETO | $0.88 x100 | $1.17 x100 | 16:00:00 |
| QSI | $1.10 x300 | $1.19 x500 | 16:59:07 |
| KRMD | $2.51 x100 | $0.00 x0 | 16:00:03 |

**Spike-bar and third-bar instrumentation (verbatim; log only):**

```text
TGE 2026-09-30  SPIKE  17:06ET  +16%  $1.80  1372 trades / 379k sh  (first co-spike bar) (as-of 18:00ET)
TGE 2026-09-30  CONFIRM-3  NO ignition 17:05ET failed third-bar hold/volume as-of 18:00ET
LPA 2026-09-30  SPIKE  16:12ET  +22%  $3.50  1174 trades / 89k sh  (first co-spike bar) (as-of 18:00ET)
LPA 2026-09-30  CONFIRM-3  NO ignition 16:10ET failed third-bar hold/volume as-of 18:00ET
WETO 2026-09-30  SPIKE  16:42ET  +16%  $1.17  249 trades / 56k sh  (first co-spike bar) (as-of 18:00ET)
WETO 2026-09-30  CONFIRM-3  YES ignition 16:40ET 8.1x; confirmed 16:50ET $1.15 as-of 18:00ET
QSI 2026-09-30  NO-SPIKE  peak +12% @17:45ET  (no bar cleared +15% on a volume co-spike) (as-of 18:00ET)
QSI 2026-09-30  CONFIRM-3  PENDING ignition 17:45ET; waiting for third bar as-of 18:00ET
KRMD 2026-09-30  NO-SPIKE  peak +15% @17:44ET  (no bar cleared +15% on a volume co-spike) (as-of 18:00ET)
KRMD 2026-09-30  CONFIRM-3  NO no local-volume new-high ignition as-of 18:00ET
```

CONFIRM-3 does not independently enter, skip, grade, or rank candidates. LPA applies the separately specified persistent-opening-high rule. The one-minute spike detector and five-minute bars have different coverage/resolution; QSI's NO-SPIKE does not reject its emerging SIP surge.

**Structured catalyst checks:** Three Tavily `websearch search` calls each for TGE, LPA, WETO, and KRMD covered earnings, press releases, and SEC material filings (6-K for the foreign issuers). QSI received those three checks plus a fourth targeted search for the surfaced September 29 8-K / September 28 event. All per-ticker budgets were respected. No dated headline alone was used for grading. No fresh catalyst was found for WETO, QSI, or KRMD; Grade None is a concern, not an entry skip.

- **TGE — Grade B, current-date interim earnings confirmed again; wire time newly verified.** [PRNewswire interim results](https://www.prnewswire.com/news-releases/tges-profit-surged-by-9-9-times-with-total-assets-at-us1-8bn-and-net-assets-at-us932m-302894260.html) were published **September 30, 2026 at 06:27 ET**. Carry the earlier primary [SEC 6-K](https://www.sec.gov/Archives/edgar/data/2053456/000121390026104923/ea0307190-6k_generation.htm) verification, accepted **September 30 at 05:14:02 ET (09:14:02Z)**, and its [results exhibit](https://www.sec.gov/Archives/edgar/data/2053456/000121390026104923/ea030719001ex99-1.htm): customer-contract revenue +35.8%, hospitality revenue +59.8%, EPS $0.12 → $0.56, net profit $2.093M → $22.848M. Total reported revenue fell, and the prior-year one-off share-based expense helped the profit comparison; no consensus beat is claimed. This is fresh morning news, not an after-close earnings release. Search filing indexes still lag the verified primary filing.
- **LPA — Grade D carried from the prior primary-source workup.** [September 30 6-K](https://www.sec.gov/Archives/edgar/data/1997711/000199771126000172/latampropertiesoftheameric.htm), accession **0001997711-26-000172**, was accepted **September 30 at 12:14 ET (16:14Z)**. Its [September 30 property-sale closing exhibit](https://www.sec.gov/Archives/edgar/data/1997711/000199771126000172/ex991lpacompletesplssalepr.htm) confirms the $145M Parque Logístico Lima Sur sale to FIBRA Prime, including $85M at closing, $60M deferred, and the $55M financing facility. Apply the specified fixed-price cash asset-purchase exclusion; this is a portfolio-property sale, not a fixed per-share takeover. Today's searches still returned older indexed material; they do not supersede the prior primary verification. Separate wire-publication time remains unverified. August 12 earnings and September 21 Costa Rica-sale news are background.
- **WETO — Grade None.** Earnings search found no verified September 30 report. The wire search returned a [July 27 warehouse-robotics cooperation announcement](https://marketchameleon.com/PressReleases/i/2343967/WETO/wetour-robotics-to-enter-into-warehouse-robotics), while [SEC results](https://www.stocktitan.net/sec-filings/WETO) returned older filings through September 18. The September 30 commentary timestamped 08:32:28 ET still lacks a verified fresh underlying announcement; its robotics-breakthrough headline is not graded. No fresh catalyst found.
- **QSI — Grade None.** [Earnings history](https://public.com/stocks/qsi/earnings) and the [company event calendar](https://ir.quantum-si.com/events-and-presentations/events) identify August 13 Q2 results; the call was at 16:30 ET that day. The [release index](https://www.quantum-si.com/news-events/press-releases) initially returned older material. The fourth search found the official [Proteus interim-data announcement](https://www.quantum-si.com/press-releases/quantum-si-presents-interim-proteus-data-at-world-hupo-2026-demonstrating-a-significant-step-change-in-performance-compared-to-platinum-pro), explicitly dated **September 28, 2026**, with a Singapore presentation on September 29. This is older than the immediately preceding overnight news window; no publication time was verified or used for grading. The [SEC index](https://www.marketwatch.com/investing/stock/qsi/financials/secfilings) shows a September 29 8-K with document date September 28, not a verified fresh September 30 event. No fresh catalyst found; four-call budget exhausted.
- **KRMD — Grade None.** [Earnings history](https://www.marketbeat.com/stocks/NASDAQ/KRMD/earnings) identifies August 5 Q2 results; [BusinessWire](https://www.businesswire.com/news/home/20260805069380/en/KORU-Medical-Systems-Announces-Second-Quarter-2026-Results-and-Updates-Full-Year-2026-Guidance) returned the same older release. SEC search found the [August 14 filing](https://investors.korumedical.com/sec-filings/all-sec-filings/content/0001161697-26-000200/form_8-k.htm) and older bylaws/manufacturing disclosures, with no verified September 30 material event. These are background; no fresh catalyst found and no fresh publication time is used for grading.

**Carry forward:** Add QSI, KRMD, GURE, and BURU to the prior 39-name pipeline: **43 unique names**, 36 tradable and seven **untradable (carried)** broker blocks (GBLRF, MHUAF, SFES, WTLLF, BMNM, FNFI, MCDIF). Those seven received no repeated SIP verification or catalyst search. Retain absent HIT/PARA/DKI and all regular-session watches for the **00:30 CEST final-scan feed-lag cross-check**. Carry HIT's FIRST-BAR-SPIKE WATCH and DKI's DEAD-CAT-OVERRIDE WATCH hypotheticals from prior scans. TGE needs renewed current-book verification and a volume/trajectory recheck; QSI needs a second qualifying scan and sustained real volume. No fill occurred, so CHASE-CAP does not apply; this is not the last scheduled scan, so FINAL-SCAN-GATE-BLOCK does not apply. No ceiling-override watch qualifies here.

**Daily email:** Include the no-entry decision, TGE's two-scan qualification and fresh earnings blocked by the frozen quote, LPA's $3.33 FIRST-BAR-SPIKE WATCH, QSI's late surge awaiting a second scan, and KRMD's supplementary discovery with only 209 shares after the closing bar. Report the stale book timestamps as the execution-verification limitation. No item from this pulse requires Juan's input.

## Scan 00:30 CEST (6:30 PM ET)

`python3 scripts/scan.py --all` ran at **18:30:29 ET on September 30** (00:30:29 CEST on October 1), in the AFTERHOURS session, and returned 12 candidates. This is the final scheduled scan for the September 30 US trading date. LPA has six scanner appearances above +10% AH; QSI has two (00:00 and 00:30). PWCM has its first qualifying appearance. PWCM and HCAI are new tonight. Regular-session appearances do not count toward the two-AH-scan gate.

  Supplementary AH-change-only (>15%, not in volume pass): none

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| TGE | [TV](https://www.tradingview.com/chart/?symbol=TGE) | $1.55 | +86.7% | +7.7% | $1.67 | +101.2% | 10.1M | 19.3M | 0.5x | 44.2M | Financial Conglomerates |
| LPA | [TV](https://www.tradingview.com/chart/?symbol=LPA) | $2.86 | +1.4% | +14.7% | $3.28 | +16.3% | 2.2M | 297K | 7.2x | 5.2M | Real Estate Development |
| QSI | [TV](https://www.tradingview.com/chart/?symbol=QSI) | $1.07 | +11.7% | +10.3% | $1.18 | +23.2% | 1.6M | 5.2M | 0.3x | 171.3M | Packaged Software |
| WETO | [TV](https://www.tradingview.com/chart/?symbol=WETO) | $1.01 | -8.2% | +7.9% | $1.09 | -0.9% | 1.6M | 9.4M | 0.2x | 915K | Other Transportation |
| SES | [TV](https://www.tradingview.com/chart/?symbol=SES) | $0.60 | +12.3% | +5.0% | $0.63 | +17.9% | 860K | 19.2M | 0.0x | 250.0M | Electrical Products |
| CHGA | [TV](https://www.tradingview.com/chart/?symbol=CHGA) | $2.40 | +22.4% | +5.2% | $2.53 | +28.9% | 447K | 3.3M | 0.1x | 1.1M | Biotechnology |
| GURE | [TV](https://www.tradingview.com/chart/?symbol=GURE) | $3.06 | -4.4% | +7.8% | $3.30 | +3.1% | 321K | 370K | 0.9x | 1.3M | Chemicals: Specialty |
| PWCM | [TV](https://www.tradingview.com/chart/?symbol=PWCM) | $1.13 | +14.5% | +15.0% | $1.30 | +31.7% | 203K | 603K | 0.3x | 2.3M | Miscellaneous Commercial Services |
| IMCC | [TV](https://www.tradingview.com/chart/?symbol=IMCC) | $2.25 | -8.2% | +6.7% | $2.40 | -2.0% | 199K | 16.9M | 0.0x | 1.5M | Agricultural Commodities/Milling |
| BURU | [TV](https://www.tradingview.com/chart/?symbol=BURU) | $0.99 | +4.9% | +9.5% | $1.08 | +14.9% | 186K | 1.1M | 0.2x | 8.4M | Electronic Components |
| FLNA | [TV](https://www.tradingview.com/chart/?symbol=FLNA) | $0.89 | -4.2% | +5.2% | $0.93 | +0.8% | 98K | 10.8M | 0.0x | 47.3M | Biotechnology |
| HCAI | [TV](https://www.tradingview.com/chart/?symbol=HCAI) | $0.53 | -0.4% | +7.3% | $0.57 | +6.9% | 50K | 1.7M | 0.0x | 7.3M | Industrial Machinery |

### Evaluation notes

**Decision: no paper entries.** LPA retains the first-bar-spike skip and has no verified current ask. QSI clears the two-scan count but recent volume has faded to tens of K shares / tens or hundreds of trades per bar, and its quote is stale. PWCM has real late ignition but only one qualifying scan and no verified current book. No candidate clears every entry gate. Alpaca reports no open positions; the order history has no new entry or open order. No order was submitted and no fill was added to the paper-trade table or `OPEN_POSITIONS.md`.

**Tradability:** New names PWCM and HCAI returned `tradable=true` before workup. Alpaca identifies PWCM as **PowerCompute, Inc.**, formerly LM Funding America: Bitcoin mining/treasury and planned HPC/AI infrastructure, alongside specialty finance. Carry the previously verified true states for other scanner and pipeline names. Carry seven **untradable (carried)** states without repeated SIP verification or catalyst searches: GBLRF, MHUAF, SFES, WTLLF, BMNM, FNFI, MCDIF. Float and sector are recorded for pattern analysis, without a float or sector skip.

- **LPA — Skip: FIRST-BAR-SPIKE, thin recent activity, and no verified current fillable ask. FIRST-BAR-SPIKE WATCH: hypothetical $3.28 at 18:30 ET / 00:30 CEST.** Scanner AH +16.4% → +14.7%, price $3.33 → $3.28 since 00:00, while discovery volume rose 2.1M → 2.2M. SIP totals 2,779,454 shares / 30,698 trades. Its AH high remains **$3.50 at 16:10 ET**, within the opening 16:00–16:15 window; no later volume-backed high reclaimed it. Every completed CONFIRM-3 verdict is NO; the earlier PENDING readings are not counted as NO. The scanner price remains 6.3% below that opening high, which does not remove the specified first-bar-spike skip. Recent bar volume is 27,475 / 317 trades → 8,505 / 130 → 36,553 / 394, with VWAP $3.32 → $3.27 → $3.25. This is not renewed liquid accumulation. **Grade D carried**, from the verified current-date fixed-price cash property-sale completion under the supplied asset-purchase exclusion. Logistics real estate; float 5.2M. This hypothetical is for morning evaluation, not a position.
- **QSI — Skip: thin/fading volume after the late surge and stale book; two qualifying scans are established.** Scanner AH +11.2% → +10.3%, price $1.19 → $1.18, discovery volume 947K → 1.6M since 00:00. The 17:45 surge reached **$1.25** on 287,048 shares / 883 trades. Volume then declined 198,985 / 661 → 84,304 / 257 → 50,028 / 227 → 47,702 / 108 → 35,659 / 74 → 34,120 / 181; VWAP eased $1.21 → $1.21 → $1.20 → $1.18 → $1.18 → $1.19. Its latest available close $1.18 is only 5.6% below the high, but proximity alone cannot replace sustained real volume. Yahoo's later timeline suggests a rebound after 18:15; that shape does not establish current SIP liquidity. **Grade None** after refreshed earnings/PR/SEC searches; no verified fresh catalyst found. Proteomics/protein sequencing; float 171.3M is recorded, not used as a skip. CONFIRM-3 NO does not cause this decision.
- **PWCM — Skip: only one qualifying AH scan and current fillable book unverified; real late ignition detected.** Scanner $1.30 / AH +15.0% / Total +31.7% is inside the actual SIP traded range. Liquid activity increased from 21,624 shares / 93 trades at 18:00 to 45,113 / 198 at 18:05, 115,066 / 1,071 at 18:10, and **874,185 / 5,313 at 18:15**, with VWAP $1.16 → $1.20 → $1.30 → $1.44. Total SIP volume is 1,111,464 shares / 6,940 trades. The available AH high is **$1.51 at 18:15**; that bar closed $1.45, +28.3% above the regular close and about +46.9% from the previous close, still below the extension ceiling. This is a real late-volume surge despite discovery VRatio 0.3x. A within-pulse TradingView check advanced to $1.42 / AH +25.7%; it is delayed-feed verification, not a second independent scheduled scan. Yahoo's later shape shows a retreat after 18:15; do not infer a current BUILD/hold solely from the delayed highs. **Grade None**; no verified fresh catalyst found. Bitcoin mining/treasury and HPC/AI infrastructure; float 2.3M. CONFIRM-3 PENDING remains log-only. Retain this late discovery for morning analysis.
- **TGE — Skip: current AH below +10% and fading recent price/volume.** Scanner AH +10.3% → +7.7%, price $1.71 → $1.67 since 00:00. SIP latest closes are $1.66 → $1.66 → $1.63, with VWAP $1.69 → $1.66 → $1.63 and 78K–122K shares / 386–588 trades per bar. Its latest available close is 11.9% below the $1.85 high at 17:05 and +5.2% above the regular close. This is a decline across scans, rather than the earlier range hold. Carry **Grade B**, verified September 30 interim earnings. The 16:59:31 quote also remains stale. Media/entertainment/hospitality; float 44.2M.
- **WETO — Skip current setup: below threshold and thin post-surge activity.** Scanner AH +10.9% → +7.9%, price $1.12 → $1.09. The latest SIP bar has only 9,577 shares / 75 trades, VWAP $1.10; no renewed liquid BUILD is established. Carry Grade None and the previously documented stale-book limitation. Physical AI/wearable robotics; float 915K.
- **KRMD — Omitted scanner watch; skip sparse prints and unverified ask.** The supplementary pass did not add it this scan, but pipeline SIP still shows a latest $3.35 print, +14.3% above the regular close, at 17:50 ET. Total volume is 31,506 shares / 12 trades; only **409 shares / four trades** followed the opening closing-auction bar. No sustained real liquidity exists. Its stale zero-ask quote cannot size an entry. Carry Grade None; infusion devices, float 43.1M. This is detected but unqualified, not a volume-backed feed rescue.

**Other scanner names:** SES (+5.0%), CHGA (+5.2%), GURE (+7.8%), IMCC (+6.7%), BURU (+9.5%), FLNA (+5.2%), and new HCAI (+7.3%) are below +10% in the discovery snapshot. SIP latest bars have 2/40/6/1/47/4/5 trades respectively. BURU's cumulative discovery volume increased 58K → 186K without sustained liquid bars; FLNA eased +7.2% → +5.2%. GURE had an earlier SIP high $4.05 at 16:50 but is now $3.30 with only 539 shares / six trades at 18:10. Current rising or cumulative figures cannot establish liquid BUILD entries here. No fresh >10% candidate workup is triggered for these names.

**Final-scan feed-lag cross-check:** All **38 tradable names** in tonight's pipeline were checked with `broker.js bars --tf 5Min --start 2026-09-30T20:00:00Z --limit 1000`, including every regular-session watch, SGRX from the initial 21:30 snapshot, and all dropped AH candidates. Every request returned `feed=sip`. The seven carried false states were excluded from repeat verification. There are now **45 unique tracked names**: the previous 43 plus PWCM and HCAI.

The liquid names' latest available bar starts at **18:15 ET**, covering through 18:20, consistent with the free-tier historical delay at this scan. The unserved later minutes are not contradictory evidence. Earlier last bars on sparse names are listed below; do not treat those as fresh levels at 18:30. No omitted candidate shows a current available >10% level on sustained liquid bars that clears the remaining entry rules. KRMD is above threshold on isolated tiny trades; PWCM is already in the scanner and lacks a second appearance/current book. HIT and PARA remain deep fades (latest closes $0.80/$0.61, 28.6%/25.6% below their AH highs); DKI is $1.47 below its $1.57 regular close and retains the Day -38.4% dead-cat skip. Carry HIT's earlier FIRST-BAR-SPIKE WATCH hypothetical $1.03 at 16:30 and DKI's DEAD-CAT-OVERRIDE WATCH $2.23 at 16:25 for morning evaluation.

A within-pulse, unfiltered TradingView lookup resolved regular-session closes for all 38 symbols so AH changes below use the **regular close**, not the previous-day close or the 21:30 intraday price. It returned QSI +9.36% while SIP's available close remained +10.3%; the SIP reading is retained, and QSI's original two qualifying scheduled appearances stand. This lookup does not count as another scan. Broker display prices are rounded to cents, so SIP-derived percentages below are approximate. Yahoo was used only for later timeline shape, with no AH volume or exact-price verification taken from it.

| Ticker | Regular close | Latest SIP close | AH% vs regular close | Bar start ET | Bar shares / trades | Total SIP shares / trades |
|--------|---------------|------------------|----------------------|--------------|---------------------|---------------------------|
| TGE | $1.55 | $1.63 | +5.2% | 18:15 | 122,006 / 588 | 10,778,525 / 38,437 |
| CMCT | $2.93 | $2.88 | -1.7% | 18:15 | 2,486 / 43 | 539,491 / 4,258 |
| CHGA | $2.4 | $2.54 | +5.8% | 18:15 | 2,240 / 40 | 516,491 / 3,591 |
| GOW | $3.18 | $2.96 | -6.9% | 18:15 | 5,187 / 57 | 1,267,631 / 9,243 |
| TNON | $4.09 | $4.05 | -1.0% | 18:15 | 7,267 / 122 | 2,134,568 / 18,668 |
| CNTB | $1.1 | $1.12 | +1.8% | 18:15 | 9,886 / 56 | 1,722,961 / 4,287 |
| VBIO | $2.8 | $2.87 | +2.5% | 18:15 | 603 / 16 | 216,117 / 1,490 |
| RFL | $1.32 | $1.26 | -4.5% | 18:15 | 415 / 6 | 25,975 / 98 |
| FFR | $1.31 | $1.31 | +0.0% | 18:15 | 2,560 / 19 | 402,492 / 1,393 |
| SOTK | $5.9 | $6.05 | +2.5% | 18:05 | 301 / 1 | 8,337 / 13 |
| MSGY | $5.66 | $5.63 | -0.5% | 18:15 | 2,125 / 55 | 203,368 / 2,704 |
| FBDT | $1.04 | $1.04 | +0.0% | 18:10 | 322 / 1 | 60,117 / 134 |
| ACTU | $0.7797 | $0.72 | -7.7% | 17:05 | 500 / 1 | 11,098 / 11 |
| PMVP | $1.67 | $1.61 | -3.6% | 17:55 | 100 / 1 | 216,037 / 23 |
| TLSA | $1.11 | $1.11 | +0.0% | 18:05 | 151 / 1 | 13,324 / 25 |
| MWYN | $1.12 | $1.12 | +0.0% | 16:00 | 311 / 3 | 311 / 3 |
| EPOW | $3.96 | $3.96 | +0.0% | 16:00 | 164 / 1 | 164 / 1 |
| HIT | $0.8207 | $0.80 | -2.5% | 18:15 | 4,740 / 18 | 6,018,419 / 22,977 |
| DKI | $1.57 | $1.47 | -6.4% | 18:15 | 7,472 / 29 | 3,407,299 / 28,247 |
| NCPL | $1.24 | $1.30 | +4.8% | 18:15 | 9,083 / 10 | 971,597 / 2,575 |
| BENF | $1.36 | $1.38 | +1.5% | 18:15 | 385 / 2 | 101,582 / 52 |
| FLNA | $0.886 | $0.94 | +6.1% | 18:15 | 1,785 / 4 | 103,655 / 412 |
| LPA | $2.86 | $3.24 | +13.3% | 18:15 | 36,553 / 394 | 2,779,454 / 30,698 |
| USBC | $0.544 | $0.55 | +1.1% | 18:00 | 150 / 1 | 55,381 / 81 |
| SES | $0.6 | $0.63 | +5.0% | 18:15 | 3,451 / 2 | 1,430,670 / 499 |
| WETO | $1.01 | $1.11 | +9.9% | 18:15 | 9,577 / 75 | 1,672,837 / 7,093 |
| IMCC | $2.25 | $2.40 | +6.7% | 18:15 | 100 / 1 | 233,321 / 1,759 |
| PARA | $0.649 | $0.61 | -6.0% | 18:15 | 1,068 / 10 | 2,782,611 / 9,369 |
| SDEV | $2.59 | $2.67 | +3.1% | 18:15 | 10,318 / 85 | 685,754 / 3,641 |
| ACH | $0.5627 | $0.56 | -0.5% | 17:40 | 125 / 1 | 378,153 / 18 |
| RCON | $1.29 | $1.27 | -1.6% | 18:15 | 200 / 1 | 70,089 / 376 |
| QSI | $1.07 | $1.18 | +10.3% | 18:15 | 34,120 / 181 | 1,714,353 / 3,738 |
| GURE | $3.06 | $3.30 | +7.8% | 18:10 | 539 / 6 | 421,519 / 5,144 |
| BURU | $0.9861 | $1.08 | +9.5% | 18:15 | 9,293 / 47 | 204,476 / 628 |
| KRMD | $2.93 | $3.35 | +14.3% | 17:50 | 200 / 1 | 31,506 / 12 |
| SGRX | $1.59 | $1.53 | -3.8% | 17:35 | 496 / 2 | 27,254 / 108 |
| PWCM | $1.13 | $1.45 | +28.3% | 18:15 | 874,185 / 5,313 | 1,111,464 / 6,940 |
| HCAI | $0.5345 | $0.56 | +4.8% | 18:15 | 1,009 / 5 | 53,380 / 203 |

**Book freshness, including one re-pull:** LPA, QSI, PWCM, TGE, and KRMD returned identical timestamps on re-pull. None verifies the book at 18:30. Consolidated SIP shows genuine trades; stale quotes do not justify a fictitious-volume or bad-print rejection. No order was sized from them.

| Ticker | Bid | Ask | Quote time ET |
|--------|-----|-----|---------------|
| LPA | $2.46 x100 | $0.00 x0 | 16:00:01 |
| QSI | $1.10 x300 | $1.19 x500 | 16:59:07 |
| PWCM | $0.946 x100 | $1.29 x100 | 16:00:00 |
| TGE | $1.49 x500 | $1.65 x400 | 16:59:31 |
| KRMD | $2.51 x100 | $0.00 x0 | 16:00:03 |

**Spike-bar and third-bar instrumentation (verbatim; log only):** The three >10% scanner candidates were instrumented; KRMD was also instrumented because the pipeline cross-check retained it above threshold on thin trades.

```text
LPA 2026-09-30  SPIKE  16:12ET  +22%  $3.50  1174 trades / 89k sh  (first co-spike bar) (as-of 18:30ET)
QSI 2026-09-30  SPIKE  17:47ET  +17%  $1.25  275 trades / 147k sh  (first co-spike bar) (as-of 18:30ET)
PWCM 2026-09-30  SPIKE  18:13ET  +19%  $1.34  418 trades / 47k sh  (first co-spike bar) (as-of 18:30ET)
LPA 2026-09-30  CONFIRM-3  NO ignition 16:10ET failed third-bar hold/volume as-of 18:30ET
QSI 2026-09-30  CONFIRM-3  NO ignition 17:45ET failed third-bar hold/volume as-of 18:30ET
PWCM 2026-09-30  CONFIRM-3  PENDING ignition 18:10ET; waiting for third bar as-of 18:30ET
KRMD 2026-09-30  NO-SPIKE  peak +15% @17:44ET  (no bar cleared +15% on a volume co-spike) (as-of 18:30ET)
KRMD 2026-09-30  CONFIRM-3  NO no local-volume new-high ignition as-of 18:30ET
```

CONFIRM-3 NO/PENDING does not independently enter, skip, grade, or rank candidates. LPA uses the separately specified persistent-opening-high rule. PWCM's ignition is at 18:10; its third five-minute bar starts at 18:20, beyond the available SIP coverage during this workup, so PENDING is expected.

**Structured catalyst checks:** QSI received three Tavily `websearch search` calls covering September 30 earnings, same-day wire releases, and SEC 8-K filings. PWCM received four calls: earnings, press releases, SEC material filings, and a corrected issuer-specific PR search after the initial expanded company name was incorrect. Only results for Alpaca-verified PowerCompute were retained. Budgets were respected. **QSI and PWCM: no verified fresh catalyst found; Grade None.** No catalyst is a documented learning-phase concern, not the reason for either skip. Prior primary-source catalyst grades with verified dates/times are carried for LPA and TGE.

- **PWCM — Grade None:** [Earnings announcement](https://www.nasdaq.com/press-release/powercompute-announces-second-quarter-2026-earnings-call-august-14-2026-2026-08-07) schedules Q2 results for **August 14, 2026 at 08:30 ET**, not today. The official [miner-refresh release](https://www.power-compute.com/investors/news-events/press-releases/detail/201/powercompute-miner-refresh-expected-to-deliver-nearly-39) is dated **September 23, 2026**, with approximately 1,000 miners expected by September 30. The earlier [operational update](https://www.power-compute.com/investors/news-events/press-releases/detail/200/powercompute-announces-august-2026-production-and) also forecasts that date. An event calendar listing September 30 as “new miners online” is a scheduled expectation, not a verified fresh completion announcement. The [SEC index](https://www.marketbeat.com/stocks/NASDAQ/PWCM/sec-filings) returns September 23 as latest 8-K. These older items are background; no current-date or preceding-overnight catalyst publication date/time was verified or used for grading.
- **QSI — Grade None:** [Earnings history](https://public.com/stocks/qsi/earnings) and the [Q2 wire release](https://www.globenewswire.com/news-release/2026/08/13/3344917/0/en/quantum-si-reports-second-quarter-2026-financial-results-and-provides-proteus-development-update.html) identify **August 13, 2026** results. Today's PR search returned August/September 9 material, and [SEC searches](https://ir.quantum-si.com/financial-information/sec-filings) returned older material without a verified September 30 event. Carry the prior verified [HUPO interim-data announcement](https://www.quantum-si.com/press-releases/quantum-si-presents-interim-proteus-data-at-world-hupo-2026-demonstrating-a-significant-step-change-in-performance-compared-to-platinum-pro), dated **September 28**, and September 29 filing describing that event as background. No fresh publication date/time is established or used for grading.
- **LPA — Grade D carried:** The verified [September 30 6-K](https://www.sec.gov/Archives/edgar/data/1997711/000199771126000172/latampropertiesoftheameric.htm) was accepted **September 30 at 12:14 ET (16:14Z)**. Its [property-sale closing release](https://www.sec.gov/Archives/edgar/data/1997711/000199771126000172/ex991lpacompletesplssalepr.htm) confirms the $145M Parque Logístico Lima Sur sale to FIBRA Prime. Carry the supplied fixed-price cash asset-purchase exclusion; no fixed per-share takeover price is claimed. Separate wire-publication time remains unverified.
- **TGE — Grade B carried:** [PRNewswire interim results](https://www.prnewswire.com/news-releases/tges-profit-surged-by-9-9-times-with-total-assets-at-us1-8bn-and-net-assets-at-us932m-302894260.html) were published **September 30 at 06:27 ET**; the verified [6-K](https://www.sec.gov/Archives/edgar/data/2053456/000121390026104923/ea0307190-6k_generation.htm) was accepted **05:14:02 ET**. The prior scan read the results: customer-contract revenue +35.8%, EPS $0.12 → $0.56, with total reported revenue declining and the absent prior-year share-based expense aiding the profit comparison. No analyst-consensus beat or new after-close release is claimed.

**Final-scan gate-block instrumentation:** No strict **FINAL-SCAN-GATE-BLOCK** case qualifies. PWCM is the relevant late discovery, but its frozen 16:00 book leaves current fillable liquidity unverified, its current hold after the later timeline retreat is unconfirmed, and CONFIRM-3 is still PENDING on delayed coverage. It is not blocked solely by the two-scan gate. KRMD additionally fails the real-volume/book checks; QSI already has two qualifying scans. These verdicts are recorded for the tracker without changing entry behavior. No fill occurred, so CHASE-CAP does not apply; no pre-entry MULTI-SESSION-RUNNER tag is needed and no first-day claim is inferred. No dead-cat or ceiling override watch is newly established.

**Daily email:** Report no entries, completion of the 38-name SIP cross-check, LPA's FIRST-BAR-SPIKE WATCH hypothetical $3.28 at 18:30, QSI's two-scan qualification with thin recent volume, and PWCM's genuine late 874K-share / 5,313-trade ignition blocked by one appearance and a frozen quote. Include KRMD's omitted but sparse prints, TGE's fading trajectory, and the repeated 16:00/16:59 quote timestamps as the execution-verification limitation. No item from this pulse requires Juan's input.

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
