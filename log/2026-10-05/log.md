# Trading Log — 2026-10-05

No post-market scans, position evaluations, or paper trades were logged for this session. This file was created by the morning evaluation on October 6. Git history has **zero `post-market scan` commits** after the October 1 session's 00:30 CEST scan; the October 2 session is likewise empty (its log holds position evaluations only).

## Morning Evaluation — 12:56 CEST (06:56 ET, October 6)

**Pulse 1: OLOX is today's winner, and the scanner never had a chance to catch it.** OLOX built from its **$0.88** close to a **$1.66** AH high on **53.5M shares / 218,065 trades**, then hit **$2.245 (+155.1%)** at the 04:00 ET PM open on **5.65M shares / 40,877 trades**. **0 of 7** evening scans ran, so this is a coverage failure, not a detection miss. A SIP reconstruction shows OLOX would have cleared the 2-AH-scan gate at **23:00 CEST near $1.37**: **+63.9%** to the PM peak, about **+38.7%** to the 04:00–04:20 plateau. No positions, no fills.

This pulse ran **2h36m late** (scheduled 10:20 CEST). Discovery came first: `scan.py --all --session premarket` at 06:45 ET, then an unfiltered TradingView PM sweep (no price, market-cap, or volume limits; 70 names above +5%) and a listed-exchange sweep of October 5 regular-session movers above +15%. All levels below are **Alpaca SIP** daily closes and 5-minute bars through the **06:30 ET** bar. Yahoo was used only for timeline shape. Raw bars are preserved in [morning-evidence-2026-10-06.json](morning-evidence-2026-10-06.json).

### Today's Winner

**OLOX — Olenox Industries (building products / modular structures / oil-and-gas services; formerly Safe & Green Holdings, SGBX)**

- Catalyst: **None verified for October 5.** Two searches found no fresh release. Background only: a non-binding LOI to merge with CS Digital Ventures (bitcoin mining / AI infrastructure) and an October 2 8-K/A correcting the CS Digital earnout (per the pm-open row, StockTitan). SG Echo subsidiary entered Chapter 11 in May. Grade **None**.
- Previous close: **$0.88** (SIP, October 5). October 2 close **$0.8415**, so Day% **+4.6%**. The regular session was quiet: the daily bar's 53.7M volume is almost entirely the AH session.
- AH ignition: **16:00 ET**, $0.88→$1.015 on 1,089,440 shares / 4,652 trades; 16:05 bar **3,231,476 / 14,793**. At 16:15 ET (22:15 CEST) it traded **$1.18–$1.34 (+34–52%)** on 3.3M shares / 13,735 trades.
- AH path: BUILD to $1.49 at 16:50, pullback to $1.23 at 17:35, second BUILD from 18:00. **AH SIP high $1.66 (+88.6%) at 18:20 ET** on 1,770,438 / 7,947. At the 18:30 ET last-scan checkpoint: **$1.52–$1.55 (+73–76%)**. AH close **$1.62** at 19:55. AH total **53,479,264 shares / 218,065 trades**.
- PM peak: **$2.245 (+155.1%) at 04:00 ET**, 5,654,390 shares / 40,877 trades, VWAP $1.9316. Closes 04:00–04:20: **$1.81, $1.87, $1.9998, $1.83, $1.805**, five consecutive bars above the +100% level ($1.76) on 676K–5.65M shares per bar. Then $1.55–$1.76 closes through 06:30.
- Premarket now: **$1.68 (+90.9%)** at the 06:30 ET SIP bar. PM total through 06:30: 24.6M shares / 135,879 trades.
- Hypothetical P&L: first realistic sighting **22:30 CEST ~$1.21 → $2.245 = +85.5%**; 2-scan gate **23:00 CEST $1.37 (Entry Total +62.8%) → $2.245 = +63.9%**; to the ~$1.90 plateau **+38.7%**; to the latest $1.68 **+22.6%**. None of these is a fill.
- Float **1.26M** | Market cap **$1.46M** (TradingView; at the $0.88 close).
- Capturable: **yes.** `tradable=true`; Alpaca's book was two-sided at **16:59:59 ET** (bid $1.36 x100 / ask $1.45 x100), one second before the 23:00 CEST checkpoint. The quote has been frozen since then, so books after 17:00 ET are unverified.
- Winner bar: >100% from the true last-session close on accumulating SIP volume, with a fillable AH book. **Clears.** Yahoo misses the peak: Yahoo PM high $2.00 versus SIP $2.245; Yahoo AH high $1.64 versus SIP $1.66.

