# Strategy Roadmap

Bigger changes to the trading system. Each idea gets researched, piloted in a
low-risk way (instrument / paper / shadow), and only promoted to the live cycle
once it has earned evidence. This file is the single source of truth for what we
are working on, what is parked, and what needs Juan.

**DEADLINE (2026-09-01, Juan directive):** the paper account has ~1 month to go
**net positive** (target ~2026-10-01; equity was $99,850.80, -$149.20 at the
08-31 cycle). If it is not positive by then, **pivot**: create new
projects/initiatives to change the strategy and research existing
agent-focused trading strategies online. Until then, keep **all** current
initiatives running and moving fast. Reinforces the parallelism steer below and
the North Star. See `FEEDBACK_LOG.md` 2026-09-01.

**Parallelism (2026-07-08, Juan's steer "move faster"):** only the **pilot**
stage is serialized (one live experiment at a time, so P&L stays attributable).
Research, instrument (log-only), and build/delivery work carry no attribution
conflict and near-zero risk, so they run **in parallel** and should not queue
behind the active pilot. Each `strategy-advance` run advances the top pilot step
**plus** clears ready low-risk build/research items (cap ~1-2 extra per run so
runs stay focused and never break the daily cycle).

**Update (2026-09-17, Juan feedback):** The YFOR audit found no raw extended-hours volume-source mismatch: entry validation uses Alpaca SIP bars, while `chart.py` uses Yahoo OHLC plus Alpaca SIP volume backfill. The mismatch was metric scope. YFOR's 17:20 ET entry bar had 941,842 shares / 4,509 trades and a 4.2x local ratio, but its prior AH session printed larger 1.37M-1.79M-share bars; the entry path did not enforce the requested 10x-plus local-spike and cross-session comparison. Route this to Initiative 1 / `scanner-improvement` to define one volume metric for both decisions and charts, classify repeat tickers as multi-session runners, and reject sub-10x local spikes. No live entry rule changed in this capture pulse. To accelerate initiative work, the external scheduler now runs `strategy-advance` at 15:00 and 18:00 Europe/Berlin on weekdays; trading scans and position-evaluation pulses are unchanged.

These are strategy-level changes and live **outside** the daily
scanner-improvement loop (which is restricted to surgical scanner/process
tweaks). The scanner-improvement task may reference this file but must not
change strategy on its own.

## North Star (the objective everything serves)

**Make the most money, fast.** The single objective is maximizing the
account-growth rate, paper now and real later. Everything else, detection rate,
the >80% baseline, win rate, clean process, is a **proxy**, valuable only while
it converts into faster account growth. When a proxy stops serving the
objective, change or drop it.

Implications that drive decisions:

- **The core strategy is a hypothesis, not a constant.** AH->PM momentum is the
  current best guess. If another setup compounds faster (PM-only gappers, the
  +300-600% runners in Initiative 6, earlier volume-lead entries in
  Initiative 1, a different universe entirely), pivot toward it. Nothing is
  sacred except the objective.
- **Prioritise by expected dollars per unit time.** Rank work by
  edge size x frequency x scalability, discounted by effort and uncertainty.
  The highest expected $/time lever wins the day. A clean process that earns
  little loses to a messy process that earns a lot.
- **Don't go broke; that is the slowest path.** "Fast" still means surviving to
  compound. While in paper/learning, "fast" = find the highest-expectancy
  repeatable edge and prove it cheaply, then scale size and concentration once
  proven. Avoid ruin, not volatility.
- **Proof before scale.** Bigger size and concentration are how money is made
  fast, but only on an edge that has shown itself. Validate cheaply (shadow /
  paper / instrument), then push size.
- **Strategy pivots that touch `Day Trading.md` or live trading are proposed to
  Juan**, not applied unilaterally, but they are always in scope to raise.

The `strategy-advance` pulse uses this section as its prioritisation lens.

## Priority order (current)

Ranked by the North Star (expected $/time). **Re-ranked 2026-07-15** after Init 6's
two tested levers (problem a: PM-only-gapper long; problem b: trailing-stop hold)
both came back negative and Init 1's volume-lead hypothesis was falsified — the
AH->PM core strategy stands, and the surviving lever is **when/how fast we detect
the ignition**, not a new signal.

1. ~~**Initiative 2 - Alpaca paper trading.**~~ **Promoted to the live paper
   cycle (2026-06-25).** Real Alpaca paper fills now drive entries/exits via
   `broker.js`. Only step 5 (flip to live real money, tiny size) remains, gated
   on a proven edge + Juan. **No pilot active.**
   **Update 2026-08-07 (Juan directive "research the alpaca problem"):** root
   cause of the recurring AH no-fill found and confirmed empirically — the paper
   account is on the **free IEX-only data plan**, and Alpaca simulates paper
   fills against the subscribed feed. IEX goes one-sided/stale at the 16:00 ET
   close (`ap=0`) for micro-float names, so there is no AH ask to cross and buy
   limits never fill; the real AH volume prints on other venues and only shows
   on SIP (which we pull for bars, hence "real SIP volume, no fill"). Feed
   mismatch, not a `broker.js` bug. Fix options: (1) pay for Alpaca SIP (~$99/mo),
   (2) switch to IBKR paper, (3) score on modeled SIP fills (free). Full writeup:
   `INIT2_ALPACA_FILL_ROOTCAUSE.md`. **Needs Juan's call on which path.**
   **Update 2026-09-04 (Juan directive, re: 09-03 email "research alternative
   providers besides alpaca; test them and find one that actually works for
   trading these stocks"):** Juan picks the **switch-broker** path (option 2/
   alternatives) over paying for Alpaca SIP or modeled fills. This is now an
   **active research directive**: research brokers with real AH/PM micro-float
   coverage (IBKR paper first, then Trading 212 / Webull / Moomoo / others),
   test each on the exact chronic-block names (AKAN, SHPH, GIPR-class
   sub-$1 micro-floats) to see which actually fills extended-hours limits, and
   report the best fit. Research/test is non-serialized low-risk work, so
   `strategy-advance` starts it in parallel with the active Init 6 pilot. No
   live broker switch applied yet — evaluate and propose when Juan provides an
   account. **Update 2026-09-22 (Juan feedback):** the IBKR/broker-switch fill
   test remains blocked for now; defer this work and move on to other
   initiatives until Juan supplies access. See `FEEDBACK_LOG.md` 2026-09-22.
   **Update 2026-09-25 (Juan feedback, INLF):** Juan calls INLF's rising
   price and exceptional volume the setup to enter. The Sep 24 scanner found
   it in four eligible-window scans, but the first entry-eligible ~$4.21
   observation had a 16:00 ET frozen Alpaca quote, so no current ask or fill
   could be verified. Its $5.73 SIP PM peak implies +36.1% theoretical from
   that observation; its $5.95 AH peak more than doubled the $2.95 true close,
   while the PM peak did not. This is the **fifth stale-book execution block**
   (NUWE, KUST, CLRO, XRTX, INLF), with no realized gain. Keep the live-book
   check; route a current-book verification diagnostic for strong volume-backed
   candidates to `scanner-improvement`. The IBKR paper-fill test stays deferred
   until Juan provides access. See `FEEDBACK_LOG.md` 2026-09-25.
   **Update 2026-09-04→09-07 (strategy-advance) — shortlist done, best fit
   identified, blocked on an account.** Researched all four candidates from
   primary sources and wrote `INIT2_BROKER_ALTERNATIVES.md`. Results:
   **Trading 212 REJECTED** (API supports extended-hours *market* orders only,
   no limit orders — our micro-cap AH strategy is limit-only). **Moomoo/Futu**
   possible but EU-access doubtful (no EU retail entity; ETH paper needs a
   US-margin account + OpenD gateway). **Webull OpenAPI = BACKUP** — EU
   developer portal confirmed (`developer.webull.eu`), official Python SDK,
   Jul-2026 API paper trading, native extended-hours; unconfirmed whether the EU
   entity's paper API exposes US micro-cap AH symbols. **IBKR paper =
   RECOMMENDED PRIMARY** — EU-regulated + the eventual live path, and its paper
   fill engine simulates against the *real consolidated market data you
   subscribe to* (shareable with paper), so a non-IEX-only US-equities data
   subscription lets AH micro-float limits fill exactly where Alpaca's free IEX
   feed cannot — the direct root-cause fix. The decisive fill test needs an
   account, so it is **blocked on Juan** (open an IBKR paper account + enable a
   US extended-hours consolidated data subscription + API access; or register at
   developer.webull.eu and share App Key/Secret). Test protocol on AKAN/SHPH/
   GIPR is written. No live broker switch until the fill test passes + Juan
   signs off.
2. **Initiative 3 - adaptive scheduling / faster ignition detection.** Promoted
   to the top research lever (2026-07-15). Init 1's 1-min backtest shows winners
   ignite in a single minute (IVF 16:53 ET) that our ~22:15 CET / 16:15 ET AH
   scan runs *before*, so we see the name flat and catch it late once it's
   already +50-100%. The edge is monitoring frequency / scan timing (catch the
   volume+price co-spike fast), which is exactly this initiative. Next: audit
   which scans fire before vs after the typical ignition window; propose a
   retimed/added AH observation scan (schedule changes -> propose to Juan).
   **Update 2026-08-06 (third live CONFIRM-3 set, 08-05 AH -> 08-06 PM):** the
   log-only third-bar gate's separation **broke down** out-of-sample. One `YES`
   was a monster (CLRO +147.7% to next-PM high) but Alpaca had no fillable AH
   ask; the other `YES` (RECT) died; and both `NO` names (PAVS +83.1%, CELZ
   +53.9%) had the day's largest PM excursions — the gate would have rejected
   them. Combined live `YES` n=7 mean +25.1% is CLRO-outlier-driven (median
   +0.9%); `NO` n=7 now holds two >50% runs. Emerging read: the selection-gate
   hypothesis is weakening while **execution (unfillable AH books, early exits
   before the PM spike) is the larger money-fast lever** — CLRO/INLF/BANL/ZJYL
   edges were unfillable or broker-blocked, and CELZ/PAVS ran only after our
   10:30 CET exit. Keep the column log-only; next runs pivot toward measuring
   the fill/exit-timing gap rather than adding scan cadence.
   **Update 2026-08-07 (execution-gap tally):** built `scripts/execution-gap.js`
   over 10 CONFIRM-3 YES/held rows (4 live sessions). **340.4% of detected PM
   upside was lost, none of it to selection.** Two buckets dominate: **fill gap
   203.4%** (CLRO +147.7, BJDX +43.5, INLF +12.2 — real winners with no fillable
   Alpaca AH ask; Initiative 2, awaiting Juan) and **exit-timing gap 137.0%**
   (CELZ +53.9, PAVS +83.1 — held names whose PM spikes fired at ~06:55/08:00 ET,
   *after* our 10:30 CET / 04:30 ET exit but still inside premarket). The
   exit-timing slice is self-inflicted and fixable in our own process. Init 3's
   original selection-gate hypothesis is confirmed **not** the money-fast lever;
   the lever is execution. Next: instrument the intra-premarket exit path
   (log-only) to size the exit-timing gap out-of-sample before proposing any
   exit-pulse retiming (a trading-pulse change -> Juan). **Flag for Juan:** the
   10:30 CET single exit pulse looks too early for multi-day holds.
   **Update 2026-08-14 (Juan feedback, 08-13 cycle):** two fresh live points
   reinforce this initiative and the ignition gate. (1) **ONFO** was entered at
   00:30 (18:30 ET) only after it had already built +44.2% and printed its
   spike — a textbook late/chase entry; Juan: "ONFO entered too late." (2)
   **GRSD** was entered on the 2-AH-scan gate with CONFIRM-3 **NO** and a thin
   3k-sh/44-trade spike bar; Juan: "absolutely a NOGO ... no volume spike."
   Both say the CONFIRM-3 volume-spike ignition should be a **hard entry gate**,
   not a log-only column, and that entry must be near the ignition, not after
   +40%. Routed as a scanner-improvement candidate (see `FEEDBACK_LOG.md`
   2026-08-14).
   **Update 2026-08-18 (Juan feedback, 08-17 XOS cycle):** direct steer — "We
   should have entered much earlier ... If necessary, also exit early. The
   pattern is clear for winners: Gigant volume and rising price." XOS was a clean
   detect but entered at $4.54 near the $4.78 AH top, after the run from $2.40.
   This is entry latency, not detection, and Juan names the winner signature
   (giant-volume + rising-price co-spike = CONFIRM-3). Reinforces two things
   already scoped here: (1) the **cadence densification** (add 16:15 + 16:45 ET
   AH scans, 22:15/22:45 CET) to cut the AH-open-cluster lag ~22m -> ~7m and
   enter nearer ignition — a scheduler change, **propose to Juan**; (2) making
   CONFIRM-3 a **hard entry gate** so we enter on the volume+price co-spike, not
   after +40-100%. The "exit early" half folds into the intra-premarket
   exit-timing gap already flagged above (AH peak, not PM, is the exit for
   extreme runners). Next `strategy-advance` run: draft the scheduler-densify +
   hard-gate proposal for Juan. See `FEEDBACK_LOG.md` 2026-08-18.
   **Update 2026-08-20 (Juan feedback, 08-19 BTCT cycle):** "BTCT you should
   have entered MUCH earlier." BTCT was the winner, detected in all 7 scans, but
   skipped on the flat +150% extension ceiling (ceiling-skip entry $1.23 -> PM
   peak $2.07 = +68.3%). Third straight cycle (ONFO 08-14, XOS 08-18, BTCT 08-20)
   where Juan flags late/missed entry on a detected winner — the money-fast lever
   stays **entry timing + the ceiling gate**, not detection. BTCT is the
   strongest case yet for the **volume-conditional +150% ceiling override** on
   accumulating-volume BUILDs (already tracked log-only by the scanner pulse this
   cycle): a flat ceiling skipped a real build-and-hold runner. Folds into the
   same proposal-to-Juan: cadence densify + hard CONFIRM-3 entry gate + the
   volume-conditional ceiling override. Separately, Juan rejected the two junk
   entries this cycle (BTOG Grade-D reverse split -39%, LOOP Grade-None
   no-catalyst -18%) — routed as a **selection-quality** scanner-improvement
   candidate (hard skip for reverse-split / no-catalyst Grade-None BUILDs),
   which also questions the enter-everything tail of the multiple-positions
   policy. See `FEEDBACK_LOG.md` 2026-08-20.
   **APPROVED 2026-08-21 (Juan "Go ahead", re: 08-20 email):** three standing
   items greenlit. (1) **AH data-source cross-check** — feed-lag miss trigger
   reached 4 cases; add an independent whole-universe gainers cross-check at the
   final AH scan so TradingView dropping live movers stops blinding us
   (scanner-improvement to wire, log-first). (3) **Reverse-split conviction
   downgrade** — this-week reverse splits with no fresh catalyst are 4/4 faded;
   downgrade entry conviction / hard-skip that pattern, folding into the 08-20
   selection-gate work. See `FEEDBACK_LOG.md` 2026-08-21.
   **Update 2026-08-27 (Juan feedback, 08-26 cycle):** "DAIC is not how we want
   to enter, there's no AH volume spike." DAIC was entered on the 2-AH-scan gate
   with the scanner logging CONFIRM-3 **YES** (AH-open bar 362k sh / 2611 trades,
   +17%) and then faded -4.6%. Juan does **not** count that bar as a real
   volume-spike ignition — it is a no-catalyst low-float squeeze already run
   sub-$0.50 -> $6+ over prior days, not the "gigant volume + rising price"
   signature. So the current CONFIRM-3 threshold admitted a name Juan rejects as
   sub-spike. Fifth repeat of the hard-CONFIRM-3-gate point (ONFO/GRSD 08-14,
   XOS 08-18, BTCT 08-20). New sub-point for the proposal to Juan: the gate must
   not only be **hard** but also **tighten what magnitude counts as an
   ignition**, since CONFIRM-3 YES fired on DAIC's thin AH-open bar. Routed to
   `scanner-improvement` to re-check the CONFIRM-3 spike-size threshold. See
   `FEEDBACK_LOG.md` 2026-08-27.
   **Update 2026-09-09 (Juan feedback, 09-08 cycle):** "SUNE is not a good entry
   because price only went up in the first 5m bar. all subsequent bars are
   stable ... How about we monitor every 5m in the beginning of PM so that we
   can enter stocks that have increasing price for the first 2 or 3 5m bars."
   Third live restatement of the 2-3-bar rule (AEMD 08-28, AMIX 07-29), now as a
   **build-confirmation gate**: require increasing price across the first 2-3 5m
   bars (a held build, not a one-bar pop like SUNE) and poll every 5m early so
   the build is caught live. Converges with Init 6's continuation gate (R+1/R+2
   must hold 80% of the ignition) — both encode "2-3 bars must hold, not one
   wick." Reinforces the cadence-densify + hard-CONFIRM-gate proposal already
   staged for Juan; the volume half of the same ask is routed to Init 1 (define
   the per-bar volume metric). See `FEEDBACK_LOG.md` 2026-09-09.
   **Update 2026-09-16 (Juan feedback, re: 09-15 cycle):** Juan explicitly
   directs the opening after-hours schedule to run every 5 minutes: "change the
   schedules for every 5m in the beginning of after hours" to avoid missing
   early igniters. This converts Init 3's prior 15-minute opening-hour proposal
   into an approved scheduler requirement. The scheduler is managed outside
   this repository; no schedule file is changed by the feedback-capture pulse.
   Route the external scheduler update to the next scheduler/strategy-advance
   run, then measure first-2/3-bar capture and ignition-to-scan lag.
   **Update 2026-09-22 (Juan feedback, TOPS cycle):** the first qualifying scan
   saw TOPS near $0.96, but the fill came at $1.40 and captured only +0.7% to
   the PM peak. This is another late-entry datapoint; keep the approved 5-minute
   opening cadence and earlier volume-and-price confirmation work as the route.
   See `FEEDBACK_LOG.md` 2026-09-22.
3. **Initiative 5 - better data + review surface (graphs, sources).** AH/PM
   volume backfill shipped (2026-07-14). Ready low-risk follow-ups: the post-push
   raw-URL 200-check (fixes the Gmail render race) and GitHub Pages HTML reports
   (richer review surface). Juan-facing; clear as parallel low-risk items.
