# Trade Log — 2026-06-12

## Morning Evaluation — 10:20 CET

### Today's Winner

**BYAH** — Park Ha Biological Technology (Household/Personal Care, Chinese micro-cap)
- Catalyst: **None found** — low-float speculative pump. Day −15.3% sell-off in regular session, then explosive AH BUILD. No fresh same-day PR.
- Previous Close (Jun 10): $1.24 | Jun 11 regular close: $1.05 (Day −15.3%)
- AH last night: strong **BUILD** — +39.5% (16:25 ET) → +108.9% (17:30) → **AH peak $2.75 (+121.8%) at 18:40 ET**, held +85–94% into 20:00 ET
- Premarket now: **PM peak $3.58 (+188.7% from $1.24) at 04:10 ET** (5-min bar high tagged $3.85), currently ~$3.29–3.37. **PM made NEW HIGHS above the AH peak.**
- Hypothetical P&L (AH detection entry ~$2.08 at 23:00 CET → PM peak $3.58): **+72%**; (AH spike entry ~$1.73 at 16:25 ET → $3.58): **+107%**
- Float: **1.0M** | Market Cap: $3.4M

**Secondary AH→PM mover: EDHL** — Everbright Digital Holding (Advertising/Marketing, Chinese micro-cap)
- Jun 11 regular close $5.98 (Day +70.9%); AH **late surge** to **$11.39 peak (19:15 ET)**; PM peak only $9.81 (04:00 ET), fading to ~$8.82. **AH was the better exit (PM < AH).** Breached the +150% extension ceiling all night → correctly skipped.

**Scanner Diagnostic:**
- **Detectable at screening time? YES.** BYAH was on the board across **all four entry-window evening scans**: 23:00 CET (+98.1% AH, $2.08), 23:30 (+101%), 00:00 (+130.4%), 00:30 (+140.9%, $2.53). It was explicitly logged each scan as **"the night's best BUILD shape"** and **"a clean test of whether the dead-cat filter costs winners."**
- **Why we didn't act:** disqualified by the **Day% ≤ −15% dead-cat-bounce filter** (Day −15.3%, sitting *exactly* on the threshold). The rule treats a stock recovering from a regular-session sell-off as a dead-cat bounce and blocks entry. We instead traded RKDA (Day +18.4%, no dead-cat flag), which faded to a loss.
- **Scanner gap:** the dead-cat filter just cost us the single best AH→PM trade of the night. BYAH's AH BUILD (+67% → +141%) reclaimed *far* above the prior close, which negates the "still falling" thesis the filter is meant to catch. **Proposed fix: override the Day% ≤ −15% disqualifier when the AH BUILD reclaims above the regular close AND shows a multi-scan BUILD (AH% rising across ≥2 scans).** An AH move that takes the stock to +100% above its regular close is not a dead-cat bounce — it is a fresh momentum event the filter is blind to.

### Baseline Tracking

- Days tracked: **30** (was 29 + 1)
- Winners detected by scanner: **26/30 (86.7%)** — HIT, SUNE, DRMA, UGRO, NXTT, POLA, BCG, PFSA, MASK, EZGO, AIIO, HTCO, WOK, LNKS, AMST, PHGE (May 20), PHGE (May 26), SNGX, ATPC, PRFX, DXST, TWAV, CHAI, MSW, TMDE, **BYAH**
- Winner selected for paper trade: **18/30 (60.0%)** — NOT incremented (we traded RKDA, not the AH→PM winner BYAH; BYAH was blocked by the dead-cat filter)
- Target: >80% detection
- Status: **BASELINE MET** (86.7% detection)
- *Note:* detection stays strong, but **selection** keeps slipping (60%). For the 2nd time in a row the scanner *saw* the winner and a filter/position rule blocked the trade (Jun 11: TMDE late-surge + one-position rule; Jun 12: BYAH dead-cat filter). The bottleneck has shifted from detection to entry rules.

### Retrospective Scan Results

Live premarket scan (04:20 ET, `scan.py --session premarket`): 8 hits — **BYAH +170.5%** (1.0M float), **EDHL +62.4%**, VSME +50.9%, RKTO +20.3%, HKIT +17.4%, RUBI +14.5%, OTLK +13.6%, RITR +7.9%.

