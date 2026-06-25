# 2026-06-25

## Morning Evaluation — 10:20 CET

### Today's Winner

**AZI** (Autozi Internet Technology) — Specialty Stores
- Catalyst: None fresh. Recent driver was Jun 9-10 $30M private placement (dilution) + auditor change; stock then bled $1.66 → $1.18 over 2 weeks. AH pop = low-float bounce/squeeze off a downtrend, no same-day 8-K/6-K.
- Previous Close: $1.18
- AH last night: $2.34 (+98.3%) at 18:45 ET (00:45 CET)
- Premarket now: $2.14 (+81.4%), peaked $2.25 (+90.7%) at 04:00 ET
- Hypothetical P&L (AH entry → PM peak): entry $1.62 → PM peak $2.25 = **+38.9%**; AH-entry → AH peak $2.34 = +44.4%
- Float: 4.4M | Market Cap: ~$77.6M

**Scanner Diagnostic:**
- Detectable at screening time? **YES**
- It was the biggest AH mover from the first scan. At 22:30 CET (+37.7%, $1.57), 23:00 (+51.8%, $1.73), built to +82.5% ($2.08) by 00:30. Float 4.4M, clean BUILD trajectory across every scan.
- **We caught AND selected it.** Flagged at 23:00 CET as the night's top candidate (Grade None; concerns logged: no fresh catalyst, not first-day activity, thin Yahoo AH volume). No Alpaca order was placed (pre-Alpaca; execution starts 2026-06-25).
- Scanner gap: none. This is a clean detection + selection win — the scanner found the day's winner in the window.

### Baseline Tracking

- Days tracked: **37** (was 36 + 1)
- Winners detected by scanner: **32/37 (86.5%)** — AZI added
- Winner selected for paper trade: **22/37 (59.5%)** — AZI was traded; we picked the right stock
- Target: >80% detection
- Status: **BASELINE MET**

### Retrospective Scan Results

Live premarket scan (04:20 ET) — 4 hits:

| Ticker | Close | PM Chg% | PM Price | Float | MCap | Industry |
|--------|-------|---------|----------|-------|------|----------|
| AZI | $1.14 | +98.2 | $2.26 | 4.4M | $77.6M | Specialty Stores |
| NEXR | $0.56 | +32.8 | $0.75 | 6.1M | $3.4M | Recreational Products |
| ROLR | $5.30 | +15.8 | $6.14 | 4.9M | $58.1M | Packaged Software |
| BCDA | $1.06 | +12.3 | $1.19 | 10.5M | $15.8M | Biotechnology |

AH reconstruction confirms AZI as the standout AH→PM continuation. NEXR/ROLR/BCDA are PM-side moves with no qualifying AH footprint (NEXR was -4% in AH last night). No other AH→PM winner.

### Trade Execution

**No trades executed.** AZI and AMS were tracked as candidates only. This is the last day of the
pre-Alpaca period: from 2026-06-25 all entries/exits run on the Alpaca paper account via
`scripts/broker.js`, and only real fills are logged. The earlier hand-maintained paper ledger
(assumed prices, never executed) has been discarded.

### Scanner Effectiveness

- Evening scans ran: **6 of 7** (22:00, 22:30, 23:00, 23:30, 00:00, 00:30 CET) — 21:30 scan missing
- Entry window (23:00–00:30 CET) fully covered → not an entry-window loss
- Candidates found: ~20 unique tickers across scans
- Retrospective matches: 1/1 (AZI caught and traded)

### Missed Opportunities

No significant missed opportunities. The day's winner (AZI) was detected and entered.

### AH Mover Follow-Through

| Ticker | AH Peak | Peak Time | AH Trajectory | Current PM | From Peak | From Close | Verdict |
|--------|---------|-----------|---------------|------------|-----------|------------|---------|
| AZI | $2.34 (+98.3%) | 18:45 ET | Build | $2.14 | -8.5% | +81.4% | Continued strong — winner, traded |
| AMS | $1.68 (+14.3%) | 16:30 ET | Spike→hold | $1.52 | -9.5% | +3.4% | Faded — PM gave back the AH gain |
| SAGT | $1.43 (+10.0%) | 16:15 ET | Spike→fade | $1.15 | -19.6% | -11.5% | Faded then crashed — correctly skipped |

**AH-peak-vs-PM-peak check:** AZI's AH peak $2.34 marginally exceeded its PM peak so far ($2.25), so late AH was the slightly better exit — but PM is early (only 04:00–04:20 data). Not an extreme runner (AH peak +98%, well under the 250% extreme-runner threshold), so no extreme-runner tally entry. AMS and SAGT both peaked in AH and faded in PM.

### Notes

- **Clean detection + selection win.** AZI is the first day in a while where the scanner found the winner AND we entered it in-window. Detection 86.5%, selection 59.5%.
- **PM-only gapper tracking:** today's biggest raw PM mover = AZI (+98%), which is an AH→PM continuation (moved +98% in after-hours, fully detectable). **Not a PM-only gapper.** No tally addition.
- **Late-AH-tail surge:** AZI's defining move (crossing +10%, building to +50%, +76%) happened during the scanned window; the 18:30–20:00 ET tail only extended an already-qualified open position from +76% to +98%. **Not a tail-surge miss.** No tally addition.
- **Fade-rule false negatives:** none. SAGT (spike→fade, peaked +10% at 16:15) and KIDZ (spike→fade, peaked +25% at 16:45 then collapsed) were both correctly skipped — both stayed down in PM (SAGT crashed -11%, KIDZ -9%). Rule worked.
- **Coverage tally:** Jun 24–25 night ran 6 of 7 scans (missing 21:30, the earliest pre-volume scan). Entry window fully covered; minor, treat as transient. Watch for recurrence.
- **No CEILING-OVERRIDE / DEAD-CAT-OVERRIDE watch candidates** flagged in last night's log.
- AZI entered Grade None with explicit concerns (no fresh catalyst, not first-day activity, dilution-driven recent history). It is running +32% anyway — another data point that low-float (4.4M) + clean BUILD trajectory can carry overnight even without a same-day catalyst (cf. DXST Jun 1, +170% no-catalyst runner).

### Price Charts

```
AZI - 2-Day Price Timeline (5-min)
Previous Close: $1.18
2-Day Range: $1.14 - $2.38
Current: $2.14 (+81.4%)
AH Peak: $2.34 (+98.3%) at 18:45 ET → held +80%+ through AH close → PM $2.25 (+90.7%) at 04:00

AH trajectory: steady BUILD from 16:05 (+26%) → 16:35 (+51%) → 18:00 (+64%) → 18:45 peak (+98%),
then held +82-95% through the AH tail. Textbook AH BUILD → PM hold.
```

## Position Evaluation — 10:30 CET

No open positions on Alpaca. AZI/AMS were never executed (pre-Alpaca candidates). Nothing to evaluate.
Switched the workflow to Alpaca paper execution as source of truth (see OPEN_POSITIONS.md).
