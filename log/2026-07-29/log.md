# 2026-07-29

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| AMIX | $4.02 | $4.68 | +16.4% | $5.29 (PM open) | 1 | None | SELL | Grade None → exit at any profit; PM spike-and-fade off $5.29 open |
| ONMD | $0.94 | $0.86 | -8.5% | $1.10 (OVN, +17%) | 1 | B | HOLD | Above -15% stop ($0.80), catalyst intact, day 1 of 2, peak below +30% trail |

**Actions taken:**
- SELL 21 AMIX @ limit $4.38 ext (id f91526f6) → filled @ **$4.68** (price improvement in liquid book). Final P&L +$13.86 (+16.4%). Moved to Closed Positions.
- ONMD held. No trail (peak +17% < +30% threshold).

**Data notes:**
- Alpaca quote feed stale (20:00-20:14Z yesterday); used SIP 5Min bars for live PM prices.
- AMIX SIP PM: $5.29 H at 08:00Z open (14.2K trades), faded to $4.44 by 08:15Z. Liquid.
- ONMD SIP PM: $0.85-0.86, vwap $0.85, liquid (5.7K trades/bar).

## Position Evaluation — 14:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| ONMD | $0.94 | $0.79 | -16.0% | $1.10 (OVN, +17%) | 1 | B | SELL | Below -15% hard stop ($0.799); PM faded $0.97→$0.79 |

**Actions taken:**
- SELL 108 ONMD @ limit $0.77 ext (id 9f018805) → filled @ **$0.79**. Final P&L -$16.20 (-16.0%). Moved to Closed Positions.
- No open positions remaining.

**Data notes:**
- Alpaca quote feed stale (bid $0.59 x100 @ 07-28 20:00Z prior close); used SIP 5Min bars for live PM.
- ONMD SIP PM: opened $0.97 H (08:00Z), faded to $0.79-0.85 band, vwap $0.81-0.88, liquid (1.1M-1.26M sh first bars). Never re-rated above entry. Grade B magnitude (4x FY2025 bookings) did not produce AH→PM follow-through.

## Scan 21:30 CET (3:30 PM ET)

**Session: REGULAR.** The market has not closed, so no AH data exists yet. The scanner returned 22 volume movers; the 11 names up at least 15% are recorded below as **Watch - pending AH confirmation**. No entries are allowed before AH confirmation or before the 23:00 CET scan.

