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

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
| PMA | $1.66 | 2026-07-09 17:00 ET | 60 | bfc7adfc | BUILD-and-hold, float 4.6M, AH +20.9% (2 scans), Total +24.8%. Grade C (ticker rebrand MSW→PMA + dilutive convertibles). |
| ELPW | $1.18 | 2026-07-09 17:30 ET | 83 | fdb8f5d7 | Late BUILD low-float squeeze, float 1.4M, AH +78.5% (2 scans), Total +57.1%. Grade D ($6M discounted offering + 1:80 reverse split). |