4. **Initiative 6 - catch the extreme runners (+300-600%).** **RE-OPENED
   2026-07-23 on Juan's directive** (re: SXTC +223% PM-only gapper): "make
   changes so we can catch the winner of today ... don't ask for approvals."
   The accumulating gapper data now changes the picture the 07-15 close relied
   on: refreshed `pm-gapper-sim.js` (n=7, adds SLGB/INLF) shows **early entry
   at 04:10 ET loses only -2.5% vs -12.5% at the 05:00 ET pulse time** (RegHigh
   best-case +15%). The surviving lever is timing — detect/enter near the 04:00
   ET ignition (folds into Init 3) — plus a **continuation-confirmation** gate
   (2+ holding bars) to skip SXTC-type opening wicks. **Gate built (2026-07-23) +
   mechanical-exit sim run (2026-07-24, `pm-gapper-exit-sim.js`) — problem (a)
   NEGATIVE at 5-min cadence:** the gate rejects most wicks but no causal exit
   (trailing / N-bar / first-lower-high) turns the admitted set positive after the
   ~1-3% spread (near-breakeven mean, negative median, 1-3/7 wins). The +31%
   PMHigh ceiling is an INLF-driven outlier (median +11%) that prints *intrabar*,
   uncapturable by a 5-min close-based exit. **No live PM-gapper scalp pulse
   proposed.** Only untested angle is a 1-min exit (peak is intrabar), deferred
   until the admitted sample grows to >= ~12 so it doesn't hinge on one INLF.
   Detection is already solved (live PM scan + pm-open-scan caught SXTC at PM
   open); problem (a) stays log-only accumulation. **Refresh 2026-07-27:** the
   holdable PM-only tally reached 11 and the gate-admitted set grew to n=8 (adds
   EHGO 07-23, a clean holdable that HELD +59% to PM-last, and BIYA 07-27 +16%).
   Re-ran `pm-gapper-exit-sim.js` — **still NEGATIVE at 5-min** (every exit's
   median negative: trail12 +2.4%/−2.0%, N1 +7.5%/−1.3%; wins INLF-outlier-driven;
   gate still admits the uninvestable WLDS). Admitted 8 < the ~12 threshold, so
   the 1-min exit test stays deferred; keep accumulating.
   **Update 2026-08-17 — deferred 1-min exit test RUN (admitted set reached
   n=12, FRGT 08-13 added) and it is the first POSITIVE Init 6 result.** Built
   `scripts/pm-gapper-exit-sim-1min.js` (log-only): reuses the exact 5-min
   continuation gate to fix entry, then walks 1-MINUTE SIP bars applying
   close-based trailing stops AND resting sell-limits at entry*(1+L%) that fill
   intrabar. **A resting +10% sell-limit (lim10) captures mean +4.0% / median
   +10.0%, positive 9 of 12** — decisively beating every 5-min exit and every
   1-min trailing stop (all negative median), and clearing the ~1-3% spread. It
   fills intrabar 7/12; the only 3 losers are the non-holdable thin/uninvestable
   admits (WLDS -23%, BJDX -9%, EHGO-2 -3%), so on the 7 holdable admits lim10 is
   positive on all (~+9.8% mean). Higher limits (lim30/50) have higher mean but
   lower fill rate and are INLF-outlier-driven; lim10 is the robust choice. The
   5-min sim was negative only because the peak prints intrabar — a 1-min resting
   limit catches it. **This converges with Init 3's independent peak-seeking
   finding (a resting +10% sell-limit was also the winner there, +6.1%/name).**
   Two separate studies now point at the same mechanism. Still log-only, no live
   PM-gapper scalp pulse proposed alone; folds into the Init 3 peak-seeking-exit
   proposal to Juan (resting +10% sell-limit). Next: keep growing the admitted
   set; consider tightening the gate to stop admitting the thin/uninvestable
   names (WLDS/BJDX) that drag the mean.
   **APPROVED 2026-08-21 (Juan "Go ahead", re: 08-20 email) — early-PM
   hypothetical-entry pilot GREENLIT.** The holdable PM-only-gapper cluster
   reached 29 logged; Juan approved running the early-PM hypothetical-entry
   pilot. This becomes the active pilot slot (pilots are serialized — confirm no
   other live experiment is running before it starts). `strategy-advance` owns
   execution: hypothetical entry near the ~04:00-04:21 ET ignition through the
   continuation gate, paired with the lim10 resting-sell-limit exit both studies
   converged on, measured log-only against the baseline before any live orders.
   See `FEEDBACK_LOG.md` 2026-08-21.
   **Update 2026-09-16 (strategy-advance) — fresh holdable PM-only gapper MEDS
   (+68.5%) is GATE-SKIPPED as a VWAP-decline false-negative; entered set holds
   n=21, edge steady +3.7%/name (net ~+1.7%), fade-tail 4/21 (19%). Init 3
   UNBLOCKED — VEEA/WAFU/YFOR exits seeded (n=41), plain +10% limit still best.
   Init 2 blocked on Juan.** One fresh holdable footprint=none PM-only gapper
   logged 09-16 (MEDS +68.5%, DataMEDS AI 1.5M-float squeeze, genuine multi-hour
   liquid exit window). Re-ran `init6-pm-pilot.js` (48 candidates): **MEDS was
   SKIPPED by the continuation gate** — its 04:10 ET ignition (12,689 tr) wicked
   to $2.90/$3.24, but the R+2 bar (04:20) per-bar VWAP $2.83 fell below R+1's
   $2.94×0.98 ($2.88), tripping the **VWAP-non-declining** reject. This is a
   conservative **false-negative**: entered at the R+3 open (~$2.62), the resting
   +10% limit ($2.88) WOULD have filled — the 04:25 bar high hit $2.88, and MEDS
   re-ramped to $4.21 by 06:10 ET. But the same VWAP-dip protection that skipped
   MEDS is what rejects the AEHL-type wick-peak faders, so the skip is by design;
   MEDS joins the wick-rebuild false-negatives (WVVIP/RDIB) as the bounded cost
   of the conservative gate. Entered set unchanged at **n=21: SUM +77.5% / mean
   +3.7% / median +10.0% / positive 16/21**, net of ~2% spread ~+1.7%/name;
   fade-tail 4/21 (BIVI, MIMI-2, BNC, AEHL) = 19%, unchanged. **Init 3 unblocked**
   — VEEA (Grade-A trail-stop win, exit $5.22 from a $7.49 peak = the first live
   Grade-A trail win, +$51.52), WAFU ($1.71) and YFOR ($1.67) all exited at the
   09-16 04:32 ET pulse (first held-name seeds since 09-11). All three are
   dead/fading post-exit books with lim10 unfilled: VEEA peak +2.1% / PM-last
   -1.3%, WAFU faded -9.9% (never traded above exit), YFOR peak +7.8% / PM-last
   +1.8%. Appended all three to `peak-seeking-exit-sim.js` (n=38 -> n=41) and
   `premarket-exit-gap.csv`; re-ran: plain **+10% sell-limit stays the best rule
   at n=41: SUM +91.4% / mean +2.2%, positive 25/41** (down from n=38's
   +100.7/+2.6; WAFU -9.9% the main drag, VEEA a small drag, YFOR a small
   positive; OCO-floor variants remain within noise, consistent with the 09-15
   stop rejection). Init 2 blocked on Juan (needs an account for the fill test).
   Still log-only, no orders. **Deadline note:** equity $99,822.72 (-$177 net,
   ~10-01 target ~2 weeks out); today's live cycle DID earn +$39.36 net via the
   AH->PM core (VEEA trail win), but the account is still net-negative and enters
   none of the PM-only gappers the pilot proves out — the two standing asks stay
   the money-fast bottleneck.
   **Update 2026-09-15 (strategy-advance) — fresh out-of-sample admit MTEN
   FILLED the +10% limit (peak-seek win); entered set n=21 firms to +3.7%/name
   (net ~+1.7%), fade-tail eases to 4/21 (19%). And the 09-14 catastrophe-stop
   hypothesis is REJECTED: a proper intrabar test shows a stop HURTS the edge at
   every width, so the exit proposal stays a plain +10% limit, no stop.** One
   fresh holdable footprint=none PM-only gapper logged 09-15 (MTEN +15.9%,
   Mingteng Intl 6.1M-float micro-cap). Re-ran `init6-pm-pilot.js` (47
   candidates): **MTEN was admitted** by the continuation gate (entered $1.14 at
   04:40 ET) and its early ramp **filled the resting +10% limit ($1.25)**
   intrabar = a win at the exit rule, even though it drifted to PM-last -9.6%
   (the exact peak-seeking case the resting limit is built for). AEHL's 09-14 row
   also recomputed -34.1% -> -32.6% on fuller 1-min bars. Entered set moves
   n=20 -> **n=21: SUM +77.5% / mean +3.7% / median +10.0% / positive 16/21**, vs
   a PM-last floor of -7.3% and a do-nothing baseline of 0%; net of ~2% spread
   **~+1.7%/name (up from +1.3%)**. The **fade-tail eases to 4/21 (BIVI -27.1,
   MIMI-2 -6.9, BNC -14.7, AEHL -32.6) = 19%** — MTEN added a limit-win not a
   fade, so the ratio slips back from 20% and stays under the ~25% that erodes
   the edge below the spread. **Catastrophe-stop RESOLVED:** the 09-14 note staged
   promoting the optional ~-15% catastrophe-stop into the exit proposal if the
   fade-tail held near ~20-25%. Built `scripts/init6-catastrophe-stop.js`
   (log-only) to test it properly with intrabar 1-min bars, and swept widths
   -15/-20/-25/-30% under both conservative and optimistic same-bar tie-breaks.
   **Every width is net-negative vs the plain +10% limit (+1.7%/name):** -15%
   -0.4, -20% +0.9, -25% +0.5, -30% -0.1. Cause: these micro-float PM gappers
   whipsaw deep intrabar then re-ramp, and the resting +10% limit's whole edge is
   staying in all premarket to catch the re-ramp — WBUY (07-23) entered $1.28,
   dumped to ~$0.84 (-34%), then re-ramped to $1.68 filling the +10% limit at
   08:32 ET; any stop bails at the whipsaw low and misses it (verified on real
   SIP bars, tie-break-robust: WBUY/WHLR are genuine time-ordered pre-empts, not
   same-bar artifacts). **Decision: DROP the optional catastrophe-stop; keep the
   exit rule a plain resting +10% sell-limit + PM-last fallback.** Init 3 remains
   **data-blocked** (VEEA held day 1, no exit at the 09-15 pulse), holds at n=38.
   Init 2 blocked on Juan (needs an account for the fill test). Still log-only, no
   orders. Next: keep seeding holdable PM-only gappers; the pilot edge is stable
   (n=21, +3.7%/name, 16/21 positive, tail 19%, two converging studies) and the
   exit rule is now simplified (no stop) — the live blocker stays the broker
   (Init 2 account) plus Juan's veto on the entry pulse. **Deadline note:** the
   ~10-01 net-positive target is ~2 weeks out and the live cycle still enters
   none of these gappers, so the two standing asks remain the money-fast
   bottleneck.
   **Update 2026-09-14 (strategy-advance) — fresh out-of-sample admit AEHL
   (footprint SIP-resolved unknown->none) is a HARD FADE; the gate false-positive
   drops the entered edge to n=20 / +3.3%/name (net ~+1.3%), fade-tail 4/20
   (20%). Init 3 data-blocked (flat book), Init 2 blocked on Juan.** First run
   since Fri 09-11 (Sat/Sun closed). Mon 09-14's PM-open scan logged three
   footprint=`unknown` gappers (Friday evening's AH scan was never captured, so
   the pulse could not classify them). Resolved all three against Friday 09-11
   SIP AH bars: **VSME** (274K sh/1489 tr at ~$1.3) and **CRBP** (thousands of
   trades at ~$10.3) both had real Friday AH sessions -> reclassified
   `ah-detected` (AH-footprint names we merely failed to scan, correctly excluded
   from the PM-only pilot); **AEHL** had ZERO Friday AH prints -> `none`, a
   genuine PM-only gapper (same class as its 08-31 weekend-gap appearance),
   eligible for the pilot. Re-ran `init6-pm-pilot.js` (46 candidates): **AEHL was
   ADMITTED** (entry $9.12 at 04:15 ET) and **faded to PM-last -34.1%** (never
   reached the +10% limit; verified the bleed to ~$6 on real 1-min volume, not a
   stray print). This is a **gate false-positive**: AEHL's 04:00 bar wicked to
   $10.61 then closed $8.69, and its R+1/R+2 closes ($9.20/$9.12) held just above
   80% of the wick high ($8.49), so the wick-high gate admitted it — then it bled
   -34% all premarket. Entered set moves n=19 -> **n=20: SUM +65.9% / mean +3.3% /
   median +10.0% / positive 15/20**, vs a PM-last floor of -7.3% and a do-nothing
   baseline of 0%; net of ~2% spread **~+1.3%/name (down from +3.3%)**. The
   **fade-tail grows to 4/20 (BIVI -27.1, MIMI-2 -6.9, BNC -14.7, AEHL -34.1) =
   20%**, nearing the ~25% that erodes the edge below the spread. **AEHL is the
   strongest evidence yet FOR the (currently optional) ~-15% catastrophe-stop on
   the exit rule**: a -15% stop caps AEHL at -15% instead of -34%, lifting the
   entered mean back to ~+4.3%/name — the fade-tail is the one risk the resting
   +10% limit cannot dodge, and a wide catastrophe-stop is the direct fix. So the
   wick-high gate cuts both ways: it false-negatives rebuilders (WVVIP/RDIB) and
   now false-positives a wick-peak fader (AEHL). Init 3 **data-blocked** (flat
   book since the 09-11 UFG/CULP exits, no held-name exit to seed), holds at
   n=38. Init 2 blocked on Juan (needs an account for the fill test). Still
   log-only, no orders. Next: keep seeding; if the fade-tail holds near/above
   ~20-25%, promote the ~-15% catastrophe-stop from optional into the exit
   proposal before proposing any live PM-gapper pulse. **Deadline note:** with
   the ~10-01 net-positive target ~2.5 weeks out and the live cycle entering none
   of these gappers, the two standing asks remain the money-fast bottleneck, and
   the pilot edge just thinned to ~+1.3%/name net — the catastrophe-stop matters.
   **Update 2026-09-11 (strategy-advance) — no fresh admit (LBGJ + SXTC both
   gate-skipped as wick-peaks); entered set holds n=19, edge steady +5.3%/name,
   fade-tail 3/19 (16%). Init 3 unblocked (UFG-2, CULP seeded, n=38); Init 2
   blocked on Juan.** Fri 09-11 logged three PM-only gappers: AENT +97.8%
   (uninvestable, straight-down spike-fade), LBGJ +29.6% and SXTC +21.9% (both
   footprint=none, in the pilot universe). Re-ran `init6-pm-pilot.js` (45
   candidates): **both LBGJ and SXTC were skipped by the continuation gate** —
   each is a first-bar wick then a flat plateau at gap-mid (LBGJ $3.25 wick ->
   $2.49-2.58 closes ~gap-mid $2.595; SXTC $2.74 wick -> $2.16-2.38 closes
   ~gap-mid $2.335), the weak-hold wick-peak shape the R+1/R+2 80%-of-high hold
   rejects by design (same as TNON/YMAT/GMEX). Entered set stays **n=19: SUM
   +100.0% / mean +5.3% / median +10.0% / positive 15/19**, vs a PM-last floor
   of -5.8% and a do-nothing baseline of 0%; net of ~2% spread ~+3.3%/name.
   Fade-tail 3/19 (BIVI -27.1%, MIMI-2 -6.9%, BNC -14.7%) = 16%, unchanged.
   (EHGO 09-10's PM-last row recomputed -2.9% -> +3.9% on fuller 1-min bars; its
   +10% limit-win was already locked, so SUM unchanged.) **Init 3 unblocked** —
   CULP and UFG (both held since before 09-08) finally exited at the 09-11
   04:30 ET pulse, the first held-name seeds since 09-04. Both are thin dead
   books: UFG exit $0.6055 -> peak $0.616 (+1.7%), lim10 ($0.666) unfilled,
   PM-last $0.57 (-5.7%); CULP exit $3.69 -> peak $3.785 (+2.6%), lim10 ($4.059)
   unfilled, PM-last +2.6%. Appended both to `peak-seeking-exit-sim.js`
   (n=36 -> n=38) and `premarket-exit-gap.csv`; re-ran: plain **+10% sell-limit
   stays the best rule at n=38: SUM +100.7% / mean +2.6%, positive 24/38** (down
   from n=36's +104.0/+2.9; UFG a small drag, CULP a small positive, conclusion
   unchanged). Init 2 remains blocked on Juan (needs an account for the fill
   test). Still log-only, no orders.
   **Update 2026-09-10 (strategy-advance) — fresh out-of-sample admit (EHGO,
   filled the +10% limit) + one gate-skip (TNON wick-peak); entered set grows to
   n=19, edge firms to +5.3%/name, fade-tail 3/19 (16%).** Thu 09-10 logged two
   holdable footprint=none PM-only gappers: EHGO +15.2% (recurring
   registered-direct-offering dilution name, 07-13/07-16/07-23/07-28/09-01) and
   TNON +47.1% (Tenon Medical, 551K-float squeeze). Re-ran `init6-pm-pilot.js`
   (43 candidates). **EHGO was admitted** by the continuation gate (entered $1.03
   at 04:30 ET after the flat 04:00-04:10 open, ignition 04:15) and its early
   ramp **filled the resting +10% limit ($1.13)** intrabar = a win at the exit
   rule, even though it drifted to PM-last -2.9% (exactly the peak-seeking case
   the resting limit is built for). **TNON was skipped** — its $4.22 first-bar
   wick then plateau ~$3.6 (>15% below the wick) is the GMEX/YMAT wick-peak
   shape the R+1/R+2 80%-of-high hold rejects by design. Entered set moves
   n=18 -> **n=19: SUM +100.0% / mean +5.3% / median +10.0% / positive 15/19**,
   vs a PM-last hold-to-open floor of -6.2% and a do-nothing baseline of 0%. Net
   of ~2% spread ~+3.3%/name. The **fade-tail eases to 3/19 (BIVI -27.1%, MIMI-2
   -6.9%, BNC -14.7%) = 16%** — EHGO added a limit-win not a fade, and n grew, so
   the ratio slips from 17% and stays well under the ~25% that would erode the
   edge below the spread. This is the second EHGO admit (07-23 held +59% PM-last)
   — the recurring dilution names keep re-igniting and the gate keeps catching
   the holdable ones. Init 3 **data-blocked** (CULP + UFG still held at the 09-10
   14:30 pulse, no held-name exit to seed; `peak-seeking-exit-sim.js` holds at
   n=36). Init 2 blocked on Juan (account). Still log-only, no orders. **Deadline
   note:** with the ~10-01 net-positive target ~3 weeks out and the live cycle
   entering none of these PM-only gappers, the two standing asks below stay the
   money-fast bottleneck — the pilot edge is stable (n=19, +5.3%/name, tail 16%,
   two converging studies) but going live needs a broker that fills these names
   (Init 2 account) plus Juan's sign-off on the entry pulse.
   **Update 2026-09-09 (strategy-advance) — two fresh out-of-sample names
   (YMAT +72.8%, DPU +45.3%) both gate-skipped as wick-peaks; entered set holds
   n=18, edge +5.0%/name, fade-tail 3/18 (17%). Wick-denominator re-test (08-26
   trigger met) confirms keeping the conservative wick-high gate.** Wed 09-09 PM
   had three holdable PM-only gappers: YMAT +72.8% (footprint=none, 1.6M float),
   DPU +45.3% (footprint=none), FGL +43.2% (ah-detected, outside the pilot's
   footprint=none universe). Re-ran `init6-pm-pilot.js` (41 candidates): **both
   YMAT and DPU were skipped by the continuation gate** — YMAT wicked to $3.28
   then plateaued ~25% below it (GMEX-style wick-peak), DPU had only 3 real bars
   (late 04:35 ramp + SIP blocking the recent ~15 min), so neither can hold R+1/
   R+2 against the wick high. Entered set stays **n=18: SUM +90.0% / mean +5.0% /
   median +10.0% / positive 14/18**, vs a PM-last floor of -6.4% and a do-nothing
   baseline of 0%; net of ~2% spread ~+3.0%/name. Fuller 09-08 data refined BNC
   to PM-last -14.7% (was -15.3%) and ISPC to -2.6% (limit-win locked); fade-tail
   3/18 (BIVI -27.1%, MIMI-2 -6.9%, BNC -14.7%) = 17%. **YMAT/DPU are the 3rd and
   4th wick-then-rebuild holdables the wick-high gate has rejected (after WVVIP
   08-25, RDIB 08-26), meeting the 08-26 trigger to re-test a holdable-gated
   close-denominator.** Re-ran `init6-gate-denom-test.js` (footprint=none, n=61):
   close-denom recovers 4 clean holdable +10% winners (WXM, RDIB, YDDL, DPU) but
   **also admits YMAT as a -23% fade into the holdable set** (its early plateau
   collapsed after 04:45 to PM-last -23%) AND balloons the uninvestable
   false-positive bucket from -16.3%/n7 to -61.7%/n13 (LICN -50%, DXST -15%). So
   the relaxation is still not free: within holdable it lifts SUM (+94.8 -> +111.7)
   but dilutes the mean (+5.9 -> +5.3) and adds a fade to the tail. **Decision:
   keep the conservative wick-high gate** — for the 09-09 pair specifically it was
   net +13% (correctly avoided YMAT -23%, missed DPU +10%), and the wick-high
   rejection of wick-peak fades is exactly the protection the pilot wants before
   going live. Init 3 data-blocked (no held-name exit, `OPEN_POSITIONS.md` flat),
   holds at n=36; Init 2 blocked on Juan (account). Still log-only, no orders.
   Next: keep seeding both sims; revisit the close-denominator only if clean
   wick-rebuild winners (WXM/RDIB/YDDL/DPU-type) start clearly outnumbering
   YMAT-type wick-fades. **Deadline note:** with the ~10-01 net-positive target
   ~3 weeks out and the live cycle entering none of these PM-only gappers, the
   two standing asks below are now the money-fast bottleneck — the Init 6 pilot
   edge is stable (n=18, +5.0%/name, tail 17%, two converging studies) but going
   live needs a broker that actually fills these names (Init 2 account) plus
   Juan's sign-off on the entry pulse.
   **Update 2026-09-08 (strategy-advance) — pilot universe widened to include
   no-AH-session holiday PM-only gappers; two fresh out-of-sample admits (ISPC
   +10% limit-win, BNC -15.3% fade), WETO-2 self-corrected to a limit-win;
   entered set n=18, edge holds +5.0%/name, fade-tail 3/18 (17%). Init 3
   data-blocked.** First run since Fri 09-04 (Mon 09-07 was Labor Day, market
   closed), so Tue 09-08 PM had three holdable PM-only gappers with **no AH
   session at all** (the purest AH-scanner blind spot): BNC +68.2%, GMEX +35.1%,
   ISPC +26.0%. These were tagged footprint=`unknown` (no AH to check), which the
   pilot loader had always excluded, so widened `init6-pm-pilot.js` to also admit
   footprint=`unknown` rows explicitly flagged as a market **holiday** (only the
   3 09-08 rows match; the other 13 `unknown` data-gap rows stay excluded — clean,
   precise). Re-ran: **GMEX skipped** by the continuation gate (wick-peak plateau
   at gap-mid, correct); **BNC admitted** (entered $6.32 at 04:15 ET) and **faded**
   — never reached the resting +10% limit ($6.95), drifted to PM-last -15.3%;
   **ISPC admitted** (entered $1.96 at 04:15 ET) and **filled the +10% limit**
   ($2.16) intrabar = a win. Separately, WETO-2 (09-04) reclassified -1.8% -> +10.0%
   on fuller 1-min bars (its +10% limit $4.35 filled intrabar). Entered set moves
   n=16 -> **n=18: SUM +89.4% / mean +5.0% / median +10.0% / positive 14/18**, vs a
   PM-last hold-to-open floor of -6.4% and a do-nothing baseline of 0%. Net of ~2%
   spread ~+3.0%/name. The **fade-tail is 3/18 (BIVI -27.1%, MIMI-2 -6.9%, BNC
   -15.3%) = 17%** — WETO-2 left the tail (corrected to a win), BNC replaced it, and
   n grew, so the ratio eased from 19% and stays under the ~25% that would erode the
   edge below the spread. **Caveat:** 09-08 rows were computed while premarket was
   still live (~09:00 ET at run time), so BNC's PM-last may shift by the 09:30 cap;
   the ISPC/WETO-2 limit fills are locked. Init 3 is **data-blocked** (no held-name
   exit since 09-04; `OPEN_POSITIONS.md` flat), so the peak-seeking sim holds at
   n=36. Init 2 broker research is blocked on Juan (needs an IBKR/Webull account
   for the fill test). Still log-only, no orders. Next: keep seeding both sims when
   Wed 09-09 data lands; with n=18 / 14 positive / two converging studies / tail at
   17%, the live PM-gapper pulse stays near proposable — hold until n grows and the
   tail stays under ~25%.
   **Update 2026-09-04 (strategy-advance) — pilot admitted a fresh
   out-of-sample name (WETO-2) and it FADED; entered set n=16, edge eases to
   +5.2%/name, fade-tail 3/16 (19%). Init 3 seeded four exits (PLAG limit-win),
   n=36.** One fresh holdable footprint=none PM-only gapper logged 09-04 (WETO
   +23.9%, recurring 864K-float name). Re-ran `init6-pm-pilot.js` (36
   candidates): **WETO-2 was admitted** by the continuation gate (entered $3.95
   at 04:20 ET) and **faded** — never reached the resting +10% limit ($4.35),
   drifted to PM-last -1.8%. Entered set moves n=15 -> **n=16: SUM +83.0% / mean
   +5.2% / median +10.0% / positive 12/16**, vs a PM-last hold-to-open floor of
   -6.5% and a do-nothing baseline of 0%. Net of ~2% spread ~+3.2%/name. The
   **fade-tail grows to 3/16 (BIVI -27.1%, MIMI-2 -6.9%, WETO-2 -1.8%) = 19%** —
   under the ~25% that would erode the edge below the spread, but WETO-2 adds a
   third and the ratio is worth watching (a recurring name that held +3.1% at
   08-31 faded this time). Init 3 had **four fresh seeds** this run: PLAG, GIPR,
   TLYS, CHPT all exited at the 09-04 04:31 ET pulse. **PLAG is a live-book spike**
   (exit $0.8441 -> PM peak $0.94 05:45 ET, **fills the resting +10% limit
   $0.9285**); TLYS/GIPR/CHPT are dead/stalled books (peaks +3.1/+2.3/below-exit,
   lim10 unfilled). Re-ran `peak-seeking-exit-sim.js`: plain **+10% sell-limit
   stays the best rule at n=36: SUM +104.0% / mean +2.9%, positive 23/36** (up
   from n=32's +95.0/+3.0; PLAG adds a +10 win, the three dead books a small
   drag). Still log-only, no orders. Next: keep seeding both sims; watch the
   Init 6 fade-tail ratio (now 19%); with n=16 / 12 positive / two converging
   studies the live PM-gapper pulse stays near proposable, hold until n grows
   and the tail stays under ~25%.
   **Update 2026-09-03 (strategy-advance) — no fresh admit (GYGY gate-skipped),
   VIVK's fade corrected to flat on fuller 1-min bars; entered set holds n=15,
   edge firms to +5.7%/name, fade-tail back to 2/15 (13%).** One fresh holdable
   footprint=none PM-only gapper logged 09-03 (GYGY +19.7%, recurring 17K
   micro-float squeeze). Re-ran `init6-pm-pilot.js` (35 candidates): **GYGY was
   skipped by the continuation gate** — its 04:00 spike faded below gap-mid then
   re-ramped at 04:40 with a thin middle (10-66k sh, 101-498 tr bars 04:05-04:25),
   failing the R+1/R+2 80%-of-high hold on real volume. No new entered row. The
   one change: last run VIVK 09-02 was recorded PM-last -9.5% (1-min bars
   incomplete when run early); on the full 09-02 1-min SIP history VIVK's exit
   recomputes to flat (entry $1.05 = PM-last $1.05), reclassifying -9.5% -> 0.0%.
   Entered set stays n=15 but SUM lifts +75.2% -> **+84.8% / mean +5.7% / median
   +10.0% / positive 12/15**, vs a PM-last hold-to-open floor of -6.8% and a
   do-nothing baseline of 0%. Net of ~2% spread ~+3.7%/name. The **fade-tail
   drops back to 2/15 (BIVI -27.1%, MIMI-2 -6.9%) = 13%** as VIVK leaves the tail
   — comfortably under the ~25% that would erode the edge below the spread. Init 3
   had **fresh seeds** this run: UFG and GELS exited at the 09-03 04:31 ET pulse.
   GELS is a live-book spike (exit $0.861 -> PM peak $0.977 05:15 ET, 873k sh/2606
   tr, **fills the resting +10% limit $0.9471**); UFG is a thin dead-book staller
   (exit $0.61 -> peak $0.6074 below exit, lim10 unfilled, PM-last -0.9%). Re-ran
   `peak-seeking-exit-sim.js`: plain **+10% sell-limit stays the best rule at
   n=32: SUM +95.0% / mean +3.0%, positive 21/32** (up from n=30's +84.2/+2.8;
   GELS adds a +10 win, UFG a small drag). Still log-only, no orders. Next: keep
   seeding both sims; the Init 6 fade-tail is contained at 13% and n=15 / 12
   positive / two converging studies keep the live PM-gapper pulse near
   proposable — hold until n grows and the tail stays under ~25%.
   **Update 2026-09-02 (strategy-advance) — pilot admitted TWO fresh
   out-of-sample names (JLHL filled the +10% limit, VIVK faded); entered set
   jumps to n=15, edge holds +5.0%/name, fade-tail 3/15 (20%).** Two holdable
   footprint=none PM-only gappers logged 09-02 (JLHL +21.2% late-ramp 04:30 ET
   BUILD, VIVK +19.7% massive-volume plateau at gap-mid). Re-ran
   `init6-pm-pilot.js` (34 candidates): **both admitted** by the continuation
   gate. JLHL's early ramp **filled the resting +10% limit ($7.49)** intrabar =
   a win at the exit rule; VIVK never reached its +10% limit and drifted to
   PM-last -9.5% = a fade. Entered set moves n=13 -> **n=15: SUM +75.2% / mean
   +5.0% / median +10.0% / positive 12/15**, vs a PM-last hold-to-open floor of
   -7.5% and a do-nothing baseline of 0%. Net of ~2% spread ~+3.0%/name. The
   **fade-tail grows to 3/15 (BIVI -27.1%, MIMI-2 -6.9%, VIVK -9.5%) = 20%** —
   still under the ~25% that would erode the edge below the spread, but the ratio
   is worth watching now that VIVK adds a third. Init 3 had **fresh seeds** this
   run: KITT and PXS exited at the 09-02 04:30 ET pulse. Both are dead-book
   stallers (KITT peak +4.6% at 06:10 ET on real vol, lim10 unfilled, PM-last
   +0.6%; PXS thin 2-5 tr/bar, peak +5.0%, lim10 unfilled, PM-last +3.9%), both
   contribute small positives. Re-ran `peak-seeking-exit-sim.js`: plain **+10%
   sell-limit stays the best rule at n=30: SUM +84.2% / mean +2.8%, positive
   20/30** (edge unchanged from n=28's +76.1/+2.7). Still log-only, no orders.
   Next: keep seeding both sims; watch the Init 6 fade-tail ratio (now 20%) — if
   it crosses ~25% the mean edge erodes below the spread. With n=15 / 12 positive
   / two converging studies, the live PM-gapper pulse is nearing proposable; hold
   until the tail confirms it stays contained.
   **Update 2026-09-01 (strategy-advance) — no fresh admit (GYGY gate-skipped),
   but WETO's fill corrected to a +10% limit hit on fuller 1-min bars; entered
   set holds n=13, edge firms to +5.8%/name, fade-tail steady 2/13.** One fresh
   holdable footprint=none PM-only gapper logged 09-01 (GYGY +17.6%, 17K-float
   squeeze) plus recurring/ah-detected names (GPRO, SSM, WETO, PETZ). Re-ran
   `init6-pm-pilot.js` (32 candidates): **GYGY was skipped by the continuation
   gate** — its 04:00 ignition (13.4k trades) held only 4 bars near the high then
   faded below gap-mid, failing the R+1/R+2 80%-of-high hold. No new entered row.
   The one change: last run WETO 08-31 was recorded PM-last +4.9% (bars
   incomplete when run early); with the full 08-31 1-min SIP history now
   available its early spike **filled the resting +10% limit ($7.70)** intrabar,
   so it reclassifies +4.9% -> +10.0%. Entered set stays n=13 but SUM lifts
   +69.6% -> **+74.8% / mean +5.8% / median +10.0% / positive 11/13**, vs a
   PM-last hold-to-open floor of -8.2% and a do-nothing baseline of 0%. Net of
   ~2% spread ~+3.8%/name. The **fade-tail holds at 2/13 (BIVI -27.1%, MIMI-2
   -6.9%) = 15%**, still well under the ~25% that would erode the edge below the
   spread. Init 3 had **no fresh seed** — PXS (entered 08-31 $6.26) is still open
   day 1, no held-name exit to measure, so the peak-seeking sim is data-blocked
   this run (held at n=28, +10%-limit rule unchanged). Still log-only, no orders.
   Next: keep seeding holdable PM-only gappers and track the fade-tail ratio;
   with n=13 / 11-13 positive / tail contained at 15% and two converging studies,
   the live PM-gapper pulse is nearing proposable — hold until n grows and the
   tail stays under ~25%.
   **Update 2026-08-31 (strategy-advance) — pilot admitted another fresh
   out-of-sample name (WETO) that HELD positive without hitting the limit;
   entered set n=13, edge steady +5.4%/name, fade-tail unchanged 2/13.** The
   tracker grew to 31 holdable footprint=none candidates (four weekend-gap
   PM-only gappers logged 08-31: AEHL +72.6%, YDDL +37.0%, WETO +26.6%, NCRA
   +21.7%). Re-ran `init6-pm-pilot.js`: **WETO was admitted** (entered $7.00 at
   04:15 ET), never reached the +10% limit ($7.70) but drifted up to PM-last
   +4.9% — a small positive, not a fade. The other three 08-31 gappers (AEHL,
   YDDL, NCRA) were skipped by the continuation gate (no qualifying
   >=3000-trade ignition hold). Entered set moves n=12 -> **n=13: SUM +69.6% /
   mean +5.4% / median +10.0% / positive 11/13**, vs a hold-to-open PM-last
   floor of -8.1% and a do-nothing baseline of 0%. Net of ~2% spread ~+3.4%/name.
   The **fade-tail holds at 2/13 (BIVI -27.1%, MIMI-2 -6.9%)** — not growing
   toward the ~1-in-4 that would erode the edge; WETO adds a positive admit.
   Still log-only, no orders. Init 3 had **no fresh seed** (no open positions
   after the 08-28 eval, so no held-name exit to measure). Next: keep seeding
   holdable PM-only gappers and track the fade-tail ratio before proposing any
   live PM-gapper pulse.
   **Update 2026-08-28 (strategy-advance) — pilot admitted a fresh out-of-sample
   name (WHLR) and it FILLED the +10% limit; entered set n=12, edge back up to
   +5.4%/name.** The tracker grew to 27 holdable footprint=none candidates (WHLR
   08-28 +128.6% and NA 08-28 +17.5% added). Re-ran `init6-pm-pilot.js`: **WHLR
   was admitted** (entered $2.69 at 04:15 ET) and its early spike **filled the
   resting +10% limit** ($2.96) before it dumped to PM-last -45.4% — exactly the
   peak-seeking case the resting limit is built for. NA was skipped by the
   continuation gate. Entered set moves n=11 -> **n=12: SUM +64.8% / mean +5.4% /
   median +10.0% / positive 10/12**, vs a PM-last floor of -9.1% and a do-nothing
   baseline of 0%. Net of ~2% spread ~+3.4%/name. The **fade-tail holds at 2/12
   (BIVI -27.1%, MIMI -6.9% at lim10)** — not growing toward the ~1-in-4 that
   would erode the edge, and the first admitted out-of-sample entry last run
   (MIMI, faded) is now offset by a winning admitted entry (WHLR). Still log-only,
   no orders. Next: keep seeding; track the fade-tail ratio before proposing any
   live PM-gapper pulse.
   **Update 2026-08-27 (strategy-advance) — pilot entered a fresh out-of-sample
   name (MIMI) and it FADED; the entered set is now n=11 with a second fade-tail
   loser.** The tracker grew to 25 holdable footprint=none candidates (MIMI 08-27
   +31% added, a PM-only gapper). Re-ran `init6-pm-pilot.js`: unlike WVVIP/RDIB
   (both wick-skipped), MIMI was **admitted** by the continuation gate (entered
   $2.45 at 04:15 ET) and then **faded** — never reached the +10% limit, dumped
   to PM-last -14.3%. This is the first admitted out-of-sample entry since the
   pilot started and it is a loser, so the entered set moves n=10 -> **n=11: SUM
   +47.4% / mean +4.3% / median +10.0% / positive 9/11**, vs a PM-last floor of
   -6.4% and a do-nothing baseline of 0%. Net of ~2% spread the edge is
   ~+2.3%/name. **The fade-tail is now 2 of 11 (BIVI -27.1%, MIMI -14.3%)** — the
   risk the resting limit cannot dodge, and worth watching as the key threat to
   the edge. Median still +10.0% (7/11 fill the limit intrabar). Still log-only,
   no orders. Next: keep seeding; if the fade-tail keeps growing toward ~1-in-4,
   the mean edge erodes below the spread and the pilot weakens — track that ratio
   before proposing any live PM-gapper pulse to Juan.
   **Update 2026-08-26 (strategy-advance) — pilot re-run + gate-denominator
   test; the wick-then-rebuild false-negative recurred (RDIB), entered n stays
   10.** The tracker grew to 24 holdable footprint=none candidates (RDIB 08-26
   +67% added, a PM-only gapper). Re-ran `init6-pm-pilot.js`: **RDIB was skipped
   by the continuation gate for the SAME reason as WVVIP** — its 04:30 ignition
   bar wicked to $18.47 then the next bar closed $14.31 (< 80% of the wick high),
   so the gate rejects a name that in fact BUILT to $17.44 by 04:45. Two runs in
   a row a real holdable BUILD (WVVIP +344%, RDIB +67%) is rejected on the
   wick-high hold denominator. Acted on the 08-25 "revisit the wick-high
   denominator if it recurs" note: built `scripts/init6-gate-denom-test.js`
   (log-only) and swept the hold denominator (bar HIGH vs bar CLOSE) over all 43
   footprint=none names. **Result: a close-denominator is NOT a free win.**
   Within the pilot's holdable-only universe it recovers RDIB and WXM (both
   +10%), lifting the entered set to n=12 / mean +6.8% / positive 11/12. But as a
   standalone mechanical gate it also admits four uninvestable wick-fades the
   current gate correctly rejects — LICN -50%, DXST -15%, ZCMD/SFHG +10% — pushing
   the false-positive bucket from -16.3% to -61.3%. So a denominator relaxation
   only helps if paired with the discretionary holdable classification; it cannot
   replace the wick-high gate alone. WVVIP is still not recovered by either
   denominator. **Decision: keep the pilot's conservative wick-high gate for now;
   the entered set stays n=10 (SUM +61.7% / mean +6.2% / positive 9/10). Log the
   wick-then-rebuild false-negative as a known, bounded cost.** Next: keep
   seeding; if a third wick-then-rebuild holdable is missed, reconsider a
   holdable-gated close-denominator variant. Still log-only, no orders.
   **Update 2026-08-25 (strategy-advance) — pilot re-run, gate rejected a wick
   PM-only gapper; entered n stays 10.** The tracker grew to 23 holdable
   footprint=none candidates (WVVIP 08-25 +344% added). Re-ran
   `init6-pm-pilot.js` (deterministic from the tracker): **WVVIP was skipped by
   the continuation gate** — its opening 5-min bar wicked to $13.51 then closed
   $7.06, so R+1/R+2 cannot hold 80% of that wick high and the gate rejects it by
   design (wick-peak filter). Entered set unchanged at n=10 (SUM +61.7% / mean
   +6.2% / positive 9/10). Caveat noted: WVVIP later rebuilt to an $11-12 plateau
   that a R+3 entry (~$7.00) would have filled +10% on, so this is a conservative
   *false-negative* — if wick-then-rebuild PM-only gappers recur, revisit whether
   the gate's wick-high denominator should use the ignition bar's close/VWAP
   rather than its high. No new entered out-of-sample row this run. Still
   log-only, no orders. Next: keep seeding; watch wick-then-rebuild false-negative
   frequency and the BIVI-type fade-tail.
   **PILOT STARTED 2026-08-24 (strategy-advance) — first comparison POSITIVE.**
   Confirmed no other live experiment is running (Init 3 work is log-only sims,
   no live orders; Init 2 has no pilot), so the serialized pilot slot is free.
   Built `scripts/init6-pm-pilot.js` (log-only, no orders) + shadow ledger
   `log/init6-pm-pilot.csv`: it runs the exact converged mechanism — 5-min
   continuation-gate entry near the ~04:00-04:21 ET ignition (enter R+3 open)
   plus the resting +10% sell-limit exit (PM-last fallback) — but restricts to
   the **fillable holdable** footprint=none universe (the mixed 1-min sim admits
   thin/uninvestable false-positives WLDS/SDEV/EHGO-2 we could never fill, which
   drag the mean). On the 22 holdable PM-only gappers the gate enters 10 (skips
   12 with no >=3000-trade ignition or failed hold). **Pilot result: SUM +61.7%
   / mean +6.2% / median +10.0% / positive 9 of 10**, vs a hold-to-open PM-last
   floor of -5.7% and a do-nothing baseline of 0% (current live cycle enters
   none of these). Net of ~2% micro-cap PM spread the edge is ~+4.2%/name. The
   one loser is BIVI -27.1% (real fade, never hit +10%, dumped to PM-last) — the
   tail the resting limit cannot avoid. Entry times cluster 04:15-05:05 ET, near
   the ignition as intended. Restricting to fillable names lifted the edge from
   the mixed sim's +2.7% to +6.2%. Still log-only, no live orders. Next: seed new
   holdable PM-only gappers as they log to grow the entered n out-of-sample, and
   watch the BIVI-type fade-tail frequency before proposing any live PM-gapper
   pulse to Juan.
