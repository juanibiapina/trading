# Feedback Log

Feedback from Juan, captured from replies to the daily trading emails (sent as
`zero@inboxkit.cc`). Newest first. Each entry routes to a roadmap initiative, a
scanner/process tweak, or is logged for review.

---

### 2026-06-26 — re: Trading Scanner Report - 2026-06-26

**Juan said:** "+760% is exactly the kind of stuff we want to catch!! it's
really important to try to extract patterns from those for the future!"

**Interpretation:** Strong endorsement of Initiative 6 (catch the extreme
runners). The ILLR +760% case — detected by the scanner but correctly skipped
on the extension ceiling + zero AH volume — is the target profile, not a miss.
Juan wants emphasis on **pattern extraction** from these extreme movers (the
ceiling-watch dataset), so future cycles can recognize and act on the setup
rather than only flagging and skipping. Pattern mining of the big movers is now
an explicit priority within Init 6, ranked alongside the "catch them" goal.

**Action:** Routed to Initiative 6. Added a pattern-extraction work item to its
rollout plan (systematically characterize each ceiling-watch / extreme-runner
name: catalyst tier, float, AH-vs-PM timing, volume profile, price path) so the
dataset produces reusable entry/skip signals. No live strategy change here;
captured and routed. Confirmed the scanner's ILLR skip was the correct call —
the gap is downstream pattern learning, not the skip logic.

---

### 2026-06-24 — re: Trading Scanner Report - 2026-06-24

**Juan said:** "yes, apply the scheduler changes if you need to"

**Interpretation:** Standing approval to add the 1-2 late post-market scans
(~01:00/01:30 CET) that the late-AH-tail tracker is building a case for. The
"if you need to" is conditional: apply when the data warrants, not
automatically. This clears the Initiative 3 blocker ("approval of any schedule
change before applying") for this specific change.

**Action:** Recorded the standing approval; did **not** add the scans yet. The
late-AH-tail tally is at 1 (ORIS, Jun 22); the tracker's own trigger for adding
late scans is a cluster of >=3-4 winners in the 18:30-20:00 ET tail. Applying
now would be guessing ahead of the data. Updated Initiative 3 to mark the
schedule change pre-authorized so the next qualifying night can apply it without
a fresh ask. Routed to: Initiative 3 (schedule) + late-AH-tail tracker.

---

### 2026-06-23 — north star: make the most money, fast (chat)

**Juan said:** "The goal is to make the most amount of money fast. Somehow this
should drive our decision making. The strategy itself can be adapted."

**Interpretation:** The objective function is account-growth rate, not detection
rate. Detection baseline / win rate / clean process are proxies, valuable only
when they convert to faster money. The core AH->PM strategy is a hypothesis that
can be replaced if another approach compounds faster. This should be the lens
the daily loops prioritise by.

**Action:**
- Added a **North Star** section to the top of `STRATEGY_ROADMAP.md`: objective
  = most money fast; proxies are subordinate; core strategy is adaptable; rank
  work by expected dollars-per-unit-time (edge x frequency x scalability less
  effort/uncertainty); proof before scale; don't go broke; strategy pivots
  touching `Day Trading.md` / live trading are proposed to Juan.
- Wired `prompts/strategy-advance.md` to this lens: added a North Star block and
  changed initiative selection to rank by money-fast impact, with explicit
  permission to add a new initiative (incl. core-strategy/universe change) if it
  is the highest lever.

---

### 2026-06-23 — re: Trading Scanner Report - 2026-06-22

**Juan said:** "I think the env vars are there! I removed the unset on zero's
.envrc, so they should appear from the parent env. Also, for a long time the
winners are 20 to 100%. I was hoping you could catch 600% and others like that."

**Interpretation:** Two points. (1) The Alpaca blocker is resolved — Juan
removed the `unset` line so the keys now inherit from the parent env. (2) New
strategic want: the daily winner has been a +20-100% AH->PM mover for weeks, but
he wants the system to catch the rare +600% explosions too. Those big movers are
typically the PM-only gappers (GLXG +343%, etc.) and extreme runners the current
AH->PM scanner structurally misses or scans too early to see.

**Action:**
- Initiative 2 (Alpaca): **unblocked.** Verified the keys are now live in the
  env (`ALPACA_API_KEY` / `ALPACA_SECRET_KEY` / `ALPACA_BASE_URL` all set) and
  hit `/v2/account` — paper account is ACTIVE, $100k, `paper-api.alpaca.markets`.
  Updated Initiative 2 status to keys-working / build broker integration next.
  Checked the consolidated Alpaca ask off. Note: `ALPACA_PAPER_TRADE` itself is
  still empty, but the base URL already points at the paper endpoint.
- The +600% want: added **Initiative 6 — catch the rare extreme runners
  (+300-600%)** to STRATEGY_ROADMAP.md (research/backlog). It ties to the
  existing PM-only-gapper tracker (the biggest raw movers keep being PM-only
  gappers the AH strategy can't see) and Initiative 1 (earlier volume-lead
  entries). Routed for research, not acted on here.

---

### 2026-06-19 — re: Trading Strategy Roadmap - setup done, slow rollout starting

**Juan said:** "Great! I also want graphs eventually, probably 5m including
volume. The alpaca key should be available."

**Interpretation:** Two points. (1) New want: the daily email should eventually
include charts — 5-minute candles with volume — for the candidates/positions it
reports. (2) Broker decision resolved: go with Alpaca for paper trading, and he
believes the API key is already provisioned.

**Action:**
- Broker choice (Initiative 2): Alpaca is approved. Updated Initiative 2 status
  from "awaiting broker choice" to "Alpaca chosen — building integration."
  Flagged a blocker: `ALPACA_API_KEY` / `ALPACA_SECRET_KEY` are still `unset` in
  zero's `.envrc` (line 7 unsets them). The key is NOT actually available yet —
  noted as an open ask so the next email asks Juan to confirm/paste the keys.
- Charts in email: added Initiative 5 (5m + volume chart attachments in the
  daily email) to STRATEGY_ROADMAP.md, status research/backlog. Alpaca's bars
  API can supply the 5m+volume data once keys land, so this dovetails with
  Initiative 2.

---

### 2026-06-18 — initial strategy direction (chat, not email)

**Juan said:** Time to start changing the strategy, slowly, building evidence
for each change. Four ideas: (1) catch spikes earlier via a pre-explosion
volume signal; (2) move to a real European broker paper account, later live;
(3) adaptive scheduling of pulses; (4) send the daily email as zero via
InboxKit and add a pulse to read replies for feedback.

**Interpretation:** Set up tools + knowledge to work through these gradually,
one pilot at a time. Put anything needing Juan (keys, decisions) in the email.

**Action:** Created `STRATEGY_ROADMAP.md` with all four initiatives. Built
InboxKit send (`scripts/send-email-inboxkit.js`), switched `daily-email.md` to
it, added this reply-check pulse + cron. Asks for Juan consolidated in the
roadmap and sent in the kickoff email.
