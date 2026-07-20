# Feedback Log

Feedback from Juan, captured from replies to the daily trading emails (sent as
`zero@inboxkit.cc`). Newest first. Each entry routes to a roadmap initiative, a
scanner/process tweak, or is logged for review.

---

### 2026-07-17 — re: Trading Scanner Report - 2026-07-16

**Juan said:** "Beautiful winner. Good job. Improvement: don't wait for my
approval."

**Interpretation:** Reinforcement and sharpening of the 07-16 "apply, don't ask"
directive. The 07-16 email still ran a **"Needs You"** block asking Juan to
approve the sub-3M-float PM-open re-check exception, on the reasoning that "it is
a live-entry rule, so it is yours to approve." Juan is closing that carve-out:
**do not gate changes on his pre-approval, live-entry rules included.** The model
should apply qualifying, evidence-backed changes via the owning pulse and report
them, with only a *retroactive* veto window — no "may I?" asks in the email.
Praise on the CJMB winner (+113% PM) confirms the detection/selection loop is on
target; the only ask is process autonomy.

**Action:**
- Added a guard to `prompts/daily-email.md`: the email must **not** emit
  "Needs You / Decision For You / yours to approve" pre-approval asks for
  strategy or entry-rule changes — those are applied by their owning pulse
  (`strategy-advance`) and *reported* (retroactive veto only). Reserve email
  asks for genuine infra/broker decisions the agent cannot execute itself.
- Updated `STRATEGY_ROADMAP.md` open-asks: the sub-3M-float exception is held
  **on evidence, not approval** — the SIP-corrected count is **3 of 5** (below
  the ≥4/5 trigger), so `strategy-advance` applies it autonomously when it next
  reaches 4/5, no Juan approval sought. The 07-17 email's "Needs You" framing on
  this item was a process regression, now guarded against.
- No live `Day Trading.md` entry-rule edit here (evidence trigger not met; and
  entry-rule scope belongs to `strategy-advance`, not this pulse).

### 2026-07-16 — re: Trading Scanner Report - 2026-07-15

**Juan said:** "The claimed winner in the email barely went up, almost no
volume. Again, we're looking for more than 100% and high volume. Also apply
stuff, don't ask confirmation."

**Interpretation:** Two points. (1) The "winner" bar is wrong. ATPC was
headlined as the winner at +72%/+88.5% on thin volume — that is not a winner.
The target Juan cares about is a real explosion: **>100% move on high volume**.
A weak, low-volume mover should not be crowned winner; if nothing clears the
bar, say "no real winner today." The "Again" signals this is a repeat note.
(2) Standing autonomy directive: **apply qualifying changes and report, do not
pose "Want me to apply it?" questions.** The 07-16 email's "Decision For You"
(sub-3M-float PM-open re-check exception, tally trigger reached) is exactly the
kind of thing to apply rather than ask about.

**Action:**
- Winner bar: edited `prompts/morning-evaluation.md` so "today's winner" must
  clear **>100% (targeting) and high, accumulating SIP volume**; a sub-100% or
  low-volume name is logged as "no real winner today," not crowned. Recurring
  point, low-risk process tweak — applied now. Flagged for the next
  scanner-improvement run to propagate to the email framing.
- Apply-don't-ask: recorded as a **standing directive** in
  `STRATEGY_ROADMAP.md` open-asks. Rewired `morning-evaluation.md` so the
  sub-3M-float exception is **handed to `strategy-advance` to apply and report**
  rather than re-proposed to Juan each morning. The live `Day Trading.md` entry-
  rule edit itself is routed to the `strategy-advance` pulse (its scope), not
  made in this feedback pulse.

### 2026-07-16 — re: Trading Scanner Report - 2026-07-14

**Juan said:** "LvLU is clearly terrible: no volume spike. The other two have
volume spikes. I wonder if we can catch the first volume spike bar. That would
be a great entry point."

**Interpretation:** Two connected points. (1) Absence of a volume spike is a
negative filter — LVLU faded with no AH volume surge, so a no-spike name should
be downgraded or skipped, not held. (2) The *first volume spike bar* is the
ideal entry trigger. This sharpens Init 1's finding: the volume-*lead*
hypothesis was falsified (volume does not precede price), but ignition is a
single-minute price+volume co-spike (IVF 16:53 ET). Juan is asking to enter
*on* that first spike bar, not to front-run it — which is a live, tradeable
reframe of Init 1, not the falsified version. The blocker is detection latency:
our AH scans run on a fixed grid and the spike bar can fire between scans
(KUST/GCTK feed-lag misses this same cycle).