**Scanner Diagnostic:**

- Detectable at screening time (~22:15 CEST)? **YES on the tape, but no scan ran.** OLOX was +34–52% AH on multi-million-share bars by 16:15 ET. TradingView postmarket fields usually fill only from ~16:30 ET, so the **22:30 CEST scan** is the first realistic hit.
- SIP reconstruction of the scheduled checkpoints (latest complete bar): 22:30 **$1.21 / AH +37.5%**, 23:00 **$1.37 / +55.7%**, 23:30 **$1.36 / +54.5%**, 00:00 **$1.33 / +51.1%**, 00:30 **$1.55 / +76.1%**. That is five qualifying >10% AH checkpoints. Entry gates at 23:00 CEST: Total +62.8% (under the +150% ceiling), Day +4.6% (no dead-cat), BUILD trajectory, the high came after the first bar, and the book was fresh. It would have been entered.
- Why we didn't act: **0 of 7 evening scans ran.** This is a scheduler/bridge outage, not a threshold or feed problem.
- Scanner gap: **no parameter change.** The fix is scheduler reliability (routed below).

### Baseline Tracking

Source: the October 1 log's baseline (Days tracked 93). **October 2 is a new baseline gap**: its log has position evaluations only, and the morning evaluation due October 5 never ran. It is not back-filled.

- Days tracked: **94** (93 + October 5 only).
- Winners detected by scanner: **72/82 (87.8%)**, unchanged. OLOX is excluded from the denominator because the scanner had no entry-window coverage (Sep 22 precedent).
- Winner selected for paper trade: **36/79 (45.6%)**, unchanged. No selection opportunity existed.
- Baseline gaps: **Sep 11, Sep 18, Sep 25, Oct 2.** The Oct 2 gap hides a large mover. `log/pm-open-scan.csv` records **SAIQ +623.2%** in the October 5 PM with an October 2 AH footprint (SIP AH high $3.24, +75.1%, on 7.01M shares). It was never diagnosed here. Oct 2 also had 0/7 scans, so it could not have been a detection miss.
- Target: >80% detection. Status: **BASELINE MET** on the recorded sample. Coverage failures and skipped retrospectives limit what the rate means.

### Retrospective Scan Results

`scan.py --all --session premarket` (06:45 ET): OLOX, SDEV, QTEX, RUBI, AIIO, WHLR, JAGX, LHSW. The unfiltered sweep added FRGT and AXG (sub-$0.50). The regular-session sweep added MI, SAIQ, VEEA, PDSB, BEAT, APUS, SGLY, SCKT, AIFA, RETO, PMI, and CTNT. All were checked on SIP AH bars and stayed under +10% AH or were thin. A forced `scan.py --all --session afterhours` at 06:49 ET returned **0 hits** (postmarket fields reset overnight). It is a secondary diagnostic only.

| Ticker | Oct 5 SIP close | AH SIP high / ET | PM SIP high / ET | PM high vs close | Peak-bar shares / trades | Latest (06:30 bar) | Classification |
|--------|-----------------|------------------|------------------|------------------|--------------------------|--------------------|----------------|
| OLOX | $0.88 | $1.66 / 18:20 | $2.245 / 04:00 | **+155.1%** | 5,654,390 / 40,877 | $1.68 (+90.9%) | AH→PM continuation; **winner** |
| FRGT | $0.245 | $0.2499 / 19:25 (AH total 95,753 / 183) | $1.32 / 04:05 | +438.8% | 7,642,162 / 45,619 | $0.5231 (+113.5%) | PM-only; below $0.50 floor; biggest raw mover |
| RUBI | $0.70 adj. ($1.05 raw) | $1.05 flat (AH total 2,230 / 11) | $1.4199 / 05:50 | +102.8% adj. | 185,585 / 884 (05:55 bar 2.47M / 15,170) | $1.09 (+55.7%) | PM-only; 1.5-for-1 stock dividend ex-date Oct 6; uninvestable |
| WHLR | $1.09 | $2.2307 / 16:05 | $2.1496 / 04:00 | +97.2% | 1,459,669 / 10,493 | $1.4596 (+33.9%) | First-bar spike; Day −47.3%; AH better |
| SDEV | $3.94 | $3.94 / 16:00, AH close $3.13 | $5.57 / 04:45 | +41.4% | 2,182,888 / 17,226 | $4.32 (+9.6%) | PM-only rebound after Day −47.3% |
| JAGX | $4.73 | $6.69 / 17:40 | $6.64 / 06:10 | +40.4% | 523,782 / 7,889 | $5.76 (+21.8%) | Late AH build; AH slightly better |
| AIIO | $1.11 | $1.14 / 16:00 (AH total 29,976) | $1.45 / 06:15 | +30.6% | 2,656,797 / 13,445 | $1.21 (+9.0%) | PM-only |
| QTEX | $1.54 | $2.18 / 19:05 | $1.90 / 05:30 | +23.4% | 1,203,387 / 4,306 | $1.7983 (+16.8%) | Late AH build, day 3 of run; AH better |
| AXG | $0.105 | $0.1296 / 16:45 | $0.1649 / 04:10 | +57.0% | 21,373,344 / 24,831 | $0.1201 (+14.4%) | Below floor; in-window AH; one-bar PM wick |
| LHSW | $0.547 | $0.6859 / 17:40 | TV PM ~$0.57 | ~+4% | AH 519,502 / 1,704 | ~+4% | Intra-bar AH spike; no checkpoint above +10% |

