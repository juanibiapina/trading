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

## Scan 22:00 CET (4:00 PM ET)

AH open (16:00 ET). Scanner returned **0 hits** — the TradingView `postmarket_volume` feed is typically empty in the first minutes after AH open, so no AH movers registered yet. Observation-only scan regardless (no entries before 23:00 CET per learning-phase default).

No candidates found. Watch names from the 21:30 regular-session scan (DOMO [open pos], AEHL, TMDE, APUS, BATL) not yet confirmed carrying into AH — re-check at 22:30/23:00 as the AH feed populates.

## Scan 22:15 CET (4:15 PM ET)

AH just opened (16:15 ET). Scanner returned **0 hits** — TradingView `postmarket_volume` feed still empty/thin in the first 15 min after AH open. Observation-only scan (no entries before 23:00 CET per learning-phase default).

Watch-name AH-book check (21:30 movers): quotes still stamped ~20:00Z (regular close) or thin:
- **AEHL** bid $0.60 / ask $9.04 x500 — bad-print ask, no real two-sided book yet
- **TMDE** bid $0.89 / ask $1.19 — stale 20:00Z, no AH activity
- **APUS** bid $0.57 / ask $0.00 x0 — no fillable AH book
- **BATL** bid $1.70 / ask $1.72 — freshest (20:13Z) but flat, no AH surge

No candidates found. No name confirmed carrying into AH yet. Re-check at 22:30/23:00 as the AH feed populates and the entry window opens.

## Scan 22:30 CET (4:30 PM ET)

