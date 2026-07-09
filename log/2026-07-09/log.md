# 2026-07-09

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| SUNE | $2.56 | $2.44 | -4.7% | ~$2.67 (+4.3%) | 1 | None | SELL | Grade None → exit first premarket opportunity. Above -10% hard stop but no catalyst; sold on PM fade. |

**Actions taken:**
- SELL 36 SUNE @ limit $2.35 ext (id 54d1a663), filled @ $2.44. Final P&L −$4.32 (−4.7%).
- PM opened $2.72 spike (single-bar, L $2.36 same bar) then faded to $2.41 / vwap $2.39. OVN peak ~$2.67. Never re-rated above entry. Grade None rule applied.
- No open positions remaining.

## Position Evaluation — 14:30 CET

No open positions. Alpaca `positions` empty; `OPEN_POSITIONS.md` reconciled (clean slate). SUNE was closed in the 10:30 pulse. Nothing to hold or sell.

## Scan 21:30 CET (3:30 PM ET)

**Regular session** (AH opens 16:00 ET / 22:00 CET). Observation only — no entries before AH per regular-session caution rule. Most high-Chg% hits show tiny share counts (100-600 sh) = stale/illiquid regular-session prints, not tradable. Notable movers to watch into AH:

| Ticker | Chart | Price | Chg% | 5mVol | IRVol | VChg% | Float | MCap | Industry |
|--------|-------|-------|------|-------|-------|-------|-------|------|----------|
| SUNE | [TV](https://www.tradingview.com/chart/?symbol=SUNE) | $2.64 | +25.1% | 23K | 103.4 | -27.0% | 3.4M | 10.9M | Engineering & Construction |
| EVGN | [TV](https://www.tradingview.com/chart/?symbol=EVGN) | $0.50 | +20.7% | 71K | 17.4 | +27.9% | 12.0M | 6.1M | Biotechnology |
| DOGZ | [TV](https://www.tradingview.com/chart/?symbol=DOGZ) | $1.01 | +1.0% | 15K | 14.6 | +111.6% | 3.9M | 14.7M | Consumer Sundries |
| HYEX | [TV](https://www.tradingview.com/chart/?symbol=HYEX) | $2.20 | +69.2% | 2K | 2.9 | +240.0% | 1.6M | 37.2M | Pharmaceuticals: Other |

**Notes:**
- SUNE: our closed position from this morning (sold PM @ $2.44, Grade None). Back to +25.1% intraday on real volume (23K/5min). Watch whether it carries into AH — do NOT re-enter the same ticker (one entry per candidate per night rule), and it stays Grade None.
- EVGN: only real-volume sub-$10 mover with float <15M besides SUNE. Sub-$1 biotech. Watch for AH catalyst.
- HYEX +69% but thin (2K/5min) — likely stale. Watch AH liquidity.
- Ultra-high %s (CYDX +493%, RBNE +1623%, VRAX +109%, WMTN +458%, SRRCF +3010%) all have <1K share prints = illiquid noise. Ignore unless real AH book appears.
- No entries: pre-AH observation scan. Re-evaluate at 22:00+ CET AH scans.

## Scan 22:00 CET (4:00 PM ET)

**AH open** — scanner 0 hits at 16:00 ET (volume not yet accumulated; normal this early). Observation only per learning-phase rule (no entries before 23:00 CET). Watchlist from 21:30 checked via broker quotes:

| Ticker | Quote (bid/ask) | Note |
|--------|-----------------|------|
| SUNE | $2.20 x100 / $2.96 x100 | Wide spread, thin. Our closed position (Grade None, do-not-re-enter). |
| EVGN | $0.42 x100 / $0.59 x500 | Wide spread, low price. Watch AH build. |
| HYEX | no quote | No Alpaca AH book. |
| DOGZ | $0.83 x100 / $0.00 x0 | Ask $0.00 x0 = no fillable AH book. |

**Notes:**
- No candidates. Books thin/wide at AH open, no accumulation yet.
- No entries (observation-only scan + no fillable liquidity). Re-evaluate at 22:30 / 23:00 CET.

## Scan 22:30 CET (4:30 PM ET)

**AH scan** — 3 hits. Observation only per learning-phase rule (no entries before 23:00 CET). SIP bars + real books:

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| ELAB | [TV](https://www.tradingview.com/chart/?symbol=ELAB) | $1.06 | +0.0% | +19.8% | $1.27 | +19.8% | 2.5M | 5.9M | 0.4x | 4.5M | Biotechnology |
| AEHL | [TV](https://www.tradingview.com/chart/?symbol=AEHL) | $1.07 | +8.6% | +15.9% | $1.24 | +25.8% | 599K | 176K | 3.4x | 15.4M | Building Products |
| PMA | [TV](https://www.tradingview.com/chart/?symbol=PMA) | $1.29 | +3.2% | +10.1% | $1.42 | +13.6% | 90K | 2.0M | 0.0x | 4.6M | Engineering & Construction |

**SIP bars (5Min, from 20:00Z / 16:00 ET) + real books:**
- **AEHL** — BUILD pattern. $1.07→$1.10→$1.26→$1.41, vol accelerating 13K→32K→641K→1.4M sh, trades 54→102→3079→7338, new high $1.49 in latest bar. Real accumulation. Book bid $1.14 x100 / ask $1.53 x100 (wide). Strongest candidate into 23:00 — watch for continued build. Float 15.4M, Building Products (non-bio).
- **ELAB** — SPIKE→FADE. Peaked $1.44 in first bar (16:00-16:05 ET) on 418K sh, huge 1.6M-sh second bar, now settling $1.26-1.28. Early peak, fading off high. Tight book bid $1.21 x200 / ask $1.22 x100. Float 4.5M biotech. Early-peak fade — low priority.
- **PMA** — building on lighter volume. $1.34→$1.54, vol 49K→17K→39K→245K sh. Book bid $1.16 / ask $1.57 (wide). Float 4.6M. Lower conviction than AEHL.

**Notes:**
- No entries (observation-only scan). AEHL is the lead BUILD candidate; ELAB fading; PMA weak build.
- Catalyst searches deferred to 23:00 entry scan (search budget). Re-evaluate all three at 23:00 CET with fresh bars + catalyst check.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
| _(none yet)_ | | | | | |
