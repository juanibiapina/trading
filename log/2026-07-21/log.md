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

## Scan 22:45 CET (4:45 PM ET) — AH

`scan.py --all` (16:45:16 ET): **5 hits.** Observation-only (learning phase: no entries before 23:00 CET).

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| CPHI | [TV](https://www.tradingview.com/chart/?symbol=CPHI) | $8.10 | +790.1% | +6.9% | $8.66 | +851.6% | 2.2M | 21.4M | 0.1x | 37.8M | Pharmaceuticals: Major |
| DFNS | [TV](https://www.tradingview.com/chart/?symbol=DFNS) | $6.57 | +54.2% | +21.8% | $8.00 | +87.8% | 394K | 2.5M | 0.2x | 88.0M | Advertising/Marketing Services |
| MIMI | [TV](https://www.tradingview.com/chart/?symbol=MIMI) | $2.16 | +1.4% | +12.5% | $2.43 | +14.1% | 360K | 5.5M | 0.1x | 4.7M | Misc Commercial Services |
| KUST | [TV](https://www.tradingview.com/chart/?symbol=KUST) | $0.96 | -24.3% | +10.3% | $1.06 | -16.5% | 102K | 9.8M | 0.0x | 577K | Misc Commercial Services |
| SNTG | [TV](https://www.tradingview.com/chart/?symbol=SNTG) | $2.09 | -0.9% | +5.3% | $2.20 | +4.3% | 63K | 16K | 4.0x | 1.1M | Finance/Rental/Leasing |

**Spike-bar instrumentation (log-only, as-of 16:45 ET):**
- DFNS — `SPIKE 16:24ET +16% $7.59 332 trades / 34k sh` (first co-spike bar)
- MIMI — `SPIKE 16:11ET +33% $2.88 144 trades / 31k sh` (first co-spike bar; unchanged from 22:30)
- KUST — `NO-SPIKE peak +17% @16:25ET` (no bar cleared +15% on a volume co-spike)

**SIP cross-check (free-tier capped at 16:30 ET / 20:30Z — ~15-min lag, expected):** The whole night so far is a **SPIKE→FADE** at the AH bell (all ignitions 16:10–16:24 ET, all now fading by 16:30):
- **DUO** (dropped from 22:45 feed) — ignited 16:10 ET to $0.88 (1.39M sh / 4258 trades), then faded $0.85→$0.54→$0.56. Round-tripped to ~flat vs $0.57 close. Classic spike→fade; fell below threshold, out of feed.
- **VIVK** (dropped from 22:45 feed) — ignited 16:10 ET to $3.11 (802K sh / 5526 trades), faded $3.05→$2.76→$2.63. Off its high, back near the $2.58 close. Spike→fade; out of feed.
- **MIMI** — peaked $2.88 (16:11 ET), faded to $2.37 by 16:30. Still +12.5% AH but declining.
- **CPHI** — Day +790% monster, AH $8.66→$7.95 fading; AH +6.9% is **below the 10% bar** and Total% +851.6% is far above the +150% ceiling. Not a candidate. 37.8M float. Note for pattern tracking (extreme intraday runner, AH giving back).
- **DFNS** — 88M float (high), $8.00→$7.25 fading after a 16:24 ET peak. VRatio 0.2x.

**Assessment:** No entries (observation-only pre-23:00). Every AH mover tonight ignited at the bell (16:10–16:24 ET) and is fading by 16:30 — a **SPIKE→FADE-only** picture so far. DUO and VIVK, the two deepest-volume ignitions, already round-tripped to near-flat and dropped out of the feed. If this pattern holds into the 23:00 entry scan, the SPIKE→FADE-only-night skip rule applies (0/10+ for PM continuation). Carry MIMI, DFNS, CPHI, KUST to 23:00; re-check DUO/VIVK for any re-ramp. No candidate currently shows a BUILD-and-hold profile.

## Scan 23:00 CET (5:00 PM ET) — AH — ENTRY-ELIGIBLE

`scan.py --all` (17:00:16 ET): **7 hits.** First entry-eligible scan of the night.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| AEHL | [TV](https://www.tradingview.com/chart/?symbol=AEHL) | $0.65 | -3.6% | +76.6% | $1.14 | +70.1% | 4.4M | 1.5M | 3.0x | 15.6M | Building Products |
| KUST | [TV](https://www.tradingview.com/chart/?symbol=KUST) | $0.96 | -24.3% | +37.4% | $1.32 | +3.9% | 1.9M | 9.9M | 0.2x | 577K | Misc Commercial Services |
| DFNS | [TV](https://www.tradingview.com/chart/?symbol=DFNS) | $6.57 | +54.2% | +12.8% | $7.41 | +74.0% | 638K | 2.6M | 0.2x | 88.0M | Advertising/Marketing Services |
| MIMI | [TV](https://www.tradingview.com/chart/?symbol=MIMI) | $2.16 | +1.4% | +5.1% | $2.27 | +6.6% | 412K | 5.5M | 0.1x | 4.7M | Misc Commercial Services |
| EZRA | [TV](https://www.tradingview.com/chart/?symbol=EZRA) | $2.29 | +1.8% | +6.1% | $2.43 | +8.0% | 156K | 74K | 2.1x | 483K | Insurance Brokers/Services |
| SNTG | [TV](https://www.tradingview.com/chart/?symbol=SNTG) | $2.09 | -0.9% | +9.7% | $2.29 | +8.7% | 86K | 19K | 4.6x | 1.1M | Finance/Rental/Leasing |
| LEXX | [TV](https://www.tradingview.com/chart/?symbol=LEXX) | $0.55 | -7.7% | +8.3% | $0.60 | -0.0% | 51K | 101K | 0.5x | 24.1M | Pharmaceuticals: Major |

Names with AH >10%: **AEHL** (+76.6%, new), **KUST** (+37.4%), **DFNS** (+12.8%). MIMI/EZRA/SNTG/LEXX all below the 10% AH bar (MIMI faded from +21.3% at 22:30 to +5.1% now — dead).

**Spike-bar instrumentation (log-only, as-of 17:00 ET):**
- AEHL — `SPIKE 16:36ET +31% $0.85 87 trades / 39k sh` (first co-spike bar; late ignition)
- KUST — `SPIKE 16:32ET +34% $1.29 466 trades / 97k sh` (first co-spike bar)
- DFNS — `SPIKE 16:24ET +16% $7.59 332 trades / 34k sh` (first co-spike bar; unchanged from 22:45)

**Tradability:** AEHL / KUST / DFNS all `tradable=true`.

**SIP verification (last bars 16:45 ET / 20:45Z, ~15-min free-tier lag — fresh relative to the 17:00 ET scan):**
- **AEHL** — real late ignition: 20:35Z (16:35 ET) 676K sh / 2687 trades, then 20:40Z (16:40 ET) **4.09M sh / 18,050 trades** exploding to H $1.38, already faded to C $0.99 by 16:45 (2.88M sh). Quote fresh $0.96/$1.02. Real volume (VRatio 3.0x confirmed) but **spike→fade off the $1.38 peak**. **First AH scan appearance → 2-AH-scan gate blocks entry tonight.**
- **KUST** — real ignition 16:30 ET building 399K → 846K → 700K sh across 16:30–16:40, peaked H $1.40 at 16:35, holding C $1.23 at 16:45 (12% off high). Quote fresh, real two-sided book $1.22/$1.24. AH% rising across scans (22:45 +10.3% → 23:00 +37.4%).
- **DFNS** — peaked H $8.30 at 16:25 ET (399K sh / 5610 trades), faded to C $7.32 by 16:45. Quote stale (ts 20:00Z, wide $5.52/$7.54). Clear **spike→fade**.

**Catalyst search:**
- **AEHL** (Antelope Enterprise, China small-cap) — recent news: H1 FY2026 results Jul 6, FY-end change Jul 9, $95K share buyback Jul 17. **No same-day (Jul 21) catalyst found** after budget. Known volatile pump name; fell 3 days into today then AH-spiked.
- **KUST** (Kustom Entertainment, micro-cap $720K mcap / 577K float) — **no same-day catalyst found**. Down-day (-24.3%) micro-float AH ramp.
- **DFNS** — no fresh same-day catalyst surfaced; high-float (88M) intraday runner giving back.

### Decisions — NO LIVE ENTRY

- **DFNS — SKIP: SPIKE→FADE.** Peaked 16:24–16:25 ET (before 17:30), declining across scans (+21.8% → +12.8%). High float 88M, no catalyst. SPIKE→FADE is 0/10+ for PM continuation.
- **KUST — DEAD-CAT-OVERRIDE WATCH (skip live, hypothetical recorded).** Day% -24.3% (≤ -15%) puts it in dead-cat territory → live entry skipped per the dead-cat filter. BUT it is *reclaiming above its regular close* ($1.23–1.32 AH vs $0.96 close) with AH% *rising* across ≥2 AH scans (22:45 +10.3% → 23:00 +37.4%) — not behaving like a genuine dead-cat bounce (which stays below the regular close). Micro-float 577K, real ignition volume, real book. Per the dead-cat-override data-collection rule: **hypothetical entry ~$1.24 @ 23:00 CET (17:00 ET), Total% +3.9%.** No catalyst. Track PM continuation for the override dataset.
- **AEHL — GATE-BLOCKED (carry).** First AH scan appearance at 23:00 → the 2-AH-scan gate can never be met via a single scan; not entry-eligible tonight regardless of trajectory. Strong new mover (VRatio 3.0x, 4.4M real AH sh) but already spike→fading off its $1.38 peak, no catalyst. Carry to 23:30 — if it re-ramps and re-appears >10%, re-evaluate (gate would then be met). Log for the morning retrospective as the night's deepest-volume AH mover.

**Night verdict:** No candidate clears all live-entry gates at 23:00. The only clean-BUILD/holding name (KUST) is dead-cat-blocked (override watch, hypothetical only). DFNS and AEHL are SPIKE→FADE. Consistent with the SPIKE→FADE-leaning picture flagged since 22:45 — every AH mover tonight ignited at/near the bell (16:10–16:36 ET) and is fading. **No live paper entry.** Carry AEHL, KUST, DFNS to 23:30/00:00; watch AEHL for a gate-meeting re-appearance and KUST for override-watch PM follow-through.

## Scan 23:30 CET (5:30 PM ET) — AH — ENTRY-ELIGIBLE

`scan.py --all` (17:30:16 ET): **10 hits.** Names with AH >10%: **AEHL** (+50.3%), **NVVE** (+29.4%, new), **KUST** (+20.7%), **SNTG** (+13.4%). CPHI/DFNS/MIMI/CRMT/LVWR/LEXX all below the 10% AH bar.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| AEHL | [TV](https://www.tradingview.com/chart/?symbol=AEHL) | $0.65 | -3.6% | +50.3% | $0.97 | +44.8% | 12.8M | 2.4M | 5.4x | 15.6M | Building Products |
| NVVE | [TV](https://www.tradingview.com/chart/?symbol=NVVE) | $7.07 | -12.4% | +29.4% | $9.15 | +13.4% | 578K | 7.0M | 0.1x | 416K | Electrical Products |
| KUST | [TV](https://www.tradingview.com/chart/?symbol=KUST) | $0.96 | -24.3% | +20.7% | $1.16 | -8.7% | 2.4M | 10.0M | 0.2x | 577K | Misc Commercial Services |
| SNTG | [TV](https://www.tradingview.com/chart/?symbol=SNTG) | $2.09 | -0.9% | +13.4% | $2.37 | +12.3% | 128K | 24K | 5.3x | 1.1M | Finance/Rental/Leasing |

**Spike-bar instrumentation (log-only, as-of 17:30 ET):**
- AEHL — `SPIKE 16:36ET +31% $0.85 87 trades / 39k sh` (unchanged from 23:00)
- NVVE — `SPIKE 16:45ET +32% $9.30 268 trades / 45k sh` (first co-spike bar)
- KUST — `SPIKE 16:32ET +34% $1.29 466 trades / 97k sh` (unchanged from 23:00)
- SNTG — `SPIKE 16:07ET +29% $2.70 56 trades / 6k sh` (early ignition, thin 6k sh)

**Tradability:** AEHL / NVVE / KUST / SNTG all `tradable=true`.

**SIP verification (last bars 21:15Z / 17:15 ET — fresh, ~15-min lag relative to the 17:30 scan):**
- **AEHL** — real ignition 16:40 ET (20:40Z) **4.09M sh / 18,050 trades** exploding to H $1.38, then a clean **fade**: $1.14→$0.99→$1.01→$0.99→$0.91→$0.92→$0.97→$0.94 (C 21:15Z). Now **32% off the $1.38 AH high** — a fade, not a hold. Quote fresh bid $0.96 / ask $1.02. Real volume (VRatio 5.4x confirmed) but SPIKE→FADE.
- **NVVE** — real late ignition 16:45 ET (20:45Z) 210K sh / 3247 trades to H $9.92, built to H $10.45 (16:55 ET), holding: recent bars $9.18→$9.75 (C 21:15Z), vwap $9.68. Now **6.7% off the $10.45 AH high — HOLDING within 20%**, on real volume (110K–270K sh/bar, thousands of trades). Post-1:18-reverse-split micro-float (~524K shares). Quote stale (bid $6.02 / ask $8.25 @ 20:00Z) but SIP shows real fresh two-sided liquidity through 21:15Z. **BUILD-and-hold.**
- **KUST** — ignition 16:30, peaked H $1.40 (16:35), faded to C $1.14 (21:15Z), **18% off high**. AH% now **falling** (23:00 +37.4% → 23:30 +20.7%). Quote fresh, two-sided $1.22/$1.24.
- **SNTG** — early ignition 16:07 ET ($2.70), faded to $2.11, choppy $2.20–2.46, now C $2.26 (21:15Z), **16% off high**. Recent bars thinning to ~1000 sh / <20 trades — volume fading hard despite VRatio 5.3x (absolute AH vol only 128K).

**Catalyst search:**
- **NVVE** (Nuvve Holding, EV/V2G) — **no same-day (Jul 21) catalyst found.** Context: 1-for-18 reverse split effective Jul 6 (share count → ~524K), 10-Q filed Jul 15, Q2 earnings not due until Aug 6. Post-reverse-split micro-float pump with repeated volatility halts; momentum/low-float move, no news catalyst.
- **AEHL** — no same-day catalyst (carried from 23:00; known volatile China small-cap pump).
- **KUST** — no same-day catalyst (carried from 23:00).

### Decisions — NO LIVE ENTRY

- **AEHL — SKIP: SPIKE→FADE (gate met).** The 2-AH-scan gate is now met (23:00 +76.6%, 23:30 +50.3%), but AH% is declining and the price is **32% off its $1.38 AH high** (peaked 16:40 ET, before 17:30). SPIKE→FADE is 0/10+ for PM continuation; no catalyst. A >20%-off-high collapse is a fade, not a hold. Skip.
- **NVVE — GATE-BLOCKED (carry, strong).** First AH scan appearance at 23:30 → the 2-AH-scan gate can never be met via a single scan; not entry-eligible tonight. But it is the night's one genuine **BUILD-and-hold**: holding within 6.7% of its $10.45 AH high on real accumulating volume, micro-float ~524K, Day% -12.4% (above -15%, not dead-cat), Total% +13.4% (well under the +150% ceiling). No catalyst (post-reverse-split momentum). **Carry to 00:00 — if it re-appears >10%, the gate is met and it becomes the strongest live candidate of the night.**
- **KUST — DEAD-CAT SKIP (override watch weakening).** Day% -24.3% (≤ -15%) → dead-cat filter blocks live entry. Prior 23:00 override-watch condition (AH% *rising* across scans while reclaiming above close) has **broken**: AH% is now *falling* (37.4% → 20.7%) and it's 18% off its high — no longer building. Hypothetical override entry from 23:00 (~$1.24) continues for the dataset, but it is now fading, not building. Skip.
- **SNTG — SKIP: gate not met + fading.** First scan >10% at 23:30 (was +5.3%, +9.7% earlier — below bar), so the 2-AH-scan gate is not met. Early peak (16:07 ET), 16% off high, volume thinning to ~1000 sh/bar. Skip.

**Night verdict:** No candidate clears all live-entry gates at 23:30. The two gate-met names are both blocked on trajectory/filter: AEHL is SPIKE→FADE (32% off high, no catalyst), KUST is a fading dead-cat. The one genuine BUILD-and-hold (NVVE) is a first-appearance name the 2-AH-scan gate structurally blocks. **No live paper entry.** Carry NVVE (primary), AEHL, KUST to 00:00 — watch NVVE for a gate-meeting re-appearance >10%.

## Scan 00:00 CET (6:00 PM ET) — AH — ENTRY-ELIGIBLE

`scan.py --all` (18:00:18 ET): **13 hits.** Names with AH >10%: **AEHL** (+53.2%), **NVVE** (+22.8%), **KUST** (+16.7%), **CPHI** (+14.8%, over-ceiling), **SNTG** (+12.0%), **IPW** (+10.8%, new), **NTCL** (+24.6%, thin/dead-cat).

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| AEHL | [TV](https://www.tradingview.com/chart/?symbol=AEHL) | $0.65 | -3.6% | +53.2% | $0.99 | +47.6% | 16.6M | 2.8M | 6.0x | 15.6M | Building Products |
| NVVE | [TV](https://www.tradingview.com/chart/?symbol=NVVE) | $7.07 | -12.4% | +22.8% | $8.68 | +7.6% | 774K | 7.0M | 0.1x | 416K | Electrical Products |
| KUST | [TV](https://www.tradingview.com/chart/?symbol=KUST) | $0.96 | -24.3% | +16.7% | $1.12 | -11.7% | 2.5M | 10.0M | 0.3x | 577K | Misc Commercial Services |
| SNTG | [TV](https://www.tradingview.com/chart/?symbol=SNTG) | $2.09 | -0.9% | +12.0% | $2.34 | +10.9% | 133K | 25K | 5.3x | 1.1M | Finance/Rental/Leasing |
| CPHI | [TV](https://www.tradingview.com/chart/?symbol=CPHI) | $8.10 | +790.1% | +14.8% | $9.30 | +922.0% | 3.8M | 21.7M | 0.2x | 37.8M | Pharmaceuticals: Major |
| IPW | [TV](https://www.tradingview.com/chart/?symbol=IPW) | $0.90 | +0.1% | +10.8% | $1.00 | +10.9% | 54K | 1.9M | 0.0x | 1.6M | Internet Retail |
| NTCL | [TV](https://www.tradingview.com/chart/?symbol=NTCL) | $3.21 | -18.5% | +24.6% | $4.00 | +1.5% | 6K | 56K | 0.1x | 755K | Packaged Software |

**Spike-bar instrumentation (log-only, as-of 18:00 ET):**
- AEHL — `SPIKE 16:36ET +31% $0.85 87 trades / 39k sh` (unchanged)
- NVVE — `SPIKE 16:45ET +32% $9.30 268 trades / 45k sh` (unchanged)
- KUST — `SPIKE 16:32ET +34% $1.29 466 trades / 97k sh` (unchanged)
- SNTG — `SPIKE 16:07ET +29% $2.70 56 trades / 6k sh` (unchanged; thin 6k-sh ignition)

**Tradability:** NVVE `tradable=true`. AEHL/KUST carried tradable=true.

**SIP verification (last bars 21:45Z / 17:45 ET — fresh, ~15-min lag relative to the 18:00 scan):**
- **NVVE** — ignition 16:45 ET (210K sh / 3247 trades) → peak **H $10.45 at 16:55 ET (very early)** → then a 30-min roll-over: recovery to $10.02 (17:15) **failed**, then $9.75 → $9.06 → $9.04 → $9.33 → $8.77 → $8.71 → **$8.80 (C 21:45Z)**. Now **15.8% off the $10.45 high** and actively declining. Volume **thinning hard**: peak bars 269K/189K sh → last bars 19K/21K sh. Quote stale/wide (bid $6.02 / ask $8.25 @ 20:00Z). Real ignition volume, but the trajectory has **turned to fade**.
- **SNTG** — thinning to ~1000–2000 sh/bar (12–22 trades), choppy $2.26–2.38, early 16:07 ET peak. Absolute AH vol only 133K despite VRatio 5.3x. Volume dying.
- **AEHL** — carried SPIKE→FADE (32%+ off its $1.38 AH high), no catalyst.
- **KUST** — carried fading dead-cat (Day -24.3%, AH% falling 37.4%→20.7%→16.7% across scans).

**Catalyst search:** NVVE — no same-day catalyst (carried from 23:30: post-1:18-reverse-split micro-float momentum, Q2 earnings due Aug 6, not tonight). AEHL/KUST/SNTG — no same-day catalyst (carried).

### Decisions — NO LIVE ENTRY

- **NVVE — SKIP: early-peak now fading (gate met but trajectory turned).** The 2-AH-scan gate is now MET (23:30 +29.4%, 00:00 +22.8%), and it was the night's one BUILD-and-hold at 23:30 (6.7% off high). But at 00:00 the profile has **rolled over**: peaked **16:55 ET (early, near the bell)**, AH% **declining across both scans** (29.4% → 22.8%), SIP price fading $9.75 → $8.80 over the last 30 min on **collapsing volume** (269K → 19K sh/bar), now 15.8% off high. Per the rule, an early peak becomes a disqualifier when the stock is *also* declining across scans — early-peak-also-fading names are 0/6+ for PM continuation. No catalyst. The within-20%-of-high floor is technically met but the active downtrend + cross-scan fade + volume death make this a SPIKE→FADE, not a hold. Skip.
- **AEHL — SKIP: SPIKE→FADE (carried).** Gate met, 32%+ off $1.38 high, declining, no catalyst. 0/10+.
- **KUST — SKIP: fading dead-cat (carried).** Day -24.3%, override-watch broke (AH% now falling 3 scans running). Hypothetical override entry from 23:00 (~$1.24) continues for the dataset only.
- **SNTG — SKIP: SPIKE→FADE + dying volume.** Gate technically met (23:30 +13.4%, 00:00 +12.0%) but early 16:07 ET peak, volume thinning to ~1–2K sh/bar. Thin, faded.
- **CPHI — not a candidate:** Total% +922% (far over +150% ceiling), extreme intraday runner giving back AH.
- **NTCL / IPW — SKIP:** NTCL 6K AH vol (thin), Day -18.5% dead-cat, Total +1.5%, first appearance. IPW first appearance at 00:00 (+10.8%), 54K vol — 2-AH-scan gate not met.

**Night verdict:** No candidate clears all live-entry gates with a hold/build trajectory. NVVE — the one BUILD-and-hold at 23:30 and the sole gate-met name with float/Day%/ceiling all clean — **turned to fade at 00:00** (early 16:55 peak, declining across scans, volume death). Every AH mover tonight ignited at/near the bell (16:07–16:55 ET) and is fading — a **SPIKE→FADE-only** picture. Per the SPIKE→FADE-only-night rule (0/10+ PM continuation), **no live paper entry.** Carry NVVE, AEHL, KUST, SNTG to the final 00:30 scan; run the final-scan feed-lag cross-check there.

## Scan 00:30 CET (6:30 PM ET) — AH — ENTRY-ELIGIBLE — FINAL SCAN

`scan.py --all` (18:30:17 ET): **13 hits.** Names with AH >10%: **AEHL** (+37.9%), **CPHI** (+55.6%, over-ceiling), **NVVE** (+24.5%), **KUST** (+17.6%, dead-cat), **MIMI** (+11.1%), **SNTG** (+10.5%).

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| AEHL | [TV](https://www.tradingview.com/chart/?symbol=AEHL) | $0.65 | -3.6% | +37.9% | $0.89 | +32.9% | 17.9M | 2.9M | 6.1x | 15.6M | Building Products |
| CPHI | [TV](https://www.tradingview.com/chart/?symbol=CPHI) | $8.10 | +790.1% | +55.6% | $12.60 | +1284.6% | 5.6M | 22.0M | 0.3x | 37.8M | Pharmaceuticals: Major |
| NVVE | [TV](https://www.tradingview.com/chart/?symbol=NVVE) | $7.07 | -12.4% | +24.5% | $8.80 | +9.1% | 826K | 7.0M | 0.1x | 416K | Electrical Products |
| KUST | [TV](https://www.tradingview.com/chart/?symbol=KUST) | $0.96 | -24.3% | +17.6% | $1.13 | -11.0% | 2.6M | 10.0M | 0.3x | 577K | Misc Commercial Services |
| MIMI | [TV](https://www.tradingview.com/chart/?symbol=MIMI) | $2.16 | +1.4% | +11.1% | $2.40 | +12.7% | 466K | 5.5M | 0.1x | 4.7M | Misc Commercial Services |
| SNTG | [TV](https://www.tradingview.com/chart/?symbol=SNTG) | $2.09 | -0.9% | +10.5% | $2.31 | +9.5% | 140K | 26K | 5.4x | 1.1M | Finance/Rental/Leasing |

**Spike-bar instrumentation (log-only, as-of 18:30 ET):**
- AEHL — `SPIKE 16:36ET +31% $0.85 87 trades / 39k sh` (unchanged)
- NVVE — `SPIKE 16:45ET +32% $9.30 268 trades / 45k sh` (unchanged)
- KUST — `SPIKE 16:32ET +34% $1.29 466 trades / 97k sh` (unchanged)
- SNTG — `SPIKE 16:07ET +29% $2.70 56 trades / 6k sh` (unchanged; thin 6k-sh ignition)

**Final-scan feed-lag cross-check (SIP bars through 21:55Z / 17:55 ET — fresh, ~35-min behind the 18:30 scan; TradingView and SIP agree, no under-reporting rescue triggered):**
- **AEHL** — post-ignition ($1.38 peak 16:40 ET) SIP faded and is chopping $0.89–1.11, last bars C $0.89 (21:55Z) on 340K sh. **~35% off the AH high** — SPIKE→FADE confirmed on fresh SIP. Real volume (VRatio 6.1x) but no hold.
- **NVVE** — peak $10.45 (16:55 ET), SIP now C $8.62 (21:55Z), **~17.5% off high**, volume collapsed (peak 269K sh/bar → last bars 10K–21K sh, ~190–300 trades). Declining across all three gate scans (29.4% → 22.8% → 24.5% is noisy but SIP price trend is down). SPIKE→FADE / early-peak-also-fading.
- **KUST** — dead-cat (Day -24.3%), AH% falling across scans (37.4% → 20.7% → 16.7% → 17.6%), SIP $1.10–1.16 on thin 5K–40K sh/bar. Still above its $0.96 close but no longer building. Dead-cat blocked.
- **SNTG** — dead: SIP 2–2062 sh/bar, 2–41 trades. Early 16:07 peak, volume dead. Absolute AH vol only 140K despite VRatio 5.4x.
- **CPHI** — Total% +1284.6% (extreme runner far over +150% ceiling), not a candidate.
- **MIMI** — 466K AH vol, Total +12.7%, faded since 22:30 (+21.3% → +11.1%). Not a hold.

**No tracked name is under-reported by TradingView while surging on SIP.** Every pipeline name (AEHL, NVVE, KUST, SNTG, MIMI, DFNS, DUO, VIVK, CPHI) is confirmed fading/dead on fresh SIP. No data-source rescue this night.

### Decisions — NO LIVE ENTRY

- **AEHL — SKIP: SPIKE→FADE.** Gate met, ~35% off $1.38 high, no catalyst. 0/10+.
- **NVVE — SKIP: early-peak-also-fading.** Gate met but peaked 16:55 ET (early), ~17.5% off high, volume collapsed, declining SIP trend. No catalyst. Early-peak-also-fading is 0/6+.
- **KUST — SKIP: fading dead-cat.** Day -24.3%, override-watch broke (AH% falling 4 scans running). Hypothetical override entry from 23:00 (~$1.24) continues for the dataset only.
- **SNTG — SKIP: SPIKE→FADE + dead volume.** Early 16:07 peak, 2–2062 sh/bar. Thin, faded.
- **CPHI — not a candidate:** +1284.6% Total%, extreme runner over ceiling.
- **MIMI — SKIP: faded since 22:30, not a hold.**

**Night verdict — SPIKE→FADE-ONLY NIGHT, NO ENTRY.** Every AH mover tonight ignited at/near the bell (16:07–16:55 ET) and faded by 17:30. The one BUILD-and-hold candidate (NVVE) turned to fade at 00:00 and stayed faded at 00:30. No candidate holds within ~20% of its AH high on sustained volume. Per the SPIKE→FADE-only-night skip rule (0/10+ PM continuation), **no live paper entry.** A skip here avoids a predictable loss, not lost data.

**Note for morning eval / email:** clean SPIKE→FADE-only night — no entry is the correct call. The night's deepest-volume mover (AEHL, VRatio 6.1x, 17.9M AH sh) was a real spike→fade off $1.38; the one genuine BUILD-and-hold (NVVE) was a first-appearance-at-23:30 name the 2-AH-scan gate structurally delayed, and it rolled over before the gate could clear on a holding trajectory. No detection gap; the scanner surfaced every mover.
