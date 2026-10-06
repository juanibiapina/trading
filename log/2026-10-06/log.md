## Position Evaluation — 12:44 CEST

**Result:** No open positions to evaluate. Alpaca paper account `PA37U2Y192A7` is active and trading is not blocked. Equity and cash are both **$99,721.90**; buying power is **$398,887.60**.

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| — | — | — | — | — | — | — | — | Alpaca reports no open positions. |

**Actions taken:**
- Created today's log before reading it. The first `sync-repo.sh` run failed with `fatal: Cannot rebase onto multiple branches`; a fresh `git fetch origin` followed by `git pull --ff-only` reported "Already up to date" and local `main` matches `origin/main` (`4b7b48f`).
- Checked `broker.js account`, `positions --json`, `orders all`, and `orders open`; positions returned `[]` and no orders are open. The latest fills (TOPS buy $1.40 / sell $0.70) are already closed.
- Confirmed `OPEN_POSITIONS.md` matches Alpaca's empty position state; no reconciliation needed.
- No position prices, P&L, holding days, peaks, or catalyst grades apply. No sells or trailing stop updates required.
- Daily email: report the empty portfolio and completed evaluation. No items require Juan's input.

## Position Evaluation — 14:30 CEST

**Result:** No open positions to evaluate. Alpaca paper account `PA37U2Y192A7` is active; equity and cash are both **$99,721.90**, buying power **$398,887.60**.

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| — | — | — | — | — | — | — | — | Alpaca reports no open positions. |

**Actions taken:**
- `sync-repo.sh` ran cleanly ("Already up to date").
- Checked `broker.js account`, `positions --json`, `orders all`, and `orders open`: positions `[]`, no open orders. Latest fills (TOPS buy $1.40 / sell $0.70) are already closed.
- `OPEN_POSITIONS.md` matches Alpaca's empty position state; no reconciliation needed.
- No sells or trailing stop updates required. Nothing for the daily email needs Juan's input.

## Scan 21:30 CEST (3:30 PM ET)

**Decision:** Watch — pending AH confirmation. No paper orders submitted; this scan precedes the 16:00 ET AH open and the 23:00 CEST entry window.

`python3 scripts/scan.py --all` ran at 15:30:23 ET (21:30:23 CEST / 19:30:23 UTC) in the REGULAR session and returned 26 candidates. The US trading date is 2026-10-06. This is today's first discovery scan; regular-session appearances add zero qualifying AH scans. Prices and volumes below are regular-session scanner readings. AH change, AH volume, and AH VRatio are not available yet, so the scanner printed no `Supplementary AH-change-only` or `AH >10% at this snapshot (unrounded)` line.

