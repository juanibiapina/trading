# Post-Market Screening - 2026-06-29

## Scan 21:30 CET (3:30 PM ET) — REGULAR SESSION

Scan ran before AH opens (4:00 PM ET / 22:00 CET). **No paper trades** — regular-session caution rule. Candidates flagged as watch pending AH confirmation. Stocks that spike intraday but don't carry into AH tend to fade.

Top movers (regular-session, AH data not yet available):

| Ticker | Chart | Price | Chg% | IRVol | VChg% | Float | MCap | Industry | Note |
|--------|-------|-------|------|-------|-------|-------|------|----------|------|
| TVRD | [TV](https://www.tradingview.com/chart/?symbol=TVRD) | $1.86 | +24.0% | 58.8x | -14.8% | 6.1M | 17.4M | Biotechnology | Watch — low float, strong IRVol |
| AZI | [TV](https://www.tradingview.com/chart/?symbol=AZI) | $2.63 | +41.4% | 10.7x | -99.8% | 4.4M | 179.0M | Specialty Stores | Watch — vol fading |
| ZCMD | [TV](https://www.tradingview.com/chart/?symbol=ZCMD) | $1.32 | +38.5% | 10.3x | -20.7% | 101K | 3.0M | Misc Commercial Svcs | Watch — tiny float |
| KUST | [TV](https://www.tradingview.com/chart/?symbol=KUST) | $1.26 | +32.6% | 7.8x | -92.3% | 577K | 790K | Misc Commercial Svcs | Watch — tiny float, vol fading |
| CNET | [TV](https://www.tradingview.com/chart/?symbol=CNET) | $1.13 | +22.9% | 100.0x | -58.4% | 3.1M | 4.1M | Advertising/Marketing | Watch — low float |

Only enter if a candidate reappears in a subsequent AH scan (22:00+ CET) with sustained momentum.

## Scan 22:00 CET (4:00 PM ET)

First AH scan. `scan.py --all` returned 0 hits — none of the regular-session watch candidates (TVRD, AZI, ZCMD, KUST, CNET) carried into after-hours with qualifying momentum/volume. Observation-only window anyway (22:00/22:30 scans are no-entry during learning phase).

No candidates found.

## Scan 22:30 CET (4:30 PM ET)

Second AH scan. `scan.py --all` returned 4 hits. Observation-only window (22:00/22:30 scans are no-entry during learning phase — entries start at 23:00 CET / 5:00 PM ET).

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| GANX | [TV](https://www.tradingview.com/chart/?symbol=GANX) | $1.98 | +13.1% | +24.7% | $2.47 | +41.1% | 2.9M | 812K | 3.5x | 41.4M | Biotechnology |
| JEM | [TV](https://www.tradingview.com/chart/?symbol=JEM) | $1.08 | -41.9% | +57.4% | $1.70 | -8.6% | 2.1M | 827K | 2.6x | 0 | Wholesale Distributors |
| MNDR | [TV](https://www.tradingview.com/chart/?symbol=MNDR) | $3.57 | +11.2% | +5.9% | $3.78 | +17.8% | 104K | 378K | 0.3x | 1.8M | Medical/Nursing Services |
| TMCI | [TV](https://www.tradingview.com/chart/?symbol=TMCI) | $4.27 | -4.3% | +7.7% | $4.60 | +3.1% | 86K | 1.7M | 0.1x | 48.1M | Medical Specialties |

**Evaluation (observation-only — no entries before 23:00 CET):**

- **GANX** — LEAD CANDIDATE. Biotech, Day +13.1%, AH peak +40.6% ($2.46 at 16:10 ET), holding +33.7% at 16:30 (within ~20% of peak — BUILD/hold profile). Total% +41.1%, well under the +150% extension ceiling. VRatio 3.5x. **Catalyst (Grade B):** Gain Therapeutics presented *positive interim Phase 1b data* for GT-02287 (Parkinson's, GBA1) at the 3rd International GBA1 Meeting 2026 — clinical data catalyst confirmed via company press release. Float 41.4M (above ideal <10M but not a filter; tracked for pattern analysis). First AH-scan appearance (22:00 had 0 hits). Needs to reappear at 23:00 for the 2-AH-scan requirement → then qualifies for entry.
- **JEM** — Skip: dead-cat bounce. Day -41.9% (crashed during regular session), AH bounce to $1.70 still -8.6% *below* prior close. Stays below regular close → genuine dead-cat, not a reclaim. No override flag.
- **MNDR** — Skip: AH +5.9% (<10% threshold), VRatio 0.3x (volume below average, fading).
- **TMCI** — Skip: AH +7.7% (<10% threshold), VRatio 0.1x (negligible AH volume).

No paper trades this scan (pre-23:00 observation window). GANX carried as the entry candidate for the 23:00 scan pending second AH-scan confirmation.

## Scan 23:00 CET (5:00 PM ET) — ENTRY WINDOW OPEN

Third AH scan, first entry-eligible scan (23:00+ CET / 5:00 PM ET). `scan.py --all` returned 5 hits.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| GANX | [TV](https://www.tradingview.com/chart/?symbol=GANX) | $1.98 | +13.1% | +25.8% | $2.49 | +42.3% | 7.1M | 1.3M | 5.5x | 41.4M | Biotechnology |
| JEM | [TV](https://www.tradingview.com/chart/?symbol=JEM) | $1.08 | -41.9% | +80.1% | $1.94 | +4.6% | 5.7M | 1.2M | 4.6x | 0 | Wholesale Distributors |
| CTNT | [TV](https://www.tradingview.com/chart/?symbol=CTNT) | $1.54 | -1.3% | +16.9% | $1.80 | +15.4% | 4.1M | 3.0M | 1.4x | 3.0M | Engineering & Construction |
| SLGB | [TV](https://www.tradingview.com/chart/?symbol=SLGB) | $0.55 | -1.1% | +11.0% | $0.61 | +9.8% | 131K | 1.5M | 0.1x | 3.0M | Air Freight/Couriers |
| TMCI | [TV](https://www.tradingview.com/chart/?symbol=TMCI) | $4.27 | -4.3% | +7.7% | $4.60 | +3.1% | 86K | 1.7M | 0.1x | 48.1M | Medical Specialties |

**Evaluation:**

- **GANX — ENTERED.** All gates cleared: 2 AH scans >10% (22:30 +24.7%, 23:00 +25.8%), float 41.4M (<50M), Day +13.1% (>-15%), Total% +42.3% (well under +150% ceiling), VRatio 5.5x. AH liquidity confirmed real two-sided book (bid $2.42 x200 / ask $2.43 x300). Yahoo intraday: AH high $2.50 at 16:40 ET, holding $2.40 at 17:00 (within ~5% of peak — BUILD/hold, not fade). Peak at 16:40 ET is before 18:30 but stock is holding near high, not declining → hold-vs-fade primary signal favors entry. **Catalyst Grade B:** positive interim Phase 1b data for GT-02287 (Parkinson's, GBA1) presented at 3rd International GBA1 Meeting 2026. **Order: bought 41 @ limit $2.46 → filled $2.39** (id ea649b1f). Cost basis $97.99.
- **JEM — Skip.** Day -41.9% (regular-session crash). Yahoo granular data (prev close $1.86) shows AH peak +11.8% ($2.08) at 16:30 ET, now fading to $1.84 (~flat). The scan's Total% +4.6% reflects a slight reclaim, but the granular intraday shows it *fading from its 16:30 peak*, not building across scans. No clean dead-cat-override (override needs AH% rising across ≥2 AH scans AND holding the reclaim — JEM is declining toward close). Data discrepancy noted (scan close $1.08 vs Yahoo prev close $1.86). Skip: dead-cat bounce, fading.
- **CTNT — Skip (watch).** Day -1.3%, AH +16.9%, low float 3.0M. First AH-scan appearance (22:00/22:30 had no CTNT) → only 1 AH scan >10%, fails the 2-AH-scan requirement. VRatio 1.4x (modest). Carry as watch for later scans.
- **SLGB — Skip.** AH +11.0% but VRatio 0.1x (131K vs 1.5M avg — negligible AH volume, likely fading). Total% +9.8% under threshold.
- **TMCI — Skip.** AH +7.7% (<10% threshold), VRatio 0.1x (86K, negligible AH volume).

**Entries this scan: 1 (GANX, Grade B).**

## Scan 23:30 CET (5:30 PM ET) — ENTRY WINDOW

Fourth AH scan. `scan.py --all` returned 5 hits. GANX already entered at 23:00 (position managed separately by premarket position-evaluation).

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| GANX | [TV](https://www.tradingview.com/chart/?symbol=GANX) | $1.98 | +13.1% | +19.2% | $2.36 | +34.9% | 9.0M | 1.5M | 6.0x | 41.4M | Biotechnology |
| CTNT | [TV](https://www.tradingview.com/chart/?symbol=CTNT) | $1.54 | -1.3% | +39.6% | $2.15 | +37.8% | 8.6M | 3.5M | 2.4x | 3.0M | Engineering & Construction |
| JEM | [TV](https://www.tradingview.com/chart/?symbol=JEM) | $1.08 | -41.9% | +68.5% | $1.82 | -2.2% | 6.5M | 1.3M | 4.9x | 0 | Wholesale Distributors |
| SLGB | [TV](https://www.tradingview.com/chart/?symbol=SLGB) | $0.55 | -1.1% | +5.8% | $0.58 | +4.6% | 168K | 1.5M | 0.1x | 3.0M | Air Freight/Couriers |
| TMCI | [TV](https://www.tradingview.com/chart/?symbol=TMCI) | $4.27 | -4.3% | +7.7% | $4.60 | +3.1% | 86K | 1.7M | 0.1x | 48.1M | Medical Specialties |

**Evaluation:**

- **CTNT — ENTERED.** New qualifying candidate. Now clears the 2-AH-scan requirement: 23:00 (+16.9%) and 23:30 (+39.6%) — and it is **BUILDING**, not fading (AH% rose +16.9% → +39.6% across the two scans). Yahoo 5m: AH high $2.15 at 17:10 ET, holding $2.07 at 17:30 (within ~5% of peak → BUILD/hold profile). Peak 17:10 is before 18:30 but stock is holding near high, not declining → hold-vs-fade primary signal favors entry. Float 3.0M (ideal <10M), Day -1.3% (>-15%), Total% +37.8% (well under +150% ceiling), VRatio 2.4x. Not a dead-cat (Day only -1.3%). AH liquidity confirmed real two-sided book (bid $1.95 x100 / ask $2.01 x100); CTNT traded real AH volume (8.6M, Yahoo 5m bars confirm). **Catalyst Grade None:** structured search (4 calls) found no same-day driver. Recent items are 4 days old — board authorized up-to-1-for-2,000 reverse split (Jun 25, Nasdaq $1 bid compliance = distress overhang) and short interest +511% to 9.5% of float (May 31→Jun 15). Likely a low-float short squeeze; no company catalyst. Entered with concern noted per learning-phase no-catalyst handling. **Order: bought 48 @ limit $2.05 → filled $2.05** (id 4f35924a; first order at $2.04 didn't fill against stale frozen quote, replaced at $2.10 → filled $2.05, stale order canceled). Cost basis $98.40. Grade None → exit at first premarket opportunity.
- **GANX — already held** (entered 23:00 @ $2.39). AH +19.2%/$2.36 at 23:30, AH Vol up to 9.0M, VRatio 6.0x. Holding. Managed by premarket position-evaluation, not re-entered.
- **JEM — Skip (dead-cat, fading).** Day -41.9% (regular-session crash). Yahoo (prev close $1.86): AH peaked +11.8% ($2.08) at 16:30 ET, now fading to ~$1.92 (+3.2%). Scan Total% -2.2% → back *below* prior close. Stays below close + fading from 16:30 peak → genuine dead-cat, not a reclaim. No override flag.
- **SLGB — Skip.** AH +5.8% (<10% threshold), VRatio 0.1x (168K, negligible AH volume).
- **TMCI — Skip.** AH +7.7% (<10% threshold), VRatio 0.1x (86K, negligible AH volume).

**Entries this scan: 1 (CTNT, Grade None — low-float squeeze, no catalyst, concern noted).**

## Scan 00:00 CET (6:00 PM ET) — ENTRY WINDOW

Fifth AH scan. `scan.py --all` returned 9 hits. GANX (entered 23:00) and CTNT (entered 23:30) already held; positions managed separately by premarket position-evaluation.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| CTNT | [TV](https://www.tradingview.com/chart/?symbol=CTNT) | $1.54 | -1.3% | +27.3% | $1.96 | +25.7% | 10.5M | 3.7M | 2.8x | 3.0M | Engineering & Construction |
| GANX | [TV](https://www.tradingview.com/chart/?symbol=GANX) | $1.98 | +13.1% | +18.2% | $2.34 | +33.7% | 9.5M | 1.6M | 6.1x | 41.4M | Biotechnology |
| JEM | [TV](https://www.tradingview.com/chart/?symbol=JEM) | $1.08 | -41.9% | +70.4% | $1.84 | -1.1% | 6.9M | 1.4M | 5.0x | 0 | Wholesale Distributors |
| LGCL | [TV](https://www.tradingview.com/chart/?symbol=LGCL) | $0.85 | +15.1% | +8.5% | $0.92 | +24.9% | 1.3M | 4.0M | 0.3x | 1.6M | Personnel Services |
| SLGB | [TV](https://www.tradingview.com/chart/?symbol=SLGB) | $0.55 | -1.1% | +14.7% | $0.63 | +13.5% | 177K | 1.5M | 0.1x | 3.0M | Air Freight/Couriers |
| ZJYL | [TV](https://www.tradingview.com/chart/?symbol=ZJYL) | $2.23 | -1.3% | +7.6% | $2.40 | +6.2% | 87K | 21K | 4.1x | 1.8M | Medical Specialties |
| TMCI | [TV](https://www.tradingview.com/chart/?symbol=TMCI) | $4.27 | -4.3% | +7.7% | $4.60 | +3.1% | 86K | 1.7M | 0.1x | 48.1M | Medical Specialties |
| EQ | [TV](https://www.tradingview.com/chart/?symbol=EQ) | $3.08 | +1.0% | +5.5% | $3.25 | +6.6% | 78K | 372K | 0.2x | 50.3M | Biotechnology |
| LFMD | [TV](https://www.tradingview.com/chart/?symbol=LFMD) | $4.20 | +1.7% | +5.5% | $4.43 | +7.3% | 71K | 1.1M | 0.1x | 39.6M | Medical/Nursing Services |

**Evaluation:**

- **GANX — already held** (entered 23:00 @ $2.39). AH +18.2%/$2.34, VRatio 6.1x, AH Vol 9.5M. Holding within ~6% of its AH high. Managed by premarket position-evaluation, not re-entered.
- **CTNT — already held** (entered 23:30 @ $2.05). AH +27.3%/$1.96, VRatio 2.8x, AH Vol up to 10.5M — still building volume. Managed by premarket position-evaluation, not re-entered.
- **JEM — Skip (dead-cat, fading).** Day -41.9% regular-session crash. AH Total% -1.1% → back below prior close. Genuine dead-cat, not a reclaim. No override flag.
- **LGCL — Skip.** NEW. AH +8.5% (<10% threshold), VRatio 0.3x (1.3M vs 4.0M avg — volume fading). Day +15.1% but AH move too weak. Fails AH-momentum gate.
- **SLGB — Skip (illiquid).** AH +14.7% but VRatio 0.1x (177K vs 1.5M avg — negligible AH volume across all scans: 131K→168K→177K). Stale/thin AH book pattern, no real liquidity. Total% +13.5%.
- **ZJYL — Skip.** NEW. AH +7.6% (<10% threshold), AH Vol 87K (negligible). Fails AH-momentum gate.
- **TMCI — Skip.** AH +7.7% (<10% threshold), VRatio 0.1x (86K, negligible AH volume).
- **EQ — Skip.** NEW. AH +5.5% (<10% threshold), VRatio 0.2x (78K, negligible AH volume).
- **LFMD — Skip.** NEW. AH +5.5% (<10% threshold), VRatio 0.1x (71K, negligible AH volume).

**Entries this scan: 0.** No new candidate clears the entry gates — all new tickers (LGCL, ZJYL, EQ, LFMD) fail the AH >10% momentum threshold; SLGB has negligible AH volume. GANX and CTNT remain held from earlier scans.

## Scan 00:30 CET (6:30 PM ET) — ENTRY WINDOW

Sixth AH scan. `scan.py --all` returned 11 hits. GANX (entered 23:00) and CTNT (entered 23:30) already held; positions managed separately by premarket position-evaluation.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| CTNT | [TV](https://www.tradingview.com/chart/?symbol=CTNT) | $1.54 | -1.3% | +27.3% | $1.96 | +25.6% | 11.2M | 3.8M | 2.9x | 3.0M | Engineering & Construction |
| GANX | [TV](https://www.tradingview.com/chart/?symbol=GANX) | $1.98 | +13.1% | +18.7% | $2.35 | +34.3% | 9.7M | 1.6M | 6.1x | 41.4M | Biotechnology |
| JEM | [TV](https://www.tradingview.com/chart/?symbol=JEM) | $1.08 | -41.9% | +59.3% | $1.72 | -7.5% | 7.2M | 1.4M | 5.1x | 0 | Wholesale Distributors |
| LGCL | [TV](https://www.tradingview.com/chart/?symbol=LGCL) | $0.85 | +15.1% | +63.2% | $1.39 | +87.8% | 3.3M | 4.2M | 0.8x | 1.6M | Personnel Services |
| MTEK | [TV](https://www.tradingview.com/chart/?symbol=MTEK) | $1.05 | -11.3% | +6.2% | $1.12 | -5.9% | 695K | 771K | 0.9x | 5.6M | Electronics/Appliances |
| SLGB | [TV](https://www.tradingview.com/chart/?symbol=SLGB) | $0.55 | -1.1% | +5.5% | $0.58 | +4.3% | 182K | 1.5M | 0.1x | 3.0M | Air Freight/Couriers |
| CELZ | [TV](https://www.tradingview.com/chart/?symbol=CELZ) | $0.81 | -32.5% | +6.1% | $0.86 | -28.3% | 88K | 281K | 0.3x | 3.7M | Medical Specialties |
| TMCI | [TV](https://www.tradingview.com/chart/?symbol=TMCI) | $4.27 | -4.3% | +7.7% | $4.60 | +3.1% | 86K | 1.7M | 0.1x | 48.1M | Medical Specialties |
| EQ | [TV](https://www.tradingview.com/chart/?symbol=EQ) | $3.08 | +1.0% | +5.5% | $3.25 | +6.6% | 79K | 372K | 0.2x | 50.3M | Biotechnology |
| LFMD | [TV](https://www.tradingview.com/chart/?symbol=LFMD) | $4.20 | +1.7% | +5.5% | $4.43 | +7.3% | 71K | 1.1M | 0.1x | 39.6M | Medical/Nursing Services |
| WHLR | [TV](https://www.tradingview.com/chart/?symbol=WHLR) | $1.29 | -15.1% | +5.4% | $1.36 | -10.5% | 50K | 644K | 0.1x | 549K | Real Estate Investment Trusts |

**Evaluation:**

- **GANX — already held** (entered 23:00 @ $2.39). AH +18.7%/$2.35, VRatio 6.1x. Now $2.36, P&L -1.2%. Holding within ~6% of AH high. Managed by premarket position-evaluation.
- **CTNT — already held** (entered 23:30 @ $2.05). AH +27.3%/$1.96, VRatio 2.9x, AH Vol up to 11.2M (still building volume). Now $1.90, P&L -7.3%. Managed by premarket position-evaluation.
- **LGCL — Skip.** NEW qualifier on paper (AH +63.2%, Total +87.8%, float 1.6M ideal) but fails on three counts: (1) **Fails 2-AH-scan requirement** — at 00:00 it was only +8.5% (<10%); this is its first AH scan >10%. (2) **SPIKE→FADE** — Yahoo 5m: spiked to AH high $1.42 (+91.9%) at 18:15 ET then collapsed to $0.99 (+34%) by 18:30. Current price is ~30% off the AH high → fade, not hold. The scan's $1.39/+63.2% snapshot is stale vs the live collapse. (3) **Illiquid/stale volume** — Yahoo shows 0 AH volume across all bars; the scan's 3.3M AH Vol / 0.8x VRatio (below average) is a stale regular-session artifact, not real AH liquidity. Skip on all three.
- **JEM — Skip (dead-cat, fading).** Day -41.9% regular-session crash. AH Total% -7.5% → back below prior close. Genuine dead-cat, not a reclaim. No override flag.
- **MTEK — Skip.** NEW. AH +6.2% (<10% threshold), VRatio 0.9x, Total% -5.9% (below close). Fails AH-momentum gate.
- **CELZ — Skip.** NEW. Day -32.5% (regular-session crash), AH +6.1% (<10% threshold), VRatio 0.3x (88K, negligible), Total% -28.3%. Dead-cat + fails AH gate.
- **WHLR — Skip.** NEW. Day -15.1%, AH +5.4% (<10% threshold), VRatio 0.1x (50K, negligible AH volume). Fails AH gate.
- **SLGB — Skip (illiquid).** AH +5.5%, VRatio 0.1x (182K vs 1.5M avg — negligible AH volume across all scans). Stale/thin book.
- **TMCI / EQ / LFMD — Skip.** All AH <10% (+7.7% / +5.5% / +5.5%) with negligible AH volume (VRatio 0.1-0.2x). Fail AH-momentum gate.

**Entries this scan: 0.** No new candidate clears the gates. LGCL was the only new ticker with a >10% AH move but it fails the 2-AH-scan requirement, is in SPIKE→FADE off its 18:15 peak, and has zero real AH volume. GANX and CTNT remain held from earlier scans.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
| GANX | $2.39 | 23:00 CET | 41 | ea649b1f | Grade B: positive Phase 1b data (GT-02287, Parkinson's GBA1); BUILD/hold, VRatio 5.5x, Total +42% |
| CTNT | $2.05 | 23:30 CET | 48 | 4f35924a | Grade None: low-float (3.0M) squeeze, no catalyst; BUILD +16.9%→+39.6%, Total +38%, concern: reverse-split overhang |

## Morning Evaluation — 10:20 CET

### Today's Winner

**BTCT** — BTC Digital Ltd. (crypto / Data Processing Services)
- Catalyst: unverified. Stock had been bleeding for days ($1.28 → $0.74 close); the AH pop is a low-float bounce, likely crypto-sympathy / squeeze. No confirmed same-day PR. **Grade None (unverified).**
- Previous Close: $0.74 (Mon close; down from $1.28 three sessions earlier)
- AH last night: $1.77 (+139.2%) at 18:50 ET (00:50 CET) — surge fired 18:20→18:50 ET
- Premarket now: $1.22 (+64.9%); PM high $1.39 (+88.0%) at the 04:00 ET open, faded immediately
- Hypothetical P&L: AH-tail entry ~$1.20 → **AH peak $1.77 = +47%** (best exit was in AH); AH entry → PM high $1.39 = +16%
- Float: 9.5M | Market Cap: $6.5M

**Scanner Diagnostic:**
- Detectable at screening time (~22:15 CET)? **NO** — flat/down in AH (~$0.68, -8%) through every scheduled scan. The move had not started.
- Why missed: the defining surge began at **18:20 ET (00:20 CET)** — was +54% by 18:20, +67.6% at 18:30 ET (the 00:30 CET last scan), and peaked +139% at **18:50 ET (00:50 CET), 20 min after the last scheduled scan**. Classified as a **late-AH-tail surge** (decisive move + peak in the unscanned 18:30–20:00 ET tail). The 00:30 scan's TradingView postmarket feed did not surface the +67% print that was already live (known feed lag).
- Scanner gap: a late scan at ~01:00/01:30 CET (covering 19:00–19:30 ET) would have caught BTCT mid-surge. This is the 2nd late-AH-tail case (ORIS Jun 22 was the founding case). Not counted against the detection baseline.

### Baseline Tracking

- Days tracked: **39** (was 38 + 1)
- Winners detected by scanner: **33/38 (86.8%)** — unchanged. Day 39 winner (BTCT) is a **late-AH-tail surge** (decisive move + peak after the 00:30 last scan) and is **excluded** from the detection baseline per the late-AH-tail rule (neither detection nor miss).
- Winner selected for paper trade: **22/38 (57.9%)** — unchanged; BTCT was not tradeable in the scanned window. We entered GANX and CTNT (both detected, both qualified).
- Target: >80% detection
- Status: **BASELINE MET** (86.8%)

### Retrospective Scan Results

Live premarket scan (04:20 ET) — 5 hits: JEM +133%, BTCT +103%, INTZ +50.6%, CAST +40.5%, CTNT +23.4%.

AH reconstruction (`check-prices.py --ah-history`):
- **BTCT** — flat ~$0.68 until 18:20 ET, then surge to $1.77 (+139%) at 18:50 ET. Late-AH-tail.
- **JEM** — AH peak only +11.8% ($2.08) at 16:30 ET, faded to ~-5% by 19:55 ET. PM-only gapper (dead-cat reclaim).
- **INTZ** — no AH footprint (~$0.68). PM-only.
- **CAST** — AH down -26% (regular crash continuation). Not a setup.
- **CTNT** — AH +27% build (we held it). PM +20%.

### Open Position P&L (Alpaca)

Positions are managed by `position-evaluation.md` (10:30 / 14:30 CET), not closed here. Read-only context:

| Ticker | Entry | Entry Total% | Catalyst | Entry Time | PM High | PM Now | P&L | P&L % | Status |
|--------|-------|--------------|----------|------------|---------|--------|-----|-------|--------|
| GANX | $2.39 | +42.3% | B — Phase 1b GT-02287 Parkinson's data | 23:00 CET | $2.19 (+25%) | $2.14 | -$10.66 | -10.9% | 🔴 Open, underwater |
| CTNT | $2.05 | +37.8% | None — low-float squeeze / reverse-split overhang | 23:30 CET | $1.88 (+21%) | $1.75 | -$14.40 | -14.6% | 🔴 Open, underwater |

Both faded from AH highs into PM. Exit decision deferred to position-evaluation.

### Scanner Effectiveness

- Evening scans ran: **7 of 7** (21:30, 22:00, 22:30, 23:00, 23:30, 00:00, 00:30 CET). Full coverage, no coverage failure.
- Candidates found: 18 unique tickers across the night.
- Entries: 2 (GANX 23:00, CTNT 23:30).
- Retrospective match on winner: BTCT not catchable in window (late-AH-tail).

### Missed Opportunities

| Ticker | AH Change | Why Missed | Would Be Profitable? |
|--------|-----------|------------|---------------------|
| BTCT | +139% (peak 18:50 ET) | Late-AH-tail surge — peaked 20 min after last scan; AH feed lagged the +67% print at 18:30 | AH-tail entry → AH peak +47%; → PM +16%. Not a baseline miss. |
| JEM | AH faded (peak +11.8%) | PM-only gapper / dead-cat — correctly skipped in AH (Total% went negative) | PM-only; no AH entry possible |

No clean AH→PM opportunity inside the scanned window was failed.

### AH Mover Follow-Through

Stocks in 2+ evening scans with AH change >10%:

| Ticker | AH Peak | Peak Time | AH Trajectory | Current PM | From Peak | From Close | Verdict |
|--------|---------|-----------|---------------|------------|-----------|-----------|---------|
| GANX | $2.50 | 16:40 ET | Spike→hold | $2.14 | -14.4% | +22.3% | Faded into PM; AH peak was better exit |
| CTNT | $2.15 | 17:10 ET | Build | $1.75 | -18.6% | +12.3% | Faded into PM; AH peak was better exit |

**AH-peak-vs-PM-peak check:** Both GANX ($2.50 AH > $2.19 PM) and CTNT ($2.15 AH > $1.88 PM) peaked in after-hours and faded into PM. BTCT same ($1.77 AH > $1.39 PM). Three more data points for the "AH peak beats PM peak" fade pattern — none were extreme runners (>250%), so they don't bear on the MSW extreme-runner hypothesis, but they reinforce that AH highs are frequently the better exit.

### Price Charts

```
BTCT — Prev Close $0.74 | 2-Day Range $0.66–$1.82 | Peak $1.77 (+139%) @ 18:50 ET
  Flat ~$0.68 all evening → surge 18:20→18:50 ET to $1.77 → faded to ~$1.40 overnight
  → PM open $1.39 (+88%) → faded to $1.22 (+65%) by 04:21 ET

JEM — Prev Close $1.86 | 2-Day Range $1.06–$3.57 | Peak $3.57 (+92%) PM
  Regular crash to $1.08 → AH bounce to $2.08 then faded to ~$1.70 → PM gap to $3.36 (04:15 ET)
```

### Notes

**Late-AH-tail surge tally** (decisive surge after 00:30 CET / 18:30 ET last scan; not a detection miss):
- ORIS — Jun 22: $2.49→$3.28 +32% at 19:25 ET, PM peak $3.93; hypo AH-tail entry ~$2.55 → +54%
- **BTCT — Jun 29→30: $0.70→$1.77 +139% peaking 18:50 ET; hypo AH-tail entry ~$1.20 → AH peak +47% / PM high +16%**
- 2 cases now. Threshold for action is ≥3–4 winners surging in this tail → would argue for adding a ~01:00/01:30 CET scan. Watch.

**PM-only gapper tally** (flat/down in AH, move began after 04:00 ET — undetectable by AH scanner):
- Known: CIIT (Jun 10 +140%), GLXG (Jun 11 +343%), TDIC (Jun 16 +140%), MBRX (Jun 23 +131%, uninvestable), CUPR (Jun 24 +81%, thin tick)
- **JEM — Jun 30: dead-cat reclaim. Crashed -41.9% regular to $1.08, AH faded, PM gapped to $3.36 (04:15 ET). Investability: borderline-holdable so far (held $3.27–3.36 for ~2 bars), but only 20 min of PM data — tentative.** Not a scanner failure.
- Pattern holds: PM-only gappers remain mostly low-conviction/uninvestable spikes → AH-scanner blind spot still low real cost.

**Fade-rule false-negative tracking:** LGCL was skipped last night on SPIKE→FADE (AH high $1.42 +92% at 18:15 ET → collapsed to $0.99 by 18:30) plus failed 2-AH-scan + zero real AH vol. No PM re-explosion observed (not in PM top movers) → fade rule was correct here. Tally unchanged (CRE Jun 17, LNKS Jun 18 remain the only re-explosion false negatives).

**Coverage:** 7/7 scans ran. No new coverage failure.

**Open positions:** GANX and CTNT both entered last night, both underwater in PM (-10.9% / -14.6%), both faded from AH highs. Reinforces that AH-peak exits beat PM holds when the catalyst is weak (CTNT Grade None) or the AH move was already extended.
