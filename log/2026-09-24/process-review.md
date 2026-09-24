# Process Review — 2026-09-24

## Sessions Reviewed

Five completed work sessions immediately before this review, timestamps UTC:

- 2026-09-24 08:30 — position evaluation
- 2026-09-24 09:00 — premarket-open scan
- 2026-09-24 09:30 — daily email
- 2026-09-24 12:20 — scanner improvement
- 2026-09-24 12:30 — position evaluation

Excluded: this process review at 12:40 UTC.

## Issues Found

### Broker CLI help probes exited with an error

- **Severity:** Wasteful
- **Sessions affected:** 2 of 5 reviewed
- **Symptom:** The 09:30 daily-email session ran `node scripts/broker.js --help` after a successful account query; the combined command exited 1. The 12:30 position-evaluation session made the same probe and received the command list with exit code 1. The 2026-09-23 process review also noted an unsupported help probe.
- **Root cause:** `broker.js` did not recognize `--help`, `-h`, or `help`; its no-argument output did not print the documented usage examples.
- **Fix:** `scripts/broker.js` now prints full usage and exits successfully for those help forms before checking API credentials. `node --check` and all four help forms passed with credentials unset; a real command still exits 1 when credentials are missing.
- **Status:** Fixed

## Additional Checks

- The five sessions made 63 bash calls. No identical bash command ran three or more times.
- No repeated exact-text edit failures, stale read offsets, missing tools, permission errors, or broken paths appeared.
- All five sessions completed their assigned work and pushed their changes.