**Basis checks:** every percentage uses the SIP October 5 close. RUBI's raw $1.05 close is divided by 1.5 for the stock dividend ($0.70), the same basis TradingView and the pm-open row use. Measured from raw $1.05, RUBI's peak is only +35.2%. `price-timeline.py` uses October 2's $0.8415 as OLOX's previous close, which gives "+166.8%"; the correct PM-gap basis is $0.88. WHLR's $1.09 official close is the day's low print. The pm-open row records late regular trades near $1.40–$1.68, so WHLR's gaps from $1.09 overstate the move from where it actually traded. MI (Day +683%) peaked at only +6.4% AH at 16:00 and fell to $4.45 (−36%). SAIQ (+3.0%) and VEEA (+7.5%) stayed under +10% AH. APUS's +16.1% at 19:50 ET was a thin tail tick (30,513 shares / 248 trades).

### Open Position P&L (Alpaca)

**No executed positions.** `positions --json` returned `[]`, and no order has been created since October 2. **Total Realized P&L (Alpaca fills only): $0.00.** Every return in this section is hypothetical.

### Scanner Effectiveness

- Evening scans ran: **0 of 7** (21:30–00:30 CEST). The log directory did not exist before this evaluation, which the coverage rule counts as "unknown". Git history settles it: zero `post-market scan` commits after the October 1 session. The whole entry window was uncovered.
- Candidates found: **0.** Retrospective matches: **n/a**.
- Supplementary AH-change-only pass: **measurement incomplete**, because no scan logs exist. This is not a zero.
- SIP reconstruction of what full coverage would have seen (>10% AH at scheduled checkpoints): **OLOX 5** (22:30–00:30), **WHLR 5** (+16.5% to +22.0%), **JAGX 3** (23:30, 00:00, 00:30), **QTEX 3** (23:30, 00:00, 00:30). LHSW and APUS had none.

### Missed Opportunities

The whole night was a coverage loss. These are hypothetical outcomes if the scans had run; none counts against the detection baseline.

| Ticker | AH change at checkpoints | Why missed / what would have blocked it | Would it have been profitable? |
|--------|--------------------------|-----------------------------------------|--------------------------------|
| OLOX | +37.5% → +55.7% → +54.5% → +51.1% → +76.1% | 0/7 scans. Would have qualified at 23:00 CEST: $1.37, Total +62.8%, BUILD, fresh book at 16:59:59 ET | **Yes**: $1.37 → $2.245 **+63.9%**; ~$1.90 plateau **+38.7%**; latest **+22.6%** |
| JAGX | −0.6% → +0.4% → +12.5% → +34.2% → +24.9% | 0/7 scans. Would have qualified at 00:00 CEST: $6.35, Total +73.5%. Alpaca book frozen at 16:00 ET (bid $4.05 / ask $5.43) | Marginal: $6.35 → $6.64 **+4.6%**; latest **−9.3%** |
| QTEX | +0.6% → +1.8% → +16.1% → +13.0% → +24.7% | 0/7 scans. Would have qualified at 00:00 CEST: $1.74, Total +58.2%. Day-3 multi-session runner; Alpaca book frozen at 16:59:55 ET | Marginal: $1.74 → $1.90 **+9.2%**; latest **+3.4%** |
| WHLR | +22.0% → +18.3% → +20.2% → +16.5% → +16.5% | Would have been blocked: Day −47.3% (dead-cat) and a first-bar AH high ($2.2307 at 16:05) | First sighting $1.33 → $2.1496 **+61.6%** raw, transient: 04:05 close $1.755, latest $1.46 |

