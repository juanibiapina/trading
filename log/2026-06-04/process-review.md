# Process Review — 2026-06-04

## Sessions Reviewed
- 2026-06-04T12-30-00 (Position Evaluation)
- 2026-06-04T12-20-00 (Scanner Improvement Review)
- 2026-06-04T08-30-00 (Position Evaluation)
- 2026-06-04T08-20-00 (Morning Evaluation Scanner)
- 2026-06-03T22-30-00 (Post-market scan)
- 2026-06-03T22-00-00 (Post-market scan)
- 2026-06-03T21-30-00 (Post-market scan)
- 2026-06-03T21-00-00 (Post-market scan)
- 2026-06-03T20-30-00 (Post-market scan)

## Issues Found

### HTTP 429 Rate Limiting on Web Search
- **Severity:** Wasteful
- **Sessions affected:** 2 out of 9 reviewed (20:30, 21:00 on June 3)
- **Symptom:** Multiple parallel `websearch search` calls hit Brave API rate limit (Free plan: 1 req/sec). Sessions get 429 errors, then have to wait or skip catalyst searches.
- **Root cause:** Sessions issue 3-4 web search calls simultaneously when searching for catalysts on multiple tickers. The Free plan rate limit is 1 request per second.
- **Fix:** Sessions should serialize web search calls with small delays, or upgrade the Brave API plan.
- **Status:** Needs user action (API plan decision or prompts could instruct serial searches)

### Skill Path Confusion (Occasional)
- **Severity:** Minor
- **Sessions affected:** 2 out of 9 reviewed
- **Symptom:** 
  - Session tried `/home/juan/.agents/skills/post-market/SKILL.md` instead of `.pi/skills/post-market/SKILL.md`
  - Session tried `.pi/skills/web-search/SKILL.md` instead of `~/.agents/skills/web-search/SKILL.md`
- **Root cause:** Model confusion about skill locations. The available_skills list in system prompt shows correct paths, but model occasionally tries wrong locations first.
- **Fix:** Not needed — sessions recovered and continued. The error handling works correctly.
- **Status:** Self-correcting (no action needed)

## Good News

### Python3 Issue is Fixed
Previous sessions had problems with `python3` not being on PATH, requiring nix-shell workarounds. This is no longer happening:
- 0 sessions in the reviewed set show nix-shell usage for python3
- All `python3 scripts/*.py` commands execute directly without workarounds
- The shell.nix or PATH configuration fix has been effective

### Overall Session Health
- 7 out of 9 sessions completed with 0 errors
- All sessions completed their primary tasks (scans ran, logs were updated, commits succeeded)
- No blocking errors that prevented session completion

## Recommendations

1. **Web search rate limiting**: Consider adding a note to prompts that use `websearch search` to serialize calls rather than running them in parallel. Or upgrade the Brave API plan if catalyst searches are important.

2. **No other action needed**: The occasional skill path confusion self-corrects, and the python3 issue has been resolved.
