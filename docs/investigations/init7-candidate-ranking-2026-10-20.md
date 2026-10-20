# Initiative 7 — Ranking candidate families outside the micro-cap events (2026-10-20 18:00 CEST)

**Choice: small-cap monthly reversal (ranks 1001–3000, long-only) is tested first.** Among the three families, it is the only one that runs on this account with no borrow. The data is already cached, so it gives an answer in one run. Frozen in `docs/investigations/init7-smallcap-reversal-freeze.json` before any return was computed.

## Ranking

Scale: $100,000 paper equity, about 21 trading days a month. Expected value is the prior effect size, cut back by our own failed tests that overlap the family. These are planning estimates, not measurements.

| Rank | Family | Prior net edge | Expected $/day at $100k | Runs on Alpaca today | Data cost | Prior evidence against |
|---|---|---|---|---|---|---|
| 1 | **Small-cap monthly reversal** (buy last month's bottom decile of ranks 1001–3000, hold 1 month) | +0.3 to +0.8% a month over the small-cap basket after 50 bps; literature reversal profits are mostly in small caps, decaying after 2000 | about $15–40 over the basket | Yes, long-only, market-on-close orders | None (2016–2025 monthly bars cached, adjusted, include inactive symbols) | The megacap 20-session reversal failed point-in-time (Oct 12), and shorting liquid up movers failed out of sample (Oct 14). Both are a different universe and side. |
| 2 | Post-earnings drift in ranks 1001–3000 | +0 to +0.5% per event over 20–60 sessions; recent studies find drift mostly gone outside micro caps | about $5–25 | Yes, long side | High: SEC 8-K item 2.02 dates for about 2,000 issuers and daily bars outside the top 1,000 (hours of fetch) | Liquid AH movers (mostly earnings) *lagged* the market by 1–2 points over 20 sessions (Oct 13). That is the opposite sign of drift. |
| 3 | Hard-to-borrow short fade on the micro-cap events | +3.24% per trade before fees, but +1.25% under stress with the interval spanning zero; borrow fees on these names often run 50–300% a year | ±$0–200, sign unknown | **No.** Paper locates return 404, and the borrowable names do not fade (Oct 16, Oct 19). | Needs a broker with locates | Blocked by Juan's Sep 22 deferral of the broker test |

**Passive comparator:** holding QQQ returned about 18% a year from 2016 to 2025. That is about $70 a trading day on $100k, more than any active estimate above. Every family must beat this comparator to justify replacing it, and so far nothing has. The stop-or-replace ask to Juan now includes this comparator.

## Why small-cap reversal first

- It is the only family with a positive expected value that can run on this account today, needing neither borrow nor new data.
- It is cheap to settle: one offline run on cached data, with a frozen pass rule.
- It also covers capacity: ranks 1001–3000 trade roughly $5M–$50M a day, so a $100k book is far below 1% of daily volume.

## What it cannot show

- Monthly closes only: the signal uses the same close the order would fill at. A market-on-close order must be sent by 15:50 ET, so the live signal would be 10 minutes stale.
- The 2016–2025 window overlaps the literature that motivates it. A pass leads to a 2025-10 – 2026-09 holdout on newly fetched adjusted bars before any shadow pilot.
- Delisted names have no exit bar; they are scored at -30% in both the portfolio and the benchmark.
