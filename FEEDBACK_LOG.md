# Feedback Log

Feedback from Juan, captured from replies to the daily trading emails (sent as
`zero@inboxkit.cc`). Newest first. Each entry routes to a roadmap initiative, a
scanner/process tweak, or is logged for review.

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
