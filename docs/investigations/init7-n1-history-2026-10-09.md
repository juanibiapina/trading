# Initiative 7: the frozen N1 rule over the past year (2026-10-09)

## Result

The frozen N1 hourly relative-strength rule loses money after costs on every past 20-session window. Over 255 full sessions (2025-10-01 to 2026-10-08) it made **+$0.083 per session per $100 before costs** and **-$0.61 after the frozen base costs** (-$2.65 under stress). It trades 5.5 round trips a session, so it needs a cost below **0.76 bps per side** to break even. Half the median NBBO spread alone is 0.65 bps. **0 of 48** rolling 20-session windows pass the frozen promotion gate against cash and QQQ.

The 20-session pilot planned for October 14 would almost certainly end in rejection. It should not start in this form.

## Method

`scripts/init7-n1-history.py` replays `init7-comparison-v1`'s N1 selector on raw SIP 5-minute bars for the eight basket symbols. It uses the same required bars as `init7-comparison-features.py`: at each slot, the seven closes ending at the last complete bar before the 16-minute delay cutoff (for 11:30 ET, the bars starting 10:35 to 11:05). Fills are the open of the 5-minute bar that starts at the slot (a mid proxy); exits are at the next slot's bar open, or the 15:55 bar open at the flatten. Each fill pays half the median NBBO spread from amendment A3 (0.645 bps) plus the frozen slippage and fee: 6.645 bps per side base, 26.645 stress. QQQ enters at the 10:30 open and exits at 15:55 under the same costs. Two half-days were excluded; no session had missing bars.

**Check against live decisions:** the replay picks the same ticker as the live `init7-observe.py` decision on all 12 slots of October 7 and October 8 (AMZN ×3, AAPL ×2, TSLA; NVDA, GOOGL, TSLA, AAPL ×3).

## Numbers per $100 starting capital

| Scenario | N1 mean per session | N1 total, 255 sessions | Positive sessions | N1 minus QQQ per session | 95% bootstrap interval vs cash |
|---|---|---|---|---|---|
| Zero cost | +$0.083 | +$21.11 | 136 | +$0.084 | -$0.067 to +$0.231 |
| Base (6.645 bps/side) | -$0.607 | -$154.84 | 66 | -$0.480 | -$0.759 to -$0.461 |
| Stress (26.645 bps/side) | -$2.655 | -$676.93 | 5 | -$2.149 | -$2.805 to -$2.508 |

N1 selected a ticker in 1,397 of 1,530 observations (91%). TSLA was picked most (317), MSFT least (122). Holding through a repeated pick would save 200 of 1,397 round trips (14%), which does not close the gap.

## What this means

- The gross signal is about zero: its interval includes zero even before costs.
- Hourly rotation through seven megacaps cannot clear any realistic friction. The edge per trade must be roughly 15–20 times larger to cover the base allowance.
- The Jev arms (A1, A2) add nothing here: they follow N1 or hold cash, and the October 6 census found a usable 8-K in 1.7% of slots.

## Limits

This is off-schedule development evidence on bars, not prospective quote-based fills. It tested only the frozen rule; no variant was searched or tuned, so it carries no selection bias. The bar open approximates the mid at the slot; prospective fills use the NBBO quote at the post-decision capture.

## Evidence

- `log/2026-10-09/init7-n1-history/result.json` (summary), `sessions.json` (per-session picks and P&L), `bars.json.gz` (cached SIP bars and calendar, 173 pages, fetched 16:05 UTC).
- Replay without network: `python3 scripts/init7-n1-history.py --out log/2026-10-09/init7-n1-history --replay` reproduces `result.json` byte for byte.
