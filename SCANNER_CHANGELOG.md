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
MAX_MARKET_CAP = 300,000,000 ($300M)
MIN_AH_VOLUME = 50,000
MIN_AH_CHANGE = 5%
MIN_AH_CHANGE_HIGH = 20%  (supplementary high-change scan, catches data gaps)
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
- Entry rules: float <50M, first day of unusual volume (sector and price thresholds are observations under review, not hard rules)
- **No-catalyst handling:** enter with concern noted (any float). "No catalyst" is a concern to document, not a skip reason. Float tracked for pattern analysis, not as filter.
- **Extended-hours volume & bad-print detection use Alpaca SIP bars, not Yahoo volume** — Yahoo's 5-min AH/PM bars report no volume for any ticker (real or phantom), so `--ah-history`/`--pm-history` show `Vol: n/a`; Yahoo zero-volume bars are not evidence of anything. For real ext-hours volume use `node scripts/broker.js bars SYM --tf 5Min --start <AH-start-UTC>` (defaults to the SIP consolidated feed — full-market vol + `vwap` + `trades`; free tier serves SIP historical, only last ~15 min blocked). Detect Yahoo bad prints by comparing the Yahoo AH/PM high vs the SIP high/VWAP (Yahoo high >> SIP = bad tick, trust SIP); cross-check the live book (`broker.js quote`, `ask $0.00 x0` = no fillable liquidity). Basis: JEM Jun 30 Yahoo AH $12.67 vs SIP high $4.54 / VWAP $4.27 on 1.5M shares — JEM traded heavily, the $12.67 was a Yahoo bad print. **Yahoo also mis-reports in the other direction — it under-counts real AH/PM *peaks* on illiquid low-float names**, so for any traded name / winner, verify the AH/PM peak against the SIP `H` and use the higher SIP peak when it is backed by real `vol`/`trades` (basis: DCX Jul 8, Yahoo PM high $1.48 vs SIP $1.63 on 1.8–2.5M sh/bar; under-reporting the peak understates the gain that was available)
- **SIP volume confirmation at entry** — before sizing, confirm the TradingView VRatio spike is *real* with `broker.js bars SYM --tf 5Min --start <AH-start-UTC>` (SIP): AH volume must be accumulating on real trades across bars (not a single stale figure) and SIP high/VWAP must corroborate the scanner AH price (far-above = bad print → skip). Discovery stays TradingView (only whole-market screener); SIP + book are the confirmation layer. All three pulse prompts (post-market-scan, morning-evaluation, position-evaluation) carry a "Data Sources (read first)" preamble so every pulse applies this hierarchy from its first action
- **Quote-freshness guard on open-position P&L** — before the morning eval reports an open position's Alpaca unrealized P&L, it checks the `broker.js quote` timestamp; a stale `current_price` (free tier often returns the prior 20:00 ET regular close on an ext-hours-active name) is cross-checked against the live overnight/PM price (SIP bars / Yahoo `--pm-history`) and the stale figure is flagged as not tradeable rather than reported as a real loss/gain (basis: SEER Jul 3, Alpaca $1.62 / −28.3% stale close vs ~$2.30 overnight +1.8%). Same guard already applied at entry and exit.
- **Verification freshness guard (no false bad-print on stale data)** — before rejecting a *strong* scanner signal (high VRatio + large AH% + built across ≥2 AH scans) as a bad print, confirm the SIP bars/quote are actually fresh (last bar/quote timestamp near the scan time). If the verification source is stale (e.g. last SIP bar 16:44 ET while scanning at 18:30 ET), a "scanner price >> SIP high" divergence is a staleness artifact, not a bad print — re-pull once, else treat the scanner reading as unconfirmed-but-live (do not skip as bad print), lean on the real-time book, prefer waiting for the next scan. Also treat a discontinuous AH% jump between consecutive scans (e.g. −8% → +214% in one step) as a feed-lag artifact to re-verify. (Basis: USDE Jul 1, real +180% AH winner detected at 00:00/00:30 CET but wrongly skipped — TradingView lagged ~30 min and SIP/quote returned stale 16:44 ET data, firing a false bad-print call.)
- **AH-liquidity sanity check before entry** — confirm `broker.js quote` shows a real two-sided after-hours book (non-zero ask price with size, non-zero bid) before sizing an order; an `ask $0.00 x0`/zero-size book means the TradingView `AH Vol`/`VRatio` is stale regular-session volume, not real AH liquidity — skip as illiquid (basis: TII Jun 26 VRatio 4.9x but `ask $0.00 x0`; recurring NEXR zero-AH-volume ramp pattern)
- **No paper trades before 23:00 CET** — 22:00 and 22:30 scans are observation only
- **AH change >10% in at least 2 after-hours scans** (regular session appearances don't count)
- Trajectory preference: build/hold patterns preferred over spike→fade; **trajectory overrides catalyst when patterns clearly diverge** (0/7 early-peak-fading vs 5/5 BUILD); **AH peak timing is a secondary tiebreaker — hold-vs-fade dominates:** early-peakers that *also fade* are 0/6+ (OCG, CNET, FOXX, ANY), peaks after 18:30 ET are 4/4 wins, but before-18:30 BUILD-and-hold names still follow through (CHAI 17:20, MSW 18:00); at later scans (00:00+ CET), prefer stocks near their AH high over early-peakers now fading; **skip all on SPIKE→FADE-only nights** (0/10+ win rate)
- **Skip dead-cat bounces** — stocks with Day% below -15% are excluded even if AH bounce is strong. **Dead-cat-override watch:** a Day% ≤ -15% candidate that BUILDS in AH to reclaim *above its regular close* (AH% rising across ≥2 scans) is not a dead-cat bounce; still skipped from live entry but flagged DEAD-CAT-OVERRIDE WATCH with a hypothetical entry for data collection (basis: BYAH Jun 11, hypothetical +72%)
- **Early-peak base-hold requires holding within ~20% of the AH high** (or making new highs); a deep collapse (>20% off the AH high) that stabilizes at a much lower base is a fade, not a hold, especially on Grade-None macro/sector-beta names (basis: SKYQ Jun 10 +129% peak → +46% rebuild → -27.6%)
- **Entry extension ceiling: 150% Total%** — skip candidates extended >150% from previous close; if only 23:00 candidate exceeds 150%, wait for later scans (late-building candidates often have better entry points). **Ceiling-override watch:** candidates that exceed 150% but show BUILD-and-hold (AH high after 17:00 ET, holding within ~20% of high across ≥2 scans, VRatio >5x) are still skipped but flagged with a hypothetical entry for data collection.
- Morning retrospective uses Yahoo AH history as the primary source; forced AH scans are secondary diagnostics only
- **PM-only gapper tracker:** each morning eval classifies the biggest raw PM mover as an AH→PM continuation (detectable) or a PM-only gapper (flat/down in AH, undetectable), with a running tally. **Each PM-only gapper is also labelled holdable vs uninvestable** (a sustained gain over ≥2 consecutive 5-min bars on real volume = holdable; an instant crash or single thin tick = uninvestable) — the blind spot only has real cost if the gappers are holdable. PM-only gappers are a structural blind spot of the AH→PM strategy, not a detection-baseline failure (data collection: CIIT Jun 10, GLXG Jun 11, TDIC Jun 16, MBRX Jun 23 uninvestable, CUPR Jun 24 thin print)
- **Late-AH-tail surge tracker:** each morning eval checks whether the winner's defining AH surge fired *after* the last scheduled scan (after 18:30 ET / 00:30 CET, before 04:00 ET PM open) in the unscanned 18:30–20:00 ET after-hours tail, with a running tally. Distinct from a PM-only gapper (the stock has an AH footprint); not a detection-threshold miss, not counted against baseline. Dataset for deciding whether to add late scans (~01:00/01:30 CET) — a scheduling decision left to the user. **Each case is sub-classified feed-lag vs true-tail:** feed-lag = already over the 10% AH threshold at the 18:30 ET last-scan timestamp but the live feed missed it (fix is data-source verification, not a late scan); true-tail = genuinely under threshold at 18:30 ET and surged after (only these argue for an added late scan) (data collection: ORIS Jun 22 true-tail surge 19:25 ET +54% hypothetical; BTCT Jun 29→30 feed-lag, already +67.6% at 18:30 ET, +47% hypothetical)
- **Fade-rule false-negative tracker:** each morning eval records any candidate skipped on the SPIKE→FADE / early-peak-fade rule that then re-exploded in premarket (PM peak above its AH peak and above a profitable entry), with a running tally (float + catalyst grade per case). The re-ramp is **float-conditional**: the trigger to propose the exception is **≥4/5 *sub-3M-float* AH-faders re-exploding** (higher-float faders — LIQT 24.2M, TGE 44.2M — keep fading and are the negative control, not counted toward the trigger). At the trigger, propose a sub-3M-float PM-open re-check exception to the fade skip. **Standing sub-3M count: 3 of 4** (LNKS/RPGL/CRE blew past, IOTR fell short); one more sub-3M re-ramp reaches the threshold (data collection: CRE Jun 17, LNKS Jun 18, IOTR Jul 7, RPGL Jul 9)
- **Reverse-split-squeeze fade tracker:** each morning eval records, for every entered/notable name whose catalyst is a reverse stock split (not a fresh operational catalyst), whether it faded overnight or continued, plus split ratio, split recency (this-week vs months-old), float, and entry→PM-peak P&L, in a running tally. A reverse split is a listing-compliance/distress signal (manufactured low float), not isolated by the catalyst-grade or float trackers. Data collection, no gate change — dataset for deciding whether reverse-split recency should downgrade entry conviction (data collection: ELPW Jul 10 1:80 faded −17.8%, YYGH Jul 10 30:1 faded −17.5%, EDHL Jul 6 1:16 months-old +6% mild, DCX Jul 8 flat)
- **Scan-coverage check:** each morning eval verifies how many of the 7 scheduled evening scans actually ran (count `## Scan` sections / git commits), records `Evening scans ran: X of 7`, and keeps a coverage-failure tally in Notes. On a night the scanner did not cover the entry window, the night's winner is **not** counted as a detection miss and selection is not penalized — it is logged as a coverage failure, not a threshold gap (founding case: Jun 18–19, only 2 of 7 scans ran)

## Modifiable Files

- `scripts/scan.py` — Scanner parameters, filters, output columns
- `scripts/check-prices.py` — Price checking utility
- `prompts/post-market-scan.md` — Evening scan prompt (evaluation criteria, log format)
- `prompts/morning-evaluation.md` — Morning evaluation prompt

## Change Log

_(entries are prepended — newest first)_

### 2026-07-10 — Add a Reverse-Split-Squeeze Fade Tracker (Isolate Manufactured-Float Distress From Catalyst Grade)

**Context:** Jul 9→10 was a clean, full-coverage night (7/7 scans). Detection baseline 88.6% (39/44, BASELINE MET), selection 50.0%. The winner **GMM** (tiny-float 1.7M AI-metaverse squeeze, SIP AH peak $3.50 +80% @19:00 ET → PM peak $4.07 +120%) was a **late-AH-tail true-tail surge** — flat through 17:45 ET, volume-confirmed explosion (925K sh/7,621 trades @18:40 ET) fired *after* the 00:30 CET last scan, so correctly not surfaced and not counted against baseline (true-tail count now 2: ORIS, GMM; threshold to propose a late scan is ≥3–4, a scheduling call left to the user). The scanner and every gate did their job — no in-scope detection/threshold defect. The three real entries all **faded** overnight and were exited in the morning position eval: **ELPW** ($1.18 Grade D, 1-for-80 reverse split) −17.8%, **PMA** ($1.66 Grade C, convertibles) −10.8%, **YYGH** ($1.66 Grade None, 30-for-1 reverse split) −17.5% (net −$45.05). The one recurring, in-scope, data-backed signal: **the two worst performers were both fresh reverse-split names** (ELPW 1:80, YYGH 30:1), and reverse splits recur in the majority of recent logs (30+ log files, e.g. EDHL 1:16, DCX, RPGL, DSY). A reverse split is a listing-compliance/distress signal — the ultra-low float is *manufactured*, not organic scarcity — and is not isolated by the existing catalyst-grade or float trackers (these names get bucketed generically as Grade None/D + tiny float). Holding/exit timing on these is the user's domain (covered by the separate strategy Init-6 exit-cost work); the in-scope move is a data-collection tracker to test whether reverse-split *recency* predicts the fade.

**Evaluation of previous changes:**
- 2026-07-09 Float-conditional fade-rule trigger: **Working — validated.** The Jul 10 morning eval applied the float condition: **WNW** (float 23.7M) faded as predicted and was explicitly logged as the **high-float negative control** (not counted toward the sub-3M trigger); ELAB (4.5M) faded. No new sub-3M case; standing sub-3M count held at **3 of 4**. The trigger scored against the sub-3M bucket exactly as designed — a higher-float fader was excluded, not counted.
- 2026-07-08 Verify PM peaks against SIP (Yahoo under-reports): **Working.** GMM's AH and PM peaks were both reported as **SIP** figures (AH $3.50 vs Yahoo $3.33; PM $4.07 SIP) with the Yahoo divergence noted; no Yahoo under-reported peak printed as fact.
- 2026-07-03 Quote-freshness guard on P&L: **Working — validated across pulses.** The morning eval and the 10:30 position eval both flagged Alpaca `quote` as stale (20:00Z close) and reported P&L against live SIP 5Min bars (ELPW/PMA/YYGH). No stale Alpaca figure printed as a real loss.
- 2026-07-02 Verification freshness guard (entry flow): **Insufficient data (still open).** No stale-verification bad-print case Jul 9; entries were SIP-confirmed real. Not exercised.
- 2026-07-01 (c) SIP volume confirmation: **Working.** GMM's late surge was confirmed real on SIP (925K sh/7,621 trades/bar) in the retrospective; entries sized only after SIP corroboration.
- Ceiling + dead-cat + late-AH-tail gates (Jun lineage): **Working.** GMM correctly classified true-tail (not a baseline miss); no ceiling/dead-cat breach; late-AH-tail true-tail count advanced to 2.

**Changes:**
1. **prompts/morning-evaluation.md** — Added a **reverse-split-squeeze fade tracker** to the Notes trackers (after the late-AH-tail tracker): for each entered/notable name whose catalyst is a reverse stock split rather than a fresh operational catalyst, record faded vs continued, split ratio, split recency (this-week vs months-old), float, and entry→PM-peak P&L, in a running tally. Seeded with ELPW, YYGH (both faded −17%, this-week splits), EDHL (months-old 1:16, mild +6% continue), DCX (flat). Explicitly a data-collection tracker, no gate change.
   - Why: reverse splits recur constantly in the logs and the two freshest reverse-split entries were the two worst performers last night, yet reverse-split structure is not isolated by any existing tracker (it hides inside generic Grade None/D + low float). A manufactured post-split float behaves differently from organic scarcity; recency (active distress) is the hypothesized discriminator.
   - Hypothesis: post-reverse-split squeezes with no fresh catalyst systematically fade, and split *recency* predicts the fade better than catalyst grade or float alone. Measurable: (1) each future reverse-split entry logs faded/continued + ratio + recency in the tally; (2) after ~5–6 cases the this-week-split vs months-old split fade rates diverge (or don't). If this-week splits fade materially more than months-old splits, it argues for a recency-based conviction downgrade; if not, the structure adds no signal beyond grade/float and the tracker is retired. If a future reverse-split entry is logged without the recency annotation, the change didn't take.

**Updated process:** Morning eval now carries a reverse-split-squeeze fade tracker (data collection, no gate change). (No scanner parameters changed.)

### 2026-07-09 — Make the Fade-Rule Exception Trigger Float-Conditional (Align Trigger With the Hypothesis)

**Context:** Jul 8→9 was a clean, full-coverage night (7/7 scans). Detection baseline 88.6% (39/44, BASELINE MET), selection 50.0%. One real entry, **SUNE** ($2.56, Grade None, BUILD-and-hold, VRatio 6.8x, AH>10% ×2, SIP-confirmed real accumulation), exited −4.7% next premarket per the Grade-None rule. The winner, **RPGL** (low-float 1.1M, Grade C Nasdaq-compliance PR), was detected in all 5 entry scans and **correctly skipped SPIKE→FADE** at live-entry time (AH% declined 23:00 +42.1% → 00:30 +33.1%, peaked $2.69 @17:05 ET, faded ~12% off high on collapsing volume) — then re-exploded to a SIP PM peak $3.05 (+69.4%). The scanner and every gate did their job; no detection miss, no threshold gap. The one in-scope, data-driven signal is in the **fade-rule false-negative tracker**: RPGL is the 4th low-float AH-fader logged, bringing the **sub-3M-float** re-ramp split to **3 of 4** (LNKS 1.5M, RPGL 1.1M, CRE blew past; IOTR 644K fell short). The morning eval computes this low-float split by hand every morning and flags a sub-3M PM-open re-check as the leading candidate change — but the *codified* trigger in the prompt was still a **blanket** "≥4/5 AH-faders re-exploding" count, which contradicts the tracker's own stated hypothesis (the exception should be *low-float-conditional*). That mismatch means the trigger could fire on the wrong evidence (e.g. counting higher-float faders that keep fading). Aligning the trigger with the hypothesis is the surgical fix; actually relaxing the fade rule is not yet warranted (still 3/4, one short of threshold, and being conservative).

**Evaluation of previous changes:**
- 2026-07-08 Verify PM peaks against SIP (Yahoo under-reports): **Working — validated.** The Jul 9 morning eval reported RPGL's PM peak as SIP **$3.05** (noting Yahoo under-reported $2.89) and SUNE's as SIP **$2.72**, and the AH peak as SIP $2.69 (Yahoo $2.53). Every peak in the retrospective used the SIP figure with the Yahoo divergence noted; no Yahoo under-reported peak was printed as fact. The cross-check took.
- 2026-07-07 Catalyst-override annotation on the fade-rule tracker: **Working.** RPGL was annotated **Grade C** and placed in the general/weak-catalyst fade tally (not the strong-catalyst A/B subset); the eval explicitly noted its re-ramp was float-driven, not catalyst-driven, and that strong catalysts still have NOT rescued fades (ALGS remains the only A/B case). Annotation applied as designed.
- 2026-07-03 Quote-freshness guard on morning-eval P&L: **Working.** Both the 10:20 morning eval and the 10:30 position eval flagged the Alpaca `quote` endpoint as stale (20:00Z close) and reported SUNE P&L against live SIP PM levels ($2.42 ≈ live SIP $2.44). No stale figure printed as a real loss.
- 2026-07-02 Verification freshness guard (entry flow): **Insufficient data.** No stale-verification bad-print situation Jul 8; SUNE was SIP-confirmed real at entry, RPGL/LIQT fades confirmed on fresh SIP. Guard not exercised. Still open.
- 2026-07-01 (c) SIP volume confirmation: **Working.** SUNE sized only after SIP corroboration (1M+ sh/bar, VWAP $2.65 corroborating scanner AH). RPGL/LIQT fades and thin names (AP, IOTR) confirmed on SIP before skipping.
- Ceiling + dead-cat + fade gates (Jun lineage): **Working.** RPGL/SUNE well under the +150% ceiling; JLHL dead-cat (Day −29.2%, never reclaimed close) correctly skipped; RPGL SPIKE→FADE skip was the disciplined call (the re-explosion is the tracked false negative, not a gate failure).

**Changes:**
1. **prompts/morning-evaluation.md** — Made the fade-rule exception **trigger float-conditional**: replaced the blanket "only a recurring pattern (≥4/5 AH-faders re-exploding) would warrant a change" with **≥4/5 *sub-3M-float* AH-faders re-exploding** (higher-float faders — LIQT 24.2M, TGE 44.2M — are the negative control and do not count toward the trigger), and recorded the standing sub-3M count (**3 of 4**) plus the concrete exception to propose at threshold (a sub-3M-float PM-open re-check of SPIKE→FADE skips). Also added IOTR (Jul 7, fell short) and RPGL (Jul 9, blew past) to the known-cases seed so the prompt is self-contained.
   - Why: the tracker's hypothesis says the exception should be low-float-conditional, but the codified trigger counted *all* faders — a mismatch that could fire on the wrong evidence. The eval already computes the sub-3M split by hand each morning; codifying it removes the ambiguity from the now-imminent decision (3/4, one short).
   - Hypothesis: the next fade-rule false-negative is scored against the **sub-3M-float** trigger, not a blanket count. Measurable: (1) the next AH-fader that re-explodes is bucketed sub-3M vs higher-float, and only a sub-3M case moves the trigger count; (2) a higher-float fader that re-ramps is logged but explicitly excluded from the trigger. If a future eval advances the trigger on a higher-float fader, the alignment didn't take.

**Updated process:** Fade-rule false-negative tracker's action trigger is now float-conditional (≥4/5 *sub-3M-float* faders re-exploding; higher-float faders are the negative control). Standing sub-3M count 3/4. (No scanner parameters changed.)

### 2026-07-08 — Verify PM Peaks Against SIP (Yahoo Under-Reports the Real Peak on Traded Low-Float Names)

**Context:** Jul 7→8 was a clean, full-coverage night (7/7 scans). Detection baseline 88.4% (38/43, BASELINE MET), selection 51.2%. Winner **IOTR** was detected in all 4 entry scans and correctly skipped SPIKE→FADE (PM peak $4.52 fell *short* of AH peak $4.65 — the fade skip was vindicated). Two real entries — **DCX** ($1.34, Grade None) and **VEEE** ($6.28, Grade C) — both exited small in premarket (DCX +3.7%, VEEE −1.8%). The scanner and gates did their job; no threshold gap (no detection miss, ceiling/dead-cat/fade rules all fired correctly). Touching scanner params would be guessing against a working system. The one real, in-scope defect is a **data-quality gap in the morning-eval PM-peak lookup**, and it lands squarely on Juan's Jul 7 steer ("catch/measure the BIG win, not a clean 6%"): the morning eval reported DCX's PM peak as **$1.48 (+10% over entry)** off Yahoo `--pm-history`, but the real SIP PM high was **$1.63 (+21.6%)** in the 04:00/04:10 ET bars on **1.8–2.5M sh/bar, 12.5k trades** — a real, liquid print, not a bad tick. Yahoo's 5-min extended-hours *high* silently **under-counts** real intra-bar peaks on the illiquid low-float names we trade. This is the mirror image of the codified Yahoo *over-report* bad-print (JEM $12.67): the retrospective already cross-checks AH levels against SIP for over-reporting, but the **PM-peak** step still trusted Yahoo alone. Under-reporting the peak systematically understates how much gain was on the table, biasing the let-winners-run analysis (the exact thing Juan wants measured) low.

**Evaluation of previous changes:**
- 2026-07-07 Catalyst-override annotation on the fade-rule tracker: **Insufficient data (still open).** No Grade-A/B fader was skipped on SPIKE→FADE on the Jul 7 night — the only fade-tally add was IOTR (Grade **None**), and its PM peak fell short of its AH peak (fade skip correct). The strong-catalyst annotation was not exercised; tracker recorded the no-catalyst case. Still open.
- 2026-07-03 Quote-freshness guard on morning-eval P&L: **Working — validated again.** Both morning eval (10:20) and both position evals (10:30 / 14:30 CET) flagged Alpaca `quote`/`positions` as returning a stale 20:00Z close and reported P&L against live SIP PM prices instead ("used SIP PM bars for live levels"). No pulse printed a stale Alpaca figure as a real loss/gain.
- 2026-07-02 Verification freshness guard (entry flow): **Insufficient data.** No stale-verification bad-print situation Jul 7 — DCX/VEEE spikes were SIP-confirmed real at entry (freshness guard applied on the stale `ask $0.00 x0` quotes: entered on the thousands-of-trades-per-bar live book, no false bad-print skip). Guard held where it did apply; the strong-signal-stale-data case did not arise.
- 2026-07-01 (c) SIP volume confirmation: **Working.** Both entries were sized only after SIP corroboration (DCX 1.06–1.58M sh/bar building to new high $1.55 @17:16 ET; VEEE new AH high $7.31 @17:25 ET on real volume). FRGT/IOTR fades and VTAK's non-unusual VRatio all confirmed on SIP before skipping. No entry against a stale-VRatio/bad-print name.
- Ceiling + dead-cat + fade gates (Jun lineage): **Working.** IOTR skipped SPIKE→FADE (correct — PM < AH peak); WFF/RDGT dead-cats skipped; no ceiling breach. No override trigger fired.

**Changes:**
1. **prompts/morning-evaluation.md** — Extended the SIP cross-check to the **PM peak**. (a) In Step 2's extended-hours/bad-print note, added the *under-report* direction: Yahoo under-counts real peaks on low-float names, so for any traded name / today's winner, verify the AH/PM peak against the SIP `H` and use the SIP peak when it is above the Yahoo high and backed by real `vol`/`trades`. (b) In the Open Position P&L **PM Peak** template note, required verifying the `--pm-history` peak against `broker.js bars ... --tf 5Min --start <PM-date>T08:00:00Z` and reporting the higher SIP peak. Both cite DCX Jul 8 ($1.48 Yahoo vs $1.63 SIP).
   - Why: the morning eval's PM-peak figure feeds the AH-peak-vs-PM-peak check, the fade-rule/PM-only-gapper trackers, and every "gain available" number. Yahoo systematically under-reports that peak on the low-float names we actually trade, so the whole let-winners-run dataset was biased low — the opposite of what Juan asked to measure.
   - Hypothesis: PM peaks reported by the morning eval match the SIP-verified real peak, not the (lower) Yahoo `--pm-history` high. Measurable: (1) the next traded/winner name whose SIP PM high exceeds its Yahoo `--pm-history` high has the **SIP** peak reported (with the divergence noted); (2) names where Yahoo and SIP agree are unaffected. If a future eval again reports a Yahoo PM peak that a same-day SIP bar clearly exceeds on real volume, the cross-check didn't take.

**Updated process:** Morning-eval PM/AH peak reporting now cross-checks Yahoo `--pm-history` against SIP bars and uses the SIP peak when Yahoo under-reports it on a real, volume-backed print (mirror of the existing Yahoo over-report bad-print check). (No scanner parameters changed.)

### 2026-07-07 — Formalize the Catalyst-Override Watch Into the Fade-Rule Tracker

**Context:** July 5→6 was a clean, full-coverage night (7/7 scans). Detection baseline 88.1% (37/42, BASELINE MET), selection 52.4%. One real entry: **EDHL** at $4.81 (Grade None, low-float double-pump BUILD/HOLD, new AH high $5.54 @17:05 ET, VRatio 4.9x on real SIP volume) — exited +6.0% next premarket per the Grade-None exit rule (PM peaked $6.29, +31% over entry, but the exit rule is the user's domain). No true detection miss; the winner (TDIC) was surfaced (00:30 scan) and correctly skipped (dead-cat, first-appearance), its winning leg an unforecastable overnight PM re-ramp. The scanner and gates did their job; touching thresholds would be guessing against a working system. The one in-scope, data-driven observation: the eval ran a **"catalyst-override watch"** on ALGS (Grade-A $25M China license deal, skipped SPIKE→FADE; outcome "catalyst did NOT overcome the early fade," AH peak $7.46 > PM peak $6.66, hypo −5%) — the 5th log mention of this ad-hoc watch, which validates "trajectory overrides catalyst" but is **not** a codified tracked field anywhere. The fade-rule false-negative tracker already records each fader's float; catalyst grade is the natural missing dimension. Folding it in (rather than adding a separate tracker) is the surgical fix.

**Evaluation of previous changes:**
- 2026-07-03 Quote-freshness guard on morning-eval P&L: **Working — validated twice.** The Jul 6 morning eval explicitly checked staleness on both open positions and reported live prices, not stale Alpaca marks: "EDHL current ~$5.00 (live... P&L not stale)" and "SEER current ~$2.13–2.17 (SIP PM confirms live, not stale)." The Jul 7 position eval independently applied it: "Alpaca `quote` endpoint returned stale data (yesterday 20:00Z close); used SIP 1-min bars for real-time PM price instead." No morning-eval or position-eval P&L line printed a stale Alpaca figure as fact. The guard took across both pulses.
- 2026-07-02 Verification freshness guard (entry flow): **Insufficient data this cycle.** No stale-verification bad-print situation Jul 6 — EDHL's spike was SIP-confirmed real at entry, ALGS/LGPS/NIVF faders were confirmed fades on fresh data. No false bad-print fired; guard not exercised. Still open.
- 2026-07-01 (c) SIP volume confirmation: **Working.** EDHL was sized only after SIP corroboration (16:15 ET 167K sh/3,359 trades, 17:05 ET 219K sh/3,487 trades, VWAP $5.07–5.54, two-sided book). ALGS SIP peak verified $7.46 @16:05 ET before the fade skip. No entry against a stale-VRatio/bad-print name.
- Ceiling + dead-cat gates (2026-06-09 / 2026-06-12 lineage): **Working.** TDIC (dead-cat, Day −25.5%, never reclaimed close in AH) correctly skipped; JLHL/GVH deep dead-cats skipped. No override trigger fired (none reclaimed above close). Watches remain open.
- 2026-06-30 feed-lag/true-tail split: **Insufficient data (still open).** No late-AH-tail case Jul 6 (TDIC's AH peak 18:00 ET was inside the scanned window; the 00:00 scan feed-lagged and it surfaced at 00:30 — logged as a feed-lag detection nuance on a dead-cat skip, not a tail surge). Tracker recorded "none."

**Changes:**
1. **prompts/morning-evaluation.md** — Extended the **fade-rule false-negative tracker** to also record each skipped fader's **catalyst grade** (A/B/C/D/None), and added a **catalyst-override annotation** sub-rule: for every strong-catalyst (Grade A/B) fader the SPIKE→FADE rule skips, record whether the catalyst overcame the fade (PM peak vs AH peak, hypo first-sighting-entry → PM-peak P&L), tracked separately from no-catalyst faders. Seeded with the founding data point ALGS (Jul 6, Grade A, hypo −5%, faded further). This formalizes the ad-hoc "catalyst-override watch" the logs have run 5+ times.
   - Why: the eval keeps running this watch by hand without a durable dataset. Catalyst grade is the one dimension the fade-rule tracker was missing; folding it into the existing tracker (vs a new tracker) avoids over-instrumentation while capturing the data needed to decide whether the fade rule ever warrants a strong-catalyst exception.
   - Hypothesis: every future strong-catalyst fader gets a recorded catalyst-grade + overcame/faded outcome in the fade-rule tally. Measurable: (1) the next Grade-A/B SPIKE→FADE skip logs its catalyst grade and PM-vs-AH outcome in the tally; (2) after ~5–6 strong-catalyst faders the split is known — a cluster that re-explodes argues for a catalyst exception to the fade rule, a cluster that keeps fading further validates trajectory-overrides-catalyst. If a future strong-catalyst fader is logged without the catalyst-grade annotation, the change didn't take.

**Updated process:** Fade-rule false-negative tracker now records catalyst grade per fader and carries a strong-catalyst catalyst-override annotation (the ad-hoc "catalyst-override watch" is now codified). (No scanner parameters changed.)

### 2026-07-03 — Quote-Freshness Guard on Morning-Eval Open Position P&L (Stop Reporting Stale Alpaca P&L as Fact)

**Context:** Jul 2→3 was a clean, full-coverage night (7/7 scans), detection baseline 87.8% (36/41). One real entry: **SEER** at $2.26 (Grade A — CEO $2.45/sh buyout proposal + activist proxy contest, 2-AH-scan qualifier, HOLD near AH high, VRatio 5.7x on real SIP accumulation). The scanner and entry gates did their job. The one in-scope defect surfaced in the **morning-eval readout**, not the scanner: the 10:20 CET morning eval's "Open Position P&L" table reported SEER at **$1.62 / −28.3% 🔴** as fact. That $1.62 was Alpaca's **stale** `current_price` — timestamped Jul 2 20:00 ET (the prior regular close, bid $1.39 / ask $1.62) — while SEER actually re-spiked overnight to ~$2.30 (peak $2.34 @23:20 ET, +1.8% vs entry). The 10:30 position-evaluation pulse caught the staleness correctly (it has a freshness guard and resolved the conflict, HOLD), but the morning eval one pulse earlier printed the stale −28.3% as a real loss. Same defect class as the 2026-07-02 entry-flow freshness guard and the 2026-07-01 USDE stale-verification miss — the guard existed for entries and exits but was **not mirrored** in the morning-eval P&L step, which still said only "note the unrealized P&L Alpaca reports." Touching scanner thresholds would be guessing against a working system (ZCMD +445%→−4.5% just validated the ceiling); this is the real, data-driven, in-scope fix.

**Evaluation of previous changes:**
- 2026-07-02 Verification freshness guard (entry flow): **Working.** The 00:00 CET SEER entry log explicitly applied it — "Quote stale (16:00 ET, ask=$1.62=regular close) — freshness guard: stale-not-contradicting, real live liquidity confirmed by fresh SIP bars" — and entered on the SIP-confirmed BUILD/hold rather than skipping on the stale quote. The guard took at entry. This entry mirrors the same guard into the morning-eval P&L readout, the one place it was missing (the *same* stale $1.62 then bit the 10:20 P&L line).
- 2026-07-01 (c) SIP volume confirmation: **Working.** FXHO's real +168% AH spike was correctly identified as *real* (SIP 173.6K sh / 7,789 trades @16:10 ET corroborating the $19.30 print), not a bad print — then skipped on the −25% Day% dead-cat gate + first-AH-scan. No bad-print false-negative tonight. SEER's scanner AH $2.18 was SIP-corroborated ($2.16–$2.21) before sizing.
- 2026-07-01 (b) SIP bars / (a) kill zero-vol tell: **Working.** All retrospective volume cited real SIP bars (CWD 100K–960K sh/bar AH fade, ZCMD 10M+ sh, DSY thin 2–18K sh/bar); no eval cited Yahoo ext-hours volume or "zero-volume bars."
- Ceiling + VRatio-override gate (2026-06-09 lineage): **Strongly validated.** ZCMD +445% AH ($6.57) — ceiling-blocked (Total% ≫150%, VRatio 2.3–2.6x failed the >5x override) — fully reverted to −4.5% ($1.05) by PM. A hypothetical override entry would have lost ~83%. Strongest extreme-runner-reversion confirmation to date.
- 2026-06-30 feed-lag/true-tail split: **Insufficient data (still open).** No late-AH-tail case Jul 2 (ZCMD peaked 17:15 ET, CWD faded through AH — both inside/irrelevant to the tail). Tracker recorded "none."
- Dead-cat-override watch: FXHO (real +168% AH, Day% −25%, nano float 97K) flagged as a *strong watch pending a 2nd AH scan at 01:00*, but there is no 01:00 scan (last is 00:30) so it never became a confirmed watch and had no liquid PM data. **Recurring friction:** a strong dead-cat-override candidate first appearing at 00:30 CET can never post a qualifying 2nd AH scan under the current 7-scan schedule. Logged, not actioned (schedule is the user's domain).

**Changes:**
1. **prompts/morning-evaluation.md** — Added a **quote-freshness guard** to Step 3 (Check Open Position P&L) and a reinforcing note on the Open Position P&L log-template table: before reporting an open position's Alpaca P&L, check the `broker.js quote` timestamp; if `current_price` is stale (prior 20:00 ET regular close on an ext-hours-active name), cross-check the live overnight/PM level via SIP bars or the Yahoo `--pm-history` timeline and report P&L against the **live** price, explicitly flagging the stale Alpaca figure as not tradeable. A stale `current_price` must not be printed as a real loss/gain. Basis SEER Jul 3.
   - Why: the morning eval reported SEER at −28.3% off a stale 20:00 ET close while it traded ~$2.30 overnight (+1.8%). The freshness guard existed for entries (2026-07-02) and exits (position-evaluation) but not for the morning-eval P&L readout, the one place today's stale quote actually misled the log.
   - Hypothesis: no future morning-eval P&L line reports a stale Alpaca `current_price` as a real loss/gain. Measurable: (1) the next time an open position's Alpaca `current_price` is stale (quote timestamp far behind the eval time) on an ext-hours-active name, the log flags the staleness and reports P&L against a SIP/PM-verified live price; (2) positions with fresh quotes are unaffected. If a future eval again prints a large stale loss/gain as fact without flagging it, the guard didn't take.

**Updated process:** Morning-eval open-position P&L now applies the same quote-freshness guard already used at entry and exit — a stale Alpaca `current_price` is cross-checked against the live overnight/PM price before any P&L is reported (Current Process). (No scanner parameters changed.)

### 2026-07-02 — Verification Freshness Guard (Stop False Bad-Print on Stale SIP/Quote Data)

**Context:** July 1→2 was full-coverage (7/7 scans), detection baseline 87.5% (35/40), but selection dropped 57.9% → 55.0% on the first genuinely-investable, liquid winner in a while that was **detected but wrongly skipped**. **USDE** (StablecoinX, 5.5M float) chopped $2.1–2.5 until 17:45 ET then exploded to a SIP-confirmed peak **$7.69 @18:30 ET** (+180% vs prior close) on 1M+ sh/bar, 16k+ trades/bar — fully fillable, not a phantom. The scanner surfaced it in every AH scan and at 00:30 CET showed the real move (AH $6.54 / +214% / VRatio 5.3x). It was skipped by a **stacked verification-layer false-negative:** (1) the TradingView postmarket feed lagged ~30 min (showed a stale $2.53 / −8% at the 00:00 scan, discontinuously jumping to +214% at 00:30); and (2) the live SIP-bar pull + `broker.js quote` both returned stale ~16:44 ET data ($2.52/$2.55, SIP high $2.79) during the fast 17:45–18:30 ET run, so the real +214% was called a **BAD PRINT** and skipped. The bad-print heuristic (added 2026-07-01 (c)) fired a false negative because the *trusted verification source was itself stale* — it had no freshness check. This is a data-reliability defect, not a threshold gap; the scanner did its job. In-scope fix per the morning-eval recommendation.

**Evaluation of previous changes:**
- 2026-07-01 (c) SIP volume confirmation + data-source preamble: **Working but incomplete — this entry patches the hole.** The SIP-confirmation step took (JEM correctly held as dead-cat/weak-catalyst skip, ALPS/EHGO caught as SPIKE→FADE, LHAI on ceiling), and the preamble was applied from the first action of each pulse (logs cite SIP vol/VWAP + book, not Yahoo volume). But the bad-print half of the step lacked a freshness guard, so it wrongly rejected USDE when its own SIP/quote data was stale. Fix below adds the guard; the confirmation step itself stands.
- 2026-07-01 (b) Switch bars to SIP: **Working.** The Jul 1 retrospective quoted real SIP ext-hours volume/VWAP/trades throughout (USDE 675K→1.35M sh/bar, JEM 1.5M sh/bar, DSY 511K sh/bar); no eval cited Yahoo ext-hours volume. Real low-IEX movers returned bars.
- 2026-07-01 (a) Kill zero-vol phantom tell: **Working.** No Jul 1/2 eval cited "zero-volume bars" as phantom evidence; phantom/skip calls cited book divergence and SIP.
- 2026-06-30 feed-lag/true-tail split: **Insufficient data (still open).** No late-AH-tail case Jul 1 (USDE 17:45 ET, DSY 18:05 ET both fired inside the scanned window, caught at 00:00/00:30). Tracker correctly recorded "none tonight."
- 2026-06-26 AH-liquidity sanity check / 2026-06-12 dead-cat-override / 2026-06-09 ceiling-override: **dead-cat-override got a data point** — JEM hypo entry $4.98 → PM peak $4.19 (−15.9%, low-volume/weak-catalyst reclaim faded, supports the filter here), while USDE was a *real-volume* reclaim (+138% above close on 1M sh/bar) that won big — strengthening the "dead-cat filter should be conditional on real reclaim volume" thesis. Both watches stay open. AH-liquidity check unexercised on a no-illiquid-entry night.

**Changes:**
1. **prompts/post-market-scan.md** — Added a **freshness guard** to the SIP volume-confirmation step: before rejecting a *strong* signal (high VRatio + large AH% + built across ≥2 AH scans) as a bad print, check the last SIP bar / quote timestamp against the scan time. If stale (far behind the scan), a "scanner price ≫ SIP high" divergence is a staleness artifact, not a bad print — re-pull once, else treat the reading as unconfirmed-but-live (do NOT skip as bad print), lean on the book, prefer waiting for the next scan. A bad print requires *fresh* SIP that reaches the scan window and still shows the price never traded. Also treat a discontinuous AH% jump between consecutive scans (e.g. −8% → +214%) as a feed-lag artifact to re-verify. Basis USDE Jul 1.
   - Why: the bad-print heuristic had no freshness check and fired a false negative on a real +180% winner because its own SIP/quote source was stale during the fast move. This is the exact failure the morning eval flagged.
   - Hypothesis: no future strong-signal winner is skipped as a bad print when the verification data is stale. Measurable: (1) the next time SIP/quote returns data far behind the scan time on a high-VRatio/large-AH% name, the log records a freshness-driven re-pull / "unconfirmed-but-live" hold rather than a bad-print skip; (2) genuine bad prints (fresh SIP shows the price never traded, e.g. JEM Jun 30 $12.67) are still skipped. If a future strong winner is again skipped citing a bad print while its verification data is stale, the guard didn't take.

**Updated process:** Entry-flow bad-print rejection now requires *fresh* SIP/quote data; stale verification cannot fire a bad-print skip on a strong live scanner signal (Current Process list above). (No scanner parameters changed.)

### 2026-07-01 (c) — SIP Volume Confirmation at Entry + Data-Source Preamble on Every Pulse

**Context:** With `broker.js bars` now on SIP (entry 2026-07-01 (b)), we have real full-market extended-hours volume, VWAP, and trade counts. Two follow-through gaps remained: (1) the **entry flow** still confirmed only fillability (the book), never that the TradingView VRatio spike was *real* — the exact hole that let stale-VRatio names (TII 4.9x, NEXR) look tradeable; and (2) the SIP/phantom knowledge lived deep in individual steps, so a fresh pulse could act before internalizing it. The strategy goal is to make money, which requires each pulse to apply the reliable data hierarchy from its first action, not rediscover it. Alpaca has **no screener**, so TradingView stays the discovery layer; SIP + book are the confirmation layer.

**Evaluation of previous changes:**
- 2026-07-01 (b) Switch bars to SIP: **Working.** Verified live — SIP returns full-market ext-hours volume (JEM 1.5M sh/bar vs IEX 2.3K), recent-data queries auto-fall back to IEX without erroring, and SIP is usable live for anything older than ~15 min (returned today's PM bars). This entry builds the entry/exit workflow on top of it.
- 2026-07-01 (a) Kill spurious zero-vol tell / earlier entries: unchanged this session.

**Changes:**
1. **prompts/post-market-scan.md** — Added a **SIP volume-confirmation** step to the entry flow (before order sizing): pull `broker.js bars SYM --tf 5Min --start <AH-start-UTC>` and require (a) real accumulating AH volume/trades across bars (not a single stale figure) and (b) SIP `H`/`vwap` corroborating the scanner's AH price (Yahoo/TV far above SIP high = bad print → skip). Paired with the existing real-time book check for the current instant.
   - Why: closes the stale-VRatio hole — the scanner's VRatio can be stale regular-session volume; SIP bars prove whether the AH spike actually traded.
   - Hypothesis: no entry is sized against a stale-VRatio/bad-print name going forward. Measurable: (1) the next TII/NEXR-style stale-VRatio candidate is skipped citing thin/absent SIP volume or a bad print; (2) real accumulating movers (GANX-style, real SIP volume) are unaffected and still entered. If an entry is placed against a name whose SIP bars show a handful of trades, the step didn't take.
2. **prompts/{post-market-scan, morning-evaluation, position-evaluation}.md** — Added an identical **"Data Sources (read first, every pulse)"** preamble at the top of all three pulse prompts: discovery = TradingView (VRatio is first-pass, not liquidity proof); real ext-hours volume + bad-print detection = SIP bars (`broker.js bars`); fillability = real-time book (`quote`); Yahoo ext-hours volume/exact levels are untrustworthy (0 volume for all; bad prints on illiquid names). So every pulse applies the hierarchy from its first action.
   - Why: user directive — the data-source knowledge must be reflected at the beginning of all pulses, not buried mid-prompt.
   - Hypothesis: each pulse uses SIP/book (not Yahoo volume) from the start. Measurable: post-cutover logs cite SIP volume/VWAP and the book for volume/liquidity calls; none cite Yahoo ext-hours volume.
3. **prompts/position-evaluation.md** — Repointed Step 2 P&L basis to Alpaca `current_price` (not Yahoo) and required verifying any peak against SIP `H`/`vwap` before acting (Yahoo PM bad-prints overstate peaks), taking the real sellable bid from `quote` before selling.
   - Why: exits were computing P&L/peaks off Yahoo PM prices, which bad-print on the illiquid names we trade.
   - Hypothesis: exit decisions use the Alpaca price/book; no sell or trail is triggered by a Yahoo bad-print peak. Measurable: the next exit pulse cites Alpaca current_price and a SIP-verified peak.

**Updated process:** Entry now requires SIP volume confirmation (real accumulating AH volume + VWAP corroboration) alongside the book check; all three pulse prompts carry a Data Sources preamble; exits use Alpaca price + SIP-verified peaks. (No scanner parameters changed.)

### 2026-07-01 (b) — Switch broker.js Bars to SIP for Real Extended-Hours Volume

**Context:** Follow-up to the earlier 2026-07-01 entry (Yahoo omits ext-hours volume). User asked whether we were getting bad data / delays and whether to pay for Alpaca SIP or Polygon. Investigation (verified live against our own credentials, not just docs):
- Yahoo's chart API structurally returns **volume=0 for all extended-hours bars** on every ticker, verified on AAPL and TSLA at 1m/5m/15m intervals. Not a delay or a fetch bug — a hard endpoint limitation.
- Worse, Yahoo ext-hours *prices* can be **bad prints**: JEM Jun 30 Yahoo AH "high" $12.67 (+1073%) never traded. Alpaca SIP shows JEM's real first AH bar at high $4.54 / VWAP $4.27 on **1,526,796 shares / 16,998 trades** — a real, heavily-traded mover, not a no-volume phantom. The "+1073%" was fictional.
- **Our free Alpaca account already serves full-market SIP historical bars** (incl. real ext-hours volume, VWAP, trade count); we were only querying `feed=iex` (~2-3% of consolidated volume, which returned "no bars" for low-IEX names like GANX). The free tier blocks only the most recent ~15 min of SIP (`"subscription does not permit querying recent SIP data"`), which does not affect a next-morning retrospective. So **no paid feed is needed** for the ext-hours-volume gap; a one-word feed switch fixes it at zero cost. (Paid options for real-time full-market during the live AH window: Alpaca Algo Trader Plus $99/mo — trivial integration; Polygon Developer $79/mo — new integration. Left to the user; not needed now.)

**Evaluation of previous changes:**
- 2026-07-01 (a) Kill spurious zero-volume-bar tell: **Superseded/extended by this entry.** That change correctly stopped Yahoo ext-hours volume being read as a phantom tell (relabeled to `n/a`). This entry adds the positive source (SIP bars) so evals have *real* ext-hours volume instead of just an absence, and reframes JEM from "phantom" to "real mover with a Yahoo bad print." The relabel stands; the phantom-detection note is upgraded (see below).
- Older watches (Jun 30 feed-lag/true-tail, Jun 26 AH-liquidity, Jun 12 dead-cat, Jun 09 ceiling): unchanged since the (a) entry today; not re-evaluated (same session).

**Changes:**
1. **scripts/broker.js** — `bars` now defaults to the **SIP** consolidated feed (was hardcoded `feed=iex`). Added a `--feed sip|iex` flag; on the free-tier "recent SIP data" block it auto-falls back to IEX (only when `--feed` was not explicitly set), so recent/live queries still return something. Output now also prints `vwap` and `trades` per bar and a `# SYM feed=<f>` header.
   - Why: IEX-only bars saw ~2-3% of volume and returned "no bars" for real movers with little IEX routing; SIP gives the full-market ext-hours volume the retrospective needs, for free.
   - Hypothesis: the next retrospective can cite real ext-hours volume/VWAP from `broker.js bars` (SIP). Measurable: (1) a phantom/bad-print night's eval quotes SIP `vol`/`vwap`/`trades` rather than "zero-volume bars"; (2) real low-IEX movers (GANX-style) now return bars instead of "no bars"; (3) recent-data queries do not error out (fall back to IEX). If bars still default to IEX or evals still cite Yahoo volume, the change didn't take.
2. **prompts/morning-evaluation.md** — Upgraded the phantom note to instruct pulling real ext-hours volume via `broker.js bars --tf 5Min --start <AH-start-UTC>` (SIP), using `vol`/`trades` for real liquidity and comparing the Yahoo AH/PM high vs SIP high/VWAP to detect Yahoo bad prints (JEM example), with the book (`quote`) as the live liquidity cross-check.
   - Why: gives evals a concrete positive method for ext-hours volume and bad-print detection instead of relying on the (now-relabeled) absent Yahoo volume.
   - Hypothesis: same measurable as change 1.

**Updated process:** Ext-hours volume & bad-print detection now use Alpaca **SIP** bars (`broker.js bars`, full-market vol + VWAP + trades) plus the live book; Yahoo ext-hours volume is unused. (No scanner parameters changed.)

### 2026-07-01 — Kill the Spurious "Zero-Volume Bars" Phantom Tell (Yahoo Ext-Hours Vol)

**Context:** June 30→July 1 was another clean, well-run night. Full coverage (7/7 scans), the AH-liquidity sanity check (Jun 26) fired correctly — ALZN was entered with its real two-sided book confirmed, while YOOV (`ask $0.00 x0`), JEM (+1073% Yahoo AH) and BTOG (+71%) were all skipped as phantom/illiquid ramps. Detection baseline 87.2% (34/39), selection 57.9% (22/39). The scanner and entry gates did their job; touching thresholds would be guessing against a working system. The one real, in-scope defect surfaced while verifying the phantom-detection logic: the morning-eval logs repeatedly cite **"zero-volume bars throughout"** as evidence a mover is a phantom (Jun 30 JEM: "Zero-volume bars throughout. Phantom."; the Notes even called it "the phantom filter (zero-vol bars + Alpaca quote mismatch)"). Live testing of `check-prices.py --ah-history` / `--pm-history` shows this is **false reasoning**: Yahoo's 5-min extended-hours bars return volume=0 for *every* ticker — the phantom JEM, the real traded ALZN, and the real traded GANX all show `AH Vol: 0` and 0 on every bar. The volume column and the `AH/PM Vol` header are a systematic Yahoo endpoint limitation, not a phantom signal. The tool was printing a hard "0" that reads like a genuine no-volume finding, so evals kept citing it as corroborating phantom evidence when it actually says nothing. The reliable phantom tell — already used and codified — is the divergence between the Yahoo ext-hours *price* and the real Alpaca book (`broker.js quote`), e.g. JEM's Yahoo AH $12.67 vs its Alpaca book stuck near $4.

**Evaluation of previous changes:**
- 2026-06-30 Feed-lag vs true-tail split: **Insufficient data (no case).** The Jul 1 eval recorded "Late-AH-tail tracking: none tonight" — JEM's decisive surge (17:20→18:10 ET) fired inside the scanned window (00:00/00:30 CET caught it), so there was no late-AH-tail case to apply the new sub-label to. The tracker did not misfire on a no-case night. Still open.
- 2026-06-26 AH-liquidity sanity check: **Working.** The Jul 1 eval/scan log shows YOOV skipped as "illiquid (no AH book)" (`ask $0.00 x0`) and JEM/BTOG skipped as zero-real-book phantoms, while ALZN was entered only after its real two-sided book was confirmed. No order sized against a phantom. This is exactly the guard's job, and it also exposed today's defect (the guard is the *correct* phantom tell; the Yahoo volume column is the wrong one).
- 2026-06-25 Align morning-eval P&L with Alpaca: **Working.** The Jul 1 eval Step 3 pulled ALZN read-only from Alpaca (entry $1.31, real fill), recorded only that fill, kept JEM/BTOG as hypothetical/phantom in the diagnostic, and deferred hold/sell to position-evaluation. No fictional ledger P&L.
- 2026-06-24 Investability label on PM-only gapper tracker: **Working.** The Jul 1 eval classified its biggest raw PM mover (JEM) as an AH→PM continuation (had AH footprint) but **uninvestable** (phantom, book never left ~$4). Label applied; tally unchanged.
- 2026-06-19 Scan-coverage check: **Working.** Jul 1 recorded `Evening scans ran: 7 of 7`, no coverage failure.
- 2026-06-18 / 2026-06-17 fade-rule trackers: **Working.** LGPS skipped SPIKE→FADE (AH peak $1.34 @ 22:15 CET) with PM peak $1.17 staying below → rule correct, tally held.
- 2026-06-12 dead-cat-override watch / 2026-06-09 ceiling-override watch: **Insufficient data (still open).** No qualifying candidate Jun 30 night (JEM stayed below its regular close → genuine dead-cat/phantom, no override flag).

**Changes:**
1. **scripts/check-prices.py** — `--ah-history` and `--pm-history` no longer print a misleading `0` for extended-hours volume. When the summed ext-hours volume is 0 (the normal case — Yahoo omits it), the header now shows `AH/PM Vol: n/a (Yahoo omits ext-hours vol)` and each per-bar `Vol` cell shows `—` instead of `0`. If Yahoo ever does return real ext-hours volume (non-zero), the real numbers still print unchanged.
   - Why: the hard `0` reads like a real no-volume finding and was being cited in evals as corroborating phantom evidence, when in fact every ticker (real and phantom) shows 0 here. Relabeling it as unavailable removes the false signal at the source.
   - Hypothesis: the next eval that inspects `--ah-history`/`--pm-history` no longer records "zero-volume bars" as a phantom tell. Measurable: (1) no eval after today cites Yahoo ext-hours bar volume as phantom evidence; (2) phantom calls cite the Alpaca book divergence (`broker.js quote`) instead. If a future eval still leans on "zero-volume bars," the relabel/prompt note didn't take and needs reinforcement.
2. **prompts/morning-evaluation.md** — Added a "Phantom-ramp detection (do NOT use Yahoo ext-hours volume)" note to Step 2: Yahoo 5-min ext-hours bars report no volume for any ticker, so zero-volume bars are not phantom evidence; classify a phantom only from the Yahoo ext-hours *price* vs the real Alpaca book (`broker.js quote` — price far above a stuck bid/ask, or `ask $0.00 x0`), citing JEM Jun 30 ($12.67 Yahoo AH vs ~$4 book) as the example.
   - Why: the flawed "zero-volume bars" reasoning appeared in the actual Jun 30 eval Notes; the note redirects future evals to the one reliable phantom tell that is already codified in the entry flow.
   - Hypothesis: same measurable as change 1 — future evals classify phantoms from book divergence, not Yahoo bar volume.

**Updated process:** Phantom-ramp classification relies on the Alpaca book divergence (`broker.js quote`), not on Yahoo extended-hours bar volume (which is uniformly absent). (No scanner parameters changed.)

### 2026-06-30 — Split Late-AH-Tail Tracker Into Feed-Lag vs True-Tail (BTCT)

**Context:** June 29→30 was a clean, well-run night. Full coverage (7/7 scans), the AH-liquidity sanity check (added Jun 26) fired correctly — both entries (GANX, CTNT) had their two-sided Alpaca books confirmed before sizing, and SLGB/LGCL were skipped as stale-volume (VRatio 0.1x, zero real AH volume). Detection baseline held at 86.8% (33/38), selection 57.9% (22/38). The night's winner, **BTCT** (+139% AH peak 18:50 ET, PM open +88%), was logged as a late-AH-tail surge — but the reconstruction shows it was **already +67.6% at 18:30 ET**, the exact timestamp of the 00:30 CET last scan, and the live scan missed it because the TradingView postmarket feed showed it flat (known feed lag). That is a different failure mode than the founding case ORIS (genuinely +22–28% / under threshold at 18:30 ET, surged at 19:25 ET). The late-AH-tail tracker conflated the two, which matters because they imply opposite fixes: a true-tail surge argues for adding a late scan (~01:00/01:30 CET), but a feed-lag miss argues for verifying the AH data source — a late scan would not have helped because the move was already live at scan time. Touching scanner thresholds is unwarranted (the scanner did its job; both qualifiers were detected and entered). The in-scope improvement is sharpening the existing instrumentation so the eventual scheduling decision is not muddied by feed-lag cases.

**Evaluation of previous changes:**
- 2026-06-26 AH-liquidity sanity check (zero-AH-volume ramp trap): **Working.** The Jun 30 eval/scan log shows the guard exercised on every entry — GANX confirmed real two-sided book (bid $2.42 x200 / ask $2.43 x300) and CTNT (bid $1.95 x100 / ask $2.01 x100) before sizing, while SLGB (VRatio 0.1x across all scans, 131K→182K AH vol) and LGCL (Yahoo showed 0 AH volume; scan's 3.3M was a stale regular-session artifact) were skipped as illiquid/stale. No order was sized against a zero-size book. The guard took and is now routine.
- 2026-06-25 Align morning-eval P&L with Alpaca: **Working.** The Jun 30 eval pulled open positions read-only via the Alpaca account (GANX entry $2.39, CTNT $2.05 — real fills), recorded only real fills, kept BTCT/JEM as hypothetical in the diagnostic, and deferred hold/sell to position-evaluation. No fictional ledger P&L.
- 2026-06-24 Investability label on PM-only gapper tracker: **Working.** The Jun 30 eval classified its biggest raw PM mover (JEM, dead-cat reclaim, PM gap to $3.36) as a PM-only gapper and applied the holdable/uninvestable label (borderline-holdable, ~2 bars, flagged tentative on 20 min of data). Classifier behaved as designed; tally annotated.
- 2026-06-23 Late-AH-tail surge tracker: **Working, and this entry refines it.** The Jun 30 eval correctly identified BTCT as a late-AH-tail case and incremented the tally to 2 (ORIS, BTCT). This change adds the feed-lag/true-tail sub-label the tracker was missing.
- 2026-06-19 Scan-coverage check: **Working.** Jun 30 recorded `Evening scans ran: 7 of 7`, no coverage failure.
- 2026-06-18 Float on fade-rule false-negative tracker / 2026-06-17 fade-rule tracker: **Working.** Jun 30 logged LGCL skipped on SPIKE→FADE (AH high $1.42 +92% at 18:15 ET → $0.99 by 18:30) with no PM re-explosion → rule correct. Tally held at 2 (CRE, LNKS).
- 2026-06-12 dead-cat-override watch / 2026-06-09 ceiling-override watch: **Insufficient data (still open).** No qualifying candidate Jun 29 night (JEM stayed below its regular close across all AH scans → genuine dead-cat, no override flag). Both watches remain open.

**Changes:**
1. **prompts/morning-evaluation.md** — Extended the late-AH-tail surge tracker to sub-classify each case as **feed-lag** (already over the 10% AH threshold at the 18:30 ET / 00:30 CET last-scan timestamp per the `--ah-history` reconstruction, but the live 00:30 scan's TradingView feed missed it) vs **true-tail** (genuinely under threshold at 18:30 ET, decisive surge fired after). Labeled the two known cases (ORIS = true-tail, BTCT = feed-lag) and split the action threshold: only ≥3–4 *true-tail* winners argue for adding a late scan; a feed-lag cluster instead points at fixing the AH data source (cross-check Yahoo AH at the last scan), not the schedule.
   - Why: the tracker drives a future add-late-scan decision, but BTCT showed that a late-AH-tail case can be a feed-lag miss (move already live at scan time) rather than a true timing gap. Without the split, a feed-lag cluster could wrongly motivate adding late scans that would not have caught the move, while the real fix (data-source verification) goes unidentified.
   - Hypothesis: each new late-AH-tail case now records a feed-lag/true-tail label. Measurable: (1) the next late-AH-tail night records the sub-label; (2) after ~5–6 cases the split is known. If true-tail dominates, it argues for an added late scan; if feed-lag dominates, it argues for verifying/replacing the AH data source instead. If the next case is logged without a sub-label, the instruction didn't take and needs reinforcement.

**Updated process:** Late-AH-tail surge tracker now sub-classifies feed-lag vs true-tail (Current Process list above). (No scanner parameters changed.)

### 2026-06-26 — Codify AH-Liquidity Sanity Check (Zero-AH-Volume Ramp Trap)

**Context:** June 25→26 was another clean detection + selection night: full coverage (7/7 scans), the winner **ILLR** (+760% PM) was detected in all 7 scans and correctly skipped (already +296%–+446% Total, far over the +150% extension ceiling, on zero real AH volume / VRatio 0.1–0.4x), and we traded **IVF** (clean 1.8M-float BUILD-and-hold on real volume, VRatio 6.2x) for a realized **+26.6%**. Detection baseline 86.8% (33/38), selection 57.9% (22/38). The scanner did its job; touching thresholds today would be guessing against a working system. The one real, recurring, in-scope risk that surfaced again is the **zero-AH-volume illiquid ramp trap**: **TII** printed `AH Vol 3.4M / VRatio 4.9x` in the scanner (which *looks* tradeable) but the Alpaca book was `ask $0.00 x0` — the TradingView volume was stale regular-session volume, not real AH liquidity, and TII round-tripped -29% from its zero-volume +110% AH spike. Same pattern as NEXR (appeared again today and Jun 25). The agent caught it only by manually checking the Alpaca book and skipping; nothing in `post-market-scan.md` formally instructs that liquidity verification, so a future run could size an order against a misleading VRatio and enter an untradeable ramp.

**Evaluation of previous changes:**
- 2026-06-25 Align morning-eval P&L with Alpaca: **Working.** The Jun 26 eval ran Step 3 as "Open Position P&L (Alpaca)", pulled IVF from the Alpaca account (real fill $1.58), recorded only that fill, kept ILLR/TII as *hypothetical* in the Scanner Diagnostic (never filled), and titled the total "Total Realized P&L (Alpaca fills only): €0.00 (position still open)". No fictional ledger P&L, no conflict with `position-evaluation.md` (which separately sold IVF at $2.00 / +26.6%). The cutover fix took.
- 2026-06-24 Investability label on PM-only gapper tracker: **Working (no case to label).** Jun 26's biggest raw mover (ILLR, +760%) was classified as an **AH→PM continuation** (moved +37% in after-hours, detectable), not a PM-only gapper, so the tally held (CIIT, GLXG, TDIC, MBRX, CUPR = 5) and there was no new gapper to apply the holdable/uninvestable label to. Classifier correct.
- 2026-06-23 Late-AH-tail surge tracker: **Working.** The Jun 26 eval ran the check on ILLR (AH peak 19:55 ET, inside the 18:30–20:00 ET tail) but correctly reasoned its defining move was the regular session + steady AH build (detected in all 7 scans, skipped on ceiling — not a tail-surge detection miss), so no new tail case. Tally held at 1 (ORIS).
- 2026-06-19 Scan-coverage check: **Working.** Jun 26 recorded `Evening scans ran: 7 of 7`, no coverage failure, tally unchanged (founding case Jun 18–19).
- 2026-06-18 Float on fade-rule false-negative tracker / 2026-06-17 fade-rule tracker: **Working.** No false negative Jun 26 — TII faded from its AH spike and stayed below in PM, but was never a live entry (zero AH volume), so not a re-explosion. Tally held at 2 (CRE, LNKS).
- 2026-06-12 dead-cat-override watch / 2026-06-09 ceiling-override watch: **Insufficient data (still open).** No qualifying candidate flagged Jun 25 night (ILLR failed the ceiling-override on VRatio <5x / zero AH volume). Both watches remain open.

**Changes:**
1. **prompts/post-market-scan.md** — Added an **AH-liquidity sanity check** to the entry flow (right before order sizing): before sizing, confirm `broker.js quote SYM` shows a real two-sided AH book (non-zero ask price *with* size, non-zero bid). If it shows `ask $0.00 x0` (or zero size on either side), treat the TradingView `AH Vol`/`VRatio` as a stale regular-session artifact and skip as **illiquid (no AH book)** rather than entering. Cited TII (Jun 26) and the recurring NEXR zero-AH-volume ramp pattern as the basis.
   - Why: the scanner's VRatio is computed from TradingView's `postmarket_volume`, which can carry stale regular-session volume and surface a misleadingly tradeable VRatio on names with no fillable AH liquidity (TII, NEXR). The agent has caught these only ad hoc by manually checking the Alpaca book; nothing in the prompt formalized that step, so a future run could enter an untradeable ramp against a false VRatio.
   - Hypothesis: going forward, every over-10% AH candidate gets a quick book check before order sizing, and any `ask $0.00 x0`/zero-size name is skipped as illiquid with a logged reason. Measurable: (1) the next zero-AH-volume ramp (TII/NEXR-style) is skipped with an explicit "illiquid (no AH book)" note rather than an attempted entry; (2) no Alpaca order is placed against a name whose quote shows no AH size; (3) genuine real-volume candidates (VRatio backed by an actual two-sided book, e.g. IVF) are unaffected and still entered. If a future run still sizes an order against a zero-size book, the guard didn't take and needs reinforcement.

**Updated process:** Entry flow now requires an AH-liquidity sanity check (real two-sided Alpaca book) before order sizing; zero-AH-book ramps are skipped as illiquid. (No scanner parameters changed.)

### 2026-06-25 — Align Morning-Eval P&L With Alpaca (Discarded-Ledger Cleanup)

**Context:** June 24→25 was a clean detection + selection win: the morning winner **AZI** (+98.3% AH, +81.4% PM) was the biggest AH mover from the first scan, built across every scan (22:30 +37.7% → 00:30 +82.5%), and was flagged at 23:00 CET as the night's top candidate. No detection gap, no fade-rule false negative, no PM-only gapper (AZI was an AH→PM continuation, the biggest raw mover), no late-AH-tail surge, no ceiling/dead-cat override candidate. Detection baseline 86.5% (32/37), selection 59.5% (22/37). Touching scanner thresholds today would be guessing against a working scanner. **The one real, in-scope change is a process-correctness fix:** today is the cutover to Alpaca paper execution — `OPEN_POSITIONS.md` and the Jun 23 `scripts/broker.js` now make the **Alpaca paper account the source of truth**, and the old hand-maintained markdown ledger (assumed prices, never executed) was explicitly discarded. But `prompts/morning-evaluation.md` Step 3 still read "paper trades **in the log**" and computed unrealized P&L from `entry_price * shares`, and its output section was titled "Paper Trade P&L" with a "Total Paper P&L" line. Left unfixed, tomorrow's morning eval would reconstruct fictional P&L from a ledger that no longer exists, or double-handle position P&L that now belongs to `position-evaluation.md` (which already owns hold/sell at 10:30/14:30 CET). The post-market-scan prompt was already migrated to Alpaca (broker.js + OPEN_POSITIONS.md) on Jun 23; the morning-eval prompt was the remaining stale reference.

**Evaluation of previous changes:**
- 2026-06-24 Investability label on PM-only gapper tracker: **Working.** The Jun 25 eval ran the PM-only gapper classification on its biggest raw mover (AZI) and correctly logged it as an **AH→PM continuation** (moved +98% in AH, detectable), leaving the tally unchanged (CIIT, GLXG, TDIC, MBRX, CUPR = 5). No new gapper to label, so the holdable/uninvestable instruction had nothing to exercise this cycle, but the classifier behaved as designed (it didn't misclassify a continuation as a gapper). Tracker intact.
- 2026-06-23 Late-AH-tail surge tracker (ORIS): **Working.** The Jun 25 eval ran the check and recorded "AZI's defining move … happened during the scanned window; the 18:30–20:00 ET tail only extended an already-qualified open position from +76% to +98%. Not a tail-surge miss." Tally held at 1 (ORIS). Correct non-fire on a no-case night.
- 2026-06-19 Scan-coverage check: **Working, and earned its keep.** The Jun 25 eval recorded `Evening scans ran: 6 of 7` (21:30 missing), confirmed the entry window (23:00–00:30 CET) was fully covered, and logged it as a transient minor miss to watch for recurrence — **not** a detection/selection penalty. This is exactly the partial-coverage case the check was built to handle: it kept the baseline honest (AZI still counted as a clean detect+select) rather than churning thresholds. Coverage-failure tally still 1 episode (Jun 18–19); the 6/7 is a single dropped pre-volume scan, below the ≥2-in-10 escalation trigger.
- 2026-06-18 Float on fade-rule false-negative tracker / 2026-06-17 fade-rule tracker: **Working.** The Jun 25 eval recorded no false negatives — SAGT (spike→fade, peaked +10% 16:15 ET) and KIDZ (spike→fade, +25% 16:45 ET then collapsed) were both correctly skipped and both stayed down in PM. Rule net-correct; tally held at 2 (CRE, LNKS).
- 2026-06-12 dead-cat-override watch / 2026-06-09 ceiling-override watch: **Insufficient data (still open).** No qualifying candidate flagged Jun 24 night. Both watches remain open.

**Changes:**
1. **prompts/morning-evaluation.md** — Repointed Step 3 from the discarded log-based ledger to Alpaca: retitled it "Check Open Position P&L (Alpaca)", replaced the `check-prices.py … entry_price*shares` recipe with `node scripts/broker.js positions` (read-only), and added explicit guards — do not place hold/sell orders here (that is `position-evaluation.md`'s job), and do not reconstruct P&L from assumed/quoted prices for stocks that never filled. Also relabeled the output section "Paper Trade P&L" → "Open Position P&L (Alpaca)" with a note that only real Alpaca fills go in the table (unfilled candidates stay in the Scanner Diagnostic as *hypothetical*), and "Total Paper P&L" → "Total Realized P&L (Alpaca fills only)".
   - Why: today's cutover made Alpaca the source of truth and discarded the markdown ledger, but the morning-eval prompt still instructed reading paper trades from the log and computing fictional `entry*shares` P&L. The post-market-scan prompt was already migrated Jun 23; this closes the last stale reference so the two prompts agree on where positions live.
   - Hypothesis: tomorrow's morning eval pulls open positions from `broker.js positions` (or states "no open positions") instead of inventing log P&L, and logs only real fills (or "No executed positions") in the P&L table. Measurable: (1) the next eval that runs Step 3 cites Alpaca, not the log; (2) no morning eval records a P&L row for a stock that never filled on Alpaca; (3) no conflict with `position-evaluation.md`'s hold/sell decisions. If a future eval still reconstructs ledger P&L, the fix didn't take and needs reinforcement.

**Updated process:** Morning-eval P&L now reads from the Alpaca paper account (`broker.js positions`) read-only; only real Alpaca fills are recorded; the discarded hand-maintained ledger is no longer referenced. (No scanner parameters changed.)

### 2026-06-24 — Add Investability Label to PM-Only Gapper Tracker

**Context:** June 23–24 was the cleanest night yet on the core thesis: full coverage (7/7 scans), the winner **VTAK** was detected *and* traded at $1.16, and it was the morning's single biggest raw PM mover (+105.8% peak, AH→PM continuation that exceeded its AH peak). Detection baseline holds at **86.1% (31/36)**. No detection miss, no coverage failure, no fade-rule false negative, no late-AH-tail case — so no threshold or filter change is warranted (the scanner did everything right; touching it now would be guessing and risk breaking a working system). The one accumulating signal is the **PM-only gapper tally, now at 5** (CIIT, GLXG, TDIC, MBRX, CUPR) over ~15 sessions — roughly 1 night in 3 the biggest raw mover is a structural AH-scanner blind spot. That tally is meant to decide whether to build a separate (risky) early-PM scan workflow, but it only records the % move, not whether the gapper was actually *tradeable*. The last two cases were not: MBRX crashed $6.64→$3.77 in 10 min, CUPR's $9.74 high was a single thin tick. If most PM-only gappers are uninvestable spikes, the blind spot costs us almost nothing and we should not add a risky PM scan.

**Evaluation of previous changes:**
- 2026-06-23 Late-AH-tail surge tracker (ORIS): **Working.** The Jun 24 eval ran the check and recorded "Late-AH-tail tally: No new case — VTAK's defining surge (17:35 ET) was inside the scanned window." The tracker executed as designed on a night with no qualifying case, leaving the tally at 1 (ORIS). It neither fabricated a case nor skipped the check.
- 2026-06-19 Scan-coverage check: **Working.** The Jun 24 eval recorded `Evening scans ran: 7 of 7`, confirmed full entry-window coverage, and left the coverage-failure tally at 1 episode (Jun 18–19). No infra escalation.
- 2026-06-18 Float on fade-rule false-negative tracker: **Working.** The Jun 24 eval logged VTAK's 2.0M float as supporting evidence for the <3M re-explosion hypothesis (VTAK faded late in AH then re-exploded past its AH peak in PM — but we *entered* it, so not a false negative; logged as a held-through-re-explosion data point). Tally held at 2 (CRE, LNKS).
- 2026-06-16 PM-only gapper tracker: **Working.** The Jun 24 eval classified CUPR (+81% PM, flat AH, float 921K, overnight news) as a PM-only gapper and incremented the tally to 5. It correctly identified VTAK (the bigger PM mover) as an AH→PM continuation, not a gapper — a positive data point that continuations can top the board. This entry builds directly on that working tracker.
- 2026-06-12 dead-cat-override watch / 2026-06-09 ceiling-override watch: **Insufficient data (still open).** No qualifying candidate flagged Jun 23 night. Both watches remain open.

**Changes:**
1. **prompts/morning-evaluation.md** — Extended the PM-only gapper tracker: (a) appended CUPR (Jun 24) and annotated MBRX/CUPR as uninvestable; (b) added an instruction to classify every PM-only gapper as **holdable** (gain sustained ≥2 consecutive 5-min bars on real volume) vs **uninvestable** (instant crash within ~10 min or a single thin/illiquid tick), recorded beside each case; (c) reframed the decision hypothesis so the blind spot only justifies an early-PM scan workflow if the gappers are *holdable*.
   - Why: the tally drives a future build/no-build decision on a risky early-PM scan, but raw % alone overstates the blind spot — the last two gappers (MBRX, CUPR) were untradeable. Without an investability label the tally would keep growing and could wrongly motivate building a PM scanner to chase moves that were never capturable in practice.
   - Hypothesis: over the next 2–4 weeks each new PM-only gapper gets a holdable/uninvestable label. Measurable: (1) the next PM-only-gapper night records a label; (2) after ~10 such cases the holdable share is known. If most are uninvestable (expected), the AH-scanner blind spot is confirmed low-cost and no early-PM scan is built; if a cluster of holdable gappers appears, that becomes the evidence to revisit the workflow.

**Updated process:** PM-only gapper tracker now records a holdable/uninvestable label per case (Current Process list above); appended CUPR (Jun 24) to the tally.

### 2026-06-23 — Instrument Late-AH-Tail Surge Tracker (ORIS After-Last-Scan Surge)

**Context:** June 22–23 was a full-coverage night (7 of 7 scans ran) and a clean detection night — the three traded names (VTAK, SKYQ, EHGO) were all caught and entered. But the morning's winner, **ORIS** (+92.5% PM peak), was a new failure mode the existing trackers don't capture. ORIS built only +22–28% in early AH (correctly under the 10% AH-from-close threshold during the scanned window), then its **defining pure-AH surge fired at 19:25 ET ($2.49→$3.28, +32%)** — **after the last scheduled scan (00:30 CET / 18:30 ET)**, in the unscanned 18:30–20:00 ET after-hours tail — and continued to a PM peak of $3.93. Hypothetical AH-tail entry ~$2.55 → PM peak: **+54%**. This is *not* a PM-only gapper (ORIS had an AH footprint and surged before 04:00 ET) and *not* a detection-threshold miss (during the scanned window it was correctly below threshold). It is a **late-AH-tail surge**: a winner whose decisive move happened in the ~90-minute window the 7-scan schedule ends before covering. The Jun 22 eval recommended adding 1–2 late scans (~01:00/01:30 CET), but the schedule lives in `scheduler.json` (off-limits to this loop). The conservative in-scope move is to instrument the mode so the eventual scheduling decision is data-driven, mirroring the proven PM-only-gapper / ceiling-override / fade-rule tracker pattern.

**Evaluation of previous changes:**
- 2026-06-19 Institutionalize scan-coverage check: **Working.** The Jun 22 eval ran the coverage check first, recorded `Evening scans ran: 7 of 7`, confirmed no coverage failure, and left the coverage-failure tally at 1 episode (Jun 18–19). No infra escalation. The check behaved exactly as designed on a clean-coverage night — it neither flagged a false failure nor let the full-coverage night go unverified.
- 2026-06-18 Add float to fade-rule false-negative tracker (LNKS): **Working / producing useful contrast data.** The Jun 22 eval recorded all four same-night faders the rule correctly skipped with floats — KIDZ (1.1M), NXGL (7.1M), BOXL (3.2M), TNON (10M) — every one stayed below its AH peak in PM. **KIDZ at 1.1M float faded and did NOT re-explode**, a clean counter-example weakening the "low float alone predicts re-explosion" hypothesis (the only two re-exploders, CRE and LNKS, were both <3M float, but low float is clearly not sufficient). Tally held at 2; the float field is generating the intended separator dataset.
- 2026-06-16 Instrument PM-only gapper frequency (TDIC): **Working.** The Jun 22 eval classified its biggest raw PM mover, MBRX (+131%, flat AH +8.7%, exploded only after 04:00 ET then crashed $6.64→$3.77 in 10 min), as a PM-only gapper and incremented the tally to 4 (CIIT, GLXG, TDIC, MBRX). The classifier correctly distinguished it from ORIS (the AH-footprint winner), validating the need for the separate late-AH-tail tracker added today.
- 2026-06-12 Instrument dead-cat-override watch (BYAH): **Insufficient data (still open).** No DEAD-CAT-OVERRIDE WATCH candidate flagged Jun 22. Watch remains open.
- 2026-06-09 Ceiling-override watch for BUILD-and-hold: **Insufficient data (still open).** No qualifying >150% BUILD-and-hold candidate Jun 22 (EHGO entered at +114%, under the ceiling). Watch remains open.

**Changes:**
1. **prompts/morning-evaluation.md** — Added a "Late-AH-tail surge tracking" instruction to Step 4 (Scanner Diagnostic), beside the PM-only gapper tracker. Each morning, check whether the winner's defining AH surge fired after the last scheduled scan (after 18:30 ET / 00:30 CET, before 04:00 ET) in the unscanned 18:30–20:00 ET tail; if so, classify it as a late-AH-tail surge and tally it (date, ticker, surge time, hypothetical AH-tail→PM-peak P&L). Explicitly distinguishes it from a PM-only gapper and from a detection-threshold miss, and states it is not counted against the detection baseline. Seeded with ORIS (Jun 22, +54% hypothetical).
   - Why: ORIS is the first cleanly-logged winner whose decisive move fired in the post-last-scan AH tail, a mode none of the existing trackers capture (PM-only-gapper requires a flat AH; detection-threshold trackers assume the move happened during the scanned window). Without a tally we cannot tell whether late-tail surges are a recurring exploitable blind spot (justifying added late scans) or a one-off. Instrumenting builds the dataset without changing the schedule or risking the scanner.
   - Hypothesis: Over the next 2–4 weeks the morning eval logs any winner whose defining surge fired in the 18:30–20:00 ET tail, accumulating a tally with hypothetical P&L. Measurable: (1) the next such night records a late-AH-tail-surge row; (2) after ~15 sessions the tally shows how often winners surge in the uncovered tail. If ≥3–4 winners cluster there, it argues for adding 1–2 late scans (~01:00/01:30 CET) — a scheduling decision left to the user; if they stay rare, the current 7-scan window stands.

**Updated process:** Added the late-AH-tail surge tracker to the morning evaluation diagnostics (Current Process list above); appended MBRX to the PM-only gapper tally.

### 2026-06-19 — Institutionalize Scan-Coverage Check (Jun 18 Cron Outage)

**Context:** June 18→19 was a **coverage failure, not a detection or selection failure.** Only **2 of 7** scheduled evening scans ran (21:30 + 22:00 CET); the entire entry window (23:00–00:30 CET) was uncaptured. Session files confirm it: trading sessions exist for 19:30 and 20:00 UTC (21:30/22:00 CET), then nothing until 09:01 the next morning — the 22:30/23:00/23:30/00:00/00:30 CET crons never started a session. The crons are correctly registered (`list_crons` shows all 7) and the scanner binary is healthy (manual runs returned 22 PM / 20 AH hits at 04:22 ET), so this was a scheduler/bridge outage during 22:30–00:30 CET, which is **outside the scanner/process files this loop may edit** (scheduler.json is off-limits). No paper trade was possible; today's morning eval correctly did not increment the selection count and kept detection baseline at 88.2% (CDT, the biggest liquid mover, was on the 21:30/22:00 watch — an AH→PM continuation, not a true miss). Because the night produced no usable detection/selection signal, making threshold changes today would be guessing. Per the be-conservative rule, the one in-scope improvement is to **institutionalize detection of this failure mode** so it is quantified going forward and never silently contaminates the baseline.

**Evaluation of previous changes:**
- 2026-06-18 Add float to fade-rule false-negative tracker (LNKS): **Insufficient data (coverage failure).** The AH window was never scanned Jun 18 night, so no fade-skip could be evaluated and no new false-negative or contrast-fader float could be recorded. Tally unchanged (CRE, LNKS = 2). Instrumentation untestable this cycle, not broken.
- 2026-06-16 Instrument PM-only gapper frequency (TDIC): **Working.** The Jun 19 eval ran the classification on its biggest *liquid* mover (CDT, +31% from close) and correctly logged it as an AH→PM continuation (on the pre-close watch), tally left unchanged (CIIT, GLXG, TDIC). It also correctly excluded WOK (+78% but 9K float) as an untradeable artifact rather than a gapper. Classifier behaved as designed even on a degraded-data morning.
- 2026-06-12 Instrument dead-cat-override watch (BYAH): **Insufficient data (still open).** No AH scan ran, so no DEAD-CAT-OVERRIDE WATCH candidate could be flagged. Watch remains open.
- 2026-06-09 Ceiling-override watch for BUILD-and-hold: **Insufficient data (still open).** No AH scan ran; nothing to flag or tally. Watch remains open.

**Changes:**
1. **prompts/morning-evaluation.md** — Added a "Scan coverage check (run first)" instruction at the top of Step 4 (Scanner Diagnostic). Each morning, count how many of the 7 scheduled evening scans actually ran (via `## Scan` log sections or `post-market scan` git commits), record `Evening scans ran: X of 7`, and keep a running coverage-failure tally in Notes. Explicitly instructs that on a night the scanner did not cover the entry window, the night's winner is **not** counted as a detection miss and selection is not penalized — it is logged as a coverage failure. Adds an escalation trigger: ≥2 coverage failures within ~10 sessions flags scheduler/bridge reliability for the user to investigate.
   - Why: Jun 18's outage was caught ad hoc and thoroughly this morning, but nothing in the process formally distinguishes a coverage failure from a detection/threshold gap, and nothing tracks recurrence. Without a formal check, a future partial-coverage night could silently deflate the detection/selection baseline (making the scanner look worse than it is) or be misread as a threshold problem prompting a wrong scanner change.
   - Hypothesis: Going forward, every morning eval logs `Evening scans ran: X of 7`. Measurable: (1) the next eval records the coverage line; (2) any future <7 night is tallied and excluded from detection-miss/selection penalties rather than guessed at; (3) if coverage failures recur (≥2 in ~10 sessions) the eval surfaces an infra-reliability flag instead of churning scanner thresholds. A clean run streak leaves the tally empty and the baseline untouched.

**Updated process:** Added the scan-coverage check to the morning evaluation diagnostics (Current Process list above).

### 2026-06-18 — Add Float to Fade-Rule False-Negative Tracker (LNKS Re-Explosion)

**Context:** June 17→18 was another clean scanner night. Detection ticked to 87.9% (29/33); the morning's biggest raw mover, **LNKS** (+184.7% PM), was an AH→PM continuation the scanner detected in every evening scan, so the baseline held and the PM-only-gapper tally was correctly left unchanged. LNKS was *skipped on the SPIKE→FADE rule* (AH peak $2.31 +40% at the very first bar 16:05 ET, then faded/chopped all night) and then re-exploded to +185% in premarket — the **2nd fade-rule false negative after CRE (Jun 17)**. We traded **LPA** instead (clean AH BUILD-and-hold $5.59 +66% → PM continuation, entered $5.21, green), exactly the strategy pattern, confirming the selection logic. Critically, the *same night* the fade rule correctly skipped **TGE** (AH +46% → PM +6%, float 44.2M) and **ATPC** (AH +52% → PM +32%), both of which faded as predicted. The two re-exploders (LNKS 1.5M float, plus CRE) vs the correctly-skipped faders (TGE 44.2M float) hint that **float** is the variable separating false-negatives from true faders. No scanner detection/selection gap to fix; this enriches the existing fade-rule tracker so the eventual rule decision can be conditional rather than blanket.

**Evaluation of previous changes:**
- 2026-06-17 Instrument fade-rule false-negative tracker (CRE): **Working.** The June 18 eval produced its first repeat data point exactly as designed — it identified LNKS as a fade-skip that re-exploded in PM, logged AH peak / PM peak / hypothetical P&L, and incremented the running tally to CRE + LNKS = 2. It also correctly noted the rule stayed net-correct that night (TGE, ATPC faded as predicted) and that 2 cases is still below the ≥4/5 threshold to change the rule. The instrumentation is generating the intended dataset.
- 2026-06-16 Instrument PM-only gapper frequency (TDIC): **Still working.** June 18's biggest raw mover (LNKS) was classified as an AH→PM continuation, tally correctly left unchanged (CIIT, GLXG, TDIC). The classifier keeps distinguishing detectable continuations from structural blind-spot gappers.
- 2026-06-12 Instrument dead-cat-override watch (BYAH): **Insufficient data (still open).** BYAH itself reappeared Jun 18 (Day -20%, AH bounce) but never reclaimed above its regular close across scans, so no DEAD-CAT-OVERRIDE WATCH was flagged. Nothing to tally. Watch remains open.
- 2026-06-09 Ceiling-override watch for BUILD-and-hold: **Insufficient data (still open).** No qualifying >150% BUILD-and-hold candidate appeared Jun 18 (LPA entered at +66%, well under the ceiling). Watch remains open.

**Changes:**
1. **prompts/morning-evaluation.md** — Extended the fade-rule false-negative tracker: (a) seeded the 2nd known case (LNKS Jun 18, float 1.5M), (b) added **float** to the per-case data recorded, and (c) instructed the eval to also record the float of the same-night faders the rule *correctly* skipped (e.g. TGE 44.2M), with an explicit hypothesis that re-exploders are distinguished by very low float (<~3M) so the eventual exception can be a conditional low-float PM-open re-check rather than a blanket one.
   - Why: the tally was started Jun 17 with only price/P&L fields; the first two cases (CRE, LNKS) and the contrast faders (TGE high-float, faded as predicted) suggest float is the key separator, but the tracker wasn't capturing it. Without float on both the false-negatives and the true-negatives, a future ≥4/5 dataset couldn't be used to design a *conditional* exception — only a risky blanket one.
   - Hypothesis: over the next 2–4 weeks the tracker accumulates float for each fade-skip re-explosion and each correctly-skipped fader. Measurable: if the re-exploders cluster at float <~3M while the correctly-skipped faders sit higher, that supports a low-float-only PM re-check exception; if floats overlap, float is not the separator and the blanket SPIKE→FADE skip stands. No change to the live skip rule until ≥4/5 accumulate.

**Updated process:** Fade-rule false-negative tracker now records float (and same-night correctly-skipped faders' floats) per case.

### 2026-06-17 — Instrument Fade-Rule False-Negative Tracker (CRE PM Re-Explosion)

**Context:** June 16→17 was the **best scanner night on record**: both of the morning's biggest movers (LNAI +173%, NIVF +166%) were detected AND traded. LNAI cleared the 2-AH-scan gate at 23:30 CET (+20.9% → +103.9%) on a clean BUILD-and-hold and was entered at $5.80; NIVF cleared at 00:30 CET (568K float, anti-dilution catalyst) entered at $0.81. Both were sold green in the premarket pulse (LNAI +10.9%, NIVF +67.9%; session realized +$78.36). The BUILD-and-hold + 2-scan + hold-vs-fade logic selected both correctly and rejected every fader (MYSE, FLZH, GDHG all faded into PM as predicted). Detection ticked to 87.5% (28/32), selection to 62.5% (20/32). The one notable miss was **CRE**: it spiked to an AH peak $4.65 (+48%) at 17:30 ET then faded steadily (correctly skipped on the SPIKE→FADE rule), but **re-exploded in premarket to $5.99 (+90%)** — its PM peak exceeded its AH peak. This is the first clear case of an AH-fader re-exploding in PM, a potential false negative of the fade-skip rule. The morning eval recommended tracking repeats before deciding whether the rule needs a PM-open re-check exception. No detection or selection gap to fix (the scanner did everything right), so this is pure instrumentation, mirroring the proven ceiling-override / dead-cat-override / PM-only-gapper watch pattern.

**Evaluation of previous changes:**
- 2026-06-16 Instrument PM-only gapper frequency (TDIC): **Working.** The June 17 eval ran the classification on its biggest raw mover (LNAI, +172.9%) and correctly logged it as an **AH→PM continuation** (moved +146% in AH, fully detectable and traded), explicitly leaving the PM-only tally unchanged (CIIT, GLXG, TDIC). The instrumentation produced its first data point exactly as designed, and the point favors the AH strategy being competitive (the night's biggest mover was a continuation we caught).
- 2026-06-12 Instrument dead-cat-override watch (BYAH): **Insufficient data.** SDOT (Day -63.1% crash, AH bounce to Total -35%) appeared all night but never reclaimed above its regular close, so no DEAD-CAT-OVERRIDE WATCH was flagged. The eval correctly logged nothing to tally. Watch remains open.
- 2026-06-11 Quantify the early-peak base-hold exception (within ~20% of AH high): **Tangentially supportive.** NIVF was an early-peaker (AH high $0.96 at 17:45 ET) entered at $0.81, -14.6% off its high (inside the 20% band) on a holding base, and won big (+67.9%). The rule correctly admitted it rather than misclassifying it as a fade. No deep-collapse-low-rebuild candidate appeared to exercise the skip side. Threshold behaved correctly on the admit side.
- 2026-06-09 Ceiling-override watch for BUILD-and-hold: **Insufficient data (still open).** LNAI's Total% +122% was under the +150% ceiling; no qualifying >150% BUILD-and-hold candidate appeared. Nothing to tally. Watch remains open.

**Changes:**
1. **prompts/morning-evaluation.md** — Added a "Fade-rule false-negative tracking" instruction to Step 4 (Scanner Diagnostic). Each morning, identify any candidate skipped on the SPIKE→FADE / early-peak-fade rule that then re-exploded in premarket (PM peak above its AH peak and above a profitable hypothetical entry), and record it in a running tally with hypothetical AH-entry→PM-peak P&L, seeded with CRE. Explicitly states a single case does not justify relaxing the rule (the fade rule correctly skipped MYSE/FLZH/GDHG the same night); only a recurring pattern (≥4/5 re-exploding) would warrant a PM-open re-check exception.
   - Why: CRE is the first clean case of an AH-fader re-exploding in PM, and it was noted ad hoc in the Jun 17 log with no running count. Without a tally we cannot tell whether AH-faders that re-explode are a recurring exploitable pattern or a one-off. Instrumenting builds the dataset without changing the SPIKE→FADE rule or risking false positives (the rule still saved capital on three faders the same night).
   - Hypothesis: Over the next 2–4 weeks the morning eval logs each AH-fader→PM-re-explosion case with hypothetical P&L, accumulating a tally. Measurable: (1) the next night a fade-skipped candidate re-explodes in PM, the eval records a tracker row; (2) after ~15 sessions the tally shows how often fade-skips are false negatives. If ≥4/5 of fade-skipped names re-explode in PM, it argues for a PM-open re-check exception (a rule decision left to the user); if they stay rare, the flat SPIKE→FADE skip stands.

**Updated process:** Added the fade-rule false-negative tracker to the morning evaluation diagnostics (Current Process list above).

### 2026-06-16 — Instrument PM-Only Gapper Frequency (TDIC Blind Spot)

**Context:** June 15 night was a clean detection + selection day for the AH→PM strategy (CRVO caught, activated on the 2-scan gate, traded), pushing detection to 87.1% (27/31, baseline met). But the morning's *biggest raw mover* was again a **PM-only gapper** the AH scanner cannot see by design: **TDIC** exploded to +140% in premarket (peak $13.83, 04:05 ET) while sitting flat-to-down (-4% to -8%) all evening in after-hours. This is the recurring structural blind spot: a stock with no AH footprint that gaps on overnight/early-AM news after 04:00 ET. It is the 3rd such case in recent weeks — CIIT (Jun 10, +140%), GLXG (Jun 11, +343%), now TDIC (Jun 16, +140%) — and each was noted ad hoc in its log with no running tally. The Jun 16 eval explicitly recommended tracking *how often* the morning's biggest mover is a PM-only gapper vs an AH→PM continuation, to decide whether a separate early-PM scan workflow is warranted. There is no detection-threshold gap to fix (a flat-AH stock has nothing to detect), so this is pure instrumentation, mirroring the proven ceiling-override / dead-cat-override watch pattern.

**Evaluation of previous changes:**
- 2026-06-12 Instrument dead-cat-override watch (BYAH): **Insufficient data.** June 15 night flagged no DEAD-CAT-OVERRIDE WATCH candidate (no Day% ≤ -15% name that BUILT in AH to reclaim above its regular close). The morning eval correctly recorded "no override-watch outcomes to tally." Watch remains open.
- 2026-06-11 Quantify the early-peak base-hold exception (within ~20% of AH high): **Insufficient data.** June 15 produced no deep-collapse-low-rebuild candidate to exercise the SKYQ exception. The names traded (HUBC, WCT, CRVO) were not within-20%-of-high misclassifications — CRVO was a genuine BUILD-and-hold (entered $3.64 vs AH high $3.77, inside the band) that still faded as a no-catalyst name. Threshold neither misfired nor validated.
- 2026-06-09 Ceiling-override watch for BUILD-and-hold: **Insufficient data (still open).** June 15 RGNT breached the ceiling but on a regular-session blow-off (+564% Day), not an AH BUILD-and-hold with VRatio >5x, so nothing qualified. The morning eval correctly logged nothing to tally. No qualifying post-17:00 BUILD-and-hold >150% candidate yet.

**Changes:**
1. **prompts/morning-evaluation.md** — Added a "PM-only gapper tracking" instruction to Step 4 (Scanner Diagnostic). Each morning, identify the single biggest raw PM mover and classify it as an AH→PM continuation (detectable) or a PM-only gapper (flat/down in AH, undetectable), keeping a running tally seeded with the three known cases (CIIT, GLXG, TDIC). Explicitly states a PM-only gapper is not a detection-baseline failure.
   - Why: PM-only gappers have been the morning's biggest mover 3 times recently, each noted ad hoc with no tally. Without a running count we cannot tell whether they dominate (justifying an early-PM scan experiment) or are occasional. Instrumenting builds the dataset without changing the strategy or risking the scanner.
   - Hypothesis: Over the next 2–4 weeks the morning eval logs a PM-only-vs-AH→PM classification of the biggest mover each night, accumulating a tally. Measurable: (1) the next morning eval records the classification line for its biggest mover; (2) after ~15 sessions the tally shows the PM-only share. If PM-only gappers are the biggest mover in a clear majority (≥60%), it argues for a separate early-PM scan workflow (a coverage decision left to the user); if AH→PM continuations stay competitive, the current AH-only coverage stands.

**Updated process:** Added the PM-only gapper tracker to the morning evaluation diagnostics (Current Process list below).

### 2026-06-12 — Instrument Dead-Cat-Override Watch (BYAH Miss)

**Context:** June 11 night was the second consecutive detection win / selection loss. BYAH (Household/Personal Care, 1.0M float, no catalyst) was the night's best BUILD shape and was on the board in **all four** entry-window scans (23:00 +98% → 00:30 +141% CET), explicitly logged each scan as "a clean test of whether the dead-cat filter costs winners." It was disqualified solely by the **Day% ≤ -15% dead-cat filter** (Day -15.3%, sitting *exactly* on the threshold). It went on to a PM peak of $3.58 (+189% from prev close), making **new highs above its AH peak** — a hypothetical +72% AH-detection trade and the night's best setup. We instead traded RKDA (Day +18.4%, no dead-cat flag), which round-tripped to -17.5%. The dead-cat filter's thesis is "recovering from a sell-off, still falling" — but BYAH's AH BUILD reclaimed ~+100% above its regular close, which the filter is blind to. Detection holds at 86.7% (26/30, baseline met); the bottleneck is now **selection** (60%), with a filter blocking the winner two nights running (Jun 11 one-position rule on TMDE, Jun 12 dead-cat on BYAH).

**Evaluation of previous changes:**
- 2026-06-11 Quantify the early-peak base-hold exception (within ~20% of AH high): **Insufficient data — no clean test.** June 11 produced no deep-collapse-low-rebuild candidate to exercise the SKYQ exception. BYAH was a clean BUILD (held within 20%, made new highs) and was blocked by a different filter (dead-cat). RKDA, the name actually traded, was an early-peaker entered within ~7% of its AH high ($1.26 vs $1.35) — inside the 20% band, so the rule correctly *did not* block it; it still faded to -17.5%, but that is a no-catalyst-pump outcome, not a within-20% misclassification. The threshold neither misfired nor was validated. Watch continues.
- 2026-06-09 Ceiling-override watch for BUILD-and-hold: **Insufficient data (still open).** June 11 EDHL breached the +150% ceiling, ran to a near-extreme $11.39 AH late surge, then faded into PM (PM < AH) — it failed the override criteria (VRatio <5x, early peak) so nothing was tallied, but it again supports keeping the ceiling on extreme late surges. No qualifying post-17:00 BUILD-and-hold >150% candidate yet.

**Changes:**
1. **prompts/post-market-scan.md** — Added a "Dead-cat-override watch (data collection)" clause to the dead-cat skip rule. A Day% ≤ -15% candidate that BUILDS in AH to *reclaim above its regular close* (AH% rising across ≥2 after-hours scans) is no longer treated as a plain dead-cat bounce: still skipped from live entry, but flagged **DEAD-CAT-OVERRIDE WATCH** with a hypothetical entry recorded. Cited BYAH as the founding case.
   - Why: BYAH was blocked solely on Day% sitting on the threshold, despite an AH BUILD that reclaimed ~+100% above its regular close — logically distinct from "still falling from a sell-off." Removing the filter outright risks re-admitting genuine bounces (only 1 winner vs the filter's 3+ losers), so this instruments the case without relaxing protection, mirroring the proven ceiling-override-watch pattern.
   - Hypothesis: Over the next 2–4 weeks we accumulate a tally of dead-cat-override candidates (deep regular-session sell-off + AH BUILD reclaiming above close) and their PM outcomes. Measurable: (1) the next night with such a candidate logs a DEAD-CAT-OVERRIDE WATCH flag with hypothetical entry; (2) the morning eval records its follow-through. If these win consistently (≥4/5), it justifies making the dead-cat filter conditional; if mixed, the flat filter stands.
2. **prompts/morning-evaluation.md** — Added a "Dead-cat-override watch outcomes" instruction beside the ceiling-override one: look up any DEAD-CAT-OVERRIDE WATCH flags from the prior night's log and record their hypothetical P&L (skipped entry → PM peak) in Notes, tallying over time.
   - Why: The evening flag only builds the dataset if the morning loop closes it with an outcome.
   - Hypothesis: The dead-cat-override dataset grows by one row per qualifying night, giving the future decision an evidence base instead of a single anecdote.

**Updated process:** Added the dead-cat-override watch clause to the "Skip dead-cat bounces" line in Current Process.

### 2026-06-11 — Quantify the Early-Peak Base-Hold Exception (SKYQ Loss)

**Context:** June 10 night was a detection win but a selection loss. SKYQ was entered at $2.28 (00:00 CET / 18:00 ET) and closed at -27.6% the next morning. The entry reasoning explicitly invoked the CHAI "held base despite early peak" exception: SKYQ peaked +129% ($3.58) at 17:00 ET, collapsed -36% to a base, and was "holding/rebuilding" across the 23:30 (+40%) → 00:00 (+46%) → 00:30 (+49%) scans. But that rebuild was to a base **64% below the AH high** ($2.28 vs $3.58), it had **no company catalyst** (Grade None, macro oil/Iran sector beta), and it round-tripped the entire AH spike overnight (PM high only $1.80). The CHAI/MSW exception was over-applied: CHAI made a *new* AH high at 17:20 and held within 20% of it; MSW was entered while still building toward its peak. SKYQ never reclaimed — it stabilized at less than half its peak level. The existing rule said "holding near its AH high" with no quantitative threshold, so a deep-collapse-low-rebuild was misread as a hold. Detection baseline remains met (25/29 = 86.2%); this is a downstream selection-quality fix.

**Evaluation of previous changes:**
- 2026-06-10 Instrument AH-vs-PM peak tracking (morning-evaluation): **Working.** The June 11 morning eval ran the AH-peak-vs-PM-peak check and tallied that *every* AH mover (SKYQ, TMDE, BATL, FLYE, DAIC, RBNE, GLBS) peaked in AH and faded into PM, adding TMDE (AH +98.6% > PM +78%) to the running "AH was the better exit" tally alongside MSW. The instrumentation is producing the dataset as designed. TMDE also showed a *moderate* AH runner (<+250%) peaks in AH, extending the pattern beyond extreme runners. Exit-timing conclusions remain the user's domain.
- 2026-06-10 Subordinate AH peak time to hold-vs-fade (post-market-scan reframe): **Partially tested / mixed.** June 10 had no clean before-18:30 BUILD-and-hold to validate the admit-side, but the reframe's hold-vs-fade emphasis was the exact lever that *misfired* on SKYQ — the agent classified a deep-collapse low-rebuild as a "hold." This entry sharpens that exception with a quantitative threshold rather than reverting it.
- 2026-06-09 Ceiling-override watch for BUILD-and-hold: **Insufficient data (2 more nights).** June 10 (CPOP +369% multi-day blow-off) and June 11 (CPOP again) produced no qualifying post-17:00 BUILD-and-hold >150% candidate. Watch remains open.

**Changes:**
1. **prompts/post-market-scan.md** — Added a quantitative definition to the early-peak base-hold exception: "holding" requires the current price to be within ~20% of the AH high (or making new highs); a deep collapse (>20% off the high) that stabilizes at a much lower base is a fade, not a hold — especially on Grade-None macro/sector-beta names. Cited SKYQ (+129%→+46% rebuild→-27.6%) as the counter-example alongside CHAI/MSW.
   - Why: SKYQ was entered by over-applying the qualitative "holding near its AH high" wording to a base 64% below the peak. CHAI/MSW both held within 20% of their high (or were still building); SKYQ did not. A threshold disambiguates the two cases.
   - Hypothesis: Next time a candidate peaks early, collapses >20% off its AH high, and stabilizes at a much lower base (especially Grade None / macro-beta), the agent classifies it as a fade and skips it, rather than entering on a "holding/rebuilding" rationale. Measurable: (1) no entry on a >20%-off-high low-rebuild Grade-None name; (2) genuine CHAI/MSW-style within-20%-of-high or still-building candidates are still admitted.

**Updated process:** Added the early-peak base-hold "within ~20% of AH high" qualifier to Current Process.

### 2026-06-10 — Subordinate AH Peak Time to Hold-vs-Fade; Instrument AH-vs-PM Peak Tracking

**Context:** June 9 night was a clean detection + selection win. MSW (Engineering & Construction, float 4.6M) was caught at the 23:00 CET entry-eligible scan (+25.8%), confirmed BUILD with a 2nd scan at 23:30 (+65.2%), and was traded at $3.24. It ran to an AH high of $5.18 (+292%) at 18:00 ET, then a PM high of $4.24 (+221%) — i.e. it **peaked before the 18:30 ET boundary** yet still followed through (+31% over entry at PM peak). Two issues surfaced: (1) MSW is the second before-18:30 BUILD-and-hold winner (after CHAI 17:20 / MTEN 17:40 on June 8), directly contradicting the "before 18:30 = 0/6 failures" framing; (2) MSW's AH peak (+292%) exceeded its PM peak (+221%) — the AH was the better exit, breaking the strategy's AH→PM-continuation thesis. Baseline detection is at 24/28 = 85.7% (met).

**Evaluation of previous changes:**
- 2026-06-09 Ceiling-override watch for BUILD-and-hold: **Insufficient data.** June 9 produced no qualifying CEILING-OVERRIDE WATCH candidate — the names exceeding +150% (CCTG, AZI) were SPIKE→FADE / microstructure-driven, not BUILD-and-hold with VRatio >5x. The morning eval correctly logged "nothing to tally." Tangentially supportive: MSW entered at +145.5% (just under the ceiling) as a BUILD-and-hold and won big (AH +292%), reinforcing that near-ceiling BUILD-and-hold can work — but it was below the ceiling, so not a ceiling-override case. Watch remains open, awaiting a qualifying >150% BUILD-and-hold night.
- 2026-06-05 Correct AH Peak Timing Boundary to 18:30 ET: **Boundary is real but the failure stat was over-attributed to peak time.** MSW (peak 18:00 ET) is now the 2nd before-18:30 BUILD-and-hold to follow through. The losers behind the "0/6" stat (OCG, CNET, FOXX, ANY) were all *early-peakers that also faded*. The distinguishing factor is hold-vs-fade, not the absolute 18:30 timestamp. Revised this entry (see change 1) rather than the boundary value itself.

**Changes:**
1. **prompts/post-market-scan.md** — Reframed the "AH peak timing" rule as "AH peak timing matters, but trajectory dominates." The 0/6 failure stat is now explicitly attributed to early-peakers that are *also fading*; added CHAI and MSW as before-18:30 BUILD-and-hold counter-examples; stated that an early peak is only a disqualifier when the stock is *also* declining across scans.
   - Why: Two clean counter-examples (CHAI, MSW) show before-18:30 peaks following through when the candidate holds/builds. The prior wording risked deprioritizing a genuine BUILD-and-hold purely on peak timestamp.
   - Hypothesis: Future scans will no longer flag a before-18:30 peak as a concern when the candidate is holding/building. Measurable: (1) the next night with a before-18:30 BUILD-and-hold candidate evaluates it on trajectory, not peak time, and is not deprioritized solely for the early peak; (2) early-peak *faders* continue to be skipped. No hard rule changed.
2. **prompts/morning-evaluation.md** — Added an "AH-peak-vs-PM-peak check" to the AH Mover Follow-Through section: record whether each mover's PM peak exceeded or fell short of its AH peak, flag AH-was-better-exit cases, and tally extreme AH runners (>250% from close) to test whether they peak in AH and fade into PM.
   - Why: MSW peaked higher in AH than PM, breaking the AH→PM thesis. This is one data point; systematic tracking builds the dataset before any exit-timing conclusion.
   - Hypothesis: Each future night with an extreme AH runner logs an AH-vs-PM peak comparison, accumulating a tally. If extreme AH runners repeatedly peak in AH (≥4/5), it argues for partial late-AH profit-taking on those names (an exit-domain decision left to the user).

**Updated process:** Reworded the "AH peak timing" clause in the Trajectory preference line to mark peak time as a secondary tiebreaker subordinate to hold-vs-fade.

### 2026-06-09 — Instrument Ceiling-Override Watch for BUILD-and-Hold Cases

**Context:** June 8 was a NO-ENTRY night, but the morning evaluation surfaced a clear entry-rule tension (not a detection gap). CHAI was detected in all four entry-eligible scans (23:00 +217% → 00:30 +249% CET), made a *new* AH high at 17:20 ET, held a $2.8–3.4 base all evening, and continued into PM ($4.47, +438% from close). Had we entered at the first eligible scan ($2.60), the hypothetical return was **+72%**. It was skipped on every scan purely by the **+150% extension ceiling**. Meanwhile the early-peak fades that same night (OCG 16:35 ET, CNET 16:45 ET, BGI 17:50 ET) all died below their prior close — the ceiling correctly excluded those. Detection baseline is solidly met (23/27 = 85.2%); the bottleneck has moved downstream to entry rules. The June 8 eval explicitly recommended *collecting more BUILD-vs-extension cases* before deciding whether the ceiling should become conditional.

**Evaluation of previous changes:**
- 2026-06-05 Correct AH Peak Timing Boundary to 18:30 ET: **Applied, with new nuance.** June 8 scans repeatedly cited the "18:30 ET continuation cutoff" when classifying candidates, so the boundary is being used as intended. However, the night's two PM carriers (CHAI peak 17:20 ET, MTEN peak 17:40 ET) both peaked *before* 18:30 ET yet still followed through because they **held a base** rather than fading. The clean failures (OCG 16:35, CNET 16:45) peaked early *and* faded. This suggests hold-vs-fade is the dominant signal and peak time is secondary — but it's one night of data. No revision to the boundary yet; the ceiling-override watch (below) will help disentangle hold-vs-fade from absolute peak time.
- 2026-06-03 Delay Entry When Only 23:00 Candidate Exceeds 150%: **Working / reinforced.** On June 8, CHAI exceeded 150% at 23:00 and the agent correctly waited rather than entering; no lower-extension BUILD alternative appeared, so it remained a no-entry. The wait behaved as designed.

**Changes:**
1. **prompts/post-market-scan.md** — Added a "Ceiling-override watch (data collection)" clause to the extension-ceiling rule. When a candidate exceeds +150% Total% but shows a genuine BUILD-and-hold profile (AH high after 17:00 ET, holding within ~20% of that high across ≥2 AH scans, VRatio >5x), still skip the entry but flag it **CEILING-OVERRIDE WATCH** and record a hypothetical entry.
   - Why: CHAI is the 2nd recent detected BUILD winner skipped solely on the ceiling. Relaxing the ceiling on one data point risks re-admitting blow-off tops (PRFX +439%→-28.8%). Instrumenting collects evidence without risking capital.
   - Hypothesis: Over the next 2–4 weeks we accumulate a clean tally of ceiling-skipped BUILD-and-hold candidates and their PM outcomes. Measurable: (1) the next night with a >150% BUILD-and-hold candidate logs a CEILING-OVERRIDE WATCH flag with hypothetical entry; (2) the morning eval records its follow-through. If these candidates win consistently (≥4/5), it justifies making the ceiling conditional; if they're mixed, the flat ceiling stands.
2. **prompts/morning-evaluation.md** — Added a Scanner Diagnostic instruction to look up any CEILING-OVERRIDE WATCH flags from the prior night's log and record their hypothetical P&L (skipped entry → PM peak) in Notes, tallying over time.
   - Why: The evening flag is only useful if the morning loop closes it with an outcome.
   - Hypothesis: The ceiling-override dataset grows by one row per qualifying night, giving the future decision an evidence base instead of anecdote.

**Updated process:** Added the ceiling-override watch clause to the "Entry extension ceiling" line in Current Process.

### 2026-06-05 — Correct AH Peak Timing Boundary to 18:30 ET

**Context:** June 4 data review revealed the June 4 changelog entry miscategorized peak times. FOXX was listed as "before 18:00 ET" but actually peaked at 18:20 ET. DXST (18:35) and LNKS (18:50) were listed as "after 19:00 ET" but peaked between 18:00-19:00. The actual data shows:

- Before 18:30 ET: ANY (17:15) lost -21.3%, FOXX (18:20) lost -15.7% → 0/6+ failures
- After 18:30 ET: DXST (18:35) +74.7%, LNKS (18:50) +61%, WOK (19:05) +177%, TWAV (19:50) +38.5% → 4/4 wins

The boundary is at 18:30 ET, not 18:00/19:00 as previously stated.

**Evaluation of previous changes:**
- 2026-06-04 Sharpen AH Peak Timing Threshold: **Data categorization was incorrect.** FOXX peaked at 18:20 ET, not before 18:00 ET. The loss at 18:20 ET shows the 18:00 boundary was too early. DXST/LNKS at 18:35/18:50 were wins despite peaking before 19:00. The true boundary is 18:30 ET.
- 2026-06-03 Delay Entry When Only 23:00 Candidate Exceeds 150%: **Insufficient data.** FOXX was at +137% (under 150% ceiling) on June 3, so the rule wasn't tested.

**Changes:**
1. **prompts/post-market-scan.md** — Corrected AH peak timing threshold from dual boundaries (18:00/19:00) to single boundary (18:30 ET). Updated data counts: before 18:30 = 0/6+ failures, after 18:30 = 4/4 wins.
   - Why: FOXX at 18:20 ET lost despite being after the previous 18:00 threshold. The actual cutoff is ~18:30 ET based on where losses end (18:20) and wins begin (18:35).
   - Hypothesis: At later scans, the agent will use 18:30 ET as the peak timing boundary. Stocks peaking before 18:30 ET will be deprioritized; stocks peaking after 18:30 ET will be preferred. Measurable: (1) next evening scan explicitly cites 18:30 ET threshold, (2) candidates with 18:00-18:30 peak times are treated as early-peakers (concern), not safe.

**Updated process:** Changed peak timing from "18:00 ET / 19:00 ET" to "18:30 ET" in Current Process section.

### 2026-06-04 — Sharpen AH Peak Timing Threshold

**Context:** June 1-4 data shows a clear pattern in AH peak timing vs PM follow-through:
- Late peaks (after 19:00 ET / 01:00 CET): TWAV 19:50→+38.5%, DXST 18:35→+74.7%, LNKS 18:50→+61%, WOK 19:05→+177% — **4/4 winners**
- Early peaks (before 18:00 ET / 00:00 CET): FOXX 18:20→-15.7%, ACCL 17:15→fade, SNAL 16:35→fade, TDIC 17:00→fade, XOS 16:35→lost — **0/5+ failures**

The current prompt said "16:00-17:30 ET" as the early peak window. Data shows 18:00 ET is the real boundary, with stocks peaking after 19:00 ET being the strongest.

**Evaluation of previous changes:**
- 2026-06-03 Delay Entry When Only 23:00 Candidate Exceeds 150%: **Insufficient data.** On June 3 evening, FOXX was at +137% (under 150% ceiling), so the rule wasn't tested. Need a case where a candidate exceeds 150% at 23:00 to evaluate.

**Changes:**
1. **prompts/post-market-scan.md** — Updated AH peak timing guidance from vague "16:00-17:30 ET" to specific thresholds with data: before 18:00 ET = 0/5+ failures, after 19:00 ET = 4/4 wins. Added explicit preference for late-peaking or still-building candidates.
   - Why: FOXX peaked at 18:20 ET and lost -15.7%. TWAV peaked at 19:50 ET and would have won +38.5%. The prior guidance wasn't specific enough to distinguish these cases.
   - Hypothesis: At later scans, the agent will explicitly check peak times and prefer candidates that peaked after 19:00 ET or are still building. Measurable: (1) next evening scan at 00:00+ CET mentions peak TIME when comparing candidates, (2) when choosing between an early-peaker and late-peaker, the late-peaker is preferred.

**Updated process:** Added specific peak timing thresholds to trajectory preference line.

### 2026-06-03 — Delay Entry When Only 23:00 Candidate Exceeds 150%

**Context:** June 1-2 showed that the 150% extension ceiling exception clause ("unless no alternatives exist") was being interpreted too loosely. ANY was entered at +154.7% at 23:00 because no other candidates qualified at that exact scan. Result: -21.3% loss. Meanwhile, DXST emerged at 00:30 with a +57% entry point and went on to gain +74.7%. The exception clause let the agent enter an extended position 90 minutes before a much better candidate appeared.

Additional data point: On June 2 evening, XOS showed BUILD pattern at 23:30 with +110.7% extension (within ceiling) but was blocked by the open ANY position.

**Evaluation of previous changes:**
- 2026-05-29 Entry Extension Ceiling: **Threshold correct, exception too loose.** ANY at +154.7% was allowed because "no alternatives at 23:00." The ceiling correctly flagged the concern, but the escape clause enabled the bad entry. Data: ANY +155%→-21.3%, while DXST +57%→+74.7% appeared 90 minutes later.
- 2026-05-28 Skip SPIKE→FADE-Only Nights: **Working.** June 2 correctly identified YMAT (+70% early peak→+17% fade), UFG (+40% early peak→+12% fade) as SPIKE→FADE and noted "would skip all."
- 2026-05-27 Trajectory Overrides Catalyst: **Insufficient data.** One-position rule blocks most test scenarios where trajectory vs catalyst choice is needed.
- 2026-05-22 High-Change Fallback: **Insufficient data.** No data gap winners since the change.

**Changes:**
1. **prompts/post-market-scan.md** — Strengthened the 150% extension ceiling from soft exception to explicit wait-for-later-scans guidance. If the only candidate at 23:00 exceeds 150%, wait for 23:30/00:00 before entering. Only enter above 150% if it's past 00:00 CET and no lower-extension alternatives have appeared across all scans.
   - Why: The previous wording ("unless no alternatives exist") was interpreted as "no alternatives at this exact scan." This allowed ANY (+155%) entry at 23:00 while DXST (+57%) was still building and appeared 90 minutes later.
   - Hypothesis: Next time a candidate exceeds 150% at 23:00 and is the only option, the agent will wait for 23:30 or 00:00 scans before entering. This allows late-building candidates to emerge. Measurable: (1) next 23:00 scan with only >150% candidate results in wait, (2) late-building alternatives are evaluated, (3) entries that happen are either below 150% or made after 00:00 with no alternatives across all scans.

**Updated parameters:** Added ANY +155%→-21.3% and DXST +57%→+75% to extension data in prompt.

### 2026-05-29 — Entry Extension Ceiling (150% Total%)

**Context:** Three consecutive paper trade losses all shared extreme entry extension:
- PRFX: Entry at +439% Total% → -28.8% loss
- VCIG: Entry at +194% Total% → -7.9% loss  
- ATPC: Entry at +154% Total% → -14.1% loss

Meanwhile, lower-extension entries have been winning:
- AMST: Entry at +76% Total% → +124% win
- NXTT: Entry at ~+23% Total% → +19% win

The May 29 morning evaluation explicitly recommended: "Consider maximum entry extension threshold." When a stock is already up 400%+ from the previous close, even a modest overnight fade (which is normal) turns a paper profit into a loss. PRFX peaked at $8.96 in AH but entry was at $7.28 — already 22% below peak at entry time.

**Evaluation of previous changes:**
- 2026-05-28 Skip SPIKE→FADE-Only Nights: **Working.** On May 28 evening, SPIKE→FADE candidates (ELAB, IOTR, OLOX) were correctly skipped at 23:00-23:30. Entry waited for PRFX's BUILD pattern at 00:00. The rule didn't prevent the loss because PRFX genuinely had BUILD pattern — the issue was extension, not trajectory.
- 2026-05-27 Trajectory Overrides Catalyst: **Still insufficient data.** May 27-28 evenings had no BUILD vs SPIKE→FADE choice — all qualifying candidates shared the same trajectory type.
- 2026-05-22 High-Change Fallback: **Insufficient data.** No data gap winners since the change.

**Changes:**
1. **prompts/post-market-scan.md** — Added "Entry extension ceiling" guidance. Candidates with Entry Total% above +150% should be skipped. Extended entries leave no margin for overnight fade. If a BUILD-pattern stock exceeds 150%, note the concern but consider skipping unless no alternatives.
   - Why: 3/3 entries above +150% Total% lost (-28.8%, -14.1%, -7.9%). 2/2 entries below +100% Total% won (+124%, +19%). The pattern is clear: chasing extremely extended stocks fails even when trajectory and catalyst are favorable.
   - Hypothesis: Next time a candidate exceeds +150% Entry Total%, it will be skipped or entered with heavy concern noted. This prevents chasing parabolic moves that leave no margin for overnight pullback. Measurable: (1) next evening scan with a >150% Total% candidate cites this rule, (2) entries stay below 150% extension.

**Updated process:** Added "Entry extension ceiling: 150% Total%" to Current Process section.

### 2026-05-28 — Skip SPIKE→FADE-Only Nights

**Context:** Three consecutive paper trade losses (ATPC -14.1%, VCIG -7.9%, TRNR -18.3%) all shared the same pattern: SPIKE→FADE (peaked before 17:30 ET in early AH, then declining). In each case, the agent correctly identified the pattern and noted the 0/7+ historical failure rate, but entered anyway because learning phase rules said "enter with concerns." On May 27, the log explicitly noted "SAGT shows BUILD pattern (5/5 win rate) vs ATPC's SPIKE→FADE (0/7 win rate)" — but SAGT only appeared at 23:30 (after position was opened), and by 00:00 it had faded below threshold.

The existing rules covered BUILD vs SPIKE→FADE selection but didn't address what to do when ALL candidates are SPIKE→FADE. Result: predictable losses.

**Evaluation of previous changes:**
- 2026-05-27 Trajectory Overrides Catalyst: **Not yet testable.** On May 27 evening, both qualifying candidates (ATPC, LNKS) showed SPIKE→FADE patterns — there was no BUILD alternative at decision time to trigger the rule. The rule was not violated; the situation didn't arise.
- 2026-05-26 No-Catalyst Skip Rule Removal: **Working.** ATPC was entered despite no catalyst (entered with concern noted). The rule isn't causing skips. The issue is trajectory, not catalyst.
- 2026-05-22 High-Change Fallback: **Insufficient data.** No data gap winners since the change.

**Changes:**
1. **prompts/post-market-scan.md** — Added explicit "SPIKE→FADE-only nights" guidance. If all qualifying candidates at entry time show SPIKE→FADE pattern (peaked before 17:30 ET and now declining), skip all rather than entering the least-bad option. Clarified that a skip on such nights is not lost data — it's avoiding a predictable loss.
   - Why: Three consecutive entries (ATPC, VCIG, TRNR) followed SPIKE→FADE patterns despite concern notes. All lost. SPIKE→FADE is now 0/10+ for PM continuation. The learning phase philosophy of "enter anyway" doesn't apply when the historical data is this clear.
   - Hypothesis: Next SPIKE→FADE-only night (all candidates peaked early, now fading) will produce a "skip all" decision with this rule cited, instead of an entry. Measurable: (1) next evening scan where all qualifying candidates show early peaks and declining AH% will result in "skip all — SPIKE→FADE-only night", (2) this preserves capital for BUILD pattern nights.

**Updated process:** Added "skip all on SPIKE→FADE-only nights (0/10+ win rate)" to trajectory preference line.

### 2026-05-27 — Trajectory Overrides Catalyst in Selection

**Context:** May 26 evening scan detected both SNGX and VCIG. SNGX had a BUILD pattern (steady increase 16:00→18:45 ET, holding near highs) with no catalyst. VCIG had a B-grade catalyst (CEO $900K insider buy) but SPIKE→FADE pattern (peaked 16:20 ET, fading). Agent chose VCIG due to catalyst. Result: SNGX +74% hypothetical, VCIG -13.6% loss.

The prompt already said "prefer build/hold over spike→fade" but didn't explicitly say trajectory should override catalyst when patterns clearly diverge. The agent followed catalyst preference over trajectory.

**Evaluation of previous changes:**
- 2026-05-26 No-Catalyst Skip Rule Removal: **Working.** SNGX wasn't skipped for "no catalyst + float ≥2M" — it was passed over because VCIG had a catalyst. The rule change worked; the issue was trajectory vs catalyst weighting.
- 2026-05-22 High-Change Fallback: **Insufficient data.** No data gap winners since the change.

**Changes:**
1. **prompts/post-market-scan.md** — Added explicit "Trajectory overrides catalyst" guidance to the learning phase section. When one candidate shows BUILD pattern and another shows SPIKE→FADE, prefer the BUILD candidate even if it lacks a catalyst and the SPIKE→FADE has one. Added data: early-peak-fading 0/7 (VCIG, TRNR, BNZI, CODX, plus 4 from May 11-13), BUILD 5/5 (SNGX, PHGE ×2, AMST, NXTT).
   - Why: May 26 data shows trajectory is more predictive than catalyst. SNGX (no catalyst, BUILD) would have won +74%; VCIG (B-grade catalyst, SPIKE→FADE) lost -13.6%. The existing "prefer build/hold" guidance wasn't strong enough to override catalyst preference.
   - Hypothesis: Next time a BUILD-pattern no-catalyst candidate competes with a SPIKE→FADE catalyst-backed candidate, the BUILD candidate will be selected. Measurable: (1) next evening scan with trajectory divergence cites this rule when selecting, (2) the BUILD candidate is entered even without a catalyst.

**Updated process:** Added "trajectory overrides catalyst when patterns clearly diverge" to Current Process trajectory preference line.

### 2026-05-26 — Remove No-Catalyst Float-Based Skip Rule (Contradiction Fix)

**Context:** The post-market prompt contained a direct contradiction:
- Learning phase default (line 73): "Document concerns but enter anyway. A paper trade with noted concerns generates data; a skip generates nothing."
- No-catalyst handling (lines 76-77): "Float ≥2M: skip"

These rules conflicted. The May 15 change added float-based skipping based on 2 data points. The May 21 change acknowledged the conflict but added an exception instead of fixing it. Result: PHGE was skipped twice (May 20: +19.3%, May 25: +170%) despite the learning phase philosophy saying "enter anyway."

Recent no-catalyst outcomes:
- OCG 1.9M float: +14.9% ✅
- LNKS 633K float: +61% ✅
- PHGE 5.9M float: +19.3% 🔥 MISSED (skipped due to float ≥2M)
- PHGE 7.4M float: +170% 🔥 MISSED (skipped due to float ≥2M)

**Evaluation of previous changes:**
- 2026-05-22 High-Change Fallback: **Insufficient data.** No data gap winners since the change.
- 2026-05-21 BUILD Pattern Exception: **Failed — didn't solve root cause.** Added exception to skip rule instead of removing the skip. PHGE still got skipped.
- 2026-05-15 Ultra-Low Float No-Catalyst Exception: **Superseded.** The float-based logic is being removed entirely.
- 2026-05-14 AH Peak Timing Guidance: **Confirmed (7 data points).** Early-peak-fading pattern 0/7.

**Changes:**
1. **prompts/post-market-scan.md** — Removed the float-based no-catalyst skip rule entirely. Replaced with simple "enter with concern noted" for all no-catalyst stocks. Float is tracked for pattern analysis but is not a filter during learning phase. This aligns with the learning phase philosophy.
   - Why: The skip rule directly contradicted "enter anyway, document concerns." Adding exceptions (May 21) didn't fix the contradiction, just narrowed when it applied. The data shows no-catalyst stocks winning across all float ranges.
   - Hypothesis: Next no-catalyst candidate (any float) will be entered with concern noted rather than skipped. Measurable: no more skips citing "no catalyst + float ≥2M" as the reason.

### 2026-05-22 — Add High-Change Fallback for AH Data Gaps

**Context:** May 22 morning evaluation revealed GOVX (the day's winner, +45.6% hypothetical) was completely missed by the scanner despite showing +21-31% AH price change throughout the scanning window (22:00-00:30 CET). The issue: TradingView's API reported AH volume as 0, so the stock was filtered out by the `postmarket_volume > 50,000` requirement. This is the 4th winner missed due to data gaps, not scanner logic.

Recent trade outcomes (May 18-22):
- AMST +124% ✅ (BUILD pattern)
- CODX -29.2% ❌ (early peak 16:35 ET)
- BNZI -20.4% ❌ (early peak 16:15 ET)
- TRNR -18.3% ❌ (early peak 16:30 ET)

**Evaluation of previous changes:**
- 2026-05-21 BUILD Pattern Exception: **Insufficient data.** No BUILD-pattern no-catalyst high-float candidates have appeared since the change. GOVX (May 21 winner) wasn't detected at all due to data gap, so the BUILD exception wasn't tested.
- 2026-05-14 AH Peak Timing Guidance: **Confirmed (6+ data points).** TRNR (peaked 16:30 ET) lost -18.3%, extending early-peak-fading pattern to 0/6. The guidance is being followed — entries are made with concerns documented, but early-peak candidates remain the only qualifying stocks on some nights.
- 2026-05-15 Ultra-Low Float No-Catalyst Exception: **Working (3 data points).** BIYA +3.6%, OCG +14.9%, no false positives.

**Changes:**
1. **scripts/scan.py** — Added supplementary "high change" query for after-hours scans. When AH change >20%, the stock is included even if volume=0 or below threshold. This mirrors the existing "day movers" supplementary query for regular session.
   - Why: GOVX had +21-31% AH change but volume=0 in API. The current filters require BOTH volume AND change. A fallback that catches very high change (>20%) regardless of volume would have caught GOVX.
   - Hypothesis: Next time a stock moves >20% in AH but has 0 volume in the API (data gap scenario), it will appear in scanner results via the high-change fallback. Measurable: (1) next evening scan in AH mode will run both primary and high-change queries, (2) next data gap winner with >20% AH change will be detected.

**Updated parameters:** Added `MIN_AH_CHANGE_HIGH = 20%` for supplementary high-change scan.

### 2026-05-21 — Add BUILD Pattern Exception to No-Catalyst Rule

**Context:** May 21 morning evaluation revealed PHGE (5.9M float, no catalyst, BUILD pattern) was skipped due to "no catalyst + float ≥2M" rule. It would have won +19.3%. Meanwhile, BNZI (1.1M float, B-grade catalyst, early-peak-fading pattern) was entered and lost -20.4%. The scanner detected both correctly — the selection logic was the failure.

Key data from May 18-21:
- AMST (BUILD pattern, B-grade) → +124% ✅
- PHGE (BUILD pattern, no catalyst, 5.9M float) → Skipped, would have been +19.3%
- BNZI (early-peak-fading, B-grade) → -20.4% ❌ (confirms 0/5 pattern)
- CODX (mid-AH peak, B-grade, +43.8% Day%) → -29.2% ❌

**Evaluation of previous changes:**
- 2026-05-14 AH Peak Timing Guidance: **Confirmed (5 data points).** BNZI (peaked 16:15 ET, faded to +17.8% by entry) lost -20.4%, extending the early-peak-fading pattern to 0/5. Build patterns continue winning (AMST +124%, PHGE +19.3% hypothetical).
- 2026-05-15 Ultra-Low Float No-Catalyst Exception: **Working (2 data points).** BIYA +3.6%, OCG +14.9%. No false positives.
- 2026-05-12 PM Peak Tracking: **Working — generating data (9 data points).** BNZI peaked $5.87 in AH, collapsed to $3.53 in PM. Still building dataset.

**Changes:**
1. **prompts/post-market-scan.md** — Added BUILD pattern exception to the no-catalyst handling for float ≥2M stocks. If a stock shows a clear BUILD pattern (steadily increasing across scans, near/making new AH highs) and no other candidates qualify, it can be entered with heavy concerns noted despite lacking a catalyst.
   - Why: The current hard "skip" for float ≥2M + no catalyst conflicts with the learning phase philosophy ("enter anyway, document concerns"). PHGE was the only BUILD-pattern stock on May 20 and would have been the best entry. The pattern appears to be a stronger predictor than catalyst presence.
   - Hypothesis: Next time a no-catalyst stock with float ≥2M shows a BUILD pattern (steadily increasing, near AH highs), the agent will enter with maximum concerns noted rather than skipping. Measurable: (1) next BUILD-pattern no-catalyst high-float candidate is entered with the exception cited, (2) outcome added to this dataset (currently 1/1 wins).

**Updated process:** Added BUILD pattern exception note to no-catalyst rule in Current Process section.

### 2026-05-20 — Evaluations Only (No Changes)

**Context:** CODX (entered May 19, exited May 20) lost -29.2%. This is the first significant loss since the scanner improvements began. The scanner detected CODX correctly (B-grade catalyst, 3.4M float, sustained >10% AH in 2 scans). The loss appears to be position management, not scanner failure.

**Evaluation of previous changes:**
- 2026-05-15 Ultra-Low Float No-Catalyst Exception: **Helped (1 data point).** BIYA (1.6M float, no catalyst) was entered May 14 per this rule and won +3.6%. The agent correctly cited the ultra-low float exception when entering.
- 2026-05-14 AH Peak Timing Guidance: **Working (3 data points).** May 18 AMST entry notes "currently at AH high +76%" (build pattern), won +124%. May 19 RRGB explicitly skipped: "peaked $4.69 at 16:05 ET (early spike), now $4.45 — steady fade from early peak." May 19 CODX noted "Peak at 16:35 (not early), holding near highs" — this assessment was correct at entry time; the fade happened overnight.
- 2026-05-12 PM Peak Tracking: **Working — generating data (7 data points).** PM Peak and Peak Time columns appearing consistently. AMST peaked $3.40 at 08:15 ET, trail stop triggered at $2.62. CODX peaked $2.88, collapsed to $1.77. Still building dataset for exit timing conclusions.

**Emerging pattern (not yet actionable):**
Recent trades suggest that Day% at entry may correlate with outcome:
- Low Day% (fresh AH move): AMST -4.6% → +124%, SNAL -0.1% → +54%, LESL -5.3% → +1.1%, BIYA -4.6% → +3.6% (4/4 wins)
- High Day% (already ran during session): CODX +43.8% → -29.2% (0/1)

This aligns with the "first day of unusual volume" entry rule. However, with only 1 data point on the high-Day% side, no change is warranted. Will continue monitoring.

**Changes:** None. Scanner and prompts working as intended. The CODX loss is a position management lesson (peak P&L +15.2% never triggered the +30% trail stop), not a scanner gap.

### 2026-05-15 — Add No-Catalyst Exception for Ultra-Low Float Stocks

**Context:** May 12-14 data reveals that the "no catalyst = skip" rule is failing for ultra-low float stocks. LNKS (633K float, no catalyst) was skipped on May 13 but was the day's winner at +61% PM. OCG (1.9M float, no catalyst) was entered on May 12 and won +14.9%. Meanwhile, catalyst stocks have mixed results (TDIC A-tier lost -18.7%, XOS A-tier lost -14.3%).

The post-market prompt had conflicting guidance:
- Step 4 of catalyst search said "note 'no catalyst found' as a skip reason"
- Learning phase default said "document concerns but enter anyway"

This caused inconsistent behavior — LNKS was skipped despite the learning phase guidance.

**Evaluation of previous changes:**
- 2026-05-14 AH Peak Timing Guidance: **Insufficient data (1 data point).** May 14 evening session noted the pattern correctly ("All candidates peaked in early AH...warning pattern") and entered BIYA with concerns documented. Need PM outcome data.
- 2026-05-12 PM Peak Tracking: **Working — generating data (4 data points).** May 13-14 P&L tables include PM Peak and Peak Time. Data accumulating but no exit timing pattern identified yet.

**Changes:**
1. **prompts/post-market-scan.md** — Removed "as a skip reason" from catalyst search step 4. Added explicit "No-catalyst handling (learning phase)" section with float-based decision:
   - Float <2M: enter with concern noted (ultra-low float can move on momentum alone)
   - Float ≥2M: skip (higher float needs catalyst)
   - Why: 2/2 ultra-low float no-catalyst trades won (OCG +14.9%, LNKS +61% if entered). The prior guidance caused LNKS to be skipped despite being a clear winner.
   - Hypothesis: Next time an ultra-low float (<2M) stock has >10% AH sustained across 2 scans but no catalyst, the agent will enter with concern noted rather than skipping. Measurable: (1) next ultra-low-float no-catalyst candidate is entered with float cited as the exception, (2) no more skips that cite "no catalyst" as the sole reason for stocks under 2M float.
   - **Evaluation:** Helped. On 2026-05-14, BIYA (1.6M float, no catalyst) was entered per this rule with the ultra-low float exception cited. Won +3.6%.

**Updated process:** Added "No-catalyst exception" rule to Current Process section.

### 2026-05-14 — Add AH Peak Timing Guidance to Trajectory Preference

**Context:** May 11-13 data shows a clear pattern: stocks that peak early in AH (16:00-17:30 ET) tend to fade in PM, while stocks still building or near their AH high at later scans show better continuation. Specific data points:
- Late AH peaks (≥18:00 ET): LNKS 18:50 → +61% PM, WOK 19:05 → +177% PM, HTCO 17:50 → +50% PM (3/3 continuation)
- Early AH peaks (<17:30 ET): SNAL 16:35 → faded initially, AEHL 17:35 → faded, TDIC 17:00 → faded, XOS 16:35 → lost (0/4 initial continuation)

The existing trajectory preference ("prefer build/hold over spike→fade") doesn't explicitly consider WHEN the peak occurred. At later scans (00:00+ CET), comparing current price to AH peak provides a more actionable signal.

**Evaluation of previous changes:**
- 2026-05-12 PM Peak Tracking: **Working — generating data (2 data points).** May 13 P&L table correctly includes PM Peak and Peak Time columns. SNAL peaked $0.84 at 04:00 ET, LESL peaked $1.81 at 04:00 ET. Both showed late PM rallies — need more data to identify optimal exit windows.
- 2026-05-08 Catalyst Tier column: **Working — generating data (6 data points).** May 13 adds SNAL (B), LESL (B). Both B-tier earnings trades won (+54%, +1.1%). Tier B now 2/3 wins. Meanwhile LNKS (None — no catalyst, skipped) would have been best (+61%). The "no catalyst = skip" rule missed the biggest winner; needs investigation.

**Changes:**
1. **prompts/post-market-scan.md** — Added AH peak timing guidance to the trajectory preference section. At later scans (00:00+ CET), compare each candidate's current price to their AH peak. Stocks that peaked early and are now well below their peak should be deprioritized relative to stocks still near their AH high.
   - Why: The existing trajectory preference ("prefer build/hold over spike→fade") is pattern-based but doesn't explicitly consider timing. The 7-datapoint pattern (3/3 late peaks → continuation, 0/4 early peaks → fade) provides a concrete timing threshold that makes the preference more actionable.
   - Hypothesis: At scans after 00:00 CET, the agent will explicitly compare candidates' current prices to their AH peaks. When choosing between an early-peaker now fading and a late-builder still near its high, the late-builder will be selected. Measurable: (1) next evening session notes mention AH peak timing when comparing candidates, (2) next time both an early-peaker and late-builder qualify, the late-builder is entered.

**Updated parameters:** None. Prompt guidance only.

### 2026-05-12 — Add PM Peak Tracking to Morning Evaluation P&L Table

**Context:** May 11 paper trades show significant upside missed by not tracking peak timing. HTCO peaked at $10.65 (+82.4%) at 05:50 ET but was exited at $9.34 (+16.75%). XOS peaked at $2.56 at 04:20 ET but was exited at $2.16 (-14.3%). The log explicitly notes: "Consider setting profit targets at +25% to capture peaks." Without peak timing data, we can't identify optimal exit windows.

**Evaluation of previous changes:**
- 2026-05-08 Catalyst Tier column: **Working — generating data (4 data points).** Column populated correctly in all recent logs. Interesting early finding: HTCO (Tier C — governance) was the biggest winner (+16.75%), outperforming XOS (Tier A — Air Force demo) which lost -14.3%. 3/4 Tier A trades won but the correlation is weaker than expected. Need more data before drawing conclusions.
- 2026-05-07 Entry Total% definition clarification: **Helped (4 data points).** Values now calculated correctly in all recent logs. AIIO +46.7%, XOS +37.0%, HTCO +37.0% — all correctly derived from (entry - prev_close) / prev_close.
- 2026-05-06 Float threshold fix (<10M → <50M): **Helped (2 data points).** AIIO (13.5M float) entered without hesitation on May 7. May 11 trades (XOS 6.6M, HTCO 3.2M) were under 10M so didn't test the threshold.

**Changes:**
1. **prompts/morning-evaluation.md** — Added "PM Peak" and "Peak Time" columns to Paper Trade P&L table. Also added instruction to use `check-prices.py --pm-history` to find peak.
   - Why: May 11 HTCO peaked at +82% but we exited at +17% — 65 points of upside missed. Without tracking when stocks peak in PM, we can't identify optimal exit windows or set data-driven profit targets.
   - Hypothesis: After 10 paper trades with PM peak tracking, we'll identify a common peak window (e.g., 05:00-08:00 ET) and measure how much upside is missed by current exit timing. Measurable: (1) next P&L table includes PM Peak and Peak Time columns, (2) after 10 trades, compute average peak time and compare potential gain (entry→peak) vs. realized gain (entry→exit).

**Updated parameters:** None. New output columns only.

### 2026-05-08 — Add Catalyst Tier to Morning Evaluation P&L Table

**Context:** Last 4 paper trades (May 4-7) show catalyst quality is the strongest predictor of outcome — stronger than Entry Total%:
- MASK (D — dilution, $1.3M convertible note): -10.6%
- OCG (None — unverified): -16.7%
- ERNA (A — breakthrough preclinical data): +4.1%
- AIIO (A — $100M acquisition): +3.6%

4/4 trades match: Tier A catalyst → win, weak/no catalyst → loss. Entry Total% does NOT show a clean correlation (OCG at +41.8% lost worst, ERNA at +67.3% won). The P&L table tracks extension but not catalyst quality, making this correlation invisible for systematic review.

**Evaluation of previous changes:**
- 2026-05-07 Entry Total% definition clarification: **Helped (1 data point).** May 7 AIIO correctly shows "+46.7% = (0.88 - 0.60) / 0.60" — total from prev close, not just AH change. Compare to May 6 ERNA which was misrecorded as "+13.6% AH" before the fix.
- 2026-05-06 Float threshold fix (<10M → <50M in prompt): **Helped (1 data point).** May 7 AIIO (13.5M float) was entered without float-related hesitation. First trade in the 10-50M float range.
- 2026-05-06 Entry Total% column: **Working (2 data points).** May 6 was misrecorded (fixed by May 7 definition change), May 7 was correct. Column integration complete.

**Changes:**
1. **prompts/morning-evaluation.md** — Added "Catalyst" column to Paper Trade P&L table template (between Entry Total% and Entry Time). Includes tier classification (A/B/C/D/None) with brief label, plus a definition note explaining the tier system from Day Trading.md.
   - Why: 4 consecutive paper trades show a perfect correlation between catalyst tier and outcome, but the P&L table only tracked Entry Total% (which doesn't correlate as cleanly). Without a Catalyst column, this signal is buried in scan notes and requires manually cross-referencing. Systematic tracking enables data-driven conclusions about whether catalyst quality should become a hard filter.
   - Hypothesis: The next morning evaluation will include catalyst tier in the P&L table. After 10 total paper trades, we'll have enough data to determine if catalyst tier predicts outcome better than Entry Total%. Measurable: (1) next P&L table includes the Catalyst column, (2) after 10 trades, we can compute win rate by catalyst tier.

**Updated parameters:** None. New output column only.

### 2026-05-07 — Fix Changelog Header + Clarify Entry Total% Definition

**Context:** The mcap ceiling was raised from $100M to $300M in `scripts/scan.py` on May 7 (commit 382d449) after the May 6 evaluation showed OSG ($190M) and NNBR ($126M) were both missed. The changelog header still said $100M. Separately, the May 6 ERNA paper trade logged "Entry Total% = +13.6% AH" — that's just the AH change, not the total move from previous close (+67.3%). The column was added on May 6 to track extension, but the definition was ambiguous enough that it was filled incorrectly on first use.

**Evaluation of previous changes:**
- 2026-05-06 Entry Total% column: **Working but misrecorded (1 data point).** The column appeared in the May 6 P&L table as intended. However, it was filled with "+13.6% AH" (just the AH change) instead of the actual total from prev close (~+67.3%). The column exists; the definition needs clarification so it's filled correctly going forward.
- 2026-05-06 Float threshold fix (<10M → <50M in prompt): **Insufficient data.** No candidate in the 10-50M range was otherwise ideal on May 6. PMAX (469K float) and ERNA (~1.17M float) were both well under 10M. ZVIA (62.7M) was over 50M. The fix hasn't been tested yet.

**Changes:**
1. **SCANNER_CHANGELOG.md** — Updated "Current Scanner Parameters" header: MAX_MARKET_CAP from $100M to $300M to match the actual value in scan.py.
   - Why: Bookkeeping. The parameter was already changed in scan.py but the changelog was out of sync. This ensures future improvement sessions read the correct baseline.
   - Hypothesis: N/A (documentation fix only).

2. **prompts/morning-evaluation.md** — Added explicit definition of "Entry Total%" below the P&L table template: total change from previous close, calculated as `(entry_price - prev_close) / prev_close`, with a worked example.
   - Why: On May 6, the agent filled this column with "+13.6% AH" (AH change only) instead of "+67.3%" (total from prev close). The column exists to measure how extended the stock is at entry — it must include the regular session move. With 5 paper trades, the extension data is the most promising predictor of outcome, but only if recorded consistently.
   - Hypothesis: The next morning evaluation will record Entry Total% as the total change from previous close, not just AH change. Measurable: (1) next P&L table shows a percentage clearly derived from (entry_price - prev_close) / prev_close, (2) the value includes the Day% component, not just AH%.

**Updated parameters:** MAX_MARKET_CAP header corrected to $300M (scan.py already had this value).

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
