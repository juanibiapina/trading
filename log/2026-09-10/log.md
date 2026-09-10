## Morning Evaluation — 10:20 CET

### Today's Winner

**No real winner today.** Nothing cleared the >100% winner bar. The biggest genuine AH→PM mover was **TNON**, but it topped at **+72.9%** on a dead-cat bounce — below the bar and off a dilution dump.

**TNON** (Tenon Medical) — Medical/Nursing Services
- Catalyst: Early repayment of $5.16M convertible notes (Sep 9, ~20h ago) ahead of the Sep 11 maturity — but funded by a dilutive $4.2M public offering that dumped the stock −27% in the Sep 9 regular session. The AH/PM move is a **dead-cat bounce** off that dilution dump. **Grade C** (balance-sheet de-risking mixed with dilution).
- Previous Close (last regular session, Sep 9): $2.44 (Yahoo prevClose $3.36 is the stale Sep 8 close — ANCHOR WARNING; TNON dumped −27% intraday Sep 9)
- AH last night: reclaimed from $2.28 to $3.40 (+39% vs the $2.44 close) at 18:40 ET; the decisive surge $2.70→$3.40 fired at 18:30 ET, then faded to $3.00 by 19:55 ET
- Premarket now (SIP): $4.22 high at the 04:00 ET open bar, on **1.18M sh / 13,095 trades** (real, liquid); currently ~$3.66-3.80 (Yahoo under-reports the peak at $3.66 vs SIP $4.22)
- Hypothetical P&L (AH reclaim ~$2.65 → PM SIP peak $4.22): **+59%** — but a sub-threshold dead-cat, never actionable under current gates
- SIP peak vs winner bar: $4.22 = **+72.9%** from close = below +100%
- Float: 551K | Market Cap: $2.5M

**Scanner Diagnostic:**
- Detectable at screening time? **YES — detected, correctly skipped.**
- TNON appeared in the 23:00 and 23:30 CET scans as `Day −27.4%, AH +6.6%/+5.3%, VRatio 0.1x` and was **DROPPED as a dead-cat** (AH bounce below the 10% threshold, Day ≤ −15%). The scanner saw it and correctly rejected it.
- The decisive reclaim-and-run ($2.70→$3.40, reclaiming the $2.44 close) fired at **18:30 ET — the last-scan boundary (00:30 CET)** — and continued into PM to $4.22. During the scanned window it was a sub-10% dead-cat bounce off a dilution dump.
- Scanner gap: none actionable. This is a dilution dead-cat that bounced +73% — below the winner bar, blocked by both the dead-cat filter and the 10% AH threshold. No gate change warranted (learning-phase dead-cat filter working as designed). Logged as a dead-cat-bounce follow-through data point (dilution dumps can bounce hard in PM, but sub-threshold at scan time).

### Baseline Tracking

- Days tracked: **80** (was 79 + 1)
- Winners detected by scanner: **66/75 (88.0%)** — +TNON (biggest genuine mover, detected in 2 scans, correctly skipped as a dead-cat)
- Winner selected for paper trade: **35/73 (47.9%)** — no >100% winner existed to capture; TNON was a sub-threshold dilution dead-cat
- Target: >80% detection
- Status: **BASELINE MET** (88.0%)

### Retrospective Scan Results

- Live PM scan (`scan.py --all --session premarket`, 04:21 ET): 3 hits — TNON +53.3% ($3.74), UFG +5.6% ($0.76), BNC +8.0% ($4.79). TNON the clear biggest.
- Forced AH scan (secondary diagnostic): 0 hits (TradingView postmarket fields empty overnight, as expected).
- AH reconstruction (`check-prices.py --ah-history`) + SIP bars confirm TNON's real 04:00 ET PM peak $4.22 (1.18M sh/13,095 tr) vs Yahoo's under-reported $3.66.
- No stock cleared >100%. Thin morning.

### Open Position P&L (Alpaca)

Three positions carried from last night's Sep 9 fills. **Quote-freshness guard applied:** Alpaca `current_price` for all three is stale (quotes timestamped 16:00 ET Sep 9). P&L below is reported against **live PM SIP** prices. Exits handled by `position-evaluation.md` (10:30 / 14:30 CET) — not managed here.

| Ticker | Entry | Entry Total% | Catalyst | Entry Time | PM Peak (SIP) | Peak Time | Live PM | P&L % (live) | Status |
|--------|-------|--------------|----------|------------|---------------|-----------|---------|--------------|--------|
| CULP | $4.10 | +17.5% | B — Q1 FY27 earnings beat (loss→$6M profit) | 23:00 CET | $4.25 | 04:00 ET | ~$4.07 | −0.7% | Open |
| HCAI | $4.80 | +14.3% | C — Beyinda framework cooperation (China) | 23:00 CET | $5.32 | 04:00 ET | ~$4.73 | −1.5% | Open |
| UFG  | $0.81 | +12.5% | B — H1 record results (rev +72%, guidance raised) | 23:30 CET | $0.83 | 04:00 ET | ~$0.77 | −4.9% | Open |

