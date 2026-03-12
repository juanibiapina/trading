# Scanner & Process Changelog

This file tracks all automated changes made to the scanning system. It is read and updated by the daily improvement cycle.

## How to Read This Log

Each entry documents:
- **Context**: What happened in recent scans that prompted the change
- **Changes**: Exactly what was modified, in which files, and why
- **Hypothesis**: What we expect to improve
- **Evaluation**: Assessment of whether previous changes helped (added in subsequent entries)

## Current Scanner Parameters

```
MIN_PRICE = 0.5
MAX_PRICE = 10.0
MAX_MARKET_CAP = 100,000,000 ($100M)
MIN_AH_VOLUME = 50,000
MIN_AH_CHANGE = 5%
MIN_PM_VOLUME = 50,000
MIN_PM_CHANGE = 5%
MIN_INTRADAY_RVOL = 10
MIN_5M_VOLUME = 5,000
```

## Current Process

- 7 evening scans every 30 min (21:30–01:30 CET)
- 2 morning evaluations (10:05, 10:20 CET)
- Paper trades with ~€100 positions
- Biotech/pharma preferred (non-biotech historically 0% win rate)
- Entry rules: <50% above close, float <10M, catalyst required, first day of unusual volume

## Modifiable Files

- `scripts/scan.py` — Scanner parameters, filters, output columns
- `scripts/check-prices.py` — Price checking utility
- `prompts/post-market-scan.md` — Evening scan prompt (evaluation criteria, log format)
- `prompts/morning-evaluation.md` — Morning evaluation prompt

## Change Log

_(entries are prepended — newest first)_

### 2026-03-12 — Complete Day% Integration in Post-Market Prompt

**Context:** The March 11 scanner change added Day% to the terminal output, but the post-market scan prompt template (`prompts/post-market-scan.md`) still used the old AH table format without Day%. Result: the March 11 evening log tables don't include Day% — the agent followed the prompt template and omitted the column. The fix from March 11 was therefore not reaching the actual trade evaluations.

**Evaluation of previous changes:**
- Day% column (2026-03-11): **Partially effective.** Scanner terminal output includes Day%, but the prompt template wasn't updated. The March 11 evening logs show AH tables without Day%. No stocks triggered the 50% rule that night (SXTP was already +71% from close alone), so the gap didn't cause a missed filter — but the data still wasn't surfaced. Fixing the prompt completes this change.
- Initial setup (2026-03-10): Scanner coverage remains strong at 86% (5/7 PM movers caught on March 11). Paper trading: 1 win (+18.3%, March 10), 1 loss (-29.5%, March 9), 0 trades March 11. Sector discipline and 50% rule continue to prevent losses — all 3 skip decisions on March 11 were correct (SXTP, ACXP, TLYS all faded).

**Changes:**
1. **prompts/post-market-scan.md** — Added Day% column to the AH table format template and added "(for AH scans, check Day% + AH Chg% = total move from previous close)" to the 50% rule entry criterion
   - Why: Scanner outputs Day% since March 11 but the prompt template still showed the old format. The agent follows the template, so Day% was lost in logging. This was the exact gap that caused the March 9 ACXP loss — the total move (+113% from Friday) was hidden.
   - Hypothesis: With Day% in the prompt template, the agent will consistently include it in AH log tables and use it when evaluating the 50% rule. Measurable: next AH scan log should include a Day% column. Next stock with Day% > 20% should have the total move (Day% + AH%) explicitly checked against the 50% threshold.

### 2026-03-11 — Add Day% Column to After-Hours Scanner

**Context:** ACXP on March 9 appeared as +47% from same-day close but was actually +113% from Friday's close (regular session had already moved +45%). Paper trade entered at $2.88 and lost -29.5%. The scanner had no way to show the regular session move, hiding the true extent of the multi-day run.

**Evaluation of previous changes:**
- Initial setup (2026-03-10): Scanner coverage is strong at 86-89% across 3 evaluated nights. Paper trading produced 1 loss (-29.5%, entry at AH peak of multi-day runner) and 1 win (+18.3%, entry at close price). Known Issue #1 (multi-day moves) was the direct cause of the loss. Addressing it now.

**Changes:**
1. **scripts/scan.py** — Added `"change"` column to `COLUMNS_AFTERHOURS` and display it as "Day%" in the AH output table
   - Why: The March 9 ACXP loss was caused by not seeing the +45% regular session move. The stock looked like +47% AH (under the 50% rule) but was +113% from previous close (well over it).
   - Hypothesis: With the Day% column visible, the agent will skip AH candidates where Day% + AH% exceeds the 50% entry threshold. I expect this to prevent entries on multi-day runners. Measurable: next time a stock with Day% > 20% appears, the agent should factor it into the entry decision.

**Updated parameters:** No threshold changes. New output column only.

### 2026-03-10 — Initial Setup

**Context:** System deployed. First night of 30-min scanning ran successfully. 19 tickers found across 7 scans. One paper trade (ACXP) entered at AH peak, lost -29.5%.

**Known Issues:**
1. Scanner only shows change from same-day close — misses multi-day moves (ACXP was +113% from Friday, appeared as +47%)
2. No bearish divergence detection (volume up + price down = distribution)
3. Tier B catalysts (FDA-adjacent) are 0/2 — may need downgrade
4. All AH movers faded overnight on 2026-03-09 — need more data to assess if this is typical

**Baseline Metrics:**
- Scanner catch rate: 86% (6/7 PM movers found in evening scans)
- Paper trade P&L: -€27 (1 trade)
- False positive rate: high (19 tickers found, only 1 remotely actionable)
