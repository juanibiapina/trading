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

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|

No entries from the 21:30, 22:00, 22:05, 22:10, 22:15, 22:20, 22:25, 22:30, or 22:45 CEST scans. All precede the 23:00 CEST entry window. SORA has three qualifying AH appearances with a FIRST-BAR-SPIKE WATCH and stale book. AMOD has two but fails the Day% rule; its volume-backed recovery is recorded as a DEAD-CAT-OVERRIDE WATCH hypothetical. WCT has two but fails the Day% and trajectory rules. SSM has one qualifying appearance with an opening-spike fade. Alpaca has no open positions or orders at the 22:45 verification.
