# Initiative Log

Daily progress on the strategy roadmap (`STRATEGY_ROADMAP.md`), one initiative
at a time. Written by the `strategy-advance` pulse. Newest first.

This is the strategy-level analog of `SCANNER_CHANGELOG.md` (which logs surgical
scanner tweaks). Each entry evaluates the previous step, records the step taken
today, and sets the hypothesis/next step for the following run.

---

### 2026-06-23 — Init 2: first live extended-hours shadow fill

**Evaluated:** Prior step (build broker.js + chart.py) — **worked.** broker.js
runs against the live paper account; chart.py renders. This run advanced the
Init 2 next step (the one pilot slot).

**Step taken:** Added `--ext` (extended_hours) limit-order support to
`scripts/broker.js`, then ran a live premarket shadow round-trip on VTAK
(mirroring today's closed 67-share paper trade). It's 09:00 ET, US premarket.

**Result:** Real fills captured.
- Ext-hours marketable limit BUY 67 VTAK filled at **$1.14 (the ask)**.
- Ext-hours limit SELL 67 VTAK filled at **$1.13 (the bid)**. Position flat, no
  leftover exposure.
- **Core Init 2 question answered: Alpaca paper DOES fill our micro-float
  sub-$10 names in extended hours, at the NBBO bid/ask.** Realistic fill model
  = buy@ask / sell@bid; spread is the real slippage (~1c, ~0.9% round trip on
  VTAK at $1.14). This means our assumed paper "wins" are not pure fiction, but
  each round trip pays the spread.
- Coverage caveat: VTAK and SKYQ had fresh 09:00 ET premarket IEX quotes; EHGO's
  quote was stale (prior close) — some names may not fill in extended hours.

**Hypothesis / next step:** Over the next sessions with open paper positions,
mirror real entries/exits as Alpaca ext-hours orders and tabulate assumed price
vs ask(entry)/bid(exit) to measure how much paper P&L survives realistic fills.
If the spread routinely eats a big share of the edge on the cheapest names, that
reshapes entry sizing/price selection.

**Needs from Juan:** nothing blocking. (Heads-up: the Init 2 pilot places real
paper orders on Alpaca during market/extended hours — still paper, no real
money. Today's test round-tripped one position and left the account flat.)

---

### 2026-06-23 — Init 2 broker + Init 5 chart prototype built

**Evaluated:** Re-rank (same day) — acted on it by working the top two priorities.

**Step taken:** Two next steps, both log-only / paper (no live-trading or pulse
rule changes, so no Juan sign-off needed):
- **Init 2:** built `scripts/broker.js` (Alpaca paper CLI, no deps) and tested
  the full path against the live paper account — account/positions, order
  submit -> new -> cancel, live quote, asset tradable lookup.
- **Init 5:** built `scripts/chart.py` (dependency-free 5m+volume candlestick,
  Yahoo data, AH/PM shading, SVG -> PNG) and verified on ORIS and VTAK.

**Result:**
- Micro-float names are tradable on Alpaca (VTAK, ORIS `tradable=true`) — the
  universe is not blocked. De-risks Init 2.
- Alpaca free IEX bars are sparse; Yahoo stays the history/5m source, Alpaca is
  for live quotes + real fills. Settled the data-source question for Init 5.
- ORIS chart visibly shows the AH->PM pattern (build in after-hours, premarket
  spike to ~$5.85 then fade) — a usable review surface.

**Hypothesis / next step:**
- Init 2 pilot: shadow-mirror paper entries/exits as Alpaca paper orders during
  market hours; compare assumed vs real fills (this is the one pilot slot).
- Init 5: confirm InboxKit attachment API, then attach charts to the daily
  email so Juan reviews them in-channel.

**Needs from Juan:** nothing blocking. (Heads-up: the Init 2 pilot will place
real paper orders on Alpaca during market hours — still paper, no real money.)

---

### 2026-06-23 — Roadmap re-ranked by money-fast + enablers

**Evaluated:** Loop bootstrap (same day) — done; this is the first prioritisation pass.

**Step taken:** Re-ranked the roadmap under the North Star, weighting Juan's
steer that working Alpaca paper (path to real money) and a better data/review
surface (graphs + sources) are high-value enablers. Added a "Priority order"
section to `STRATEGY_ROADMAP.md` and broadened Init 5 from "charts in email" to
"better data + review surface (charts, sources)."

**Result:** Order is 2 (Alpaca, foundation) -> 5 (data + graphs to review/steer)
-> 6 (extreme runners, biggest raw lever) -> 1 (earlier entries) -> 3 (adaptive
scheduling, ongoing). Init 4 done. Juan put 5 before 6 (2026-06-23) so the
census and big-mover work land as something he can review. Key insight driving
#1: Alpaca shadow fills will reveal whether our micro-float paper "wins" are real.

**Hypothesis / next step:** Next run starts Init 2 — build `scripts/broker.js`
against the live paper account (submit/track orders, read fills), then shadow
the existing paper entries/exits to compare assumed vs real fills.

**Needs from Juan:** nothing blocking.

---

### 2026-06-23 — Loop bootstrapped

**Evaluated:** n/a — first entry.

**Step taken:** Created the `strategy-advance` daily pulse (`prompts/strategy-advance.md`)
and this log. The loop walks `STRATEGY_ROADMAP.md` one initiative at a time
(Research -> Instrument -> Pilot -> Promote), one small step per day.

**Result:** A daily mechanism now exists to move strategy initiatives, mirroring
the scanner-improvement loop. Current roadmap state: Init 2 (Alpaca) unblocked
and ready to build; Init 6 (catch extreme runners) at research; Init 1, 3, 5 at
research/backlog.

**Hypothesis / next step:** First real run should pick the active initiative.
Likely order: (1) Init 2 — build `scripts/broker.js` against the live paper
account; then (2) Init 6 — the +200%-mover census. Init 3 (adaptive scheduling)
is the loop's own domain and can retime pulses as evidence accrues.

**Needs from Juan:** confirm the pulse cadence/time (proposed: daily 15:00
Berlin, after process-review).
