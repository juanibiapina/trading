# Trade Log — 2026-06-23

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| VTAK | $1.49 | $1.51 | +1.3% | $1.65 (+10.7%) | 1 | B | HOLD | Above stop ($1.27), within 2-day window, trail not active (<+30%) |
| SKYQ | $1.87 | $1.66 | -11.2% | $1.93 | 1 | C | SELL | Hard stop ($1.68) breached in premarket |
| EHGO | $3.85 | $3.43 | -10.9% | $4.00 | 1 | C | SELL | Hard stop ($3.47) breached in premarket |

**Actions taken:**
- SELL SKYQ @ $1.66 (53 sh): -$11.13 (-11.2%). Stop breached; PM faded from AH peak.
- SELL EHGO @ $3.43 (25 sh): -$10.50 (-10.9%). Stop breached; steady PM fade from $4.00 AH peak.
- HOLD VTAK @ $1.51 (Grade B, day 1). Stop $1.27.

## Position Evaluation — 14:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| VTAK | $1.49 | $1.13 | -24.2% | $1.65 | 1 | B | SELL | Hard stop ($1.27) breached; PM peaked only $1.32 (below entry), faded through stop |

**Actions taken:**
- SELL VTAK @ $1.25 (67 sh): -$16.08 (-16.1%). Grade B hard stop breached. PM never recovered above entry; fill near stop crossing (PM 08:55 $1.24 → 09:00 $1.14).

No open positions remaining.

## Paper Trades

| Ticker | Entry Price | Entry Time | Shares (~€100) | Catalyst Grade | Reason |
|--------|-------------|------------|-----------------|----------------|--------|

## Scan 22:00 CET (4:00 PM ET)

AH scan, run right at the 16:00 ET open. Scanner: **0 hits** — no AH volume registered yet (bars not populated at the open). `check-prices --ah-history` on the 21:30 watch shortlist still returned prior-day bars (06-22/06-18), confirming today's AH feed hasn't updated.

Learning-phase rule: 22:00 scan is **observation only** — no entries before 23:00 CET regardless.

Watch shortlist carry-forward (to confirm at 22:30/23:00 when AH data populates):

| Ticker | Float | 21:30 Price | 21:30 Chg% | Status |
|--------|-------|-------------|------------|--------|
| GITS | 2.2M | $2.00 | +32.1% | Best watch — vol was building into close |
| HSCS | 3.1M | $2.68 | +51.4% | Big move, vol was fading at 21:30 |
| RDGT | 884K | $1.75 | +27.7% | Tiny float, fading vol |
| CRMT | 7.6M | $3.93 | +30.6% | Likely earnings reaction |
| CYAN | 4.0M | $0.52 | +33.2% | Low vol, sub-$1 |

**Decision:** No paper trades. Re-scan at 22:30/23:00 CET to see which carry into AH with sustained volume.

## Scan 21:30 CET (3:30 PM ET)

Regular session scan (market still open). No entries — flagging candidates as **Watch — pending AH confirmation**. Per regular-session caution: only enter if a name reappears in an AH scan (22:00+ CET) with sustained momentum.

Watch shortlist (float <10M, real volume, sustained move):

| Ticker | Chart | Price | Chg% | 5mVol | IRVol | VChg% | Float | MCap | Industry | Note |
|--------|-------|-------|------|-------|-------|-------|-------|------|----------|------|
| GITS | [TV](https://www.tradingview.com/chart/?symbol=GITS) | $2.00 | +32.1% | 71K | 674x | +142.5% | 2.2M | 7.3M | Packaged Software | Volume building into close — best watch |
| HSCS | [TV](https://www.tradingview.com/chart/?symbol=HSCS) | $2.68 | +51.4% | 57K | 2763x | -85.4% | 3.1M | 8.5M | Medical Specialties | Big move but volume fading |
| RDGT | [TV](https://www.tradingview.com/chart/?symbol=RDGT) | $1.75 | +27.7% | 25K | 77x | -55.0% | 884K | 1.6M | Medical Distributors | Tiny float, fading vol |
| CRMT | [TV](https://www.tradingview.com/chart/?symbol=CRMT) | $3.93 | +30.6% | 34K | 4.0x | -35.2% | 7.6M | 32.6M | Specialty Stores | Earnings reaction likely |
| CYAN | [TV](https://www.tradingview.com/chart/?symbol=CYAN) | $0.52 | +33.2% | 1K | 4.0x | +36.8% | 4.0M | 3.8M | Pharma | Low vol, sub-$1 |

Other movers were mostly low-volume noise (5mVol <1K) or high-float (AZREF 64M, OBGRF 29.5M, FWRXF 44.5M). 58 raw hits; full list in scanner output.

**Decision:** No paper trades — regular session, before AH. Re-scan at 22:00+ CET to confirm which of these carry momentum into after-hours.