### AH Mover Follow-Through

No evening scans exist, so this table covers names that the SIP reconstruction puts above +10% AH at two or more scheduled checkpoints. Current = SIP close of the 06:30 ET bar (historical, not an executable quote).

| Ticker | AH Peak | Peak Time | AH Trajectory | Current PM | From AH Peak | From Close | Verdict |
|--------|---------|-----------|---------------|------------|--------------|------------|---------|
| OLOX | $1.66 | 18:20 | **Build** (+37.5 → 55.7 → 54.5 → 51.1 → 76.1%) | $1.68 | +1.2% | +90.9% | PM peak $2.245 **exceeded AH by 35.2%**; real continuation |
| WHLR | $2.2307 | 16:05 | **Spike→hold** (first-bar spike to +104.7%, then +16–22%) | $1.4596 | −34.6% | +33.9% | PM peak $2.1496 **fell short (−3.6%)**; AH better |
| JAGX | $6.69 | 17:40 | **Late surge** (−0.6 → 0.4 → 12.5 → 34.2 → 24.9%) | $5.76 | −13.9% | +21.8% | PM peak $6.64 **fell short (−0.7%)**; AH slightly better |
| QTEX | $2.18 | 19:05 | **Late surge**; peak after the last scan (+0.6 → 1.8 → 16.1 → 13.0 → 24.7%) | $1.7983 | −17.5% | +16.8% | PM peak $1.90 **fell short (−12.8%)**; AH better |

### Notes

