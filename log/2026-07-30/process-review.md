# Process Review — 2026-07-30

## Sessions Reviewed
Five most recent completed sessions before this review (timestamps are UTC):

- 2026-07-30 08:30 — position evaluation
- 2026-07-30 09:00 — pm-open scan
- 2026-07-30 09:30 — daily email
- 2026-07-30 12:20 — scanner improvement
- 2026-07-30 12:30 — position evaluation

## Issues Found

### `scan.py --help` crashed on percent formatting
- **Severity:** Minor
- **Sessions affected:** 1 out of 5 reviewed
- **Symptom:** the scanner-improvement verification ran `python3 scripts/scan.py --help` and got `ValueError: unsupported format character 'm'`. The command was in a semicolon-separated shell call whose final command succeeded, so the tool result was not marked as an error.
- **Root cause:** the `--day-movers` help string passed through both Python `%` formatting and argparse's help formatting. Escaping percent signs for only the first pass left a bare `%` for argparse.
- **Fix:** the scanner-improvement session doubled the escapes for both formatting passes in `scripts/scan.py`, then verified `--help`, Python compilation, and `git diff --check`. Commit `5a1d2fc` is pushed.
- **Status:** Fixed

## Health Checks

- No blocking errors. All five sessions completed their tasks; four committed and pushed, and the daily email sent with InboxKit id 76.
- No command was retried three or more times.
- The pm-open scan had one over-broad CSV assertion against all historical rows. It narrowed the check to the three appended rows and passed on the next attempt. This occurred once and does not warrant a prompt change.
- The first position evaluation tried to read the new calendar day's log before creating it, producing one `ENOENT`, then created the log and completed. No repeat was found in recent workload sessions.
- One chained `rg` call returned nonzero because its second search had no matches. It did not affect the task.
- No command-not-found, permission, PATH, package, SIP 403, or websearch invocation failures occurred in the reviewed sessions.
- No closed issue from prior reviews recurred. The 2026-03-24 Python environment issue was not re-verified.

## Needs From Juan

Nothing. The only tooling defect was fixed and pushed by the scanner-improvement session.