| Ticker | Chart | Price | Day% | 5mVol | Avg5m | IRVol | VChg% | Float | Industry |
|--------|-------|-------|------|-------|-------|-------|-------|-------|----------|
| SMXT | [TV](https://www.tradingview.com/chart/?symbol=SMXT) | $3.29 | +38.7% | 44K | 67K | 382.5 | -16.0% | 3.5M | Engineering & Construction |
| DLXY | [TV](https://www.tradingview.com/chart/?symbol=DLXY) | $2.38 | +21.1% | 23K | 10K | 51.8 | +112.4% | 1.0M | Wholesale Distributors |
| EVOL | [TV](https://www.tradingview.com/chart/?symbol=EVOL) | $0.60 | +0.0% | 11K | 1K | 40.9 | +3564.0% | 3.7M | Information Technology Services |
| JONE | [TV](https://www.tradingview.com/chart/?symbol=JONE) | $9.81 | -0.1% | 18K | 67K | 34.8 | -12.0% | 21.0M | Financial Conglomerates |
| AIFA | [TV](https://www.tradingview.com/chart/?symbol=AIFA) | $7.50 | +27.6% | 12K | 8K | 29.6 | -16.4% | 3.3M | Movies/Entertainment |
| MHUAF | [TV](https://www.tradingview.com/chart/?symbol=MHUAF) | $7.00 | +0.0% | 5K | 631 | 28.7 | +4955.0% | 613K | Medical Specialties |
| XSLL | [TV](https://www.tradingview.com/chart/?symbol=XSLL) | $10.00 | -0.1% | 129K | 69K | 25.1 | +0.9% | 20.9M | Financial Conglomerates |
| AIIO | [TV](https://www.tradingview.com/chart/?symbol=AIIO) | $1.16 | +4.5% | 42K | 59K | 22.0 | +171.2% | 106.7M | Motor Vehicles |
| ARKR | [TV](https://www.tradingview.com/chart/?symbol=ARKR) | $4.32 | -4.0% | 14K | 7K | 21.4 | +5.5% | 1.8M | Restaurants |
| APMC | [TV](https://www.tradingview.com/chart/?symbol=APMC) | $9.97 | +0.1% | 25K | 12K | 21.1 | +0.1% | 16.0M | Financial Conglomerates |
| VNPKF | [TV](https://www.tradingview.com/chart/?symbol=VNPKF) | $0.56 | +11.7% | 25K | 11K | 13.6 | +518.5% | 56.3M | Chemicals: Agricultural |
| WTLLF | [TV](https://www.tradingview.com/chart/?symbol=WTLLF) | $3.85 | -3.0% | 10K | 10K | 12.2 | +300.0% | 7.0M | Engineering & Construction |
| NWINF | [TV](https://www.tradingview.com/chart/?symbol=NWINF) | $0.82 | -0.9% | 19K | 3K | 11.3 | +18800.0% | 29.4M | Beverages: Alcoholic |
| HUHU | [TV](https://www.tradingview.com/chart/?symbol=HUHU) | $3.95 | -10.2% | 9K | 6K | 11.0 | -49.7% | 7.3M | Information Technology Services |
| KHDHF | [TV](https://www.tradingview.com/chart/?symbol=KHDHF) | $2.33 | +3.6% | 8K | 1K | 10.9 | +866.3% | 5.5M | Construction Materials |
| MOBX | [TV](https://www.tradingview.com/chart/?symbol=MOBX) | $1.12 | +72.3% | 2K | 781K | 134.9 | -99.2% | 15.8M | Semiconductors |
| OLOX | [TV](https://www.tradingview.com/chart/?symbol=OLOX) | $1.43 | +62.5% | 309 | 131K | 279.2 | -99.8% | 1.3M | Building Products |
| APUS | [TV](https://www.tradingview.com/chart/?symbol=APUS) | $7.16 | +56.0% | 100 | 175K | 4.8 | -99.9% | 563K | Biotechnology |
| IPDN | [TV](https://www.tradingview.com/chart/?symbol=IPDN) | $4.53 | +46.1% | 3K | 104K | 23.2 | -95.9% | 476K | Commercial Printing/Forms |
| XHLD | [TV](https://www.tradingview.com/chart/?symbol=XHLD) | $0.60 | +46.0% | 100 | 220K | 36.8 | -100.0% | 10.5M | Miscellaneous Commercial Services |
| PMI | [TV](https://www.tradingview.com/chart/?symbol=PMI) | $8.54 | +23.2% | 12K | 16K | 4.1 | +311.2% | 1.4M | Medical Specialties |
| FFR | [TV](https://www.tradingview.com/chart/?symbol=FFR) | $1.39 | +23.0% | 9K | 10K | 1.0 | -67.5% | 7.1M | Packaged Software |
| BESS | [TV](https://www.tradingview.com/chart/?symbol=BESS) | $2.25 | +21.0% | 627 | 1K | 2.3 | +527.0% | 4.4M | Electrical Products |
| JAGX | [TV](https://www.tradingview.com/chart/?symbol=JAGX) | $5.62 | +18.9% | 1K | 35K | 2.7 | -93.7% | 1.7M | Pharmaceuticals: Major |
| MODD | [TV](https://www.tradingview.com/chart/?symbol=MODD) | $2.71 | +17.8% | 100 | 790 | 2.2 | +0.0% | 8.8M | Medical Specialties |
| OFS | [TV](https://www.tradingview.com/chart/?symbol=OFS) | $4.17 | +17.0% | 200 | 5K | 13.2 | -96.1% | 13.3M | Investment Trusts/Mutual Funds |

A run four seconds earlier (15:30:19 ET) returned 28 hits: the same names plus **KAPA** ($1.19, Day -23.2%, 13K 5mVol, IRVol 97.0, float 2.2M, Pharmaceuticals: Major) and **RUBI** ($0.65, Day -7.1%, 11K 5mVol, IRVol 23.6, float 1.8M, Marine Shipping). Both are carried as watch names.

### Evaluation notes

**Watch — pending AH confirmation (22 names):** SMXT, KAPA, DLXY, JONE, AIFA, XSLL, RUBI, AIIO, ARKR, APMC, HUHU, MOBX, OLOX, APUS, IPDN, XHLD, PMI, FFR, BESS, JAGX, MODD, OFS. `broker.js tradable` returned `tradable=true` for each. Float and industry are recorded for pattern tracking only.

**Untradable — carry forward (6 names):** EVOL, MHUAF, VNPKF, WTLLF, NWINF, KHDHF returned `tradable=false` (all OTC). Carry these broker blocks into later scans without repeating SIP verification or catalyst searches. None is an AH-qualified-but-untradable entry yet.

**Trajectory observations:** SMXT (+38.7%, IRVol 382.5, 44K latest 5-min volume), DLXY (+21.1%, VChg +112.4%), and PMI (+23.2%, VChg +311.2%) are the day movers still trading actively into the close. The biggest day movers (MOBX +72.3%, OLOX +62.5%, APUS +56.0%, IPDN +46.1%, XHLD +46.0%) show VChg between -95.9% and -100.0% on latest 5-min volumes of 100 to 3K shares. These regular-session fields do not establish real AH accumulation or an AH BUILD/HOLD.

**Day% guard:** KAPA (-23.2%) is below -15%; an AH bounce would be a dead-cat skip unless it reclaims above its regular close and builds across ≥2 AH scans (DEAD-CAT-OVERRIDE WATCH). HUHU (-10.2%) is above the -15% line. Recheck every Day% against the completed regular close before any entry.

**Multi-session context (for MULTI-SESSION-RUNNER tagging if they qualify in AH):** OLOX is the October 5 AH→PM winner (`WINNERS_TRACKING.md`: $0.88 close → $2.245 PM peak); today's +62.5% is day 2 of that move. JAGX had >10% AH at three October 5 checkpoints in the SIP reconstruction; today's +18.9% is from the $4.73 October 5 close. APUS, AIFA, PMI, AIIO, and RUBI appeared in the October 5 morning sweeps.

**Price-basis note:** RUBI's -7.1% uses the stock-dividend-adjusted October 5 close of $0.70 ($1.05 raw ÷ 1.5). Against the raw $1.05 close, $0.65 would read as -38%. Use the adjusted basis if RUBI becomes an AH candidate.

## Scan 22:00 CEST (4:00 PM ET)

**Decision:** Observe — no candidates found. No paper orders submitted; entries begin at the 23:00 CEST scan (17:00 ET).

`python3 scripts/scan.py --all` ran at 16:00:17 ET (22:00:17 CEST / 20:00:17 UTC) in the AFTERHOURS session and returned 0 hits. A rerun at 16:02:05 ET also returned 0 hits with the same two lines. The US trading date is 2026-10-06.

No candidates found.

```text
  Supplementary AH-change-only (>15%, not in volume pass): none
  AH >10% at this snapshot (unrounded): none
```

### Evaluation notes

**AH appearance count:** This is tonight's first AH scan. No ticker has a scanner-confirmed >10% AH appearance; the 21:30 regular-session appearances do not count toward the two-AH-scan entry gate. No candidate requires catalyst research, SIP verification, spike-bar, CONFIRM-3, volume-context, or book-check instrumentation at this snapshot.

**Carry forward:** Keep all 28 names from the 21:30 watchlist in tonight's pipeline, including the KAPA dead-cat guard (Day -23.2%) and the OLOX day-2 multi-session tag. EVOL, MHUAF, VNPKF, WTLLF, NWINF, and KHDHF remain untradable (carried). This opening scan returned no price or volume evidence for the watchlist, so absence does not establish an AH fade. AH volume verification starts at `2026-10-06T20:00:00Z`.

**Daily email:** No item from this scan requires Juan's input.

## Scan 22:05 CEST (4:05 PM ET)

**Decision:** Observe — no candidates found. No paper orders submitted; entries begin at the 23:00 CEST scan (17:00 ET).

`python3 scripts/scan.py --all` ran at 16:05:15 ET (22:05:15 CEST / 20:05:15 UTC) in the AFTERHOURS session and returned 0 hits. The US trading date is 2026-10-06.

No candidates found.

```text
  Supplementary AH-change-only (>15%, not in volume pass): none
  AH >10% at this snapshot (unrounded): none
```

### Evaluation notes

**AH appearance count:** This is tonight's second AH scan, and neither AH scan has a scanner-confirmed >10% AH appearance. No candidate requires catalyst research, SIP verification, spike-bar, CONFIRM-3, volume-context, or book-check instrumentation at this snapshot.

**Carry forward:** Keep all 28 names from the 21:30 watchlist in tonight's pipeline, including the KAPA dead-cat guard (Day -23.2%) and the OLOX day-2 multi-session tag. EVOL, MHUAF, VNPKF, WTLLF, NWINF, and KHDHF remain untradable (carried). Five minutes into AH, the scanner still returned no price or volume evidence for the watchlist, so absence does not establish an AH fade.

**Daily email:** No item from this scan requires Juan's input.

## Scan 22:10 CEST (4:10 PM ET)

**Decision:** Observe — no candidates found. No paper orders submitted; entries begin at the 23:00 CEST scan (17:00 ET).

`python3 scripts/scan.py --all` ran at 16:10:16 ET (22:10:16 CEST / 20:10:16 UTC) in the AFTERHOURS session and returned 0 hits. The US trading date is 2026-10-06.

No candidates found.

```text
  Supplementary AH-change-only (>15%, not in volume pass): none
  AH >10% at this snapshot (unrounded): none
```

### Evaluation notes

**AH appearance count:** This is tonight's third AH scan, and none of the three AH scans (22:00, 22:05, 22:10) has a scanner-confirmed >10% AH appearance. No candidate requires catalyst research, SIP verification, spike-bar, CONFIRM-3, volume-context, or book-check instrumentation at this snapshot.

**Carry forward:** Keep all 28 names from the 21:30 watchlist in tonight's pipeline, including the KAPA dead-cat guard (Day -23.2%) and the OLOX day-2 multi-session tag. EVOL, MHUAF, VNPKF, WTLLF, NWINF, and KHDHF remain untradable (carried). Ten minutes into AH, the scanner still returned no price or volume evidence for the watchlist, so absence does not establish an AH fade.

**Daily email:** No item from this scan requires Juan's input.

## Scan 22:15 CEST (4:15 PM ET)

**Decision:** Observe — no candidates found. No paper orders submitted; entries begin at the 23:00 CEST scan (17:00 ET).

`python3 scripts/scan.py --all` ran at 16:15:16 ET (22:15:16 CEST / 20:15:16 UTC) in the AFTERHOURS session and returned 0 hits. The US trading date is 2026-10-06. Repository sync completed before scanning.

No candidates found.

```text
  Supplementary AH-change-only (>15%, not in volume pass): none
  AH >10% at this snapshot (unrounded): none
```

### Evaluation notes

**AH appearance count:** This is tonight's fourth AH scan, and none of the four AH scans (22:00, 22:05, 22:10, 22:15) has a scanner-confirmed >10% AH appearance. No candidate requires catalyst research, SIP verification, spike-bar, CONFIRM-3, volume-context, or book-check instrumentation at this snapshot.

**Feed timing:** Four empty opening scans match prior nights. On 2026-10-01 the scanner also returned 0 hits from 22:00 through 22:15 CEST and produced its first AH hit (WCT) at 22:20 CEST, so the empty result here is consistent with the TradingView postmarket feed delay at the open.

**Carry forward:** Keep all 28 names from the 21:30 watchlist in tonight's pipeline, including the KAPA dead-cat guard (Day -23.2%) and the OLOX day-2 multi-session tag. EVOL, MHUAF, VNPKF, WTLLF, NWINF, and KHDHF remain untradable (carried). Fifteen minutes into AH, the scanner still returned no price or volume evidence for the watchlist, so absence does not establish an AH fade. AH volume verification starts at `2026-10-06T20:00:00Z`.

**Daily email:** No item from this scan requires Juan's input.

## Scan 22:20 CEST (4:20 PM ET)

**Decision:** No entry. Tonight's first AH hits: VCIG, NCPL, SXTC, and ICMB each have **1** qualifying >10% AH appearance (2 required), and entries begin at 23:00 CEST. VCIG is the only name with heavy real volume, a fresh two-sided book, and Day% above -15%; its AH high is in the opening window with CONFIRM-3 NO, so it is a FIRST-BAR-SPIKE WATCH unless a later volume-backed high appears. No paper orders submitted.

`python3 scripts/scan.py --all` ran at 16:20:13 ET (22:20:13 CEST / 20:20:13 UTC) in the AFTERHOURS session and returned 5 hits. The US trading date is 2026-10-06. Repository sync completed before the scan. Scanner readings are discovery evidence; SIP and quote checks follow.

```text
  Supplementary AH-change-only (>15%, not in volume pass): ICMB
  AH >10% at this snapshot (unrounded): ICMB, NCPL, SXTC, VCIG
```

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| VCIG | [TV](https://www.tradingview.com/chart/?symbol=VCIG) | $1.41 | +54.8% | +19.9% | $1.69 | +85.5% | 3.1M | 1.6M | 2.0x | 1.0M | Miscellaneous Commercial Services |
| YFOR | [TV](https://www.tradingview.com/chart/?symbol=YFOR) | $1.13 | -18.1% | +7.1% | $1.21 | -12.3% | 569K | 547K | 1.0x | 3.9M | Miscellaneous Commercial Services |
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $1.09 | -17.4% | +11.9% | $1.22 | -7.6% | 69K | 14.3M | 0.0x | 4.4M | Miscellaneous Commercial Services |
| SXTC | [TV](https://www.tradingview.com/chart/?symbol=SXTC) | $1.25 | -39.9% | +11.2% | $1.39 | -33.2% | 65K | 481K | 0.1x | 1.0M | Pharmaceuticals: Major |
| ICMB | [TV](https://www.tradingview.com/chart/?symbol=ICMB) | $0.72 | +2.1% | +20.4% | $0.87 | +22.9% | 1K | 38K | 0.0x | 12.1M | Financial Conglomerates |

### Evaluation notes

**Tradability:** `broker.js tradable` returned `tradable=true` (Nasdaq, active) for VCIG, NCPL, SXTC, ICMB, and YFOR before the SIP and catalyst workup. None of these names was in the 21:30 regular-session watchlist.

**SIP bars** (`broker.js bars SYM --tf 5Min --start 2026-10-06T20:00:00Z`, feed=sip). The newest bar starts 16:05 ET, about 15 minutes behind the scan, which matches the free-tier delay.

| Ticker | Bar ET | Open | High | Low | Close | Shares | VWAP | Trades |
|--------|--------|------|------|-----|-------|--------|------|--------|
| VCIG | 16:00 | $1.41 | $1.73 | $1.29 | $1.70 | 3,344,455 | $1.56 | 15,386 |
| VCIG | 16:05 | $1.69 | $1.86 | $1.61 | $1.85 | 3,445,449 | $1.75 | 17,205 |
| SXTC | 16:00 | $1.25 | $1.65 | $1.25 | $1.40 | 75,597 | $1.44 | 478 |
| SXTC | 16:05 | $1.39 | $1.85 | $1.36 | $1.57 | 683,755 | $1.66 | 4,488 |
| NCPL | 16:00 | $1.09 | $1.28 | $1.09 | $1.24 | 71,987 | $1.20 | 261 |
| NCPL | 16:05 | $1.22 | $1.28 | $1.18 | $1.18 | 71,440 | $1.22 | 172 |
| ICMB | 16:00 | $0.87 | $0.87 | $0.76 | $0.87 | 1,537 | $0.81 | 47 |
| ICMB | 16:05 | $0.87 | $0.87 | $0.72 | $0.74 | 23,780 | $0.80 | 123 |

**VCIG — skip entry (gate and window); FIRST-BAR-SPIKE WATCH.** SIP shows **6.79M shares / 32,591 trades** in two bars, rising bar over bar, so the volume is real and accumulating. The scanner's $1.69 matches the 16:00 bar close and lags the tape. The AH high is **$1.86 (+31.9%) in the 16:05 bar**, inside the 16:00–16:15 opening window. Yahoo's timeline (shape only) shows $1.84 at 16:10, $1.71 at 16:15, and $1.76 at 16:21. The fresh IEX quote is `VCIG  bid $1.73 x100  ask $1.79 x200  @ 2026-10-06T20:22:07.258067163Z`, a sized two-sided book. At $1.76 the price is **5.4% below the high**, so it is holding within 20%, but no later volume-backed new high exists yet. Day +54.8% passes. Total% is +85.5% at the scanner price and about +93% at $1.76, under the +150% ceiling. Float 1.0M is recorded for pattern tracking.

- **Catalyst Grade C (dated, time unverified).** The [GlobeNewswire release dated October 6, 2026](https://www.globenewswire.com/news-release/2026/10/06/3375960/0/en/vci-global-launches-vgain-compute-ai-token-platform-expanding-into-ai-infrastructure-and-llm-services.html) announces the launch of the VGAIN Compute AI token platform at subsidiary V Gallant. It is a product-launch PR with no revenue figure. The search result showed it "38 minutes ago" at about 16:27 ET, which suggests release near the close, but the page extract has no timestamp. The release is from the current trading date. Background: a $125M equity facility and convertible-note financing reported September 29–30 (dilution overhang). Three of four searches used.
- **Prior activity:** SIP daily volume was 5.9M on October 2 and 1.6M on October 5, compared with 24K–66K in late September. The stock fell from $1.49 to $0.91 over those two sessions, so today's +54.8% is a rebound after a sell-off. It is not a MULTI-SESSION-RUNNER, and it fails the "first day of unusual activity" criterion.
- **FIRST-BAR-SPIKE WATCH:** hypothetical entry **$1.69 (scanner) at 22:20 CEST / 16:20 ET**; the fresh IEX ask at the same scan was $1.79. This is for morning measurement only, with no fill or position. If the opening-window high stands and CONFIRM-3 stays NO at 23:00, apply the first-bar-spike skip even though price holds within 20% of the high.

**SXTC — skip entry; Day% failure.** SIP volume jumped from 75,597 shares / 478 trades to **683,755 shares / 4,488 trades** in the 16:05 bar. That is real volume, ignited in the second bar. The AH high is **$1.85 (+48.0%) in the 16:05 bar**. Yahoo shows $1.63 at 16:10, $1.45 at 16:15, and $1.48 at 16:21, about **20% below the high**. The scanner's $1.39 matches the 16:00 bar close and lags. Day **-39.9%** fails the Day% above -15% rule. The AH price is above the $1.25 regular close, but DEAD-CAT-OVERRIDE WATCH requires AH% rising across ≥2 AH scans, which has not happened yet. CONFIRM-3 is PENDING (ignition 16:05 ET), so no first-bar-spike watch is assigned. The IEX quote is stale and empty (`SXTC  bid $1.05 x100  ask $0.00 x0  @ 2026-10-06T20:00:03.61384345Z`); the delayed SIP book was two-sided at 16:06:59 ET (see BOOK lines).

- **Catalyst Grade None — no catalyst found.** Four searches covered earnings, same-day press releases, 6-K filings, and a Tavily news search. Results were dated background only: a January 2026 registered direct offering, the February 3, 2026 1-for-150 reverse split, a most recent indexed SEC filing on September 17, 2026, and an undated "Announces Share Consolidation" headline. The daily closes fell four straight sessions, from $3.01 on September 30 to $1.25 today. No-catalyst is a documented concern, not a skip reason.

**NCPL — skip; thin drift and Day% failure.** SIP shows 71,987 shares / 261 trades, then 71,440 shares / 172 trades: tens of thousands of shares and hundreds of trades per bar, with VRatio 0.0x. This is thin, not accumulating. Price slipped from the $1.28 high to a $1.18 close; Yahoo shows $1.19 (+9.2%) at 16:20. The IEX quote is stale with no ask (`NCPL  bid $0.95 x100  ask $0.00 x0  @ 2026-10-06T20:00:03.614882635Z`). Day **-17.4%** also fails. NCPL is a recurring AH name (logged September 21, 23, 24, and 30), so it is not a first day of unusual activity.

- **Catalyst Grade None — no catalyst found.** Four searches found only background and negative items: a [Rosen Law Firm investigation release, October 6, 14:06 ET](https://www.globenewswire.com/news-release/2026/10/06/3375925/673/en/netcapital-investor-news-if-you-have-suffered-losses-in-netcapital-inc-nasdaq-ncpl-you-are-encouraged-to-contact-the-rosen-law-firm-about-your-rights.html) (shareholder solicitation, not an upside catalyst), the September 25 Nasdaq delinquency notice for late 10-Q/10-K filings, and an August Wells Notice statement.

**ICMB — skip; thin print.** The scanner's $0.87 (+20.4%) is the 16:00 bar's high on **1,537 shares / 47 trades**. The 16:05 bar traded 23,780 shares / 123 trades and closed at **$0.74 (+2.8%)**; Yahoo shows $0.75 at 16:20. SIP confirms $0.87 printed, so this is a thin print rather than a bad print, and volume is not accumulating. The IEX quote is stale and wide (`ICMB  bid $0.59 x100  ask $0.99 x100  @ 2026-10-06T20:00:01.890841022Z`). The name entered through the supplementary AH-change-only pass.

- **Catalyst Grade None — no catalyst found.** Four searches found only background: April 2026 NAV decline, dividend suspension, and strategic-alternatives review; the June 2 Work Genius exit 8-K; and May Q1 results. Nothing is dated October 6.

**FIRST-BAR-SPIKE WATCH (NCPL, ICMB):** Both AH highs are in the opening window (NCPL $1.28 at 16:00–16:05, ICMB $0.87 at 16:00), with CONFIRM-3 NO on the first evaluation. Hypothetical scanner entries: **NCPL $1.22 and ICMB $0.87 at 22:20 CEST / 16:20 ET**, for morning measurement only. Both are also thin-volume skips, so the watch adds a data point and does not change the decision.

**YFOR:** +7.1% AH, below the 10% instrumentation threshold. Day -18.1%. It is tracked for the final-scan cross-check only.

**Instrumentation (verbatim; log-only):**

```text
VCIG 2026-10-06  NO-SPIKE  peak +26% @16:05ET  (no bar cleared +15% on a volume co-spike) (as-of 16:20ET)
VCIG 2026-10-06  CONFIRM-3  NO no local-volume new-high ignition as-of 16:20ET
NCPL 2026-10-06  NO-SPIKE  peak +17% @16:03ET  (no bar cleared +15% on a volume co-spike) (as-of 16:20ET)
NCPL 2026-10-06  CONFIRM-3  NO no local-volume new-high ignition as-of 16:20ET
SXTC 2026-10-06  SPIKE  16:03ET  +32%  $1.65  135 trades / 30k sh  (first co-spike bar) (as-of 16:20ET)
SXTC 2026-10-06  CONFIRM-3  PENDING ignition 16:05ET; waiting for third bar as-of 16:20ET
ICMB 2026-10-06  SPIKE  16:04ET  +21%  $0.87  47 trades / 2k sh  (first co-spike bar) (as-of 16:20ET)
ICMB 2026-10-06  CONFIRM-3  NO no local-volume new-high ignition as-of 16:20ET
```

VCIG shows NO-SPIKE despite 3.3M+ shares per bar; the detector's 5x volume co-spike test likely compares against today's heavy regular-session volume (16.6M SIP shares). Record as a data point.

**Shared SIP volume context (`sip-ah-volume-v1`, log-only):** Prior trading date 2026-10-05 (a normal Monday session). Inputs archived as `log/2026-10-06/SYM-2220-volume-sip.json` (SIP, 5Min, raw, single page from `2026-10-05T20:00:00Z`); computed rows in `SYM-2220-volume-metric.json`. Every completed bar is in warmup, so local and prior-peak ratios are unknown. Prior-session coverage is incomplete for all four (VCIG 41/48, NCPL 25/48, SXTC 10/48, ICMB 1/48), so prior-peak ratios stay unknown at later scans too. Observed prior-session peaks for context: VCIG 10,916, NCPL 6,551, SXTC 789, ICMB 521 shares. The undated SXTC share-consolidation headline is an unreviewed share-changing corporate action, which also leaves SXTC cross-session comparisons unverified.

```text
# VCIG shared SIP volume; prior 2026-10-05 41/48 slots; log-only
# reconstructed as-of 2026-10-06T20:20:13+00:00; source fetched 2026-10-06T20:21:37.864736Z
VCIG 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=3344455 local=unknown prior-peak=unknown status=warmup
VCIG 2026-10-06  VOLUME-CONTEXT 16:05ET start=2026-10-06T20:05:00+00:00 shares=3445449 local=unknown prior-peak=unknown status=warmup
# NCPL shared SIP volume; prior 2026-10-05 25/48 slots; log-only
# reconstructed as-of 2026-10-06T20:20:13+00:00; source fetched 2026-10-06T20:21:38.519672Z
NCPL 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=71987 local=unknown prior-peak=unknown status=warmup
NCPL 2026-10-06  VOLUME-CONTEXT 16:05ET start=2026-10-06T20:05:00+00:00 shares=71440 local=unknown prior-peak=unknown status=warmup
# SXTC shared SIP volume; prior 2026-10-05 10/48 slots; log-only
# reconstructed as-of 2026-10-06T20:20:13+00:00; source fetched 2026-10-06T20:21:39.195705Z
SXTC 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=75597 local=unknown prior-peak=unknown status=warmup
SXTC 2026-10-06  VOLUME-CONTEXT 16:05ET start=2026-10-06T20:05:00+00:00 shares=683755 local=unknown prior-peak=unknown status=warmup
# ICMB shared SIP volume; prior 2026-10-05 1/48 slots; log-only
# reconstructed as-of 2026-10-06T20:20:13+00:00; source fetched 2026-10-06T20:21:39.904715Z
ICMB 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=1537 local=unknown prior-peak=unknown status=warmup
ICMB 2026-10-06  VOLUME-CONTEXT 16:05ET start=2026-10-06T20:05:00+00:00 shares=23780 local=unknown prior-peak=unknown status=warmup
```

**Book diagnostic (verbatim; log-only)** for the two names with accumulating SIP volume:

```text
VCIG BOOK iex bid $1.74 x100 / ask $1.79 x200 @ 2026-10-06 16:21:58 ET age 1s two-sided spread 2.79% of ask
VCIG BOOK sip-15m bid $1.70 x400 / ask $1.71 x500 @ 2026-10-06 16:06:59 ET age 15m00s two-sided spread 0.58% of ask
VCIG BOOK refresh +15s iex advanced @ 2026-10-06 16:22:07 ET
VCIG BOOK verdict: IEX FRESH; SIP-15m TWO-SIDED (observed 2026-10-06 16:21:59 ET; log-only)
SXTC BOOK iex bid $1.05 x100 / ask $0.0000 x0 @ 2026-10-06 16:00:03 ET age 21m56s one-sided/empty
SXTC BOOK sip-15m bid $1.74 x5000 / ask $1.75 x400 @ 2026-10-06 16:06:59 ET age 15m00s two-sided spread 0.57% of ask
SXTC BOOK refresh +15s iex unchanged @ 2026-10-06 16:00:03 ET
SXTC BOOK verdict: IEX STALE 21m56s; SIP-15m TWO-SIDED (observed 2026-10-06 16:21:59 ET; log-only)
```

**Carry forward:** VCIG, SXTC, NCPL, and ICMB each have 1 AH appearance. YFOR is below threshold. Keep all 28 names from the 21:30 watchlist in the pipeline; none appeared in this scan, which is not evidence of a fade. KAPA's dead-cat guard and OLOX's day-2 tag still apply. EVOL, MHUAF, VNPKF, WTLLF, NWINF, and KHDHF remain untradable (carried). At 23:00, VCIG needs a second >10% appearance plus a volume-backed high after 16:15 ET to clear the first-bar-spike skip.

**Daily email:** Report VCIG's real opening volume (6.8M shares in 10 minutes) on a same-day AI product PR, its opening-window high with CONFIRM-3 NO (FIRST-BAR-SPIKE WATCH), SXTC's real 16:05 ignition blocked by Day -39.9%, and the thin NCPL/ICMB prints. No item from this scan requires Juan's input.

## Scan 22:25 CEST (4:25 PM ET)

**Decision:** No entry; entries begin at the 23:00 CEST scan. VCIG and SXTC now each have **2** qualifying >10% AH appearances (22:20, 22:25). BIYA has its first. VCIG's live price has moved above its opening-window high, so the first-bar-spike skip is pending SIP confirmation at 23:00. SXTC meets the DEAD-CAT-OVERRIDE WATCH condition, so it gets a hypothetical entry and no live order. No paper orders submitted.

`python3 scripts/scan.py --all` ran at 16:25:29 ET (22:25:29 CEST / 20:25:29 UTC) in the AFTERHOURS session and returned 5 hits. The US trading date is 2026-10-06. Repository sync completed before the scan.

```text
  Supplementary AH-change-only (>15%, not in volume pass): none
  AH >10% at this snapshot (unrounded): BIYA, SXTC, VCIG
```

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| VCIG | [TV](https://www.tradingview.com/chart/?symbol=VCIG) | $1.41 | +54.8% | +31.2% | $1.85 | +103.1% | 6.2M | 1.9M | 3.2x | 1.0M | Miscellaneous Commercial Services |
| SXTC | [TV](https://www.tradingview.com/chart/?symbol=SXTC) | $1.25 | -39.9% | +25.6% | $1.57 | -24.5% | 658K | 550K | 1.2x | 1.0M | Pharmaceuticals: Major |
| BIYA | [TV](https://www.tradingview.com/chart/?symbol=BIYA) | $1.36 | -2.5% | +24.5% | $1.70 | +21.4% | 256K | 1.6M | 0.2x | 2.7M | Personnel Services |
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $1.09 | -17.4% | +8.3% | $1.18 | -10.6% | 139K | 14.3M | 0.0x | 4.4M | Miscellaneous Commercial Services |
| MTNB | [TV](https://www.tradingview.com/chart/?symbol=MTNB) | $3.01 | +6.7% | +5.3% | $3.17 | +12.4% | 60K | 203K | 0.3x | 773K | Pharmaceuticals: Major |

### Evaluation notes

**Tradability:** `broker.js tradable` returned `tradable=true` for VCIG, SXTC, BIYA, NCPL (Nasdaq) and MTNB (AMEX), all active.

**Close basis:** dated SIP daily closes confirm the scanner's Day%: VCIG $0.91 → $1.41, SXTC $2.08 → $1.25, BIYA $1.40 → $1.36.

**SIP bars** (`broker.js bars SYM --tf 5Min --start 2026-10-06T20:00:00Z`, feed=sip). The newest bar starts 16:10 ET, about 15 minutes behind the scan, which matches the free-tier delay.

| Ticker | Bar ET | Open | High | Low | Close | Shares | VWAP | Trades |
|--------|--------|------|------|-----|-------|--------|------|--------|
| VCIG | 16:00 | $1.41 | $1.73 | $1.29 | $1.70 | 3,344,455 | $1.56 | 15,386 |
| VCIG | 16:05 | $1.69 | $1.86 | $1.61 | $1.85 | 3,445,449 | $1.75 | 17,205 |
| VCIG | 16:10 | $1.85 | $1.94 | $1.65 | $1.84 | 2,459,351 | $1.85 | 12,500 |
| SXTC | 16:00 | $1.25 | $1.65 | $1.25 | $1.40 | 75,597 | $1.44 | 478 |
| SXTC | 16:05 | $1.39 | $1.85 | $1.36 | $1.57 | 683,755 | $1.66 | 4,488 |
| SXTC | 16:10 | $1.57 | $1.70 | $1.48 | $1.61 | 212,492 | $1.57 | 1,599 |
| BIYA | 16:00 | $1.365 | $1.365 | $1.365 | $1.365 | 1,095 | $1.37 | 4 |
| BIYA | 16:05 | $1.365 | $1.71 | $1.36 | $1.71 | 285,556 | $1.61 | 1,638 |
| BIYA | 16:10 | $1.70 | $1.78 | $1.65 | $1.75 | 1,072,394 | $1.71 | 6,193 |
| NCPL | 16:00 | $1.09 | $1.28 | $1.09 | $1.24 | 71,987 | $1.20 | 261 |
| NCPL | 16:05 | $1.22 | $1.28 | $1.18 | $1.18 | 71,440 | $1.22 | 172 |
| NCPL | 16:10 | $1.20 | $1.21 | $1.18 | $1.20 | 7,284 | $1.20 | 40 |

**Yahoo timeline (shape only, not volume or exact levels):**

| Ticker | 16:00 | 16:05 | 16:10 | 16:15 | 16:20 | 16:25 | 16:30 | 16:31 |
|--------|-------|-------|-------|-------|-------|-------|-------|-------|
| VCIG | $1.70 | $1.85 | $1.84 | $1.71 | $1.73 | $2.02 | $2.02 | $2.00 |
| SXTC | $1.40 | $1.57 | $1.63 | $1.45 | $1.56 | $1.74 | $1.82 | $2.06 |
| BIYA | $1.36 | $1.69 | $1.75 | $1.82 | $1.85 | $1.77 | $1.75 | $1.81 |

**VCIG — second qualifying AH scan; no entry before 23:00. FIRST-BAR-SPIKE WATCH status pending.** SIP added a third heavy bar (2.46M shares / 12,500 trades at 16:10 ET), for **9.25M shares / 45,091 trades** in 15 minutes. The SIP high rose to **$1.94 in the 16:10 bar**, which is still inside the 16:00–16:15 opening window. CONFIRM-3 reads NO through 16:25 ET. After the 16:15 dip to $1.71, the Yahoo shape shows **$2.02 at 16:25–16:30 ET**. The fresh IEX quote also sits above the SIP high (`VCIG  bid $1.96 x3700  ask $1.99 x200  @ 2026-10-06T20:27:10.822957357Z`). That points to a new high after 16:15 ET. SIP has not covered it yet, so it is not volume-confirmed. At $2.00, Total% is about **+120%** from the $0.91 prior close. That is under the +150% ceiling but at the edge of the >~120% fade zone in the chase-cap instrumentation. Day +54.8% passes. Float 1.0M is recorded for pattern tracking.

- **Catalyst Grade C (unchanged).** Two more targeted searches and one page extract returned only the same [October 6, 2026 GlobeNewswire release](https://www.globenewswire.com/news-release/2026/10/06/3375960/0/en/vci-global-launches-vgain-compute-ai-token-platform-expanding-into-ai-infrastructure-and-llm-services.html) on the VGAIN Compute AI token platform launch. The page extract carries the dateline "Oct. 06, 2026" but no clock time. Search ages ("44 minutes ago" at about 16:28 ET) put dissemination near 15:45 ET. Background is unchanged: the September 29–30 $125M equity facility and convertible note (dilution overhang).
- **Prior activity:** SIP daily volume was 5.9M on October 2 and 1.6M on October 5, against 24K–66K in late September. Today's 20.4M is a rebound after a two-day sell-off from $1.49 to $0.91. It is not the first day of unusual activity. It is also not a MULTI-SESSION-RUNNER, because the prior sessions fell.
- **23:00 check:** if SIP bars through about 16:45 ET show the $2.0 area on accumulating volume and CONFIRM-3 turns YES, the high is volume-backed after 16:15, and the first-bar-spike skip no longer applies. If CONFIRM-3 stays NO and SIP keeps the high at the 16:10 bar, the skip stands. The 22:20 hypothetical ($1.69 at 16:20 ET) stays on record.

**SXTC — second qualifying AH scan; skip live entry (Day -39.9%); DEAD-CAT-OVERRIDE WATCH.** AH change rose from +11.2% (22:20) to +25.6% (22:25), and the price is above the $1.25 regular close. That meets the override-watch condition. **Hypothetical entry: $1.57 (scanner) at 22:25 CEST / 16:25 ET.** Total% there is -24.5% from the $2.08 prior close. Caveat: both scanner readings equal the SIP 16:00 and 16:05 bar closes, so the scanner rise partly reflects a feed catching up. The tape itself peaked at **$1.85 in the 16:05 bar** (683,755 shares / 4,488 trades), cooled in the 16:10 bar (212,492 / 1,599, close $1.61), and dipped to $1.45 on Yahoo at 16:15. Yahoo now shows a second leg: $1.74 at 16:25, $1.82 at 16:30, $2.06 at 16:31. SIP has not covered that leg, so its volume is unconfirmed. The IEX quote is stale and empty (`SXTC  bid $1.05 x100  ask $0.00 x0  @ 2026-10-06T20:00:03.61384345Z`); the delayed SIP book was two-sided at 16:12 ET (see BOOK lines). CONFIRM-3 stays PENDING with ignition at 16:05 ET.

- **Catalyst Grade None — no catalyst found (re-run).** Four new searches covered general news, same-day announcements, 6-K offering and split filings, and dated October 6 coverage. They found only background: an undated "to offer up to $100M of Class A ordinary shares" SEC-filing headline, the January 2026 $0.15 registered direct offering, the February 3, 2026 1-for-150 reverse split, and an intraday mover list noting a 21.16% decline to $1.64 (Benzinga, about 13:30 ET). Nothing upside-oriented is dated October 6.
- **Prior activity:** daily SIP volume was 870K on September 29, 780K on October 2, and 950K on October 5, while the price fell from $3.01 (September 30) to $1.25. This is not the first day of unusual activity.

**BIYA — first qualifying AH scan; no entry (gate and window).** Ignition came in the 16:05 bar (285,556 shares / 1,638 trades) and grew in the 16:10 bar to **1,072,394 shares / 6,193 trades**. That is real accumulation, even though the scanner VRatio reads 0.2x. The SIP high is $1.78 in the 16:10 bar, and the SIP VWAP of $1.71 corroborates the scanner's $1.70. Yahoo shows a further rise to $1.85 at 16:20 and $1.81 at 16:31. The fresh IEX quote is two-sided (`BIYA  bid $1.74 x100  ask $1.78 x100  @ 2026-10-06T20:27:11.167397624Z`). Day -2.5% passes; Total% is +21.4%; float 2.7M. CONFIRM-3 is PENDING (ignition 16:05 ET), so first-bar-spike status is undetermined.

- **Catalyst Grade None — no catalyst found.** Four searches covered general news, same-day announcements, press release and 6-K filings, and day-fresh coverage. They found only background: the July 8, 2026 1-for-10 reverse split approval, an October 4 Wall Street Zen rating change from strong sell to sell, and older "Binance Plan" operating updates. Nothing is dated October 6. No-catalyst is a documented concern, not a skip reason.
- **Prior activity:** BIYA was the September 29 in-window feed-lag observation. That night its AH reached $2.74, and the September 30 session ran to $3.18 on 11.5M shares, then closed at $1.96. It has drifted to $1.36 since. Today's AH move re-ignites a name that already had unusual activity one week ago, so it is not a first-day igniter. It is also not a MULTI-SESSION-RUNNER, because the stock fell across the intervening sessions.

**NCPL:** AH change fell from +11.9% to **+8.3%**, below the 10% threshold. SIP volume thinned to 7,284 shares / 40 trades in the 16:10 bar. It stays skipped as a thin drift (Day -17.4%), and its 22:20 FIRST-BAR-SPIKE WATCH hypothetical stands. **ICMB** is absent from this scan; its 22:20 thin-print skip and watch stand. **MTNB** shows +5.3% AH (Total +12.4%), below the instrumentation threshold, and is tracked only.

**Instrumentation (verbatim; log-only):**

```text
VCIG 2026-10-06  NO-SPIKE  peak +36% @16:10ET  (no bar cleared +15% on a volume co-spike) (as-of 16:25ET)
VCIG 2026-10-06  CONFIRM-3  NO no local-volume new-high ignition as-of 16:25ET
SXTC 2026-10-06  SPIKE  16:03ET  +32%  $1.65  135 trades / 30k sh  (first co-spike bar) (as-of 16:25ET)
SXTC 2026-10-06  CONFIRM-3  PENDING ignition 16:05ET; waiting for third bar as-of 16:25ET
BIYA 2026-10-06  SPIKE  16:08ET  +21%  $1.65  372 trades / 58k sh  (first co-spike bar) (as-of 16:25ET)
BIYA 2026-10-06  CONFIRM-3  PENDING ignition 16:05ET; waiting for third bar as-of 16:25ET
```

**Shared SIP volume context (`sip-ah-volume-v1`, log-only):** The prior trading date is 2026-10-05, a normal Monday session. `volume_metric.py`'s own fetch returned HTTP 403, because its fixed 20:00 ET end time falls inside the free-tier recent-data block. The inputs were therefore fetched with `broker.js bars SYM --tf 5Min --start 2026-10-05T20:00:00Z --limit 1000 --feed sip --json`. Each returned one page with no next-page token. They are archived as `log/2026-10-06/SYM-2225-volume-sip.json` (SIP, 5Min, raw, fetch time in `observed_utc`), with computed rows in `SYM-2225-volume-metric.json`. All completed bars are still in warmup, so local ratios are unknown. Prior-session coverage is incomplete (VCIG 41/48, SXTC 10/48, BIYA 18/48), so prior-peak ratios remain unknown. Observed prior-session peaks, for context: VCIG 10,916, SXTC 789, BIYA 3,094 shares. SXTC's undated share-consolidation headline and BIYA's July 2026 1-for-10 reverse split are share-changing corporate actions that have not been reviewed against this window, so cross-session comparisons for both stay unverified.

```text
# VCIG shared SIP volume; prior 2026-10-05 41/48 slots; log-only
# reconstructed as-of 2026-10-06T20:25:29+00:00; source fetched 2026-10-06T20:26:41.230217Z
VCIG 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=3344455 local=unknown prior-peak=unknown status=warmup
VCIG 2026-10-06  VOLUME-CONTEXT 16:05ET start=2026-10-06T20:05:00+00:00 shares=3445449 local=unknown prior-peak=unknown status=warmup
VCIG 2026-10-06  VOLUME-CONTEXT 16:10ET start=2026-10-06T20:10:00+00:00 shares=2459351 local=unknown prior-peak=unknown status=warmup
# SXTC shared SIP volume; prior 2026-10-05 10/48 slots; log-only
# reconstructed as-of 2026-10-06T20:25:29+00:00; source fetched 2026-10-06T20:26:43.364321Z
SXTC 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=75597 local=unknown prior-peak=unknown status=warmup
SXTC 2026-10-06  VOLUME-CONTEXT 16:05ET start=2026-10-06T20:05:00+00:00 shares=683755 local=unknown prior-peak=unknown status=warmup
SXTC 2026-10-06  VOLUME-CONTEXT 16:10ET start=2026-10-06T20:10:00+00:00 shares=212492 local=unknown prior-peak=unknown status=warmup
# BIYA shared SIP volume; prior 2026-10-05 18/48 slots; log-only
# reconstructed as-of 2026-10-06T20:25:29+00:00; source fetched 2026-10-06T20:26:45.472010Z
BIYA 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=1095 local=unknown prior-peak=unknown status=warmup
BIYA 2026-10-06  VOLUME-CONTEXT 16:05ET start=2026-10-06T20:05:00+00:00 shares=285556 local=unknown prior-peak=unknown status=warmup
BIYA 2026-10-06  VOLUME-CONTEXT 16:10ET start=2026-10-06T20:10:00+00:00 shares=1072394 local=unknown prior-peak=unknown status=warmup
```

**Book diagnostic (verbatim; log-only)** for the three tradable >10% names with accumulating SIP volume:

```text
VCIG BOOK iex bid $1.96 x3700 / ask $1.99 x200 @ 2026-10-06 16:27:12 ET age 0s two-sided spread 1.51% of ask
VCIG BOOK sip-15m bid $1.80 x100 / ask $1.81 x5200 @ 2026-10-06 16:12:12 ET age 15m00s two-sided spread 0.55% of ask
VCIG BOOK refresh +15s iex advanced @ 2026-10-06 16:27:28 ET
VCIG BOOK verdict: IEX FRESH; SIP-15m TWO-SIDED (observed 2026-10-06 16:27:12 ET; log-only)
SXTC BOOK iex bid $1.05 x100 / ask $0.0000 x0 @ 2026-10-06 16:00:03 ET age 27m09s one-sided/empty
SXTC BOOK sip-15m bid $1.57 x100 / ask $1.59 x100 @ 2026-10-06 16:12:12 ET age 15m00s two-sided spread 1.26% of ask
SXTC BOOK refresh +15s iex unchanged @ 2026-10-06 16:00:03 ET
SXTC BOOK verdict: IEX STALE 27m09s; SIP-15m TWO-SIDED (observed 2026-10-06 16:27:12 ET; log-only)
BIYA BOOK iex bid $1.75 x100 / ask $1.76 x100 @ 2026-10-06 16:27:13 ET age 0s two-sided spread 0.57% of ask
BIYA BOOK sip-15m bid $1.66 x100 / ask $1.67 x1700 @ 2026-10-06 16:12:13 ET age 15m00s two-sided spread 0.60% of ask
BIYA BOOK refresh +15s iex advanced @ 2026-10-06 16:27:24 ET
BIYA BOOK verdict: IEX FRESH; SIP-15m TWO-SIDED (observed 2026-10-06 16:27:12 ET; log-only)
```

**Carry forward:** AH appearance counts are VCIG 2, SXTC 2, BIYA 1, NCPL 1, and ICMB 1. At 23:00, VCIG clears the appearance gate; its entry depends on the first-bar-spike check above plus SIP corroboration and a fresh book. SXTC remains blocked by Day% and stays on DEAD-CAT-OVERRIDE WATCH. BIYA needs a second >10% appearance. Keep all 28 names from the 21:30 watchlist in the pipeline for the final-scan cross-check. KAPA's dead-cat guard and OLOX's day-2 tag still apply. EVOL, MHUAF, VNPKF, WTLLF, NWINF, and KHDHF remain untradable (carried).

**Daily email:** Report VCIG's 9.25M shares in its first 15 AH minutes and its post-16:15 push to about $2.00 (pending SIP), SXTC's DEAD-CAT-OVERRIDE WATCH hypothetical at $1.57 with a second leg toward $2.06, BIYA's no-catalyst 1.07M-share 16:10 bar one week after its September 29 AH spike, and the `volume_metric.py` 403 on its built-in fetch (its fixed 20:00 ET end time hits the free-tier recent-data block; fixed for this scan with a `broker.js` fetch). No item from this scan requires Juan's input.

## Scan 22:30 CEST (4:30 PM ET)

**Decision:** No entry; entries begin at the 23:00 CEST scan. AH appearance counts are now VCIG **3**, SXTC **3**, BIYA **2** (22:25, 22:30). BIYA is the cleanest setup so far: CONFIRM-3 turned **YES**, its SIP high came in the 16:15 bar (after the opening window) on 1.60M shares / 9,966 trades, and it holds about 5% below that high on a fresh two-sided book. VCIG's CONFIRM-3 is still NO through the 16:15 SIP bar, so its first-bar-spike status waits on SIP for the post-16:20 push. SXTC stays blocked by Day -39.9% and on DEAD-CAT-OVERRIDE WATCH; Yahoo shows a new leg to about $2.36 after this scan. No paper orders submitted.

`python3 scripts/scan.py --all` ran at 16:30:14 ET (22:30:14 CEST / 20:30:14 UTC) in the AFTERHOURS session and returned 6 hits. The US trading date is 2026-10-06. Repository sync completed before the scan.

```text
  Supplementary AH-change-only (>15%, not in volume pass): none
  AH >10% at this snapshot (unrounded): BIYA, SXTC, VCIG
```

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| VCIG | [TV](https://www.tradingview.com/chart/?symbol=VCIG) | $1.41 | +54.8% | +29.9% | $1.83 | +101.0% | 8.4M | 2.2M | 3.9x | 1.0M | Miscellaneous Commercial Services |
| BIYA | [TV](https://www.tradingview.com/chart/?symbol=BIYA) | $1.36 | -2.5% | +26.0% | $1.72 | +22.9% | 1.1M | 1.7M | 0.7x | 2.7M | Personnel Services |
| SXTC | [TV](https://www.tradingview.com/chart/?symbol=SXTC) | $1.25 | -39.9% | +22.4% | $1.53 | -26.4% | 832K | 571K | 1.5x | 1.0M | Pharmaceuticals: Major |
| XHLD | [TV](https://www.tradingview.com/chart/?symbol=XHLD) | $0.62 | +51.6% | +6.4% | $0.66 | +61.3% | 687K | 19.4M | 0.0x | 10.5M | Miscellaneous Commercial Services |
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $1.09 | -17.4% | +9.6% | $1.20 | -9.5% | 143K | 14.3M | 0.0x | 4.4M | Miscellaneous Commercial Services |
| BURU | [TV](https://www.tradingview.com/chart/?symbol=BURU) | $1.20 | +7.1% | +5.8% | $1.27 | +13.4% | 118K | 1.6M | 0.1x | 8.4M | Electronic Components |

### Evaluation notes

**Tradability:** VCIG, SXTC, BIYA, and NCPL were verified `tradable=true` earlier tonight. XHLD (Nasdaq) and BURU (AMEX) returned `tradable=true`, both active.

**New SIP bar** (`broker.js bars SYM --tf 5Min --start 2026-10-06T20:00:00Z`, feed=sip). A re-pull at 16:33 ET still ended at the 16:15 bar, about 15 minutes behind, which matches the free-tier delay. Earlier bars are in the 22:20 and 22:25 tables.

| Ticker | Bar ET | Open | High | Low | Close | Shares | VWAP | Trades |
|--------|--------|------|------|-----|-------|--------|------|--------|
| VCIG | 16:15 | $1.83 | $1.94 | $1.70 | $1.71 | 2,090,194 | $1.83 | 10,506 |
| SXTC | 16:15 | $1.63 | $1.63 | $1.41 | $1.45 | 103,774 | $1.48 | 788 |
| BIYA | 16:15 | $1.75 | $1.92 | $1.71 | $1.81 | 1,596,650 | $1.82 | 9,966 |

**Yahoo timeline (shape only, not volume or exact levels):** VCIG $2.02 at 16:25, $1.92 at 16:30, $1.91 at 16:33. BIYA $1.77 at 16:25, $1.79 at 16:30, $1.82 at 16:33. SXTC one-minute closes $1.73 at 16:25, $1.82 at 16:30, $2.15 at 16:31, $2.30 at 16:32, $2.36 at 16:33 (one-minute high $2.50).

**BIYA — second qualifying AH scan; no entry before 23:00. BUILD with real volume.** SIP volume rose every bar: 285,556 → 1,072,394 → **1,596,650 shares** (1,638 → 6,193 → **9,966 trades**). The scanner's 0.7x VRatio understates this. The SIP high is **$1.92 in the 16:15 bar** (AH +41.2%, Total +37.1% from the $1.40 prior close), which is after the 16:00–16:15 opening window, so the first-bar-spike skip does not apply. The SIP VWAP of $1.82 corroborates the scanner's $1.72 as a lagged reading, not a bad print. The fresh IEX quote is two-sided (`BIYA  bid $1.76 x100  ask $1.79 x100  @ 2026-10-06T20:31:24.486137742Z`). At Yahoo's $1.82 the price is **5% below the high**, holding. Day -2.5% passes; Total% is about +30%, far under the +150% ceiling. Float 2.7M.

- **Catalyst Grade None — no catalyst found.** Four new searches (press release, day-fresh announcements, 6-K filings, and a Tavily news query) found only background: the [PRNewswire first-half fiscal 2026 results](https://www.prnewswire.com/news-releases/baiya-international-group-inc-announces-first-half-of-fiscal-year-2026-financial-results-302893401.html) from about a week ago, the July 8, 2026 1-for-10 reverse split, and the Wall Street Zen strong-sell-to-sell change reported October 5. Nothing is dated October 6. No-catalyst is a documented concern, not a skip reason.
- **Prior activity:** SIP daily bars show 2.93M shares on September 29 and 11.53M on September 30 (high $3.18, close $1.96), then 125K–372K per day while the price slid to $1.40. Today's regular session traded 4.04M shares. This is a re-ignition one week after the September 29–30 spike, so it fails a strict "first day of unusual activity" reading. It is not a MULTI-SESSION-RUNNER, because the intervening sessions fell. `WINNERS_TRACKING.md` has no BIYA entry.

**VCIG — third qualifying AH scan; first-bar-spike status still pending.** The new 16:15 bar matched the $1.94 high without exceeding it, on 2,090,194 shares / 10,506 trades, and closed at $1.71. Per-bar volume is easing (3.34M → 3.45M → 2.46M → 2.09M). CONFIRM-3 stays NO through the 16:15 bar. The real-time IEX quote printed **bid $2.00 / ask $2.04 at 16:31:27 ET**, then $1.97/$1.99 at 16:31:38 ET. Both sit above the $1.94 SIP high, and Yahoo showed $2.02 at 16:25. That is a post-16:15 high near $2.02–2.04 that SIP has not yet covered; Yahoo is back to $1.91 at 16:33. At $2.00 Total% is +119.6% from the $0.91 prior close, at the edge of the >~120% fade zone. Catalyst Grade C (October 6 GlobeNewswire VGAIN Compute launch; clock time still unverified) and prior-activity notes are unchanged from 22:25.

**SXTC — third qualifying AH scan; skip live entry (Day -39.9%); DEAD-CAT-OVERRIDE WATCH continues.** The 22:25 hypothetical ($1.57 at 16:25 ET) stands. SIP through 16:15 ET shows a fade from the $1.85 16:05 high on shrinking volume (683,755 → 212,492 → **103,774 shares**), and CONFIRM-3 turned **NO** (failed third-bar hold/volume). The scanner's AH change dipped from +25.6% to +22.4%, matching that dip. Yahoo then shows a sharp second leg after the scan: **$2.36 at 16:33 ET**, which would be AH +89% and Total +13.5% above the $2.08 prior close. SIP has not covered that leg, the IEX quote is still frozen at 16:00:03 ET with no ask, and the delayed SIP book at 16:16 ET was $1.50/$1.51. Per the freshness guard, treat the leg as unconfirmed but live, not as a bad print. One more day-fresh search found no catalyst (only a Benzinga intraday mover list noting a 21.16% decline to $1.64); Grade None stands.

**Below threshold:** NCPL rose back to +9.6% on 143K AH shares; its 22:20 thin-drift skip and FIRST-BAR-SPIKE WATCH hypothetical stand, and IEX is still frozen with no ask. XHLD (+6.4% AH, Day +51.6%, Total +61.3%, from the 21:30 watchlist) and BURU (+5.8% AH, Day +7.1%) are tracked only. ICMB and MTNB are absent.

**Instrumentation (verbatim; log-only):**

```text
VCIG 2026-10-06  NO-SPIKE  peak +38% @16:12ET  (no bar cleared +15% on a volume co-spike) (as-of 16:30ET)
VCIG 2026-10-06  CONFIRM-3  NO no local-volume new-high ignition as-of 16:30ET
SXTC 2026-10-06  SPIKE  16:03ET  +32%  $1.65  135 trades / 30k sh  (first co-spike bar) (as-of 16:30ET)
SXTC 2026-10-06  CONFIRM-3  NO ignition 16:05ET failed third-bar hold/volume as-of 16:30ET
BIYA 2026-10-06  SPIKE  16:08ET  +21%  $1.65  372 trades / 58k sh  (first co-spike bar) (as-of 16:30ET)
BIYA 2026-10-06  CONFIRM-3  YES ignition 16:05ET 260.8x; confirmed 16:15ET $1.81 as-of 16:30ET
```

**Shared SIP volume context (`sip-ah-volume-v1`, log-only):** The prior trading date is 2026-10-05. `volume_metric.py --save-input` again returned HTTP 403 on its built-in fetch, so the inputs were fetched with `broker.js bars SYM --tf 5Min --start 2026-10-05T20:00:00Z --limit 1000 --feed sip --json` (one page each, no next-page token) and archived as `log/2026-10-06/SYM-2230-volume-sip.json`, with computed rows in `SYM-2230-volume-metric.json`. The concurrent 22:25 pulse's `git add log/` committed these files in `c8be4e2`. The 16:15 bar is the first with a local ratio. Prior-session coverage is incomplete (VCIG 41/48, SXTC 10/48, BIYA 18/48), so prior-peak ratios stay unknown; observed prior peaks are VCIG 10,916, SXTC 789, and BIYA 3,094 shares. The SXTC share-consolidation headline and BIYA's July 1-for-10 reverse split remain unreviewed against this window.

```text
# VCIG shared SIP volume; prior 2026-10-05 41/48 slots; log-only
# reconstructed as-of 2026-10-06T20:30:14+00:00; source fetched 2026-10-06T20:32:13.853065Z
VCIG 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=3344455 local=unknown prior-peak=unknown status=warmup
VCIG 2026-10-06  VOLUME-CONTEXT 16:05ET start=2026-10-06T20:05:00+00:00 shares=3445449 local=unknown prior-peak=unknown status=warmup
VCIG 2026-10-06  VOLUME-CONTEXT 16:10ET start=2026-10-06T20:10:00+00:00 shares=2459351 local=unknown prior-peak=unknown status=warmup
VCIG 2026-10-06  VOLUME-CONTEXT 16:15ET start=2026-10-06T20:15:00+00:00 shares=2090194 local=0.6250x prior-peak=unknown status=ok
# SXTC shared SIP volume; prior 2026-10-05 10/48 slots; log-only
# reconstructed as-of 2026-10-06T20:30:14+00:00; source fetched 2026-10-06T20:32:16.010125Z
SXTC 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=75597 local=unknown prior-peak=unknown status=warmup
SXTC 2026-10-06  VOLUME-CONTEXT 16:05ET start=2026-10-06T20:05:00+00:00 shares=683755 local=unknown prior-peak=unknown status=warmup
SXTC 2026-10-06  VOLUME-CONTEXT 16:10ET start=2026-10-06T20:10:00+00:00 shares=212492 local=unknown prior-peak=unknown status=warmup
SXTC 2026-10-06  VOLUME-CONTEXT 16:15ET start=2026-10-06T20:15:00+00:00 shares=103774 local=0.4884x prior-peak=unknown status=ok
# BIYA shared SIP volume; prior 2026-10-05 18/48 slots; log-only
# reconstructed as-of 2026-10-06T20:30:14+00:00; source fetched 2026-10-06T20:32:18.171658Z
BIYA 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=1095 local=unknown prior-peak=unknown status=warmup
BIYA 2026-10-06  VOLUME-CONTEXT 16:05ET start=2026-10-06T20:05:00+00:00 shares=285556 local=unknown prior-peak=unknown status=warmup
BIYA 2026-10-06  VOLUME-CONTEXT 16:10ET start=2026-10-06T20:10:00+00:00 shares=1072394 local=unknown prior-peak=unknown status=warmup
BIYA 2026-10-06  VOLUME-CONTEXT 16:15ET start=2026-10-06T20:15:00+00:00 shares=1596650 local=5.5914x prior-peak=unknown status=ok
```

**Book diagnostic (verbatim; log-only):**

```text
VCIG BOOK iex bid $1.97 x1000 / ask $1.99 x100 @ 2026-10-06 16:31:38 ET age 1s two-sided spread 1.01% of ask
VCIG BOOK sip-15m bid $1.78 x800 / ask $1.79 x1200 @ 2026-10-06 16:16:38 ET age 15m01s two-sided spread 0.56% of ask
VCIG BOOK refresh +15s iex advanced @ 2026-10-06 16:31:54 ET
VCIG BOOK verdict: IEX FRESH; SIP-15m TWO-SIDED (observed 2026-10-06 16:31:38 ET; log-only)
SXTC BOOK iex bid $1.05 x100 / ask $0.0000 x0 @ 2026-10-06 16:00:03 ET age 31m35s one-sided/empty
SXTC BOOK sip-15m bid $1.50 x2000 / ask $1.51 x1100 @ 2026-10-06 16:16:38 ET age 15m00s two-sided spread 0.66% of ask
SXTC BOOK refresh +15s iex unchanged @ 2026-10-06 16:00:03 ET
SXTC BOOK verdict: IEX STALE 31m35s; SIP-15m TWO-SIDED (observed 2026-10-06 16:31:38 ET; log-only)
BIYA BOOK iex bid $1.76 x100 / ask $1.79 x100 @ 2026-10-06 16:31:24 ET age 14s two-sided spread 1.68% of ask
BIYA BOOK sip-15m bid $1.88 x5800 / ask $1.89 x10400 @ 2026-10-06 16:16:38 ET age 15m00s two-sided spread 0.53% of ask
BIYA BOOK refresh +15s iex advanced @ 2026-10-06 16:31:53 ET
BIYA BOOK verdict: IEX FRESH; SIP-15m TWO-SIDED (observed 2026-10-06 16:31:38 ET; log-only)
```

**23:00 checklist:** BIYA clears the appearance gate; enter if it still shows >10% AH, SIP keeps accumulating, it holds within ~20% of its high, and the IEX book is fresh and two-sided (Grade None, concern noted). VCIG clears the appearance gate; the first-bar-spike skip lifts only if SIP bars through about 16:45 ET show the ~$2.02 high on accumulating volume and CONFIRM-3 turns YES. SXTC stays a Day% skip; check SIP for the 16:30 leg and note whether it holds above the $2.08 prior close. Keep all 28 names from the 21:30 watchlist in the pipeline for the final-scan cross-check. KAPA's dead-cat guard and OLOX's day-2 tag still apply. EVOL, MHUAF, VNPKF, WTLLF, NWINF, and KHDHF remain untradable (carried).

**Daily email:** Report BIYA turning CONFIRM-3 YES on 1.60M shares in the 16:15 bar with no catalyst found, VCIG's unconfirmed push above its opening-window high, and SXTC's unconfirmed Yahoo leg to $2.36 while on DEAD-CAT-OVERRIDE WATCH. No item from this scan requires Juan's input.

## Scan 22:45 CEST (4:45 PM ET)

**Decision:** No entry; entries begin at the 23:00 CEST scan. AH appearance counts are now VCIG **4**, SXTC **4**, BIYA **3**, NCPL **2**, MI **1**, LHSW **1**. BIYA remains the 23:00 lead: CONFIRM-3 YES, a new SIP high of $1.94 in the 16:30 bar, and about 7% below that high at 16:46 ET. VCIG set a volume-backed high of $2.10 in the 16:25 bar, which moves its high out of the opening window, but it has since faded to $1.53/$1.55 (27% off the high). SXTC reclaimed its $2.08 prior close on 1.34M shares in the 16:30 bar and stays on DEAD-CAT-OVERRIDE WATCH (Day -39.9%). New names MI (Day -82.4%, same-day $2.55M registered direct offering) and LHSW (spike back below its close) are skips. No paper orders submitted.

`python3 scripts/scan.py --all` ran at 16:45:20 ET (22:45:20 CEST / 20:45:20 UTC) in the AFTERHOURS session and returned 7 hits. The US trading date is 2026-10-06. Repository sync completed before the scan.

```text
  Supplementary AH-change-only (>15%, not in volume pass): none
  AH >10% at this snapshot (unrounded): BIYA, LHSW, MI, NCPL, SXTC, VCIG
```

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| VCIG | [TV](https://www.tradingview.com/chart/?symbol=VCIG) | $1.41 | +54.8% | +43.2% | $2.02 | +121.7% | 13.9M | 2.8M | 5.0x | 1.0M | Miscellaneous Commercial Services |
| MI | [TV](https://www.tradingview.com/chart/?symbol=MI) | $1.23 | -82.4% | +25.2% | $1.54 | -78.0% | 4.3M | 18.4M | 0.2x | 542K | Internet Software/Services |
| BIYA | [TV](https://www.tradingview.com/chart/?symbol=BIYA) | $1.36 | -2.5% | +29.7% | $1.77 | +26.4% | 3.3M | 1.9M | 1.7x | 2.7M | Personnel Services |
| SXTC | [TV](https://www.tradingview.com/chart/?symbol=SXTC) | $1.25 | -39.9% | +40.0% | $1.75 | -15.9% | 1.5M | 650K | 2.4x | 1.0M | Pharmaceuticals: Major |
| OLOX | [TV](https://www.tradingview.com/chart/?symbol=OLOX) | $1.25 | +42.0% | +9.6% | $1.37 | +55.7% | 904K | 15.1M | 0.1x | 1.3M | Building Products |
| LHSW | [TV](https://www.tradingview.com/chart/?symbol=LHSW) | $0.57 | +3.5% | +18.9% | $0.67 | +23.1% | 559K | 1.5M | 0.4x | 1.0M | Computer Processing Hardware |
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $1.09 | -17.4% | +10.1% | $1.20 | -9.1% | 158K | 14.3M | 0.0x | 4.4M | Miscellaneous Commercial Services |

### Evaluation notes

**Tradability:** MI (AMEX), LHSW (Nasdaq), and OLOX (Nasdaq) returned `tradable=true`, all active. VCIG, BIYA, SXTC, and NCPL were verified earlier tonight.

**Close basis:** dated SIP daily closes confirm the new names' Day%: MI $7.00 (October 5) → $1.23, LHSW $0.55 → $0.57.

**New SIP bars** (`broker.js bars SYM --tf 5Min --start 2026-10-06T20:00:00Z`, feed=sip). The newest bar starts 16:30 ET, about 15 minutes behind the scan, which matches the free-tier delay. Earlier VCIG, BIYA, and SXTC bars are in the 22:20–22:30 tables.

| Ticker | Bar ET | Open | High | Low | Close | Shares | VWAP | Trades |
|--------|--------|------|------|-----|-------|--------|------|--------|
| VCIG | 16:20 | $1.72 | $1.85 | $1.71 | $1.72 | 1,123,854 | $1.77 | 6,267 |
| VCIG | 16:25 | $1.72 | $2.10 | $1.71 | $2.01 | 2,771,585 | $1.95 | 15,430 |
| VCIG | 16:30 | $2.02 | $2.07 | $1.87 | $1.90 | 1,820,673 | $1.96 | 10,561 |
| BIYA | 16:20 | $1.81 | $1.85 | $1.65 | $1.85 | 550,815 | $1.74 | 3,532 |
| BIYA | 16:25 | $1.85 | $1.87 | $1.70 | $1.77 | 307,657 | $1.78 | 2,003 |
| BIYA | 16:30 | $1.77 | $1.94 | $1.75 | $1.85 | 452,655 | $1.86 | 2,671 |
| SXTC | 16:20 | $1.45 | $1.77 | $1.41 | $1.56 | 295,399 | $1.59 | 1,761 |
| SXTC | 16:25 | $1.59 | $1.85 | $1.55 | $1.76 | 394,574 | $1.73 | 2,403 |
| SXTC | 16:30 | $1.75 | $2.58 | $1.71 | $2.19 | 1,344,735 | $2.26 | 10,722 |
| MI | 16:00 | $1.23 | $1.30 | $1.21 | $1.23 | 220,361 | $1.25 | 947 |
| MI | 16:05 | $1.22 | $1.26 | $1.18 | $1.23 | 137,355 | $1.22 | 589 |
| MI | 16:10 | $1.24 | $1.29 | $1.19 | $1.27 | 159,195 | $1.24 | 666 |
| MI | 16:15 | $1.27 | $1.73 | $1.22 | $1.70 | 1,263,614 | $1.52 | 5,991 |
| MI | 16:20 | $1.70 | $1.84 | $1.60 | $1.64 | 2,036,291 | $1.71 | 10,224 |
| MI | 16:25 | $1.64 | $1.69 | $1.50 | $1.55 | 868,347 | $1.61 | 3,726 |
| MI | 16:30 | $1.54 | $1.63 | $1.45 | $1.52 | 427,999 | $1.55 | 2,025 |
| LHSW | 16:00 | $0.57 | $0.57 | $0.57 | $0.57 | 11,339 | $0.57 | 3 |
| LHSW | 16:15 | $0.56 | $0.63 | $0.56 | $0.62 | 60,835 | $0.60 | 187 |
| LHSW | 16:20 | $0.62 | $0.62 | $0.56 | $0.62 | 118,219 | $0.60 | 296 |
| LHSW | 16:25 | $0.62 | $0.69 | $0.61 | $0.68 | 399,935 | $0.64 | 1,453 |
| LHSW | 16:30 | $0.67 | $0.68 | $0.57 | $0.59 | 373,669 | $0.62 | 1,233 |
| NCPL | 16:30 | $1.20 | $1.20 | $1.20 | $1.20 | 234 | $1.20 | 2 |

**Yahoo timeline (shape only, not volume or exact levels):**

| Ticker | 16:30 | 16:35 | 16:40 | 16:45 | 16:46 |
|--------|-------|-------|-------|-------|-------|
| VCIG | $1.91 | $1.84 | $1.66 | $1.64 | $1.64 |
| BIYA | $1.85 | $2.04 | $1.88 | $1.86 | $1.80 |
| SXTC | $2.16 | $1.94 | $2.13 | $2.14 | — |
| MI | $1.53 | $1.50 | $1.52 | $1.53 | — |
| LHSW | $0.59 | $0.58 | $0.58 | $0.56 | — |

**BIYA — third qualifying AH scan; no entry before 23:00. Still holding near its high.** The 16:30 bar made a new SIP high of **$1.94** on 452,655 shares / 2,671 trades (VWAP $1.86). Per-bar volume eased after the 16:15 peak (1,596,650 → 550,815 → 307,657 → 452,655 shares) but stays in the hundreds of thousands of shares and thousands of trades. CONFIRM-3 stays **YES**. Yahoo shows a push to $2.04 at 16:35, and the last IEX quote was $2.05/$2.09 at 16:40:59 ET. SIP has not covered that push yet. Yahoo then shows $1.80 at 16:46, which is **7% below the $1.94 SIP high** and about 12% below the unconfirmed $2.05 print, so it is holding within 20%. At $1.80, Total% is +28.6% from the $1.40 prior close, far under the +150% ceiling. Day -2.5% passes. The IEX book was 6 minutes stale at the book check; the delayed SIP book at 16:32 ET was $1.84/$1.85.

- **Catalyst Grade None — no catalyst found.** One more search ("Baiya International announces") plus one follow-up found only background: the late-September first-half fiscal 2026 results, the July 8, 2026 1-for-10 reverse split, the August 11 $2M BNB investment, and a [1-for-25 reverse split effective December 29, 2025](https://www.globenewswire.com/news-release/2025/12/26/3210635/0/en/Baiya-International-Group-Inc-Announce-Reverse-Split-Record-Date.html). Nothing is dated October 6. No-catalyst is a documented concern, not a skip reason.
- **Prior activity** (unchanged from 22:30): re-ignition one week after the September 29–30 spike; not a MULTI-SESSION-RUNNER, because the intervening sessions fell.

**VCIG — fourth qualifying AH scan; skip at this snapshot (fade).** The 16:25 bar set a new SIP high of **$2.10** (AH +48.9%, Total +130.8% from the $0.91 prior close) on 2,771,585 shares / 15,430 trades, which confirms the post-16:15 push seen on Yahoo and IEX at 22:30. The AH high is therefore outside the 16:00–16:15 opening window, so the first-bar-spike rule no longer applies. CONFIRM-3 still reads NO, because the 16:25 bar's volume was below the opening bars. The price has since dropped: the fresh IEX quote at 16:47:05 ET was **$1.53/$1.55**, **27% below the $2.10 high**, and Yahoo shows a steady slide from $2.02 at 16:25 to $1.64 at 16:46. That is a fade beyond the ~20% hold threshold, after a peak at 16:25 ET. At $1.54, Total% is +69%. The 22:20 FIRST-BAR-SPIKE WATCH hypothetical ($1.69 at 16:20 ET) stays on record for morning measurement. Catalyst Grade C (October 6 GlobeNewswire VGAIN Compute launch; clock time still unverified) is unchanged. At 23:00, VCIG enters only if it recovers to within ~20% of $2.10 (about $1.68 or higher) on accumulating SIP volume.

**SXTC — fourth qualifying AH scan; skip live entry (Day -39.9%); DEAD-CAT-OVERRIDE WATCH continues.** SIP now confirms the second leg: the 16:30 bar traded **1,344,735 shares / 10,722 trades**, with a high of **$2.58** (AH +106%, Total +24.0%) and a VWAP of $2.26 above the $2.08 prior close. Volume built across three bars (295,399 → 394,574 → 1,344,735 shares). The fresh IEX quote at 16:46:54 ET was **$2.29/$2.36**, about 10% below the high and +10% to +13% above the prior close. Scanner AH change ran +11.2% → +25.6% → +22.4% → +40.0% across the four AH scans; the scanner's $1.75 matches the 16:25 bar close and lags the tape. CONFIRM-3 reads NO, because it scores the 16:05 ignition, which failed its third bar; the tool does not re-score the 16:30 leg. The 22:25 hypothetical ($1.57 at 16:25 ET) stands; the IEX ask of $2.36 at 16:46 ET is recorded as the current reading. Catalyst Grade None is unchanged. The Day% rule still blocks a live entry.

**MI — first AH appearance; skip (dead-cat bounce, Grade D).** NFT Limited ran from a $0.89 close on October 2 to a $7.00 close on October 5 (high $10.42, 167M SIP shares), then collapsed **-82.4%** today to $1.23. AH was flat through 16:10 ET. It ignited in the 16:15 bar (1,263,614 shares / 5,991 trades), peaked at **$1.84 in the 16:20 bar** (2,036,291 shares / 10,224 trades; AH +49.6%), and faded on shrinking volume (868,347 → 427,999 shares). The fresh IEX quote at 16:46:54 ET was $1.56/$1.58, 15% below the AH high and 77% below the $7.00 prior close. This is a dead-cat bounce from a regular-session crash. It is above today's $1.23 close, but DEAD-CAT-OVERRIDE WATCH requires AH% rising across ≥2 AH scans, and this is the first appearance with price already falling from a 16:20 peak. CONFIRM-3 reads NO (ignition 16:15 failed its third bar).

- **Catalyst Grade D — dilution.** [GlobeNewswire, October 6, 2026: "NFT Ltd. Announces Pricing of $2.55 Million Registered Direct Offering"](https://www.globenewswire.com/news-release/2026/10/06/3375889/0/en/nft-ltd-announces-pricing-of-2-55-million-registered-direct-offering.html). The search listed it about 3 hours before 16:50 ET, so release was near 13:50 ET; the exact clock time is unverified. Background: an October 5 6-K stating management knew of no undisclosed news behind the October 5 spike, and October 6 premarket coverage of a 48–50% decline. Three searches used.
- **Multi-session context:** day 2 of a move that ran +687% on October 5 and gave back 82% today. Not a first day of unusual activity.

**LHSW — first AH appearance; skip (spike faded below close).** Volume ignited in the 16:25 bar (399,935 shares / 1,453 trades) to a high of **$0.69** (AH +21%), then the 16:30 bar fell to a $0.59 close on 373,669 shares. Yahoo shows $0.56 at 16:45, below the $0.57 regular close. The scanner's $0.67 matches the 16:25 bar and lags. The IEX quote is frozen at 16:00:00 ET ($0.47/$0.65); the delayed SIP book at 16:32 ET was $0.5876/$0.60. CONFIRM-3 is PENDING (ignition 16:25 ET), but the price has already given back the whole move.

- **Catalyst Grade None — no catalyst found.** Three searches found only background: the [August 13, 2026 fiscal 2026 results](https://www.globenewswire.com/news-release/2026/08/13/3344951/0/en/lianhe-sowell-international-group-ltd-announces-financial-results-for-fiscal-year-2026.html) (year ended March 31), September 22 news, a September 28 6-K on a Chery subsidiary promoting its equipment, and a January 2026 UAE robotics headquarters plan.
- **Prior activity:** SIP daily volume was 346M shares on September 22 (high $1.34), then 0.2M–6.7M per day as the price slid to $0.47 on October 2. Not a first day of unusual activity.

**NCPL — second >10% AH appearance (22:20, 22:45); skip stands (thin drift, Day -17.4%).** The scanner's +10.1% sits on SIP bars of 7,199 shares (16:25) and **234 shares / 2 trades** (16:30). The 22:20 FIRST-BAR-SPIKE WATCH hypothetical stands.

**Below threshold:** OLOX (+9.6% AH, Day +42.0%, Total +55.7%) is the October 5 AH→PM winner on day 2 (MULTI-SESSION-RUNNER if it qualifies). SIP shows a slow climb from a $1.20 low at 16:05 to a $1.44 high in the 16:30 bar on 289,334 shares / 947 trades; the fresh IEX quote was $1.36/$1.37 at 16:44:28 ET. A >10% reading at 23:00 would be its first qualifying AH appearance. ICMB, MTNB, XHLD, BURU, and YFOR are absent.

**Instrumentation (verbatim; log-only):**

```text
VCIG 2026-10-06  NO-SPIKE  peak +49% @16:28ET  (no bar cleared +15% on a volume co-spike) (as-of 16:45ET)
VCIG 2026-10-06  CONFIRM-3  NO no local-volume new-high ignition as-of 16:45ET
BIYA 2026-10-06  SPIKE  16:08ET  +21%  $1.65  372 trades / 58k sh  (first co-spike bar) (as-of 16:45ET)
BIYA 2026-10-06  CONFIRM-3  YES ignition 16:05ET 260.8x; confirmed 16:15ET $1.81 as-of 16:45ET
SXTC 2026-10-06  SPIKE  16:03ET  +32%  $1.65  135 trades / 30k sh  (first co-spike bar) (as-of 16:45ET)
SXTC 2026-10-06  CONFIRM-3  NO ignition 16:05ET failed third-bar hold/volume as-of 16:45ET
MI 2026-10-06  SPIKE  16:18ET  +30%  $1.60  2066 trades / 421k sh  (first co-spike bar) (as-of 16:45ET)
MI 2026-10-06  CONFIRM-3  NO ignition 16:15ET failed third-bar hold/volume as-of 16:45ET
LHSW 2026-10-06  SPIKE  16:25ET  +19%  $0.68  413 trades / 110k sh  (first co-spike bar) (as-of 16:45ET)
LHSW 2026-10-06  CONFIRM-3  PENDING ignition 16:25ET; waiting for third bar as-of 16:45ET
NCPL 2026-10-06  NO-SPIKE  peak +17% @16:03ET  (no bar cleared +15% on a volume co-spike) (as-of 16:45ET)
NCPL 2026-10-06  CONFIRM-3  NO no local-volume new-high ignition as-of 16:45ET
```

**Shared SIP volume context (`sip-ah-volume-v1`, log-only):** The prior trading date is 2026-10-05, a normal Monday session. Inputs were fetched with `broker.js bars SYM --tf 5Min --start 2026-10-05T20:00:00Z --limit 1000 --feed sip --json` (one page each, no next-page token) and archived as `log/2026-10-06/SYM-2245-volume-sip.json`, with computed rows in `SYM-2245-volume-metric.json`. MI is the only name with complete prior-session coverage (48/48); its 16:20 bar was 1.93x the October 5 AH peak. The others stay incomplete (VCIG 41/48, BIYA 18/48, SXTC 10/48, LHSW 44/48, NCPL 25/48), so their prior-peak ratios remain unknown. LHSW has no 16:05 or 16:10 bars, so its 16:15–16:25 rows lack a baseline. The SXTC share-consolidation headline and BIYA's July 1-for-10 reverse split remain unreviewed against this window. MI's registered direct offering adds shares but does not rescale per-share volume; no MI or LHSW split turned up in tonight's searches.

```text
# VCIG shared SIP volume; prior 2026-10-05 41/48 slots; log-only
# reconstructed as-of 2026-10-06T20:45:20+00:00; source fetched 2026-10-06T20:46:40.251841Z
VCIG 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=3344455 local=unknown prior-peak=unknown status=warmup
VCIG 2026-10-06  VOLUME-CONTEXT 16:05ET start=2026-10-06T20:05:00+00:00 shares=3445449 local=unknown prior-peak=unknown status=warmup
VCIG 2026-10-06  VOLUME-CONTEXT 16:10ET start=2026-10-06T20:10:00+00:00 shares=2459351 local=unknown prior-peak=unknown status=warmup
VCIG 2026-10-06  VOLUME-CONTEXT 16:15ET start=2026-10-06T20:15:00+00:00 shares=2090194 local=0.6250x prior-peak=unknown status=ok
VCIG 2026-10-06  VOLUME-CONTEXT 16:20ET start=2026-10-06T20:20:00+00:00 shares=1123854 local=0.4570x prior-peak=unknown status=ok
VCIG 2026-10-06  VOLUME-CONTEXT 16:25ET start=2026-10-06T20:25:00+00:00 shares=2771585 local=1.3260x prior-peak=unknown status=ok
VCIG 2026-10-06  VOLUME-CONTEXT 16:30ET start=2026-10-06T20:30:00+00:00 shares=1820673 local=0.8711x prior-peak=unknown status=ok
# BIYA shared SIP volume; prior 2026-10-05 18/48 slots; log-only
# reconstructed as-of 2026-10-06T20:45:20+00:00; source fetched 2026-10-06T20:46:40.857794Z
BIYA 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=1095 local=unknown prior-peak=unknown status=warmup
BIYA 2026-10-06  VOLUME-CONTEXT 16:05ET start=2026-10-06T20:05:00+00:00 shares=285556 local=unknown prior-peak=unknown status=warmup
BIYA 2026-10-06  VOLUME-CONTEXT 16:10ET start=2026-10-06T20:10:00+00:00 shares=1072394 local=unknown prior-peak=unknown status=warmup
BIYA 2026-10-06  VOLUME-CONTEXT 16:15ET start=2026-10-06T20:15:00+00:00 shares=1596650 local=5.5914x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 16:20ET start=2026-10-06T20:20:00+00:00 shares=550815 local=0.5136x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 16:25ET start=2026-10-06T20:25:00+00:00 shares=307657 local=0.2869x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 16:30ET start=2026-10-06T20:30:00+00:00 shares=452655 local=0.8218x prior-peak=unknown status=ok
# SXTC shared SIP volume; prior 2026-10-05 10/48 slots; log-only
# reconstructed as-of 2026-10-06T20:45:20+00:00; source fetched 2026-10-06T20:46:41.484242Z
SXTC 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=75597 local=unknown prior-peak=unknown status=warmup
SXTC 2026-10-06  VOLUME-CONTEXT 16:05ET start=2026-10-06T20:05:00+00:00 shares=683755 local=unknown prior-peak=unknown status=warmup
SXTC 2026-10-06  VOLUME-CONTEXT 16:10ET start=2026-10-06T20:10:00+00:00 shares=212492 local=unknown prior-peak=unknown status=warmup
SXTC 2026-10-06  VOLUME-CONTEXT 16:15ET start=2026-10-06T20:15:00+00:00 shares=103774 local=0.4884x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 16:20ET start=2026-10-06T20:20:00+00:00 shares=295399 local=1.3902x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 16:25ET start=2026-10-06T20:25:00+00:00 shares=394574 local=1.8569x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 16:30ET start=2026-10-06T20:30:00+00:00 shares=1344735 local=4.5523x prior-peak=unknown status=ok
# MI shared SIP volume; prior 2026-10-05 48/48 slots; log-only
# reconstructed as-of 2026-10-06T20:45:20+00:00; source fetched 2026-10-06T20:46:42.091992Z
MI 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=220361 local=unknown prior-peak=0.2093x status=warmup
MI 2026-10-06  VOLUME-CONTEXT 16:05ET start=2026-10-06T20:05:00+00:00 shares=137355 local=unknown prior-peak=0.1304x status=warmup
MI 2026-10-06  VOLUME-CONTEXT 16:10ET start=2026-10-06T20:10:00+00:00 shares=159195 local=unknown prior-peak=0.1512x status=warmup
MI 2026-10-06  VOLUME-CONTEXT 16:15ET start=2026-10-06T20:15:00+00:00 shares=1263614 local=7.9375x prior-peak=1.2000x status=ok
MI 2026-10-06  VOLUME-CONTEXT 16:20ET start=2026-10-06T20:20:00+00:00 shares=2036291 local=12.7912x prior-peak=1.9338x status=ok
MI 2026-10-06  VOLUME-CONTEXT 16:25ET start=2026-10-06T20:25:00+00:00 shares=868347 local=0.6872x prior-peak=0.8246x status=ok
MI 2026-10-06  VOLUME-CONTEXT 16:30ET start=2026-10-06T20:30:00+00:00 shares=427999 local=0.3387x prior-peak=0.4064x status=ok
# LHSW shared SIP volume; prior 2026-10-05 44/48 slots; log-only
# reconstructed as-of 2026-10-06T20:45:20+00:00; source fetched 2026-10-06T20:46:42.735155Z
LHSW 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=11339 local=unknown prior-peak=unknown status=warmup
LHSW 2026-10-06  VOLUME-CONTEXT 16:15ET start=2026-10-06T20:15:00+00:00 shares=60835 local=unknown prior-peak=unknown status=missing-baseline
LHSW 2026-10-06  VOLUME-CONTEXT 16:20ET start=2026-10-06T20:20:00+00:00 shares=118219 local=unknown prior-peak=unknown status=missing-baseline
LHSW 2026-10-06  VOLUME-CONTEXT 16:25ET start=2026-10-06T20:25:00+00:00 shares=399935 local=unknown prior-peak=unknown status=missing-baseline
LHSW 2026-10-06  VOLUME-CONTEXT 16:30ET start=2026-10-06T20:30:00+00:00 shares=373669 local=3.1608x prior-peak=unknown status=ok
# NCPL shared SIP volume; prior 2026-10-05 25/48 slots; log-only
# reconstructed as-of 2026-10-06T20:45:20+00:00; source fetched 2026-10-06T20:46:43.332847Z
NCPL 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=71987 local=unknown prior-peak=unknown status=warmup
NCPL 2026-10-06  VOLUME-CONTEXT 16:05ET start=2026-10-06T20:05:00+00:00 shares=71440 local=unknown prior-peak=unknown status=warmup
NCPL 2026-10-06  VOLUME-CONTEXT 16:10ET start=2026-10-06T20:10:00+00:00 shares=7284 local=unknown prior-peak=unknown status=warmup
NCPL 2026-10-06  VOLUME-CONTEXT 16:15ET start=2026-10-06T20:15:00+00:00 shares=4790 local=0.0670x prior-peak=unknown status=ok
NCPL 2026-10-06  VOLUME-CONTEXT 16:20ET start=2026-10-06T20:20:00+00:00 shares=1020 local=0.1400x prior-peak=unknown status=ok
NCPL 2026-10-06  VOLUME-CONTEXT 16:25ET start=2026-10-06T20:25:00+00:00 shares=7199 local=1.5029x prior-peak=unknown status=ok
NCPL 2026-10-06  VOLUME-CONTEXT 16:30ET start=2026-10-06T20:30:00+00:00 shares=234 local=0.0489x prior-peak=unknown status=ok
```

**Book diagnostic (verbatim; log-only)** for the five tradable >10% names with accumulating SIP volume:

```text
VCIG BOOK iex bid $1.53 x200 / ask $1.55 x100 @ 2026-10-06 16:47:05 ET age 0s two-sided spread 1.29% of ask
VCIG BOOK sip-15m bid $1.97 x1000 / ask $1.98 x1500 @ 2026-10-06 16:32:05 ET age 15m00s two-sided spread 0.51% of ask
VCIG BOOK refresh +15s iex advanced @ 2026-10-06 16:47:20 ET
VCIG BOOK verdict: IEX FRESH; SIP-15m TWO-SIDED (observed 2026-10-06 16:47:05 ET; log-only)
BIYA BOOK iex bid $2.05 x100 / ask $2.09 x100 @ 2026-10-06 16:40:59 ET age 6m05s two-sided spread 1.91% of ask
BIYA BOOK sip-15m bid $1.84 x500 / ask $1.85 x1900 @ 2026-10-06 16:32:05 ET age 15m00s two-sided spread 0.54% of ask
BIYA BOOK refresh +15s iex unchanged @ 2026-10-06 16:40:59 ET
BIYA BOOK verdict: IEX STALE 6m05s; SIP-15m TWO-SIDED (observed 2026-10-06 16:47:05 ET; log-only)
SXTC BOOK iex bid $2.29 x100 / ask $2.36 x100 @ 2026-10-06 16:46:54 ET age 11s two-sided spread 2.97% of ask
SXTC BOOK sip-15m bid $2.19 x100 / ask $2.21 x2000 @ 2026-10-06 16:32:05 ET age 15m00s two-sided spread 0.90% of ask
SXTC BOOK refresh +15s iex unchanged @ 2026-10-06 16:46:54 ET
SXTC BOOK verdict: IEX FRESH; SIP-15m TWO-SIDED (observed 2026-10-06 16:47:05 ET; log-only)
MI BOOK iex bid $1.56 x100 / ask $1.58 x100 @ 2026-10-06 16:46:54 ET age 11s two-sided spread 1.27% of ask
MI BOOK sip-15m bid $1.57 x3000 / ask $1.59 x2100 @ 2026-10-06 16:32:04 ET age 15m01s two-sided spread 1.26% of ask
MI BOOK refresh +15s iex advanced @ 2026-10-06 16:47:18 ET
MI BOOK verdict: IEX FRESH; SIP-15m TWO-SIDED (observed 2026-10-06 16:47:05 ET; log-only)
LHSW BOOK iex bid $0.4695 x100 / ask $0.6496 x100 @ 2026-10-06 16:00:00 ET age 47m05s two-sided spread 27.72% of ask
LHSW BOOK sip-15m bid $0.5876 x100 / ask $0.6000 x200 @ 2026-10-06 16:32:01 ET age 15m04s two-sided spread 2.07% of ask
LHSW BOOK refresh +15s iex unchanged @ 2026-10-06 16:00:00 ET
LHSW BOOK verdict: IEX STALE 47m05s; SIP-15m TWO-SIDED (observed 2026-10-06 16:47:05 ET; log-only)
```

**23:00 checklist:** BIYA is the lead. Enter if it still shows >10% AH, SIP keeps printing hundreds of thousands of shares per bar, it holds within ~20% of its high, and the IEX book is fresh and two-sided (Grade None, concern noted). VCIG enters only if it recovers to within ~20% of its $2.10 high on accumulating SIP volume; otherwise it is a SPIKE→FADE skip. SXTC stays a Day% skip on DEAD-CAT-OVERRIDE WATCH; record whether it holds above the $2.08 prior close. MI stays a dead-cat and Grade D skip. LHSW stays skipped unless it rebuilds above $0.63 (+10%) on real volume. OLOX needs >10% AH for a first qualifying appearance. Keep all 28 names from the 21:30 watchlist in the pipeline for the final-scan cross-check. KAPA's dead-cat guard still applies. EVOL, MHUAF, VNPKF, WTLLF, NWINF, and KHDHF remain untradable (carried).

**Daily email:** Report BIYA's new $1.94 SIP high with CONFIRM-3 YES ahead of the 23:00 entry window, VCIG's volume-backed $2.10 high at 16:25 ET followed by a 27% fade, SXTC's SIP-confirmed reclaim of its prior close (1.34M shares, high $2.58) while blocked by Day -39.9% on DEAD-CAT-OVERRIDE WATCH, and the MI dead-cat bounce on a same-day registered direct offering. No item from this scan requires Juan's input.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|

No entries at the 21:30 CEST regular-session scan. Entries open at the 23:00 CEST scan.
