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

## Scan 22:00 CET (4:00 PM ET)

**AFTERHOURS session** — but AH opened this exact minute (16:00 ET). `scan.py --all` returned **0 hits**; ext-hours volume has not accumulated yet and Yahoo still serves yesterday's AH history. Nothing to evaluate this pulse.

Per learning-phase default, the 22:00 pulse is observation-only regardless (no entries before 23:00 CET). Watchlist carried from 21:30 for the next AH scan:

- **NVVE** — micro-float (416K) +88.9% Day%, 752.9x IRVol; top AH-watch if it sustains after the open.
- **VTAK** — sub-2M float (2.0M) +95% intraday.
- **IOTR** — 644K float but very thin (300 sh/5m); watch for real AH book.
- **YAAS / SKYQ / TVRD / SRXH / WTXR** — secondary watches.

No candidates found (0 scanner hits). Re-scan at 22:30 CET once AH volume builds.

## Scan 22:30 CET (4:30 PM ET)

**AFTERHOURS session** — AH volume now building. `scan.py --all` returned **2 hits**.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| SRXH | [TV](https://www.tradingview.com/chart/?symbol=SRXH) | $1.97 | +45.9% | +11.7% | $2.20 | +63.0% | 2.7M | 10.1M | 0.3x | 0 | Biotechnology |
| LIQT | [TV](https://www.tradingview.com/chart/?symbol=LIQT) | $0.77 | +2.5% | +10.1% | $0.85 | +12.9% | 72K | 247K | 0.3x | 24.2M | Industrial Machinery |

**Observation-only pulse** (learning-phase default: no entries before 23:00 CET). Notes:

- **SRXH** — carried from the 21:30 watchlist (regular +47%). Now building in AH: Day +45.9% → AH +11.7% → Total +63.0%. BUILD pattern from regular into AH. Biotech. VRatio 0.3x is weak (AH Vol 2.7M < AvgVol 10.1M) — the scanner counts it a hit on absolute AH volume, but AH is not yet outpacing normal daily flow. Top watch for the 23:00 entry scan; needs a real two-sided book and sustained AH% to qualify.
- **LIQT** — new. +10.1% AH, Total only +12.9%, float 24.2M, VRatio 0.3x (72K AH vs 247K avg). Weak AH volume, modest move, mid float. Low priority.
- **Watchlist attrition:** NVVE / VTAK / IOTR (top regular-session micro-floats) did NOT reappear as AH hits — regular-session spikes not carrying into AH so far. Re-check at 23:00.

No entries (observation-only). Re-scan at 23:00 CET for first entry window.
