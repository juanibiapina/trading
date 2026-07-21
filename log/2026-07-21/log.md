# Morning Evaluation - 2026-07-21

## Morning Evaluation — 10:20 CET

### Today's Winner

**HIHO** — Miscellaneous Manufacturing (Highway Holdings Limited)
- Catalyst: **Grade B** — Q1 FY2027 earnings (Mon Jul 20): net sales ~$2.0M **+29.2% YoY**, gross profit +58.4% to $835K, margin +800bps to 42%, return to net-income growth
- Previous Close: $0.81
- AH last night: **$1.69 (+108%)** at 16:35 ET (22:35 CET), SIP 2.6M sh / 12.5k trades that bar
- Premarket now: **$1.66 (+105%)**, live SIP; **PM peak $1.89 (+133%)** at 04:00 ET
- Hypothetical P&L (AH entry → PM peak): our fill $1.50 → $1.89 = **+26%**; early-AH ~$1.31 → $1.89 = **+44%**
- Float: 2.8M | Market Cap: ~$4.3M
- **SIP volume confirming the bar:** AH ramp bars 195K → 3.26M → 3.48M → 1.43M → 2.98M → 2.14M → 2.59M sh (thousands of trades/bar); PM re-explosion 4.9M sh / 30,638 trades in the 04:00 ET bar. Real, accumulating volume — clears the >100% winner bar decisively.

**Scanner Diagnostic:**
- Detectable at screening time? **YES — and DETECTED + ENTERED.**
- HIHO appeared in **6 consecutive AH scans** (22:30 +49.5%, 22:45 +59.2%, 23:00 +67.8%, 23:30, 00:00, 00:30). Entered at the 23:00 CET entry-eligible scan **@ $1.50** (59 sh, id ddf2e698) once the 2-AH-scan gate was met, as a Grade B low-float (2.8M) BUILD with real SIP accumulation, Total% +100.8% under the +150% ceiling.
- **This is the best-case outcome:** the scanner caught the winner AND we traded it. No gap.
- Scanner gap: none for this name.

**Note (sub-3M-float re-ramp hypothesis):** HIHO faded from its $1.69 AH high to ~$1.28 through the evening, then **re-exploded in PM to $1.89** — the classic sub-3M-float (2.8M) fade→re-explode shape. This is *not* a fade-rule false negative (we entered before the fade, never skipped it), but it corroborates the hypothesis that sub-3M-float AH-faders re-ramp in PM. It also shows PM peak ($1.89) exceeded AH peak ($1.69): a continuation, not the extreme-runner AH-fade pattern (HIHO stayed under +250% AH).

### Baseline Tracking

Prior baseline (2026-07-16 log): 50 days, 43/48 detected, 24/48 selected. **Tracking gap:** logs 07-17 through 07-20 carry no `Days tracked:` line (morning evals on the 07-17 Fri and 07-20 Mon trading days did not record baseline), so intervening sessions were not baseline-counted; the denominator understates true trading days. Incrementing by 1 for the 07-20 winner per the standard rule.

- Days tracked: **51** (was 50 + 1)
- Winners detected by scanner: **44/49 (89.8%)** — HIHO added (detected across 6 AH scans 22:30–00:30 CET)
- Winner selected for paper trade: **25/49 (51.0%)** — HIHO entered @ $1.50; we traded the right stock
- Target: >80% detection
- Status: **BASELINE MET**

### Retrospective Scan Results

- Live PM scan (04:20 ET): 5 hits — HIHO +78.6% ($1.66), RDGT +43.0% ($2.26), SLGB +18.3%, PAPL +25.4%, LASE +11.9%. HIHO the clear standout.
- Forced AH scan: 0 hits (postmarket TradingView field empty overnight — expected, per known limitation).
- AH reconstruction (`--ah-history` + SIP bars) confirms HIHO as the night's only >100% mover on real accumulating volume.

