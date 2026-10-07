## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| BIYA | $1.91 | $2.44 | +27.8% | $2.86 (+49.7%) | 1 | None | SELL | Grade None exit at first PM opportunity at any profit. Filled $2.41 (+26.2%). |
| MTEN | $1.39 | $1.48 | +6.5% | $1.79 (+28.8%) | 1 | B | HOLD | Day 1 of 2. Peak +28.8% is under the +30% trail trigger ($1.81). Hard stop $1.18 not hit. Catalyst intact (MTEN is the acquirer in a completed $15M cash acquisition, so the fixed-price buyout re-grade does not apply). |

**Actions taken:**

- SELL BIYA 52 @ limit $2.25 ext (id 12241ef6) filled @ $2.41. +$26.00 (+26.2%). The 08:10Z PM spike to $2.86 was a single heavy bar (4.2M sh, vwap $2.31); the book settled $2.17–2.24 by 08:15Z, and the fill came in above that on the Alpaca mark.
- MTEN held. No order placed. If a new SIP peak clears $1.81 (+30%), set trail at peak × 0.85. Time-limit exit at the 2026-10-08 PM pulse.

**Data notes:** IEX quotes for both names were stale (prior-day 20:46–20:54Z timestamps, BIYA bid $1.88, MTEN bid $1.00), and IEX returned no PM bars. Levels come from SIP 5Min bars (latest complete bar 08:15Z) and the Alpaca position mark. Both books were liquid at the PM open: BIYA 6.5K–29.5K trades per bar, MTEN 2.5K–18.5K. MTEN printed a spike and fade: $1.79 at 08:05Z, then $1.38 by 08:15Z on 1.0M shares. That fade is the risk for the 14:30 pulse.

## Position Evaluation — 14:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| MTEN | $1.39 | $1.32 mark / $1.20 bid | -5.0% mark, -13.7% bid | $1.79 (+28.8%) | 1 | B | SELL | Hard stop $1.18 (-15%) breached on SIP: low $1.12 at 11:30Z, 5Min closes $1.15–1.20 from 11:30Z to 12:15Z. Pulse-time bounce was fading. Filled $1.21 (-12.9%). |

**Actions taken:**

- SELL MTEN 70 @ limit $1.16 ext (id ad6671de) filled @ $1.21 at 12:31Z. -$12.60 (-12.9%). No open positions remain.

**Why sell above the stop line:** The Alpaca mark ($1.32) sat above the stop, but the verified SIP tape spent 45 minutes at or below $1.18 before the pulse (11:30Z bar L $1.12 / C $1.15 on 661K sh, 1987 trades). The mark came from a 12:21Z spike on IEX ($1.20 → $1.60 → $1.02 within two minutes, 181 trades) with no new SEC filing (EDGAR shows only the 10-06 6-K). The live bid fell from $1.29 to $1.20 in 36 seconds during the pulse. Stops do not execute in extended hours, so the pulse is the stop; holding to the 10-08 time limit would have meant carrying a breached Grade B stop through a regular session.

**Data notes:** The SIP 5Min feed lagged about 15 minutes (latest bar 12:15Z at 12:30Z), so the 12:20Z+ bars came from IEX 1Min. The Alpaca quote was live this pulse (12:30Z timestamps, 700 x 700). The PM shape: open spike to $1.79 (08:05Z), $1.41–1.55 range through 10:50Z, then a heavy break at 10:55–11:00Z (864K + 997K sh) to $1.20–1.27 and a second leg to $1.12 at 11:30Z. Yahoo's timeline matched the SIP shape.
