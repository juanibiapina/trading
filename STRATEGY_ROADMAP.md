# Strategy Roadmap

Bigger changes to the trading system, rolled out **one at a time**. Each idea
gets researched, piloted in a low-risk way (instrument / paper / shadow), and
only promoted to the live cycle once it has earned evidence. This file is the
single source of truth for what we are working on, what is parked, and what
needs Juan.

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

Ranked by the North Star (expected $/time), adjusted for Juan's steer
(2026-06-23) that a working **Alpaca paper account** (path to real money) and a
better **data + review surface** (graphs, sources) are high-value enablers.

1. **Initiative 2 - Alpaca paper trading (foundation, do first).** Cheap now
   (keys work, just build `broker.js`) and it de-risks every other bet: it tells
   us whether our paper fills on micro-float sub-$10 names are even real. If the
   assumed fills do not hold, the current "wins" are partly illusory and the
   edge needs rethinking. It is also the only path to real money, which is the
   goal. Low effort, low risk, high leverage.
2. **Initiative 5 - better data + review surface (graphs, sources).** Juan needs
   to review data to steer, and the work below (especially the Init 6 census)
   should land as something he can actually review. Charts (5m + volume) and a
   stronger data source (Alpaca market data, now available via the Init 2 keys;
   financialdatasets.ai as backup to gappy Yahoo) improve every decision and
   make the loop auditable. Sequenced ahead of Init 6 at Juan's call (2026-06-23).
3. **Initiative 6 - catch the extreme runners (+300-600%).** The biggest raw
   money lever: the current strategy tops out on +20-100% AH movers that fade,
   while the biggest moves keep being PM-only gappers we ignore. Start with the
   cheap census (no new infra), surfaced through the Init 5 review tooling.
   Highest upside, higher uncertainty, so research first and pilot only once the
   data justifies it.
4. **Initiative 1 - earlier volume-lead entries.** Refines the existing edge and
   overlaps Init 6's minute-volume analysis, so it rides on that data work.
   Lower standalone priority.
5. **Initiative 3 - adaptive scheduling.** Ongoing enabler; the strategy-advance
   loop already exists. Retime/add pulses (e.g. the PM-open scan Init 6 may
   need) as evidence accrues. No standalone push.

Done: Initiative 4 (email identity + reply feedback).

## How we roll changes out

1. **Research** — understand the mechanism, the data we need, and the cost.
2. **Instrument** — start logging the signal/metric without acting on it
   (mirrors the proven ceiling-override / dead-cat / PM-only-gapper trackers).
3. **Pilot** — act on it in paper/shadow mode, measure against the baseline.
4. **Promote** — only after evidence (target: a clear edge over several weeks).

Never run more than one initiative in the *pilot* stage at a time, so effects
stay attributable.

---

## Initiative 1 — Earlier entries via a pre-explosion volume signal

**Idea (Juan):** We catch spikes late, once they are already +50-100%. Charts
suggest a volume surge precedes the price explosion. If we detect the volume
ramp (e.g. ~10x normal) we could enter earlier, before the move.

**Status:** Research / not started.

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

**Status:** Alpaca chosen (Juan, 2026-06-19) — **keys now working (2026-06-23).**
Juan removed the `unset` line so `ALPACA_API_KEY` / `ALPACA_SECRET_KEY` /
`ALPACA_BASE_URL` inherit from the parent env. Verified against `/v2/account`:
paper account ACTIVE, $100k, `paper-api.alpaca.markets`. Unblocked — next step is
to build the broker integration (shadow mode). `ALPACA_PAPER_TRADE` is still
empty, but the base URL already points at the paper endpoint.

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
2. Build `scripts/broker.js` (or .py): submit/track paper orders, read fills.
3. Shadow mode: mirror existing paper entries/exits as Alpaca paper orders,
   compare real fills to our assumed prices for a few weeks.
4. Switch the paper-trade ledger to use real fills.
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

**Status:** Research / backlog. Data-source upgrade is newly unblocked — the
Alpaca keys (Init 2) now provide a market-data API for bars/quotes.

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

**Idea (Juan):** The fixed schedule may have pulses at the wrong moments. Allow
adapting how often and when we scan/evaluate — space some out, simplify or add
others, adapt to market conditions and time zones. Keep cost in mind; don't run
constantly.

**Status:** In progress — the daily **`strategy-advance` pulse** (2026-06-23) is
the first deliverable: a loop that advances this roadmap one initiative per day
and is explicitly allowed to add/retime pulses as part of this initiative. Next:
audit which pulses produce actionable output vs run empty, then propose a
trimmed/retimed schedule.

**Current schedule (cron, Europe/Berlin local time):**
- Post-market scans: 21:30, 22:00, 22:30, 23:00, 23:30, 00:00, 00:30 (7 scans)
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

---

## Initiative 4 — Email identity + reply-driven feedback loop

**Idea (Juan):** Send the daily email as **zero** (via InboxKit) instead of from
Juan's Gmail. Add a pulse that checks for replies to those emails; replies are
the channel for Juan's feedback to feed back into the system.

**Status:** DONE (initial setup) — iterating.

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

**Idea (Juan, 2026-06-23):** For weeks the daily winner has been a +20-100%
AH->PM mover. Juan wants the system to also catch the rare +600% explosions
("600% and others like that"), not just the moderate movers.

**Status:** Research / backlog.

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
1. Quantify: over the last ~6 weeks, list every +200% mover (AH or PM) and tag
   each detectable / PM-only-gapper / uninvestable-spike. Use the PM-only-gapper
   tracker already running in the morning eval as the seed dataset.
2. If a tradable subset exists, instrument a PM-open scan (log only, no action).
3. Pilot hypothetical entries on that subset; compare to the current strategy.
4. Promote only if the extreme-runner capture beats current net of false spikes.

**Needs from Juan:** nothing yet (research uses existing data + the gapper
tracker).

---

## Open asks for Juan (consolidated)

- [x] Initiative 2: Alpaca keys are live (Juan removed the `unset`, 2026-06-23);
      verified against `/v2/account`. Nothing blocking. Optional: set
      `ALPACA_PAPER_TRADE=1` explicitly.
- [ ] Initiative 3: confirm whether to trim/retime the scan schedule once the
      audit proposes a plan.
