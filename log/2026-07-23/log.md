# Morning Evaluation - 2026-07-23

## Morning Evaluation — 10:20 CET

Session evaluated: **2026-07-22** after-hours → **2026-07-23** premarket. Pulse 1.

### Today's Winner

**LGCL** — Personnel Services (Lucas GC Limited, NasdaqCM low-float)
- Catalyst: **Grade None** — no same-day PR found (5 searches last night). Undated agentic-AI patent headline + 40:1 reverse split Oct 2025 (months-old). Low-float momentum squeeze, no fresh operational catalyst.
- Previous Close: $0.95 (regular-session close; Yahoo prior-day close $0.98)
- AH last night: ignition 17:25 ET, accelerating BUILD to SIP AH peak **$1.79 (+88%)** at 19:45 ET on 500k–920k sh/bar (3,000–5,800 trades each)
- Premarket now: **$2.35 (+147%)** at pulse; PM peak SIP **$2.47 (+160%)** at 04:05 ET (08:05Z)
- Hypothetical P&L (AH entry → PM peak): our actual entry $1.58 → PM peak $2.47 = **+56.3%**; optimal ignition entry ~$1.15 → $2.47 = **+115%**
- Float: 1.6M | Market Cap: $40.7M
- SIP confirmation it cleared the bar: PM open bar 08:00Z **3,152,969 sh / 27,219 trades** (H $2.37), 08:05Z **1,955,926 sh / 16,399 trades** (H $2.47). Real, accumulating, >100% move. AH BUILD also real (600k–920k sh/bar).

**Scanner Diagnostic:**
- Detectable at screening time (~22:15 CET)? **YES — and we entered it.**
- What it looked like: LGCL's ignition fired 17:25 ET (23:25 CET), so it was flat at the 22:15 CET screening scan. It first appeared as an AH mover in the **00:00 CET scan (+57.6%)** and reappeared in the **00:30 CET final scan (+55.5%)**. On its 2nd AH scan it cleared the 2-AH-scan gate (Day −2.9% above dead-cat, Total +51% under +150 ceiling, float 1.6M ideal, VRatio 6.6x, textbook accelerating BUILD peaking late). **ENTERED $1.58 at 00:30 CET.**
- This is a clean **detected + selected** winner — the ideal outcome. The scanner caught it and we traded it.
- Scanner gap: none. Textbook detection and correct entry decision.

### Baseline Tracking

LGCL is a valid AH-detectable winner (real AH BUILD >10% across 2 scans), so it counts in both numerator and denominator. Days tracked +1 for the session evaluated. Detected +1 (caught), selected +1 (entered).

- Days tracked: **53** (was 52 + 1)
- Winners detected by scanner: **45/50 (90.0%)** — added LGCL
- Winner selected for paper trade: **26/50 (52.0%)** — added LGCL (entered $1.58)
- Target: >80% detection
- Status: **BASELINE MET** (90.0%)
- **Baseline gap (carried):** 2026-07-17 and 2026-07-20 morning evals recorded no `Days tracked:` line — those two trading-day retrospectives were never baseline-counted (denominator understates true trading days). The immediately-preceding trading day (07-22) *does* carry a baseline line, so **no new gap this cycle**.

### Retrospective Scan Results

- Live PM scan (04:21 ET): 5 hits — **LGCL +147% $2.35**, PLAG +56.9% $0.92, ZYBT +31.9% $1.82, EHGO +15.9% $2.04, AEHL +22.1% $0.68.
- Forced AH scan (04:21 ET): 0 hits (expected overnight — TradingView postmarket fields stale; secondary diagnostic only).
- AH reconstruction (SIP + Yahoo `--ah-history`): LGCL had the night's strongest real AH BUILD (500k–920k sh/bar). PLAG, ZYBT, AEHL, DOMO all had real but smaller AH volume; INM/STFS/NTCL thin.

### Open Position P&L (Alpaca)

Four open positions from last night's paper trades. Exits handled by `position-evaluation.md` (10:30/14:30 CET) — **not closed here**. Prices below are live PM; Alpaca `current_price` on LGCL lags (see flag).

