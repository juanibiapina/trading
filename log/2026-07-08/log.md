# Trade Log — 2026-07-08

## Position Evaluation — 10:30 CET

Premarket window (04:30 ET). Source of truth: Alpaca positions + SIP bars. Quote endpoint returned stale close (20:00Z) values; used SIP PM bars for live levels.

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| SEER | $2.26 | $2.16 | -4.4% | $2.34 (+3.5%) | 5 | A | HOLD | Day 5/5 time limit today. Catalyst intact ($2.45 buyout floor). Book dead now (621 sh/bar) — exit at 14:30 CET window for a better fill. No stop/trail hit. |
| DCX | $1.34 | $1.48→$1.39 | +3.7% | $1.63 (PM H) | 1 | None | SELL | Grade None → exit first PM opportunity at profit. PM opened strong (2.5M sh/bar) then faded; sold on fade. |
| VEEE | $6.28 | $6.30 | -1.8% | $7.31 (AH) | 1 | C | SELL | Grade C → exit in first PM pulse. Faded from AH high $7.31 / PM open $6.97 to vwap $6.45. Above -10% stop. |

**Actions taken:**
- SELL 66 DCX @ $1.39 ext (id a10d862b) — first limit $1.44 didn't fill (price faded to $1.40), re-priced to $1.36, filled $1.39. P&L +$3.30 (+3.7%).
- SELL 15 VEEE @ $6.17 ext (id 590df196). P&L -$1.65 (-1.8%).
- SEER held; flagged for exit at 14:30 CET pulse (final day, thin PM book now).

**Realized today:** +$3.30 (DCX) − $1.65 (VEEE) = **+$1.65 net**.

## Position Evaluation — 14:30 CET

Premarket window (08:30 ET). Second pulse to exit SEER at the deeper-book window per the 10:30 plan.

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| SEER | $2.26 | $2.20 | -2.7% | $2.34 (+3.5%) | 5 | A | SELL | Day 5/5 Grade A time limit reached. Catalyst intact ($2.45 buyout floor) but hold window over. SIP PM prints steady $2.16–2.20; no trail/stop hit. |

**Actions taken:**
- SELL 43 SEER @ limit $2.12 ext (id 34b9f54e) — filled @ $2.20 (filled at the real bid, better than limit). P&L -$2.58 (-2.65%).

**Realized 14:30 pulse:** -$2.58 (SEER).
**Realized today total:** +$3.30 (DCX) − $1.65 (VEEE) − $2.58 (SEER) = **-$0.93 net**. All positions flat.

---

# Post-Market Screening - 2026-07-08

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|

## Scan 21:30 CET (3:30 PM ET)

**REGULAR session** (scanner reports `Session: REGULAR`). AH opens 16:00 ET / 22:00 CET. Per the regular-session caution rule, no paper trades enter now — all candidates are **Watch — pending AH confirmation**. Re-check at the 22:00+ CET AH scans; only enter if a name reappears with sustained AH momentum (and per learning-phase default, no entries before 23:00 CET).

Notable regular-session movers (sorted by relative volume / Chg%):

| Ticker | Chart | Price | Day% | IRVol | Float | MCap | Industry | Note |
|--------|-------|-------|------|-------|-------|------|----------|------|
| NVVE | [TV](https://www.tradingview.com/chart/?symbol=NVVE) | $9.80 | +88.9% | 752.9x | 416K | $5.1M | Electrical Products | Micro-float, huge Day% + IRVol — top AH-watch |
| VTAK | [TV](https://www.tradingview.com/chart/?symbol=VTAK) | $1.39 | +95.0% | 20.6x | 2.0M | $1.9M | Medical Specialties | Sub-2M float, +95% intraday |
| TVRD | [TV](https://www.tradingview.com/chart/?symbol=TVRD) | $4.76 | +53.5% | 4.5x | 6.1M | $44.7M | Biotechnology | Biotech, mid Day% |
| WTXR | [TV](https://www.tradingview.com/chart/?symbol=WTXR) | $0.69 | +52.3% | 15.9x | 43.2M | $61.0M | Oil & Gas Production | High float |
| SRXH | [TV](https://www.tradingview.com/chart/?symbol=SRXH) | $1.99 | +47.0% | 8.4x | — | $19.5M | Biotechnology | Biotech |
| IOTR | [TV](https://www.tradingview.com/chart/?symbol=IOTR) | $3.55 | +40.9% | 1192x | 644K | $17.3M | IT Services | Low float, very thin (300 sh/5m) |
| YAAS | [TV](https://www.tradingview.com/chart/?symbol=YAAS) | $0.91 | +27.7% | 34.1x | 12.0M | $20.7M | Packaged Software | — |
| SKYQ | [TV](https://www.tradingview.com/chart/?symbol=SKYQ) | $3.75 | +24.8% | 3.7x | 3.8M | $18.0M | Integrated Oil | Prior-loss name (Jun 10 -27.6%) |

No entries — regular-session scan. Watch list carried to AH scans.
