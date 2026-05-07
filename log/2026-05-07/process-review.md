# Process Review — 2026-05-07

## Sessions Reviewed

15 sessions spanning May 6-7:
- 2026-05-07T12:20 — Scanner Improvement Review
- 2026-05-07T12:00 — Morning Eval Pulse 3
- 2026-05-07T10:00 — Morning Eval Pulse 2
- 2026-05-07T09:30 — Daily summary email
- 2026-05-07T08:20 — Morning Evaluation (Pulse 1)
- 2026-05-06T22:30 — Post-market scan
- 2026-05-06T22:00 — Post-market scan
- 2026-05-06T21:30 — Post-market scan
- 2026-05-06T21:00 — Post-market scan
- 2026-05-06T20:30 — Post-market scan
- 2026-05-06T20:00 — Post-market scan
- 2026-05-06T19:30 — Post-market scan
- 2026-05-06T12:40 — Daily Process Review (yesterday)
- 2026-05-06T12:20 — Scanner Improvement Review
- 2026-05-06T12:00 — Morning Eval Pulse 3

## Issues Found

### 1. Git pull fix from yesterday is working ✅
- **Severity:** Previously Critical, now resolved
- **Sessions affected:** 0 out of 13 today (was 2/5 yesterday)
- **Symptom:** `git pull` failed with "cannot pull with rebase: You have unstaged changes"
- **Root cause:** Morning-evaluation prompt had vague git pull instructions; sessions between commits left dirty working tree
- **Fix:** Yesterday's process review added `git stash && git pull --ff-only && git stash pop 2>/dev/null || true` to `prompts/morning-evaluation.md`
- **Status:** Fixed — all 3 morning eval sessions today used the resilient pattern with zero errors

### 2. Post-market-scan prompt had same vague git pull instruction
- **Severity:** Wasteful (latent — will fail when working tree is dirty)
- **Sessions affected:** 7 post-market sessions use plain `git pull` without stash
- **Symptom:** Post-market sessions all do bare `git pull` — works only because each session commits before ending. Fragile: any user edit or race condition would break it.
- **Root cause:** `prompts/post-market-scan.md` said "Make sure the repository is clean (stash if needed)" without specifying the exact command
- **Fix:** Updated `prompts/post-market-scan.md` to use the same resilient pattern: `git stash && git pull --ff-only && git stash pop 2>/dev/null || true`
- **Status:** Fixed

### 3. Scanner-improvement and process-review prompts have no git pull step
- **Severity:** Minor (latent)
- **Sessions affected:** 0 currently — works because they run after morning-evaluation which commits+pushes
- **Symptom:** If user pushes changes from elsewhere between morning-eval and these tasks, they'd work on stale code
- **Root cause:** These prompts assume they inherit a clean, up-to-date working tree from the previous task
- **Fix:** Not fixed — both prompts prohibit self-modification. Low risk since they run sequentially after morning-eval.
- **Status:** Noted, no action needed unless it causes problems

## No Other Issues Found

- **python3:** Running directly on PATH — no nix-shell workarounds needed (0/50 calls used nix-shell)
- **No command-not-found errors** across all 15 sessions
- **No Python tracebacks** in any session
- **No excessive retries** — only one benign duplicate (`test -f process-review.md` in daily-email, 2x)
- **Tool call efficiency:** Post-market sessions are lean (7-10 bash calls each). Morning eval Pulse 1 uses more (23 bash) but that's expected — it does the heavy lifting while Pulses 2-3 are lighter (5-12).
- **websearch skill** read only when actually needed (3/15 sessions) — not wasteful