- CULP: PM peak $4.25 slightly above AH peak $4.18 = mild continuation; roughly flat at entry.
- HCAI: FIRST-BAR-SPIKE entry. PM peak $5.32 (+10.8% over entry) was a **single 04:00-bar pop** (vwap $4.89), round-tripped to $4.73. AH peak $5.55 > PM peak $5.32 = faded.
- UFG: AH peak $0.92 > PM peak $0.83 = faded; below entry.

Alpaca `current_price` shown by `positions` (CULP $4.10, HCAI $4.83, UFG $0.76) is stale/near-close and not tradeable — do not read as real P&L.

**Total Realized P&L (Alpaca fills only): none this pulse** (positions open, exits at position-eval).

### Scanner Effectiveness

- Evening scans ran: **7 of 7** scheduled (21:30, 22:00, 22:30, 23:00, 23:30, 00:00, 00:30 CET) + 2 extra (22:15, 22:45) = 9 total. **Full coverage, entry window captured.**
- Candidates found: ~10 unique tickers (HCAI, CULP, UFG, FTFT, PHGE, YMAT, DPU, FRTT, SUNE, TNON, others).
- Entered: CULP (Grade B), HCAI (Grade C), UFG (Grade B). Skipped: FTFT (faded intraday spike + dilution).
- Retrospective match: TNON (biggest PM mover) detected in-window.

### Missed Opportunities

| Ticker | AH Change | Why Missed | Would Be Profitable? |
|--------|-----------|------------|---------------------|

No significant missed opportunities. TNON detected + correctly skipped; no >100% winner existed.

### AH Mover Follow-Through

| Ticker | AH Peak | Peak Time | AH Trajectory | Current PM | From Peak | From Close | Verdict |
|--------|---------|-----------|---------------|------------|-----------|------------|---------|
| CULP | $4.18 | 16:15 ET | Build/hold | ~$4.07 | −4% | +16.6% | Mild continue (PM $4.25 > AH peak) |
| HCAI | $5.55 | 16:10 ET | Spike→fade (first-bar) | ~$4.73 | −15% | +12.6% | Faded (AH peak was the exit) |
| UFG | $0.92 | 16:45 ET | Spike→fade | ~$0.77 | −16% | +6.9% | Faded (AH peak was the exit) |
| FTFT | $2.54 | AH | Spike→fade (lower high vs $3.55 intraday) | ~$2.00 | −21% | −4% | Faded further (skip validated) |
| TNON | $3.40 | 18:40 ET | Late reclaim (dead-cat) | ~$3.66-4.22 | +24% (SIP) | +72.9% (SIP) | PM exceeded AH (dead-cat bounce continued) |

**AH-peak-vs-PM-peak check:** No entered name reached the >~+130% extreme-runner zone, so no additions to the extreme-zone fade tally (standing 8 fade / 1 continue, unchanged). HCAI, UFG, FTFT all had AH peaks above their PM peaks (AH was the better exit) — the ordinary AH-top pattern, not the extreme-zone case.

### Price Charts

```
TNON  prev close (Sep 9) $2.44 | 2-day range $2.22-$4.57 | SIP PM peak $4.22 (+72.9%) 04:00 ET
      (Yahoo anchors to stale $3.36; intraday $4.57 was pre-dump Sep 9 12:40 ET)
CULP  prev close $3.42 | range $3.42-$4.24 | PM peak $4.24 (+24.0%) 09-10 08:00 ET | entry $4.10
HCAI  prev close $4.22 | range $4.01-$5.59 | AH peak $5.59 (+32.5%) 09-09 20:10 ET | PM peak $5.32 | entry $4.80
UFG   prev close $0.72 | AH peak $0.92 | PM peak $0.83 | entry $0.81
```

### Notes

