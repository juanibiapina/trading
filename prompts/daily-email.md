Send the daily summary email. This is the last task in the daily cycle.

Read today's logs and send a single HTML email summarizing everything.

## Steps

### 1. Read Today's Data

Determine yesterday's US trading date. This is the date the morning evaluation used (the AH session being reviewed). The log was created by last night's post-market scans and updated by this morning's evaluation.

Read:
- `log/YYYY-MM-DD/log.md` -- morning eval: today's winner, scanner diagnostic, baseline tracking, paper trades, AH mover follow-through
- `SCANNER_CHANGELOG.md` -- latest entry for today's scanner improvement
- `log/YYYY-MM-DD/process-review.md` -- process issues found (optional)

Check whether `log/YYYY-MM-DD/process-review.md` exists before reading it. If it is missing, treat that as "no process review file for this cycle" rather than an error.

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

```bash
node scripts/send-email-inboxkit.js \
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
<p>[Issues found and severity, or "No issues - all sessions ran clean."]</p>
<p>[If any issues need user action, highlight them]</p>

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
- Sender is `zero@inboxkit.cc`. Invite a reply for feedback (it feeds the
  `check-email-replies` pulse). If `STRATEGY_ROADMAP.md` has open asks for Juan,
  surface them briefly in the email.