### Open Position P&L (Alpaca)

| Ticker | Entry | Entry Total% | Catalyst | Entry Time | PM Peak | Peak Time | Exit | P&L | P&L % | Status |
|--------|-------|--------------|----------|------------|---------|-----------|------|-----|-------|--------|
| HIHO | $1.50 | +85.2% | B — Q1 earnings +29.2% YoY sales | 2026-07-20 23:01 CET | $1.89 (SIP) | 04:00 ET | open | — | +10.7% (live) | 🟢 Open, up |
| PAPL | $1.10 | +25.0% | B — Pineapple Fin Q3 earnings | 2026-07-21 00:01 CET | $1.28 (SIP) | 04:00 ET | open | — | -2.7% (live) | 🔴 Open, down |

**Quote-freshness note:** Alpaca `positions` reported HIHO $1.61 (+7.3%) and PAPL $1.06 (-3.6%), but both quotes are stale (HIHO ts 20:59Z / PAPL ts 20:00Z = last night's close; PAPL book shows `ask $0.00 x0`). Live SIP PM: HIHO last bar (08:05Z) closed **$1.66** → P&L **+10.7%**; PAPL last bar closed **$1.07** → P&L **-2.7%**. P&L reported against the live SIP prices, not the stale Alpaca figures. **Exits handled by position-evaluation (10:30 / 14:30 CET) — not here.**

**Total Realized P&L (Alpaca fills only): €0.00** (both positions still open)

### Scanner Effectiveness

- Evening scans ran: **7 of 7** scheduled (21:30, 22:00, 22:30, 23:00, 23:30, 00:00, 00:30 CET; plus extra 22:15 / 22:45 observation scans). Full coverage — entry window intact.
- Candidates found: HIHO, PAPL, ADVB, RDGT, SHPH, GORO, GBR, SLGB, HXHX, CJMB, others
- Retrospective matches: HIHO (winner) fully caught + entered; PAPL entered; ADVB / RDGT surfaced but gate/ceiling-blocked.

### Missed Opportunities

| Ticker | AH Change | Why Missed | Would Be Profitable? |
|--------|-----------|------------|---------------------|
| RDGT | +24.7% AH | 1st AH scan appearance at the **final** 00:30 scan → 2-AH-scan gate can never be met; not a threshold miss | PM peak $2.33 (SIP, +47% from $1.58) at 04:00 ET on 1.9M sh — a real late micro-float mover the gate structurally blocks |

No true detection miss: the winner was caught and traded.

### AH Mover Follow-Through

| Ticker | AH Peak | Peak Time | AH Trajectory | Current PM | From Peak | From Close | Verdict |
|--------|---------|-----------|---------------|------------|-----------|-----------|---------|
| HIHO | $1.69 (+108%) | 16:35 ET | Spike→hold→PM re-explode | $1.66 (PM peak $1.89) | PM peak +12% vs AH peak | +105% | ✅ Winner, entered; **PM peak > AH peak (continuation)** |
| ADVB | $13.05 (+159%) | 18:15 ET | Build (late) | $9.88 (PM peak $11.00) | **-16% below AH peak** | +96% | AH was the better exit; ceiling-skip validated |
| PAPL | $1.33 (+51%) | 17:35 ET | Build→fade | $1.07 (PM peak $1.28) | -20% below AH peak | +22% | Entered $1.10; faded, roughly flat |
| RDGT | $2.07 (+31%) | 18:00 ET | Late surge | $2.27 (PM peak $2.33) | PM peak +13% vs AH peak | +47% | Gate-blocked; PM continued |

**AH-peak-vs-PM-peak check:** HIHO and RDGT continued higher into PM (PM peak > AH peak). ADVB (+159% AH, extended) and PAPL faded into PM (AH peak was the better exit). ADVB adds to the extreme-runner-fades dataset (though under the 250% threshold): a +159% AH runner peaked in AH ($13.05) and gave back to $11.00 PM.

### Price Charts

```
HIHO — 2-Day Price Timeline
Previous Close: $0.81 | 2-Day Range: $0.71 - $1.89
Current: $1.57 (+93.8%) | Peak: $1.89 (+133.3%) at 07-21 04:00 ET
AH: spike to $1.69 (16:35 ET) → hold ~$1.28-1.40 overnight → PM re-explosion to $1.89 (04:00 ET, 4.9M sh / 30.6k trades)
```

### Notes

- **Full-coverage clean night, winner caught + traded.** HIHO is a textbook detected-and-entered winner: Grade B earnings catalyst, low float 2.8M, multi-scan AH BUILD, real SIP volume, entered under the +150% ceiling. Best-case scanner outcome. PM re-explosion (+133%) beat the AH peak — let-winners-run: PM peak $1.89 vs our $1.50 entry = +26% available; position-evaluation manages the exit.

- **ADVB ceiling-override watch outcome (2026-07-20 → 21):** skipped at 00:30 CET only on the +150% ceiling (SIP-real ~+156-158%, TradingView-printed +125% was feed-lag). Hypothetical skipped entry ~$12.91 → **PM peak $11.00 = -15%**. ADVB **faded** into PM (AH peak $13.05 > PM peak $11.00). **Ceiling rule validated** — the extended entry would have lost. Running ceiling-override tally now leans toward keeping the ceiling.

- **RDGT gate-structure note:** a real micro-float (884K) late mover — 1st AH appearance at the final 00:30 scan, PM continued to $2.33 (+47%). Same structural class as prior "late-at-final-scan" names the 2-AH-scan gate blocks; not a detection or threshold miss. Watch-only.

- **Sub-3M-float fade→re-explode tally (corroborating, not a false negative):** HIHO 2.8M faded $1.69→$1.28 then PM $1.89. We entered it, so it does not increment the fade-rule false-negative count (still **sub-3M 3 of 5**, ≥4/5 trigger NOT met), but it's another sub-3M name that re-ramped in PM — consistent with the hypothesis.

- **Baseline tracking gap:** no `Days tracked:` line in the 07-17 / 07-20 logs (morning evals those days didn't record baseline). Flag for Juan (email): the retrospective baseline was not maintained on 2 trading days; if morning-eval runs are being skipped or not committed, the detection denominator drifts. One-off vs recurring is unclear — worth a look at the scheduler for the morning-eval pulse.

- **Broker-block:** SHPH again `tradable=false` across all AH scans (qualified-but-untradable; the recurring low-float pharma broker-block). AH +18-24% but no fillable book. Adds to the cumulative tradability-gap dataset.
</content>

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Peak % | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|--------|------|-------|----------|--------|
| HIHO | $1.50 | ~$1.59 (SIP) | +6% | $1.89 | +26% | 1 | B | HOLD | Day 1 of 2, catalyst intact, peak under +30% trail threshold, above -15% hard stop ($1.28) |
| PAPL | $1.10 | ~$1.06 (SIP) | -3.6% | $1.33 | +21% | 1 | B | HOLD | Day 1 of 2, catalyst intact, peak under +30% trail threshold, above -15% hard stop ($0.94) |

**Data note:** Alpaca quote feed stale (HIHO ts 20:59Z, PAPL ts 20:00Z = last night's close; PAPL book `ask $0.00 x0`). P&L based on live SIP 5Min bars (last bar 08:15Z / 04:15 ET). HIHO SIP last close $1.59 / vwap $1.62; PAPL SIP last close $1.06 / vwap $1.08. Early premarket (~04:30 ET) — thin so far.

**Actions taken:**
- None. Both HOLD. No trail stops set (both peaks under +30% Grade B trail threshold). No hard stops hit. No time limit reached (Grade B allows 2 days; both are day 1).
- Next evaluation 14:30 CET pulse.

## Position Evaluation — 14:30 CET

| Ticker | Entry | Current | P&L % | Peak | Peak % | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|--------|------|-------|----------|--------|
| HIHO | $1.50 | $1.26 (fill) | -16.0% | $1.89 | +26% | 2 | B | SELL | Day-2 time limit reached AND at -15% hard stop ($1.28). SIP PM opened $1.89 then faded; live bid $1.21 x1000 |
| PAPL | $1.10 | $0.84 (fill) | -23.6% | $1.33 | +21% | 1 | B | SELL | Below -15% hard stop ($0.94). SIP PM faded $1.28→$0.83 on real volume |

**Data note:** HIHO Alpaca quote fresh at pulse (bid $1.21 x1000, ask $1.27 x1000). PAPL Alpaca quote stale (yesterday 20:00Z, `ask $0.00 x0`) but SIP 5Min bars showed real PM liquidity (341K/153K/180K sh recent bars) at $0.80-0.85 — used SIP for exit price. Both fills came in above limit.

**Actions taken:**
- **SELL HIHO** 59 @ limit $1.18 ext (id f879332a) → filled @ **$1.26**. P&L **-$14.16 (-16.0%)**. Grade B day-2 time limit + hard stop.
- **SELL PAPL** 80 @ limit $0.79 ext (id 9ca4f305) → filled @ **$0.84**. P&L **-$20.80 (-23.6%)**. Grade B below -15% hard stop.
- Both moved to Closed Positions in OPEN_POSITIONS.md. **Flat — no open positions.**
- Combined realized P&L this pulse: **-$34.96**.

---

# Post-Market Screening - 2026-07-21

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|

## Scan 21:30 CET (3:30 PM ET) — REGULAR SESSION

Regular-session scan, before AH opens (22:00 CET / 4:00 PM ET). **No entries** per regular-session caution rule. Candidates flagged Watch — pending AH confirmation. Only enter if a name reappears in an AH scan (22:00+ CET) with sustained momentum.

Notable low-float / big intraday movers to watch into AH:

| Ticker | Price | Chg% | Float | IRVol | VChg% | Industry | Note |
|--------|-------|------|-------|-------|-------|----------|------|
| VIVK | $3.00 | +73.7% | 405K | 211.3 | -68.3 | Chemicals: Specialty | Tiny float, big move; vol fading |
| OMH | $0.79 | +216.5% | 22.2M | 2713.1 | -100.0 | Real Estate Dev | Huge % but vol collapsing |
| SLGB | $0.97 | +90.7% | 3.0M | 1228.0 | -99.2 | Air Freight | Low float; vol fading hard |
| MLEC | $9.20 | +39.4% | 200K | 43.3 | +202.6 | Misc Commercial Svcs | Micro-float, vol building |
| DFNS | $6.56 | +54.0% | 88.0M | 56.1 | -49.6 | Advertising/Mktg | High float |
| GREE | $2.88 | +35.2% | 10.7M | 37.9 | +189.5 | Packaged Software | Vol building |
| KIDZ | $0.55 | +32.9% | 2.1M | 77.7 | -36.1 | Internet Software | Low float |

**Watch — pending AH confirmation:** VIVK, MLEC, SLGB, KIDZ (lowest floats). No catalyst research or entries at regular-session scan; re-evaluate at 22:00+ CET AH scans.

## Scan 22:00 CET (4:00 PM ET) — AH OPEN

`scan.py --all` (16:00:10 ET): **0 hits.** AH just opened at the scan minute — TradingView `postmarket_volume`/`postmarket_change` fields are empty at the bell, the expected first-scan blank. No candidates surfaced.

Observation-only scan (learning phase: no entries before 23:00 CET). None of the 21:30 regular-session watch names (VIVK, MLEC, SLGB, KIDZ) re-appeared in the AH feed yet — too early; re-check at 22:30. No entries.

## Scan 22:15 CET (4:15 PM ET) — AH

`scan.py --all` (16:15:10 ET): **0 hits.** No candidates. AH feed still empty 15 min after the bell — TradingView `postmarket_volume`/`postmarket_change` fields not yet populated for movers.

Observation-only scan (learning phase: no entries before 23:00 CET). Watch names from 21:30 (VIVK, MLEC, SLGB, KIDZ) still not surfacing in the AH feed. No candidates >10% AH → no spike-bar instrumentation to run this scan. No entries.

## Scan 22:30 CET (4:30 PM ET) — AH

`scan.py --all` (16:30:11 ET): **4 hits.** AH feed populated — first real candidates of the night.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| DUO | [TV](https://www.tradingview.com/chart/?symbol=DUO) | $0.57 | +5.6% | +47.0% | $0.84 | +55.3% | 1.3M | 164K | 8.1x | 38.5M | Internet Software/Services |
| VIVK | [TV](https://www.tradingview.com/chart/?symbol=VIVK) | $2.58 | +49.1% | +18.6% | $3.06 | +76.9% | 1.0M | 14.8M | 0.1x | 405K | Chemicals: Specialty |
| MIMI | [TV](https://www.tradingview.com/chart/?symbol=MIMI) | $2.16 | +1.4% | +21.3% | $2.62 | +23.0% | 130K | 5.4M | 0.0x | 4.7M | Misc Commercial Services |
| KUST | [TV](https://www.tradingview.com/chart/?symbol=KUST) | $0.96 | -24.3% | +6.2% | $1.02 | -19.7% | 72K | 9.7M | 0.0x | 577K | Misc Commercial Services |

**Spike-bar instrumentation (log-only, as-of 16:30 ET):**
- DUO — `SPIKE 16:10ET +19% $0.68 105 trades / 37k sh` (first co-spike bar)
- VIVK — `SPIKE 16:13ET +17% $3.02 1650 trades / 218k sh` (first co-spike bar)
- MIMI — `SPIKE 16:11ET +33% $2.88 144 trades / 31k sh` (first co-spike bar)

All three fired an ignition bar early in AH (16:10–16:13 ET). VIVK's ignition bar is by far the deepest (1650 trades / 218k sh) vs DUO (105 trades / 37k sh) and MIMI (144 trades / 31k sh).

**Observation-only (learning phase: no entries before 23:00 CET). No catalyst research or entries this scan** — full workup deferred to the 23:00 entry-eligible scan. Notes for pattern tracking:
- **DUO** — 38.5M float (high), but VRatio 8.1x is the only *real* AH-volume signal of the night (1.3M sh AH on 164K avg). AH +47%, Total +55.3% (under the +150% ceiling). New name (not on the 21:30 watch). First co-spike late (16:10 ET early). Internet Software.
- **VIVK** — 405K micro-float, and it carried its regular-session pump (+49.1% Day, +73.7% intraday at 21:30) into AH (+18.6% AH → +76.9% Total). This is the first 21:30 watch name to reappear in AH. VRatio 0.1x is an artifact of the huge 14.8M avg vol (today's regular-session pump inflated the denominator), not thin AH — SIP spike-bar shows 218k sh on the ignition bar. **Total% +76.9% under ceiling.** Watch for BUILD vs fade into 23:00.
- **MIMI** — 4.7M float, AH +21.3%, but AH vol only 130K (VRatio 0.0x) — thinnest of the three. Total% +23.0% (low extension). Watch.
- **KUST** — Day -24.3% (dead-cat territory), AH only +6.2% (below the 10% bar), Total% still negative (-19.7%). Not a candidate; note it was a 07-14 feed-lag name but tonight it is a faded down-day, not a mover.

Carry DUO, VIVK, MIMI to the 23:00 scan for the 2-AH-scan gate + full catalyst workup. All three need a second AH appearance at 23:00 before any entry is eligible.