**Action:** Routed to Initiative 1 (reopened as a co-spike *entry-trigger* +
no-spike *negative filter*, distinct from the falsified volume-lead rule) and
Initiative 3 (detection timing — catching the spike bar needs tighter scan
cadence around ignition). Notes added to both. No strategy change applied here
(capture/route only). Feeds the next `strategy-advance` run.

---

### 2026-07-10 — re: Trading Scanner Report - 2026-07-09

**Juan said:** "The chart still has no volume in AH. If you have no data there,
how can we even enter?"

**Interpretation:** Repeat and escalation of the 07-09 AH-volume feedback. The
07-09 report shipped the same blank extended-hours volume panel (Yahoo's 5m feed
carries volume only for the regular session), so nothing visibly changed since
Juan flagged it. His sharper point reframes it from a chart-cosmetics issue to a
decision-integrity one: if the volume panel is empty in exactly the AH window
where we claim our edge, the chart can't justify an entry — and by extension the
scanner's own AH volume numbers (VRatio, the 925K-sh/bar surge cited for GMM)
need a trustworthy source too. This is the data-source-quality half of Init 5,
already its top priority; the escalation means it should be done before the next
cosmetic email work.

**Action:** Routed to Initiative 5, bumped to the immediate next task. Did not
implement here (this pulse captures/routes, no large changes). Concrete step
unchanged from 07-09: merge an extended-hours 5m volume feed into `chart.py`
(Alpaca 5m bars first — keys live via Init 2 — TradingView as fallback, already
used in `scripts/pm-volume-check.py`), populate the pre/post volume panel, scale
bars honestly. Flagged the priority in Init 5's notes for the next
scanner-improvement run to pick up.

---

### 2026-07-09 — re: Trading Scanner Report - 2026-07-08

**Juan said:** "- RPGL chart isn't showing - SUNE chart is showing, yes! but
problem: there's no volume in post market. we need volume in post market!"

**Interpretation:** Two separate issues with the inline email charts (Init 5).
(1) One of the two inline `<img>` charts (RPGL) did not render in Gmail while the
other (SUNE) did. Both raw.githubusercontent PNGs were committed in the same
commit (86cbfb7, 11:30:56 CET) and both return HTTP 200 now, so the files are
fine — this is a Gmail image-proxy race: the proxy fetched RPGL before the raw
CDN had propagated the new commit and cached the miss, while SUNE landed. The
"push before send" step exists but doesn't verify each URL is live first.
(2) The bigger, structural one: the volume panel is empty in the post-market
(and pre-market) region of every chart. Confirmed root cause — Yahoo's 5m chart
feed returns volume ONLY for the regular session (tested AAPL/TSLA: 0/132 pre,
0/97 post bars carry volume; 156/156 regular do). Since our entire AH->PM edge
lives in extended hours, a blank extended-hours volume panel defeats the point
of the chart. This is the data-source-quality half of Init 5.

**Action:** Routed both to Initiative 5. (a) Post-market volume: needs a second
data source for extended-hours 5m volume (Alpaca bars, live keys; or TradingView,
already used in `pm-volume-check.py`) merged into `chart.py` for pre/post bars —
sized so it does not lie about liquidity. Logged as Init 5's next concrete step.
(b) Chart-render race: small process tweak for the daily-email pulse — after
push, poll each raw URL for HTTP 200 (and/or add a short delay) before sending,
so Gmail's proxy never caches a miss. Noted for the next scanner/process run. No
trading logic changed here.

---

### 2026-07-08 — re: Trading Scanner Report - 2026-07-07

**Juan said:** "no need to remove, you're free to create pulses"

**Interpretation:** Reply to the Open Ask about the new log-only PM-open scan
pulse (`trading-pm-open-scan-1100`, added 07-07). Two points: (1) keep that
pulse — do not remove it. (2) Broader grant of autonomy: the loop is free to
create pulses without asking first. This widens the existing log-only-pulse
allowance toward general pulse creation.

**Action:** Resolved the Initiative 6 veto-window open ask (kept the pulse).
Updated the Open Asks list to mark it confirmed and noted the standing
autonomy to create pulses. No strategy change.

---

### 2026-07-07 — re: Trading Scanner Report - 2026-07-06

**Juan said:** "This isn't good. I'd rather catch the bigger jump, not a
'clean 6%'. Remember our goal, which you should always consider when making
decisions: catching BIG wins."

**Interpretation:** Direct reiteration of the North Star and a critique of the
07-06 cycle's framing. The email led with a "clean +6.0%" EDHL exit as the
headline result while TDIC (+65% overnight PM re-ramp) was skipped. Juan is
unhappy that the system is optimizing for and celebrating moderate, safe
movers. Two threads: (1) don't frame a +6% premarket exit as the win — it maps
to Initiative 6 rollout problem (b): the premarket-exit rule caps gains and
stops winners running. (2) Keep prioritizing Initiative 6 (catch the +300-600%
runners); the moderate AH->PM movers are not the target.

