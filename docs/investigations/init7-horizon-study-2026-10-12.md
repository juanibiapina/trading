# Initiative 7 horizon study and 20-session reversal test — 2026-10-12

## Question

N1's hourly rotation in the seven megacaps loses after costs (2026-10-09). Does any holding
horizon in this basket move enough per trade to clear the frozen base cost of 13.29 bps per round
trip (2 × 6.645 bps: 4 bps slippage + 2 bps fee + half the 1.29 bps median NBBO spread per side)?

## Method

`scripts/init7-horizon-study.py` reads the SIP 5-minute bars cached by `init7-n1-history.py`
(255 full sessions, 2025-10-01 to 2026-10-08) and measures gross return per trade, with fills at the
bar open at each entry and exit stamp:

- **momentum:** N1's selector (best return relative to QQQ over a lookback equal to the horizon)
- **reversal:** its mirror (worst relative return, bought only if its own and relative returns are negative)
- **basket / qqq:** equal-weight seven names, and QQQ alone
- **abs_move:** mean absolute single-name move, the ceiling for any selection edge

Horizons: 1 hour at N1's slots, 10:30 to the close, overnight, and 1, 5 and 20 sessions close to
close. Intervals are moving-block bootstraps with block = horizon in sessions.

## Result 1: no intraday or overnight horizon clears the hurdle

| Horizon | Momentum gross | Momentum − QQQ | Reversal − QQQ | Mean abs move |
|---|---:|---:|---:|---:|
| 1 hour | +2.3 bps [-0.6, 5.6] | +2.3 | +1.0 | 35 |
| 10:30 → close | -1.1 | -0.9 | +0.9 | 86 |
| Overnight | +5.1 | -1.2 | +3.2 | 92 |
| 1 session | -7.3 | -16.6 | +3.6 | 164 |
| 5 sessions | -25.6 | -75.2 | +27.7 [-68, 110] | 384 |
| 20 sessions | -125 | -296 [-629, -72] | **+305 [63, 602]** | 742 |

Hourly momentum makes +2.3 bps a trade against a 13.3 bps hurdle, matching the N1 replay. Price
moves are big enough at every horizon (35 bps an hour), but no selector captures enough of them.
Momentum gets worse as horizons lengthen; reversal improves. Only 20-session reversal clears the
hurdle with an interval above it. That is 1 of 12 selector/horizon variants, on about 10
independent trades, so it is a hypothesis.

## Result 2: 20-session reversal passes its frozen out-of-sample test, but the selection edge is not significant

The rule and pass criterion were frozen in `docs/investigations/init7-reversal20-freeze.json`
before any data older than 2025-10-01 was fetched. `scripts/init7-reversal20-oos.py` replays it on
adjusted daily SIP bars, 2016-01-04 to 2025-09-30 (2,450 sessions, all eight symbols complete).

- **Frozen criterion: passed.** 92 non-overlapping trades (29 periods in cash): +342 bps gross,
  **+181 bps over QQQ** per 20 sessions, 49 of 92 positive. Overlapping excess +205 bps, block
  interval [+39, +357]. Halves +251 and +119. All 20 start offsets are positive (+75 to +318).
- **By year (offset 0):** 2016 -165, 2017 +723, 2018 +223, 2019 -206, 2020 +930, 2021 +390,
  2022 -8, 2023 +420, 2024 -251, 2025 +130.
- **Survivorship control (reported alongside the frozen criterion):** the basket is today's
  megacaps, chosen with hindsight. Holding all seven equally beats QQQ by **+131 bps per 20
  sessions** with no selection. The reversal pick beats that basket by only **+82 bps** (offset 0:
  +75), interval **[-54, +208]**, halves +72 and +91.
- TSLA is 37 of 92 picks, NVDA and META 15 each, MSFT 1.

About two thirds of the excess over QQQ comes from the hindsight basket. The remaining selection
edge has a consistent sign in both halves but is not distinguishable from zero.

## Decision

- **Intraday megacap rotation is rejected** at every horizon from 1 hour to overnight. The October
  14 pilot stays cancelled.
- **20-session reversal is not promoted.** Its selection edge needs a basket without hindsight
  before it counts. If it is real, +82 bps per 20 sessions is about 10% a year over the basket at
  one trade a month: positive and scalable, but slow.
- Next test: rebuild the basket point in time (top names by trailing dollar volume each month from
  a broad US list, including names that later shrank or delisted) and rerun the frozen rule.

## Reproduce

```bash
python3 scripts/init7-horizon-study.py --bars log/2026-10-09/init7-n1-history/bars.json.gz --out log/2026-10-12/init7-horizon-study
python3 scripts/init7-reversal20-oos.py --out log/2026-10-12/init7-reversal20-oos --replay
```