AH reconstruction (`check-prices.py --ah-history`):
- **BYAH** — AH BUILD $1.05 → **$2.75 peak (+121.8%, 18:40 ET)**, held +85–94% to 20:00. PM continued to **$3.58 (04:10 ET)**, new high. ← **AH→PM winner.**
- **EDHL** — AH already +116% at open, late surge to **$11.39 (19:15 ET)**; PM peak $9.81 (04:00) < AH. AH was the better exit. Ceiling-breach all night.
- **VSME** — AH chop $1.11–2.17 (Day −45.9% dead-cat); PM +50.9%. Disqualified.

### Paper Trade P&L

| Ticker | Entry | Entry Total% | Catalyst | Entry Time | PM Peak | Peak Time | Exit | P&L | P&L % | Status |
|--------|-------|--------------|----------|------------|---------|-----------|------|-----|-------|--------|
| RKDA | $1.26 | +35% | None — low-float speculative pump | 23:00 CET (17:00 ET) | $1.07 | 04:00 ET | (open) | −€17.38 | −17.5% | 🔴 Open |

RKDA round-tripped its AH base: entered $1.26 at the +50% AH-peak hold ($1.35, 16:15 ET), chopped its base overnight, now PM ~$1.04–1.07 (−17.5% vs entry). PM high only $1.07. The no-catalyst low-float pump faded as the prior data warned. **Exit decision handled by position-evaluation.md (10:30 / 14:30 CET) — not this prompt.**

**Total Paper P&L (open): −€17.38**

### Scanner Effectiveness

- Evening scans ran: 7 times (21:30 – 00:30 CET)
- Candidates found: ~25 unique tickers
- Retrospective matches: BYAH caught (detected every entry-window scan, blocked by dead-cat filter). EDHL caught (ceiling-breach skip). RKDA traded → faded to a loss.

### Missed Opportunities

