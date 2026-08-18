
# Post-Market Screening - 2026-08-18

## Scan 21:30 CET (3:30 PM ET) — regular session, watch only

Regular session (AH opens 16:00 ET / 22:00 CET). No paper trades per regular-session caution rule. Candidates flagged "Watch — pending AH confirmation"; enter only if they reappear in a 22:00+ CET AH scan with sustained momentum.

| Ticker | Price | Day% | 5mVol | AvgVol | IRVol | Float | MCap | Industry | Note |
|--------|-------|------|-------|--------|-------|-------|------|----------|------|
| XOS | $4.37 | +109.1% | 163K | 180K | 150.3 | 6.9M | 29.7M | Motor Vehicles | Watch — sold this AM at loss; USAF-contract name back running |
| CAST | $2.13 | +147.7% | 1.5M | 1.9M | 122.7 | 19.7M | 40.9M | Internet Software/Svcs | Watch — float >10M |
| CDTG | $5.36 | +91.5% | 534K | 657K | 31.1 | 3.0M | 8.5M | Industrial Machinery | Watch — low float |
| AIXC | $1.34 | +88.2% | 170K | 312K | 2263.4 | 6.8M | 27.0M | Packaged Software | Watch — huge IRVol, volume fading (VChg -62%) |
| SLE | $5.24 | +73.5% | 146K | 82K | 31.1 | 1.6M | 8.9M | Internet Software/Svcs | Watch — low float, VChg +140% |
| SXTC | $5.43 | +44.7% | 158 | 20K | 6.0 | 1.3M | 7.2M | Pharma Major | Watch — volume near-dead (VChg -99.6%) |
| EJH | $2.08 | +43.5% | 11K | 38K | 470.6 | 2.5M | 6.7M | Consumer Services | Watch — low float |

The $10 flat Financial Conglomerates (ACGC, SHOT, MUZE, VII) show extreme IRVol at ~0% change — SPAC/auction artifacts, not momentum. Skipped.

## Scan 22:00 CET (4:00 PM ET) — AH open, observation only

`scan.py --all`: **0 hits.** AH session just opened (16:00 ET exact); postmarket volume not yet accumulated. No candidates from whole-market screen.

21:30 regular-session watch names have not reappeared in an AH scan yet — none crossed into the AH screen at open. Nothing to confirm this scan. Observation-only window regardless (learning phase: no entries before 23:00 CET). Re-check watch names (XOS, CAST, CDTG, AIXC, SLE, EJH) at 22:30/23:00 for AH carry-over.

No paper trades.

## Scan 22:15 CET (4:15 PM ET) — AH open, observation only

`scan.py --all`: **0 hits.** First AH 5-min bar (16:00–16:05 ET) just closed; whole-market screen still shows no candidates above threshold.

SIP cross-check of 21:30 regular-session watch names (first AH bar):

| Ticker | Reg Close | AH C (16:05 ET) | AH move | Vol/bar | Trades | Read |
|--------|-----------|-----------------|---------|---------|--------|------|
| XOS | $4.37 | $4.30 | ~flat | 303K | 1527 | flat, no AH build |
| CAST | $2.13 | $2.15 | ~flat | 1.0M | 4437 | flat |
| CDTG | $5.36 | $3.10 | −42% | 222K | 1386 | collapsing in AH |
| SLE | $5.24 | $4.94 | −6% | 1.0M | 9245 | fading off close |

No watch name is building into AH — all flat or fading on the first bar. Nothing to confirm. Observation-only window regardless (learning phase: no entries before 23:00 CET). Re-check at 22:30/23:00 for any name that starts building.

No paper trades.

## Scan 22:30 CET (4:30 PM ET) — AH open, observation only

