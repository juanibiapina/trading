# Initiative 3: resting sell-limit exit on 89 real entries (2026-10-08)

Log-only study. No order, live rule, size or pulse timing changed.

## Question

Does the standing exit proposal (rest a sell-limit +10% above the 04:30 ET price, fall back to the last premarket close) beat a plain 04:30 ET market exit on every real Alpaca AH entry? The September 23 result (+3.0% per name, n=44) measured gain against our own exit, on a hand-picked list.

## Method

`scripts/init3-limit-exit-eval.py` reads the 89 closed AH entries archived by `volume-entry-eval.py` (`log/2026-10-06/init1-volume-policy/`), fetches each entry's next-session 5-minute SIP premarket (04:00–09:30 ET) into `log/2026-10-08/init3-limit-exit/sip-pm/`, and scores each rule as a return on the real entry price. `--replay` reproduces `result.json` byte for byte offline.

- `base0430`: sell at the open of the first bar at or after 04:30 ET.
- `exitL<k>`: the standing proposal at k = 5/10/15/20%.
- `entryL<k>`: a sell-limit k% above the entry price, resting from the first bar after the fill through the evening and premarket; fallback is `base0430`.
- `V` variants fill only when the bar's VWAP reaches the limit, a check against thin prints that touch a 5-minute high without real size.
- Paired sign-flip test against `base0430`, seed 7, 10,000 flips.

## Results (n=89, all measured)

| Rule | Mean | Median | Wins | Filled | Diff vs base0430 | p |
|---|---:|---:|---:|---:|---:|---:|
| Realized (real exits) | -3.2% | -7.7% | 28 | — | -2.45 pts | 0.06 |
| base0430 | -0.8% | -4.3% | 29 | — | — | — |
| exitL10 (standing proposal) | -0.8% | -2.2% | 38 | 46 | -0.08 pts | 0.97 |
| exitL5 | +0.1% | -2.9% | 39 | 65 | +0.89 pts | 0.39 |
| entryL10 | +2.2% | +10.0% | 59 | 58 (39 in AH) | +2.99 pts | 0.19 |
| entryL15 | +3.3% | +15.0% | 51 | 49 (26 in AH) | +4.09 pts | 0.049 |
| entryV15 (VWAP fill) | 0.0% | -1.5% | 39 | 34 | +0.73 pts | 0.80 |
| entryV10 (VWAP fill) | +0.1% | +10.0% | 49 | 46 | +0.89 pts | 0.75 |

Chronological halves for entryL15: +5.6% then +1.1%. Without its top two names (IVF, ALZN) it is +3.1%.

## Findings

1. **The standing +10% exit proposal does not hold on the full sample.** It adds -0.08 points per trade over a plain 04:30 exit. It is withdrawn as a live-exit proposal.
2. **An entry-anchored resting limit is the only rule with a positive tail-robust mean**, but it fails the conservative check. With touch fills, +15% gives +3.3% per trade (p 0.049, the best of 16 rules tested, so not significant after the multiple tests). With VWAP fills it drops to 0.0%. About half its fills come from evening AH bars, where thin prints touch highs. The second chronological half is +1.1%.
3. **Real execution costs about 2.5 points per trade against a modeled 04:30 open.** The 74 trades exited next premarket lose 1.8 points on average (median -0.2) against the 04:30 open. The 15 trades held past the next morning lose **5.5 points** on average (median -7.9).
4. **No exit rule makes the core strategy clearly profitable.** The best conservative variant is about breakeven before spread, which strengthens the Initiative 7 liquid-session proposal.

## Limits

5-minute bars cannot show whether a touch would have filled our order. Bar opens omit the spread for the baseline. Alpaca extended-hours orders are DAY limit orders, so a resting AH limit must be re-placed for the premarket session. The paper account fills against IEX, so a paper test of AH limits would not measure SIP touches.

## Initiative 1 check (same run)

All 24 October 7 volume-metric files are `sip-ah-volume-v2` (331 rows: 254 `ok`, 59 `warmup`, 18 `floored`). The local report renders 24 sections and 331 rows, and the published page (Pages run 37778868698, success) is byte-identical to the local build.
