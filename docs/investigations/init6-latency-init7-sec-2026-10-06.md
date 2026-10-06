# Initiative 6 causal latency and Initiative 7 SEC archiver — 2026-10-06

## Summary

Initiative 6's modeled premarket edge depends on entering at the R+3 bar open, within seconds of the confirmation bar's close. Moving that entry 5 minutes later removes the net edge; 15 minutes, the delay of the current data path, turns it into a loss. The 04:10 ET discovery cohort has also been recording the previous session's list every day. The pilot therefore fails its causal execution check with the current stack, and its pilot slot is released.

Initiative 7's SEC primary-source archiver is built and verified, with a frozen ticker-to-CIK mapping and seven real captures. A 92-day census shows the frozen A1 arm would find a usable 8-K in only 1.7% of observations, so a 20-session comparison would contain about two Jev decisions. The A1 design needs an amendment before prospective instrumentation starts.

## Initiative 6: entry latency

`scripts/init6-pm-pilot.js --delay-min N` moves the entry to the first 5-minute bar that opens at least N minutes after the R+2 confirmation bar ends. Gate, exit and universe are unchanged; research runs leave the ledgers untouched. A full default run reproduced the existing ledger and liquidity audit byte for byte.

| Entry latency after R+2 ends | Holdable n | Mean +10% limit exit (gross) | After assumed 2% spread | Positive | All classes n=35, gross |
|---|---|---|---|---|---|
| 0 min (R+3 open, ledger definition) | 26 | +4.4% | +2.4% | 20/26 | +3.4% |
| 5 min | 26 | +0.7% | -1.3% | 18/26 | +1.7% |
| 10 min | 26 | -3.7% | -5.7% | 15/26 | -1.7% |
| 15 min | 26 | -4.4% | -6.4% | 12/26 | -2.5% |

Outputs: [0 min](../../log/2026-10-06/init6-latency-0min.txt), [5 min](../../log/2026-10-06/init6-latency-5min.txt), [10 min](../../log/2026-10-06/init6-latency-10min.txt), [15 min](../../log/2026-10-06/init6-latency-15min.txt).

The current path cannot enter at R+3:

- **Free SIP bars** are served only once they are at least 15 minutes old, and the gate's 3,000-trade threshold is defined on SIP trades.
- **The TradingView screener lags.** All four checked 04:10 ET cohorts hold the previous session's final premarket prices, not the current session's. Oct 5 lists SGRX at $1.775, exactly its Oct 2 PM-last. Oct 2 lists SDEV at $3.59, its Oct 1 09:25 ET close, while SIP traded $4.36–$4.82 at 04:00–04:15. Oct 1 lists CNTB at $1.8805 (Sep 30 PM-last about $1.88) while it traded $1.03–$1.13. Sep 30 lists BKYI at +100%, Sep 29's gap. Quote ages are 11–60 hours. The [09:15 ET probe](../../log/2026-10-06/tv-delay-probe-0915et.json) found the screener price inside the latest real-time IEX bar for 0 of 8 names, with matches in bars up to 17 minutes old. An unarchived 09:03 ET probe placed 4 of 5 names in the bar 16 minutes old. IEX is one venue, so this bounds the lag loosely; the cohort files are the stronger evidence.
- **No pulse runs between 04:10 and 04:30 ET.** Ignitions cluster at 04:00–04:21 ET; the next premarket pulses are the 04:30 position evaluation (exits only) and the 05:00 log-only scan.

Even with paid real-time consolidated data, an agent pulse needs minutes to start and decide, and the edge is gone at 5 minutes. Executing it would need a deterministic watcher that orders within about a minute, plus fills a paper broker can simulate on stale IEX premarket books. That is the Initiative 2 dependency again, and the 1-minute limit-fill model is itself optimistic.

**Decision:** the pilot fails its causal check, and the pilot slot is released. The tracker, ledger and cohort keep running log-only, so the R+3 ledger remains an upper bound. No live rule or pulse changed.

**Fresh cases.** QTEX (Oct 5, PM-only, holdable) was rejected by the VWAP condition: the R+2 VWAP of $1.39 fell below 98% of R+1's $1.44. An R+3 entry at $1.40 would have reached the $1.54 limit at 04:25 ET. This is the second VWAP false negative after MEDS. QTEX appears in the Oct 5 cohort only through Friday's stale row ($0.9261), so it is not a discovery hit. RUBI (Oct 6) was correctly rejected: it fell from $1.40 to $0.78 after a 05:55 ET ignition. It is uninvestable after its 1.5-for-1 stock dividend. Oct 6 has no cohort because of the outage.

