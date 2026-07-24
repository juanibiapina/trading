# Morning Evaluation - 2026-07-24

## Morning Evaluation — 10:20 CET

Session evaluated: **2026-07-23** after-hours → **2026-07-24** premarket. Pulse 1.

### Today's Winner

**LVWR** — Recreational Products (LiveWire Group, electric motorcycles, NYSE; Harley-Davidson spinoff)
- Catalyst: **Grade A** — Q2 2026 earnings, consolidated revenue **+55%** (reported Jul 23). Stock fell -15.3% during the regular session, then surged +58% in late AH on the results/earnings call (Benzinga, ~overnight).
- Previous Close: **$0.77** (Jul 23 regular close, down -15.3% on the day; note Jul 22 close was $0.91)
- AH last night: dead through the scanned window, then **ignition 19:15 ET (01:15 CET)** → SIP AH peak **$1.48 (+92%)** at 19:20 ET on 490k sh / 3,412 trades
- Premarket now: **~$1.65 (+114%)** at pulse (scan $1.64 at 04:21 ET)
- PM peak: SIP **$2.09 (+171%)** at 04:00 ET on **3,458,219 sh / 22,671 trades** (Yahoo under-reported this as $1.71 — SIP is truth)
- Hypothetical P&L: AH-tail entry ~$1.35 → PM peak $2.09 = **+55%**; realistic PM-open re-entry (first-bar VWAP $1.63) → $2.09 = **+28%** (but the peak printed inside that same first PM bar, so a realistic exit was ~$1.71 = +5%)
- Float: 10.2M | Market Cap: $157.7M
- SIP confirmation it cleared the bar: PM open bar 08:00Z **3.46M sh / 22,671 trades** (H $2.09), AH ignition bar 23:20Z 490,689 sh / 3,412 trades. Real, accumulating, >100% move. **This is a real winner.**

**Scanner Diagnostic:**
- Detectable at screening time (~22:15 CET)? **NO.**
- Through all 9 scans LVWR was a **dead-cat bounce below its prior close** (scanner Total -6.5% → -1.5% vs the $0.91 Jul-22 anchor; thin AH vol 60K sh, VRatio 0.1x, 1–3 trades/bar). It was surfaced and **correctly skipped as a dead-cat** at the 00:30 final scan.
- The decisive surge to SIP $1.48 fired at **19:15 ET (01:15 CET), 45 min AFTER the 00:30 CET final scan (18:30 ET)**. At the last scan LVWR was ~$0.85-0.90, genuinely under threshold and below its regular close.
- Classification: **late-AH-tail surge, TRUE-TAIL sub-type** (genuinely sub-threshold at 18:30 ET; the move fired in the unscanned 18:30–20:00 ET tail). **Not a detection-threshold miss; not counted against the baseline.**
- Scanner gap: only 1–2 late scans (~01:00/01:30 CET) covering the 18:30–20:00 ET tail would have caught the ignition. Scheduling decision — see Notes for the running true-tail tally.

### Baseline Tracking

LVWR is a **late-AH-tail surge** (defining surge after the final scan), so — like a PM-only gapper — it is excluded from both the detection numerator and denominator (not a valid AH-detection sample). Detection and selection ratios hold at /50. Days tracked increments by 1 for the session evaluated.

- Days tracked: **54** (was 53 + 1)
- Winners detected by scanner: **45/50 (90.0%)** — unchanged (LVWR excluded, late-tail)
- Winner selected for paper trade: **26/50 (52.0%)** — unchanged
- Target: >80% detection
- Status: **BASELINE MET** (90.0%)
- **Caveat this cycle:** the 90% headline is optimistic. WLDS (see Missed Opportunities) was a real **in-window** heavy-volume AH mover the scanner never surfaced — a genuine detection failure not captured by the single-winner metric.
- **Baseline gap (carried):** 2026-07-17 and 2026-07-20 morning evals recorded no `Days tracked:` line — those two trading-day retrospectives were never baseline-counted (denominator understates true trading days). The immediately-preceding trading day (07-23) *does* carry a baseline line, so **no new gap this cycle**.

### Retrospective Scan Results