| Ticker | Chart | Prev Close | Price | Day% | 5m Vol | IRVol | VChg | Float | Industry |
|--------|-------|------------|-------|------|--------|-------|------|-------|----------|
| NCRA | [TV](https://www.tradingview.com/chart/?symbol=NCRA) | $1.43 | $3.09 | +116.1% | 137K | 994.3x | -58.3% | 535K | Engineering & Construction |
| SPRC | [TV](https://www.tradingview.com/chart/?symbol=SPRC) | $5.33 | $8.81 | +65.2% | 98K | 245.6x | +73.9% | 563K | Pharmaceuticals: Major |
| SYBX | [TV](https://www.tradingview.com/chart/?symbol=SYBX) | $0.72 | $1.15 | +59.7% | 13K | 84.7x | +5.9% | 9.6M | Financial Conglomerates |
| AMIX | [TV](https://www.tradingview.com/chart/?symbol=AMIX) | $2.75 | $4.35 | +58.2% | 91K | 230.2x | -36.3% | 502K | Medical Specialties |
| STFS | [TV](https://www.tradingview.com/chart/?symbol=STFS) | $3.63 | $5.11 | +40.6% | 87K | 25.9x | -30.6% | 1.1M | Advertising/Marketing Services |
| GMM | [TV](https://www.tradingview.com/chart/?symbol=GMM) | $2.47 | $3.02 | +22.2% | 9K | 6.2x | +63.7% | 1.7M | Packaged Software |
| MWYN | [TV](https://www.tradingview.com/chart/?symbol=MWYN) | $0.49 | $0.60 | +21.7% | 118 | 30.4x | -93.9% | 14.2M | Home Improvement Chains |
| BXBL | [TV](https://www.tradingview.com/chart/?symbol=BXBL) | $4.20 | $5.09 | +21.2% | 1K | 0.7x | +29.0% | 961K | Homebuilding |
| VIVK | [TV](https://www.tradingview.com/chart/?symbol=VIVK) | $1.94 | $2.35 | +21.1% | 36K | 1.0x | -63.2% | 590K | Chemicals: Specialty |
| CTXR | [TV](https://www.tradingview.com/chart/?symbol=CTXR) | $0.49 | $0.57 | +15.5% | 1K | 2.7x | +364.7% | 27.0M | Medical Specialties |
| ROC | [TV](https://www.tradingview.com/chart/?symbol=ROC) | $4.27 | $4.92 | +15.2% | 100 | 1.2x | +0.0% | 5.4M | Packaged Software |

**Decision notes:**
- Watch all listed names pending a 22:00+ CET AH reappearance. Regular-session appearances do not count toward the two-scan AH gate.
- SYBX is untradable on Alpaca. Carry it forward as `untradable (carried)` if it appears again.
- NCRA, SPRC, AMIX, STFS, GMM, MWYN, BXBL, VIVK, CTXR, and ROC are Alpaca-tradable.
- No catalyst searches, spike-bar checks, SIP verification, quotes, or orders at this pre-AH scan. No paper trades entered.

## Scan 22:00 CET (4:00 PM ET)

No candidates found.

- **Day-movers pre-seed (log-only):** NCRA +93.7%: `NO-SPIKE no AH bars yet (as-of 16:00ET)`; SPRC +84.2%: `NO-SPIKE no AH bars yet (as-of 16:00ET)`; AMIX +54.2%: `NO-SPIKE no AH bars yet (as-of 16:00ET)`; STFS +34.4%: `NO-SPIKE no AH bars yet (as-of 16:00ET)`; MWYN +29.4%: `NO-SPIKE no AH bars yet (as-of 16:00ET)`; VIVK +25.8%: `NO-SPIKE no AH bars yet (as-of 16:00ET)`; SKYQ +21.9%: `NO-SPIKE no AH bars yet (as-of 16:00ET)`; BXBL +21.4%: `NO-SPIKE no AH bars yet (as-of 16:00ET)`; GMM +21.1%: `NO-SPIKE no AH bars yet (as-of 16:00ET)`; BATL +18.4%: `NO-SPIKE no AH bars yet (as-of 16:00ET)`; YIBO +18.3%: `NO-SPIKE no AH bars yet (as-of 16:00ET)`.
- Observation only. TradingView had no post-market hits at the AH open. No candidates, evaluations, or paper entries.

## Scan 22:15 CET (4:15 PM ET)

No candidates found.

- **Day-movers pre-seed (log-only):** NCRA +120.3%: `NO-SPIKE flat/faded (peak <= base) (no bar cleared +15% on a volume co-spike) (as-of 16:15ET)`; AMIX +66.2%: `NO-SPIKE flat/faded (peak <= base) (no bar cleared +15% on a volume co-spike) (as-of 16:15ET)`; SPRC +60.2%: `NO-SPIKE flat/faded (peak <= base) (no bar cleared +15% on a volume co-spike) (as-of 16:15ET)`; STFS +33.5%: `NO-SPIKE peak +2% @16:00ET (no bar cleared +15% on a volume co-spike) (as-of 16:15ET)`; MWYN +31.8%: `NO-SPIKE flat/faded (peak <= base) (no bar cleared +15% on a volume co-spike) (as-of 16:15ET)`; DCX +26.4%: `NO-SPIKE peak +5% @16:00ET (no bar cleared +15% on a volume co-spike) (as-of 16:15ET)`; SKYQ +23.2%: `NO-SPIKE flat/faded (peak <= base) (no bar cleared +15% on a volume co-spike) (as-of 16:15ET)`; VIVK +22.7%: `NO-SPIKE flat/faded (peak <= base) (no bar cleared +15% on a volume co-spike) (as-of 16:15ET)`; GWAV +21.1%: `NO-SPIKE flat/faded (peak <= base) (no bar cleared +15% on a volume co-spike) (as-of 16:15ET)`; BXBL +19.0%: `NO-SPIKE flat/faded (peak <= base) (no bar cleared +15% on a volume co-spike) (as-of 16:15ET)`; GMM +18.2%: `NO-SPIKE flat/faded (peak <= base) (no bar cleared +15% on a volume co-spike) (as-of 16:15ET)`; BATL +17.2%: `NO-SPIKE flat/faded (peak <= base) (no bar cleared +15% on a volume co-spike) (as-of 16:15ET)`; YHC +15.8%: `NO-SPIKE peak +1% @16:00ET (no bar cleared +15% on a volume co-spike) (as-of 16:15ET)`.
- Observation only. TradingView post-market fields still returned no main-screener hits. The pre-seed is instrumentation only and produced no candidates or entry decisions. No paper trades entered.

## Scan 22:30 CET (4:30 PM ET)

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| DCX | [TV](https://www.tradingview.com/chart/?symbol=DCX) | $1.08 | +19.7% | +31.5% | $1.42 | +57.4% | 1.8M | 285K | 6.3x | 2.1M | Motor Vehicles |
| CRE | [TV](https://www.tradingview.com/chart/?symbol=CRE) | $2.42 | -1.4% | +20.9% | $2.92 | +19.2% | 277K | 60K | 4.7x | 1.1M | Commercial Printing/Forms |
| SXTP | [TV](https://www.tradingview.com/chart/?symbol=SXTP) | $1.49 | -0.7% | +8.7% | $1.62 | +8.0% | 61K | 42K | 1.5x | 2.6M | Biotechnology |

**Instrumentation and verification:**
- DCX: `SPIKE  16:03ET  +22%  $1.32  712 trades / 104k sh  (first co-spike bar) (as-of 16:30ET)`. SIP confirms a real BUILD from $1.20 to $1.42 through 16:10 ET, with 425K-1.03M shares and 2.7K-5.8K trades per bar. The 16:30 ET book was fresh and two-sided at $1.50 x100 / $1.52 x100. Yahoo showed a $1.52 AH high at 16:25 ET, consistent with continued building.
- CRE: `SPIKE  16:06ET  +16%  $2.80  26 trades / 4k sh  (first co-spike bar) (as-of 16:30ET)`. SIP confirms a real spike, including 117K-264K shares and 1.6K-4.0K trades per bar, but the move peaked early at $3.50 and faded to $2.84 by 16:15 ET. Yahoo likewise faded from $3.00 at 16:05 to $2.80 at 16:30. The broker quote was stale at 16:00 ET, so the scanner's current $2.92 reading is unconfirmed rather than rejected.
- SXTP: below the +10% workup threshold. SIP confirms choppy, thinner trading and a fade to $1.49 by 16:15 ET; the broker quote was stale at 16:00 ET.

**Catalysts and decisions:**
- DCX: same-day PR announces a non-binding MOU with Whales AI for an AI/STEM robotics education platform and a potential $20M investment. Weak/non-binding catalyst, provisionally Grade C. Alpaca tradable. **Watch only:** first qualifying AH scan and entries are prohibited before 23:00 CET.
- CRE: no same-day earnings or company catalyst found within the four-call search budget; search results only surfaced older company releases and an unrelated LSE ticker's earnings. Alpaca tradable. **Watch only:** first qualifying AH scan, current trajectory is SPIKE→FADE, and entries are prohibited before 23:00 CET.
- SXTP: Alpaca tradable. **Watch only:** AH change is below +10%, with no sustained momentum gate yet.
- No paper orders submitted. DCX and CRE need to sustain above +10% in another AH scan before they can qualify for entry.

## Scan 22:45 CET (4:45 PM ET)

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| DCX | [TV](https://www.tradingview.com/chart/?symbol=DCX) | $1.08 | +19.7% | +40.7% | $1.52 | +68.5% | 4.7M | 614K | 7.6x | 2.1M | Motor Vehicles |
| CRE | [TV](https://www.tradingview.com/chart/?symbol=CRE) | $2.42 | -1.4% | +15.9% | $2.80 | +14.3% | 394K | 76K | 5.2x | 1.1M | Commercial Printing/Forms |
| AMIX | [TV](https://www.tradingview.com/chart/?symbol=AMIX) | $4.57 | +66.2% | +5.7% | $4.83 | +75.6% | 166K | 8.9M | 0.0x | 502K | Medical Specialties |
| BOOM | [TV](https://www.tradingview.com/chart/?symbol=BOOM) | $5.42 | -0.7% | +19.0% | $6.45 | +18.1% | 72K | 177K | 0.4x | 18.0M | Oilfield Services/Equipment |
| NUWE | [TV](https://www.tradingview.com/chart/?symbol=NUWE) | $1.89 | -2.1% | +10.6% | $2.09 | +8.3% | 52K | 115K | 0.5x | 363K | Medical Specialties |

**Instrumentation and verification:**
- DCX: `SPIKE  16:03ET  +22%  $1.32  712 trades / 104k sh  (first co-spike bar) (as-of 16:45ET)`. SIP remains highly liquid through 16:30 ET, but the live 16:45 ET book was $1.25 x100 / $1.27 x100 and Yahoo was $1.26, well below the scanner's stale $1.52. It peaked at $1.59 and has now faded about 21% from that high. AH volume rose from 1.8M to 4.7M, but trajectory changed from BUILD to SPIKE→FADE.
- CRE: `SPIKE  16:06ET  +16%  $2.80  26 trades / 4k sh  (first co-spike bar) (as-of 16:45ET)`. SIP confirms the early $3.50 high followed by lower closes to $2.71 and volume collapse from 264K to 12K shares per bar. Yahoo was $2.73 at 16:45 ET. The quote remained stale at 16:00 ET. Clear SPIKE→FADE.
- BOOM: `SPIKE  16:09ET  +26%  $6.82  180 trades / 6k sh  (first co-spike bar) (as-of 16:45ET)`. SIP confirms real but modest trading, mostly 8K-28K shares and 42-378 trades per bar. It peaked at $6.82 near 16:09 ET and drifted to about $6.25-$6.30 by 16:45 ET. The quote was stale at 16:14 ET, so current fillability is not confirmed.
- NUWE: `SPIKE  16:28ET  +16%  $2.20  190 trades / 16k sh  (first co-spike bar) (as-of 16:45ET)`. TradingView under-reported the move: Yahoo showed a steady build to $2.63 at 16:45 ET (+36% from its $1.93 prior close), while lagged SIP reached $2.19 with volume and trades increasing into 16:30 ET. The quote was stale at 16:00 ET with no ask, so this is unconfirmed-but-live rather than an illiquidity rejection.
- AMIX: SIP and Yahoo show a late build from $4.48 to $5.25, but the scanner AH change remained below +10%. Its 0.0x VRatio reflects the very high regular-session average volume, not absence of AH trades.

**Catalysts and decisions:**
- DCX: same non-binding Whales AI MOU and potential $20M investment, provisional Grade C. Alpaca tradable. **Watch only:** it has two scanner appearances above +10%, but entries are prohibited before 23:00 CET and fresh price data now shows a deep fade.
- CRE: repeated four-call structured search found no same-day earnings, PR, or material filing. Alpaca tradable. **Skip for now:** two AH scans above +10%, but it peaked early and is fading on collapsing volume. No order before 23:00 CET in any case.
- AMIX: Alpaca tradable. **Watch only:** first main AH scan and scanner AH change below +10%, so it does not clear the sustained-momentum gate.
- BOOM: DMC Global scheduled Q2 results after today's close, with the call at 17:00 ET; the move coincided with the scheduled release, but the exact results were not yet indexed. Provisional Grade B earnings catalyst. Alpaca tradable. **Watch only:** first qualifying AH scan, modest VRatio, early peak, and entries are prohibited before 23:00 CET.
- NUWE: no same-day catalyst found within the four-call budget; the latest identified company news was July 27 preliminary Q2 revenue growth of 14%. Grade None. Alpaca tradable. **Watch only:** first qualifying AH scan, scanner/SIP feed lag, and no fresh two-sided broker book yet. No-catalyst status is a concern, not a gate.
- No paper orders submitted. At 23:00 CET, recheck whether DCX and CRE are holding within 20% of their highs, and whether BOOM or NUWE sustain above +10% in a second AH scan.

## Scan 23:00 CET (5:00 PM ET)

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| DCX | [TV](https://www.tradingview.com/chart/?symbol=DCX) | $1.08 | +19.7% | +23.1% | $1.33 | +47.5% | 6.2M | 785K | 7.9x | 2.1M | Motor Vehicles |
| NUWE | [TV](https://www.tradingview.com/chart/?symbol=NUWE) | $1.89 | -2.1% | +35.4% | $2.56 | +32.6% | 594K | 185K | 3.2x | 363K | Medical Specialties |
| AMIX | [TV](https://www.tradingview.com/chart/?symbol=AMIX) | $4.57 | +66.2% | +14.1% | $5.21 | +89.6% | 486K | 8.9M | 0.1x | 502K | Medical Specialties |
| CRE | [TV](https://www.tradingview.com/chart/?symbol=CRE) | $2.42 | -1.4% | +13.9% | $2.75 | +12.2% | 429K | 81K | 5.3x | 1.1M | Commercial Printing/Forms |
| ONMD | [TV](https://www.tradingview.com/chart/?symbol=ONMD) | $0.64 | -9.4% | +7.3% | $0.69 | -2.7% | 164K | 4.4M | 0.0x | 16.4M | Packaged Software |
| SXTP | [TV](https://www.tradingview.com/chart/?symbol=SXTP) | $1.49 | -0.7% | +8.7% | $1.62 | +8.0% | 113K | 49K | 2.3x | 2.6M | Biotechnology |
| BOOM | [TV](https://www.tradingview.com/chart/?symbol=BOOM) | $5.42 | -0.7% | +13.5% | $6.15 | +12.6% | 99K | 179K | 0.6x | 18.0M | Oilfield Services/Equipment |
| ASBP | [TV](https://www.tradingview.com/chart/?symbol=ASBP) | $5.61 | -22.6% | +20.3% | $6.75 | -6.8% | 3K | 64K | 0.0x | 1.2M | Pharmaceuticals: Other |

**Instrumentation and verification:**
- DCX: `DCX 2026-07-29  SPIKE  16:03ET  +22%  $1.32  712 trades / 104k sh  (first co-spike bar) (as-of 17:00ET)`. Scanner AH volume rose from 4.7M to 6.2M, but fresh price history shows the stock peaked at $1.59 at 16:25 ET, dropped to $1.28, and was only $1.35 at 17:00 ET. The fresh book was $0.05 x100 / $1.40 x2500, which is not a usable two-sided market.
- NUWE: `NUWE 2026-07-29  SPIKE  16:28ET  +16%  $2.20  190 trades / 16k sh  (first co-spike bar) (as-of 17:00ET)`. SIP confirms a real BUILD, accelerating from 34K shares and 391 trades at 16:25 ET to 553K shares and 6,747 trades at 16:40 ET, then 411K shares and 4,576 trades at 16:45 ET. Yahoo reached $2.75 at 16:45 and held $2.56 at 17:00. The broker quote remained stale at 16:00 ET with `ask $0.00 x0` after a re-pull, so the move is unconfirmed-but-live rather than rejected as a bad print.
- AMIX: `AMIX 2026-07-29  SPIKE  16:41ET  +17%  $5.36  714 trades / 65k sh  (first co-spike bar) (as-of 17:00ET)`. SIP shows a real late BUILD to $5.50, with volume increasing to 270K shares and 2,686 trades in the 16:45 ET bar. Yahoo held $5.25 at 17:00 ET. The quote remained stale at 16:00 ET.
- CRE: `CRE 2026-07-29  SPIKE  16:06ET  +16%  $2.80  26 trades / 4k sh  (first co-spike bar) (as-of 17:00ET)`. Fresh price history contradicts the stale scanner level: CRE faded from its early $3.50 SIP high to $2.59 at 17:00 ET, with volume collapsing to 7K shares and 69 trades in the latest SIP bar. Clear SPIKE→FADE.
- BOOM: `BOOM 2026-07-29  SPIKE  16:09ET  +26%  $6.82  180 trades / 6k sh  (first co-spike bar) (as-of 17:00ET)`. SIP shows modest but real volume and an early $6.82 high. Yahoo shows the stock recovered from $6.23 at 16:40 to $6.61 at 16:50-17:00, within 3% of the high. The book remained stale at 16:14 ET after a re-pull, so current fillability could not be confirmed.
- ASBP: `ASBP 2026-07-29  NO-SPIKE  peak +20% @16:44ET  (no bar cleared +15% on a volume co-spike) (as-of 17:00ET)`. SIP contains only 3K AH shares and 16 trades across four isolated bars. Yahoo's $6.40 high remained below the $7.25 previous close. The quote was stale with no ask. This is a thin dead-cat bounce, not a volume-backed reclaim.

**Catalysts and decisions:**
- DCX: same-day non-binding Whales AI MOU and possible $20M investment, Grade C. **Skip:** two scans above +10%, but it peaked early, is fading, and the fresh book has a non-viable $0.05 bid.
- NUWE: repeat structured search found no July 29 earnings, PR, or 8-K. The newest releases were July 28 Wisconsin Aquadex installations and July 27 preliminary Q2 revenue growth. Grade None. **Wait:** two scans above +10% and a genuine BUILD, but the stale zero-ask quote fails the required real-time fillability check. Recheck at the next scan.
- AMIX: no same-day earnings, PR, or 8-K found; July 23-24 patent and preclinical-study releases are the newest company news. Grade None. **Watch:** strong late BUILD, but this is its first scan above +10%, so it does not yet meet the two-scan gate. Scanner VRatio is low because regular-session volume was 68M shares; SIP confirms real AH trading.
- CRE: repeat structured search again found no same-day catalyst. Grade None. **Skip:** although it has three scans above +10%, fresh data shows an early SPIKE→FADE on collapsing volume.
- BOOM: DMC Global reported Q2 sales of $157.0M, net income attributable to DMC of $0.5M or $0.10 per diluted share, and adjusted EBITDA attributable to DMC of $10.7M at 16:05 ET. Grade B earnings catalyst. **Wait:** two scans above +10% and holding near its AH high after a late recovery, but the quote is 45 minutes stale and current fillability is not confirmed. Recheck at the next scan.
- ASBP: no same-day earnings, PR, or 8-K found within the search budget; the latest 8-K was July 20. **Skip:** Day -22.6%, still below the previous close, only about 3K AH shares, and no fillable ask. It does not qualify for DEAD-CAT-OVERRIDE WATCH because it has not reclaimed the previous close.
- ONMD and SXTP remain below +10% AH. No workup or entry.
- No paper orders submitted. No positions were added to `OPEN_POSITIONS.md`.

## Scan 23:30 CET (5:30 PM ET)

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| DCX | [TV](https://www.tradingview.com/chart/?symbol=DCX) | $1.08 | +19.7% | +19.4% | $1.29 | +43.0% | 7.1M | 884K | 8.0x | 2.1M | Motor Vehicles |
| NUWE | [TV](https://www.tradingview.com/chart/?symbol=NUWE) | $1.89 | -2.1% | +110.1% | $3.97 | +105.7% | 3.6M | 569K | 6.3x | 363K | Medical Specialties |
| AMIX | [TV](https://www.tradingview.com/chart/?symbol=AMIX) | $4.57 | +66.2% | +5.7% | $4.83 | +75.6% | 1.2M | 9.0M | 0.1x | 502K | Medical Specialties |
| ONCO | [TV](https://www.tradingview.com/chart/?symbol=ONCO) | $0.75 | -9.7% | +14.3% | $0.86 | +3.2% | 665K | 339K | 2.0x | 3.7M | Pharmaceuticals: Major |
| ONMD | [TV](https://www.tradingview.com/chart/?symbol=ONMD) | $0.64 | -9.4% | +7.4% | $0.69 | -2.7% | 348K | 4.4M | 0.1x | 16.4M | Packaged Software |
| BOOM | [TV](https://www.tradingview.com/chart/?symbol=BOOM) | $5.42 | -0.7% | +20.7% | $6.54 | +19.8% | 146K | 185K | 0.8x | 18.0M | Oilfield Services/Equipment |
| SXTP | [TV](https://www.tradingview.com/chart/?symbol=SXTP) | $1.49 | -0.7% | +12.8% | $1.68 | +12.0% | 140K | 52K | 2.7x | 2.6M | Biotechnology |

**Instrumentation and verification:**
- DCX: `DCX 2026-07-29  SPIKE  16:03ET  +22%  $1.32  712 trades / 104k sh  (first co-spike bar) (as-of 17:30ET)`. Scanner AH volume increased to 7.1M. Fresh SIP/Yahoo show a rebound from $1.27 to $1.38-$1.43 at 17:15-17:30 ET, within 13% of the $1.59 high, but two quote pulls remained stuck at 17:00 ET with a non-viable $0.05 x100 / $1.40 x2500 book.
- NUWE: `NUWE 2026-07-29  SPIKE  16:28ET  +16%  $2.20  190 trades / 16k sh  (first co-spike bar) (as-of 17:30ET)`. SIP confirms the surge is real: the 17:05 and 17:10 ET bars traded 1.12M and 1.35M shares on 10.6K and 15.0K trades. Yahoo held $3.46 at 17:30 after a $3.97 high, within 13% of the high. Two quote pulls remained stale at 16:00 ET with `ask $0.00 x0`.
- ONCO: `ONCO 2026-07-29  SPIKE  17:03ET  +40%  $1.05  311 trades / 98k sh  (first co-spike bar) (as-of 17:30ET)`. SIP confirms a real 293K-share ignition bar, but volume fell to 50K shares by 17:15 ET and Yahoo shows a fade from $0.98 at 17:00 to $0.83 at 17:30. The quote was stale at 16:00 ET with no ask.
- BOOM: `BOOM 2026-07-29  SPIKE  16:09ET  +26%  $6.82  180 trades / 6k sh  (first co-spike bar) (as-of 17:30ET)`. SIP and Yahoo show a recovery and hold at $6.54-$6.60 through 17:30 ET, within 4% of the $6.82 high. Real AH volume continues across bars, though it remains modest. Two quote pulls stayed stale at 16:14 ET, so current fillability is unconfirmed.
- SXTP: `SXTP 2026-07-29  SPIKE  16:13ET  +16%  $1.73  99 trades / 38k sh  (first co-spike bar) (as-of 17:30ET)`. SIP shows thin but continuous trading and Yahoo shows a gradual build to $1.72 at 17:30 ET, near its $1.73 high. The quote remained stale at 16:00 ET.
- AMIX faded from its $5.45 AH high to $4.90 and its scanner AH change dropped below +10%. CRE dropped out of the scan; Yahoo was $2.45 at 17:29 ET after the early $3.00 spike, confirming the prior SPIKE→FADE call.

**Catalysts and decisions:**
- DCX: same Grade C non-binding Whales AI MOU. **Skip:** it has sustained momentum and rebounded near its high, but the broker book remains unusable. No fillable two-sided market means no order.
- NUWE: the repeat search found no July 29 earnings, PR, or 8-K. July 27 preliminary Q2 revenue growth remains the newest material release. Grade None. **Wait:** genuine BUILD, multiple scans above +10%, and Total% below the ceiling, but the zero-ask quote is stale and cannot confirm a fillable book. The freshness guard makes this unconfirmed-but-live, not a bad-print rejection.
- AMIX: below +10% AH and only one prior scan above +10%. **Watch:** no sustained two-scan gate at the current threshold.
- ONCO: Alpaca tradable. No same-day earnings, PR, or 8-K found within the four-call budget. Grade None. **Skip for now:** first qualifying scan, immediate SPIKE→FADE, and no fillable ask.
- BOOM: Grade B Q2 earnings catalyst. **Wait:** multiple scans above +10%, Total% +19.8%, and holding near the high, but the broker quote is over an hour stale. A second pull did not refresh, so fillability is unconfirmed and no order was sent.
- SXTP: no same-day earnings, PR, or 8-K found within the four-call budget; the newest surfaced 8-K was one week old. Grade None. **Watch:** first scan above +10%, so it does not meet the two-scan gate.
- ONMD remains below +10% AH. No workup or entry.
- No paper orders submitted. No positions were added to `OPEN_POSITIONS.md`.

## Scan 00:00 CET (6:00 PM ET)

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| DCX | [TV](https://www.tradingview.com/chart/?symbol=DCX) | $1.08 | +19.7% | +35.2% | $1.46 | +61.9% | 8.2M | 1.0M | 8.2x | 2.1M | Motor Vehicles |
| NUWE | [TV](https://www.tradingview.com/chart/?symbol=NUWE) | $1.89 | -2.1% | +111.7% | $4.00 | +107.3% | 6.5M | 943K | 6.9x | 363K | Medical Specialties |
| AMIX | [TV](https://www.tradingview.com/chart/?symbol=AMIX) | $4.57 | +66.2% | +8.3% | $4.95 | +80.0% | 1.3M | 9.0M | 0.1x | 502K | Medical Specialties |
| ONCO | [TV](https://www.tradingview.com/chart/?symbol=ONCO) | $0.75 | -9.7% | +9.7% | $0.82 | -1.0% | 837K | 357K | 2.3x | 3.7M | Pharmaceuticals: Major |
| ONMD | [TV](https://www.tradingview.com/chart/?symbol=ONMD) | $0.64 | -9.4% | +13.6% | $0.73 | +2.9% | 623K | 4.4M | 0.1x | 16.4M | Packaged Software |
| GWAV | [TV](https://www.tradingview.com/chart/?symbol=GWAV) | $3.06 | +23.1% | +12.7% | $3.45 | +38.8% | 223K | 497K | 0.4x | 805K | Miscellaneous Commercial Services |
| BOOM | [TV](https://www.tradingview.com/chart/?symbol=BOOM) | $5.42 | -0.7% | +19.9% | $6.50 | +19.0% | 169K | 188K | 0.9x | 18.0M | Oilfield Services/Equipment |
| NAUT | [TV](https://www.tradingview.com/chart/?symbol=NAUT) | $1.04 | -13.3% | +6.7% | $1.11 | -7.5% | 84K | 804K | 0.1x | 63.4M | Biotechnology |

**Instrumentation and verification:**
- DCX: `DCX 2026-07-29  SPIKE  16:03ET  +22%  $1.32  712 trades / 104k sh  (first co-spike bar) (as-of 18:00ET)`. Scanner volume rose to 8.2M. Yahoo was $1.33 at 18:00 ET, below the stale $1.46 scanner price but within 16% of the $1.59 high. SIP stopped at 17:35 ET and the quote remained stuck at 17:00 ET with an unusable $0.05 x100 / $1.40 x2500 book.
- NUWE: `NUWE 2026-07-29  SPIKE  16:28ET  +16%  $2.20  190 trades / 16k sh  (first co-spike bar) (as-of 18:00ET)`. The real surge continued to a $4.09 SIP high on million-share, 10K-15K-trade bars. Yahoo was $3.40 at 18:00 ET, 16% below its $4.07 high and below the lagged scanner price. SIP stopped at 17:35 ET and the quote remained stuck at 16:00 ET with `ask $0.00 x0`.
- ONMD: `ONMD 2026-07-29  SPIKE  17:33ET  +16%  $0.74  63 trades / 14k sh  (first co-spike bar) (as-of 18:00ET)`. SIP confirms a brief $0.78 spike on 148K shares at 17:30 ET, followed by a drop to $0.70. Yahoo was $0.70 at 18:00 ET, only -2.0% versus the prior close, contradicting the scanner's stale +13.6% reading. The quote was stale with no ask.
- GWAV: `GWAV 2026-07-29  SPIKE  16:17ET  +16%  $3.55  239 trades / 27k sh  (first co-spike bar) (as-of 18:00ET)`. SIP shows two real spikes, first to $3.75 at 16:15 ET and then to $3.76 at 17:30 ET, but modest volume of 44K and 19K shares in the latest available bars. Yahoo was $3.47 at 18:00 ET, within 8% of the high and consistent with the scanner. The broker quote was stale at 16:18 ET, so current fillability is unconfirmed.
- BOOM: `BOOM 2026-07-29  SPIKE  16:09ET  +26%  $6.82  180 trades / 6k sh  (first co-spike bar) (as-of 18:00ET)`. Yahoo held $6.55 at 18:00 ET, within 4% of the high and consistent with the scanner. SIP confirms continuous but modest trading and a stable $6.50-$6.60 base; its latest bar was 25 minutes stale. The last broker book remained the stale 16:14 ET $6.22 x100 / $6.43 x100 quote.
- AMIX held around $5.04 but its scanner AH change stayed below +10%. ONCO faded to $0.84 after its $0.98 spike and also fell below +10%. NAUT remained below the workup threshold.

**Catalysts and decisions:**
- DCX: same Grade C non-binding Whales AI MOU. **Skip:** sustained scanner momentum and a late rebound do not overcome the unusable, stale one-sided book. No fillable two-sided market was confirmed.
- NUWE: the repeat structured search again found no July 29 earnings, PR, or 8-K. July 28 Aquadex installations and July 27 preliminary Q2 revenue growth remain the newest releases. Grade None. **Wait:** genuine high-volume BUILD-and-hold and Total% below the ceiling, but the stale zero-ask quote still cannot confirm a fillable book. The source is stale rather than evidence of a bad print.
- ONMD: no July 29 earnings, PR, or 8-K found. The July 28 $11.5M+ AI-training data agreement is the prior-day catalyst. **Skip:** this is its first scanner appearance above +10%, fresh Yahoo data shows the spike already faded below the threshold, and there is no fillable ask.
- GWAV: a July 29 Form 10-Q reported that Q1 revenue doubled and the quarterly loss narrowed. Grade B earnings catalyst. Alpaca tradable. **Watch:** first main AH scan above +10%, so it has not met the two-scan gate; volume is real but modest and the quote is stale.
- BOOM: Grade B Q2 earnings catalyst. **Wait:** multiple scans above +10%, low extension, and a strong hold near the AH high clear the trajectory gates, but the mandatory real-time two-sided-book check remains stale and cannot confirm fillability. Recheck at 00:30 CET.
- AMIX, ONCO, and NAUT are below +10% AH and do not qualify for entry. No paper orders were submitted and no positions were added to `OPEN_POSITIONS.md`.

## Scan 00:30 CET (6:30 PM ET)

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| DCX | [TV](https://www.tradingview.com/chart/?symbol=DCX) | $1.08 | +19.7% | +24.1% | $1.34 | +48.6% | 8.6M | 1.0M | 8.2x | 2.1M | Motor Vehicles |
| NUWE | [TV](https://www.tradingview.com/chart/?symbol=NUWE) | $1.89 | -2.1% | +75.6% | $3.32 | +72.0% | 7.8M | 1.1M | 7.1x | 363K | Medical Specialties |
| AMIX | [TV](https://www.tradingview.com/chart/?symbol=AMIX) | $4.57 | +66.2% | +8.5% | $4.96 | +80.4% | 1.4M | 9.0M | 0.2x | 502K | Medical Specialties |
| ONCO | [TV](https://www.tradingview.com/chart/?symbol=ONCO) | $0.75 | -9.7% | +8.4% | $0.81 | -2.2% | 875K | 361K | 2.4x | 3.7M | Pharmaceuticals: Major |
| ONMD | [TV](https://www.tradingview.com/chart/?symbol=ONMD) | $0.64 | -9.4% | +5.4% | $0.68 | -4.5% | 704K | 4.4M | 0.2x | 16.4M | Packaged Software |
| CRE | [TV](https://www.tradingview.com/chart/?symbol=CRE) | $2.42 | -1.4% | +9.3% | $2.64 | +7.8% | 479K | 87K | 5.5x | 1.1M | Commercial Printing/Forms |
| SXTP | [TV](https://www.tradingview.com/chart/?symbol=SXTP) | $1.49 | -0.7% | +12.1% | $1.67 | +11.3% | 423K | 84K | 5.0x | 2.6M | Biotechnology |
| GWAV | [TV](https://www.tradingview.com/chart/?symbol=GWAV) | $3.06 | +23.1% | +8.8% | $3.33 | +34.0% | 244K | 499K | 0.5x | 805K | Miscellaneous Commercial Services |
| BOOM | [TV](https://www.tradingview.com/chart/?symbol=BOOM) | $5.42 | -0.7% | +23.1% | $6.67 | +22.2% | 176K | 188K | 0.9x | 18.0M | Oilfield Services/Equipment |
| SHPH | [TV](https://www.tradingview.com/chart/?symbol=SHPH) | $2.78 | -0.4% | +7.6% | $2.99 | +7.2% | 93K | 568K | 0.2x | 596K | Pharmaceuticals: Major |
| NAUT | [TV](https://www.tradingview.com/chart/?symbol=NAUT) | $1.04 | -13.3% | +6.7% | $1.11 | -7.5% | 84K | 804K | 0.1x | 63.4M | Biotechnology |

**Instrumentation and verification:**
- DCX: `DCX 2026-07-29  SPIKE  16:03ET  +22%  $1.32  712 trades / 104k sh  (first co-spike bar) (as-of 18:30ET)`. TradingView volume increased to 8.6M. Yahoo was $1.42 at 18:30 ET, within 11% of the $1.59 SIP high, but the broker quote stayed frozen at 17:00 ET with an unusable $0.05 x100 / $1.40 x2500 book.
- NUWE: `NUWE 2026-07-29  SPIKE  16:28ET  +16%  $2.20  190 trades / 16k sh  (first co-spike bar) (as-of 18:30ET)`. SIP confirms the move on million-share bars and 10K-15K trades per bar through 17:35 ET. Yahoo was $3.28 at 18:30 ET, 19% below the $4.07 high. The quote remained frozen at 16:00 ET with `ask $0.00 x0`.
- SXTP: `SXTP 2026-07-29  SPIKE  16:13ET  +16%  $1.73  99 trades / 38k sh  (first co-spike bar) (as-of 18:30ET)`. Yahoo was $1.63 at 18:29 ET, only +8.7% from the regular close. The scanner's +12.1% reading was stale; its quote was also frozen at 16:00 ET.
- BOOM: `BOOM 2026-07-29  SPIKE  16:09ET  +26%  $6.82  180 trades / 6k sh  (first co-spike bar) (as-of 18:30ET)`. Yahoo made a late $6.72 high and held $6.71 at 18:30 ET. SIP confirms continuous real AH trading and a stable $6.50-$6.60 base through its lagged 17:35 ET bar. A $6.75 limit order filled at $6.72, confirming current fillability.

**Final-scan feed-lag cross-check:**
- Cross-checked all prior AH candidates and the 21:30 regular-session watch list. NCRA, SPRC, STFS, GMM, MWYN, BXBL, VIVK, CTXR, and ROC were not above +10% versus their regular-session closes. SYBX remained untradable (carried).
- GWAV was under-reported by TradingView. Yahoo showed $3.40 at 18:30 ET, +11.1% versus the $3.06 regular close, and lagged SIP confirms the 17:30 ignition on 43.7K shares and 729 trades. Treat this as its second threshold scan. No entry: the only broker quote was over two hours stale with a $3.32 / $4.20 spread, so a current fillable price could not be confirmed.

**Catalysts and decisions:**
- BOOM: Grade B Q2 earnings catalyst. Multiple scans above +10%, Total% +22.2%, late high, and a hold within 2% of that high cleared the sustained-momentum and trajectory gates. **BUY:** 14 shares filled at $6.72 on Alpaca paper, order `7ee5dc6d-913c-4fca-90e8-0d4f5d5959ec`.
- NUWE: Grade None; repeated structured searches found no July 29 catalyst. **Skip:** genuine volume-backed move and multiple qualifying scans, but the mandatory book check still showed no ask. It also declined steadily from $4.07 to $3.28 after 17:40 ET.
- DCX: Grade C non-binding Whales AI MOU. **Skip:** the price recovered near its high, but the broker book remained unusable and stale.
- SXTP: Grade None. **Skip:** fresh Yahoo data was below +10%, and the move did not sustain the threshold across two scans.
- GWAV: Grade B Q1 10-Q catalyst. **Skip:** final feed-lag rescue met the two-scan threshold, but the stale $0.88-wide broker spread did not establish a current fillable book.
- AMIX, ONCO, ONMD, CRE, SHPH, and NAUT were below +10% AH. SHPH remains untradable (carried). No other orders were submitted.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
| BOOM | $6.72 | 00:31 CET | 14 | 7ee5dc6d-913c-4fca-90e8-0d4f5d5959ec | Grade B Q2 earnings; sustained +10% across scans, late high, holding within 2% of AH high, real SIP volume |

## Morning Evaluation - 10:20 CET

### Today's Winner

**NUWE** - Medical Specialties
- Catalyst: **Grade None**. No July 29 company news was verified. The latest known items were July 28 Aquadex installations in Wisconsin and July 27 preliminary Q2 revenue growth of 14%; the morning search returned no relevant NUWE result.
- Previous Close: **$1.89**
- AH last night: SIP high **$4.10 (+116.9%)** at 17:40 ET / 23:40 CET. The move was real and liquid: peak ignition bars traded 1.12M-1.35M shares and 10.6K-15.0K trades per five minutes.
- Premarket now: **~$4.18 (+121.2%)**; SIP PM high **$4.67 (+147.1%)** at 04:00 ET on 1.04M shares and 17,456 trades. Yahoo under-reported the real high at $4.35.
- Hypothetical P&L (realistic 17:00 ET AH entry $2.56 → SIP PM peak $4.67): **+82.4%**
- Float: **363K** | Market Cap: **~$689K**

NUWE clears the winner bar: its SIP-backed high exceeded +100% from the regular close on heavy, accumulating volume and it held above +100% into premarket.

**Scanner Diagnostic:**
- Detectable at screening time? **YES**
- NUWE first surfaced at 22:45 CET at a stale TradingView $2.09 (+10.6% AH), while Yahoo and SIP already showed a real build near $2.63-$2.75 on 411K-553K shares and 4.6K-6.7K trades per bar. By 23:00 CET it was the cleanest BUILD candidate, then reached +110% on the 23:30 scan.
- We did not enter because Alpaca's book stayed frozen at the 16:00 ET close with `ask $0.00 x0`. This was not a detection or selection-rule miss. The mandatory fillability guard prevented an untradeable paper order.
- Scanner gap: none for detection. The execution-data gap is stale extended-hours quotes; the standing independent AH data-source verification recommendation remains appropriate, but a price/volume threshold change would not help.

**Broker-block tracking:** No `tradable=false` qualifier this session. NUWE was Alpaca-tradable but lacked a fresh fillable book, so it does not enter the broker-block tally.

### Baseline Tracking

- Days tracked: **57** (was 56 + 1)
- Winners detected by scanner: **47/53 (88.7%)**: NUWE added
- Winner selected for paper trade: **27/53 (50.9%)**: BOOM was entered; NUWE was detected but could not pass the live-book check
- Target: >80% detection
- Status: **BASELINE MET**
- **Baseline gap:** none new. The prior baseline is 2026-07-28, the immediately preceding US trading day. Historic uncounted 2026-07-17 and 2026-07-20 gaps remain visible and were not back-filled.

### Retrospective Scan Results

The 04:20 ET whole-market PM scan returned NUWE +129.2%, DCX +53.2%, GVH +35.1%, CAST +17.5%, and DGNX +14.5%. SIP reconstruction established NUWE as the only real >100% AH→PM explosion. DCX also produced a liquid PM-open high of $1.85, but only +71.3% from its actual $1.08 regular close. GVH was a small late-tail move; DGNX and CAST began their gains in PM or from regular-session anchor effects.

### Open Position P&L (Alpaca)

Alpaca holds one real position. Its `positions` price of $6.50 and the quote `$6.22 / $6.43 @ 2026-07-29T20:14Z` are stale. Yahoo's live PM timeline was ~$6.40 at 04:20 ET; SIP confirmed a $6.59 PM high at 04:00 ET and $6.55 at 04:05 ET. The live-mark P&L below uses $6.40. No hold/sell action was taken here.

| Ticker | Entry | Entry Total% | Catalyst | Entry Time | PM Peak | Peak Time | Exit | P&L | P&L % | Status |
|--------|-------|--------------|----------|------------|---------|-----------|------|-----|-------|--------|
| BOOM | $6.72 | +24.0% | B: Q2 earnings | 00:31 CET | $6.59 (SIP) | 04:00 ET | open | -$4.48 live | -4.8% live | Open; position evaluation handles exit |

**Total Realized P&L (Alpaca fills only): $0.00**

### Scanner Effectiveness

- Evening scans ran: **7 of 7 scheduled** (21:30, 22:00, 22:30, 23:00, 23:30, 00:00, 00:30 CET), plus 22:15 and 22:45 observation scans
- Candidates found: **12 unique AH tickers**
- Retrospective matches: **2/5 PM scan names** (NUWE and DCX). The three non-matches were weak PM-only or late-tail names, not meaningful winner misses.

### Missed Opportunities

| Ticker | AH Change | Why Missed | Would Be Profitable? |
|--------|-----------|------------|---------------------|
| GVH | −10% at final scan; +22% by 19:55 ET | Move began in the unscanned AH tail and remained below winner scale | No meaningful AH→PM edge; PM peak only $1.23 |
| DGNX | +5.3% at final scan | Below +10% during the full scanned window; move began at PM open | No AH setup; PM peak +18.7% |
| CAST | ~+2% from actual $1.20 regular close | Below threshold all evening; Yahoo's two-day anchor makes the headline misleading | No significant AH edge |

No significant detection miss. NUWE, the real winner, was caught.

### AH Mover Follow-Through

| Ticker | AH Peak | Peak Time | AH Trajectory | Current PM | From Peak | From Close | Verdict |
|--------|---------|-----------|---------------|------------|-----------|------------|---------|
| NUWE | $4.10 SIP | 17:40 ET | Build → hold → late rebuild | ~$4.18; PM peak $4.67 | −10.5% from PM peak | +121% | **PM exceeded AH; winner detected, no fillable book** |
| DCX | $1.59 SIP | 16:25 ET | Spike→fade→recover/hold | ~$1.46; PM peak $1.85 | −21.1% from PM peak | +35.2% vs $1.08 close | PM exceeded AH on 1.08M shares at open; skipped on unusable book |
| CRE | $3.50 SIP | 16:05 ET | Spike→fade | ~$2.66 thin | −24.0% from AH peak | +9.9% vs $2.42 close | **PM fell short of AH; fade skip correct** |
| SXTP | $1.84 SIP | 17:25 ET | Choppy spike→fade | ~$1.47; PM peak $1.63 | −20.1% from AH peak | −1.3% | **PM fell short of AH; threshold loss correct** |
| BOOM | $6.82 SIP | 16:05 ET | Spike→hold / late high | ~$6.40; PM peak $6.59 | −6.2% from AH peak | +18.1% | **PM fell short of AH; AH was the better exit** |

**AH-peak-vs-PM-peak check:** NUWE and DCX exceeded their AH peaks in PM. CRE, SXTP, and BOOM did not. No >250%-from-close extreme-runner case occurred.

### Notes

- **Coverage:** all 7 scheduled scans ran. No new coverage-failure row. The prior 2026-07-28 6/7 failure remains the latest incident.
- **Ceiling/dead-cat overrides:** no `CEILING-OVERRIDE WATCH` or `DEAD-CAT-OVERRIDE WATCH` was logged last night.
- **Fade-rule false-negative tracking:** CRE (float 1.1M, Grade None) adds a new sub-3M negative control. AH SIP peak $3.50; PM SIP peak $2.66, below AH. (a) first-sighting ~$2.92 → $2.66 = **−8.9%**; (b) PM-open VWAP $2.46 → $2.66 = **+8.1%**, but the peak had only 160 shares / 3 trades and was not a plausible exit. Standing sub-3M tally becomes **3 of 7 re-exploded** (LNKS, RPGL, ATPC yes; the prior CRE cycle, IOTR, WLDS, and today's separate CRE cycle fell short). The ≥4/5 trigger remains not met. No strong-catalyst fader was skipped.
- **PM-only gapper:** the morning's biggest raw mover was NUWE, an **AH→PM continuation**, not a PM-only gapper. Standing PM-only holdable tally remains **1 clear of 6**.
- **Late-AH-tail surge:** none for the winner. NUWE's decisive move began before 18:30 ET and was already +69.9% at the final scan. GVH moved in the tail but was only a +23% minor mover, not a winner-scale case.
- **In-window feed-lag misses:** none new; NUWE was surfaced. Standing count remains **3**, with the ≥3 escalation reached. Route the recommendation for an independent whole-universe AH gainers cross-check at the final scan to the daily email as a data-reliability decision.
- **Price-floor exclusions:** no new sub-$0.50 case surfaced in the broad PM scan. Standing count remains **3 total, 0 holdable**, all from 2026-07-28.
- **Reverse-split squeezes:** no new verified reverse-split case. Recency split remains this-week **3/3 faded**; weeks/months-old **3 non-fade / 1 fade**.
- **Selection diagnosis:** the scanner found the correct stock. The lost opportunity came from stale/no-ask broker market data, while the selected BOOM setup produced only a modest PM fade. This supports separating detection quality from execution-feed availability.

### Price Charts

Generated with `python3 scripts/price-timeline.py NUWE DCX BOOM`:

```text
NUWE  2-day range $1.85-$4.69 | current $4.19 | peak $4.69 at 04:00 ET
$4.35 |                                                  █     █
      |                                             ███ █  ████
$1.85 |████████████████████████████████████████████
      +------------------------------------------------------------>
AH: $2.19 at 16:30 → $4.07 at 17:40 → $3.59 at 19:55
PM: $4.35 at 04:00 → $4.19 at 04:20 (SIP high $4.67)

DCX   2-day range $0.77-$1.85 | current $1.46 | peak $1.85 at 04:00 ET
$1.65 |                                    █                 █
      |                              █████████████████████████ ███
$0.77 |██████████████████████████████
      +------------------------------------------------------------>
AH: $1.52 at 16:25 → $1.27 at 17:00 → $1.43 at 19:55
PM: SIP $1.85 high at 04:00 → $1.46 at 04:20

BOOM  2-day range $5.29-$6.97 | current $6.40 | peak $6.97 near AH open
$6.72 |███  ██                                              ██████
      |   ██  ██████
$5.29 |             ████████████████████████████████████████
      +------------------------------------------------------------>
AH: held mainly $6.50-$6.72; PM: $6.50 at 04:00 → $6.40 at 04:20
```
