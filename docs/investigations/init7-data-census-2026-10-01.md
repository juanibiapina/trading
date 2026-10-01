# Initiative 7 — liquid regular-session data census

Captured 2026-10-01T16:04:08.580666+00:00; completed SIP date 2026-09-30.

**8/8 fresh, positive-size two-sided IEX books at this observation.**
The exchange calendar supplies session bounds; SIP requests consume every page and never fall back to IEX.

| Symbol | Completed SIP slots | Current delayed SIP slots | Quote age (s) | Bid / ask | Sizes bid / ask | Spread (bps) | Fresh <=60s |
|---|---:|---:|---:|---|---|---:|---|
| AAPL | 78/78 | 27/27 | 0.435 | 327.82 / 327.92 | 80 / 40 | 3.050 | True |
| MSFT | 78/78 | 27/27 | 0.124 | 512.94 / 514.43 | 40 / 80 | 29.006 | True |
| NVDA | 78/78 | 27/27 | 0.181 | 229.81 / 229.84 | 100 / 100 | 1.305 | True |
| AMZN | 78/78 | 27/27 | 0.115 | 247.23 / 247.74 | 100 / 100 | 20.607 | True |
| GOOGL | 78/78 | 27/27 | 0.349 | 340.28 / 340.92 | 80 / 40 | 18.790 | True |
| META | 78/78 | 27/27 | 0.656 | 725.2 / 727.64 | 80 / 160 | 33.589 | True |
| TSLA | 78/78 | 27/27 | 0.275 | 357.65 / 359 | 80 / 280 | 37.675 | True |
| QQQ | 78/78 | 27/27 | 0.060 | 738.71 / 738.77 | 80 / 280 | 0.812 | True |

## Frequency, friction and cost

Median fresh-book spread: **19.699 bps**; observed range 0.812–37.675 bps.
At a $100 research allocation, crossing this median spread once per round trip costs about **$0.1970**, before slippage and fees.
Current SIP last completed-bar ends were 1148.2–1148.2 seconds old at receipt, with a deliberate 16-minute request buffer.
Capture made 6 read requests (2 SIP pages), totaling 3.605 seconds in requests. Existing access required no new subscription.
The normal session supplies 78 five-minute slots per symbol. Six hourly basket observations at 10:00–15:00 ET are feasible in calendar time, but repeated fresh-book availability is unmeasured.
A numerical control needs zero model calls. A bounded agent variant would make one call per basket observation: six calls per full session.
Its actual inference price and token count remain unknown. A prospective $0.05/call budget would cap six calls at $0.30/session; this is a design budget, not a measured bill.
For comparison, at $100 allocation and six actual trades a $0.30 inference bill alone needs 5 bps average gross return per trade, plus spread, slippage and fees. Opportunity count is unknown.

## Decision and limits

Data feasibility supports specifying one numerical control and one bounded agent variant before observing future outcomes. It does not establish a profitable strategy or a fill.
IEX is one venue, not a consolidated executable book. A single snapshot cannot establish all-day coverage, depth at a proposed size, historical slippage, or an edge over AH→PM.
Current SIP is delayed; a future control must use only bars actually returned at each decision. Archive quote and source receipt times.
Initiative 6 retains the sole pilot slot. Any regular-session trading adoption stays a proposal for Juan's daily email; no order or schedule change follows from this census.

## Reproduce

```bash
python3 scripts/init7-data-census.py --input log/2026-10-01/init7-data-census.json \
  --report /tmp/init7-census-replay.md
```

## Next deliverable

October 2 15:00 CEST: write one frozen numerical control and one bounded agent variant, with causal observation timing, equal capital, cash/QQQ comparators, net dollars per session, model costs and a complete trial record. Keep this at Research until a prospective instrumentation protocol is ready.
