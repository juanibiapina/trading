# Process Review — 2026-08-26

## Sessions Reviewed

All 18 work sessions since the last review (2026-08-25 12:40), timestamps UTC:

- 2026-08-25 13:00 — post-review work session
- 2026-08-25 19:30, 20:00, 20:15, 20:30, 20:45, 21:00, 21:30, 22:00, 22:30 — post-market scan / evaluation block
- 2026-08-26 07:00 — email reply check
- 2026-08-26 08:20 — morning evaluation of overnight scan
- 2026-08-26 08:30 — position evaluation
- 2026-08-26 09:00 — premarket-open gapper scan
- 2026-08-26 09:30 — daily email
- 2026-08-26 12:20 — scanner improvement
- 2026-08-26 12:30 — position evaluation

## Method

Each session is JSONL. Tool results carry `role: "toolResult"` with an
`isError` boolean and result text. Scanned all 18 sessions for:

- `isError == true` on any tool result (1 hit total, analyzed below)
- failure keywords in result text (`command not found`, `no such file`,
  `permission denied`, `modulenotfound`, `traceback`, `nix-shell`, `fatal:`)
- workaround/install commands (`nix-shell`, `sudo`, `pip install`,
  `npm install`, `apt-get`)
- identical command repeated 3+ times within a session (retry-loop detection)
- **new this review:** the exact broker error text `order_id is missing`, which
  prior reviews' keyword lists did not cover

Keyword hits inside file content (prompts, prior `process-review.md`) were
excluded as reads, not live output. Of the 23 `command not found` and similar
strings seen, all live in files sessions read; none are live command failures
(only 1 `isError` across the whole window, the one below).

## Issues Found

### `broker.js cancel` rejects the short order id it displays

- **Severity:** Wasteful (borderline Critical: it delays canceling a resting
  sell during a live position exit).
- **Sessions affected:** 1 of 18 this window (08-26 08:30), but recurring:
  the same failure appears in sessions on 2026-06-29, 07-15 (x2), 08-05 (x2),
  08-10, 08-13, and 08-18. Not flagged by any prior review.
- **Symptom:** `broker.js orders` prints an 8-char id prefix (e.g. `ca5835ba`).
  Feeding that prefix to `broker.js cancel ca5835ba` returns
  `ERROR: 422 Unprocessable Entity: order_id is missing` — a misleading message
  unrelated to the real cause. Sessions then flail (`cancel --id`,
  `order cancel`) before rediscovering they must paste the full UUID.
- **Root cause:** `cmdOrders` shows `o.id.slice(0, 8)`, but `cmdCancel` passed
  the argument straight to Alpaca's `DELETE /v2/orders/<id>`, which needs the
  full UUID. The truncated id produces the cryptic 422.
- **Fix:** `cmdCancel` now resolves any non-UUID argument against open orders by
  prefix. `cancel ca5835ba` looks up the matching open order and cancels the
  full UUID. Exact UUIDs still pass through unchanged. Ambiguous or unmatched
  prefixes get a clear error instead of the 422. Verified: syntax check passes,
  UUID regex and prefix-match logic tested.
- **Status:** Fixed (`scripts/broker.js`).

## Note (no action needed)

- **scan.py:** Ran natively every time (`python3 scripts/scan.py --all` and
  `--all --session premarket`). No `nix-shell` anywhere. The closed 2026-03-24
  Python-environment issue stays closed; not re-verified.
- **Workarounds / installs:** No `nix-shell`, `sudo`, `pip install`,
  `npm install`, or `apt-get` in any session.
- **Retries:** No command retried 3+ times before succeeding.
- **Prompt confusion / stale references:** None observed.
