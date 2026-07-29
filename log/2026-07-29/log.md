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

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
