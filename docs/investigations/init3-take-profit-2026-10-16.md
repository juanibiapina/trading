# Initiative 3: resting take-profit replay (2026-10-16)

**Result: fails the frozen pass rule; no exit change.** Freeze: `docs/investigations/init3-take-profit-freeze.json` (13:35 UTC, before any bar was fetched). Script: `scripts/init3-take-profit-replay.py`. Output: `log/2026-10-16/init3-take-profit/result.json`.

## Question

Juan, Oct 15: "YYAI good entry, late exit." Would a sell limit placed right after each AH buy fill, resting through AH and premarket until the 04:30 ET sell-all, beat the 04:30 exit?

## Data

103 filled AH buy orders on the Alpaca paper account from 2026-06-25 to 2026-10-15. The baseline is the 04:30 ET SIP bid on the next trading day (2 rows used the first 04:00 bar open). A limit counts as filled at its price when a 1-minute SIP bar after the fill minute trades above it, through 20:00 ET or from 04:00 to 04:29 ET.

## Results

Baseline mean: **-1.05%** per trade.

| Limit | Fill rate | Mean return | Paired gain vs 04:30 | Interval (Bonferroni, 3) | Halves |
|---|---|---|---|---|---|
| +10% | 57% | +0.18% | +1.23 pts | [-3.90, +5.06] | +1.03 / +1.42 |
| +15% | 49% | +1.11% | +2.16 pts | [-2.68, +5.80] | +2.48 / +1.85 |
| +20% | 39% | +0.95% | +2.00 pts | [-3.20, +5.88] | +1.49 / +2.50 |

Every variant's mean gain is positive in both halves, but no lower bound clears zero, so none passes.

Fills since Oct 12: the limit rescues YYAI (04:30 -18.5%; AH high +23%) and AGMH (-3.6%; high +23%). It caps AEHL (+55.8% at 04:30) at the limit. BKYI, NCPL, TCRT and XXII never reach +10%, so the limit leaves them unchanged.

## Limits

Bar highs are trade prints, so the replay assumes a resting order fills when price trades above it; queue position and quoted size are ignored. The fills come from rules that changed over the period. With n=103 and fat tails (one AEHL is worth ~0.4 points of mean), the test can only detect gains of about 4 points or more. A larger replay on the 1,103 census events would need 18:30–20:00 ET and 04:00–04:30 ET 1-minute bars.
