# Process Review — 2026-09-16

## Sessions Reviewed

All 17 work sessions since the last review (2026-09-15 12:40 UTC) through this
review. Timestamps UTC:

- 2026-09-15 13:00, 19:30, 20:00, 20:15, 20:30, 20:45, 21:00, 21:30, 22:00, 22:30
- 2026-09-16 07:00, 08:20, 08:30, 09:00, 09:30, 12:20, 12:30

Excluded: this review (2026-09-16 12:40).

## Method

Each session is JSONL. `message` records carry either assistant `toolCall` content
parts (`name`, `arguments.command`) or `role: "toolResult"` records (`toolName`,
`isError`, text). Parsed every session programmatically for:

- `isError == true` on any tool result
- identical bash commands repeated 3+ times within a session (retry-loop detection)
- failure keywords in bash *result* text (`command not found`, `no such file`,
  `permission denied`, `traceback`, `modulenotfound`, `403`, `429`, `timeout`,
  `connection refused`, `nix-shell`, `pip install`, `fatal:`)
- workaround/install commands in live bash (`nix-shell`, `sudo`, `pip install`,
  `apt`, `npm install`, `chmod +x`)
- `scan.py` invocations, confirming native execution (no nix-shell fallback)
- git log, confirming each session committed its output

## Findings

- **186 bash calls across 17 sessions. Zero retry loops.** No bash command repeated
  3+ times in any session.
- **scan.py runs native in every session.** 13 real invocations, all `python3
  scripts/scan.py ...`. Zero nix-shell fallback. The 2026-03-24 fix holds.
- **Zero live workaround/install commands** (no `nix-shell`, `sudo`, `pip install`,
  `apt`, `npm install`, `chmod +x`).
- **All 17 sessions committed and pushed** their output (git log shows one commit per
  session task). No stalls, no abandoned tasks. The 07:00 email-reply poll returned an
  empty inbox and exited cleanly (1 bash call) — expected, not a stall.
- **No prompt ships a broken grep pattern.** Every `grep` in `prompts/*.md` uses
  `-l`, `-E` alternation, `-Fn`, or BRE `\|` — all safe under the ripgrep wrapper. The
  two grep failures this window were agent-composed ad-hoc commands, not prompt text.

### Confirmed recurrence: `grep` is a ripgrep wrapper (`grg`)

- **Severity:** Minor
- **Sessions affected:** 2 of 17 (2026-09-16 08:20 morning-eval, 12:20
  scanner-improvement), both self-corrected on the very next bash call.
- **Symptom:** In this environment `grep` is a shell function calling `grg` → `rg`
  (ripgrep 15.2.0). Two GNU-grep idioms fail:
  1. **Attached context number** — `grep -A6 "Price Timeline"` errors with
     `rg: error parsing flag -A: value is not a valid number`. Ripgrep needs the
     number space-separated: `-A 6`. (08:20 session; next call switched to `-E` and
     succeeded.)
  2. **Literal unescaped parens in the pattern** — `grep -n "... (1 ran: XRTX)"`
     errors with `rg: regex parse error: unclosed group`. Ripgrep treats the pattern
     as regex; GNU grep BRE would treat `(` as literal. (12:20 session; next call
     switched to `grep -Fn` and succeeded.)
- **Root cause:** The wrapper interprets patterns and flags as ripgrep, not GNU-grep
  BRE. Also note `grep -r` maps to ripgrep's `--replace`, not recursive search — use
  `rg` for recursion.
- **History:** The 2026-09-15 review logged this as "tracking only" and predicted a
  recurrence would warrant a permanent note. This window is that recurrence (2
  occurrences, 2 distinct session types). It also appeared once in the prior window
  (2026-09-15 12:20). Trend: ~1–2 occurrences per review window, always self-correcting
  at the cost of ~1 extra bash call.
- **Fix:** None applied. The wrapper is a deliberate global NixOS shell config
  (`grep () { grg "$@"; }`), not a trading prompt/script/rule. Overriding it
  system-wide is outside this review's scope and would defeat the intended tooling.
  The prompts are already clean, so there is no surgical prompt fix that would prevent
  agent ad-hoc `grep`. Cost is trivial (~1 extra bash call per occurrence, both
  self-corrected same-session), which does not justify a global environment change or
  routing to the user. Logged as a confirmed low-cost recurring pattern; revisit only
  if frequency climbs enough to justify proposing a shell-config change.
- **Status:** No action needed — confirmed recurring, cost negligible.

### Benign one-off: `xxd` not installed

- **Severity:** Minor
- **Sessions affected:** 1 of 17 (2026-09-16 09:00 pm-open-scan).
- **Symptom:** `tail -c 50 log/pm-open-scan.csv | xxd | tail -2 && ... wc -l ...`
  printed `xxd: command not found`, but the compound command continued and the
  `wc -l` half returned the intended line count (181). The agent was inspecting
  trailing bytes of the CSV; it did not retry `xxd` or seek a workaround.
- **Root cause:** `xxd` is not on PATH in this environment. It is not needed for any
  routine task — this is the only real occurrence across all sessions.
- **Fix:** None. Not a recurring need; installing a hex viewer for one diagnostic is
  disproportionate. `od -c` or `tail | cat -A` cover the same need if it recurs.
- **Status:** No action needed.

## No Systemic Issues Found

Clean window across all 17 sessions. No missing required tools, permission errors,
broken paths, retry loops, rediscovered workarounds, prompt confusion, out-of-order
steps, or stale references. scan.py runs native everywhere; every session committed
its output. The only events were two self-correcting `grep`-vs-ripgrep gotchas (a
confirmed low-cost recurring pattern) and one benign missing-`xxd` diagnostic. No
fixes made; nothing to flag for user action.
