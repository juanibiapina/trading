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

## Scan 22:00 CEST (4:00 PM ET)

**Decision:** Observe — no candidates found. No paper orders submitted; entries begin at the 23:00 CEST scan (17:00 ET).

`python3 scripts/scan.py --all` ran at 16:00:27 ET (22:00:27 CEST / 20:00:27 UTC), in the AFTERHOURS session, and returned 0 hits. The US trading date is 2026-10-01.

No candidates found.

```text
Supplementary AH-change-only (>15%, not in volume pass): none
AH >10% at this snapshot (unrounded): none
```

### Evaluation notes

**AH appearance count:** This is tonight's first AH scan. No ticker has a scanner-confirmed >10% AH appearance at this snapshot; the 21:30 regular-session appearances do not count toward the two-AH-scan entry gate. No AH candidate requires catalyst research, SIP verification, spike-bar, or CONFIRM-3 instrumentation at this scan.

**Carry forward:** Keep all 28 names from the 21:30 watchlist in tonight's pipeline. The eight recorded broker blocks — EVOL, GBLRF, MHUAF, CRMZ, FNFI, SGRP, LTCEF, EJH — remain untradable (carried). Their absence from this opening scan does not establish an AH fade; no new price or volume evidence was returned. Preserve the pipeline for later scans and the 00:30 CEST final-scan feed-lag cross-check. AH volume verification starts at `2026-10-01T20:00:00Z`.

**Daily email:** No item from this scan requires Juan's input.

## Scan 22:05 CEST (4:05 PM ET)

**Decision:** Observe — no candidates found. No paper orders submitted; entries begin at the 23:00 CEST scan (17:00 ET).

`python3 scripts/scan.py --all` ran at 16:05:25 ET (22:05:25 CEST / 20:05:25 UTC), in the AFTERHOURS session, and returned 0 hits. The US trading date is 2026-10-01. Repository sync completed before scanning.

No candidates found.

```text
  Supplementary AH-change-only (>15%, not in volume pass): none
  AH >10% at this snapshot (unrounded): none
```

### Evaluation notes

**AH appearance count:** Both AH scans so far (22:00 and 22:05 CEST) returned no candidates. No ticker has a scanner-confirmed >10% AH appearance. The 21:30 regular-session appearances do not count toward the two-AH-scan entry gate. There are no AH candidates requiring catalyst research, SIP verification, spike-bar, or CONFIRM-3 instrumentation at this snapshot.

**Carry forward:** Retain all 28 names from the 21:30 watchlist for later scans and the 00:30 CEST final-scan feed-lag cross-check. EVOL, GBLRF, MHUAF, CRMZ, FNFI, SGRP, LTCEF, and EJH remain untradable (carried). This scan supplies no updated price or volume evidence for the watchlist; absence alone does not establish an AH fade. AH volume verification starts at `2026-10-01T20:00:00Z`.

**Daily email:** No item from this scan requires Juan's input.

## Scan 22:10 CEST (4:10 PM ET)

**Decision:** Observe — no candidates found. No paper orders submitted; entries begin at the 23:00 CEST scan (17:00 ET).

`python3 scripts/scan.py --all` ran at 16:10:24 ET (22:10:24 CEST / 20:10:24 UTC), in the AFTERHOURS session, and returned 0 hits. The US trading date is 2026-10-01. Repository sync completed before scanning.

No candidates found.

```text
  Supplementary AH-change-only (>15%, not in volume pass): none
  AH >10% at this snapshot (unrounded): none
```

### Evaluation notes

**AH appearance count:** All three AH scans so far (22:00, 22:05, and 22:10 CEST) returned no candidates. No ticker has a scanner-confirmed >10% AH appearance. The 21:30 regular-session appearances do not count toward the two-AH-scan entry gate. There are no AH candidates requiring catalyst research, SIP verification, spike-bar, or CONFIRM-3 instrumentation at this snapshot.

**Carry forward:** Retain all 28 names from the 21:30 watchlist for later scans and the 00:30 CEST final-scan feed-lag cross-check. EVOL, GBLRF, MHUAF, CRMZ, FNFI, SGRP, LTCEF, and EJH remain untradable (carried). This scan supplies no updated price or volume evidence for the watchlist; absence alone does not establish an AH fade. AH volume verification starts at `2026-10-01T20:00:00Z`.

**Daily email:** No item from this scan requires Juan's input.

## Scan 22:15 CEST (4:15 PM ET)

**Decision:** Observe — no candidates found. No paper orders submitted; entries begin at the 23:00 CEST scan (17:00 ET).

`python3 scripts/scan.py --all` ran at 16:15:29 ET (22:15:29 CEST / 20:15:29 UTC), in the AFTERHOURS session, and returned 0 hits. The US trading date is 2026-10-01. Repository sync completed before scanning.

No candidates found.

```text
  Supplementary AH-change-only (>15%, not in volume pass): none
  AH >10% at this snapshot (unrounded): none
```

### Evaluation notes

**AH appearance count:** All four AH scans so far (22:00, 22:05, 22:10, and 22:15 CEST) returned no candidates. No ticker has a scanner-confirmed >10% AH appearance. The 21:30 regular-session appearances do not count toward the two-AH-scan entry gate. There are no AH candidates requiring catalyst research, SIP verification, spike-bar, or CONFIRM-3 instrumentation at this snapshot.

**Carry forward:** Retain all 28 names from the 21:30 watchlist for later scans and the 00:30 CEST final-scan feed-lag cross-check. EVOL, GBLRF, MHUAF, CRMZ, FNFI, SGRP, LTCEF, and EJH remain untradable (carried). This scan supplies no updated price or volume evidence for the watchlist; absence alone does not establish an AH fade. AH volume verification starts at `2026-10-01T20:00:00Z`.

**Daily email:** No item from this scan requires Juan's input.

## Scan 22:20 CEST (4:20 PM ET)

**Decision:** No entry. WCT is today's first AH candidate, but the entry window has not opened and it has only one qualifying AH appearance. Its Day% is below the dead-cat cutoff, and the verified opening spike is already fading. No paper orders submitted.

`python3 scripts/scan.py --all` ran at 16:20:28 ET (22:20:28 CEST / 20:20:28 UTC), in the AFTERHOURS session, and returned 1 hit. The US trading date is 2026-10-01. Repository sync completed before scanning. Scanner readings below are discovery evidence; SIP and quote checks follow.