- **No real winner today** — nothing cleared >100%. Biggest genuine mover TNON +72.9% was a dilution dead-cat (funded offering + note repayment), detected and correctly skipped. Thin morning (3 PM scan hits).
- **Baseline chain intact:** latest baseline (Days tracked 79) evaluated Sep 8 night (winner SUNE), logged in the Sep 8 file. Sep 9 night is the immediately-preceding session, evaluated here → 80. No baseline gap.
- **Full scan coverage:** 7 of 7 scheduled scans ran (+2 extra). No coverage failure.
- **First-bar-spike entry outcome tracking:** +HCAI (Aug→Sep pattern: AH high $5.55 @16:10 ET first bar, CONFIRM-3 NO, entered $4.80 → PM peak $5.32 one-bar pop then round-tripped to $4.73 = **flat/faded**). **Standing: 3 first-bar-spike entries, 0 ran sustained** (LABT faded, SUNE flat/round-trip, HCAI flat/faded). Trending toward the ≥4/5 fade-or-flat threshold that would route a hold-test refinement to Juan's daily email — one more fade-or-flat reaches it. Data collection only.
- **Multi-session-runner outcome tracking:** +CULP (day-1 fresh igniter, Day +2.0%, Grade B, entered $4.10 → PM peak $4.25 = **+3.7%, flat/marginal**), +HCAI (day-1 fresh igniter, Day −0.5%, Grade C, entered $4.80 → PM peak $5.32 then faded = **flat/faded**), +UFG (day-1 fresh igniter, Day +25.0% same-day earnings, Grade B, entered $0.81 → PM peak $0.83 then $0.77 = **faded**). **Standing: 1 multi-session runner (1 faded) / 19 first-day igniters (6 ran, 6 flat, 7 faded).** First-day run rate 6/19 (31.6%) — the "fresh igniters follow through" hypothesis stays weak. (Early-PM reads at 04:20 ET; may firm at position-eval pulses.)
- **Fade-rule false-negative tracking:** FTFT skipped on the faded-intraday-spike/extended rule (ran $3.55 intraday → faded to $2.09 close → AH bounce $2.54 = lower high). PM peak $2.14 < AH peak $2.54 = **faded further, skip correct, no re-explosion, no cost.** Not a sub-3M-float name; does not count toward the ≥4/5 sub-3M trigger. Standing sub-3M count unchanged at 4 of 14.
- **Reverse-split-squeeze fade tracking:** FTFT (1-for-4, Aug 26 = ~2 weeks old / weeks-old bucket, Grade C framework agreements, **skipped not entered**) faded (AH $2.54 → PM $2.14). Adds to weeks/months-old bucket as a fade (skip-validation, no entry P&L). Weeks/months-old bucket now 3 continue / 3 fade. This-week bucket unchanged at 4/4 fade (recency signal RESOLVED — recommendation already routed to Juan's daily email).
- **Chase-cap / entry-extension:** CULP fill $4.10 (below qualifying $4.07/+19%, no chase), HCAI fill $4.80 (~qualifying, no chase), UFG fill $0.81 (no chase). No chased-into-fade-zone fills. Standing count 1 (XOS), unchanged.
- **PM-only gapper tracking:** Today's biggest raw PM mover (TNON) is an **AH→PM continuation** (real AH footprint, reclaimed to $3.40 in AH), not a PM-only gapper — detectable, no blind spot this morning. Standing holdable PM-only-gapper count in `log/pm-open-scan.csv`: **48** (well above the ≥3-4 cluster threshold). Holdable-cluster action already standing: route the Initiative-6 early-PM hypothetical-entry pilot to Juan's daily email.
- **In-window feed-lag miss:** none this session. Standing count 4 (escalation trigger REACHED — AH-data-source cross-check recommendation already routed to daily email).
- **Broker-block / stale-book / no-fillable-book / float-gate / final-scan gate-block:** no new cases this session. Standing counts unchanged (broker-block 2; stale-book 3; no-fillable-book 2; float-gate 1; final-scan gate-block 2).
- **Open positions carried:** CULP, HCAI, UFG — all flat-to-down in early PM, none reclaimed their AH peak (CULP mild continue). Position management (hold/sell) at the 10:30 / 14:30 CET position-eval pulses, not here.

## Position Evaluation — 10:30 CET

Source of truth: Alpaca `broker.js positions`. Quote feed frozen at 20:00Z prior close for all three names; priced off SIP 5Min PM bars (PM open 08:00Z EDT).

| Ticker | Entry | Current | P&L % | Peak (SIP) | Peak P&L | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|------|-------|----------|--------|
| CULP | $4.10 | $4.10 | ~0% | $4.25 | +3.7% | 1 | B | HOLD | Day 1 of 2, flat, stop $3.49 not hit, earnings-beat catalyst intact |
| UFG | $0.81 | $0.77 | -4.9% | $0.83 (AH $0.92 +13.6%) | +2.5% today | 1 | B | HOLD | Day 1 of 2, above -15% stop ($0.69), record-results catalyst intact |
| HCAI | $4.80 | $4.75 | -1.0% | $5.32 (first-bar spike) | +10.8% | 1 | C | SELL | Grade C = exit first PM pulse; above -10% stop ($4.32) |

**SIP PM bars (08:00-08:15Z):**
- CULP: O$4.15 H$4.25 →holding $4.07-4.16, vwap $4.11, liquid (1542→39 trades/bar)
- UFG: O$0.82 dip$0.75 →holding $0.76-0.78, vwap $0.77, liquid (3410→187 trades/bar)
- HCAI: O$4.60 spike$5.32 →holding $4.75-4.90, vwap $4.78 (2576→210 trades/bar); book went dead after 08:15Z

**Actions taken:**
- SELL 20 HCAI @ limit $4.68 ext (id 56b71006) — submitted, resting in dead PM book (no trades since 08:15Z, last traded $4.73-4.75). Awaiting fill; confirm at 14:30 pulse.
- CULP, UFG: no action (HOLD, both Grade B day 1 within params).

## Position Evaluation — 14:30 CET

Source of truth: Alpaca `broker.js positions`. Quote feed still frozen at 20:00Z prior close for all three names (CULP ask $4.11, HCAI bid $3.59/ask $0.00 x0, UFG ask $0.83); priced off SIP 5Min PM bars (latest ~12:15Z, ~15 min old).

| Ticker | Entry | Current (SIP) | P&L % | Peak (SIP) | Peak P&L | Days | Grade | Decision | Reason |
|--------|-------|---------------|-------|------------|----------|------|-------|----------|--------|
| CULP | $4.10 | $4.10 | ~0% | $4.25 | +3.7% | 1 | B | HOLD | Day 1 of 2, flat, stop $3.49 not hit, earnings-beat catalyst intact |
| UFG | $0.81 | $0.71 | -12.3% | $0.83 | +2.5% | 1 | B | HOLD | Day 1 of 2, above -15% stop ($0.69), record-results catalyst intact; near stop |
| HCAI | $4.80 | $4.18 | -12.9% | $5.32 (first-bar) | +10.8% | 1 | C | SELL | Grade C first-PM-pulse + below -10% hard stop ($4.32) |

**SIP PM levels (near 14:30 CET / 12:15Z):**
- CULP: holding $4.08-4.15, vwap ~$4.10, liquid (17-51 trades/bar). ~flat vs entry.
- UFG: bled from $0.77 open to $0.68-0.72, holding ~$0.71, vwap $0.71. -12.3%, above $0.69 stop.
- HCAI: first-bar $5.32 pop (vwap $4.89) round-tripped; bled to $4.15-4.24 midday (vwap $4.16-4.22), below -10% hard stop.

**Actions taken:**
- SELL HCAI: canceled stale 10:30 order (id 56b71006, limit $4.68, unfilled in dead book). Repriced SELL 20 @ limit $4.10 ext (id b4efbafd) → filled @ $4.13 (price improvement). Real fill $4.13. P&L -$13.40 (-14.0%). Moved to Closed Positions.
- CULP: HOLD, no action (Grade B day 1, ~flat, within params).
- UFG: HOLD, no action (Grade B day 1, -12.3%, above -15% stop). Near stop — sell next pulse if it breaks $0.69.

## Scan 21:30 CET (3:30 PM ET)

**REGULAR session — AH not open yet (opens 16:00 ET / 22:00 CET).** Watch-only pulse per regular-session caution rule. No paper entries. Candidates flagged pending AH confirmation; only enter if they reappear in a 22:00+ CET AH scan with sustained momentum.

Regular-session movers >10% (watch list):

| Ticker | Chg% | Price | Float | MCap | VChg% | Industry | Note |
|--------|------|-------|-------|------|-------|----------|------|
| TNON | +119.3 | $5.35 | 899K | $2.5M | -100.0 | Medical/Nursing Services | Yesterday's dilution dead-cat (+72.9% PM); volume dead — watch AH |
| DBGI | +83.2 | $6.87 | 906K | $6.4M | -99.9 | Apparel/Footwear | Tiny float; volume dead — watch AH |
| AHMA | +36.3 | $1.75 | 2.1M | $51.9M | -82.5 | Misc Commercial Services | Low float; intraday pop faded — watch AH |
| VANAF | +29.3 | $0.75 | 5.6M | $12.6M | -67.7 | Financial Conglomerates | Volume faded — watch AH |
| PSIG | +28.4 | $2.29 | 8.6M | $35.3M | +22.0 | Air Freight/Couriers | Volume still positive — watch AH |
| PHGE | +24.1 | $2.01 | n/a | $5.5M | -99.9 | Biotechnology | Prior winner name; volume dead — watch AH |
| BYSI | +21.8 | $0.77 | 31.9M | $31.5M | -45.1 | Pharmaceuticals: Major | High float — watch AH |
| SKYQ | +20.4 | $3.21 | 7.3M | $28.4M | -81.4 | Integrated Oil | Volume faded — watch AH |
| ATER | +20.3 | $0.85 | 13.7M | $15.3M | +572.0 | Internet Retail | Volume building into close — watch AH |
| CMRC | +18.3 | $3.08 | 73.4M | $254.8M | -27.9 | Packaged Software | High float — watch AH |
| TPET | +11.1 | $2.01 | 4.8M | $9.9M | +77.1 | Integrated Oil | Volume still positive — watch AH |

Notes:
- Most movers show collapsed intraday volume (VChg -80%+), meaning the regular-session pop already faded. ATER (VChg +572), TPET (+77), PSIG (+22) are the exceptions with volume still building/positive into the close.
- TNON is yesterday's dilution dead-cat that bounced +72.9% in PM — already traded through; watch only, no re-entry thesis unless a fresh AH catalyst appears.
- No spike-bar / CONFIRM-3 instrumentation this pulse — AH bars do not exist yet (AH opens 16:00 ET).
- **Action:** none. Re-scan at 22:00+ CET to see which names carry real AH liquidity.

## Scan 22:00 CET (4:00 PM ET)

**AH just opened (16:00 ET).** Scanner ran at 16:00:28 ET — 28 seconds into after-hours, before any postmarket volume accumulates. TradingView postmarket fields empty this early.

**No candidates found.**

- `scan.py --all` (AFTERHOURS session): 0 hits.
- Observation-only pulse (before 23:00 CET) — no entries regardless.
- 21:30 regular-session watch names (TNON, DBGI, AHMA, VANAF, PSIG, PHGE, BYSI, SKYQ, ATER, CMRC, TPET) carry forward; re-check for real AH liquidity at 22:30. Most showed collapsed intraday volume (VChg −80%+) at 21:30, so few are expected to carry into AH.
- **Action:** none. Re-scan at 22:30 CET once AH volume accumulates.

## Scan 22:15 CET (4:15 PM ET)

**AH open 15 min (16:15 ET).** Scanner ran at 16:15:24 ET.

**No candidates found.**

- `scan.py --all` (AFTERHOURS session): 0 hits. TradingView postmarket volume still not accumulating enough to clear thresholds this early.
- Observation-only pulse (before 23:00 CET) — no entries regardless.
- 21:30 regular-session watch names (TNON, DBGI, AHMA, VANAF, PSIG, PHGE, BYSI, SKYQ, ATER, CMRC, TPET) still not carrying into AH on the scan — consistent with their collapsed intraday volume (VChg −80%+). ATER/TPET/PSIG (the volume-still-positive exceptions at 21:30) also absent so far.
- No spike-bar / CONFIRM-3 instrumentation this pulse — no AH candidates above the 10% threshold to instrument.
- **Action:** none. Re-scan at 22:30 CET once AH volume accumulates.

## Scan 22:30 CET (4:30 PM ET)

**AH open 30 min (16:30 ET).** Scanner ran at 16:30:11 ET — 1 hit.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| XRTX | [TV](https://www.tradingview.com/chart/?symbol=XRTX) | $2.11 | −2.2% | +16.6% | $2.46 | +14.0% | 470K | 76K | 6.2x | 1.7M | Pharmaceuticals: Major |

**Observation-only pulse (before 23:00 CET) — no entries regardless.**

**XRTX instrumentation:**
- `SPIKE 16:05ET +28% $2.70 390 trades / 38k sh (first co-spike bar)` — ignition fired in the **first AH bar**.
- `CONFIRM-3 NO ignition 16:05ET failed third-bar hold/volume` — no local-volume new-high build after the open pop.
- SIP bars: real volume but **fading across bars** — 16:05 bar 344,820 sh / 3,509 trades (H $2.74, the AH peak), 16:10 bar 235,333 sh / 2,264 trades (H $2.58), 16:15 bar 160,156 sh / 1,752 trades (H $2.54, close $2.28). Price and per-bar volume both declining off the 16:05 peak.
- Quote: `bid $1.85 x100 ask $0.00 x0` (timestamped 20:00:02Z = stale/near-close; no live fillable ask reading yet).
- **Pattern: first-bar spike → fade.** Float 1.7M (<3M), VRatio 6.2x, but AH high ($2.74) printed in the first bar and volume is fading — this is the FIRST-BAR-SPIKE / SPIKE→FADE profile, not a build. Watch at 23:00: needs a volume-backed new AH high (CONFIRM-3 flip) to become entry-worthy; on current trajectory it is a skip candidate under the first-bar-spike rule.

**Catalyst:** not searched this pulse (observation-only; no entry). Structured catalyst search deferred to the 23:00 entry scan if XRTX still clears the AH threshold.

- 21:30 regular-session watch names (TNON, DBGI, AHMA, VANAF, PSIG, PHGE, BYSI, SKYQ, ATER, CMRC, TPET) still absent from the AH scan — consistent with their collapsed intraday volume. None carried real AH liquidity.
- **Action:** none (observation-only). Re-scan at 23:00 CET; XRTX is the only live AH candidate so far — evaluate for entry then if it holds the threshold and flips to a build.

## Scan 22:45 CET (4:45 PM ET)

**AH open 45 min (16:45 ET).** Scanner ran at 16:45:13 ET — 2 hits.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| TNON | [TV](https://www.tradingview.com/chart/?symbol=TNON) | $5.30 | +117.2% | +8.5% | $5.75 | +135.7% | 2.9M | 14.3M | 0.2x | 899K | Medical/Nursing Services |
| XRTX | [TV](https://www.tradingview.com/chart/?symbol=XRTX) | $2.11 | −2.2% | +15.2% | $2.43 | +12.6% | 718K | 106K | 6.8x | 1.7M | Pharmaceuticals: Major |

**Observation-only pulse (before 23:00 CET) — no entries regardless.**

**XRTX instrumentation (AH >10%):**
- `SPIKE 16:05ET +28% $2.70 390 trades / 38k sh (first co-spike bar)` — ignition still the first AH bar.
- `CONFIRM-3 NO ignition 16:05ET failed third-bar hold/volume as-of 16:45ET` — still no volume-backed new AH high.
- SIP bars confirm **first-bar spike → fade**: 16:05 peak $2.74 (344,820 sh / 3,509 trades), then 235K → 160K → 59K → 78K → 40K sh per bar; price bled to ~$2.40. VWAP $2.40 last bar.
- Quote `bid $1.85 x100 ask $0.00 x0` (timestamped 20:00:02Z = stale/near-close; no live fillable ask).
- **Pattern unchanged: FIRST-BAR-SPIKE / SPIKE→FADE.** Float 1.7M, VRatio 6.8x, but AH high printed first bar, CONFIRM-3 NO, volume fading. On current trajectory this is a **skip under the first-bar-spike rule** unless it flips CONFIRM-3 at 23:00.

**TNON (AH +8.5%, below 10% instrumentation threshold; huge Total% from Day%):**
- Yesterday's dilution dead-cat (funded $4.2M offering + note repayment) that bounced +72.9% in PM. Today it ran the **regular session +117.2%** and is up a further +8.5% in AH — this is a **MULTI-SESSION-RUNNER** (day 2+ of the move), not a fresh first-day igniter.
- VRatio 0.2x (AH vol 2.9M vs 14.3M avg) = **thin AH relative to the huge daily volume**; AH move is a small extension on top of an already-extended runner.
- Total% +135.7% (below the +150% ceiling but a late-stage runner). Quote `bid $4.47 x100 ask $0.00 x0` (stale near-close; no live fillable ask).
- Not entry-worthy: late-stage multi-session runner, thin AH VRatio, dilution-driven origin. Watch only.

- 21:30 regular-session watch names (DBGI, AHMA, VANAF, PSIG, PHGE, BYSI, SKYQ, ATER, CMRC, TPET) still absent from the AH scan.
- **Action:** none (observation-only). Re-scan at 23:00 CET. XRTX = first-bar-spike/fade skip candidate; TNON = multi-session-runner watch. No BUILD pattern present yet.

## Scan 23:00 CET (5:00 PM ET)

**AH open 60 min (17:00 ET). Entry window open (23:00+ CET).** Scanner ran at 17:00:18 ET — 4 hits.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| DBGI | [TV](https://www.tradingview.com/chart/?symbol=DBGI) | $6.79 | +81.1% | +13.1% | $7.68 | +104.8% | 1.0M | 3.1M | 0.3x | 906K | Apparel/Footwear |
| XRTX | [TV](https://www.tradingview.com/chart/?symbol=XRTX) | $2.11 | −2.2% | +13.7% | $2.40 | +11.2% | 794K | 115K | 6.9x | 1.7M | Pharmaceuticals: Major |
| OMH | [TV](https://www.tradingview.com/chart/?symbol=OMH) | $2.25 | −10.4% | +8.0% | $2.43 | −3.2% | 179K | 185K | 1.0x | n/a | Real Estate Development |
| CLIK | [TV](https://www.tradingview.com/chart/?symbol=CLIK) | $1.25 | +8.7% | +7.2% | $1.34 | +16.5% | 68K | 685K | 0.1x | 1.8M | Personnel Services |

OMH (AH +8.0%) and CLIK (AH +7.2%) are **below the 10% AH threshold** — not entry candidates, no instrumentation.

**Decision this pulse: NO live entry.** The only BUILD candidate (DBGI) is on its first AH scan >10% and fails the 2-AH-scan gate; the only 2-AH-scan-gate passer (XRTX) is a first-bar-spike skip. Wait for 23:30.

### DBGI — strong BUILD, pending 2nd-scan confirmation (NOT entered)

- **Instrumentation:** `NO-SPIKE peak +16% @16:43ET (no single bar cleared +15% co-spike)` — because the move is a *gradual volume-backed build across many bars*, not a single ignition bar. `CONFIRM-3 PENDING ignition 16:40ET` (waiting on third bar).
- **SIP bars = genuine BUILD, not a first-bar pop:** 16:00 H$7.18 (178K sh/2313 tr) → 16:20 H$7.45 (214K/2769, new high) → 16:40 **H$7.85 (371K sh/5,374 trades — biggest volume bar, new AH high)** → 16:45 C$7.60 (160K/2557). Per-bar volume rising into the new highs = real accumulation. Corroborates scanner AH $7.68; no bad print.
- **Setup:** float **906K** (tiny, ideal), fresh **day-1 igniter** (prior close $3.75, not in WINNERS_TRACKING, no multi-session run), Total% **+104.8%** (under +150% ceiling), Day% **+81.1%** (above −15%), `tradable=true`. Quote `bid $5.86 ask $7.75 x100` timestamped 20:00Z = stale near-close (no live fillable ask reading yet).
- **Catalyst (Grade B):** same-day (8h ago) announcement of a **$165M contract + go-private process review** — binding U.S. program covering 771,481 residents, $3.3M guaranteed cash flow through Dec 31 2026, 15–18% margin forecast; builds on the collegiate program + government-contract turnaround (Aug 12 positive-cash-flow PR). Transformational scale for a $6.3M-cap company. Go-private is a *review* (not a fixed-price cash deal) → still momentum-gradable, not the merger-arb exclusion.
- **Gate status:** clears **every** entry rule except the **2-AH-scan gate** — its first AH-scan appearance >10% is this 23:00 scan (it was below 10% AH / absent at 22:00–22:45; SIP shows it only cleared +10% AH once it printed $7.60+ at 16:40 ET, after the TradingView postmarket feed had lagged the earlier scans). **One AH scan >10% = cannot enter yet.**
- **Action:** carry as the **leading entry candidate**. If DBGI holds >10% AH at the 23:30 scan (2nd AH scan), enter per the gates — real accumulating volume, tiny float, Grade B catalyst, under ceiling. This is a genuine BUILD, the pattern the strategy waits for.

### XRTX — SKIP (first-bar-spike / fade), FIRST-BAR-SPIKE WATCH hypothetical recorded

- **Passes the 2-AH-scan gate** (>10% AH at 22:30 +16.6%, 22:45 +15.2%, 23:00 +13.7%) — but skipped on the first-bar-spike rule.
- **Instrumentation:** `SPIKE 16:05ET +28% $2.70 390 trades / 38k sh (first co-spike bar)` — AH high printed in the **first AH bar**. `CONFIRM-3 NO ignition 16:05ET failed third-bar hold/volume as-of 17:00ET` — every scan.
- **SIP bars = first-bar spike → fade:** 16:05 peak **$2.74 (344,820 sh / 3,509 trades)** → volume fades every bar (235K → 160K → 59K → 78K → 40K → 21K → 24K → 35K sh); price bled to ~$2.40–2.44, vwap $2.43. No volume-backed new AH high after the open bar.
- **Skip rule:** AH high in the first AH bar (16:00–16:15 ET) + CONFIRM-3 NO every scan = **single-bar pop, not a build → skip live entry** even though it sits within ~20% of that open high. Float 1.7M / VRatio 6.9x do not override.
- **FIRST-BAR-SPIKE WATCH (hypothetical):** entry $2.44 @ 23:00 CET (17:00 ET). Morning-eval tracks whether the skip was correct. (Standing first-bar-spike entries 0/3 sustained; this is a skipped-watch, not a live entry.)

### Other tracked names

- **TNON** (multi-session runner): yesterday's dilution dead-cat (+72.9% PM), ran regular session +117% today, +8.5% AH at 22:45. AH +8.0% region now, VRatio 0.2–0.3x (thin AH on 14.3M avg vol). Late-stage day-2+ runner, dilution origin — watch only, not entry-worthy.
- 21:30 regular-session watch names (AHMA, VANAF, PSIG, PHGE, BYSI, SKYQ, ATER, CMRC, TPET): still absent from the AH scan / below threshold. None carried real AH liquidity.
- **No dead-cat-override, ceiling-override, chase-cap, final-scan-gate-block, broker-block, stale-book, or no-fillable-book cases** this pulse. DBGI is a clean 2-AH-scan-gate-pending BUILD; XRTX a first-bar-spike skip.
- **Action:** none (no entry). Re-scan at 23:30 CET — primary watch is DBGI holding >10% AH to clear the 2-scan gate and become entry-worthy.

## Scan 23:30 CET (5:30 PM ET)

**AH open 90 min (17:30 ET). Entry window open (23:00+ CET).** Scanner ran at 17:30:14 ET — 6 hits.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| TNON | [TV](https://www.tradingview.com/chart/?symbol=TNON) | $5.30 | +117.2% | +7.2% | $5.68 | +132.8% | 5.1M | 14.6M | 0.3x | 899K | Medical/Nursing Services |
| DBGI | [TV](https://www.tradingview.com/chart/?symbol=DBGI) | $6.79 | +81.1% | +6.9% | $7.26 | +93.6% | 1.4M | 3.2M | 0.4x | 906K | Apparel/Footwear |
| XRTX | [TV](https://www.tradingview.com/chart/?symbol=XRTX) | $2.11 | −2.2% | +12.3% | $2.37 | +9.8% | 904K | 128K | 7.1x | 1.7M | Pharmaceuticals: Major |
| GBR | [TV](https://www.tradingview.com/chart/?symbol=GBR) | $0.84 | +11.1% | +5.5% | $0.89 | +17.2% | 511K | 83K | 6.1x | 4.7M | Real Estate Development |
| TPET | [TV](https://www.tradingview.com/chart/?symbol=TPET) | $2.02 | +11.6% | +5.9% | $2.14 | +18.1% | 277K | 2.4M | 0.1x | 4.8M | Integrated Oil |
| FTFT | [TV](https://www.tradingview.com/chart/?symbol=FTFT) | $2.05 | −1.9% | +8.3% | $2.22 | +6.2% | 227K | 11.3M | 0.0x | 5.4M | Finance/Rental/Leasing |

**Only XRTX clears the 10% AH threshold this scan.** DBGI (+6.9%), TNON (+7.2%), GBR (+5.5%), TPET (+5.9%), FTFT (+8.3%) are all below the 10% AH threshold — not entry candidates.

**Decision this pulse: NO live entry.** The only 2-AH-scan-gate passer (XRTX) is a confirmed first-bar-spike skip. The BUILD candidate (DBGI) topped and faded below the 10% AH threshold, and never got a 2nd AH scan >10% — gate not met.

### DBGI — BUILD topped and faded, 2-AH-scan gate NOT met (NOT entered)

- **Instrumentation:** `NO-SPIKE peak +16% @16:43ET` (gradual volume-backed build, no single ignition bar), `CONFIRM-3 NO ignition 16:40ET failed third-bar hold/volume as-of 17:30ET`.
- **SIP bars = build peaked at 16:40 ET, now bleeding:** ran to **H$7.85 (371K sh / 5,374 trades) at 16:40 ET** (the big-volume new-high bar), then faded every bar: $7.60 → $7.37 → $7.26 → $7.33 → $7.20 → $7.38. Current ~$7.38 (17:15 ET bar), holding within ~6% of the $7.85 peak but per-bar volume decaying (371K → 160K → 115K → 82K → 80K → 71K → 43K → 59K sh).
- **Gate status:** cleared >10% AH **only once** (23:00 scan, +13.1% / AH $7.68). At 22:30–22:45 it was below threshold/absent; at 23:30 it faded to +8.7% AH (SIP) / +6.9% (scanner). **Only 1 AH scan >10% → fails the 2-AH-scan gate.** The build peaked at 16:40 ET (+15.6% AH high) and is bleeding — the gate correctly blocks a topped-and-fading entry.
- **Setup (recorded):** float 906K (tiny), day-1 fresh igniter, Grade B ($165M contract + go-private review), Total% +93.6% (under +150% ceiling), Day% +81.1%. A clean setup that simply did not sustain 10% AH across 2 scans.
- **Action:** carry as watch. If DBGI reclaims >10% AH ($7.47+) and holds at the 00:00 scan, it earns its 2nd qualifying AH scan — re-evaluate then. On current fading trajectory it is a topped build, not an entry.

### XRTX — SKIP (first-bar-spike / fade), FIRST-BAR-SPIKE WATCH carried

- **Passes the 2-AH-scan gate** (>10% AH at 22:30 +16.6%, 22:45 +15.2%, 23:00 +13.7%, 23:30 +12.3%) — but skipped on the first-bar-spike rule.
- **Instrumentation:** `SPIKE 16:05ET +28% $2.70 390 trades / 38k sh (first co-spike bar)`, `CONFIRM-3 NO ignition 16:05ET failed third-bar hold/volume as-of 17:30ET` — every scan.
- **SIP bars = first-bar spike → fade unchanged:** peak $2.74 (344,820 sh / 3,509 trades) at 16:05 ET, then volume fades every bar to ~5–35K sh; price flat-lined ~$2.38–2.40, vwap $2.38. No volume-backed new AH high after the open bar.
- **Skip rule:** AH high in the first AH bar (16:00–16:15 ET) + CONFIRM-3 NO every scan = single-bar pop, not a build → skip live entry. Float 1.7M / VRatio 7.1x do not override.
- **FIRST-BAR-SPIKE WATCH (hypothetical):** entry $2.44 @ 23:00 CET carried; still sits ~$2.40 (within ~20% of $2.74 high). Morning-eval tracks whether the skip was correct. (Standing first-bar-spike entries 0/3 sustained.)

### Other tracked names

- **TNON** (multi-session runner): yesterday's dilution dead-cat, ran regular session +117%, now +7.2% AH (VRatio 0.3x, thin on 14.6M avg vol). Late-stage day-2+ dilution runner — watch only, not entry-worthy.
- **GBR** (NEW): Day +11.1%, AH +5.5% (below threshold), Total +17.2%, float 4.7M, VRatio 6.1x. Real Estate Development. Below the 10% AH threshold — no entry, no full workup. Watch at 00:00 if it clears 10% AH.
- **TPET** (Day +11.6%, AH +5.9%), **FTFT** (Day −1.9%, AH +8.3%): both below the 10% AH threshold; TPET VRatio 0.1x (thin AH), FTFT VRatio 0.0x (yesterday's faded reverse-split name). No entry.
- **No dead-cat-override, ceiling-override, chase-cap, final-scan-gate-block, broker-block, stale-book, or no-fillable-book cases** this pulse.
- **Action:** none (no entry). Re-scan at 00:00 CET — primary watch is DBGI reclaiming >10% AH for a 2nd qualifying scan; GBR as a secondary if it clears threshold.