- **Coverage-failure tally, last 10 completed US sessions (Sep 22–Oct 5):** **Sep 22 2/7, Sep 25 0/7, Sep 29 3/7, Oct 2 0/7** (log has position evaluations only), **Oct 5: no log, and git shows 0 scan commits**. Sep 23, 24, 28, 30, and Oct 1 were 7/7. That is **5 failures in 10 sessions** (4 by log, 1 by commit evidence), worse than the 4/10 reported October 2. Route the scheduler/bridge investigation to the daily email. Nights without entry-window coverage are not charged as detection or selection misses.
- **Outage scope (October 2 evening → October 6):** nothing ran after the October 2 18:21 strategy-advance commit until October 5 10:11 (init6 cohort), then only the 11:04 pm-open scan. October 5 had no position evaluations, no morning evaluation, and no evening scans. October 6 jobs are starting late and overlapping: this pulse and the 10:30 position evaluation both started at 12:44 CEST, and the pm-open scan logged itself as a "late run" at 06:44 ET. That position evaluation recorded `sync-repo.sh` failing with `fatal: Cannot rebase onto multiple branches` and recovered with a manual fetch/ff-only pull. The cost of this outage is one real winner: OLOX at about +39% to +64% hypothetical.
- **CEILING-OVERRIDE / DEAD-CAT-OVERRIDE / FIRST-BAR-SPIKE WATCH outcomes:** none were flagged, because no scan log exists. Informational only: WHLR (float 568K, Grade None, 1-for-9 reverse split Sep 21) shows both a dead-cat and a confirmed first-bar spike. Its $2.2307 16:05 high was never surpassed in the complete 16:00–20:00 SIP bars. The PM peak of $2.1496 fell 3.6% short of it. Its hypothetical +61.6% from first sighting did not hold: the next PM closes were $1.755 and $1.67, and the stock dropped below $1.62 from 04:20. It was never a WATCH, so the counts stay at: first-bar **11 valid (2 ran / 9 faded-flat), 13 flagged, 2 superseded; 3 pre-gate, 0 ran**. The dead-cat named history is unchanged.
- **Sub-3M AH-fader tracker: 4/22, unchanged.** No fade-rule skip could occur without scans. WHLR is a low-float control outside the denominator (dead-cat co-block). AH $2.2307 → PM $2.1496 **fell short**. (a) First sighting $1.33 → peak **+61.6%**; (b) 04:00 ET PM-open VWAP $1.8046 → peak **+19.1%**, after which closes fell to $1.755 and $1.67. No Grade A/B fader.
- **Raw PM leader / PM-only tracking:** the biggest raw PM mover is **FRGT, +438.8%** ($0.245 → $1.32 SIP at 04:05). It is a **PM-only gapper**: AH was flat at $0.2499 max on 95,753 shares / 183 trades. Investability: the 04:00 bar opened at $0.33 and closed $0.9505 (VWAP $0.6004). The $1.32 high was a wick inside the 04:05 bar (VWAP $1.086, close $1.00). Closes then slid: $0.88, $0.84, $0.84, $0.76, $0.74 by 04:30, $0.66 by 05:15, $0.52 by 06:30. The gain over the close stayed above +200% for five bars on 3.3M–8.9M shares and 14K–46K trades, which counts as **holdable under the ≥2-bar rule**. But no close came within 20% of the wick, and an entry after the 04:00 bar lost money. The Alpaca quote has been frozen since 16:00 ET (ask $0.00 x0). No catalyst was found; the Sep 18 AI POD launch is old. FRGT is **absent from `log/pm-open-scan.csv`** because that pulse also uses the $0.50 floor. RUBI (+102.8% adjusted, PM-only) is in the CSV as uninvestable. The CSV holdable PM-only count is **62** (60 on Oct 2). Route the Initiative-6 cluster and the FRGT sub-$0.50 PM-only blind spot to the daily email. A PM-only gapper is not a scanner failure.
- **Late-AH-tail tracking:** nothing new. OLOX's defining surge came at 16:00 ET, inside the window. QTEX's $2.18 high at 19:05 came after the last scan, but QTEX was already above +10% at three checkpoints. APUS's 19:50 tick was thin. Standing: **2 true-tail (ORIS, GNS) / 1 feed-lag (BTCT)**.
- **In-window feed-lag standing: 7, unchanged.** It cannot be measured on a night with no scans. Carry the reached independent whole-universe AH verification recommendation to the email.
- **Price-floor exclusions: 9 → 10 observations across 6 → 7 nights; 0 confirmed >100%-and-holdable, 1 inherited pending.** New row **AXG Oct 5→6**: close $0.105, `tradable=true`, float 66.1M. In-window AH: the 16:45 bar closed $0.1288 (**+22.7%**, high $0.1296) on **1,001,920 shares / 893 trades**. The next bar (2.25M / 1,814) reversed to $0.113, and AXG was ~$0.112 (+6.5%) at 18:30 ET. PM high $0.1649 (**+57.0%**) at 04:10 on 21.4M / 24,831, next close $0.1199. Hypothetical 16:45 VWAP $0.1240 → peak **+33.0%**. The Alpaca book at 16:00 ET was bid $0.10 / ask $0.13, a spread of **23% of ask**. Verdict: **uninvestable** (wide spread, one-bar wick, under 100%). The floor would have excluded it even if scans had run. FRGT does not count here because it had no in-window AH signal. The floor-change trigger is still unmet.
- **Execution and selection trackers, unchanged (nothing testable without scans):** broker-block **2** (SHPH); stale-book-only **6** (4 profitable / 2 negative controls); no-fillable-book **4**; float-only **1**; final-scan-only **2**. Alpaca quotes for OLOX, QTEX, JAGX, FRGT, RUBI, and WHLR are all frozen at October 5 16:00–17:00 ET, so the frozen-quote feed limitation persists.
- **Actual-entry trackers, unchanged:** no fills. Multi-session runners **1 entry, faded**; first-day igniters **27 entries (9 ran / 8 flat / 10 faded), 33.3% ran**. Fill-chase **1, never reclaimed**. Reverse-split recency **4/5 this-week faded / 4/6 older continued**. RUBI's 1.5-for-1 is a forward stock dividend, not a reverse split.
- **Extreme-runner tally: 15 fades / 2 continues (88.2%), unchanged.** OLOX's total extension at its AH peak was +97.3% (from the Oct 2 close of $0.8415), below the ~+130% zone, so it is not added. For the record, its PM went on to +166.8% total, a continuation. WHLR's total extension is negative against Oct 2. The partial-profit routing trigger stays reached.
- **SIP basis checks (Oct 2 → Oct 5 closes):** OLOX $0.8415 → $0.88; WHLR $2.07 → $1.09; JAGX $3.66 → $4.73; QTEX $1.10 → $1.54; SDEV $7.48 → $3.94; AIIO $1.19 → $1.11; FRGT $0.2522 → $0.245; AXG → $0.105; RUBI $1.08 → $1.05 raw ($0.70 adjusted). Entry Total% uses Oct 2; PM gaps use Oct 5. Hypothetical entries: OLOX $1.37 (+62.8%), JAGX $6.35 (+73.5%), QTEX $1.74 (+58.2%).

