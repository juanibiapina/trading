# Strategy Roadmap

Bigger changes to the trading system. Each idea gets researched, piloted in a
low-risk way (instrument / paper / shadow), and only promoted to the live cycle
once it has earned evidence. This file is the single source of truth for what we
are working on, what is parked, and what needs Juan.

**Parallelism (2026-07-08, Juan's steer "move faster"):** only the **pilot**
stage is serialized (one live experiment at a time, so P&L stays attributable).
Research, instrument (log-only), and build/delivery work carry no attribution
conflict and near-zero risk, so they run **in parallel** and should not queue
behind the active pilot. Each `strategy-advance` run advances the top pilot step
**plus** clears ready low-risk build/research items (cap ~1-2 extra per run so
runs stay focused and never break the daily cycle).

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
2. **Initiative 3 - adaptive scheduling / faster ignition detection.** Promoted
   to the top research lever (2026-07-15). Init 1's 1-min backtest shows winners
   ignite in a single minute (IVF 16:53 ET) that our ~22:15 CET / 16:15 ET AH
   scan runs *before*, so we see the name flat and catch it late once it's
   already +50-100%. The edge is monitoring frequency / scan timing (catch the
   volume+price co-spike fast), which is exactly this initiative. Next: audit
   which scans fire before vs after the typical ignition window; propose a
   retimed/added AH observation scan (schedule changes -> propose to Juan).
3. **Initiative 5 - better data + review surface (graphs, sources).** AH/PM
   volume backfill shipped (2026-07-14). Ready low-risk follow-ups: the post-push
   raw-URL 200-check (fixes the Gmail render race) and GitHub Pages HTML reports
   (richer review surface). Juan-facing; clear as parallel low-risk items.
4. **Initiative 6 - catch the extreme runners (+300-600%).** **No longer an
   active pilot** (2026-07-15): both structured levers tested negative (problem a
   PM-gapper long -8 to -13%/trade; problem b trailing-stop hold -3 to -5%/trade).
   `pm-open-scan` stays cheap log-only accumulation. Only surviving thread is a
   possible intraday momentum-continuation re-entry — parked pending a bigger
   sample. Re-open only if the accumulating gapper data changes the picture.
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

**Idea (Juan):** The fixed schedule may have pulses at the wrong moments. Allow
adapting how often and when we scan/evaluate — space some out, simplify or add
others, adapt to market conditions and time zones. Keep cost in mind; don't run
constantly.

**Status:** In progress — **promoted to the top research lever (2026-07-15).**
The daily **`strategy-advance` pulse** (2026-06-23) was the first deliverable.
Init 1's 1-min backtest (`INIT1_VOLUME_LEAD.md`) gives this initiative concrete
evidence: winners ignite in a single minute (IVF 16:53 ET) and our AH scan at
~22:15 CET / **16:15 ET runs ~38 min *before* that ignition**, so we see the
name flat and only catch it on a later scan once it is already +50-100% — the
"we catch late" problem is a **scan-timing / monitoring-frequency** problem, not
a missing signal. Next: audit each recent winner's ignition time (ET) vs our
scan grid to quantify how often the AH scans fire before ignition, then propose
a retimed/added AH observation scan (a trading-scan timing change -> propose to
Juan for veto, don't apply silently).

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

**Status:** **Instrument — ACTIVE (2026-07-14).** **Update 2026-07-14 — the
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

## Open asks for Juan (consolidated)

- [x] Initiative 2: Alpaca keys are live (Juan removed the `unset`, 2026-06-23);
      verified against `/v2/account`. Nothing blocking. Optional: set
      `ALPACA_PAPER_TRADE=1` explicitly.
- [ ] Initiative 3: confirm whether to trim/retime the scan schedule once the
      audit proposes a plan.
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
- [x] Initiative 6 (problem a): the **holdable PM-only gappers carry no long
      edge** (2026-07-14). `scripts/pm-gapper-sim.js` shows all realistic
      entry×exit combos lose (-8 to -13%/trade); no live-pulse entry rule is
      proposed. `pm-open-scan` stays log-only. No Juan action needed.