**Action:** Routed to Initiative 6 (active). Updated its Status note with this
steer — reinforces PM-open scan priority and flags that the premarket-exit /
no-hold rule is the gain-capping mechanism Juan is pushing against (rollout
problem b, "let winners run"). No unilateral strategy change; the exit-rule
question is a `Day Trading.md` / live-trading change, so it stays a proposal
for the strategy-advance pulse to raise with Juan. Also a process note: the
daily email should stop headlining moderate exits as the "win."

---

### 2026-07-03 — re: Trading Scanner Report - 2026-07-02

**Juan said:** "Make the repo public."

**Interpretation:** Go-ahead for Initiative 5 path (d) — the 07-02 email's Open
Ask offered (c) an InboxKit image feature vs (d) making `juanibiapina/trading`
public + GitHub Pages. Juan picked (d). This unblocks inline charts (public repo
doubles as a zero-auth PNG host, fixing path (a)'s only gap) and enables the
richer HTML-report review surface.

**Action:** Done now. Re-ran the secrets-safety scan (no credentials in tracked
files; `broker.js`, `send-email-inboxkit.js`, `send-email.js` all read keys from
env / `~/.gmcli/accounts.json` outside the repo; only tracked config is the
harmless `.config/dev-session` tmux layout). Set repo visibility to PUBLIC via
`gh repo edit`. Roadmap Initiative 5 updated. Next scanner-improvement / daily-
email run can now wire inline `<img src>` PNGs (GitHub raw / Pages) and publish
HTML reports.

---

### 2026-07-01 — re: Trading Scanner Report - 2026-06-30

**Juan said:** "For the images, can I add a feature to inboxkit that would allow
emails with images? Alternatively, is the trading repo safe to make public? If
so, we could have HTML reports published as GitHub pages."

**Interpretation:** Response to Initiative 5's open ask (inline charts). Juan
offers two new delivery paths beyond the "host a PNG + `<img src>`" plan:
- **(c) InboxKit image feature.** Juan owns InboxKit (repo at
  `~/Sync/notes/zero`), so he can add attachment/inline-image support to the
  send API. This removes the "no attachment API" blocker that killed the
  earlier attach plan.
- **(d) Public repo + GitHub Pages.** Make `juanibiapina/trading` public and
  publish HTML reports (with charts) as GitHub Pages. This also gives a
  zero-auth public host for the PNGs (solving path (a)'s hosting gap) and a
  richer review surface than email — which is the broader Initiative 5 goal.

Secrets check done: no credentials are committed. `broker.js` and
`send-email-inboxkit.js` read all keys (Alpaca, InboxKit) from env vars; the
only config-ish tracked file (`.config/dev-session`) is a harmless tmux layout.
Repo is safe to make public from a secrets standpoint. Decision to publish is
Juan's (it exposes the full strategy + trade history).

**Action:** Routed to Initiative 5. Added paths (c) and (d) to the initiative
and flagged the secrets-safety finding. These are the two most promising routes
(both remove the hosting blocker); path (d) doubles as the "better review
surface" half of Initiative 5. Left the pick to the next strategy-advance /
infra run since choosing between them (and the make-public call) is Juan's.

---

### 2026-06-30 — re: Trading Scanner Report - 2026-06-29

**Juan said:** "The link to the chart didn't work. Also I'd like the chart image
directly in the email. Let me know if inboxkit needs new email features."

**Interpretation:** Path (b) of Initiative 5 (commit charts + link the GitHub
blob URL) has failed on both counts. The `github.com/.../blob/...` link 404s
(verified) because the repo is private — Gmail/anyone not logged into GitHub
can't open it — and a blob URL can never render inline anyway. Juan wants the
chart **embedded in the email body**, not linked. That requires path (a): host
each PNG at a public https URL and inline it with `<img src>`. The "inboxkit
needs new email features" note is a false lead — InboxKit already sends `html`,
and Gmail proxies remote https images; the gap is hosting, not the send API
(InboxKit has no attachment API, confirmed 2026-06-25).

**Action:** Routed to Initiative 5. Flipped the recommended delivery path from
(b) to (a) and marked path (b) dead in the roadmap. Next scanner/infra run: pick
a zero-auth public host for the daily PNG (e.g. a raw-served public gist, R2/
Cloudflare, or a public assets repo) and switch `prompts/daily-email.md` to emit
`<img src>` inline instead of blob links.

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
