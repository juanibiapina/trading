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

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|

No entries at the 21:30 CEST regular-session scan. Entries open at the 23:00 CEST scan.
