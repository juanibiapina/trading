# Report the model used for the daily trading email

Status: Prompt updated on 2026-10-02. The next scheduled email provides the delivery check.

## Goal

Add one footer to every daily trading email showing the selected provider, model ID, and reasoning level of the session sending that email.

## Findings and decision

The current merged Pi settings for the trading directory select `openai-codex/gpt-6.1-sol`. The user chose to make the model visible in each email and leave model selection as it stands.

The 27 trading jobs run as standalone bridge sessions. The daily email job reads `prompts/daily-email.md` at execution time. This prompt owns the HTML body and already requires saving the exact sent HTML to `log/YYYY-MM-DD/daily-email.html` after delivery.

Pi 0.99.1 exposes `PI_PROVIDER`, `PI_MODEL`, and `PI_REASONING_LEVEL` to LLM shell commands. The SDK resolves these values from the current session when each command starts, including for custom bash tools. They identify the selected Pi model; a router's upstream model may differ. Use these runtime values as the evidence for the footer.

## What to change and why

Update only `prompts/daily-email.md`:

1. **The email session's model is read before sending.** Add an instruction in the Send Email step to read `PI_PROVIDER`, `PI_MODEL`, and `PI_REASONING_LEVEL` through the bash tool immediately before finalizing the HTML. Use the returned values rather than inferring them from configured defaults. If a value is missing, show `unavailable` for that value.

2. **Every email contains a compact model footer.** Add one line after the Key Takeaway in the HTML template, labeled `Email session`. Use the exact provider/model ID and reasoning level, with ordinary HTML escaping. For example, when those runtime values are present:

   `Email session: openai-codex/gpt-6.1-sol · reasoning: xhigh`

   Attribute this line to the email session. The overnight work summarized in the email can come from other sessions. The existing saved HTML preserves the footer without adding receipt fields.

## Verification

Review the prompt diff and confirm the model read occurs before sending, the footer appears once, and the template uses runtime placeholders. Check the HTML placement locally without sending an email. This is a reversible prompt edit and needs no new automated tests. The next scheduled email and its saved HTML provide the delivery check. The scheduler reads the prompt on each run, so deployment needs no bridge restart.

## Out of scope

Bridge source changes, scheduled-job refactoring, model-default changes, per-session model reporting for overnight scans, changes to Jev reporting, receipt-schema changes, and resending an earlier email.

## Skills to use

- `documentation` — write the prompt instruction and keep its model-reporting rule in one place.
- `pi` — use the documented shell session metadata.
- `workspace` — edit the trading repository and check its working-tree state.
- `vocabulary` and `deep-modules` — keep this change local to the existing email prompt interface.

## Acceptance criteria

The next daily email includes exactly one `Email session` footer populated from that sending session's runtime provider/model/reasoning values. Missing metadata is labeled unavailable. The saved sent HTML contains the same footer. Model selection retains its current behavior.