| Ticker | Entry | Entry Total% | Catalyst | Entry Time | PM Peak | Peak Time | Exit | P&L | P&L % | Status |
|--------|-------|--------------|----------|------------|---------|-----------|------|-----|-------|--------|
| LGCL | $1.58 | +66.3% | None | 00:30 CET | $2.47 (SIP) | 04:05 ET | open | — | **+48.7%** (live $2.35) | 🟢 Open — winner |
| DOMO | $3.92 | +14.2% | A — $400M asset sale | 23:32 CET | $4.20 (SIP) | 04:00 ET | open | — | −1.5% | 🟡 Open |
| AEHL | $0.69 | +23% | None | 00:01 CET | $0.74 (SIP) | 04:00 ET | open | — | ~flat (+1.4%) | 🟡 Open |
| PLAG | $0.98 | +66% | None | 23:01 CET | $1.13 (SIP) | 04:05 ET | open | — | −6.1% (live $0.92) | 🟡 Open |

**Quote-freshness flag (LGCL):** Alpaca `positions` reports LGCL `current_price $2.01 (+27.2%)` and the live `quote` returns bid $0.82 / ask $1.16 stamped **2026-07-22T20:00Z (prior 20:00 ET regular close)** — both stale/lagging. The live PM print (scan $2.35, last SIP bar close $2.26, SIP peak $2.47) is the tradeable level. Reported LGCL P&L uses the live $2.35 (+48.7%), not the stale Alpaca $2.01.

**Total Realized P&L (Alpaca fills only): +€0.00** (no exits yet — positions still open, exits at 10:30/14:30).

### Scanner Effectiveness

- Evening scans ran: **7 of 7** scheduled (21:30, 22:00, 22:30, 23:00, 23:30, 00:00, 00:30 CET), plus 2 bonus (22:15, 22:45) = 9 total. **Full coverage — entry window fully captured.**
- Candidates found: PLAG, ZYBT, LGCL, AEHL, DOMO, INM, STFS, NTCL, IVVD (9 unique AH movers).
- Retrospective matches: winner LGCL = detected + entered. All 4 entries (LGCL, DOMO, AEHL, PLAG) were real AH movers surfaced by the scanner.

### Missed Opportunities

| Ticker | AH Change | Why Missed | Would Be Profitable? |
|--------|-----------|------------|---------------------|

No significant missed opportunities. The winner (LGCL) was detected and traded. All other AH movers were surfaced; the ones we skipped (INM, STFS, NTCL, IVVD) faded on thin PM volume.

### AH Mover Follow-Through

| Ticker | AH Peak | Peak Time | AH Trajectory | Current PM | From Peak | From Close | Verdict |
|--------|---------|-----------|---------------|------------|-----------|-----------|---------|
| LGCL | $1.79 (SIP +88%) | 19:45 ET | Build (late) | $2.35 (+147%) | +31% | +147% | **WINNER — PM peak $2.47 > AH peak. Detected + entered $1.58. Continuation confirmed.** |
| PLAG | ~$1.05 AH | ~AH | Spike→fade | $0.92 (+56%) | fade | +56% | PM peak $1.13 briefly > entry then faded; held, −6% vs entry |
| DOMO | ~$4.00 AH | ~AH | Build-and-hold | $3.86 | fade | +14% | PM peak $4.20 then settled; Grade A but low extension, mild |
| AEHL | $1.38 prior night | — | Spike→fade | $0.68 (+22%) | fade | +22% | Entered $0.69; PM peak $0.74 then flat; recurring crypto-treasury pump |
| ZYBT | — | — | — | $1.82 (+32%) | — | +32% | PM high $2.15 (842k sh) then faded to $1.82; not entered, minor |
| STFS | — | — | — | ~$4.12 | — | — | PM high $4.70 on thin vol (20k sh) → faded; correctly skipped |
| INM | — | — | — | ~$1.58 | — | — | Thin PM (17k sh); correctly skipped |
| NTCL | — | — | — | ~$3.37 | — | — | Thin PM (1.2k sh); correctly skipped |

