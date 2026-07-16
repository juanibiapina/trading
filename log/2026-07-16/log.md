# 2026-07-16

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|

## Scan 22:30 CET (4:30 PM ET) — AFTERHOURS

Scanner returned 4 hits. Observation-only scan (learning phase blocks entries before 23:00 CET).

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| PMAX | [TV](https://www.tradingview.com/chart/?symbol=PMAX) | $1.76 | +6.0% | +18.1% | $2.08 | +25.2% | 1.4M | 260K | 5.2x | 892K | Specialty Telecommunications |
| GLXG | [TV](https://www.tradingview.com/chart/?symbol=GLXG) | $1.07 | -14.4% | +31.8% | $1.41 | +12.8% | 527K | 120K | 4.4x | 1.7M | Miscellaneous Commercial Services |
| ATPC | [TV](https://www.tradingview.com/chart/?symbol=ATPC) | $4.20 | +66.7% | +8.3% | $4.55 | +80.6% | 1.3M | 4.1M | 0.3x | 475K | Pharmaceuticals: Other |
| CRDF | [TV](https://www.tradingview.com/chart/?symbol=CRDF) | $0.87 | -1.7% | +5.2% | $0.92 | +3.5% | 344K | 2.3M | 0.2x | 62.5M | Medical Specialties |

**Observations (no entries — before 23:00 CET gate):**
- **PMAX** (new): first AH appearance, AH +18.1% above the 10% gate, float 892K, VRatio 5.2x, low extension (+25% total). BUILD watch — track for the 23:00 scan. Needs a 2nd AH scan >10% to clear the entry gate.
- **GLXG** (new): AH +31.8% but Day% -14.4%, right at the dead-cat threshold. AH price $1.41 sits above regular close $1.07 (reclaim), so watch for dead-cat-override behavior. Float 1.7M. Track.
- **ATPC** (carried from 21:30 regular scan): AH only +8.3%, below the 10% gate. VRatio 0.3x = volume fading, not building into AH. Watch only.
- **CRDF** (new): AH +5.2% below the 10% gate, float 62.5M (high), VRatio 0.2x. Not a candidate.

**Decision:** No entries. Observation-only scan (before 23:00 CET). PMAX and GLXG are the names to watch; both need a 2nd AH scan >10% to qualify. Re-scan at 23:00 CET.

## Scan 22:00 CET (4:00 PM ET) — AFTERHOURS open

Scanner returned 0 hits. AH just opened; observation-only scan (learning phase blocks entries before 23:00 CET).

No candidates found.

**Decision:** No entries. First AH scan of the night, no movers detected. Re-scan at 22:30/23:00 CET.

## Scan 21:30 CET (3:30 PM ET) — REGULAR session

AH not open yet (opens 16:00 ET / 22:00 CET). Regular-session caution: no entries, watch only pending AH confirmation. Scanner returned 55 regular-session hits; notable low-float movers below.

| Ticker | Chart | Price | Chg% | Float | MCap | IRVol | VChg% | Industry | Note |
|--------|-------|-------|------|-------|------|-------|-------|----------|------|
| ATPC | [TV](https://www.tradingview.com/chart/?symbol=ATPC) | $4.12 | +63.5% | 475K | 4.1M | 1588x | -99.3% | Pharma: Other | Vol fading (5mVol 500) |
| STAK | [TV](https://www.tradingview.com/chart/?symbol=STAK) | $3.80 | +78.4% | 0 | 38.0M | 242x | -99.9% | Oilfield Svc | Vol fading |
| DXST | [TV](https://www.tradingview.com/chart/?symbol=DXST) | $2.72 | +30.8% | 1.2M | 4.9M | 54x | -99.3% | Env Svc | Prior winner name; vol fading |
| TGHL | [TV](https://www.tradingview.com/chart/?symbol=TGHL) | $1.49 | +82.9% | 12.7M | 37.7M | 28x | -99.9% | IT Svc | Already traded+sold today (-18.6%) |
| CLIK | [TV](https://www.tradingview.com/chart/?symbol=CLIK) | $1.77 | +19.7% | 724K | 5.8M | 122x | -86.1% | Personnel Svc | Vol fading |
| CRNG | [TV](https://www.tradingview.com/chart/?symbol=CRNG) | $2.00 | +263.6% | 0 | 35.3M | 1.5x | +485% | REIT | Low rel-vol |

**Decision:** No entries. This is a pre-AH regular-session scan; per the regular-session caution rule, candidates are watch-only pending AH confirmation (22:00+ CET). Most notable movers show VChg -99% (regular-session volume already fading, not building into AH). Learning-phase policy also blocks entries before the 23:00 CET scan. Re-scan at 22:00 CET when AH opens.

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| TGHL | $1.33962 | $1.09 | -18.6% | $1.33 (PM) | 1 | None | SELL | Grade None: exit first PM opportunity + below -10% hard stop |

**Actions taken:**
- SELL 79 TGHL @ limit $1.04 ext (id e56b50df) → filled @ $1.09. Final P&L -$19.72 (-18.6%).
- No open positions remain.

**Notes:**
- TGHL faded from PM open $1.15; 5Min SIP bars $1.33H→$1.08C on 5.6M sh, vwap $1.07-1.20 (liquid book). Sold into the fade per Grade None rule.
- Broker quote endpoint returned a stale close-print bid ($1.18 @ prior 20:59Z); used live SIP bars for pricing instead.

## Position Evaluation — 14:30 CET

No open positions. Alpaca `positions` returns empty; `OPEN_POSITIONS.md` already reconciled (shows none). TGHL was the last position, sold in the 10:30 pulse @ $1.09. Nothing to evaluate.

**Actions taken:**
- None.
