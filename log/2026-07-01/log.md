## Scan 21:30 CET (3:30 PM ET) — REGULAR session

Scan ran before AH open (16:00 ET / 22:00 CET). Per regular-session caution: no paper trades. Candidates flagged for AH confirmation at 22:00+ CET scans.

| Ticker | Chart | Price | Chg% | IRVol | VChg% | Float | MCap | Industry | Note |
|--------|-------|-------|------|-------|-------|-------|------|----------|------|
| LHAI | [TV](https://www.tradingview.com/chart/?symbol=LHAI) | $1.84 | +178.8% | 1411.9x | -23.5% | 8.1M | 10.7M | Packaged Software | Top mover — Watch, pending AH confirmation |
| WMTN | [TV](https://www.tradingview.com/chart/?symbol=WMTN) | $0.68 | +458.4% | 2.8x | -50.0% | 11.1M | 13.6M | Precious Metals | Big % but thin vol — Watch |
| ABVN | [TV](https://www.tradingview.com/chart/?symbol=ABVN) | $1.50 | +172.7% | 3.6x | -50.0% | 14.9M | 58.0M | Specialty Stores | Watch, low vol |
| EHGO | [TV](https://www.tradingview.com/chart/?symbol=EHGO) | $2.52 | +93.9% | 1.5x | -76.6% | 1.4M | 2.9M | Wholesale Distributors | Low float, vol fading — Watch |
| STKE | [TV](https://www.tradingview.com/chart/?symbol=STKE) | $1.62 | +38.5% | 32.0x | -57.0% | 25.9M | 62.2M | Financial Conglomerates | Watch |
| CLEV | [TV](https://www.tradingview.com/chart/?symbol=CLEV) | $0.75 | +41.5% | 5.1x | +16.4% | 6.1M | 10.5M | Tools & Hardware | Watch |
| PNBK | [TV](https://www.tradingview.com/chart/?symbol=PNBK) | $1.25 | +30.0% | 6.1x | +394.4% | 83.3M | 146.5M | Regional Banks | High float — Watch |

63 total hits. Many Financial Conglomerates ~$9.9x are SPAC/pre-deal names pinned near NAV (TRAD, PONO, ACGC, SCPQ, MYX, IRAB) — ignore. Focus for AH confirmation: **LHAI** (biggest move + huge IRVol + sub-10M float).

**Action:** Re-scan at 22:00+ CET once AH opens. Enter only at 23:00+ CET (learning-phase default) if a candidate shows sustained AH momentum.

## Scan 22:00 CET (4:00 PM ET) — first AH scan

`scan.py --all` (AFTERHOURS mode): **0 AH hits.** Expected — AH just opened at 16:00 ET, no extended-hours volume has accumulated yet to trip the VRatio filter.

Regular-session watch candidates from 21:30 (LHAI, WMTN, ABVN, EHGO, STKE, CLEV) still pending AH confirmation. No fresh AH volume signal yet.

**Decision:** No entries (observation only — before 23:00 CET learning-phase gate, and no qualifying AH candidates). Re-scan at 22:30 / 23:00 CET as AH volume builds.

## Scan 22:30 CET (4:30 PM ET) — AH observation

`scan.py --all` (AFTERHOURS): **3 hits.** None of the 21:30 regular-session watch names (LHAI, WMTN, ABVN, EHGO, STKE, CLEV) confirmed in AH.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| JEM | [TV](https://www.tradingview.com/chart/?symbol=JEM) | $3.21 | -19.1% | +36.8% | $4.39 | +10.6% | 2.1M | 20.5M | 0.1x | ~4.5M | Wholesale Distributors |
| ALPS | [TV](https://www.tradingview.com/chart/?symbol=ALPS) | $0.58 | +0.5% | +23.5% | $0.72 | +24.1% | 2.1M | 296K | 7.0x | 45.0M | Miscellaneous |
| WHLR | [TV](https://www.tradingview.com/chart/?symbol=WHLR) | $0.99 | -20.8% | +21.3% | $1.20 | -4.0% | 91K | 743K | 0.1x | 549K | REIT |

**SIP verification (bars from 20:00Z / 16:00 ET):**
- **JEM** — REAL accumulation: 375K → 728K → 1.51M → 745K sh/bar, 3,046→13,643 trades/bar. SIP VWAP $4.47 corroborates AH price $4.39 (no bad print). Peak $4.83 @16:10 ET, now $4.24. Day% -19.1 (≤-15 dead-cat zone) but AH BUILDS to reclaim +10.6% above previous close → **DEAD-CAT-OVERRIDE WATCH**. Quote stale (`ask $0.00 x0` @20:00Z) — recheck book at 23:00.
- **ALPS** — REAL accumulation: 93K → 1.78M → 346K → 213K sh/bar, VWAP $0.66–0.74 corroborates. Real two-sided book (`ask $0.75 x100`, bid $0.75 x100). Clean BUILD from a flat regular day (Day +0.5%), float 45M (<50M gate), VRatio 7.0x. Peaked $0.86 @16:05 ET (early), now softening to $0.70–0.72 — watch for hold vs fade.
- **WHLR** — dead-cat: Day -20.8%, Total -4.0% (still below regular close), thin AH vol (peak 74K sh/bar). Textbook bounce off a sell-off. Skip.

**Decision:** No entries — observation only (before 23:00 CET learning-phase gate). Best BUILD candidate for the 23:00 scan is **ALPS** (real book, sub-50M float, reclaim from flat) provided it holds near its AH high rather than fading. **JEM** flagged dead-cat-override watch (record hypothetical if it holds the reclaim). Re-scan at 23:00 CET to confirm momentum before any entry.

## Scan 23:00 CET (5:00 PM ET) — AH, entry-eligible

`scan.py --all` (AFTERHOURS): **8 hits.**

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| LHAI | [TV](https://www.tradingview.com/chart/?symbol=LHAI) | $2.74 | +315.2% | +5.5% | $2.89 | +337.9% | 17.4M | 32.7M | 0.5x | 8.1M | Packaged Software |
| JEM | [TV](https://www.tradingview.com/chart/?symbol=JEM) | $3.21 | -19.1% | +38.9% | $4.46 | +12.3% | 4.1M | 20.8M | 0.2x | ~4.5M | Wholesale Distributors |
| ALPS | [TV](https://www.tradingview.com/chart/?symbol=ALPS) | $0.58 | +0.5% | +14.8% | $0.67 | +15.4% | 2.7M | 366K | 7.5x | 45.0M | Miscellaneous |
| WHLR | [TV](https://www.tradingview.com/chart/?symbol=WHLR) | $0.99 | -20.8% | +21.3% | $1.20 | -4.0% | 1.1M | 851K | 1.3x | 549K | REIT |
| USDE | [TV](https://www.tradingview.com/chart/?symbol=USDE) | $2.08 | -24.4% | +24.0% | $2.58 | -6.2% | 266K | 214K | 1.2x | 5.5M | Packaged Software |
| STKE | [TV](https://www.tradingview.com/chart/?symbol=STKE) | $1.60 | +36.8% | +7.5% | $1.72 | +47.0% | 124K | 670K | 0.2x | 25.9M | Financial Conglomerates |
| UNCY | [TV](https://www.tradingview.com/chart/?symbol=UNCY) | $5.28 | +12.6% | +6.1% | $5.60 | +19.4% | 113K | 4.6M | 0.0x | 24.3M | Biotechnology |
| WCT | [TV](https://www.tradingview.com/chart/?symbol=WCT) | $1.21 | +29.2% | +5.8% | $1.28 | +36.7% | 61K | 267K | 0.2x | 909K | Packaged Software |

**SIP verification (bars from 20:00Z / 16:00 ET, fresh to ~16:45 ET):**
- **JEM** — REAL accumulation, now BUILDING to new AH highs: 375K→728K→**1.51M**→745K→…→952K sh/bar, 3,046→13,643 trades/bar peak. Consolidated $4.0–4.5 (16:15–16:40 ET), then broke to a **new AH high at 16:45 ET** (close $5.06, high $5.24, 8,981 trades). Real two-sided book: **bid $4.94 x100 / ask $4.98 x100 @16:54 ET**. SIP VWAP corroborates (no bad print). Day -19.1% (≤-15% dead-cat zone) BUT AH builds to reclaim **+54% above previous close**, AH% rising across 22:30 (+36.8%) → 23:00 (+38.9%) → now (~+58%). Reclaim above close negates the "still falling" thesis → **DEAD-CAT-OVERRIDE WATCH** (skip live, record hypothetical). **Catalyst:** GlobeNewswire PR July 1 — board approved *exploring* an AI + blockchain + crypto-payment supply-chain platform (707 Cayman Holdings). Buzzword "exploration" (not a signed deal) = weak, **Grade C**; plus dilution overhang (F-1 for 48.75M-share resale via Hudson Global equity purchase agreement). Stock pumped intraday to ~$8.46 (10 AM ET) then dumped to close $3.21 — the AH bounce is off that dump. Weak/dilution-tainted catalyst reinforces the skip; dead-cat filter protects here.
- **ALPS** — turned **SPIKE→FADE**. Peaked $0.86 @16:05 ET (early), volume collapsing (5,684 → 1,342 → 657 → …→ 80 trades/bar), price faded to $0.68 (below peak). AH% dropped 22:30 (+23.5%/$0.72) → now (+14.8%/$0.67). Fresh book stale (last quote @16:05 ET). Was the 22:30 BUILD hope; no longer holding → skip.
- **LHAI** — Total% +337.9% (far over +150% ceiling), VRatio 0.5x (fails ceiling-override >5x requirement), and fading: quote **bid $2.63 / ask $2.65** vs scanner AH $2.89. Regular-session pump extension, no override → skip (ceiling).
- **WHLR** — dead-cat: Day -20.8%, Total -4.0% (still below regular close), thin AH. Skip.
- **USDE** — dead-cat: Day -24.4%, Total -6.2% (below close), VRatio 1.2x. Skip.
- **STKE / UNCY / WCT** — thin AH (VRatio 0.2x / 0.0x / 0.2x), tiny AH volume — no real extended-hours spike. Skip.

**Decision: No live entry.** JEM is the only real AH build but sits in the dead-cat-override bucket (Day -19.1%, weak/dilution catalyst, AH bounce off an intraday pump-dump) → skip live, record hypothetical below. ALPS faded from its 22:30 BUILD. LHAI over ceiling. All others thin AH or dead-cat. No BUILD candidate clears the entry gates tonight.

**Hypothetical (DEAD-CAT-OVERRIDE WATCH data collection):**

| Ticker | Hyp. Entry | Entry Time | Basis | Track |
|--------|-----------|-----------|-------|-------|
| JEM | $4.98 (ask) | 23:00 CET (5:00 PM ET) | Day -19.1% but AH reclaims +54% above close, AH% rising ≥2 scans, real book, new AH high 16:45 ET | Compare PM peak vs $4.98 to test whether dead-cat filter should become conditional |

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| ALZN | $1.31 | $1.29 | -1.5% | $1.45 (+10.7%) | 1 | None | SELL | Grade None → exit first PM opportunity; faded from overnight peak, no catalyst |

**Actions taken:**
- Submitted extended-hours limit SELL 73 ALZN @ $1.29 (id f7da27e2). Order resting in thin early-premarket book (4:30 AM ET); will fill as premarket liquidity arrives.
- Overnight peak updated to $1.45 (was $1.40).
- Hard stop $1.18 (-10%) not hit. Position near breakeven.

**Note:** Confirm fill at 14:30 CET run; record real fill price and move ALZN to Closed Positions.
