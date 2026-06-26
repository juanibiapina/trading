# Initiative Log

Daily progress on the strategy roadmap (`STRATEGY_ROADMAP.md`), one initiative
at a time. Written by the `strategy-advance` pulse. Newest first.

This is the strategy-level analog of `SCANNER_CHANGELOG.md` (which logs surgical
scanner tweaks). Each entry evaluates the previous step, records the step taken
today, and sets the hypothesis/next step for the following run.

---

### 2026-06-26 — Init 5: charts wired into the daily email (path b)

**Evaluated:** Prior step (2026-06-25 Init 5: default to path (b) and wire
chart.py PNGs + repo links into the daily-email pulse if Juan doesn't object) —
**proceeded; Juan didn't object.** No new feedback touched chart delivery (the
only feedback since, 2026-06-24, was the scheduler approval), so the (b)
recommendation stands and was applied.

**Step taken:** (1) Proved the chart pipeline end-to-end on today's *real*
reported tickers, not just old samples: `chart.py ILLR --range 2d` and
`chart.py IVF --range 2d` rendered into `log/2026-06-26/` (49 KB / 44 KB PNGs).
Visually confirmed the ILLR PNG shows the full AH->PM pattern (regular climb ->
after-hours build to ~$4.20 amber -> premarket spike to ~$7 then fade blue, with
the early volume surge). (2) Wired path (b) into `prompts/daily-email.md`: a new
"Generate Charts" step runs `chart.py` for the winner + each open Alpaca position
into `log/YYYY-MM-DD/`, and a "Charts (5m + volume)" email section links each PNG
via its GitHub blob URL. Log-only change; no trading logic touched.

**Result:** The daily email now has an auditable chart surface with zero new
infra (no host, no attachment API). `convert` (ImageMagick) is present, so the
pipeline runs in the cron environment. Charts ride the existing
`log/YYYY-MM-DD/TICKER-HHMM.png` convention and are committed by the cycle's git
step, so the email links resolve for Juan (authenticated to the private repo).

