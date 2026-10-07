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

## Scan 23:00 CEST (5:00 PM ET)

**Decision:** Entered **BIYA**, 52 shares filled at **$1.91** on Alpaca (order `d20b26bc`, 17:01:28 ET). It is the only candidate that clears every gate at this first entry scan. VCIG is a SPIKE→FADE skip: it peaked at $2.10 at 16:25 ET and traded at $1.34 at 17:00 ET, 36% below that high. SXTC stays blocked by Day -39.9% and remains on DEAD-CAT-OVERRIDE WATCH. MI (dead-cat bounce, Grade D dilution) and NCPL (thin drift) are skips. AH appearance counts are now VCIG **5**, SXTC **5**, BIYA **4**, NCPL **3**, MI **2**, LHSW **1**.

`python3 scripts/scan.py --all` ran at 17:00:13 ET (23:00:13 CEST / 21:00:13 UTC) in the AFTERHOURS session and returned 8 hits. The US trading date is 2026-10-06. Repository sync completed before the scan.

```text
  Supplementary AH-change-only (>15%, not in volume pass): none
  AH >10% at this snapshot (unrounded): BIYA, MI, NCPL, SXTC, VCIG
```

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| VCIG | [TV](https://www.tradingview.com/chart/?symbol=VCIG) | $1.41 | +54.8% | +18.4% | $1.67 | +83.3% | 18.2M | 3.2M | 5.6x | 1.0M | Miscellaneous Commercial Services |
| MI | [TV](https://www.tradingview.com/chart/?symbol=MI) | $1.23 | -82.4% | +24.0% | $1.52 | -78.2% | 5.3M | 18.5M | 0.3x | 542K | Internet Software/Services |
| BIYA | [TV](https://www.tradingview.com/chart/?symbol=BIYA) | $1.36 | -2.5% | +37.7% | $1.88 | +34.3% | 4.8M | 2.1M | 2.3x | 2.7M | Personnel Services |
| SXTC | [TV](https://www.tradingview.com/chart/?symbol=SXTC) | $1.25 | -39.9% | +70.4% | $2.13 | +2.4% | 3.5M | 892K | 3.9x | 1.0M | Pharmaceuticals: Major |
| OLOX | [TV](https://www.tradingview.com/chart/?symbol=OLOX) | $1.25 | +42.0% | +9.2% | $1.36 | +55.1% | 1.4M | 15.2M | 0.1x | 1.3M | Building Products |
| MTEN | [TV](https://www.tradingview.com/chart/?symbol=MTEN) | $0.96 | -0.4% | +9.5% | $1.05 | +9.1% | 716K | 216K | 3.3x | 6.1M | Industrial Machinery |
| LCFY | [TV](https://www.tradingview.com/chart/?symbol=LCFY) | $2.05 | -12.4% | +6.8% | $2.19 | -6.4% | 222K | 321K | 0.7x | 1.4M | Packaged Software |
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $1.09 | -17.4% | +10.1% | $1.20 | -9.1% | 161K | 14.3M | 0.0x | 4.4M | Miscellaneous Commercial Services |

### Evaluation notes

**Tradability:** BIYA was re-verified `tradable=true` (Nasdaq, active) immediately before the order. MTEN (Nasdaq) returned `tradable=true`. VCIG, SXTC, MI, NCPL, OLOX, and LCFY were verified earlier tonight.

**New SIP bars** (`broker.js bars SYM --tf 5Min --start 2026-10-06T20:35:00Z`, feed=sip). The newest bar starts 16:45 ET, about 15 minutes behind the scan, which matches the free-tier delay. Earlier bars are in the 22:20–22:45 tables.

| Ticker | Bar ET | Open | High | Low | Close | Shares | VWAP | Trades |
|--------|--------|------|------|-----|-------|--------|------|--------|
| BIYA | 16:35 | $1.85 | $2.04 | $1.81 | $2.04 | 413,407 | $1.90 | 2,927 |
| BIYA | 16:40 | $2.03 | $2.07 | $1.82 | $1.88 | 802,489 | $1.95 | 5,837 |
| BIYA | 16:45 | $1.88 | $1.92 | $1.79 | $1.84 | 347,463 | $1.85 | 2,031 |
| VCIG | 16:35 | $1.90 | $2.00 | $1.80 | $1.83 | 1,591,789 | $1.90 | 8,803 |
| VCIG | 16:40 | $1.83 | $1.84 | $1.66 | $1.66 | 1,295,319 | $1.76 | 7,199 |
| VCIG | 16:45 | $1.67 | $1.67 | $1.43 | $1.48 | 2,568,431 | $1.54 | 11,743 |
| SXTC | 16:35 | $2.18 | $2.20 | $1.88 | $1.93 | 563,974 | $2.03 | 4,829 |
| SXTC | 16:40 | $1.94 | $2.25 | $1.94 | $2.13 | 508,099 | $2.13 | 4,700 |
| SXTC | 16:45 | $2.13 | $2.49 | $2.08 | $2.37 | 865,653 | $2.34 | 7,320 |
| MI | 16:35 | $1.52 | $1.55 | $1.40 | $1.50 | 400,416 | $1.48 | 1,897 |
| MI | 16:40 | $1.50 | $1.56 | $1.48 | $1.52 | 214,703 | $1.53 | 1,011 |
| MI | 16:45 | $1.52 | $1.63 | $1.52 | $1.52 | 461,613 | $1.59 | 1,905 |
| NCPL | 16:35 | $1.20 | $1.21 | $1.20 | $1.20 | 1,540 | $1.20 | 5 |
| NCPL | 16:40 | $1.20 | $1.21 | $1.20 | $1.20 | 1,404 | $1.20 | 8 |
| NCPL | 16:45 | $1.20 | $1.20 | $1.20 | $1.20 | 175 | $1.20 | 1 |
| MTEN | 16:30 | $0.96 | $1.12 | $0.96 | $1.12 | 152,894 | $1.06 | 579 |
| MTEN | 16:35 | $1.12 | $1.12 | $1.00 | $1.11 | 170,255 | $1.05 | 715 |
| MTEN | 16:40 | $1.10 | $1.17 | $1.02 | $1.05 | 478,591 | $1.09 | 2,144 |
| MTEN | 16:45 | $1.05 | $1.06 | $0.96 | $0.99 | 166,035 | $1.00 | 762 |

**Yahoo timeline (shape only, not volume or exact levels):**

| Ticker | 16:45 | 16:50 | 16:55 | 17:00 |
|--------|-------|-------|-------|-------|
| BIYA | $1.84 | $1.85 | $1.85 | $1.87 |
| VCIG | $1.48 | $1.40 | $1.36 | $1.34 |
| SXTC | $2.37 | $2.17 | $2.06 | $2.05 |
| MI | $1.52 | $1.57 | $1.58 | $1.55 |

BIYA's one-minute Yahoo bars show $2.07 at 16:36–16:37 ET and $1.879 at 17:01 ET, inside a $1.83–$1.93 range since 16:40.

**BIYA — fourth qualifying AH scan; ENTERED at $1.91 (Grade None).** Every entry gate passes:

- **Appearance gate:** >10% AH in four AH scans (22:25, 22:30, 22:45, 23:00).
- **Day%** -2.5% (above -15%). **Total%** at the fill is +36.4% from the $1.40 prior close, far under the +150% ceiling.
- **Trajectory: BUILD and hold.** SIP made a new high of **$2.07 in the 16:40 bar** on 802,489 shares / 5,837 trades, so the high is well outside the 16:00–16:15 opening window and the first-bar-spike skip does not apply. CONFIRM-3 has read YES since 22:30. At 17:00 ET the price sat at $1.87–$1.88, **9% below the high**, inside the ~20% hold threshold.
- **SIP volume is real and accumulating:** every bar since 16:10 has carried 300K–1.6M shares and 2,000–10,000 trades. The scanner's 2.3x VRatio understates it.
- **SIP corroborates the scanner price:** the 16:45 bar VWAP of $1.85 and close of $1.84 match the scanner's $1.88; this is not a bad print.
- **Book:** the IEX quote at 16:54:16 ET was two-sided (`BIYA  bid $1.88 x100  ask $1.92 x100`). IEX stops quoting at 17:00 ET, so the quote was 7 minutes old at the order; the delayed SIP book at 16:47 ET was $1.86/$1.87 with size on both sides.
- **Catalyst Grade None — no catalyst found.** One more dated search ("Baiya International BIYA October 6 2026") returned only quote and market-cap pages. Across tonight's scans, eleven searches found nothing dated October 6; background is the late-September first-half fiscal 2026 results, the July 8, 2026 1-for-10 reverse split, and the October 5 Wall Street Zen rating change. Concern noted; exit at the first premarket opportunity.
- **Prior activity:** re-ignition one week after the September 29–30 spike (11.53M shares on September 30, high $3.18), followed by a slide to $1.40. It fails a strict "first day of unusual activity" reading but is not a MULTI-SESSION-RUNNER, because the intervening sessions fell. `WINNERS_TRACKING.md` has no BIYA entry.
- **Pre-buy checks:** `broker.js positions` showed no open positions and `orders all` showed no BIYA order today.
- **Order:** `buy BIYA 52 --limit 1.95 --ext` (QTY = floor($100 / $1.92 ask)). Filled 52 @ **$1.91** at 17:01:28 ET; cost $99.32. Grade None hard stop -10% = $1.72.
- **Chase check:** the qualifying-scan reading (22:30, second >10% appearance) was $1.72 / Total +22.9%. The fill's Total +36.4% is a 13.5-point gap and far from the >~120% fade zone, so no CHASE-CAP note applies.

**VCIG — fifth qualifying AH scan; skip (SPIKE→FADE).** The AH high is $2.10 in the 16:25 bar. Since then each bar closed lower ($1.90 → $1.83 → $1.66 → $1.48), and the 16:45 bar sold off to a $1.43 low on the heaviest volume since the open (2,568,431 shares / 11,743 trades). Yahoo shows $1.34 at 17:00 ET, **36% below the high** and +47% Total from the $0.91 prior close. The scanner's $1.67 matches the 16:40 bar close and lags the tape. The last IEX quote (16:59:59 ET) was a wide $1.32/$1.96. It peaked before 17:30 ET and is declining across scans, so it fails the hold rule. CONFIRM-3 stays NO. Catalyst Grade C (October 6 GlobeNewswire VGAIN Compute launch) is unchanged. The 22:20 FIRST-BAR-SPIKE WATCH hypothetical ($1.69 at 16:20 ET) stays on record for morning measurement.

**SXTC — fifth qualifying AH scan; skip live entry (Day -39.9%); DEAD-CAT-OVERRIDE WATCH continues.** The 22:25 hypothetical ($1.57 at 16:25 ET) stands. Scanner AH change rose to **+70.4%** ($2.13, Total +2.4%), which corroborates the 16:30–16:45 leg. SIP shows the leg held on real volume: 563,974 → 508,099 → 865,653 shares per bar (4,700–7,320 trades), with a 16:45 bar high of $2.49, close of $2.37, and VWAP of $2.34, all above the $2.08 prior close. Yahoo then shows $2.17 at 16:50 and **$2.05 at 17:00**, just below the prior close and 20.5% below the $2.58 AH high (16:30 bar). The IEX quote is frozen at 16:48:07 ET ($2.19/$2.24). CONFIRM-3 still scores the failed 16:05 ignition and reads NO. Catalyst Grade None is unchanged.

**MI — second >10% AH appearance; skip (dead-cat bounce, Grade D).** AH change slipped from +25.2% to +24.0%, so it does not meet the DEAD-CAT-OVERRIDE WATCH condition of AH% rising across two AH scans. SIP shows a $1.48–$1.63 range on 214,703–461,613 shares per bar since 16:35, 11–16% below the $1.84 high at 16:20 ET and 78% below the $7.00 prior close. Yahoo shows $1.55 at 17:00. The same-day $2.55M registered direct offering keeps it Grade D.

**NCPL — third >10% AH appearance; skip stands (thin drift, Day -17.4%).** SIP printed 1,540, 1,404, and **175 shares** in the 16:35–16:45 bars, with 1–8 trades each. The 22:20 FIRST-BAR-SPIKE WATCH hypothetical stands.

**Below threshold:**

- **MTEN** (new; +9.5% AH, Day -0.4%, float 6.1M, VRatio 3.3x): SIP shows ignition in the 16:30 bar (152,894 shares / 579 trades), a high of **$1.17** in the 16:40 bar on 478,591 shares / 2,144 trades (+21.9% from the $0.96 close), then a 16:45 close of $0.99 (+3%). It is a spike that has already faded. It needs a >10% reading for a first qualifying appearance.
- **OLOX** (+9.2% AH, Day +42.0%, Total +55.1%; day 2 after its October 5 AH→PM win): SIP volume is fading (289,334 → 135,341 → 65,443 → 59,308 shares) with the price at $1.34–$1.37. No qualifying appearance yet.
- **LCFY** (+6.8% AH, Day -12.4%): tracked only.
- **LHSW** is absent from this scan; its 22:45 skip stands.

**Instrumentation (verbatim; log-only):**

```text
BIYA 2026-10-06  SPIKE  16:08ET  +21%  $1.65  372 trades / 58k sh  (first co-spike bar) (as-of 17:00ET)
BIYA 2026-10-06  CONFIRM-3  YES ignition 16:05ET 260.8x; confirmed 16:15ET $1.81 as-of 17:00ET
VCIG 2026-10-06  NO-SPIKE  peak +49% @16:28ET  (no bar cleared +15% on a volume co-spike) (as-of 17:00ET)
VCIG 2026-10-06  CONFIRM-3  NO no local-volume new-high ignition as-of 17:00ET
SXTC 2026-10-06  SPIKE  16:03ET  +32%  $1.65  135 trades / 30k sh  (first co-spike bar) (as-of 17:00ET)
SXTC 2026-10-06  CONFIRM-3  NO ignition 16:05ET failed third-bar hold/volume as-of 17:00ET
MI 2026-10-06  SPIKE  16:18ET  +30%  $1.60  2066 trades / 421k sh  (first co-spike bar) (as-of 17:00ET)
MI 2026-10-06  CONFIRM-3  NO ignition 16:15ET failed third-bar hold/volume as-of 17:00ET
NCPL 2026-10-06  NO-SPIKE  peak +17% @16:03ET  (no bar cleared +15% on a volume co-spike) (as-of 17:00ET)
NCPL 2026-10-06  CONFIRM-3  NO no local-volume new-high ignition as-of 17:00ET
```

**Shared SIP volume context (`sip-ah-volume-v1`, log-only):** The prior trading date is 2026-10-05, a normal Monday session. Inputs were fetched with `broker.js bars SYM --tf 5Min --start 2026-10-05T20:00:00Z --limit 1000 --feed sip --json` (one page each, no next-page token) and archived as `log/2026-10-06/SYM-2300-volume-sip.json`, with computed rows in `SYM-2300-volume-metric.json`. MI is the only name with complete prior-session coverage (48/48). The others stay incomplete (BIYA 18/48, VCIG 41/48, SXTC 10/48, NCPL 25/48), so their prior-peak ratios remain unknown. BIYA's 16:40 bar, which set the new high, was 1.94x local. The SXTC share-consolidation headline and BIYA's July 1-for-10 reverse split remain unreviewed against this window.

```text
# BIYA shared SIP volume; prior 2026-10-05 18/48 slots; log-only
# reconstructed as-of 2026-10-06T21:00:13+00:00; source fetched 2026-10-06T21:01:58.624913Z
BIYA 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=1095 local=unknown prior-peak=unknown status=warmup
BIYA 2026-10-06  VOLUME-CONTEXT 16:05ET start=2026-10-06T20:05:00+00:00 shares=285556 local=unknown prior-peak=unknown status=warmup
BIYA 2026-10-06  VOLUME-CONTEXT 16:10ET start=2026-10-06T20:10:00+00:00 shares=1072394 local=unknown prior-peak=unknown status=warmup
BIYA 2026-10-06  VOLUME-CONTEXT 16:15ET start=2026-10-06T20:15:00+00:00 shares=1596650 local=5.5914x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 16:20ET start=2026-10-06T20:20:00+00:00 shares=550815 local=0.5136x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 16:25ET start=2026-10-06T20:25:00+00:00 shares=307657 local=0.2869x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 16:30ET start=2026-10-06T20:30:00+00:00 shares=452655 local=0.8218x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 16:35ET start=2026-10-06T20:35:00+00:00 shares=413407 local=0.9133x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 16:40ET start=2026-10-06T20:40:00+00:00 shares=802489 local=1.9412x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 16:45ET start=2026-10-06T20:45:00+00:00 shares=347463 local=0.7676x prior-peak=unknown status=ok
# VCIG shared SIP volume; prior 2026-10-05 41/48 slots; log-only
# reconstructed as-of 2026-10-06T21:00:13+00:00; source fetched 2026-10-06T21:01:59.257259Z
VCIG 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=3344455 local=unknown prior-peak=unknown status=warmup
VCIG 2026-10-06  VOLUME-CONTEXT 16:05ET start=2026-10-06T20:05:00+00:00 shares=3445449 local=unknown prior-peak=unknown status=warmup
VCIG 2026-10-06  VOLUME-CONTEXT 16:10ET start=2026-10-06T20:10:00+00:00 shares=2459351 local=unknown prior-peak=unknown status=warmup
VCIG 2026-10-06  VOLUME-CONTEXT 16:15ET start=2026-10-06T20:15:00+00:00 shares=2090194 local=0.6250x prior-peak=unknown status=ok
VCIG 2026-10-06  VOLUME-CONTEXT 16:20ET start=2026-10-06T20:20:00+00:00 shares=1123854 local=0.4570x prior-peak=unknown status=ok
VCIG 2026-10-06  VOLUME-CONTEXT 16:25ET start=2026-10-06T20:25:00+00:00 shares=2771585 local=1.3260x prior-peak=unknown status=ok
VCIG 2026-10-06  VOLUME-CONTEXT 16:30ET start=2026-10-06T20:30:00+00:00 shares=1820673 local=0.8711x prior-peak=unknown status=ok
VCIG 2026-10-06  VOLUME-CONTEXT 16:35ET start=2026-10-06T20:35:00+00:00 shares=1591789 local=0.8743x prior-peak=unknown status=ok
VCIG 2026-10-06  VOLUME-CONTEXT 16:40ET start=2026-10-06T20:40:00+00:00 shares=1295319 local=0.7115x prior-peak=unknown status=ok
VCIG 2026-10-06  VOLUME-CONTEXT 16:45ET start=2026-10-06T20:45:00+00:00 shares=2568431 local=1.6135x prior-peak=unknown status=ok
# SXTC shared SIP volume; prior 2026-10-05 10/48 slots; log-only
# reconstructed as-of 2026-10-06T21:00:13+00:00; source fetched 2026-10-06T21:01:59.875738Z
SXTC 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=75597 local=unknown prior-peak=unknown status=warmup
SXTC 2026-10-06  VOLUME-CONTEXT 16:05ET start=2026-10-06T20:05:00+00:00 shares=683755 local=unknown prior-peak=unknown status=warmup
SXTC 2026-10-06  VOLUME-CONTEXT 16:10ET start=2026-10-06T20:10:00+00:00 shares=212492 local=unknown prior-peak=unknown status=warmup
SXTC 2026-10-06  VOLUME-CONTEXT 16:15ET start=2026-10-06T20:15:00+00:00 shares=103774 local=0.4884x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 16:20ET start=2026-10-06T20:20:00+00:00 shares=295399 local=1.3902x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 16:25ET start=2026-10-06T20:25:00+00:00 shares=394574 local=1.8569x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 16:30ET start=2026-10-06T20:30:00+00:00 shares=1344735 local=4.5523x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 16:35ET start=2026-10-06T20:35:00+00:00 shares=563974 local=1.4293x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 16:40ET start=2026-10-06T20:40:00+00:00 shares=508099 local=0.9009x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 16:45ET start=2026-10-06T20:45:00+00:00 shares=865653 local=1.5349x prior-peak=unknown status=ok
# MI shared SIP volume; prior 2026-10-05 48/48 slots; log-only
# reconstructed as-of 2026-10-06T21:00:13+00:00; source fetched 2026-10-06T21:02:00.479386Z
MI 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=220361 local=unknown prior-peak=0.2093x status=warmup
MI 2026-10-06  VOLUME-CONTEXT 16:05ET start=2026-10-06T20:05:00+00:00 shares=137355 local=unknown prior-peak=0.1304x status=warmup
MI 2026-10-06  VOLUME-CONTEXT 16:10ET start=2026-10-06T20:10:00+00:00 shares=159195 local=unknown prior-peak=0.1512x status=warmup
MI 2026-10-06  VOLUME-CONTEXT 16:15ET start=2026-10-06T20:15:00+00:00 shares=1263614 local=7.9375x prior-peak=1.2000x status=ok
MI 2026-10-06  VOLUME-CONTEXT 16:20ET start=2026-10-06T20:20:00+00:00 shares=2036291 local=12.7912x prior-peak=1.9338x status=ok
MI 2026-10-06  VOLUME-CONTEXT 16:25ET start=2026-10-06T20:25:00+00:00 shares=868347 local=0.6872x prior-peak=0.8246x status=ok
MI 2026-10-06  VOLUME-CONTEXT 16:30ET start=2026-10-06T20:30:00+00:00 shares=427999 local=0.3387x prior-peak=0.4064x status=ok
MI 2026-10-06  VOLUME-CONTEXT 16:35ET start=2026-10-06T20:35:00+00:00 shares=400416 local=0.4611x prior-peak=0.3803x status=ok
MI 2026-10-06  VOLUME-CONTEXT 16:40ET start=2026-10-06T20:40:00+00:00 shares=214703 local=0.5016x prior-peak=0.2039x status=ok
MI 2026-10-06  VOLUME-CONTEXT 16:45ET start=2026-10-06T20:45:00+00:00 shares=461613 local=1.1528x prior-peak=0.4384x status=ok
# NCPL shared SIP volume; prior 2026-10-05 25/48 slots; log-only
# reconstructed as-of 2026-10-06T21:00:13+00:00; source fetched 2026-10-06T21:02:01.094138Z
NCPL 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=71987 local=unknown prior-peak=unknown status=warmup
NCPL 2026-10-06  VOLUME-CONTEXT 16:05ET start=2026-10-06T20:05:00+00:00 shares=71440 local=unknown prior-peak=unknown status=warmup
NCPL 2026-10-06  VOLUME-CONTEXT 16:10ET start=2026-10-06T20:10:00+00:00 shares=7284 local=unknown prior-peak=unknown status=warmup
NCPL 2026-10-06  VOLUME-CONTEXT 16:15ET start=2026-10-06T20:15:00+00:00 shares=4790 local=0.0670x prior-peak=unknown status=ok
NCPL 2026-10-06  VOLUME-CONTEXT 16:20ET start=2026-10-06T20:20:00+00:00 shares=1020 local=0.1400x prior-peak=unknown status=ok
NCPL 2026-10-06  VOLUME-CONTEXT 16:25ET start=2026-10-06T20:25:00+00:00 shares=7199 local=1.5029x prior-peak=unknown status=ok
NCPL 2026-10-06  VOLUME-CONTEXT 16:30ET start=2026-10-06T20:30:00+00:00 shares=234 local=0.0489x prior-peak=unknown status=ok
NCPL 2026-10-06  VOLUME-CONTEXT 16:35ET start=2026-10-06T20:35:00+00:00 shares=1540 local=1.5098x prior-peak=unknown status=ok
NCPL 2026-10-06  VOLUME-CONTEXT 16:40ET start=2026-10-06T20:40:00+00:00 shares=1404 local=0.9117x prior-peak=unknown status=ok
NCPL 2026-10-06  VOLUME-CONTEXT 16:45ET start=2026-10-06T20:45:00+00:00 shares=175 local=0.1246x prior-peak=unknown status=ok
```

**Book diagnostic (verbatim; log-only)** for the four tradable >10% names with accumulating SIP volume. From this scan on, IEX quotes are frozen at or before 17:00 ET, when IEX stops quoting.

```text
BIYA BOOK iex bid $1.88 x100 / ask $1.92 x100 @ 2026-10-06 16:54:16 ET age 8m01s two-sided spread 2.08% of ask
BIYA BOOK sip-15m bid $1.86 x900 / ask $1.87 x100 @ 2026-10-06 16:47:15 ET age 15m01s two-sided spread 0.53% of ask
BIYA BOOK refresh +15s iex unchanged @ 2026-10-06 16:54:16 ET
BIYA BOOK verdict: IEX STALE 8m01s; SIP-15m TWO-SIDED (observed 2026-10-06 17:02:16 ET; log-only)
VCIG BOOK iex bid $1.32 x2300 / ask $1.96 x200 @ 2026-10-06 16:59:59 ET age 2m18s two-sided spread 32.65% of ask
VCIG BOOK sip-15m bid $1.53 x3900 / ask $1.54 x3000 @ 2026-10-06 16:47:17 ET age 15m00s two-sided spread 0.65% of ask
VCIG BOOK refresh +15s iex unchanged @ 2026-10-06 16:59:59 ET
VCIG BOOK verdict: IEX STALE 2m18s; SIP-15m TWO-SIDED (observed 2026-10-06 17:02:16 ET; log-only)
SXTC BOOK iex bid $2.19 x100 / ask $2.24 x100 @ 2026-10-06 16:48:07 ET age 14m09s two-sided spread 2.23% of ask
SXTC BOOK sip-15m bid $2.34 x800 / ask $2.37 x2000 @ 2026-10-06 16:47:16 ET age 15m01s two-sided spread 1.27% of ask
SXTC BOOK refresh +15s iex unchanged @ 2026-10-06 16:48:07 ET
SXTC BOOK verdict: IEX STALE 14m09s; SIP-15m TWO-SIDED (observed 2026-10-06 17:02:16 ET; log-only)
MI BOOK iex bid $1.56 x100 / ask $1.59 x100 @ 2026-10-06 16:59:55 ET age 2m21s two-sided spread 1.89% of ask
MI BOOK sip-15m bid $1.58 x1000 / ask $1.59 x2000 @ 2026-10-06 16:47:16 ET age 15m00s two-sided spread 0.63% of ask
MI BOOK refresh +15s iex unchanged @ 2026-10-06 16:59:55 ET
MI BOOK verdict: IEX STALE 2m21s; SIP-15m TWO-SIDED (observed 2026-10-06 17:02:16 ET; log-only)
```

**Carry forward:** BIYA is entered; later scans skip it as `already entered` and track it only. VCIG is a SPIKE→FADE skip unless it rebuilds to within ~20% of $2.10 (about $1.68) on accumulating SIP volume. SXTC stays a Day% skip on DEAD-CAT-OVERRIDE WATCH; record whether it holds near its $2.08 prior close. MI stays a dead-cat and Grade D skip. MTEN needs a >10% reading for a first qualifying appearance. Keep all 28 names from the 21:30 watchlist in the pipeline for the final-scan cross-check. KAPA's dead-cat guard and OLOX's day-2 tag still apply. EVOL, MHUAF, VNPKF, WTLLF, NWINF, and KHDHF remain untradable (carried).

**Daily email:** Report the BIYA entry (52 @ $1.91, Grade None, no catalyst found in eleven searches; BUILD to a $2.07 SIP high at 16:40 ET on 802K shares, CONFIRM-3 YES, held 9% below the high at entry), VCIG's fade to $1.34 (36% off its $2.10 high) on the heaviest bar since the open, and SXTC's DEAD-CAT-OVERRIDE WATCH leg holding $2.37–$2.49 in the 16:45 SIP bar before Yahoo showed $2.05 at 17:00. No item from this scan requires Juan's input.

## Scan 23:30 CEST (5:30 PM ET)

**Decision:** No new entry. Every name with two or more qualifying AH scans is blocked: SXTC by Day -39.9% (DEAD-CAT-OVERRIDE WATCH continues), MI as a fading dead-cat bounce with Grade D dilution, and NCPL as a thin drift. BIYA is `already entered` and trades at $2.14 (+12.0% on the position). **MTEN** is the new lead: a 16:30 ET 6-K reported a completed $15M cash acquisition, and the 17:15 SIP bar ignited on 969,962 shares / 5,649 trades to $1.29. This is its first >10% AH appearance, so it can only qualify at 00:00. LCFY (first appearance, thin volume) and WHLR (first appearance, Day -16.5%) are skips. AH appearance counts: SXTC **6**, BIYA **5**, VCIG **5** (absent tonight), NCPL **4**, MI **3**, MTEN **1**, LCFY **1**, WHLR **1**, LHSW **1**.

`python3 scripts/scan.py --all` ran at 17:30:14 ET (23:30:14 CEST / 21:30:14 UTC) in the AFTERHOURS session and returned 11 hits. The US trading date is 2026-10-06. Repository sync completed before the scan.

```text
  Supplementary AH-change-only (>15%, not in volume pass): none
  AH >10% at this snapshot (unrounded): BIYA, LCFY, MI, MTEN, NCPL, SXTC, WHLR
```

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| MI | [TV](https://www.tradingview.com/chart/?symbol=MI) | $1.23 | -82.4% | +20.6% | $1.48 | -78.8% | 6.4M | 18.6M | 0.3x | 542K | Internet Software/Services |
| BIYA | [TV](https://www.tradingview.com/chart/?symbol=BIYA) | $1.36 | -2.5% | +43.6% | $1.96 | +40.0% | 6.4M | 2.3M | 2.8x | 2.7M | Personnel Services |
| SXTC | [TV](https://www.tradingview.com/chart/?symbol=SXTC) | $1.25 | -39.9% | +74.4% | $2.18 | +4.8% | 5.3M | 1.1M | 4.8x | 1.0M | Pharmaceuticals: Major |
| OLOX | [TV](https://www.tradingview.com/chart/?symbol=OLOX) | $1.25 | +42.0% | +8.0% | $1.35 | +53.4% | 1.7M | 15.2M | 0.1x | 1.3M | Building Products |
| QTEX | [TV](https://www.tradingview.com/chart/?symbol=QTEX) | $1.59 | +3.2% | +5.7% | $1.68 | +9.1% | 1.1M | 35.0M | 0.0x | 58.6M | Medical Specialties |
| WHLR | [TV](https://www.tradingview.com/chart/?symbol=WHLR) | $0.91 | -16.5% | +13.2% | $1.03 | -5.5% | 1.1M | 13.2M | 0.1x | 568K | Real Estate Investment Trusts |
| MTEN | [TV](https://www.tradingview.com/chart/?symbol=MTEN) | $0.96 | -0.4% | +10.6% | $1.06 | +10.1% | 951K | 245K | 3.9x | 6.1M | Industrial Machinery |
| LCFY | [TV](https://www.tradingview.com/chart/?symbol=LCFY) | $2.05 | -12.4% | +21.5% | $2.49 | +6.4% | 383K | 339K | 1.1x | 1.4M | Packaged Software |
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $1.09 | -17.4% | +10.1% | $1.20 | -9.1% | 163K | 14.3M | 0.0x | 4.4M | Miscellaneous Commercial Services |
| ALDX | [TV](https://www.tradingview.com/chart/?symbol=ALDX) | $0.92 | -0.8% | +6.9% | $0.98 | +6.0% | 87K | 2.9M | 0.0x | 58.1M | Biotechnology |
| DCX | [TV](https://www.tradingview.com/chart/?symbol=DCX) | $3.11 | -8.0% | +7.7% | $3.35 | -0.9% | 77K | 542K | 0.1x | 259K | Motor Vehicles |

### Evaluation notes

**Tradability:** WHLR, LCFY, and MTEN returned `tradable=true` (Nasdaq, active) before the SIP and catalyst workup. BIYA, SXTC, MI, and NCPL were verified earlier tonight.

**New SIP bars** (`broker.js bars SYM --tf 5Min`, feed=sip). The newest bar starts 17:15 ET, about 15 minutes behind the scan, which matches the free-tier delay. Earlier bars for carried names are in the 22:20–23:00 tables.

| Ticker | Bar ET | Open | High | Low | Close | Shares | VWAP | Trades |
|--------|--------|------|------|-----|-------|--------|------|--------|
| MTEN | 16:50 | $0.99 | $1.00 | $0.96 | $0.98 | 25,301 | $0.98 | 118 |
| MTEN | 16:55 | $0.99 | $1.05 | $0.98 | $1.04 | 12,949 | $1.01 | 88 |
| MTEN | 17:00 | $1.04 | $1.06 | $1.02 | $1.05 | 33,587 | $1.04 | 209 |
| MTEN | 17:05 | $1.05 | $1.05 | $1.01 | $1.02 | 36,447 | $1.03 | 262 |
| MTEN | 17:10 | $1.02 | $1.06 | $1.02 | $1.06 | 18,168 | $1.04 | 155 |
| MTEN | 17:15 | $1.06 | $1.29 | $1.06 | $1.20 | 969,962 | $1.21 | 5,649 |
| LCFY | 16:35 | $2.17 | $2.62 | $2.17 | $2.36 | 103,702 | $2.45 | 1,096 |
| LCFY | 16:40 | $2.38 | $2.59 | $2.17 | $2.22 | 161,504 | $2.38 | 1,318 |
| LCFY | 16:45 | $2.22 | $2.34 | $2.22 | $2.23 | 39,640 | $2.32 | 315 |
| LCFY | 16:50 | $2.26 | $2.33 | $2.23 | $2.31 | 24,367 | $2.29 | 116 |
| LCFY | 16:55 | $2.29 | $2.35 | $2.28 | $2.32 | 13,202 | $2.31 | 92 |
| LCFY | 17:00 | $2.34 | $2.50 | $2.33 | $2.45 | 55,564 | $2.45 | 507 |
| LCFY | 17:05 | $2.46 | $2.48 | $2.45 | $2.46 | 23,480 | $2.45 | 155 |
| LCFY | 17:10 | $2.44 | $2.50 | $2.40 | $2.49 | 23,553 | $2.45 | 173 |
| LCFY | 17:15 | $2.49 | $2.49 | $2.41 | $2.41 | 13,446 | $2.45 | 118 |
| WHLR | 16:40 | $0.93 | $0.96 | $0.93 | $0.95 | 23,713 | $0.95 | 94 |
| WHLR | 16:45 | $0.96 | $1.24 | $0.95 | $1.24 | 265,151 | $1.08 | 1,097 |
| WHLR | 16:50 | $1.23 | $1.24 | $1.05 | $1.06 | 280,898 | $1.11 | 1,385 |
| WHLR | 16:55 | $1.06 | $1.16 | $1.00 | $1.03 | 288,869 | $1.09 | 1,168 |
| WHLR | 17:00 | $1.03 | $1.03 | $0.96 | $0.98 | 84,294 | $1.00 | 298 |
| WHLR | 17:05 | $0.98 | $1.04 | $0.96 | $1.04 | 46,520 | $1.00 | 173 |
| WHLR | 17:10 | $1.04 | $1.08 | $1.00 | $1.03 | 48,261 | $1.05 | 220 |
| WHLR | 17:15 | $1.03 | $1.04 | $1.01 | $1.04 | 26,393 | $1.02 | 85 |
| BIYA | 16:50 | $1.84 | $1.95 | $1.82 | $1.85 | 242,874 | $1.89 | 1,615 |
| BIYA | 16:55 | $1.85 | $1.91 | $1.83 | $1.85 | 152,538 | $1.86 | 1,030 |
| BIYA | 17:00 | $1.85 | $1.98 | $1.84 | $1.92 | 248,222 | $1.92 | 1,676 |
| BIYA | 17:05 | $1.93 | $2.06 | $1.85 | $1.89 | 633,569 | $1.96 | 3,835 |
| BIYA | 17:10 | $1.89 | $1.99 | $1.87 | $1.96 | 155,877 | $1.92 | 1,126 |
| BIYA | 17:15 | $1.96 | $1.96 | $1.86 | $1.87 | 131,059 | $1.90 | 894 |
| SXTC | 16:50 | $2.38 | $2.38 | $2.17 | $2.17 | 407,217 | $2.26 | 2,955 |
| SXTC | 16:55 | $2.18 | $2.21 | $1.92 | $2.06 | 329,554 | $2.07 | 2,503 |
| SXTC | 17:00 | $2.06 | $2.10 | $2.00 | $2.05 | 138,698 | $2.05 | 1,061 |
| SXTC | 17:05 | $2.04 | $2.19 | $2.04 | $2.14 | 243,462 | $2.13 | 1,839 |
| SXTC | 17:10 | $2.14 | $2.19 | $2.07 | $2.17 | 110,255 | $2.13 | 969 |
| SXTC | 17:15 | $2.18 | $2.28 | $2.05 | $2.10 | 302,849 | $2.17 | 2,438 |
| MI | 16:50 | $1.52 | $1.66 | $1.51 | $1.57 | 288,180 | $1.60 | 1,382 |
| MI | 16:55 | $1.56 | $1.64 | $1.51 | $1.57 | 181,642 | $1.58 | 1,079 |
| MI | 17:00 | $1.57 | $1.58 | $1.52 | $1.53 | 90,521 | $1.55 | 519 |
| MI | 17:05 | $1.54 | $1.59 | $1.47 | $1.57 | 140,158 | $1.52 | 672 |
| MI | 17:10 | $1.55 | $1.57 | $1.49 | $1.49 | 74,036 | $1.53 | 415 |
| MI | 17:15 | $1.48 | $1.55 | $1.48 | $1.51 | 63,034 | $1.51 | 337 |
| VCIG | 16:50 | $1.47 | $1.53 | $1.38 | $1.40 | 1,286,525 | $1.44 | 6,047 |
| VCIG | 16:55 | $1.41 | $1.42 | $1.33 | $1.37 | 1,300,049 | $1.37 | 5,480 |
| VCIG | 17:00 | $1.37 | $1.46 | $1.33 | $1.37 | 859,175 | $1.39 | 4,324 |
| VCIG | 17:05 | $1.38 | $1.38 | $1.22 | $1.23 | 1,096,786 | $1.29 | 5,333 |
| VCIG | 17:10 | $1.23 | $1.29 | $1.20 | $1.26 | 591,663 | $1.28 | 2,872 |
| VCIG | 17:15 | $1.26 | $1.32 | $1.24 | $1.25 | 469,311 | $1.28 | 1,958 |

NCPL printed 240–1,760 shares and 1–6 trades per bar from 16:50 to 17:15 ET at $1.19–$1.20.

**Yahoo timeline (shape only, not volume or exact levels):**

| Ticker | 17:05 | 17:10 | 17:15 | 17:20 | 17:25 | 17:30 |
|--------|-------|-------|-------|-------|-------|-------|
| MTEN | $1.03 | $1.06 | $1.21 | $1.27 | $1.19 | $1.20 |
| LCFY | $2.47 | $2.50 | $2.41 | $2.40 | $2.40 | $2.44 |
| WHLR | $1.04 | $1.03 | $1.04 | $1.07 | $1.05 | $1.08 |
| BIYA | $1.90 | $1.96 | $1.87 | $1.92 | $2.17 | $2.22 |
| SXTC | $2.14 | $2.19 | $2.10 | $1.98 | $1.97 | $1.97 |
| MI | $1.57 | $1.49 | $1.51 | $1.51 | $1.51 | $1.52 |
| VCIG | $1.23 | $1.26 | $1.25 | $1.26 | $1.16 | $1.17 |

**MTEN — first >10% AH appearance; no entry possible until 00:00 (2-AH-scan gate). Lead for 00:00.** The scanner's $1.06 matches the 17:10 bar and lags the tape. SIP shows a first leg at 16:30–16:45 ET (152,894 → 170,255 → 478,591 shares, high $1.17), a fade to $0.96–$1.06 on 13K–36K shares per bar, then a second ignition in the **17:15 bar: 969,962 shares / 5,649 trades, high $1.29, close $1.20, VWAP $1.21**. That bar is 28.9x local volume. The AH high of $1.29 (+34.4% AH, +33.8% Total from the $0.964 prior close) sits well outside the opening window. Yahoo shows $1.27 at 17:20 and $1.20–$1.21 at 17:30–17:31, about 7% below the high. The delayed SIP book at 17:19 ET was $1.19 x3,400 / $1.20 x300. The IEX quote is frozen at 16:46:21 ET ($1.00/$1.02) and does not reflect the current price. Day -0.4% passes, Total% about +24.5% at $1.20 is far under the +150% ceiling, and float is 6.1M.

- **Catalyst Grade B — completed acquisition (acquirer side), dated and timed.** [6-K accepted by EDGAR 2026-10-06 16:30:51 ET](https://www.sec.gov/Archives/edgar/data/1948099/000121390026107243/ea0307735-6k_mingteng.htm): on October 6, 2026, Mingteng signed and completed a Share Transfer Agreement to buy 100% of HK Phoenix Gateway Alliance Limited from Mr. ZHENG Delin, which indirectly brings in Shanghai Shangyun Yingfei Technology Co. and Shanghai Minwen Industrial Co. Consideration is **USD 15,000,000, already paid**. TipRanks summarized it about 16:55 ET. Grade B, not A: the filing discloses no target business, revenue, or rationale, there is no press release, and the $15M price is about twice MTEN's $7.3M market cap. MTEN is the buyer, so the merger-arb exclusion does not apply. The 16:30 bar ignition matches the filing time. Two websearch calls plus the EDGAR filing; a TipRanks extract returned HTTP 403.
- **First day of unusual activity:** SIP daily volume was 78K–190K shares from September 22 to October 5 with price pinned at $0.94–$1.06. Today's move is fresh. Not a MULTI-SESSION-RUNNER; no `WINNERS_TRACKING.md` entry.
- **CONFIRM-3 NO** scores the 16:30 ignition, which failed its third bar; the tool does not re-score the 17:15 leg (same limitation as SXTC).

**LCFY — first >10% AH appearance; skip at this snapshot (thin drift).** Volume ignited in the 16:35 bar (103,702 shares / 1,096 trades) to the AH high of **$2.62** (+27.8% AH, +12.0% Total from the $2.34 prior close), then fell to 13K–56K shares and 92–507 trades per bar. Price has climbed back to $2.41–$2.50 (Yahoo $2.44 at 17:30, 7% below the high). Rising price on tens of thousands of shares per bar is a thin drift under the MODD rule. CONFIRM-3 reads NO (16:35 ignition failed its third bar). Day -12.4% passes. The IEX book was not checked; thin SIP volume keeps LCFY out of the book diagnostic.

- **Catalyst Grade B — fresh acquisition agreement (acquirer side).** [GlobeNewswire, October 6, 2026: "Locafy to Acquire Map Labs' Assets, Significantly Expanding Revenue and U.S. Customer Base"](https://www.globenewswire.com/news-release/2026/10/06/3375402/0/en/locafy-to-acquire-map-labs-assets-significantly-expanding-revenue-and-u-s-customer-base.html): definitive agreement to buy Map Labs' assets and customer base for up to US$3.0M cash, closing on or before December 31, 2026. Search results listed it about 10 hours before 17:30 ET, so it came out near 07:30 ET; the exact clock time is unverified. The regular session sold the news: SIP shows a $1.33–$2.40 range on 3.34M shares against a few thousand shares a day in late September, closing -12.4%. Two searches used.
- **First day of unusual activity:** yes (daily volume 940–40,842 shares from September 22 to October 5).

**WHLR — first >10% AH appearance; skip (Day -16.5%, dead-cat bounce).** Volume ignited in the 16:45 bar (265,151 shares / 1,097 trades) to **$1.24** (+36.3% AH from the $0.91 close), then faded to $0.96–$1.08 on 26K–84K shares per bar. Yahoo shows $1.08 at 17:30, 13% below the high and about 1% below the $1.09 prior close. It is above today's $0.91 close, but DEAD-CAT-OVERRIDE WATCH requires AH% rising across two AH scans. A second, higher reading at 00:00 would start that watch. CONFIRM-3 reads NO.

- **Catalyst Grade None — no catalyst found.** Two searches found only October 6 premarket stories on a Form 4 ownership change and the stock sliding, plus the Q2 2026 results. A Form 4 is not an upside catalyst.
- **Multi-session context:** WHLR is the September 22 `WINNERS_TRACKING.md` entry (1-for-9 reverse split; $5.10 PM peak). SIP daily bars show a $8.71 high on September 23 (92.8M shares), then a slide to today's $0.84 low on 14.8M shares. Not a first day of unusual activity.

**BIYA — `already entered` (52 @ $1.91); tracking only.** The 17:05 SIP bar pushed to $2.06 on 633,569 shares / 3,835 trades, and Yahoo shows a new push to **$2.22 at 17:30**, above the $2.07 SIP high (SIP has not covered it yet). `broker.js positions` marks it at $2.14, **+$11.96 (+12.0%)**. CONFIRM-3 stays YES. The delayed SIP book at 17:19 ET was $1.87/$1.88.

**SXTC — sixth qualifying AH scan; skip live entry (Day -39.9%); DEAD-CAT-OVERRIDE WATCH continues.** Scanner AH change rose again (+70.4% → +74.4%). SIP bars from 16:50 to 17:15 held $1.92–$2.38 on 110K–407K shares and 969–2,955 trades each. Yahoo shows **$1.97 at 17:30**: +57.6% above the $1.25 regular close, 5% below the $2.08 prior close, and 24% below the $2.58 AH high (16:30 bar). The 22:25 hypothetical ($1.57 at 16:25 ET) stands.

**MI — third >10% AH appearance; skip (dead-cat bounce, Grade D).** Scanner AH change declined across three scans (+25.2% → +24.0% → +20.6%). SIP volume shrank from 288,180 to 63,034 shares per bar; Yahoo shows $1.52 at 17:30, 17% below the $1.84 high. The same-day registered direct offering keeps it Grade D.

**NCPL — fourth >10% AH appearance; skip stands (thin drift, Day -17.4%).**

**VCIG — absent from this scan; SPIKE→FADE confirmed.** SIP bars kept selling on heavy volume (469K–1.30M shares per bar) to a $1.20 low; Yahoo shows **$1.17 at 17:30**, 17% below today's $1.41 close and 44% below the $2.10 high. The 22:20 FIRST-BAR-SPIKE WATCH hypothetical ($1.69 at 16:20 ET) stays on record.

**Below threshold:** OLOX (+8.0% AH, day 2 after its October 5 win), QTEX (+5.7%), ALDX (+6.9%), and DCX (+7.7%) are tracked only.

**Instrumentation (verbatim; log-only):**

```text
BIYA 2026-10-06  SPIKE  16:08ET  +21%  $1.65  372 trades / 58k sh  (first co-spike bar) (as-of 17:30ET)
BIYA 2026-10-06  CONFIRM-3  YES ignition 16:05ET 260.8x; confirmed 16:15ET $1.81 as-of 17:30ET
SXTC 2026-10-06  SPIKE  16:03ET  +32%  $1.65  135 trades / 30k sh  (first co-spike bar) (as-of 17:30ET)
SXTC 2026-10-06  CONFIRM-3  NO ignition 16:05ET failed third-bar hold/volume as-of 17:30ET
MI 2026-10-06  SPIKE  16:18ET  +30%  $1.60  2066 trades / 421k sh  (first co-spike bar) (as-of 17:30ET)
MI 2026-10-06  CONFIRM-3  NO ignition 16:15ET failed third-bar hold/volume as-of 17:30ET
NCPL 2026-10-06  NO-SPIKE  peak +17% @16:03ET  (no bar cleared +15% on a volume co-spike) (as-of 17:30ET)
NCPL 2026-10-06  CONFIRM-3  NO no local-volume new-high ignition as-of 17:30ET
MTEN 2026-10-06  SPIKE  16:41ET  +22%  $1.17  637 trades / 143k sh  (first co-spike bar) (as-of 17:30ET)
MTEN 2026-10-06  CONFIRM-3  NO ignition 16:30ET failed third-bar hold/volume as-of 17:30ET
LCFY 2026-10-06  NO-SPIKE  peak +28% @16:38ET  (no bar cleared +15% on a volume co-spike) (as-of 17:30ET)
LCFY 2026-10-06  CONFIRM-3  NO ignition 16:35ET failed third-bar hold/volume as-of 17:30ET
WHLR 2026-10-06  SPIKE  16:46ET  +16%  $1.06  110 trades / 34k sh  (first co-spike bar) (as-of 17:30ET)
WHLR 2026-10-06  CONFIRM-3  NO ignition 16:45ET failed third-bar hold/volume as-of 17:30ET
```

**Shared SIP volume context (`sip-ah-volume-v1`, log-only):** The prior trading date is 2026-10-05, a normal Monday session. Inputs were fetched with `broker.js bars SYM --tf 5Min --start 2026-10-05T20:00:00Z --limit 1000 --feed sip --json` (one page each, no next-page token) and archived as `log/2026-10-06/SYM-2330-volume-sip.json`, with computed rows in `SYM-2330-volume-metric.json`. MI and WHLR have complete prior-session coverage (48/48). The others stay incomplete (BIYA 18/48, SXTC 10/48, NCPL 25/48, MTEN 5/48, LCFY 1/48), so their prior-peak ratios remain unknown. MTEN and LCFY have no bars between their first bar and their ignition, so their first rows lack a baseline. MTEN's 17:15 bar reads 28.88x local. WHLR's 16:45 ignition bar was 21.2x local but only 0.21x its October 5 AH peak. The SXTC share-consolidation headline, BIYA's July 1-for-10 reverse split, and WHLR's September 21 1-for-9 reverse split remain unreviewed against this window.

```text
# BIYA shared SIP volume; prior 2026-10-05 18/48 slots; log-only
# reconstructed as-of 2026-10-06T21:30:14+00:00; source fetched 2026-10-06T21:34:02.548049Z
BIYA 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=1095 local=unknown prior-peak=unknown status=warmup
BIYA 2026-10-06  VOLUME-CONTEXT 16:05ET start=2026-10-06T20:05:00+00:00 shares=285556 local=unknown prior-peak=unknown status=warmup
BIYA 2026-10-06  VOLUME-CONTEXT 16:10ET start=2026-10-06T20:10:00+00:00 shares=1072394 local=unknown prior-peak=unknown status=warmup
BIYA 2026-10-06  VOLUME-CONTEXT 16:15ET start=2026-10-06T20:15:00+00:00 shares=1596650 local=5.5914x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 16:20ET start=2026-10-06T20:20:00+00:00 shares=550815 local=0.5136x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 16:25ET start=2026-10-06T20:25:00+00:00 shares=307657 local=0.2869x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 16:30ET start=2026-10-06T20:30:00+00:00 shares=452655 local=0.8218x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 16:35ET start=2026-10-06T20:35:00+00:00 shares=413407 local=0.9133x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 16:40ET start=2026-10-06T20:40:00+00:00 shares=802489 local=1.9412x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 16:45ET start=2026-10-06T20:45:00+00:00 shares=347463 local=0.7676x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 16:50ET start=2026-10-06T20:50:00+00:00 shares=242874 local=0.5875x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 16:55ET start=2026-10-06T20:55:00+00:00 shares=152538 local=0.4390x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 17:00ET start=2026-10-06T21:00:00+00:00 shares=248222 local=1.0220x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 17:05ET start=2026-10-06T21:05:00+00:00 shares=633569 local=2.6086x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 17:10ET start=2026-10-06T21:10:00+00:00 shares=155877 local=0.6280x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 17:15ET start=2026-10-06T21:15:00+00:00 shares=131059 local=0.5280x prior-peak=unknown status=ok
# SXTC shared SIP volume; prior 2026-10-05 10/48 slots; log-only
# reconstructed as-of 2026-10-06T21:30:14+00:00; source fetched 2026-10-06T21:34:03.158922Z
SXTC 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=75597 local=unknown prior-peak=unknown status=warmup
SXTC 2026-10-06  VOLUME-CONTEXT 16:05ET start=2026-10-06T20:05:00+00:00 shares=683755 local=unknown prior-peak=unknown status=warmup
SXTC 2026-10-06  VOLUME-CONTEXT 16:10ET start=2026-10-06T20:10:00+00:00 shares=212492 local=unknown prior-peak=unknown status=warmup
SXTC 2026-10-06  VOLUME-CONTEXT 16:15ET start=2026-10-06T20:15:00+00:00 shares=103774 local=0.4884x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 16:20ET start=2026-10-06T20:20:00+00:00 shares=295399 local=1.3902x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 16:25ET start=2026-10-06T20:25:00+00:00 shares=394574 local=1.8569x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 16:30ET start=2026-10-06T20:30:00+00:00 shares=1344735 local=4.5523x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 16:35ET start=2026-10-06T20:35:00+00:00 shares=563974 local=1.4293x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 16:40ET start=2026-10-06T20:40:00+00:00 shares=508099 local=0.9009x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 16:45ET start=2026-10-06T20:45:00+00:00 shares=865653 local=1.5349x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 16:50ET start=2026-10-06T20:50:00+00:00 shares=407217 local=0.7220x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 16:55ET start=2026-10-06T20:55:00+00:00 shares=329554 local=0.6486x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 17:00ET start=2026-10-06T21:00:00+00:00 shares=138698 local=0.3406x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 17:05ET start=2026-10-06T21:05:00+00:00 shares=243462 local=0.7388x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 17:10ET start=2026-10-06T21:10:00+00:00 shares=110255 local=0.4529x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 17:15ET start=2026-10-06T21:15:00+00:00 shares=302849 local=2.1835x prior-peak=unknown status=ok
# MI shared SIP volume; prior 2026-10-05 48/48 slots; log-only
# reconstructed as-of 2026-10-06T21:30:14+00:00; source fetched 2026-10-06T21:34:03.756052Z
MI 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=220361 local=unknown prior-peak=0.2093x status=warmup
MI 2026-10-06  VOLUME-CONTEXT 16:05ET start=2026-10-06T20:05:00+00:00 shares=137355 local=unknown prior-peak=0.1304x status=warmup
MI 2026-10-06  VOLUME-CONTEXT 16:10ET start=2026-10-06T20:10:00+00:00 shares=159195 local=unknown prior-peak=0.1512x status=warmup
MI 2026-10-06  VOLUME-CONTEXT 16:15ET start=2026-10-06T20:15:00+00:00 shares=1263614 local=7.9375x prior-peak=1.2000x status=ok
MI 2026-10-06  VOLUME-CONTEXT 16:20ET start=2026-10-06T20:20:00+00:00 shares=2036291 local=12.7912x prior-peak=1.9338x status=ok
MI 2026-10-06  VOLUME-CONTEXT 16:25ET start=2026-10-06T20:25:00+00:00 shares=868347 local=0.6872x prior-peak=0.8246x status=ok
MI 2026-10-06  VOLUME-CONTEXT 16:30ET start=2026-10-06T20:30:00+00:00 shares=427999 local=0.3387x prior-peak=0.4064x status=ok
MI 2026-10-06  VOLUME-CONTEXT 16:35ET start=2026-10-06T20:35:00+00:00 shares=400416 local=0.4611x prior-peak=0.3803x status=ok
MI 2026-10-06  VOLUME-CONTEXT 16:40ET start=2026-10-06T20:40:00+00:00 shares=214703 local=0.5016x prior-peak=0.2039x status=ok
MI 2026-10-06  VOLUME-CONTEXT 16:45ET start=2026-10-06T20:45:00+00:00 shares=461613 local=1.1528x prior-peak=0.4384x status=ok
MI 2026-10-06  VOLUME-CONTEXT 16:50ET start=2026-10-06T20:50:00+00:00 shares=288180 local=0.7197x prior-peak=0.2737x status=ok
MI 2026-10-06  VOLUME-CONTEXT 16:55ET start=2026-10-06T20:55:00+00:00 shares=181642 local=0.6303x prior-peak=0.1725x status=ok
MI 2026-10-06  VOLUME-CONTEXT 17:00ET start=2026-10-06T21:00:00+00:00 shares=90521 local=0.3141x prior-peak=0.0860x status=ok
MI 2026-10-06  VOLUME-CONTEXT 17:05ET start=2026-10-06T21:05:00+00:00 shares=140158 local=0.7716x prior-peak=0.1331x status=ok
MI 2026-10-06  VOLUME-CONTEXT 17:10ET start=2026-10-06T21:10:00+00:00 shares=74036 local=0.5282x prior-peak=0.0703x status=ok
MI 2026-10-06  VOLUME-CONTEXT 17:15ET start=2026-10-06T21:15:00+00:00 shares=63034 local=0.6963x prior-peak=0.0599x status=ok
# NCPL shared SIP volume; prior 2026-10-05 25/48 slots; log-only
# reconstructed as-of 2026-10-06T21:30:14+00:00; source fetched 2026-10-06T21:34:04.423818Z
NCPL 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=71987 local=unknown prior-peak=unknown status=warmup
NCPL 2026-10-06  VOLUME-CONTEXT 16:05ET start=2026-10-06T20:05:00+00:00 shares=71440 local=unknown prior-peak=unknown status=warmup
NCPL 2026-10-06  VOLUME-CONTEXT 16:10ET start=2026-10-06T20:10:00+00:00 shares=7284 local=unknown prior-peak=unknown status=warmup
NCPL 2026-10-06  VOLUME-CONTEXT 16:15ET start=2026-10-06T20:15:00+00:00 shares=4790 local=0.0670x prior-peak=unknown status=ok
NCPL 2026-10-06  VOLUME-CONTEXT 16:20ET start=2026-10-06T20:20:00+00:00 shares=1020 local=0.1400x prior-peak=unknown status=ok
NCPL 2026-10-06  VOLUME-CONTEXT 16:25ET start=2026-10-06T20:25:00+00:00 shares=7199 local=1.5029x prior-peak=unknown status=ok
NCPL 2026-10-06  VOLUME-CONTEXT 16:30ET start=2026-10-06T20:30:00+00:00 shares=234 local=0.0489x prior-peak=unknown status=ok
NCPL 2026-10-06  VOLUME-CONTEXT 16:35ET start=2026-10-06T20:35:00+00:00 shares=1540 local=1.5098x prior-peak=unknown status=ok
NCPL 2026-10-06  VOLUME-CONTEXT 16:40ET start=2026-10-06T20:40:00+00:00 shares=1404 local=0.9117x prior-peak=unknown status=ok
NCPL 2026-10-06  VOLUME-CONTEXT 16:45ET start=2026-10-06T20:45:00+00:00 shares=175 local=0.1246x prior-peak=unknown status=ok
NCPL 2026-10-06  VOLUME-CONTEXT 16:50ET start=2026-10-06T20:50:00+00:00 shares=240 local=0.1709x prior-peak=unknown status=ok
NCPL 2026-10-06  VOLUME-CONTEXT 17:00ET start=2026-10-06T21:00:00+00:00 shares=1760 local=unknown prior-peak=unknown status=missing-baseline
NCPL 2026-10-06  VOLUME-CONTEXT 17:05ET start=2026-10-06T21:05:00+00:00 shares=340 local=unknown prior-peak=unknown status=missing-baseline
NCPL 2026-10-06  VOLUME-CONTEXT 17:15ET start=2026-10-06T21:15:00+00:00 shares=1000 local=unknown prior-peak=unknown status=missing-baseline
# MTEN shared SIP volume; prior 2026-10-05 5/48 slots; log-only
# reconstructed as-of 2026-10-06T21:30:14+00:00; source fetched 2026-10-06T21:34:05.030493Z
MTEN 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=652 local=unknown prior-peak=unknown status=warmup
MTEN 2026-10-06  VOLUME-CONTEXT 16:30ET start=2026-10-06T20:30:00+00:00 shares=152894 local=unknown prior-peak=unknown status=missing-baseline
MTEN 2026-10-06  VOLUME-CONTEXT 16:35ET start=2026-10-06T20:35:00+00:00 shares=170255 local=unknown prior-peak=unknown status=missing-baseline
MTEN 2026-10-06  VOLUME-CONTEXT 16:40ET start=2026-10-06T20:40:00+00:00 shares=478591 local=unknown prior-peak=unknown status=missing-baseline
MTEN 2026-10-06  VOLUME-CONTEXT 16:45ET start=2026-10-06T20:45:00+00:00 shares=166035 local=0.9752x prior-peak=unknown status=ok
MTEN 2026-10-06  VOLUME-CONTEXT 16:50ET start=2026-10-06T20:50:00+00:00 shares=25301 local=0.1486x prior-peak=unknown status=ok
MTEN 2026-10-06  VOLUME-CONTEXT 16:55ET start=2026-10-06T20:55:00+00:00 shares=12949 local=0.0780x prior-peak=unknown status=ok
MTEN 2026-10-06  VOLUME-CONTEXT 17:00ET start=2026-10-06T21:00:00+00:00 shares=33587 local=1.3275x prior-peak=unknown status=ok
MTEN 2026-10-06  VOLUME-CONTEXT 17:05ET start=2026-10-06T21:05:00+00:00 shares=36447 local=1.4405x prior-peak=unknown status=ok
MTEN 2026-10-06  VOLUME-CONTEXT 17:10ET start=2026-10-06T21:10:00+00:00 shares=18168 local=0.5409x prior-peak=unknown status=ok
MTEN 2026-10-06  VOLUME-CONTEXT 17:15ET start=2026-10-06T21:15:00+00:00 shares=969962 local=28.8791x prior-peak=unknown status=ok
# LCFY shared SIP volume; prior 2026-10-05 1/48 slots; log-only
# reconstructed as-of 2026-10-06T21:30:14+00:00; source fetched 2026-10-06T21:34:05.632334Z
LCFY 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=5907 local=unknown prior-peak=unknown status=warmup
LCFY 2026-10-06  VOLUME-CONTEXT 16:15ET start=2026-10-06T20:15:00+00:00 shares=411 local=unknown prior-peak=unknown status=missing-baseline
LCFY 2026-10-06  VOLUME-CONTEXT 16:20ET start=2026-10-06T20:20:00+00:00 shares=3627 local=unknown prior-peak=unknown status=missing-baseline
LCFY 2026-10-06  VOLUME-CONTEXT 16:25ET start=2026-10-06T20:25:00+00:00 shares=677 local=unknown prior-peak=unknown status=missing-baseline
LCFY 2026-10-06  VOLUME-CONTEXT 16:30ET start=2026-10-06T20:30:00+00:00 shares=1468 local=2.1684x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 16:35ET start=2026-10-06T20:35:00+00:00 shares=103702 local=70.6417x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 16:40ET start=2026-10-06T20:40:00+00:00 shares=161504 local=110.0163x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 16:45ET start=2026-10-06T20:45:00+00:00 shares=39640 local=0.3822x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 16:50ET start=2026-10-06T20:50:00+00:00 shares=24367 local=0.2350x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 16:55ET start=2026-10-06T20:55:00+00:00 shares=13202 local=0.3330x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 17:00ET start=2026-10-06T21:00:00+00:00 shares=55564 local=2.2803x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 17:05ET start=2026-10-06T21:05:00+00:00 shares=23480 local=0.9636x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 17:10ET start=2026-10-06T21:10:00+00:00 shares=23553 local=1.0031x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 17:15ET start=2026-10-06T21:15:00+00:00 shares=13446 local=0.5709x prior-peak=unknown status=ok
# WHLR shared SIP volume; prior 2026-10-05 48/48 slots; log-only
# reconstructed as-of 2026-10-06T21:30:14+00:00; source fetched 2026-10-06T21:34:06.238444Z
WHLR 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=79913 local=unknown prior-peak=0.0640x status=warmup
WHLR 2026-10-06  VOLUME-CONTEXT 16:05ET start=2026-10-06T20:05:00+00:00 shares=42488 local=unknown prior-peak=0.0340x status=warmup
WHLR 2026-10-06  VOLUME-CONTEXT 16:10ET start=2026-10-06T20:10:00+00:00 shares=11795 local=unknown prior-peak=0.0094x status=warmup
WHLR 2026-10-06  VOLUME-CONTEXT 16:15ET start=2026-10-06T20:15:00+00:00 shares=8067 local=0.1899x prior-peak=0.0065x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 16:20ET start=2026-10-06T20:20:00+00:00 shares=10432 local=0.8844x prior-peak=0.0084x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 16:25ET start=2026-10-06T20:25:00+00:00 shares=12272 local=1.1764x prior-peak=0.0098x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 16:30ET start=2026-10-06T20:30:00+00:00 shares=8867 local=0.8500x prior-peak=0.0071x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 16:35ET start=2026-10-06T20:35:00+00:00 shares=12529 local=1.2010x prior-peak=0.0100x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 16:40ET start=2026-10-06T20:40:00+00:00 shares=23713 local=1.9323x prior-peak=0.0190x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 16:45ET start=2026-10-06T20:45:00+00:00 shares=265151 local=21.1630x prior-peak=0.2124x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 16:50ET start=2026-10-06T20:50:00+00:00 shares=280898 local=11.8457x prior-peak=0.2250x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 16:55ET start=2026-10-06T20:55:00+00:00 shares=288869 local=1.0895x prior-peak=0.2314x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 17:00ET start=2026-10-06T21:00:00+00:00 shares=84294 local=0.3001x prior-peak=0.0675x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 17:05ET start=2026-10-06T21:05:00+00:00 shares=46520 local=0.1656x prior-peak=0.0373x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 17:10ET start=2026-10-06T21:10:00+00:00 shares=48261 local=0.5725x prior-peak=0.0387x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 17:15ET start=2026-10-06T21:15:00+00:00 shares=26393 local=0.5469x prior-peak=0.0211x status=ok
```

**Book diagnostic (verbatim; log-only)** for the five tradable >10% names with accumulating SIP volume (LCFY and NCPL are thin and excluded). All IEX quotes are frozen at or before 17:00 ET.

```text
BIYA BOOK iex bid $1.88 x100 / ask $1.92 x100 @ 2026-10-06 16:54:16 ET age 40m12s two-sided spread 2.08% of ask
BIYA BOOK sip-15m bid $1.87 x200 / ask $1.88 x1400 @ 2026-10-06 17:19:28 ET age 15m00s two-sided spread 0.53% of ask
BIYA BOOK refresh +15s iex unchanged @ 2026-10-06 16:54:16 ET
BIYA BOOK verdict: IEX STALE 40m12s; SIP-15m TWO-SIDED (observed 2026-10-06 17:34:28 ET; log-only)
SXTC BOOK iex bid $2.19 x100 / ask $2.24 x100 @ 2026-10-06 16:48:07 ET age 46m20s two-sided spread 2.23% of ask
SXTC BOOK sip-15m bid $2.05 x400 / ask $2.06 x1100 @ 2026-10-06 17:19:27 ET age 15m01s two-sided spread 0.49% of ask
SXTC BOOK refresh +15s iex unchanged @ 2026-10-06 16:48:07 ET
SXTC BOOK verdict: IEX STALE 46m20s; SIP-15m TWO-SIDED (observed 2026-10-06 17:34:28 ET; log-only)
MI BOOK iex bid $1.56 x100 / ask $1.59 x100 @ 2026-10-06 16:59:55 ET age 34m32s two-sided spread 1.89% of ask
MI BOOK sip-15m bid $1.50 x100 / ask $1.51 x200 @ 2026-10-06 17:19:25 ET age 15m03s two-sided spread 0.66% of ask
MI BOOK refresh +15s iex unchanged @ 2026-10-06 16:59:55 ET
MI BOOK verdict: IEX STALE 34m32s; SIP-15m TWO-SIDED (observed 2026-10-06 17:34:28 ET; log-only)
MTEN BOOK iex bid $1.00 x100 / ask $1.02 x100 @ 2026-10-06 16:46:21 ET age 48m07s two-sided spread 1.96% of ask
MTEN BOOK sip-15m bid $1.19 x3400 / ask $1.20 x300 @ 2026-10-06 17:19:28 ET age 15m00s two-sided spread 0.83% of ask
MTEN BOOK refresh +15s iex unchanged @ 2026-10-06 16:46:21 ET
MTEN BOOK verdict: IEX STALE 48m07s; SIP-15m TWO-SIDED (observed 2026-10-06 17:34:28 ET; log-only)
WHLR BOOK iex bid $1.03 x100 / ask $1.07 x100 @ 2026-10-06 16:57:58 ET age 36m30s two-sided spread 3.74% of ask
WHLR BOOK sip-15m bid $1.03 x100 / ask $1.04 x100 @ 2026-10-06 17:19:21 ET age 15m07s two-sided spread 0.96% of ask
WHLR BOOK refresh +15s iex unchanged @ 2026-10-06 16:57:58 ET
WHLR BOOK verdict: IEX STALE 36m30s; SIP-15m TWO-SIDED (observed 2026-10-06 17:34:28 ET; log-only)
```

**00:00 checklist:** MTEN is the lead. Enter if it shows a second >10% AH reading, the 17:20+ SIP bars keep hundreds of thousands of shares and thousands of trades, and the price holds within ~20% of its $1.29 high (about $1.03 or higher). Its IEX quote is frozen at $1.00/$1.02 from 16:46 ET, so price the limit from the newest SIP bar and Yahoo, a few cents above the last trade. LCFY needs per-bar volume back in the hundreds of thousands to count as a BUILD. WHLR starts a DEAD-CAT-OVERRIDE WATCH if its AH% rises at 00:00 while it stays above the $0.91 close. SXTC stays a Day% skip on DEAD-CAT-OVERRIDE WATCH. MI and NCPL stay skips. Keep all 28 names from the 21:30 watchlist in the pipeline for the 00:30 final-scan cross-check. KAPA's dead-cat guard and OLOX's day-2 tag still apply. EVOL, MHUAF, VNPKF, WTLLF, NWINF, and KHDHF remain untradable (carried).

**Daily email:** Report MTEN's late ignition (970K shares in the 17:15 bar to $1.29) on a same-day 6-K for a $15M cash acquisition, the BIYA position at +12.0% with Yahoo showing a new $2.22 high, VCIG's continued fade to $1.17 (44% off its high), and LCFY's acquisition PR that sold off in the regular session before a thin AH recovery. No item from this scan requires Juan's input.

## Scan 00:00 CEST (6:00 PM ET)

**Decision:** Entered **MTEN**, 70 shares filled at **$1.39** on Alpaca (order `271309e2`, 18:01:20 ET). It cleared its second >10% AH scan (+10.6% → +51.2%) on a volume-backed BUILD: every SIP bar from 17:15 to 17:45 ET carried 711K–1.48M shares and 3,894–7,914 trades, with a new high of $1.59 in the 17:40 bar. Catalyst Grade B (same-day 6-K for a completed $15M cash acquisition). LCFY (second appearance) is a thin-drift skip. WHLR (second appearance) stays a Day% skip; its AH% rise is a thin drift, so it does not start a DEAD-CAT-OVERRIDE WATCH. SXTC, MI, and NCPL skips stand. BIYA is `already entered` at +14.1%. AH appearance counts: SXTC **7**, BIYA **6**, NCPL **5**, VCIG **5** (absent), MI **4**, MTEN **2**, LCFY **2**, WHLR **2**, LHSW **1**.

`python3 scripts/scan.py --all` ran at 18:00:20 ET (00:00:20 CEST on October 7 / 22:00:20 UTC) in the AFTERHOURS session and returned 15 hits. The US trading date is 2026-10-06. Repository sync completed before the scan.

```text
  Supplementary AH-change-only (>15%, not in volume pass): none
  AH >10% at this snapshot (unrounded): BIYA, LCFY, MI, MTEN, NCPL, SXTC, WHLR
```

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| BIYA | [TV](https://www.tradingview.com/chart/?symbol=BIYA) | $1.36 | -2.5% | +47.1% | $2.01 | +43.4% | 8.1M | 2.5M | 3.3x | 2.7M | Personnel Services |
| MI | [TV](https://www.tradingview.com/chart/?symbol=MI) | $1.23 | -82.4% | +12.2% | $1.38 | -80.3% | 6.8M | 18.7M | 0.4x | 542K | Internet Software/Services |
| MTEN | [TV](https://www.tradingview.com/chart/?symbol=MTEN) | $0.96 | -0.4% | +51.2% | $1.45 | +50.7% | 6.5M | 880K | 7.3x | 6.1M | Industrial Machinery |
| SXTC | [TV](https://www.tradingview.com/chart/?symbol=SXTC) | $1.25 | -39.9% | +52.8% | $1.91 | -8.2% | 6.0M | 1.2M | 5.0x | 1.0M | Pharmaceuticals: Major |
| XHLD | [TV](https://www.tradingview.com/chart/?symbol=XHLD) | $0.62 | +51.6% | +9.9% | $0.68 | +66.5% | 3.3M | 19.7M | 0.2x | 10.5M | Miscellaneous Commercial Services |
| OLOX | [TV](https://www.tradingview.com/chart/?symbol=OLOX) | $1.25 | +42.0% | +7.2% | $1.34 | +52.3% | 1.9M | 15.2M | 0.1x | 1.3M | Building Products |
| WHLR | [TV](https://www.tradingview.com/chart/?symbol=WHLR) | $0.91 | -16.5% | +14.3% | $1.04 | -4.6% | 1.4M | 13.3M | 0.1x | 568K | Real Estate Investment Trusts |
| LCFY | [TV](https://www.tradingview.com/chart/?symbol=LCFY) | $2.05 | -12.4% | +18.6% | $2.43 | +3.9% | 434K | 345K | 1.3x | 1.4M | Packaged Software |
| JAGX | [TV](https://www.tradingview.com/chart/?symbol=JAGX) | $5.62 | +18.8% | +6.0% | $5.96 | +26.0% | 233K | 9.7M | 0.0x | 1.7M | Pharmaceuticals: Major |
| STEX | [TV](https://www.tradingview.com/chart/?symbol=STEX) | $0.52 | -12.7% | +6.0% | $0.55 | -7.5% | 191K | 1.1M | 0.2x | 105.3M | Investment Banks/Brokers |
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $1.09 | -17.4% | +14.7% | $1.25 | -5.3% | 185K | 14.3M | 0.0x | 4.4M | Miscellaneous Commercial Services |
| DCX | [TV](https://www.tradingview.com/chart/?symbol=DCX) | $3.11 | -8.0% | +6.8% | $3.32 | -1.8% | 144K | 550K | 0.3x | 259K | Motor Vehicles |
| ALDX | [TV](https://www.tradingview.com/chart/?symbol=ALDX) | $0.92 | -0.8% | +6.9% | $0.98 | +6.0% | 87K | 2.9M | 0.0x | 58.1M | Biotechnology |
| FEAM | [TV](https://www.tradingview.com/chart/?symbol=FEAM) | $3.76 | -4.1% | +8.5% | $4.08 | +4.1% | 73K | 861K | 0.1x | 20.9M | Chemicals: Specialty |
| NCT | [TV](https://www.tradingview.com/chart/?symbol=NCT) | $1.50 | -13.3% | +6.0% | $1.59 | -8.1% | 70K | 702K | 0.1x | 921K | Marine Shipping |

### Evaluation notes

**Tradability:** MTEN was re-verified `tradable=true` (Nasdaq, active) immediately before the order. XHLD returned `tradable=true` (Nasdaq, active). The other >10% names were verified earlier tonight.

**New SIP bars** (`broker.js bars SYM --tf 5Min --start 2026-10-06T21:15:00Z`, feed=sip). The newest bar starts 17:45 ET, 15 minutes behind the scan, which matches the free-tier delay. The 17:15 bars are in the 23:30 table.

| Ticker | Bar ET | Open | High | Low | Close | Shares | VWAP | Trades |
|--------|--------|------|------|-----|-------|--------|------|--------|
| MTEN | 17:20 | $1.20 | $1.32 | $1.16 | $1.27 | 1,188,203 | $1.26 | 6,665 |
| MTEN | 17:25 | $1.27 | $1.28 | $1.16 | $1.19 | 711,200 | $1.22 | 3,894 |
| MTEN | 17:30 | $1.19 | $1.37 | $1.17 | $1.35 | 952,125 | $1.31 | 4,475 |
| MTEN | 17:35 | $1.35 | $1.45 | $1.31 | $1.41 | 1,017,234 | $1.39 | 5,173 |
| MTEN | 17:40 | $1.43 | $1.59 | $1.41 | $1.45 | 1,476,192 | $1.48 | 7,914 |
| MTEN | 17:45 | $1.45 | $1.51 | $1.40 | $1.44 | 743,161 | $1.46 | 4,350 |
| BIYA | 17:20 | $1.88 | $1.94 | $1.86 | $1.93 | 110,912 | $1.91 | 589 |
| BIYA | 17:25 | $1.92 | $2.20 | $1.92 | $2.16 | 502,588 | $2.05 | 3,386 |
| BIYA | 17:30 | $2.17 | $2.22 | $2.08 | $2.11 | 662,827 | $2.15 | 4,647 |
| BIYA | 17:35 | $2.11 | $2.16 | $1.95 | $2.01 | 370,276 | $2.05 | 2,588 |
| BIYA | 17:40 | $2.01 | $2.03 | $1.98 | $2.00 | 151,300 | $2.00 | 978 |
| BIYA | 17:45 | $2.01 | $2.10 | $1.99 | $2.01 | 125,390 | $2.04 | 869 |
| SXTC | 17:20 | $2.10 | $2.11 | $1.92 | $1.97 | 149,611 | $2.00 | 1,325 |
| SXTC | 17:25 | $2.01 | $2.06 | $1.97 | $1.97 | 118,758 | $2.00 | 890 |
| SXTC | 17:30 | $1.96 | $1.98 | $1.86 | $1.89 | 126,365 | $1.91 | 951 |
| SXTC | 17:35 | $1.90 | $1.99 | $1.89 | $1.94 | 71,986 | $1.95 | 492 |
| SXTC | 17:40 | $1.93 | $1.95 | $1.85 | $1.91 | 43,870 | $1.90 | 382 |
| SXTC | 17:45 | $1.91 | $1.99 | $1.91 | $1.98 | 54,064 | $1.97 | 426 |
| MI | 17:20 | $1.51 | $1.54 | $1.50 | $1.51 | 30,822 | $1.52 | 244 |
| MI | 17:25 | $1.50 | $1.55 | $1.48 | $1.51 | 68,471 | $1.51 | 316 |
| MI | 17:30 | $1.52 | $1.52 | $1.49 | $1.51 | 74,194 | $1.50 | 208 |
| MI | 17:35 | $1.52 | $1.55 | $1.51 | $1.51 | 69,043 | $1.53 | 226 |
| MI | 17:40 | $1.52 | $1.54 | $1.37 | $1.38 | 103,922 | $1.44 | 481 |
| MI | 17:45 | $1.38 | $1.44 | $1.37 | $1.44 | 137,959 | $1.40 | 458 |
| WHLR | 17:20 | $1.04 | $1.07 | $1.00 | $1.07 | 31,083 | $1.02 | 112 |
| WHLR | 17:25 | $1.07 | $1.07 | $1.03 | $1.06 | 36,138 | $1.05 | 107 |
| WHLR | 17:30 | $1.05 | $1.10 | $1.04 | $1.10 | 100,082 | $1.08 | 313 |
| WHLR | 17:35 | $1.09 | $1.10 | $1.02 | $1.03 | 39,862 | $1.06 | 206 |
| WHLR | 17:40 | $1.03 | $1.05 | $1.02 | $1.04 | 27,010 | $1.04 | 101 |
| WHLR | 17:45 | $1.04 | $1.04 | $1.02 | $1.02 | 21,022 | $1.03 | 88 |
| LCFY | 17:20 | $2.43 | $2.44 | $2.40 | $2.40 | 7,187 | $2.42 | 81 |
| LCFY | 17:25 | $2.40 | $2.40 | $2.40 | $2.40 | 2,983 | $2.40 | 45 |
| LCFY | 17:30 | $2.42 | $2.50 | $2.40 | $2.50 | 27,230 | $2.49 | 275 |
| LCFY | 17:35 | $2.49 | $2.49 | $2.43 | $2.46 | 10,004 | $2.47 | 63 |
| LCFY | 17:40 | $2.43 | $2.43 | $2.43 | $2.43 | 2,072 | $2.43 | 18 |
| LCFY | 17:45 | $2.43 | $2.45 | $2.43 | $2.45 | 1,561 | $2.45 | 12 |

NCPL printed 457–17,274 shares and 2–30 trades per bar from 17:20 to 17:45 ET at $1.20–$1.25 (no 17:30 bar).

**Yahoo timeline (shape only, not volume or exact levels):**

| Ticker | 17:35 | 17:40 | 17:45 | 17:50 | 17:55 | 18:00 | 18:03 |
|--------|-------|-------|-------|-------|-------|-------|-------|
| MTEN | $1.42 | $1.45 | $1.44 | $1.47 | $1.35 | $1.41 | $1.40 |
| BIYA | $2.02 | $2.00 | $2.00 | $2.04 | $2.12 | $2.11 | $2.15 |
| SXTC | $1.93 | $1.91 | $1.98 | $1.95 | $1.99 | $2.16 | $2.09 |
| MI | $1.51 | $1.38 | $1.44 | $1.50 | $1.50 | $1.42 | $1.44 |
| WHLR | $1.04 | $1.04 | $1.03 | $1.02 | $1.04 | $1.02 | $1.02 |
| LCFY | $2.42 | $2.43 | $2.45 | $2.50 | $2.44 | $2.45 | — |

MTEN's one-minute Yahoo bars show the $1.58 high at 17:40 ET and trades between $1.35 and $1.44 from 17:56 to 18:03 ET.

**MTEN — second qualifying AH scan; ENTERED at $1.39 (Grade B).** Every entry gate passes:

- **Appearance gate:** >10% AH in two AH scans (23:30 +10.6%, 00:00 +51.2%).
- **Day%** -0.4% (above -15%). **Total%** at the fill is +44.4% from the $0.962 prior close, far under the +150% ceiling. Float 6.1M.
- **Trajectory: BUILD.** After the 17:15 re-ignition, SIP made higher highs in four of the next five bars ($1.29 → $1.32 → $1.37 → $1.45 → **$1.59 at 17:40 ET**). The high is late, far outside the 16:00–16:15 opening window, so the first-bar-spike skip does not apply. At the fill the price was 12.6% below the high, inside the ~20% hold threshold. The pullback since 17:45 ($1.35–$1.44 on Yahoo) is the main risk to watch.
- **SIP volume is real and accumulating:** 711,200–1,476,192 shares and 3,894–7,914 trades in every bar from 17:15 to 17:45 ET, and the scanner VRatio rose from 3.9x to 7.3x.
- **SIP corroborates the scanner price:** the 17:45 bar close of $1.44 and VWAP of $1.46 match the scanner's $1.45; this is not a bad print. The newest SIP bar is 15 minutes behind the scan, the normal free-tier delay.
- **Book:** the IEX quote is frozen at 16:46:21 ET (`bid $1.00 x100  ask $1.02 x100`), two-sided with size. The delayed SIP book at 17:47:41 ET was $1.48 x1,000 / $1.49 x3,100. I priced the limit from the latest Yahoo trades ($1.35–$1.39 at 17:56–18:00 ET) rather than the stale IEX ask.
- **Catalyst Grade B — completed acquisition (acquirer side), dated and timed.** The 6-K accepted by EDGAR at 16:30:51 ET on October 6 (graded at 23:30) reports a signed and completed $15M cash purchase of HK Phoenix Gateway Alliance Limited. No new search was needed. Concern noted: the price is about twice MTEN's $7.3M market cap and the filing gives no target revenue or rationale. Hold up to 2 days with a -15% hard stop at $1.18.
- **First day of unusual activity:** SIP daily volume was 116K–170K shares from October 1 to October 5; today printed 10.2M shares. Not a MULTI-SESSION-RUNNER; no `WINNERS_TRACKING.md` entry. MTEN was last traded on August 10–11 (Grade None, -2.9%), a separate episode.
- **Pre-buy checks:** `broker.js positions` showed only BIYA and `orders all` showed no MTEN order today.
- **Order:** `buy MTEN 70 --limit 1.42 --ext` (QTY = floor($100 / $1.42)). Filled 70 @ **$1.39** at 18:01:20 ET; cost $97.30.
- **Chase check:** this scan is the qualifying scan ($1.45 / Total +50.7%). The fill's Total +44.4% is 6.3 points below it, so no CHASE-CAP note applies.
- **CONFIRM-3 NO** scores the 16:30 ignition, which failed its third bar; the tool does not re-score the 17:15 leg. This is log-only and does not gate the entry.

**LCFY — second >10% AH appearance; skip (thin drift).** AH change slipped from +21.5% to +18.6%. SIP printed 1,561–27,230 shares and 12–275 trades per bar from 17:20 to 17:45 ET at $2.40–$2.50; Yahoo shows $2.45 at 18:00, 6.5% below the $2.62 high from the 16:35 bar. That fails the SIP accumulation rule under the MODD precedent. Day -12.4%, Total +3.9%, and the Grade B Map Labs acquisition PR (October 6) would otherwise pass. CONFIRM-3 reads NO. Thin volume keeps LCFY out of the book diagnostic.

**WHLR — second >10% AH appearance; skip (Day -16.5%); no DEAD-CAT-OVERRIDE WATCH.** Scanner AH change rose from +13.2% to +14.3% and the price stays above the $0.91 regular close. The 23:30 checklist said this would start the watch, but SIP shows a thin drift: 21,022–100,082 shares and 88–313 trades per bar at $1.02–$1.10, 16% below the $1.24 high from 16:45 ET. The watch exists to test the dead-cat filter on BYAH-style builds; this thin drift would also fail the accumulation rule, so recording it would skew that sample. Reference price for the morning tally: $1.04 (scanner) at 18:00 ET, Total -4.6% from the $1.09 prior close. Catalyst Grade None.

**BIYA — `already entered` (52 @ $1.91); tracking only.** SIP confirmed the 17:25–17:30 push to a new **$2.22 high** on 502,588 and 662,827 shares (3,386 and 4,647 trades), then a pullback to $2.00–$2.01 on 125K–370K shares. Yahoo shows $2.15 at 18:03. `broker.js positions` marks it at $2.18, **+$14.04 (+14.1%)**. CONFIRM-3 stays YES.

**SXTC — seventh qualifying AH scan; skip live entry (Day -39.9%); DEAD-CAT-OVERRIDE WATCH continues.** The scanner's +52.8% ($1.91) matches the 17:30–17:45 SIP closes ($1.89–$1.98) and lags the tape: Yahoo shows **$2.16 at 18:00 and $2.09 at 18:03**, back at the $2.08 prior close and 19% below the $2.58 AH high. SIP volume is shrinking (149,611 → 54,064 shares per bar). The 22:25 hypothetical ($1.57 at 16:25 ET) stands.

**MI — fourth >10% AH appearance; skip (dead-cat bounce, Grade D).** AH change kept falling (+25.2% → +24.0% → +20.6% → +12.2%). The 17:40 SIP bar broke to $1.37 on 103,922 shares; Yahoo shows $1.44 at 18:03, 22% below the $1.84 high.

**NCPL — fifth >10% AH appearance; skip stands (thin drift, Day -17.4%).** AH change rose to +14.7% ($1.25) on 2–30 trades per bar. Like WHLR, this is a thin drift and does not start a DEAD-CAT-OVERRIDE WATCH.

**VCIG** is absent from this scan; its SPIKE→FADE skip and the 22:20 FIRST-BAR-SPIKE WATCH hypothetical ($1.69 at 16:20 ET) stand.

**Below threshold:**

- **XHLD** (+9.9% AH, Day +51.6%, Total +66.5%, float 10.5M; on the 21:30 watchlist, +6.4% at 22:30): SIP shows AH pops to $0.69 in the 16:15 bar (818,437 shares / 2,162 trades) and the 17:00 bar (322,091 shares / 735 trades), with $0.61–$0.67 and 31K–146K shares in the other bars. Yahoo shows $0.67 at 18:02. It cannot reach two >10% AH scans before the final scan.
- **OLOX** (+7.2%, day 2 after its October 5 win), **FEAM** (+8.5%), **ALDX** (+6.9%), **DCX** (+6.8%), **JAGX** (+6.0%, Day +18.8%), **STEX** (+6.0%), and **NCT** (+6.0%) are tracked only.

**Instrumentation (verbatim; log-only):**

```text
BIYA 2026-10-06  SPIKE  16:08ET  +21%  $1.65  372 trades / 58k sh  (first co-spike bar) (as-of 18:00ET)
BIYA 2026-10-06  CONFIRM-3  YES ignition 16:05ET 260.8x; confirmed 16:15ET $1.81 as-of 18:00ET
MTEN 2026-10-06  SPIKE  16:41ET  +22%  $1.17  637 trades / 143k sh  (first co-spike bar) (as-of 18:00ET)
MTEN 2026-10-06  CONFIRM-3  NO ignition 16:30ET failed third-bar hold/volume as-of 18:00ET
LCFY 2026-10-06  NO-SPIKE  peak +28% @16:38ET  (no bar cleared +15% on a volume co-spike) (as-of 18:00ET)
LCFY 2026-10-06  CONFIRM-3  NO ignition 16:35ET failed third-bar hold/volume as-of 18:00ET
WHLR 2026-10-06  SPIKE  16:46ET  +16%  $1.06  110 trades / 34k sh  (first co-spike bar) (as-of 18:00ET)
WHLR 2026-10-06  CONFIRM-3  NO ignition 16:45ET failed third-bar hold/volume as-of 18:00ET
SXTC 2026-10-06  SPIKE  16:03ET  +32%  $1.65  135 trades / 30k sh  (first co-spike bar) (as-of 18:00ET)
SXTC 2026-10-06  CONFIRM-3  NO ignition 16:05ET failed third-bar hold/volume as-of 18:00ET
MI 2026-10-06  SPIKE  16:18ET  +30%  $1.60  2066 trades / 421k sh  (first co-spike bar) (as-of 18:00ET)
MI 2026-10-06  CONFIRM-3  NO ignition 16:15ET failed third-bar hold/volume as-of 18:00ET
NCPL 2026-10-06  NO-SPIKE  peak +17% @16:03ET  (no bar cleared +15% on a volume co-spike) (as-of 18:00ET)
NCPL 2026-10-06  CONFIRM-3  NO no local-volume new-high ignition as-of 18:00ET
```

**Shared SIP volume context (`sip-ah-volume-v1`, log-only):** The prior trading date is 2026-10-05, a normal Monday session. Inputs were fetched with `broker.js bars SYM --tf 5Min --start 2026-10-05T20:00:00Z --limit 1000 --feed sip --json` (one page each, no next-page token) and archived as `log/2026-10-06/SYM-0000-volume-sip.json`, with computed rows in `SYM-0000-volume-metric.json`. MI and WHLR have complete prior-session coverage (48/48). The others stay incomplete (MTEN 5/48, BIYA 18/48, LCFY 1/48, SXTC 10/48, NCPL 25/48), so their prior-peak ratios remain unknown. MTEN's 17:20 bar reads 32.60x local; the 17:40 bar that set the high reads 1.55x. The SXTC share-consolidation headline, BIYA's July 1-for-10 reverse split, and WHLR's September 21 1-for-9 reverse split remain unreviewed against this window.

```text
# MTEN shared SIP volume; prior 2026-10-05 5/48 slots; log-only
# reconstructed as-of 2026-10-06T22:00:20+00:00; source fetched 2026-10-06T22:02:14.941775Z
MTEN 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=652 local=unknown prior-peak=unknown status=warmup
MTEN 2026-10-06  VOLUME-CONTEXT 16:30ET start=2026-10-06T20:30:00+00:00 shares=152894 local=unknown prior-peak=unknown status=missing-baseline
MTEN 2026-10-06  VOLUME-CONTEXT 16:35ET start=2026-10-06T20:35:00+00:00 shares=170255 local=unknown prior-peak=unknown status=missing-baseline
MTEN 2026-10-06  VOLUME-CONTEXT 16:40ET start=2026-10-06T20:40:00+00:00 shares=478591 local=unknown prior-peak=unknown status=missing-baseline
MTEN 2026-10-06  VOLUME-CONTEXT 16:45ET start=2026-10-06T20:45:00+00:00 shares=166035 local=0.9752x prior-peak=unknown status=ok
MTEN 2026-10-06  VOLUME-CONTEXT 16:50ET start=2026-10-06T20:50:00+00:00 shares=25301 local=0.1486x prior-peak=unknown status=ok
MTEN 2026-10-06  VOLUME-CONTEXT 16:55ET start=2026-10-06T20:55:00+00:00 shares=12949 local=0.0780x prior-peak=unknown status=ok
MTEN 2026-10-06  VOLUME-CONTEXT 17:00ET start=2026-10-06T21:00:00+00:00 shares=33587 local=1.3275x prior-peak=unknown status=ok
MTEN 2026-10-06  VOLUME-CONTEXT 17:05ET start=2026-10-06T21:05:00+00:00 shares=36447 local=1.4405x prior-peak=unknown status=ok
MTEN 2026-10-06  VOLUME-CONTEXT 17:10ET start=2026-10-06T21:10:00+00:00 shares=18168 local=0.5409x prior-peak=unknown status=ok
MTEN 2026-10-06  VOLUME-CONTEXT 17:15ET start=2026-10-06T21:15:00+00:00 shares=969962 local=28.8791x prior-peak=unknown status=ok
MTEN 2026-10-06  VOLUME-CONTEXT 17:20ET start=2026-10-06T21:20:00+00:00 shares=1188203 local=32.6008x prior-peak=unknown status=ok
MTEN 2026-10-06  VOLUME-CONTEXT 17:25ET start=2026-10-06T21:25:00+00:00 shares=711200 local=0.7332x prior-peak=unknown status=ok
MTEN 2026-10-06  VOLUME-CONTEXT 17:30ET start=2026-10-06T21:30:00+00:00 shares=952125 local=0.9816x prior-peak=unknown status=ok
MTEN 2026-10-06  VOLUME-CONTEXT 17:35ET start=2026-10-06T21:35:00+00:00 shares=1017234 local=1.0684x prior-peak=unknown status=ok
MTEN 2026-10-06  VOLUME-CONTEXT 17:40ET start=2026-10-06T21:40:00+00:00 shares=1476192 local=1.5504x prior-peak=unknown status=ok
MTEN 2026-10-06  VOLUME-CONTEXT 17:45ET start=2026-10-06T21:45:00+00:00 shares=743161 local=0.7306x prior-peak=unknown status=ok
# BIYA shared SIP volume; prior 2026-10-05 18/48 slots; log-only
# reconstructed as-of 2026-10-06T22:00:20+00:00; source fetched 2026-10-06T22:02:17.045720Z
BIYA 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=1095 local=unknown prior-peak=unknown status=warmup
BIYA 2026-10-06  VOLUME-CONTEXT 16:05ET start=2026-10-06T20:05:00+00:00 shares=285556 local=unknown prior-peak=unknown status=warmup
BIYA 2026-10-06  VOLUME-CONTEXT 16:10ET start=2026-10-06T20:10:00+00:00 shares=1072394 local=unknown prior-peak=unknown status=warmup
BIYA 2026-10-06  VOLUME-CONTEXT 16:15ET start=2026-10-06T20:15:00+00:00 shares=1596650 local=5.5914x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 16:20ET start=2026-10-06T20:20:00+00:00 shares=550815 local=0.5136x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 16:25ET start=2026-10-06T20:25:00+00:00 shares=307657 local=0.2869x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 16:30ET start=2026-10-06T20:30:00+00:00 shares=452655 local=0.8218x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 16:35ET start=2026-10-06T20:35:00+00:00 shares=413407 local=0.9133x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 16:40ET start=2026-10-06T20:40:00+00:00 shares=802489 local=1.9412x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 16:45ET start=2026-10-06T20:45:00+00:00 shares=347463 local=0.7676x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 16:50ET start=2026-10-06T20:50:00+00:00 shares=242874 local=0.5875x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 16:55ET start=2026-10-06T20:55:00+00:00 shares=152538 local=0.4390x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 17:00ET start=2026-10-06T21:00:00+00:00 shares=248222 local=1.0220x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 17:05ET start=2026-10-06T21:05:00+00:00 shares=633569 local=2.6086x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 17:10ET start=2026-10-06T21:10:00+00:00 shares=155877 local=0.6280x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 17:15ET start=2026-10-06T21:15:00+00:00 shares=131059 local=0.5280x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 17:20ET start=2026-10-06T21:20:00+00:00 shares=110912 local=0.7115x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 17:25ET start=2026-10-06T21:25:00+00:00 shares=502588 local=3.8348x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 17:30ET start=2026-10-06T21:30:00+00:00 shares=662827 local=5.0575x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 17:35ET start=2026-10-06T21:35:00+00:00 shares=370276 local=0.7367x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 17:40ET start=2026-10-06T21:40:00+00:00 shares=151300 local=0.3010x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 17:45ET start=2026-10-06T21:45:00+00:00 shares=125390 local=0.3386x prior-peak=unknown status=ok
# LCFY shared SIP volume; prior 2026-10-05 1/48 slots; log-only
# reconstructed as-of 2026-10-06T22:00:20+00:00; source fetched 2026-10-06T22:02:19.198614Z
LCFY 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=5907 local=unknown prior-peak=unknown status=warmup
LCFY 2026-10-06  VOLUME-CONTEXT 16:15ET start=2026-10-06T20:15:00+00:00 shares=411 local=unknown prior-peak=unknown status=missing-baseline
LCFY 2026-10-06  VOLUME-CONTEXT 16:20ET start=2026-10-06T20:20:00+00:00 shares=3627 local=unknown prior-peak=unknown status=missing-baseline
LCFY 2026-10-06  VOLUME-CONTEXT 16:25ET start=2026-10-06T20:25:00+00:00 shares=677 local=unknown prior-peak=unknown status=missing-baseline
LCFY 2026-10-06  VOLUME-CONTEXT 16:30ET start=2026-10-06T20:30:00+00:00 shares=1468 local=2.1684x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 16:35ET start=2026-10-06T20:35:00+00:00 shares=103702 local=70.6417x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 16:40ET start=2026-10-06T20:40:00+00:00 shares=161504 local=110.0163x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 16:45ET start=2026-10-06T20:45:00+00:00 shares=39640 local=0.3822x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 16:50ET start=2026-10-06T20:50:00+00:00 shares=24367 local=0.2350x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 16:55ET start=2026-10-06T20:55:00+00:00 shares=13202 local=0.3330x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 17:00ET start=2026-10-06T21:00:00+00:00 shares=55564 local=2.2803x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 17:05ET start=2026-10-06T21:05:00+00:00 shares=23480 local=0.9636x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 17:10ET start=2026-10-06T21:10:00+00:00 shares=23553 local=1.0031x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 17:15ET start=2026-10-06T21:15:00+00:00 shares=13446 local=0.5709x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 17:20ET start=2026-10-06T21:20:00+00:00 shares=7187 local=0.3061x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 17:25ET start=2026-10-06T21:25:00+00:00 shares=2983 local=0.2219x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 17:30ET start=2026-10-06T21:30:00+00:00 shares=27230 local=3.7888x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 17:35ET start=2026-10-06T21:35:00+00:00 shares=10004 local=1.3920x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 17:40ET start=2026-10-06T21:40:00+00:00 shares=2072 local=0.2071x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 17:45ET start=2026-10-06T21:45:00+00:00 shares=1561 local=0.1560x prior-peak=unknown status=ok
# WHLR shared SIP volume; prior 2026-10-05 48/48 slots; log-only
# reconstructed as-of 2026-10-06T22:00:20+00:00; source fetched 2026-10-06T22:02:21.313793Z
WHLR 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=79913 local=unknown prior-peak=0.0640x status=warmup
WHLR 2026-10-06  VOLUME-CONTEXT 16:05ET start=2026-10-06T20:05:00+00:00 shares=42488 local=unknown prior-peak=0.0340x status=warmup
WHLR 2026-10-06  VOLUME-CONTEXT 16:10ET start=2026-10-06T20:10:00+00:00 shares=11795 local=unknown prior-peak=0.0094x status=warmup
WHLR 2026-10-06  VOLUME-CONTEXT 16:15ET start=2026-10-06T20:15:00+00:00 shares=8067 local=0.1899x prior-peak=0.0065x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 16:20ET start=2026-10-06T20:20:00+00:00 shares=10432 local=0.8844x prior-peak=0.0084x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 16:25ET start=2026-10-06T20:25:00+00:00 shares=12272 local=1.1764x prior-peak=0.0098x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 16:30ET start=2026-10-06T20:30:00+00:00 shares=8867 local=0.8500x prior-peak=0.0071x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 16:35ET start=2026-10-06T20:35:00+00:00 shares=12529 local=1.2010x prior-peak=0.0100x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 16:40ET start=2026-10-06T20:40:00+00:00 shares=23713 local=1.9323x prior-peak=0.0190x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 16:45ET start=2026-10-06T20:45:00+00:00 shares=265151 local=21.1630x prior-peak=0.2124x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 16:50ET start=2026-10-06T20:50:00+00:00 shares=280898 local=11.8457x prior-peak=0.2250x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 16:55ET start=2026-10-06T20:55:00+00:00 shares=288869 local=1.0895x prior-peak=0.2314x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 17:00ET start=2026-10-06T21:00:00+00:00 shares=84294 local=0.3001x prior-peak=0.0675x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 17:05ET start=2026-10-06T21:05:00+00:00 shares=46520 local=0.1656x prior-peak=0.0373x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 17:10ET start=2026-10-06T21:10:00+00:00 shares=48261 local=0.5725x prior-peak=0.0387x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 17:15ET start=2026-10-06T21:15:00+00:00 shares=26393 local=0.5469x prior-peak=0.0211x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 17:20ET start=2026-10-06T21:20:00+00:00 shares=31083 local=0.6682x prior-peak=0.0249x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 17:25ET start=2026-10-06T21:25:00+00:00 shares=36138 local=1.1626x prior-peak=0.0289x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 17:30ET start=2026-10-06T21:30:00+00:00 shares=100082 local=3.2198x prior-peak=0.0802x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 17:35ET start=2026-10-06T21:35:00+00:00 shares=39862 local=1.1030x prior-peak=0.0319x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 17:40ET start=2026-10-06T21:40:00+00:00 shares=27010 local=0.6776x prior-peak=0.0216x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 17:45ET start=2026-10-06T21:45:00+00:00 shares=21022 local=0.5274x prior-peak=0.0168x status=ok
# SXTC shared SIP volume; prior 2026-10-05 10/48 slots; log-only
# reconstructed as-of 2026-10-06T22:00:20+00:00; source fetched 2026-10-06T22:02:23.468514Z
SXTC 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=75597 local=unknown prior-peak=unknown status=warmup
SXTC 2026-10-06  VOLUME-CONTEXT 16:05ET start=2026-10-06T20:05:00+00:00 shares=683755 local=unknown prior-peak=unknown status=warmup
SXTC 2026-10-06  VOLUME-CONTEXT 16:10ET start=2026-10-06T20:10:00+00:00 shares=212492 local=unknown prior-peak=unknown status=warmup
SXTC 2026-10-06  VOLUME-CONTEXT 16:15ET start=2026-10-06T20:15:00+00:00 shares=103774 local=0.4884x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 16:20ET start=2026-10-06T20:20:00+00:00 shares=295399 local=1.3902x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 16:25ET start=2026-10-06T20:25:00+00:00 shares=394574 local=1.8569x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 16:30ET start=2026-10-06T20:30:00+00:00 shares=1344735 local=4.5523x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 16:35ET start=2026-10-06T20:35:00+00:00 shares=563974 local=1.4293x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 16:40ET start=2026-10-06T20:40:00+00:00 shares=508099 local=0.9009x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 16:45ET start=2026-10-06T20:45:00+00:00 shares=865653 local=1.5349x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 16:50ET start=2026-10-06T20:50:00+00:00 shares=407217 local=0.7220x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 16:55ET start=2026-10-06T20:55:00+00:00 shares=329554 local=0.6486x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 17:00ET start=2026-10-06T21:00:00+00:00 shares=138698 local=0.3406x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 17:05ET start=2026-10-06T21:05:00+00:00 shares=243462 local=0.7388x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 17:10ET start=2026-10-06T21:10:00+00:00 shares=110255 local=0.4529x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 17:15ET start=2026-10-06T21:15:00+00:00 shares=302849 local=2.1835x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 17:20ET start=2026-10-06T21:20:00+00:00 shares=149611 local=0.6145x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 17:25ET start=2026-10-06T21:25:00+00:00 shares=118758 local=0.7938x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 17:30ET start=2026-10-06T21:30:00+00:00 shares=126365 local=0.8446x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 17:35ET start=2026-10-06T21:35:00+00:00 shares=71986 local=0.5697x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 17:40ET start=2026-10-06T21:40:00+00:00 shares=43870 local=0.3694x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 17:45ET start=2026-10-06T21:45:00+00:00 shares=54064 local=0.7510x prior-peak=unknown status=ok
# MI shared SIP volume; prior 2026-10-05 48/48 slots; log-only
# reconstructed as-of 2026-10-06T22:00:20+00:00; source fetched 2026-10-06T22:02:25.527619Z
MI 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=220361 local=unknown prior-peak=0.2093x status=warmup
MI 2026-10-06  VOLUME-CONTEXT 16:05ET start=2026-10-06T20:05:00+00:00 shares=137355 local=unknown prior-peak=0.1304x status=warmup
MI 2026-10-06  VOLUME-CONTEXT 16:10ET start=2026-10-06T20:10:00+00:00 shares=159195 local=unknown prior-peak=0.1512x status=warmup
MI 2026-10-06  VOLUME-CONTEXT 16:15ET start=2026-10-06T20:15:00+00:00 shares=1263614 local=7.9375x prior-peak=1.2000x status=ok
MI 2026-10-06  VOLUME-CONTEXT 16:20ET start=2026-10-06T20:20:00+00:00 shares=2036291 local=12.7912x prior-peak=1.9338x status=ok
MI 2026-10-06  VOLUME-CONTEXT 16:25ET start=2026-10-06T20:25:00+00:00 shares=868347 local=0.6872x prior-peak=0.8246x status=ok
MI 2026-10-06  VOLUME-CONTEXT 16:30ET start=2026-10-06T20:30:00+00:00 shares=427999 local=0.3387x prior-peak=0.4064x status=ok
MI 2026-10-06  VOLUME-CONTEXT 16:35ET start=2026-10-06T20:35:00+00:00 shares=400416 local=0.4611x prior-peak=0.3803x status=ok
MI 2026-10-06  VOLUME-CONTEXT 16:40ET start=2026-10-06T20:40:00+00:00 shares=214703 local=0.5016x prior-peak=0.2039x status=ok
MI 2026-10-06  VOLUME-CONTEXT 16:45ET start=2026-10-06T20:45:00+00:00 shares=461613 local=1.1528x prior-peak=0.4384x status=ok
MI 2026-10-06  VOLUME-CONTEXT 16:50ET start=2026-10-06T20:50:00+00:00 shares=288180 local=0.7197x prior-peak=0.2737x status=ok
MI 2026-10-06  VOLUME-CONTEXT 16:55ET start=2026-10-06T20:55:00+00:00 shares=181642 local=0.6303x prior-peak=0.1725x status=ok
MI 2026-10-06  VOLUME-CONTEXT 17:00ET start=2026-10-06T21:00:00+00:00 shares=90521 local=0.3141x prior-peak=0.0860x status=ok
MI 2026-10-06  VOLUME-CONTEXT 17:05ET start=2026-10-06T21:05:00+00:00 shares=140158 local=0.7716x prior-peak=0.1331x status=ok
MI 2026-10-06  VOLUME-CONTEXT 17:10ET start=2026-10-06T21:10:00+00:00 shares=74036 local=0.5282x prior-peak=0.0703x status=ok
MI 2026-10-06  VOLUME-CONTEXT 17:15ET start=2026-10-06T21:15:00+00:00 shares=63034 local=0.6963x prior-peak=0.0599x status=ok
MI 2026-10-06  VOLUME-CONTEXT 17:20ET start=2026-10-06T21:20:00+00:00 shares=30822 local=0.4163x prior-peak=0.0293x status=ok
MI 2026-10-06  VOLUME-CONTEXT 17:25ET start=2026-10-06T21:25:00+00:00 shares=68471 local=1.0863x prior-peak=0.0650x status=ok
MI 2026-10-06  VOLUME-CONTEXT 17:30ET start=2026-10-06T21:30:00+00:00 shares=74194 local=1.1770x prior-peak=0.0705x status=ok
MI 2026-10-06  VOLUME-CONTEXT 17:35ET start=2026-10-06T21:35:00+00:00 shares=69043 local=1.0084x prior-peak=0.0656x status=ok
MI 2026-10-06  VOLUME-CONTEXT 17:40ET start=2026-10-06T21:40:00+00:00 shares=103922 local=1.5052x prior-peak=0.0987x status=ok
MI 2026-10-06  VOLUME-CONTEXT 17:45ET start=2026-10-06T21:45:00+00:00 shares=137959 local=1.8594x prior-peak=0.1310x status=ok
# NCPL shared SIP volume; prior 2026-10-05 25/48 slots; log-only
# reconstructed as-of 2026-10-06T22:00:20+00:00; source fetched 2026-10-06T22:02:27.727634Z
NCPL 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=71987 local=unknown prior-peak=unknown status=warmup
NCPL 2026-10-06  VOLUME-CONTEXT 16:05ET start=2026-10-06T20:05:00+00:00 shares=71440 local=unknown prior-peak=unknown status=warmup
NCPL 2026-10-06  VOLUME-CONTEXT 16:10ET start=2026-10-06T20:10:00+00:00 shares=7284 local=unknown prior-peak=unknown status=warmup
NCPL 2026-10-06  VOLUME-CONTEXT 16:15ET start=2026-10-06T20:15:00+00:00 shares=4790 local=0.0670x prior-peak=unknown status=ok
NCPL 2026-10-06  VOLUME-CONTEXT 16:20ET start=2026-10-06T20:20:00+00:00 shares=1020 local=0.1400x prior-peak=unknown status=ok
NCPL 2026-10-06  VOLUME-CONTEXT 16:25ET start=2026-10-06T20:25:00+00:00 shares=7199 local=1.5029x prior-peak=unknown status=ok
NCPL 2026-10-06  VOLUME-CONTEXT 16:30ET start=2026-10-06T20:30:00+00:00 shares=234 local=0.0489x prior-peak=unknown status=ok
NCPL 2026-10-06  VOLUME-CONTEXT 16:35ET start=2026-10-06T20:35:00+00:00 shares=1540 local=1.5098x prior-peak=unknown status=ok
NCPL 2026-10-06  VOLUME-CONTEXT 16:40ET start=2026-10-06T20:40:00+00:00 shares=1404 local=0.9117x prior-peak=unknown status=ok
NCPL 2026-10-06  VOLUME-CONTEXT 16:45ET start=2026-10-06T20:45:00+00:00 shares=175 local=0.1246x prior-peak=unknown status=ok
NCPL 2026-10-06  VOLUME-CONTEXT 16:50ET start=2026-10-06T20:50:00+00:00 shares=240 local=0.1709x prior-peak=unknown status=ok
NCPL 2026-10-06  VOLUME-CONTEXT 17:00ET start=2026-10-06T21:00:00+00:00 shares=1760 local=unknown prior-peak=unknown status=missing-baseline
NCPL 2026-10-06  VOLUME-CONTEXT 17:05ET start=2026-10-06T21:05:00+00:00 shares=340 local=unknown prior-peak=unknown status=missing-baseline
NCPL 2026-10-06  VOLUME-CONTEXT 17:15ET start=2026-10-06T21:15:00+00:00 shares=1000 local=unknown prior-peak=unknown status=missing-baseline
NCPL 2026-10-06  VOLUME-CONTEXT 17:20ET start=2026-10-06T21:20:00+00:00 shares=457 local=unknown prior-peak=unknown status=missing-baseline
NCPL 2026-10-06  VOLUME-CONTEXT 17:25ET start=2026-10-06T21:25:00+00:00 shares=1104 local=unknown prior-peak=unknown status=missing-baseline
NCPL 2026-10-06  VOLUME-CONTEXT 17:35ET start=2026-10-06T21:35:00+00:00 shares=17274 local=unknown prior-peak=unknown status=missing-baseline
NCPL 2026-10-06  VOLUME-CONTEXT 17:40ET start=2026-10-06T21:40:00+00:00 shares=2298 local=unknown prior-peak=unknown status=missing-baseline
NCPL 2026-10-06  VOLUME-CONTEXT 17:45ET start=2026-10-06T21:45:00+00:00 shares=2315 local=unknown prior-peak=unknown status=missing-baseline
```

**Book diagnostic (verbatim; log-only)** for the five tradable >10% names with SIP volume above the thin-drift level (LCFY and NCPL are excluded). All IEX quotes are frozen at or before 17:00 ET.

```text
MTEN BOOK iex bid $1.00 x100 / ask $1.02 x100 @ 2026-10-06 16:46:21 ET age 1h16m two-sided spread 1.96% of ask
MTEN BOOK sip-15m bid $1.48 x1000 / ask $1.49 x3100 @ 2026-10-06 17:47:41 ET age 15m00s two-sided spread 0.67% of ask
MTEN BOOK refresh +15s iex unchanged @ 2026-10-06 16:46:21 ET
MTEN BOOK verdict: IEX STALE 1h16m; SIP-15m TWO-SIDED (observed 2026-10-06 18:02:40 ET; log-only)
BIYA BOOK iex bid $1.88 x100 / ask $1.92 x100 @ 2026-10-06 16:54:16 ET age 1h08m two-sided spread 2.08% of ask
BIYA BOOK sip-15m bid $2.04 x1100 / ask $2.05 x300 @ 2026-10-06 17:47:38 ET age 15m02s two-sided spread 0.49% of ask
BIYA BOOK refresh +15s iex unchanged @ 2026-10-06 16:54:16 ET
BIYA BOOK verdict: IEX STALE 1h08m; SIP-15m TWO-SIDED (observed 2026-10-06 18:02:40 ET; log-only)
SXTC BOOK iex bid $2.19 x100 / ask $2.24 x100 @ 2026-10-06 16:48:07 ET age 1h14m two-sided spread 2.23% of ask
SXTC BOOK sip-15m bid $1.94 x300 / ask $1.95 x900 @ 2026-10-06 17:47:40 ET age 15m00s two-sided spread 0.51% of ask
SXTC BOOK refresh +15s iex unchanged @ 2026-10-06 16:48:07 ET
SXTC BOOK verdict: IEX STALE 1h14m; SIP-15m TWO-SIDED (observed 2026-10-06 18:02:40 ET; log-only)
MI BOOK iex bid $1.56 x100 / ask $1.59 x100 @ 2026-10-06 16:59:55 ET age 1h02m two-sided spread 1.89% of ask
MI BOOK sip-15m bid $1.38 x700 / ask $1.39 x500 @ 2026-10-06 17:47:40 ET age 15m01s two-sided spread 0.72% of ask
MI BOOK refresh +15s iex unchanged @ 2026-10-06 16:59:55 ET
MI BOOK verdict: IEX STALE 1h02m; SIP-15m TWO-SIDED (observed 2026-10-06 18:02:40 ET; log-only)
WHLR BOOK iex bid $1.03 x100 / ask $1.07 x100 @ 2026-10-06 16:57:58 ET age 1h04m two-sided spread 3.74% of ask
WHLR BOOK sip-15m bid $1.03 x800 / ask $1.04 x400 @ 2026-10-06 17:47:39 ET age 15m01s two-sided spread 0.96% of ask
WHLR BOOK refresh +15s iex unchanged @ 2026-10-06 16:57:58 ET
WHLR BOOK verdict: IEX STALE 1h04m; SIP-15m TWO-SIDED (observed 2026-10-06 18:02:40 ET; log-only)
```

**00:30 checklist (final scan):** MTEN and BIYA are `already entered`; track them only. LCFY can still qualify if per-bar SIP volume returns to hundreds of thousands of shares. WHLR and NCPL stay Day% skips unless SIP volume turns into a real build; SXTC stays a Day% skip on DEAD-CAT-OVERRIDE WATCH. MI stays a dead-cat and Grade D skip. Run the final-scan feed-lag cross-check on every tracked name (VCIG, SXTC, BIYA, MI, NCPL, MTEN, LCFY, WHLR, LHSW, OLOX, XHLD, and the 28-name 21:30 watchlist), and record a FINAL-SCAN-GATE-BLOCK note for any first-appearance late igniter with real SIP volume. KAPA's dead-cat guard and OLOX's day-2 tag still apply. EVOL, MHUAF, VNPKF, WTLLF, NWINF, and KHDHF remain untradable (carried).

**Daily email:** Report the MTEN entry (70 @ $1.39, Grade B on the same-day 6-K for a completed $15M cash acquisition; BUILD from the 17:15 ET re-ignition to a $1.59 SIP high at 17:40 ET on 711K–1.48M shares per bar; filled 12.6% below the high), the BIYA position at +14.1% after a new $2.22 high, SXTC trading back at its $2.08 prior close on DEAD-CAT-OVERRIDE WATCH, and the decision not to start a WHLR watch on a thin drift. No item from this scan requires Juan's input.

## Scan 00:30 CEST (6:30 PM ET)

**Decision:** No entry at the final scan. BURU is the only new >10% name. Its 18:00–18:05 ET spike ran on real SIP volume (745,287 shares and 3,910 trades in the 18:05 bar), but this is its first >10% AH appearance, so the 2-AH-scan gate blocks it. CONFIRM-3 reads NO, so it does not qualify as a FINAL-SCAN-GATE-BLOCK. Every repeat name keeps its earlier skip: SXTC (Day -39.9%, DEAD-CAT-OVERRIDE WATCH continues), MI (dead-cat bounce, Grade D), NCPL and WHLR (Day% below -15% on thin SIP volume), and LCFY (thin drift, now fading). Open positions: BIYA is +23.6% after a new $2.39 SIP high and MTEN is +6.5%. The feed-lag cross-check found no tracked name above +10% that the scanner dropped or under-reported. Final AH appearance counts: SXTC **8**, BIYA **7**, NCPL **6**, MI **5**, VCIG **5** (absent), MTEN **3**, LCFY **3**, WHLR **3**, BURU **1**, LHSW **1**, ICMB **1**.

`python3 scripts/scan.py --all` ran at 18:30:09 ET (00:30:09 CEST on October 7 / 22:30:09 UTC) in the AFTERHOURS session and returned 12 hits. The US trading date is 2026-10-06. Repository sync completed before the scan.

```text
  Supplementary AH-change-only (>15%, not in volume pass): none
  AH >10% at this snapshot (unrounded): BIYA, BURU, LCFY, MI, MTEN, NCPL, SXTC, WHLR
```

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| MTEN | [TV](https://www.tradingview.com/chart/?symbol=MTEN) | $0.96 | -0.4% | +41.9% | $1.36 | +41.3% | 9.5M | 1.2M | 7.8x | 6.1M | Industrial Machinery |
| BIYA | [TV](https://www.tradingview.com/chart/?symbol=BIYA) | $1.36 | -2.5% | +67.0% | $2.28 | +62.9% | 9.3M | 2.6M | 3.6x | 2.7M | Personnel Services |
| MI | [TV](https://www.tradingview.com/chart/?symbol=MI) | $1.23 | -82.4% | +18.7% | $1.46 | -79.1% | 7.2M | 18.7M | 0.4x | 542K | Internet Software/Services |
| SXTC | [TV](https://www.tradingview.com/chart/?symbol=SXTC) | $1.25 | -39.9% | +54.4% | $1.93 | -7.2% | 6.4M | 1.2M | 5.2x | 1.0M | Pharmaceuticals: Major |
| XHLD | [TV](https://www.tradingview.com/chart/?symbol=XHLD) | $0.62 | +51.6% | +5.2% | $0.66 | +59.5% | 3.7M | 19.8M | 0.2x | 10.5M | Miscellaneous Commercial Services |
| WHLR | [TV](https://www.tradingview.com/chart/?symbol=WHLR) | $0.91 | -16.5% | +11.0% | $1.01 | -7.3% | 1.5M | 13.3M | 0.1x | 568K | Real Estate Investment Trusts |
| BURU | [TV](https://www.tradingview.com/chart/?symbol=BURU) | $1.20 | +7.1% | +13.3% | $1.36 | +21.4% | 1.3M | 1.7M | 0.8x | 8.4M | Electronic Components |
| LCFY | [TV](https://www.tradingview.com/chart/?symbol=LCFY) | $2.05 | -12.4% | +10.2% | $2.26 | -3.4% | 461K | 348K | 1.3x | 1.4M | Packaged Software |
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $1.09 | -17.4% | +26.1% | $1.38 | +4.2% | 258K | 14.3M | 0.0x | 4.4M | Miscellaneous Commercial Services |
| STEX | [TV](https://www.tradingview.com/chart/?symbol=STEX) | $0.52 | -12.7% | +6.4% | $0.55 | -7.2% | 210K | 1.1M | 0.2x | 105.3M | Investment Banks/Brokers |
| DCX | [TV](https://www.tradingview.com/chart/?symbol=DCX) | $3.11 | -8.0% | +7.7% | $3.35 | -0.9% | 158K | 552K | 0.3x | 259K | Motor Vehicles |
| FEAM | [TV](https://www.tradingview.com/chart/?symbol=FEAM) | $3.76 | -4.1% | +5.1% | $3.95 | +0.8% | 90K | 863K | 0.1x | 20.9M | Chemicals: Specialty |

### Evaluation notes

**Tradability:** BURU was re-verified `tradable=true` (AMEX, active) before the SIP and catalyst workup. The other >10% names were verified earlier tonight.

**New SIP bars** (`broker.js bars SYM --tf 5Min --start 2026-10-06T21:40:00Z --limit 1000`, feed=sip). The newest bar starts 18:15 ET, 15 minutes behind the scan, which matches the free-tier delay.

| Ticker | Bar ET | Open | High | Low | Close | Shares | VWAP | Trades |
|--------|--------|------|------|-----|-------|--------|------|--------|
| BURU | 17:55 | $1.25 | $1.25 | $1.25 | $1.25 | 1,168 | $1.25 | 12 |
| BURU | 18:00 | $1.25 | $1.51 | $1.25 | $1.48 | 148,338 | $1.39 | 549 |
| BURU | 18:05 | $1.48 | $1.54 | $1.38 | $1.40 | 745,287 | $1.45 | 3,910 |
| BURU | 18:10 | $1.40 | $1.41 | $1.30 | $1.36 | 297,953 | $1.35 | 1,699 |
| BURU | 18:15 | $1.36 | $1.40 | $1.31 | $1.35 | 169,829 | $1.36 | 885 |
| BIYA | 17:50 | $2.00 | $2.08 | $1.98 | $2.04 | 78,955 | $2.01 | 580 |
| BIYA | 17:55 | $2.04 | $2.15 | $2.03 | $2.12 | 159,587 | $2.08 | 919 |
| BIYA | 18:00 | $2.12 | $2.22 | $2.06 | $2.16 | 384,968 | $2.15 | 2,294 |
| BIYA | 18:05 | $2.16 | $2.18 | $2.06 | $2.13 | 146,383 | $2.12 | 1,087 |
| BIYA | 18:10 | $2.14 | $2.35 | $2.13 | $2.29 | 638,636 | $2.25 | 4,703 |
| BIYA | 18:15 | $2.30 | $2.39 | $2.25 | $2.34 | 460,625 | $2.32 | 3,438 |
| MTEN | 17:50 | $1.44 | $1.50 | $1.37 | $1.47 | 813,333 | $1.43 | 4,263 |
| MTEN | 17:55 | $1.48 | $1.49 | $1.35 | $1.35 | 734,449 | $1.40 | 3,897 |
| MTEN | 18:00 | $1.36 | $1.44 | $1.35 | $1.39 | 522,431 | $1.40 | 2,292 |
| MTEN | 18:05 | $1.38 | $1.40 | $1.33 | $1.39 | 369,491 | $1.36 | 1,851 |
| MTEN | 18:10 | $1.39 | $1.40 | $1.36 | $1.37 | 228,087 | $1.37 | 1,108 |
| MTEN | 18:15 | $1.37 | $1.52 | $1.34 | $1.49 | 739,281 | $1.45 | 3,135 |
| SXTC | 18:00 | $1.99 | $2.20 | $1.99 | $2.07 | 213,751 | $2.10 | 1,579 |
| SXTC | 18:05 | $2.06 | $2.09 | $1.98 | $1.99 | 87,783 | $2.03 | 603 |
| SXTC | 18:10 | $2.00 | $2.02 | $1.93 | $1.93 | 45,975 | $1.96 | 361 |
| SXTC | 18:15 | $1.95 | $1.99 | $1.93 | $1.97 | 36,807 | $1.95 | 236 |
| NCPL | 18:05 | $1.26 | $1.34 | $1.26 | $1.34 | 36,521 | $1.31 | 194 |
| NCPL | 18:10 | $1.34 | $1.39 | $1.31 | $1.37 | 50,963 | $1.35 | 323 |
| NCPL | 18:15 | $1.37 | $1.40 | $1.36 | $1.37 | 47,507 | $1.38 | 262 |

From 17:50 to 18:15 ET, MI printed 21,249–122,101 shares and 127–375 trades per bar at $1.37–$1.53 (18:15 close $1.38). WHLR printed 5,311–23,459 shares and 31–150 trades per bar at $0.98–$1.04. LCFY printed 2,487–7,627 shares and 28–57 trades per bar and slid from a $2.50 high at 17:50 to a $2.25 close at 18:15. NCPL had no 17:55 or 18:00 bar.

**Yahoo timeline (shape only, not volume or exact levels):**

| Ticker | 18:00 | 18:05 | 18:10 | 18:15 | 18:20 | 18:25 | 18:30 | 18:34 |
|--------|-------|-------|-------|-------|-------|-------|-------|-------|
| BURU | $1.48 | $1.40 | $1.36 | $1.35 | $1.40 | $1.37 | $1.43 | $1.44 |
| BIYA | $2.16 | $2.13 | $2.29 | $2.34 | $2.29 | $2.34 | $2.38 | $2.40 |
| MTEN | $1.38 | $1.39 | $1.37 | $1.49 | $1.47 | $1.48 | $1.48 | $1.49 |
| SXTC | $2.07 | $1.99 | $1.93 | $1.99 | $1.97 | $2.02 | $2.00 | $1.98 |
| NCPL | $1.27 | $1.34 | $1.38 | $1.38 | $1.38 | $1.39 | $1.41 | $1.38 |
| MI | $1.43 | $1.44 | $1.46 | $1.38 | $1.43 | $1.48 | $1.46 | $1.46 |
| WHLR | $1.02 | $0.99 | $1.02 | $1.03 | $1.03 | $1.03 | $1.02 | $1.00 (18:33) |
| LCFY | $2.43 | $2.39 | $2.26 | $2.25 | $2.22 | $2.28 | $2.28 | $2.28 (18:33) |

**BURU — first >10% AH appearance; no entry (2-AH-scan gate); not a FINAL-SCAN-GATE-BLOCK.**

- **Profile:** Nuburu, NYSE American, defense lasers. Day +7.1%, Total +21.4% at the scanner's $1.36 (prior close $1.12), float 8.4M. It appeared at 22:30 at +5.8%, below threshold.
- **SIP:** BURU traded flat at $1.21–$1.25 on under 10K shares per bar from 16:25 to 17:55 ET. It ignited at 18:00 ET (148,338 shares / 549 trades, high $1.51) and peaked at **$1.54** in the 18:05 bar on 745,287 shares and 3,910 trades. The next two bars closed at $1.36 and $1.35 while volume fell to 297,953 and then 169,829 shares, 77% below the 18:05 bar. Yahoo shows $1.43–$1.44 at 18:30–18:34 ET, about 7% below the SIP high.
- **SIP corroborates the scanner price:** the 18:15 bar's $1.35 close and $1.36 VWAP match the scanner's $1.36, so this is not a bad print.
- **Catalyst Grade C (financing restructuring); the driver is unconfirmed.** The [8-K accepted 2026-10-06 17:10:13 ET](https://www.sec.gov/Archives/edgar/data/1814215/000119312526415780/buru-20260930.htm) (acceptance time from `.hdr.sgml`) reports two agreements effective September 30, filed under Item 1.01. In the first, a side letter makes certain Series B preferred holders forfeit conversions priced below $0.10 per share and adds a monthly penalty if conversion shares are not registered on time. In the second, Nuburu returns 295,000 Heckler & Koch shares to Brick Lane in exchange for cancelling the $15M convertible note. The filing landed 50 minutes before the 18:00 ET ignition, so it may not be the driver. Background only: a September 22 BusinessWire PR targeted closing the 70% Tekne acquisition in the first week of October, and four searches found no closing announcement. A 1-for-40 reverse split took effect on September 1.
- **Activity history:** SIP daily volume ran 488K–4.1M shares from September 28 to October 5, while the price climbed from $0.94 to $1.12. Today printed 3.2M shares. BURU has no `WINNERS_TRACKING.md` entry.
- **Why this is not a FINAL-SCAN-GATE-BLOCK:** the rule requires CONFIRM-3 YES on accumulating volume, and BURU reads NO with shrinking per-bar volume. The book is also unverified. The IEX quote is frozen at 16:00:00 ET ($1.01 / $1.35 x100), and `book-check.js` returned a delayed SIP quote dated 2026-07-17 at $0.0726 (a pre-split price), so that row says nothing about tonight's book.
- **Reference price for the morning tally:** $1.36 (scanner) at 18:30 ET, Total +21.4%.

**BIYA — `already entered` (52 @ $1.91); tracking only.** SIP made a new high of **$2.39** in the 18:15 bar after a 638,636-share, 4,703-trade push at 18:10. Yahoo shows $2.40 at 18:34. `broker.js positions` marks it at $2.36, **+$23.40 (+23.6%)**. CONFIRM-3 stays YES.

**MTEN — `already entered` (70 @ $1.39); tracking only.** The 17:55–18:10 bars pulled back to $1.33–$1.40 on 228K–734K shares, then the 18:15 bar re-expanded to a $1.52 high and a $1.49 close on 739,281 shares and 3,135 trades. The high is still the $1.59 from 17:40 ET. `broker.js positions` marks it at $1.48, **+$6.30 (+6.5%)**. The scanner's $1.36 lags the tape by about 30 minutes.

**SXTC — eighth qualifying AH scan; skip live entry (Day -39.9%); DEAD-CAT-OVERRIDE WATCH continues.** The 18:00 bar popped to $2.20 on 213,751 shares, then three bars faded to a $1.93–$1.97 close on 36,807–87,783 shares. Yahoo shows $1.98–$2.02, back near the $2.08 prior close and about 25% below the $2.58 AH high. The 22:25 hypothetical ($1.57 at 16:25 ET) stands.

**NCPL — sixth >10% AH appearance; skip stands (Day -17.4%, thin volume); no DEAD-CAT-OVERRIDE WATCH.** On price, NCPL now fits the watch conditions. AH change rose from +14.7% to +26.1%, the SIP high of $1.40 at 18:15 tops the $1.28 opening high, Total% turned positive (+4.2%), and CONFIRM-3 flipped to YES on an 18:05 ignition. Volume is still thin: 36,521–50,963 shares and 194–323 trades per bar, with VRatio 0.0x, below the accumulation rule. That keeps the 00:00 decision for WHLR and NCPL: thin drifts do not enter the watch sample. Reference price for the morning tally: $1.38 (scanner) at 18:30 ET. Grade None.

**MI — fifth >10% AH appearance; skip (dead-cat bounce, Grade D).** AH change bounced from +12.2% to +18.7% ($1.46), but SIP stayed at $1.37–$1.53 on 21K–122K shares per bar. That is 21% below the $1.84 high, and AH% has risen in only one scan.

**WHLR — third >10% AH appearance; skip (Day -16.5%, thin drift).** AH change fell from +14.3% to +11.0% ($1.01) on 5,311–23,459 shares per bar. The 00:00 reference price ($1.04 at 18:00 ET) stands.

**LCFY — third >10% AH appearance; skip (thin drift, fading).** AH change fell from +18.6% to +10.2% ($2.26). SIP printed 2,487–7,627 shares per bar and closed at $2.25 at 18:15, 14% below the $2.62 high from 16:35 ET.

**VCIG** is absent from this scan. Yahoo shows $0.97 at 18:31 ET, 31% below the $1.41 SIP close. Its SPIKE→FADE skip and the 22:20 FIRST-BAR-SPIKE WATCH hypothetical ($1.69 at 16:20 ET) stand.

**Below threshold:** XHLD (+5.2%), DCX (+7.7%), STEX (+6.4%), and FEAM (+5.1%) are tracked only.

**Final-scan feed-lag cross-check:** I checked every tracked name against dated SIP closes and the Yahoo AH timeline (`check-prices.py --ah-history --date 2026-10-06`). For names near the threshold, I also pulled SIP 5-minute bars. No tracked name sits above +10% while missing from, or under-reported by, the scanner.

- **AH names from earlier scans:** LHSW $0.56 (-1.1%), ICMB $0.75 (+3.8%, last print 16:57 ET), and YFOR $1.03 (-8.8%) are all below threshold.
- **OLOX:** SIP from 17:50 to 18:15 ET traded $1.27–$1.36 on 23K–104K shares per bar, +2% to +9% over the $1.25 close; Yahoo shows $1.33 (+6.4%) at 18:31. It is absent from this scan and below threshold.
- **21:30 watchlist:** JAGX +5.0%, AIFA +2.6%, PMI +1.1%, MODD +0.7%, OFS +0.5%, AIIO 0.0%, ARKR 0.0%, HUHU -0.1%, SMXT -0.3%, IPDN -0.9%, APUS -1.8%, DLXY -3.3%, KAPA -4.3%, FFR -4.3%, RUBI -5.2% (against the $0.6541 SIP close), BESS -5.7%, and MOBX -7.1%. JONE, XSLL, and APMC show no AH prints after 16:10 ET.
- **Untradable (carried, not rechecked):** EVOL, MHUAF, VNPKF, WTLLF, NWINF, and KHDHF.

**Instrumentation (verbatim; log-only):**

```text
BIYA 2026-10-06  SPIKE  16:08ET  +21%  $1.65  372 trades / 58k sh  (first co-spike bar) (as-of 18:30ET)
BIYA 2026-10-06  CONFIRM-3  YES ignition 16:05ET 260.8x; confirmed 16:15ET $1.81 as-of 18:30ET
BURU 2026-10-06  SPIKE  18:04ET  +26%  $1.51  396 trades / 95k sh  (first co-spike bar) (as-of 18:30ET)
BURU 2026-10-06  CONFIRM-3  NO ignition 18:00ET failed third-bar hold/volume as-of 18:30ET
LCFY 2026-10-06  NO-SPIKE  peak +28% @16:38ET  (no bar cleared +15% on a volume co-spike) (as-of 18:30ET)
LCFY 2026-10-06  CONFIRM-3  NO ignition 16:35ET failed third-bar hold/volume as-of 18:30ET
MI 2026-10-06  SPIKE  16:18ET  +30%  $1.60  2066 trades / 421k sh  (first co-spike bar) (as-of 18:30ET)
MI 2026-10-06  CONFIRM-3  NO ignition 16:15ET failed third-bar hold/volume as-of 18:30ET
MTEN 2026-10-06  SPIKE  16:41ET  +22%  $1.17  637 trades / 143k sh  (first co-spike bar) (as-of 18:30ET)
MTEN 2026-10-06  CONFIRM-3  NO ignition 16:30ET failed third-bar hold/volume as-of 18:30ET
NCPL 2026-10-06  SPIKE  18:05ET  +20%  $1.31  43 trades / 10k sh  (first co-spike bar) (as-of 18:30ET)
NCPL 2026-10-06  CONFIRM-3  YES ignition 18:05ET 15.9x; confirmed 18:15ET $1.37 as-of 18:30ET
SXTC 2026-10-06  SPIKE  16:03ET  +32%  $1.65  135 trades / 30k sh  (first co-spike bar) (as-of 18:30ET)
SXTC 2026-10-06  CONFIRM-3  NO ignition 16:05ET failed third-bar hold/volume as-of 18:30ET
WHLR 2026-10-06  SPIKE  16:46ET  +16%  $1.06  110 trades / 34k sh  (first co-spike bar) (as-of 18:30ET)
WHLR 2026-10-06  CONFIRM-3  NO ignition 16:45ET failed third-bar hold/volume as-of 18:30ET
```

**Shared SIP volume context (`sip-ah-volume-v1`, log-only):** The prior trading date is 2026-10-05, a normal Monday session. Inputs were fetched with `broker.js bars SYM --tf 5Min --start 2026-10-05T20:00:00Z --limit 1000 --feed sip --json` (one page each, no next-page token). They are archived as `log/2026-10-06/SYM-0030-volume-sip.json`, with computed rows in `SYM-0030-volume-metric.json`, for all eight `tradable=true` >10% names. MI and WHLR have complete prior-session coverage (48/48). The others stay incomplete (BURU 37/48, NCPL 25/48, BIYA 18/48, SXTC 10/48, MTEN 5/48, LCFY 1/48), so their prior-peak ratios remain unknown. BURU's 18:05 bar reads 378.51x local. BURU's September 1 reverse split precedes both sessions. The SXTC share-consolidation headline, BIYA's July 1-for-10 reverse split, and WHLR's September 21 1-for-9 reverse split remain unreviewed against this window.

```text
# BIYA shared SIP volume; prior 2026-10-05 18/48 slots; log-only
# reconstructed as-of 2026-10-06T22:30:09+00:00; source fetched 2026-10-06T22:32:27.938233Z
BIYA 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=1095 local=unknown prior-peak=unknown status=warmup
BIYA 2026-10-06  VOLUME-CONTEXT 16:05ET start=2026-10-06T20:05:00+00:00 shares=285556 local=unknown prior-peak=unknown status=warmup
BIYA 2026-10-06  VOLUME-CONTEXT 16:10ET start=2026-10-06T20:10:00+00:00 shares=1072394 local=unknown prior-peak=unknown status=warmup
BIYA 2026-10-06  VOLUME-CONTEXT 16:15ET start=2026-10-06T20:15:00+00:00 shares=1596650 local=5.5914x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 16:20ET start=2026-10-06T20:20:00+00:00 shares=550815 local=0.5136x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 16:25ET start=2026-10-06T20:25:00+00:00 shares=307657 local=0.2869x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 16:30ET start=2026-10-06T20:30:00+00:00 shares=452655 local=0.8218x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 16:35ET start=2026-10-06T20:35:00+00:00 shares=413407 local=0.9133x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 16:40ET start=2026-10-06T20:40:00+00:00 shares=802489 local=1.9412x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 16:45ET start=2026-10-06T20:45:00+00:00 shares=347463 local=0.7676x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 16:50ET start=2026-10-06T20:50:00+00:00 shares=242874 local=0.5875x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 16:55ET start=2026-10-06T20:55:00+00:00 shares=152538 local=0.4390x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 17:00ET start=2026-10-06T21:00:00+00:00 shares=248222 local=1.0220x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 17:05ET start=2026-10-06T21:05:00+00:00 shares=633569 local=2.6086x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 17:10ET start=2026-10-06T21:10:00+00:00 shares=155877 local=0.6280x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 17:15ET start=2026-10-06T21:15:00+00:00 shares=131059 local=0.5280x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 17:20ET start=2026-10-06T21:20:00+00:00 shares=110912 local=0.7115x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 17:25ET start=2026-10-06T21:25:00+00:00 shares=502588 local=3.8348x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 17:30ET start=2026-10-06T21:30:00+00:00 shares=662827 local=5.0575x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 17:35ET start=2026-10-06T21:35:00+00:00 shares=370276 local=0.7367x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 17:40ET start=2026-10-06T21:40:00+00:00 shares=151300 local=0.3010x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 17:45ET start=2026-10-06T21:45:00+00:00 shares=125390 local=0.3386x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 17:50ET start=2026-10-06T21:50:00+00:00 shares=78955 local=0.5218x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 17:55ET start=2026-10-06T21:55:00+00:00 shares=159587 local=1.2727x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 18:00ET start=2026-10-06T22:00:00+00:00 shares=384968 local=3.0702x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 18:05ET start=2026-10-06T22:05:00+00:00 shares=146383 local=0.9173x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 18:10ET start=2026-10-06T22:10:00+00:00 shares=638636 local=4.0018x prior-peak=unknown status=ok
BIYA 2026-10-06  VOLUME-CONTEXT 18:15ET start=2026-10-06T22:15:00+00:00 shares=460625 local=1.1965x prior-peak=unknown status=ok
# BURU shared SIP volume; prior 2026-10-05 37/48 slots; log-only
# reconstructed as-of 2026-10-06T22:30:09+00:00; source fetched 2026-10-06T22:32:28.539019Z
BURU 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=6313 local=unknown prior-peak=unknown status=warmup
BURU 2026-10-06  VOLUME-CONTEXT 16:05ET start=2026-10-06T20:05:00+00:00 shares=887 local=unknown prior-peak=unknown status=warmup
BURU 2026-10-06  VOLUME-CONTEXT 16:10ET start=2026-10-06T20:10:00+00:00 shares=114004 local=unknown prior-peak=unknown status=warmup
BURU 2026-10-06  VOLUME-CONTEXT 16:15ET start=2026-10-06T20:15:00+00:00 shares=75845 local=12.0141x prior-peak=unknown status=ok
BURU 2026-10-06  VOLUME-CONTEXT 16:20ET start=2026-10-06T20:20:00+00:00 shares=39438 local=0.5200x prior-peak=unknown status=ok
BURU 2026-10-06  VOLUME-CONTEXT 16:25ET start=2026-10-06T20:25:00+00:00 shares=9181 local=0.1210x prior-peak=unknown status=ok
BURU 2026-10-06  VOLUME-CONTEXT 16:30ET start=2026-10-06T20:30:00+00:00 shares=10984 local=0.2785x prior-peak=unknown status=ok
BURU 2026-10-06  VOLUME-CONTEXT 16:35ET start=2026-10-06T20:35:00+00:00 shares=2007 local=0.1827x prior-peak=unknown status=ok
BURU 2026-10-06  VOLUME-CONTEXT 16:40ET start=2026-10-06T20:40:00+00:00 shares=5517 local=0.6009x prior-peak=unknown status=ok
BURU 2026-10-06  VOLUME-CONTEXT 16:45ET start=2026-10-06T20:45:00+00:00 shares=3769 local=0.6832x prior-peak=unknown status=ok
BURU 2026-10-06  VOLUME-CONTEXT 16:50ET start=2026-10-06T20:50:00+00:00 shares=1447 local=0.3839x prior-peak=unknown status=ok
BURU 2026-10-06  VOLUME-CONTEXT 16:55ET start=2026-10-06T20:55:00+00:00 shares=658 local=0.1746x prior-peak=unknown status=ok
BURU 2026-10-06  VOLUME-CONTEXT 17:00ET start=2026-10-06T21:00:00+00:00 shares=9885 local=6.8314x prior-peak=unknown status=ok
BURU 2026-10-06  VOLUME-CONTEXT 17:05ET start=2026-10-06T21:05:00+00:00 shares=931 local=0.6434x prior-peak=unknown status=ok
BURU 2026-10-06  VOLUME-CONTEXT 17:10ET start=2026-10-06T21:10:00+00:00 shares=2025 local=2.1751x prior-peak=unknown status=ok
BURU 2026-10-06  VOLUME-CONTEXT 17:15ET start=2026-10-06T21:15:00+00:00 shares=1044 local=0.5156x prior-peak=unknown status=ok
BURU 2026-10-06  VOLUME-CONTEXT 17:20ET start=2026-10-06T21:20:00+00:00 shares=783 local=0.7500x prior-peak=unknown status=ok
BURU 2026-10-06  VOLUME-CONTEXT 17:25ET start=2026-10-06T21:25:00+00:00 shares=1066 local=1.0211x prior-peak=unknown status=ok
BURU 2026-10-06  VOLUME-CONTEXT 17:30ET start=2026-10-06T21:30:00+00:00 shares=302 local=0.2893x prior-peak=unknown status=ok
BURU 2026-10-06  VOLUME-CONTEXT 17:35ET start=2026-10-06T21:35:00+00:00 shares=1692 local=2.1609x prior-peak=unknown status=ok
BURU 2026-10-06  VOLUME-CONTEXT 17:40ET start=2026-10-06T21:40:00+00:00 shares=966 local=0.9062x prior-peak=unknown status=ok
BURU 2026-10-06  VOLUME-CONTEXT 17:45ET start=2026-10-06T21:45:00+00:00 shares=8855 local=9.1667x prior-peak=unknown status=ok
BURU 2026-10-06  VOLUME-CONTEXT 17:50ET start=2026-10-06T21:50:00+00:00 shares=1969 local=1.1637x prior-peak=unknown status=ok
BURU 2026-10-06  VOLUME-CONTEXT 17:55ET start=2026-10-06T21:55:00+00:00 shares=1168 local=0.5932x prior-peak=unknown status=ok
BURU 2026-10-06  VOLUME-CONTEXT 18:00ET start=2026-10-06T22:00:00+00:00 shares=148338 local=75.3367x prior-peak=unknown status=ok
BURU 2026-10-06  VOLUME-CONTEXT 18:05ET start=2026-10-06T22:05:00+00:00 shares=745287 local=378.5104x prior-peak=unknown status=ok
BURU 2026-10-06  VOLUME-CONTEXT 18:10ET start=2026-10-06T22:10:00+00:00 shares=297953 local=2.0086x prior-peak=unknown status=ok
BURU 2026-10-06  VOLUME-CONTEXT 18:15ET start=2026-10-06T22:15:00+00:00 shares=169829 local=0.5700x prior-peak=unknown status=ok
# LCFY shared SIP volume; prior 2026-10-05 1/48 slots; log-only
# reconstructed as-of 2026-10-06T22:30:09+00:00; source fetched 2026-10-06T22:32:29.160686Z
LCFY 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=5907 local=unknown prior-peak=unknown status=warmup
LCFY 2026-10-06  VOLUME-CONTEXT 16:15ET start=2026-10-06T20:15:00+00:00 shares=411 local=unknown prior-peak=unknown status=missing-baseline
LCFY 2026-10-06  VOLUME-CONTEXT 16:20ET start=2026-10-06T20:20:00+00:00 shares=3627 local=unknown prior-peak=unknown status=missing-baseline
LCFY 2026-10-06  VOLUME-CONTEXT 16:25ET start=2026-10-06T20:25:00+00:00 shares=677 local=unknown prior-peak=unknown status=missing-baseline
LCFY 2026-10-06  VOLUME-CONTEXT 16:30ET start=2026-10-06T20:30:00+00:00 shares=1468 local=2.1684x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 16:35ET start=2026-10-06T20:35:00+00:00 shares=103702 local=70.6417x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 16:40ET start=2026-10-06T20:40:00+00:00 shares=161504 local=110.0163x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 16:45ET start=2026-10-06T20:45:00+00:00 shares=39640 local=0.3822x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 16:50ET start=2026-10-06T20:50:00+00:00 shares=24367 local=0.2350x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 16:55ET start=2026-10-06T20:55:00+00:00 shares=13202 local=0.3330x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 17:00ET start=2026-10-06T21:00:00+00:00 shares=55564 local=2.2803x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 17:05ET start=2026-10-06T21:05:00+00:00 shares=23480 local=0.9636x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 17:10ET start=2026-10-06T21:10:00+00:00 shares=23553 local=1.0031x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 17:15ET start=2026-10-06T21:15:00+00:00 shares=13446 local=0.5709x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 17:20ET start=2026-10-06T21:20:00+00:00 shares=7187 local=0.3061x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 17:25ET start=2026-10-06T21:25:00+00:00 shares=2983 local=0.2219x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 17:30ET start=2026-10-06T21:30:00+00:00 shares=27230 local=3.7888x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 17:35ET start=2026-10-06T21:35:00+00:00 shares=10004 local=1.3920x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 17:40ET start=2026-10-06T21:40:00+00:00 shares=2072 local=0.2071x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 17:45ET start=2026-10-06T21:45:00+00:00 shares=1561 local=0.1560x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 17:50ET start=2026-10-06T21:50:00+00:00 shares=7627 local=3.6810x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 17:55ET start=2026-10-06T21:55:00+00:00 shares=7108 local=3.4305x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 18:00ET start=2026-10-06T22:00:00+00:00 shares=2487 local=0.3499x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 18:05ET start=2026-10-06T22:05:00+00:00 shares=5625 local=0.7914x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 18:10ET start=2026-10-06T22:10:00+00:00 shares=7080 local=1.2587x prior-peak=unknown status=ok
LCFY 2026-10-06  VOLUME-CONTEXT 18:15ET start=2026-10-06T22:15:00+00:00 shares=3881 local=0.6900x prior-peak=unknown status=ok
# MI shared SIP volume; prior 2026-10-05 48/48 slots; log-only
# reconstructed as-of 2026-10-06T22:30:09+00:00; source fetched 2026-10-06T22:32:29.776718Z
MI 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=220361 local=unknown prior-peak=0.2093x status=warmup
MI 2026-10-06  VOLUME-CONTEXT 16:05ET start=2026-10-06T20:05:00+00:00 shares=137355 local=unknown prior-peak=0.1304x status=warmup
MI 2026-10-06  VOLUME-CONTEXT 16:10ET start=2026-10-06T20:10:00+00:00 shares=159195 local=unknown prior-peak=0.1512x status=warmup
MI 2026-10-06  VOLUME-CONTEXT 16:15ET start=2026-10-06T20:15:00+00:00 shares=1263614 local=7.9375x prior-peak=1.2000x status=ok
MI 2026-10-06  VOLUME-CONTEXT 16:20ET start=2026-10-06T20:20:00+00:00 shares=2036291 local=12.7912x prior-peak=1.9338x status=ok
MI 2026-10-06  VOLUME-CONTEXT 16:25ET start=2026-10-06T20:25:00+00:00 shares=868347 local=0.6872x prior-peak=0.8246x status=ok
MI 2026-10-06  VOLUME-CONTEXT 16:30ET start=2026-10-06T20:30:00+00:00 shares=427999 local=0.3387x prior-peak=0.4064x status=ok
MI 2026-10-06  VOLUME-CONTEXT 16:35ET start=2026-10-06T20:35:00+00:00 shares=400416 local=0.4611x prior-peak=0.3803x status=ok
MI 2026-10-06  VOLUME-CONTEXT 16:40ET start=2026-10-06T20:40:00+00:00 shares=214703 local=0.5016x prior-peak=0.2039x status=ok
MI 2026-10-06  VOLUME-CONTEXT 16:45ET start=2026-10-06T20:45:00+00:00 shares=461613 local=1.1528x prior-peak=0.4384x status=ok
MI 2026-10-06  VOLUME-CONTEXT 16:50ET start=2026-10-06T20:50:00+00:00 shares=288180 local=0.7197x prior-peak=0.2737x status=ok
MI 2026-10-06  VOLUME-CONTEXT 16:55ET start=2026-10-06T20:55:00+00:00 shares=181642 local=0.6303x prior-peak=0.1725x status=ok
MI 2026-10-06  VOLUME-CONTEXT 17:00ET start=2026-10-06T21:00:00+00:00 shares=90521 local=0.3141x prior-peak=0.0860x status=ok
MI 2026-10-06  VOLUME-CONTEXT 17:05ET start=2026-10-06T21:05:00+00:00 shares=140158 local=0.7716x prior-peak=0.1331x status=ok
MI 2026-10-06  VOLUME-CONTEXT 17:10ET start=2026-10-06T21:10:00+00:00 shares=74036 local=0.5282x prior-peak=0.0703x status=ok
MI 2026-10-06  VOLUME-CONTEXT 17:15ET start=2026-10-06T21:15:00+00:00 shares=63034 local=0.6963x prior-peak=0.0599x status=ok
MI 2026-10-06  VOLUME-CONTEXT 17:20ET start=2026-10-06T21:20:00+00:00 shares=30822 local=0.4163x prior-peak=0.0293x status=ok
MI 2026-10-06  VOLUME-CONTEXT 17:25ET start=2026-10-06T21:25:00+00:00 shares=68471 local=1.0863x prior-peak=0.0650x status=ok
MI 2026-10-06  VOLUME-CONTEXT 17:30ET start=2026-10-06T21:30:00+00:00 shares=74194 local=1.1770x prior-peak=0.0705x status=ok
MI 2026-10-06  VOLUME-CONTEXT 17:35ET start=2026-10-06T21:35:00+00:00 shares=69043 local=1.0084x prior-peak=0.0656x status=ok
MI 2026-10-06  VOLUME-CONTEXT 17:40ET start=2026-10-06T21:40:00+00:00 shares=103922 local=1.5052x prior-peak=0.0987x status=ok
MI 2026-10-06  VOLUME-CONTEXT 17:45ET start=2026-10-06T21:45:00+00:00 shares=137959 local=1.8594x prior-peak=0.1310x status=ok
MI 2026-10-06  VOLUME-CONTEXT 17:50ET start=2026-10-06T21:50:00+00:00 shares=122101 local=1.1749x prior-peak=0.1160x status=ok
MI 2026-10-06  VOLUME-CONTEXT 17:55ET start=2026-10-06T21:55:00+00:00 shares=40452 local=0.3313x prior-peak=0.0384x status=ok
MI 2026-10-06  VOLUME-CONTEXT 18:00ET start=2026-10-06T22:00:00+00:00 shares=86486 local=0.7083x prior-peak=0.0821x status=ok
MI 2026-10-06  VOLUME-CONTEXT 18:05ET start=2026-10-06T22:05:00+00:00 shares=38515 local=0.4453x prior-peak=0.0366x status=ok
MI 2026-10-06  VOLUME-CONTEXT 18:10ET start=2026-10-06T22:10:00+00:00 shares=21249 local=0.5253x prior-peak=0.0202x status=ok
MI 2026-10-06  VOLUME-CONTEXT 18:15ET start=2026-10-06T22:15:00+00:00 shares=59207 local=1.5372x prior-peak=0.0562x status=ok
# MTEN shared SIP volume; prior 2026-10-05 5/48 slots; log-only
# reconstructed as-of 2026-10-06T22:30:09+00:00; source fetched 2026-10-06T22:32:30.422989Z
MTEN 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=652 local=unknown prior-peak=unknown status=warmup
MTEN 2026-10-06  VOLUME-CONTEXT 16:30ET start=2026-10-06T20:30:00+00:00 shares=152894 local=unknown prior-peak=unknown status=missing-baseline
MTEN 2026-10-06  VOLUME-CONTEXT 16:35ET start=2026-10-06T20:35:00+00:00 shares=170255 local=unknown prior-peak=unknown status=missing-baseline
MTEN 2026-10-06  VOLUME-CONTEXT 16:40ET start=2026-10-06T20:40:00+00:00 shares=478591 local=unknown prior-peak=unknown status=missing-baseline
MTEN 2026-10-06  VOLUME-CONTEXT 16:45ET start=2026-10-06T20:45:00+00:00 shares=166035 local=0.9752x prior-peak=unknown status=ok
MTEN 2026-10-06  VOLUME-CONTEXT 16:50ET start=2026-10-06T20:50:00+00:00 shares=25301 local=0.1486x prior-peak=unknown status=ok
MTEN 2026-10-06  VOLUME-CONTEXT 16:55ET start=2026-10-06T20:55:00+00:00 shares=12949 local=0.0780x prior-peak=unknown status=ok
MTEN 2026-10-06  VOLUME-CONTEXT 17:00ET start=2026-10-06T21:00:00+00:00 shares=33587 local=1.3275x prior-peak=unknown status=ok
MTEN 2026-10-06  VOLUME-CONTEXT 17:05ET start=2026-10-06T21:05:00+00:00 shares=36447 local=1.4405x prior-peak=unknown status=ok
MTEN 2026-10-06  VOLUME-CONTEXT 17:10ET start=2026-10-06T21:10:00+00:00 shares=18168 local=0.5409x prior-peak=unknown status=ok
MTEN 2026-10-06  VOLUME-CONTEXT 17:15ET start=2026-10-06T21:15:00+00:00 shares=969962 local=28.8791x prior-peak=unknown status=ok
MTEN 2026-10-06  VOLUME-CONTEXT 17:20ET start=2026-10-06T21:20:00+00:00 shares=1188203 local=32.6008x prior-peak=unknown status=ok
MTEN 2026-10-06  VOLUME-CONTEXT 17:25ET start=2026-10-06T21:25:00+00:00 shares=711200 local=0.7332x prior-peak=unknown status=ok
MTEN 2026-10-06  VOLUME-CONTEXT 17:30ET start=2026-10-06T21:30:00+00:00 shares=952125 local=0.9816x prior-peak=unknown status=ok
MTEN 2026-10-06  VOLUME-CONTEXT 17:35ET start=2026-10-06T21:35:00+00:00 shares=1017234 local=1.0684x prior-peak=unknown status=ok
MTEN 2026-10-06  VOLUME-CONTEXT 17:40ET start=2026-10-06T21:40:00+00:00 shares=1476192 local=1.5504x prior-peak=unknown status=ok
MTEN 2026-10-06  VOLUME-CONTEXT 17:45ET start=2026-10-06T21:45:00+00:00 shares=743161 local=0.7306x prior-peak=unknown status=ok
MTEN 2026-10-06  VOLUME-CONTEXT 17:50ET start=2026-10-06T21:50:00+00:00 shares=813333 local=0.7996x prior-peak=unknown status=ok
MTEN 2026-10-06  VOLUME-CONTEXT 17:55ET start=2026-10-06T21:55:00+00:00 shares=734449 local=0.9030x prior-peak=unknown status=ok
MTEN 2026-10-06  VOLUME-CONTEXT 18:00ET start=2026-10-06T22:00:00+00:00 shares=522431 local=0.7030x prior-peak=unknown status=ok
MTEN 2026-10-06  VOLUME-CONTEXT 18:05ET start=2026-10-06T22:05:00+00:00 shares=369491 local=0.5031x prior-peak=unknown status=ok
MTEN 2026-10-06  VOLUME-CONTEXT 18:10ET start=2026-10-06T22:10:00+00:00 shares=228087 local=0.4366x prior-peak=unknown status=ok
MTEN 2026-10-06  VOLUME-CONTEXT 18:15ET start=2026-10-06T22:15:00+00:00 shares=739281 local=2.0008x prior-peak=unknown status=ok
# NCPL shared SIP volume; prior 2026-10-05 25/48 slots; log-only
# reconstructed as-of 2026-10-06T22:30:09+00:00; source fetched 2026-10-06T22:32:31.032815Z
NCPL 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=71987 local=unknown prior-peak=unknown status=warmup
NCPL 2026-10-06  VOLUME-CONTEXT 16:05ET start=2026-10-06T20:05:00+00:00 shares=71440 local=unknown prior-peak=unknown status=warmup
NCPL 2026-10-06  VOLUME-CONTEXT 16:10ET start=2026-10-06T20:10:00+00:00 shares=7284 local=unknown prior-peak=unknown status=warmup
NCPL 2026-10-06  VOLUME-CONTEXT 16:15ET start=2026-10-06T20:15:00+00:00 shares=4790 local=0.0670x prior-peak=unknown status=ok
NCPL 2026-10-06  VOLUME-CONTEXT 16:20ET start=2026-10-06T20:20:00+00:00 shares=1020 local=0.1400x prior-peak=unknown status=ok
NCPL 2026-10-06  VOLUME-CONTEXT 16:25ET start=2026-10-06T20:25:00+00:00 shares=7199 local=1.5029x prior-peak=unknown status=ok
NCPL 2026-10-06  VOLUME-CONTEXT 16:30ET start=2026-10-06T20:30:00+00:00 shares=234 local=0.0489x prior-peak=unknown status=ok
NCPL 2026-10-06  VOLUME-CONTEXT 16:35ET start=2026-10-06T20:35:00+00:00 shares=1540 local=1.5098x prior-peak=unknown status=ok
NCPL 2026-10-06  VOLUME-CONTEXT 16:40ET start=2026-10-06T20:40:00+00:00 shares=1404 local=0.9117x prior-peak=unknown status=ok
NCPL 2026-10-06  VOLUME-CONTEXT 16:45ET start=2026-10-06T20:45:00+00:00 shares=175 local=0.1246x prior-peak=unknown status=ok
NCPL 2026-10-06  VOLUME-CONTEXT 16:50ET start=2026-10-06T20:50:00+00:00 shares=240 local=0.1709x prior-peak=unknown status=ok
NCPL 2026-10-06  VOLUME-CONTEXT 17:00ET start=2026-10-06T21:00:00+00:00 shares=1760 local=unknown prior-peak=unknown status=missing-baseline
NCPL 2026-10-06  VOLUME-CONTEXT 17:05ET start=2026-10-06T21:05:00+00:00 shares=340 local=unknown prior-peak=unknown status=missing-baseline
NCPL 2026-10-06  VOLUME-CONTEXT 17:15ET start=2026-10-06T21:15:00+00:00 shares=1000 local=unknown prior-peak=unknown status=missing-baseline
NCPL 2026-10-06  VOLUME-CONTEXT 17:20ET start=2026-10-06T21:20:00+00:00 shares=457 local=unknown prior-peak=unknown status=missing-baseline
NCPL 2026-10-06  VOLUME-CONTEXT 17:25ET start=2026-10-06T21:25:00+00:00 shares=1104 local=unknown prior-peak=unknown status=missing-baseline
NCPL 2026-10-06  VOLUME-CONTEXT 17:35ET start=2026-10-06T21:35:00+00:00 shares=17274 local=unknown prior-peak=unknown status=missing-baseline
NCPL 2026-10-06  VOLUME-CONTEXT 17:40ET start=2026-10-06T21:40:00+00:00 shares=2298 local=unknown prior-peak=unknown status=missing-baseline
NCPL 2026-10-06  VOLUME-CONTEXT 17:45ET start=2026-10-06T21:45:00+00:00 shares=2315 local=unknown prior-peak=unknown status=missing-baseline
NCPL 2026-10-06  VOLUME-CONTEXT 17:50ET start=2026-10-06T21:50:00+00:00 shares=423 local=0.1827x prior-peak=unknown status=ok
NCPL 2026-10-06  VOLUME-CONTEXT 18:05ET start=2026-10-06T22:05:00+00:00 shares=36521 local=unknown prior-peak=unknown status=missing-baseline
NCPL 2026-10-06  VOLUME-CONTEXT 18:10ET start=2026-10-06T22:10:00+00:00 shares=50963 local=unknown prior-peak=unknown status=missing-baseline
NCPL 2026-10-06  VOLUME-CONTEXT 18:15ET start=2026-10-06T22:15:00+00:00 shares=47507 local=unknown prior-peak=unknown status=missing-baseline
# SXTC shared SIP volume; prior 2026-10-05 10/48 slots; log-only
# reconstructed as-of 2026-10-06T22:30:09+00:00; source fetched 2026-10-06T22:32:31.631191Z
SXTC 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=75597 local=unknown prior-peak=unknown status=warmup
SXTC 2026-10-06  VOLUME-CONTEXT 16:05ET start=2026-10-06T20:05:00+00:00 shares=683755 local=unknown prior-peak=unknown status=warmup
SXTC 2026-10-06  VOLUME-CONTEXT 16:10ET start=2026-10-06T20:10:00+00:00 shares=212492 local=unknown prior-peak=unknown status=warmup
SXTC 2026-10-06  VOLUME-CONTEXT 16:15ET start=2026-10-06T20:15:00+00:00 shares=103774 local=0.4884x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 16:20ET start=2026-10-06T20:20:00+00:00 shares=295399 local=1.3902x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 16:25ET start=2026-10-06T20:25:00+00:00 shares=394574 local=1.8569x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 16:30ET start=2026-10-06T20:30:00+00:00 shares=1344735 local=4.5523x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 16:35ET start=2026-10-06T20:35:00+00:00 shares=563974 local=1.4293x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 16:40ET start=2026-10-06T20:40:00+00:00 shares=508099 local=0.9009x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 16:45ET start=2026-10-06T20:45:00+00:00 shares=865653 local=1.5349x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 16:50ET start=2026-10-06T20:50:00+00:00 shares=407217 local=0.7220x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 16:55ET start=2026-10-06T20:55:00+00:00 shares=329554 local=0.6486x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 17:00ET start=2026-10-06T21:00:00+00:00 shares=138698 local=0.3406x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 17:05ET start=2026-10-06T21:05:00+00:00 shares=243462 local=0.7388x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 17:10ET start=2026-10-06T21:10:00+00:00 shares=110255 local=0.4529x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 17:15ET start=2026-10-06T21:15:00+00:00 shares=302849 local=2.1835x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 17:20ET start=2026-10-06T21:20:00+00:00 shares=149611 local=0.6145x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 17:25ET start=2026-10-06T21:25:00+00:00 shares=118758 local=0.7938x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 17:30ET start=2026-10-06T21:30:00+00:00 shares=126365 local=0.8446x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 17:35ET start=2026-10-06T21:35:00+00:00 shares=71986 local=0.5697x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 17:40ET start=2026-10-06T21:40:00+00:00 shares=43870 local=0.3694x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 17:45ET start=2026-10-06T21:45:00+00:00 shares=54064 local=0.7510x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 17:50ET start=2026-10-06T21:50:00+00:00 shares=51712 local=0.9565x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 17:55ET start=2026-10-06T21:55:00+00:00 shares=30898 local=0.5975x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 18:00ET start=2026-10-06T22:00:00+00:00 shares=213751 local=4.1335x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 18:05ET start=2026-10-06T22:05:00+00:00 shares=87783 local=1.6975x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 18:10ET start=2026-10-06T22:10:00+00:00 shares=45975 local=0.5237x prior-peak=unknown status=ok
SXTC 2026-10-06  VOLUME-CONTEXT 18:15ET start=2026-10-06T22:15:00+00:00 shares=36807 local=0.4193x prior-peak=unknown status=ok
# WHLR shared SIP volume; prior 2026-10-05 48/48 slots; log-only
# reconstructed as-of 2026-10-06T22:30:09+00:00; source fetched 2026-10-06T22:32:32.230763Z
WHLR 2026-10-06  VOLUME-CONTEXT 16:00ET start=2026-10-06T20:00:00+00:00 shares=79913 local=unknown prior-peak=0.0640x status=warmup
WHLR 2026-10-06  VOLUME-CONTEXT 16:05ET start=2026-10-06T20:05:00+00:00 shares=42488 local=unknown prior-peak=0.0340x status=warmup
WHLR 2026-10-06  VOLUME-CONTEXT 16:10ET start=2026-10-06T20:10:00+00:00 shares=11795 local=unknown prior-peak=0.0094x status=warmup
WHLR 2026-10-06  VOLUME-CONTEXT 16:15ET start=2026-10-06T20:15:00+00:00 shares=8067 local=0.1899x prior-peak=0.0065x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 16:20ET start=2026-10-06T20:20:00+00:00 shares=10432 local=0.8844x prior-peak=0.0084x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 16:25ET start=2026-10-06T20:25:00+00:00 shares=12272 local=1.1764x prior-peak=0.0098x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 16:30ET start=2026-10-06T20:30:00+00:00 shares=8867 local=0.8500x prior-peak=0.0071x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 16:35ET start=2026-10-06T20:35:00+00:00 shares=12529 local=1.2010x prior-peak=0.0100x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 16:40ET start=2026-10-06T20:40:00+00:00 shares=23713 local=1.9323x prior-peak=0.0190x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 16:45ET start=2026-10-06T20:45:00+00:00 shares=265151 local=21.1630x prior-peak=0.2124x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 16:50ET start=2026-10-06T20:50:00+00:00 shares=280898 local=11.8457x prior-peak=0.2250x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 16:55ET start=2026-10-06T20:55:00+00:00 shares=288869 local=1.0895x prior-peak=0.2314x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 17:00ET start=2026-10-06T21:00:00+00:00 shares=84294 local=0.3001x prior-peak=0.0675x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 17:05ET start=2026-10-06T21:05:00+00:00 shares=46520 local=0.1656x prior-peak=0.0373x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 17:10ET start=2026-10-06T21:10:00+00:00 shares=48261 local=0.5725x prior-peak=0.0387x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 17:15ET start=2026-10-06T21:15:00+00:00 shares=26393 local=0.5469x prior-peak=0.0211x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 17:20ET start=2026-10-06T21:20:00+00:00 shares=31083 local=0.6682x prior-peak=0.0249x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 17:25ET start=2026-10-06T21:25:00+00:00 shares=36138 local=1.1626x prior-peak=0.0289x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 17:30ET start=2026-10-06T21:30:00+00:00 shares=100082 local=3.2198x prior-peak=0.0802x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 17:35ET start=2026-10-06T21:35:00+00:00 shares=39862 local=1.1030x prior-peak=0.0319x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 17:40ET start=2026-10-06T21:40:00+00:00 shares=27010 local=0.6776x prior-peak=0.0216x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 17:45ET start=2026-10-06T21:45:00+00:00 shares=21022 local=0.5274x prior-peak=0.0168x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 17:50ET start=2026-10-06T21:50:00+00:00 shares=23459 local=0.8685x prior-peak=0.0188x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 17:55ET start=2026-10-06T21:55:00+00:00 shares=7911 local=0.3372x prior-peak=0.0063x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 18:00ET start=2026-10-06T22:00:00+00:00 shares=5558 local=0.2644x prior-peak=0.0045x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 18:05ET start=2026-10-06T22:05:00+00:00 shares=21548 local=2.7238x prior-peak=0.0173x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 18:10ET start=2026-10-06T22:10:00+00:00 shares=7978 local=1.0085x prior-peak=0.0064x status=ok
WHLR 2026-10-06  VOLUME-CONTEXT 18:15ET start=2026-10-06T22:15:00+00:00 shares=5311 local=0.6657x prior-peak=0.0043x status=ok
```

**Book diagnostic (verbatim; log-only)** for the seven tradable >10% names with SIP volume above LCFY's single-digit-thousand bars. All IEX quotes are frozen at or before 17:00 ET. BURU's `sip-15m` row is a 2026-07-17 quote and does not describe tonight's book.

```text
BIYA BOOK iex bid $1.88 x100 / ask $1.92 x100 @ 2026-10-06 16:54:16 ET age 1h38m two-sided spread 2.08% of ask
BIYA BOOK sip-15m bid $2.32 x200 / ask $2.33 x1700 @ 2026-10-06 18:18:04 ET age 15m00s two-sided spread 0.43% of ask
BIYA BOOK refresh +15s iex unchanged @ 2026-10-06 16:54:16 ET
BIYA BOOK verdict: IEX STALE 1h38m; SIP-15m TWO-SIDED (observed 2026-10-06 18:33:04 ET; log-only)
MTEN BOOK iex bid $1.00 x100 / ask $1.02 x100 @ 2026-10-06 16:46:21 ET age 1h46m two-sided spread 1.96% of ask
MTEN BOOK sip-15m bid $1.49 x2900 / ask $1.50 x6000 @ 2026-10-06 18:18:04 ET age 15m00s two-sided spread 0.67% of ask
MTEN BOOK refresh +15s iex unchanged @ 2026-10-06 16:46:21 ET
MTEN BOOK verdict: IEX STALE 1h46m; SIP-15m TWO-SIDED (observed 2026-10-06 18:33:04 ET; log-only)
BURU BOOK iex bid $1.01 x100 / ask $1.35 x100 @ 2026-10-06 16:00:00 ET age 2h33m two-sided spread 25.19% of ask
BURU BOOK sip-15m bid $0.0726 x9000 / ask $0.0728 x2000 @ 2026-07-17 11:28:27 ET age 1951h04m two-sided spread 0.27% of ask
BURU BOOK refresh +15s iex unchanged @ 2026-10-06 16:00:00 ET
BURU BOOK verdict: IEX STALE 2h33m; SIP-15m TWO-SIDED (observed 2026-10-06 18:33:04 ET; log-only)
SXTC BOOK iex bid $2.19 x100 / ask $2.24 x100 @ 2026-10-06 16:48:07 ET age 1h44m two-sided spread 2.23% of ask
SXTC BOOK sip-15m bid $1.96 x1100 / ask $1.97 x200 @ 2026-10-06 18:18:04 ET age 15m00s two-sided spread 0.51% of ask
SXTC BOOK refresh +15s iex unchanged @ 2026-10-06 16:48:07 ET
SXTC BOOK verdict: IEX STALE 1h44m; SIP-15m TWO-SIDED (observed 2026-10-06 18:33:04 ET; log-only)
MI BOOK iex bid $1.56 x100 / ask $1.59 x100 @ 2026-10-06 16:59:55 ET age 1h33m two-sided spread 1.89% of ask
MI BOOK sip-15m bid $1.40 x4900 / ask $1.42 x500 @ 2026-10-06 18:17:59 ET age 15m06s two-sided spread 1.41% of ask
MI BOOK refresh +15s iex unchanged @ 2026-10-06 16:59:55 ET
MI BOOK verdict: IEX STALE 1h33m; SIP-15m TWO-SIDED (observed 2026-10-06 18:33:04 ET; log-only)
NCPL BOOK iex bid $0.9460 x100 / ask $0.0000 x0 @ 2026-10-06 16:00:03 ET age 2h33m one-sided/empty
NCPL BOOK sip-15m bid $1.38 x400 / ask $1.40 x1700 @ 2026-10-06 18:18:00 ET age 15m04s two-sided spread 1.43% of ask
NCPL BOOK refresh +15s iex unchanged @ 2026-10-06 16:00:03 ET
NCPL BOOK verdict: IEX STALE 2h33m; SIP-15m TWO-SIDED (observed 2026-10-06 18:33:04 ET; log-only)
WHLR BOOK iex bid $1.03 x100 / ask $1.07 x100 @ 2026-10-06 16:57:58 ET age 1h35m two-sided spread 3.74% of ask
WHLR BOOK sip-15m bid $1.02 x200 / ask $1.04 x200 @ 2026-10-06 18:17:55 ET age 15m09s two-sided spread 1.92% of ask
WHLR BOOK refresh +15s iex unchanged @ 2026-10-06 16:57:58 ET
WHLR BOOK verdict: IEX STALE 1h35m; SIP-15m TWO-SIDED (observed 2026-10-06 18:33:04 ET; log-only)
```

**Night summary for the morning evaluation:** Two positions are open, BIYA (52 @ $1.91, Grade None) and MTEN (70 @ $1.39, Grade B). Measure these morning references:

- **Watch hypotheticals:** SXTC DEAD-CAT-OVERRIDE WATCH ($1.57 at 16:25 ET) and VCIG FIRST-BAR-SPIKE WATCH ($1.69 at 16:20 ET).
- **Earlier FIRST-BAR-SPIKE WATCH hypotheticals:** NCPL and ICMB ($1.22 and $0.87 at 16:20 ET).
- **Reference prices only:** BURU $1.36 (late 18:00 ET spike, blocked by the gate), NCPL $1.38 (late CONFIRM-3 YES on thin volume), and WHLR $1.04 (18:00 ET).

**Daily email:** Report BIYA at +23.6% after a new $2.39 SIP high and MTEN at +6.5% after its 18:15 re-expansion. Report BURU's late 18:00 ET spike (745K shares in one bar, CONFIRM-3 NO), blocked by the 2-AH-scan gate, with a Grade C financing 8-K accepted at 17:10 ET. Report NCPL's late CONFIRM-3 YES on thin volume, kept out of the DEAD-CAT-OVERRIDE sample. One tooling issue: `book-check.js` returned a 2026-07-17 pre-split SIP quote for BURU and labelled it `TWO-SIDED`. The delayed-book diagnostic can mislabel names that changed share structure, and this needs a fix. No item from this scan requires Juan's input.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
| BIYA | $1.91 | 23:01 CEST (17:01 ET) | 52 | d20b26bc-7405-4f87-831e-dd4f6e5d927b | Grade None. BUILD/hold: SIP high $2.07 at 16:40 ET on 802K sh, CONFIRM-3 YES, 4 AH scans >10%, 9% below high at entry, Day -2.5%, Total +36.4%. No catalyst found (concern noted); exit at first premarket opportunity. |
| MTEN | $1.39 | 00:01 CEST Oct 7 (18:01 ET) | 70 | 271309e2-7bd3-49e7-b39f-0728681f53c6 | Grade B (same-day 6-K: completed $15M cash acquisition of HK Phoenix Gateway Alliance). BUILD: 17:15 ET re-ignition, SIP 711K–1.48M sh/bar, new high $1.59 at 17:40 ET, 2 AH scans >10% (+10.6% → +51.2%), Day -0.4%, Total +44.4%, 12.6% below high at entry. Hard stop $1.18 (-15%); hold up to 2 days. |

No entries at the 21:30 CEST regular-session scan. Entries open at the 23:00 CEST scan.

## Morning Evaluation — 10:20 CEST (04:20 ET, October 7)

**Pulse 1: BIYA is today's winner. The scanner detected it and we hold it.** BIYA built all evening from its **$1.365** close to a **$2.4893** AH high, then spiked to **$2.86 (+109.5%)** at 04:13–04:14 ET on **2.78M shares / 19,856 trades** in those two minutes. We entered at **$1.91** at 23:01 CEST, so the position reached **+49.7%** at the peak and is **+25.7%** at 04:29 ET. The >100% level held for only about two minutes; the liquid level since then is **$2.39–$2.51 (+75% to +84%)**. MTEN, our second entry, peaked at **$1.79 (+86.7%)**, below the bar. The biggest raw mover, **TOPP (+309.9%)**, sits below the scanner's $0.50 floor. It is the first floor exclusion to clear >100% and hold on a tight SIP book.

Discovery ran before reading this log: `scan.py --all --session premarket` at 04:20 ET, then an unfiltered TradingView PM sweep (no price, cap, or volume limit) and a listed-exchange sweep of October 6 regular-session movers above +15%. Every level below is an **Alpaca SIP** daily close or 5-minute/1-minute bar through the **04:15 ET** bar (SIP lags about 15 minutes). Yahoo and TradingView were used only for timeline shape and the latest price. October 6 is a normal Tuesday session, so every % uses the October 6 SIP close; entry Total% uses the October 5 SIP close.

### Today's Winner

**BIYA — Baiya International Group (personnel services, China), Nasdaq**

- Catalyst: **None.** The scanner ran eleven searches and found nothing fresh. Background only: a 1-for-10 reverse split in July 2026 and an AH spike on September 29. Grade **None**.
- Previous close: **$1.365** (SIP, October 6; Day −2.5% from the $1.40 October 5 close). The tooling's "$1.40 previous close" is October 5's and understates the gain (+104.3%).
- AH last night: ignited at **16:05 ET** (285,556 → 1,072,394 → 1,596,650 shares per bar through 16:15). SIP at the scheduled checkpoints: 22:30 **$1.77 (+29.7%)**, 23:00 **$1.85 (+35.5%)**, 23:30 **$2.16 (+58.2%)**, 00:00 **$2.12 (+55.3%)**, 00:30 **$2.34 (+71.4%)**. AH SIP high **$2.4893 (+82.4%) at 19:55 ET**; AH total **14.06M shares / 93,035 trades**.
- Premarket: opened at $2.04 and dipped to $1.70 by 04:04. It rebuilt from 04:08, and the **04:13 minute ran $2.14 → $2.84 (1,160,916 shares / 8,239 trades, close $2.76)**. The **04:14 minute hit $2.86** and closed $2.16 (1,621,736 / 11,617). The 04:10 5-minute bar holds 4,196,580 shares / 29,466 trades. TradingView also shows a $2.86 PM high. Since then: $2.39–$2.51 (+75% to +84%) at 04:25–04:30 ET.
- Hypothetical P&L: first sighting (22:30 checkpoint) **$1.77 → $2.86 = +61.6%**. Real fill **$1.91 → $2.86 = +49.7%**; to the ~$2.40 plateau **+25.7%**.
- Float **2.7M** | Market cap **$8.6M** (TradingView).
- Capturable: **yes, and captured.** We hold an Alpaca fill (52 @ $1.91). The IEX quote froze at 16:54 ET, but the 00:30 scan logged a two-sided SIP book at 18:18 ET ($2.32 / $2.33).
- Winner bar: >100% from the true last-session close on heavy, accumulating SIP volume, with a fillable book. **Clears, narrowly.** The >100% print lasted about two minutes, and the sustained PM level is +75–84%. Yahoo's 5-minute high was $2.60 until the 04:10 bar was finalized; the SIP and TradingView $2.86 is the real peak.

**Scanner Diagnostic:**

- Detectable at screening time (~22:15 CEST)? **YES.** At 16:15 ET BIYA was +30% on 1.6M shares per bar. The scanner first listed it at **22:25 CEST**, then in 7 AH scans in total.
- What it looked like and what we did: at 23:00 it had CONFIRM-3 YES, a SIP high of $2.07 at 16:40, a BUILD trajectory, Day −2.5%, and Total +36.4%. It held 9% below the high on a fresh book. We **entered at the first entry scan (23:00 CEST), 52 @ $1.91.** No catalyst was found; the scanner noted that as a concern but did not use it as a skip reason.
- Scanner gap: **none for BIYA.** The detection and selection both worked. Exits are owned by `position-evaluation.md`.

**Also notable (not the headline):**

- **TOPP — Toppoint Holdings (trucking), AMEX, close $0.1116. Below the $0.50 floor; biggest raw PM mover.** In-window AH signal: the 18:05 bar closed **$0.1288 (+15.4%)** on 344,725 shares / 636 trades, and the 18:10 bar closed $0.1276 (+14.3%, high $0.1362) on **1,132,824 / 1,528** (VWAP $0.1310). At the 18:30 ET checkpoint it was +6.0%. A late tail followed: **$0.1495 (+34.0%) at 19:30 ET** on 656,502 / 564. PM: **$0.4574 (+309.9%) at 04:00** on **18,314,928 / 25,777**, then 5-minute closes **$0.3097, $0.3095, $0.2813, $0.2734** (+177% → +145%) on 7.1M–18.3M shares per bar; Yahoo shows $0.27 (+141%) at 04:29. SIP book: **$0.1296 x28,400 / $0.1340 at 18:11:59 ET (spread 3.3% of ask)** and **$0.3078 / $0.3126 at 04:06:59 ET (1.5%)**. The IEX quote has been frozen at 16:00 ET with `ask $0.00 x0`. `tradable=true`, float 20.8M, Grade None (one search, nothing found). Hypothetical **18:10 VWAP $0.1310 → $0.4574 = +249%**, or **+136%** to the 04:05 close. The scanner never saw it: `MIN_PRICE = $0.50`. Even without the floor, no scheduled checkpoint caught it above +10%, so it would likely have failed the 2-AH-scan gate.
- **MTEN — Mingteng International (automotive molds), our second entry.** Same-day 6-K on a completed $15M acquisition of HK Phoenix Gateway Alliance (Grade B per the scan). BUILD from a 17:15 ET re-ignition to an AH SIP high of $1.755 (+83.1%) at 19:55 ET. PM SIP high **$1.79 (+86.7%) at 04:05** on 2,257,912 / 12,747, then $1.44–$1.52. Below the bar. Detected (3 AH scans) and entered at $1.39.
- **BYAH (+104.5%) is a PM-only spike.** It had no AH trades. The 04:01 minute wicked to $4.96 on 78,354 shares / 1,260 trades and closed $3.04 the same minute; by 04:25 it was $2.46 (+1.4%). It is uninvestable and not a winner.

### Baseline Tracking

Source: the October 5 log (Days tracked 94), which is the immediately preceding trading day. **No new baseline gap.** Existing gaps stay **Sep 11, Sep 18, Sep 25, Oct 2**.

- Days tracked: **95** (94 + October 6 only).
- Winners detected by scanner: **73/84 (86.9%)**. BIYA is added as detected (+1/+1). **TOPP adds one price-floor detection miss** (+0/+1), following the July 30 (MGRX, SBEV) and September 28 (SLXN) convention: a real, in-window, volume-backed AH mover that the universe floor excluded counts in the denominator even when it is not the headline winner.
- Winner selected for paper trade: **37/80 (46.3%)**. BIYA was entered (+1/+1).
- Target: >80% detection. Status: **BASELINE MET.** Coverage failures, the four skipped retrospectives, and the raw floor exclusions in the denominator all limit what the rate means.

### Retrospective Scan Results

`scan.py --all --session premarket` (04:20 ET): MTEN, BIYA, BURU, MI, SDEV, BYAH, SXTC. The unfiltered sweep added TOPP (sub-$0.50), NCPL, and thin single-print names (PMEC, DFLI, MKZR, OFS, BLIN, NEOG, LONA, IVF, XWEL: 100–1,810 PM shares). The regular-session sweep (OLB, MOBX, APUS, VCIG, XHLD, IPDN, SMXT, OLOX, FRGT, AIFA, PMI, DLXY, JAGX, MODD, JUNS, FFR, BESS, BFRG, RMSG) found no other in-window AH mover above +10% on real volume except VCIG (+48.9%, detected, faded). A forced `scan.py --all --session afterhours` at 04:30 ET returned **0 hits**, because the postmarket fields reset overnight.

| Ticker | Oct 6 SIP close | AH SIP high / ET | PM SIP high / ET | PM high vs close | Peak-bar shares / trades | Latest | Classification |
|--------|-----------------|------------------|------------------|------------------|--------------------------|--------|----------------|
| BIYA | $1.365 | $2.4893 / 19:55 | $2.86 / 04:14 | **+109.5%** | 4,196,580 / 29,466 (5-min) | ~$2.40 (+76%) | AH→PM continuation; **winner**; detected + entered |
| TOPP | $0.1116 | $0.1495 / 19:30 | $0.4574 / 04:00 | **+309.9%** | 18,314,928 / 25,777 | $0.27 (+141%) | Below $0.50 floor; in-window AH +15%, late tail +34%, PM gap; biggest raw mover |
| BYAH | $2.425 | no AH trades | $4.96 / 04:01 | +104.5% | 78,354 / 1,260 (1-min) | $2.46 (+1.4%) | PM-only; one-minute wick; uninvestable |
| MTEN | $0.9587 | $1.755 / 19:55 | $1.79 / 04:05 | +86.7% | 2,257,912 / 12,747 | ~$1.44–1.52 (+50–59%) | AH→PM continuation; detected + entered |
| MI | $1.23 | $1.84 / 16:20 | $2.0262 / 04:00 | +64.7% | 1,669,220 / 10,749 | $1.84 (+49.5%) | Dead-cat bounce (Day −82.4%); PM topped the AH high |
| SXTC | $1.25 | $2.58 / 16:30 | $1.94 / 04:00 | +55.2% | 191,723 / 2,296 | $1.72 (+37.6%) | Dead-cat (Day −39.9%); AH better |
| BURU | $1.20 | $1.95 / 19:15 | $1.82 / 04:00 | +51.7% | 1,352,692 / 7,861 | $1.31 (+9.3%) | Final-scan first sighting; tail high after the last scan |
| NCPL | $1.09 | $1.53 / 19:50 | $1.47 / 04:00 | +34.9% | 73,244 / 855 | $1.31 (+20.2%) | Thin drift (Day −17.4%) |
| SDEV | $3.25 | $3.54 / 19:05 (+8.9%) | $4.01 / 04:00 | +23.4% | 1,792,248 / 14,687 | $3.83 (+17.9%) | PM-driven; AH under +10% |
| WHLR | $0.91 | $1.24 / 16:45 | $1.05 / 04:00 | +15.4% | 99,903 / 1,290 | $0.94 (+3.0%) | Dead-cat (Day −16.5%), thin; AH better |
| LCFY | $2.05 | $2.62 / 16:35 | $2.24 / 04:00 | +9.3% | 6,051 / 47 | $2.10 (+2.5%) | Thin drift; AH better |
| VCIG | $1.41 | $2.10 / 16:25 | $1.18 / 04:00 | −16.3% | 406,058 / 2,172 | $0.95 (−32.6%) | Spike→fade; correctly skipped |

### Open Position P&L (Alpaca)

Both fills are open and owned by `position-evaluation.md` (10:30 / 14:30 CET); this pulse placed no orders. Alpaca's `current_price` matches the live price ($2.40 / $1.44 against Yahoo's $2.39 / $1.44 at 04:29 ET), so the P&L is current. The IEX quotes behind it are frozen (BIYA 16:54:16 ET, MTEN 16:46:21 ET October 6), so the live check came from Yahoo and SIP.

| Ticker | Entry | Entry Total% | Catalyst | Entry Time | PM Peak | Peak Time | Exit | P&L | P&L % | Status |
|--------|-------|--------------|----------|------------|---------|-----------|------|-----|-------|--------|
| BIYA | $1.91 | +36.4% (vs $1.40) | None — no catalyst found | 23:01 CEST (17:01 ET) | $2.86 (SIP) | 04:14 ET | open | +$25.48 unrealized | +25.7% | Open; peak +49.7% |
| MTEN | $1.39 | +44.4% (vs $0.9624) | B — same-day 6-K, completed $15M acquisition | 00:01 CEST (18:01 ET) | $1.79 (SIP) | 04:05 ET | open | +$3.58 unrealized | +3.7% | Open; peak +28.8% |

**Total Realized P&L (Alpaca fills only): $0.00.** Both positions are unrealized.

### Scanner Effectiveness

- Evening scans ran: **7 of 7** scheduled checkpoints (21:30, 22:00, 22:30, 23:00, 23:30, 00:00, 00:30 CEST), plus six extra observations (22:05, 22:10, 22:15, 22:20, 22:25, 22:45). The entry window was fully covered.
- Candidates found: **11 unique tickers** with a >10% AH appearance (SXTC 8, BIYA 7, NCPL 6, MI 5, VCIG 5, MTEN 3, LCFY 3, WHLR 3, BURU 1, LHSW 1, ICMB 1), plus a 28-name regular-session watchlist.
- Retrospective matches: **6/6 in-universe AH→PM movers detected** (BIYA, MTEN, MI, SXTC, BURU, NCPL). TOPP was missed (floor). BYAH is PM-only.
- Supplementary AH-change-only pass: the line is present in all 12 AH scans. **1 unique ticker (ICMB), outcome: 0 continuation / 0 faded / 1 unassessed.** ICMB has **no SIP PM prints through the 04:15 ET bar**. Its only logged AH price was $0.87 (22:20), on a 1,537-share opening bar; the AH tape drifted to $0.70–$0.75 after that.

### Missed Opportunities

| Ticker | AH Change | Why Missed | Would Be Profitable? |
|--------|-----------|------------|---------------------|
| TOPP | +15.4% at 18:05 ET on 345K–1.13M shares per bar; +34% tail at 19:30 | Below `MIN_PRICE = $0.50`. Even without the floor, no scheduled checkpoint showed it above +10% (18:30: +6.0%), so it would likely have had only one appearance | **Yes**: $0.1310 → $0.4574 **+249%** peak; **+136%** to the 04:05 close |
| BURU | +18% at 00:30 (first and only appearance); tail high $1.95 at 19:15 | 2-AH-scan gate. CONFIRM-3 NO, so it is not a final-scan gate-block | Transient: $1.36 → $1.82 **+33.8%** at the 04:00 bar, which closed $1.48 (+8.8%); latest $1.31 |

MI, SXTC, WHLR, NCPL, LCFY, and VCIG were detected and skipped on Day%, thin volume, or fade rules. Their outcomes are in the trackers below.

### AH Mover Follow-Through

Every name with two or more >10% AH scans. Current = latest SIP 5-minute close (04:10–04:15 ET) or the 04:29 Yahoo print for the two open positions.

| Ticker | AH Peak | Peak Time | AH Trajectory | Current PM | From Peak | From Close | Verdict |
|--------|---------|-----------|---------------|------------|-----------|------------|---------|
| BIYA | $2.4893 | 19:55 | **Build** (+30 → 36 → 58 → 55 → 71%) | $2.40 | −3.6% | +75.8% | PM peak $2.86 **exceeded AH by 14.9%**; continuation |
| MTEN | $1.755 | 19:55 | **Late surge / build** (+8 → 24 → 41 → 54%) | $1.44 | −17.9% | +50.2% | PM peak $1.79 **exceeded AH by 2.0%**, then faded |
| MI | $1.84 | 16:20 | **Spike→fade** (+25 → 24 → 21 → 12 → 19%) | $1.84 | 0.0% | +49.5% | PM peak $2.0262 **exceeded AH by 10.1%** |
| SXTC | $2.58 | 16:30 | **Spike→hold** (+11 → 26 → 22 → 70 → 74 → 53 → 54%) | $1.72 | −33.3% | +37.6% | PM peak $1.94 **fell short (−24.8%)**; AH better |
| NCPL | $1.53 | 19:50 | **Late surge**, thin (+10 → 10 → 15 → 28%) | $1.31 | −14.4% | +20.2% | PM peak $1.47 **fell short (−3.9%)**; AH better |
| WHLR | $1.24 | 16:45 | **Spike→hold**, thin (+13 → 16 → 14 → 13%) | $0.94 | −24.4% | +3.0% | PM peak $1.05 **fell short (−15.3%)**; AH better |
| LCFY | $2.62 | 16:35 | **Spike→fade**, thin (+21.5 → 18.6 → 10.2%) | $2.10 | −19.8% | +2.5% | PM peak $2.24 **fell short (−14.5%)**; AH better |
| VCIG | $2.10 | 16:25 | **Spike→fade** (+43% → −27%) | $0.95 | −54.8% | −32.6% | PM peak $1.18 **fell short (−43.8%)**; AH better |

**Chase-cap check:** both fills were near the qualifying-scan price (BIYA Entry Total +36.4%, MTEN +44.4%), far below the ~+120% zone, and PM reclaimed both. No new chase case; the standing count stays **1 (XOS), never reclaimed**.

### Notes

- **Coverage, last 10 completed sessions (Sep 23–Oct 6):** **Sep 25 0/7, Sep 29 3/7, Oct 2 0/7** (position evaluations only), **Oct 5 0/7** (no log, zero scan commits). Sep 23, 24, 28, 30, Oct 1, and **Oct 6 ran 7/7.** That is **4 failures in 10 sessions**, down from 5 after Sep 22 dropped out of the window. It is still above the ≥2 trigger, so the scheduler/bridge investigation stays routed to the email. Tonight's coverage was complete, and this pulse started on time (10:20 CEST).
- **CEILING-OVERRIDE WATCH:** none flagged.
- **DEAD-CAT-OVERRIDE WATCH — SXTC** (float 1.0M, Grade None, Day −39.9%): hypothetical **$1.57 at 22:25 CEST → PM SIP peak $1.94 (04:00, 191,723 / 2,296) = +23.6%**. The next closes ($1.84, $1.72) stayed above the entry. The PM peak stayed below the $2.58 AH high and the $2.08 October 5 close. Named history: founding **BYAH +72%**, **BENF −0.6%, ACTU −9.6%, WHLR −2.6%, DKI −37.2%, AMOD +65.7%, SXTC +23.6%**, now **3 positive / 4 negative**. MI and WHLR were dead-cat skips that did not meet the watch condition; MI's PM peak beat its AH high by 10.1% anyway (first sighting $1.54 at 22:45 → $2.0262, +31.6%).
- **Sub-3M fade-rule sample: 4/22 → 4/23 (17.4%).** Add **VCIG** (float 1.04M, Grade C: a same-day product-launch PR plus a $125M equity-facility overhang). The 23:00 skip was SPIKE→FADE. AH SIP peak $2.10 at 16:25 → PM peak $1.18: **fell short.** (a) First qualifying scan $1.69 → $1.18 = **−30.2%**. (b) PM-open VWAP $1.0035 → $1.18 = **+17.6%** on 406,058 / 2,172, with the next close $0.96, below the VWAP, so the gain was transient. Controls outside the denominator: **LCFY** (1.4M, thin-drift co-block; AH $2.62 → PM $2.24; (a) first qualifying scan $2.49 at 23:30 → −10.0%, (b) $2.1623 → +3.6% on 6,051 / 47 shares). **MI** (542K, dead-cat co-block) re-exploded above its AH high; see above. No Grade A/B fader this cycle. The exception trigger stays far off.
- **FIRST-BAR-SPIKE WATCH:** three names were flagged at 22:20. Full 16:00–20:00 SIP bars give these results.
  - **VCIG: superseded.** Its 16:25 high of $2.10 came on 2.77M shares / 15,430 trades. Hypothetical $1.69 → $1.18 = −30.2%.
  - **NCPL: superseded.** Later highs reached $1.40 at 18:15 (47,507 / 262) and $1.53 at 19:50 (28,158 / 109), above the $1.28 opening high, on volume similar to its 72K-share opening bars. Hypothetical $1.22 → $1.47 = +20.5%, with the next close $1.35.
  - **ICMB: confirmed first-bar case.** The $0.87 at 16:00 was never exceeded, but the PM verdict is **pending** because there are no PM prints.
  - Standing: **11 valid (2 ran / 9 faded-flat), 16 flagged, 4 superseded (NCI, SSM, VCIG, NCPL), 1 pending (ICMB); 3 pre-gate entries, 0 ran.** No run to route.
- **Raw PM leader / PM-only tracking:** the biggest raw PM mover is **TOPP, +309.9%**. It is **not PM-only**: it had an in-window +15% AH move on 1.13M shares and a +34% late tail. It is an AH→PM continuation that the floor excluded. The only PM-only gapper is **BYAH (+104.5%), uninvestable**: a one-minute wick that closed 39% off its high in the same minute, on 78K shares, with no catalyst found. `log/pm-open-scan.csv` has **no October 7 rows yet** at 04:30 ET. The CSV holdable PM-only count is **62**. Carry the Initiative-6 cluster to the email. A PM-only gapper is not a scanner failure.
- **Price-floor exclusions: 10 → 11 observations across 7 → 8 nights; 0 → 1 confirmed >100%-and-holdable; 1 inherited pending.** New row **TOPP Oct 6→7**: close $0.1116, `tradable=true`, float 20.8M, Grade None. In-window AH at 18:05–18:10 was **+14–15% on 345K–1.13M shares / 636–1,528 trades**. PM peak **$0.4574 (+309.9%)**. Hypothetical 18:10 VWAP → peak **+249%**, or **+136%** to the 04:05 close. Verdict: **holdable.** Four consecutive 5-minute closes stayed at +145% to +177% on 7.1M–18.3M shares. The SIP spread was 3.3% of ask at 18:12 ET and 1.5% at 04:07 ET. The broker-side IEX book stayed frozen and empty, so a live Alpaca entry would have hit the stale-quote problem. TOPP is the first case to meet both legs of the floor-change trigger (≥3 such names on ≥3 nights): **1 of 3. Not met.** Route as a question, not a parameter change.
- **Late-AH-tail tracking:** BIYA's defining surge came at 16:05 ET, inside the window. Its 19:55 high continued a build that had already been detected. MTEN is the same case. TOPP's 19:15–19:30 surge (+16% → +34%) is a tail move on a below-floor name, so it is not added (GNS precedent). BURU's $1.95 tail high at 19:15 came after a detected 18:00 ignition. Standing **2 true-tail (ORIS, GNS) / 1 feed-lag (BTCT)**, unchanged.
- **In-window feed-lag: 7, unchanged.** Every in-universe in-window mover above +10% on real volume was surfaced. OLOX touched +10–11% at 17:05–17:30 on 26K–55K shares / 90–216 trades per bar, which is thin, not accumulating. Carry the reached whole-universe AH verification recommendation to the email.
- **Execution and selection trackers:** broker-block **2**; stale-book-only **6** (4 profitable / 2 negative); no-fillable-book **4**; float-only **1**; final-scan-only **2**. All unchanged. Both fills tonight executed while the IEX quote was frozen: BIYA at 17:01 ET against a 16:54 quote, and MTEN at 18:01 ET against a 16:46 quote ($1.00 / $1.02). The limits were priced from SIP bars. This shows a frozen IEX quote does not prevent a paper fill when the limit is set from SIP; that is evidence for the stale-book feed decision. **BURU** (float 8.4M, Grade C financing 8-K, ignited 18:00 ET) is a near-case excluded from the final-scan tally because CONFIRM-3 was NO. Its reference $1.36 reached $1.82 at the 04:00 bar (+33.8%), but the bar closed $1.48 and it is now $1.31, so the run was transient.
- **Actual-entry trackers:** both entries are **day-1 fresh igniters** (BIYA Day −2.5%, MTEN Day −0.4%), and **both ran**: BIYA $1.91 → $2.86 (+49.7%), MTEN $1.39 → $1.79 (+28.8%). First-day igniters **27 → 29 entries (11 ran / 8 flat / 10 faded) = 37.9% ran**; multi-session **1, faded**, unchanged. Reverse-split recency stays **4/5 this-week faded / 4/6 older continued**. BIYA's July 1-for-10 split is background, not the catalyst note, so it is not added (October 1 convention).
- **Extreme-runner tally: 15 fades / 2 continues (88.2%), unchanged.** No AH peak reached the ~+130% zone: BIYA +77.8% total from $1.40, MTEN +82.4% from $0.9624, SXTC +24.0% total from $2.08 (+106% only from its crashed $1.25 close). The partial-profit routing trigger stays reached.
- **SIP basis checks:** October 6 closes BIYA $1.365, MTEN $0.9587, TOPP $0.1116, SXTC $1.25, MI $1.23, NCPL $1.09, VCIG $1.41, BURU $1.20, WHLR $0.91, LCFY $2.05, BYAH $2.425. October 5 closes for Entry Total%: BIYA $1.40, MTEN $0.9624. `price-timeline.py` uses October 5's close for BIYA ($1.40, showing "+104.3%"); the October 6 basis gives +109.5%.
- **Tooling (carried from the 00:30 scan):** `book-check.js` returned a pre-split July 17 SIP quote for BURU and labelled it `TWO-SIDED`. Names whose share structure changed can be mislabelled.

### Daily Email Routing

- Headline: **BIYA is a real winner, detected and traded.** SIP PM peak $2.86 (+109.5%) on 2.78M shares in two minutes. Our 52 @ $1.91 entry peaked at +49.7% and is +25.7% at 04:29 ET. The >100% level held only about two minutes. MTEN (entered $1.39) peaked at +28.8% and is +3.7%. Detection **73/84 (86.9%)**, selection **37/80 (46.3%)**, 95 days tracked. No realized P&L yet.
- **Question for Juan — sub-$0.50 floor:** TOPP (+309.9% PM, holdable for 20+ minutes on a 1.5–3.3% SIP spread, in-window AH +15% on 1.13M shares) is the first floor exclusion to meet both the >100% and the holdable-on-tight-spread legs. The trigger needs 3 such names on 3 nights; this is 1 of 3. Should a log-only sub-$0.50 observation pass start collecting these, given the broker-side IEX book is frozen for such names?
- **Scheduler/bridge reliability (decision for Juan):** 4 coverage failures in the last 10 sessions (Sep 25, Sep 29, Oct 2, Oct 5). October 6 ran 7/7 and this pulse started on time.
- **Stale-quote feed:** both fills executed on frozen IEX quotes with SIP-priced limits. Add this to the stale-book feed decision (6 standing cases).
- Carry forward: 7 feed-lag observations → whole-universe AH verification; 62-row holdable PM-only cluster → Initiative 6; 15/17 extreme-runner fades → partial-profit decision; reverse-split recency recommendation; the `book-check.js` pre-split quote bug. The sub-3M fade (4/23), price-floor (1 of 3), and first-bar (no new run) triggers are not met.

### Price Charts

Excerpts from `python3 scripts/price-timeline.py BIYA MTEN TOPP` at ~04:29 ET. The tool's BIYA previous close is October 5's ($1.40), not October 6's ($1.365). The tables above set the levels; these rows show shape only. The block charts were flat and are omitted.

```text
BIYA  Previous Close: $1.40 | 2-Day Range: $1.30 - $2.86 | Current: $2.39 (+70.7%) | Peak: $2.86 (+104.3%) at 10-07 04:10 ET
  [AH] 10-06 16:05 ET: $1.69 (+20.7%)   [AH] 16:35: $2.04 (+45.4%)   [AH] 17:25: $2.17 (+54.9%)
  [AH] 10-06 18:15 ET: $2.34 (+67.2%)   [AH] 18:30: $2.38 (+70.1%)   [AH] 19:00: $2.22 (+58.6%)
  [PM] 10-07 04:00 ET: $1.79 (+27.9%)   [PM] 04:05: $1.95 (+39.3%)   [PM] 04:10: $2.16 (+54.3%)
  [PM] 10-07 04:15 ET: $2.24 (+60.0%)   [PM] 04:20: $2.45 (+75.0%)   [PM] 04:29: $2.39 (+70.7%)

MTEN  Previous Close: $0.96 | 2-Day Range: $0.96 - $1.79 | Current: $1.45 (+50.7%) | Peak: $1.79 (+86.0%) at 10-07 04:05 ET
  [AH] 10-06 16:30 ET: $1.10 (+14.1%)   [AH] 18:30: $1.49 (+55.0%)   [AH] 18:45: $1.65 (+71.4%)
  [PM] 10-07 04:00 ET: $1.72 (+78.7%)   [PM] 04:05: $1.49 (+54.7%)   [PM] 04:15: $1.38 (+43.4%)
  [PM] 10-07 04:25 ET: $1.44 (+49.5%)   [PM] 04:29: $1.44 (+49.6%)

TOPP  Previous Close: $0.11 | 2-Day Range: $0.11 - $0.46 | Current: $0.27 (+141.4%) | Peak: $0.46 (+312.1%) at 10-07 04:00 ET
  [AH] 10-06 18:10 ET: $0.13 (+16.8%)   [AH] 19:50: $0.14 (+24.0%)
  [PM] 10-07 04:00 ET: $0.31 (+179.0%)  [PM] 04:05: $0.31 (+178.8%)  [PM] 04:10: $0.28 (+153.4%)
  [PM] 10-07 04:15 ET: $0.27 (+146.3%)  [PM] 04:20: $0.25 (+129.1%)  [PM] 04:29: $0.27 (+141.4%)
```
