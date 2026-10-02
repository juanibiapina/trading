# Initiative 7 — frozen liquid-session comparison

## Decision

The numerical versus bounded-agent design is delivered. [The frozen configuration](init7-comparison-v1.json) is the source of truth for thresholds, timing, capital, costs, source capture, comparators and evaluation gates. Its SHA-256 is `df00c3bc9dd86117191ab86b838589e2dfdd5231ae6f1c62861b2e484915dc98`.

This advances Research and log-only instrumentation. Initiative 6 retains the sole pilot slot. No comparative portfolio or performance pilot starts with this delivery. An eventual regular-session/universe adoption remains the existing daily-email proposal.

## What the comparison isolates

**N1** selects the strongest positive stock return relative to QQQ over the same completed half-hour window. **A1** receives that same candidate and uses the pinned Jev catalyst classifier to retain it or choose cash. It cannot replace the ticker, search for another event or predict a return. This isolates whether the event judgment improves the numerical selection after inference and trading costs.

The price rule is a simple first hypothesis. It was selected without a historical return search and has no measured trading edge. The probability cutoffs are frozen design choices; the earlier easy classifier controls did not establish calibration. A missing source means cash for A1, so results must include source availability as well as classification accuracy.

Both future arms start with equal capital, use the same post-decision book and have the same exposure limit and exit times. Cash and QQQ use the same capital and calendar window. Actual AH→PM account dollars are reported separately with their deployed capital and holding hours. This prevents a dollar result from a different allocation from masquerading as an equal-exposure comparison.

## Causal timing

The configuration uses six observations beginning at 10:30 ET. At 10:00, a 16-minute delayed request would have only ten minutes of completed regular-session data, insufficient for the selected half-hour feature. Starting later resolves that dependency before outcomes are collected.

The new [feature replay](../../scripts/init7-comparison-features.py) uses seven exact, consecutive SIP closes for every basket symbol, the exchange-calendar bounds and only pages received by the reference cutoff. The last bar end must precede the earlier of the requested end and market clock minus the buffer. Missing slots make the basket cash. Latest IEX bars cannot replace SIP features. A quote returned before the decision is a diagnostic; prospective modeled entries require a new quote after the common decision is saved.

The capture design requires exact SEC source bytes, accession/issuer identity, acceptance and receipt times, hashes, extracted text and failed-request records in exclusive observation directories. A later retrieval of an older publication cannot be used for an earlier decision. Full input text must fit the classifier's request limit; oversized or incomplete evidence results in a recorded cash decision. This primary-source archiver is **specified, not implemented or network-verified yet**.

[SEC's current interface documentation](https://www.sec.gov/search-filings/edgar-application-programming-interfaces), read October 2, says company submissions are updated as filings are disseminated and describes the zero-padded CIK submissions endpoint. Dissemination time does not establish our receipt time. SEC-only evidence can miss an issuer release that precedes its filing; the availability tally must expose that limitation.

## Capital feasibility and friction

All eight prices in the October 1 census exceed the research allocation, so whole shares would produce no position. Today's read-only `/v2/assets/SYM` responses report **8/8 active, tradable and fractionable**; raw dated responses are in [the eligibility archive](../../log/2026-10-02/init7-asset-eligibility.json). This resolves asset eligibility, not account-level acceptance or a fill. No order was sent.

[Alpaca's fractional documentation](https://docs.alpaca.markets/us/docs/fractional-trading), read October 2, describes fractional quantities and day orders in both paper and live accounts. The page also contains inconsistent wording about extended-hours/order-type support. Regular-session fractional day market orders are supported by both passages; an eventual execution check must verify the chosen path. The existing broker-test deferral is preserved.

Using the earlier census median spread as a fixed illustration, a $95 position incurs approximately **$0.187** in spread crossing. With the frozen base slippage and assumed fee allowance, friction becomes approximately **$0.301 per round trip**; the stress case is **$0.681**. At the conservative $0.05 call budget, the agent needs approximately **0.370% gross per round trip** in the base case and **0.770%** in the stress case. Those are arithmetic break-even illustrations, not forecasts; future quote-specific costs replace the illustrative spread. The prior Jev control batch cost much less than this call budget, but its tokens do not bound a full filing request.

The protocol records billed and estimated inference separately, charges calls that end in cash, and preserves unknown usage/cost. Slippage and fee allowances remain assumptions. Required capture/data costs count against each standalone strategy; setup/research effort is reported separately. A positive gross return cannot support adoption with unresolved operating costs.

## Verification

[The dated reference output](../../log/2026-10-02/init7-comparison-reference.json) replays the October 1 census: **56/56 required closes** are present, all seven stock returns are negative and N1 chooses cash. The strongest relative name, META, is still negative in absolute terms. The reference is off the frozen observation schedule and predates the freeze; it is explicitly excluded from prospective performance.

[The verification record](../../log/2026-10-02/init7-comparison-verification.json) contains **13 passed CLI checks**. They cover exact replay, positive selection/ties, missing QQQ slots, insufficient opening data, future-bar independence, receipt causality, wrong-feed rejection, unfinished pagination, duplicate timestamps, zero prices and overwrite refusal. Synthetic positive selection keeps the quote marked diagnostic. Python compilation and `git diff --check` passed.

This run made **zero Jev calls**. It added no inference charge; the prior six-call manifest remains the only live classification batch. No prospective classification accuracy, calibration, return or account-growth rate is measured by this delivery.

Reproduce the reference in a new output file:

```bash
python3 scripts/init7-comparison-features.py \
  --design docs/investigations/init7-comparison-v1.json \
  --input log/2026-10-01/init7-data-census.json \
  --output /tmp/init7-comparison-reference.json
```

## Next delivery and dependencies

**October 5 15:00 CEST:** implement the immutable SEC primary-source archiver, verify one real issuer capture or archive its actual access failure, and reject future receipts and overwrites. Freeze the ticker/CIK mapping and deterministic text extraction before prospective Jev inference. This is ready work alongside the older Initiative 1 sparse-baseline delivery.

**October 5 18:00 CEST:** deliver the common observation orchestration and identify the first future scheduled capture that the running scheduler can actually load. A new log-only pulse may collect inputs and classifications; it cannot start a second performance pilot. Do not reconstruct earlier observations after the fact.

Five full prospective instrumentation sessions precede any comparison pilot. The pilot additionally depends on release of Initiative 6's slot and verified causal capture, followed by a frozen future exchange-calendar window. Actual fills and any live plan/session change require the later execution/review step. Research is not blocked by Juan's deferred broker access.
