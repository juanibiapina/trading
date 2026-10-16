# Initiative 7: can the micro-cap short fade be executed on Alpaca? (2026-10-16 18:00 CEST)

Written while the prior-year fetch for the frozen short-fade test (gob `KaJ`) runs. This note fixes, before any prior-year result exists, which frozen cell counts as executable. It does not change the freeze (`init7-microcap-short-fade-freeze.json`).

## Broker facts (checked 2026-10-16)

| Question | Answer | Source |
|---|---|---|
| Can a short be opened in extended hours? | Yes. "Short selling is also treated the same" in pre-market and after-hours; extended-hours orders must be limit, `day` or `gtc`. | docs.alpaca.markets/us/docs/orders-at-alpaca |
| ETB borrow cost | $0 locate and $0 borrow fee for Trading API users. The freeze charges 25 bps per night, which is conservative for ETB. | docs.alpaca.markets/us/docs/margin-and-short-selling |
| HTB names | Need a paid locate (round lots of 100, single use, non-refundable) plus a daily borrow fee at the stock's HTB rate, charged on round lots, 3 days over a weekend. | same page |
| Paper account `PA37U2Y192A7` | `shorting_enabled: true`, `no_shorting: false`, multiplier 4. | `GET /v2/account`, `/v2/account/configurations` |
| Locate API on paper | `GET /v1/locates/quotes` and `GET /v1/locates` return 404 on `paper-api.alpaca.markets`. HTB shorts cannot be opened or priced on paper. | live call |
| Recent live entries | YYAI, AGMH, AEHL, NCPL, TCRT, XXII, FCHL, BKYI, CIGL, DKI: all `shortable: false`, `easy_to_borrow: false` today (TSLA control: both true). | `GET /v2/assets/{sym}` |

## Decision rule fixed before the result

- **On Alpaca paper, only the `etb` cells are executable.** A pass in `all/exit_open` alone shows the fade exists but is not a tradable strategy on this account. It becomes tradable only with HTB access (a live Alpaca account with locates, or another broker), priced with real locate and borrow quotes. That ties it to Initiative 2, which Juan deferred on September 22.
- The `etb` flag is today's flag applied to past events. Names that collapsed may have lost ETB status since, so the cell's composition carries look-ahead in an unknown direction.

## In-sample split by move size (descriptive; the October 15 caches chose the test, so not evidence)

1,103 events, mean net return of the short at each cover:

| AH move at scan | n | ETB share | ETB, open cover | not ETB, open cover | ETB, 04:30 | not ETB, 04:30 |
|---|---|---|---|---|---|---|
| 10–25% | 644 | 23% | -0.68% | -0.01% | -0.66% | -2.24% |
| 25–50% | 314 | 14% | +4.74% | +5.00% | +6.54% | +2.37% |
| 50–150% | 145 | 6% | +5.91% | +9.84% | +2.94% | +3.05% |

The fade lives in moves of 25% or more, and those are the names least likely to be ETB: about 53 ETB events a year (about one a week) out of 459. The ten real live entries above, all large moves, are none of them shortable.

## Money-fast reading

If the prior year confirms the in-sample shape, the Alpaca-executable flow is about one ETB short a week. At ~$100 per trade (learning-phase size) and +5% that is about $5 a week; at the account's full overnight buying power it is capped by the thin ETB book in these names. The larger flow (about 400 non-ETB events a year) needs HTB locates, whose fee for a sub-$5 micro-cap can match the edge: a $0.05 locate on a $2 stock is 2.5% before any daily borrow fee. Any proposal from this lane must therefore price real locate quotes, which needs a live account.