**AH-peak-vs-PM-peak:** LGCL PM peak ($2.47) **exceeded** its AH peak ($1.79) — a clean AH→PM continuation, the pattern the strategy hunts. Not an extreme >250% AH runner, so no new MSW-class "AH-was-better-exit" data point. AEHL and the thin names faded (AH ≥ PM), correctly skipped or already held.

### Price Charts

```
LGCL — 2-Day Timeline
Prev Close: $0.95 (reg) | Range: $0.95–$2.47 | Current: $2.35 (+147%)
Peak: $2.47 (+160%) at 07-23 08:05 ET (04:05 ET)
AH 07-22: ignition 17:25 ET → accelerating BUILD 500k-920k sh/bar → AH peak $1.79 (+88%) 19:45 ET
PM 07-23 04:00 ET: gap up $1.56 → $2.47 on 3.15M sh/bar (27k trades) → continuation, HELD (position open)
Entry: $1.58 @ 00:30 CET (18:30 ET) on 2nd AH scan → +48.7% live, +56.3% to PM peak
```

### Notes

- **Clean detected + selected winner — best outcome of the cycle.** LGCL was surfaced by the scanner on 2 AH scans, cleared every gate, was entered at $1.58, and delivered a real AH→PM continuation to $2.47 (+160% from close). This is exactly what the strategy is built to catch. Position still open — exit decision is for the 10:30/14:30 position-evaluation pulses (Grade None → exit first PM opportunity per entry note).

- **Reverse-split-recency tally (updated):** LGCL had a **40:1 reverse split Oct 2025 (months-old)** and **continued** (entered $1.58 → PM peak $2.47 = +56%). This mirrors EDHL (months-old split, mild continue) and reinforces the recency hypothesis: months-old splits do **not** systematically fade, unlike this-week splits (3/3 faded: ELPW, YYGH, BIYA). Recency split now: this-week 3/3 faded; months-old 2/2 non-fade (EDHL mild continue, **LGCL continue**). The recency signal keeps strengthening — one more this-week fade (→4/4) or a this-week continuation would resolve it for a daily-email conviction-downgrade recommendation. Not applied as a gate.

- **PM-only-gapper tally: UNCHANGED.** Today's biggest raw PM mover is LGCL (+147%), an **AH→PM continuation** (moved >10% in AH, detected), NOT a PM-only gapper. Standing holdable count stays 1 clear (SXTC) of 6. No new PM-only case.

- **Late-AH-tail tally: UNCHANGED.** LGCL's defining surge (ignition 17:25 ET → BUILD to $1.78 by 18:15 ET) fired **inside** the scanned window and was caught by the 00:00/00:30 CET scans. Its later $1.79 print at 19:45 ET is in the unscanned tail but the stock was already detected and entered at 18:30 ET — not a tail-dependent case.

- **Fade-rule false-negative tally: UNCHANGED. Sub-3M count stays 3 of 5, ≥4/5 trigger NOT met.** No sub-3M AH-fader re-exploded tonight. LGCL did not fade (it BUILT and was entered), so it is not a fade-rule case. Live-flip exception stays withdrawn pending one more clean sub-3M SIP-verified blow-past.

- **Ceiling-override / dead-cat-override watch: none.** LGCL Total +51% at entry (well under +150 ceiling), Day −2.9% (above −15% dead-cat). No overridden candidates last night.

- **Broker-block tally: UNCHANGED.** All 4 qualified candidates (LGCL, DOMO, AEHL, PLAG) filled normally. No `tradable=false` blocks last night.

- **Coverage:** full 9-scan night (7/7 scheduled + 2 bonus). No coverage failure to add to the tally.

