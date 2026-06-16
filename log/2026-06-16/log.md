# Morning Evaluation - 2026-06-16

## Morning Evaluation — 10:21 CET

_Pulse 1. PM session only ~20 min old (now 04:21 ET). Peaks below are "so far"; position-evaluation (10:30/14:30 CET) tracks the rest of premarket._

### Today's Winner

**CRVO** — Misc Commercial Services (CervoMed Inc., biotech)
- Catalyst: None fresh. Known items predate the spike — $10.5M private placement (Jun 10, Grade D dilution) and H.C. Wainwright Neuro Summit appearance (Jun 15 AM). Late unexplained AH spike at 17:40 ET.
- Previous Close: $2.45 (Jun 15 regular close $2.48, Day +1.2%)
- AH last night: $3.77 (+53.9%) at 18:20 ET / 00:20 CET — BUILD-and-hold, late new high
- Premarket now: $3.28 (+33.9%), PM peak $3.74 (+52.7%) at 04:10 ET so far
- Hypothetical P&L (AH entry → PM peak): early AH entry ~$3.37 → PM peak $3.74 = **+11%**
- Float: 4.8M | Market Cap: $23.0M | VRatio at entry 5.8x

**Scanner Diagnostic:**
- Detectable at screening time? **YES** — and we acted on it. CRVO appeared in the 00:00 CET scan (+35.9%) and activated on the 2nd AH scan at 00:30 CET (+50.8%), where we entered a paper trade at $3.64.
- BUILD-and-hold pattern: flat all afternoon → spiked +36.7% at 17:40 ET → new AH high $3.77 at 18:20 ET → held +48%. Float 4.8M ideal, VRatio jumped 1.1x→5.8x.
- Scanner gap: none for CRVO. It was caught and traded correctly. The gap is the **PM-only gapper** (see TDIC below), which AH screening structurally cannot catch.

**Biggest raw PM mover (not an AH→PM winner): TDIC** — Dreamland Limited
- PM now ~$11.05 (+92%), PM peak $13.83 (+140.8%) at 04:05 ET, vs prev close ~$5.74.
- **Flat/down in after-hours** ($5.30–$5.50, -4% to -8% all evening). No AH signal whatsoever.
- This is a pure premarket gapper — news likely broke overnight/early AM. Our evening AH scanner could **not** have flagged it; there was nothing to detect. Structural blind spot of the AH→PM strategy.

### Baseline Tracking

- Days tracked: **31** (was 30 + 1)
- Winners detected by scanner: **27/31 (87.1%)** — HIT, SUNE, DRMA, UGRO, NXTT, POLA, BCG, PFSA, MASK, EZGO, AIIO, HTCO, WOK, LNKS, AMST, PHGE (May 20), PHGE (May 26), SNGX, ATPC, PRFX, DXST, TWAV, CHAI, MSW, TMDE, BYAH, **CRVO**
- Winner selected for paper trade: **19/31 (61.3%)** — incremented; we entered CRVO (the AH→PM winner) at $3.64, 00:30 CET
- Target: >80% detection
- Status: **BASELINE MET** (87.1% detection)

### Retrospective Scan Results

- **PM scan (04:20 ET):** 3 hits — TDIC (+100.9%), CRVO (+46.0%), HITI (+21.8%)
- **Forced AH scan (04:20 ET):** 0 hits (overnight TradingView postmarket fields return 0, as expected — use evening live scans as the retrospective source)
- **AH reconstruction (check-prices --ah-history):**
  - CRVO: AH high $3.77 (+53.9%) at 18:20 ET → held +38-40% into close of AH. Clean AH→PM continuation.
  - TDIC: AH $5.30-$5.50 (-4% to -8%). No AH move. PM-only gapper.
  - HITI: AH high $2.74 (+18.6%) → PM $2.83 (+22.5%). Modest, held.
- **Data quirk:** Yahoo's Jun 15 daily close is null for several names, so `check-prices.py` defaults its "prev close" to the Jun 12 value. This badly distorts RGNT (shows +386% off a stale $1.50 ref; RGNT actually closed ~$9.40 Jun 15 and is ~$7.30 PM = **down**). `price-timeline.py` also printed impossible "08:00 ET" bars (future data at 04:20 ET) — disregarded; pm-history is the reliable current snapshot.

### Paper Trade P&L

| Ticker | Entry | Entry Total% | Catalyst | Entry Time | PM Peak | Peak Time | Exit | P&L | P&L % | Status |
|--------|-------|--------------|----------|------------|---------|-----------|------|-----|-------|--------|
| HUBC   | $2.06 | +74.6% | None — no catalyst, dilution risk | 23:30 CET | $1.96 | 04:20 ET | — | -€5.28 | -5.3% | 🔴 Open |
| WCT    | $1.94 | +33.8% | D — 1-for-400 reverse consolidation | 23:30 CET | $1.62 | 04:00 ET | — | -€20.91 | -21.1% | 🔴 Open |
| CRVO   | $3.64 | +48.6% | None — late AH spike, Jun 10 dilution | 00:30 CET | $3.74 | 04:10 ET | — | -€9.72 | -9.9% | 🔴 Open |

