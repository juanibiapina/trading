# Initiative 7: liquid after-hours movers census (2026-10-13)

**Result: the AH→PM continuation has no edge in liquid names over the past year, before or after costs.** The frozen test fails at all three exits. The candidate is dropped.

- Freeze: `docs/investigations/init7-liquid-ah-census-freeze.json` (written before any fetch)
- Script: `scripts/init7-liquid-ah-census.py` (live fetch about 55 minutes; `--replay` reproduces the result from cache)
- Evidence: `log/2026-10-13/init7-liquid-ah-census/result.json`, `events.json.gz` and the cached bars and quotes

## What was tested

For each full trading day from 2025-10-01 to 2026-09-30 (249 AH dates), the universe is the point-in-time top 1,000 names by SIP dollar volume over the prior three months (1,251 distinct names). An ignition is a move of at least 3% from the official close to the last 5-minute bar by 16:55 ET, with 16:05–16:55 volume at least 3× its 20-session median and at least $1M traded. The long trade buys at the SIP NBBO ask at 17:00 ET and sells at one of three exits on the next day:

- the NBBO bid at 04:30 ET
- the official open minus 5 bps
- the official close minus 5 bps

There were 783 long and 637 short ignitions. 61 lacked a valid 17:00 quote and 1 lacked a next-day bar, leaving 743 long trades. No split fell inside a hold.

## Results (long, per trade, 98.33% interval by AH date)

| Exit | Net mean | Interval | Halves | Win rate | Gross at mid |
|---|---|---|---|---|---|
| 04:30 bid | -1.41% | [-2.06, -0.88] | -1.22 / -1.60 | 33% | +0.13% [-0.29, +0.51] |
| 09:30 open | -0.34% | [-0.90, +0.18] | -0.54 / -0.13 | 45% | +0.09% [-0.47, +0.59] |
| Close | -1.29% | [-2.67, -0.16] | -1.28 / -1.31 | 39% | -0.87% [-2.26, +0.27] |

- **No drift to capture.** Measured from the 17:00 mid, the next open is +0.09% on average, and the interval spans zero. In liquid names the after-hours move is fully priced by 17:00. Holding through the next session gives back almost 1%.
- **Costs dominate.** The median 17:00 spread is 43 bps (quartiles 20 and 89). The 04:30 book is thin: selling at the 04:30 bid costs 1.5 points per trade on average, against 0.4 points at the open.
- **The fade fails too.** Shorting the down movers (descriptive only) loses at every exit: -2.5% at 04:30, -1.0% at the open, -1.7% at the close.
- **Move size does not rescue it.** Moves of 3–6% and 6–10% lose at every exit. Moves above 10% show +0.39% net at the open, but the interval is [-0.74, +1.48] and the first half is negative (n=173). The 192 trades with an entry spread of 20 bps or less net +0.07% at the open. Both are descriptive and cannot rescue a failed frozen test.

## Decision

The liquid AH-mover candidate is dropped. With the megacap rotation and the 20-session reversal, this is the third Initiative 7 candidate rejected on frozen tests. The next step tests whether the drift appears over days instead of hours. The open below is the first regular-session price after the event. Buying there and holding 5 or 20 sessions avoids the extended-hours spread and is the documented post-earnings drift setup. The 1,420 cached events supply the event list; the test needs only daily bars.
