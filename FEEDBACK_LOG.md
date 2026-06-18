# Feedback Log

Feedback from Juan, captured from replies to the daily trading emails (sent as
`zero@inboxkit.cc`). Newest first. Each entry routes to a roadmap initiative, a
scanner/process tweak, or is logged for review.

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