_PM only 20 min old; peaks are provisional. Exit decisions handled by position-evaluation._

**Total Paper P&L (unrealized, provisional): -€35.91**

### Scanner Effectiveness

- Evening scans ran: 7 times (21:30 - 00:30 CET)
- Candidates found: ~15 unique tickers (HITI, ZNB, AVAT, HUBC, CIIT, WCT, RGNT, SKYA, GELS, CRVO, AHMA, UCAR, GMM, + 21:30 regular-session watch list)
- Retrospective matches: CRVO caught (the AH→PM winner). TDIC missed (PM-only gapper, undetectable in AH).

### Missed Opportunities

| Ticker | AH Change | Why Missed | Would Be Profitable? |
|--------|-----------|------------|---------------------|
| TDIC | Flat/down (-4% to -8%) | PM-only gapper — no AH move to detect; news broke overnight/early AM | Yes as a PM-only play (+140%), but NOT an AH→PM trade — outside strategy scope |

### AH Mover Follow-Through

| Ticker | AH Peak | Peak Time | AH Trajectory | Current PM | From Peak | From Close | Verdict |
|--------|---------|-----------|---------------|------------|-----------|------------|---------|
| HUBC | $2.19 (+85.6%) | 17:30 ET | Build → ease | $1.95 | -11% | +16% (vs $1.68) | Faded; AH was better exit |
| CRVO | $3.77 (+53.9%) | 18:20 ET | Build-and-hold | $3.28 (peak $3.74) | ~flat at peak | +34% (vs $2.45) | Held; PM ≈ AH peak |
| WCT | $1.99 (~+37%) | 17:25 ET | Choppy whipsaw | $1.53 (peak $1.62) | -19% | +5% (vs $1.45) | Faded |
| HITI | $2.74 (+18.6%) | 16:05 ET | Spike → hold | $2.79 (peak $2.83) | +3% | +21% (vs $2.31) | Held/built; PM exceeded AH |
| ZNB | ~$1.58 (+66%) | 16:15 ET | Spike → fade | $0.93 | — | -2% | Faded hard (correctly skipped) |
| RGNT | +599% total | regular blow-off | Regular blow-off | ~$7.30 | down | down vs $9.40 close | Faded (correctly skipped, ceiling) |

**AH-peak-vs-PM-peak check:** HUBC and WCT both peaked in AH and faded into PM (AH was the better exit). CRVO peaked roughly equal AH≈PM. HITI's PM peak slightly exceeded its AH peak. No new clean data point for the extreme-AH-runner (>250% from close) fade hypothesis this session — RGNT's +599% was regular-session driven, not an AH run, but it faded into PM (directionally consistent).

### Price Charts

CRVO AH→PM (from check-prices, ET):
```
AH:  16:00 $2.48 (flat) → 17:40 $3.35 (+36.7% spike) → 18:20 $3.77 (+53.9% high) → held +38-40% to 19:55
PM:  04:00 $3.62 (+47.8%) → 04:10 $3.74 (+52.7% peak so far) → 04:20 $3.28 (+33.9%)
```

TDIC PM-only gapper (ET):
```
AH:  16:00-19:55 $5.30-$5.50 (-4% to -8%, no move)
PM:  04:00 $10.64 (+85%) → 04:05 $13.83 (+140.8% peak) → 04:20 $11.05 (+92%)
```

_(price-timeline.py output omitted — its post-04:20 ET timestamps are a timezone artifact and not real data at this hour.)_

### Notes

- **Clean detection day for the AH→PM strategy:** CRVO was caught, activated on the 2-scan gate, and traded. Detection rate ticks to 87.1% (27/31), and we selected the right stock (19/31 selected).
- **The real story is TDIC** (+140% PM, pure gapper). This is the recurring PM-only blind spot: a stock with no AH footprint that explodes after 04:00 ET on overnight news. AH screening cannot catch these by design. Worth tracking how often the morning's *biggest* mover is a PM-only gapper vs an AH→PM continuation — if PM-only gappers dominate, a separate early-PM scan workflow may be warranted.
- **Open positions are red so far**, but PM is only 20 min old. HUBC and WCT both faded from AH (no fresh catalyst / reverse-split overhang — the weak-catalyst names underperforming again). CRVO holding near its AH level.
- No ceiling-override or dead-cat-override watch candidates were flagged last night, so no override-watch outcomes to tally.
</content>
</invoke>
