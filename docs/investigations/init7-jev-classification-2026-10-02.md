# Initiative 7 — Jev stock classification

## Decision

Start with stock catalyst classification in shadow mode: identify the documented event and independently flag dilutive financing and binding commercial activity. These distinctions address observed grading mistakes involving financing, exploratory ventures and old asset-sale payments. Reuse numerical volume, session-history and quote calculations for price setups; Jev's contribution is interpreting event text.

The expected account-growth benefit is fewer selection mistakes at a small inference cost. Incremental net dollars per session remain unknown. This is Research plus Instrument, with no second pilot, trading adoption or profitability claim. Initiative 6 retains the pilot slot. The alternative liquid-universe comparison remains the larger strategy test after the missed account deadline.

## Related projects and what they classify

Primary material read October 2, 2026. Reported performance below belongs to the authors and measures their stated task.

| Project / approach | Inputs and classification target | Evaluation and costs | Use in this initiative |
|---|---|---|---|
| [ProsusAI FinBERT model card](https://huggingface.co/ProsusAI/finbert) and [original paper](https://arxiv.org/html/1908.10063), Table 2 | Financial sentences; positive, negative or neutral sentiment, with softmax probabilities. | Financial PhraseBank, reported 10-fold cross validation: accuracy 0.86 / macro F1 0.84 across all data; accuracy 0.97 / F1 0.95 on full annotator agreement. Training uses an AWS p2.xlarge with K80; dollar cost per inference is not reported. Self-hosting still costs compute and maintenance. | A sentiment control is available, but positive language does not distinguish commercial commitments from dilution or promotional plans. No stock-return conclusion follows from sentence accuracy. |
| [FinBERT-FLS model card](https://huggingface.co/yiyanghkust/finbert-fls) | Financial text; Specific FLS, Non-specific FLS or Not-FLS (forward-looking statement). Fine-tuned on 3,500 manually annotated annual-report MD&A sentences from Russell 3000 firms. | The inspected card supplies a model invocation, without a held-out metric or dollar cost. | Useful distinction between an expectation and a completed event. Our initial rubric explicitly excludes future expected regulatory clearance from completed regulatory events. |
| [Snowflake SEC Analytical Search quickstart](https://www.snowflake.com/en/developers/guides/analytical-search-over-sec-filings-with-snowflake-cowork) | Dated SEC filings, chunks, ticker and SIC metadata; event type (earnings, M&A, leadership, risk, guidance, regulatory, capital markets, bankruptcy, annual/quarterly/current report, other), sentiment (positive/negative/neutral/mixed), and industry. | Demonstrated counting/listing queries on February 3, 2025 filings; this inspected quickstart does not report a held-out event confusion matrix or trading returns. Costs span warehouse, search, orchestration and per-row AI functions; no single measured dollar budget is reported. Primary page HTTP fetch was blocked; web-search extraction supplied its full text. | Reuse source IDs, timestamps and semantic labels joined to numerical calculations. A warehouse and multi-agent workflow are unnecessary for the first six cases. |
| [TypeSafe SEC-industry cookbook](https://docs.typesafe.ai/cookbooks/classification_using_confidence.md) | Item 1 Business sections of 60 annual reports, 1993–2024; one Choice over 75 SIC major groups, optionally broadened to 10 divisions when confidence <0.9. | Forced groups: 39/60; confident subset: 27/30; mixed group/division policy: 48/60 useful labels. Filings were selected because text supports the self-reported SIC code. This is a curated demonstration and a coarser-label policy, not comparable full-resolution accuracy or a trading test. Cookbook dollar cost is not reported. | Industry labels are metadata. Preserve confidence, but do not import its 0.9 threshold or impose a sector filter. |
| [TypeSafe feature-discovery cookbook](https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery.md) | Wine tasting notes, with generated Score/Noul questions yielding 67 numerical features for CatBoost critic-score regression. | 2,000 reviews; 800 untouched evaluation rows. Reported RMSE improves from word-count CatBoost 2.47 to 1.77 after five search rounds. This is not a stock classifier. | Preserve reusable probabilities for a later chronological outcome test. Autoresearch requires enough independent labels and a complete trial record before applying it to trades. |

A [FinBERT practitioner discussion](https://www.reddit.com/r/algotrading/comments/ecdgnj/finbert_financial_sentiment_analysis_with) raises corpus/date and writing-style transfer concerns. These are research checks, not performance evidence. The first local run will use current catalyst language and clear missing/mixed evidence controls.

## Frozen first specification

`stock-catalyst-v1` is defined in `scripts/init7-jev-classify.py`. Six expected cases are frozen in `log/2026-10-02/init7-jev-inputs-v1.json` before inference: AMOD, SORA and ELUT source summaries plus synthetic binding-contract, missing-evidence and mixed-event controls.

One request per case asks three independent questions over the same state: one Choice for the principal catalyst and two Noul evidence flags. Choice labels cover earnings/guidance, completed regulatory/clinical events, commercial operations, financing/dilution, non-binding plans, asset cash receipts, fixed-price acquisitions, mixed/other and unknown. Noul flags mean evidence is supplied, not a forecast or proof that an absent event does not exist. Mixed cases can carry both independent flags.

Each model state includes ticker, decision cutoff and source publication times/text. The runner rejects sources published after the cutoff. Expected labels, trading grades, subsequent prices and outcomes are excluded from requests. Archived cases are reconstructed summaries of the contemporaneous October 1 log; they are neither verbatim primary documents nor prospective profitability evidence. The publisher/SEC URLs and summary provenance are recorded per case. Future instrumentation needs immutable primary excerpts and actual observation times before outcome collection.

Use the pinned model `jev-1.13.0` and the documented HTTP endpoint `POST https://api.typesafe.ai/v1/systemone`. Live [HTTP reference](https://docs.typesafe.ai/api.md), [Python SDK](https://docs.typesafe.ai/sdk/python.md), [Choice](https://docs.typesafe.ai/primitives/choice.md), [State](https://docs.typesafe.ai/concepts/state.md), [confidence](https://docs.typesafe.ai/confidence.md) and [model/pricing](https://docs.typesafe.ai/models.md) were read before implementation. The Python standard-library HTTP runner avoids a new dependency and SDK retry charges in this first bounded run.

Record every request, response distribution, returned model, latency, token usage and failure. Existing output directories are rejected. An attempted call is saved before transmission; failures stop the batch and preserve unknown usage instead of implying zero. Costs use the checked October 2 published rate **$0.042 per million input tokens; output tokens free**. The estimate comes from measured token usage and is distinct from a billed charge. Charges are unavailable through the inspected response schema. Search, research-agent, data and infrastructure costs are outside this inference estimate and are not asserted as zero.

## Evaluation and next deliveries

The first six cases verify the interface and semantic controls. Compare all three outputs to expected labels chosen before inference; for this descriptive check only, map Noul probabilities at 0.5. Preserve raw probabilities, every disagreement and confidence. Six selected cases cannot establish accuracy, calibration or trading edge.

At **October 2 18:00 CEST**, freeze the numerical-control versus bounded-agent comparison with equal capital, causal observation times, delayed SIP availability, cash/QQQ comparators, spread/slippage and inference costs. This delivery was deferred at 15:00 to complete Juan's new Jev handoff and the older Initiative 3 replay. A prospective classifier/outcome comparison follows that design; it remains research while Initiative 6 occupies the pilot slot.

The next daily email must read the dated run manifest and include Jev labels, calls, tokens, estimated costs and any failure. No new input is needed from Juan; his broker-test deferral remains in force.

## First run result

Completed **2026-10-02 13:09:23–13:09:25 UTC** with `jev-1.13.0`: **6 successful calls / 18 expected judgments matched**. The three archived summaries classified AMOD as financing/dilution, SORA as a non-binding plan and ELUT as an asset cash receipt. The synthetic binding-contract, missing-evidence and mixed-event controls also matched. All six Choice confidences were 1.0; a selected easy batch does not test calibration. AMOD's financing evidence probability was 0.96, while the mixed control preserved both financing (0.98) and binding commercial activity (0.96).

Measured usage: **5,471 input / 931 output tokens**. At the frozen published rate, **estimated Jev inference cost = $0.000229782 USD**. The API response supplies no billed charge, so measured charge remains unavailable. Six request latencies ranged **0.277–0.471 seconds**, and the whole batch finished in approximately 2.15 seconds. No failed live request occurred. These figures cover this batch only, with no claim about all-account usage or research-agent costs.

Authoritative artifacts: `log/2026-10-02/init7-jev-shadow-v1/manifest.json`, `inputs.json` and `case-01.json` through `case-06.json`. Each case preserves the exact request and response; the manifest contains the frozen-input SHA-256 and pricing source. Offline replay exactly matches the saved summary. Public CLI checks reject future publication times and an existing output directory. A simulated HTTP 429 at the network interface verifies that a failed attempt is archived with unknown total cost; it made no additional live call. Expected labels and provenance fields were verified absent from model state. Python compilation and syntax/whitespace checks passed.

```bash
# Read-only validation; no model call.
python3 scripts/init7-jev-classify.py --input log/2026-10-02/init7-jev-inputs-v1.json
# Reproduce the recorded result with no network or new charge.
python3 scripts/init7-jev-classify.py --replay log/2026-10-02/init7-jev-shadow-v1
# A future authorized batch uses a new output directory.
python3 scripts/init7-jev-classify.py --input NEW_DATED_INPUTS.json --out-dir NEW_DATED_RUN_DIR --run
```

Next classification delivery: at October 2 18:00, define the prospective comparison and immutable primary-source capture. More labeled summaries would repeat this interface check; profit evidence needs future observations and outcomes.
