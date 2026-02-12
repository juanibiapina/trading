# TradingView Scanner (Archived)

**Status:** Not useful - archived Feb 2026

This document contains information about using the TradingView Screener API that was previously part of the trading plan.

---

## Scanner Learnings (Feb 5, 2026)

**Key insight: `relative_volume_intraday` beats `relative_volume_10d_calc`.**
- `relative_volume_10d_calc|5` compares current 5m bar to the overall 10-day average 5m bar — useless because open/close bars skew the average, making normal mid-day bars look like spikes.
- `relative_volume_intraday|5` compares to what's typical *for this specific time of day* — much more accurate for detecting real unusual activity.

**Catalyst verification is critical.**
- Scanner finds volume spikes, but not all spikes are tradeable.
- No-news pumps (GDTC — Discord pump by "Grandmaster-Obi") spike and fade fast.
- Real catalysts (AIM — Phase 2 clinical data, CISS — ownership filing + fleet expansion, TRUG — product launch partnership) have more follow-through.
- Always check news before entering.

**Consider expanding beyond biotech.**
- CISS (shipping, 194K float) and TRUG (software/gaming) both had real catalysts and big moves.
- Ultra-low float (<500K) produces the most violent moves regardless of sector.
- Run scanner with `--all` flag, then filter by catalyst quality manually.

---

## Resources

- [After-Hours Gainers (TradingView)](https://www.tradingview.com/markets/stocks-usa/market-movers-after-hours-gainers/) - Shows stocks gaining in after-hours trading

---

## TradingView Screener API (Free)

Undocumented API for scanning the entire US stock market. No API key needed. Can filter by sector, market cap, float, volume, and extended hours data. Python package available: `pip install tradingview-screener`.

- [tradingview-screener PyPI](https://pypi.org/project/tradingview-screener/)
- [GitHub](https://github.com/shner-elmo/TradingView-Screener)
- [All available fields](https://shner-elmo.github.io/TradingView-Screener/fields/stocks.html)
- [Pre-built screeners](https://shner-elmo.github.io/TradingView-Screener/screeners/stocks/america.html) (includes `postmarket_gainers`, `premarket_gainers`, etc.)

**Key fields for our strategy:**

| Field | Description | Timeframes |
|-------|-------------|------------|
| `relative_volume_intraday\|5` | Volume vs same time-of-day average (5m) | Best for detecting unusual activity |
| `volume\|5` | Current 5-min bar volume | `\|1`, `\|5`, `\|15`, `\|30`, `\|60` |
| `volume_change\|5` | Volume change % from previous bar | Same timeframes |
| `average_volume_10d_calc\|5` | Average 5-min volume (10-day) | Same timeframes |
| `postmarket_volume` | Post-market volume | Daily only |
| `postmarket_change` | Post-market change % | Daily only |
| `premarket_volume` | Pre-market volume | Daily only |
| `premarket_change` | Pre-market change % | Daily only |
| `float_shares_outstanding` | Shares float | — |
| `market_cap_basic` | Market cap | — |
| `sector` | e.g., "Health Technology" | — |
| `industry` | e.g., "Biotechnology", "Pharmaceuticals: Major" | — |

**Biotech volume spike screener (during regular hours):**

```bash
curl -s -X POST "https://scanner.tradingview.com/america/scan" \
  -H "Content-Type: application/json" \
  -d '{
    "columns": ["name", "close", "volume|5", "average_volume_10d_calc|5", "relative_volume_10d_calc|5", "relative_volume_intraday|5", "volume_change|5", "change", "sector", "industry", "market_cap_basic"],
    "filter": [
      {"left": "relative_volume_intraday|5", "operation": "greater", "right": 10},
      {"left": "market_cap_basic", "operation": "in_range", "right": [0, 100000000]},
      {"left": "close", "operation": "in_range", "right": [0.5, 10]},
      {"left": "sector", "operation": "equal", "right": "Health Technology"},
      {"left": "volume|5", "operation": "greater", "right": 5000}
    ],
    "sort": {"sortBy": "relative_volume_intraday|5", "sortOrder": "desc"},
    "markets": ["america"],
    "symbols": {"query": {"types": ["stock"]}},
    "options": {"lang": "en"},
    "range": [0, 20]
  }'
```

**Key insight:** `relative_volume_intraday|5` compares the current 5-min bar to what's typical for that specific time of day (not the daily average). This avoids false positives from normal open/close volume spikes. Use `volume|5 > 5000` as absolute floor to filter out noise from ultra-thin stocks.

---

## Custom Scanner Script

Usage from trading plan:
- **Scanner:** Use custom TradingView screener script (`scripts/scan.py`) to detect volume spikes. Run with `--all` to scan all sectors, then verify catalyst manually.

Scripts in `scripts/` directory:
- `scan.py` - Main TradingView screener script
- `pm-volume-check.py` - Post-market volume checker