| Ticker | AH Change | Why Missed | Would Be Profitable? |
|--------|-----------|------------|---------------------|
| BYAH | +140.9% (AH peak +121.8%, 18:40 ET) | Detected all 4 entry scans but **disqualified by Day% −15.3% dead-cat filter** | Yes — AH entry ~$2.08 → PM peak $3.58 = **+72%** (the night's best trade) |
| EDHL | +178.6% peak (16:30 ET), late surge $11.39 (19:15) | Detected but **breached +150% extension ceiling** all night | AH→AH only (+225% from $3.50); faded PM < AH — ceiling skip was correct |

### AH Mover Follow-Through

How last night's top AH movers (2+ evening scans, AH >10%) performed into premarket. (PM prints sparse at 04:20 ET; "Current PM" uses latest available.)

| Ticker | AH Peak | Peak Time | AH Trajectory | Current PM | From Peak | From Close | Verdict |
|--------|---------|-----------|---------------|------------|-----------|------------|---------|
| BYAH | $2.75 | 18:40 ET | **BUILD** (+67% → +141% across scans) | $3.58 (PM peak) | **+30%** | +188.7% | **WINNER — PM exceeded AH**; new highs in premarket |
| EDHL | $11.39 | 19:15 ET | Late surge (BUILD on top of +116% open) | $9.81 → $8.82 | −14% → −23% | +63% (PM) | Peaked in AH; PM faded — AH was better exit |
| RKDA | $1.35 | 16:15 ET | Spike→base-hold | $1.07 | −21% | +18% (PM) | Round-tripped; our entry $1.26 now −17.5% |
| RITR | $0.98 | 16:20 ET | Spike→fade | $0.57 | −42% | −24% | Faded hard below close; REIT, 17.3M float |
| RKTO | $1.96 | 00:30 scan | Modest build | $1.33 | −32% | −10% | Pharma, 21.7M float; faded |
| CCHH | $0.62 | 17:05 ET | Spike→fade | $0.35 | −44% | −33% | Restaurants; collapsed below close |
| RUBI | $0.79 | 17:45 ET | Late build | $0.47 | −41% | −24% | Marine shipping beta; faded |
| MTEN | $2.59 | 00:30 scan | Modest build | $1.71 | −34% | −25% | 843K float, dilution (Grade D); faded |
| SDEV | $1.31 | 17:25 ET | Clean build | $1.07 | −18% | −2% | Held best of the faders; 27.1M float |

**AH-peak-vs-PM-peak check:** **BYAH broke the recent streak** — its PM peak ($3.58) *exceeded* its AH peak ($2.75), the first AH→PM continuation since GLXG (and GLXG was PM-only). BYAH's AH peak was +121.8% (a *moderate* runner, well below the +250% "extreme" threshold), consistent with the hypothesis that moderate AH builds can continue into PM while extreme runners fade. **EDHL is the opposite data point**: a near-extreme late surge ($11.39, +90% from close / +225% from $3.50) that peaked in AH and faded into PM. Running tally — "AH was the better exit": MSW (Jun 9), TMDE (Jun 10), full Jun 10 board, now **EDHL (Jun 11)**. "PM exceeded AH": **BYAH (Jun 11)** — the one we were blocked from trading.

### Price Charts

```
BYAH — 2-Day Timeline (5-min)  [AH→PM WINNER, no catalyst, 1.0M float, Day −15.3% dead-cat]
Prev Close $1.24 | Jun 11 reg close $1.05 | Current ~$3.29–3.37 (+165–172%)
AH path:  −15% (16:00) → +39.5% (16:25) → +108.9% (17:30) → +121.8% peak ($2.75, 18:40) → held +85–94% to 20:00
PM path:  $2.84 (04:00, +129%) → $2.90 → $3.58 peak (04:10, +188.7%; bar high $3.85) → $3.29–3.37 (04:20)
Verdict:  Strongest BUILD of the night; PM made NEW HIGHS above AH. Blocked only by the Day% −15.3% dead-cat filter.

EDHL — 2-Day Timeline (5-min)  [secondary, ceiling-breach skip, Chinese micro-cap]
Prev Close $3.50 | Jun 11 reg close $5.98 | PM ~$8.82 (+152% from $3.50)
AH path:  +116% (16:00) → +178.6% peak (16:30) → faded to +107% (19:00) → late surge $11.39 (+225%, 19:15)
PM path:  $9.81 peak (04:00) → $8.74–8.82 (04:15)
Verdict:  Near-extreme runner; peaked in AH, faded into PM. +150% ceiling correctly skipped it.
```

### Notes
- **The dead-cat filter cost us the winner — highest-value finding of the night.** BYAH was tracked across every entry scan, flagged each time as the best BUILD shape and an explicit "test of whether the dead-cat filter costs winners." The test resolved: **YES.** A stock that sells off −15% intraday and then BUILDS +140% in AH (reclaiming to +100% above its regular close) is not a dead-cat bounce. Recommend a **conditional override**: allow Day% ≤ −15% names if AH reclaims above the regular close AND AH% rises across ≥2 scans (a genuine BUILD). This is the second consecutive morning where detection worked but an entry rule blocked the winner.
- **Selection rate is now the bottleneck, not detection.** Detection holds at 86.7% (target met); selection sits at 60%. Two nights running the scanner saw the winner and a rule (one-position Jun 11, dead-cat Jun 12) blocked the trade. With multi-position trading now allowed (W24 change), the one-position block is gone — the dead-cat filter is the remaining blocker to fix.
- **Ceiling continues to be vindicated by faders.** EDHL breached the +150% ceiling, ran to a near-extreme $11.39 AH, then faded into PM (PM < AH). No CEILING-OVERRIDE WATCH was flagged last night (EDHL failed override criteria: VRatio <5x, early peak). Nothing to tally for the override-watch dataset, but EDHL adds support FOR keeping the ceiling on extreme late surges.
- **RKDA (held) confirms the no-catalyst low-float pump risk** again: clean HOLD pattern, ideal float (2.1M), but zero catalyst → round-tripped to −17.5%. Pattern quality alone (float + BUILD) did not save it. Exit handled by position-evaluation.md.
</content>
</invoke>