AH open ~30 min in. Scanner returned **1 hit: ZCMD**. Observation-only scan (no entries before 23:00 CET per learning-phase default).

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| ZCMD | [TV](https://www.tradingview.com/chart/?symbol=ZCMD) | $1.73 | -59.7% | +16.8% | $2.02 | -52.9% | 713K | 16.3M | 0.0x | 1.1M | Miscellaneous Commercial Services |

**Spike-bar instrumentation:** `SPIKE 16:10ET +25% $2.16 1164 trades / 178k sh (first co-spike bar) (as-of 16:30ET)`. Real ignition bar fired.

**ZCMD workup:**
- **tradable=true** (NASDAQ). Real two-sided AH book: bid $1.98 x100 / ask $2.03 x100 @ 20:18Z (fresh).
- **SIP AH volume (real, accumulating):** 20:00Z 42k sh/264tr → 20:05Z 134k/777tr → 20:10Z 648k/4,706tr (H $2.19) → 20:15Z 228k/1,983tr (C $1.92). VWAP $2.02–2.08 corroborates scanner AH price. Not a bad print — genuine liquid AH move.
- **Catalyst — Grade D (dilution / crashed pump).** ZCMD ran $0.96 (Jun 29) → $4.18 close (Jul 22), a ~4x low-float pump on a 1:31 reverse split, a $5M best-efforts offering (closed Jun 1), and a July founder share issuance boosting control to 99.45%. **Today (Jul 23) it crashed -59.7%** ($4.18→$1.73). AH +16.8% bounce to ~$2.02 is a recovery off that crash.
- **Verdict: SKIP — dead-cat bounce.** Day% -59.7% (far below the -15% dead-cat threshold); AH bounce off a crashed multi-day dilutive pump. Even outside the observation-only window this fails the entry gates. Grade D catalyst (dilution) reinforces the skip.
- **Dead-cat-override watch: not yet triggered.** AH ~$2.02 is currently *above* the regular close ($1.73), which would qualify for the override watch — BUT (1) this is only ZCMD's 1st AH scan (override needs AH% rising across ≥2 AH scans), and (2) it is already fading off the $2.19 ignition high (20:15Z bar closed $1.92, below the first-scan $2.02). Not building. Re-check at 23:00 — if AH% is rising and it holds above $1.73 on a 2nd scan, flag DEAD-CAT-OVERRIDE WATCH and record a hypothetical entry.

**Decision:** No entries (observation-only 22:30 scan; ZCMD is a dead-cat bounce regardless). Re-evaluate ZCMD at 23:00+ for the override-watch condition. 21:30 watch names (AEHL, TMDE, APUS, BATL) did not register as AH movers this scan.

## Scan 22:45 CET (4:45 PM ET)

AH ~45 min in. Scanner returned **5 hits**. Observation-only scan (no entries before 23:00 CET per learning-phase default).

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| PAVS | [TV](https://www.tradingview.com/chart/?symbol=PAVS) | $5.91 | +52.3% | +21.5% | $7.18 | +85.1% | 535K | 1.7M | 0.3x | 857K | Pharmaceuticals: Other |
| AKAN | [TV](https://www.tradingview.com/chart/?symbol=AKAN) | $8.07 | +0.1% | +10.2% | $8.89 | +10.3% | 59K | 27K | 2.2x | 541K | Agricultural Commodities/Milling |
| UCAR | [TV](https://www.tradingview.com/chart/?symbol=UCAR) | $1.00 | -4.8% | +8.0% | $1.08 | +2.9% | 1.8M | 895K | 2.0x | 23.9M | Motor Vehicles |
| ANY | [TV](https://www.tradingview.com/chart/?symbol=ANY) | $1.76 | +8.3% | +7.1% | $1.89 | +16.0% | 50K | 332K | 0.2x | 6.0M | IT Services |
| ZCMD | [TV](https://www.tradingview.com/chart/?symbol=ZCMD) | $1.73 | -59.7% | +5.8% | $1.83 | -57.3% | 1.1M | 16.4M | 0.1x | 1.1M | Misc Commercial Services |

**Spike-bar instrumentation (AH >10% names):**
- `PAVS 2026-07-23 SPIKE 16:28ET +16% $6.85 1244 trades / 78k sh (first co-spike bar) (as-of 16:45ET)`
- `AKAN 2026-07-23 SPIKE 16:09ET +29% $10.44 459 trades / 13k sh (first co-spike bar) (as-of 16:45ET)`

**PAVS workup (strong candidate — track for 23:00 entry window):**
- **tradable=true** (NASDAQ). Quote bid $5.13 / ask $6.84 x100 (stamped 20:00Z; SIP bars fresh through 20:30Z).
- **SIP AH volume (real, accelerating BUILD):** 20:00Z 121k sh/1,172tr → 20:05Z 99k/1,351tr → 20:10Z 46k/985tr (brief dip) → **20:25Z 406k/5,764tr (H $7.78)** → **20:30Z 442k/7,130tr (H $7.55, C $7.42)**. VWAP $6.94–7.22 corroborates scanner AH $7.18. Genuine liquid AH move, accelerating on volume, not a bad print.
- **Catalyst — Grade C (anti-dilution / momentum squeeze, no fresh same-day PR).** PAVS = Paranovus Entertainment Technology (AI-entertainment). Days ago (~Jul 20/21) it surged +65% PM after **terminating its Alliance Global Partners ATM share-sale agreement** (~5.9M shares sold under the deal) — removes dilution overhang. **1-for-100 reverse split announced Jun 25** (month-old, not this-week). Today +52% regular session on 9.99M sh (~11x post-split float). 4 searches found **no fresh Jul 23-specific PR/8-K/earnings** — today's move is low-float momentum continuation of the anti-dilution story.
- **Float 857K (ultra-low, ideal). Day +52.3% (positive — NOT dead-cat). Total +85% (under +150 ceiling).**
- **Reverse-split-recency:** month-old 1:100 split (not this-week) → per the recency hypothesis, month-old splits do not systematically fade. Not a gate.
- **Verdict: strong BUILD candidate, but observation-only (before 23:00 CET).** This is PAVS's **1st AH scan** appearance. At the 23:00 scan it would be its 2nd AH scan → clears the 2-AH-scan gate if it holds. Textbook profile (ultra-low float, positive Day%, real accelerating SIP volume, under ceiling, ignition 16:28 ET building). Re-evaluate at 23:00 for live entry.

**Other candidates:**
- **AKAN** — Day +0.1% (flat regular session), AH +10.2% $8.89, float 541K but AH vol thin (59K sh, spike 16:09 ET only 459 trades/13k sh). Weak/illiquid AH move; entry at $8.89 → QTY ~11 sh. Low priority. Re-check at 23:00.
- **UCAR/ANY** — AH change below 10% threshold; not qualifying candidates. Track only.
- **ZCMD** — fading as predicted: 22:30 AH +16.8% $2.02 → now +5.8% $1.83. Dead-cat bounce (Day -59.7%) confirmed rolling over. Dead-cat-override watch **NOT triggered** (fading below the 22:30 print, not building above close). Skip stands.

**Decision:** No entries (observation-only 22:45 scan). **PAVS is the lead candidate** for the 23:00 entry window — ultra-low float, positive Day%, real accelerating SIP BUILD, under ceiling. Re-evaluate PAVS (+AKAN) at 23:00 when the entry window opens and PAVS reaches its 2nd AH scan.

## Scan 23:00 CET (5:00 PM ET)

AH ~1h in. **Entry window open** (23:00 CET / 5:00 PM ET). Scanner returned **3 hits**.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| PAVS | [TV](https://www.tradingview.com/chart/?symbol=PAVS) | $5.91 | +52.3% | +22.7% | $7.25 | +86.9% | 1.1M | 1.8M | 0.6x | 857K | Pharmaceuticals: Other |
| AKAN | [TV](https://www.tradingview.com/chart/?symbol=AKAN) | $8.07 | +0.1% | +19.0% | $9.60 | +19.1% | 75K | 30K | 2.5x | 541K | Agricultural Commodities/Milling |
| UCAR | [TV](https://www.tradingview.com/chart/?symbol=UCAR) | $1.00 | -4.8% | +9.0% | $1.09 | +3.8% | 2.3M | 958K | 2.4x | 23.9M | Motor Vehicles |

**Spike-bar instrumentation (AH >10% names, log-only):**
- `PAVS 2026-07-23 SPIKE 16:28ET +16% $6.85 1244 trades / 78k sh (first co-spike bar) (as-of 17:00ET)`
- `AKAN 2026-07-23 SPIKE 16:09ET +29% $10.44 459 trades / 13k sh (first co-spike bar) (as-of 17:00ET)`

Both show a real ignition bar. PAVS's ignition (16:28 ET) precedes its main volume surge at 16:25–16:45 ET; AKAN's ignition (16:09 ET) is the early $10.44 spike bar.

**PAVS workup — ENTERED.**
- **tradable=true** (NASDAQ). Quote bid $5.13 / ask $6.84 x100 (stamped 20:00Z stale); SIP bars fresh through 20:45Z ($7.34 C).
- **2nd AH scan** (22:45 +21.5% → 23:00 +22.7%): AH% rising across scans, clears the 2-AH-scan gate.
- **SIP AH volume (real, accelerating BUILD, holding):** 20:25Z 406k sh/5,764tr (H $7.78) → 20:30Z 442k/7,130tr → 20:35Z 234k/4,151tr → 20:40Z 181k/3,502tr → 20:45Z 240k/4,174tr (C $7.34, H $7.48). VWAP $7.11–7.32 corroborates scanner AH $7.25. Genuine liquid accumulation, not a bad print.
- **Trajectory: BUILD-and-hold.** Early dip ($6.42→$5.88, 20:00–20:20Z), then ignition 20:25Z to $7.78 peak, holding $7.17–7.42 through 20:45Z (within ~6% of AH high). Not fading.
- **Catalyst — Grade C** (anti-dilution / momentum squeeze; carried from 22:45 workup). Paranovus terminated its A.G.P. ATM share-sale agreement ~Jul 20/21 (removes dilution overhang); 1-for-100 reverse split Jun 25 (month-old). No fresh Jul 23-specific PR/8-K/earnings in 4 searches → low-float continuation of the anti-dilution story.
- **Float 857K (ultra-low, ideal). Day +52.3% (positive, not dead-cat). Entry Total% ~+85% (under +150 ceiling).**
- **Verdict: ENTER.** All gates cleared: 2 AH scans >10%, float <50M, Day% above -15%, BUILD-and-hold near AH high, under ceiling. **BUY 13 PAVS @ limit $7.50 ext (id b7fd6a5e) → filled $7.17.**

**AKAN workup — ENTERED.**
- **tradable=true** (NASDAQ). Quote bid $6.92 / ask $9.56 x100 (stamped 20:00Z stale); SIP fresh through 20:45Z ($9.40 C).
- **2nd AH scan** (22:45 +10.2% → 23:00 +19.0%): AH% rising across scans, clears the 2-AH-scan gate.
- **SIP AH volume (real but thin):** ignition 20:05Z 16k sh/573tr (H $10.44) → 20:10Z 62k/1,680tr (fade, L $8.57, C $9.11) → base $8.80–9.00 on 3k–14k sh/bar → rebuild 20:40Z 26k/768tr (C $9.43), 20:45Z 12k/446tr (C $9.40). VWAP $8.77–9.47 corroborates scanner AH price. Fillable (573–768 trades on active bars, two-sided book ask $9.56 x100). Not a bad print, not a no-book illiquid ramp.
- **Trajectory: early spike → fade → rebuild within 20% of high.** Peak $10.44 at 16:05 ET (early), faded to $8.57 (-18% off high), rebuilt to $9.40–9.60 (~10% off high, within the 20% "holding" band). AH% is *rising* across the 2 scans (+10.2% → +19.0%), so building live, not declining. Not a deep SKYQ-style >20% low-rebuild.
- **Catalyst — Grade None.** 4 searches: no fresh Jul 23 PR/8-K/earnings. Reverse split 1-for-4.5 was Apr 13 (months old). Nasdaq equity-deficiency notice Jun 18 (compliance plan due Jul 31). Cannabis micro-cap low-float momentum, no fresh catalyst. Per no-catalyst handling: concern noted, not a skip.
- **Float 541K (ultra-low, ideal). Day +0.1% (flat, not dead-cat). Entry Total% ~+17.5% (well under ceiling).**
- **Verdict: ENTER (with no-catalyst concern noted).** Clears all gates: 2 AH scans >10%, float <50M, Day% above -15%, holding within 20% of AH high with rising AH%, under ceiling. Multiple positions allowed (W24 2026). **BUY 10 AKAN @ limit $9.70 ext (id e21b6504) → filled $9.47.**

**Other:**
- **UCAR** — AH +9.0% (below 10% threshold), Total +3.8%. Not a qualifying candidate. Track only.

**Decision:** ENTERED PAVS ($7.17) and AKAN ($9.47). PAVS is the stronger name (BUILD-and-hold, real heavy SIP volume, Grade C); AKAN is a thinner ultra-low-float Grade-None momentum name that cleared the gates. Both under the +150 ceiling, both >10% AH across 2 scans. DOMO (open Grade A position) not re-entered (one entry per candidate). ZCMD dead-cat bounce (Day -59.7%) not re-checked as a candidate — confirmed rolling over at 22:45.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
| PAVS | $7.17 | 2026-07-23 23:00 CET | 13 | b7fd6a5e | Grade C anti-dilution; ultra-low float 857K, Day +52%, BUILD-and-hold near AH high, real heavy SIP volume (400k+ sh/bar), Total ~+85% under ceiling, 2 AH scans >10%. |
| AKAN | $9.47 | 2026-07-23 23:00 CET | 10 | e21b6504 | Grade None (no catalyst); ultra-low float 541K, Day +0.1%, rising AH% across 2 scans, holding within 20% of AH high, Total ~+17.5% under ceiling. Cannabis micro-cap momentum, no-catalyst concern noted. |
