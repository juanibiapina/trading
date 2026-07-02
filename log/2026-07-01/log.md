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

## Scan 00:30 CET (6:30 PM ET) — AH, entry-eligible

`scan.py --all` (AFTERHOURS): **13 hits.**

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| DSY | [TV](https://www.tradingview.com/chart/?symbol=DSY) | $2.88 | +7.5% | +83.3% | $5.28 | +97.0% | 383K | 133K | 2.9x | 1.3M | Miscellaneous (Big Tree Cloud) |
| USDE | [TV](https://www.tradingview.com/chart/?symbol=USDE) | $2.08 | -24.4% | +214.4% | $6.54 | +137.8% | 4.0M | 753K | 5.3x | 5.5M | Packaged Software |
| JEM | [TV](https://www.tradingview.com/chart/?symbol=JEM) | $3.21 | -19.1% | +25.2% | $4.02 | +1.3% | 8.6M | 21.3M | 0.4x | ~4.5M | Wholesale Distributors |
| WHLR | [TV](https://www.tradingview.com/chart/?symbol=WHLR) | $0.99 | -20.8% | +19.1% | $1.18 | -5.7% | 1.7M | 923K | 1.9x | 549K | REIT |
| CAST | [TV](https://www.tradingview.com/chart/?symbol=CAST) | $4.86 | -27.7% | +14.4% | $5.56 | -17.3% | 672K | 15.8M | 0.0x | 16.5M | Internet Software/Services |
| SKYQ | [TV](https://www.tradingview.com/chart/?symbol=SKYQ) | $2.97 | -19.1% | +6.4% | $3.16 | -13.9% | 406K | 37.1M | 0.0x | 3.8M | Integrated Oil |
| WCT | [TV](https://www.tradingview.com/chart/?symbol=WCT) | $1.21 | +29.2% | +40.5% | $1.70 | +81.6% | 378K | 301K | 1.3x | 909K | Packaged Software |
| HUMA | [TV](https://www.tradingview.com/chart/?symbol=HUMA) | $0.67 | -13.8% | +5.4% | $0.71 | -9.1% | 315K | 26.6M | 0.0x | 244.5M | Biotechnology |
| AVAT | [TV](https://www.tradingview.com/chart/?symbol=AVAT) | $0.50 | +0.1% | +10.3% | $0.55 | +10.4% | 279K | 902K | 0.3x | 20.7M | Financial Conglomerates |
| SLGB | [TV](https://www.tradingview.com/chart/?symbol=SLGB) | $0.66 | +5.4% | +6.1% | $0.70 | +11.8% | 129K | 248K | 0.5x | 3.0M | Air Freight/Couriers |
| DEFT | [TV](https://www.tradingview.com/chart/?symbol=DEFT) | $0.51 | -0.7% | +5.5% | $0.54 | +4.8% | 76K | 3.4M | 0.0x | 352.9M | Investment Managers |
| SENS | [TV](https://www.tradingview.com/chart/?symbol=SENS) | $5.36 | -5.6% | +5.2% | $5.64 | -0.7% | 74K | 1.2M | 0.1x | 45.9M | Electronic Components |
| BTCS | [TV](https://www.tradingview.com/chart/?symbol=BTCS) | $1.12 | +0.9% | +6.2% | $1.19 | +7.2% | 70K | 1.3M | 0.1x | 38.5M | Regional Banks |

**SIP verification (bars from 20:00Z / 16:00 ET):**
- **DSY** (NEW to AH, 1st AH appearance) — **REAL accumulation, fresh late BUILD.** Flat/quiet through 16:00–17:55 ET (~140–1,000 sh/bar), then broke out at **18:05 ET**: $2.95→$5.17 high, 82,444 sh / 1,156 trades → 18:10 ET $5.88 high, **511,276 sh / 8,619 trades** → 18:15 ET **new AH high $6.46**, 389,013 sh / 6,768 trades (close $6.26). Yahoo shows a spike to $6.99 then pullback to ~$5.51. Real spike, positive Day +7.5% (NOT dead-cat), ideal float 1.3M, Total% +97% (under 150% ceiling). **Book stale** (`bid $2.40 / ask $3.27 @20:00Z` = 16:00 ET, pre-breakout — not a current fillable read). **Catalyst:** structured search (4 calls) found **no same-day catalyst** — recent DSY news is stale (Apr listing transfer, Feb/Jan AI-buzzword PRs). Chinese small-cap with 1-for-20 reverse-split history = classic low-float squeeze profile. **Two blocks: (1) 1st AH appearance → fails the ≥2-AH-scan confirmation gate; (2) stale book can't confirm fillable AH liquidity at the breakout price.** Skip live; **top watch for 01:00** — if it confirms a 2nd AH scan >10% AND holds within ~20% of its ~$6.99 high with a real two-sided book, re-evaluate.
- **USDE** — **BAD PRINT + dead-cat.** Scanner AH $6.54 (+214%) is not corroborated by SIP: SIP high only $2.79 (16:35 ET), now faded to $2.33–2.57; quote `bid $2.52 / ask $2.55`. The $6.54 print is spurious. Real move is an early-peak (16:35 ET) fade off a Day -24.4% sell-off (dead-cat). Skip as stale VRatio / bad print + dead-cat.
- **JEM** — **DEAD-CAT-OVERRIDE WATCH continues.** AH now fading further: peak $5.47 @16:50 ET → $4.02 now. Real book unchanged `bid $4.94 / ask $4.98`. Day -19.1% (≤-15% dead-cat zone), weak AI/blockchain "exploration" PR + F-1 dilution overhang (Grade C). Skip live — hypothetical already recorded at 23:00 @ $4.98 (unchanged).
- **WHLR** (Total -5.7%) / **CAST** (Total -17.3%, VRatio 0.0x) / **SKYQ** (Day -19.1%, Total -13.9%, VRatio 0.0x — same faded-spike profile as the SKYQ Jun 10 -27.6% loss) / **HUMA** (Total -9.1%, float 244.5M) — dead-cat bounces still below their regular close and/or thin. Skip.
- **WCT** (VRatio 1.3x, AH vol 378K but float 909K, Total +81.6% — climbing but tiny AvgVol base, no SIP-confirmed real book) / **AVAT / SLGB / DEFT / SENS / BTCS** — thin AH (VRatio 0.0–0.5x), no real extended-hours spike. Skip.

**Decision: No live entry.** DSY is the one genuine fresh real-volume BUILD (positive day, ideal 1.3M float, real accumulation) but fails the ≥2-AH-scan confirmation gate (1st AH appearance) and has a stale book at the breakout price, plus no same-day catalyst found → skip live, top watch for 01:00 (consistent with the EHGO 1-AH-scan skip earlier tonight). USDE is a bad print off a dead-cat. JEM stays in dead-cat-override watch (hypothetical tracked at $4.98). All others dead-cat or thin.

**Watch for 01:00 CET:** DSY — if it confirms a 2nd AH scan >10%, holds within ~20% of its ~$6.99 high, and shows a real two-sided book, re-evaluate for entry. JEM — track PM reclaim vs $4.98 hypothetical.

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| ALZN | $1.31 | $1.29 | -1.5% | $1.45 (+10.7%) | 1 | None | SELL | Grade None → exit first PM opportunity; faded from overnight peak, no catalyst |

**Actions taken:**
- Submitted extended-hours limit SELL 73 ALZN @ $1.29 (id f7da27e2). Order resting in thin early-premarket book (4:30 AM ET); will fill as premarket liquidity arrives.
- Overnight peak updated to $1.45 (was $1.40).
- Hard stop $1.18 (-10%) not hit. Position near breakeven.

**Note:** Confirm fill at 14:30 CET run; record real fill price and move ALZN to Closed Positions.

## Morning Evaluation — 10:20 CET

### Today's Winner

**USDE (StablecoinX Inc.)** — Packaged Software (crypto/stablecoin treasury) — *real, liquid AH→PM winner; DETECTED but wrongly skipped*
- Catalyst: crypto/stablecoin-treasury news (specifics unverified premarket) — real-volume AH melt-up, not a phantom. Likely Grade A/B given the 1M+ share/16k+ trade bars.
- Jun 30 close: $2.75 | Jul 1 regular close: ~$2.08 (Day **-24.4%**, a down day → dead-cat starting point)
- AH last night: chopped $2.1–2.5 until 17:45 ET, then exploded → **peak $7.69 @18:30 ET (SIP)** / Yahoo $7.30. That is **+270% from the $2.08 reg close / +180% from the $2.75 prior close.**
- Premarket now: $5.61 (+104% vs $2.75); PM peak **$5.70 @04:00 ET**
- Hypothetical P&L: AH breakout entry ~$4.40 (17:55 ET) → AH peak $7.69 = **+75%**; → PM peak $5.70 = **+30%**. AH was the better exit (AH peak > PM peak).
- Float: 5.5M | Market Cap: ~$12M
- **Liquidity: real.** SIP bars during the run: 675K→951K→1.35M→1.14M→1.11M sh/bar, 7,271→16,763 trades/bar, VWAP $3.59→$6.57. Fully fillable — this was a tradeable winner, not a phantom.

**Scanner Diagnostic:**
- Detectable at screening time? **YES** — USDE appeared in every AH scan (23:00, 23:30, 00:00, 00:30 CET) and at **00:30 CET the scanner showed the real move: AH $6.54 (+214%), VRatio 5.3x.** SIP confirms $6.54 exactly (22:10Z bar: H $6.88 / C $6.54 / VWAP $6.12 on 1.1M sh, 17,654 trades). It was **not** a bad print.
- **Why we didn't act — verification-layer false-negative (the key finding):**
  1. **TradingView postmarket feed lag.** At the 00:00 CET scan (18:00 ET), USDE was really $5.98 (+117%) on a 1.35M-share bar, but TradingView showed a stale AH $2.53 / Total -8% / VRatio 1.7x → classified dead-cat. The feed lagged ~30 min during the fast move.
  2. **Stale SIP/quote verification.** At the 00:30 CET scan TradingView caught up (+214%/$6.54), but the live SIP-bar pull and the `broker.js quote` both returned stale ~16:35–16:44 ET data ($2.52/$2.55, SIP high $2.79) that didn't reflect the 17:45+ ET explosion → the real +214% was wrongly called a **BAD PRINT** and skipped. (Confirmed this morning: `broker.js quote USDE` *still* returns `bid $2.52 / ask $2.55 @16:44 ET` — the free-tier quote endpoint serves a stale cached quote; the SIP bars I pulled retrospectively show the real $6–7.69 run.)
- This is a **data-source reliability failure, not a detection miss.** The scanner surfaced USDE; the price/volume feeds serving the live scan (both TradingView and the verification SIP/quote) were stale during the fast move, and the bad-print heuristic fired a false negative on a real winner.
- Scanner gap / fix: add a **freshness check** to the verification step — compare the SIP-bar / quote timestamp against the scan time. If the "trusted" verification source is stale (timestamp far behind the scan), do **not** use it to override a strong scanner signal (high VRatio + large AH%); treat the scanner reading as unconfirmed-but-live rather than a bad print, and re-pull. Also flag TradingView feed lag when a name's AH% jumps discontinuously between scans (−8% → +214% in one 30-min step is a lag artifact, not reality).

### Baseline Tracking

- Days tracked: **41** (was 40 + 1)
- Winners detected by scanner: **35/40 (87.5%)** — USDE detected (added to list). Day-39 BTCT remains excluded (late-AH-tail).
- Winner selected for paper trade: **22/40 (55.0%)** — USDE **NOT** selected (wrongly rejected as bad print by stale verification data). First genuinely-investable, liquid winner in a while that was detected but wrongly skipped — selection rate drops 57.9% → 55.0%.
- Target: >80% detection
- Status: **BASELINE MET** (detection) — but a **selection/verification failure** to fix.

### Retrospective Scan Results

Live premarket scan (04:20 ET): 6 hits — WHLR +138.5% (PM-only gapper), USDE +175% (winner, AH→PM continuation), JEM +30.8% (dead-cat-override fade), DSY +50%, SDEV +27.9%, BTOG +6%.

AH reconstruction (SIP bars, Jul 1 16:00–20:00 ET):
- **USDE**: down/chop to 17:45 ET, then ramp $2.85→$7.69 by 18:30 ET on 1M+ sh/bar, 16k+ trades/bar. Real, liquid. AH peak $7.69 > PM peak $5.70.
- **DSY**: quiet to 18:05 ET, then broke out $2.95→$6.46 (18:15 ET) on 511K/389K-sh bars, held $5–6 through 19:55 ET. Real. Caught at 00:30 (+83.3%, VRatio 2.9x) but skipped on ≥2-AH-scan gate + stale book. AH peak ~$6.46 > PM peak $4.73.
- **WHLR**: flat $1.0–1.4 all AH (peak $1.37 @19:10 ET, only +10%, thin ≤124K-sh bars). PM-only gapper (below).
- **EHGO**: SPIKE→FADE off $3.48 early peak (17:05 ET). PM peak $2.67 stayed **below** AH peak — fade rule correct.

### Open Position P&L (Alpaca)

`broker.js positions`: **No open positions.** (ALZN SELL from the 10:30 position-evaluation run — fill confirmation is that run's job, not this one.)

**No executed positions this session.** USDE was a real winner but was skipped (verification false-negative); no fill. It belongs in the Scanner Diagnostic as hypothetical (AH ~$4.40 → PM peak $5.70 = +30%), not here.

**Total Realized P&L (Alpaca fills only): €0.00**

### Scanner Effectiveness

- Evening scans ran: **7 of 7** (21:30, 22:00, 22:30, 23:00, 23:30, 00:00, 00:30 CET). Full coverage — entry window captured.
- Candidates found: USDE (detected, wrongly skipped), DSY, JEM, EHGO, WHLR, WCT, and thin names.
- Retrospective matches: USDE, DSY, JEM, EHGO all appeared in evening scans. No missed movers — the failure was classification, not detection.

### Missed Opportunities

| Ticker | AH Change | Why Missed | Would Be Profitable? |
|--------|-----------|------------|---------------------|
| USDE | +214% (AH $6.54, SIP-confirmed) | **Not a detection miss** — surfaced at 00:00/00:30 CET. Skipped by stale verification: TradingView feed-lagged at 00:00 ($2.53 vs real $5.98), then SIP/quote verification returned stale 16:44 ET data at 00:30 → false bad-print call. | Yes — hypo AH ~$4.40 → PM peak +30%, → AH peak +75%. Liquid/fillable. |

### AH Mover Follow-Through

| Ticker | AH Peak | Peak Time | AH Trajectory | Current PM | From Peak | From Close | Verdict |
|--------|---------|-----------|---------------|------------|-----------|-----------|---------|
| USDE | $7.69 (+180% vs $2.75) | 18:30 ET | Build (real, 1M+ sh/bar) | $5.61 | -27% | +104% | Real winner; DETECTED, wrongly skipped; AH peak > PM peak |
| DSY  | $6.46 (+141% vs $2.68) | 18:15 ET | Late Build (18:05 ET) | $4.32 | -33% | +61% | Real; skipped on ≥2-scan gate; AH peak > PM peak |
| JEM  | $5.47 (+38% vs $3.97) | 16:50 ET | Spike→fade | $4.09 | -25% | +3% | Dead-cat-override; faded; AH peak > PM peak |
| EHGO | $3.48 (+31%) | 17:05 ET | Spike→fade | $2.54 | -27% | +95% | Fade correct; PM peak $2.67 < AH peak |

**AH-peak-vs-PM-peak check:** All four had AH peak > PM peak — AH was the better exit. **USDE AH peak +180% > PM peak +107%** — another extreme-runner data point where AH peak beat PM (the AH-peak-fade hypothesis; USDE at +180% is under the 250% threshold but still faded AH→PM). DSY (+141%) and EHGO also AH>PM.

### Price Charts

```
USDE — 2-Day (5-min), real liquid AH→PM winner
Jun30 close $2.75 | Jul1 reg close ~$2.08 (Day -24.4%) | AH peak $7.69 @18:30 ET | PM peak $5.70 @04:00 ET | now $5.61
17:45 $2.90 ─ 17:50 $3.83 ─ 17:55 $4.38 ─ 18:00 $5.98 ─ 18:10 $6.56 ─ 18:30 $7.30/7.69 (peak) ─ 23:55 $5.84 ─ PM $5.70→$5.61
SIP volume during run: 675K→951K→1.35M→1.14M sh/bar, 7.3k→16.8k trades/bar — fully fillable.

WHLR — PM-only gapper (549K float REIT)
Prev close $1.25 | AH flat $1.0-1.4 (peak $1.37 @19:10 ET, thin) | PM peak $2.66 @04:10 ET | now $2.16
PM: 04:00 $2.36 ─ 04:05 $2.57 ─ 04:10 $2.66 (peak) ─ 04:15 $2.50 ─ 04:20 $2.27 (2 bars near peak then fade)

DSY — real late-AH BUILD, faded into PM
Prev close $2.68 | AH breakout 18:05 ET → peak $6.46 @18:15 ET | PM peak $4.73 @04:05 ET | now $4.32
```

### Notes

- **KEY FINDING — verification-layer false-negative on a real winner (USDE).** For the first time in a while, a genuinely investable, liquid winner (+180% AH on 1M+ sh/bar) was **detected** by the scanner but **wrongly skipped** — not by a strategy gate but by **stale verification data**. Two stacked data failures: (1) TradingView postmarket feed lagged ~30 min at the 00:00 CET scan (showed $2.53 vs real $5.98); (2) the SIP-bar pull + `broker.js quote` returned stale ~16:44 ET data at 00:30, triggering a false "bad print" rejection of the real +214% read. **The bad-print heuristic fired a false negative because the trusted verification source was itself stale.** Fix: freshness-check the SIP/quote timestamp before letting it override a live scanner signal; flag discontinuous AH% jumps (−8%→+214% in one step) as feed-lag artifacts. This is a **data-reliability** fix, not a threshold change. (Confirmed 10:20 CET: `broker.js quote USDE` still returns the stale $2.52/$2.55 @16:44 ET.)
- **Dead-cat-override angle on USDE.** USDE was also a dead-cat-override candidate: Day -24.4% (down big) that then reclaimed to +138% above the prior close **on real 1M-share volume**. Unlike the JEM/BYAH low-volume bounces, this reclaim was massive and real → this is the **strongest data point yet that the dead-cat filter should be conditional on real reclaim volume** (a Day-down stock reclaiming far above its close on sustained 1M+ sh/bar volume is not a dead cat). Tally with BYAH (Jun 11, hypo +72%) — dead-cat-override winners now include a huge one.
- **DEAD-CAT-OVERRIDE WATCH outcome (JEM, from last night):** hypo entry $4.98 (23:00 CET) → PM peak $4.19 = **-15.9%**. JEM faded — supports the dead-cat filter *here* (low-volume, weak/dilution catalyst). Contrast with USDE (real-volume reclaim, big winner): the discriminator is **reclaim volume**, not the dead-cat label alone.
- **Fade-rule tracking (EHGO):** skipped SPIKE→FADE off $3.48 early peak (17:05 ET). PM peak $2.67 stayed **below** AH peak → fade rule **correct**. Float **1.4M (ultra-low)** yet it did **not** re-explode above its AH peak — a low-float fader that stayed faded, which **weakens** the "low-float faders re-explode in PM" hypothesis (CRE/LNKS). Record as a correct-skip low-float contrast.
- **PM-only gapper tracking:** biggest raw PM mover = **WHLR** (+112.7% vs $1.25, PM peak $2.66). AH was flat (<10%, thin) → **PM-only gapper** (structurally undetectable by the AH scanner). Investability: **holdable-marginal** — 2 consecutive 5-min bars near peak ($2.57, $2.66) then faded to $2.27 within 10 min; 549K float REIT. Not a scanner failure; do not count against detection.
- **Late-AH-tail tracking:** none tonight. USDE's surge (17:45 ET) and DSY's breakout (18:05 ET) both fired **inside** the scanned window and were caught at 00:00/00:30 CET. No post-18:30-ET tail case.
- **Coverage-failure tally:** none tonight (7/7). No recurrence.
