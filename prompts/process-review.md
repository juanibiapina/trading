Review recent pi session logs for operational problems — not trading quality, but process quality.

This runs daily after scanner-improvement. The goal: catch systemic issues where automated sessions waste time, fail repeatedly, or work around broken tooling.

**The python3 example:** for weeks, every session failed on `python3 scripts/scan.py`, then spent time discovering a nix-shell workaround. No existing task caught this because they all focused on trading outcomes, not operational health. This task would have caught it on day one.

## What To Look For

1. **Repeated errors** — the same command failing across multiple sessions (missing tools, bad paths, permission errors)
2. **Workarounds** — sessions discovering the same fix every time instead of it being permanent (e.g., nix-shell for python3)
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
| **Critical** | Blocks the session from completing its task | python3 not on PATH |
| **Wasteful** | Session completes but burns time/tokens on workarounds | Retrying with nix-shell every time |
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

### 6. Send Daily Summary Email

This is the last task in the daily cycle. Send an HTML email summarizing everything: morning evaluation, scanner improvement, and process review.

Read today's data from:
- `log/YYYY-MM-DD/log.md` (morning eval results, paper trades, today's winner)
- `SCANNER_CHANGELOG.md` (latest scanner improvement entry)
- `log/YYYY-MM-DD/process-review.md` (process issues found, if any)

Use the HTML email script (not gmcli -- it doesn't support HTML):

```bash
node scripts/send-email.js \
  --to juanibiapina@gmail.com \
  --subject "Trading Scanner Report - YYYY-MM-DD" \
  --body '<div style="font-family: -apple-system, Arial, sans-serif; max-width: 600px; margin: 0 auto; color: #333;">
<h2 style="color: #1a1a1a; border-bottom: 2px solid #e0e0e0; padding-bottom: 8px;">Overnight Cycle: [date range]</h2>

<h3 style="color: #555; margin-top: 20px;">Post-Market Scans</h3>
<p>[How many scans ran, unique tickers, notable movers]</p>

<h3 style="color: #555;">Today&rsquo;s Winner</h3>
<p><strong>[TICKER]</strong> ([sector]) &mdash; [catalyst]<br/>
AH entry: $X &rarr; PM peak: $X (<span style="color: #2e7d32; font-weight: bold;">+X%</span> hypothetical)</p>
<p>Scanner caught it? <strong style="color: #2e7d32;">YES</strong> or <strong style="color: #c62828;">NO</strong> &mdash; [brief reason if missed]</p>

<h3 style="color: #555;">Baseline Status</h3>
<p style="font-size: 18px; background: #f5f5f5; padding: 10px; border-radius: 4px;">Detection rate: <strong>X/Y (X%)</strong> &mdash; Target: &gt;80%<br/>
<span style="color: #1976d2;">[BASELINE MET / NOT MET]</span></p>

<h3 style="color: #555;">Paper Trades</h3>
<p style="font-size: 18px;">Paper P&amp;L: <span style="color: #2e7d32; font-weight: bold;">+$X (+X%)</span> or <span style="color: #c62828; font-weight: bold;">-$X (-X%)</span></p>
<p style="background: #f5f5f5; padding: 10px; border-radius: 4px;">Cumulative Paper P&amp;L: [running total]</p>

<h3 style="color: #555;">Scanner Improvement</h3>
<p>[What changed, brief hypothesis]</p>

<h3 style="color: #555;">Process Review</h3>
<p>[Issues found and severity, or "No issues found - all sessions ran clean."]</p>
<p>[If any issues need user action, highlight them here]</p>

<h3 style="color: #555;">Key Takeaway</h3>
<p style="background: #e3f2fd; padding: 10px; border-radius: 4px; border-left: 4px solid #1976d2;">[One sentence: the single most important thing from this cycle]</p>
</div>'
```

**Formatting rules:**
- Subject: use ASCII only -- use `-` not em dashes (they break encoding)
- Body: HTML with inline styles (email clients strip `<style>` tags)
- Use `&amp;` for `&`, `&mdash;` for em dashes, `&euro;` for euros
- Color wins green (`#2e7d32`), losses red (`#c62828`)
- Keep it short -- scannable on a phone in under 30 seconds