- **Active Watch check:** SXTC (day 1 winner, PM-only gapper) faded from $7.91 peak / $5.69 to **$2.68** — the holdable window closed by day 2 as expected for a no-catalyst PM squeeze. HIHO (entered $1.50, sold $1.26) at **$1.07** day 3, still unwinding.

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| AEHL | $0.69 | $0.70 | +1.5% | $0.82 (OVN) | 1 | None | SELL | Exit at any profit; sold $0.70 |
| LGCL | $1.58 | $1.96 | +24.1% | $2.47 (PM) | 1 | None | SELL | Exit at any profit; sold into fade $1.96 |
| PLAG | $0.98 | $0.86 | -12.2% | $1.79 (OVN) | 1 | None | SELL | Below -10% hard stop; sold $0.86 |
| DOMO | $3.92 | $3.82 | -2.5% | $4.20 (PM) | 1 | A | HOLD | Catalyst intact ($400M acquisition), day 1/5, within -25% stop ($2.94) |

**Actions taken:**
- SELL AEHL 136 @ limit $0.66 ext (id 48266080) → filled $0.70. P&L +$1.36 (+1.5%)
- SELL LGCL 58 @ limit $1.82 ext (id d510e021) → filled $1.96. P&L +$22.04 (+24.1%)
- SELL PLAG 97 @ limit $0.83 ext (id 876ddb3a) → filled $0.86. P&L -$11.64 (-12.2%)
- HOLD DOMO (Grade A, day 1)
- Net realized this pulse: **+$11.76**. LGCL was the clean detect→select→continuation winner (+24%).

## Position Evaluation — 14:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| DOMO | $3.92 | $4.19 | +6.9% | $4.50 (+14.8%) | 1 | A | HOLD | Day 1/5, catalyst intact, peak below +50% trail threshold, above -25% hard stop ($2.94) |

**Actions taken:**
- None. HOLD DOMO. SIP peak $4.50 at 11:55Z on 1.98M sh/bar (real accumulating volume), faded to $4.14 bid. No trail (peak +14.8% < +50%). Hard stop $2.94 intact.

---

# Post-Market Screening - 2026-07-23

## Scan 21:30 CET (3:30 PM ET)

Regular-session scan (15:30 ET), **before AH opens** (16:00 ET / 22:00 CET). Watch only — no entries per regular-session-caution rule. Only enter if a name reappears in a 22:00+ CET AH scan with sustained momentum.

Real intraday movers (meaningful 5m volume; most other scan hits are sub-1K-share illiquid artifacts with stale IRVol):

| Ticker | Chart | Price | Day% | 5mVol | IRVol | VChg% | Float | MCap | Industry | Note |
|--------|-------|-------|------|-------|-------|-------|-------|------|----------|------|
| DOMO | [TV](https://www.tradingview.com/chart/?symbol=DOMO) | $3.95 | +25.4% | 86K | 28.8 | +44.8 | 36.9M | 178.3M | Packaged Software | **Open position** (Grade A, $400M asset sale). Not re-entered (one entry/candidate). |
| AEHL | [TV](https://www.tradingview.com/chart/?symbol=AEHL) | $0.68 | +22.1% | 169K | 23.9 | +244.8 | 15.6M | 12.3M | Building Products | Watch — pending AH. Low-float crypto-treasury pump, sold this AM $0.70. |
| TMDE | [TV](https://www.tradingview.com/chart/?symbol=TMDE) | $1.05 | +22.6% | 16K | 8.7 | +231.1 | 16.5M | 24.8M | Wholesale Distributors | Watch — pending AH. |
| APUS | [TV](https://www.tradingview.com/chart/?symbol=APUS) | $0.77 | +17.3% | 39K | 1.9 | +310.3 | 5.6M | 11.7M | Biotechnology | Watch — pending AH. Low float 5.6M. |
| BATL | [TV](https://www.tradingview.com/chart/?symbol=BATL) | $1.80 | +16.1% | 187K | 1.8 | +50.4 | 18.0M | 39.6M | Oil & Gas Production | Watch — pending AH. |

**Decision:** No entries — regular-session watch scan. AH opens at 22:00 CET; the 22:00/22:30 scans are observation-only per learning-phase default (no entries before 23:00 CET). Re-evaluate DOMO/AEHL/TMDE/APUS/BATL for AH carry at the 22:00+ scans. Scanner otherwise returned 56 hits, but the remainder are sub-1K-share prints (IRVol inflated on stale regular-session volume), not fillable movers.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
