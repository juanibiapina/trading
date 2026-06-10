Review recent pi session logs for operational problems — not trading quality, but process quality.

This runs daily after scanner-improvement. The goal: catch systemic issues where automated sessions waste time, fail repeatedly, or work around broken tooling.

**Why this task exists (historical example, now closed):** for weeks every session failed on `python3 scripts/scan.py` and re-discovered a nix-shell workaround. No trading-focused task caught it because they looked at outcomes, not operational health. That specific issue was resolved on 2026-03-24 — **do not re-verify it.** It's named here only to illustrate the *class* of problem to hunt for: a permanent fix that never got made permanent.

**Don't re-litigate closed issues.** Before reporting anything, skim the recent `log/*/process-review.md` entries. If an issue has been confirmed resolved across multiple prior reviews, leave it out — re-confirming dead issues is noise. Only report what's actually happening now.

## What To Look For

1. **Repeated errors** — the same command failing across multiple sessions (missing tools, bad paths, permission errors)
2. **Workarounds** — sessions discovering the same fix every time instead of it being permanent
3. **Excessive retries** — commands being retried 3+ times before succeeding
4. **Token waste** — long debugging sequences that could be avoided with a simple environment fix
5. **Prompt confusion** — sessions misinterpreting instructions, doing steps out of order, or skipping steps
6. **Stale references** — prompts referencing tools, files, or rules that no longer exist

## What You Can Fix

- Environment issues: propose changes to system packages, PATH, shell config
- Prompt clarity: fix ambiguous instructions in `prompts/*.md` that cause confusion
- Missing tools: add scripts or install packages that sessions keep needing
- Stale references: update prompts that reference outdated rules or files

## What You Must NOT Change

- `Day Trading.md` (user-maintained)
- `AGENTS.md` (agent instructions)
- Trading strategy, rules, or position sizing
- This file

## Steps

### 1. Read Recent Sessions

Read the last 3-5 session logs from:
```
~/.pi/agent/sessions/--home-juan-workspace-juanibiapina-trading--/
```

Sessions are JSONL files. For each, look at tool calls and results:
- `bash` tool calls: check for non-zero exit codes, "command not found", repeated attempts
- Patterns across sessions: same error appearing in multiple sessions = systemic issue

Focus on the most recent sessions first. Use grep to scan efficiently:
```bash
# Find failed commands across recent sessions
ls -t ~/.pi/agent/sessions/--home-juan-workspace-juanibiapina-trading--/*.jsonl | head -5 | xargs grep -l "command not found\|exit code\|Permission denied\|No such file"
```

### 2. Identify Issues

For each issue found, classify it:

| Severity | Description | Example |
|----------|-------------|---------|
| **Critical** | Blocks the session from completing its task | A required tool missing from PATH |
| **Wasteful** | Session completes but burns time/tokens on workarounds | Re-discovering the same fix every run |
| **Minor** | Cosmetic or low-impact inefficiency | Unnecessary commands |

### 3. Fix or Report

**For issues you can fix directly** (prompt clarity, stale references, missing scripts):
- Make the fix (small, surgical)
- Document what you changed and why

**For issues requiring user action** (system packages, NixOS config, external tools):
- Document clearly in the log: what's broken, how often it happens, what the fix is
- Flag as "needs user action"

### 4. Update Log

Create or append to `log/YYYY-MM-DD/process-review.md`:

```markdown
# Process Review — YYYY-MM-DD

## Sessions Reviewed
- [list of session timestamps reviewed]

## Issues Found

### [Issue Title]
- **Severity:** Critical / Wasteful / Minor
- **Sessions affected:** X out of Y reviewed
- **Symptom:** [what happens]
- **Root cause:** [why it happens]
- **Fix:** [what was done, or what needs user action]
- **Status:** Fixed / Needs user action

## No Issues Found
[If clean, say so — that's useful data too]
```

### 5. Commit

```bash
git add log/ prompts/
git commit -m "process review YYYY-MM-DD: [brief summary]"
git push
```

*Note: the daily summary email is sent by a separate task (daily-email.md).*
