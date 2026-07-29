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

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
