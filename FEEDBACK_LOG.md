# Feedback Log

Feedback from Juan, captured from replies to the daily trading emails (sent as
`zero@inboxkit.cc`). Newest first. Each entry routes to a roadmap initiative, a
scanner/process tweak, or is logged for review.

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
