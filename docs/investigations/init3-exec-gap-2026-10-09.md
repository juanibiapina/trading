# Initiative 3: where the realized-vs-modeled exit gap comes from (2026-10-09)

Log-only study. No order, live rule, size or pulse timing changed.

## Question

On the 89 real Alpaca AH entries, real exits return 2.45 points per trade less than a modeled market exit at the 04:30 ET bar open (`init3-limit-exit-2026-10-08.md`). Is that gap the spread we pay at the exit fill, or the time we choose to sell?

## Method

`scripts/init3-exec-gap.py` rebuilds each entry's exit fills from the archived Alpaca orders (`log/2026-10-06/init1-volume-policy/orders.json`, FIFO, the same pairing as `volume-entry-eval.py`) and fetches the last SIP quote at or before each fill into `log/2026-10-09/init3-exec-gap/sip-quotes/`. Per trade:

- **execution** = (fill price − NBBO mid at the fill) / entry price: spread and slippage.
- **timing** = (NBBO mid at the fill − 04:30 ET open) / entry price: when we sold.

The two parts add up exactly to realized − base0430. Realized returns match the archive for all 89 trades. `--replay` reproduces `result.json` byte for byte offline. All 89 trades have a usable quote; the median quote age is 2.5 s (9 are older than 60 s).

## Results (n=89, all measured)

| Exit group | n | Gap | Execution | Timing |
|---|---:|---:|---:|---:|
| All | 89 | -2.45 | -0.64 | -1.81 |
| Next premarket, sold 04:30–05:00 ET | 63 | +0.16 | -0.42 | +0.58 |
| Next premarket, held to the 08:30 ET pulse | 11 | -13.25 | -0.50 | -12.75 |
| Held to a later day | 15 | -5.47 | -1.66 | -3.81 |

Points per trade, means. Exit legs: median NBBO spread 0.71% of mid (mean 1.39%); fills land at the bid on average (0.01% above it, none below).

**Held trades.** The 26 trades the 04:30 ET evaluation chose to HOLD (the Grade A/B multi-session hold rules in `prompts/position-evaluation.md`) returned **-11.9%** against **-3.1%** had they been sold at the 04:30 open. Gap -8.77 points per trade, median -11.55, 21 of 26 worse, sign-flip p 0.038 (seed 7, 10,000 flips). Both chronological halves are negative (-12.74, -4.80); without the two best and two worst trades the gap is -10.89. The 11 same-morning holds were sold at the 08:30 ET pulse on a hard or trailing stop (GCTK -37.6%, PAPL -23.6%, DTSS -27.3%, DRMA -19.1%). The two big winners from holding (CHPT +50.9, VEEA +46.2 timing) do not offset the losers (DARE -39.9, TOPS -44.6, ONFO -28.3).

## Findings

1. **Timing explains three quarters of the gap and execution one quarter.** Spread and slippage cost 0.64 points per trade; paying the bid in a 0.7% median spread is what that looks like. Initiative 7's 12 bps base allowance is far below this, but those names are liquid megacaps.
2. **The hold decision is the loss.** Holds cost 2.22 points across all 89 trades; the 63 trades sold at 04:30 actually beat the modeled open by 0.58 points of timing.
3. **Selling every position at the 04:30 ET evaluation would have moved the realized mean from -3.2% to -1.0% per trade** (held trades priced at the 04:30 open plus their own execution cost). It does not make the core strategy profitable.
4. The decision is causal: the 04:30 ET evaluation already sees the 04:30 open when it decides to hold.

## Proposal (live rule, routed to Juan)

Retire the Grade A/B multi-session holds: sell every position at the first premarket evaluation (10:30 CEST / 04:30 ET). This edits holding rules in `prompts/position-evaluation.md` and `OPEN_POSITIONS.md`, so it is proposed through the daily email and the consolidated asks, not applied by `strategy-advance`.

## Limits

n=26 held trades; p 0.038 is one test, chosen after the October 8 study pointed at multi-day holds. Quotes are SIP NBBO; the paper account filled against IEX, so the execution term mixes spread and the IEX simulation. The counterfactual prices held trades at the 04:30 bar open, which omits the spread they would have paid at that time; their own execution term is added back.
