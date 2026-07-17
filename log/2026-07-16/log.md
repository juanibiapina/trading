# 2026-07-16

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
| BIYA | $4.55 | 23:46 CET (5:46 PM ET) | 22 | 2c02d728 | Qualified all gates (2 AH scans >10%, float 2.7M, Day -8.4%, Total +48% <150%), HOLD trajectory. Grade None (no catalyst). Order submitted 23:30, filled 23:46. |
| CJMB | $1.01 | 00:30 CET (6:30 PM ET) | 95 | 49b582bf | Qualified all gates (2 AH scans >10%: 00:00 +26.6%, 00:30 +19.5%; Day +16.5%; Total +39.2% <150%), late-BUILD post-17:30 peak, holding within 20% of high. Grade B (Jul 16 ASU partnership PR). Filled @ $1.01. |

## Scan 00:30 CET (6:30 PM ET) — AFTERHOURS (entry-eligible, FINAL SCAN)

Scanner returned 9 hits. CJMB now clears the 2-AH-scan gate as a late-BUILD with a fresh same-day catalyst — **ENTERED.** GCTK cleared the gate but remains an early-peak fade / re-pump. LBGJ now has 2 AH scans but is a thin illiquid ramp. SIP feed stale ~45 min (last bar 17:45 ET vs 18:30 ET scan) — freshness guard applied, leaned on scanner + SIP-up-to-17:45.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| GCTK | [TV](https://www.tradingview.com/chart/?symbol=GCTK) | $0.50 | -5.5% | +35.7% | $0.68 | +28.2% | 19.5M | 14.5M | 1.3x | 6.2M | Medical Specialties |
| JSPR | [TV](https://www.tradingview.com/chart/?symbol=JSPR) | $0.77 | +11.8% | +7.2% | $0.83 | +20.0% | 9.1M | 1.9M | 4.8x | 25.2M | Biotechnology |
| PMAX | [TV](https://www.tradingview.com/chart/?symbol=PMAX) | $1.76 | +6.0% | +12.5% | $1.98 | +19.3% | 6.5M | 886K | 7.3x | 892K | Specialty Telecommunications |
| BIYA | [TV](https://www.tradingview.com/chart/?symbol=BIYA) | $3.04 | -8.4% | +48.0% | $4.50 | +35.5% | 4.5M | 1.7M | 2.7x | 2.7M | Personnel Services |
| CJMB | [TV](https://www.tradingview.com/chart/?symbol=CJMB) | $0.86 | +16.5% | +19.5% | $1.03 | +39.2% | 3.4M | 607K | 5.6x | 0 | Air Freight/Couriers |
| GLXG | [TV](https://www.tradingview.com/chart/?symbol=GLXG) | $1.07 | -14.4% | +19.6% | $1.28 | +2.4% | 1.9M | 285K | 6.8x | 1.7M | Miscellaneous Commercial Services |
| STXS | [TV](https://www.tradingview.com/chart/?symbol=STXS) | $1.65 | +1.9% | +12.7% | $1.86 | +14.8% | 1.0M | 1.1M | 0.9x | 80.4M | Medical Specialties |
| VCIG | [TV](https://www.tradingview.com/chart/?symbol=VCIG) | $1.08 | -32.1% | +16.7% | $1.26 | -20.8% | 877K | 258K | 3.4x | 4.4M | Miscellaneous Commercial Services |
| LBGJ | [TV](https://www.tradingview.com/chart/?symbol=LBGJ) | $2.19 | +19.7% | +24.2% | $2.72 | +48.6% | 451K | 769K | 0.6x | 3.0M | Home Furnishings |

**Gate evaluation (all times ET; SIP bars from 16:00 ET / 20:00Z; quote feed frozen @16:00 ET / 20:00Z — leaned on SIP + scanner per freshness guard):**
- **CJMB** — **QUALIFIES on all gates. ENTERED (filled @ $1.01).** 2 AH scans >10% (00:00 +26.6%, 00:30 +19.5%); Day +16.5% (well above -15%); Total +39.2% (below 150% ceiling); float unknown (scanner 0, not a filter), MCap $4.9M. SIP confirms real late-BUILD: dead $0.79-0.86 until 17:30 ET, then exploded $0.79→$1.05, peaked **$1.13 at 17:40 ET** (post-17:30, favorable timing) on 1.07M sh / 5336 trades; last SIP bar 17:45 ET $0.98; scanner at 18:30 shows $1.03 (fresher than SIP, above the last bar, within 20% of the $1.13 high). ~2.7M sh across the surge, thousands of trades/bar — real accumulation, not a stale VRatio. Two-sided fillable book (bid $0.72 / ask $0.97 x100; timestamp stale @16:00 ET = frozen-feed artifact, not $0 x0). tradable=true. **Trajectory: late-BUILD holding near AH high.** Catalyst: **same-day Jul 16 GlobeNewswire PR** — strategic partnership with Alabama State University to advance US pharmaceutical manufacturing and supply-chain resilience (integrated pharma manufacturing ecosystem at the Atlas Complex). Solid partnership news → **Grade B** (hold up to 2 days, stop -15%). BUY 95 CJMB @ limit $1.10 ext (id 49b582bf) → filled @ $1.01. QTY sized ~$100 on real price. Added to OPEN_POSITIONS.md.
- **BIYA** — **already held (filled @ $4.55, 23:46 CET).** Still building: +48.0% AH ($4.50) vs +37.5% at entry; position +8.7% at scan time. One entry per candidate per night — no re-entry. Premarket position-eval manages the exit. Grade None.
- **GCTK** — **Clears the 2-AH-scan gate (23:30 +41.4%, 00:00 +29.8%, 00:30 +35.7%) but SKIP on trajectory (early-peak fade + re-pump).** SIP: peaked **$0.80 at 17:20 ET** (before 18:30), then declined $0.74→$0.70→$0.66→$0.65 (last bar 17:40 ET) on collapsing volume (2.2M→628K sh/bar). Scanner at 18:30 $0.68 — slight tick up but still -15-19% off the high, AH% choppy (41.4→29.8→35.7), not a clean build to new highs. Early peak becomes a disqualifier when the name is also declining across scans — GCTK is. Added: GCTK was **traded 07-14 and dumped -37.6%** (reverse-merger that behaved like dilution); this is a re-pump of an already-dumped name, not a fresh catalyst build. Skip.
- **LBGJ** — **2 AH scans now (00:00 +16.4%, 00:30 +24.2%) but SKIP: illiquid ramp.** VRatio 0.6x (below avg vol); SIP flat $2.05-2.20 on hundreds of sh/bar most of AH, then a thin spike to $2.78 at 17:40 ET (only 47K sh / 428 trades). Wide two-sided book (bid $1.81 / ask $2.51) = thin. Real accumulation absent. Skip — illiquid ramp.
- **PMAX** — QUALIFIES on gates but SPIKE→FADE confirmed (peaked $2.36 at 16:25 ET, faded, now $1.98). Skip.
- **GLXG** — Total +2.4%, Day -14.4%, faded from early peak, dilution/shelf risk. Skip.
- **VCIG** — Day -32.1%, Total -20.8% (AH below regular close). Dead-cat. Skip.
- **STXS** — float 80.4M, VRatio 0.9x. Not a candidate.
- **JSPR** — new, AH +7.2% (below the 10% gate), float 25.2M, biotech. Not entry-eligible.

**Final-scan feed-lag cross-check:** All tracked names (BIYA, GCTK, PMAX, GLXG, VCIG, STXS, LBGJ, CJMB) appeared in the fresh 18:30 ET scan — no under-reported/omitted names to rescue via SIP. JSPR is a new sub-gate name.

**Decision: ENTER CJMB (qualifies on all gates, late-BUILD, Grade B ASU partnership catalyst). Filled @ $1.01.** BIYA already held and building (no re-entry). GCTK cleared the gate but is an early-peak fade / re-pump — skip. LBGJ thin/illiquid — skip. No override flags on any skipped name (none is Day% ≤-15% with a reclaim, none exceeds +150% Total%). Night ends with 2 open positions: BIYA (Grade None) and CJMB (Grade B). Premarket position-evaluation manages both exits.

## Scan 00:00 CET (6:00 PM ET) — AFTERHOURS (entry-eligible)

Scanner returned 9 hits. BIYA (already held) building further; GCTK now clears the 2-AH-scan gate but has rolled over; CJMB is a fresh late-BUILD name.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| GCTK | [TV](https://www.tradingview.com/chart/?symbol=GCTK) | $0.50 | -5.5% | +29.8% | $0.65 | +22.7% | 16.4M | 14.1M | 1.2x | 6.2M | Medical Specialties |
| PMAX | [TV](https://www.tradingview.com/chart/?symbol=PMAX) | $1.76 | +6.0% | +11.4% | $1.96 | +18.1% | 6.2M | 859K | 7.3x | 892K | Specialty Telecommunications |
| BIYA | [TV](https://www.tradingview.com/chart/?symbol=BIYA) | $3.04 | -8.4% | +53.6% | $4.67 | +40.7% | 4.0M | 1.6M | 2.5x | 2.7M | Personnel Services |
| CJMB | [TV](https://www.tradingview.com/chart/?symbol=CJMB) | $0.86 | +16.5% | +26.6% | $1.09 | +47.5% | 2.0M | 459K | 4.4x | 0 | Air Freight/Couriers |
| GLXG | [TV](https://www.tradingview.com/chart/?symbol=GLXG) | $1.07 | -14.4% | +19.6% | $1.28 | +2.4% | 1.9M | 279K | 6.8x | 1.7M | Miscellaneous Commercial Services |
| STXS | [TV](https://www.tradingview.com/chart/?symbol=STXS) | $1.65 | +1.9% | +15.2% | $1.90 | +17.3% | 882K | 1.1M | 0.8x | 80.4M | Medical Specialties |
| VCIG | [TV](https://www.tradingview.com/chart/?symbol=VCIG) | $1.08 | -32.1% | +15.7% | $1.25 | -21.4% | 811K | 251K | 3.2x | 4.4M | Miscellaneous Commercial Services |
| DXST | [TV](https://www.tradingview.com/chart/?symbol=DXST) | $2.99 | +43.8% | +6.0% | $3.17 | +52.4% | 485K | 2.5M | 0.2x | 1.2M | Environmental Services |
| LBGJ | [TV](https://www.tradingview.com/chart/?symbol=LBGJ) | $2.19 | +19.7% | +16.4% | $2.55 | +39.3% | 85K | 723K | 0.1x | 3.0M | Home Furnishings |

**Gate evaluation (all times ET; SIP bars from 16:00 ET / 20:00Z; quote feed stale @16:00 ET / 20:00Z — leaned on SIP per freshness guard):**
- **BIYA** — **already entered at 23:30 (filled @ $4.55, 23:46 CET).** Still building: +53.6% AH ($4.67) vs +37.5% at 23:30. Position healthy, HOLD trajectory intact. One entry per candidate per night — no new action. Premarket position-eval will manage the exit. Grade None.
- **GCTK** — **Clears the 2-AH-scan gate now (23:30 +41.4%, 00:00 +29.8%) but SKIP on trajectory (fade).** SIP: exploded 16:55 ET ($0.49→$0.71), peaked **$0.80 at 17:20 ET**, then rolled over — last 4 bars declining ($0.74C→$0.70→$0.66→$0.65C @17:40 ET) on falling volume (2.2M→630K sh/bar). Now $0.65, **-19% off high and at the edge of the 20% hold band**, AND AH% declined scan-over-scan (41.4%→29.8%). Per hold-vs-fade rule, an early peak (17:20 ET, before 18:30) becomes a disqualifier when the name is *also declining across scans* — GCTK is. Added context: GCTK was **traded 07-14 and dumped -37.6%** (reverse-merger catalyst that behaved like dilution); this is a **re-pump of an already-dumped name**, not a fresh catalyst build. No websearch tool available this pulse to re-check same-day news, but trajectory (fade) overrides catalyst regardless. Skip. Watch for a genuine rebuild (new AH high) at 00:30 CET.
- **CJMB** — **Fresh late-BUILD, but only 1 AH scan >10% — cannot qualify (needs 2nd AH scan).** SIP: dead $0.84 until 17:30 ET, then exploded $0.79→$1.05, built to **$1.13 at 17:40 ET** (1.07M sh/5336 trades — real volume), latest bar 17:45 ET pulled to $0.98. Genuine late build with a post-17:30 peak (favorable timing), float unknown (scanner shows 0). First AH appearance at 00:00 — the feed-lag rescue path only recovers already-tracked names, and the 2-AH-scan entry gate is not met. **Strong watch for 00:30 CET** — if it holds >10% AH it clears the gate and becomes a prime late-BUILD entry.
- **LBGJ** — new, 1 AH scan, **illiquid.** VRatio 0.1x; SIP flat $2.05–2.20 on hundreds of sh/bar for most of AH, then a thin 47K-sh spike to $2.78 at 17:40 ET (only 428 trades). Thin book, can't qualify (1 AH scan). Skip — illiquid ramp, watch only.
- **PMAX** — QUALIFIES on gates but SPIKE→FADE confirmed (peaked $2.36 at 16:25 ET, faded). Skip.
- **GLXG** — Total +2.4%, Day -14.4%, faded from early peak, dilution/shelf risk. Skip.
- **VCIG** — Day -32.1%, Total -21.4% (AH below regular close). Dead-cat. Skip.
- **STXS** — float 80.4M, VRatio 0.8x. Not a candidate.
- **DXST** — AH +6.0% (below 10% gate), VRatio 0.2x (vol fading). Not entry-eligible this scan.

**Decision: No NEW entries.** BIYA already held and building (no re-entry, one per candidate). GCTK cleared the gate but rolled over from its 17:20 ET peak (fade + re-pump of an already-dumped name) — skip. CJMB (strong late-BUILD) and LBGJ (thin) each have only 1 AH scan and cannot qualify yet. No override flags: GCTK is not Day% ≤-15% (no dead-cat-override) nor Total% >150% (no ceiling-override). **CJMB is the name to watch at 00:30 CET** — a post-17:30 late build that clears the gate if it holds >10% AH.

## Scan 23:30 CET (5:30 PM ET) — AFTERHOURS (entry-eligible)

Scanner returned 6 hits. BIYA now clears the 2-AH-scan gate; GCTK is a fresh late-BUILD name.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| GCTK | [TV](https://www.tradingview.com/chart/?symbol=GCTK) | $0.50 | -5.5% | +41.4% | $0.71 | +33.7% | 8.1M | 13.3M | 0.6x | 6.2M | Medical Specialties |
| PMAX | [TV](https://www.tradingview.com/chart/?symbol=PMAX) | $1.76 | +6.0% | +13.8% | $2.00 | +20.6% | 5.8M | 805K | 7.2x | 892K | Specialty Telecommunications |
| BIYA | [TV](https://www.tradingview.com/chart/?symbol=BIYA) | $3.04 | -8.4% | +37.5% | $4.18 | +25.9% | 3.1M | 1.5M | 2.1x | 2.7M | Personnel Services |
| GLXG | [TV](https://www.tradingview.com/chart/?symbol=GLXG) | $1.07 | -14.4% | +18.7% | $1.27 | +1.6% | 1.7M | 257K | 6.6x | 1.7M | Miscellaneous Commercial Services |
| VCIG | [TV](https://www.tradingview.com/chart/?symbol=VCIG) | $1.08 | -32.1% | +6.5% | $1.15 | -27.7% | 744K | 243K | 3.1x | 4.4M | Miscellaneous Commercial Services |
| STXS | [TV](https://www.tradingview.com/chart/?symbol=STXS) | $1.65 | +1.9% | +13.9% | $1.88 | +16.0% | 619K | 1.0M | 0.6x | 80.4M | Medical Specialties |

**Gate evaluation (all times ET; SIP bars from 16:00 ET / 20:00Z):**
- **BIYA** — **QUALIFIES on all gates. ENTERED (order working, see below).** 2 AH scans >10% (23:00 +40.8%, 23:30 +37.5%); float 2.7M (ideal <10M); Day -8.4% (above -15%); Total from close to entry ask +48% (below 150% ceiling). SIP confirms real liquidity: spiked 16:25 ET, peaked $4.68 at 16:35 ET, then **HOLDING** $4.18–$4.52 for 40+ min, now $4.35 (-7% off high, within the 20% band). 500K–846K sh/bar, 6–11K trades/bar. Two-sided fillable book (bid $4.46/ask $4.51 x100). tradable=true. **Trajectory: HOLD near AH high** (not SPIKE→FADE) — early 16:35 peak does not disqualify a name holding within 20% of its high (per hold-vs-fade rule). Catalyst: **none found** (4 searches). 1-for-10 reverse split effective Jul 13 (3 days ago, not today's driver); crypto/BNB "Ark Plan" narrative + April institutional equity deal (dilution history). Low-float China microcap momentum. No fresh same-day earnings/PR/8-K. Entered with **no-catalyst concern noted**, Grade None.
- **GCTK** — **Strong late-BUILD, but only 1 AH scan >10% — cannot qualify yet (needs 2nd AH scan).** Dead ($0.48–0.50) from 16:00–16:50 ET, then **exploded 16:55 ET** ($0.49→$0.71) on 1.95M sh/3462 trades, accelerating: 17:05 ET 3.0M sh $0.72, latest bar 17:15 ET makes a **new high $0.76** (close $0.74) on 2.2M sh. Genuine late build, real volume, float 6.2M, Day -5.5%. This is the strongest trajectory of the night but appears for the first time at 23:30 (fresh name, no prior AH footprint) — the feed-lag rescue path only recovers already-tracked names, and the 2-AH-scan entry gate is not met. Quote stale (@16:00 ET book $0.42/$0.57). **Strong watch for the 00:00 CET scan** — if it holds >10% AH it clears the gate and becomes a prime BUILD entry.
- **PMAX** — QUALIFIES on gates (3 AH scans) but **SPIKE→FADE confirmed.** Peaked $2.36 at 16:25 ET, now $1.93 (SIP), -18% off high, volume collapsed (1.18M→87K sh/bar). Slight scanner uptick to $2.00 was noise. No catalyst. Skip (SPIKE→FADE 0/10+ for PM continuation).
- **GLXG** — Total +1.6%, AH price $1.27 faded below prior scans, Day -14.4%, choppy/faded from early peak. Dilution/shelf risk (Galaxy Payroll). Skip.
- **VCIG** — Day -32.1%, Total -27.7% (AH below regular close). Textbook dead-cat. Skip.
- **STXS** — float 80.4M, VRatio 0.6x. Not a candidate.

**Decision: ENTER BIYA (qualifies on all gates, HOLD trajectory). Order submitted, unfilled at scan time.**
- BUY 22 BIYA @ limit $4.55 ext (id 2c02d728) — QTY = floor($100/$4.51 ask) = 22.
- **Unfilled after ~2 min working.** Alpaca's AH quote feed is frozen at 20:55Z (16:55 ET) and the paper engine isn't matching despite the limit being marketable (limit $4.55 > last $4.35 > ask $4.51). This is a broker-side feed-lag, not a rejection. Order left **working** (day order, expires tonight; can only fill at ≤$4.55). No position exists yet, so not added to OPEN_POSITIONS.md — the premarket position-evaluation pulse will pick it up via `broker.js positions` if it fills tonight.
- No override flags: BIYA is not Day% ≤-15% (no dead-cat-override) nor Total% >150% (no ceiling-override).
- **GCTK is the name to watch at 00:00 CET** — strongest BUILD of the night, needs its 2nd AH scan >10% to clear the entry gate.

## Scan 23:00 CET (5:00 PM ET) — AFTERHOURS (entry-eligible)

Scanner returned 5 hits. First entry-eligible scan of the night (learning-phase gate opens at 23:00 CET).

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| PMAX | [TV](https://www.tradingview.com/chart/?symbol=PMAX) | $1.76 | +6.0% | +13.1% | $1.99 | +19.9% | 5.1M | 721K | 7.1x | 892K | Specialty Telecommunications |
| BIYA | [TV](https://www.tradingview.com/chart/?symbol=BIYA) | $3.04 | -8.4% | +40.8% | $4.28 | +28.9% | 1.5M | 1.3M | 1.2x | 2.7M | Personnel Services |
| GLXG | [TV](https://www.tradingview.com/chart/?symbol=GLXG) | $1.07 | -14.4% | +22.4% | $1.31 | +4.8% | 1.2M | 199K | 6.1x | 1.7M | Miscellaneous Commercial Services |
| VCIG | [TV](https://www.tradingview.com/chart/?symbol=VCIG) | $1.08 | -32.1% | +13.0% | $1.22 | -23.3% | 684K | 237K | 2.9x | 4.4M | Miscellaneous Commercial Services |
| STXS | [TV](https://www.tradingview.com/chart/?symbol=STXS) | $1.65 | +1.9% | +10.9% | $1.83 | +13.0% | 364K | 1.0M | 0.4x | 80.4M | Medical Specialties |

**Gate evaluation (all times ET; SIP bars from 16:00 ET / 20:00Z):**
- **PMAX** — QUALIFIES on gates (2 AH scans >10%: 22:30 +18.1%, 23:00 +13.1%; float 892K; Day +6.0%; Total +19.9% low extension). SIP confirms real liquidity (millions of sh, thousands of trades/bar). **Trajectory: SPIKE→FADE.** Peaked $2.36 at 16:25 ET, now $1.96 (quote bid $1.93/ask $1.96), -17% off high, volume fading (1.18M→215K/bar). Peaked before 17:30 ET and declining. Catalyst: **none found** (4 searches — no earnings/PR/8-K).
- **GLXG** — QUALIFIES on gates (2 AH scans >10%: 22:30 +31.8%, 23:00 +22.4%; float 1.7M; Day -14.4%, just above the -15% dead-cat line). SIP: peaked $1.58 at 16:10 ET, collapsed -23% to $1.21, choppy rebuild to $1.43 (16:45), now $1.31 on quote (-17% off high). **Trajectory: early peak + choppy/faded**, not a clean build. Catalyst: **none fresh** — low-float momentum/pump name (Galaxy Payroll Group) with shelf-registration/dilution history (same mechanic as its June 11 +238% surge). Dilution risk.
- **BIYA** — new, only 1 AH scan >10% (+40.8%). Cannot qualify (needs 2nd AH scan >10%). VRatio 1.2x (vol barely above avg). SIP shows real trades (peak $4.68 at 16:35 ET) but early. Watch for a 2nd scan.
- **VCIG** — Day -32.1%, Total -23.3% (AH price below regular close). Textbook dead-cat bounce. Skip.
- **STXS** — float 80.4M (high), VRatio 0.4x (vol fading). Not a candidate.

**Decision: No entries. SPIKE→FADE-only night.** Both qualifying candidates (PMAX, GLXG) peaked in the first ~25 min of AH (16:25 / 16:10 ET), both before 17:30 ET, and are now ~17% off their highs and fading/choppy — neither is making new highs or holding near its AH high. Neither has a catalyst; GLXG carries dilution/shelf risk. Per the SPIKE→FADE-only-night rule, skip all rather than enter the least-bad option (SPIKE→FADE is 0/10+ for PM continuation regardless of float or extension). PMAX and GLXG stay on watch — if either builds a genuine second leg (new AH high after 17:30 ET) at a later scan, re-evaluate. No override flags: neither is Day% ≤-15% (no dead-cat-override) nor Total% >+150% (no ceiling-override).

## Scan 22:30 CET (4:30 PM ET) — AFTERHOURS

Scanner returned 4 hits. Observation-only scan (learning phase blocks entries before 23:00 CET).

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| PMAX | [TV](https://www.tradingview.com/chart/?symbol=PMAX) | $1.76 | +6.0% | +18.1% | $2.08 | +25.2% | 1.4M | 260K | 5.2x | 892K | Specialty Telecommunications |
| GLXG | [TV](https://www.tradingview.com/chart/?symbol=GLXG) | $1.07 | -14.4% | +31.8% | $1.41 | +12.8% | 527K | 120K | 4.4x | 1.7M | Miscellaneous Commercial Services |
| ATPC | [TV](https://www.tradingview.com/chart/?symbol=ATPC) | $4.20 | +66.7% | +8.3% | $4.55 | +80.6% | 1.3M | 4.1M | 0.3x | 475K | Pharmaceuticals: Other |
| CRDF | [TV](https://www.tradingview.com/chart/?symbol=CRDF) | $0.87 | -1.7% | +5.2% | $0.92 | +3.5% | 344K | 2.3M | 0.2x | 62.5M | Medical Specialties |

**Observations (no entries — before 23:00 CET gate):**
- **PMAX** (new): first AH appearance, AH +18.1% above the 10% gate, float 892K, VRatio 5.2x, low extension (+25% total). BUILD watch — track for the 23:00 scan. Needs a 2nd AH scan >10% to clear the entry gate.
- **GLXG** (new): AH +31.8% but Day% -14.4%, right at the dead-cat threshold. AH price $1.41 sits above regular close $1.07 (reclaim), so watch for dead-cat-override behavior. Float 1.7M. Track.
- **ATPC** (carried from 21:30 regular scan): AH only +8.3%, below the 10% gate. VRatio 0.3x = volume fading, not building into AH. Watch only.
- **CRDF** (new): AH +5.2% below the 10% gate, float 62.5M (high), VRatio 0.2x. Not a candidate.

**Decision:** No entries. Observation-only scan (before 23:00 CET). PMAX and GLXG are the names to watch; both need a 2nd AH scan >10% to qualify. Re-scan at 23:00 CET.

## Scan 22:00 CET (4:00 PM ET) — AFTERHOURS open

Scanner returned 0 hits. AH just opened; observation-only scan (learning phase blocks entries before 23:00 CET).

No candidates found.

**Decision:** No entries. First AH scan of the night, no movers detected. Re-scan at 22:30/23:00 CET.

## Scan 21:30 CET (3:30 PM ET) — REGULAR session

AH not open yet (opens 16:00 ET / 22:00 CET). Regular-session caution: no entries, watch only pending AH confirmation. Scanner returned 55 regular-session hits; notable low-float movers below.

| Ticker | Chart | Price | Chg% | Float | MCap | IRVol | VChg% | Industry | Note |
|--------|-------|-------|------|-------|------|-------|-------|----------|------|
| ATPC | [TV](https://www.tradingview.com/chart/?symbol=ATPC) | $4.12 | +63.5% | 475K | 4.1M | 1588x | -99.3% | Pharma: Other | Vol fading (5mVol 500) |
| STAK | [TV](https://www.tradingview.com/chart/?symbol=STAK) | $3.80 | +78.4% | 0 | 38.0M | 242x | -99.9% | Oilfield Svc | Vol fading |
| DXST | [TV](https://www.tradingview.com/chart/?symbol=DXST) | $2.72 | +30.8% | 1.2M | 4.9M | 54x | -99.3% | Env Svc | Prior winner name; vol fading |
| TGHL | [TV](https://www.tradingview.com/chart/?symbol=TGHL) | $1.49 | +82.9% | 12.7M | 37.7M | 28x | -99.9% | IT Svc | Already traded+sold today (-18.6%) |
| CLIK | [TV](https://www.tradingview.com/chart/?symbol=CLIK) | $1.77 | +19.7% | 724K | 5.8M | 122x | -86.1% | Personnel Svc | Vol fading |
| CRNG | [TV](https://www.tradingview.com/chart/?symbol=CRNG) | $2.00 | +263.6% | 0 | 35.3M | 1.5x | +485% | REIT | Low rel-vol |

**Decision:** No entries. This is a pre-AH regular-session scan; per the regular-session caution rule, candidates are watch-only pending AH confirmation (22:00+ CET). Most notable movers show VChg -99% (regular-session volume already fading, not building into AH). Learning-phase policy also blocks entries before the 23:00 CET scan. Re-scan at 22:00 CET when AH opens.

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| TGHL | $1.33962 | $1.09 | -18.6% | $1.33 (PM) | 1 | None | SELL | Grade None: exit first PM opportunity + below -10% hard stop |

**Actions taken:**
- SELL 79 TGHL @ limit $1.04 ext (id e56b50df) → filled @ $1.09. Final P&L -$19.72 (-18.6%).
- No open positions remain.

**Notes:**
- TGHL faded from PM open $1.15; 5Min SIP bars $1.33H→$1.08C on 5.6M sh, vwap $1.07-1.20 (liquid book). Sold into the fade per Grade None rule.
- Broker quote endpoint returned a stale close-print bid ($1.18 @ prior 20:59Z); used live SIP bars for pricing instead.

## Position Evaluation — 14:30 CET

No open positions. Alpaca `positions` returns empty; `OPEN_POSITIONS.md` already reconciled (shows none). TGHL was the last position, sold in the 10:30 pulse @ $1.09. Nothing to evaluate.

**Actions taken:**
- None.

## Morning Evaluation — 10:20 CET

### Today's Winner

**CJMB** — Air Freight/Couriers (Callan JMB Inc.)
- Catalyst: Jul 16 GlobeNewswire PR — strategic partnership with Alabama State University to advance US pharmaceutical manufacturing / supply-chain resilience (**Grade B**)
- Previous Close: $0.74
- AH last night: SIP peak **$1.36 (+83.8%)** at 19:20 ET (01:20 CET); at the 18:30 ET final scan it was ~$1.03 (+39%)
- Premarket now: **$1.50 (+102.9%)**, still climbing
- PM peak: **$1.58 (+113.5%)** at 04:00 ET on 2.6M sh / 18,052 trades (SIP; Yahoo showed $1.48, under-reported — use SIP)
- Hypothetical P&L (AH entry $1.01 → PM peak $1.58): **+56.4%**
- Float: unknown (scanner 0) | Market Cap: $4.9M
- **Winner bar: CLEARED** — >100% on high, accumulating SIP volume (AH built on 300K–1M+ sh/bar, thousands of trades; PM open exploded on 2.6M sh)

**Scanner Diagnostic:**
- Detectable at screening time? **YES — and we ENTERED it.**
- Dead $0.79–0.86 until 17:30 ET (23:30 CET), then a genuine late-BUILD: first AH scan appearance at 00:00 CET (+26.6%), qualified the 2-AH-scan gate at 00:30 CET (+19.5%), post-17:30 peak on real accumulating volume, Grade B same-day partnership catalyst. **Entered @ $1.01** (00:30 CET final scan). Position now +44.6%.
- The decisive AH continuation ($1.03 → $1.36) fired after the 18:30 ET final scan, but the stock was already detected and entered at that scan — not a late-AH-tail miss.
- Scanner gap: **none.** This is the target outcome — detected, qualified, and selected the actual winner.

### Baseline Tracking

- Days tracked: **50** (was 49 + 1)
- Winners detected by scanner: **43/48 (89.6%)** — CJMB added (detected across 00:00 + 00:30 CET scans)
- Winner selected for paper trade: **24/48 (50.0%)** — CJMB entered @ $1.01; we traded the right stock
- Target: >80% detection
- Status: **BASELINE MET**

### Retrospective Scan Results

PM scan (04:20 ET) top hits: CJMB +62.6% (ref $0.86; +102.9% from $0.74 close), BIYA +35.9%, PMAX +23.9%, VCIG +16.6%, GLXG +12.1%, STXS +9.7%. CJMB is the only name clearing the winner bar. All PM movers were in last night's evening scans — no undetected winner.

### Open Position P&L (Alpaca)

| Ticker | Entry | Entry Total% | Catalyst | Entry Time | PM Peak | Peak Time | Exit | P&L | P&L % | Status |
|--------|-------|--------------|----------|------------|---------|-----------|------|-----|-------|--------|
| CJMB | $1.01 | +39.2% | B — ASU pharma partnership | 00:30 CET | $1.58 | 04:00 ET | open | +$42.75 | +44.6% | 🟢 Open, winning |
| BIYA | $4.55 | +48.0% | None | 23:46 CET | $4.42 | 04:05 ET | open | −$4.6%* | −4.6%* | 🔴 Open, faded |

\* **Quote-freshness flag:** Alpaca `positions` shows BIYA current $4.08 / −10.3%, but SIP PM bars have BIYA building — $4.34 close / $4.42 high at 04:05 ET (472K+429K sh, 8.3K+7.7K trades). Live P&L ≈ −4.6% against $4.34, not −10.3%. Exit is owned by position-evaluation (10:30 CET), not this pulse.

**No realized P&L yet — both positions open.** Exits handled by position-evaluation.

### Scanner Effectiveness

- Evening scans ran: **7 of 7** (21:30, 22:00, 22:30, 23:00, 23:30, 00:00, 00:30 CET) — full coverage, entry window captured
- Candidates found: ~11 unique tickers across the night (GCTK, PMAX, BIYA, CJMB, GLXG, VCIG, STXS, LBGJ, JSPR, DXST, ATPC/CRDF regular)
- Retrospective matches: every PM mover was in the evening scans

### Missed Opportunities

No significant missed opportunities. The morning winner (CJMB) was detected and entered.

### AH Mover Follow-Through

| Ticker | AH Peak | Peak Time | AH Trajectory | Current PM | From Peak | From Close | Verdict |
|--------|---------|-----------|---------------|------------|-----------|------------|---------|
| CJMB | $1.36 (SIP) | 19:20 ET | late-BUILD | $1.50 (+102.9%) | −5% | +102.9% | 🚀 WINNER — PM **exceeded** AH peak, continuation confirmed |
| BIYA | $5.19 (SIP) | 18:30 ET | Build→hold→fade | $4.34 | −16.4% | +30.7% | Faded — PM peak $4.42 **fell short** of AH peak (flag; AH was better exit) |
| GCTK | $0.80 (SIP) | 17:20 ET | spike→fade | $0.53 (+5.0%) | −34% | +5.0% | Faded (correctly skipped on fade rule) |
| PMAX | $2.36 (SIP) | 16:25 ET | spike→fade | $2.18 (+23.9%) | −7.6% | +23.9% | Faded — PM held +24% but < AH peak (correctly skipped) |
| GLXG | ~$1.41 | 18:30 ET (22:30 CET) | spike→fade/choppy | $1.20 (+12.1%) | −15% | +12.1% | Faded (correctly skipped) |

**AH-peak-vs-PM-peak:** CJMB's AH peak (+83.8%, moderate runner) was **exceeded** in PM (+113.5%) — supports the "moderate AH runners continue, extreme (>250%) AH runners fade" hypothesis. BIYA (+56.3% AH) fell short in PM — a moderate runner that still faded (no catalyst, reverse-split name).

### Notes

- **Clean detection + selection night.** CJMB detected, qualified all gates, entered @ $1.01, now +44.6% and still above +100%. This is the target outcome the baseline hunts for.
- **Reverse-split-squeeze fade tally (add BIYA):** BIYA — 1-for-10 reverse split effective Jul 13 (**this-week**), no fresh catalyst (Grade None), float 2.7M, entered $4.55 → PM peak $4.42 = **−2.9%** (current −4.6% to −10.3%), **faded**. AH peak $5.19 was the better exit. Consistent with the hypothesis that fresh-reverse-split names with no operational catalyst fade. Running tally: ELPW (faded), YYGH (faded), EDHL (mild continue, months-old), DCX (flat), **BIYA (faded, this-week)**.
- **Sub-3M-float fade negative controls (correct skips):** PMAX (892K float) peaked 16:25 ET spike→fade, PM $2.18 < AH peak $2.36 — did not re-explode. GLXG (1.7M float) faded, PM $1.20 below AH peak — did not re-explode. Both correctly skipped; both are negative data points for the sub-3M PM-open re-check exception (spike→fade sub-3M names that peak in the first AH minutes do NOT re-ramp). No sub-3M AH-fader re-exploded in PM this session; standing sub-3M count stays 4 of 5.
- **PM-only gapper watch:** biggest raw PM mover = CJMB (+102.9%), classified as **AH→PM continuation** (moved +39% in AH, detectable), not a PM-only gapper. No PM-only-gapper blind spot today.
- **Late-AH-tail watch:** CJMB's continuation fired after the 18:30 ET final scan, but the name was already detected and entered at that scan — not counted as a tail miss.
- **Broker-block tally:** none this session (both CJMB and BIYA filled).
- **Ceiling-override / dead-cat-override watch:** none flagged last night; no outcomes to record.
- **Fade-rule false negatives:** none — PMAX, GLXG, GCTK all faded as the rule predicted (none re-exploded in PM).
