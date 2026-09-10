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
