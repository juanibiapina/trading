Check for replies to the trading emails and capture Juan's feedback.

The daily trading summary is sent from `zero@inboxkit.cc` via InboxKit. Juan
replies to those emails with feedback. This pulse polls for unread replies,
records the feedback, and acts on anything quick. It runs once a day.

## Steps

### 1. Poll InboxKit for unread messages

```bash
KEY=$(grep -E '^export INBOXKIT_API_KEY=' /home/juan/Sync/notes/zero/.envrc | sed -E 's/^export INBOXKIT_API_KEY=//; s/^"//; s/"$//')
curl -s "https://inboxkit.cc/api/messages?unread=true" -H "Authorization: Bearer $KEY"
```

If there are no unread messages, stop. Do not send anything. Report "no replies".

### 2. Read each reply

For each unread message that is a reply to a trading email (subject contains
"Trading Scanner Report" or is clearly trading-related):

```bash
curl -s https://inboxkit.cc/api/messages/ID -H "Authorization: Bearer $KEY"
```

Ignore unrelated mail (do not mark those read; leave them for other workflows).

### 3. Capture the feedback

Append an entry to `FEEDBACK_LOG.md` (newest first, after the header):

```markdown
### YYYY-MM-DD — re: [email subject]

**Juan said:** [verbatim or close paraphrase of the feedback]

**Interpretation:** [what this means for the system]

**Action:** [what you did now, or what roadmap item it feeds, or "logged for review"]
```

If the feedback maps to a `STRATEGY_ROADMAP.md` initiative, update that
initiative's notes/status. If it is a small scanner/process point, note it so
the next scanner-improvement run can pick it up. Do not make large strategy
changes here; capture and route them.

### 4. Mark processed messages as read

```bash
curl -s -X PATCH https://inboxkit.cc/api/messages/ID \
  -H "Authorization: Bearer $KEY" \
  -H "Content-Type: application/json" \
  -d '{"read": true}'
```

### 5. Commit

```bash
git add -A && git commit -m "feedback YYYY-MM-DD: [brief]" && git push
```

Report a one-line summary of what feedback came in and how it was routed.
