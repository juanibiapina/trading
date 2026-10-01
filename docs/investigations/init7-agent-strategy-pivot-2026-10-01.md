# Initiative 7 — Alternative agent strategies at the October 1 checkpoint

## Decision

Open research into an agent-assisted strategy for liquid US stocks during regular hours. First verify data and executable quotes on a fixed small universe. Keep Initiative 6 as the sole pilot while this research proceeds.

A move to regular-session trading changes the session and universe in `Day Trading.md`. Route that proposal to Juan through the daily email. Today's deliverable is the source comparison and research decision; a live strategy switch is not supported yet.

## Account checkpoint

At the October 1 15:00 CEST strategy run, `node scripts/broker.js account` returned **$99,721.90**, down **$278.10 (0.2781%)** from $100,000. `positions --json` returned `[]`. The account has not met Juan's September 1 net-positive deadline, so his alternative-strategy research directive is now active.

The existing PM-only pilot has 26 retrospectively holdable admissions since July 13. Its modeled mean is +4.4% gross, approximately +2.4% after an assumed 2% spread. At €100 per admit that is approximately €2.40; quote freshness, causal discovery and actual fills remain unproved. More scanner detections alone do not establish faster account growth.

## Existing agent approaches checked online

Read October 1, 2026. Returns below are reported by the authors. None is a reproduced return on this account.

| Approach | Mechanism and original evidence | Practical limit | Research decision |
|---|---|---|---|
| [AI-Trader](https://arxiv.org/html/2512.10971v1), §§3–4 | A tool-using agent chooses buy/sell/hold with cash available. US evaluation uses Nasdaq-100 stocks at hourly cadence, October 1–November 7, 2025. MiniMax-M2 reports +9.56% cumulative return versus QQQ +1.87%; GPT-5 reports +1.56%. | A short window, model dependence and a different capital allocation. The inspected evaluation does not establish our spread, slippage, inference-cost or broker-fill assumptions. | Use its liquid universe and time-bounded observations as the cheapest first alternative to investigate. Do not copy its headline return into an expected-return forecast. |
| [TradingAgents](https://arxiv.org/html/2412.20138v1), workflow and simulation sections | Analysts, bull/bear researchers, trader, risk reviewers and fund manager debate structured reports. Historical simulation runs June 19–November 19, 2024, against buy-and-hold and technical baselines. | Several agent roles and repeated debates consume inference and execution time. Historical dates can be known to the model even when retrieval excludes future news. A cost-adjusted local reproduction is absent. | Park the full debate framework. Its evidence-verification step may be useful after a cheap baseline exists. |
| [FinAgent](https://arxiv.org/html/2402.18485v1), §5 and Table 4 | News, prices and charts feed memory, two reflection layers and a decision module. Five stocks plus ETH; training June 2022–June 2023, test June 2023–January 2024. TSLA's reported 92.27 figure is **ARR% in Table 4**, not a comparable cumulative account return. | Historical test, several reasoning/memory stages and unverified local execution costs. Our account has no reproduction of the claimed advantage. | Park the full memory framework; retain the idea of recording timestamped event evidence alongside numerical bars. |

Two evaluation studies change how these candidates should be tested:

- [Profit Mirage](https://arxiv.org/html/2510.07920v1), §2.1: with GPT-4o, moving the evaluated dates beyond the model's stated knowledge cutoff reduced the reported Sharpe across the tested methods by 51.48%–62.23%; TradingAgents fell 55.68%. This is a separate re-evaluation, not our result or proof that every agent fails.
- [What survives honest evaluation?](https://arxiv.org/html/2608.27734v1), abstract and §§3–6: the authors report rejecting every LLM-discovered strategy in their cost-aware experiments across two models and repeated searches. They record every tested candidate and separate design from held-out data. Their universes and daily horizons differ from our proposed intraday test; the useful mechanism is the complete trial record and separation of future outcomes from decisions.

A [Reddit example](https://www.reddit.com/r/deeplearning/comments/1o0w6io/trained_an_autonomous_trading_agent_up_132_this/) surfaced during the search claims both +1.32% and $100,000→$102,892.63, which imply different returns. Treat forum anecdotes as leads for verification. They provide no promotion evidence.

## Candidate to investigate first

**Hypothesis:** liquid regular-session stocks may produce more executable opportunities with lower trading friction and less discovery delay than the current extended-hours micro-cap universe. An agent can contribute by verifying fresh company events and choosing an action from a bounded set. Its incremental value must beat a numerical baseline after its operating costs.

Start the data feasibility check with **AAPL, MSFT, NVDA, AMZN, GOOGL, META, TSLA**, plus **QQQ** as a market comparator. This is a fixed prospective convenience basket, not a historical Nasdaq-100 constituent reconstruction or a claim of broad generalization.

Use only long/cash research. First examine a regular-session intraday horizon, with any hypothetical exposure closed within that session. This would require a change to the current premarket-only exit/session rules before any trading adoption.

The money-fast rationale is executable frequency and capacity: these candidates may avoid the known stale extended-hours IEX books and support repeated observations. Their edge size and net dollars per day are **unknown**. This warrants a cheap feasibility test, not a claim that liquid stocks already outperform Initiative 6.

## Feasibility delivery — October 1 18:00 CEST

The [read-only census](init7-data-census-2026-10-01.md) is complete, with raw evidence in `log/2026-10-01/init7-data-census.json` and an offline replay in `scripts/init7-data-census.py`. Data feasibility supports specifying the prospective comparison; it does not establish an execution edge. The next deliverable is a frozen numerical control and one bounded agent variant at the October 2 15:00 run.

The census covered all eight fixed symbols:

1. Fetch September 30 completed regular-session SIP five-minute bars with explicit start/end times and pagination. Record coverage and the calendar/session bounds.
2. Capture October 1 regular-session IEX quotes with observation time, quote age, positive bid/ask sizes and spread. A quote is evidence about the book, not an order fill.
3. Estimate executable observation frequency, data delay, and operating cost for one bounded agent decision versus a simple price-only control. Record missing evidence without assuming a fill.

This delivery needs the existing Alpaca read access and an open regular session; it does **not** need the deferred IBKR account. It can run alongside the current pilot and without another pulse.

After feasibility, specify one numerical baseline and one agent-assisted variant before observing their future outcomes. Freeze decisions and source publication/observation times, count every tried variant, and compare equal capital and time windows. Record net dollars per session, spread/slippage, inference cost, drawdown and capital time. Include cash, QQQ and the actual AH→PM account result as comparators; historical LLM news decisions cannot be treated as unknown-future tests.

## Needs from Juan

The daily email should surface the proposed liquid regular-session strategy/universe direction. Research is unblocked. A future trading adoption requires evidence and Juan's review; preserve his September 22 broker-test deferral.
