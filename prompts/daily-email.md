Send the daily summary email for the completed overnight cycle. This pulse runs before the day's scanner improvement and process review.

Read the completed work available at send time and send one HTML email.

## Steps

### 1. Read Completed Data

Determine yesterday's US trading date. This is the date the morning evaluation used (the AH session being reviewed). The log was created by last night's post-market scans and updated by this morning's evaluation.

Read:
- `log/YYYY-MM-DD/log.md` -- morning eval: today's winner, scanner diagnostic, baseline tracking, paper trades, AH mover follow-through
- `SCANNER_CHANGELOG.md` -- latest completed scanner improvement; label its date, since today's improvement may run after this email
- Latest completed `log/*/process-review.md` -- process issues and any needs-user-action items; label its date, since today's review may run after this email
- `INITIATIVE_LOG.md` and `STRATEGY_ROADMAP.md` -- completed progress for every initiative since the previous successful daily email, including parallel work recorded under another initiative's heading
- `FEEDBACK_LOG.md` -- new feedback and the changes or follow-up it caused
- Jev classification/usage artifacts referenced by Initiative 7 in `INITIATIVE_LOG.md` and `STRATEGY_ROADMAP.md` -- latest completed results and model costs

**Jev reporting (Juan's October 1 reply, captured October 2):** Every daily email must include a **Jev Results and Costs** section. Give the run date/model, classified tickers and labels or a concise outcome summary, calls/token usage, and the cost in its currency for the reporting window. Identify measured charges versus estimates and cite the artifact period; report cumulative cost only if recorded. If no run completed, say "Not run" or "Failed" with the reason/next deliverable. State zero calls and $0 only when verified; otherwise say usage/cost unavailable. Preserve any cost from failed attempts. An absent artifact must not imply zero cost. This section is required even before the first classifier delivery; `scanner-improvement` and `process-review` should check its presence and evidence.

Resolve the initiative reporting window from the latest successful `log/*/daily-email.json` receipt (`status: sent`, ordered by `sent_at`). If the receipt is missing, locate the previous daily-email session and run `python3 scripts/pi-session-text.py /absolute/path/to/session.jsonl --role toolResult --contains 'Sent from zero@inboxkit.cc'`. Use the timestamp of a successful bash result with an InboxKit `status: sent` response. The reader accepts both string and array message content and missing optional fields; inferred DuckDB structs can fail on these logs. If no successful send time is available, state the window used and report the latest completed initiative entries with their dates. Include all initiatives that moved in that window, even when their work belongs to a different trading-cycle date. Group multiple steps for one initiative into one concise update: initiative number/name, completion date/time, concrete step, result, and next step. An unchanged rerun is monitoring; describe it accurately. If none moved, say so and name the next concrete deliverable. Briefly identify active work that is blocked or deferred and the dependency or next check; preserve Juan's broker-test deferral.

Use the cycle date resolved above for the overnight log, chart paths, and email subject; do not default to the current calendar date when the current day's directory contains only position or scan entries. Read the cycle log from the start. Before using a nonzero read offset, check the file's current line count; never reuse an offset from another log, and treat a short log as valid.

Find the newest existing process review by date, independent of the overnight log date. If there is no completed review, say "No completed process review available." If the latest review predates this email, do not describe the intervening sessions as reviewed or clean. Include any unresolved needs-user-action item from that review in the email. Today's later scanner improvement and process review can be reported in the next daily email.

### 2. Generate Charts (Initiative 5)

Render a 5m + volume chart for the **winner** and for each **open Alpaca
position** reported in the email, into today's log dir. The renderer is
dependency-free (Yahoo bars -> SVG -> PNG, AH/PM shaded):

```bash
python3 scripts/chart.py TICKER --range 2d --out log/YYYY-MM-DD/TICKER-HHMM.png
```

Use the cycle date for the dir and the current time (CET) for `HHMM`. If
`chart.py` fails for a ticker (no Yahoo data, etc.), skip that chart and still
send the email -- charts are a review aid, not a blocker.

**Mark entries/exits on the chart (Juan asked 2026-07-22).** When the ticker has
a real Alpaca fill, add `--entry` / `--exit` so the chart shows where we
actually traded. Get fills from `node scripts/broker.js orders all` (use
`filled_avg_price` and the fill timestamp, converted to **exchange-local /
ET**). Pass price alone, or `PRICE@YYYY-MM-DD HH:MM` to pin the marker to the
fill bar:

```bash
# winner/position we entered and exited
python3 scripts/chart.py HIHO --range 2d --out log/.../HIHO-HHMM.png \
  --entry "1.50@2026-07-20 16:05" --exit "1.89@2026-07-21 08:10"
# still-open position: entry only
python3 scripts/chart.py PAPL --range 2d --out log/.../PAPL-HHMM.png \
  --entry "1.10@2026-07-20 17:09"
```

Omit the flags when there is no real fill (e.g. a detected-but-not-traded
winner) -- markers reflect actual trades, not hypotheticals.

InboxKit has **no attachment API**, but the repo is **public** (2026-07-03), so
charts are **inlined into the email body** via `raw.githubusercontent.com`
image URLs. Gmail proxies remote https images, so `<img src>` renders inline.

**Commit + push the charts BEFORE sending the email** so the raw URL resolves
when Gmail's proxy fetches it (Juan reported the old blob links 404'd, and Gmail
can cache a 404 if the image isn't live at send time):

```bash
git add log/YYYY-MM-DD/*.png
git commit -m "daily-email charts YYYY-MM-DD"
git push
```

**After push, verify each raw URL is live (HTTP 200) BEFORE sending.** Gmail's
image proxy caches a 404 if it fetches the URL before the raw CDN has propagated
the new commit (this is why RPGL didn't render on 07-09 while SUNE did). Poll
each chart URL until it returns 200 (short retries), then send:

```bash
for url in <each raw.githubusercontent URL for this cycle>; do
  for i in $(seq 1 10); do
    code=$(curl -s -o /dev/null -w "%{http_code}" "$url")
    [ "$code" = "200" ] && break
    sleep 3
  done
  echo "$code  $url"
done
```

If any URL is still not 200 after the retries, drop that one image from the email
(omit its `<img>`) rather than shipping a broken inline image.

Raw URL format (verified 200 on the public repo):

```
https://raw.githubusercontent.com/juanibiapina/trading/main/log/YYYY-MM-DD/TICKER-HHMM.png
```

Add a "Charts" section to the email body with one inline image per chart, e.g.:

```html
<h3 style="color: #555;">Charts (5m + volume)</h3>
<p style="margin: 0 0 4px;"><strong>TICKER (winner)</strong></p>
<img src="https://raw.githubusercontent.com/juanibiapina/trading/main/log/YYYY-MM-DD/TICKER-HHMM.png" alt="TICKER 5m chart" style="width: 100%; max-width: 560px; height: auto; border: 1px solid #e0e0e0; border-radius: 4px; margin-bottom: 12px;"/>
<p style="margin: 0 0 4px;"><strong>TICKER (open position)</strong></p>
<img src="https://raw.githubusercontent.com/juanibiapina/trading/main/log/YYYY-MM-DD/TICKER-HHMM.png" alt="TICKER 5m chart" style="width: 100%; max-width: 560px; height: auto; border: 1px solid #e0e0e0; border-radius: 4px; margin-bottom: 12px;"/>
</p>
```

If `chart.py` produced no charts for this cycle, omit the Charts section.

### 3. Send Email

Send as `zero@inboxkit.cc` via InboxKit (not from Juan's Gmail). Juan replies to
these emails with feedback; the `check-email-replies` pulse reads those replies.

Immediately before finalizing the HTML, read this session's provider, model ID,
and reasoning level through the bash tool:

```bash
printf 'provider=%s\nmodel=%s\nreasoning=%s\n' \
  "${PI_PROVIDER:-unavailable}" "${PI_MODEL:-unavailable}" "${PI_REASONING_LEVEL:-unavailable}"
```

Populate the `Email session` footer from these returned values and HTML-escape
each value. Use the exact runtime IDs; if a value is missing, show `unavailable`.
The footer identifies the session preparing and sending this email. Other
completed trading work can have used other models.

```bash
node scripts/send-email-inboxkit.js \
  --to juanibiapina@gmail.com \
  --subject "Trading Scanner Report - YYYY-MM-DD" \
  --body '<div style="font-family: -apple-system, Arial, sans-serif; max-width: 600px; margin: 0 auto; color: #333;">
<h2 style="color: #1a1a1a; border-bottom: 2px solid #e0e0e0; padding-bottom: 8px;">Overnight Cycle: [date range]</h2>

<h3 style="color: #555; margin-top: 20px;">Post-Market Scans</h3>
<p>[How many scans ran, unique tickers, notable movers]</p>

<h3 style="color: #555;">Today&rsquo;s Winner</h3>
<!-- Winner must be ACTIONABLE/capturable (real fillable AH book), not just the
     biggest %. An uncapturable phantom/dilution spike (ask $0.00 x0, no fillable
     book) is NOT the winner even at +194% — crown the best captured/tradable
     mover and note the uncapturable spike separately as detected & skipped.
     See morning-evaluation.md "Actionable-winner refinement" (WVVIP 08-26). -->
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
<p>[Date of latest completed change and what changed, with brief hypothesis; say if no change is recorded for this overnight cycle]</p>

<h3 style="color: #555;">Process Review</h3>
<p>[Date of latest completed review and its findings; if none exists, say no completed review is available. Do not claim today's sessions ran clean before they are reviewed.]</p>
<p>[If the completed review has unresolved needs-user-action items, highlight them]</p>

<h3 style="color: #555;">Initiative Progress</h3>
<p>[Reporting window: previous successful email send time through this send time]</p>
<ul>
<li><strong>Initiative [N] &mdash; [name], [completion date/time]</strong>: [completed step and concrete result]. Next: [next deliverable].</li>
</ul>
<p>[One update per initiative that moved, including parallel work. If none moved, say so and give the next concrete deliverable. Briefly list active blocked/deferred work and its dependency or next check.]</p>

<h3 style="color: #555;">Jev Results and Costs</h3>
<p>[Run date/model and stock classification results, or explicit not-run/failure status with the next deliverable. Reporting-window calls/token usage and measured cost or labeled estimate with currency; state unavailable when records are missing. Include costs from failed attempts.]</p>

<h3 style="color: #555;">Feedback Acknowledged</h3>
<!-- Juan asked (08-27) to see his feedback reflected back so he knows it landed.
     Read the newest FEEDBACK_LOG.md entries (since the last email) and list each
     one: what Juan said (short) + what changed/where it routed. If nothing new
     since the last cycle, say "No new feedback since last report." Never omit
     this section. -->
<ul>
<li><strong>[date] &mdash; "[short quote of Juan's point]"</strong>: [what changed / routed to Initiative X / logged].</li>
</ul>

<h3 style="color: #555;">Key Takeaway</h3>
<p style="background: #e3f2fd; padding: 10px; border-radius: 4px; border-left: 4px solid #1976d2;">[One sentence: the single most important thing from this cycle]</p>

<p style="font-size: 12px; color: #666; margin-top: 20px;">Email session: [provider]/[model ID] &middot; reasoning: [reasoning level]</p>
</div>'
```

After a successful InboxKit response, save the exact sent HTML as `log/YYYY-MM-DD/daily-email.html` and a `daily-email.json` receipt with `status`, `message_id`, UTC `sent_at`, `sent_at_source`, `previous_successful_send_at`, and `reporting_cutoff_at`. Use the response's send timestamp when provided; otherwise record the local time the success response arrived and label that source. Commit and push both files. If saving the receipt fails after delivery, recover the record from the session result; sending again would duplicate the email.

**Formatting rules:**
- Subject: use ASCII only -- use `-` not em dashes (they break encoding)
- Body: HTML with inline styles (email clients strip `<style>` tags)
- Use `&amp;` for `&`, `&mdash;` for em dashes, `&euro;` for euros
- Color wins green (`#2e7d32`), losses red (`#c62828`)
- Keep it short -- scannable on a phone in under 30 seconds
- Sender is `zero@inboxkit.cc`. Invite a reply for feedback (it feeds the
  `check-email-replies` pulse). If `STRATEGY_ROADMAP.md` has open asks for Juan,
  surface them briefly in the email.
- **Do not gate changes on Juan's pre-approval** (standing directive, 2026-07-16
  reinforced 2026-07-17: "apply, don't ask" / "don't wait for my approval").
  Never emit "Needs You / Decision For You / yours to approve" blocks for
  strategy or entry-rule changes, *including live-entry rules* — those are
  applied by their owning pulse (`strategy-advance` for `Day Trading.md` rules,
  `scanner-improvement` for scanner/process) and **reported** here for a
  *retroactive* veto only ("wired X; say the word to revert"). Reserve email
  asks strictly for decisions the agent cannot execute itself (infra, broker
  coverage, funding).
