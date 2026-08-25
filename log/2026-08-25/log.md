
# Post-Market Screening - 2026-08-25

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| WLDS | $3.30 | $2.66 | -19.4% | $3.58 | 1 | None | SELL | Grade None exit first PM + far below -10% hard stop; PM no follow-through |

**Actions taken:**
- SELL 28 WLDS @ limit $2.58 ext (id 2eeb31ea) filled @ $2.66. Real fill $2.66, P&L -$17.92 (-19.4%).
- No open positions remain.

## Position Evaluation — 14:30 CET

No open positions (Alpaca source of truth). WLDS closed at 10:30 pulse. OPEN_POSITIONS.md reconciled (shows none). Nothing to evaluate or sell.

## Scan 21:30 CET (3:30 PM ET)

**REGULAR session** — AH not open yet (opens 22:00 CET / 4:00 PM ET). No entries per regular-session caution rule. Low-float / big-move names flagged as watch pending AH confirmation.

| Ticker | Chart | Price | Chg% | Float | MCap | IRVol | VChg% | Industry | Watch |
|--------|-------|-------|------|-------|------|-------|-------|----------|-------|
| DAIC | [TV](https://www.tradingview.com/chart/?symbol=DAIC) | $3.48 | +101.2% | 1.3M | 3.4M | 10.4 | +185.9 | Miscellaneous | Watch |
| PMI | [TV](https://www.tradingview.com/chart/?symbol=PMI) | $9.91 | +93.1% | 1.3M | 12.0M | 25.9 | +33.6 | Medical Specialties | Watch |
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $0.58 | +127.1% | 4.4M | 2.0M | 833.1 | -20.4 | Misc Commercial Services | Watch (fading vol) |
| JEM | [TV](https://www.tradingview.com/chart/?symbol=JEM) | $6.66 | +74.3% | n/a | 4.3M | 566.6 | -39.2 | Wholesale Distributors | Watch (fading vol) |
| TNMG | [TV](https://www.tradingview.com/chart/?symbol=TNMG) | $0.61 | +54.2% | 2.3M | 1.8M | 505.0 | +90.9 | Internet Software/Services | Watch |
| AMIX | [TV](https://www.tradingview.com/chart/?symbol=AMIX) | $8.26 | +53.8% | 946K | 8.0M | 157.0 | -68.4 | Medical Specialties | Watch (fading vol) |
| SWVL | [TV](https://www.tradingview.com/chart/?symbol=SWVL) | $2.19 | +49.0% | 5.3M | 21.8M | 6337.1 | -46.5 | Other Transportation | Watch (fading vol) |

**Notes:**
- Regular-session scan only. Instrumentation (spike-bar, third-bar confirmation) not run — AH ignition tools apply after 4:00 PM ET open.
- Watchlist above = low-float (<10M) names with >45% intraday move. Re-evaluate at 22:00+ CET AH scans; enter only if a name reappears with sustained AH momentum (2+ AH scans) and clears all entry gates at 23:00+ CET.
- Several names (NCPL, JEM, AMIX, SWVL) already showing fading intraday volume (VChg% negative or IRVol declining) — spike-then-fade risk into AH.

## Scan 22:00 CET (4:00 PM ET)

**AH just opened** (16:00 ET). Scanner `--all`: 0 hits. Observation-only scan (learning-phase entry gate is 23:00+ CET). No entries.

Carry-forward check on 21:30 low-float watch names (AH quotes at 16:00 ET, seconds into session — thin/forming books):

| Ticker | Reg Close | AH Bid | AH Ask | Note |
|--------|-----------|--------|--------|------|
| DAIC | $3.48 | $3.31 | $0.00 x0 | No AH ask/offer — no fillable book yet |
| PMI | $9.91 | $8.25 | $10.90 | Wide spread, below reg close |
| NCPL | $0.58 | $0.49 | $0.65 | Below close, thin |
| TNMG | $0.61 | $0.48 | $0.65 | Below close, thin |
| AMIX | $8.26 | $6.21 | $8.25 | Below close, wide |

**Notes:**
- Scanner returned no AH movers >threshold at open. Watch names sitting flat/below regular close, no AH momentum yet.
- Instrumentation (spike-bar, third-bar confirmation) not run — no candidate cleared threshold and it's observation-only.
- Re-evaluate at 22:30 / 23:00 CET. Entries only at 23:00+ with a candidate clearing all gates (float <50M, AH >10% in ≥2 AH scans, Day% > -15%).

## Scan 22:15 CET (4:15 PM ET)

**AH open ~15 min in.** Scanner `--all`: 0 hits (feed lag). Observation-only (entry gate 23:00+ CET). No entries.

SIP cross-check on 21:30 watch names — **DAIC is a real AH mover the TradingView feed missed**:

| Ticker | Reg Close | AH SIP C | AH% | AH Vol | Trades | AH Ask | Note |
|--------|-----------|----------|-----|--------|--------|--------|------|
| DAIC | $3.48 | $4.19 (H $4.36) | +20% | 745K | 6004 | $0.00 x0 | Real SIP build above close; but no fillable ask book yet |
| PMI | $9.91 | $8.82 (vwap $9.18) | -11% | 244K | 3004 | $10.90 | Below close, fading |
| NCPL | $0.58 | $0.52 | -10% | 1.8M | 2892 | $0.90 | Below close |
| TNMG | $0.61 | ~$0.48–0.65 | flat | — | — | $0.65 | Stale quote, no build |
| AMIX | $8.26 | — | — | — | — | $8.25 | Below close, wide |
| SWVL | $2.19 | — | — | — | — | $2.49 | Flat |

**Instrumentation (log-only, DAIC AH >10%):**
- `DAIC 2026-08-25 NO-SPIKE flat/faded (peak <= base) (no bar cleared +15% on a volume co-spike) as-of 16:15ET`
- `DAIC 2026-08-25 CONFIRM-3 NO no local-volume new-high ignition as-of 16:15ET`

**Notes:**
- DAIC building in AH on real SIP volume (745K sh / 6004 trades first bar, C $4.19 = +20% above reg close $3.48, Total% ~+142% from prior close). TradingView `--all` returned 0 — feed-lag omission. Flag for entry evaluation at 23:00+ CET (needs 2-AH-scan gate + fillable ask book; currently `ask $0.00 x0`, no fill possible).
- DAIC Total% ~+142% sits near the +150% extension ceiling — watch entry extension at later scans.
- Other watch names (PMI, NCPL, AMIX, SWVL) all sitting below reg close in AH — spike-then-fade, no new momentum.
- Re-evaluate at 22:30 / 23:00 CET.

## Scan 22:30 CET (4:30 PM ET)

**AH ~30 min in.** Scanner `--all`: 3 hits. Observation-only (learning-phase entry gate 23:00+ CET). No entries.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| XPON | [TV](https://www.tradingview.com/chart/?symbol=XPON) | $5.27 | -15.0% | +41.0% | $7.43 | +19.8% | 2.3M | 10.5M | 0.2x | 891K | Electrical Products |
| YYGH | [TV](https://www.tradingview.com/chart/?symbol=YYGH) | $1.15 | -3.4% | +37.8% | $1.58 | +33.2% | 2.5M | 903K | 2.8x | 1.6M | Misc Commercial Services |
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $0.57 | +124.3% | +9.3% | $0.63 | +145.2% | 7.9M | 50.4M | 0.2x | 4.4M | Misc Commercial Services |

**Instrumentation (log-only, AH >10%):**
- `XPON 2026-08-25 SPIKE 16:01ET +17% $6.19 1317 trades / 136k sh (first co-spike bar) as-of 16:30ET`
- `XPON 2026-08-25 CONFIRM-3 NO no local-volume new-high ignition as-of 16:30ET`
- `YYGH 2026-08-25 SPIKE 16:10ET +36% $1.56 1748 trades / 443k sh (first co-spike bar) as-of 16:30ET`
- `YYGH 2026-08-25 CONFIRM-3 PENDING ignition 16:10ET; waiting for third bar as-of 16:30ET`
- `DAIC 2026-08-25 NO-SPIKE peak +12% @16:03ET (no bar cleared +15% on volume co-spike) as-of 16:30ET`
- `DAIC 2026-08-25 CONFIRM-3 NO no local-volume new-high ignition as-of 16:30ET`

**SIP verification (feed=sip, AH bars from 16:00 ET):**

| Ticker | 16:00 vwap | 16:05 | 16:10 | 16:15 | Trajectory | Real-time book |
|--------|-----------|-------|-------|-------|-----------|----------------|
| XPON | $6.56 | $7.33 | $7.38 | $7.72 (C $7.91) | **BUILD** — rising vwap all 4 bars, 0.5–1.4M sh/bar, 7k–19k trades | quote stale 16:00ET, `ask $0.00 x0` (no live book yet) |
| YYGH | $1.16 (7 tr) | — | $1.52 (2.8M sh) | $1.54 (C $1.49, off $1.65 high) | SPIKE 16:10 then slight fade, holding near | live book `bid $1.63 x100 / ask $1.66 x100` |
| DAIC | $4.11 (H $4.36) | $4.07 | $3.72 | $3.69 (C $3.76) | **SPIKE→FADE** — peaked first bar, off ~13% | quote stale 16:00ET, `ask $0.00 x0` |

**Notes:**
- **XPON** = strongest candidate. Real, volume-backed BUILD (SIP vwap climbing $6.56→$7.72, >1M sh/bar). Tiny float 891K. SIP corroborates scanner $7.43 (SIP H $8.09). Day% -15.0% (right at the dead-cat threshold — regular session was a -15% drop; AH is reclaiming above the $5.27 close to $7.43, so this is a reclaim-above-close BUILD, not a below-close dead-cat bounce). Total% only +19.8% (well under the +150% ceiling). tradable=true. Blocker: real-time ask book stale/empty at this scan — recheck at 23:00 for a fillable ask. Needs 2nd AH scan to clear the 2-AH-scan gate; this is its first AH appearance.
- **YYGH** = real mover, live two-sided book, float 1.6M, tradable=true. Spiked hard 16:10 (2.8M sh) then faded slightly, holding ~$1.5. First AH appearance — needs a 2nd AH scan. Watch for build-vs-fade at 23:00.
- **DAIC** = the 21:30/22:15 watch name faded. Peaked first AH bar $4.36 then declined to $3.6–3.8. SPIKE→FADE, no fillable book. Drop unless it rebuilds.
- **NCPL** = AH +9.3% (below 10% threshold); +124% move is regular-session, VRatio 0.2x (fading). Not a real AH mover. Skip.
- Re-evaluate at 23:00 CET (entry gate). XPON leads on trajectory (BUILD) if it holds and shows a fillable book; needs its 2nd AH scan to clear the gate.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|

No entries — regular-session scan, AH not open.