- Live PM scan (04:21 ET): 7 hits — **LVWR +113% $1.64**, WLDS +39.9% $3.12, ZCMD +17.9% $2.04, VIVK +14.6% $2.43, CPHI +10.3% $2.04, ANY +17.6% $2.08, INEO +20.3% $0.87.
- AH reconstruction (SIP + Yahoo `--ah-history`): LVWR's real AH move fired 19:15 ET (after the last scan). **WLDS** had a large, heavy-volume AH surge to SIP $3.51 at 18:20-18:25 ET — inside scanned hours — that the evening scanner missed (see Missed Opportunities).

### Open Position P&L (Alpaca)

Five open positions (four from last night's 07-23 entries; DOMO carried from 07-22, day 3). Exits handled by `position-evaluation.md` (10:30/14:30 CET) — **not closed here**. Prices below are live SIP PM (04:00-04:10 ET); freshness-guarded.

| Ticker | Entry | Entry Total% | Catalyst | Entry Time | PM Peak | Peak Time | Exit | P&L | P&L % | Status |
|--------|-------|--------------|----------|------------|---------|-----------|------|-----|-------|--------|
| AKAN | $9.47 | +19.1% | None | 23:00 CET | $11.10 (SIP) | 04:00 ET | open | — | **+3.8%** (live $9.83) | 🟢 Open — PM spike then fade |
| JEM | $5.37 | +64% | D — dilution | 22:32 CET | $5.69 (SIP) | 04:10 ET | open | — | **~+4%** (live SIP ~$5.6) | 🟡 Open (Alpaca $6.24 STALE) |
| DOMO | $3.92 | +14.2% | A — $400M asset sale | 23:32 CET (07-22) | $3.97 | 04:00 ET | open | — | ~flat (live $3.93) | 🟡 Open — day 3, flat |
| ANY | $2.29 | +16.6% | C — Cathedra BTC acq. | 00:30 CET | $2.32 (SIP) | 04:00 ET | open | — | **-9.6%** (live $2.07) | 🔴 Open — faded |
| PAVS | $7.17 | +85% | C — anti-dilution | 23:00 CET | $6.20 (SIP) | 04:00 ET | open | — | **-18.4%** (live $5.85) | 🔴 Open — faded, AH was exit |

**Quote-freshness flag (JEM):** Alpaca `positions` reports JEM `now $6.24 (+16.2%)` but the live `quote` is stamped **2026-07-23T20:00Z (prior regular close)** — stale. Live SIP PM bars show JEM $5.19 (04:05 ET) recovering to $5.63 (04:10 ET), so real P&L is ~+2 to +5%, not +16.2%. Reported against the live SIP level, not the stale Alpaca $6.24.

**Total Realized P&L (Alpaca fills only): +€0.00** (no exits yet — positions still open, exits at 10:30/14:30).

### Scanner Effectiveness

- Evening scans ran: **7 of 7** scheduled (21:30, 22:00, 22:30, 23:00, 23:30, 00:00, 00:30 CET), plus 2 bonus (22:15, 22:45) = 9 total. **Full coverage — entry window fully captured.**
- Candidates found: PAVS, AKAN, JEM, ANY, ZCMD, UCAR, OCG, LVWR (dead-cat), IPW, MX.
- Retrospective matches: winner LVWR = surfaced but correctly skipped (dead-cat; real move came post-final-scan). **WLDS = NOT surfaced (in-window miss).** All 4 entries (PAVS, AKAN, JEM, ANY) were real AH movers the scanner surfaced.

### Missed Opportunities

| Ticker | AH Change | Why Missed | Would Be Profitable? |
|--------|-----------|------------|---------------------|
| WLDS | AH peak SIP **$3.51 (+137%** from $1.48 / **+57%** from $2.23 close) at 18:20-18:25 ET, 746k-793k sh/bar, 6,300-6,951 trades | **Real detection miss.** Heavy-volume AH surge fired **inside** the scanned window (00:20-00:25 CET, between the 00:00 and 00:30 scans) yet WLDS never appeared in any evening scan. Likely **TradingView postmarket feed-lag** at the 00:30 scan (surge ~5-10 min old; at 18:30 ET SIP showed $3.11 = +40% from close, which should have triggered). WLDS was never a tracked name, so the 00:30 feed-lag cross-check (tracked names only) never verified it. | **YES** — AH entry $2.50 → PM peak SIP $3.69 = **+48%** |

WLDS PM: opened 04:00 ET $3.15, peak SIP **$3.69** on 1.08M sh / 13,280 trades, faded to ~$3.12. Nasdaq, float 2.0M, MCap $4.9M, neural-interface tech momentum (no specific fresh PR found; Grade None-to-unclear). This mirrors the **BTCT (Jun 30) and KUST (Jul 15) feed-lag misses** — a recurring pattern where a real in-window AH surge is not surfaced because TradingView's postmarket feed lags the SIP tape. See Notes.

### AH Mover Follow-Through

Movers that appeared in 2+ evening scans with AH change >10%:

| Ticker | AH Peak | Peak Time | AH Trajectory | Current PM | From Peak | From Close | Verdict |
|--------|---------|-----------|---------------|------------|-----------|-----------|---------|
| PAVS | $7.34 (SIP) | 17:45 ET | Build-and-hold | $5.85 | -20% | +85%→+167% faded | AH was the exit; PM peak $6.20 < AH peak |
| AKAN | $10.44 (SIP early) | 16:05 ET | Spike→fade→rebuild | $9.83 | -12% | +22% | **PM peak $11.10 > AH peak $10.44** (re-spiked at PM open, then faded) |
| JEM | $6.09 (SIP) | 17:12 ET | Late surge | ~$5.6 | -8% | +18% | AH was the better exit; PM peak $5.69 < AH peak |
| ANY | $2.32 (SIP) | 18:00 ET | Late build | $2.07 | -11% | +18% | Roughly flat AH↔PM; faded off both |

**AH-peak-vs-PM-peak:** PAVS and JEM both peaked in **after-hours** — AH was the better exit (the pattern the strategy hunts against on extended names). AKAN's PM peak ($11.10) briefly **exceeded** its AH peak ($10.44) in the first PM bar, then faded. None was an extreme >250% AH runner, so no new MSW-class data point. Winner LVWR's PM peak ($2.09) also cleanly exceeded its AH peak ($1.48) — AH→PM continuation.

### Price Charts

```
LVWR — prev close $0.77 (Jul 23) | Jul 22 close $0.91
 AH: dead-cat below close through scans → ignition 19:15 ET → SIP AH peak $1.48 (+92%) 19:20 ET
 PM: open 04:00 ET $1.37 → SIP peak $2.09 (+171%) on 3.46M sh/22.7k trades → faded ~$1.65
 Peak: $2.09 (+171%) @ 07-24 04:00 ET   [late-AH-tail surge, true-tail]

WLDS — prev close $2.23 (Jul 23, +50% regular) | Jul 22 close $1.48
 AH: build $2.17→$2.30 → SURGE 18:20 ET → SIP AH peak $3.51 (+57%/+137%) on 746-793k sh/bar
 PM: open 04:00 ET $3.15 → SIP peak $3.69 (+65%) on 1.08M sh/13.3k trades → faded ~$3.12
 Peak: $3.69 (+65% from close) @ 07-24 04:00 ET   [MISSED — in-window feed-lag]
```

### Notes

- **Late-AH-tail surge tally (updated):** LVWR (Jul 23→24, **true-tail**; genuinely sub-threshold/dead-cat at 18:30 ET, ignition 19:15 ET, SIP AH peak $1.48 +92%, PM peak $2.09; hypo AH-tail entry ~$1.35 → PM peak +55%). Prior: ORIS (Jun 22, true-tail), BTCT (Jun 29→30, feed-lag). **True-tail count now 2 (ORIS, LVWR).** The threshold to propose 1–2 late scans (~01:00/01:30 CET) is ≥3–4 true-tail winners — **not yet met** (2). A single more true-tail case would reach the bar; routing to the daily email as a scheduling recommendation at that point, not applied here.
- **Feed-lag / in-window miss tally (WLDS this cycle):** WLDS is a clear **in-window detection failure** — heavy real SIP volume (746k-793k sh/bar, ~6,900 trades) at 18:20-18:25 ET, never surfaced by the 00:30 scan. Joins BTCT (Jun 30) and KUST (Jul 15) as TradingView postmarket **feed-lag** cases. **This is now ≥3 feed-lag misses** — the pattern points at fixing/cross-checking the AH data source (e.g. a Yahoo/SIP cross-check of the whole live-scan universe at the final scan, not just already-tracked names), not at the scan schedule. **Recommend routing an AH-data-source-verification note to the daily email** (a data-reliability decision for Juan).
- **Reverse-split-recency tally (updated):** **PAVS** (Jul 23→24, 1-for-100, **Jun 25 ~4 weeks old**, float 857K, Grade C anti-dilution, entered $7.17 → PM peak $6.20 −13.5% / exited-level −18.4%, AH peak $7.34 was the better exit) — **FADED.** This is the first **non-this-week** reverse-split name to fade, softening the "months-old splits don't fade" read. Recency split now: **this-week 3/3 faded** (ELPW, YYGH, BIYA); **weeks/months-old 2/3 non-fade** (EDHL mild continue, LGCL continue, **PAVS faded**). The this-week signal (3/3 fade) still holds cleanly; the older-split bucket is mixed. Not applied as a gate — data collection.
- **Fade-rule false-negative tally: UNCHANGED. Sub-3M count stays 3 of 5, ≥4/5 trigger NOT met.** No sub-3M AH-fader re-exploded overnight. Live-flip exception stays withdrawn pending one more clean sub-3M SIP-verified blow-past.
- **Ceiling-override / dead-cat-override watch: none flagged last night, none to follow up.** LVWR was a dead-cat but was thin/dead during scans (not a multi-scan BUILD above close), so it did not qualify for the dead-cat-override watch — it was cleanly a late-AH-tail surge instead.
- **Broker-block tally: UNCHANGED.** All 4 entries (PAVS, AKAN, JEM, ANY) filled normally. No `tradable=false` blocks last night.
- **PM-only gapper tally: UNCHANGED.** Today's biggest raw PM mover (LVWR +171% SIP) is an **AH→PM continuation** (had an after-hours footprint), not a PM-only gapper. Standing holdable count stays 1 (SXTC) of 6.
- **Active Watch check:** LGCL (day 1 winner, entered $1.58, sold $1.96) faded to **$0.95** — round-trip back to its pre-pump level, one-day pump as typical. SXTC (day 3, PM-only gapper) **$2.02**, still unwinding. HIHO (day 4, entered $1.50 sold $1.26) **$1.15**, still unwinding.
</content>

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| DOMO | $3.92 | $3.93 | +0.3% | $4.50 (+14.8%) | 2 | A | HOLD | Day 2/5, $400M acquisition intact. Peak below +50% trail threshold → no trail. Above -25% hard stop ($2.94). PM $3.91-3.94 liquid. |
| JEM | $5.37 | $7.34 (fill) | +36.7% | $6.79 PM | 2 | D | SELL | Grade D → exit at any profit. Limit $5.35 filled @ $7.34 into a PM spike (08:15 ET H $6.79). |
| PAVS | $7.17 | $5.58 (fill) | -22.2% | $7.34 AH | 1 | C | SELL | Below -10% hard stop + Grade C premarket exit. PM $5.66-5.85 thin. |
| ANY | $2.29 | $2.03 (fill) | -11.4% | $2.52 AH | 2 | C | SELL | Below -10% hard stop + Grade C premarket exit. PM ~$2.04, liquid (285k sh first bar). |
| AKAN | $9.47 | ~$9.95 PM | +5% | $11.10 PM | 1 | None | SELL (pending) | Grade None → exit at profit. SELL 10 @ limit $9.80 ext live (id f58787b9); paper fill engine uses sparse IEX feed for AKAN, order resting priced-to-fill below PM range ($9.93-10.07). |

**Actions taken:**
- SELL 17 JEM @ limit $5.35 ext (id 2fc57e92) → **filled @ $7.34**. P&L **+$33.49 (+36.7%)**. Grade D exit; limit filled into PM spike.
- SELL 13 PAVS @ limit $5.55 ext (id 162792ff) → **filled @ $5.58**. P&L **-$20.67 (-22.2%)**. Grade C, below stop.
- SELL 41 ANY @ limit $2.00 ext (id e0f134e7) → **filled @ $2.03**. P&L **-$10.66 (-11.4%)**. Grade C, below stop.
- SELL 10 AKAN @ limit $9.80 ext (id f58787b9) → **live/pending** (sparse IEX fill feed). Grade None exit; order priced below PM trade range.
- HOLD DOMO (Grade A, day 2/5, catalyst intact).

**Net realized this pulse:** +$33.49 −$20.67 −$10.66 = **+$2.16** across 3 fills.
