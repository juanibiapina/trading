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

## Scan 23:30 CET (5:30 PM ET) — AH, entry-eligible

`scan.py --all` (AFTERHOURS): **8 hits.**

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| JEM | [TV](https://www.tradingview.com/chart/?symbol=JEM) | $3.21 | -19.1% | +51.7% | $4.87 | +22.7% | 7.0M | 21.1M | 0.3x | ~4.5M | Wholesale Distributors |
| EHGO | [TV](https://www.tradingview.com/chart/?symbol=EHGO) | $2.66 | +104.6% | +17.7% | $3.13 | +140.8% | 3.5M | 33.9M | 0.1x | 1.4M | Wholesale Distributors |
| WHLR | [TV](https://www.tradingview.com/chart/?symbol=WHLR) | $0.99 | -20.8% | +16.2% | $1.15 | -8.0% | 1.3M | 874K | 1.5x | 549K | REIT |
| USDE | [TV](https://www.tradingview.com/chart/?symbol=USDE) | $2.08 | -24.4% | +13.5% | $2.36 | -14.2% | 350K | 224K | 1.6x | 5.5M | Packaged Software |
| HUMA | [TV](https://www.tradingview.com/chart/?symbol=HUMA) | $0.67 | -13.8% | +8.5% | $0.73 | -6.5% | 240K | 26.6M | 0.0x | 244.5M | Biotechnology |
| STKE | [TV](https://www.tradingview.com/chart/?symbol=STKE) | $1.60 | +36.8% | +6.9% | $1.71 | +46.2% | 148K | 673K | 0.2x | 25.9M | Financial Conglomerates |
| CAST | [TV](https://www.tradingview.com/chart/?symbol=CAST) | $4.86 | -27.7% | +9.1% | $5.30 | -21.1% | 97K | 15.7M | 0.0x | 16.5M | Internet Software/Services |
| WCT | [TV](https://www.tradingview.com/chart/?symbol=WCT) | $1.21 | +29.2% | +8.3% | $1.31 | +39.9% | 76K | 268K | 0.3x | 909K | Packaged Software |

**SIP verification (bars from 20:00Z / 16:00 ET, fresh to ~17:15 ET):**
- **EHGO** (NEW to AH — 21:30 appearance was regular session, doesn't count toward ≥2 AH-scan gate) — REAL accumulation. Consolidated $2.42–2.70 (16:00–16:50 ET), then **broke out at 17:00 ET**: $3.20 high / 1.12M sh / 7,519 trades → **peak $3.48 @17:05 ET** / 1.30M sh / 9,496 trades. Last 3 bars **declining**: close $3.35 (17:05) → $3.13 (17:10) → $2.97 (17:15); Yahoo timeline chops $2.69–2.83 after. Off peak ~-15%. Positive Day +104.6% (NOT a dead-cat), float 1.4M (ideal), Total% +140.8% (under 150% ceiling). Book (stale @16:51 ET): bid $2.55 / ask $2.61. **Catalyst:** "breakthrough AI product platform" (buzzword, drove intraday +65–85%) **BUT active heavy dilution** — $750K registered direct offering priced at **$1.00/share** closing today (July 1), on top of a $1.479M offering closed June 25. Dilution at $1.00 vs $2.66+ price = **Grade D overhang**. Stock has whipsawed $6.75→$1.30 in weeks. **Two disqualifiers: (1) only 1 AH scan — fails the ≥2-AH-scan confirmation gate; (2) early peak (17:05 ET) now fading across 3 bars.** Plus dilution. **Skip live; top watch for 00:00** — needs to confirm a 2nd AH scan AND hold/rebuild, but the $1.00 dilution keeps grade weak even then.
- **JEM** — continue **DEAD-CAT-OVERRIDE WATCH**. Real accumulation, AH% still rising across scans: +36.8% (22:30) → +38.9% (23:00) → +51.7% (now). Peak $5.47 @16:50 ET, now fading to $4.82 (17:15 ET, -12% off peak). Real book bid $4.94 / ask $4.98. Day -19.1% (≤-15% dead-cat zone) but reclaims +22.7% above close. Catalyst still weak (AI/blockchain "exploration" PR) + F-1 dilution overhang → Grade C. **Skip live** (hypothetical already recorded at 23:00 @ $4.98; entry unchanged, still ~$4.98 book).
- **WHLR** (Total -8.0%, below close) / **USDE** (Total -14.2%, below close) / **HUMA** (Total -6.5%, float 244.5M, VRatio 0.0x) / **CAST** (Total -21.1%, below close, VRatio 0.0x) — dead-cat bounces still under their regular close and/or thin. Skip.
- **STKE / WCT** — thin AH (VRatio 0.2x / 0.3x, tiny AH vol). No real spike. Skip.

**Decision: No live entry.** EHGO is the only fresh real AH build with positive day + ideal float, but it fails the ≥2-AH-scan gate (first AH appearance), is fading off an early 17:05 peak, and carries active $1.00/share dilution → skip live, top watch for 00:00. JEM stays in dead-cat-override watch (skip live, hypothetical tracked). All others dead-cat or thin. No candidate clears the entry gates tonight.

**Watch for 00:00 CET:** EHGO — if it confirms a 2nd AH scan >10% AND holds/rebuilds within ~20% of $3.48, re-evaluate (dilution still caps grade). JEM — track PM reclaim vs $4.98 hypothetical.

## Scan 00:00 CET (6:00 PM ET) — AH, entry-eligible

`scan.py --all` (AFTERHOURS): **12 hits.**

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| JEM | [TV](https://www.tradingview.com/chart/?symbol=JEM) | $3.21 | -19.1% | +46.1% | $4.69 | +18.1% | 8.0M | 21.3M | 0.4x | ~4.5M | Wholesale Distributors |
| EHGO | [TV](https://www.tradingview.com/chart/?symbol=EHGO) | $2.66 | +104.6% | +7.1% | $2.85 | +119.2% | 4.7M | 34.1M | 0.1x | 1.4M | Wholesale Distributors |
| WHLR | [TV](https://www.tradingview.com/chart/?symbol=WHLR) | $0.99 | -20.8% | +19.3% | $1.18 | -5.5% | 1.6M | 908K | 1.7x | 549K | REIT |
| CAST | [TV](https://www.tradingview.com/chart/?symbol=CAST) | $4.86 | -27.7% | +13.4% | $5.51 | -18.0% | 581K | 15.8M | 0.0x | 16.5M | Internet Software/Services |
| USDE | [TV](https://www.tradingview.com/chart/?symbol=USDE) | $2.08 | -24.4% | +21.6% | $2.53 | -8.0% | 393K | 230K | 1.7x | 5.5M | Packaged Software |
| SKYQ | [TV](https://www.tradingview.com/chart/?symbol=SKYQ) | $2.97 | -19.1% | +9.1% | $3.24 | -11.7% | 367K | 37.1M | 0.0x | 3.8M | Integrated Oil |
| HUMA | [TV](https://www.tradingview.com/chart/?symbol=HUMA) | $0.67 | -13.8% | +7.0% | $0.72 | -7.7% | 300K | 26.6M | 0.0x | 244.5M | Biotechnology |
| BIYA | [TV](https://www.tradingview.com/chart/?symbol=BIYA) | $0.54 | -3.7% | +5.9% | $0.57 | +2.0% | 298K | 45.3M | 0.0x | 2.3M | Personnel Services |
| WCT | [TV](https://www.tradingview.com/chart/?symbol=WCT) | $1.21 | +29.2% | +5.8% | $1.28 | +36.7% | 87K | 270K | 0.3x | 909K | Packaged Software |
| DEFT | [TV](https://www.tradingview.com/chart/?symbol=DEFT) | $0.51 | -0.7% | +5.5% | $0.54 | +4.8% | 75K | 3.4M | 0.0x | 352.9M | Investment Managers |
| BTCS | [TV](https://www.tradingview.com/chart/?symbol=BTCS) | $1.12 | +0.9% | +7.1% | $1.20 | +8.1% | 69K | 1.3M | 0.1x | 38.5M | Regional Banks |
| VFF | [TV](https://www.tradingview.com/chart/?symbol=VFF) | $1.99 | -0.5% | +5.0% | $2.09 | +4.5% | 52K | 1.2M | 0.0x | 108.7M | Agricultural Commodities |

**SIP verification (bars from 20:00Z / 16:00 ET, fresh to ~17:35 ET):**
- **EHGO** (top watch from 23:30, now its 2nd AH scan) — **SPIKE→FADE confirmed.** Broke out to peak **$3.48 @17:05 ET** (1.30M sh / 9,496 trades), then declined every bar since: $3.35→$3.13→$2.97→$2.69→$2.85→$2.86→$2.79 (17:35 ET), now ~-20% off peak. Volume/trades fading in lockstep (9,496→5,229→4,131→2,846→2,054→1,124→1,000). AH% dropped across the 2 AH scans: +17.7% (23:30) → +7.1% (00:00). Book stale bid $2.55 / ask $2.61. **Fails hold/rebuild** (current $2.79 vs $3.48 high = >20% off, and declining, not rebuilding) + active **$1.00/share dilution (Grade D)**. Early 17:05 peak + fading = 0/7 pattern → **skip.**
- **JEM** — **DEAD-CAT-OVERRIDE WATCH continues.** AH% now fading from its peak read: +36.8% (22:30) → +38.9% (23:00) → +51.7% (23:30) → +46.1% (00:00). Peak $5.47 @16:50 ET, now $4.69. Real book unchanged bid $4.94 / ask $4.98. Day -19.1% (≤-15% dead-cat zone), weak AI/blockchain "exploration" PR + F-1 dilution overhang (Grade C). **Skip live** — hypothetical already recorded at 23:00 @ $4.98 (unchanged). Track PM reclaim vs $4.98.
- **WHLR** (Total -5.5%) / **USDE** (Total -8.0%) / **CAST** (Total -18.0%, VRatio 0.0x) / **SKYQ** (Day -19.1%, Total -11.7%, VRatio 0.0x — same faded-spike profile as the SKYQ Jun 10 -27.6% loss) / **HUMA** (Total -7.7%, float 244.5M) — all dead-cat bounces still below their regular close and/or thin AH. Skip.
- **BIYA / WCT / DEFT / BTCS / VFF** — thin AH (VRatio 0.0–0.3x, tiny AH vol), no real extended-hours spike. Skip.

**Decision: No live entry.** SPIKE→FADE / dead-cat-only night. The 00:00 top watch (EHGO) confirmed a fade off its early 17:05 peak on its 2nd AH scan (fails hold/rebuild) with $1.00 dilution. JEM stays in dead-cat-override watch (skip live, hypothetical tracked at $4.98). Every other hit is a dead-cat bounce below its close or thin AH. Per SPIKE→FADE-only-night rule, skip all rather than entering the least-bad option — a skip here avoids a predictable loss, it is not lost data.

**Final EOD watch:** JEM — track overnight/PM reclaim vs $4.98 hypothetical (dead-cat-override data collection). EHGO — record whether the faded early peak continues to bleed in PM (fade-pattern confirmation data).

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| ALZN | $1.31 | $1.29 | -1.5% | $1.45 (+10.7%) | 1 | None | SELL | Grade None → exit first PM opportunity; faded from overnight peak, no catalyst |

**Actions taken:**
- Submitted extended-hours limit SELL 73 ALZN @ $1.29 (id f7da27e2). Order resting in thin early-premarket book (4:30 AM ET); will fill as premarket liquidity arrives.
- Overnight peak updated to $1.45 (was $1.40).
- Hard stop $1.18 (-10%) not hit. Position near breakeven.

**Note:** Confirm fill at 14:30 CET run; record real fill price and move ALZN to Closed Positions.
