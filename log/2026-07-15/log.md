# 2026-07-15

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| GCTK | $0.87 | $0.71 | -18.4% | ~$0.95 (+9%) | 1 | A | HOLD | Above -25% hard stop ($0.6525); peak never >+50% so no trail; day 1 of 5, catalyst intact |
| LVLU | $11.03 | $8.89 | -19.4% | $11.99 (+8.7%) | 2 | B | SELL | Below -15% hard stop ($9.38) AND day-2 time limit; sell @ $8.40 working (no PM liquidity) |
| VTAK | $0.72 | $0.80 | +11.1% | $1.27 (+76%) | 1 | None | SELL | Grade None → exit at any profit; PM spiked $1.27 then faded, sold into fade |
| XCUR | $2.40 | $2.00 | -16.7% | $2.26 | 1 | None | SELL | Grade None → exit first PM opportunity; below -10% hard stop |

**Actions taken:**
- SELL 125 VTAK @ limit $0.80 ext (id 3652f341) — filled @ **$0.80**, +$10.00 (+11.1%)
- SELL 41 XCUR @ limit $1.92 ext (id 9c193da3) — filled @ **$2.00**, -$16.40 (-16.7%)
- SELL 9 LVLU @ limit $8.40 ext (id a2a6a973) — **still working**, no PM liquidity; confirm fill at 14:30 pulse
- HOLD 101 GCTK — Grade A, above hard stop, catalyst intact

**Realized P&L this pulse:** VTAK +$10.00, XCUR -$16.40 = **-$6.40 net** (LVLU pending)

