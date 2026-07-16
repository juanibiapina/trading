# 2026-07-16

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|

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
