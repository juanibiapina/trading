# 2026-07-09

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| SUNE | $2.56 | $2.44 | -4.7% | ~$2.67 (+4.3%) | 1 | None | SELL | Grade None → exit first premarket opportunity. Above -10% hard stop but no catalyst; sold on PM fade. |

**Actions taken:**
- SELL 36 SUNE @ limit $2.35 ext (id 54d1a663), filled @ $2.44. Final P&L −$4.32 (−4.7%).
- PM opened $2.72 spike (single-bar, L $2.36 same bar) then faded to $2.41 / vwap $2.39. OVN peak ~$2.67. Never re-rated above entry. Grade None rule applied.
- No open positions remaining.

## Position Evaluation — 14:30 CET

No open positions. Alpaca `positions` empty; `OPEN_POSITIONS.md` reconciled (clean slate). SUNE was closed in the 10:30 pulse. Nothing to hold or sell.

## Scan 21:30 CET (3:30 PM ET)

**Regular session** (AH opens 16:00 ET / 22:00 CET). Observation only — no entries before AH per regular-session caution rule. Most high-Chg% hits show tiny share counts (100-600 sh) = stale/illiquid regular-session prints, not tradable. Notable movers to watch into AH:

| Ticker | Chart | Price | Chg% | 5mVol | IRVol | VChg% | Float | MCap | Industry |
|--------|-------|-------|------|-------|-------|-------|-------|------|----------|
| SUNE | [TV](https://www.tradingview.com/chart/?symbol=SUNE) | $2.64 | +25.1% | 23K | 103.4 | -27.0% | 3.4M | 10.9M | Engineering & Construction |
| EVGN | [TV](https://www.tradingview.com/chart/?symbol=EVGN) | $0.50 | +20.7% | 71K | 17.4 | +27.9% | 12.0M | 6.1M | Biotechnology |
| DOGZ | [TV](https://www.tradingview.com/chart/?symbol=DOGZ) | $1.01 | +1.0% | 15K | 14.6 | +111.6% | 3.9M | 14.7M | Consumer Sundries |
| HYEX | [TV](https://www.tradingview.com/chart/?symbol=HYEX) | $2.20 | +69.2% | 2K | 2.9 | +240.0% | 1.6M | 37.2M | Pharmaceuticals: Other |

**Notes:**
- SUNE: our closed position from this morning (sold PM @ $2.44, Grade None). Back to +25.1% intraday on real volume (23K/5min). Watch whether it carries into AH — do NOT re-enter the same ticker (one entry per candidate per night rule), and it stays Grade None.
- EVGN: only real-volume sub-$10 mover with float <15M besides SUNE. Sub-$1 biotech. Watch for AH catalyst.
- HYEX +69% but thin (2K/5min) — likely stale. Watch AH liquidity.
- Ultra-high %s (CYDX +493%, RBNE +1623%, VRAX +109%, WMTN +458%, SRRCF +3010%) all have <1K share prints = illiquid noise. Ignore unless real AH book appears.
- No entries: pre-AH observation scan. Re-evaluate at 22:00+ CET AH scans.

## Scan 22:00 CET (4:00 PM ET)

**AH open** — scanner 0 hits at 16:00 ET (volume not yet accumulated; normal this early). Observation only per learning-phase rule (no entries before 23:00 CET). Watchlist from 21:30 checked via broker quotes:

| Ticker | Quote (bid/ask) | Note |
|--------|-----------------|------|
| SUNE | $2.20 x100 / $2.96 x100 | Wide spread, thin. Our closed position (Grade None, do-not-re-enter). |
| EVGN | $0.42 x100 / $0.59 x500 | Wide spread, low price. Watch AH build. |
| HYEX | no quote | No Alpaca AH book. |
| DOGZ | $0.83 x100 / $0.00 x0 | Ask $0.00 x0 = no fillable AH book. |

**Notes:**
- No candidates. Books thin/wide at AH open, no accumulation yet.
- No entries (observation-only scan + no fillable liquidity). Re-evaluate at 22:30 / 23:00 CET.

## Scan 22:30 CET (4:30 PM ET)

**AH scan** — 3 hits. Observation only per learning-phase rule (no entries before 23:00 CET). SIP bars + real books:

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| ELAB | [TV](https://www.tradingview.com/chart/?symbol=ELAB) | $1.06 | +0.0% | +19.8% | $1.27 | +19.8% | 2.5M | 5.9M | 0.4x | 4.5M | Biotechnology |
| AEHL | [TV](https://www.tradingview.com/chart/?symbol=AEHL) | $1.07 | +8.6% | +15.9% | $1.24 | +25.8% | 599K | 176K | 3.4x | 15.4M | Building Products |
| PMA | [TV](https://www.tradingview.com/chart/?symbol=PMA) | $1.29 | +3.2% | +10.1% | $1.42 | +13.6% | 90K | 2.0M | 0.0x | 4.6M | Engineering & Construction |

**SIP bars (5Min, from 20:00Z / 16:00 ET) + real books:**
- **AEHL** — BUILD pattern. $1.07→$1.10→$1.26→$1.41, vol accelerating 13K→32K→641K→1.4M sh, trades 54→102→3079→7338, new high $1.49 in latest bar. Real accumulation. Book bid $1.14 x100 / ask $1.53 x100 (wide). Strongest candidate into 23:00 — watch for continued build. Float 15.4M, Building Products (non-bio).
- **ELAB** — SPIKE→FADE. Peaked $1.44 in first bar (16:00-16:05 ET) on 418K sh, huge 1.6M-sh second bar, now settling $1.26-1.28. Early peak, fading off high. Tight book bid $1.21 x200 / ask $1.22 x100. Float 4.5M biotech. Early-peak fade — low priority.
- **PMA** — building on lighter volume. $1.34→$1.54, vol 49K→17K→39K→245K sh. Book bid $1.16 / ask $1.57 (wide). Float 4.6M. Lower conviction than AEHL.

**Notes:**
- No entries (observation-only scan). AEHL is the lead BUILD candidate; ELAB fading; PMA weak build.
- Catalyst searches deferred to 23:00 entry scan (search budget). Re-evaluate all three at 23:00 CET with fresh bars + catalyst check.

## Scan 23:00 CET (5:00 PM ET)

**AH entry scan** — 7 hits. Entries allowed (23:00+ CET). SIP bars (5Min from 20:00Z / 16:00 ET, fresh to 16:45 ET) + real books:

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| PMA | [TV](https://www.tradingview.com/chart/?symbol=PMA) | $1.29 | +3.2% | +20.9% | $1.56 | +24.8% | 2.3M | 2.3M | 1.0x | 4.6M | Engineering & Construction |
| ELAB | [TV](https://www.tradingview.com/chart/?symbol=ELAB) | $1.06 | +0.0% | +15.6% | $1.23 | +15.6% | 4.1M | 6.1M | 0.7x | 4.5M | Biotechnology |
| ZNB | [TV](https://www.tradingview.com/chart/?symbol=ZNB) | $0.51 | +1.8% | +16.5% | $0.59 | +18.6% | 2.2M | 2.3M | 0.9x | 1.6M | Internet Software/Services |
| ELPW | [TV](https://www.tradingview.com/chart/?symbol=ELPW) | $0.57 | -12.0% | +15.8% | $0.66 | +1.9% | 602K | 2.1M | 0.3x | 1.4M | Electrical Products |
| WRAP | [TV](https://www.tradingview.com/chart/?symbol=WRAP) | $2.36 | +48.4% | +6.8% | $2.52 | +58.5% | 514K | 6.4M | 0.1x | 37.9M | Medical Specialties |
| THRY | [TV](https://www.tradingview.com/chart/?symbol=THRY) | $4.32 | +5.9% | +8.5% | $4.69 | +14.9% | 118K | 710K | 0.2x | 40.2M | Packaged Software |
| RYOJ | [TV](https://www.tradingview.com/chart/?symbol=RYOJ) | $3.88 | +31.5% | +5.7% | $4.10 | +39.0% | 72K | 1.2M | 0.1x | 2.3M | Medical/Nursing Services |

**SIP bars (5Min) + books:**
- **PMA** — BUILD-and-hold. Gapped to $1.74 at open (+39% from prior ~$1.25), faded all day to $1.29 close (+3.2%), then AH built to a *new* high $1.80 at 16:35 ET (above the intraday high $1.745). Vol accelerating: 50K→245K→341K→744K→751K→266K→434K sh, trades to 3798/4714. Holding ~$1.62 (~11% off high = within 20% → hold). SIP corroborates (H $1.80, no bad print). Book bid $1.16 / ask $1.57 (wide but sized). Float 4.6M. **ENTERED.**
- **ELAB** — SPIKE→FADE. Peaked $1.44 in first bar (16:00 ET) on 419K sh, huge 1.6M-sh second bar, now settling $1.24. Early-peak fade. Tight book bid $1.24/ask $1.25. Skip per trajectory rule (0/7+ PM continuation).
- **ZNB** — strong SIP build ($0.51→$0.70 new highs, 1.7M sh/5005 trades latest bar) BUT `quote ask $0.00 x0` = **no fillable AH book**. Skip as illiquid (no AH book) per liquidity sanity check. Also only 1 AH scan.
- **AEHL** (22:30 lead) — dropped from scan; SIP shows collapse $1.49 (16:15 ET) → $1.04 (~30% off high, round-trip below close). Faded spike. Skip.
- **ELPW** — Day -12%, Total only +1.9%, thin (602K vs 2.1M avg), 1 scan. Skip.
- **WRAP / THRY / RYOJ** — AH Chg <10% gate (6.8% / 8.5% / 5.7%). Skip.

**Catalyst (PMA):** Former ticker **MSW** (Ming Shing Group, HK wet-trades construction) — documented prior BUILD-and-hold winner (+31% over entry). MSW acquired *PMA Nano Carbon Tech Limited* (closed Jun 9) via stock purchase + **convertible promissory notes** (dilutive), and the Nasdaq ticker changed **MSW→PMA effective today (Jul 9)**. Today's trigger is the ticker-change/rebrand — a weak/symbolic catalyst with dilution overhang, not fresh operational news. **Grade C** (leaning None), dilution concern noted → exit premarket.

**Decision:** Enter PMA. Passes all gates — float 4.6M (<10M), AH >10% in 2 AH scans (22:30 +10.1%, 23:00 +20.9%, building), Day% +3.2 (>-15%), Total% +24.8 (<150 ceiling), BUILD-and-hold, real SIP accumulation, fillable/tradable, SIP corroborates price. Weak-catalyst concern noted per learning-phase rule. All others fail a gate.

**Order:** BUY 60 PMA @ limit $1.68 ext (id bfc7adfc) — **filled @ $1.66**. Cost $99.60. Grade C.

## Scan 23:30 CET (5:30 PM ET)

**AH entry scan** — 7 hits. Entries allowed. SIP bars (5Min from 20:00Z / 16:00 ET, fresh to 17:15 ET) + real books:

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| ELPW | [TV](https://www.tradingview.com/chart/?symbol=ELPW) | $0.57 | -12.0% | +78.5% | $1.01 | +57.1% | 10.0M | 3.1M | 3.3x | 1.4M | Electrical Products |
| PMA | [TV](https://www.tradingview.com/chart/?symbol=PMA) | $1.29 | +3.2% | +33.3% | $1.72 | +37.6% | 5.2M | 2.6M | 2.0x | 4.6M | Engineering & Construction |
| ELAB | [TV](https://www.tradingview.com/chart/?symbol=ELAB) | $1.06 | +0.0% | +17.0% | $1.24 | +17.0% | 4.7M | 6.2M | 0.8x | 4.5M | Biotechnology |
| WRAP | [TV](https://www.tradingview.com/chart/?symbol=WRAP) | $2.36 | +48.4% | +11.4% | $2.63 | +65.4% | 1.9M | 6.6M | 0.3x | 37.9M | Medical Specialties |
| RKTO | [TV](https://www.tradingview.com/chart/?symbol=RKTO) | $0.91 | +13.4% | +5.0% | $0.96 | +19.1% | 1.3M | 15.3M | 0.1x | 21.7M | Pharmaceuticals: Major |
| WNW | [TV](https://www.tradingview.com/chart/?symbol=WNW) | $3.32 | -6.2% | +14.8% | $3.81 | +7.6% | 345K | 195K | 1.8x | 23.7M | Internet Retail |
| DSS | [TV](https://www.tradingview.com/chart/?symbol=DSS) | $0.61 | -0.0% | +8.2% | $0.66 | +8.2% | 112K | 84K | 1.3x | 3.9M | Commercial Printing/Forms |

**SIP bars (5Min) + books:**
- **ELPW** — strong late BUILD. Flat $0.57–0.63 until 16:40 ET, then accelerated: 16:55 ET bar 2.4M sh/6466 trades ($0.67→$0.89), then 2.1M / 2.2M / 2.9M / 3.6M sh across bars, price $0.89→$1.01→new high $1.12 at 17:15 ET (last bar, 10,139 trades). Massive real accumulation, still making new highs after 17:00 ET. Float 1.4M (post 1-for-80 reverse split). Day -12% (NOT ≤-15%, dead-cat filter does not apply); Total +57.1% (under 150 ceiling). Quote frozen/stale at 16:59 ET (bid $0.70 / ask $7.00 garbage) — **freshness guard**: strong signal (VRatio 3.3, AH +78.5%, built across 2 AH scans), stale quote is not a bad print / not an illiquid book; SIP shows real fillable liquidity (10k+ trades/bar). **ENTERED** (limit fill confirmed real book).
- **PMA** (already entered 23:00 @ $1.66) — continued build, AH now +33.3% / $1.72, 5.2M AH vol. Holding. No action (one entry per candidate per night).
- **ELAB** — still SPIKE→FADE from 16:00 ET peak $1.44. Skip per trajectory rule.
- **WNW** — AH +14.8% but Total only +7.6% (Day -6.2%), 1 AH scan, float 23.7M. Weak/single-scan. Skip.
- **RKTO / DSS** — AH Chg <10% gate (5.0% / 8.2%). Skip.

**Catalyst (ELPW):** Discounted **US$6.0M public offering** (dilution — crashed the stock ~52% on pricing) + a **1-for-80 reverse share consolidation** (source of the tiny 1.4M float). Catalyst is negative/dilutive → **Grade D**. But the AH move is a genuine low-float squeeze on real volume, a clear BUILD peaking after 17:00 ET. Per learning-phase rule, trajectory (BUILD, 5/5) overrides catalyst; dilution concern noted → exit at first premarket opportunity.

**Decision:** Enter ELPW. Passes gates — float 1.4M (<10M), AH >10% in 2 AH scans (23:00 +15.8%, 23:30 +78.5%, building), Day% -12 (>-15), Total% +57.1 (<150), strong late BUILD, real SIP accumulation, tradable, freshness-guarded fillable book. Grade D catalyst → hold-to-first-PM.

**Order:** BUY 83 ELPW @ limit $1.20 ext (id fdb8f5d7) — **filled @ $1.18**. Cost $97.94. Grade D.

## Scan 00:00 CET (6:00 PM ET)

**AH entry scan** — 6 hits. Entries allowed. Two positions already open (PMA @ $1.66, ELPW @ $1.18 — management deferred to premarket position-evaluation). SIP bars (5Min from 20:00Z / 16:00 ET, fresh to 17:45 ET) + real books:

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| ELPW | [TV](https://www.tradingview.com/chart/?symbol=ELPW) | $0.57 | -12.0% | +89.1% | $1.07 | +66.5% | 25.7M | 4.7M | 5.4x | 1.4M | Electrical Products |
| PMA | [TV](https://www.tradingview.com/chart/?symbol=PMA) | $1.29 | +3.2% | +17.9% | $1.52 | +21.6% | 6.2M | 2.7M | 2.3x | 4.6M | Engineering & Construction |
| ELAB | [TV](https://www.tradingview.com/chart/?symbol=ELAB) | $1.06 | +0.0% | +19.3% | $1.26 | +19.3% | 6.2M | 6.3M | 1.0x | 4.5M | Biotechnology |
| WRAP | [TV](https://www.tradingview.com/chart/?symbol=WRAP) | $2.36 | +48.4% | +5.9% | $2.50 | +57.2% | 2.3M | 6.6M | 0.3x | 37.9M | Medical Specialties |
| WNW | [TV](https://www.tradingview.com/chart/?symbol=WNW) | $3.32 | -6.2% | +16.0% | $3.85 | +8.8% | 430K | 207K | 2.1x | 23.7M | Internet Retail |
| YYGH | [TV](https://www.tradingview.com/chart/?symbol=YYGH) | $1.37 | -3.5% | +13.1% | $1.55 | +9.2% | 93K | 838K | 0.1x | 133K | Misc Commercial Services |

**SIP bars (5Min) + books:**
- **YYGH** (NEW) — fresh late BUILD. Dead all afternoon (1-3 trades/bar) until 17:35 ET, then exploded: 17:35 ET 14.9K sh/26 trades → 17:40 ET 86K sh/634 trades ($1.41→$1.68) → 17:45 ET 470K sh/3115 trades ($1.55→$1.87 new high). Real accelerating accumulation, tiny 133K float. Scanner VRatio 0.1x is **stale** (missed the explosion); SIP confirms the real spike. Quote bid $1.16/ask $1.56 stale (16:00 ET timestamp) — freshness guard, not a bad print. **BUT this is YYGH's first AH scan >10%** — fails the 2-AH-scan entry gate. **Skip entry, flag as strong WATCH for 00:30 CET.** Tradable=true.
- **WNW** — SPIKE→FADE. Peaked $4.50 at 16:15 ET (early, on 130K sh), choppy fade since; secondary push to $4.18 at 17:25 ET then declining $3.97→$3.93→$3.85→$3.87 into 17:45 ET. Early peak before 17:30 + declining trajectory (0/10+ PM continuation). Float 23.7M (large), Day -6.2%, Total +8.8%, China internet-retail small cap. 2 AH scans (23:30 +14.8%, 00:00 +16.0%) so passes 2-scan gate, but SPIKE→FADE dominates → **skip**.
- **ELPW** (open position @ $1.18) — AH now +89.1% / $1.07, VRatio 5.4x, still the strongest AH mover. No new entry (one entry per candidate; position now -21%, management deferred to premarket).
- **PMA** (open position @ $1.66) — AH +17.9% / $1.52, holding. No action (position -9.6%, deferred to premarket).
- **ELAB** — still SPIKE→FADE from 16:00 ET peak $1.44. Skip (0/7+).
- **WRAP** — AH +5.9% < 10% gate, float 37.9M. Skip.

**Catalyst (YYGH):** YY Group Holdings (Singapore facility-management / AI). Driver is a **30-for-1 reverse stock split** effective ~Jun 18 — explains the 133K float and rebasing from ~$0.14 to ~$1.37. Earlier PRs (OpenClaw agentic AI, humanoid-robotics initiative) are weeks old. No fresh same-day (Jul 9) operational catalyst found — low-float post-reverse-split squeeze. **No catalyst found** (concern noted; not a skip reason, but moot this scan on the 2-scan gate).

**Decision: No new entries this scan.** WNW is the only 2-scan qualifier and it's SPIKE→FADE (skip-all on a SPIKE→FADE-only qualifier). YYGH is a fresh, real, tiny-float BUILD but on its first AH scan — the strongest watch for 00:30 CET; if it prints a 2nd AH scan >10% while holding/building, it's a prime entry (float 133K, late build after 17:30 ET, real accumulation). Held positions PMA/ELPW unchanged.

## Scan 00:30 CET (6:30 PM ET)

**AH entry scan** — 8 hits. Entries allowed. Two positions open (PMA @ $1.66, ELPW @ $1.18). SIP bars (5Min from 20:00Z / 16:00 ET, fresh to 18:15 ET) + real books:

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| YYGH | [TV](https://www.tradingview.com/chart/?symbol=YYGH) | $1.37 | -3.5% | +39.4% | $1.91 | +34.5% | 2.5M | 1.1M | 2.2x | 133K | Misc Commercial Services |
| ELPW | [TV](https://www.tradingview.com/chart/?symbol=ELPW) | $0.57 | -12.0% | +49.8% | $0.85 | +31.8% | 32.7M | 5.5M | 6.0x | 1.4M | Electrical Products |
| ELAB | [TV](https://www.tradingview.com/chart/?symbol=ELAB) | $1.06 | +0.0% | +23.6% | $1.31 | +23.6% | 6.7M | 6.4M | 1.0x | 4.5M | Biotechnology |
| PMA | [TV](https://www.tradingview.com/chart/?symbol=PMA) | $1.29 | +3.2% | +13.2% | $1.46 | +16.8% | 6.5M | 2.8M | 2.4x | 4.6M | Engineering & Construction |
| WRAP | [TV](https://www.tradingview.com/chart/?symbol=WRAP) | $2.36 | +48.4% | +7.2% | $2.53 | +59.1% | 2.4M | 6.6M | 0.4x | 37.9M | Medical Specialties |
| HCTI | [TV](https://www.tradingview.com/chart/?symbol=HCTI) | $1.91 | +12.4% | +5.7% | $2.02 | +18.8% | 531K | 554K | 1.0x | 1.9M | IT Services |
| WNW | [TV](https://www.tradingview.com/chart/?symbol=WNW) | $3.32 | -6.2% | +18.1% | $3.92 | +10.7% | 454K | 210K | 2.2x | 23.7M | Internet Retail |
| PEPG | [TV](https://www.tradingview.com/chart/?symbol=PEPG) | $2.30 | +15.6% | +5.1% | $2.42 | +21.5% | 170K | 858K | 0.2x | 60.7M | Biotechnology |

**SIP bars (5Min) + books:**
- **YYGH** (NEW entry) — the WATCH flagged at 00:00 CET now on its 2nd AH scan >10% (00:00 +13.1%, 00:30 +39.4%). SIP confirms real accelerating BUILD: dead until 17:35 ET, then 15K→86K→470K→357K→353K→325K→531K→686K sh/bar, trades to 4155, new high **$2.00 at 18:10 ET** (late peak, historically 4/4 for PM continuation). Latest fresh bar 18:15 ET reversed O $1.91 H $1.94 L $1.60 C $1.60 on 565K sh (~20% off the $2.00 high — noted risk). Scan-over-scan still rising ($1.55 00:00 → $1.60 real / $1.91 lagged). Quote stale (bid $1.16/ask $1.56 @ 16:00 ET) — freshness guard: not a bad print, SIP shows real fillable liquidity (3.5k trades/bar). Float 133K (extreme low). **ENTERED.**
- **ELPW** (open position @ $1.18) — AH now +49.8% / $0.85 (faded from +89% peak $1.12 at 17:15 ET). VRatio 6.0x. No new entry (one per candidate; position -28.5%, management deferred to premarket).
- **PMA** (open position @ $1.66) — AH +13.2% / $1.46, faded from earlier. No action (position -12.7%, deferred to premarket).
- **ELAB** — still SPIKE→FADE from 16:00 ET peak $1.44. Skip (0/7+).
- **WNW** — SPIKE→FADE (peaked $4.50 at 16:15 ET, still fading), float 23.7M, Total +10.7%. Skip.
- **WRAP / HCTI / PEPG** — AH Chg <10% gate (7.2% / 5.7% / 5.1%). Skip.

**Catalyst (YYGH):** YY Group Holdings (Singapore facility-management / AI). Driver is the **30-for-1 reverse stock split** (~Jun 18) that produced the 133K float; earlier PRs (OpenClaw agentic AI, humanoid-robotics) are weeks old. No fresh same-day (Jul 9) operational catalyst — low-float post-reverse-split squeeze. **Grade None** (concern noted; not a skip reason during learning phase) → exit at first premarket opportunity.

**Decision:** Enter YYGH. Clears all gates — float 133K (<10M), AH >10% in 2 AH scans (00:00 +13.1%, 00:30 +39.4%, building), Day% -3.5 (>-15), Total% +34.5 (<150 ceiling), late BUILD peaking 18:10 ET on real SIP accumulation, tradable, freshness-guarded fillable book. Fade risk from the last reversal bar noted. Grade None → hold-to-first-PM. All others fail a gate.

**Order:** BUY 58 YYGH @ limit $1.70 ext (id 10a73764) — **filled @ $1.66**. Cost $96.28. Grade None.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
| PMA | $1.66 | 2026-07-09 17:00 ET | 60 | bfc7adfc | BUILD-and-hold, float 4.6M, AH +20.9% (2 scans), Total +24.8%. Grade C (ticker rebrand MSW→PMA + dilutive convertibles). |
| ELPW | $1.18 | 2026-07-09 17:30 ET | 83 | fdb8f5d7 | Late BUILD low-float squeeze, float 1.4M, AH +78.5% (2 scans), Total +57.1%. Grade D ($6M discounted offering + 1:80 reverse split). |
| YYGH | $1.66 | 2026-07-09 18:30 ET | 58 | 10a73764 | Late BUILD low-float squeeze, float 133K, AH +39.4% (2 scans), Total +34.5%, peak $2.00 @ 18:10 ET. Grade None (30:1 reverse split, no fresh catalyst). |

## Morning Evaluation — 10:20 CET

### Today's Winner

**GMM** — Global Mofy AI Limited (Packaged Software / AI, China)
- Catalyst: unverified — no fresh same-day PR confirmed in scan window; tiny-float (1.7M) AI-metaverse name, classic low-float squeeze profile. Grade None pending news check.
- Previous Close: $1.85
- AH last night: flat through 17:45 ET, then late BUILD — $2.10 (+13%) at 18:00 ET → SIP peak **$3.50 at 19:00 ET** (Yahoo $3.33, +79.9%). SIP-confirmed real liquidity: 276K sh @18:35 ET, **925K sh / 7621 trades @18:40 ET**, 700K+ sh/bar through 19:00 ET. No bad print.
- Premarket now: $3.55–3.74 (+92% to +102%); **PM peak SIP $4.07 @04:05 ET** (+120%), 1.5M sh/bar, 21k trades.
- Hypothetical P&L (AH volume-confirmed entry $2.50 @18:35 ET → PM peak $4.07): **+63%** (from first 10% cross $2.10 → +94%)
- Float: 1.7M | Market Cap: $3.6M

**Scanner Diagnostic:**
- Detectable at screening time (~22:15 CET / 16:15 ET)? **NO** — GMM was flat at $1.85 (0%) through 17:45 ET; the move started only at 18:00 ET.
- At the last scheduled scan (00:30 CET / 18:30 ET) GMM was +22% ($2.26) but on negligible cumulative AH volume (~66K vs 703K avg, VRatio ~0.1) — below the scanner's volume/VRatio gate, so correctly not surfaced. The volume-confirmed explosion (276K→925K sh/bar) fired 18:35–19:00 ET, **after** the last scan.
- Classification: **late-AH-tail surge (true-tail)**. Decisive volume-backed move fired in the unscanned 18:30–20:00 ET tail. Not a detection-threshold miss; **not counted against the detection baseline.** Nuance: price was technically already +22% at 18:30 ET, but the scanner requires volume confirmation, which arrived after the last scan — so this leans true-tail (a late scan would have helped), not feed-lag.
- Scanner gap: a late scan at ~01:00 CET (19:00 ET) would have caught GMM at $3.33 +80% on 700K+ sh/bar. Adds to the late-AH-tail dataset (see Notes).

### Baseline Tracking

- Days tracked: **46** (was 45 + 1)
- Winners detected by scanner: **39/44 (88.6%)** — GMM excluded from denominator (late-AH-tail surge, decisive move after last scan; not counted against baseline).
- Winner selected for paper trade: **22/44 (50.0%)** — GMM not selectable (surged after last scan).
- Target: >80% detection
- Status: **BASELINE MET**

### Retrospective Scan Results

Live PM scan (04:20 ET) top hits: **GMM +95.7% ($3.62)**, ELPW +83.7% ($1.04, held), ELAB +20.8%, WOK +18.3%, PMA +8.7% (held). GMM AH reconstruction (Yahoo `--ah-history` + SIP bars) confirms the AH→PM continuation above. No forced AH scan needed — SIP bars give the definitive AH footprint.

### Open Position P&L (Alpaca)

Three positions carried from last night's entries. **All Alpaca quotes are stale (20:00 ET regular close);** P&L reported against live PM. Exits handled by position-evaluation (10:30 / 14:30 CET), not here.

| Ticker | Entry | Entry Total% | Catalyst | Entry Time | Live PM | From Entry | Status |
|--------|-------|--------------|----------|------------|---------|------------|--------|
| ELPW | $1.18 | +57.1% | D — $6M offering + 1:80 reverse split | 17:30 ET | ~$1.03 (+61% from close, faded from AH peak $1.27) | **−12.7%** | Holding |
| PMA  | $1.66 | +24.8% | C — MSW→PMA rebrand + convertibles | 17:00 ET | ~$1.45 (PM range $1.42–1.63) | **−12.7%** | Holding |
| YYGH | $1.66 | +34.5% | None — 30:1 reverse split, no fresh PR | 18:30 ET | ~$1.40 (PM range $1.38–1.42) | **−15.7%** | Holding |

Alpaca stale figures were ELPW $1.01 / PMA $1.47 / YYGH $1.39 (all @20:00 ET close). **No executed exits yet** — no realized P&L. All three faded from AH peaks into PM (ELPW AH $1.27→PM $1.03; the AH peak was the better exit on the low-float squeezes).

**Total Realized P&L (Alpaca fills only): €0.00** (no exits).

### Scanner Effectiveness

- Evening scans ran: **7 of 7** (21:30 – 00:30 CET). No coverage failure.
- Candidates found: PMA, ELPW, YYGH (entered), plus WNW, ELAB, AEHL, WRAP/HCTI/PEPG (skipped).
- Retrospective match on winner: **GMM not in any of the 7 scans** — surfaced only in the 18:30–20:00 ET tail after the last scan.

### Missed Opportunities

| Ticker | AH Change | Why Missed | Would Be Profitable? |
|--------|-----------|------------|---------------------|
| GMM | +80% (peak 19:00 ET) | Late-AH-tail: flat through 17:45 ET; volume-confirmed surge fired 18:35–19:00 ET, after the 00:30 CET last scan | Yes — hypo AH $2.50 → PM peak $4.07 = **+63%** |

### AH Mover Follow-Through

| Ticker | AH Peak | Peak Time | AH Trajectory | Current PM | From Peak | From Close | Verdict |
|--------|---------|-----------|---------------|------------|-----------|------------|---------|
| ELPW | $1.27 | 17:30 ET | Spike→fade | ~$1.03 | −19% | +61% | AH peak was better exit; faded overnight |
| PMA  | $1.80 | 16:35 ET | Build→fade | ~$1.45 | −19% | +12% | Faded from AH high into PM |
| YYGH | $2.00 | 18:10 ET | Late build→fade | ~$1.40 | −30% | +9% | Late-build peak faded hard; AH peak was exit |
| WNW  | $4.50 | 16:15 ET | Spike→fade | faded | — | — | Correctly skipped (SPIKE→FADE, float 23.7M) |
| ELAB | $1.44 | 16:00 ET | Spike→fade | ~$1.28 | −11% | +21% | Correctly skipped (early-peak fade) |

**AH-peak-vs-PM-peak check:** All held names (ELPW/PMA/YYGH) peaked in AH and faded into PM — AH was the better exit on each. None reached the >250%-from-close extreme-runner bar (extreme-runner tally unchanged). GMM (winner) is the exception: PM peak $4.07 **exceeded** AH peak $3.50 — a true AH→PM continuation, not an AH-peak fader.

### Price Charts

```
GMM — flat $1.85 through 17:45 ET → late BUILD to $3.33/$3.50 SIP @19:00 ET (+80%)
      → held ~$2.75-3.20 overnight → PM peak $4.07 @04:05 ET (+120%). 2-day range $1.83-$4.10.
      Decisive volume: 925K sh/7621 trades @18:40 ET (after 00:30 CET last scan).
```

### Notes

- **Late-AH-tail tally (add GMM):** ORIS (Jun 22, true-tail), BTCT (Jun 29→30, feed-lag), **GMM (Jul 9→10, true-tail)** — flat through 17:45 ET, +22% at 18:30 ET last scan but on ~66K sh (VRatio ~0.1, below volume gate), volume-confirmed surge to +80% fired 18:35–19:00 ET; hypo AH-tail entry $2.50 → PM peak $4.07 = **+63%**. **True-tail count now 2** (ORIS, GMM). Threshold to propose a late scan (~01:00/01:30 CET) is ≥3–4 true-tail winners — 2 of ≥3–4, watch. One more true-tail tail-surge reaches the flag.
- **PM-only gapper tally:** biggest raw PM mover today = **GMM +102%**, an **AH→PM continuation** (moved +80% in AH), not a PM-only gapper. No holdable PM-only blind spot today.
- **Fade-rule false-negative tally:** no new sub-3M case tonight. WNW faded as predicted (float 23.7M — high-float negative control); ELAB faded (float 4.5M). **Standing sub-3M count unchanged: 3 of 4** (LNKS, RPGL, CRE blew past; IOTR fell short).
- **Coverage tally:** 7/7 scans ran. No coverage failure. No CEILING-OVERRIDE or DEAD-CAT-OVERRIDE watches were flagged last night.
- **Held-position pattern:** all three entries (ELPW/PMA/YYGH) were AH BUILDs that peaked in AH and faded overnight into PM (each now −13% to −16% from entry). Consistent with prior observation that low-float AH squeezes often top in after-hours; the fade-into-PM on these mirrors the SPIKE→FADE names we skip. Data point for position-evaluation, not acted on here.
- **Prev-winner watch:** IOTR bounced $2.53→$3.54 (Day-2 dead-cat bounce); RPGL faded $2.90→$1.78; TDIC ~$3.98 (flat).
