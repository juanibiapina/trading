# Initiative Log

Daily progress on the strategy roadmap (`STRATEGY_ROADMAP.md`), one initiative
at a time. Written by the `strategy-advance` pulse. Newest first.

This is the strategy-level analog of `SCANNER_CHANGELOG.md` (which logs surgical
scanner tweaks). Each entry evaluates the previous step, records the step taken
today, and sets the hypothesis/next step for the following run.

---

### 2026-06-23 — Roadmap re-ranked by money-fast + enablers

**Evaluated:** Loop bootstrap (same day) — done; this is the first prioritisation pass.

**Step taken:** Re-ranked the roadmap under the North Star, weighting Juan's
steer that working Alpaca paper (path to real money) and a better data/review
surface (graphs + sources) are high-value enablers. Added a "Priority order"
section to `STRATEGY_ROADMAP.md` and broadened Init 5 from "charts in email" to
"better data + review surface (charts, sources)."

**Result:** Order is 2 (Alpaca, foundation) -> 6 (extreme runners, biggest raw
lever) -> 5 (data + graphs to review/steer) -> 1 (earlier entries) -> 3
(adaptive scheduling, ongoing). Init 4 done. Key insight driving #1: Alpaca
shadow fills will reveal whether our micro-float paper "wins" are real.

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