```text
  Supplementary AH-change-only (>15%, not in volume pass): none
  AH >10% at this snapshot (unrounded): WCT
```

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| WCT | [TV](https://www.tradingview.com/chart/?symbol=WCT) | $1.67 | -79.4% | +35.3% | $2.26 | -72.1% | 798K | 1.6M | 0.5x | 3.3M | Packaged Software |

### Evaluation notes

**WCT — skip entry; track opening spike.** `broker.js tradable WCT` returned `tradable=true`, active on Nasdaq, before the volume and catalyst workup. Float 3.3M and the software sector are recorded for pattern tracking. WCT was absent from the four previous AH scans; the unrounded scanner line establishes **1 qualifying >10% AH appearance**, not the required 2. Entries begin at 23:00 CEST (17:00 ET).

**SIP volume and price:** `broker.js bars WCT --tf 5Min --start 2026-10-01T20:00:00Z --limit 300` returned consolidated SIP bars:

| Bar start ET | Open | High | Low | Close | Shares | VWAP | Trades |
|--------------|------|------|-----|-------|--------|------|--------|
| 16:00 | $1.67 | $2.34 | $1.67 | $2.26 | 921,567 | $2.14 | 6,344 |
| 16:05 | $2.26 | $2.29 | $2.05 | $2.12 | 798,840 | $2.16 | 5,788 |

The returned AH tape contains **1,720,407 shares / 12,132 trades** across two bars. This is real volume across bars, not a thin drift or stale regular-session volume artifact; the scanner's $2.26 traded within the SIP range. The latest returned bar starts at 16:05 ET, consistent with the free-tier delay at this opening scan. It verifies the early move, not the current price. Volume eased 13.3% between these bars, and the close fell $2.26 → $2.12 after an opening-bar high of $2.34. The latest verified close is 9.4% below that high, but proximity alone does not establish a BUILD/HOLD.

**Trajectory and feed delay:** Yahoo `check-prices.py --ah-history WCT` also shows a descending timeline after the 16:00 bar, continuing through 16:21 ET. Use that result for shape only; its extended-hours volume is unavailable and its exact prices are not entry levels. Its metadata previous close is $8.09, while the completed regular close is $1.67: AH% is measured from $1.67; Day% and Total% use $8.09. The helper's displayed AH changes anchored to $8.09 are not AH appearance evidence. The scanner's $2.26 matches the opening SIP bar close and appears delayed relative to the declining timeline; preserve the snapshot without treating it as a current executable quote.

**Book:** Both `broker.js quote WCT` checks returned `WCT  bid $1.44 x100  ask $0.00 x0  @ 2026-10-01T20:00:01.128879053Z`. The quote is about 20 minutes behind this scan and remained unchanged on retry. **Illiquid (no AH book verified):** there is no non-zero sized ask available from this source, so it cannot support an entry. The stale quote does not negate the confirmed SIP volume or prove that the current market has no liquidity. Recheck the book on a later eligible scan; do not label this a bad print.

**Catalyst Grade: None — no catalyst found.** Four structured searches covered (1) today's earnings, (2) same-day GlobeNewswire/PRNewswire/BusinessWire releases, (3) SEC 8-K/6-K filings, and (4) a Tavily search for same-day earnings, announcements, and filings. No current-trading-date or immediately preceding overnight release with a verified timestamp was found. Results included the [August 31 offering close](https://www.globenewswire.com/news-release/2026/08/31/3353707/0/en/wellchange-holdings-company-limited-announces-closing-of-7-5-million-public-offering-of-its-class-a-ordinary-shares.html), the [September 3 reverse-split announcement, effective September 8](https://www.globenewswire.com/news-release/2026/09/03/3356010/0/en/wellchange-holdings-company-limited-announces-1-for-5-reverse-stock-split-effective-september-8-2026.html), and a [filing index](https://www.stocktitan.net/sec-filings/WCT/) reporting September 3 as its latest filing. These are dated background, not a fresh catalyst; indexed results cannot establish that no newer filing exists. No-catalyst is a documented concern, not an entry skip reason.

**Instrumentation (verbatim; log-only):**

```text
WCT 2026-10-01  SPIKE  16:01ET  +32%  $2.20  1188 trades / 167k sh  (first co-spike bar) (as-of 16:20ET)
WCT 2026-10-01  CONFIRM-3  NO no local-volume new-high ignition as-of 16:20ET
```

**FIRST-BAR-SPIKE WATCH:** hypothetical scanner entry **$2.26 at 22:20 CEST / 16:20 ET**, for morning evaluation only; no fill or position. The observed SIP high $2.34 was in the first AH bar, and CONFIRM-3 is NO on its first evaluation. There is no verified later volume-backed new high. Carry the watch into later scans to check whether the opening high remains the AH high and CONFIRM-3 stays NO. The detector verdicts alone do not determine entry eligibility.

**Other entry gates:** Day -79.4% fails the Day% above -15% requirement. Although the opening move reclaimed above the $1.67 regular close, **DEAD-CAT-OVERRIDE WATCH is not established**: rising AH% across at least two AH scans has not occurred. Total -72.1% is below the +150% ceiling. No chase-cap, final-scan gate-block, or multi-session entry annotation applies because no entry was made and this is an opening scan.

**Carry forward:** Retain WCT plus all 28 regular-session pipeline names for later scans and the 00:30 CEST final-scan feed-lag cross-check. EVOL, GBLRF, MHUAF, CRMZ, FNFI, SGRP, LTCEF, and EJH remain untradable (carried); no repeat workup was performed on them. Their absence supplies no new trajectory evidence. AH volume verification starts at `2026-10-01T20:00:00Z`.

**Daily email:** Report WCT's real opening volume, fading trajectory, stale zero-ask quote, and FIRST-BAR-SPIKE WATCH hypothetical. No item from this scan requires Juan's input.

## Scan 22:25 CEST (4:25 PM ET)

**Decision:** Observe — no paper orders submitted. Entries begin at the 23:00 CEST scan (17:00 ET). SORA and SSM each have their first qualifying >10% AH appearance; WCT now has two, but fails the Day% rule and continues to fade.

`python3 scripts/scan.py --all` ran at 16:25:28 ET (22:25:28 CEST / 20:25:28 UTC), in the AFTERHOURS session, and returned 5 hits after repository sync. The US trading date is 2026-10-01. Scanner prices and volumes are discovery readings; the verification below distinguishes delayed readings from current executable levels.

```text
  Supplementary AH-change-only (>15%, not in volume pass): none
  AH >10% at this snapshot (unrounded): SORA, SSM, WCT
```

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| SSM | [TV](https://www.tradingview.com/chart/?symbol=SSM) | $2.21 | +97.3% | +10.4% | $2.44 | +117.8% | 2.6M | 8.0M | 0.3x | 1.1M | Motor Vehicles |
| WCT | [TV](https://www.tradingview.com/chart/?symbol=WCT) | $1.67 | -79.4% | +25.8% | $2.10 | -74.0% | 1.5M | 1.6M | 0.9x | 3.3M | Packaged Software |
| SORA | [TV](https://www.tradingview.com/chart/?symbol=SORA) | $2.40 | +4.3% | +22.1% | $2.93 | +27.3% | 257K | 46K | 5.5x | 4.9M | Wholesale Distributors |
| MVST | [TV](https://www.tradingview.com/chart/?symbol=MVST) | $0.66 | +3.2% | +6.0% | $0.70 | +9.4% | 76K | 5.7M | 0.0x | 210.1M | Electrical Products |
| AGIG | [TV](https://www.tradingview.com/chart/?symbol=AGIG) | $0.96 | -11.6% | +5.9% | $1.02 | -6.4% | 63K | 139K | 0.5x | 11.9M | Oil & Gas Production |

### Evaluation notes

**Broker availability:** SORA, MVST, and AGIG returned `tradable=true` before further workup. SSM's 21:30 and WCT's 22:20 `tradable=true` checks are carried forward. Float and sector are tracked; MVST's 210.1M float does not independently disqualify it in the learning phase.

**AH appearance counts:** WCT **2** (22:20, 22:25); SORA **1** (22:25); SSM **1** (22:25); MVST and AGIG **0**. These counts use the scanner's unrounded >10% lists. SSM's regular-session appearance adds no AH count. All scanner Total% values are below +150%; no ceiling override applies.

**SIP verification:** `broker.js bars SYM --tf 5Min --start 2026-10-01T20:00:00Z --limit 300` returned consolidated SIP for all three >10% candidates. The newest returned bars start at 16:10 ET, consistent with approximately 15 minutes of free-tier delay at this snapshot. They verify the opening tape, not the latest scan-minute price.

| Ticker | Bar start ET | Open | High | Low | Close | Shares | VWAP | Trades |
|--------|--------------|------|------|-----|-------|--------|------|--------|
| SORA | 16:05 | $2.43 | $3.64 | $2.42 | $2.93 | 369,642 | $3.10 | 5,208 |
| SORA | 16:10 | $2.93 | $3.30 | $2.91 | $3.27 | 599,575 | $3.18 | 6,817 |
| SSM | 16:00 | $2.21 | $2.32 | $2.07 | $2.10 | 1,165,872 | $2.15 | 6,195 |
| SSM | 16:05 | $2.10 | $2.49 | $2.07 | $2.44 | 1,695,858 | $2.33 | 9,312 |
| SSM | 16:10 | $2.44 | $2.44 | $2.21 | $2.27 | 780,544 | $2.31 | 4,733 |
| WCT | 16:00 | $1.67 | $2.34 | $1.67 | $2.26 | 921,567 | $2.14 | 6,344 |
| WCT | 16:05 | $2.26 | $2.29 | $2.05 | $2.12 | 798,840 | $2.16 | 5,788 |
| WCT | 16:10 | $2.10 | $2.10 | $1.82 | $1.84 | 496,570 | $1.94 | 3,277 |

**SORA — watch recovery; current liquidity unconfirmed.** SIP totals **969,217 shares / 12,025 trades**. The scanner's $2.93 is corroborated by the 16:05 bar. The next bar closes higher at $3.27 with higher volume and VWAP; this is real accumulation across the available bars. That close is 10.2% below the observed $3.64 opening high at 16:05. Yahoo's timeline continues to recover after the initial spike through 16:20, then pulls back; use it for shape only, not exact highs, volume, or entry levels. A sustained BUILD/HOLD and any later new high still require subsequent SIP confirmation.

**SORA catalyst — Grade C, fresh exploratory agreement.** Four structured searches covered today's earnings, same-day newswire releases, SEC 8-K/6-K filings, and a Tavily follow-up. No same-day earnings or material filing was verified. The [GlobeNewswire release](https://www.globenewswire.com/news-release/2026/10/01/3373374/0/en/asiastrategy-signs-memorandum-of-understanding-with-plume-network-to-advance-real-world-asset-tokenisation-across-asia.html), verified from its full text, is dated **October 1, 2026, 16:05 ET / 22:05 CEST**. AsiaStrategy signed a **non-binding** memorandum with Plume to explore a tokenised-financial-products joint venture. Definitive documents, approvals, and regulatory requirements remain outstanding; no product has launched. Grade C reflects the exploratory framework rather than a completed major operational deal. The direct page request timed out; primary-release extraction supplied the date, time, and terms.

**SORA book:** Both checks returned `SORA  bid $1.93 x100  ask $2.78 x100  @ 2026-10-01T20:00:00.60007104Z`. Sizes are non-zero, but the quote is already 25 minutes behind the snapshot and unchanged on retry. Current fillable liquidity is **unconfirmed**. The delayed quote does not refute the SIP move; no bad-print rejection is warranted. Recheck at a later eligible scan.

**SSM — opening spike followed by decline.** SIP totals **3,642,274 shares / 20,240 trades**; the scanner's $2.44 genuinely traded in the 16:05 bar. Volume then falls 54.0% and the close declines to $2.27. The fresh book returned `SSM  bid $2.06 x100  ask $2.11 x100  @ 2026-10-01T20:23:53.425627497Z`. Its ask is 4.5% below the $2.21 regular close and 15.3% below the observed $2.49 AH high; this current book and Yahoo's descending timeline corroborate a fade. The +10.4% scanner snapshot is delayed relative to the fresh quote. Retain its appearance count, but do not treat the scanner price as current momentum. Proximity within 20% of the high does not make a declining trajectory a HOLD.

**SSM catalyst — Grade None; no fully verified fresh catalyst found.** Four structured searches covered earnings, newswire releases, same-day material filings, and a Tavily follow-up. The [filing/news index](https://www.stocktitan.net/overview/SSM/) mentions an **October 1 Schedule 13D** concerning about $371K of Alpine Fox share purchases with no present control plans. The filing's acceptance time and underlying transaction dates were not verified, so it is an unresolved possible driver and is not used to assign a catalyst grade. The Sports One reverse-merger LOI is dated August 31 and remains background. No-catalyst is a concern, not an entry skip reason.

**WCT — skip; Day% failure and continuing fade.** Scanner AH% falls **+35.3% → +25.8%**, scanner price **$2.26 → $2.10**, while displayed AH volume rises **798K → 1.5M**. SIP now totals **2,216,977 shares / 15,409 trades**, up 496,570 shares and 3,277 trades from the previous verification. Real volume continues, but per-bar volume, VWAP, and closes decline; the newest verified close $1.84 is **21.4% below** the $2.34 opening high. Yahoo's later timeline also declines. This is SPIKE→FADE. Day **-79.4%** independently fails the entry rule. AH% is falling across its two appearances, so no DEAD-CAT-OVERRIDE WATCH is established. Grade None from the preceding four-search workup is carried forward; WCT was not skipped for lack of a catalyst.

**WCT book:** Both checks returned `WCT  bid $1.44 x100  ask $0.00 x0  @ 2026-10-01T20:00:01.128879053Z`, unchanged from 22:20. **Illiquid (no current AH book verified):** no sized ask is available from this source. The quote is stale and cannot prove that the present consolidated market has no liquidity; it also cannot support an order. The scanner's $2.10 is corroborated by historical SIP trades, so this is not a verified bad print.

**Instrumentation (verbatim):** Spike-bar and CONFIRM-3 outputs are recorded for learning. Their standalone verdicts do not grade or rank entries; the separate first-bar-spike rule uses the opening-high trajectory evidence.

```text
SORA 2026-10-01  SPIKE  16:06ET  +52%  $3.64  243 trades / 17k sh  (first co-spike bar) (as-of 16:25ET)
SORA 2026-10-01  CONFIRM-3  NO no local-volume new-high ignition as-of 16:25ET
SSM 2026-10-01  NO-SPIKE  peak +13% @16:09ET  (no bar cleared +15% on a volume co-spike) (as-of 16:25ET)
SSM 2026-10-01  CONFIRM-3  NO no local-volume new-high ignition as-of 16:25ET
WCT 2026-10-01  SPIKE  16:01ET  +32%  $2.20  1188 trades / 167k sh  (first co-spike bar) (as-of 16:25ET)
WCT 2026-10-01  CONFIRM-3  NO no local-volume new-high ignition as-of 16:25ET
```

**FIRST-BAR-SPIKE WATCH:** All observed SIP highs are in the 16:00–16:15 opening window, with CONFIRM-3 NO in every evaluation available so far. Record hypothetical scanner entries for morning measurement: **SORA $2.93 at 22:25 CEST / 16:25 ET**, **SSM $2.44 at 22:25 CEST / 16:25 ET**, and **WCT $2.10 at 22:25 CEST / 16:25 ET**. WCT's original **$2.26 at 22:20 CEST / 16:20 ET** watch remains recorded above. These are hypothetical observations, not fills or executable quotes. SORA's watch is provisional while its recovering timeline awaits later SIP: revisit the opening-high condition if a later volume-backed new high appears. SSM and WCT currently show opening-spike fades. If the opening highs persist and CONFIRM-3 remains NO at entry time, apply the first-bar-spike skip.

**MVST and AGIG — watch below entry threshold.** This is each name's first AH discovery. AH +6.0% and +5.9% supply no >10% appearance. Day% exceeds -15% for both; sector and float are recorded without independent exclusions. No qualifying momentum or real AH liquidity is established by their scanner readings. Catalyst and detector workups are not required below the >10% threshold.

**Carry forward:** Retain the 28 regular-session names plus WCT, SORA, MVST, and AGIG in tonight's pipeline (32 unique names; SSM was already on the regular watchlist). EVOL, GBLRF, MHUAF, CRMZ, FNFI, SGRP, LTCEF, and EJH remain untradable (carried). Preserve all pipeline names for the 00:30 CEST final-scan feed-lag cross-check. Yahoo volume was not used; Yahoo AH% anchored to the previous day's close was not used for appearance counts. No fills occurred, so there is no new OPEN_POSITIONS entry, chase-cap, or multi-session entry annotation. Final-scan gate-block instrumentation is not due at this scan.

**Daily email:** Report SORA's 16:05 ET non-binding Plume catalyst and recovery with stale liquidity verification, SSM's delayed scanner gain versus fresh below-close book, WCT's continued fade and Day% failure, and the hypothetical FIRST-BAR-SPIKE WATCH entries. No item from this scan requires Juan's input.

## Scan 22:30 CEST (4:30 PM ET)

**Decision:** Observe — no paper orders submitted. This snapshot precedes the 23:00 CEST entry window. SORA now has two qualifying >10% AH appearances, but its opening-high watch persists and its current book remains unverified. New candidate AMOD has one qualifying appearance and fails the Day% rule.

`python3 scripts/scan.py --all` ran at 16:30:40 ET (22:30:40 CEST / 20:30:40 UTC), in the AFTERHOURS session, and returned 5 hits after repository sync. The US trading date is 2026-10-01. Verification ran after the snapshot; detector cutoffs preserve the 16:30 ET scan minute.

```text
  Supplementary AH-change-only (>15%, not in volume pass): none
  AH >10% at this snapshot (unrounded): AMOD, SORA
```

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| WCT | [TV](https://www.tradingview.com/chart/?symbol=WCT) | $1.67 | -79.4% | +7.8% | $1.80 | -77.8% | 1.9M | 1.7M | 1.1x | 3.3M | Packaged Software |
| SORA | [TV](https://www.tradingview.com/chart/?symbol=SORA) | $2.40 | +4.3% | +34.6% | $3.23 | +40.4% | 766K | 113K | 6.8x | 4.9M | Wholesale Distributors |
| MVST | [TV](https://www.tradingview.com/chart/?symbol=MVST) | $0.66 | +3.2% | +6.0% | $0.70 | +9.4% | 76K | 5.7M | 0.0x | 210.1M | Electrical Products |
| AGIG | [TV](https://www.tradingview.com/chart/?symbol=AGIG) | $0.96 | -11.6% | +5.9% | $1.02 | -6.4% | 63K | 139K | 0.5x | 11.9M | Oil & Gas Production |
| AMOD | [TV](https://www.tradingview.com/chart/?symbol=AMOD) | $1.17 | -24.5% | +10.1% | $1.29 | -16.9% | 61K | 167K | 0.4x | 543K | Packaged Software |

### Evaluation notes

**Broker and appearance counts:** AMOD returned `tradable=true`, active on Nasdaq, before its SIP/catalyst workup. Prior `tradable=true` checks for SORA, WCT, SSM, MVST, and AGIG carry forward. The unrounded scanner lists now establish **SORA 2** (22:25, 22:30), **WCT 2** (22:20, 22:25), **SSM 1** (22:25), **AMOD 1** (22:30), and **MVST/AGIG 0**. WCT's current +7.8% adds no appearance; SSM is absent and adds none. Regular-session appearances do not count. Float and sector remain pattern observations, not independent learning-phase exclusions.

**SIP verification:** `broker.js bars SYM --tf 5Min --start 2026-10-01T20:00:00Z --limit 300` returned consolidated SIP. The newest returned bar for each checked name starts at 16:15 ET, consistent with the free-tier delay around 16:30. These bars verify the tape through the available opening window, not the current scan-minute level.

| Ticker | Bar start ET | Open | High | Low | Close | Shares | VWAP | Trades |
|--------|--------------|------|------|-----|-------|--------|------|--------|
| SORA | 16:05 | $2.43 | $3.64 | $2.42 | $2.93 | 369,642 | $3.10 | 5,208 |
| SORA | 16:10 | $2.93 | $3.30 | $2.91 | $3.27 | 599,575 | $3.18 | 6,817 |
| SORA | 16:15 | $3.25 | $3.30 | $2.95 | $3.15 | 511,111 | $3.13 | 6,149 |
| AMOD | 16:00 | $1.17 | $1.17 | $1.17 | $1.17 | 546 | $1.17 | 4 |
| AMOD | 16:05 | $1.19 | $1.19 | $1.14 | $1.14 | 688 | $1.16 | 4 |
| AMOD | 16:10 | $1.18 | $1.29 | $1.18 | $1.28 | 40,155 | $1.23 | 192 |
| AMOD | 16:15 | $1.26 | $1.55 | $1.26 | $1.34 | 951,981 | $1.39 | 5,009 |
| WCT | 16:15 | $1.83 | $1.85 | $1.70 | $1.76 | 254,831 | $1.77 | 1,688 |
| SSM | 16:15 | $2.26 | $2.26 | $2.08 | $2.15 | 564,563 | $2.15 | 3,518 |

**SORA — watch recovery; FIRST-BAR-SPIKE WATCH persists.** Scanner AH% rises **+22.1% → +34.6%**, price **$2.93 → $3.23**, Total% **+27.3% → +40.4%**, and AH volume **257K → 766K**. SIP totals **1,480,328 shares / 18,174 trades**, adding **511,111 shares / 6,149 trades** since 22:25. Volume remains substantial across bars; the latest bar is 14.8% lighter than its predecessor, with close $3.27 → $3.15 and VWAP $3.18 → $3.13. The scanner's $3.23 is within verified SIP ranges, so there is no bad-print rejection. The observed high remains **$3.64 in the 16:05 bar**; the latest verified close is **13.5% below** it. Yahoo's later timeline shows recovery and pullbacks rather than a monotonic fade, but cannot establish an exact high or real volume. Treat this as a hold attempt after an opening spike; a later volume-backed new high is still unverified.

**SORA catalyst and book:** Carry **Grade C** from the verified [GlobeNewswire release](https://www.globenewswire.com/news-release/2026/10/01/3373374/0/en/asiastrategy-signs-memorandum-of-understanding-with-plume-network-to-advance-real-world-asset-tokenisation-across-asia.html), **October 1, 2026, 16:05 ET / 22:05 CEST**: a non-binding memorandum with Plume to explore a tokenised-products joint venture. No new search is needed to reuse this dated, verified catalyst. Quote checks and a SIP re-pull remained unchanged: `SORA  bid $1.93 x100  ask $2.78 x100  @ 2026-10-01T20:00:00.60007104Z`. This sized quote is about 30 minutes behind the scan; it does not confirm a current fillable book or contradict the subsequent SIP move. Recheck at a later eligible scan. **FIRST-BAR-SPIKE WATCH hypothetical: $3.23 at 22:30 CEST / 16:30 ET**, using the scanner snapshot for measurement only. The opening-window high and CONFIRM-3 NO persist across both evaluations; apply the first-bar-spike skip at entry time if those conditions remain. Revisit the opening-high condition when later SIP bars arrive.

**AMOD — skip entry; Day% failure, late opening-volume ignition.** This is its first discovery tonight. Day **-24.5%** fails the requirement to exceed -15%; one qualifying appearance also falls short of two. Total **-16.9%** is below the extension ceiling. SIP totals **993,370 shares / 5,209 trades**, with a sharp increase from 40,155 shares / 192 trades at 16:10 to **951,981 shares / 5,009 trades at 16:15**. The scanner's $1.29 genuinely traded; the next available bar reaches $1.55 with VWAP $1.39. This is a real volume ignition after initially sparse bars, not a stale-VRatio or thin-drift rejection. Sustained accumulation after the ignition awaits later bars. The observed high is in the **16:15–16:20 bar**, after the 16:00–16:15 opening window; CONFIRM-3 is PENDING, so no first-bar-spike watch is assigned. No DEAD-CAT-OVERRIDE WATCH is established yet: AH% has not risen across at least two AH scans.

**AMOD catalyst — Grade D, fresh PIPE-closing disclosure.** Four structured searches covered today's earnings, same-day newswire releases, SEC 8-K filings, and a Tavily follow-up. No same-day earnings or newswire release was verified. The fourth search found an October 1 8-K; the indexed article returned HTTP 403, but the [primary SEC filing](https://www.sec.gov/Archives/edgar/data/1862463/000149315226045296/form8-k.htm) and [EDGAR filing index](https://www.sec.gov/Archives/edgar/data/1862463/000149315226045296/0001493152-26-045296-index.html) were retrieved and checked. The index records **filing date October 1, 2026; accepted 11:30:52 (EDGAR displayed time)**. This is a fresh disclosure today of the September 30 closing of a previously announced PIPE: **51,621,560 common shares plus warrants for 51,621,560 additional shares at $4.36**, in exchange for **3,170 bitcoin**. The company also reports restored Nasdaq equity compliance, subject to continued monitoring. Grade D reflects the share issuance and warrant dilution; no acquisition-momentum grade is assigned. The scanner's **543K float may be stale** after the issuance; the current freely tradable float is unverified, and issued shares do not by themselves establish float.

**AMOD book:** Two checks returned `AMOD  bid $1.40 x100  ask $1.43 x100  @ 2026-10-01T20:31:25.495099643Z`, fresh at verification time 16:31:30 ET. A real two-sided sized book is available after the snapshot. It corroborates the move rather than the delayed scanner's exact current price. No sizing or order was attempted because the time, appearance-count, and Day% gates fail.

**Instrumentation (verbatim; log-only):** Neither standalone detector verdict changes entry grading or ranking.

```text
SORA 2026-10-01  SPIKE  16:06ET  +52%  $3.64  243 trades / 17k sh  (first co-spike bar) (as-of 16:30ET)
SORA 2026-10-01  CONFIRM-3  NO no local-volume new-high ignition as-of 16:30ET
AMOD 2026-10-01  SPIKE  16:15ET  +15%  $1.35  366 trades / 64k sh  (first co-spike bar) (as-of 16:30ET)
AMOD 2026-10-01  CONFIRM-3  PENDING ignition 16:15ET; waiting for third bar as-of 16:30ET
```

**WCT — skip; Day% failure and continued SPIKE→FADE.** Scanner AH% falls **+35.3% → +25.8% → +7.8%**, and price **$2.26 → $2.10 → $1.80**, even as displayed AH volume rises **798K → 1.5M → 1.9M**. SIP totals **2,471,808 shares / 17,097 trades**; the newest bar adds 254,831 shares / 1,688 trades, with volume down 48.7% and close $1.84 → $1.76. That close is **24.8% below** the $2.34 opening high. Yahoo's later descending shape supports the fade; its exact levels and volume were not used. The quote remains stale: `WCT  bid $1.44 x100  ask $0.00 x0  @ 2026-10-01T20:00:01.128879053Z`; no current fillable ask is verified. Grade None and the prior FIRST-BAR-SPIKE WATCH hypotheticals carry forward. There is no rising-AH% dead-cat override. WCT is below the instrumentation threshold in this snapshot.

**SSM — absent from discovery; fade remains verified.** No additional >10% appearance is counted. SIP totals **4,206,837 shares / 23,758 trades**, adding 564,563 shares / 3,518 trades at 16:15. Its closes fall **$2.44 → $2.27 → $2.15**, with per-bar volume down 27.7% in the latest bar. The high remains $2.49 at 16:05; the latest close is 13.7% below it and below the $2.21 regular close. Quote: `SSM  bid $2.06 x100  ask $2.11 x100  @ 2026-10-01T20:23:53.425627497Z`, about seven minutes old at this scan. Yahoo's later shape stays below the completed regular close. Preserve Grade None, the unresolved Schedule 13D driver, and the prior opening-spike hypothetical; absence alone is not the fade evidence.

**MVST and AGIG — watch below entry threshold.** Scanner prices, AH%, and displayed volumes are unchanged from 22:25. AH +6.0% and +5.9% supply no qualifying appearance. No real AH accumulation or fillable liquidity is established by these readings alone; float and industry remain observations.

**Carry forward and fills:** Retain **33 unique pipeline names**: the 28 regular-session names plus WCT, SORA, MVST, AGIG, and AMOD; SSM was already in the regular watchlist. EVOL, GBLRF, MHUAF, CRMZ, FNFI, SGRP, LTCEF, and EJH remain untradable (carried), with no repeated workup. Preserve the pipeline for the 00:30 CEST final-scan cross-check. Alpaca reports **no open orders and no open positions**. There is no fill to add to OPEN_POSITIONS, chase-cap note, or multi-session entry annotation; final-scan gate-block instrumentation is not due. Yahoo's previous-day-close percentages and volume were not used for AH appearance counts or liquidity decisions.

**Daily email:** Report SORA's second qualifying appearance, substantial SIP volume, persistent opening-high watch and stale book; AMOD's real ignition, fresh Grade D dilution disclosure and Day% block; and WCT/SSM's fading opening spikes. No item from this scan requires Juan's input.

## Scan 22:45 CEST (4:45 PM ET)

**Decision:** No entry. This snapshot precedes the 23:00 CEST entry window. SORA retains its opening-spike skip; AMOD fails the Day% rule despite its volume-backed recovery. Record both hypothetical watches for morning evaluation. No paper orders submitted.

`python3 scripts/scan.py --all` ran at **16:45:28 ET / 22:45:28 CEST / 20:45:28 UTC**, in the AFTERHOURS session, after `bash scripts/sync-repo.sh` reported the repository up to date. The US trading date is **2026-10-01**. Verification ran at approximately 16:45–16:46 ET; detector cutoffs preserve the 16:45 ET scan minute. The table preserves the scanner snapshot, including its delayed discovery readings.

```text
  Supplementary AH-change-only (>15%, not in volume pass): none
  AH >10% at this snapshot (unrounded): AMOD, SORA
```

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| SCKT | [TV](https://www.tradingview.com/chart/?symbol=SCKT) | $0.54 | +21.0% | +7.4% | $0.58 | +29.9% | 6.9M | 12.6M | 0.5x | 5.7M | Computer Peripherals |
| SORA | [TV](https://www.tradingview.com/chart/?symbol=SORA) | $2.40 | +4.3% | +34.2% | $3.22 | +39.9% | 2.0M | 281K | 7.3x | 4.9M | Wholesale Distributors |
| AMOD | [TV](https://www.tradingview.com/chart/?symbol=AMOD) | $1.17 | -24.5% | +16.8% | $1.37 | -11.8% | 1.7M | 352K | 4.9x | 543K | Packaged Software |
| MVST | [TV](https://www.tradingview.com/chart/?symbol=MVST) | $0.66 | +3.2% | +6.0% | $0.70 | +9.4% | 77K | 5.7M | 0.0x | 210.1M | Electrical Products |
| AGIG | [TV](https://www.tradingview.com/chart/?symbol=AGIG) | $0.96 | -11.6% | +5.1% | $1.01 | -7.1% | 64K | 139K | 0.5x | 11.9M | Oil & Gas Production |

### Evaluation notes

**Broker availability and AH counts:** New candidate SCKT returned `tradable=true`, active on Nasdaq, before further workup. Prior positive tradability checks carry forward for SORA, AMOD, MVST, AGIG, WCT, and SSM. The unrounded scanner lines now establish **SORA 3** (22:25, 22:30, 22:45), **AMOD 2** (22:30, 22:45), **WCT 2** (22:20, 22:25), **SSM 1** (22:25), and **SCKT/MVST/AGIG 0**. WCT and SSM are absent at this snapshot and add no appearance. Regular-session appearances add no AH count. All five displayed Total% values are below +150%; float and sector remain pattern observations, not independent learning-phase exclusions.

**SIP verification:** `broker.js bars SYM --tf 5Min --start 2026-10-01T20:00:00Z --limit 300` returned consolidated SIP for SORA and AMOD. Each newest returned bar starts at **16:30 ET**, approximately 15 minutes behind the scan, consistent with the free-tier delay. The following bars extend the preceding scan's verification:

| Ticker | Bar start ET | Open | High | Low | Close | Shares | VWAP | Trades |
|--------|--------------|------|------|-----|-------|--------|------|--------|
| SORA | 16:20 | $3.17 | $3.48 | $2.95 | $3.40 | 673,956 | $3.29 | 7,207 |
| SORA | 16:25 | $3.38 | $3.55 | $3.15 | $3.20 | 554,531 | $3.31 | 6,513 |
| SORA | 16:30 | $3.22 | $3.33 | $3.00 | $3.08 | 424,861 | $3.14 | 4,933 |
| AMOD | 16:20 | $1.34 | $1.44 | $1.30 | $1.39 | 557,517 | $1.37 | 2,952 |
| AMOD | 16:25 | $1.38 | $1.44 | $1.33 | $1.37 | 360,155 | $1.39 | 1,890 |
| AMOD | 16:30 | $1.37 | $1.50 | $1.35 | $1.44 | 467,778 | $1.45 | 2,755 |

**SORA — skip opening spike; recent recovery is fading.** Scanner AH% has moved **+22.1% → +34.6% → +34.2%**, with prices **$2.93 → $3.23 → $3.22**. Displayed AH volume increases **766K → 2.0M**, and VRatio **6.8x → 7.3x** since 22:30. SIP totals **3,133,676 shares / 36,827 trades**, adding **1,653,348 shares / 18,653 trades** since the previous verification. This is real accumulation across bars, and $3.22 is corroborated by the SIP ranges. The opening high remains **$3.64 in the 16:05 bar**; the later recovery reached only $3.55 at 16:25. Recent closes decline **$3.40 → $3.20 → $3.08**, with the last close **15.4% below** the AH high. Volume declines across those three bars, most recently **23.4%**, and VWAP falls $3.31 → $3.14. Yahoo's later timeline also shows the recovery easing, with small rebounds; only its shape is used. Its displayed high and previous-day-close percentages are not SIP highs or AH appearance evidence.

**SORA FIRST-BAR-SPIKE WATCH:** The AH high remains in the 16:00–16:15 ET opening window, with CONFIRM-3 **NO in all three evaluations**. Apply the opening-spike entry skip even though price remains within 20% of that high. Record hypothetical scanner entry **$3.22 at 22:45 CEST / 16:45 ET**, Total **+39.9%**, for morning measurement; this is not a fill. Earlier hypotheticals remain in their original scan sections. Revisit the opening-high condition if subsequent SIP establishes a later volume-backed new high.

**SORA catalyst and book:** Carry **Grade C** from the verified [GlobeNewswire release](https://www.globenewswire.com/news-release/2026/10/01/3373374/0/en/asiastrategy-signs-memorandum-of-understanding-with-plume-network-to-advance-real-world-asset-tokenisation-across-asia.html), dated **October 1, 2026, 16:05 ET / 22:05 CEST**: the non-binding Plume memorandum to explore a tokenised-products joint venture. Its dated terms were verified in the 22:25 workup; no fresh catalyst search is needed to carry this grade. Both quote checks returned `SORA  bid $1.93 x100  ask $2.78 x100  @ 2026-10-01T20:00:00.60007104Z`. The unchanged quote is about **45 minutes old**, so current fillable liquidity is **unconfirmed** despite non-zero sizes. This stale book does not contradict the later consolidated trades, and no bad-print rejection is assigned. Recheck on the next eligible scan.

**AMOD — skip live entry; DEAD-CAT-OVERRIDE WATCH.** Scanner AH% rises **+10.1% → +16.8%**, price **$1.29 → $1.37**, Total% **-16.9% → -11.8%**, and displayed AH volume **61K → 1.7M**. It now meets the two-AH-appearance requirement, but Day **-24.5%** fails the requirement to exceed -15%. SIP totals **2,378,820 shares / 12,806 trades**, adding **1,385,450 shares / 7,597 trades** since 22:30. Real trading continues after the 16:15 ignition; the last bar's volume increases **29.9%**, trades increase 1,890 → 2,755, close rises $1.37 → $1.44, and VWAP rises $1.39 → $1.45. This is a volume-backed recovery above the **$1.17 completed regular close**, with rising scanner AH% across two scans. Flag **DEAD-CAT-OVERRIDE WATCH**, hypothetical scanner entry **$1.37 at 22:45 CEST / 16:45 ET**, Total **-11.8%**. The Day% block stays in place; no live entry is made.

**AMOD trajectory, catalyst, and book:** The observed high remains **$1.55 in the 16:15–16:20 bar**, after the opening window. The last verified close is **7.1% below** that high; no new high is established. CONFIRM-3 is now NO, which is recorded as instrumentation and supplies no independent skip or grade. Carry **Grade D** from the [October 1 SEC 8-K](https://www.sec.gov/Archives/edgar/data/1862463/000149315226045296/form8-k.htm), accepted **11:30:52 on October 1, 2026 (EDGAR displayed time)** in the [filing index](https://www.sec.gov/Archives/edgar/data/1862463/000149315226045296/0001493152-26-045296-index.html). The prior workup verified today's disclosure of the September 30 PIPE closing: 51,621,560 shares plus warrants for the same number, in exchange for 3,170 bitcoin. The scanner's **543K float may be stale** after that issuance; current freely tradable float remains unverified. Quote: `AMOD  bid $1.42 x100  ask $1.45 x100  @ 2026-10-01T20:45:54.398088725Z`, fresh at verification with a sized two-sided book. The scanner's $1.37 is corroborated by SIP, while its current level is delayed relative to the book. Yahoo's later shape supports the recovery; its previous-close anchor $1.55 is distinct from the completed regular close $1.17, and its extended-hours volume and exact levels were not used.

**Instrumentation (verbatim; log-only):** Standalone spike-bar and CONFIRM-3 verdicts do not rank or grade candidates. The separate first-bar-spike rule above uses the opening-high trajectory and repeated NO condition.

```text
SORA 2026-10-01  SPIKE  16:06ET  +52%  $3.64  243 trades / 17k sh  (first co-spike bar) (as-of 16:45ET)
SORA 2026-10-01  CONFIRM-3  NO no local-volume new-high ignition as-of 16:45ET
AMOD 2026-10-01  SPIKE  16:15ET  +15%  $1.35  366 trades / 64k sh  (first co-spike bar) (as-of 16:45ET)
AMOD 2026-10-01  CONFIRM-3  NO ignition 16:15ET failed third-bar hold/volume as-of 16:45ET
```

**SCKT — new watch below threshold.** AH **+7.4%** supplies no qualifying >10% appearance. Day +21.0%, float 5.7M, and Computer Peripherals are recorded for pattern tracking. The scanner's 6.9M AH volume / 0.5x VRatio is discovery evidence only; real AH accumulation and executable liquidity have not been verified. Catalyst and detector workups are not required below the >10% threshold.

**MVST and AGIG — remain below threshold.** MVST remains at AH +6.0% / $0.70; displayed volume edges 76K → 77K. AGIG eases from AH +5.9% / $1.02 to **+5.1% / $1.01**, while displayed volume edges 63K → 64K. Neither supplies a qualifying appearance or confirmed entry liquidity. Float and sector remain observations.

**WCT and SSM — absent from this discovery snapshot.** Their earlier Day%/fade and opening-spike blocks carry forward; no additional tape verification was performed on them in this scan. Absence alone supplies no fresh trajectory conclusion. Preserve both names and their earlier hypothetical watches for later scans and the final cross-check.

**Carry forward and fills:** Tonight's pipeline now contains **34 unique names**: the 28 regular-session names plus WCT, SORA, MVST, AGIG, AMOD, and SCKT. EVOL, GBLRF, MHUAF, CRMZ, FNFI, SGRP, LTCEF, and EJH remain **untradable (carried)**, without repeated SIP or catalyst workups. Preserve the pipeline for the **00:30 CEST / 18:30 ET final-scan feed-lag cross-check**. Alpaca `positions --json` returned `[]`, and `orders open` returned `No open orders.` No fills require an OPEN_POSITIONS entry. Chase-cap and multi-session entry instrumentation do not apply without an entry; final-scan gate-block instrumentation is not due at this scan.

**Daily email:** Include SORA's persistent FIRST-BAR-SPIKE WATCH, declining recovery and stale quote; AMOD's DEAD-CAT-OVERRIDE WATCH hypothetical, real volume, Grade D dilution disclosure and Day% block; and SCKT's below-threshold discovery. No item requires Juan's input.

## Scan 23:00 CEST (5:00 PM ET)

**Decision:** Skip all entries at this snapshot. The entry window is now open, but SORA remains an opening-bar spike without a later verified volume-backed new high, and AMOD fails the Day% rule. SCKT and MVST remain below the >10% AH threshold. No paper orders submitted.

`python3 scripts/scan.py --all` ran at **17:00:24 ET / 23:00:24 CEST / 21:00:24 UTC**, in the AFTERHOURS session, after `bash scripts/sync-repo.sh` reported the repository up to date. The US trading date is **2026-10-01**. Broker verification followed the snapshot; detector cutoffs preserve the **17:00 ET** scan minute. The table preserves scanner discovery readings.

```text
  Supplementary AH-change-only (>15%, not in volume pass): none
  AH >10% at this snapshot (unrounded): AMOD, SORA
```

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| SCKT | [TV](https://www.tradingview.com/chart/?symbol=SCKT) | $0.54 | +21.0% | +7.4% | $0.58 | +30.0% | 9.9M | 12.9M | 0.8x | 5.7M | Computer Peripherals |
| AMOD | [TV](https://www.tradingview.com/chart/?symbol=AMOD) | $1.17 | -24.5% | +20.4% | $1.41 | -9.1% | 3.3M | 528K | 6.2x | 543K | Packaged Software |
| SORA | [TV](https://www.tradingview.com/chart/?symbol=SORA) | $2.40 | +4.3% | +26.7% | $3.04 | +32.1% | 2.6M | 357K | 7.3x | 4.9M | Wholesale Distributors |
| MVST | [TV](https://www.tradingview.com/chart/?symbol=MVST) | $0.66 | +3.2% | +6.0% | $0.70 | +9.4% | 80K | 5.8M | 0.0x | 210.1M | Electrical Products |

### Evaluation notes

**Tradability and AH appearance counts:** Prior `tradable=true` checks carry forward for all four scanner names; there is no new candidate requiring an initial broker check or catalyst search. The unrounded scanner lists establish **SORA 4** (22:25, 22:30, 22:45, 23:00), **AMOD 3** (22:30, 22:45, 23:00), **WCT 2** (22:20, 22:25), **SSM 1** (22:25), and **SCKT/MVST/AGIG 0**. Regular-session appearances add no AH count. All current scanner Total% values are below +150%. Float and industry remain pattern observations; no candidate is excluded for sector or float.

**SIP verification:** `broker.js bars SYM --tf 5Min --start 2026-10-01T20:00:00Z --limit 300` returned consolidated SIP for SORA and AMOD. Both newest returned bars start at **16:45 ET**, consistent with the approximately 15-minute free-tier delay. The bars below extend the preceding scan's tape verification; the source confirms trading through the available window rather than the current scan-minute price.

| Ticker | Bar start ET | Open | High | Low | Close | Shares | VWAP | Trades |
|--------|--------------|------|------|-----|-------|--------|------|--------|
| SORA | 16:35 | $3.08 | $3.15 | $2.97 | $3.13 | 190,813 | $3.04 | 2,159 |
| SORA | 16:40 | $3.14 | $3.15 | $3.00 | $3.06 | 147,480 | $3.06 | 1,645 |
| SORA | 16:45 | $3.04 | $3.14 | $3.00 | $3.01 | 119,786 | $3.07 | 1,534 |
| AMOD | 16:35 | $1.44 | $1.59 | $1.43 | $1.45 | 682,332 | $1.52 | 3,916 |
| AMOD | 16:40 | $1.45 | $1.56 | $1.40 | $1.40 | 600,356 | $1.49 | 3,077 |
| AMOD | 16:45 | $1.41 | $1.45 | $1.32 | $1.32 | 403,322 | $1.37 | 2,018 |

**SORA — skip FIRST-BAR-SPIKE; recent volume and price decline.** Since 22:45, scanner AH% falls **+34.2% → +26.7%**, price **$3.22 → $3.04**, and Total% **+39.9% → +32.1%**, while displayed AH volume grows **2.0M → 2.6M** and VRatio remains **7.3x**. SIP totals **3,591,755 shares / 42,165 trades**, adding **458,079 shares / 5,338 trades** since the previous verification. The scanner's $3.04 is corroborated by SIP trading; the move is real. Per-bar volume declines **424,861 → 190,813 → 147,480 → 119,786 shares**, with the last bar down **18.8%**. Recent closes decline **$3.13 → $3.06 → $3.01**. The observed AH high remains **$3.64 in the 16:05 bar**, and the latest verified close is **17.3% below** it. No subsequent verified bar makes a new high. The Yahoo timeline through approximately 17:01 ET shows small rebounds around the lower base; it is used only for shape, not exact levels, highs, volume, or appearance counts.

**SORA FIRST-BAR-SPIKE WATCH:** The observed high remains in the **16:00–16:15 ET opening window**, and CONFIRM-3 is **NO in all four evaluations**. Apply the explicit opening-spike skip at this eligible entry scan despite proximity within 20% of the high. Record hypothetical scanner entry **$3.04 at 23:00 CEST / 17:00 ET**, Total **+32.1%**, for morning measurement only. Revisit the opening-high condition if later SIP establishes a volume-backed new high. The detector's standalone verdict does not assign a grade or rank.

**SORA catalyst and quote:** Carry **Grade C** from the verified [GlobeNewswire release](https://www.globenewswire.com/news-release/2026/10/01/3373374/0/en/asiastrategy-signs-memorandum-of-understanding-with-plume-network-to-advance-real-world-asset-tokenisation-across-asia.html), **October 1, 2026, 16:05 ET / 22:05 CEST**: a non-binding Plume memorandum to explore a tokenised-products joint venture. The full terms and timestamp were verified at 22:25. Both quote checks again returned `SORA  bid $1.93 x100  ask $2.78 x100  @ 2026-10-01T20:00:00.60007104Z`. This unchanged quote is about **60 minutes old**. Current fillable liquidity remains **unconfirmed**; the stale quote does not contradict later SIP or establish a bad print. No sizing or order is supported by this book verification.

**AMOD — skip Day% failure; DEAD-CAT-OVERRIDE WATCH retained with fade concern.** Scanner AH% rises **+10.1% → +16.8% → +20.4%**, price **$1.29 → $1.37 → $1.41**, and Total% **-16.9% → -11.8% → -9.1%** across its three appearances. Since 22:45, displayed AH volume increases **1.7M → 3.3M** and VRatio **4.9x → 6.2x**. Day **-24.5%** independently fails the requirement to exceed -15%; the live entry remains blocked. SIP totals **4,064,830 shares / 21,817 trades**, adding **1,686,010 shares / 9,011 trades**. This confirms substantial real trading across bars and corroborates the scanner's $1.41.

**AMOD trajectory and hypothetical:** SIP establishes a later AH high of **$1.59 in the 16:35 bar**, above the prior $1.55 high at 16:15. Subsequent closes fall **$1.45 → $1.40 → $1.32**, VWAP falls **$1.52 → $1.49 → $1.37**, and volume falls **682,332 → 600,356 → 403,322 shares** (latest **-32.8%**). The latest verified close is **17.0% below** the new high and remains above the **$1.17 regular close**. Rising scanner AH% therefore overstates the latest trajectory: a real recovery made a later high, then faded. Retain **DEAD-CAT-OVERRIDE WATCH**, hypothetical scanner entry **$1.41 at 23:00 CEST / 17:00 ET**, Total **-9.1%**, with this fade concern for morning evaluation. The current book returned `AMOD  bid $1.31 x100  ask $1.34 x100  @ 2026-10-01T20:58:48.514738532Z`, approximately two minutes behind the snapshot, with a sized two-sided book. Its lower level supports the pullback. Yahoo's later timeline also shows a lower base after the recovery; only its shape is used. No first-bar-spike label applies to the later 16:35 high, and CONFIRM-3 NO supplies no independent skip.

**AMOD catalyst:** Carry **Grade D** from the verified [October 1 SEC 8-K](https://www.sec.gov/Archives/edgar/data/1862463/000149315226045296/form8-k.htm), accepted **11:30:52 on October 1, 2026 (EDGAR displayed time)** in the [filing index](https://www.sec.gov/Archives/edgar/data/1862463/000149315226045296/0001493152-26-045296-index.html). This is today's disclosure of the September 30 PIPE closing: **51,621,560 common shares plus warrants for the same number**, in exchange for 3,170 bitcoin. The previously verified issuance and warrant dilution support Grade D. Scanner float **543K may be stale** after the issuance; current freely tradable float is unverified. No fresh search is required to carry the dated, verified grade. The entry skip is based on Day%, with the latest fade additionally documented.

**Instrumentation (verbatim; log-only):** Standalone SPIKE and CONFIRM-3 verdicts do not enter, skip, grade, or rank trades. The separate first-bar-spike rule above uses the opening-high trajectory and repeated NO condition.

```text
SORA 2026-10-01  SPIKE  16:06ET  +52%  $3.64  243 trades / 17k sh  (first co-spike bar) (as-of 17:00ET)
SORA 2026-10-01  CONFIRM-3  NO no local-volume new-high ignition as-of 17:00ET
AMOD 2026-10-01  SPIKE  16:15ET  +15%  $1.35  366 trades / 64k sh  (first co-spike bar) (as-of 17:00ET)
AMOD 2026-10-01  CONFIRM-3  NO ignition 16:15ET failed third-bar hold/volume as-of 17:00ET
```

**SCKT and MVST — below entry threshold.** SCKT remains **+7.4% AH / $0.58**; displayed volume grows **6.9M → 9.9M** and VRatio **0.5x → 0.8x**. MVST remains **+6.0% AH / $0.70**; displayed volume edges **77K → 80K**. Neither has a scanner-confirmed >10% appearance, and their discovery volumes do not establish real AH liquidity. No qualifying entry, catalyst workup, or detector instrumentation is due for these below-threshold names.

**Absent pipeline names:** AGIG, WCT, and SSM are absent from this snapshot and add no appearance. Carry their prior notes and hypothetical watches without inferring a new trajectory from absence. EVOL, GBLRF, MHUAF, CRMZ, FNFI, SGRP, LTCEF, and EJH remain **untradable (carried)**; no repeated SIP or catalyst workup was performed on them.

**Carry forward and fills:** Retain all **34 unique pipeline names** for later scans and the **00:30 CEST / 18:30 ET final-scan feed-lag cross-check**. Alpaca `positions --json` returned `[]` and `orders open` returned `No open orders.` No entry order was submitted, so there is no fill to add to OPEN_POSITIONS. Chase-cap and multi-session entry instrumentation do not apply without an entry; final-scan gate-block instrumentation is not due. Yahoo volume and percentages anchored to the previous day's close were not used for AH appearance counts or execution decisions.

**Daily email:** Include the 23:00 no-entry decision, SORA's FIRST-BAR-SPIKE WATCH hypothetical and hour-old quote, and AMOD's DEAD-CAT-OVERRIDE WATCH hypothetical with its later high, subsequent fade, Grade D disclosure, and Day% block. No item requires Juan's input.

## Scan 23:30 CEST (5:30 PM ET)

**Decision:** No entry. SORA retains its first-bar-spike block, AMOD fails the Day% rule, and newly discovered ELUT has only one qualifying AH appearance with a pullback after its initial surge. The other six scanner names are below the >10% AH threshold. No paper orders submitted.

`python3 scripts/scan.py --all` ran at **17:30:28 ET / 23:30:28 CEST / 21:30:28 UTC**, in the AFTERHOURS session, and returned **9 hits** after `bash scripts/sync-repo.sh` reported the repository up to date. The US trading date is **2026-10-01**. Broker verification followed the snapshot; detector cutoffs preserve **17:30 ET**. The table preserves scanner discovery readings.

```text
  Supplementary AH-change-only (>15%, not in volume pass): none
  AH >10% at this snapshot (unrounded): AMOD, ELUT, SORA
```

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| SCKT | [TV](https://www.tradingview.com/chart/?symbol=SCKT) | $0.54 | +21.0% | +5.1% | $0.57 | +27.2% | 10.9M | 13.0M | 0.8x | 5.7M | Computer Peripherals |
| SSM | [TV](https://www.tradingview.com/chart/?symbol=SSM) | $2.21 | +97.3% | +5.9% | $2.34 | +108.9% | 9.0M | 8.7M | 1.0x | 1.1M | Motor Vehicles |
| AMOD | [TV](https://www.tradingview.com/chart/?symbol=AMOD) | $1.17 | -24.5% | +14.5% | $1.34 | -13.5% | 4.2M | 623K | 6.7x | 543K | Packaged Software |
| ELUT | [TV](https://www.tradingview.com/chart/?symbol=ELUT) | $0.80 | +1.3% | +20.0% | $0.96 | +21.5% | 3.4M | 397K | 8.4x | 35.3M | Biotechnology |
| SORA | [TV](https://www.tradingview.com/chart/?symbol=SORA) | $2.40 | +4.3% | +35.0% | $3.24 | +40.8% | 3.1M | 423K | 7.4x | 4.9M | Wholesale Distributors |
| SDEV | [TV](https://www.tradingview.com/chart/?symbol=SDEV) | $3.66 | +41.3% | +5.7% | $3.87 | +49.4% | 1.4M | 36.8M | 0.0x | 1.8M | Pharmaceuticals: Major |
| NCI | [TV](https://www.tradingview.com/chart/?symbol=NCI) | $1.06 | -15.9% | +5.7% | $1.12 | -11.1% | 292K | 4.1M | 0.1x | 2.4M | Apparel/Footwear Retail |
| AGIG | [TV](https://www.tradingview.com/chart/?symbol=AGIG) | $0.96 | -11.6% | +5.9% | $1.02 | -6.4% | 65K | 139K | 0.5x | 11.9M | Oil & Gas Production |
| CMCT | [TV](https://www.tradingview.com/chart/?symbol=CMCT) | $3.62 | +23.5% | +9.5% | $3.96 | +35.3% | 51K | 3.4M | 0.0x | 2.8M | Real Estate Investment Trusts |

### Evaluation notes

**Broker availability and AH counts:** Fresh candidates **ELUT and NCI returned `tradable=true`**, active on Nasdaq, before further workup. Positive checks for the other seven names carry forward from prior scans. The unrounded scanner lists now establish **SORA 5**, **AMOD 4**, **ELUT 1**, **WCT 2**, **SSM 1**, and **SCKT/MVST/AGIG/SDEV/NCI/CMCT 0**. Regular-session appearances do not count. Every current Total% is below +150%. Float and sector are tracked without independent learning-phase exclusions.

**SIP verification:** Consolidated `broker.js bars SYM --tf 5Min --start 2026-10-01T20:00:00Z --limit 300` returned bars for all three >10% names through **17:15 ET**, consistent with the approximately 15-minute free-tier delay. The scanner prices are corroborated by SIP ranges; no bad-print rejection applies. ELUT's repeat pull returned the same latest bar and exact data. The table shows ELUT's ignition and subsequent bars, plus the latest SORA/AMOD bars:

| Ticker | Bar start ET | Open | High | Low | Close | Shares | VWAP | Trades |
|--------|--------------|------|------|-----|-------|--------|------|--------|
| ELUT | 16:45 | $0.82 | $1.10 | $0.82 | $1.04 | 576,066 | $1.01 | 2,363 |
| ELUT | 16:50 | $1.04 | $1.04 | $0.95 | $0.99 | 856,630 | $1.00 | 4,181 |
| ELUT | 16:55 | $1.00 | $1.02 | $0.95 | $0.98 | 669,554 | $0.99 | 2,800 |
| ELUT | 17:00 | $0.98 | $0.99 | $0.91 | $0.94 | 490,561 | $0.94 | 1,932 |
| ELUT | 17:05 | $0.95 | $0.99 | $0.92 | $0.98 | 551,896 | $0.96 | 1,627 |
| ELUT | 17:10 | $0.98 | $0.98 | $0.94 | $0.97 | 562,486 | $0.97 | 1,266 |
| ELUT | 17:15 | $0.96 | $0.97 | $0.94 | $0.95 | 206,171 | $0.96 | 539 |
| SORA | 17:05 | $3.09 | $3.12 | $3.06 | $3.06 | 54,793 | $3.09 | 670 |
| SORA | 17:10 | $3.06 | $3.31 | $3.06 | $3.23 | 196,364 | $3.22 | 2,039 |
| SORA | 17:15 | $3.24 | $3.31 | $3.12 | $3.15 | 218,151 | $3.21 | 2,319 |
| AMOD | 17:05 | $1.34 | $1.42 | $1.31 | $1.38 | 108,404 | $1.37 | 518 |
| AMOD | 17:10 | $1.36 | $1.40 | $1.33 | $1.34 | 77,251 | $1.37 | 336 |
| AMOD | 17:15 | $1.34 | $1.37 | $1.32 | $1.33 | 45,929 | $1.34 | 274 |

**ELUT — watch; first qualifying appearance and post-ignition pullback.** AH **+20.0%**, Day **+1.3%**, and Total **+21.5%** pass their percentage thresholds, but this first appearance does not meet the two-AH-scan gate. Float **35.3M** and Biotechnology are pattern observations. SIP totals **3,913,741 shares / 14,711 trades**, including 377 shares / 3 trades at 16:00 before the 16:45 ignition. Hundreds of thousands of shares and thousands of trades across multiple bars verify a real surge, rather than stale VRatio or a thin drift. The high is **$1.10 in the 16:45 bar**, after the opening window. The latest exact SIP close **$0.9492** is **13.7% below** that high. After a rebound at 17:05, closes ease again; latest volume falls **63.3%** and trades fall 1,266 → 539. No later high or sustained BUILD is verified. Yahoo's later timeline likewise shows a lower base with small rebounds; only its shape is used. Reassess trajectory and liquidity if ELUT returns above threshold in a later scan. This is not a FIRST-BAR-SPIKE WATCH because its peak occurred after 16:15 ET; CONFIRM-3 NO supplies no independent entry block.

**ELUT catalyst — Grade C, fresh cash-receipt and funding update.** Three structured searches covered today's earnings, same-day newswire releases, and same-day SEC 8-K filings. No same-day earnings report or fresh 8-K was verified. The [primary GlobeNewswire release](https://www.globenewswire.com/news-release/2026/10/01/3373430/0/en/elutia-receives-8-million-payment-from-boston-scientific-company-now-fully-funded-into-2029.html), checked in full, is dated **October 1, 2026, 16:45 ET / 22:45 CEST**. Boston Scientific released the full **$8M escrow holdback**, without claims, from the BioEnvelope sale that closed **October 1, 2025**. Elutia says this completes its funding milestones and funds operations into 2029 without an equity offering. Grade C reflects the scheduled cash receipt and balance-sheet update. The 2025 sale is background; today's release does not announce a new acquisition agreement or FDA clearance. NXT-41x clearance remains expected in **H1 2027**, so the search index's October 1 FDA-event reference is not used as a catalyst.

**SORA — skip FIRST-BAR-SPIKE despite a real rebound.** Since 23:00, scanner AH% rises **+26.7% → +35.0%**, price **$3.04 → $3.24**, Total **+32.1% → +40.8%**, and displayed AH volume **2.6M → 3.1M**. SIP totals **4,376,288 shares / 50,777 trades**, adding **784,533 shares / 8,612 trades**. Recent activity rebounds from 54,793 shares / 670 trades at 17:05 to 196,364 / 2,039 at 17:10 and 218,151 / 2,319 at 17:15. This corroborates the recovery, but its later high reaches only **$3.31**, below the **$3.64 opening high in the 16:05 bar**. The latest close $3.15 is **13.5% below** the opening high and pulls back from $3.23. CONFIRM-3 remains **NO in all five evaluations**. Apply the explicit first-bar-spike skip. **FIRST-BAR-SPIKE WATCH hypothetical: $3.24 at 23:30 CEST / 17:30 ET**, Total **+40.8%**, for morning measurement only. Revisit the block if later SIP establishes a volume-backed new high.

**SORA catalyst:** Carry **Grade C** from the verified October 1 GlobeNewswire release linked in the 22:25 workup, **16:05 ET / 22:05 CEST**: a non-binding Plume memorandum to explore a tokenised-products joint venture. Its date and terms remain verified; no repeat catalyst search is required.

**AMOD — skip Day% failure; recovery has faded.** Scanner AH% falls **+20.4% → +14.5%**, price **$1.41 → $1.34**, and Total **-9.1% → -13.5%**, even as displayed AH volume increases **3.3M → 4.2M** and VRatio **6.2x → 6.7x**. Day **-24.5%** fails the requirement to exceed -15%. SIP totals **4,671,356 shares / 24,854 trades**, adding **606,526 shares / 3,037 trades**. The high remains **$1.59 in the 16:35 bar**; latest close $1.33 is **16.4% below** it. Recent closes **$1.38 → $1.34 → $1.33**, VWAP, shares and trades decline; latest volume falls **40.5%**, to 45,929 shares / 274 trades. This is a fading recovery with thinning current participation, not a fresh BUILD. Retain the earlier **DEAD-CAT-OVERRIDE WATCH** hypotheticals for morning measurement; this falling-AH% snapshot supplies no new rising-AH% override observation.

**AMOD catalyst:** Carry **Grade D** from the verified October 1 SEC 8-K and filing index linked in the 22:30 workup, accepted **11:30:52 on October 1, 2026 (EDGAR displayed time)**. Today's disclosure covers the September 30 PIPE closing: **51,621,560 shares plus warrants for the same number**, in exchange for 3,170 bitcoin. Scanner float **543K may be stale** after that issuance; current freely tradable float remains unverified. The Day% block determines the skip; the latest fade is an additional concern.

**Quote freshness:** The following quotes were returned after the snapshot. ELUT and SORA were checked twice and remained unchanged:

```text
ELUT  bid $0.85 x300  ask $1.01 x100  @ 2026-10-01T20:57:24.346040236Z
SORA  bid $1.93 x100  ask $2.78 x100  @ 2026-10-01T20:00:00.60007104Z
AMOD  bid $1.31 x100  ask $1.34 x100  @ 2026-10-01T20:58:48.514738532Z
```

ELUT's quote is about **33 minutes old**, SORA's **90 minutes old**, and AMOD's **31 minutes old** at the scan. Both sides have non-zero prices and sizes, but **current fillable liquidity is unconfirmed** for all three. These stale quotes cannot contradict later consolidated trades or establish a bad print. No sizing or order was attempted because the candidate entry gates already fail. Recheck the book at the next eligible scan.

**Instrumentation (verbatim; log-only):** Standalone SPIKE and CONFIRM-3 verdicts do not grade or rank entries. The separate first-bar-spike rule applies to SORA's persistent opening high and repeated NO condition.

```text
ELUT 2026-10-01  SPIKE  16:46ET  +38%  $1.10  95 trades / 25k sh  (first co-spike bar) (as-of 17:30ET)
SORA 2026-10-01  SPIKE  16:06ET  +52%  $3.64  243 trades / 17k sh  (first co-spike bar) (as-of 17:30ET)
AMOD 2026-10-01  SPIKE  16:15ET  +15%  $1.35  366 trades / 64k sh  (first co-spike bar) (as-of 17:30ET)
ELUT 2026-10-01  CONFIRM-3  NO ignition 16:45ET failed third-bar hold/volume as-of 17:30ET
SORA 2026-10-01  CONFIRM-3  NO no local-volume new-high ignition as-of 17:30ET
AMOD 2026-10-01  CONFIRM-3  NO ignition 16:15ET failed third-bar hold/volume as-of 17:30ET
```

**Other scanner names — below entry threshold:** SCKT eases **+7.4% → +5.1% AH**, while displayed volume grows **9.9M → 10.9M**. SSM returns at **+5.9% AH**, below its one earlier qualifying appearance; the earlier opening-spike watch carries forward without a new trajectory conclusion from this snapshot. SDEV and CMCT make their first AH scanner appearances at **+5.7%** and **+9.5%**; their regular-session sightings add no AH count. New NCI is **+5.7% AH** and also fails the Day% rule at **-15.9%**. AGIG returns at **+5.9% AH / $1.02**, versus +5.1% / $1.01 at 22:45. None supplies a qualifying >10% appearance. These discovery volumes alone do not verify real AH accumulation or executable liquidity; catalyst and detector workups are not required below threshold.

**Carry forward and fills:** Retain **36 unique pipeline names**: the prior 34 plus ELUT and NCI. Preserve them for later scans and the **00:30 CEST / 18:30 ET final-scan feed-lag cross-check**. WCT and MVST are absent and add no appearance; their prior notes carry forward. EVOL, GBLRF, MHUAF, CRMZ, FNFI, SGRP, LTCEF, and EJH remain **untradable (carried)**, with no repeated workup. Alpaca `positions --json` returned `[]`; `orders open` returned `No open orders.` No fill requires an OPEN_POSITIONS entry. Chase-cap and multi-session entry instrumentation do not apply without an entry; final-scan gate-block instrumentation is not due. Yahoo volume, exact AH levels, and previous-day-close percentages were not used for liquidity, high verification, or appearance counts.

**Daily email:** Report ELUT's first qualifying appearance, real 16:45 ignition, fresh Grade C $8M cash-receipt release, subsequent pullback and stale quote; SORA's renewed volume without a later new high and FIRST-BAR-SPIKE WATCH hypothetical; and AMOD's Day% block and thinning fade. No item requires Juan's input.

## Scan 00:00 CEST (6:00 PM ET)

**Decision:** No entry. ELUT now has two qualifying AH appearances, but its early surge continues to fade with lighter recent participation. SORA retains its first-bar-spike block. AMOD has resumed a real BUILD but still fails the Day% rule; record a new hypothetical override watch. SCKT, IPW, and UONEK each have only one qualifying appearance, with additional volume/book concerns. No paper orders submitted.

`python3 scripts/scan.py --all` ran at **18:00:26 ET / 00:00:26 CEST on October 2 / 22:00:26 UTC on October 1**, in the AFTERHOURS session, and returned **13 hits** after `bash scripts/sync-repo.sh` reported the repository up to date. The US trading date and log date remain **2026-10-01**, because Berlin time is before 06:00. Verification followed at approximately 18:00–18:03 ET; detector cutoffs preserve **18:00 ET**. The table preserves scanner discovery readings.

```text
  Supplementary AH-change-only (>15%, not in volume pass): UONEK
  AH >10% at this snapshot (unrounded): AMOD, ELUT, IPW, SCKT, SORA, UONEK
```

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| SCKT | [TV](https://www.tradingview.com/chart/?symbol=SCKT) | $0.54 | +21.0% | +11.7% | $0.60 | +35.2% | 12.1M | 13.1M | 0.9x | 5.7M | Computer Peripherals |
| AMOD | [TV](https://www.tradingview.com/chart/?symbol=AMOD) | $1.17 | -24.5% | +32.5% | $1.55 | +0.0% | 4.8M | 696K | 6.9x | 543K | Packaged Software |
| ELUT | [TV](https://www.tradingview.com/chart/?symbol=ELUT) | $0.80 | +1.3% | +17.5% | $0.94 | +19.0% | 4.2M | 489K | 8.6x | 35.3M | Biotechnology |
| SORA | [TV](https://www.tradingview.com/chart/?symbol=SORA) | $2.40 | +4.3% | +28.8% | $3.09 | +34.3% | 3.6M | 481K | 7.4x | 4.9M | Wholesale Distributors |
| SDEV | [TV](https://www.tradingview.com/chart/?symbol=SDEV) | $3.66 | +41.3% | +6.6% | $3.90 | +50.6% | 2.0M | 36.9M | 0.1x | 1.8M | Pharmaceuticals: Major |
| BTTC | [TV](https://www.tradingview.com/chart/?symbol=BTTC) | $0.63 | +21.8% | +5.0% | $0.67 | +27.9% | 1.4M | 64.5M | 0.0x | 10.8M | Packaged Software |
| IPW | [TV](https://www.tradingview.com/chart/?symbol=IPW) | $1.14 | -1.7% | +10.5% | $1.26 | +8.6% | 1.2M | 431K | 2.7x | 1.2M | Internet Retail |
| QNME | [TV](https://www.tradingview.com/chart/?symbol=QNME) | $0.54 | +1.2% | +7.8% | $0.58 | +9.0% | 656K | 55.4M | 0.0x | 25.8M | Air Freight/Couriers |
| NCI | [TV](https://www.tradingview.com/chart/?symbol=NCI) | $1.06 | -15.9% | +6.6% | $1.13 | -10.3% | 355K | 4.1M | 0.1x | 2.4M | Apparel/Footwear Retail |
| AGIG | [TV](https://www.tradingview.com/chart/?symbol=AGIG) | $0.96 | -11.6% | +5.9% | $1.02 | -6.4% | 65K | 139K | 0.5x | 11.9M | Oil & Gas Production |
| CMCT | [TV](https://www.tradingview.com/chart/?symbol=CMCT) | $3.62 | +23.5% | +6.4% | $3.85 | +31.4% | 59K | 3.4M | 0.0x | 2.8M | Real Estate Investment Trusts |
| KPTI | [TV](https://www.tradingview.com/chart/?symbol=KPTI) | $0.87 | -29.0% | +6.1% | $0.92 | -24.6% | 58K | 1.4M | 0.0x | 18.6M | Pharmaceuticals: Major |
| UONEK | [TV](https://www.tradingview.com/chart/?symbol=UONEK) | $3.64 | -3.7% | +15.1% | $4.19 | +10.8% | 552 | 10K | 0.1x | 1.6M | Movies/Entertainment |

### Evaluation notes

**Tradability and appearance counts:** Fresh candidates **IPW, UONEK, QNME, and KPTI returned `tradable=true`**, active on Nasdaq, before further workup. Other positive checks carry forward, including SCKT's 22:45 check and BTTC's regular-session check. The unrounded scanner lists establish **SORA 6**, **AMOD 5**, **ELUT 2** (23:30, 00:00), **SCKT 1**, **IPW 1**, **UONEK 1**, **WCT 2**, and **SSM 1**. SCKT's earlier below-threshold appearances add zero; regular-session appearances add zero. UONEK was added by the supplementary change pass, which does not qualify it for entry. All displayed Total% values are below +150%. Float and industry are observations; no sector or float exclusion was applied.

**SIP verification and freshness:** `broker.js bars SYM --tf 5Min --start 2026-10-01T20:00:00Z --limit 300` returned **consolidated SIP** for all six >10% names. A repeat pull with `--json` confirmed the same newest **17:45 ET** bar for each, consistent with the approximately 15-minute free-tier delay. No pagination remains. These bars establish the available tape, rather than a current executable quote. Every scanner AH price is within observed SIP ranges; no verified bad-print rejection applies. Yahoo `check-prices.py --ah-history` supplied later timeline shapes only. Its extended-hours volume, exact prices/highs, and changes anchored to the previous day's close were not used for liquidity or appearance counts.

| Ticker | Verified AH shares | Trades | SIP AH high / bar start ET | Latest SIP close | Off high | Latest bar shares / trades |
|--------|--------------------|--------|---------------------------|------------------|----------|---------------------------|
| ELUT | 4,802,169 | 17,523 | $1.10 / 16:45 | $0.9200 | -16.4% | 167,940 / 512 |
| SCKT | 12,659,017 | 22,881 | $0.6539 / 16:15 | $0.5970 | -8.7% | 57,359 / 188 |
| SORA | 4,797,063 | 54,786 | $3.64 / 16:05 | $3.0300 | -16.8% | 77,621 / 767 |
| AMOD | 5,899,928 | 30,878 | $1.69 / 17:45 | $1.6689 | -1.2% | 580,711 / 2,998 |
| IPW | 1,432,511 | 9,917 | $1.4969 / 17:15 | $1.2100 | -19.2% | 42,270 / 260 |
| UONEK | 1,335 | 51 | $4.19 / 17:35 | $3.8500 | -8.1% | 570 / 20 |

**ELUT — skip SPIKE→FADE with lighter recent participation; current book unconfirmed.** Since 23:30, scanner AH% falls **+20.0% → +17.5%**, price **$0.96 → $0.94**, and Total **+21.5% → +19.0%**, while discovery volume grows **3.4M → 4.2M**. SIP adds **888,428 shares / 2,812 trades** since the preceding verification, but the early surge's hundreds-of-thousands of shares and thousands of trades per bar have eased to **79,049–192,007 shares / 245–723 trades** in the last four bars. Recent closes fall **$0.9603 → $0.9589 → $0.9392 → $0.9200** at 17:30–17:45; VWAP eases **$0.9620 → $0.9466 → $0.9468 → $0.9373**. The last bar's shares increase 28.8%, but this does not reverse the lower prices or restore ignition-level participation. Its high remains at **16:45**, followed by lower highs and a renewed decline; the later Yahoo shape also continues downward with small rebounds. Being within 20% of that high alone does not establish a HOLD. The two-appearance gate is met, but the trajectory requirement and the requirement for sustained volume are not. This is not an opening-bar spike; CONFIRM-3 NO supplies no independent block. Reassess if the final scan shows a sustained recovery on renewed volume.

**SORA — skip FIRST-BAR-SPIKE.** Since 23:30, scanner AH% falls **+35.0% → +28.8%**, price **$3.24 → $3.09**, and Total **+40.8% → +34.3%**, while discovery volume grows **3.1M → 3.6M**. SIP adds **420,775 shares / 4,009 trades**. The opening high remains **$3.64 in the 16:05 bar**; no later bar exceeds it. Recent closes are **$3.21 → $3.08 → $3.10 → $3.03** at 17:30–17:45, with only 43,664–101,832 shares / 428–820 trades per bar. CONFIRM-3 remains **NO in all six evaluations**. Apply the first-bar-spike skip even within 20% of the opening high. **FIRST-BAR-SPIKE WATCH hypothetical: $3.09 at 00:00 CEST / 18:00 ET**, Total **+34.3%**. Revisit the block if a later volume-backed new high appears; this hypothetical is not a fill.

**AMOD — skip Day% failure; renewed BUILD / DEAD-CAT-OVERRIDE WATCH.** Since 23:30, scanner AH% rises **+14.5% → +32.5%**, price **$1.34 → $1.55**, and Total **-13.5% → +0.0%**, while discovery volume grows **4.2M → 4.8M**. SIP adds **1,228,572 shares / 6,024 trades** and confirms a genuine late rebuild: at 17:35, 17:40, and 17:45, closes rise **$1.43 → $1.5502 → $1.6689**, VWAP rises **$1.4408 → $1.5025 → $1.6253**, shares rise **103,870 → 240,491 → 580,711**, and trades rise **546 → 1,114 → 2,998**. The **17:45 high $1.69** exceeds the former **16:35 high $1.59**. This is a volume-backed BUILD above the **$1.17 regular close**, not thin drift or a bad print. Day **-24.5%** still blocks live entry. **DEAD-CAT-OVERRIDE WATCH hypothetical: $1.55 at 00:00 CEST / 18:00 ET**, Total **+0.0%**. Rising AH% across the 23:30 and 00:00 snapshots and the renewed real accumulation support this new observation; earlier hypotheticals remain in their original sections. CONFIRM-3's original failed-ignition verdict does not block or downgrade the renewed build. Scanner float **543K may be stale** after the PIPE issuance.

**SCKT — watch; first qualifying appearance, thinner recovery and no verified fillable ask.** Since 23:30, scanner AH% rises **+5.1% → +11.7%**, price **$0.57 → $0.60**, and discovery volume **10.9M → 12.1M**. SIP confirms the real earlier spike: **2.50M / 4,341 trades at 16:15**, followed by **2.87M / 4,940 at 16:20**. A later recovery closes at $0.61 at 17:30, but its next closes are **$0.5965 → $0.6033 → $0.5970**, and volume falls **443,916 → 266,692 → 259,328 → 57,359 shares**, with latest volume down **77.9%** and only **188 trades**. The sub-1x discovery ratio plus weakening recent tape does not establish a fresh BUILD. The two-appearance gate fails independently. Its high occurred in the **16:15–16:20 bar**, after the opening window, so no FIRST-BAR-SPIKE WATCH is assigned. The stale zero-ask quote below provides no current fillable book; it does not erase the real SIP volume.

**IPW — watch/skip this entry; first appearance and SPIKE→FADE.** New discovery, float **1.2M**, Internet Retail, Day **-1.7%**, Total **+8.6%**. SIP verifies a real **17:15 ignition** and multi-bar activity: **247,763 / 1,729 trades**, **339,684 / 2,643**, and **380,249 / 2,379** at 17:15–17:25. The rebound never exceeds the **$1.4969 high in the 17:15 bar**. Later closes ease **$1.4000 → $1.2880 → $1.2600 → $1.2700 → $1.2100**; the last two bars have only **35,111 / 274 trades** and **42,270 / 260**. The latest close is **19.2% below** the high. Yahoo's later shape continues the fade before a small rebound. One qualifying appearance fails the two-scan gate; price and recent participation also fail the sustained BUILD/HOLD check. CONFIRM-3 **YES is logged only** and does not override the current trajectory. No first-bar-spike label applies to a 17:15 high.

**UONEK — skip thin/not-accumulating AH tape; one appearance.** New supplementary-pass discovery, float **1.6M**, Movies/Entertainment, Day **-3.7%**, Total **+10.8%**. SIP returns only three sparse bars: **130 shares / 16 trades at 17:30**, **635 / 15 at 17:35**, and **570 / 20 at 17:45**, totaling **1,335 shares / 51 trades**. The scanner's $4.19 did trade in the 17:35 bar, so do not call it a bad print. This is not the accumulating hundreds-of-thousands of shares / thousands of trades required for real momentum entry. The Yahoo timeline is erratic and diverges from precise SIP levels; those prices are not used. Proximity to the high, a sized but stale quote, and supplementary discovery cannot establish liquidity. The two-appearance gate also fails.

**Catalysts — dated prior grades carried; new structured searches completed:**

- **ELUT, Grade C:** [GlobeNewswire cash-receipt release](https://www.globenewswire.com/news-release/2026/10/01/3373430/0/en/elutia-receives-8-million-payment-from-boston-scientific-company-now-fully-funded-into-2029.html), **October 1, 2026, 16:45 ET / 22:45 CEST**, verified in full at 23:30. The $8M escrow payment from the 2025 BioEnvelope sale funds operations into 2029; no new acquisition or FDA clearance was announced.
- **SORA, Grade C:** [GlobeNewswire Plume memorandum](https://www.globenewswire.com/news-release/2026/10/01/3373374/0/en/asiastrategy-signs-memorandum-of-understanding-with-plume-network-to-advance-real-world-asset-tokenisation-across-asia.html), **October 1, 2026, 16:05 ET / 22:05 CEST**, verified in the 22:25 workup. The exploratory joint-venture memorandum is non-binding.
- **AMOD, Grade D:** [SEC 8-K](https://www.sec.gov/Archives/edgar/data/1862463/000149315226045296/form8-k.htm) and [acceptance index](https://www.sec.gov/Archives/edgar/data/1862463/000149315226045296/0001493152-26-045296-index.html), **October 1, 2026, accepted 11:30:52 (EDGAR displayed time)**, verified at 22:30. Fresh disclosure of the September 30 PIPE closing: **51,621,560 shares plus warrants for the same number**, exchanged for 3,170 bitcoin.
- **SCKT, Grade None — no catalyst found:** Four calls covered today's earnings, same-day newswire/company releases, same-day SEC 8-K, and a Tavily follow-up. The [July 30 Q2 earnings release](https://www.prnewswire.com/news-releases/socket-mobile-reports-second-quarter-2026-results-302839330.html) is background. Company indexes surfaced CaptureSDK/product announcements without a verified current-date release time; no grade is assigned from those headlines.
- **IPW, Grade None — no catalyst found:** Four calls covered today's earnings, same-day newswire/company releases, same-day SEC 8-K, and a Tavily follow-up. The [company release index](https://ipower.gcs-web.com) surfaced an **August 5 reverse split** and **July 23 non-binding GPU LOI**, both background. No current-date or immediately preceding overnight catalyst with a verified timestamp was found.
- **UONEK, Grade None — no catalyst found:** Four calls covered today's earnings, same-day newswire releases, same-day SEC 8-K, and a Tavily follow-up. Results surfaced Q2 earnings, older debt restructurings and the **January 16 reverse-split release**, without a verified fresh event. No current-date or immediately preceding overnight catalyst with a verified timestamp was found.

No-catalyst is a documented concern, not an entry skip reason. The searches stop at four calls per new >10% workup. Search indexes cannot establish the absence of a newer filing.

**Quote freshness and liquidity:** Each quote was checked twice and remained unchanged:

```text
ELUT  bid $0.85 x300  ask $1.01 x100  @ 2026-10-01T20:57:24.346040236Z
SCKT  bid $0.46 x100  ask $0.00 x0  @ 2026-10-01T20:00:02.143954291Z
SORA  bid $1.93 x100  ask $2.78 x100  @ 2026-10-01T20:00:00.60007104Z
AMOD  bid $1.31 x100  ask $1.34 x100  @ 2026-10-01T20:58:48.514738532Z
IPW  bid $0.95 x100  ask $1.37 x100  @ 2026-10-01T20:00:02.084910545Z
UONEK  bid $3.00 x100  ask $4.53 x100  @ 2026-10-01T20:00:00.367415945Z
```

ELUT's quote is about **63 minutes old**, AMOD's **61 minutes old**, and the others **120 minutes old** at the snapshot. **Current fillable liquidity is unconfirmed for all six**. SCKT has **no sized ask from this source** and cannot support an entry; the stale quote does not prove current consolidated-market illiquidity. The other sized books are also stale and cannot supply current sizing prices. Do not reject a strong scanner move as a bad print from these stale quotes. Updated SIP corroborates the real AMOD build and the other scanner levels. No sizing or order was attempted because entry gates already fail; recheck the book on the final scan.

**Instrumentation (verbatim; log-only):** Standalone SPIKE and CONFIRM-3 results do not grade, rank, or determine entries. SORA's separate first-bar-spike rule uses its persistent opening high and repeated NO condition.

```text
ELUT 2026-10-01  SPIKE  16:46ET  +38%  $1.10  95 trades / 25k sh  (first co-spike bar) (as-of 18:00ET)
ELUT 2026-10-01  CONFIRM-3  NO ignition 16:45ET failed third-bar hold/volume as-of 18:00ET
SCKT 2026-10-01  SPIKE  16:18ET  +20%  $0.65  1981 trades / 1068k sh  (first co-spike bar) (as-of 18:00ET)
SCKT 2026-10-01  CONFIRM-3  NO ignition 16:15ET failed third-bar hold/volume as-of 18:00ET
SORA 2026-10-01  SPIKE  16:06ET  +52%  $3.64  243 trades / 17k sh  (first co-spike bar) (as-of 18:00ET)
SORA 2026-10-01  CONFIRM-3  NO no local-volume new-high ignition as-of 18:00ET
AMOD 2026-10-01  SPIKE  16:15ET  +15%  $1.35  366 trades / 64k sh  (first co-spike bar) (as-of 18:00ET)
AMOD 2026-10-01  CONFIRM-3  NO ignition 16:15ET failed third-bar hold/volume as-of 18:00ET
IPW 2026-10-01  SPIKE  17:18ET  +27%  $1.45  366 trades / 46k sh  (first co-spike bar) (as-of 18:00ET)
IPW 2026-10-01  CONFIRM-3  YES ignition 17:15ET 148.8x; confirmed 17:25ET $1.40 as-of 18:00ET
UONEK 2026-10-01  NO-SPIKE  peak +15% @17:36ET  (no bar cleared +15% on a volume co-spike) (as-of 18:00ET)
UONEK 2026-10-01  CONFIRM-3  NO no local-volume new-high ignition as-of 18:00ET
```

**Other scanner names — below entry threshold:** SDEV rises **+5.7% → +6.6% AH** with discovery volume **1.4M → 2.0M**; NCI rises **+5.7% → +6.6%** with **292K → 355K**, but Day **-15.9%** also fails. CMCT eases **+9.5% → +6.4%**, price **$3.96 → $3.85**, with **51K → 59K**. AGIG remains **+5.9% / $1.02 / 65K**. BTTC makes its first AH appearance at **+5.0%**, separate from its regular-session watch. New QNME is **+7.8%**; new KPTI is **+6.1%** and Day **-29.0%**, below the Day% cutoff. None supplies a >10% AH appearance. Discovery volume alone does not establish AH accumulation or a fillable book; no catalyst or detector workup is due below threshold.

**Carry forward and fills:** Tonight's pipeline contains **40 unique names**: the preceding 36 plus IPW, UONEK, QNME, and KPTI. Retain every pipeline name, including absent regular-session watches, for the **00:30 CEST / 18:30 ET final-scan feed-lag cross-check**. WCT, SSM, and MVST are absent and add no appearance; their prior notes and hypothetical watches carry forward. EVOL, GBLRF, MHUAF, CRMZ, FNFI, SGRP, LTCEF, and EJH remain **untradable (carried)** without repeated volume/catalyst workups. Alpaca `positions --json` returned `[]`, `orders open` returned `No open orders.`, and `orders all` shows no new entry fills. No fill requires an OPEN_POSITIONS entry. Chase-cap and multi-session-runner entry instrumentation do not apply without an entry. This is the 18:00 scan; final-scan gate-block instrumentation is due at 18:30, not here.

**Daily email:** Report the no-entry decision; ELUT's second appearance with declining price and lighter tape; SORA's FIRST-BAR-SPIKE WATCH at $3.09; AMOD's renewed real BUILD and DEAD-CAT-OVERRIDE WATCH at $1.55 despite its Day% block; SCKT's stale zero-ask quote; IPW's real ignition followed by fade; and UONEK's supplementary discovery with only 1,335 SIP shares / 51 trades. Include the stale-quote verification limitation. No item requires Juan's input.

## Scan 00:30 CEST (6:30 PM ET)

**Decision:** No entry. AMOD continues a real late BUILD but fails the Day% rule. SORA retains its first-bar-spike block. SDEV, HTCR, and TARA each have their first qualifying >10% AH appearance, with additional book or volume blocks. The final pipeline check found no omitted candidate with current accumulating volume that clears the entry gates. No paper orders submitted.

`python3 scripts/scan.py --all` ran at **18:30:26 ET / 00:30:26 CEST on October 2 / 22:30:26 UTC on October 1**, in the AFTERHOURS session, and returned **10 hits** after `bash scripts/sync-repo.sh` reported the repository up to date. The US trading date and log date remain **2026-10-01**. Verification followed the snapshot; detector cutoffs preserve **18:30 ET**. The table preserves the scanner's discovery readings.

```text
  Supplementary AH-change-only (>15%, not in volume pass): none
  AH >10% at this snapshot (unrounded): AMOD, HTCR, SDEV, SORA, TARA
```

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| SCKT | [TV](https://www.tradingview.com/chart/?symbol=SCKT) | $0.54 | +21.0% | +9.3% | $0.59 | +32.3% | 12.4M | 13.2M | 0.9x | 5.7M | Computer Peripherals |
| AMOD | [TV](https://www.tradingview.com/chart/?symbol=AMOD) | $1.17 | -24.5% | +72.6% | $2.02 | +30.3% | 8.3M | 1.1M | 7.7x | 543K | Packaged Software |
| SORA | [TV](https://www.tradingview.com/chart/?symbol=SORA) | $2.40 | +4.3% | +25.8% | $3.02 | +31.3% | 3.8M | 505K | 7.4x | 4.9M | Wholesale Distributors |
| SDEV | [TV](https://www.tradingview.com/chart/?symbol=SDEV) | $3.66 | +41.3% | +12.6% | $4.12 | +59.1% | 2.6M | 36.9M | 0.1x | 1.8M | Pharmaceuticals: Major |
| IPW | [TV](https://www.tradingview.com/chart/?symbol=IPW) | $1.14 | -1.7% | +7.9% | $1.23 | +6.0% | 1.3M | 448K | 2.9x | 1.2M | Internet Retail |
| QNME | [TV](https://www.tradingview.com/chart/?symbol=QNME) | $0.54 | +1.2% | +5.4% | $0.57 | +6.7% | 705K | 55.4M | 0.0x | 25.8M | Air Freight/Couriers |
| TARA | [TV](https://www.tradingview.com/chart/?symbol=TARA) | $2.76 | -9.5% | +11.2% | $3.07 | +0.7% | 171K | 2.4M | 0.1x | 52.2M | Pharmaceuticals: Major |
| HTCR | [TV](https://www.tradingview.com/chart/?symbol=HTCR) | $1.93 | -3.7% | +20.5% | $2.32 | +16.0% | 128K | 29K | 4.3x | 614K | Packaged Software |
| AGIG | [TV](https://www.tradingview.com/chart/?symbol=AGIG) | $0.96 | -11.6% | +5.9% | $1.02 | -6.4% | 65K | 139K | 0.5x | 11.9M | Oil & Gas Production |
| CMCT | [TV](https://www.tradingview.com/chart/?symbol=CMCT) | $3.62 | +23.5% | +6.4% | $3.85 | +31.4% | 60K | 3.4M | 0.0x | 2.8M | Real Estate Investment Trusts |

### Evaluation notes

**Tradability and appearance counts:** New names **HTCR and TARA returned `tradable=true`**, active on Nasdaq, before their SIP/catalyst workups. SDEV's positive 21:30 check and the other prior positive checks carry forward. The unrounded scanner lists now establish **SORA 7**, **AMOD 6**, **ELUT 2**, **WCT 2**, and **SSM/SCKT/IPW/UONEK/SDEV/HTCR/TARA 1 each**. The current scanner readings add no appearance for SCKT or IPW. Regular-session sightings and prior below-threshold AH sightings add zero. Every current scanner Total% is below +150%. Float is recorded for learning; TARA's 52.2M float is not an independent exclusion.

**SIP verification:** All 34 tradable names in the expanded pipeline were pulled with `broker.js bars SYM --tf 5Min --start 2026-10-01T20:00:00Z --limit 300 --feed sip --json`. Explicit SIP requests succeeded, and every response had `next_page_token=null`; no IEX volume was substituted. Active names returned newest bars starting at **18:15 ET**, consistent with the free-tier delay. Sparse names have older last trades, detailed below. Prices, highs, volumes, VWAPs, and trade counts used for decisions come from SIP. Yahoo's later AH timeline was used for shape only. None of the checked scanner levels requires a bad-print rejection.

| Ticker | Verified AH shares | Trades | SIP AH high / bar start ET | Latest SIP close | Off high | Latest bar shares / trades |
|--------|--------------------|--------|---------------------------|------------------|----------|---------------------------|
| AMOD | 9,831,002 | 50,048 | $2.0999 / 18:10 | $1.9900 | -5.2% | 743,205 / 3,652 |
| SORA | 4,980,123 | 56,510 | $3.64 / 16:05 | $3.0600 | -15.9% | 29,554 / 307 |
| SDEV | 3,165,731 | 19,958 | $4.19 / 18:15 | $4.1600 | -0.7% | 261,719 / 1,886 |
| HTCR | 222,649 | 2,886 | $2.466 / 18:15 | $2.3900 | -3.1% | 52,054 / 638 |
| TARA | 171,459 | 8 | $3.07 / 17:55 | $3.0700 | 0.0% | 100 / 1 |

**AMOD — skip Day% failure; DEAD-CAT-OVERRIDE WATCH.** Since 00:00, scanner AH% rises **+32.5% → +72.6%**, price **$1.55 → $2.02**, Total% **+0.0% → +30.3%**, and discovery volume **4.8M → 8.3M**. SIP adds **3,931,074 shares / 19,170 trades** since the prior verification. At 18:05, 18:10, and 18:15, closes are **$1.8612 → $2.0200 → $1.9900**, VWAP rises **$1.848713 → $1.938607 → $1.962797**, and volume is **609,739 → 805,622 → 743,205 shares**, with **2,928 → 3,704 → 3,652 trades**. The later high at 18:10 replaces the former $1.69 high. This is substantial real accumulation and a BUILD followed by a shallow pullback. The scanner's $2.02 is corroborated by the 18:10 bar; the normal SIP delay does not establish a bad print. Yahoo's later shape shows further easing after the surge, so the verification does not claim an executable scan-minute price. **Day -24.5% still blocks entry.** Record **DEAD-CAT-OVERRIDE WATCH**, hypothetical scanner entry **$2.02 at 00:30 CEST / 18:30 ET**, Total **+30.3%**, for morning measurement. This continues the rising-AH% recovery above the $1.17 regular close; no position was opened.

**SORA — skip FIRST-BAR-SPIKE; participation continues to thin.** Scanner AH% eases **+28.8% → +25.8%**, price **$3.09 → $3.02**, and Total% **+34.3% → +31.3%**, while discovery volume grows **3.6M → 3.8M**. SIP adds **183,060 shares / 1,724 trades** since 00:00. Its high remains **$3.64 in the 16:05 opening bar**, with no later new high. The last three bars have **21,323 / 208 trades**, **28,828 / 259**, and **29,554 / 307**, with VWAP falling **$3.089819 → $3.046593 → $3.027703**. CONFIRM-3 is **NO in all seven evaluations**. Apply the explicit first-bar-spike skip even within 20% of the high; current participation also fails the sustained-volume check. **FIRST-BAR-SPIKE WATCH hypothetical: $3.02 at 00:30 CEST / 18:30 ET**, Total **+31.3%**. Earlier hypotheticals remain historical observations.

**SDEV — watch/skip entry; first >10% appearance and stale book.** Scanner AH% rises **+6.6% → +12.6%**, price **$3.90 → $4.12**, and discovery volume **2.0M → 2.6M**. SIP verifies a real late surge: at 18:05–18:15, closes rise **$3.9601 → $4.1300 → $4.1600**, VWAP rises **$3.948444 → $4.063488 → $4.141201**, and activity rises from **78,457 shares / 351 trades** to **303,113 / 1,702** and **261,719 / 1,886**. The last bar makes a new $4.19 high and stays within 0.7% of it. The 0.1x scanner VRatio does not negate this real tape. **One qualifying AH snapshot fails the two-scan gate**, and the quote below cannot establish current fillable liquidity. CONFIRM-3 PENDING is instrumentation only and does not itself block or downgrade this build. The scanner classifies SDEV as Pharmaceuticals: Major; company disclosures describe the former NovaBay business as an on-chain holding company focused on the Sky ecosystem, so track the crypto/stablecoin exposure as well.

**HTCR — skip entry; first appearance, thin recent tape, no verified ask.** Float **614K**, Packaged Software, Day **-3.7%**, and Total **+16.0%** are recorded. SIP corroborates the $2.32 scanner level and shows a later high, with closes **$2.27 → $2.30 → $2.39** and rising VWAP in the last three bars. However, those bars contain only **29,631 / 343 trades**, **58,362 / 365**, and **52,054 / 638**. This is real trading but does not meet the accumulating hundreds-of-thousands of shares / thousands of trades per bar required for entry; rising price alone is insufficient. The **one-appearance gate** also fails. Both quote checks return **ask $0.00 x0**, so no fillable ask is verified. That stale quote cannot erase the real SIP trades or establish a bad print.

**TARA — skip thin/not-accumulating tape; first appearance.** SIP contains **171,359 shares / 7 trades at 16:00**, all at the $2.76 regular close, then **one 100-share trade at $3.07 at 17:55**. There is no multi-bar momentum accumulation; almost all displayed volume is at the closing level. The scanner's $3.07 did trade, so this is an isolated print rather than a proven erroneous price. Its last SIP trade is **35 minutes before the snapshot**, and its book is also stale; neither source establishes a current executable level. The one-appearance gate fails independently. Float **52.2M**, Day **-9.5%**, Total **+0.7%**, and the pharmaceutical sector are tracked without a float exclusion.

**Catalysts:** Carry AMOD **Grade D** from the verified October 1 SEC 8-K, accepted **11:30:52 (EDGAR displayed time)**, linked and described at 22:30. The disclosure covers the September 30 PIPE closing and warrants; its scanner float remains potentially stale. Carry SORA **Grade C** from the verified October 1 GlobeNewswire release at **16:05 ET / 22:05 CEST**, linked at 22:25, for the non-binding Plume memorandum. No undated headline was used to change either grade.

Four structured `websearch search` calls per newly above-threshold workup covered (1) today's earnings, (2) same-day newswire/company releases, (3) same-day SEC 8-K filings, and (4) a Tavily follow-up:

- **HTCR, Grade None — no catalyst found.** [August 13 Q2 earnings](https://www.globenewswire.com/news-release/2026/08/13/3344511/0/en/heartcore-reports-second-quarter-2026-financial-results.html) are background. A search surfaced a CMS/SaaS correction-notice headline without a verified release date/time; it remains an unresolved possible driver and is not graded. The filing index surfaced September 25 as its latest 8-K, outside the fresh-news window.
- **SDEV, Grade None — no catalyst found.** The [primary Q2 earnings exhibit](https://www.sec.gov/Archives/edgar/data/1389545/000143774926025172/ex_995199.htm) is dated **July 31**, and the [unusual-trading 8-K](https://www.stocktitan.net/sec-filings/SDEV/8-k-stablecoin-development-corp-reports-material-event-1268cc9fec81.html) is dated **September 29**. Both are background. Same-day trading commentary describes price action without establishing a new company event; no fresh operational catalyst is graded.
- **TARA, Grade None — no catalyst found.** Searches surfaced prior quarterly results and clinical-program updates. The [company/news index](https://www.stocktitan.net/overview/TARA) lists ADVANCED-2 enrollment and THRIVE-3 interim results as **October 1–December 31 Q4 windows**, which are anticipated milestones rather than announcements today. No timestamped same-day result, earnings release, or material filing was verified.

Searches stop at four calls per workup. No-catalyst is a concern to document, not an entry skip reason. Search indexes do not prove that no newer filing exists.

**Quote freshness and liquidity:** All eight quotes were checked twice and stayed unchanged:

```text
AMOD  bid $1.31 x100  ask $1.34 x100  @ 2026-10-01T20:58:48.514738532Z
SORA  bid $1.93 x100  ask $2.78 x100  @ 2026-10-01T20:00:00.60007104Z
SDEV  bid $3.64 x200  ask $3.66 x200  @ 2026-10-01T19:59:51.902231575Z
HTCR  bid $1.65 x100  ask $0.00 x0  @ 2026-10-01T20:00:03.171830189Z
TARA  bid $2.27 x100  ask $3.30 x100  @ 2026-10-01T20:00:01.034555123Z
SCKT  bid $0.46 x100  ask $0.00 x0  @ 2026-10-01T20:00:02.143954291Z
IPW  bid $0.95 x100  ask $1.37 x100  @ 2026-10-01T20:00:02.084910545Z
ELUT  bid $0.85 x300  ask $1.01 x100  @ 2026-10-01T20:57:24.346040236Z
```

AMOD's quote is about **91 minutes old**, ELUT's **93 minutes old**, and the others **150 minutes old** at the snapshot. **Current fillable liquidity is unconfirmed for all eight**. HTCR and SCKT additionally have no sized ask from this source. No sizing price can be taken from these frozen quotes. Their divergence from later SIP trades is source staleness, not evidence of bad prints. The independent entry blocks above remain in effect.

**Instrumentation (verbatim; log-only):** Outputs preserve the 18:30 scan cutoff. SCKT and IPW were also instrumented because the final cross-check finds historical SIP levels above 10%. Standalone detector verdicts do not grade, rank, or determine entry decisions. SORA's separate first-bar-spike rule uses its opening-high trajectory and repeated NO condition.

```text
AMOD 2026-10-01  SPIKE  16:15ET  +15%  $1.35  366 trades / 64k sh  (first co-spike bar) (as-of 18:30ET)
AMOD 2026-10-01  CONFIRM-3  NO ignition 16:15ET failed third-bar hold/volume as-of 18:30ET
SORA 2026-10-01  SPIKE  16:06ET  +52%  $3.64  243 trades / 17k sh  (first co-spike bar) (as-of 18:30ET)
SORA 2026-10-01  CONFIRM-3  NO no local-volume new-high ignition as-of 18:30ET
SDEV 2026-10-01  NO-SPIKE  peak +13% @18:16ET  (no bar cleared +15% on a volume co-spike) (as-of 18:30ET)
SDEV 2026-10-01  CONFIRM-3  PENDING ignition 18:10ET; waiting for third bar as-of 18:30ET
HTCR 2026-10-01  NO-SPIKE  peak +28% @18:16ET  (no bar cleared +15% on a volume co-spike) (as-of 18:30ET)
HTCR 2026-10-01  CONFIRM-3  NO ignition 17:55ET failed third-bar hold/volume as-of 18:30ET
TARA 2026-10-01  NO-SPIKE  peak +11% @17:59ET  (no bar cleared +15% on a volume co-spike) (as-of 18:30ET)
TARA 2026-10-01  CONFIRM-3  NO no local-volume new-high ignition as-of 18:30ET
SCKT 2026-10-01  SPIKE  16:18ET  +20%  $0.65  1981 trades / 1068k sh  (first co-spike bar) (as-of 18:30ET)
SCKT 2026-10-01  CONFIRM-3  NO ignition 16:15ET failed third-bar hold/volume as-of 18:30ET
IPW 2026-10-01  SPIKE  17:18ET  +27%  $1.45  366 trades / 46k sh  (first co-spike bar) (as-of 18:30ET)
IPW 2026-10-01  CONFIRM-3  YES ignition 17:15ET 148.8x; confirmed 17:25ET $1.40 as-of 18:30ET
```

### Final-scan feed-lag cross-check

**Coverage:** Cross-checked **all 32 tradable names from the prior 40-name pipeline**, including all 20 tradable regular-session watches, plus new HTCR/TARA in the workup above. EVOL, GBLRF, MHUAF, CRMZ, FNFI, SGRP, LTCEF, and EJH remain **untradable (carried)**; the early broker-block rule prevents repeating their SIP or catalyst workups. Tonight's complete pipeline is now **42 names**. The table records the latest available SIP bar, its close and volume/trades, and AH change measured from the completed regular-close reference. For scanner names that close is already recorded above; for omitted names Yahoo helper metadata supplies the reference only, so these percentages are diagnostic and are not exact executable prices or retrospective scanner counts.

**SCKT and IPW — higher SIP levels, insufficient current volume for rescue.** SCKT's 18:15 SIP close **$0.5991 / +10.94% AH** exceeds the scanner's +9.3%, but recent bars have only **22,202–45,739 shares / 75–105 trades**. Its latest close is 8.4% below the $0.6539 16:15 high, and the later Yahoo shape stays flat at the lower base. IPW's 18:15 SIP close **$1.32 / +15.79% AH** exceeds the scanner's +7.9%, but recent bars contain only **3,007–19,186 shares / 29–98 trades**; the latest close remains 11.8% below its $1.4969 17:15 high. A sparse rebound and CONFIRM-3 YES do not establish current volume-backed BUILD. Both fail the thin/not-accumulating gate and have stale books; SCKT has no sized ask. Preserve the higher historical SIP readings without claiming a current liquid >10% rescue or adding an earlier scanner appearance. Their prior Grade None concerns carry forward; neither was skipped for no catalyst.

**ELUT — omitted because the surge has faded.** SIP now totals **5,719,032 shares / 20,071 trades**, adding **916,863 / 2,548** since 00:00. The latest close **$0.8206** is only **+2.57% above $0.80** and **25.4% below** the $1.10 16:45 high. Recent closes ease $0.8421 → $0.8158 → $0.8206 with volume 336,407 → 95,909 → 45,081 and trades 710 → 194 → 149. This is a faded spike, not a hold. The earlier Grade C cash-receipt catalyst is unchanged, dated October 1 at 16:45 ET. No entry rescue applies.

**SSM — update the earlier opening-high observation.** SIP establishes a later **$2.59 high at 17:00**, exceeding its former $2.49 opening high. The old first-bar-spike condition therefore no longer applies; its earlier hypothetical watches remain historical measurements. Its latest close **$2.32 / +4.98% AH** is below threshold, with recent volume/trades declining to 92,839 / 503. It retains only one scanner-confirmed >10% appearance and does not qualify for entry.

**Other absent names:** No omitted name has a latest SIP close above 10% on substantial current accumulation. GIPR's latest close is +9.07% with only 43,256 shares / 69 trades. MTNE returns no SIP bars and no Yahoo AH history, so its final level remains unverified rather than flat or faded. Older final bars on sparse names do not establish a current quote.

| Ticker | Last SIP bar ET | SIP close | AH% reference | Last bar shares / trades |
|--------|-----------------|-----------|---------------|--------------------------|
| AGIG | 17:10 | $1.0201 | +5.82% | 664 / 1 |
| AISP | 18:15 | $2.2450 | +1.13% | 1,751 / 14 |
| AMOD | 18:15 | $1.9900 | +70.09% | 743,205 / 3,652 |
| ATOS | 16:00 | $2.2700 | +0.00% | 1,795 / 4 |
| BIRD | 18:15 | $3.4400 | -1.43% | 733 / 8 |
| BTTC | 18:15 | $0.6399 | +1.09% | 33,461 / 89 |
| CMCT | 18:05 | $3.8500 | +6.35% | 108 / 1 |
| DMRC | 17:35 | $6.6300 | -1.92% | 125 / 2 |
| ELUT | 18:15 | $0.8206 | +2.57% | 45,081 / 149 |
| GIPR | 18:15 | $0.4930 | +9.07% | 43,256 / 69 |
| INSG | 18:10 | $4.3400 | -0.69% | 114 / 8 |
| IPW | 18:15 | $1.3200 | +15.79% | 19,186 / 98 |
| KPTI | 18:15 | $0.8981 | +3.59% | 9,500 / 2 |
| KUST | 16:20 | $4.4300 | +0.23% | 100 / 1 |
| LONA | 18:15 | $4.3400 | -0.91% | 158 / 6 |
| MEDS | 18:15 | $4.1000 | +0.99% | 4,226 / 46 |
| MTNE | No bars | Unverified | Unverified | 0 / 0 |
| MVST | 18:15 | $0.6890 | +4.39% | 2,000 / 1 |
| MYPS | 16:00 | $4.7200 | +0.00% | 225 / 1 |
| NAMM | 18:15 | $1.2700 | -2.31% | 19,255 / 16 |
| NCI | 18:15 | $1.0700 | +0.94% | 17,332 / 23 |
| NCPL | 18:15 | $1.5100 | -2.58% | 4,244 / 9 |
| NXL | 18:15 | $7.1009 | -5.95% | 11,354 / 181 |
| QNME | 18:15 | $0.5700 | +5.95% | 6,319 / 30 |
| SCKT | 18:15 | $0.5991 | +10.94% | 36,800 / 86 |
| SDEV | 18:15 | $4.1600 | +13.66% | 261,719 / 1,886 |
| SES | 18:15 | $0.8287 | +1.56% | 10,259 / 41 |
| SORA | 18:15 | $3.0600 | +27.50% | 29,554 / 307 |
| SSM | 18:15 | $2.3200 | +4.98% | 92,839 / 503 |
| UONEK | 18:00 | $3.8400 | +5.49% | 100 / 1 |
| VEEA | 18:15 | $3.4200 | -1.44% | 3,962 / 70 |
| WCT | 18:15 | $1.4800 | -11.38% | 16,722 / 84 |

**Final-scan gate-block instrumentation:** No name qualifies for **FINAL-SCAN-GATE-BLOCK**. SDEV has a real late 18:10 surge but its CONFIRM-3 is PENDING and its book is frozen at the regular close; it is not blocked solely by the two-AH-scan rule. HTCR also fails the volume and ask-book checks, and TARA fails accumulation. No entry is made from a first final-scan appearance. No ceiling-override watch is due; every candidate is below +150% Total%. Chase-cap and multi-session-runner entry annotations are not applicable because no entry or fill occurred.

**Fills and daily email:** Alpaca `positions --json` returned `[]`, `orders open` returned `No open orders.`, and `orders all --json` contains no October 1 entry fill. No fill requires an OPEN_POSITIONS entry. Daily email: report the final no-entry result; AMOD's **$2.02 DEAD-CAT-OVERRIDE WATCH** with real volume and the Day% block; SORA's **$3.02 FIRST-BAR-SPIKE WATCH**; SDEV's real late surge blocked by one appearance and stale book; HTCR's thin tape/zero ask; TARA's isolated 100-share print; SCKT/IPW's higher historical SIP readings without current accumulation; ELUT's deeper fade; and SSM's later-high correction. Include the frozen-quote limitation and HTCR's unresolved catalyst headline. **No question requires Juan's input.**

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|

No entries through the final 00:30 CEST scan (18:30 ET on October 1). AMOD has six qualifying AH appearances and a real late BUILD, but Day -24.5% blocks entry. SORA has seven and retains its first-bar-spike block. SDEV, HTCR, and TARA have one each, with stale-book or volume blocks. SCKT/IPW have higher historical SIP levels but insufficient current accumulation; ELUT has faded below threshold. The AMOD and SORA hypothetical watches are recorded in the scan notes and are not fills. Alpaca has no open positions or orders; OPEN_POSITIONS remains consistent with the broker.