### Daily Email Routing

- Headline: **OLOX is a real winner (+155.1% SIP PM peak on 5.65M shares / 40,877 trades) that we missed only because 0/7 evening scans ran.** It would have qualified at 23:00 CEST near $1.37 for +63.9% to the peak (~+38.7% to the liquid plateau). No fills; detection 72/82 and selection 36/79 unchanged; 94 days tracked.
- **Scheduler/bridge outage (decision for Juan):** 5 coverage failures in the last 10 sessions (Sep 22 2/7, Sep 25 0/7, Sep 29 3/7, Oct 2 0/7, Oct 5 0/7 by commits). Nothing ran from October 2 evening to October 5 morning except two morning jobs. October 6 pulses are starting more than 2 hours late and overlapping, and one hit a `sync-repo.sh` rebase failure. This needs an infrastructure investigation; no threshold change compensates for missed jobs.
- **New baseline gap Oct 2** (joins Sep 11, 18, 25). The skipped Oct 2 retrospective hides SAIQ's +623% Oct 5 PM gap, which had a +75% Oct 2 AH footprint.
- Carry forward: 7 feed-lag observations → whole-universe AH verification; frozen extended-hours quotes; the 62-row holdable PM-only cluster → Initiative 6, plus FRGT (+438.8% PM-only, sub-$0.50, missing from both scanners); 15/17 extreme-runner fades → partial-profit decision; reverse-split recency recommendation. The price-floor (10 observations, 0 holdable >100%) and sub-3M fade (4/22) triggers stay unmet.

### Price Charts

Excerpts from `python3 scripts/price-timeline.py OLOX JAGX WHLR` at ~06:52 ET. The tool's previous close is **October 2's**, not October 5's, so its percentages are total two-day moves. The SIP tables above set the levels; these charts show shape only. The WHLR chart's left edge is October 5's own premarket ($2.60), before the regular-session crash.

```text
========================================================================
 OLOX - 2-Day Price Timeline (5-min intervals)
========================================================================

Previous Close: $0.84
2-Day Range: $0.80 - $2.25
Current: $1.67 (+97.9% from prev close)
Peak: $2.25 (+166.8%) at 10-06 04:00 ET

Chart (oldest → newest):
$   2.00 │                                                           █
         │
         │                                                          █
         │
         │                                                █ ██     █
         │                                              █  █  █████
         │                                      █████    █
         │                                   ██      ███
         │                                     █
         │
         │                                  █
$   0.80 │██████████████████████████████████
         └────────────────────────────────────────────────────────────

========================================================================
 JAGX - 2-Day Price Timeline (5-min intervals)
========================================================================

Previous Close: $3.66
2-Day Range: $4.03 - $6.69
Current: $5.84 (+59.5% from prev close)
Peak: $6.69 (+82.8%) at 10-05 17:40 ET

Chart (oldest → newest):
$   6.58 │
         │                                                       █
         │                                                          █
         │                                                      █    █
         │                                                        ██
         │                        █                            █
         │                          █
         │                         █ ██
         │                             ███████████  ███████  ██
         │ █                                      ██       ██
         │█ ████ ██    ███  █
$   4.03 │      █  ████   ██ █████
         └────────────────────────────────────────────────────────────

========================================================================
 WHLR - 2-Day Price Timeline (5-min intervals)
========================================================================

Previous Close: $2.07
2-Day Range: $1.22 - $2.60
Current: $1.41 (-31.9% from prev close)
Peak: $2.60 (+25.6%) at 10-05 04:00 ET

Chart (oldest → newest):
$   2.30 │  █
         │█  █
         │ █  █          █   █
         │     ██████████ ███ ██
         │
         │                       ████   ██
         │                      █    ███  ███
         │                                   ███ █    █
         │                                      █ ████ █ █
         │
         │                                              █ ██     █  █
$   1.22 │                                                  █████ ██ █
         └────────────────────────────────────────────────────────────
```

**Multi-day tracking:** OLOX was added to Active Watch in `WINNERS_TRACKING.md`. There were no prior Active Watch rows to refresh or move to Historical.