5. **Initiative 1 - earlier volume-lead entries.** **Hypothesis falsified
   (2026-07-15):** volume does not lead price — ignition is a single-minute
   co-spike at both 5m and 1m resolution (`INIT1_VOLUME_LEAD.md`). No standalone
   edge; its value folds into Init 3 (detect the ignition fast). Effectively
   closed as a distinct initiative.

Done: Initiative 4 (email identity + reply feedback).

## How we roll changes out

1. **Research** — understand the mechanism, the data we need, and the cost.
2. **Instrument** — start logging the signal/metric without acting on it
   (mirrors the proven ceiling-override / dead-cat / PM-only-gapper trackers).
3. **Pilot** — act on it in paper/shadow mode, measure against the baseline.
4. **Promote** — only after evidence (target: a clear edge over several weeks).

Serialization applies to the **pilot** stage only: never run more than one
initiative in *pilot* at a time, so effects stay attributable. Non-pilot work
(Research, Instrument/log-only, build/delivery) is **not** serialized and runs
in parallel.

---

## Initiative 1 — Earlier entries via a pre-explosion volume signal

**Idea (Juan):** We catch spikes late, once they are already +50-100%. Charts
suggest a volume surge precedes the price explosion. If we detect the volume
ramp (e.g. ~10x normal) we could enter earlier, before the move.