## Position Evaluation — 14:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| GCTK | $0.8743 | $0.55 | -37.6% | ~$0.95 (+9%) | 2 | A | SELL | Below -25% hard stop ($0.6525). SIP PM faded steadily $0.95→$0.55 (12:15Z vwap $0.56, liquid ~660 trades/bar). Grade A hard stop hit → exit |
| LVLU | $11.03 | $8.12 | -26.4% | $11.99 (+8.7%) | 2 | B | SELL | Below -15% hard stop ($9.38) AND day-2 time limit. SIP $8.00-8.10, thin (11 trades/bar). Prior $8.40 order canceled (wouldn't fill) and repriced |

**Actions taken:**
- Canceled stale LVLU order a2a6a973 ($8.40 limit, wouldn't fill against $8.00-8.10 book)
- SELL 101 GCTK @ limit $0.53 ext (id 86275106) — filled @ **$0.546**, -$33.16 (-37.6%)
- SELL 9 LVLU @ limit $7.85 ext (id 2cdf7fc6) — filled @ **$8.12**, -$26.19 (-26.4%)

**Realized P&L this pulse:** GCTK -$33.16, LVLU -$26.19 = **-$59.35 net**

**Day total (both pulses):** VTAK +$10.00, XCUR -$16.40, GCTK -$33.16, LVLU -$26.19 = **-$65.75 net**

**No open positions remaining.** Account equity ~$99,930.

**Note (GCTK):** Grade A operational catalyst (Lōkahi reverse merger) did not produce a multi-day runner — collapsed from PM open $0.95 to $0.55 on day 2. The completed-reverse-merger structure carried dilution/control-change risk flagged at entry; the -25% hard stop did its job. Data point: not every Grade A operational catalyst sustains; reverse-merger completions may behave more like dilution events than AIIO/UGRO-style acquisitions.

---

# Post-Market Screening - 2026-07-15

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
| TGHL | $1.33962 | 23:36 CET | 79 | 625d905a | BUILD-and-hold, cleared 2-AH-scan gate at 23:30. Grade None (no catalyst). Float 12.7M, Total% +84.5% |

## Scan 21:30 CET (3:30 PM ET)

**Regular session — AH not yet open. No entries (regular-session caution rule).** Watch candidates flagged for AH confirmation at 22:00+ CET scans. Most scan hits show collapsed VChg% (volume already faded intraday), so few clean watches.

| Ticker | Chart | Price | Chg% | 5mVol | Avg5m | IRVol | VChg% | Float | MCap | Industry |
|--------|-------|-------|------|-------|-------|-------|-------|-------|------|----------|
| JTAI | [TV](https://www.tradingview.com/chart/?symbol=JTAI) | $3.40 | +636.4% | 100 | 68K | 5.5 | -99.9% | 1.2M | 4.8M | Airlines |
| ASPD | [TV](https://www.tradingview.com/chart/?symbol=ASPD) | $2.89 | +189.0% | 478 | 854 | 0.5 | +19.5% | 0 | 4.8M | REIT |
| CPHI | [TV](https://www.tradingview.com/chart/?symbol=CPHI) | $1.15 | +87.1% | 804 | 336K | 23.9 | -99.8% | 37.8M | 46.6M | Pharma: Major |
| MRAI | [TV](https://www.tradingview.com/chart/?symbol=MRAI) | $1.25 | +66.7% | 301 | 4K | 9.3 | -99.0% | 11.3M | 31.6M | Packaged Software |
| SOBR | [TV](https://www.tradingview.com/chart/?symbol=SOBR) | $1.80 | +54.3% | 200 | 332K | 5.2 | -99.9% | 2.3M | 5.1M | Electronic Equip |
| KUST | [TV](https://www.tradingview.com/chart/?symbol=KUST) | $1.37 | +35.6% | 350 | 323K | 6.5 | -99.5% | 577K | 859K | Misc Commercial |

**Notes:** All watch candidates show VChg% near -99% (5-min volume collapsed vs earlier intraday spike) — these spiked earlier in the regular session and are fading, not building. JTAI +636% is the biggest mover (float 1.2M) but volume is dead (100 sh/5min). None qualify for entry at a regular-session scan regardless; re-evaluate any that carry into AH with sustained volume at the 22:00/22:30/23:00 CET scans. Entries only permitted at 23:00+ CET per learning-phase default.

## Scan 22:00 CET (4:00 PM ET)

**No candidates found.** Scanner returned 0 hits at AH open (16:00 ET). Observation-only scan (learning-phase rule: no entries before 23:00 CET). None of the 21:30 regular-session watch names (JTAI, ASPD, CPHI, MRAI, SOBR, KUST) reappeared above threshold as AH opened — consistent with their faded regular-session volume. Re-check at 22:30/23:00 for any AH carry.

## Scan 22:30 CET (4:30 PM ET)

**Observation-only (learning-phase rule: no entries before 23:00 CET).** 5 scanner hits; 3 clear the >10% AH threshold. All three confirmed as real AH movers on SIP (thousands of trades/bar, heavy volume). Trajectory read from SIP through 4:15 PM ET (~15 min lag).

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| CPHI | [TV](https://www.tradingview.com/chart/?symbol=CPHI) | $1.10 | +78.9% | +30.0% | $1.43 | +132.6% | 4.2M | 10.5M | 0.4x | 37.8M | Pharma: Major |
| NTRP | [TV](https://www.tradingview.com/chart/?symbol=NTRP) | $2.04 | +1.5% | +16.2% | $2.37 | +17.9% | 999K | 154K | 6.5x | 745K | Packaged Software |
| RBNE | [TV](https://www.tradingview.com/chart/?symbol=RBNE) | $5.27 | -10.0% | +12.3% | $5.92 | +1.1% | 576K | 165K | 3.5x | 562K | Marine Shipping |

(ATPC +7.6% and RAYA +5.8% below the 10% AH threshold — not tracked.)

**Trajectory notes (prep for 23:00 entry scan):**
- **CPHI** — BUILD. SIP vwap $1.03→$1.50 across 4 bars, volume rising (334K→2.7M/bar), high $1.59. Real accumulation. Concerns: +78.9% already banked in regular session (AH adds only +30% on top), Total% +132.6% approaching the +150% ceiling, wide AH book (bid $1.50 / ask $3.40 — ask stale far above SIP high $1.59). tradable=true. Second appearance (was +87% in 21:30 regular scan). Needs catalyst workup + 2-AH-scan gate check at 23:00.
- **NTRP** — Fresh AH spike (Day only +1.5%), low extension +17.9%, float 745K, VRatio 6.5x, tight book ($2.40/$2.43). Peaked $2.71 at 4:10 PM, fading to $2.27 by 4:15 — early-peak-fade watch. First AH appearance; needs a 2nd AH scan to clear the gate. tradable=true.
- **RBNE** — Dead-cat pattern: Day -10% (down regular session), AH bounce peaked $7.23 at 4:05 PM, now fading to $6.15, Total% only +1.1% (still below regular close). Early peak + fade + down-day bounce = skip candidate. tradable=true.

**No entries (observation-only scan).** Re-evaluate CPHI/NTRP at 23:00 with full catalyst search; both need a 2nd AH-scan confirmation to satisfy the entry gate.

## Scan 23:00 CET (5:00 PM ET)

**Entry scan (learning-phase: entries now permitted at 23:00+ CET).** 5 scanner hits; TGHL is new this scan. SIP verified through 16:45 ET (~15 min lag).

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| TGHL | [TV](https://www.tradingview.com/chart/?symbol=TGHL) | $0.81 | +23.2% | +49.8% | $1.22 | +84.5% | 13.3M | 9.6M | 1.4x | 12.7M | IT Services |
| CPHI | [TV](https://www.tradingview.com/chart/?symbol=CPHI) | $1.10 | +78.9% | +16.5% | $1.28 | +108.4% | 12.3M | 11.4M | 1.1x | 37.8M | Pharma: Major |
| NTRP | [TV](https://www.tradingview.com/chart/?symbol=NTRP) | $2.04 | +1.5% | +14.7% | $2.34 | +16.4% | 3.4M | 448K | 7.7x | 745K | Packaged Software |
| RBNE | [TV](https://www.tradingview.com/chart/?symbol=RBNE) | $5.27 | -10.0% | +10.2% | $5.81 | -0.8% | 680K | 180K | 3.8x | 562K | Marine Shipping |

(ATPC +9.9% AH also hit; below tracking priority, Day -3.1%, Total% +6.5% — early-peak fade, skip.)

**Evaluation (no entries this scan):**

- **TGHL** — Strongest profile but blocked by the 2-AH-scan gate. SIP: flat ~$0.79-0.81 until 16:20 ET, then exploded $0.80→$1.15 on 2.38M sh / 6,326 trades. Peaked $1.38 at 16:35 ET, holding $1.21-1.25 at 16:45 (within ~12% of high). Volume massively real and accumulating (2-4M sh/bar, 6-13K trades/bar). Live book $1.18/$1.26 (16:59 ET) corroborates SIP — not a bad print. Float 12.7M, Total% +84.5% (below +150 ceiling). tradable=true. **Catalyst:** no same-day PR found (3 searches); only recent company news is a Nasdaq stockholders'-equity-deficiency / delisting notice (negative) plus an older MoU with the Government of Republika Srpska. No catalyst found. **Gate block:** first AH appearance — the spike started at 16:20 ET, after the 22:30 SIP read, so it was absent from the 22:00 and 22:30 scans. Fails the ≥2-AH-scan requirement. **Top watch for 23:30**: if it holds $1.15+ on sustained volume into its 2nd AH scan, it clears the gate and becomes an entry candidate (BUILD-and-hold, float <50M, Total% below ceiling; enter with no-catalyst concern noted).
- **CPHI** — SPIKE→FADE, skip. SIP peaked $1.59 at 16:15 ET, faded steadily to $1.24-1.30 by 16:45 (~-20% off peak), volume declining 2.7M→531K/bar. AH% dropped 30%→16.5% across scans; Total% slipped 132.6%→108.4%. Early peak (16:15 ET) + declining across scans + fading volume + wide stale book (bid $1.41 / ask $3.40). Day +78.9% already banked in regular session. Cleared the 2-scan gate structurally but trajectory disqualifies it.
- **NTRP** — SPIKE→FADE collapsed below close, skip. SIP spiked to $2.71 at 16:10 ET (very early), faded to $2.15 by 16:45; live book $1.92/$1.95 at 16:59 ET — now BELOW its $2.04 close (scanner's $2.34 is stale feed-lag). -29% off peak. Cleared the 2-scan gate structurally but collapsed.
- **RBNE** — Dead-cat bounce, skip. Day -10% (down regular session), AH bounce peaked early and Total% only -0.8% (still below regular close). Down-day bounce, no reclaim.

**No entries.** The two gate-clearing candidates (CPHI, NTRP) are both SPIKE→FADE; the one clean BUILD-and-hold (TGHL) has not cleared the 2-AH-scan gate (fresh 16:20 ET spike). SPIKE→FADE-only among eligible names → skip per the SPIKE→FADE-only-night rule. TGHL carried forward as the top watch for the 23:30 scan.

## Scan 23:30 CET (5:30 PM ET)

**Entry scan.** 6 scanner hits. TGHL now appears for the **2nd AH scan** (23:00 + 23:30, both AH +49.8%), clearing the 2-AH-scan gate. SIP verified fresh through 17:18 ET.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| TGHL | [TV](https://www.tradingview.com/chart/?symbol=TGHL) | $0.81 | +23.2% | +49.8% | $1.22 | +84.5% | 21.0M | 10.4M | 2.0x | 12.7M | IT Services |
| GCTK | [TV](https://www.tradingview.com/chart/?symbol=GCTK) | $0.53 | -0.0% | +11.9% | $0.59 | +11.9% | 2.6M | 12.0M | 0.2x | 6.2M | Medical Specialties |
| JTAI | [TV](https://www.tradingview.com/chart/?symbol=JTAI) | $3.14 | +580.1% | +19.4% | $3.75 | +712.2% | 1.2M | 5.8M | 0.2x | 1.2M | Airlines |
| VTAK | [TV](https://www.tradingview.com/chart/?symbol=VTAK) | $0.58 | +3.6% | +9.7% | $0.64 | +13.6% | 717K | 30.2M | 0.0x | 2.6M | Medical Specialties |
| RBNE | [TV](https://www.tradingview.com/chart/?symbol=RBNE) | $5.27 | -10.0% | +5.9% | $5.58 | -4.7% | 702K | 183K | 3.8x | 562K | Marine Shipping |
| ATPC | [TV](https://www.tradingview.com/chart/?symbol=ATPC) | $2.52 | -3.1% | +11.9% | $2.82 | +8.5% | 427K | 85K | 5.0x | 475K | Pharmaceuticals: Other |

**ENTERED: TGHL** — 79 sh @ **$1.33962** (order 625d905a, 23:36 CET). Cleared all entry gates:
- **2-AH-scan gate:** appeared 23:00 (AH +49.8%) and 23:30 (AH +49.8%) — both >10% ✓
- **BUILD-and-hold trajectory:** SIP shows spike $0.80→$1.38 (peak 16:35 ET), then holding $1.15-1.25 across 10 bars through 17:18 ET (within ~15% of high, current ~$1.17-1.20). Before-18:30 peak but holding within 20%, not fading → qualifies per hold-vs-fade rule.
- **Real SIP volume:** 2-4M sh/bar at peak, still 60-250K sh/bar & hundreds of trades/bar at 17:18 ET. Not a bad print (live book corroborates).
- **Fillable book, tradable=true.** Float 12.7M (<50M), Day% +23.2% (>-15%), Total% +84.5% (below +150 ceiling).
- **Catalyst: None.** Re-ran search this scan (4 queries): no same-day PR; intellectia.ai attributes the move to "broad market strength"; only company news is the May 26 Nasdaq stockholders'-equity-deficiency notice (negative). Entered with no-catalyst concern noted (learning-phase no-catalyst handling).
- **Fill note:** limit orders at $1.27/$1.29 would not cross because Alpaca's real-time feed for TGHL was frozen at 16:59 ET (stale $1.26 ask). Repriced to $1.35 to force a fill against the live book; filled @ $1.33962.

**Grade: None → exit at first premarket opportunity.**

**Skips (this scan):**
- **GCTK** — VRatio 0.2x (no real AH volume), Total% only +11.9%; already traded and exited today. Thin, skip.
- **JTAI** — Total% +712.2% (Day +580% banked in regular session), far above +150 ceiling; AH VRatio 0.2x (thin AH). Skip: extension ceiling + thin AH.
- **VTAK** — AH +9.7% (below 10% threshold), VRatio 0.0x; already exited today. Skip.
- **RBNE** — dead-cat (Day -10%), AH +5.9% (below threshold), Total% -4.7% (below close). Skip.
- **ATPC** — fails 2-AH-scan >10% gate (23:00 was +9.9%, below threshold). SIP: late peak $3.01 at 16:55 ET but volume collapsing (1685 trades at peak → 85 last bar), wide stale book ($2.19/$2.89). Fading thin. Skip.

## Scan 00:00 CET (6:00 PM ET)

**Entry scan.** 7 scanner hits. No new entry candidates. TGHL (already held) is building strongly. ATPC now clears the 2-AH-scan gate but trajectory disqualifies. SIP verified through 17:45 ET (~15 min lag).

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| TGHL | [TV](https://www.tradingview.com/chart/?symbol=TGHL) | $0.81 | +23.2% | +95.2% | $1.59 | +140.4% | 28.6M | 11.2M | 2.5x | 12.7M | IT Services |
| GCTK | [TV](https://www.tradingview.com/chart/?symbol=GCTK) | $0.53 | -0.0% | +9.6% | $0.58 | +9.6% | 3.4M | 12.0M | 0.3x | 6.2M | Medical Specialties |
| JTAI | [TV](https://www.tradingview.com/chart/?symbol=JTAI) | $3.14 | +580.1% | +21.7% | $3.82 | +727.7% | 3.0M | 6.0M | 0.5x | 1.2M | Airlines |
| VTAK | [TV](https://www.tradingview.com/chart/?symbol=VTAK) | $0.58 | +3.6% | +7.1% | $0.62 | +11.0% | 806K | 30.2M | 0.0x | 2.6M | Medical Specialties |
| RBNE | [TV](https://www.tradingview.com/chart/?symbol=RBNE) | $5.27 | -10.0% | +7.7% | $5.68 | -3.1% | 715K | 185K | 3.9x | 562K | Marine Shipping |
| ATPC | [TV](https://www.tradingview.com/chart/?symbol=ATPC) | $2.52 | -3.1% | +13.1% | $2.85 | +9.6% | 476K | 91K | 5.2x | 475K | Pharmaceuticals: Other |
| ERNA | [TV](https://www.tradingview.com/chart/?symbol=ERNA) | $6.73 | +11.1% | +5.3% | $7.09 | +17.0% | 119K | 2.6M | 0.0x | 679K | Pharmaceuticals: Major |

**Evaluation (no new entries this scan):**

- **TGHL (HELD)** — thesis confirming. SIP/Yahoo AH shows a clean BUILD: after the 16:20-16:35 ET spike it held $1.15-1.25, then broke to **new AH highs $1.55-1.56 at 17:40-18:00 ET** (+135.9% peak). Position now 79 sh @ $1.34, marked $1.49 (+11.2%). No add (one entry per candidate per night). Grade None → exit at first premarket opportunity (handled by position-evaluation premarket).
- **ATPC** — clears the 2-AH-scan >10% gate for the first time (23:30 +11.9%, 00:00 +13.1%), float 475K (ideal), Total% +9.6% (far below ceiling), Day -3.1% (not dead-cat). **But trajectory disqualifies: faded opening spike, not BUILD.** Yahoo/SIP show a single first-bar spike to $3.08 at 16:05 ET (+18.4%), then an immediate collapse to a choppy $2.7-3.0 base that never reclaimed the high across 2 hours. Descending intraday peaks ($3.08→$3.01→$3.00→$2.99), spiky/fading volume (push bars then collapse to 44-92 trades/bar), and a wide stale quote book (bid $2.19 / ask $2.89, frozen @16:00 ET). The rising scanner AH% (7.6→9.9→11.9→13.1) is the base drifting up within the choppy range, not a build toward the high. SPIKE→FADE character (0/10+ for PM continuation) → skip on trajectory. tradable=true.
- **ERNA** — new, but AH +5.3% (below 10% threshold), Total% +17.0%, and quote shows **ask $0.00 x0 (no AH book)**. Skip: below threshold + illiquid (no AH book).
- **GCTK** — VRatio 0.3x (no real AH volume), Total% +9.6% (below threshold); already traded/exited today. Skip.
- **JTAI** — Total% +727.7% (Day +580% banked in regular session), far above +150 ceiling; AH VRatio 0.5x (thin). Skip: extension ceiling + thin AH.
- **VTAK** — AH +7.1% (below threshold), VRatio 0.0x; already exited today. Skip.
- **RBNE** — dead-cat (Day -10%), AH +7.7% (below threshold), Total% -3.1% (below close). Skip.

**No new entries.** Only gate-clearing new name (ATPC) is a faded opening spike; all other hits are below threshold, over the extension ceiling, dead-cat, or already traded. TGHL remains the sole open position and is building toward its AH high — thesis intact.

## Scan 00:30 CET (6:30 PM ET) — FINAL SCAN

**Entry scan + final feed-lag cross-check.** 7 scanner hits. No new entries. TGHL (held) still building. ATPC clears the 2-AH-scan gate on AH% but trajectory disqualifies (confirmed SPIKE→FADE on SIP).

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| TGHL | [TV](https://www.tradingview.com/chart/?symbol=TGHL) | $0.81 | +23.2% | +91.5% | $1.56 | +135.9% | 36.0M | 12.0M | 3.0x | 12.7M | IT Services |
| GCTK | [TV](https://www.tradingview.com/chart/?symbol=GCTK) | $0.53 | -0.0% | +7.7% | $0.57 | +7.6% | 3.5M | 12.1M | 0.3x | 6.2M | Medical Specialties |
| JTAI | [TV](https://www.tradingview.com/chart/?symbol=JTAI) | $3.14 | +580.1% | +9.9% | $3.45 | +647.7% | 3.5M | 6.1M | 0.6x | 1.2M | Airlines |
| RBNE | [TV](https://www.tradingview.com/chart/?symbol=RBNE) | $5.27 | -10.0% | +5.3% | $5.55 | -5.2% | 720K | 186K | 3.9x | 562K | Marine Shipping |
| ATPC | [TV](https://www.tradingview.com/chart/?symbol=ATPC) | $2.52 | -3.1% | +16.3% | $2.93 | +12.7% | 511K | 95K | 5.4x | 475K | Pharmaceuticals: Other |
| ILLR | [TV](https://www.tradingview.com/chart/?symbol=ILLR) | $1.28 | -44.6% | +6.3% | $1.36 | -41.1% | 261K | 1.9M | 0.1x | 17.9M | Packaged Software |
| ERNA | [TV](https://www.tradingview.com/chart/?symbol=ERNA) | $6.73 | +11.1% | +6.0% | $7.13 | +17.7% | 133K | 2.6M | 0.1x | 679K | Pharmaceuticals: Major |

**Evaluation (no new entries):**

- **TGHL (HELD)** — thesis holding. Position 79 sh @ $1.34, marked $1.44 (+7.5%). Scanner AH +91.5% ($1.56), SIP peak $1.55-1.56 at 17:40-18:00 ET. No add (one entry per candidate per night). Grade None → premarket exit (position-evaluation handles).
- **ATPC** — clears the 2-AH-scan >10% gate (23:30 +11.9%, 00:00 +13.1%, 00:30 +16.3%), float 475K (ideal), Total% +12.7% (far below ceiling), Day -3.1% (not dead-cat). **But SIP confirms SPIKE→FADE → skip.** Bars: spike to $3.18 at 16:10 ET (very early peak), immediate collapse to a choppy $2.66-3.01 base, descending peaks ($3.18→$3.01→$3.00), thinning volume (49K→6.3K sh/bar), never reclaimed the high across ~1.5 hrs. Rising scanner AH% is the base drifting inside the choppy range, not a build. Book stale ($2.19/$2.89 frozen 16:00 ET). SPIKE→FADE is 0/10+ for PM continuation — trajectory dominates the ideal float. Skip.
- **ILLR** — new. Day -44.6% (massive down day), AH +6.3% (below threshold), Total% -41.1% (deep below close). SIP thin (34-56 trades/bar, ~5K sh). Dead-cat + below threshold + thin. Skip.
- **JTAI** — Total% +647.7% (Day +580% banked in regular session), far above +150 ceiling. Real AH volume (SIP $3.92, 3088 trades/bar) but extension ceiling disqualifies. Skip.
- **ERNA** — AH +6.0% (below threshold), VRatio 0.1x, illiquid. Skip.
- **GCTK** — AH +7.7% (below threshold), VRatio 0.3x (no real AH volume), already traded/exited today. Skip.
- **RBNE** — dead-cat (Day -10%), AH +5.3% (below threshold), Total% -5.2% (below close). Skip.

**Final feed-lag cross-check (per last-scan rule):** cross-checked tracked names against SIP. No under-reported real mover being dropped. CPHI faded to $1.14-1.19 (~+4-8% AH, below threshold — correctly dropped from scan). JTAI real volume but over the extension ceiling. ILLR dead-cat/thin. The one real BUILD mover (TGHL) is already held and correctly reported. No rescue needed.

**Night summary:** 8 scans (21:30–00:30 CET). One entry: **TGHL** (79 sh @ $1.33962, BUILD-and-hold, Grade None, no catalyst). TGHL closed the night +7.5% and building toward its AH high — thesis intact into premarket. All other candidates were SPIKE→FADE (ATPC, CPHI, NTRP), over the extension ceiling (JTAI), dead-cat (RBNE, ILLR), or below threshold/illiquid (GCTK, VTAK, ERNA). Premarket exit for TGHL handled by position-evaluation.


---

## Morning Evaluation — 10:20 CET

### Today's Winner

**ATPC** — Agape ATP Corporation (Pharmaceuticals: Other)
- Catalyst: **None found** (evening scans ran 3+ searches, no same-day PR). Ultra-low-float squeeze pattern.
- Previous Close: $2.60
- AH last night: built quietly to +10% through the scanned window, then surged late — SIP AH peak **$3.87** at 19:20 ET / 01:20 CET (285K sh, 4,194 trades) — after the 00:30 CET final scan.
- Premarket now: SIP PM peak **$4.90** at 04:00 ET (1.53M sh, 24,179 trades), currently ~$3.86 (+48% from close)
- Hypothetical P&L (gate-clear AH entry $2.85 → PM peak $4.90): **+72%** | (from close: +88.5%)
- Float: **475K** (ultra-low) | Market Cap: $2.5M

**Scanner Diagnostic:**
- Detectable at screening time? **YES** — ATPC appeared in **5 evening scans** (22:30, 23:00, 23:30, 00:00, 00:30) and cleared the 2-AH-scan >10% gate at 00:00 (AH +13.1%, float 475K, Total% only +9.6%, Day -3.1% not dead-cat).
- Why we didn't act: **skipped on the SPIKE→FADE trajectory rule.** Through the scanned window (to 18:30 ET) SIP showed a faded opening spike ($3.08 at 16:05 ET) then a choppy $2.7-3.0 base with descending peaks and thinning volume — genuine spike→fade character; rising scanner AH% was the base drifting up, not a build toward the high. The evening read was correct *for the scanned window*.
- What changed after the last scan: the decisive surge to the AH peak $3.87 fired at **19:20 ET (01:20 CET), ~50 min after the final scan**, then extended to the PM peak $4.90 on 1.5M shares at PM open.
- Scanner gap: this is a **fade-rule false negative** — a sub-3M-float AH-fader that re-exploded. The fix under test is a **sub-3M-float PM-open re-check** (re-check sub-3M faders at PM open before writing them off), not a blanket relaxation of the fade rule. See Notes: this case brings the sub-3M fade-false-negative tally to **4 of 5**, reaching the ≥4/5 trigger to propose the exception.

### Baseline Tracking

- Days tracked: **49** (was 48 + 1)
- Winners detected by scanner: **42/47 (89.4%)** — ATPC added (detected, appeared in 5 scans; skipped on fade rule, not a detection miss).
- Winner selected for paper trade: **23/47 (48.9%)** — ATPC not entered (fade-rule skip). We entered TGHL, which faded.
- Target: >80% detection
- Status: **BASELINE MET** (detection 89.4%). Bottleneck is now the entry/selection rules, not detection — the fade rule skipped a detected +72% winner.

### Retrospective Scan Results
- Live premarket scan (04:20 ET): 6 hits — ATPC +56.7% (top, VRatio 3.6, float 475K), DXST +48.9% (VRatio 0.5), TGHL +36.3%, VTAK +10.4%, EHGO +18.7%, JTAI +8.3%.
- Forced AH scan: 0 hits (expected overnight — TradingView postmarket fields return stale/zero next morning).
- AH reconstruction (SIP bars, authoritative): ATPC late-tail surge to $3.87 (19:20 ET) → PM peak $4.90; JTAI AH peak $4.36 (17:15 ET, 834K sh) → faded to $3.57 PM.
- **Yahoo under-reported both peaks:** ATPC AH high Yahoo $3.65 vs SIP $3.87; ATPC PM high Yahoo $3.96 vs SIP $4.90. SIP peaks used.

### Open Position P&L (Alpaca)

| Ticker | Entry | Entry Total% | Catalyst | Entry Time | PM Peak | Peak Time | Exit | P&L | P&L % | Status |
|--------|-------|--------------|----------|------------|---------|-----------|------|-----|-------|--------|
| TGHL | $1.3396 | +84.5% | None | 23:36 CET | $1.11 (PM) | ~04:20 ET | open | −$19.72 | −18.6% | 🔴 Holding (fading) |

TGHL entered last night as a BUILD-and-hold (Grade None). AH peak $1.59, now ~$1.09 in PM — faded below entry. **Not managed here** (exits handled by position-evaluation 10:30/14:30 CET). Alpaca `current_price` $1.09 is consistent with the live PM scan ($1.11) — not stale.

**Total Realized P&L (Alpaca fills only): none this pulse** (TGHL still open). Account equity $99,906.55.

### Scanner Effectiveness

- Evening scans ran: **7 of 7** (21:30 - 00:30 CET). Full coverage — entry window intact.
- Candidates found: 11 unique tickers across the night (JTAI, ASPD, CPHI, MRAI, SOBR, KUST, NTRP, RBNE, TGHL, GCTK, VTAK, ATPC, ILLR, ERNA).
- Retrospective match: today's winner (ATPC) was in-scan (5 appearances). Detection worked; the fade rule blocked the trade.

### Missed Opportunities

| Ticker | AH Change | Why Missed | Would Be Profitable? |
|--------|-----------|------------|---------------------|
| ATPC | +16% at last scan → +49% AH tail | Skipped on SPIKE→FADE rule; decisive surge fired 19:20 ET after final scan | Yes — hypo +72% (AH $2.85 → PM $4.90) |

### AH Mover Follow-Through

| Ticker | AH Peak | Peak Time | AH Trajectory | Current PM | From Peak | From Close | Verdict |
|--------|---------|-----------|---------------|------------|-----------|------------|---------|
| ATPC | $3.87 (SIP) | 19:20 ET (tail) | Spike→fade (scanned) → re-exploded | $4.90 peak / $3.86 | +27% then back | +88.5% peak | **PM EXCEEDED AH — winner** |
| JTAI | $4.36 (SIP) | 17:15 ET | Spike→fade | $3.57 peak / $3.42 | −18% | +14% peak | PM fell short of AH peak |
| TGHL | $1.59 | ~18:00 ET | Build → faded PM | $1.09 | −31% | +35% peak | PM fell short (our entry, −18.6%) |
| CPHI | $1.59 | 16:15 ET | Spike→fade | faded <close | — | below close | Correctly skipped |
| NTRP | $2.71 | 16:10 ET | Spike→fade (collapsed <close) | faded <close | — | below close | Correctly skipped |

**AH-peak-vs-PM-peak:** ATPC PM peak $4.90 > AH peak $3.87 (real continuation). JTAI and TGHL both peaked in AH and faded into PM (AH was the better exit). No >250%-from-close extreme runner this session.

### Notes

**🔴 FADE-RULE SUB-3M TALLY REACHES 4/5 — trigger hit.** ATPC (float **475K**) is a sub-3M-float AH-fader, skipped on the SPIKE→FADE rule, that re-exploded (scanned-window peak ~$3.18 → AH-tail $3.87 → PM peak $4.90). This is the **4th of 5** sub-3M faders to blow past:
- LNKS 1.5M — blew past ✓
- RPGL 1.1M — blew past ✓
- CRE — blew past ✓
- IOTR 644K — fell short ✗
- **ATPC 475K — blew past ✓ (new)**
- Standing: **4 of 5 sub-3M faders re-exploded.** This reaches the ≥4/5 trigger. **Proposal for the daily email:** add a **sub-3M-float PM-open re-check exception** to the SPIKE→FADE skip — re-check sub-3M-float faders at PM open before writing them off, keeping higher-float faders (LIQT 24.2M, TGE 44.2M negative controls) skipped. Catalyst bucket: ATPC is a **no-catalyst** fader (no strong catalyst needed to rescue it — low float alone carried it).

**Late-AH-tail context (not a detection miss):** ATPC's defining surge fired at 19:20 ET / 01:20 CET, ~50 min after the 00:30 CET final scan, in the unscanned 18:30-20:00 ET tail. But ATPC was already surfaced in the scan at +16% and skipped on trajectory, so this is primarily a fade-rule false negative, not a coverage/tail detection gap. Hypo AH-tail entry ~$3.30 → PM peak $4.90 = +48%.

**PM-only gapper (biggest raw PM mover):** ATPC is the morning's biggest raw PM mover (+52% from close in PM) and is an **AH→PM continuation** (detectable — moved >10% in AH), NOT a PM-only gapper. Secondary: **DXST** (+48.9% PM) IS a PM-only gapper — SIP shows it flat in AH (8 trades, $2.05-2.08), move began only at 04:00 ET ($2.28→$3.85 on 1.3M sh). Holdable (sustained across 2+ PM bars on real volume). Structurally undetectable by the AH scanner; not counted against baseline.

**Coverage:** 7 of 7 evening scans ran. No coverage failure.

**Broader read:** detection is solidly above the 80% baseline (89.4%). The recurring cost is now the entry rules — specifically the fade rule skipping detected sub-3M-float winners (ATPC today). This is the "Refine" phase concern flagged in Day Trading.md.

### Price Charts

```

========================================================================
 ATPC - 2-Day Price Timeline (5-min intervals)
========================================================================

Previous Close: $2.60
2-Day Range: $2.51 - $4.90
Current: $3.82 (+46.9% from prev close)
Peak: $4.90 (+88.5%) at 07-16 08:00 ET

Chart (oldest → newest):
$   3.96 │                                                            
         │                                                            
         │                                                            
         │                                                            
         │                                                            
         │                                                            
         │                                                            
         │                                        █                   
         │                                                  ██     █  
         │                                               █ █  ███ █ ██
         │                                         ██████ █      █    
$   2.51 │████████████████████████████████████████                    
         └────────────────────────────────────────────────────────────

Session Timeline (last 24h):
------------------------------------------------------------
  [OVN] 07-15 20:30 ET: $   2.72 (  +4.6%)  Vol:           
  [OVN] 07-15 20:35 ET: $   2.70 (  +3.9%)  Vol:           
  [OVN] 07-15 20:40 ET: $   2.80 (  +7.7%)  Vol:           
```
