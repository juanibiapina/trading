# Initiative 1 sparse-slot policy and volume gates on 89 real entries — 2026-10-06

## Summary

The sparse-baseline question is resolved with `sip-ah-volume-v2`, an opt-in version of the shared metric. INLF's ignition, which v1 reported as unknown, measures **6,232x locally and 1,726x the prior evening's peak bar**. GIPR's prior session becomes fully covered.

Measured on all 89 Alpaca paper AH entries (June 25 – September 21), **no volume gate separates winners from losers.** Each tested gate admits a group that still loses money. The pass/fail return gaps have permutation p-values of 0.60–0.997. Juan's 10x local rule would have admitted 57 entries at −2.1% mean (−$120) and rejected 32 at −5.2% (−$154). The two medians are almost equal (−7.7% and −8.0%), and the gap is within chance (p = 0.60).

All 89 entries together: 28 wins, mean **−3.2%**, median **−7.7%**, standard deviation 25.7%, **−$274.81**. A normal 95% interval for the mean is about −8.5% to +2.1%. The core AH→PM entries have not shown positive expectancy, and volume selection does not change that on this sample.

## Policy v2

`python3 scripts/volume_metric.py ... --metric-version sip-ah-volume-v2`. v1 stays the default, and the live log-only scan path is unchanged. v1 output on the archived YFOR, INLF and GIPR inputs is byte-identical after the refactor.

- **Absent slots inside the returned span are zero-trade intervals.** Alpaca emits a bar only for an interval with trades. A missing slot counts as zero when it falls at or after the request start and before the latest bar already closed by `as_of`. Data lag can only truncate the tail, so slots after that bar stay unknown. A source without a recorded request start begins its span at the first returned bar.
- **Round-lot floor.** Local baselines and the prior peak are floored at 100 shares (`floored` status). A 623,155-share bar after zero-trade slots is a spike; a 300-share bar after zeros is 3x, not infinite.
- **Prior coverage.** With inferred zeros, the prior AH session is complete whenever a current-session bar is visible. The v1 observed-only peak is still a lower bound, so a ratio below 1 against it was already conclusive.
- The previous **trading** date and normal 16:00 closes come from the Alpaca calendar. All 89 entry dates and their prior sessions were normal.

| Control | Bar | Shares | v2 local | v2 / prior AH peak | Juan's label |
|---|---|---:|---:|---:|---|
| INLF Sep 24 | 16:30 ignition | 623,155 | 6,231.6x (floored) | 1,726.2x (prior peak 361) | wanted |
| GIPR Sep 3 | 16:40 ignition | 679,473 | 13.6x | 0.75x (prior peak 905,954; 45 observed + 3 inferred zero) | rejected |
| GIPR Sep 3 | 16:55 session peak | 1,817,888 | 2.0x | 2.0x | rejected |
| YFOR Sep 16 | 17:20 entry bar | 941,842 | 25.5x | 0.53x | rejected |

## Outcome test

`scripts/volume-entry-eval.py` pages every Alpaca order since June 1 and pairs each AH buy fill with later sells, first in first out. All 91 buys pair fully. Two 09:01 ET VTAK test lots (−$1.53) are excluded, and the 89 AH lots total −$274.81. Together that is within $1.76 of the account's −$278.10. Each entry is measured on bars closed **15 minutes before its fill**, the free-SIP delay, so every value was available at decision time. Ratios use the session-to-date maximum bar.

| Gate (first four declared before results) | Pass n / mean / median / $ | Fail n / mean / median / $ | Permutation p |
|---|---|---|---:|
| Session peak ≥ 1x prior AH peak | 86 / −3.2% / −8.4% / −$265.72 | 3 / −3.1% / −4.6% / −$9.09 | 0.997 |
| ≥ 3x prior AH peak | 84 / −2.9% / −8.4% / −$235.96 | 5 / −8.2% / −6.4% / −$38.86 | 0.611 |
| ≥ 10x prior AH peak | 78 / −3.1% / −8.4% / −$234.12 | 11 / −3.9% / −7.4% / −$40.70 | 0.929 |
| Max local ratio ≥ 10x (Juan's rule) | 57 / −2.1% / −7.7% / −$120.43 | 32 / −5.2% / −8.0% / −$154.38 | 0.605 |
| AH peak ≥ 1x same-day regular max bar (secondary) | 75 / −2.8% / −8.2% / −$195.73 | 14 / −5.5% / −6.0% / −$79.08 | 0.717 |
| AH peak ≥ 3x same-day regular max bar (secondary) | 68 / −3.8% / −8.4% / −$243.39 | 21 / −1.3% / −7.7% / −$31.43 | 0.704 |

The permutation test shuffles returns between pass and fail groups (seed 7, 10,000 draws, two-sided on the mean gap). The two regular-session gates were added after the first four results. They test the baseline Juan's GELS and DAIC remarks describe, and their directions disagree between thresholds.

**Juan's labels.** The prior-AH baseline flags 3 of his 10 entered rejections: BOOM 1.6x, GIPR 2.0x, YFOR 0.5x. Most entries were first-day news movers with near-silent previous evenings, so GELS (13,056x), UFG (18,295x) and SUNE (897x) pass easily. The same-day regular-session baseline flags GELS 0.43x, GIPR 0.39x and GRSD 0.79x. Together the two baselines flag 5 of 10: BOOM, GIPR, YFOR, GELS and GRSD. ONMD, TLYS, UFG, SUNE and CHPT pass both; Juan rejected some of them on other grounds, such as SUNE's single-bar pop. WLDS, which he praised, passes both and lost 19.4%. CHPT, which he rejected, returned +50.1%.

## Decision

- **Policy:** v2 resolves the sparse-baseline and prior-coverage question. Absence before a later visible bar is zero trades, and ratios use the round-lot floor.
- **Gate:** none of the six volume gates is promoted, since none shows an edge on 89 real entries. This includes the 10x local rule and both cross-session baselines. The measurement stays log-only.
- **Strategy:** the losses are spread across every volume profile, so volume selection is not the lever that makes the AH→PM entries profitable. This adds weight to Initiative 7's executable-universe research and to the existing liquid-session proposal in the daily email.

## Limits

- 89 entries is a small sample with heavy tails: BAOS +148.9%, DARE −51.2%, TOPS −50.0%. The test can miss a modest edge, and it says nothing about names the scanner never entered (INLF Sep 24, OLOX Oct 5).
- Entries were already filtered by the scanner, so these gates were tested only on names that passed the existing rules.
- Absent-slot inference assumes Alpaca omits only intervals without qualifying trades. Intervals containing only bar-excluded trades also read as zero.
- Fill timing uses the actual fill; the scan that decided each entry may have seen slightly earlier data.

## Reproduce

```bash
python3 scripts/volume_metric.py INLF 2026-09-24 --prior-date 2026-09-23 \
  --as-of 2026-09-24T17:30:00-04:00 --input log/2026-10-01/INLF-volume-sip.json \
  --metric-version sip-ah-volume-v2
python3 scripts/volume-entry-eval.py log/2026-10-06/init1-volume-policy --replay
```

The archive `log/2026-10-06/init1-volume-policy/` holds the reduced fills (`orders.json`), the calendar, 89 SIP inputs and `result.json`. The replay reproduced the network run's rows exactly.
