# 2026-10-14

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| AEHL | $15.40 | $23.80 | +54.5% | $25.25 (SIP; $29.76 spike print) | 1 | None | SELL | No catalyst: exit at first PM opportunity, in profit |
| AGMH | $0.66 | $0.64 | -2.5% | $0.74 (SIP PM 04:00) | 1 | C | SELL | Grade C exits in first PM pulse; PM fade from $0.74 to $0.63 |
| BKYI | $3.26 | $2.48 | -23.9% | $3.26 | 1 | B | SELL | -15% hard stop breached ($2.77); PM broke to $2.43 |

Prices: Alpaca `current_price`; peaks checked on SIP 5‑min bars from 08:00Z. Quotes were stale (last update at yesterday's 20:00Z close), so limits were set below the latest SIP 5‑min closes.

**Actions taken:**
- SELL AEHL 6 @ limit $22.90 → filled $23.78 (order 3ecd0f1b): +$50.28 (+54.4%)
- SELL AGMH 144 @ limit $0.61 → filled $0.64 (order 4c1c748e): -$2.88 (-3.0%)
- SELL BKYI 30 @ limit $2.40 → filled $2.48 (order a25240dc): -$23.40 (-23.9%)
- Net: +$24.00 on $285.24 deployed. No open positions remain.

**Notes:**
- BKYI: Grade B contract win, but the AH buy came after a +98% run and it gapped below entry at the PM open. The -15% stop could not be enforced overnight; the first chance to act was already at -24%.
- AEHL: the no-catalyst AH build ran another +55% at the PM open on heavy SIP volume (~806K sh in 20 min). The quick-exit rule captured most of it.

## Position Evaluation — 14:30 CET

No open positions (Alpaca `positions` empty; `OPEN_POSITIONS.md` matches). Equity $99,728.46, all cash.

**Actions taken:**
- None

## Scan 21:30 CET (3:30 PM ET)

Regular session (pre-AH). Observation only; no entries.

| Ticker | Chart | Price | Day% | 5mVol | Avg5m | IRVol | Float | MCap | Industry |
|--------|-------|-------|------|-------|-------|-------|-------|------|----------|
| GLND | [TV](https://www.tradingview.com/chart/?symbol=GLND) | $3.65 | +65.2% | 285K | 392K | 19.6 | 27.5M | 159.6M | Financial Conglomerates |
| NXGL | [TV](https://www.tradingview.com/chart/?symbol=NXGL) | $5.83 | +44.0% | 230K | 49K | 17.6 | n/a | 17.9M | Chemicals: Specialty |
| TDIC | [TV](https://www.tradingview.com/chart/?symbol=TDIC) | $2.19 | +34.7% | 25K | 32K | 827.1 | 2.0M | 7.7M | Miscellaneous Commercial Services |
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $1.84 | +32.3% | 12K | 56K | 1.4 | 4.4M | 14.4M | Miscellaneous Commercial Services |
| MXCT | [TV](https://www.tradingview.com/chart/?symbol=MXCT) | $1.24 | +28.6% | 6K | 45K | 51.9 | 94.8M | 128.0M | Biotechnology |
| BOXL | [TV](https://www.tradingview.com/chart/?symbol=BOXL) | $3.41 | +21.8% | 3K | 3K | 8.2 | 715K | 2.9M | Computer Peripherals |
| CCG | [TV](https://www.tradingview.com/chart/?symbol=CCG) | $5.20 | +18.5% | 603 | 556 | 0.4 | 943K | 13.0M | Packaged Software |
| MWYN | [TV](https://www.tradingview.com/chart/?symbol=MWYN) | $1.88 | +17.5% | 5K | 5K | 4.0 | 13.0M | 38.0M | Home Improvement Chains |
| GENK | [TV](https://www.tradingview.com/chart/?symbol=GENK) | $1.70 | +17.2% | 34K | 54K | 2104.9 | 6.6M | 59.3M | Restaurants |
| GRML | [TV](https://www.tradingview.com/chart/?symbol=GRML) | $6.46 | +16.6% | 38K | 37K | 4.1 | 12.1M | 86.2M | Miscellaneous Commercial Services |
| FMFC | [TV](https://www.tradingview.com/chart/?symbol=FMFC) | $5.75 | +15.9% | 700 | 580 | 7.4 | n/a | 2.8M | Consumer Sundries |
| GAUZ | [TV](https://www.tradingview.com/chart/?symbol=GAUZ) | $4.74 | +15.9% | 170 | 761 | 10.2 | 1.0M | 5.4M | Industrial Specialties |
| KMRK | [TV](https://www.tradingview.com/chart/?symbol=KMRK) | $1.53 | +15.0% | 5K | 2K | 3.2 | 4.6M | 32.3M | Miscellaneous Commercial Services |
| DFNS | [TV](https://www.tradingview.com/chart/?symbol=DFNS) | $6.46 | +12.4% | 17K | 12K | 25.0 | 2.5M | 21.0M | Advertising/Marketing Services |

Scanner returned 25 hits; the table keeps the 14 with Day% >+10%. Omitted: ~$10 Financial Conglomerates trading flat (APMC, SUMA, BWIV, KPET, ATLQ, JONE, MRCO, likely SPAC trust-value units), and EVOL, FFAI, LRAXF, KHDHF (Day% between −4% and +4%).

**Evaluation notes:**
- Watch — pending AH confirmation: GLND, NXGL, TDIC, NCPL, MXCT, BOXL, CCG, MWYN, GENK, GRML, FMFC, GAUZ, KMRK, DFNS. Intraday moves do not count; entry needs >10% AH in ≥2 AH scans from 22:00 CET, and the entry window opens at 23:00 CET.
- Still trading 5m volume near or above average: GLND (285K vs 392K), NXGL (230K vs 49K), GENK (34K vs 54K), GRML (38K vs 37K), TDIC (25K vs 32K). MXCT and NCPL volume has faded (VChg −92% and −78%).
- Prior footprint: GLND was a PM-only mover this morning ($2.21 Oct 13 close → $3.13 PM high) and is now +65% on the day, so it is day 2 of a move; check SIP daily bars for the MULTI-SESSION-RUNNER tag if it qualifies in AH. NCPL was a >10% AH name on Oct 13 (NO-SPIKE, CONFIRM-3 NO, first-bar high) and on Oct 6/7/12; today's +32% puts it at day 2+. GRML (+19.2% PM this morning) and MWYN (Oct 12–13 watch) also repeat.
- MXCT float 94.8M exceeds the 50M float condition on the entry gate.

## Scan 22:00 CET (4:00 PM ET)

No candidates found. AH-open pulse: the 16:00:09 ET snapshot has no AH prints yet.

Supplementary AH-change-only (>15%, not in volume pass): none

AH >10% at this snapshot (unrounded): none

**Evaluation notes:**
- No >10% AH candidates, so no spike-bar, CONFIRM-3, SIP volume or book checks to run. The 21:30 watch names (GLND, NXGL, TDIC, NCPL, etc.) carry to the next pulse.
- Observation window (before 23:00 CET); no entries.

## Scan 22:05 CET (4:05 PM ET)

No candidates found. AH-open pulse: the 16:05:09 ET snapshot shows 0 hits.

Supplementary AH-change-only (>15%, not in volume pass): none

AH >10% at this snapshot (unrounded): none

**Evaluation notes:**
- No >10% AH candidates, so no spike-bar, CONFIRM-3, SIP volume or book checks to run. The 21:30 watch names (GLND, NXGL, TDIC, NCPL, etc.) carry to the next pulse.
- Observation window (before 23:00 CET); no entries.

## Scan 22:10 CET (4:10 PM ET)

No candidates found. The 16:10:11 ET snapshot shows 0 hits, the third empty AH-open pulse in a row.

Supplementary AH-change-only (>15%, not in volume pass): none

AH >10% at this snapshot (unrounded): none

**Evaluation notes:**
- No >10% AH candidates, so no spike-bar, CONFIRM-3, SIP volume or book checks to run. Free-tier SIP still blocks the 16:00–16:10 ET bars, so a cross-check of the 21:30 watch names (GLND, NXGL, TDIC, NCPL, etc.) waits for a later pulse.
- Observation window (before 23:00 CET); no entries.

## Scan 22:15 CET (4:15 PM ET)

No candidates found. The 16:15:09 ET snapshot shows 0 hits, the fourth empty AH pulse in a row.

Supplementary AH-change-only (>15%, not in volume pass): none

AH >10% at this snapshot (unrounded): none

**Evaluation notes:**
- No >10% AH candidates, so no spike-bar, CONFIRM-3, SIP volume or book checks to run.
- SIP cross-check of the 21:30 watch names (16:00 ET bar now served): the empty scan agrees with SIP. GLND 16:00 bar C $3.77 (vwap $3.85, 326K sh / 1,435 trades) is below its 15:55 close of $3.90. TDIC C $2.19 is below its $2.27 close. GENK C $1.63 is below its $1.68 close. NXGL 16:00 bar H $6.34 / C $5.76 (vwap $5.79, 237K sh / 3,234 trades), with C below its $5.83 price at 15:30 ET; the high was a brief wick. No watch name holds >10% AH.
- Observation window (before 23:00 CET); no entries.

## Scan 22:20 CET (4:20 PM ET)

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $1.59 | +14.4% | +17.1% | $1.86 | +34.0% | 672K | 11.5M | 0.1x | 4.4M | Miscellaneous Commercial Services |

Supplementary AH-change-only (>15%, not in volume pass): none

AH >10% at this snapshot (unrounded): NCPL

**Evaluation notes:**
- NCPL: first AH scan above 10% (1 of 2 needed). It sold off into the close ($1.84 at 15:30 ET → $1.57 at 15:55) and reclaimed the intraday level in AH. `tradable=true`.
  - Spike-bar: `NCPL 2026-10-14  NO-SPIKE  peak +19% @16:05ET  (no bar cleared +15% on a volume co-spike) (as-of 16:20ET)`
  - Third-bar: `NCPL 2026-10-14  CONFIRM-3  NO no local-volume new-high ignition as-of 16:20ET`
  - Volume context (`NCPL-1620-volume-metric.json`, source `NCPL-1620-volume-sip.json`):
    - `# NCPL shared SIP volume sip-ah-volume-v2; prior 2026-10-13 48+0zero/48 slots; floor 100; same-date regular peak 841121 sh; log-only`
    - `# reconstructed as-of 2026-10-14T20:20:11+00:00; source fetched 2026-10-14T20:20:24.554380+00:00`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 16:00ET start=2026-10-14T20:00:00+00:00 shares=730815 local=unknown prior-peak=2.4272x rth-peak=0.8689x status=warmup`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 16:05ET start=2026-10-14T20:05:00+00:00 shares=410260 local=unknown prior-peak=1.3626x rth-peak=0.4878x status=warmup`
    - Consumer verdict with the metric: `NCPL 2026-10-14  CONFIRM-3  NO no local-volume new-high ignition as-of 16:20ET`
  - SIP 5-min bars: 16:00 O $1.59 H $1.89 C $1.87 (vwap $1.80, 731K sh / 3,532 trades); 16:05 H $1.90 C $1.82 (vwap $1.85, 410K sh / 2,392 trades). Real volume, and the SIP high corroborates the $1.86 scanner price. The 16:10+ bars are still inside the free-tier delay.
  - Book: `node scripts/broker.js quote` bid $1.97 x100 / ask $2.04 x100 at 16:19:27 ET, above the scanner's $1.86, so NCPL kept rising after the snapshot (~+28% AH, ~+46% Total at $2.03 against the $1.39 prior close implied by Day%).
    - `NCPL BOOK iex bid $2.00 x100 / ask $2.03 x100 @ 2026-10-14 16:20:32 ET age 0s two-sided spread 1.48% of ask`
    - `NCPL BOOK sip-15m bid $1.87 x600 / ask $1.88 x600 @ 2026-10-14 16:05:32 ET age 15m00s two-sided spread 0.53% of ask`
    - `NCPL BOOK refresh +15s iex advanced @ 2026-10-14 16:20:45 ET`
    - `NCPL BOOK verdict: IEX FRESH; SIP-15m TWO-SIDED (observed 2026-10-14 16:20:32 ET; log-only)`
  - Catalyst (2 searches): GlobeNewswire 2026-10-14, ~16:00 ET, "Netcapital Inc. Regains Compliance with Nasdaq Minimum Bid Price Requirement" (Nasdaq letter dated Oct 7). Fresh but minor: **Grade C**. Background: securities class-action law firm PRs (Portnoy, Wolf Haldenstein, Oct 11–14; class period Dec 15 2021 – Sep 3 2026). The Wolf Haldenstein headline calls NCPL "acquired"; no acquisition release turned up, so treat that as unverified wording.
  - Day 2+ of a move (21:30 notes: >10% AH on Oct 6/7/12/13). Run the MULTI-SESSION-RUNNER SIP daily-bar check if it qualifies for entry.
- Observation window (before 23:00 CET); no entries.

## Scan 22:25 CET (4:25 PM ET)

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $1.59 | +14.4% | +13.9% | $1.81 | +30.3% | 1.0M | 11.5M | 0.1x | 4.4M | Miscellaneous Commercial Services |
| TRUG | [TV](https://www.tradingview.com/chart/?symbol=TRUG) | $1.38 | -20.7% | +14.4% | $1.58 | -9.2% | 69K | 308K | 0.2x | 1.2M | Packaged Software |

Supplementary AH-change-only (>15%, not in volume pass): none

AH >10% at this snapshot (unrounded): NCPL, TRUG

**Evaluation notes:**
- NCPL: second AH scan above 10% (2 of 2), so it meets the scan-count gate for the 23:00 window. The SIP trajectory is fading off the open: high $1.90 in the 16:05 bar, then 16:10 C $1.78 on 103K sh / 750 trades, down from 731K and 410K. The IEX quote ($2.02 / $2.08 at 16:24 ET) sits above the SIP 16:10 bar; recheck the high and the trajectory at 23:00. `tradable=true`. Catalyst unchanged: Grade C (Nasdaq bid-price compliance PR, GlobeNewswire 2026-10-14 ~16:00 ET).
  - Spike-bar: `NCPL 2026-10-14  NO-SPIKE  peak +19% @16:05ET  (no bar cleared +15% on a volume co-spike) (as-of 16:25ET)`
  - Third-bar: `NCPL 2026-10-14  CONFIRM-3  NO no local-volume new-high ignition as-of 16:25ET`
  - Volume context (`NCPL-1625-volume-metric.json`, source `NCPL-1625-volume-sip.json`):
    - `# NCPL shared SIP volume sip-ah-volume-v2; prior 2026-10-13 48+0zero/48 slots; floor 100; same-date regular peak 841121 sh; log-only`
    - `# reconstructed as-of 2026-10-14T20:25:10+00:00; source fetched 2026-10-14T20:25:33.686793+00:00`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 16:00ET start=2026-10-14T20:00:00+00:00 shares=730815 local=unknown prior-peak=2.4272x rth-peak=0.8689x status=warmup`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 16:05ET start=2026-10-14T20:05:00+00:00 shares=410260 local=unknown prior-peak=1.3626x rth-peak=0.4878x status=warmup`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 16:10ET start=2026-10-14T20:10:00+00:00 shares=102754 local=unknown prior-peak=0.3413x rth-peak=0.1222x status=warmup`
    - Consumer verdict with the metric: `NCPL 2026-10-14  CONFIRM-3  NO no local-volume new-high ignition as-of 16:25ET`
  - Book:
    - `NCPL BOOK iex bid $2.02 x100 / ask $2.08 x100 @ 2026-10-14 16:24:10 ET age 1m27s two-sided spread 2.88% of ask`
    - `NCPL BOOK sip-15m bid $1.78 x3000 / ask $1.80 x400 @ 2026-10-14 16:10:37 ET age 15m00s two-sided spread 1.11% of ask`
    - `NCPL BOOK refresh +15s iex unchanged @ 2026-10-14 16:24:10 ET`
    - `NCPL BOOK verdict: IEX STALE 1m27s; SIP-15m TWO-SIDED (observed 2026-10-14 16:25:37 ET; log-only)`
  - MULTI-SESSION-RUNNER check (SIP daily bars): Oct 9 C $1.14 → Oct 12 C $1.54 (+35%, H $2.66 on 52.0M sh) → Oct 13 C $1.39 → Oct 14 C $1.59. No prior session closed ≥+50% and today's close is below 2x the Oct 9 close ($2.28), so the tag does not apply. It is a repeat mover (Oct 6/7/12/13 AH footprints) rather than a fresh igniter.
  - First-bar-spike watch: the AH high so far is in the 16:05 bar (inside the 16:00–16:15 window) and CONFIRM-3 reads NO at both scans. If that holds at 23:00, the first-bar-spike skip applies.
- TRUG: first AH scan above 10% (1 of 2). `tradable=true`. Day% −20.7% puts it under the dead-cat filter; Total% −9.2% means the AH move is still below the Oct 13 close of $1.74. SIP shows a real ignition in the 16:10 bar: H $1.74, C $1.51, vwap $1.62, 814K sh / 5,582 trades (vs 72K / 205 trades at 16:05). The bar closed 13% off its high, and the fresh IEX quote ($1.39 / $1.42 at 16:25 ET) is back near the $1.38 close, so the spike looks round-tripped.
  - Spike-bar: `TRUG 2026-10-14  SPIKE  16:10ET  +22%  $1.68  1089 trades / 168k sh  (first co-spike bar) (as-of 16:25ET)`
  - Third-bar: `TRUG 2026-10-14  CONFIRM-3  PENDING ignition 16:05ET; waiting for third bar as-of 16:25ET`
  - Volume context (`TRUG-1625-volume-metric.json`, source `TRUG-1625-volume-sip.json`):
    - `# TRUG shared SIP volume sip-ah-volume-v2; prior 2026-10-13 21+27zero/48 slots; floor 100; same-date regular peak 32960 sh; log-only`
    - `# reconstructed as-of 2026-10-14T20:25:10+00:00; source fetched 2026-10-14T20:25:35.748101+00:00`
    - `TRUG 2026-10-14  VOLUME-CONTEXT 16:00ET start=2026-10-14T20:00:00+00:00 shares=1891 local=unknown prior-peak=0.5529x rth-peak=0.0574x status=warmup`
    - `TRUG 2026-10-14  VOLUME-CONTEXT 16:05ET start=2026-10-14T20:05:00+00:00 shares=71586 local=unknown prior-peak=20.9316x rth-peak=2.1719x status=warmup`
    - `TRUG 2026-10-14  VOLUME-CONTEXT 16:10ET start=2026-10-14T20:10:00+00:00 shares=813779 local=unknown prior-peak=237.9471x rth-peak=24.6899x status=warmup`
    - Consumer verdict with the metric: `TRUG 2026-10-14  CONFIRM-3  PENDING ignition 16:05ET; waiting for third bar as-of 16:25ET`
  - Book:
    - `TRUG BOOK iex bid $1.39 x100 / ask $1.42 x100 @ 2026-10-14 16:25:32 ET age 5s two-sided spread 2.11% of ask`
    - `TRUG BOOK sip-15m bid $1.60 x300 / ask $1.61 x11200 @ 2026-10-14 16:10:37 ET age 15m00s two-sided spread 0.62% of ask`
    - `TRUG BOOK refresh +15s iex advanced @ 2026-10-14 16:25:44 ET`
    - `TRUG BOOK verdict: IEX FRESH; SIP-15m TWO-SIDED (observed 2026-10-14 16:25:37 ET; log-only)`
  - Catalyst (2 searches): GlobeNewswire 2026-10-14 08:35 ET, "TruGolf Links Engages Polymath for Cap Table Tokenization" (intercompany agreement after the Polymath merger). It is same-day but came out before the open, and the stock fell 20.7% after it, so it does not explain the AH move. Background: Nasdaq equity-shortfall notice (8-K, Aug 21, compliance plan due Oct 5). No after-close release found: **Grade None**.
  - SIP daily bars: Oct 7 C $2.75 → Oct 14 C $1.38, a multi-session decline. No MULTI-SESSION-RUNNER tag.
  - TRUG was the Aug 25 FINAL-SCAN-GATE-BLOCK name.
- Observation window (before 23:00 CET); no entries.

## Scan 22:30 CET (4:30 PM ET)

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $1.59 | +14.4% | +11.9% | $1.78 | +28.1% | 1.1M | 11.5M | 0.1x | 4.4M | Miscellaneous Commercial Services |
| TRUG | [TV](https://www.tradingview.com/chart/?symbol=TRUG) | $1.38 | -20.7% | +10.1% | $1.52 | -12.6% | 767K | 388K | 2.0x | 1.2M | Packaged Software |
| TCRT | [TV](https://www.tradingview.com/chart/?symbol=TCRT) | $2.07 | -31.7% | +7.7% | $2.23 | -26.4% | 130K | 32.9M | 0.0x | 2.3M | Biotechnology |

Supplementary AH-change-only (>15%, not in volume pass): none

AH >10% at this snapshot (unrounded): NCPL, TRUG

**Evaluation notes:**
- NCPL: third AH scan above 10% (scan-count gate already met). The scanner's $1.78 lags the tape: the SIP 16:15 bar made a new AH high (O $1.78 H $2.05 C $2.02, vwap $1.94, 708K sh / 3,541 trades) after the 16:10 lull, and the fresh IEX quote is $2.06 / $2.08 (~+31% AH, ~+50% Total vs the $1.39 prior close). That is a rebuild on real volume, above the 16:05 high of $1.90. CONFIRM-3 still reads NO. The new high sits in the 16:15 bar, on the edge of the first-bar window; whether the first-bar-spike skip applies depends on whether it keeps making highs after 16:15 at the 23:00 check. Catalyst unchanged: Grade C (Nasdaq bid-price compliance PR, GlobeNewswire 2026-10-14 ~16:00 ET). `tradable=true`.
  - Spike-bar: `NCPL 2026-10-14  NO-SPIKE  peak +19% @16:05ET  (no bar cleared +15% on a volume co-spike) (as-of 16:30ET)`
  - Third-bar: `NCPL 2026-10-14  CONFIRM-3  NO no local-volume new-high ignition as-of 16:30ET`
  - Volume context (`NCPL-1630-volume-metric.json`, source `NCPL-1630-volume-sip.json`):
    - `# NCPL shared SIP volume sip-ah-volume-v2; prior 2026-10-13 48+0zero/48 slots; floor 100; same-date regular peak 841121 sh; log-only`
    - `# reconstructed as-of 2026-10-14T20:30:08+00:00; source fetched 2026-10-14T20:30:20.921266+00:00`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 16:00ET start=2026-10-14T20:00:00+00:00 shares=730815 local=unknown prior-peak=2.4272x rth-peak=0.8689x status=warmup`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 16:05ET start=2026-10-14T20:05:00+00:00 shares=410260 local=unknown prior-peak=1.3626x rth-peak=0.4878x status=warmup`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 16:10ET start=2026-10-14T20:10:00+00:00 shares=102754 local=unknown prior-peak=0.3413x rth-peak=0.1222x status=warmup`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 16:15ET start=2026-10-14T20:15:00+00:00 shares=707616 local=1.7248x prior-peak=2.3502x rth-peak=0.8413x status=ok`
    - Consumer verdict with the metric: `NCPL 2026-10-14  CONFIRM-3  NO no local-volume new-high ignition as-of 16:30ET`
  - Book:
    - `NCPL BOOK iex bid $2.06 x100 / ask $2.08 x100 @ 2026-10-14 16:30:28 ET age 0s two-sided spread 0.96% of ask`
    - `NCPL BOOK sip-15m bid $1.77 x700 / ask $1.78 x2300 @ 2026-10-14 16:15:29 ET age 15m00s two-sided spread 0.56% of ask`
    - `NCPL BOOK refresh +15s iex advanced @ 2026-10-14 16:30:32 ET`
    - `NCPL BOOK verdict: IEX FRESH; SIP-15m TWO-SIDED (observed 2026-10-14 16:30:29 ET; log-only)`
- TRUG: second AH scan above 10% (2 of 2), but Day% −20.7% puts it under the dead-cat filter, and it is still below the Oct 13 close ($1.74), so no DEAD-CAT-OVERRIDE. The 16:10 spike (H $1.74) is fading: 16:15 bar H $1.63 C $1.46, vwap $1.53, 378K sh / 2,766 trades, and the fresh IEX quote is $1.39 / $1.42, back at the $1.38 close. CONFIRM-3 turned NO. Catalyst unchanged: Grade None. `tradable=true`.
  - Spike-bar: `TRUG 2026-10-14  SPIKE  16:10ET  +22%  $1.68  1089 trades / 168k sh  (first co-spike bar) (as-of 16:30ET)`
  - Third-bar: `TRUG 2026-10-14  CONFIRM-3  NO ignition 16:05ET failed third-bar hold/volume as-of 16:30ET`
  - Volume context (`TRUG-1630-volume-metric.json`, source `TRUG-1630-volume-sip.json`):
    - `# TRUG shared SIP volume sip-ah-volume-v2; prior 2026-10-13 21+27zero/48 slots; floor 100; same-date regular peak 32960 sh; log-only`
    - `# reconstructed as-of 2026-10-14T20:30:08+00:00; source fetched 2026-10-14T20:30:26.653463+00:00`
    - `TRUG 2026-10-14  VOLUME-CONTEXT 16:00ET start=2026-10-14T20:00:00+00:00 shares=1891 local=unknown prior-peak=0.5529x rth-peak=0.0574x status=warmup`
    - `TRUG 2026-10-14  VOLUME-CONTEXT 16:05ET start=2026-10-14T20:05:00+00:00 shares=71586 local=unknown prior-peak=20.9316x rth-peak=2.1719x status=warmup`
    - `TRUG 2026-10-14  VOLUME-CONTEXT 16:10ET start=2026-10-14T20:10:00+00:00 shares=813779 local=unknown prior-peak=237.9471x rth-peak=24.6899x status=warmup`
    - `TRUG 2026-10-14  VOLUME-CONTEXT 16:15ET start=2026-10-14T20:15:00+00:00 shares=377922 local=5.2793x prior-peak=110.5035x rth-peak=11.4661x status=ok`
    - Consumer verdict with the metric: `TRUG 2026-10-14  CONFIRM-3  NO ignition 16:05ET failed third-bar hold/volume as-of 16:30ET`
  - Book:
    - `TRUG BOOK iex bid $1.39 x100 / ask $1.42 x100 @ 2026-10-14 16:30:10 ET age 19s two-sided spread 2.11% of ask`
    - `TRUG BOOK sip-15m bid $1.53 x800 / ask $1.55 x300 @ 2026-10-14 16:15:28 ET age 15m00s two-sided spread 1.29% of ask`
    - `TRUG BOOK refresh +15s iex unchanged @ 2026-10-14 16:30:10 ET`
    - `TRUG BOOK verdict: IEX FRESH; SIP-15m TWO-SIDED (observed 2026-10-14 16:30:29 ET; log-only)`
- TCRT: AH +7.7%, below the 10% threshold; Day% −31.7%. Not evaluated.
- Observation window (before 23:00 CET); no entries.

## Scan 22:45 CET (4:45 PM ET)

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $1.59 | +14.4% | +31.4% | $2.09 | +50.4% | 3.8M | 11.8M | 0.3x | 4.4M | Miscellaneous Commercial Services |
| YYAI | [TV](https://www.tradingview.com/chart/?symbol=YYAI) | $0.69 | -2.6% | +8.5% | $0.75 | +5.6% | 393K | 253K | 1.6x | 4.6M | Containers/Packaging |
| TCRT | [TV](https://www.tradingview.com/chart/?symbol=TCRT) | $2.07 | -31.7% | +10.1% | $2.28 | -24.8% | 295K | 32.9M | 0.0x | 2.3M | Biotechnology |
| SDEV | [TV](https://www.tradingview.com/chart/?symbol=SDEV) | $0.99 | -20.8% | +5.0% | $1.04 | -16.8% | 252K | 50.1M | 0.0x | 51.8M | Financial Conglomerates |
| CDXS | [TV](https://www.tradingview.com/chart/?symbol=CDXS) | $1.29 | -2.3% | +5.6% | $1.36 | +3.2% | 75K | 805K | 0.1x | 101.7M | Chemicals: Specialty |

Supplementary AH-change-only (>15%, not in volume pass): none

AH >10% at this snapshot (unrounded): NCPL, TCRT

The 22:35 and 22:40 pulses left no section in the log; this scan follows 22:30.

**Evaluation notes:**
- NCPL: fourth AH scan above 10% (scan-count gate met). It is building: SIP made new AH highs after the first-bar window, 16:20 bar H $2.13 (1.27M sh / 6,661 trades) and 16:25 bar H $2.14 C $2.10 (911K sh / 4,880 trades); 16:30 C $2.04 on 502K sh / 2,789 trades. The fresh IEX quote is $2.12 / $2.14 at 16:45 ET (~+53% Total vs the $1.39 prior close), at the AH high. With the high now in the 16:25 bar, the first-bar-spike skip no longer applies on high timing, though CONFIRM-3 still reads NO. Catalyst unchanged: Grade C (Nasdaq bid-price compliance PR, GlobeNewswire 2026-10-14 ~16:00 ET). `tradable=true`. Repeat mover, no MULTI-SESSION-RUNNER tag (22:25 check). Entry decision waits for the 23:00 window.
  - Spike-bar: `NCPL 2026-10-14  SPIKE  16:19ET  +29%  $2.05  2021 trades / 400k sh  (first co-spike bar) (as-of 16:45ET)`
  - Third-bar: `NCPL 2026-10-14  CONFIRM-3  NO ignition 16:20ET failed third-bar hold/volume as-of 16:45ET`
  - Volume context (`NCPL-1645-volume-metric.json`, source `NCPL-1645-volume-sip.json`):
    - `# NCPL shared SIP volume sip-ah-volume-v2; prior 2026-10-13 48+0zero/48 slots; floor 100; same-date regular peak 841121 sh; log-only`
    - `# reconstructed as-of 2026-10-14T20:45:12+00:00; source fetched 2026-10-14T20:45:33.716805+00:00`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 16:00ET start=2026-10-14T20:00:00+00:00 shares=730815 local=unknown prior-peak=2.4272x rth-peak=0.8689x status=warmup`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 16:05ET start=2026-10-14T20:05:00+00:00 shares=410260 local=unknown prior-peak=1.3626x rth-peak=0.4878x status=warmup`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 16:10ET start=2026-10-14T20:10:00+00:00 shares=102754 local=unknown prior-peak=0.3413x rth-peak=0.1222x status=warmup`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 16:15ET start=2026-10-14T20:15:00+00:00 shares=707616 local=1.7248x prior-peak=2.3502x rth-peak=0.8413x status=ok`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 16:20ET start=2026-10-14T20:20:00+00:00 shares=1273437 local=3.1040x prior-peak=4.2294x rth-peak=1.5140x status=ok`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 16:25ET start=2026-10-14T20:25:00+00:00 shares=910853 local=1.2872x prior-peak=3.0252x rth-peak=1.0829x status=ok`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 16:30ET start=2026-10-14T20:30:00+00:00 shares=501736 local=0.5508x prior-peak=1.6664x rth-peak=0.5965x status=ok`
    - Consumer verdict with the metric: `NCPL 2026-10-14  CONFIRM-3  NO ignition 16:20ET failed third-bar hold/volume as-of 16:45ET`
  - Book:
    - `NCPL BOOK iex bid $2.12 x100 / ask $2.14 x100 @ 2026-10-14 16:45:37 ET age 0s two-sided spread 0.93% of ask`
    - `NCPL BOOK sip-15m bid $2.06 x900 / ask $2.07 x900 @ 2026-10-14 16:30:37 ET age 15m00s two-sided spread 0.48% of ask`
    - `NCPL BOOK refresh +15s iex advanced @ 2026-10-14 16:45:41 ET`
    - `NCPL BOOK verdict: IEX FRESH; SIP-15m TWO-SIDED (observed 2026-10-14 16:45:37 ET; log-only)`
- TCRT: first AH scan above 10% (1 of 2). `tradable=true`. Day% −31.7% puts it under the dead-cat filter, and Total% −24.8% keeps it far below the Oct 13 close, so no DEAD-CAT-OVERRIDE. SIP volume is thin: 27K–79K sh and 141–346 trades per bar from 16:00 to 16:30 ET (prior-peak ratios 0.02–0.05x), so the drift from $2.07 to $2.29 is a thin drift, not a build. No book check (SIP volume not accumulating).
  - Spike-bar: `TCRT 2026-10-14  NO-SPIKE  peak +11% @16:24ET  (no bar cleared +15% on a volume co-spike) (as-of 16:45ET)`
  - Third-bar: `TCRT 2026-10-14  CONFIRM-3  NO no local-volume new-high ignition as-of 16:45ET`
  - Volume context (`TCRT-1645-volume-metric.json`, source `TCRT-1645-volume-sip.json`):
    - `# TCRT shared SIP volume sip-ah-volume-v2; prior 2026-10-13 48+0zero/48 slots; floor 100; same-date regular peak 3615305 sh; log-only`
    - `# reconstructed as-of 2026-10-14T20:45:12+00:00; source fetched 2026-10-14T20:45:35.774595+00:00`
    - `TCRT 2026-10-14  VOLUME-CONTEXT 16:00ET start=2026-10-14T20:00:00+00:00 shares=53130 local=unknown prior-peak=0.0335x rth-peak=0.0147x status=warmup`
    - `TCRT 2026-10-14  VOLUME-CONTEXT 16:05ET start=2026-10-14T20:05:00+00:00 shares=27428 local=unknown prior-peak=0.0173x rth-peak=0.0076x status=warmup`
    - `TCRT 2026-10-14  VOLUME-CONTEXT 16:10ET start=2026-10-14T20:10:00+00:00 shares=60354 local=unknown prior-peak=0.0381x rth-peak=0.0167x status=warmup`
    - `TCRT 2026-10-14  VOLUME-CONTEXT 16:15ET start=2026-10-14T20:15:00+00:00 shares=66856 local=1.2583x prior-peak=0.0422x rth-peak=0.0185x status=ok`
    - `TCRT 2026-10-14  VOLUME-CONTEXT 16:20ET start=2026-10-14T20:20:00+00:00 shares=78990 local=1.3088x prior-peak=0.0498x rth-peak=0.0218x status=ok`
    - `TCRT 2026-10-14  VOLUME-CONTEXT 16:25ET start=2026-10-14T20:25:00+00:00 shares=33679 local=0.5038x prior-peak=0.0212x rth-peak=0.0093x status=ok`
    - `TCRT 2026-10-14  VOLUME-CONTEXT 16:30ET start=2026-10-14T20:30:00+00:00 shares=48679 local=0.7281x prior-peak=0.0307x rth-peak=0.0135x status=ok`
    - Consumer verdict with the metric: `TCRT 2026-10-14  CONFIRM-3  NO no local-volume new-high ignition as-of 16:45ET`
  - Catalyst (3 searches): Alaunos Therapeutics completed its acquisition of Velaris Therapeutics with a concurrent $350M private placement (GlobeNewswire 2026-10-13 ~10:31 ET). That is prior-day news, background only; it drove the Oct 13 spike that today's −31.7% session unwound. No Oct 14 after-close release found: **Grade None**.
- TRUG: dropped out of the scan (below 10% AH); the 16:10 spike has round-tripped toward the $1.38 close.
- YYAI, SDEV, CDXS: AH below 10%. Not evaluated.
- Observation window (before 23:00 CET); no entries.

## Scan 23:00 CET (5:00 PM ET)

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $1.59 | +14.4% | +31.4% | $2.09 | +50.4% | 4.9M | 11.9M | 0.4x | 4.4M | Miscellaneous Commercial Services |
| YYAI | [TV](https://www.tradingview.com/chart/?symbol=YYAI) | $0.69 | -2.6% | +6.4% | $0.74 | +3.6% | 634K | 281K | 2.3x | 4.6M | Containers/Packaging |
| TCRT | [TV](https://www.tradingview.com/chart/?symbol=TCRT) | $2.07 | -31.7% | +6.8% | $2.21 | -27.1% | 396K | 32.9M | 0.0x | 2.3M | Biotechnology |
| SDEV | [TV](https://www.tradingview.com/chart/?symbol=SDEV) | $0.99 | -20.8% | +5.1% | $1.04 | -16.8% | 325K | 50.1M | 0.0x | 51.8M | Financial Conglomerates |
| BENF | [TV](https://www.tradingview.com/chart/?symbol=BENF) | $0.87 | -0.3% | +5.1% | $0.92 | +4.8% | 307K | 964K | 0.3x | 2.6M | Investment Managers |
| CISS | [TV](https://www.tradingview.com/chart/?symbol=CISS) | $0.53 | -15.5% | +6.1% | $0.56 | -10.4% | 97K | 1.0M | 0.1x | 1.5M | Marine Shipping |
| CDXS | [TV](https://www.tradingview.com/chart/?symbol=CDXS) | $1.29 | -2.3% | +5.6% | $1.36 | +3.2% | 75K | 805K | 0.1x | 101.7M | Chemicals: Specialty |

Supplementary AH-change-only (>15%, not in volume pass): none

AH >10% at this snapshot (unrounded): NCPL

The scanner's +31.4% / $2.09 for NCPL matches the 22:45 snapshot, so TradingView's figure is lagging. SIP and the IEX quote put NCPL at $2.15–$2.20.

**Evaluation notes:**
- NCPL: **ENTERED**. Fifth AH scan above 10%. Float 4.4M, Day% +14.4%, Total% under the +150% ceiling. The stock is building: SIP made new AH highs of $2.15 in the 16:40 bar (516K sh / 2,966 trades) and the 16:45 bar (392K sh / 2,328 trades), and volume is still accumulating at 276K–517K sh per bar since 16:30. The fresh IEX quote at 16:59 ET is $2.16 / $2.20, at the AH high. The AH high falls after the first-bar window, so the first-bar-spike skip does not apply, although CONFIRM-3 still reads NO. Catalyst Grade C: Nasdaq bid-price compliance PR (GlobeNewswire 2026-10-14 ~16:00 ET). `tradable=true`. The 22:25 check found no MULTI-SESSION-RUNNER tag. Bought 45 sh with a $2.24 limit; filled at **$2.16** (order 529b8e3a). Entry Total% is +55.4% vs the $1.39 prior close. The fill came in below the ask, so no CHASE-CAP.
  - Spike-bar: `NCPL 2026-10-14  SPIKE  16:19ET  +29%  $2.05  2021 trades / 400k sh  (first co-spike bar) (as-of 17:00ET)`
  - Third-bar: `NCPL 2026-10-14  CONFIRM-3  NO ignition 16:20ET failed third-bar hold/volume as-of 17:00ET`
  - Volume context (`NCPL-1700-volume-metric.json`, source `NCPL-1700-volume-sip.json`):
    - `# NCPL shared SIP volume sip-ah-volume-v2; prior 2026-10-13 48+0zero/48 slots; floor 100; same-date regular peak 841121 sh; log-only`
    - `# reconstructed as-of 2026-10-14T21:00:07+00:00; source fetched 2026-10-14T21:00:22.088238+00:00`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 16:00ET start=2026-10-14T20:00:00+00:00 shares=730815 local=unknown prior-peak=2.4272x rth-peak=0.8689x status=warmup`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 16:05ET start=2026-10-14T20:05:00+00:00 shares=410260 local=unknown prior-peak=1.3626x rth-peak=0.4878x status=warmup`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 16:10ET start=2026-10-14T20:10:00+00:00 shares=102754 local=unknown prior-peak=0.3413x rth-peak=0.1222x status=warmup`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 16:15ET start=2026-10-14T20:15:00+00:00 shares=707616 local=1.7248x prior-peak=2.3502x rth-peak=0.8413x status=ok`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 16:20ET start=2026-10-14T20:20:00+00:00 shares=1273437 local=3.1040x prior-peak=4.2294x rth-peak=1.5140x status=ok`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 16:25ET start=2026-10-14T20:25:00+00:00 shares=910853 local=1.2872x prior-peak=3.0252x rth-peak=1.0829x status=ok`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 16:30ET start=2026-10-14T20:30:00+00:00 shares=501736 local=0.5508x prior-peak=1.6664x rth-peak=0.5965x status=ok`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 16:35ET start=2026-10-14T20:35:00+00:00 shares=276180 local=0.3032x prior-peak=0.9173x rth-peak=0.3283x status=ok`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 16:40ET start=2026-10-14T20:40:00+00:00 shares=516498 local=1.0294x prior-peak=1.7154x rth-peak=0.6141x status=ok`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 16:45ET start=2026-10-14T20:45:00+00:00 shares=391784 local=0.7809x prior-peak=1.3012x rth-peak=0.4658x status=ok`
    - Consumer verdict with the metric: `NCPL 2026-10-14  CONFIRM-3  NO ignition 16:20ET failed third-bar hold/volume as-of 17:00ET`
  - Book:
    - `NCPL BOOK iex bid $2.16 x100 / ask $2.20 x100 @ 2026-10-14 16:59:34 ET age 49s two-sided spread 1.82% of ask`
    - `NCPL BOOK sip-15m bid $2.07 x2700 / ask $2.08 x500 @ 2026-10-14 16:45:21 ET age 15m02s two-sided spread 0.48% of ask`
    - `NCPL BOOK refresh +15s iex unchanged @ 2026-10-14 16:59:34 ET`
    - `NCPL BOOK verdict: IEX FRESH; SIP-15m TWO-SIDED (observed 2026-10-14 17:00:23 ET; log-only)`
- TCRT: back below 10% AH (+6.8%), so it stays at 1 AH scan above 10%. Dead-cat (Day% −31.7%), thin SIP volume, Grade None. Not eligible.
- YYAI, SDEV, BENF, CISS, CDXS: AH below 10%. Not evaluated.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
| NCPL | $2.16 | 23:00 CET (17:00 ET) | 45 | 529b8e3a-fefd-418e-a890-521863b1f423 | Grade C (Nasdaq compliance PR); AH BUILD with new highs on 276K–517K sh/bar; float 4.4M; Total +55.4% |
