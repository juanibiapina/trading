Check for replies to the trading emails and capture Juan's feedback.

The daily trading summary is sent from Juan's Gmail account
(`juanibiapina@gmail.com`) to the same address. Juan replies in the report's
Gmail thread with feedback. This pulse finds new replies, records the feedback,
and acts on anything quick. It runs once a day.

Load the `gmcli` skill. The gmcli account is always `juanibiapina@gmail.com`.

## Steps

### 1. Find new replies

List recent report threads:

```bash
gmcli juanibiapina@gmail.com search 'subject:"Trading Scanner Report" newer_than:14d'
```

Read each thread:

```bash
gmcli juanibiapina@gmail.com thread THREAD_ID
```

Every message in a thread is from `juanibiapina@gmail.com`. The first message
is the report itself; its ID matches `message_id` in a
`log/*/daily-email.json` receipt. Every later message is a reply from Juan.

A reply is new when its Message-ID does not appear in `FEEDBACK_LOG.md`
(`rg -n 'Gmail message MESSAGE_ID' FEEDBACK_LOG.md`). Do not use the `UNREAD`
label: Juan opening the thread in Gmail marks it read.

If there are no new replies, stop. Do not send anything. Report "no replies".

### 2. Capture the feedback

For each new reply, append an entry to `FEEDBACK_LOG.md` (newest first, after the header):

```markdown
### YYYY-MM-DD — re: [email subject]

**Juan said:** [verbatim or close paraphrase of the feedback] (Gmail message MESSAGE_ID, received YYYY-MM-DD HH:MM UTC.)

**Interpretation:** [what this means for the system]

**Action:** [what you did now, or what roadmap item it feeds, or "logged for review"]
```

The Gmail message ID in the entry is how later runs know the reply was
processed. Leave out the quoted report text below Juan's reply.

If the feedback maps to a `STRATEGY_ROADMAP.md` initiative, update that
initiative's notes/status. If it is a small scanner/process point, note it so
the next scanner-improvement run can pick it up. Do not make large strategy
changes here; capture and route them.

### 3. Commit

```bash
git add -A && git commit -m "feedback YYYY-MM-DD: [brief]" && git push
```

Report a one-line summary of what feedback came in and how it was routed.