**Status:** **Research done — hypothesis FALSIFIED (2026-07-15).** Built
`scripts/volume-lead.js` (log-only) and ran it on 7 winners with real Alpaca SIP
bars. Volume does **not** lead price: on every real AH mover (IVF, VTAK, EDHL,
MSW) the price reaches +20% at or before the volume threshold (LEAD ≈ 0 or
negative). Zoomed to 1-min on the clearest case, **IVF ignited in a single
minute (16:53 ET): +19% price jump and the 25k-share/72-trade volume spike in
the same bar** — no quiet volume ramp to front-run. The two PM-only gappers
(GLXG/CIIT) showed a big "lead" but it is a **false positive** on thin AH prints
(hundreds of shares, <40 trades); their real move is a news-driven 04:00 ET PM
explosion with no tradeable AH precursor. Full write-up in `INIT1_VOLUME_LEAD.md`.
**Reframe:** "we catch late" is real, but the fix is **faster ignition detection
/ scan timing** (our AH scan at ~16:15 ET runs *before* IVF's 16:53 ET ignition),
which is Initiative 3, not a volume-lead entry rule. This initiative folds into
Init 3 and is effectively closed.

**Reopened angle (Juan, 2026-07-16 email feedback):** the volume *lead* is dead,
but Juan proposes the *first volume spike bar* as the entry trigger ("that would
be a great entry point") and no-spike as a negative filter ("LVLU is clearly
terrible: no volume spike"). This is the co-spike entry, distinct from front-
running: enter on the ignition bar, skip/downgrade names with no AH volume
surge. Consistent with the IVF 16:53 ET single-minute ignition finding. Blocker
is detection latency (spike fires between fixed scans, e.g. KUST/GCTK feed-lag
misses on the 07-14 cycle) — so the tradeable form of this needs Init 3's
tighter scan cadence. Next: (a) add a no-AH-volume-spike negative filter to the
scanner grade, (b) prototype a spike-bar entry trigger once scan cadence can
resolve the bar. Captured from FEEDBACK_LOG 2026-07-16.

**Feedback update (2026-09-03) — QUANTIFIED THRESHOLD:** Juan rejected GELS
(and TLYS/CHPT/UFG) on the 09-02 email — "you are entering trades that do not
have clear volume spikes. The volume when you enter must be spiking 10 to 20
times more than what it was before ... when you entered GELS the volume was the
same as the previous night, so you should not enter. We're looking for things
that are starting to grow in volume." This puts a **hard number** on the
per-bar volume-change gate that prior feedback (DAIC/BOOM/ONMD/GRSD) described
only directionally: the entry bar's volume must be **10-20x the ticker's own
immediately preceding volume**, not just elevated versus average daily volume.
A big % move on flat/prior-night-level volume is a price-only spike and a hard
skip. Routed to `scanner-improvement` to implement the 10-20x local-spike gate
as a hard entry filter and add GELS as a negative control. See FEEDBACK_LOG
2026-09-03.

**Feedback update (2026-09-04) — GIPR added as a negative control:** Juan on
the 09-03 email — "GIPR is another violation of volume rule." GIPR was entered
($0.63 -> $0.48, -23.8%) on a weak volume build, cleared the scan-count/CONFIRM
gate but had no real 10-20x per-bar ignition. Sixth-plus repeat of the theme.
Add GIPR alongside GELS as a negative control the queued 10-20x local-spike
hard gate must reject. See FEEDBACK_LOG 2026-09-04.

**Feedback update (2026-09-09) — SUNE negative control + define the volume
metric:** Juan on the 09-08 email — "SUNE is not a good entry because price only
went up in the first 5m bar. all subsequent bars are stable ... super high
volume compared to the rest of the time (something is happening, volume is
enough, no need for catalist). the graph for volume reveals a lot to me, but I
don't know what the calculation should be." Two items. (1) **SUNE** is a new
negative control of a *different* shape than the flat-volume rejects: a
single-bar price pop that stalls (first 5m bar up, subsequent bars flat) — the
"one bar up then stable" case the entry gate must reject. Add alongside GELS/
GIPR. (2) **Define the volume metric.** Juan explicitly asks what the volume
calculation should be — turn the directional 10-20x idea into a concrete spec:
per-bar volume vs a rolling baseline of the ticker's own recent bars, the
ratio/threshold, and how to render it on the daily-email chart (folds into
Init 5) so the "graph reveals a lot" becomes a computed gate. "No need for
catalyst" reaffirms the volume+price co-spike can stand alone. Routed to
`scanner-improvement` to specify and implement. See FEEDBACK_LOG 2026-09-09.

**Feedback update (2026-08-25):** Juan flagged DAIC (re: 08-24 email) — "no
volume spike. normal hours volume is the same as after hours, it was only a
price spike. UPDATE PROCESS." DAIC was not actually entered (skipped on the
+150% ceiling), so this is a general selection-rule steer, not an entry
correction: a large % move with AH per-bar volume ≈ normal-hours volume is a
price-only spike and a hard skip. Reinforces the per-bar volume-change gate
already proposed here (measure the ignition bar's volume vs the ticker's own
preceding bars, not only shares/avg-vol) and the CONFIRM-3 hard entry gate in
Init 3. Same signature as GRSD (08-14), BOOM (07-31), ONMD (07-29). Juan also
praised the WLDS trade ("traded well, good job") despite its -19.4% loss — the
volume-backed AH BUILD selection is the pattern to keep even when a trade fades.
Captured from FEEDBACK_LOG 2026-08-25.

**Feedback update (2026-07-31):** Juan also rejected BOOM because its volume
before the price spike stayed roughly flat and the later increase was too small
to justify entry. His follow-up explicitly ordered the open BOOM position sold;
the exit order was submitted on 2026-08-03. This sharpens the proposed gate:
measure each ignition bar's volume jump against that ticker's immediately
preceding bars, not only absolute AH shares or volume versus average daily
volume. Add BOOM as a negative control to Initiative 3's 5-minute replay and
test whether a local volume-change gate rejects it without excluding real
winners.

**Feedback update (2026-07-29):** Juan rejected the ONMD buy because "there
isn't enough volume." The scan recorded 5M AH shares / 3.7x average volume, but
the chart showed modest AH bars beside a 5.9M regular-open bar. Treat this as a
selection and presentation check, not proof for an immediate threshold: test
whether the no-spike negative filter would reject ONMD on per-bar volume,
trades, and accumulation, and fix Initiative 5's shared volume scale so the
review chart does not distort the comparison. Catalyst size must not rescue a
name whose real volume profile fails the eventual gate.

**Why it is plausible:** the scanner already computes VRatio (AH volume vs avg)
and IRVol (intraday relative volume). The winners (LNAI, LPA) showed VRatio
6-8x at entry. The hypothesis is that volume crosses a threshold *before* the
big % move, so a volume-first trigger could front-run the price-first trigger.

**Open questions:**
- Does volume actually lead price on our winners, or move together? Need to
  pull minute-level AH/PM volume for past winners and check the lead/lag.
- What threshold (VRatio, absolute shares, rate-of-change) separates real
  pre-moves from noise/thin prints? Thin single-print spikes (DWTX, CTNT) are
  the main false-positive risk.
- Does an earlier entry actually improve P&L, or just increase exposure to
  fakeouts that never explode?

**Rollout plan:**
1. Build a backtest: for each past winner, reconstruct minute volume and find
   when VRatio first crossed candidate thresholds vs when price crossed +20%.
2. Instrument: add a "volume-lead" flag/column to the scanner output (log only,
   no action) and record in morning eval whether it would have fired early.
3. Pilot: add hypothetical early-entry rows to paper trades, compare to actual.
4. Promote only if early entries beat current entries net of false positives.

**Needs from Juan:** nothing yet (research uses existing Yahoo data).

---

## Initiative 2 — Real broker paper trading (Europe), then live

**Idea (Juan):** Move from spreadsheet-style paper P&L to a real broker's paper
account available in Europe, so numbers reflect real fills/spreads/liquidity.
Eventually switch the same integration to live trading.

**Status:** **PROMOTED to the live paper cycle (2026-06-25).** The
scanner-improvement loop wired `broker.js` directly into the trading pulses
(commits `0c43af9` "switch to Alpaca paper execution; clean break from fictional
ledger" and `a508bfe`): `post-market-scan.md` submits real ext-hours Alpaca
paper buys, `position-evaluation.md` submits real sells, and
`morning-evaluation.md` reads positions/P&L from Alpaca as the source of truth.
The hand-maintained assumed-price ledger was discarded; `OPEN_POSITIONS.md` now
mirrors Alpaca. This makes the shadow-fills comparison moot — real fills are
captured natively at entry/exit, which is what rollout steps 3-4 aimed for.
Account `PA37U2Y192A7` is flat at ~$99,998.41 (two validation round-trips paid
~$1.59 spread). The only remaining step is 5 (live real money, tiny size),
gated on a proven edge and Juan's sign-off — not now. **The single pilot slot
is now free for Initiative 5.**

**Directive 2026-09-04 (Juan, re: 09-03 email) — research broker alternatives
to Alpaca.** "Can you also research alternative providers besides alpaca? test
them and find one that actually works for trading these stocks." Root cause of
the chronic AH no-fill is the Alpaca free IEX-only feed (see the 08-07 update
and `INIT2_ALPACA_FILL_ROOTCAUSE.md`); Juan chooses to switch brokers rather
than pay for Alpaca SIP or score on modeled fills. Active research directive for
`strategy-advance` (non-serialized, low-risk): (1) shortlist brokers with a
paper/API and real extended-hours micro-float coverage — IBKR paper first, then
Trading 212 / Webull / Moomoo / others; (2) test each on the exact names Alpaca
blocks (AKAN, SHPH, and GIPR-class sub-$1 micro-floats) to confirm which
actually fills extended-hours limit orders; (3) report the best fit and propose
the switch. No live broker change applied here — evaluate and propose. See
FEEDBACK_LOG 2026-09-04.

**Prior pilot status (2026-06-24, superseded):** second ext-hours round-trip + shadow-fills ledger
started. Repeated the VTAK shadow round-trip in premarket: BUY 86
filled at **$1.35 (the ask)**, SELL filled at **$1.34 (the bid)**, position
flat. Spread held at **1c** even at the higher price, so relative cost shrank to
**0.74%** round trip (vs 0.88% at $1.14 yesterday) — the buy@ask / sell@bid
model is confirmed twice. EPOW (sub-$1, $0.52) had **no fresh ext-hours quote**
(ask $0.00, stale prior close) and would not have filled in extended hours —
confirming the coverage gap is worst on the cheapest names. Started a
shadow-fills ledger at `log/shadow-fills.csv` to accumulate these comparisons.
Applied the fill model to today's two real closed paper trades: VTAK (+70.7%)
loses only ~1-2% of its gain to spread (survives easily); EPOW (-10.1%) would
have its loss widened ~29% by spread and might not have filled at all. **Takeaway
so far:** spread is a rounding error on big winners but meaningfully erodes small
losers, and sub-$1 names carry real ext-hours non-fill risk. Earlier findings
hold: micro-float names are `tradable=true`; Alpaca IEX historical bars are
sparse so Yahoo stays the chart/history source.

**Open question for next step:** historical NBBO isn't available on the free
tier, so reconstructing past fills is impossible — real comparison needs fills
captured *at the moment* of each paper entry/exit. Options: (a) a log-only
shadow pulse that mirrors current open paper positions to Alpaca at entry/exit
windows, or (b) wiring a shadow order into the scan/eval pulses (changes pulse
behavior -> propose to Juan, don't apply silently).

**Findings:**
- The environment already scaffolds `ALPACA_API_KEY`, `ALPACA_SECRET_KEY`,
  `ALPACA_PAPER_TRADE` (currently unset), which suggests Alpaca was the intended
  path. Alpaca paper accounts are free, give instant REST API keys, and model
  fills/slippage. Caveat: live US-equities trading from the EU is restricted,
  and some micro-float / OTC names we trade may not be tradable on Alpaca.
- Interactive Brokers (IBKR) is EU-regulated, has a paper account + API
  (Client Portal / TWS), and a real path to live trading on US small caps. More
  setup overhead than Alpaca.
- Trading 212 / others: practice modes exist but lack a documented trading API.

**Recommendation:** start the paper phase on **Alpaca** (lowest friction, env
convention already exists, clean REST API). Keep **IBKR** as the live-trading
target later. Validate that our typical tickers (sub-$10, low float) are
tradable before committing.

**Rollout plan:**
1. ~~Juan creates an Alpaca paper account, provides API key/secret.~~ ✓ done.
2. ~~Build `scripts/broker.js`: submit/track orders, read fills; add `--ext`.~~ ✓ done.
3. Shadow mode: mirror existing paper entries/exits as Alpaca paper orders,
   compare real fills to our assumed prices for a few weeks. **In progress** —
   first round-trip fills at ask/bid; collect more across sessions.
4. Switch the paper-trade ledger to use real fills (buy@ask / sell@bid).
5. Much later, after a proven edge: flip to live with tiny size.

**Needs from Juan:** nothing blocking — keys are live. (Optional: set
`ALPACA_PAPER_TRADE=1` explicitly, though the base URL already targets paper.)

---

## Initiative 5 — Better data + review surface (charts, sources)

**Idea (Juan, 2026-06-19; broadened 2026-06-23):** Juan needs to **review the
data to steer**. Two parts: (a) graphs in the daily email, "probably 5m
including volume," for the candidates/positions reported; (b) improve the
underlying **data sources** so the numbers are reliable enough to act on and
chart (Yahoo AH/PM data is gappy; Alpaca market data and financialdatasets.ai
are candidates).

**Status:** **Wired into the daily email (2026-06-26, path b).** `scripts/chart.py`
is dependency-free,
5m + volume candlestick that fetches Yahoo bars (incl. AH/PM), shades the pre/
post sessions, and renders SVG -> PNG via ImageMagick. Verified on ORIS (the
AH->PM winner: regular climb -> after-hours build -> premarket spike to ~$5.85
then fade, all visible) and VTAK. Data-source eval: Yahoo is the better history/
5m source (Alpaca IEX bars are sparse); Alpaca is best for live quotes/fills.

**Update (2026-06-25) — InboxKit has NO attachment API; the attach-PNG plan is
dead.** Checked the authoritative spec (`https://inboxkit.cc/api/openapi.json`):
`POST /api/messages` accepts only `to`, `subject`, `text`, `html` — no
attachment or multipart field. So charts cannot be attached. Re-verified the
chart pipeline on today's winner **AZI**: `chart.py AZI --range 2d` renders the
full AH->PM pattern (flat regular session ~$1.25 -> after-hours spike to ~$2.34
-> premarket fade to ~$1.79, with the volume panel) — the renderer is fine; only
delivery is blocked. Two viable delivery paths remain:
- **(a) Inline `<img src="https://...">` with a hosted PNG.** Gmail proxies and
  displays remote https images. Needs somewhere to host each daily chart with a
  public URL (base64 data URIs are stripped by Gmail, so those won't work).
- **(b) Commit charts to the daily log dir as a gallery + link from the email.**
  Charts already follow the `log/YYYY-MM-DD/TICKER-HHMM.png` convention; Juan is
  authenticated to the (private) GitHub repo, so an email link to the day's log
  dir shows the charts with zero hosting. Lowest effort, no new infra.

**Update (2026-06-26) — path (b) wired into the daily-email pulse.** Juan didn't
object to the (b) recommendation, so applied it: `prompts/daily-email.md` now has
a "Generate Charts" step that runs `chart.py` for the winner + each open Alpaca
position into `log/YYYY-MM-DD/`, and a "Charts (5m + volume)" email section that
links each PNG via its GitHub blob URL
(`https://github.com/juanibiapina/trading/blob/main/log/.../TICKER-HHMM.png`).
Log-only change, no trading logic touched. Verified the full pipeline on today's
real tickers: `chart.py ILLR --range 2d` and `chart.py IVF --range 2d` both
rendered (49 KB / 44 KB PNGs); the ILLR chart clearly shows the regular-session
climb -> after-hours build to ~$4.20 (amber) -> premarket spike to ~$7 then fade
(blue) with the volume surge in the panel. First live use: tomorrow's daily
email. Remaining check: confirm the committed PNG actually displays when Juan
opens the GitHub blob link (it resolves only after the cycle's git push).

**Update (2026-06-30) — path (b) is DEAD; switch to path (a) inline images.**
Juan's reply to the 06-29 email: "The link to the chart didn't work. Also I'd
like the chart image directly in the email." The GitHub blob link 404s (verified)
because the repo is private, so Gmail and any not-logged-in viewer can't open it,
and a blob URL can't render inline regardless. Path (b) is abandoned. Reviving
path (a): host each daily PNG at a public https URL and inline it with
`<img src="https://...">` (Gmail proxies remote https images; base64 data URIs
are stripped, so hosting is mandatory). InboxKit needs no new features — it
already sends `html`; the only gap is a zero-auth public host. Next step: choose
a host (public gist raw, Cloudflare R2, or a dedicated public assets repo) and
update `prompts/daily-email.md` to emit inline `<img>` instead of blob links.

**Update (2026-07-01) — Juan proposes two better paths (c, d).** Reply to the
06-30 email: "can I add a feature to inboxkit that would allow emails with
images? Alternatively, is the trading repo safe to make public? If so, we could
have HTML reports published as GitHub pages." Two new options, both removing the
hosting blocker:
- **(c) InboxKit image feature.** Juan owns InboxKit (`~/Sync/notes/zero`), so
  attachment/inline-image support can be added to its send API — this reverses
  the 2026-06-25 "no attachment API" blocker. Would let
  `send-email-inboxkit.js` attach or inline the PNG directly.
- **(d) Public repo + GitHub Pages.** Make `juanibiapina/trading` public and
  publish HTML reports (charts inline) as GitHub Pages. Doubles as a zero-auth
  public PNG host (fixes path (a)'s only gap) AND delivers the "better review
  surface" half of this initiative in one move — richer than email.
- **Secrets-safety check (done 2026-07-01):** repo is safe to publish. No
  credentials committed; `broker.js` (Alpaca) and `send-email-inboxkit.js`
  (InboxKit) read all keys from env vars, and the only config-ish tracked file
  (`.config/dev-session`) is a harmless tmux layout. The make-public decision
  (exposes full strategy + trade history) is Juan's.

**Update (2026-07-03) — Juan approved path (d); repo is now PUBLIC.** Reply to
the 07-02 email: "Make the repo public." Re-ran the secrets scan (clean — all
keys from env / `~/.gmcli/accounts.json`, only tracked config is the tmux
`.config/dev-session`) and set `juanibiapina/trading` to public via `gh repo
edit`. Hosting blocker is gone: GitHub blob/raw URLs and (once enabled) GitHub
Pages now serve `log/YYYY-MM-DD/TICKER-HHMM.png` with zero auth. Next steps:
(1) update `prompts/daily-email.md` to inline charts via a raw.githubusercontent
`<img src>` (Gmail proxies remote https images), and optionally (2) publish HTML
reports via GitHub Pages for the richer review surface.

**Update (2026-07-08) — inline `<img>` raw-URL charts WIRED into the daily
email.** Switched `prompts/daily-email.md` step 2 from blob links (which 404'd
for Juan on 06-30) to inline `<img src="https://raw.githubusercontent.com/...">`
images, now that the repo is public. Verified a `raw.githubusercontent.com` PNG
URL returns **HTTP 200** on the public repo and that `chart.py` still renders
(SHPH 2d, 45 KB). Added a **commit + push charts BEFORE sending** step so the
raw URL is live when Gmail's image proxy fetches it (prevents Gmail caching a
404 the way the old flow risked). First live use: next daily-email run. Remaining
check: confirm the inline image actually displays in Juan's Gmail on the next
report. GitHub Pages HTML reports remain a follow-on for the richer review
surface.

**Update (2026-07-09) — first live inline-chart reply: partial render + a real
data gap.** Juan's reply to the 07-08 email: "RPGL chart isn't showing"; "SUNE
chart is showing, yes! but... there's no volume in post market. we need volume in
post market!" Two findings:
- **Render race (minor).** SUNE's inline `<img>` displayed; RPGL's did not, even
  though both PNGs are in the same commit (86cbfb7) and both raw URLs return 200
  now. Cause: Gmail's image proxy fetched RPGL before the raw CDN propagated the
  new commit and cached the miss. The "push before send" step is not enough — add
  a post-push check that polls each `raw.githubusercontent` URL for HTTP 200 (and
  a short delay) before sending. Routed as a daily-email process tweak.
- **Extended-hours volume is BLANK (structural).** Confirmed Yahoo's 5m chart
  feed returns volume only for the regular session: tested AAPL and TSLA, both
  0/132 pre and 0/97 post bars carry volume vs 156/156 regular. `chart.py` draws
  volume per bar, so the pre/post (blue/amber) panel is empty by construction —
  exactly the region our AH->PM edge lives in. This is the **data-source-quality
  half** of this initiative and now the priority within Init 5. Fix: source
  extended-hours 5m volume from a second feed and use it for pre/post bars —
  candidates are **Alpaca bars** (keys live via Init 2) and **TradingView**
  (already the PM-volume source in `scripts/pm-volume-check.py`). Keep the
  regular session on Yahoo or unify on the better feed; scale bars honestly.

**Update (2026-07-10) — Juan escalated the blank AH volume; make it the
immediate next task.** Reply to the 07-09 email: "The chart still has no volume
in AH. If you have no data there, how can we even enter?" Same panel shipped
unchanged, so he reframed it from cosmetics to decision integrity: an empty
volume panel in the exact AH window where our edge lives can't justify an entry,
and the scanner's own AH volume figures (VRatio, per-bar surge) need a
trustworthy feed too. No new fix — this is the already-documented recommended
step below, now the priority ahead of the render-race 200-check and GitHub Pages.

**Update (2026-07-14) — extended-hours volume backfill WIRED into `chart.py`.**
Addressed Juan's escalated ask ("the chart still has no volume in AH... how can
we even enter?"). Added `backfill_ext_volume()` to `scripts/chart.py`: after the
Yahoo fetch (which returns vol=0 for every pre/post bar) it pulls Alpaca SIP 5m
bars via `broker.js`, matches by timestamp, and fills the missing extended-hours
volume (degrades silently to Yahoo if Alpaca is unavailable). Verified on MIMI
(a 07-13 PM-only gapper): **170 ext-hours bars backfilled**, the premarket volume
panel now renders the 04:00 ramp that was previously blank. The AH/PM volume
blind spot in the review surface is closed. Remaining Init 5 items: (1) minor
cosmetic — the regular-open volume bar can dwarf the ext-hours bars on the shared
scale (follow-up, not blocking); (2) the post-push raw-URL 200-check for the
daily-email render race; (3) GitHub Pages HTML reports for the richer surface.

**Update (2026-07-22) — entry/exit markers WIRED into `chart.py` + the daily
email.** Juan's reply to the 07-20 email: "Awesome work! Can you add the enter
and exit markers in the graphs?" Added `--entry` / `--exit` flags to
`scripts/chart.py` (each `PRICE` or `PRICE@YYYY-MM-DD HH:MM`, exchange-local):
draws a dashed price line + a triangle marker (entry blue/up, exit magenta/down)
pinned to the fill bar, labeled, with legend swatches; backward compatible.
`prompts/daily-email.md` step 2 now pulls real Alpaca fills
(`broker.js orders all`) and passes the flags so charts show where we actually
traded (markers for real fills only — omit for detected-not-traded winners,
entry-only for still-open positions). Verified on HIHO (entry $1.50 @ 07-20
16:05 -> exit $1.89 @ 07-21 08:10). First live use: next daily-email run.
Remaining Init 5 items unchanged: (1) minor cosmetic regular-open volume bar
scale; (2) post-push raw-URL 200-check for the render race; (3) GitHub Pages
HTML reports.

**Feedback update (2026-09-24):** Juan reported that the Sep 23 daily-email charts did not work, then asked us to disregard the report because he may have been offline. All three raw PNG URLs (SPHL, GCTK, TOPS) returned HTTP 200 with `image/png` on recheck. No new chart-delivery defect is established; keep the current delivery path and investigate only if it recurs while online. See `FEEDBACK_LOG.md` 2026-09-24.

**Feedback update (2026-07-29):** Juan read ONMD's chart as "not enough volume."
The AH tape logged 5M shares / 3.7x average, but the shared volume axis was set
by a 5.9M regular-open bar, visually compressing the AH bars. The volume-scale
item is no longer only cosmetic because it affects Juan's entry review. Next
chart pass should use a session-aware scale or clipped/log scale while labeling
true values, so AH accumulation can be judged without inflating it.

**Prior recommended step (superseded above):** merge an extended-hours volume
source into `chart.py` (Alpaca 5m bars first, TradingView fallback) so the
post/pre volume panel is populated, then add the post-push raw-URL 200-check to
the daily-email pulse.

**Findings/notes:**
- Need a data source for 5-minute OHLCV bars. Yahoo's chart API already serves
  5m bars (`interval=5m&range=5d`, with `includePrePost=true` for AH/PM). Alpaca
  bars API (Initiative 2) is now available (keys live) as a sturdier source.
- Render to PNG (e.g. lightweight candlestick + volume subplot) and attach to
  the InboxKit email, or inline as base64. Verify InboxKit attachment support.
- Keep it cheap: only chart the reported tickers, not the whole scan.

**Rollout plan:**
1. Prototype a 5m+volume candlestick PNG from Yahoo data for one ticker.
2. Wire attachment into `scripts/send-email-inboxkit.js`.
3. Add charts to the daily email for reported candidates/positions.

**Needs from Juan:** nothing yet; will confirm look/format on first prototype.

---

## Initiative 3 — Adaptive scheduling of pulses

**Latest status (2026-08-26): +10% limit strengthens at n=24 — two live-book exits (XPON, YYGH) both fill the +10% limit (SUM +81.2% / mean +3.4%, positive 16/24).** Today's 04:30-04:31 ET position eval sold two held names: **XPON** ($6.42) and **YYGH** ($2.02). Both are live-book names with a genuine post-exit *premarket* spike that fills the +10% limit: XPON exit $6.42 -> peak $7.15 05:10 ET (+11.4%, 145k sh/2827 tr); YYGH exit $2.02 -> peak $2.61 07:00 ET (+29.2%). Seeded both into `peak-seeking-exit-sim.js` (n=22 -> n=24) and `premarket-exit-gap.csv`, re-ran: plain **+10% sell-limit stays the core rule, SUM +81.2% / mean +3.4%, positive 16/24** (up from +61.2% / +2.8% / 14/22). Both new seeds contribute +10%, so mean rose. The dead-book-dumper tail (LOOP -20.5) is still 1 of the last 8 seeds, not growing; the wide ~-15% catastrophe-stop stays optional. `CONFIRM-3` and both instruments stay log-only. Next run: keep seeding held names as they exit. **Prior status (2026-08-25): +10% limit unchanged at n=22 — one more dead-book faller (WLDS) seeded, no swing (SUM +61.2% / mean +2.8%, positive 14/22).** WLDS (held from 08-24 $3.30, exited 08-25 04:30 ET at $2.66, -19%) is another thin dead-book stall: post-exit PM peak only $2.85 04:40 ET (+7.1%, 186-696 tr/bar), the +10% limit ($2.93) never fills, PM-last ~$2.65 (-0.4%). Seeded into `peak-seeking-exit-sim.js` (n=21 -> n=22) and `premarket-exit-gap.csv`. Re-ran the sim: plain **+10% sell-limit stays the core rule at n=22, SUM +61.2% / mean +2.8%, positive 14/22** — WLDS's -0.4% is a negligible drag, no change to the conclusion. Dead-book-dumper watch: WLDS is a *staller* (~0), not a *dumper* (unlike LOOP -20.5); the extreme-dumper tail (LOOP) is still 1 of the last 6 seeds, not growing, so the wide ~-15% catastrophe-stop stays optional not required. `CONFIRM-3` and both instruments stay log-only. Next run: keep seeding held names as they exit. **Prior status (2026-08-21): OCO-floor variant tested — a breakeven stop is WRONG (whipsaws everything), only a WIDE catastrophe-stop (~-15%) helps, and only marginally. Plain +10% limit stays the core rule at n=21 (SUM +61.6% / mean +2.9%, positive 14/21).** Three more held names exited at the 08-21 04:30 ET pulse — **SUGP** ($4.27), **LGO** ($0.6701), **ISPC** ($1.79), all dead-book faders — seeded into `peak-seeking-exit-sim.js` (n=18 -> n=21) and `premarket-exit-gap.csv`. None filled the +10% limit: SUGP dumped to PM-last -6.3%, ISPC to -8.4%, LGO stalled +6.0%. Executed the 08-20 next step — built the **OCO-floor variant** into the sim (resting +10% sell-limit paired with a protective stop F% below the exit price, causal per-bar) and swept F in {0,5,10,15,20}. **Result kills the naive 08-20 refinement:** a stop AT the exit price (breakeven, O0) collapses to SUM +20.8 / mean +1.0, positive only 3/21 — it whipsaws nearly every winner, because the first post-exit bar dips through the exit price intrabar before the name spikes (PAVS/CELZ/BAOS/GXAI/XOS/MSS all get stopped at 0% instead of +10%). A moderate floor (O5) still whipsaws dip-then-rip winners (BOXL +10->-5, MTEN +3->-5) and nets WORSE than plain L10 (+50.4 < +61.6). Only a **wide catastrophe-stop** helps: O15 (stop -15% below exit) catches only the extreme dumper LOOP (-20.5 -> -15.0, +5.5 saved) with zero collateral whipsaw (SUM +67.1, positive 14/21); O10 is marginally higher (+68.0) but whipsaws SUGP (-5.9 -> -10.0). **Conclusion:** the plain resting +10% sell-limit stays the core rule; the LOOP-type -20% tail is the price of the free optionality, and if a protective stop is added at all it must be a **wide ~-15% catastrophe-stop, never a breakeven OCO**. The +5.5 improvement rests entirely on one dumper (LOOP), so it is a minor refinement, not a change to the core proposal. `CONFIRM-3` and both instruments stay log-only. Next run: keep seeding held names; the OCO question is answered (breakeven stop rejected, wide catastrophe-stop optional) — refocus on out-of-sample seeding of the core +10% rule and any dead-book-dumper frequency (LOOP/SUGP/ISPC are 3 of the last 5 seeds — watch whether the dumper tail is growing enough to justify the wide stop). **Prior status (2026-08-20): +10% resting sell-limit still the best rule at n=18, but a dead-book faller (LOOP) exposes real fallback downside (mean +3.7%, positive 13/18).** Two more held names exited at the 08-20 04:30 ET pulse — **BTOG** (Grade D, -39% exit $0.76) and **LOOP** (Grade None, -18% exit $1.11), both weak/dumped-at-open names — seeded into `peak-seeking-exit-sim.js` (n=16 -> n=18) and `premarket-exit-gap.csv`. Neither had premarket upside: BTOG peaked only +1.2% ($0.7694, thin 9.3k sh) and LOOP +4.5% ($1.16, 203k sh) then **dumped to PM-last $0.882**. Both leave the +10% limit unfilled, so the sim's realistic fallback (cancel at 09:30, sell into the open) captures BTOG -3.9% and **LOOP -20.5%**. Re-ran the sim: the resting **+10% sell-limit remains the best rule — SUM +67.0% / mean +3.7%, positive on 13 of 18**, still beating every trailing stop (best trail12 +2.1% mean) and every other limit width (L5 +1.7, L15 +3.0, L20 +1.5, L30 +1.7). The five negatives are all dead-book/faded names (MGIH -1.0, DARE -1.2, ONFO -3.5, BTOG -3.9, **LOOP -20.5**). **New nuance the two 08-20 seeds surface:** the "safe on dead books (~0)" claim is only true for dead books that *stall*; a dead book that actively *dumps* into the open (LOOP) turns the unfilled-fallback into a real loss vs the plain 04:30 exit, because you cannot retroactively sell at the 04:30 price once you have committed to resting the limit. This refines the proposal to Juan: pair the resting +10% sell-limit with a protective **stop at the 04:30 exit price (OCO)** so a name that fades back through the exit level market-outs near breakeven instead of dumping to the open. The core edge still holds (13/18 positive, +10% still dominant), but the naive "market exit fallback" wording understated the tail. `CONFIRM-3` and both instruments stay log-only. Next run: keep seeding held names; simulate the OCO-floor variant (limit +10% / stop at exit) to confirm it neutralises LOOP-type fallers without hurting the live-book winners. **Prior status (2026-08-19): +10% resting sell-limit edge STRENGTHENS out-of-sample (n=16, mean +5.7%, positive 13/16).** Two more held names exited at the 08-19 04:31 ET pulse — **MSS** (Grade None, +15.8% green exit) and **TNON** (Grade None, +12.1% green exit), both live-book names — seeded into `peak-seeking-exit-sim.js` (n=14 -> n=16) and `premarket-exit-gap.csv`. Both showed a genuine post-exit *premarket* peak that fills the +10% limit: **MSS exit $2.20 -> $2.44 at 04:45 ET (+10.9%)**, **TNON exit $9.74 -> $11.44 at 04:35 ET (+17.5%)**. Re-ran the sim: the resting **+10% sell-limit is again the best rule and improves — SUM +91.4% / mean +5.7%, positive on 13 of 16**, still beating every trailing stop (best trail12 +3.1% mean) and every other limit width (L5 +3.4, L15 +4.9, L20 +3.2, L30 +3.5). The only three negatives are the dead-book/stalled names (MGIH -1.0, DARE -1.2, ONFO -3.5) — every live-book name contributes positively, confirming the edge concentrates in names with a live premarket book and a resting limit is free optionality on dead books. Peak-ceiling tally now +396.3% over 16. n=16 out-of-sample plus two converging studies (Init 3 overnight holds + Init 6 PM-only gappers) make the firm proposal to Juan well-evidenced. `CONFIRM-3` and both instruments stay log-only. Next run: keep seeding held names as they exit; watch dead-book losers keep contributing ~0. **Prior status (2026-08-18): +10% resting sell-limit edge HOLDS out-of-sample (n=14, mean +5.1%, positive 10/14).** Five held names exited at the 08-18 04:31 ET pulse (DARE, GRSD, ONFO, SGLY, XOS) — the first fresh seeds since GXAI (08-13). Added all five to `peak-seeking-exit-sim.js` and `premarket-exit-gap.csv`. The resting **+10% sell-limit stays the best rule at n=14: SUM +71.6% / mean +5.1%, positive on 10 of 14**, still beating every trailing stop (best trail12 +3.5% mean) and every other limit width (L5 +3.3, L15 +4.7, L20 +4.0). Out-of-sample the two same-day dumped-at-open names still gave big *premarket* upside after our exit — **SGLY spiked to $9.83 at 04:50 ET (+83.7%) and XOS to $4.36 at 05:55 ET (+25.3%)** — both filling the +10% limit. The three multi-day-stalled Grade-B losers (DARE/GRSD/ONFO, exited on time-limit far below entry) had dead books and no premarket upside (peaks +0.5/+7.4/+0.9%), correctly contributing ~0 or slightly negative — the edge concentrates in names with a live book. Peak-ceiling tally now +368.9% over 14. The +10%-limit finding survives the added dead-book losers, strengthening (not weakening) the firm proposal to Juan. `CONFIRM-3` and both instruments stay log-only. Next run: keep seeding held names as they exit; watch whether time-limit-stalled losers keep contributing ~0 (they should — a resting limit is free optionality that only helps live books). **Prior status (2026-08-14): peak-seeking exit sim — a resting +10% sell-limit is the winning mechanism (+55.1% total / +6.1%/name, positive 8 of 9).** Executed the 08-13 next step: built `scripts/peak-seeking-exit-sim.js` (log-only, no orders) to test the alternative the sweep pointed to — a resting sell-limit or trailing stop set at the 04:30 ET exit decision, walked across real premarket SIP 5-min bars, capped at 09:30 ET. Baseline = our actual 04:30 exit; positive = beats selling at 04:30. **Resting sell-limit results (gain vs exit): +5% -> +34.8% total; +10% -> +55.1% total (+6.1%/name), positive on 8/9 (only MGIH -1.0); +15% -> +39.7%; +20% -> +20.2%.** The +10% limit is best AND robust (not one-outlier-driven: even excluding PAVS it is +45.1% over 8). Why +10% beats higher limits: the early peakers (BAOS, BOXL) spike ~+10-16% then crash, so a modest resting limit fills into the first spike and locks it before the dump; a +15-20% limit never fills on those and falls to a deeply negative PM-last (BAOS -25.5%). **Trailing stops are worse and whipsaw** (best +25.8% at 20% width, but negative on BAOS/BOXL/MGIH). **Decisive contrast:** the fixed second pulse captured only +25.0% total (one-outlier-driven); the resting +10% sell-limit captures +55.1% and is positive on 8/9 — a peak-seeking rule, not a second decision time, is the right fix. **Firmed proposal to Juan:** at the 04:30 ET exit decision, instead of a plain market exit for Grade-None/held overnight names, place a resting sell-limit ~+10% above the exit price (GTC through premarket, cancel at 09:30 ET), keeping the 04:30 market exit only as the fallback if unfilled. Changes live exit behavior -> proposed, not applied. Next run: seed 1-2 more held names as they exit to confirm the +10%-limit edge holds out-of-sample. `CONFIRM-3` and both instruments stay log-only.

**Prior status (2026-08-13): CRITICAL refinement — the peak-ceiling gap is mostly UNCAPTURABLE by a naive fixed second exit pulse.** Seeded GXAI (Grade C, sold at the 08-13 04:30 ET exit): exit $1.28 -> PM peak $1.56 at 05:35 ET (+21.9%, 1.8M sh / 7.5k trades, genuine) then faded to PM-last $1.33 (+3.9%). 9/9 seeded held names now show a positive post-exit premarket peak (running peak-ceiling tally +251.1%). **But** built `scripts/premarket-exit-pulse-sweep.js` to test what a *realistic fixed second pulse* would actually capture — price at the bar close of each candidate second-pulse time vs our 04:30 ET exit, summed over all 9 names. **Result: the best fixed time (06:00 ET / 12:00 CET) captures only +25.0% total (~+2.8%/name), and it is dominated by one outlier (PAVS +25.4%); without PAVS it is near zero.** Every other candidate time is worse (05:30 ET +1.1%, 07:00 ET +13.6%). Reason: the early peakers (BAOS -21%, BOXL -1%, GXAI faded, WAFU/MTEN small) DUMP before any reasonable second pulse fires, so a hold-to-a-fixed-later-time rule gives back most of the peak. **Conclusion: the +251% is a peak ceiling, not a capturable edge.** A blind second exit pulse would not reliably beat the 04:30 ET exit; capturing the gap would require a *peak-seeking* mechanism (trailing stop / limit-on-spike set at entry), not a second fixed decision time. **Softened proposal to Juan:** rather than "add a second exit pulse," the better-evidenced ask is a peak-seeking premarket exit (a resting limit or trailing stop above entry) so early spikes are sold into strength; a plain second pulse is not supported by the sweep. Still proposed, not applied (changes live exit behavior). **Prior status (2026-08-12): +229.2% peak ceiling over 8 names (BAOS/BOXL/FF added).** Seeded three names sold at the 08-12 04:31 ET exit: **BAOS** exit $2.24 -> PM peak $2.51 at 04:35 ET (+12.1%) then crashed to PM-last $1.16 (-48%); **BOXL** $5.83 -> $6.80 at 05:05 ET (+16.6%) then faded to $4.52 (-22%); **FF** $6.20 -> $6.43 at 06:30 ET (+3.7%). Bimodal split: early peakers (BAOS 04:35, BOXL 05:05, WAFU 05:05, MTEN 05:40, GXAI 05:35) vs later peakers (FF 06:30, PAVS 06:55, MGIH 07:30, CELZ 08:00). **Prior status (2026-08-11): +196.8% over 5 names (WAFU/MTEN/MGIH added).** Seeded the three Grade-None names sold at the 08-11 10:30 CET (04:31 ET) exit into `premarket-exit-gap.js`: **WAFU** $2.10 -> PM peak $2.30 at 05:05 ET (+9.5%); **MTEN** $1.35 -> $1.45 at 05:40 ET (+7.4%); **MGIH** $2.02 -> a genuine liquid spike to **$2.70 at 07:30 ET (+33.7%)** on 2.9M sh / 23,710 trades (VWAP $2.47), then a crash to $1.61 the next bar. All 5 seeded held names now show a positive premarket peak *after* our 04:31 ET exit (peaks 05:05–08:00 ET, +7.4 to +82.0%), summed **+196.8%**. **Nuance that refines the proposal:** PAVS/CELZ held their gains to PM-last (+39%/+38%), but WAFU/MTEN/MGIH faded hard to PM-last (-21%/-3%/-26%) — so the gap is the *peak* ceiling and its capture is timing-dependent; a naive hold-to-PM-last second pulse would lose on the three new names, but a peak-seeking exit at a second decision point around 06:00–08:00 ET would catch MGIH's 07:30 spike and the PAVS/CELZ 06:55–08:00 peaks. The proposal stands: add a second premarket position-eval pulse (~12:00–14:00 CET / 06:00–08:00 ET). Needs Juan's veto before wiring (changes live exit timing). Next run: keep seeding held names; if a single fixed second-pulse time is chosen, note WAFU/MTEN peaked earlier (05:05/05:40 ET) so one pulse can't catch every peak. **Prior status (2026-08-10): +146.2% over 2 names (PAVS/CELZ).** Built `scripts/premarket-exit-gap.js` + `log/premarket-exit-gap.csv` (log-only). For each held name it pulls SIP 5-min bars, finds the highest premarket HIGH *strictly after* our actual exit fill, and **caps the window at 09:30 ET (13:30Z)** so it never counts regular-session prices we are barred from holding into. Both held names from the execution-gap tally show a large, liquid, *premarket* spike hours after our 10:30 CET (04:31 ET) exit: **PAVS** exit $6.65 -> PM peak **$12.10 at 06:55 ET (+82.0%)**; **CELZ** exit $0.834 -> PM peak **$1.37 at 08:00 ET (+64.3%)**, the $1.37 bar on 6.9M sh / 17,237 trades (VWAP $1.29 — genuine, not a bad print). Summed premarket exit-timing gap = **+146.2%** over 2 names, measured from our actual exit and capped at the open. This corroborates the 08-07 tally (which used entry references and reached over the open) and pins the fixable-in-our-own-process slice at ~+146% across two sessions. **Flag/proposal for Juan (trading-pulse change — proposed, not applied):** the single 10:30 CET exit pulse is far too early for these overnight-AH holds; premarket peaks fired 06:55–08:00 ET (12:55–14:00 CET). Candidate: add a second premarket position-eval pulse around 12:00–14:00 CET (06:00–08:00 ET) so Grade-None holds can catch the later premarket peak instead of exiting at the 04:31 ET floor. Needs Juan's veto before wiring (it changes live exit timing). Next run: seed 1–2 more held names as they occur to confirm the gap persists out-of-sample before/after any pulse change. `CONFIRM-3` stays log-only.

**Prior status (2026-08-05): Second live third-bar outcome set recorded; no 5-minute pulse change justified.** The 2026-08-04 AH session adds five out-of-sample rows: `CONFIRM-3 YES` INLF (+12.2% PM-high from $4.50 confirmation), BJDX (+43.5% from $1.24), BANL (-19.9%), and ZJYL (+0.9%); `NO` TRUG was flat. Combined live `YES` is now n=5: two meaningful PM excursions, one flat result, and two losses. This is not a tradable edge: the positive results are peak ceilings with no spread, INLF had no fillable AH ask, and BJDX had already faded in AH. `CONFIRM-3` remains log-only and cannot affect entry, grading, ranking, or schedules; collect more distinct outcomes. Full table and caveats are in `INIT3_IGNITION_TIMING.md`. Parallel check: Init 6's continuation-gate sample remains n=11, still one short of the n>=12 trigger for its deferred one-minute exit test; the refreshed 5-minute exits remain negative after spread.

**Idea (Juan):** The fixed schedule may have pulses at the wrong moments. Allow
adapting how often and when we scan/evaluate — space some out, simplify or add
others, adapt to market conditions and time zones. Keep cost in mind; don't run
constantly.

**Status:** In progress. **Day-movers pre-seed RETIRED after n=2 live nights with zero entry-lead (2026-07-30).** Night 2 repeated the result: every pre-seed name was NO-SPIKE at 22:15 CET; the 22:30 screener found DCX/CRE/SXTP without an early flag, and the real winner NUWE (+147% PM peak) was outside the pre-seed. DCX's later-replayed 16:03 ignition was absent from its live 16:15 SIP check, exposing data-arrival lag rather than a symbol-source gap. Removed the log-only pre-seed block from `post-market-scan.md`; `scan.py --day-movers` remains available for research and the regular scan. No schedule or trading rule changed. **Next:** replay recent AH-open winners and fades on a 5-minute grid, testing Juan's second/third-bar price-plus-volume confirmation against the current 15-minute cadence on entry price, false positives, and pulse cost. **Parallel Init 5 delivery (2026-07-30):** `chart.py` now caps only strong volume outliers at the nonzero-bar p95, labels the display cap plus true maximum, and marks clipped bars, so regular-open prints no longer flatten the AH/PM volume profile. Verified on ONMD (232 SIP ext-hours bars; display cap 0.5M, true max 14.0M).

**Prior result (2026-07-29):** First live night (07-28) the pre-seed predicted **0 of 4** real AH ignitions (AMIX/YIBO/IOTR/EGG): only EGG was on the watch list and it faded, while AMIX (paper-entered → PM +63% winner 07-29), YIBO, IOTR were pure post-close ignitions with no regular-session footprint. Extended winner census (6 recent ah-detected holdable PM winners) confirms **only 2/6 (STFS, BIYA) are reachable** by a day-movers pre-seed; the other 4 (incl. the biggest, AMIX −1.4% reg) ignite post-close and are blind to it. Decisive: the pre-seed gives **no actionable entry-lead** — it surfaces ~half of winners, and even those are already on the 16:30 ET screener (22:30 CET) a full 30 min before the 23:00 CET entry window opens, so its only edge would be a 22:00–22:15 name the 22:30 screener misses, which did not happen. Kept cheap log-only for 1–2 more nights to confirm zero-lead; if nights 2–3 repeat, trim the pre-seed instruction (Init-3 cost cut, no schedule/rule change). Details appended to `INIT3_IGNITION_TIMING.md`.

**Feedback update (2026-08-28):** Juan on AEMD (that night's winner, AH entry
$3.12 -> PM peak $3.82, +22.4%): *"Aemd could have been entered earlier. 2 or 3
5m bars are enough. We may need to have more pulses?"* This is the **second
live example** of the same entry-latency gap after AMIX (07-29): the current
cadence enters winners several bars after ignition, and Juan reiterates that a
2-3 bar volume+price co-spike is enough confirmation to enter, so denser early
5-minute pulses should let us enter on the confirming bar instead of a later
scan. Reinforces (does not change) the staged next step: the 5-minute-grid
replay of AH-open ignitions measuring entry price / false positives / pulse
cost vs the current grid, then the tighter-early-cadence proposal to Juan.
`spike-bar.js` already fires on the first co-spike bar; the open question is the
entry-timing tradeoff, kept log-only until the replay shows an edge. Pairs with
the 08-27 DAIC feedback (stricter spike gate): combined target is enter fast on
a real 2-3 bar ignition and only on that.

**Feedback update (2026-07-29):** Juan asked whether AMIX could have been bought
on its second or third 5m volume bar and suggested more 5-minute pulses at the
start of AH. AMIX ignited at 16:03 ET, but the whole-market screener did not
surface it until 16:30 ET, after much of the move. Next research step: replay
recent AH-open ignitions using a 5-minute grid and a second/third-bar
price-plus-volume confirmation, then compare entry price, false positives, and
pulse cost against the current 15-minute grid. Keep this log-only until the
replay shows an edge; do not change the live entry schedule from one example.

**Prior: day-movers pre-seed WIRED (2026-07-28, log-only).**
Executed the 07-27 next step: added `--day-movers` to `scripts/scan.py` (the
day% filter now works in *any* session — during after-hours the `change` column
still carries the regular-session day% — sorted by day%, and restricted to
NASDAQ/NYSE/AMEX because a pure day%-sorted list came back **39 of 50 OTC**,
untradable on Alpaca and crowding real names out of the 50-row window). Wired it
into `prompts/post-market-scan.md` as an **early-window pre-seed for the 22:00
and 22:15 CET scans only**: run the watch list, run `spike-bar.js` per name, log
the verdict. No entries, no gates, additive to the screener. Verified live:
`scan.py --day-movers --session afterhours` returns 26 listed hits (was 50 with
39 OTC), the default regular/AH scan paths are unchanged, and `spike-bar.js
BIYA:2026-07-27 --now 17:00` / `CNET:2026-07-27` return clean NO-SPIKE verdicts.
This closes the 07-20 finding that the screener is blind before ~16:30 ET (the
22:00/22:15 scans returned 0 hits), while the 07-27 LGCL counter-example keeps it
labelled structurally incomplete: flat-regular post-close igniters have no
regular-session footprint and still depend on the 16:30 ET screener + tight AH
grid. **Prior: watch-source census extended (2026-07-27, n=7→9):
JEM (+34% reg) confirms the "already a day-mover" path (PM +48% winner, caught),
but LGCL breaks the "both winners caught" claim — it was flat/low-volume in the
regular session (−3.1% close, 78.6k reg-session sh) yet ran PM +114%, the biggest
recent winner, with no regular-session footprint to pre-seed on. Conclusion: wire
the day-movers list as an *additive* log-only pre-seed (rescues already-moving
names 15–30 min ahead of the 16:30 ET screener) but it is structurally
incomplete — flat-regular post-close igniters still need the screener + tight AH
grid. Not a substitute.** **Prior: watch-list source tested (2026-07-22); spike-bar
column live-validated on the first wired AH session (2026-07-20); two
decision-relevant findings + a proposal to Juan.**

**Update (2026-07-22) — watch-list source test (pilot step b).** The 07-20
finding that the screener is blind before ~16:30 ET means the only way to shrink
open-window catch-lag is to run the SIP spike-bar check on a **pre-seeded watch
list** at 22:00/22:15 CET. Tested the obvious source — scan.py's regular-session
day-movers (`MIN_DAY_CHANGE_REGULAR=15`) — against 7 recent AH igniters using
Alpaca daily (regular-session) bars: **3/7 clear the threshold, but both traded
WINNERS (HIHO +19.2% reg, CJMB +16.2% reg) are caught and the misses skew to
faders/losers (PAPL −23.6%, KUST dead-cat, AEHL fade).** The AH→PM continuations
we make money on were already +16–19% in the regular session before their AH
ignition, so a 16:00 ET day-movers list surfaces them and lets the SIP check
catch the ignition bar 15–30 min ahead of the screener. It can't help a
flat-regular post-close-news igniter (PAPL) — those depend on the external
~16:30 ET screener population. Full table in `INIT3_IGNITION_TIMING.md`. **Next:
wire scan.py `--day-movers` as the 22:00/22:15 watch source, run spike-bar.js on
each (log-only), and measure whether the "winners are already day-movers"
pattern holds over more sessions before any entry use.** The 07-21 session added
no late-window igniter (winner SXTC was a PM-only gapper; AEHL/KUST faded and
were correctly gate-blocked), so proposal (C)'s late-window tally holds at 2 — 
held one more session. On
Mon 07-20 the wired 22:15/22:45 CET scans and the spike-bar column fired live for
the first time (`log/2026-07-20/log.md`). **(1) Column validated end-to-end** on 6
real names: HIHO/SHPH SPIKE 16:04, PAPL SPIKE 17:09, ADVB SPIKE 17:32, RDGT SPIKE
18:00, and **GORO NO-SPIKE = correct skip** (AH +240% on 17K sh / 160M float = bad
print). But SPIKE ≠ winner (PAPL, ADVB fired SPIKE then faded) — continuation
gating still required. **(2) The screener feed is BLIND before ~16:30 ET:** the
22:00/22:15 scans returned **0 screener hits** (TradingView postmarket field
doesn't populate until ~16:30 ET), so the open-hour densification adds nothing via
the screener — only the SIP cross-check (feed-lag rescue) reached the early window
and flagged ADVB at 22:15. HIHO ignited 16:04 but the screener didn't surface it
until 22:30 (~26 min lag); cost no entry (entry banned before 23:00 CET). Next
step: make the 22:00/22:15 scans run the SIP spike-bar check on the regular-session
watch list by default (the screener won't help there). **(3) Late-window (17:00–
18:30 ET) densification case strengthened → PROPOSED to Juan:** RDGT ignited 18:00
ET but first appeared at the 18:30 final scan (2-AH-scan gate un-meetable) and ran
to PM +47%; an 18:15 ET scan (00:15 CET) would have made it entry-eligible. Joins
CJMB (07-16, traded winner +19.8%, caught +27m late). Late-window support tally =
**2** (low end of the 2–3 trigger). **Proposal (C): add 23:45 + 00:15 CET (17:45 +
18:15 ET) entry-eligible scans to 15-min-space the late window** — these change
live entry behavior (after the 23:00 ban), so **Juan veto window; not applied.**
Details in `INIT3_IGNITION_TIMING.md` (first-live-session section). **Prior:
out-of-sample detector validation (2026-07-20 3 names); AH-open scans wired
(2026-07-17) + spike-bar detector built & wired as a log-only scan column
(2026-07-17, 2nd step).**
Proposal (A) was applied: added crons `trading-post-market-2215` and
`trading-post-market-2245` (16:15/16:45 ET, Mon–Thu) to `scheduler.json`. Both
fire *before* the 23:00 CET entry ban, so they are log/observation-only (no new
entry window) — fine to apply directly. The AH-open hour is now 15-min-spaced:
22:00, 22:15, 22:30, 22:45, 23:00 CET, halving catch-lag on the dominant
16:08–16:53 ET ignition cluster. **Spike-bar detector now built:**
`scripts/spike-bar.js` (log-only, no orders) is the live counterpart of
`ignition-timing.js` — for a candidate + AH-eve date + `--now HH:MM` ET cutoff it
reports whether the first price+volume co-spike (ignition) bar has fired yet
(`SPIKE 16:53ET +19% $1.48 72 trades / 25k sh`) or not (`NO-SPIKE flat/faded`),
directly answering Juan's "catch the first volume spike bar" ask. Verified
consistent with the audit on IVF (16:53), TGHL (16:21), XCUR (16:08), and reads
NO-SPIKE on LVLU (Juan's "no volume spike" example) and on IVF as-of 16:30 (pre-
ignition). Wired into `prompts/post-market-scan.md` as a **log-only column** (run
per >10% candidate, record the verdict; no entry gate yet) so the tighter grid
accumulates live ignition-bar timing. (B) tail scans still held (MSW=1, below
3–4 trigger). The daily **`strategy-advance`
pulse** (2026-06-23) was the first deliverable. Built
`scripts/ignition-timing.js` (log-only) and ran it on 10 AH winners' 1-min SIP
bars (`INIT3_IGNITION_TIMING.md`). **Key finding: the grid is too coarse, not
mis-phased.** 9 of 10 winners ignite *inside* the grid window, but the 30-min
spacing means the first scan sees the move **7–29 min after ignition (median
~+18m)**, already partway up. Two gaps: (1) the **AH-open cluster** — 6 of 10
ignite 16:08–16:53 ET and wait up to +22m for the 16:30/17:00 scan; (2) a
**tail** past the 18:30 ET grid end — MSW ignited 19:01 ET and the grid never
sees it live. **Proposed to Juan (touches trading-scan timing — veto, don't
apply silently):** (A) add 22:15 + 22:45 CET (16:15/16:45 ET) *observation*
scans to 15-min-space the open hour (halves catch-lag on the dominant cluster);
(B) add 01:00/01:30 CET (19:00/19:30 ET) tail scans (Juan pre-authorized; tail
count now MSW=1, below the 3–4 trigger). Entry is still banned before 17:00 ET,
so (A) scans catch+log the ignition to feed a faster 17:00 ET decision —
exactly the enabler for Juan's 2026-07-16 "catch the first volume spike bar"
ask, whose blocker is this detection latency.

**Current schedule (cron, Europe/Berlin local time):**
**Update 2026-09-18 (strategy-advance) — Init 6 pilot rechecked; Init 3 exit-gap seed completed; opening-grid evidence remains insufficient.** The 2026-09-18 PM-open tracker added SSM, DLXY, TCRT, CPOP, BTCT, BNC, USDE, and YCBD, but the three `footprint=none` rows were `thin`, so no new holdable PM-only case entered the pilot. Re-running `init6-pm-pilot.js` leaves the active pilot at **n=21, SUM +77.5%, mean +3.7%/name, positive 16/21, fade-tail 4/21 (19%)**; this is insufficient new pilot data, not a failure. The complete Sep 17 SIP window reconciled DTSS and YFOR: DTSS's capped post-exit peak was $1.18 and YFOR's was $1.876; the conflicting YFOR $2.25 position-evaluation mark was excluded. Adding both seeds takes the Init 3 peak-seeking sim to **n=43; plain +10% limit SUM +101.9%, mean +2.4%/name, positive 27/43**. The first complete five-minute opening-grid session ran all 13 scans, but 22:05/22:10/22:15 returned no candidates; the first actionable names appeared at 22:20 and 22:30, so no lag reduction is proven after one session. Both changes remain log-only; no entry, exit, or existing trading-pulse rule changed. **Next:** collect more opening-grid sessions, measure first observation against SIP ignition, and keep seeding the Init 6 pilot. Init 6 remains the serialized active pilot; Init 3 remains low-risk instrumentation.

**Update 2026-09-18 18:00 (strategy-advance) — opening-grid replay adds one insufficient data point.** Re-ran the active Init 6 pilot with no new holdable PM-only admit: **n=21, SUM +77.5%, mean +3.7%/name, positive 16/21, fade-tail 4/21 (19%)**. In parallel, replayed the Sep 17 AH candidates through the log-only second/third-bar confirmation test: **SSM was the only 2-bar admit (1/8), with +27.5% to PM open and +4.6% entry-price improvement versus the current legal grid; no candidate passed the 3-bar test**. The single admitted case is not enough to justify a schedule or entry-rule change; keep collecting sessions and measure ignition-to-first-observation lag. No live rules, orders, or schedules changed.

**Update 2026-09-17 (strategy-advance) — active Init 6 pilot rechecked; Init 3 opening cadence densified in log-only mode.** The 09-17 PM-open scan added DAIC, KXIN, and RETO as `ah-detected`, so no new `footprint=none` candidate entered the Init 6 universe. Re-ran `init6-pm-pilot.js` over 48 candidates; the deterministic ledger remains **n=21, SUM +77.5%, mean +3.7%/name, positive 16/21, fade-tail 4/21 (19%)**. This is insufficient new pilot sample, not a failure. For Init 3, added four new observation pulses at 22:05, 22:10, 22:20, and 22:25 CET (16:05, 16:10, 16:20, and 16:25 ET), completing five-minute coverage through the first 30 minutes of after-hours without retiming an existing pulse; these run before the 23:00 CET entry window and place no orders. A fresh nine-name 2026-09-16 `ah-5m-confirmation.js` check returned 2 YES and 7 NO (DAIC 17:30 ET at 724.8x; YFOR 17:15 ET at 4.2x), which is instrumentation rather than promotion evidence. Cost is +4 observation rounds/day; next measure ignition-to-scan lag, first-2/3-bar capture, and false positives.

- Post-market scans: 21:30, 22:00, 22:05, 22:10, **22:15**, 22:20, 22:25, 22:30, **22:45**, 23:00, 23:30, 00:00, 00:30 (13 scans; 22:05/22:10/22:20/22:25 added 2026-09-17 as observation-only; 22:15/22:45 added 2026-07-17, observation-only)
- Morning eval: 10:20 | Position evals: 10:30, 14:30
- Daily email: 11:30 | Scanner improvement: 14:20 | Process review: 14:40

**Observations to test:**
- The 21:30 and 22:00 scans rarely produce entries (entries banned before
  23:00). They may be reducible to one observation scan, saving rounds.
- Premarket peaks happen ~04:00-04:15 ET (10:00-10:15 CET) but the first
  position eval is 10:30 CET — we may be a touch late on exits. A 10:00 CET
  pulse could catch PM peaks closer to the top.
- DST and US-holiday handling: scans should follow NYSE hours.

**Rollout plan:**
1. Audit which pulses produced actionable output over the last ~4 weeks
   (entries, exits, or material observations) vs ran empty.
2. Propose a trimmed/retimed schedule with a cost estimate (rounds/day).
3. Change crons one at a time; watch for missed detections/exits.

**Needs from Juan:** approval of any schedule change before applying (the agent
can edit its own crons but should confirm timing changes here first).
- **Veto window (2026-07-21) — proposal (C):** add 23:45 + 00:15 CET (17:45 +
  18:15 ET) *entry-eligible* scans to 15-min-space the late window. Evidence:
  CJMB + RDGT under-caught by the 30-min late spacing. Silence = wire a future
  run; say the word to veto.
- **Pre-authorized (2026-06-24):** Juan approved adding the 1-2 late
  post-market scans (~01:00/01:30 CET) that the late-AH-tail tracker is building
  a case for ("apply the scheduler changes if you need to"). Apply when the
  tracker's evidence warrants (>=3-4 winners clustering in the 18:30-20:00 ET
  tail); tally is at 1 (ORIS) as of Jun 24, so not yet applied.

---

## Initiative 4 — Email identity + reply-driven feedback loop

**Idea (Juan):** Send the daily email as **zero** (via InboxKit) instead of from
Juan's Gmail. Add a pulse that checks for replies to those emails; replies are
the channel for Juan's feedback to feed back into the system.

**Status:** DONE (initial setup) — iterating. Jev results/cost reporting added 2026-10-02; the next daily email will verify delivery alongside initiative progress reporting.

**Progress 2026-10-02 (Juan's October 1 reply):** `prompts/daily-email.md` now always reads the Initiative 7 Jev artifacts and includes Jev Results and Costs, covering completed results, call/token usage, measured or labeled estimated costs, and explicit not-run/failure/unavailable status. The classifier research and implementation are routed to Initiative 7. Verify the required section in the next successful email; scanner-improvement/process-review should check the artifacts behind its claims. See `FEEDBACK_LOG.md` 2026-10-02, InboxKit message 177.

**Progress 2026-10-01 (Juan's Sep 30 reply):** Updated `prompts/daily-email.md` to read the initiative log and roadmap and report every initiative that moved since the previous successful email, with the completed step, result, date, and next step. Recorded this delivery in `INITIATIVE_LOG.md`. See `FEEDBACK_LOG.md` 2026-10-01, InboxKit message 175.

**Cross-initiative directive:** Juan requires initiatives to move. `strategy-advance` now checks the last concrete progress and next deliverable for every active initiative, prioritizes work that has waited longest among comparable unblocked items, and must produce new evidence, resolve an open question, or deliver a verified change each run. An unchanged rerun is a monitoring result. When the pilot has no new data, advance another ready research, instrumentation, or build item. Record the exact dependency and next check for blocked work; Initiative 2's broker test remains deferred per Juan's Sep 22 instruction. `process-review` now checks for repeated runs without concrete progress and for missing initiative updates in the daily email.

**What is set up:**
- `scripts/send-email-inboxkit.js` — sends as `zero@inboxkit.cc` via InboxKit
  (key read from zero's `.envrc`).
- `prompts/daily-email.md` updated to use it.
- `prompts/check-email-replies.md` + a daily cron poll InboxKit for unread
  replies, extract feedback, append it to `FEEDBACK_LOG.md`, and mark read.

**Needs from Juan:** just reply to the daily emails with feedback. Anything
requiring action (keys, decisions) will be listed in the email and here.

---

## Initiative 6 — Catch the rare extreme runners (+300-600%)

**Status / progress 2026-09-30 18:00 CEST: ACTIVE serialized pilot, log-only.** Completed-window rerun of `scripts/init6-pm-pilot.js` found no Sep 30 PM-only tracker case; NCI, KALA, BIYA, and WETO all had AH footprints. The completed holdable ledger remains **26 modeled admits / +115.2% total / +4.4% gross per admit / 20 positive**, approximately +2.4% after an assumed 2% spread; all retrospective classes remain 35 admits / +3.4% gross. The 04:10 prospective cohort captured 19 names before the entry window, but today's selected tracker has zero PM-only names, so pilot discovery and executable returns remain untested. Next: compare the first prospectively captured PM-only candidate with the frozen universe, gate, and fresh executable book; keep hypothetical returns out of live decisions. At the October 1 checkpoint, if account equity is still negative, open Juan's requested alternative-strategy research and pivot proposal. No live order, rule, or schedule changed.

**Parallel Initiative 3 research, 2026-09-30 18:00:** Saved Pi sessions show the Sep 29 22:30 CEST scan completed, then the 22:45, 23:00, 23:30, 00:00, and 00:30 jobs each started and ended in about one second with `Your authentication token has been invalidated. Please try signing in again.` All four entry scans were lost to this provider authentication interruption; the Sep 30 15:00 session completed, so the failure was transient. This Sep 29 loss does **not** test whether removing four opening observation scans would preserve coverage; the Sep 22 usage-limit failure remains separate evidence for that pending veto proposal. At the next AH entry window, verify session completion and auth status before attributing missing names to timing or strategy. Restoring entry-window execution has greater near-term dollar potential than optimizing a ~€2.40 modeled PM-only admit, but the missed KALA opportunity remains hypothetical and its book was stale. The consolidated asks below are unchanged.


**Status / progress 2026-09-30 15:00 CEST: ACTIVE serialized pilot, log-only; executable edge still unproven.** The first prospective cohort file was written at 04:10:40 ET, before the earliest possible 04:15 R+3 entry. A repeatable read-only audit (`scripts/init6-cohort-audit.py`) compared its 19 frozen TradingView names against the four gappers later selected for the PM tracker: **0/4 overlap** (NCI, KALA, BIYA, WETO absent). All four have verified AH footprints; the tracker has **zero PM-only cases today**, so this does not measure PM-only pilot recall or add a pilot return. The tracker selects gappers after observation and does not label every cohort name, so the other 19 cannot be counted as rejects. Of 19 IEX quotes, 14 were labeled two-sided, but every quote was **40,255–43,839 seconds old** and **zero** had an ask with positive size aged <=60 seconds; neither a displayed two-sided book nor a SIP high proves an executable fill. Next: at the 18:00 run, recheck the completed Sep 30 window and preserve the 26-row completed holdable ledger if no PM-only admit appears; compare the next genuinely PM-only prospective candidate against the frozen cohort, including late ignition and quote freshness. No entry/order/schedule changed. Paper equity remains **$99,721.90 (-$278.10)**; the ~October 1 pivot checkpoint is tomorrow.

**Parallel Initiative 3 research, 2026-09-30:** The Sep 29 daily log records **3/7 core AH scans** and no 23:00–00:30 entry scans; four of the last ten completed sessions had incomplete core coverage. KALA surged inside the missing entry window, with a theoretical $0.62→$0.80 PM peak (+29.0%) but no verified fillable ask. Restoring eligible entry-window coverage has a higher immediate expected-dollar opportunity than optimizing the small, hindsight-conditioned PM-only pilot, though no executable gain is established. The four-observation-scan retirement proposal remains pending Juan's veto via daily email; yesterday's missed sessions have no confirmed root cause, so no trading scan timing was changed. Initiative 2's broker-access test remains deferred at Juan's request; the existing premarket-exit review remains open.


**Status / progress 2026-09-29 18:00 CEST: ACTIVE serialized pilot, log-only; not promotion-ready.** Completed-window SIP rerun adds BKYI, with modeled $3.03 entry at 04:15 ET and a +10% high touch, to the hindsight-`holdable` ledger: **26 admits, +115.2% total / +4.4% gross per admit / 20 positive**, approximately +2.4% after an assumed 2% spread. All retrospective classes have **35 admits, +3.4% gross per admit**. The prior step's prospective-cohort hypothesis remains **insufficient data**: no Sep 29 CSV or 10:10 Berlin cohort session exists, so BKYI has no frozen discovery or contemporaneous quote evidence. The bridge loads scheduler jobs at startup; its current process started at 15:04 today, after the missed window. Added three persistent, log-only 09:10 Berlin shadow snapshot jobs for the March/October/November DST mismatch dates; the ET guard permits only 04:07–04:14 ET on weekdays and prevents duplicate files. These new jobs require the next bridge restart to become active; the existing 10:10 job was present before today's 15:04 startup and is due Sep 30. Next: verify a Sep 30 cohort file was written before the first modeled entry, compare its complete frozen set with the later tracker (including rejects and late igniters), and inspect quote age. Verify new mismatch jobs are loaded before October 25. Neither OHLC touches nor IEX quotes prove fills. At ~€100 per trade, +2.4% modeled net is only ~€2.40 per admit; paper equity is still $99,721.90 (-$278.10), so this cannot close the deficit by October 1 at current frequency. Reassess other core strategies at the deadline if equity stays negative. **Parallel Initiative 3 instrumentation:** DST observation coverage, no trading scan/evaluation timing or live rule changed. Initiative 2 broker access remains deferred at Juan's request; standing schedule veto and exit review remain open.


**Status / progress 2026-09-28 18:00 CEST: ACTIVE serialized pilot, log-only; not promotion-ready.** Completed-window rerun added WBUY (modeled $0.96 at 05:10 ET, +10% limit high touched) and SDEV (modeled $1.75 at 04:15 ET, limit unfilled, -2.29% to PM-last). The hindsight-`holdable` ledger is now **25 admits / +105.2% total / +4.2% gross per admit / 19 positive**, approximately +2.2% per admit after an assumed 2% spread; all retrospective classes have **34 admits / +3.2% gross per admit**. Neither estimate verifies a buy at the R+3 open or a sell at the high-touch limit. The 04:10 prospective cohort job was installed after today's PM window; no 2026-09-28 cohort exists, so today's names cannot validate discovery or quote freshness. Next aligned weekday, verify the file is captured before entry, compare its full frozen candidate set with the later tracker and gate, and record late discoveries such as WBUY (04:30 ignition), rejects, and stale quotes. The existing 10:10 Berlin cron needs ET alignment during the Europe/US DST mismatch weeks; its ET guard will skip rather than manufacture a cohort. At ~€100 learning size, even the **modeled** 2.2% net is ~€2.20 per admitted trade; the pilot has only 25 hindsight-selected admits since mid-July, so it cannot plausibly erase the account's $278.10 paper deficit by the October 1 checkpoint at current size and frequency. Do not scale without executable evidence. Parallel Initiative 3 research replayed five Sep 25 AH/PM names: the second-bar test admitted none; the third-bar test admitted only CLRO at 19:30 ET, after the 18:30 entry grid (PM open +5.9%, PM high +48.7% from a modeled $4.91), with no executable current-grid comparison. No live timing change follows. Initiative 2 broker access is deferred at Juan's request; the four-scan retirement veto and Initiative 3 exit review remain open. No trading pulse or live rule changed.


**Progress 2026-09-28 15:00 CEST — ACTIVE serialized pilot, log-only.** The 11:00 PM scan found two fresh `footprint=none` holdables, WBUY and SDEV. A **provisional** 09:00 ET rerun of `init6-pm-pilot.js` admits both: WBUY's modeled $0.96 entry at 05:10 ET touched its +10% limit; SDEV's $1.75 entry at 04:15 ET had not touched the limit and was -1.7% at the then-available last bar. Neither row is final before 09:30 ET; the committed 23-row ledger remains the completed-session baseline until the 18:00 rerun. The preceding 32-admission liquidity audit did not identify a causal investability rule. Added `init6-cohort-snapshot.py` and one log-only 10:10 Berlin observation pulse: on future aligned weekdays it freezes the TradingView top-50 PM-volume discovery set at 04:10 ET with IEX bid/ask, timestamp, and quote age before the earliest R+3 hypothetical entry. A 09:03 ET dry run found 17 names and 14 two-sided IEX quotes without writing a hindsight cohort. The next run should finalize WBUY/SDEV, then use the first actual 04:10 snapshot to measure misses, later gate accepts/rejects, and quote age; late igniters, top-50/50K discovery filters, SIP publication delay, stale IEX quotes, and hypothetical limit touches still limit the executable-edge claim. The paper account is flat at $99,721.90 (-$278.10). No existing trading scan/evaluation pulse was retimed; Initiative 2 remains deferred for Juan's broker access. The proposed retirement of four existing AH scans stays pending Juan's veto. No demonstrated higher executable dollars-per-time setup has displaced this pilot; the October 1 pivot checkpoint remains in force.


**Current status (2026-09-25 18:00 CEST): ACTIVE serialized pilot, log-only; not promotion-ready.** The completed Sep 25 PM window adds no admitted candidate: SDEV was PM-only but thin and fails the continuation gate; the other four tracked names were AH-detected. The holdable ledger remains **23 entries, +4.2% gross/name (+2.2% after assumed 2% spread), 18/23 positive**, versus the current PM-only live baseline of zero trades. An all-classification audit (`log/init6-preentry-liquidity.csv`) records the minimum trade count and dollar volume of the two completed confirmation bars **before** each hypothetical R+3 entry, across 32 admitted names. These metrics do not reproduce the hindsight `holdable` label: a >=1,000-trade minimum retains all **3 uninvestable** admits and 1/6 thin admits while excluding 5/23 holdable admits; it returns +3.19% gross/name on 22 admits versus +3.11% on the 10 it excludes. This is an in-sample diagnostic, **not** a tested selection rule. The modeled highs are not verified sell fills and historical executable quotes are unavailable; the tracker itself is assembled after PM observation. Next: log a prospective, pre-entry PM-only candidate cohort and available quotes, then compare executed/quoted fillability and returns without retrospective universe or class filters. The live paper account remains $99,721.90 (-$278.10) and flat, so the October 1 pivot checkpoint still matters. No competing core strategy has a better demonstrated executable $/time edge; no orders or schedule/rule changes were made. Parallel Initiative 3 research replayed eight Sep 24 AH names against full Sep 25 PM bars: second-bar confirmation admitted none; third-bar admitted INLF, NCPL, and FTHM, with only +1.3% mean entry-price advantage versus the current grid. These are modeled entries and PM-high ceilings, not fillable returns; keep log-only. Initiative 2 remains deferred pending Juan's broker access, and the four-scan retirement proposal is still pending his veto.


**Progress update (2026-09-24, 15:00 CEST):** Re-ran `scripts/init6-pm-pilot.js` over 50 tracked candidates. Sep 24's GCTK and WETO rows were AH-detected, while SPHL was uninvestable; no new PM-only holdable entered. The log-only pilot remains **n=23, SUM +97.5%, mean +4.2%/name, median +10.0%, positive 18/23, fade-tail 4/23 (17%)**, or estimated **+2.2%/name after ~2% spread**, against the live-cycle baseline of 0%. This is hypothetical, not a live edge; keep the pilot active and do not promote it. Paper equity remains **$99,721.90 (-$278.10)** with no open positions. No new evidence identifies a faster competing core strategy.

**Parallel Initiative 3 research (2026-09-24):** Replayed seven Sep 23 AH candidates against Sep 24 PM bars available through 09:02 ET. The **2-bar test admitted 2/7**: GCTK showed +20.6% to PM first-bar open / +62.4% observed PM high from the hypothetical $3.11 entry versus the $4.32 current-grid entry; WETO showed +24.9% / +39.9% from $1.93 versus grid $1.90. The **3-bar test admitted 3/7**, adding NCPL, which returned -20.8% to PM open and only +4.0% to the observed PM high. Mean entry-price advantage was +13.2% for 2-bar and +1.9% for 3-bar; this is a small, outlier-sensitive sample and the 09:02 ET PM window was incomplete. Re-run after 09:30 ET before judging; no cadence, gate, or live-entry change is justified. The prior full-window +5%/+10% exit comparison remains inconclusive at n=44 (both +3.0% mean; 2.6-point total difference).

**Parallel Initiative 5 delivery (2026-09-24):** Generated `reports/2026-09-23/index.html` with three charts, passed local link checks, and published it through Pages run **36003309053**. The report, report index, and all three chart assets returned HTTP 200. No live order, trading rule, or scan/evaluation time changed. The four-pulse retirement proposal remains pending Juan's veto; the Init 2 broker test and Init 3 exit proposal remain open asks.

**Idea (Juan, 2026-06-23):** For weeks the daily winner has been a +20-100%
AH->PM mover. Juan wants the system to also catch the rare +600% explosions
("600% and others like that"), not just the moderate movers.

**Status:** **RE-OPENED — ACTIVE (2026-07-23, Juan directive). Mechanical-exit
sim run (2026-07-24) — NEGATIVE at 5-min cadence: no causal exit converts the
gate-admitted set to positive expectancy after spread.** The +31% PMHigh ceiling
is an outlier mirage (INLF +96%; median only +11%) and prints *intrabar*, so a
5-min close-based exit can't capture it. Every trailing-stop / N-bar /
first-lower-high rule lands near-breakeven mean, negative median, 1-3/7 wins,
below the ~1-3% spread. **No live PM-gapper scalp pulse proposed.** The gate is a
good wick *filter* but not a tradable edge at this cadence; the only untested
angle is a 1-min exit (the peak is intrabar), deferred until the admitted sample
grows to >= ~12 so it doesn't hinge on one INLF. Problem (a) stays log-only
accumulation. Next: keep `pm-open-scan` growing n; build the 1-min exit test at
n>=12.

**Current status (2026-09-25 15:00 CEST):** **ACTIVE serialized pilot; log-only, not promotion-ready.** Re-ran `scripts/init6-pm-pilot.js` on the 50 holdable candidates: Sep 25 INLF/GLND/FTHM were AH-detected, IFBD thin/AH-detected, and SDEV PM-only but classified thin after the 04:45 ET observation window. No fresh holdable PM-only candidate entered. The holdable ledger remains **n=23, SUM +97.5%, mean +4.2% gross/name, positive 18/23, fade-tail 4/23 (17%)**, or **+2.2%/name after an assumed 2% spread**. Added a log-only sensitivity tally for the **post-session `holdable` label**: across completed PM windows the same gate admits 6 thin names (mean +5.8%) and 3 uninvestable names (mean -10.4%); all 32 admitted names return **+3.2% gross / +1.2% after assumed spread**, before actual fillability. This is not a realizable estimate: thin/uninvestable labels use later session data, OHLC high-touch does not prove limit fills, and the IEX paper account cannot fill some names. The classification-conditioned +2.2% estimate cannot be promoted as a causal live edge. **Next:** wait for Sep 25's completed 09:30 ET window and rerun the pilot/sensitivity; define a pre-entry liquidity/investability test from available bars and quotes, then compare it with these hindsight labels before proposing any live PM entry. The account remains net-negative at the last observed $99,721.90; broker access remains deferred at Juan's request. No higher-proven $/time core setup has appeared, but the classification bias is a direct threat to Initiative 6's claimed edge. No order, rule, or existing trading-pulse time changed.

**Prior status (2026-09-24 18:00 CEST):** **ACTIVE serialized pilot; log-only.** Re-ran `scripts/init6-pm-pilot.js` over 50 candidates: Sep 24 GCTK and WETO remain AH-detected; SPHL is uninvestable; no fresh PM-only holdable entered. The ledger remains **n=23, SUM +97.5%, mean +4.2%/name, median +10.0%, positive 18/23, fade-tail 4/23 (17%)**; estimated **+2.2%/name net of ~2% spread** remains hypothetical against the live-cycle baseline of 0%. Paper equity is **$99,721.90 (-$278.10)** and the account is flat. No current evidence identifies a higher-expected-dollar-per-time core-strategy lever; the pilot remains the lead empirical experiment but is not ready for promotion.

**Progress update (2026-09-24 18:00 CEST) — Initiative 3 full-window replay:** Replayed seven Sep 23 AH candidates against Sep 24 PM SIP bars through 09:25 ET. The 2-bar test remains **2/7** (GCTK, WETO); its +13.2% mean entry-price advantage is GCTK-driven—excluding GCTK, WETO's $1.93 entry is **1.6% worse** than the $1.90 current-grid entry. The 3-bar test remains **3/7**, adding NCPL: its $1.49 hypothetical entry was **-20.8% to PM open** but saw a **+43.6% PM-high excursion**. That excursion is not an exit-fill result, and one session does not establish a repeatable edge. Keep both timing tests log-only; no cadence, gate, or live-entry change is justified.

**Prior status (2026-09-23):** Re-ran `scripts/init6-pm-pilot.js` over 50 tracked candidates after the Sep 23 PM-open scan. WHLR and IPDN were AH-detected and SQFT was thin, so no fresh PM-only holdable entered; the pilot stays **n=23, SUM +97.5%, mean +4.2%/name, median +10.0%, positive 18/23, fade-tail 4/23 (17%)**. Full-window PM-last mean is **-7.3%**, giving estimated **+2.2%/name after ~2% spread**; this remains hypothetical, not live-account edge. **Parallel Initiative 3 research (2026-09-23):** replayed six Sep 22 AH candidates against Sep 23 PM SIP bars. Second- and third-bar tests each admitted SQFT (fade) and DCOY (winner), while rejecting WHLR, IPDN, BFRG, and HAO. Early-entry price edge versus the current legal grid averaged **-4.6% (2-bar)** and **-10.8% (3-bar)**; one session does not support a cadence or hard-gate change. The Sep 22 daily log records only **2/7 core scheduled AH scans**. Session traces identify the cause: the 22:25 CET scan made nine assistant tool calls and then failed with `Codex error: The usage limit has been reached`; the 22:30, 22:45, 23:00, 23:30, 00:00, and 00:30 sessions failed immediately with the same error. All jobs were present in `scheduler.json`, so this is quota exhaustion, not missing crons. **Proposed to Juan for veto:** retire the four added five-minute observation pulses at 22:05, 22:10, 22:20, and 22:25 CET (four fewer sessions per evening), retain 22:00/22:15/22:30/22:45 and every 23:00-00:30 scan; this restores 15-minute opening coverage and protects later entry scans. No schedule change has been applied. **Money-fast check:** paper equity is **$99,721.90 (-$278.10 vs $100,000)** after TOPS realized -$44.80; coverage completion is the more immediate unblocked lever than denser cadence; Init 6 is the active PM-only entry pilot, while Init 3's positive +10% result is a separate proposed exit mechanism. **Parallel Initiative 5 build (2026-09-23):** generated `reports/2026-09-22/index.html` with both TOPS and WHLR charts; Python compilation passed, both relative chart links resolve locally, and the deployed report plus both chart URLs returned HTTP 200 (Pages run 35866528073 succeeded). No live order, rule, or existing scan timing changed. Juan's 2026-09-23 reply, “You need to leave before open,” reaffirms the existing premarket-exit/no-hold-through-open boundary; TOPS exited at 04:31 ET and no positions remain. No policy change is needed. Standing asks remain the Init 2 broker test access and Juan's review of the Init 3 +10% exit proposal; the new scan-resource veto proposal is listed under Open asks for Juan.

**Prior status (2026-09-22):** **ACTIVE serialized pilot; log-only.** Re-ran `scripts/init6-pm-pilot.js` after the 2026-09-22 PM-open scan. Two fresh `footprint=none` holdables, STI and GURE, passed the continuation gate and filled the hypothetical +10% limit; the ledger is now **n=23, SUM +97.5%, mean +4.2%/name, median +10.0%, positive 18/23, fade-tail 4/23 (17%)**, versus a PM-last mean of **-7.6%**. **Parallel Initiative 3 progress (2026-09-22):** replayed the complete 2026-09-21 AH set through `scripts/ah-5m-confirmation-replay.js`; QNME was the only 2-bar and 3-bar admit (second-bar entry +18.6% to PM open / +104.7% to PM high; third-bar +29.1% / +122.8% versus the current-grid entry), while GRML and GDC rejected, STI had no AH ignition, and GURE had only two AH bars. One of five cases is insufficient to change the schedule or hard gate. **Parallel Initiative 5 progress (2026-09-22):** generated and verified `reports/2026-09-21/index.html` with one chart and updated the report index; `python3 -m py_compile scripts/generate-html-report.py` passed. All work stayed log-only; no live rule, order, or existing trading-pulse timing changed.

**Prior status (2026-09-21):** **ACTIVE serialized pilot; log-only.** Re-ran `scripts/init6-pm-pilot.js` after the 2026-09-21 PM-open scan. GLND, GRML, and LOBO were AH-detected holdables; AVAT and SUIG were thin PM-only rows, so no new PM-only candidate entered the pilot. The ledger remains **n=21, SUM +77.5%, mean +3.7%/name, positive 16/21, fade-tail 4/21 (19%)**. **Progress note (2026-09-21 18:00 CEST):** the second same-day rerun found no new market session or holdable PM-only candidate; Initiative 5's dependency-free `scripts/generate-html-report.py` prototype generated and verified `reports/2026-09-18/index.html` plus the report index.

**Parallel Initiative 3 research (2026-09-21):** Replayed the complete 2026-09-18 AH session through `scripts/ah-5m-confirmation-replay.js`. The second-bar test admitted 3/5 (GLND, GRML, LOBO); the third-bar test admitted 2/5 (GLND, LOBO). GLND's second-bar entry reached +82.3% at PM open and +126.8% at PM high; GRML reached +45.5% at PM open and +153.9% at PM high but failed the third-bar test; LOBO was a false-positive at -9.2%/-14.8% to PM open. AVAT and SUIG had no qualifying local-volume ignition. This mixed one-session result is insufficient to change the schedule or hard gate. All work stayed log-only; no orders, live rules, or schedules changed.

**Update 2026-07-24 (strategy-advance) — mechanical-exit sim, problem (a)
NEGATIVE at 5-min cadence.** Built `scripts/pm-gapper-exit-sim.js` (log-only):
reuses the continuation gate for entry, then walks PM 5-min bars applying causal
close-based exits (trailing 8/12/15/20%, N-bars 1/2/3, first-lower-high). On the
now-n=7 admitted set: PMHigh ceiling mean +31.1% / **median only +11.0%** (INLF
+96% outlier), but every mechanical exit is near-breakeven mean, **negative
median, 1-3/7 wins** (best mean N1 +8.8% is entirely INLF; median -1.1%). None
clears the ~1-3% micro-cap PM spread or reliably beats the flat PM-last floor.
Root cause: the peak prints *inside the entry bar* (INLF 08:15Z open $3.76 ->
$7.19 high) so a 5-min close-based exit can't sell it. Also a gate false-positive
(WLDS, classified uninvestable, admitted and loses on every exit). **Conclusion:
do not propose a live PM-gapper scalp pulse; the gate filters wicks but yields no
tradable edge at 5-min cadence.** Full write-up in `INIT6_PM_GAPPER_SIM.md`
("Mechanical-exit sim 2026-07-24"). Next: keep accumulating gappers; build a
1-min exit test only once the admitted set reaches ~12 (result currently hinges
on one INLF). No live orders, no `Day Trading.md` change.

**Update 2026-07-23 (2nd, strategy-advance) — continuation-gate sim.** Built
`scripts/pm-gapper-continuation-sim.js` (log-only, no orders): a causal gate that
enters only after price holds near the ignition high for 2 bars (R+1 and R+2 each
close >= 80% of the running high, VWAP non-declining), entering at R+3, else
skipping. Ran on all 18 PM-only gappers (footprint=none) in `pm-open-scan.csv`.
**(1)** The gate **rejects 7/7 wick-fades** (SXTC, LICN, ZCMD, UONEK, DXST + 2
thin) — the 80%-of-high hold rule is the discriminator the fixed-time sim lacked;
5 holdables are false-rejected, mostly on the VWAP rule (SLGB +76.5%, EHGO +75%),
a tuning knob. **(2)** On the 6 admitted names, holding to PM-last/RegOpen loses
-9%, but the **PMHigh reachable after entry is positive on every one** (mean
+28.5%, median +15.7%: INLF +96%, WBUY +31%, EHGO +21%, MIMI +11%, SKYQ +10%,
BJDX +3%). So the entry lands near the ramp base and a positive peak exists — the
07-14 "12/12 lose" close was an artifact of fixed-time entry + hold-to-fixed-exit.
The gate is a **scalp** rule, not a hold rule. Full write-up appended to
`INIT6_PM_GAPPER_SIM.md`. **Next step: simulate a mechanical exit** (trailing
stop / N-bars / first-lower-high) to measure how much of the +28.5% PMHigh
ceiling is capturable vs the -9% hold floor — that number decides a live-pulse
proposal to Juan. No live orders; no `Day Trading.md` change.

**Update 2026-07-23 — Juan re-opened problem (a) after the SXTC +223% night.**
Feedback (re: 07-22 email): "Can we make changes so that we can catch the winner
of today? ... Go ahead and make the changes. Don't ask for approvals." Two facts
reframe it: **(1) detection is already solved** — SXTC was caught at PM open by
both the morning pulse's live PM scan (04:21 ET, +121% $5.93) and `pm-open-scan`
(05:00 ET, logged uninvestable: single $7.91 wick 04:05, VWAP bled
$6.75->$4.77). The AH scanner is structurally blind to PM-open gappers; the PM
scanners are not. **(2) The 07-14 NEGATIVE close was on n=4; refreshed
`pm-gapper-sim.js` (n=7, adds SLGB 07-21 +76.5%, INLF 07-22 +100.9%) shifts the
picture on entry timing:** entry at the 05:00 ET pulse time still loses -12.5%
(PM-last), but **early entry at 04:10 ET loses only -2.5%** (RegOpen -2.2%) and
lifts best-case RegHigh from +2.5% to **+15.0%**. So the surviving edge is
*timing* — hit the ignition near 04:00 ET, not an hour later (this folds into
Initiative 3, faster ignition detection) — combined with a **continuation gate**
(enter only on 2+ consecutive holding bars, not the opening wick) to exclude
SXTC-type single-bar spikes. **Next step (owned by `strategy-advance`, applied
autonomously per Juan's standing no-approval directive):** build a *log-only*
hypothetical PM-only-gapper entry at earliest detection (~04:10-04:21 ET, using
the morning live-PM-scan feed) with the continuation gate; measure hypothetical
P&L before proposing any live pulse. No live orders and no `Day Trading.md`
change from the feedback pulse that routed this. The prior negative levers below
stand as recorded, but problem (a) is no longer closed.

**Update 2026-07-14 — the
PM-only-gapper hypothetical-entry pilot came back NEGATIVE; problem (a) is
closed with no live-pulse proposal.** Built `scripts/pm-gapper-sim.js`
(log-only): for the 5 holdable + no-AH-footprint gappers in `pm-open-scan.csv`
it hypothetically buys at the 05:00 ET pulse time (and, as a separate scenario,
at an earlier 04:10 ET pulse) and exits at PM-last / regular-open / regular-
close. **12 of 12 realistic entry×exit combinations lose** (entry@05:00: PM-last
-11.7%, RegOpen -11.4%, RegClose -13.4%; even the earlier 04:10 entry stays -8
to -10%). Only the untradeable best-case RegHigh is positive (+1.9% / +6.8%).
The "holdable" tag measures **exitability, not profitability**: these names peak
in the first 1-2 bars (04:00-04:35 ET) then bleed, so by the time holding is
confirmed the entry is already faded. Earlier detection helps a few points but
does not rescue it. **Conclusion: do not promote a PM-only-gapper long pilot;
keep `pm-open-scan` as cheap log-only accumulation, no live entry rule proposed
to Juan.** Full analysis in `INIT6_PM_GAPPER_SIM.md`. Both problem (a) and
problem (b) now have documented negative results, so the AH->PM core strategy
stands unchallenged by the extreme-mover work to date; the only surviving thread
is a possible intraday momentum-continuation re-entry (different, harder setup),
parked pending a bigger sample.

**Prior update 2026-07-13 — the
trailing-stop simulation came back NEGATIVE; the problem-(b) partial-hold pilot
is WITHDRAWN, and problem (a) (PM-only gappers) hit its rollout-step-3
trigger.** Built `scripts/trailing-sim.js` (log-only): it takes each closed
round-trip's premarket exit as a hypothetical hold-start, walks the exit-day
regular-session 5-min SIP path, and simulates a trailing stop at 8/12/15/20%.
**Every width, both gate configs (green-at-exit and hold-all), LOSES vs the
all-out-premarket baseline** (green-gate added return -3.2 to -5.1%/trade;
hold-all -4.1 to -5.0%/trade). Two reasons: only 3 of 14 exits were green and 2
of those faded (the runners — VTAK/GANX/SUNE/PMA/YYGH — were RED at exit, so the
gate excludes them), and the +29% "upside left" is uncapturable because these
microcaps whipsaw to their highs (IVF's +55% high at 14:55 ET, but an 8% trail
stops at -8%). So problem (b) has **no demonstrated mechanical edge** — the
premarket-exit rule is validated by the data and the pilot ask is withdrawn.
Full analysis in `INIT6_EXIT_COST.md`. **Meanwhile the PM-open scan (07-13)
logged MIMI (+68%) and EHGO (+75%) as holdable PM-only gappers with no AH
footprint, bringing the holdable PM-only-gapper tally to 4 (SHPH, BJDX, MIMI,
EHGO)** — the ~3-4 trigger for rollout step 3. Next lever: design a log-only
hypothetical-entry pilot on PM-only gappers (no live orders, no Juan gate).
**Prior update 2026-07-10 — the
exit-time signal test came back NEGATIVE, which reshaped the earlier pilot.** Built
`scripts/exit-signal.js` (log-only) to answer the open question “what signal at
the premarket-exit check separates the IVF-type regular-session runners from the
DCX-type open-dumpers?” It pulls each exit-day’s premarket 5-min SIP bars up to
the exit and measures green%, momentum, off-PM-high, and volume-trend at the
exit check, grouped by verdict (n=11). **None of the signals separate the two
classes** (LEFT vs SAVED means: green +0.9/-1.5, momo -5.7/-11.3, offHigh
-20.7/-19.2, volTrend -0.9/+16.2). The runners look identical to the dumpers at
04:30 ET — all fading ~5-12% off a PM high, near-flat green; **IVF was itself
fading -11.6% into its exit** yet ran to +55% mid-session. This **kills the
“hold if still-green + higher-highs” filter** and points the pilot at a
**trailing-stop partial hold on every green exit** (the stop, not a predictive
signal, sorts runners from faders). Also refreshed `exit-cost.js`: SUNE
(exited 07-09) closed as a 4th **LEFT** (+16% left), so the tally is now **4
LEFT / 5 SAVED / 2 flat, avg +29.7% upside missed** on the clipped runners.
Full analysis in `INIT6_EXIT_COST.md`. Still a proposal for Juan (edits the
`Day Trading.md` no-hold rule); not applied. **Prior update 2026-07-09 — problem
(b) got its first hard evidence.** Built `scripts/exit-cost.js` (log-only research, no
orders) and ran it across all 10 closed paper round-trips: it compares each
premarket exit to the *same regular session's* high/close (Alpaca daily bars =
regular-session only). Result: **3 LEFT (rule clipped a runner) / 5 SAVED (dodged
a dump) / 2 flat; avg upside missed on LEFT trades = +34.3%.** The standout is
**IVF**, our biggest realized winner (+26.6%): it traded to **+55.5% above our
exit in the regular session**, with its $3.11 high at **14:55 ET (midday)** — ~10h
after our 04:30 ET premarket exit — a direct counter-example to the "peaks in PM,
dumps at open" thesis. Takeaway: the blanket premarket-exit rule protects capital
on faders (every SAVED case was a loser/small-gainer, downside already size-
capped) but clips the rare BIG regular-session runner, which is exactly Juan's
"catch BIG wins" critique. Full analysis + proposed pilot in
`INIT6_EXIT_COST.md`. A blanket change is NOT justified (DCX -31%, VEEE -25% to
close show holding everything would bleed faders); the edge is *selectively*
holding movers still green + making higher highs at the exit check. **This is a
proposal for Juan** (it edits the `Day Trading.md` "never hold through the day"
rule) — not applied. PM-only-gapper tally (rollout a) advanced to **2 holdable**
(SHPH 07-08, BJDX 07-09; ELPW 07-09 was thin). **Juan steer 2026-07-07** (re:
07-06 email): "I'd rather catch the bigger jump, not a 'clean 6%'... catching BIG
wins." Reinforces this initiative as the priority and pushes on rollout problem
(b) — the premarket-exit / no-hold rule caps gains and is the mechanism stopping
winners from running (07-06 EDHL exited +6% while TDIC re-ramped +65% overnight).
The daily email framing moderate exits as the "win" also drew the critique. The
exit-rule change touches `Day Trading.md`/live trading, so it stays a proposal
for the strategy-advance pulse to raise, not a unilateral change. Log-only
**PM-open scan pulse is built and scheduled.** `prompts/pm-open-scan.md` runs at 11:00 CET / 05:00 ET
(Mon-Fri, cron `trading-pm-open-scan-1100`): discovers whole-market PM gappers via
`scan.py` (premarket session), classifies each holdable / uninvestable / thin from
real Alpaca-SIP 5-min bars (`broker.js bars --feed sip`), and appends to
`log/pm-open-scan.csv`. **No orders, no change to any existing trading-scan
timing.** Pipeline verified live on today's gapper SUGP (ramped 07:00 ET on
3.4-5.8M sh/bar, held $1.00-1.10 across 6+ bars = holdable). First scheduled run:
tomorrow 11:00 CET. **Flagged for Juan to veto (log-only, so applied directly).**

**Update (2026-07-08) - first scheduled run fired; 4 gappers logged.** The
11:00 CET pulse ran (commit a59fccc) and appended 4 rows to
`log/pm-open-scan.csv`, all classified **holdable**: IOTR (+62.7%, AH-detected
continuation), DCX (+36.3%, AH-detected), BATL (+18.3%, AH-detected BUILD), and
**SHPH (+13.8%, genuine PM-only gapper, no AH footprint, DOGE-mining
acquisition catalyst)** - held $3.65-4.13 within 20% of the $4.34 PM high across
6+ bars. SHPH is the target class (structurally invisible to the AH scanner).
**Running real-time holdable PM-only-gapper tally: 1 (SHPH).** Trigger for
rollout step 3 (propose hypothetical-entry pilot to Juan) is ~3-4; keep
collecting. The three AH-detected names confirm the pulse also captures
AH->PM continuers the main scanner already sees (useful cross-check, not the
blind-spot target).
Prior status (Research, 2026-07-06): Census in
`INIT6_EXTREME_MOVERS.md` (**14 cases, May 14-Jun 26**). **Key update 2026-07-06:
the PM-open-scan gate is MET — live-fillability confirmed.** Ran the fillability
check the gate required (Alpaca SIP historical minute bars via `broker.js bars
--feed sip`): both holdable PM-only gappers, CIIT (+140%) and GLXG (+343%), traded
on **millions of shares and 18K-58K trades per 5-min bar across the whole 04:00-05:00
ET ramp** — genuinely fillable, not the single-tick risk Yahoo's `vol=0` implied.
TDIC (uninvestable control) also had deep liquidity, confirming uninvestability is
a price-*path* property, not a liquidity one. Alpaca SIP is now a validated
premarket data source the scan can use. **Next: draft the log-only PM-open scan
pulse** (~04:00-05:00 ET, instrumentation only, no orders); a new log-only pulse
may be added directly but will be flagged for Juan's veto first. **Prior decision
2026-07-03: the Tier-A-catalyst hold rule is SHELVED; the PM-open scan (pattern 2)
is the lever to advance.** Cross-tabbing pattern 3 (catalyst tier) against
pattern 4 (real-AH-volume gate) shows the hold rule has **zero tradeable
supporting cases**: the only AH continuer (ILLR) had zero real AH volume
(untradeable), and every *tradeable* AH runner faded (premarket exit was correct
each time). So formalizing a catalyst hold rule would act on an untradeable
pattern — parked until a tradeable Tier-A AH runner (real AH volume + holdable)
appears; keep logging the catalyst tag so it's captured if it comes. The
reachable +200-600% money is in pattern 2's **holdable PM-only gappers** (CIIT
+140%, GLXG +343%), so rollout step 2 (a log-only PM-open scan) is the next
proposal — gated on 1-2 more holdable gappers or a live-fillability check. **Prior
key update 2026-07-02:** pattern 3
**strengthened to 5 faders / 1 continuer, 100% consistent**; added **pattern 6:**
regular-session spikes (EVOL +300%, CPOP +369%, ATLN +220%) are a distinct
negative class the AH->PM strategy structurally cannot and should not trade
(AH <10%). Prior key update (2026-06-30): **Key update 2026-06-30:**
classified the three unlabeled PM-only gappers from their 15m premarket bars
(`scripts/init6-pmbars.py`) and **flipped pattern 2** — PM-only gappers are NOT
mostly uninvestable. CIIT (+140%) and GLXG (+343%) both held elevated across the
entire 5h premarket and opened on 48-53M shares = **holdable**; only TDIC
decayed instantly. Running PM-only tally: 2 holdable / 3 uninvestable, and the
two holdable ones are exactly the big movers Juan wants. So the AH-blind-spot
has **real cost**, raising the priority of rollout step 2 (a log-only PM-open
scan). Other strong patterns: (3) catalyst tier separates AH continuers from
faders — ILLR (Tier A, SpaceX) ran +760%, MSW (Grade C dilution) faded; (4)
headline AH % on zero AH volume (ILLR, TII) is an untradeable trap. Juan
reiterated priority (2026-06-26): ILLR +760% is "exactly the kind of stuff we
want to catch." Pattern extraction is co-equal with catching them (rollout 1b).

**Why it is hard / where the big moves hide:**
- The biggest raw movers each morning keep being **PM-only gappers** — flat or
  down in after-hours, then exploding only after 04:00 ET on overnight news
  (CIIT +140%, GLXG +343%, TDIC +140%, MBRX +131%). The AH->PM scanner cannot
  see these by design (no AH footprint to detect).
- True AH extreme runners (>250% in AH) are very rare in our data (MSW Jun 9 is
  the only one tracked). Most AH movers we catch top out at +60-130% and then
  fade into PM.
- So "catch 600%" is really two separate problems: (a) a PM-open scan workflow
  for gappers with no AH signal, and (b) holding/letting winners run instead of
  the premarket-exit rule capping gains.

**Open questions:**
- Are the +300-600% names reachable at a tradable price, or do they spike and
  collapse in minutes (MBRX $6.64->$3.77 in 10 min) — i.e. uninvestable?
- Would an early-PM scan (04:00-05:00 ET) plus a momentum-hold rule actually
  capture them, or just add chop and false positives?
- Does this conflict with the proven premarket-exit discipline (most movers
  peak in PM then dump at open)?

**Rollout plan:**
1. ~~Quantify: list every +200% mover, tag detectable / PM-gapper /
   uninvestable.~~ **Done** (census, 14 cases). Seeded from the PM-only-gapper
   tracker in the morning eval.
   **In progress (2026-06-30):** 9-case census built; the three unlabeled
   PM-only gappers now classified (CIIT/GLXG holdable, TDIC uninvestable). Next:
   mine older logs (Mar-May) for more +200% cases toward the ~15-20 threshold,
   then decide whether the holdable-PM-gapper evidence justifies proposing
   rollout step 2 (a log-only PM-open scan) to Juan.
1b. **Extract patterns (Juan, 2026-06-26):** for every extreme runner and
   ceiling-watch name (e.g. ILLR +760%), characterize catalyst tier, float,
   AH-vs-PM timing, volume profile (VRatio path), and price path through the
   move. Goal: turn the ceiling-watch dataset into reusable entry/skip signals
   so the system recognizes the setup early instead of only flagging and
   skipping it. This is co-equal with "catch them," not a sub-task.
2. ~~Instrument a PM-open scan (log only, no action).~~ **Done 2026-07-07** —
   `prompts/pm-open-scan.md` + cron `trading-pm-open-scan-1100` (11:00 CET /
   05:00 ET, Mon-Fri) log holdable/uninvestable/thin gappers to
   `log/pm-open-scan.csv`. Now accumulating real-time gapper cases.
3. Pilot hypothetical entries on that subset; compare to the current strategy.
4. Promote only if the extreme-runner capture beats current net of false spikes.

**Needs from Juan:** nothing yet (research uses existing data + the gapper
tracker).

---

## Current priorities and initiative status — 2026-10-06 15:00 CEST

This checkpoint supersedes earlier checkpoints and initiative status paragraphs. **Initiative 6's pilot failed its causal execution check, and the pilot slot is released.** **Initiative 7's SEC archiver is built and verified**, and its census shows the frozen A1 arm would rarely act. The two October 5 strategy runs and all 13 October 5 post-market scans were lost to the expired Anthropic login; nothing was skipped by choice. Paper equity at 15:16 CEST is **$99,721.90 (-$278.10)**, flat.

**Money-fast selection:** The largest measured loss this week is reliability. Provider failures stopped scheduled scans three times in 14 days (Sep 22, Sep 29, Oct 5), and OLOX, missed on Oct 5, simulated +63.9% under the existing gates. The fix is outside this repo and is already in the daily email as the process review's decision for Juan. Within this loop, Initiative 6's latency test decides whether its modeled +2.4% net per name could be earned at all; it cannot with the current stack. The released slot leaves Initiative 7's liquid-session comparison as the only pilot candidate. Its archiver was the oldest overdue build, and the census changes its design before instrumentation starts.

| Initiative | Latest concrete progress | Current status / dependency | Next deliverable and check |
|---|---|---|---|
| 1 — shared volume measurement | October 1 18:00 consumers verified | **Instrument.** Sparse-baseline policy deferred again today, after the outage and two larger results. | **October 6 18:00:** resolve one sparse-baseline/prior-coverage policy against INLF/GIPR/YFOR. |
| 2 — broker execution | September 7 alternatives research | **Deferred per Juan's September 22 instruction.** Initiative 6's latency result adds a second reason it matters: premarket entries need real-time consolidated data and simulated fills on live books. | Resume the AKAN/SHPH/GIPR protocol only when access arrives; no renewed ask. |
| 3 — scheduling and exits | October 6 15:00: outage and screener-lag evidence recorded | **Research.** Provider failures stopped scans three times in 14 days (Sep 22, Sep 29, Oct 5–6). The process review's late-start guard now stops post-market pulses outside 15:25–20:00 ET. The screener's lag of roughly 15 minutes also delays AH discovery. | **October 7 15:00:** one causal later-rebuild comparison using shared measurements, with screener lag modeled. Bridge DST-loading check before October 25. |
| 4 — initiative reporting | Receipt 179 covered Initiatives 7/6/3/4 | **Delivered and verified.** | Next daily email: Initiative 6 latency result and slot release, Initiative 7 archiver/census/A2 proposal, Initiative 3 outage record, Jev not run today. |
| 5 — review surface | October 1 consumers and Pages publication verified | **Build delivered.** | Check shared rows beside charts on the next chart-bearing cycle. |
| 6 — PM-only gappers | October 6 15:00: latency study, stale-cohort finding, QTEX/RUBI gate check | **Pilot ENDED (failed causal check); log-only research continues.** The edge needs entry within about 5 minutes of the confirmation bar's close. The current data path is about 15 minutes late, and no pulse runs 04:10–04:30 ET. | Keep the tracker/ledger log-only as an upper bound. Reopen only with real-time consolidated data and a deterministic sub-minute watcher. The cohort window stays useless until it moves after the screener lag; correct seasonal UTC bounds before winter. |
| 7 — alternative agent strategies / Jev | October 6 15:00: SEC archiver, frozen CIK mapping, 7 real captures, 92-day census | **Research plus Instrument.** A1 would have a usable 8-K in 1.7% of observations, so a 20-session pilot would hold about two Jev decisions. | **October 6 18:00:** freeze amendment A2 (veto variant: keep N1 without a usable source; cash on financing/dilution or non-binding-plan labels). **October 7 15:00:** observation orchestration and the first loadable scheduled capture. Five instrumentation sessions precede the comparison pilot, which can take the free slot. |

**Initiative 6 progress, October 6 15:00:** `init6-pm-pilot.js --delay-min N` delays the entry and leaves the gate, exit and ledgers unchanged; a default run reproduced both ledgers exactly. Holdable n=26 mean +10%-limit return: **+4.4% at R+3 open (+2.4% after the assumed 2% spread), +0.7% at 5 minutes (-1.3% net), -3.7% at 10 minutes, -4.4% at 15 minutes (-6.4% net)**. Positive cases fall 20 → 18 → 15 → 12. Across all 35 classes the mean falls from +3.4% to -2.5% gross. Every checked 04:10 ET cohort (Sep 30, Oct 1, Oct 2, Oct 5) holds the previous session's final premarket prices, for example SDEV $3.59 on Oct 2 while SIP traded $4.36–$4.82. So the cohort never measured same-day discovery, and earlier "discovery miss" results are void. QTEX (Oct 5) is a second VWAP false negative, a +10% limit win missed. Its cohort presence came from Friday's stale row. RUBI (Oct 6) was correctly rejected, and Oct 6 has no cohort because of the outage. Ad-hoc runs no longer overwrite the ledger. Evidence: `docs/investigations/init6-latency-init7-sec-2026-10-06.md`, `log/2026-10-06/init6-latency-*min.txt`, `log/2026-10-06/tv-delay-probe-0915et.json`.

**Initiative 7 progress, October 6 15:00:** Delivered `scripts/init7-sec-archive.py` (`map`, `capture`, `replay`, `census`). The mapping froze 7 unique CIKs (SHA-256 `7afbd376…`). Seven real captures at 13:14 UTC returned `no_8k_within_window`, so every arm was cash. A historical AAPL capture archived the 8-K and EX-99.1, then rejected them as `received_after_cutoff`. All eight archives replay offline with no problems. Overwrite, a cutoff without a time zone and a tampered text file are rejected or detected. The submissions JSON acceptance time is 4 hours late for 6 of 16 filings (Apple, Amazon, Meta), so the filing header's Eastern time is used. Census of Jul 6 – Oct 5, 2,772 slots: **16 8-Ks, 8 fit the 20KB request, 3.5% of slots have a recent 8-K and 1.7% have a usable one**. Only 2 of 7 earnings releases fit. Archived bytes are marked binary in `.gitattributes` so git keeps them exact. No Jev call this run.

**Initiative 3 progress, October 6 15:00:** Added the outage record to the scheduling evidence: provider failures on Sep 22 (usage limit), Sep 29 (token invalidated) and Oct 5–6 (expired refresh token). The last outage lasted 21.7 hours, and 0 of 13 Oct 5 post-market scans ran. The process review added the post-market late-start guard and duplicate-entry check. Provider fallback and alerting need Juan. The screener's lag of roughly 15 minutes is a new input for the AH timing replay.

**Previous-step evaluation:** The October 2 18:00 plan for October 5 did not run because of the outage. Today the SEC archiver **worked** as specified and exposed a design flaw (A1 availability) before any instrumentation sessions were spent. Initiative 6's "next PM-only case" check **worked** and produced the decisive latency result. Initiative 1's sparse-baseline policy and Initiative 7 orchestration are rescheduled above with dated slots.

**Needs from Juan / consolidated asks:** nothing new from this loop. The process review's provider-fallback/alert decision is in the daily email. Preserve the liquid-session proposal, Initiative 2's deferral, and the unapplied Initiative 3 scan-retirement/exit proposals. No trading-pulse timing change is proposed.

## Prior checkpoint — 2026-10-02 18:00 CEST

This checkpoint supersedes the earlier checkpoints and initiative status paragraphs. **Initiative 7 delivered the frozen numerical/agent comparison, verified its price-feature selector and resolved fractional asset eligibility. Initiative 6 and Initiative 3 finalized the earlier incomplete PM results.** Initiative 6 remains the only pilot. Paper equity at approximately 18:03 is **$99,721.90 (-$278.10)** with no positions. The existing liquid-session/core-universe proposal remains for the daily email.

**Money-fast selection:** Initiative 6's completed SGRX check resolves whether a later qualifying ignition existed before any admission claim. Initiative 7 remains the highest potential account-growth research lever because liquid regular-session observations could increase executable frequency and capacity; its edge is still unknown, and the frozen comparison now measures Jev's incremental value against the same numerical candidate after costs. Initiative 3's completed replay closes the older pending timing comparison and supplies no promotion evidence. No larger proved lever appeared today. Initiative 1's older sparse-baseline work retains its October 5 delivery alongside Initiative 7's next source build.

| Initiative | Latest concrete progress | Current status / dependency | Next deliverable and check |
|---|---|---|---|
| 1 — shared volume measurement | October 1 18:00: shared confirmation/HTML consumers verified | **Instrument.** Sparse-slot policy and prior-session coverage remain untested. Skipped today for the due alternative design and completed replay. | October 5 15:00: resolve one sparse-baseline policy against INLF/GIPR/YFOR; next chart-bearing cycle checks identical rows. |
| 2 — broker execution | September 7 alternatives research | **Deferred per Juan's September 22 instruction.** Depends on his broker/data/API access. | Resume the written AKAN/SHPH/GIPR fill protocol only when access arrives; no renewed access ask. |
| 3 — scheduling and exits | October 2 18:00: full-PM replay finalized, all 13 selected rows unchanged | **Research / Instrument.** No cadence edge or new actual exit. Later rebuilds remain outside this first-ignition variant. | October 6 15:00: one causal later-rebuild comparison using shared measurements, after October 5 source/sparse-baseline deliveries. Seed exits after a new fill; bridge loading check before October 25. |
| 4 — initiative reporting | October 2 reporting prompt and receipt 178 verified at 15:00 | **Delivered and verified.** No new reporting change required. | Next daily email: separate Initiative 7 design/selector/eligibility and Initiative 3 completed replay updates, Initiative 6 final result, and exact Jev calls/costs and dependencies. |
| 5 — review surface | October 1 consumers and Pages publication verified | **Build delivered.** Verification beside charts depends on the next qualifying chart/report cycle. | Inspect shared rows beside charts when that cycle exists. Sparse-coverage work follows Initiative 1 on October 5. |
| 6 — PM-only gappers | October 2 18:00: complete 66-slot SGRX audit closes the pending result | **ACTIVE sole pilot, log-only.** No 3,000-trade ignition in SGRX's full PM session; no admission. Ledger remains 26 holdable / 35 all-class rows. | October 5: retain the pre-entry cohort and check the next genuine PM-only case against discovery, causal gates, quote availability and completed outcome. Untracked cohort outcomes and executable edge remain unresolved. |
| 7 — alternative agent strategies / Jev | October 2 18:00: frozen comparison, selector and eight asset responses delivered | **Research plus Instrument.** Numerical N1 and bounded Jev A1 are frozen but untried prospectively. Primary-source archiver is specified and unbuilt; no second performance pilot. | October 5 15:00: build/verify immutable SEC source capture and issuer mapping. October 5 18:00: observation orchestration and the first future scheduled capture that can actually load. Five full instrumentation sessions and release of the pilot slot precede a comparison pilot. |

**Initiative 7 progress, October 2 18:00:** Delivered `docs/investigations/init7-comparison-v1.json`, `docs/investigations/init7-comparison-2026-10-02.md` and `scripts/init7-comparison-features.py`. The configuration freezes the seven-stock/QQQ basket, delayed exact-slot half-hour features, six observations beginning at 10:30 ET, equal research capital, numerical relative-strength selection and one Jev event veto on the same candidate. It specifies immutable primary-source bytes/receipt times/hashes, cash/QQQ comparators, all tried variants, base/stress friction and complete operating-cost accounting. Any future pilot needs the sole slot released, causal capture verified and its next 20 full calendar sessions frozen before entries. Existing live rules and sizes are untouched.

All **8/8 assets** report active/tradable/fractionable in `log/2026-10-02/init7-asset-eligibility.json`, resolving the whole-share constraint at the research allocation without an order. The archived development reference has **56/56 required closes**, all seven stock returns negative and N1 cash; its off-schedule pre-freeze data are explicitly excluded from prospective performance. **13 CLI checks**, compilation and whitespace validation passed, including future-bar independence, late receipt rejection, missing slots, feed/pagination checks and overwrite refusal. Design/selector hashes and results are in `log/2026-10-02/init7-comparison-reference.json` and `init7-comparison-verification.json`. No Jev call occurred in this run; the earlier six-call manifest remains the classification evidence. No prospective accuracy, calibration or net return is proved. The SEC archiver is the next concrete dependency, not a delivered capture.

**Initiative 6 progress, October 2 18:00:** Explicit SIP archive `log/2026-10-02/init6-SGRX-audit-1800.json` has **66/66 PM slots**, no missing/duplicate bars and no remaining pagination. Maximum trades stays **2,651 <3,000** through the completed 09:30 ET end; no later ignition or admission exists. PM high **$2.08**, PM-last **$1.775** are observations, not fills or pilot returns. The frozen cohort's selected PM-only overlap remains **0/1**, with no fresh positive-size ask among its 17 names; this does not establish universe recall. A later regular-session **$1.67 x100 / $1.68 x100** quote, **16.693 seconds old**, cannot reconstruct a PM fill. Existing ledgers remain unchanged without another broad historical fetch.

**Initiative 3 progress, October 2 18:00:** Completed `log/2026-10-02/init3-opening-replay-1800.json` exactly matches all 13 earlier selected-case lines. Second-bar admits remain **0**; third-bar admits only **IPW**, modeled **$1.40 at 17:30 ET**, identical to the legal grid, **-18.6% to PM open / -10.7% PM-high ceiling**. AMOD's later rebuild is still excluded, TARA's two bars are insufficient, and original-fixture denominators are not used. Finishing the outcome window revealed no entry-price advantage. Full completed-window evidence and limits: `docs/investigations/init6-init3-final-2026-10-02.md`.

**Previous-step evaluation:** The latest 15:00 hypothesis **worked for its named delivery/closure targets**: the deferred numerical/agent specification is delivered, SGRX's no-ignition result held through the complete PM session, and the completed AH replay is unchanged. The Jev implementation remains supported by its earlier control evidence; future primary-source accuracy and trading edge still have **insufficient data**. The paper account remains negative, supporting the existing alternative-strategy research priority. This run finalized the remaining named process-review handoffs; no new handoff was silently carried forward.

**Consolidated dependencies:** Initiative 7 needs its SEC archiver and prospective receipt/decision captures, then five full instrumentation sessions and the released pilot slot; these are agent work, with the October 5 deliveries above. Initiative 6 needs new prospective PM-only discovery/gate/book evidence and coverage of untracked cohort names; its seasonal UTC bounds need correction before winter. Initiative 3 needs an actual exit fill for seeding and a bridge loading check before October 25. Initiative 1/5 needs sparse-slot/prior-session interpretation and the next chart-bearing cycle. Initiative 2 alone depends on Juan-provided access and remains deferred.

**Needs from Juan / consolidated asks:** nothing new. Preserve the existing liquid-session/core-universe daily-email proposal, Initiative 2's deferral, and unapplied Initiative 3 scan-retirement/exit proposals. No new trading-pulse timing change is proposed or applied.

## Prior checkpoint — 2026-10-02 15:00 CEST

This checkpoint supersedes the earlier checkpoints and initiative status paragraphs below. **Initiative 7 delivered the sourced Jev classification comparison and its first verified shadow run; Initiative 3 resumed the deferred replay and verified scan completion; Initiative 6 added a prospective discovery/gate audit.** Initiative 6 remains the only pilot. Paper equity at today's 14:30 evaluation remains **$99,721.90 (-$278.10)**, with no positions. The deadline-triggered alternative liquid-universe proposal remains active research and a daily-email proposal.

**Money-fast selection:** Initiative 6's new SGRX audit tests whether its modeled micro-cap edge can be discovered and entered causally. Initiative 7's cheap catalyst judgments could reduce financing/promotional selection mistakes and provide reusable features for the larger liquid-universe comparison; incremental profit remains unknown. Initiative 3's older deferred replay tests earlier entry prices and rejects another cadence promotion on this evidence. An executable liquid-session comparison still has greater potential account-growth impact than scaling rare hindsight-selected PM-only returns. AMOD's missed later rebuild is an Initiative 3 research question; it does not prove a new entry rule.

| Initiative | Latest concrete progress | Current status / dependency | Next deliverable and check |
|---|---|---|---|
| 1 — shared volume measurement | October 1 18:00: shared confirmation/HTML consumers verified | **Instrument.** Sparse-slot interpretation and prior-session coverage remain untested; no gate promotion. Skipped today for Juan's new Jev handoff and the older Initiative 3 replay. | October 5 15:00: resolve one sparse-baseline policy against INLF/GIPR/YFOR controls; next chart-bearing cycle checks identical rows. |
| 2 — broker execution | September 7 alternatives research | **Deferred per Juan's September 22 instruction.** Depends on his broker/data/API access. | Resume AKAN/SHPH/GIPR extended-hours fill protocol only when access arrives; no renewed access ask. |
| 3 — scheduling and exits | October 2: archived completion check and September 30/October 1 AH replays | **Research / Instrument.** All 12 reviewed AH sessions completed; four entry sessions had no assistant error. October 2 PM highs remain interim; no new actual exit. | October 2 18:00: finalize the October 1 AH/October 2 PM replay. Next research delivery tests later rebuilds with causal shared measurements. Seed exits only after a new fill; bridge loading check for DST jobs before October 25. |
| 4 — initiative reporting | October 2 Jev reporting prompt; receipt 178 now verified | **Delivered and verified.** Latest successful email separately reports Initiatives 1/4/5/7 and includes Jev not-run/usage-unavailable status. | Next daily email: report the new Jev manifest, Initiative 3 replay and Initiative 6 audit, with exact windows, costs and dependencies. |
| 5 — review surface | October 1 18:00 consumers and subsequent Pages publication verified | **Build delivered.** Chart-bearing verification depends on the next qualifying chart/report cycle; no new chart issue. | Inspect shared rows beside charts when that cycle exists. Sparse-coverage work follows Initiative 1 on October 5. |
| 6 — PM-only gappers | October 2: archived SGRX discovery/gate/current-book audit | **ACTIVE sole pilot, log-only.** SGRX was absent from the 04:10 snapshot and had no >=3,000-trade ignition through 08:50 ET bar end. Completed ledger stays 26 holdable / 35 all-class admits through September 29. | October 2 18:00: finalize SGRX after complete PM and delayed SIP availability; compare any later ignition, frozen discovery and available quote evidence. No fill or promotion inferred. |
| 7 — alternative agent strategies / Jev | October 2: sourced comparison, frozen labels/inputs, six verified calls and offline replay | **Research plus Instrument delivered.** `stock-catalyst-v1`, pinned `jev-1.13.0`; all 18 selected control judgments matched. Prospective accuracy, calibration and net dollars remain unmeasured. | October 2 18:00: freeze numerical-control versus bounded-agent design with equal capital, causal observation times, delayed SIP, cash/QQQ comparators and all costs; specify immutable primary-source capture. Deferred from 15:00 to complete Jev delivery and the older replay. |

**Initiative 7 progress, October 2:** Delivered `docs/investigations/init7-jev-classification-2026-10-02.md`, `scripts/init7-jev-classify.py`, frozen `log/2026-10-02/init7-jev-inputs-v1.json` and `log/2026-10-02/init7-jev-shadow-v1/`. The comparison covers FinBERT sentiment, FinBERT-FLS forward-looking language, Snowflake SEC event classification, TypeSafe SIC classification and its feature-discovery cookbook, including their inputs, labels, evaluation limits and cost availability. Jev classified archived AMOD as financing/dilution, SORA as a non-binding plan and ELUT as an asset cash receipt; synthetic commercial, missing and mixed controls also matched. Six calls measured **5,471 input / 931 output tokens**, with **$0.000229782 USD estimated inference cost** at the checked published rate; actual billed charge is unavailable. This covers this batch only, with research/data/agent costs outside that estimate. Archived summaries and synthetic controls are interface evidence, not prospective trading accuracy or profit. Offline replay, future-source rejection, overwrite rejection, a simulated failed-call/unknown-cost archive, compilation and whitespace checks passed. The next email reads the manifest and every disagreement/failure; no live request failed in this batch.

**Initiative 6 progress, October 2:** The frozen **04:10:23 ET** cohort contained **17 names** and zero fresh positive-size asks (ages 42,070–43,831 seconds). SGRX is the sole selected PM-only tracker case and is absent, giving one discovery miss without a whole-universe recall estimate. Explicit SIP input archived in `log/2026-10-02/init6-SGRX-audit-1500.json` retains **58 completed bars through 08:50 ET bar end**, maximum **2,651 trades**, below the frozen 3,000 threshold; no ignition, confirmations or entry yet. A later IEX book had $1.76 x100 bid / $1.77 x100 ask, approximately 0.103 seconds old at the response-file write. That later fresh quote cannot prove an earlier entry or fill. Full PM outcomes remain pending at this cutoff. Evidence and next check: `docs/investigations/init6-init3-checks-2026-10-02.md`.

**Initiative 3 progress, October 2:** Archived saved-session evidence shows **12/12 AH scans completed with zero assistant errors**, including all four eligible entry scans; September 29's authentication failure did not recur. In the 13 selected October 1 AH cases, second-bar admits **0**, third-bar admits only **IPW**, modeled $1.40 at 17:30 ET, the same as the legal grid, returning **-18.6% to next PM open**; its PM high remains interim. AMOD's first ignition is rejected and its later rebuild is outside this variant. The completed September 30 reference admits only WETO: earlier second-bar $1.22 / -4.9% PM-open versus legal-grid $1.15 / +0.9%; third-bar $1.16 / 0.0%. Original-fixture denominator lines, insufficient TARA/BOXL bars and unverified OHLC fills are excluded from promotion claims. Per-case archives and limits are linked from the evidence report. No schedule or entry-rule change follows.

**Previous-step evaluation:** The latest Initiative 4 reporting hypothesis **worked**: sent receipt **178**, October 2 09:37:06 UTC, and its exact archived HTML contain Jev Results and Costs with pending implementation and unavailable usage/cost, plus each initiative that moved in its reporting window. The classification handoff is now delivered. The earlier liquid-universe census supports this research but still has **insufficient edge evidence**; the numerical/agent design is assigned to 18:00. Initiative 6's full-window result remains **insufficient data** at this run, so its new audit and the two parallel deliveries supply the progress.

**Needs from Juan / consolidated asks:** nothing new. Preserve Initiative 2's deferral, the existing liquid-session/core-universe daily-email proposal, and the unapplied Initiative 3 scan-retirement/exit proposals. No new trading-pulse timing change, order, plan change or size change is proposed by this run.

## Prior checkpoint — 2026-10-01 18:00 CEST

This checkpoint supersedes the 15:00 status below. **Initiative 7 advanced in Research; Initiatives 1/5 delivered verified shared-volume consumers in Instrument/build.** Initiative 6 retains the only pilot slot and added no case on the completed October 1 window. Paper equity remains **$99,721.90 (-$278.10)** with no positions. The deadline-triggered alternative-universe proposal remains for the daily email; no trading rule, position size or existing pulse timing changed.

**Money-fast selection:** Initiative 7's liquid regular-session census tests whether existing access can support more frequent observations and lower friction than the current rare PM-only admits; an execution-ready alternative has higher potential account-growth impact than another unchanged pilot rerun, though its edge remains unknown. Initiative 1/5 consumer delivery closes the oldest ready measurement request and exposes entry-quality errors before further gate tuning. Initiative 3's next replay was deferred today to finish those two named deliveries; it resumes in the October 2 run alongside the prospective alternative-strategy design. Initiative 2 remains deferred at Juan's request.

| Initiative | Latest concrete progress | Current status / dependency | Next deliverable and check |
|---|---|---|---|
| 1 — shared volume measurement | October 1 18:00: confirmation consumes the shared computed JSON; INLF/GIPR controls added | **Instrument, reopened.** All 50 available rows agree across JSON, CLI and HTML; the existing verdict is preserved. INLF's sparse ignition baseline is unknown, while losing GIPR clears 10x. | Resolve sparse-slot interpretation and prior-session coverage before any gate proposal; next chart-bearing cycle checks the same rows beside charts. |
| 2 — broker execution | September 7 alternatives research | **Deferred per Juan's September 22 instruction.** Needs his broker/data/API access. | Resume the written AKAN/SHPH/GIPR extended-hours fill protocol only when access arrives; no renewed access ask. |
| 3 — scheduling and exits | September 30 authentication cause resolved; September 30 entry sessions completed without errors | **Research / Instrument.** No new held-name exit; schedule-resource veto and exit proposal remain unapplied. | October 2: check October 1 AH session completion/authentication and replay its complete AH/PM candidates. Seed the next actual exit; verify DST jobs loaded before October 25. |
| 4 — initiative reporting | October 1 receipt/HTML verification | **Delivered and verified.** Latest successful email covered Initiatives 3/4/6; today's later work awaits its reporting window. | Next daily email: separate dated Initiative 1/5/7 updates for both October 1 runs, unchanged pilot monitoring, checkpoint/pivot proposal, and exact dependencies. |
| 5 — review surface | October 1 18:00: shared-volume HTML tables generated and checked | **Build delivered locally.** Dated `*-volume-metric.json` files opt into the normal Pages rebuild; no additional market fetch occurs in report generation. | Verify the published October 1 report after push, then check beside charts on the next chart-bearing cycle. |
| 6 — PM-only gappers | September 30 cohort audit; last new modeled admit September 29 | **ACTIVE sole pilot, log-only.** Completed October 1 rerun is monitoring: 26 holdable / 35 all-class admits unchanged; no tracked PM-only case and no fresh ask in the frozen cohort. | October 2 04:10 ET: retain the next prospective capture; at the next genuine PM-only case compare discovery, all causal gate decisions, quote age and completed outcome. No promotion without execution evidence. |
| 7 — alternative agent strategies | October 1 18:00: archived liquid-basket SIP/quote census and offline replay delivered | **Research, unblocked.** Eight fresh IEX books at one observation; full completed SIP coverage. No second pilot started. | October 2 15:00 CEST: freeze one numerical control and one bounded agent variant, causal timing, equal capital, cash/QQQ comparators and operating costs before future outcomes. |

**Initiative 7 progress, October 1 18:00:** Delivered `scripts/init7-data-census.py`, raw `log/2026-10-01/init7-data-census.json`, and `docs/investigations/init7-data-census-2026-10-01.md`. Calendar-bounded September 30 SIP coverage is **78/78 five-minute bars on each of eight fixed symbols**; October 1 delayed SIP is **27/27 each**. At 12:04:08 ET all eight IEX books were two-sided with positive sizes, quote ages **0.060–0.656 seconds**, median spread **19.699 bps** (range 0.812–37.675). At $100 research allocation the median crossing cost is approximately $0.197 per round trip before slippage/fees. Current SIP bar ends were approximately 19 minutes old with a deliberate 16-minute request buffer. Six read requests took 3.605 seconds; no new subscription or model call was needed. Six hourly agent calls would cost at most $0.30/session under a prospective $0.05/call design budget; actual token cost, opportunity count, repeated book coverage and profitable edge are still unknown. Network execution, compilation and archived report replay passed. This supports designing the comparison, not trading adoption.

**Initiative 1/5 progress, October 1 18:00:** Added `ah-5m-confirmation.js --volume-metric PATH` and HTML report consumption from the same archived calculation. Generated `reports/2026-10-01/index.html`; **50 timestamps/share counts/local ratios/prior ratios match** the JSON and CLI, with the original YFOR header/verdict preserved. Invalid symbol/date and incomplete-cutoff files fail before broker requests. New controls show **INLF September 24 16:30: 623,155 shares but missing local baseline, prior coverage 4/48**; **GIPR September 3 16:40: 13.6131x locally, prior coverage 45/48**, despite being Juan's rejected losing entry. An unknown baseline as a rejection would miss INLF; 10x alone admits GIPR. No entry-threshold promotion follows. Specification and full evidence: `docs/investigations/shared-sip-volume-consumers-2026-10-01.md`.

**Initiative 6 evaluation, October 1 18:00:** The completed-window rerun and cohort audit preserve the earlier result: no tracked PM-only case, 21 frozen names, zero positive-size asks <=60 seconds old. The 26-admit holdable ledger and 35-admit all-class tally are unchanged. This is insufficient new pilot evidence and is recorded as monitoring. Parallel deliveries supplied the progress.

**Needs from Juan / consolidated asks:** nothing new. The existing Initiative 7 regular-session/core-universe direction is a daily-email proposal; research proceeds with existing access. Preserve Initiative 2's deferral and the unapplied Initiative 3 schedule-veto/exit proposals. No new trading-pulse schedule change is proposed by this run.

## Prior checkpoint — 2026-10-01 15:00 CEST

This checkpoint supersedes the July priority framing where it assumes the AH→PM core is the best surviving approach. **Paper equity is $99,721.90, down $278.10 (0.2781%) from $100,000, with no positions.** Juan's September 1 net-positive deadline has not been met. Open alternative agent-strategy research now; any change to the trading session, universe or plan goes to his daily email as a proposal.

The next research priority is **Initiative 7's liquid regular-session feasibility census**: a different executable universe may offer more repeatable dollars per day than the rare modeled PM-only admits. Its edge remains unknown. **Initiative 6 retains the sole pilot slot**; Initiatives 1/5 share the oldest ready measurement delivery and advanced today. No live strategy, existing trading-pulse timing or position size changed.

| Initiative | Last concrete progress before this run | Current status / dependency | Next deliverable and check |
|---|---|---|---|
| 1 — shared volume measurement | July 15 original research; September 9 metric request remained undelivered through today's process review | **Instrument, reopened** for the shared metric; original volume-lead hypothesis remains falsified. Calculation and YFOR report delivered today. | October 1 18:00: opt-in log-only consumption by confirmation output and chart/report annotations, with one common bar timestamp and ratio. |
| 2 — broker execution | September 7 alternatives research | **Deferred at Juan's September 22 request.** Requires an IBKR paper account with consolidated US data/API access or usable Webull paper credentials. | Resume the AKAN/SHPH/GIPR extended-hours fill protocol when access arrives; do not repeat the access ask or let it block other work. |
| 3 — scheduling and exits | September 30 authentication root cause | **Research / Instrument.** October 1 process review confirms all four September 30 entry sessions reached a final response without assistant errors. Exit research has no new fill since TOPS September 23; scan retirement stays proposed. | Next eligible AH window: check session completion and authentication recurrence. Next held-name exit: seed full premarket bars. Review the September 30 replay after the two ready deliveries; verify DST jobs loaded before October 25. |
| 4 — initiative reporting | October 1 prompt delivery | **Delivered and verified.** Email receipt 176 and archived HTML include separate Initiative 3/4/6 updates in the correct reporting window. | Next daily email: include each initiative that moved in this run, plus the October 1 checkpoint and exact dependencies. |
| 5 — review surface | September 24 verified Pages report | **Build delivery.** Shared-volume report delivered today through the same calculation as the JSON interface. | October 1 18:00: opt-in annotations with matching metric rows; the next chart-bearing daily cycle verifies daily delivery. |
| 6 — PM-only gappers | September 30 prospective-cohort audit; last new modeled admit September 29 | **ACTIVE sole pilot, log-only; today's ledger rerun is monitoring.** Needs prospective PM-only discovery and a current executable book. | At 18:00 recheck the completed October 1 window; next PM-only case: compare frozen discovery, causal gate decisions and quote age. Untracked snapshot names need gate/outcome coverage before a recall claim. |
| 7 — alternative agent strategies | Opened today | **Research, unblocked.** Read access exists; no second pilot started. | October 1 18:00: completed September 30 SIP coverage and current regular-session quote/spread census on eight fixed symbols. |

**Initiative 1/5 progress, October 1:** Delivered `scripts/volume_metric.py`, specification `docs/investigations/shared-sip-volume-metric.md`, archived raw SIP input and `log/2026-10-01/YFOR-volume-audit.md`. `sip-ah-volume-v1` uses a three-slot preceding AH median, explicit missing/zero handling, completed-bar bounds and the previous completed AH maximum with coverage. JSON and the report share the calculation. YFOR September 16 **17:15 = 4.1814x local**; **17:20 = 25.5041x local but 0.5252x the prior-session maximum**. The older 4.2x label belongs to the ignition, not the 941,842-share later bar. Local 10x alone therefore does not reproduce Juan's cross-session objection. Network execution, archived replay, compilation, future-bar independence, missing/zero-baseline behavior, prior coverage and DST bounds passed. This completes both named process-review handoffs; consumer wiring is the next instrumentation step, with decision rules intact.

**Initiative 6 evaluation, October 1:** The 04:10:21 ET prospective snapshot contains 21 names; all four later selected tracker names (SDEV, QSI, LPA, BURU) have AH footprints and are absent from it. There are zero tracked PM-only cases and zero positive-size asks <=60 seconds old; quote ages are 40,250–43,821 seconds. The script rerun preserves the completed 26-row ledger (+4.4% modeled gross/admit, approximately +2.4% after assumed spread; all classes 35/+3.4% gross). This is **insufficient new pilot evidence**, not an additional edge. No claim about untracked cohort outcomes or real fills follows. The pilot check used its budget; parallel work supplied today's progress.

**Initiative 4 evaluation, October 1:** The latest entry's reporting hypothesis worked: successful InboxKit receipt 176 (`2026-10-01T09:37:54.944392+00:00`) and the archived September 30 HTML report include Initiatives 3, 4 and 6. Today's later metric and pivot work belong in the next email. No separate message was sent.

## Initiative 7 — Alternative agent strategies and executable universe

**Status:** **RESEARCH opened 2026-10-01** under Juan's September 1 deadline directive. Source comparison and proposed research direction are in `docs/investigations/init7-agent-strategy-pivot-2026-10-01.md`.

**Progress October 1:** Compared AI-Trader's hourly Nasdaq-100 tool-using agent, TradingAgents' analyst/debate framework and FinAgent's multimodal memory/reflection approach against two studies of leakage and strategy-search bias. AI-Trader reports MiniMax-M2 +9.56% versus QQQ +1.87% during October 1–November 7, 2025, while GPT-5 returns +1.56%; these are author results, not an edge reproduced on this account. Historical model knowledge and unverified local execution/inference costs prevent adopting the published headline returns. The cheapest next alternative is an **agent-assisted liquid US regular-session strategy**, first checked for data and executable books on AAPL/MSFT/NVDA/AMZN/GOOGL/META/TSLA plus QQQ. Frequency, friction and capacity could address the current stale-book/rare-admit bottlenecks; expected net dollars remain unmeasured.

**Update 2026-10-02 (Juan's October 1 reply, InboxKit 177):** Add **Jev stock classification** to this initiative. Use the `research` skill to find related projects and approaches, including exactly what they classify, their inputs, labels, evaluation method and reported costs. Use the available `typesafe-ai` skill for Jev and read the current API/SDK docs before implementation. Juan reports that the TypeSafe API key is available in the environment. The live documentation index includes [SEC annual-report industry classification](https://docs.typesafe.ai/cookbooks/classification_using_confidence.md) and [feature discovery](https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery.md) as starting points; neither establishes a trading edge. Initiative 4 now requires Jev results and costs in every daily email. See `FEEDBACK_LOG.md` 2026-10-02.

**Next smallest step:** At October 2 15:00 CEST, deliver a sourced comparison of stock-classification projects and select a bounded label/input specification for Jev. Save research in `docs/investigations/`; record its path and next deliverable in `INITIATIVE_LOG.md`. Then build the smallest shadow classification run with the existing environment key, preserving the model/version, dated inputs, labels/probabilities, call/token usage, actual cost or an explicitly labeled pricing estimate, and failures in dated artifacts referenced by the initiative log. Feed those artifacts to the daily email; verify representative cases before drawing trading conclusions. Continue the frozen numerical-control versus bounded-agent comparison with causal timing, equal capital, cash/QQQ comparators and all operating costs. Research and instrumentation proceed alongside Initiative 6.

**Needs from Juan:** consideration of the eventual regular-session/universe direction through the daily email; nothing blocks research. Preserve the deferred broker test.

## Open asks for Juan (consolidated)

- [ ] **Initiative 7 (2026-10-01, core strategy/universe proposal; daily email):** the paper account missed the net-positive checkpoint. Propose evaluating an agent-assisted liquid US regular-session strategy as a replacement candidate for AH→PM micro-caps. Research is active and unblocked; live adoption needs prospective edge and execution evidence plus Juan's review. No live switch, new order or trading schedule change has been applied.

**Broker-ask status refresh (2026-10-01):** the historical Initiative 2 access item below is **deferred per Juan's September 22 instruction**, not a renewed request. Resume only when he supplies access. Existing Initiative 3 schedule-veto and exit-review proposals remain unapplied; no new schedule change is proposed today.

- [ ] Initiative 3 (2026-09-23, schedule-resource veto): **PROPOSAL — retire the four added five-minute observation scans at 22:05, 22:10, 22:20, and 22:25 CET; retain 22:00, 22:15, 22:30, 22:45, and all 23:00-00:30 entry scans.** On Sep 22 the 22:25 scan hit `Codex error: The usage limit has been reached`, then the 22:30, 22:45, 23:00, 23:30, 00:00, and 00:30 sessions hit the same limit; only 2/7 core scans completed. The proposed trim removes **4 agent runs per evening** and restores 15-minute opening spacing while protecting late entry coverage. This changes existing scan timing; **not applied, pending Juan's veto**.

- [x] **APPLIED 2026-07-28 — catalyst taxonomy split (merger-arb ≠ Grade A).**
      The 07-27 proposal drew no veto and DOMO has since **closed at -9.4%**
      (held the full 5-day Grade-A window, peak +14.8%, pinned $3.5-4.5 all
      week), so the split was applied under Juan's standing "apply, don't ask"
      directive: a **definitive fixed-price cash buyout / asset purchase /
      merger agreement is graded D (exit at first premarket opportunity)**, never
      Grade-A-hold; rumored / competing-bid / unfixed-ratio M&A stays
      momentum-gradable. Written into the grading table in
      `prompts/post-market-scan.md`, the Grade-A rules in
      `prompts/position-evaluation.md` (re-grade an open position to D if its
      catalyst is a fixed-price cash deal), and the holding-rules table in
      `OPEN_POSITIONS.md`. `Day Trading.md` needed no edit (it holds no grade
      table). Retroactive veto is fine: say the word and it reverts.
      **Original proposal (2026-07-27):** split the catalyst taxonomy: cash buyouts / definitive
      merger agreements are NOT Grade-A momentum holds (2026-07-27, from Juan's
      07-24 DOMO feedback).** DOMO was graded A (Progress Software $400M all-cash
      asset purchase) and held under the "Grade A → hold up to 5 days, trail
      −20%" rule, but an all-cash deal **pins the price near the deal value and
      kills the AH→PM overnight momentum the strategy depends on** — DOMO sat
      dead ($3.92 entry → brief $4.50 → $3.71, −5.4%) for days. Juan: "I have no
      idea why you're holding that." The Grade-A hold rule was built for
      **operational/momentum** catalysts (BATL gas agreement, VIVS partnership)
      that ignite overnight momentum, not for merger-arb. **Proposed change to
      the `Day Trading.md` / `OPEN_POSITIONS.md` catalyst-grade table:** a
      **definitive cash buyout / merger agreement at a fixed price** is graded
      **None/exit-premarket** (skip at entry, or exit at the first premarket
      opportunity), never Grade-A-hold. Only *rumored/competing-bid* M&A that can
      still re-rate stays momentum-gradable. This edits live holding rules →
      **proposed, not applied by this pulse.** DOMO itself is already exit-flagged
      for the next premarket eval (currently still open at −5.4%; the AH book is a
      ~30% spread, so exit waits for premarket). Silence on this proposal = a
      future `strategy-advance` run applies the taxonomy split and reports it.
- [x] **Standing directive (2026-07-16, reinforced 2026-07-17): apply, don't
      ask.** Juan: "apply stuff, don't ask confirmation" / "don't wait for my
      approval." Stop posing "Decision For You / Needs You / Want me to apply
      it?" questions in the daily email for qualifying, evidence-backed changes —
      apply them (via the owning pulse: `strategy-advance` for `Day Trading.md`
      entry rules, `scanner-improvement` for scanner/process) and report what was
      done, with a **retroactive** veto only. The 07-17 reply closes the
      "live-entry rule = yours to approve" carve-out: **even live-entry rules are
      applied autonomously and reported, not pre-approved.** Reserve email asks
      for decisions the agent cannot execute (infra, broker, funding). Guard
      wired into `prompts/daily-email.md` (2026-07-17). The sub-3M-float PM-open
      re-check exception is held **on evidence, not approval** — SIP-corrected
      count is 3/5 (below the ≥4/5 trigger); `strategy-advance` applies it when
      it next reaches 4/5, without asking.
- [x] **Winner bar tightened (2026-07-16).** Juan (recurring): the email
      headlined a weak +72%/+88.5%, low-volume name (ATPC) as "winner" — the bar
      is **>100% on high, accumulating SIP volume**; below that, report "no real
      winner today." Applied to `prompts/morning-evaluation.md`.

- [x] Initiative 2: Alpaca keys are live (Juan removed the `unset`, 2026-06-23);
      verified against `/v2/account`. Nothing blocking. Optional: set
      `ALPACA_PAPER_TRADE=1` explicitly.
- [ ] Initiative 2 (broker switch): **NEW ASK (2026-09-07)** — open an account so
      the empirical AH-fill test can run. Research (`INIT2_BROKER_ALTERNATIVES.md`)
      picks **IBKR paper as primary** (its fill engine simulates against real
      *consolidated* market data you subscribe to, so AH micro-float limits fill
      where Alpaca's free IEX feed cannot — the direct root-cause fix) and
      **Webull OpenAPI EU as backup** (`developer.webull.eu`, lowest setup).
      Trading 212 rejected (extended-hours market orders only). **To unblock:**
      open an IBKR paper account + enable/share a US-equities data subscription
      with extended-hours consolidated quotes + API access; OR register at
      developer.webull.eu and share App Key/Secret. This *replaces* the old
      08-07 "Alpaca SIP / IBKR / modeled fills" decision (Juan chose switch-broker
      on 09-04). No live switch until the fill test on AKAN/SHPH/GIPR passes.
- [x] Initiative 3: **AH cadence change (A) WIRED (2026-07-17).** The 07-16
      veto window passed with no objection, so the two *observation-only* AH-open
      scans (22:15 + 22:45 CET / 16:15/16:45 ET, Mon–Thu) were added to
      `scheduler.json` — both fire before the 23:00 CET entry ban (no new entry
      window), so they qualify as log-only pulses applied directly. Retroactive
      veto still fine: say the word to remove them. (B) 01:00/01:30 CET tail
      scans remain held (MSW=1, below the 3–4 trigger).
- [ ] Initiative 3: **PROPOSAL (C) — veto window (2026-07-21).** Add
      **23:45 + 00:15 CET (17:45 + 18:15 ET)** post-market scans to 15-min-space
      the *late* AH window (17:00–18:30 ET), mirroring the open-hour densification.
      These are **entry-eligible** (after the 23:00 CET ban), so they change live
      entry behavior → proposed, not applied. Evidence: two late-window movers the
      current 30-min spacing under-caught — CJMB (07-16, traded winner +19.8%,
      caught +27m late) and RDGT (07-20, ignited 18:00 ET, gate-blocked at the
      18:30 final scan, ran to PM +47%; an 18:15 scan would have made it
      entry-eligible). Silence = wire it a future run once the tally is firm;
      say the word to veto. Details in `INIT3_IGNITION_TIMING.md`.
- [ ] Initiative 3 (execution pivot): **FIRMED PROPOSAL — replace the plain
      04:30 ET market exit for Grade-None/held overnight names with a resting
      sell-limit ~+10% above the exit price (GTC through premarket, cancel at
      09:30 ET); keep the 04:30 market exit only as the fallback if unfilled.**
      Evidence (updated 09-11, `scripts/peak-seeking-exit-sim.js`, log-only,
      **n=38 out-of-sample seeds**): the resting +10% sell-limit stays the best
      robust rule at **+100.7% total / +2.6% per name, positive on 24 of 38** vs
      selling at 04:30, beating every trailing stop and non-outlier-driven wider
      limit. It wins because early peakers spike then crash, so a modest resting
      limit fills into the first spike before the dump; today's WHLR-type
      early-spike-then-dump pattern is the canonical case.
      **OCO-stop question is answered (08-21):** the naive breakeven OCO stop is
      **rejected** — it whipsaws nearly every winner (collapses to +1.0%/name,
      positive only 3/28). Only a **wide ~-15% catastrophe-stop** helps at all,
      and only marginally (it rescues the single LOOP-type dumper), so it stays
      **optional, not required**. The clean ask is the plain resting +10%
      sell-limit (GTC premarket, cancel 09:30 ET, plain 04:30 market exit as
      fallback). Changes live exit behavior → **proposed, not applied**. Details
      in the Initiative 3 status + `log/premarket-exit-gap.csv`. **Full-window correction (2026-09-23):** `peak-seeking-exit-sim.js` had used the broker CLI's default 20 five-minute bars (100 minutes), not the full premarket. Fetching 300 bars and capping at 09:30 ET gives **n=44**: the +5% limit returns **+132.7% total (+3.0% per name)**, while the +10% limit returns **+130.1% (+3.0%)**, positive 30/44. The 2.6-point aggregate difference does not distinguish thresholds; this supersedes earlier simulator totals. Keep both thresholds log-only and collect more completed exits; no live exit change is promoted.
- [x] Initiative 6 (problem b): the **partial-hold pilot ask is WITHDRAWN**
      (2026-07-13). `scripts/trailing-sim.js` simulated the trailing-stop hold
      on all 14 closed round-trips' real regular-session 5-min SIP paths; every
      stop width (8/12/15/20%) and both gate configs LOSE vs the all-out-
      premarket baseline (-3 to -5% added return/trade). No Juan action needed —
      the premarket-exit rule stands, and problem (b) needs no `Day Trading.md`
      edit. Init 6 refocuses on problem (a), the holdable PM-only gappers.
- [x] Initiative 6: **veto window** — a new log-only PM-open scan pulse
      (`trading-pm-open-scan-1100`, 11:00 CET / 05:00 ET Mon-Fri) was added
      2026-07-07. It places no orders and changes no existing trading-scan
      timing; it only logs gappers to `log/pm-open-scan.csv`. Juan confirmed
      2026-07-08: keep it ("no need to remove") and granted standing autonomy
      to create pulses ("you're free to create pulses").
- [x] Initiative 5: inline charts in the email body shipped (2026-07-08). With
      the repo public, `daily-email.md` now inlines each chart via
      `raw.githubusercontent.com` `<img src>` (verified HTTP 200), replacing the
      blob links that 404'd for Juan on 06-30. First live use is the next daily
      email; open check is whether the image displays in Juan's Gmail.
- [x] Initiative 5: **AH/PM volume blank fixed** (2026-07-14). `chart.py` now
      backfills extended-hours volume from Alpaca SIP (Yahoo returns vol=0
      there); verified on MIMI (170 bars filled). Closes Juan's escalated
      07-10 ask ("the chart still has no volume in AH"). No Juan action needed.
- [x] Initiative 5: **daily-email render race fixed** (2026-07-16). Added a
      post-push raw-URL HTTP-200 poll to `prompts/daily-email.md` before sending
      (drops any image still not live), closing the 07-09 RPGL-didn't-render
      race. GitHub Pages HTML reports remain the last open Init 5 follow-on. **Update 2026-09-22 18:00 CEST:** added `.github/workflows/pages.yml` to build the latest report and chart assets into a Pages artifact on pushes to `main`; the local build reproduced `reports/2026-09-21/index.html` with one chart, and the public chart URL returned HTTP 200. Pages deployment is delivery-only and does not change trading logic or pulse timing.
- [x] Initiative 6 (problem a): the **holdable PM-only gappers carry no long
      edge** (2026-07-14). `scripts/pm-gapper-sim.js` shows all realistic
      entry×exit combos lose (-8 to -13%/trade); no live-pulse entry rule is
      proposed. `pm-open-scan` stays log-only. No Juan action needed.
