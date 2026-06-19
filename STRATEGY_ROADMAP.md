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

**Status:** Alpaca chosen (Juan, 2026-06-19) — building integration. Blocked on
working API keys: `ALPACA_API_KEY` / `ALPACA_SECRET_KEY` are still `unset` in
zero's `.envrc`. Juan said the key "should be available" but it is not populated
yet — re-asked in the next email.

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
1. Juan creates an Alpaca paper account, provides API key/secret.
2. Build `scripts/broker.js` (or .py): submit/track paper orders, read fills.
3. Shadow mode: mirror existing paper entries/exits as Alpaca paper orders,
   compare real fills to our assumed prices for a few weeks.
4. Switch the paper-trade ledger to use real fills.
5. Much later, after a proven edge: flip to live with tiny size.

**Needs from Juan:**
- Decide broker (recommend Alpaca for paper).
- Create the paper account and add `ALPACA_API_KEY` / `ALPACA_SECRET_KEY` to
  zero's `.envrc` (and set `ALPACA_PAPER_TRADE=1`).

---

## Initiative 5 — Charts in the daily email (5m + volume)

**Idea (Juan, 2026-06-19):** The daily email should eventually include graphs —
"probably 5m including volume" — for the candidates/positions it reports, not
just text.

**Status:** Research / backlog.

**Findings/notes:**
- Need a data source for 5-minute OHLCV bars. Yahoo's chart API already serves
  5m bars (`interval=5m&range=5d`, with `includePrePost=true` for AH/PM). Alpaca
  bars API (Initiative 2) is another source once keys land.
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

**Status:** Research / not started.

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

## Open asks for Juan (consolidated)

- [ ] Initiative 2: Alpaca chosen ✓. Still need working keys — add
      `ALPACA_API_KEY` / `ALPACA_SECRET_KEY` / `ALPACA_PAPER_TRADE=1` to zero's
      `.envrc` (currently `unset` on line 7). Juan thought they were available;
      they are not populated yet.
- [ ] Initiative 3: confirm whether to trim/retime the scan schedule once the
      audit proposes a plan.
