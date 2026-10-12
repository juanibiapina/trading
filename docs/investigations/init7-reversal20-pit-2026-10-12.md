# Initiative 7: 20-session reversal on a point-in-time basket (2026-10-12 18:00)

## Result

The frozen 20-session reversal rule **fails** once the basket is chosen point in time. It still beats QQQ, but most of that comes from holding the basket. The pick's edge over the basket is not significant and is zero in the second half. Per the freeze, the megacap reversal candidate is dropped and Initiative 7 moves to a different universe.

| Series, bps per 20 sessions | Mean (97 non-overlapping trades) | Block-20 bootstrap interval (overlapping) | Halves | Offsets positive | Pass |
|---|---|---|---|---|---|
| Pick minus QQQ | +175 | [+2, +338] | +270 / +82 | 20 of 20 | yes |
| Pick minus point-in-time basket | +91 | [-56, +224] | +183 / -0 | 18 of 20 | **no** |
| Basket minus QQQ (no selection) | +89 | — | — | — | — |

With the hindsight basket (15:00 run) the pick beat QQQ by +181 and the basket by +82 [-54, +208]. Removing hindsight barely changes the numbers, so survivorship was smaller than feared. The selection edge still fails on its own: its lower bound is below zero and the 2021–2025 half contributes nothing. TSLA is 27 of 97 picks. By year, excess over QQQ ranges from -413 bps (2024) to +1,007 bps (2020).

## Method

- **Freeze:** `docs/investigations/init7-reversal20-pit-freeze.json`, written before any broad-universe data was fetched. Only the basket changes; the signal, selection, hold, benchmark, prices and window follow `init7-reversal20-freeze.json`.
- **Universe:** 8,092 symbols. These are Alpaca active and inactive NASDAQ/NYSE/AMEX stocks with fund names excluded, plus every S&P 500 member since 2016 from fja05680/sp500. The S&P list adds delisted names that Alpaca's asset list omits, such as TWTR, ATVI and SIVB. 7,262 symbols returned monthly SIP bars.
- **Basket:** each month, the 7 names with the highest SIP vwap × volume over the prior three complete months. 20 names entered at least once: AAPL (100% of days), AMZN, GOOGL (96%), MSFT (83%), TSLA (74%), META (72%), NVDA (67%), BABA (31%), AMD (27%), NFLX (21%), and BA, BAC, PLTR, NIO, BRK.B, PG, SMCI, MSTR, MRNA, ROKU (under 8% each). Today's seven fill 84% of slots. No basket name delisted during a hold, and no slot was dropped for missing bars.
- **Deviations forced by data:** Alpaca SIP history starts in January 2016, so decisions begin in April 2016, the first month with three complete prior months. FB and META report the same volume with different dividend adjustment, so duplicate bars are matched on volume alone and the longer history (META) is kept.

## What it means for the money

- The megacap lane offers no selection edge. Its one positive result is that an equal-weight top-7 dollar-volume basket, chosen point in time, beat QQQ by 89 bps per 20 sessions (about 11% a year) over 2016–2025. That is a passive tilt in one regime. It is slow money and not an agent strategy, so it is recorded and not pursued.
- Next universe: liquid names that make large after-hours moves, chiefly on earnings. The AH→PM pattern stays, but books are executable and moves (several percent) dwarf the ~13 bps cost. The first step is a census using only SIP 5-minute bars: among the top ~1,000 names by dollar volume, find AH ignitions (16:00–17:00 ET move and volume spike) and measure the return to the next premarket, open and close after costs.

## Reproduce

```bash
python3 scripts/init7-reversal20-pit.py --out log/2026-10-12/init7-reversal20-pit --replay
```

Cached inputs (`universe.json.gz`, `monthly.json.gz`, `daily.json.gz`) and `result.json` are in `log/2026-10-12/init7-reversal20-pit/`. The live fetch took 17 minutes.