`scan.py --all`: **2 hits.** First AH movers to cross the whole-market screen tonight.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| TNON | [TV](https://www.tradingview.com/chart/?symbol=TNON) | $5.45 | +10.8% | +56.5% | $8.53 | +73.4% | 1.6M | 350K | 4.6x | 551K | Medical/Nursing Services |
| CNET | [TV](https://www.tradingview.com/chart/?symbol=CNET) | $1.38 | +5.3% | +16.1% | $1.60 | +22.3% | 754K | 107K | 7.1x | 3.0M | Advertising/Marketing Services |

**Instrumentation (log-only, no decision impact):**
- TNON: `SPIKE 16:01ET +28% $7.00 1787 trades / 137k sh` · `CONFIRM-3 NO no local-volume new-high ignition as-of 16:30ET`
- CNET: `NO-SPIKE peak +33% @16:09ET (no bar cleared +15% on volume co-spike)` · `CONFIRM-3 NO`

**SIP 5-min bars (real AH volume):**

| Ticker | Bar C path (16:00→16:15 ET) | Vol/bar | Trades/bar | Read |
|--------|-----------------------------|---------|------------|------|
| TNON | $7.03 → $7.60 → $8.51 → $8.58 | 595K–880K | 9.7k–15.8k | genuine BUILD, real accumulation |
| CNET | $1.67 → $1.60 → $1.38 | 526K→248K | 4.1k→1.8k | SPIKE→FADE, volume fading |

**Evaluation (observation-only, no entries before 23:00 CET):**
- **TNON** — tiny 551K float, Total% +73.4% (under +150% ceiling), SIP confirms real accumulating AH volume and a clean BUILD ($7.03→$8.58). Strong watch. But this is its **first** AH scan appearance (0 hits at 22:00/22:15) — the 2-AH-scan gate is not met. Needs to reappear >10% AH at 23:00 to qualify. No catalyst search yet (defer to 23:00 if it holds).
- **CNET** — SIP shows SPIKE→FADE (peaked $1.84 16:05 ET, now $1.38, volume halving each bar). Fails BUILD/hold. Watch only; likely skip.

No paper trades (learning-phase observation window, both fail 2-AH-scan gate).

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|

_No entries — regular-session watch scan only._

## Position Evaluation — 10:30 CET

| Ticker | Entry | Exit/Now | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|----------|-------|------|------|-------|----------|--------|
| DARE | $1.70 | $0.83 | -51.2% | $1.79 | 5 | B | SELL | Day-5 past 2-day limit + far below -15% stop; Juan flagged 08-14 |
| GRSD | $2.17 | $2.01 | -7.4% | $2.35 | 5 | B | SELL | Day-5 time limit; dead book, never re-rated |
| ONFO | $3.02 | $2.26 | -25.2% | $3.88 | 4 | B | SELL | Day-4 past limit + below -15% stop ($2.567) |
| SGLY | $7.01 | $5.35 | -23.7% | $7.25 | 0 | None | SELL | Exit first PM + below -10% stop ($6.31); dumped at open |
| XOS | $4.54 | $3.48 | -23.3% | $4.78 | 1 | B | SELL | Below -15% hard stop ($3.86); dumped at PM open |

**Actions taken:**
- Sold all 5 positions (extended-hours limit, all price-improved over limit).
- DARE 58 @ $0.83 (id 6d0996dc) — realized -$50.46
- GRSD 45 @ $2.01 (id 207f9758) — realized -$7.20
- ONFO 29 @ $2.26 (id 97313753) — realized -$22.04
- SGLY 14 @ $5.35 (id 4b1bca32) — realized -$23.24
- XOS 21 @ $3.48 (id 6e310b97) — realized -$22.26
- **Total realized: -$124.94.** Account flat, no open positions.

**Notes / for daily email:**
- Rough pulse: 5/5 losers. Two Grade B names (DARE, GRSD) were held well past the 2-day time limit — DARE bled from -7% to -51% while stalled. Time-limit exits must fire on schedule, not wait for a crash.
- XOS had a genuine catalyst (USAF contract) + real AH BUILD to +117% yet still gave zero PM follow-through and dumped at open. Reinforces: AH BUILD alone (even with catalyst) does not predict PM continuation.

## Position Evaluation — 14:30 CET

No open positions (Alpaca source of truth confirms flat). All 5 positions closed at the 10:30 CET pulse. OPEN_POSITIONS.md agrees. No action.