**Hypothesis / next step:** Tomorrow's daily email is the first live use. Next
run: confirm the email actually rendered a Charts section and that the GitHub
blob link displays the committed PNG when opened (resolves only after the
cycle's push). If links work, Init 5's email-charts rollout step is done and the
focus shifts to data-source quality (the second half of Init 5) or hands the
pilot slot to Init 6 (the +200%-mover census, now surfaceable through these
charts).

**Needs from Juan:** nothing blocking. Optional: if he'd rather not click into
the repo, he can ask for inline hosted images (path a) instead.

---

### 2026-06-25 — Init 2 promoted to live paper; Init 5 attachment path resolved

**Evaluated:** Prior step (2026-06-24 Init 2: decide shadow-pulse vs wire-into-pulses
to capture fills at entry/exit) — **overtaken by events, resolved.** The
scanner-improvement loop already wired `broker.js` directly into the trading
pulses (commits `0c43af9` "switch to Alpaca paper execution; clean break from
fictional ledger" and `a508bfe`): `post-market-scan.md` now submits real
ext-hours Alpaca paper buys, `position-evaluation.md` submits real sells, and
`morning-evaluation.md` / `OPEN_POSITIONS.md` treat Alpaca as the source of
truth. Real fills are captured natively at entry/exit — exactly what the
shadow-fills comparison (rollout steps 3-4) was meant to achieve, so that
approach is moot. **Init 2 is effectively promoted to the live paper cycle;
only step 5 (real money, tiny size) remains, gated on a proven edge + Juan.**
Account `PA37U2Y192A7` verified flat at $99,998.41 (no open positions; two old
VTAK validation round-trips paid ~$1.59 total spread).

**Step taken:** With the single pilot slot freed, switched the active initiative
to **Init 5** (next by priority; Juan needs a review surface to steer the now-
live paper P&L). Resolved Init 5's blocking question — whether InboxKit supports
attachments — by reading the authoritative OpenAPI spec
(`https://inboxkit.cc/api/openapi.json`), then re-verified the chart renderer on
today's winner AZI.

**Result:**
- **InboxKit `POST /api/messages` supports only `to`, `subject`, `text`, `html`
  — NO attachment/multipart field.** The "attach PNG to the daily email" plan
  is dead. (Spec is the source of truth; no guessing against the live sender.)
- `chart.py AZI --range 2d` renders the full AH->PM pattern (flat ~$1.25 ->
  after-hours spike to ~$2.34 -> premarket fade to ~$1.79, volume panel intact),
  50 KB PNG. The renderer is healthy on current data; only delivery is blocked.
- Two delivery paths survive: (a) inline `<img src="https://...">` with a hosted
  PNG (Gmail proxies remote https images; base64 data URIs are stripped, so no);
  (b) commit charts to the daily log dir (existing `TICKER-HHMM.png` convention)
  and link from the email — Juan is authenticated to the repo, zero hosting.
  Leaning (b).

**Hypothesis / next step:** If Juan confirms (b) (or doesn't object), wire the
daily-email pulse to generate `chart.py` PNGs for the reported winner + any open
positions into `log/YYYY-MM-DD/` and add repo links in the email body — a
log-only change to `daily-email.md`, no trading-logic impact. Verify the links
resolve before relying on them.

**Needs from Juan:** confirm chart delivery preference — (b) committed charts +
email link (recommended, no hosting) vs (a) inline images needing a public host.
Not blocking; will default to (b) next run if no objection.

---

### 2026-06-24 — Init 2: second ext-hours round-trip + shadow-fills ledger

**Evaluated:** Prior step (first VTAK ext-hours round-trip, buy@ask/sell@bid) —
**worked and now replicated.** A second VTAK round-trip this morning filled the
same way: BUY 86 @ **$1.35 (ask)**, SELL 86 @ **$1.34 (bid)**, flat. The fill
model holds on a second occasion.

**Step taken:** It's 09:00 ET (US premarket), account flat. Ran a fresh VTAK
ext-hours shadow round-trip (86 sh, mirroring today's real paper size), checked
EPOW (today's other paper name) for ext-hours fill viability, and started a
persistent ledger `log/shadow-fills.csv` to accumulate assumed-vs-real fill
comparisons. Then applied the fill model to today's two closed paper trades.

**Result:**
- VTAK BUY @ $1.35 = ask, SELL @ $1.34 = bid. Spread held at **1c** even at the
  higher price, so relative round-trip cost shrank to **0.74%** (vs 0.88% at
  $1.14 yesterday). Cheaper the name, bigger the relative spread bite.
- EPOW ($0.52, sub-$1) had **no fresh ext-hours quote** (ask $0.00, stale
  06-23 20:00 ET close) — would **not** have filled in extended hours. Coverage
  gap is worst on the cheapest names (matches yesterday's EHGO caveat).
- Spread cost on today's real paper trades (1c/leg): VTAK (+70.7%) loses only
  ~1-2% of its gain — survives easily. EPOW (-10.1%) would have its loss widened
  ~29% and might not have filled at all. **Spread is a rounding error on big
  winners but meaningfully erodes small losers; sub-$1 names carry non-fill
  risk.**

**Hypothesis / next step:** Free-tier Alpaca has no historical NBBO, so past
fills can't be reconstructed — a real assumed-vs-real comparison needs fills
captured *at the moment* of each paper entry/exit. Next run: decide between (a)
a log-only shadow pulse that mirrors open paper positions to Alpaca at the
entry/exit windows, or (b) wiring a shadow order into the scan/eval pulses.
Option (b) changes pulse behavior and must be proposed to Juan; option (a) is a
new log-only pulse and can be built directly. Lean toward (a). Keep appending
to `log/shadow-fills.csv`.

**Needs from Juan:** nothing blocking. Heads-up for the next step: if we mirror
live paper entries/exits automatically, it will place real (paper) Alpaca orders
during scan/eval windows — still paper, no real money.

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