A bug fix is included: ad-hoc runs (`SYM DATE`) used to overwrite the ledger with their single case. They now leave it unchanged.

## Initiative 7: SEC archiver

[`scripts/init7-sec-archive.py`](../../scripts/init7-sec-archive.py) implements the frozen primary-source protocol:

- **`map`** froze the mapping from SEC `company_tickers.json`: seven unique CIKs, no ambiguity, mapping SHA-256 `7afbd376…26e6e7`. The [raw response, request metadata and mapping](../../log/2026-10-06/init7-sec/mapping/) are archived.
- **`capture`** creates an exclusive directory and saves exact bytes and metadata for the submissions JSON, headers, filing index, 8-K and every EX-99. Metadata covers URL, request and receipt times, status, content type, length and hash. It reads acceptance from the filing header, extracts text deterministically (`init7-sec-text-v1`), and checks receipt and acceptance against the cutoff. The complete request is validated with the classifier's own `requests_for` and 20KB limit. It writes `jev-case.json` only when every check passes; otherwise it records a cash reason.
- **`replay`** re-verifies archived bytes, text and the decision offline.

**Acceptance time.** The submissions JSON `acceptanceDateTime` is unreliable. In the census, 6 of 16 filings (Apple 1, Amazon 4, Meta 1) read exactly 14,400 seconds (4 hours) later than the true UTC acceptance from the filing header; the other 10 match. Apple's January and February 2026 filings read 5 hours late, the winter Eastern offset. The header's ACCEPTANCE-DATETIME, read as America/New_York, is authoritative. Apple's earnings acceptance at 16:30:28 ET confirms that reading.

**Verification:**

- **Real captures:** seven [captures](../../log/2026-10-06/init7-sec/verify-now/) at cutoff 13:14:09 UTC found no 8-K within 24 hours, so every issuer is cash with reason `no_8k_within_window`.
- **Documents and late receipt:** a [historical AAPL capture](../../log/2026-10-06/init7-sec/verify-late/AAPL-2026-07-31/) with cutoff Jul 31 10:32 ET archived the 8-K and EX-99.1 and was rejected as `received_after_cutoff`.
- **Offline checks:** all eight archives replay with no problems. Rewriting a capture directory and a cutoff without a time zone both fail before any request. A tampered text file is detected.
- **Synthetic decisions** on Apple's archived text (code paths only): the complete 17,138-byte request is eligible. Oversized text gives `source_too_large`, a later acceptance gives `future_source`, and a failed request gives `source_request_failed`.

## Initiative 7: A1 source availability

The [census](../../log/2026-10-06/init7-sec/census-2026-07-06-to-10-05.json) covers Jul 6 – Oct 5: 66 weekdays × 6 observation times × 7 issuers = 2,772 slots. It keeps hashes and sizes only. It ran 67 SEC requests with no failures.

| Measure | Count |
|---|---|
| 8-K filings | 16 |
| Complete Jev request within 20KB | 8 of 16 |
| Earnings 8-Ks (item 2.02) within 20KB | 2 of 7 (AAPL 17,138 B; TSLA deliveries 8,000 B) |
| Slots with an 8-K accepted in the prior 24 h | 96 (3.5%) |
| Slots with a usable 8-K (fits 20KB) | 48 (1.7%) |

A1 keeps N1's ticker only when that ticker has a usable 8-K with an allowed label. At 1.7% availability, a 20-session pilot (120 observations) would contain about two Jev decisions. A1 would be cash about 98% of the time, so the comparison would measure N1 against cash rather than Jev's value. Five of the seven earnings releases exceed the limit; the frozen rules forbid truncation.

**Proposed amendment (to freeze before orchestration):** register **A2** as a veto variant. A2 keeps N1's candidate when no usable source exists and goes to cash only when Jev labels a usable source as financing/dilution or as a non-binding plan. This measures Jev where it can act and keeps A1 in the trial register. A deterministic lead extraction (press-release headline and opening paragraphs) for oversized exhibits would be a separate, independently frozen variant.

## Limits

- The latency study reuses hindsight-classified tracker names and modeled 1-minute limit fills; it has no real fills.
- The census fetched filings after the fact. It measures frequency and size, not causal receipt. Its weekday count includes exchange holidays.
- Jev made no calls this run; the earlier six-call manifest remains the only live classification evidence.
