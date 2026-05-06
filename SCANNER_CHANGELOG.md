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
MIN_DAY_CHANGE_REGULAR = 15%  (supplementary regular session scan)
```

## Current Process

- 7 evening scans every 30 min (21:30–01:30 CET)
- 3 morning evaluations (10:20, 12:00, 14:00 CET)
- Paper trades with ~€100 positions
- All sectors — no sector restriction (learning phase, see Day Trading.md)
- Session timing follows America/New_York market hours, including DST
- Regular session scans (21:30 CET) flag candidates as "Watch" — paper trades only entered during AH scans (22:00+ CET)
- Entry rules: float <50M, catalyst required, first day of unusual volume (sector and price thresholds are observations under review, not hard rules)
- **No paper trades before 23:00 CET** — 22:00 and 22:30 scans are observation only
- **AH change >10% in at least 2 after-hours scans** (regular session appearances don't count)
- Trajectory preference: build/hold patterns preferred over spike→fade
- **Skip dead-cat bounces** — stocks with Day% below -15% are excluded even if AH bounce is strong
- Morning retrospective uses Yahoo AH history as the primary source; forced AH scans are secondary diagnostics only

## Modifiable Files

- `scripts/scan.py` — Scanner parameters, filters, output columns
- `scripts/check-prices.py` — Price checking utility
- `prompts/post-market-scan.md` — Evening scan prompt (evaluation criteria, log format)
- `prompts/morning-evaluation.md` — Morning evaluation prompt

## Change Log

_(entries are prepended — newest first)_

### 2026-05-06 — Track Entry Extension in Morning Evaluation

**Context:** Last 4 paper trades show a pattern: the one winner (NXTT, +19.1%) had the lowest Total% at entry (~+23%), while the three losers were all highly extended at entry (MASK +78%, OCG +42%, BFRG -20% dead cat). May 5's OCG was entered at +41.8% Total and peaked at +43% — essentially a buy-at-top. May 4's MASK was entered at +78% Total and never recovered. The Total% column exists in scanner output but isn't systematically tracked in the evaluation template alongside P&L, making the correlation invisible over time.

**Evaluation of previous changes:**
- 2026-05-05 DST session timing fix: **Helped.** May 5 evening scan at 22:00 CET correctly ran in AH mode (0 hits because nothing qualified yet, but 22:30 returned proper AH columns with Close/Day%/AH Chg). Compare with May 4 at 22:00 which still showed "regular-session data" before the fix.
- 2026-05-05 Yahoo AH as primary retrospective: **Helped.** May 5 morning evaluation explicitly uses "Yahoo AH reconstruction confirms both real AH continuation names were EZGO and OCG" and doesn't rely on the forced AH scan (which returned 0 hits again). The retrospective correctly identified the winner from AH+PM data.

**Changes:**
1. **prompts/morning-evaluation.md** — Added "Entry Total%" column to the Paper Trade P&L table template (between Entry price and Entry Time).
   - Why: Total% at entry is the best single measure of how extended the stock is when we buy it. It combines Day% + AH% into one number representing the total move from previous close. The last 4 paper trades suggest entries above ~+40% Total underperform, but with only 4 data points this is a hypothesis, not a rule. Systematic tracking in the P&L table will build the dataset needed to set a data-driven threshold.
   - Hypothesis: Future morning evaluations will include Total% at entry alongside P&L. After 5-10 more paper trades, we'll have enough data to determine if a Total% entry ceiling improves selection. Measurable: (1) next morning evaluation P&L table includes the Entry Total% column, (2) after 10 trades total, we can compute correlation between entry extension and outcome.

2. **prompts/post-market-scan.md** — Fixed float threshold in learning-phase default from `<10M` to `<50M` (consistency fix — already documented as `<50M` in Current Process section since earlier changelog entries).
   - Why: The prompt was out of sync with the documented process. May 5's EZGO (20.7M float, +81.8% hypothetical) was skipped partly because the prompt said "<10M" even though the learning-phase rules use <50M. Aligning prevents unnecessary restrictiveness.
   - Hypothesis: Agent will no longer over-penalize candidates with floats in the 10-50M range. Measurable: next time a candidate with float 10-50M qualifies on other criteria, it won't be dismissed for float alone.

### 2026-05-05 — Fix DST Session Timing + Use Yahoo AH Reconstruction

**Context:** The 2026-05-04 session showed the scanner logic was mostly sound but the plumbing around it was off. MASK was detected and CWD was correctly skipped as a dead-cat bounce, yet the 22:00 CET scan still behaved like a regular-session watchlist even though US after-hours had already opened. In the morning, the forced after-hours scan returned 0 hits even though the live evening log clearly contained AH movers. Both issues point to tool/process timing, not strategy.

**Evaluation of previous changes:**
- 2026-04-03 dead-cat bounce skip rule: **Helped.** CWD (-26.6% day) was explicitly skipped at 23:00, 23:30, 00:00, and 00:30 CET despite reaching +20.0% AH. The rule worked as intended and kept the slot free for stronger names.
- 2026-04-02 Total% prompt integration: **Helped.** Every 2026-05-04 AH table included Total%, and the notes used it directly for both MASK (+78.0% at entry) and CWD (still negative vs previous close).
- 2026-04-02 AH-scan requirement clarification: **Mixed but helpful.** MASK was not entered on its first AH appearance at 22:30 CET. It only qualified at 23:00 after two AH scans. That part worked. But the fixed ET offset meant the 22:00 CET run was still treated as regular session during DST, so the first true AH read came later than it should have.

**Changes:**
1. **scripts/scan.py** and **scripts/check-prices.py** — Replaced the fixed ET offset with `America/New_York` timezone handling.
   - Why: Both scripts used a hard-coded UTC-5 offset. During DST that is one hour late, which shifts session detection and printed ET timestamps. On 2026-05-04 this made 22:00 CET behave like pre-AH instead of the first real AH scan.
   - Hypothesis: During DST, the 22:00 CET run will classify as after-hours instead of regular session. Measurable: (1) `scripts/scan.py` prints ET timestamps that match America/New_York, (2) evening logs stop describing 22:00 CET as a regular-session placeholder on DST dates.

2. **prompts/morning-evaluation.md** — Made Yahoo AH reconstruction (`check-prices.py --ah-history`) the primary retrospective source. Forced `scan.py --session afterhours` runs remain optional diagnostics only.
   - Why: On 2026-05-04 the forced AH scan returned 0 hits even though MASK and INHD clearly had AH moves in the evening log. The prompt was steering the evaluation toward a weak overnight source.
   - Hypothesis: Next morning evaluation will identify the winner from PM scan plus Yahoo AH reconstruction instead of treating a 0-hit forced AH scan as the main retrospective. Measurable: (1) the retrospective section explicitly cites AH reconstruction, (2) winner diagnostics use `--ah-history` data when forced AH scan is empty.

### 2026-04-03 — Add Dead-Cat Bounce Skip Rule

**Context:** BFRG (Apr 2) crashed -25.9% during regular session, bounced +16.7% in AH, was entered at $1.40 as the first candidate meeting criteria (>10% AH in 2 scans). It faded to $1.29 (-7.9% loss). Total% from prev close was -16% at entry. Meanwhile PFSA (building momentum, +10.8% then +42.1% AH) was blocked by the existing position. The morning evaluation explicitly recommended: "skip stocks that crashed >15% in regular session." This is the 3rd+ observation of dead-cat bounces failing: BFRG (Apr 2, -7.9%), HPAI (Mar 31, -25% day, AH bounce to +10.7%, dead in PM with no trades), and the pattern aligns with earlier observations about crash-recovery bounces not carrying through.

**Evaluation of previous changes:**
- Total% Prompt Integration (2026-04-02): **Working (1 data point).** Apr 2 evening scan tables include Total% column consistently. BFRG's negative Total% (-14% to -16%) was visible in every scan table, and the morning eval referenced it directly. Integration complete.
- AH Scan Requirement Clarification (2026-04-02): **Working (1 data point).** On Apr 2, the agent correctly required 2 AH scans before entering. BFRG was tracked across 23:00 (+21.7%) and 23:30 (+16.7%) before entry. PFSA was not entered at 23:30 because it had only 1 scan at >10%. Rule followed correctly. However, the rule didn't prevent the bad entry (BFRG still qualified despite being a dead-cat bounce).
- 23:00 CET Minimum Entry Time (2026-03-31): **Working (4 data points, all compliant).** Mar 31 ELAB 23:10, Apr 1 AGPU 23:00, Apr 2 BFRG 23:30. No violations. Rule is embedded.
- Supplementary Day Movers Query (2026-03-26): **Working (4 data points).** Regular session scans consistently produce 50-58 hits. Functioning as intended.

**Changes:**
1. **prompts/post-market-scan.md** — Added dead-cat bounce skip rule to the learning phase default criteria. Stocks with Day% below -15% are now excluded from paper trade entry, even if their AH bounce exceeds +10%. Added brief explanation with evidence count.
   - Why: Dead-cat bounces (big regular session crash followed by AH bounce) have failed in 3+ observations. The stock is recovering from a sell-off, not building new momentum. On Apr 2, this would have prevented the BFRG entry (-7.9% loss) and left the position open for PFSA (+16.7% to +50% hypothetical).
   - Hypothesis: Next time a stock crashes >15% during regular session and bounces >10% in AH, the agent will skip it instead of entering. This frees the position for better candidates that emerge later. Measurable: (1) next dead-cat bounce candidate is explicitly skipped with this rule cited, (2) on nights where only a dead-cat bounce qualifies, "skip all" is chosen instead of entering a losing position.
   - **Evaluation:** Helped. On 2026-05-04, CWD (-26.6% day) bounced as high as +20.0% AH but was skipped in every qualifying scan with the dead-cat rule cited. The filter did its job.

**Updated process:** Added "Skip dead-cat bounces" to Current Process section.

### 2026-04-02 — Complete Total% Prompt Integration + Clarify AH Scan Requirement

**Context:** AGPU (Apr 1) was entered at 23:00 CET with +168% Total% from prev close, the fourth entry above +100% extension to produce a loss (-18.2%). The Total% column was added to the scanner terminal on Apr 1 but not to the prompt table format (same gap as Day% in Mar 11 to Mar 12). Meanwhile, AGPU had appeared in 4 scans (21:30, 22:00, 22:30 regular + 23:00 AH) but only 1 was an after-hours scan. The "sustained across 2+ scans" rule was met by counting regular session appearances, which don't measure AH momentum. The agent entered on the first AH data point with no inter-scan trajectory comparison possible.

**Evaluation of previous changes:**
- Total% Column (2026-04-01): **Working but incomplete integration (1 data point).** Scanner terminal output includes Total%. AGPU at +168% Total% was noted as a concern in the log notes. However, the prompt table format didn't include Total%, so it was computed manually in notes rather than shown consistently in tables. Same integration gap as Day% (Mar 11 scanner, Mar 12 prompt fix). Completing integration now.
- 23:00 CET Minimum Entry Time (2026-03-31): **Working (2 data points, both compliant).** Mar 31 ELAB entered at 23:10 CET. Apr 1 AGPU entered at 23:00 CET. Rule is being followed consistently.
- Trajectory Preference (2026-03-31): **Mixed results (2 data points).** Mar 31 ELAB entered on a "build->fade->build" pattern, +8.1% win. Apr 1 AGPU entered on a "build" pattern that was actually a 1-hour spike decelerating, -18.2% loss. The trajectory classification was unreliable for AGPU because only 1 AH data point existed. The "build" was inferred from intra-scan 5m candle data, not from comparing AH% across consecutive scans. With only 1 AH scan, trajectory cannot be reliably classified.
- Supplementary Day Movers Query (2026-03-26): **Working (3 data points).** Mar 30, Mar 31, Apr 1 regular session scans all produced 54-58 hits. The wider net is functioning as intended.

**Changes:**
1. **prompts/post-market-scan.md** — Added Total% column to the AH table format template (between AH Price and AH Vol). Same completion pattern as the Day% prompt integration on Mar 12.
   - Why: Scanner outputs Total% since Apr 1 but the prompt template still showed the old format without it. The agent computes Total% manually in notes but inconsistently. On Apr 1, AGPU's +168% Total% was buried in evaluation notes instead of being visible in the scan table. Consistent table visibility enables better pattern recognition across scans.
   - Hypothesis: Next AH scan tables will include a Total% column. The agent will reference Total% consistently when evaluating extension rather than computing it ad-hoc. Measurable: (1) next evening's AH scan tables include Total%, (2) Total% appears in the evaluation for every candidate, not just the one selected for paper trade.
   - **Evaluation:** Helped. On 2026-05-04, every AH table included Total%, and the notes used it directly to frame MASK's +78.0% extension and CWD's still-negative total move.

2. **prompts/post-market-scan.md** — Clarified "sustained across 2+ scans" in the learning phase default to specifically require 2+ after-hours scans (22:00+ CET). Regular session appearances don't count toward this requirement.
   - Why: On Apr 1, AGPU appeared in 4 scans (3 regular + 1 AH) and was entered at the first AH scan (23:00 CET). With only 1 AH data point, trajectory classification was unreliable: the agent classified AGPU as "build" based on intra-scan 5m candle data, but the next scan (23:30) revealed AH% declining from +18.8% to +16.0% (fading). Requiring 2 AH data points ensures trajectory is compared between scans, not inferred within a single scan. This also provides a natural 30-minute delay after first AH appearance, allowing early spikes to reveal whether they sustain or fade.
   - Hypothesis: Next time a stock first appears in an AH scan, the agent will wait for the next AH scan before entering. Stocks that spike early and fade (like AGPU) will show declining AH% between their first and second AH scans, triggering the trajectory preference against spike->fade. Measurable: (1) no entry on a stock's first AH appearance, (2) when AH% declines between consecutive AH scans, the stock is classified as fading and deprioritized.
   - **Evaluation:** Mixed but helpful. On 2026-05-04, MASK first appeared at 22:30 CET and was not entered until the 23:00 CET scan after a second AH read. That prevented an even earlier chase. But the DST timing bug still made the 22:00 CET run regular-session only, which reduced the amount of true AH data available before the decision.

**Updated process:** Added "AH change >10% in at least 2 after-hours scans" to Current Process section.

### 2026-04-01 — Add Total% Column to AH Scanner Output

**Context:** ELAB (Mar 31, +108% from prev close) and ASTC (Mar 30, +145% from prev close) were both extremely extended when entered as paper trades. The agent calculated total extension manually in the log notes ("ELAB +68% day + 23% AH = +108% from prev close") but the scanner output only showed Day% and AH Chg% separately. Meanwhile BCG (Mar 31 winner, -2% day + 39% AH = +37% total) was far less extended. The extension assessment is currently ad-hoc and inconsistent across scans.

**Evaluation of previous changes:**
- 23:00 CET Minimum Entry Time (2026-03-31): **Insufficient data (1 data point).** Mar 31 ELAB entered at 23:10 CET (compliant). Result: +8.1% (still open at morning eval). The rule was followed correctly. BCG (winner) appeared at 23:50 CET, 40 min after entry, suggesting even 23:00 may be too early, but 1 data point is not enough to adjust timing.
- Trajectory Preference (2026-03-31): **Insufficient data (1 data point).** ELAB was the only qualifying candidate at 23:00, so no build-vs-spike comparison was possible. Agent correctly noted ELAB's "build->fade->build" trajectory.
- Supplementary Day Movers Query (2026-03-26): **Working (2 data points).** Both Mar 30 and Mar 31 regular session scans produced ~54 hits (up from 10-15 with RVOL-only). The wider net is functioning as intended. Need more data to confirm it improves winner detection specifically.

**Changes:**
1. **scripts/scan.py** — Added "Total%" column to after-hours scanner output. Computes total change from previous close as (1 + Day%) x (1 + AH%) - 1. Displayed between "AH Price" and "AH Vol" columns.
   - Why: The agent already calculates this manually in evaluation notes, but inconsistently. Making it a column ensures it's visible at every scan. Stocks entered above +100% total extension have underperformed: ASTC -27.4% at +145%, ELAB +8.1% but suboptimal at +108%. The Mar 31 winner BCG was only +37% total. This column enables systematic tracking of whether extension correlates with outcomes.
   - Hypothesis: The Total% column will appear in all future AH scans. The agent will reference it when assessing extension risk, making the evaluation more consistent. Over 2 weeks of data, this enables a data-driven conclusion about whether a total-extension threshold should become a filter. Measurable: (1) the column appears in the next AH scan output, (2) the agent mentions Total% when evaluating paper trade extension risk.

**Updated parameters:** No threshold changes. New output column only.

### 2026-03-31 — Enforce 23:00 CET Minimum Entry Time + Trajectory Preference

**Context:** Two of the last four paper trades were entered at 22:30 CET (the second AH scan) despite the learning phase default saying "third AH scan (23:00+ CET)." Both 22:30 entries were spike-and-fade patterns that lost badly: HCTI -17.2% (Mar 25, entered at 22:30 on a +43% spike already fading to +37%) and ASTC -27.4% (Mar 30, entered at 22:30 on a +20% spike that reversed to -3% by 23:00). Meanwhile, the one entry at 23:00+ (NXTT, Mar 24) showed a build pattern across 6 scans and won +19.1%. On Mar 30, the morning evaluation explicitly noted: "don't enter in the first hour of AH" and "late AH scans are more valuable than early ones." The AH trajectory data across 4 days consistently shows build/hold patterns outperforming spike-and-fade.

**Evaluation of previous changes:**
- Supplementary Day Movers Query (2026-03-26): **Insufficient data (1 data point).** Mar 30 regular session scan produced 54 hits (up from typical ~10-15 with RVOL-only query), confirming the supplementary query is producing more candidates. Several low-RVOL stocks with big day moves appeared (VINO +98% at 0.3x RVOL, SONX +67% at 2.3x RVOL). POLA (day's winner, +25.8% day) may have been in the 54 results but was not highlighted as a top watch candidate. Need more sessions to confirm detection improvement.
- AH Trajectory Tracking (2026-03-25): **Working well (4 data points).** Trajectory column present in all recent evaluations. Clear signal emerging: build patterns (NXTT +19%, POLA +28%) and spike-hold (BFRG +16%) outperform spike-and-fade (ASTC -27%, HCTI -17%, HSDT 0%). On Mar 25, ALL 6 AH movers were spike-and-fade and 0/6 followed through. On Mar 30, POLA (build) was the clear winner while ASTC (spike-and-fade) was the clear loser. Data supports using trajectory as a selection factor.
- Learning Phase Paper Trade Default (2026-03-24): **Mechanism working, selection quality poor.** 4 paper trades generated (vs 0 before the change). But selection rate for winners: 1/7 (14.3%). The mechanism generates trades, but the early entry timing (22:30 on 2 of 4 trades) selects spike-and-fade candidates before their pattern becomes visible.

**Changes:**
1. **prompts/post-market-scan.md** — Made the 23:00 CET minimum entry time explicit and non-negotiable. Changed from soft "If by the third AH scan (23:00+ CET)..." to bold "**Do not enter paper trades before the 23:00 CET scan (5:00 PM ET).** The 22:00 and 22:30 scans are for observation only." Also added trajectory preference: "prefer those showing a build or hold AH pattern over those that spiked early and are now fading from their peak."
   - Why: The existing "third AH scan" wording was too soft. On Mar 25 and Mar 30, the agent entered at 22:30 because the candidate "looked strong." Both were spike-and-fade losses. By 23:00, both spikes had already started fading, making the pattern visible. Waiting 30 more minutes would have either prevented the entry or redirected it to a more stable candidate.
   - Hypothesis: Next evening session will not enter any paper trade before the 23:00 CET scan. Spike-and-fade candidates that would have been entered at 22:30 will be visible as fading by 23:00 and either skipped or deprioritized in favor of build/hold patterns. Measurable: (1) no paper trade entry timestamp before 23:00 CET, (2) when a spike-and-fade candidate exists alongside a build/hold candidate, the build/hold is selected.

**Updated process:** Added "No paper trades before 23:00 CET" and "Trajectory preference: build/hold over spike→fade" to Current Process section.

### 2026-03-26 — Supplementary Day Movers Query for Regular Session

**Context:** EEIQ on Mar 25 was the day's winner (+222% PM from close, float 860K, $4M mcap) but was NOT caught by the 21:30 regular session scan despite having a +22.4% day change. The existing regular session filters require both RVOL > 10x AND 5m volume > 5000, which catches "currently spiking" stocks but misses stocks that had big moves earlier and are winding down. EEIQ's 5-minute RVOL at 3:30 PM ET was only ~7.4x (below 10x threshold). Detection rate dropped from 100% to 83.3% (5/6) for the first time.

**Evaluation of previous changes:**
- AH Trajectory Tracking (2026-03-25): **Working (1 data point).** Mar 25 morning eval includes trajectory classification for all 6 AH movers (Spike→fade, Late surge→fade, Build→hold, Spike→hold). Column filled correctly. Need more data points before evaluating predictive value.
- Learning Phase Paper Trade Default (2026-03-24): **Working (2 data points).** NXTT +19.1% win, HCTI -17.2% loss. Selection rate improved from 0% to 33% (2/6). The mechanism is generating paper trade data as intended. One win, one loss is expected in early learning.

**Changes:**
1. **scripts/scan.py** — Added supplementary "day movers" query for regular session scans. During regular session, the scanner now runs two queries and merges results: (1) the existing RVOL > 10x / 5m vol > 5000 query for currently active stocks, and (2) a new query filtering by day% change > 15% for stocks that moved earlier. Results are deduplicated by ticker.
   - Why: The 21:30 regular session scan is the first scan of the evening and serves as a watch list for AH. Its RVOL/5m-volume filters catch stocks actively spiking but miss stocks that moved significantly during the day and are now winding down. EEIQ (+22.4% day, 860K float) is exactly this pattern. Being on the watch list would have prompted AH monitoring and potential PM tracking.
   - Hypothesis: Next regular session scan (21:30 CET) will include stocks with >15% day change even if their current 5-minute RVOL is below 10x. Specifically, a stock like EEIQ (+22.4%, ultra-low float) will appear in results. Measurable: compare the 21:30 scan results tonight with what would have been caught before. Any stock with >15% day change and <10x 5m RVOL should now appear.

**Updated parameters:** Added `MIN_DAY_CHANGE_REGULAR = 15%` (supplementary regular session filter).

### 2026-03-25 — AH Trajectory Pattern Tracking in Morning Evaluation

**Context:** After 5 days of AH mover follow-through tracking (Mar 17-24), the morning evaluation captures whether AH movers continue into PM but doesn't classify the AH trajectory pattern in a structured, aggregatable way. Recent data shows a potential correlation: steady-build patterns continued to PM while spike-and-fade patterns gave back gains. NXTT (Mar 24) built steadily across 6 scans (+6%→+13%→+15%→+14%→+20%→+23%) and won +19.1% in PM. MDAI (same night) peaked at +11.5% early, faded to +10.9%, and gave back all AH gains by PM. The agent notes these patterns informally but they aren't structured for aggregation ahead of the W13 review.

**Evaluation of previous changes:**
- Learning Phase Paper Trade Default (2026-03-24): **Working (1 data point).** On Mar 24, NXTT met criteria (float 4.9M, >10% AH sustained across 2 scans by 23:00 CET) and was paper traded despite concerns (dead cat bounce, no catalyst). Result: +19.1% win. Hypothesis confirmed: "next qualifying night should produce a paper trade, not 'skip all'" happened immediately. Selection rate improved from 0% to 20% (1/5).
- Catalyst Re-Search (2026-03-20): **Working (2 data points).** Mar 23 EDBL re-searched at 00:00 and 00:30 (no catalyst, genuine absence). Mar 24 NXTT re-searched at 22:30, 23:00, 00:30 (no catalyst, genuine absence). Process followed correctly both times.
- Selection Rate Tracking (2026-03-20): **Working (2 data points).** Both Mar 23 and Mar 24 morning evaluations include the metric. Mar 23: 0/4. Mar 24: 1/5. Making the selection gap visible as intended.

**Changes:**
1. **prompts/morning-evaluation.md** — Added "AH Trajectory" column to the AH Mover Follow-Through table with classification instructions (Build, Spike→fade, Spike→hold, Late surge).
   - Why: 5 days of follow-through data suggest trajectory type predicts PM outcome, but the data is captured as free-text in Verdict, not as a structured category. The W13 review (target in Day Trading.md) will need aggregatable data to identify which AH patterns predict follow-through.
   - Hypothesis: All future morning evaluations will include AH trajectory classification. After 10+ data points (~2 weeks), we expect to see whether trajectory type correlates with PM follow-through rate, enabling the evening scan to prioritize candidates showing building momentum. Measurable: next morning evaluation should include the AH Trajectory column.

### 2026-03-24 — Learning Phase Paper Trade Default

**Context:** After 4 days of baseline tracking (Mar 17-23), the scanner detects 100% of winners (4/4) but the selection rate is near 0%. The morning evaluation on Mar 23 explicitly states: "Entry rules are too conservative: every detected winner was rejected" and "Next session: consider paper trading the top candidate even if extension or catalyst concerns exist, to collect data." The Day Trading.md learning phase says "paper trade and focus entirely on scanner accuracy" and "No hard sector or entry-price restrictions," but the post-market prompt had no mechanism to push toward trading over skipping. Result: 3 of the last 4 nights produced "skip all" outcomes, generating no data to refine entry rules.

**Evaluation of previous changes:**
- Catalyst Re-Search (2026-03-20): **Working (1 data point).** On Mar 23, EDBL was re-searched at 00:00 and 00:30 CET per the new rule. No catalyst was found (genuine absence, not a search failure). The process was followed correctly.
- Selection Rate Tracking (2026-03-20): **Working (1 data point).** Mar 23 morning evaluation includes "Winner selected for paper trade: 0/4 (0%)." Metric is being tracked as intended, making the selection gap visible. (Note: DRMA on Mar 19 was both the winner and was paper traded, so the actual rate may be 1/4 = 25%, not 0/4.)

**Changes:**
1. **prompts/post-market-scan.md** — Added "Learning phase default" paragraph to Step 4 (Paper Trade Decisions), between the evaluation criteria and the regular session caution block. During the learning phase, if by the third AH scan (23:00+ CET) at least one candidate has float <10M and AH change >10% sustained across 2+ scans, paper trade the best available candidate. Concerns should be documented but should not prevent entry. "Skip all" is reserved for nights when no candidate sustains >10% AH across multiple scans.
   - Why: The scanner's detection is solved (4/4 = 100%). The bottleneck is now selection: winners are found but not traded because the agent applies observations (extension, catalyst strength) as hard filters despite the prompt saying they aren't. The learning phase requires paper trades to generate data, but 3 of the last 4 nights produced zero trades. The Day Trading.md already says to paper trade with no hard restrictions; this change makes the prompt match the stated strategy.
   - Hypothesis: Next evening session with at least one candidate meeting the minimum bar (float <10M, AH >10% across 2+ scans) will result in a paper trade entry, even if there are concerns. Selection rate should improve from 0-25% toward >50% over the next week. Measurable: the next qualifying night should produce a paper trade, not "skip all."

### 2026-03-20 — Catalyst Re-Search for Returning Candidates + Selection Rate Tracking

**Context:** On March 17 (HIT) and March 19 (DRMA), catalysts appeared 15-30 minutes after AH opened but weren't found until the 23:00 scan (third AH scan). At the 22:30 scan, returning candidates previously marked "no catalyst" were noted as "still skipped" without re-running the catalyst search. On March 19, DRMA's Benzinga article (patent notice) was published at 4:27 PM ET. The 22:30 scan (4:30 PM ET) could have found it with a re-search, enabling entry at $1.37 instead of $1.45 (5.5% better). Separately, the morning evaluation tracks detection rate (3/3, 100%) but not selection rate (2/3, 67%); the March 18 SUNE miss showed these are different problems.

**Evaluation of previous changes:**
- Structured Catalyst Research (2026-03-19): **Partially working, insufficient data (1 data point).** DRMA on March 19: the structured checklist was followed at 22:00 (checked earnings, press releases, SEC filings; all empty). Catalyst found at 23:00 via Benzinga. The checklist guided the search correctly but the article hadn't been published yet at scan time (4:00 PM ET vs 4:27 PM ET publish). The checklist alone doesn't solve the timing lag for catalysts that appear after 22:00.
- No-Sector-Restriction (2026-03-18): **Working (3 data points).** March 18-19 evaluated all sectors on merit. DRMA (Pharmaceuticals), IDN (Software), MASK (IT Services) all assessed without sector bias.
- AH Mover Follow-Through (2026-03-17): **Working well (3 data points).** Tables generated on March 17, 18, 19. Generating clear signal: entries <25% AH with real catalysts hold into PM (3/3), entries >30% AH fade (2/2).
- Regular Session Entry Guard (2026-03-13): **Confirmed (8+ data points).** March 19: SER, WETO, SUNE, CHNR all flagged Watch at 21:30, none carried into AH. No false entries.

**Changes:**
1. **prompts/post-market-scan.md** — Added catalyst re-search instruction for returning candidates. When a stock was previously skipped for "no catalyst" and still shows >10% AH change in a subsequent scan, the agent must re-run the structured catalyst search instead of repeating the prior skip. Includes note that PRs and news articles frequently appear 15-30 minutes after AH opens.
   - Why: On March 17 and 19, catalysts became findable at the 22:30 scan (30 min after AH open) but the agent didn't re-search, only noting "still skipped." The 22:30 scan's re-evaluation just confirmed the prior skip without looking for new information.
   - Hypothesis: Next time a stock appears with >10% AH change and "no catalyst" at 22:00, the 22:30 scan will re-run the catalyst search and find any catalyst published in the intervening 30 minutes. Measurable: the next catalyst that appears 15-30 min after AH opens should be found at the second scan (22:30) rather than the third (23:00).

2. **prompts/morning-evaluation.md** — Added "Winner selected for paper trade" metric to the Baseline Tracking section, tracking whether the day's winner was the stock we actually traded (not just detected).
   - Why: Detection rate is 100% (3/3) but selection rate is 67% (2/3). March 18's SUNE miss was a selection failure, not a detection failure. Tracking both metrics separately makes this gap visible and measurable.
   - Hypothesis: The selection rate metric will be tracked in all future morning evaluations. Over 2 weeks this builds a dataset showing whether selection is improving alongside detection. Measurable: next morning evaluation should include the new metric.

### 2026-03-19 — Structured Catalyst Research Steps in Post-Market Prompt

**Context:** On March 17, HIT's PR dropped at 22:01 CET but wasn't found until the 23:00 scan (30-min delay). On March 18, SUNE's earnings were released on GlobeNewswire after close (pre-announced March 16) but the agent searched for news and missed it entirely, skipping SUNE as "no catalyst" across all 6 AH scans. SUNE was the day's winner (+22.2% PM from close, least extended of AH movers, low float 3.4M). Meanwhile MDAI was chosen instead (+32.5% entry, lost -8.8%). The March 18 morning evaluation states: "The scanner works; the evaluation/catalyst research is the weak link." The prompt's guidance was just "search for news if needed" with no specifics on where or how.

**Evaluation of previous changes:**
- No-Sector-Restriction Reinforcement (2026-03-18): **Working.** March 18 evening scans evaluated all sectors on merit. MDAI (Medical Specialties), SER (Commercial Services), SUNE (Engineering/Construction) all assessed without sector filtering. SUNE was skipped for "no catalyst", not for sector. First successful test.
- AH Mover Follow-Through (2026-03-17): **Working well (2 data points).** Both March 17 and 18 evaluations include the table. March 18's table revealed only the least-extended mover (SUNE +20.8%) held into PM while MDAI (+32.5%) and SER (+54.7%) faded. Generating actionable insight as intended.
- Regular Session Entry Guard (2026-03-13): **Confirmed (6/6 tests).** March 18: AIM (+43.7%) and ARTL (+50.7%) flagged Watch at 21:30, neither appeared in AH. Guard is now 6/6 on preventing bad entries.

**Changes:**
1. **prompts/post-market-scan.md** — Replaced the vague "Has a clear catalyst (search for news if needed)" criterion with a structured 4-step catalyst research checklist for every AH mover >10%: (1) check if earnings were released today, (2) search GlobeNewswire/PRNewswire/BusinessWire for same-day press releases, (3) check SEC 8-K filings, (4) only mark "no catalyst found" after steps 1-3 fail.
   - Why: Two consecutive days (March 17-18) the scanner detected the winner but the evaluation dismissed it because catalyst research was too shallow. SUNE's earnings release was publicly findable on GlobeNewswire and pre-announced March 16, but the generic "search for news" instruction wasn't specific enough.
   - Hypothesis: The next evening scan with AH movers >10% will perform the structured catalyst search. Specifically, if a stock has after-close earnings (the most common AH catalyst), the search should find it. Measurable: the next stock with an earnings-driven AH move should have its catalyst identified at the first scan it appears in, not missed and labeled "no catalyst."

### 2026-03-18 — Reinforce No-Sector-Restriction in Post-Market Prompt

**Context:** March 16 had ONFO (float 4.1M, +31.4% AH, appeared in 5+ scans) and JVA (float 5.0M, +20.5% AH, earnings beat catalyst) both skipped solely for being "non-biotech (0% win rate)". The prompt already said "Any sector — no sector restriction" but the agent cited the Day Trading.md observation "Non-biotech 0/6" as a hard skip reason. Meanwhile, on March 17 the agent correctly entered HIT (IT Services, non-biotech) with a strong catalyst. The inconsistency shows the prompt wording wasn't strong enough to prevent the observations from being treated as hard rules.

**Evaluation of previous changes:**
- AH Mover Follow-Through (2026-03-17): **Working.** March 17 morning evaluation includes the table with 7 AH movers tracked. Only 1 data point so far. Insufficient data for full evaluation of whether it influences decisions, but the data is being collected as intended.
- Regular Session Entry Guard (2026-03-13): **Confirmed helpful (2nd test).** March 16: HCWB (+81.2%) and NBY (+19.8%) flagged as "Watch" at 21:30 CET. Neither appeared in AH scans. HCWB faded from $0.94 to $0.80 overnight. March 17: UCAR (+62.7%) and JVA (+30.0%) flagged as "Watch" at 21:30. Both lost momentum in AH. Guard is 4/4 on preventing bad entries.

**Changes:**
1. **prompts/post-market-scan.md** — Replaced the sector bullet in Step 4 entry criteria with explicit language: "do NOT skip stocks for being outside biotech/pharma. The 'non-biotech 0/6' observation is a hypothesis under investigation, not a filter." Also updated the pattern-tracking bullet to clarify observations are NOT skip criteria.
   - Why: On March 16, two candidates with good float (<10M) and sustained AH momentum were skipped solely for sector. The trading plan explicitly says "No hard sector or entry-price restrictions" and notes the observations are "NOT hard rules." The prompt needs to match.
   - Hypothesis: The next evening scan with non-biotech candidates meeting all other criteria (float <10M, catalyst, volume) will evaluate them on merit rather than auto-skipping for sector. This will produce paper trade data across sectors, enabling the learning phase to actually test whether sector matters. Measurable: on the next night with non-biotech AH movers with catalysts and low floats, at least one should get a paper trade entry (or a substantive skip reason other than sector).

### 2026-03-17 — Add AH Mover Follow-Through Section to Morning Evaluation

**Context:** The March 16 morning evaluation included an ad hoc "AH Mover Follow-Through" table tracking how AH movers performed into premarket. This analysis showed 7/8 AH movers faded from their peaks (LIDR -13%, ONFO -14.8%, HCWB -14.9%, DCGO -5.5%, NCPL -10.3%), with only WNW continuing higher. This is directly relevant data for the core trading hypothesis (enter AH → exit PM), but the morning evaluation prompt didn't include it — the agent added it on its own initiative on March 16 only.

**Evaluation of previous changes:**
- Regular Session Entry Guard (2026-03-13): **Helped.** First real test on March 16. HCWB (+81.2%) and NBY (+19.8%) were flagged as "Watch — pending AH confirmation" at 21:30 CET. Neither appeared in any AH scan → correctly dropped. HCWB faded from $0.94 to $0.80 overnight (-14.9%). The guard prevented what would have been a loss.
- Day% prompt integration (2026-03-12): Working. Day% column appears in all AH tables consistently. No stock has triggered the combined Day%+AH% > 50% check yet. Insufficient data for full evaluation.

**Changes:**
1. **prompts/morning-evaluation.md** — Added "AH Mover Follow-Through" subsection to the log template (between Missed Opportunities and Notes). Instructs the agent to track every stock that appeared in 2+ evening scans with AH change >10%, showing AH peak, peak time, current PM price, fade from peak, and change from prev close.
   - Why: This analysis was done ad hoc on March 16 but not on March 10, 11, or 12. It directly measures the core trading hypothesis (AH momentum → PM continuation). Making it explicit ensures consistent data collection.
   - Hypothesis: Every future morning evaluation will include AH→PM follow-through data. Over 2 weeks, this builds a dataset of ~30-50 AH movers with PM outcomes, enabling data-driven conclusions about which AH patterns carry through. Measurable: next morning evaluation should include the AH Mover Follow-Through table even on days with no paper trades.

### 2026-03-13 — Regular Session Entry Guard in Post-Market Prompt

**Context:** March 12 paper trades (SPRC -18.6%, AEMD -4.6%) were both entered during the 21:30 CET scan — regular session, 30 min before market close. Neither stock appeared in any subsequent AH scan. The trading plan says "enter in AH" but the prompt treated regular-session candidates identically to AH candidates, allowing immediate paper trade entries. This is the third consecutive daily loss from questionable entries (March 9: ACXP -29.5% at AH peak, March 12: two regular-session entries that faded). Paper trade record: 1W/3L.

**Evaluation of previous changes:**
- Day% prompt integration (2026-03-12): **Working as intended.** March 12 AH tables include Day% column. CODX was correctly evaluated using Day% (-18.8%) + AH% (+44.1%) to calculate total move from prev close (~+17%). No stock triggered the 50% rule through Day%+AH% combo that night, so the filter hasn't been stress-tested yet. Insufficient data for full evaluation.
- Day% scanner column (2026-03-11): **Complete.** Column appears in terminal output and prompt-generated tables. No issues.

**Changes:**
1. **prompts/post-market-scan.md** — Added "Regular session caution" block to Step 4 (Paper Trade Decisions). When the scan runs before AH opens (21:30 CET / before 4:00 PM ET), candidates are flagged as "Watch — pending AH confirmation" instead of entering paper trades. Trades are only entered from AH scans (22:00+ CET).
   - Why: 2/2 regular-session paper trades on March 12 lost money. Both stocks had intraday spikes that didn't carry into AH. The trading plan requires AH entries, but the prompt allowed immediate entry from regular-session scans.
   - Hypothesis: Regular-session candidates that don't reappear in AH scans will be correctly skipped, preventing premature entries. Measurable: next 21:30 CET scan should show "Watch" flags instead of paper trade entries. If a candidate from a regular scan doesn't appear in AH, no paper trade should be placed.

**Updated process:** Regular session scans now produce "Watch" candidates, not paper trade entries.

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
