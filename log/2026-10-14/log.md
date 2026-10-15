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

## Scan 23:30 CET (5:30 PM ET)

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $1.59 | +14.4% | +39.6% | $2.22 | +59.7% | 6.8M | 12.2M | 0.6x | 4.4M | Miscellaneous Commercial Services |
| YYAI | [TV](https://www.tradingview.com/chart/?symbol=YYAI) | $0.69 | -2.6% | +11.5% | $0.77 | +8.6% | 735K | 291K | 2.5x | 4.6M | Containers/Packaging |
| TCRT | [TV](https://www.tradingview.com/chart/?symbol=TCRT) | $2.07 | -31.7% | +6.2% | $2.20 | -27.4% | 482K | 32.9M | 0.0x | 2.3M | Biotechnology |
| SDEV | [TV](https://www.tradingview.com/chart/?symbol=SDEV) | $0.99 | -20.8% | +5.1% | $1.04 | -16.8% | 365K | 50.1M | 0.0x | 51.8M | Financial Conglomerates |
| CISS | [TV](https://www.tradingview.com/chart/?symbol=CISS) | $0.53 | -15.5% | +8.6% | $0.57 | -8.3% | 231K | 1.1M | 0.2x | 1.5M | Marine Shipping |
| SBNYL | [TV](https://www.tradingview.com/chart/?symbol=SBNYL) | $1.25 | -0.8% | +10.4% | $1.38 | +9.5% | 180K | 40K | 4.5x | 59.6M | Regional Banks |
| AGMH | [TV](https://www.tradingview.com/chart/?symbol=AGMH) | $0.50 | -5.4% | +5.8% | $0.53 | +0.1% | 161K | 10.2M | 0.0x | 735K | Packaged Software |
| CDXS | [TV](https://www.tradingview.com/chart/?symbol=CDXS) | $1.29 | -2.3% | +5.6% | $1.36 | +3.2% | 75K | 805K | 0.1x | 101.7M | Chemicals: Specialty |
| FBGL | [TV](https://www.tradingview.com/chart/?symbol=FBGL) | $2.40 | -31.6% | +6.2% | $2.55 | -27.4% | 59K | 359K | 0.2x | n/a | Engineering & Construction |

Supplementary AH-change-only (>15%, not in volume pass): none

AH >10% at this snapshot (unrounded): NCPL, SBNYL, YYAI

The 23:05–23:25 pulses left no section in the log; this scan follows 23:00.

**Evaluation notes:**
- NCPL: **already entered** (45 sh @ $2.16, 23:00 CET); broker shows the position and the filled buy, so no new order. Still building: SIP made a new AH high of $2.25 in the 17:10 bar (413K sh / 2,314 trades, VWAP $2.20) and the 17:15 bar held $2.15–$2.24 on 296K sh / 1,889 trades. Volume keeps accumulating at 295K–413K sh per bar. Scanner $2.22 (+59.7% Total) matches SIP. Position at $2.17, +0.5%.
  - Spike-bar: `NCPL 2026-10-14  SPIKE  16:19ET  +29%  $2.05  2021 trades / 400k sh  (first co-spike bar) (as-of 17:30ET)`
  - Third-bar: `NCPL 2026-10-14  CONFIRM-3  NO ignition 16:20ET failed third-bar hold/volume as-of 17:30ET`
  - Volume context (`NCPL-1730-volume-metric.json`, source `NCPL-1730-volume-sip.json`):
    - `# NCPL shared SIP volume sip-ah-volume-v2; prior 2026-10-13 48+0zero/48 slots; floor 100; same-date regular peak 841121 sh; log-only`
    - `# reconstructed as-of 2026-10-14T21:30:08+00:00; source fetched 2026-10-14T21:30:32.923875+00:00`
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
    - `NCPL 2026-10-14  VOLUME-CONTEXT 16:50ET start=2026-10-14T20:50:00+00:00 shares=189984 local=0.4849x prior-peak=0.6310x rth-peak=0.2259x status=ok`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 16:55ET start=2026-10-14T20:55:00+00:00 shares=428924 local=1.0948x prior-peak=1.4246x rth-peak=0.5099x status=ok`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 17:00ET start=2026-10-14T21:00:00+00:00 shares=395166 local=1.0086x prior-peak=1.3125x rth-peak=0.4698x status=ok`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 17:05ET start=2026-10-14T21:05:00+00:00 shares=295024 local=0.7466x prior-peak=0.9799x rth-peak=0.3508x status=ok`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 17:10ET start=2026-10-14T21:10:00+00:00 shares=412687 local=1.0443x prior-peak=1.3706x rth-peak=0.4906x status=ok`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 17:15ET start=2026-10-14T21:15:00+00:00 shares=295566 local=0.7480x prior-peak=0.9817x rth-peak=0.3514x status=ok`
    - Consumer verdict with the metric: `NCPL 2026-10-14  CONFIRM-3  NO ignition 16:20ET failed third-bar hold/volume as-of 17:30ET`
  - Book:
    - `NCPL BOOK iex bid $2.16 x100 / ask $2.20 x100 @ 2026-10-14 16:59:34 ET age 31m08s two-sided spread 1.82% of ask`
    - `NCPL BOOK sip-15m bid $2.19 x2100 / ask $2.20 x2100 @ 2026-10-14 17:15:43 ET age 15m00s two-sided spread 0.45% of ask`
    - `NCPL BOOK refresh +15s iex unchanged @ 2026-10-14 16:59:34 ET`
    - `NCPL BOOK verdict: IEX STALE 31m08s; SIP-15m TWO-SIDED (observed 2026-10-14 17:30:43 ET; log-only)`
- YYAI: first AH scan above 10% (1 of 2), so not eligible this pulse. `tradable=true`. Scanner AH +11.5% ($0.77) but Total% only +8.6% vs the prior close. SIP shows an early pop to $0.84–$0.85 in the 16:15–16:25 bars (182K–217K sh, 697–962 trades), then a thin drift at $0.72–$0.78 on 8K–33K sh and 18–67 trades per bar since 16:45. That is a faded early spike with thin volume, not a build. No book check (SIP volume not accumulating). Catalyst (2 searches): only background items (Oct 2025 AiRWA rename and $100M JuCoin investment, Dec 2025 registered direct offering); no Oct 14 release found: **Grade None**.
  - Spike-bar: `YYAI 2026-10-14  SPIKE  16:19ET  +22%  $0.84  121 trades / 23k sh  (first co-spike bar) (as-of 17:30ET)`
  - Third-bar: `YYAI 2026-10-14  CONFIRM-3  NO no local-volume new-high ignition as-of 17:30ET`
  - Volume context (`YYAI-1730-volume-metric.json`, source `YYAI-1730-volume-sip.json`):
    - `# YYAI shared SIP volume sip-ah-volume-v2; prior 2026-10-13 4+44zero/48 slots; floor 100; same-date regular peak 11250 sh; log-only`
    - `# reconstructed as-of 2026-10-14T21:30:08+00:00; source fetched 2026-10-14T21:30:34.927506+00:00`
    - `YYAI 2026-10-14  VOLUME-CONTEXT 16:15ET start=2026-10-14T20:15:00+00:00 shares=27783 local=277.8300x prior-peak=55.5660x rth-peak=2.4696x status=floored`
    - `YYAI 2026-10-14  VOLUME-CONTEXT 16:20ET start=2026-10-14T20:20:00+00:00 shares=182000 local=1820.0000x prior-peak=364.0000x rth-peak=16.1778x status=floored`
    - `YYAI 2026-10-14  VOLUME-CONTEXT 16:25ET start=2026-10-14T20:25:00+00:00 shares=217084 local=7.8136x prior-peak=434.1680x rth-peak=19.2964x status=ok`
    - `YYAI 2026-10-14  VOLUME-CONTEXT 16:30ET start=2026-10-14T20:30:00+00:00 shares=133382 local=0.7329x prior-peak=266.7640x rth-peak=11.8562x status=ok`
    - `YYAI 2026-10-14  VOLUME-CONTEXT 16:35ET start=2026-10-14T20:35:00+00:00 shares=52908 local=0.2907x prior-peak=105.8160x rth-peak=4.7029x status=ok`
    - `YYAI 2026-10-14  VOLUME-CONTEXT 16:40ET start=2026-10-14T20:40:00+00:00 shares=73449 local=0.5507x prior-peak=146.8980x rth-peak=6.5288x status=ok`
    - `YYAI 2026-10-14  VOLUME-CONTEXT 16:45ET start=2026-10-14T20:45:00+00:00 shares=21078 local=0.2870x prior-peak=42.1560x rth-peak=1.8736x status=ok`
    - `YYAI 2026-10-14  VOLUME-CONTEXT 16:50ET start=2026-10-14T20:50:00+00:00 shares=23423 local=0.4427x prior-peak=46.8460x rth-peak=2.0820x status=ok`
    - `YYAI 2026-10-14  VOLUME-CONTEXT 16:55ET start=2026-10-14T20:55:00+00:00 shares=8250 local=0.3522x prior-peak=16.5000x rth-peak=0.7333x status=ok`
    - `YYAI 2026-10-14  VOLUME-CONTEXT 17:00ET start=2026-10-14T21:00:00+00:00 shares=32629 local=1.5480x prior-peak=65.2580x rth-peak=2.9004x status=ok`
    - `YYAI 2026-10-14  VOLUME-CONTEXT 17:05ET start=2026-10-14T21:05:00+00:00 shares=8826 local=0.3768x prior-peak=17.6520x rth-peak=0.7845x status=ok`
    - `YYAI 2026-10-14  VOLUME-CONTEXT 17:10ET start=2026-10-14T21:10:00+00:00 shares=8632 local=0.9780x prior-peak=17.2640x rth-peak=0.7673x status=ok`
    - `YYAI 2026-10-14  VOLUME-CONTEXT 17:15ET start=2026-10-14T21:15:00+00:00 shares=10380 local=1.1761x prior-peak=20.7600x rth-peak=0.9227x status=ok`
    - Consumer verdict with the metric: `YYAI 2026-10-14  CONFIRM-3  NO no local-volume new-high ignition as-of 17:30ET`
- SBNYL: **untradable** (`tradable=false`, OTC preferred). Qualified-but-untradable broker-block for the morning tally: AH +10.4%, first AH scan above 10%. Carry as untradable; no SIP or catalyst workup.
  - Spike-bar: `SBNYL 2026-10-14: NO prior-close (daily bar missing)`
  - Third-bar: `SBNYL 2026-10-14  CONFIRM-3  NO-DATA prior close unavailable`
- TCRT, SDEV, CISS, AGMH, CDXS, FBGL: AH below 10%. Not evaluated (TCRT stays dead-cat, Day% −31.7%).
- No new entries.

## Scan 00:00 CET (6:00 PM ET)

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $1.59 | +14.4% | +35.9% | $2.16 | +55.4% | 7.7M | 12.2M | 0.6x | 4.4M | Miscellaneous Commercial Services |
| YYAI | [TV](https://www.tradingview.com/chart/?symbol=YYAI) | $0.69 | -2.6% | +21.4% | $0.84 | +18.2% | 1.1M | 336K | 3.4x | 4.6M | Containers/Packaging |
| GMEX | [TV](https://www.tradingview.com/chart/?symbol=GMEX) | $1.71 | -18.2% | +5.3% | $1.80 | -13.9% | 812K | 563K | 1.4x | n/a | Specialty Stores |
| GENK | [TV](https://www.tradingview.com/chart/?symbol=GENK) | $1.69 | +16.6% | +5.2% | $1.78 | +22.7% | 308K | 5.7M | 0.1x | 6.6M | Restaurants |
| CLNE | [TV](https://www.tradingview.com/chart/?symbol=CLNE) | $1.35 | -5.6% | +7.4% | $1.45 | +1.4% | 307K | 949K | 0.3x | 161.1M | Gas Distributors |
| CISS | [TV](https://www.tradingview.com/chart/?symbol=CISS) | $0.53 | -15.5% | +7.7% | $0.57 | -9.0% | 245K | 1.1M | 0.2x | 1.5M | Marine Shipping |
| AGMH | [TV](https://www.tradingview.com/chart/?symbol=AGMH) | $0.50 | -5.4% | +7.2% | $0.54 | +1.4% | 202K | 10.2M | 0.0x | 735K | Packaged Software |
| SBNYL | [TV](https://www.tradingview.com/chart/?symbol=SBNYL) | $1.25 | -0.8% | +10.4% | $1.38 | +9.5% | 180K | 40K | 4.5x | 59.6M | Regional Banks |
| JBDI | [TV](https://www.tradingview.com/chart/?symbol=JBDI) | $2.51 | -26.8% | +10.0% | $2.76 | -19.5% | 86K | 9.6M | 0.0x | n/a | Wholesale Distributors |
| LUCD | [TV](https://www.tradingview.com/chart/?symbol=LUCD) | $0.54 | -10.4% | +6.8% | $0.58 | -4.3% | 69K | 2.3M | 0.0x | 160.1M | Medical Specialties |

Supplementary AH-change-only (>15%, not in volume pass): none

AH >10% at this snapshot (unrounded): NCPL, SBNYL, YYAI

**Evaluation notes:**
- YYAI: **ENTERED**. Second AH scan above 10% (23:30 +11.5%, 00:00 +21.4%). Float 4.6M, Day% −2.6%, Total% under the +150% ceiling. SIP shows a second ignition after the faded 16:15–16:25 pop: the 17:30 bar ran to $0.90 (48K sh / 344 trades), the 17:35 bar printed 126K sh / 746 trades, and the 17:40 bar made the AH high of **$0.95** on 234K sh / 996 trades (VWAP $0.86). The 17:45 bar pulled back to a $0.79 close on 113K sh / 466 trades. The delayed SIP book at 17:45:40 ET was $0.850 / $0.853, and the scanner's $0.84 sits ~12% under the high, so the stock is holding. The AH high came at 17:40 ET, after the first-bar window, and CONFIRM-3 reads YES, so the first-bar-spike skip does not apply. `tradable=true`. Freshness guard: `broker.js quote` returned a frozen 16:00 ET IEX quote (`bid $0.59 x100 ask $0.00 x0`, 2 h old). Real SIP trades contradict it, so the zero ask is a stale artifact and does not trigger the illiquid skip (OLB Oct 8 precedent). The fill confirms a live book. Multi-session check: SIP daily closes were flat to down at $0.79 → $0.71 over Oct 6–13, with no session ≥+50%, and YYAI does not appear in `WINNERS_TRACKING.md`. That makes it a fresh day-1 igniter, so no MULTI-SESSION-RUNNER tag. Catalyst re-searched (2 searches this scan, 4 total): Benzinga's 17:06 ET AH movers list carries only the price move. Background items only: a 1-for-40 reverse split (May 14), a 1-for-20 reverse split (Aug 13), and a Nasdaq 10-K deficiency notice (Aug 28; plan due Oct 23). **Grade None**, entered with concern noted: no catalyst, serial reverse splits, and a pending compliance deadline. Bought 116 sh with a $0.88 limit; filled at **$0.82** (order eaba150d). Entry Total% is +15.8% vs the $0.708 prior close. The qualifying scan showed $0.84 / +18.2%, and the fill came in below it, so no CHASE-CAP.
  - Spike-bar: `YYAI 2026-10-14  SPIKE  16:19ET  +22%  $0.84  121 trades / 23k sh  (first co-spike bar) (as-of 18:00ET)`
  - Third-bar: `YYAI 2026-10-14  CONFIRM-3  YES ignition 17:30ET 3.5x; confirmed 17:40ET $0.84 as-of 18:00ET`
  - Volume context (`YYAI-1800-volume-metric.json`, source `YYAI-1800-volume-sip.json`):
    - `# YYAI shared SIP volume sip-ah-volume-v2; prior 2026-10-13 4+44zero/48 slots; floor 100; same-date regular peak 11250 sh; log-only`
    - `# reconstructed as-of 2026-10-14T22:00:55+00:00; source fetched 2026-10-14T22:00:56.219946+00:00`
    - Rows 16:15–16:45 ET match the 23:30 section.
    - `YYAI 2026-10-14  VOLUME-CONTEXT 16:50ET start=2026-10-14T20:50:00+00:00 shares=23423 local=0.4427x prior-peak=46.8460x rth-peak=2.0820x status=ok`
    - `YYAI 2026-10-14  VOLUME-CONTEXT 16:55ET start=2026-10-14T20:55:00+00:00 shares=8250 local=0.3522x prior-peak=16.5000x rth-peak=0.7333x status=ok`
    - `YYAI 2026-10-14  VOLUME-CONTEXT 17:00ET start=2026-10-14T21:00:00+00:00 shares=32629 local=1.5480x prior-peak=65.2580x rth-peak=2.9004x status=ok`
    - `YYAI 2026-10-14  VOLUME-CONTEXT 17:05ET start=2026-10-14T21:05:00+00:00 shares=8826 local=0.3768x prior-peak=17.6520x rth-peak=0.7845x status=ok`
    - `YYAI 2026-10-14  VOLUME-CONTEXT 17:10ET start=2026-10-14T21:10:00+00:00 shares=8632 local=0.9780x prior-peak=17.2640x rth-peak=0.7673x status=ok`
    - `YYAI 2026-10-14  VOLUME-CONTEXT 17:15ET start=2026-10-14T21:15:00+00:00 shares=10380 local=1.1761x prior-peak=20.7600x rth-peak=0.9227x status=ok`
    - `YYAI 2026-10-14  VOLUME-CONTEXT 17:20ET start=2026-10-14T21:20:00+00:00 shares=14970 local=1.6961x prior-peak=29.9400x rth-peak=1.3307x status=ok`
    - `YYAI 2026-10-14  VOLUME-CONTEXT 17:25ET start=2026-10-14T21:25:00+00:00 shares=13917 local=1.3408x prior-peak=27.8340x rth-peak=1.2371x status=ok`
    - `YYAI 2026-10-14  VOLUME-CONTEXT 17:30ET start=2026-10-14T21:30:00+00:00 shares=48293 local=3.4701x prior-peak=96.5860x rth-peak=4.2927x status=ok`
    - `YYAI 2026-10-14  VOLUME-CONTEXT 17:35ET start=2026-10-14T21:35:00+00:00 shares=126182 local=8.4290x prior-peak=252.3640x rth-peak=11.2162x status=ok`
    - `YYAI 2026-10-14  VOLUME-CONTEXT 17:40ET start=2026-10-14T21:40:00+00:00 shares=234086 local=4.8472x prior-peak=468.1720x rth-peak=20.8076x status=ok`
    - `YYAI 2026-10-14  VOLUME-CONTEXT 17:45ET start=2026-10-14T21:45:00+00:00 shares=113113 local=0.8964x prior-peak=226.2260x rth-peak=10.0545x status=ok`
    - Consumer verdict with the metric: `YYAI 2026-10-14  CONFIRM-3  YES ignition 17:30ET 3.5x; confirmed 17:40ET $0.84 as-of 18:00ET`
  - Book:
    - `YYAI BOOK iex bid $0.5942 x100 / ask $0.0000 x0 @ 2026-10-14 16:00:04 ET age 2h00m one-sided/empty`
    - `YYAI BOOK sip-15m bid $0.8502 x100 / ask $0.8530 x1000 @ 2026-10-14 17:45:40 ET age 15m00s two-sided spread 0.33% of ask`
    - `YYAI BOOK refresh +15s iex unchanged @ 2026-10-14 16:00:04 ET`
    - `YYAI BOOK verdict: IEX STALE 2h00m; SIP-15m TWO-SIDED (observed 2026-10-14 18:00:39 ET; log-only)`
- NCPL: **already entered** (45 sh @ $2.16, 23:00 CET); the broker shows the position and the filled buy, so no new order. Holding: the scanner shows $2.16 (+55.4% Total), and the delayed SIP book at 17:45 ET was $2.17 / $2.18, within ~4% of the $2.25 AH high. Volume is cooling to 76K–185K sh per bar since 17:20 ET, down from 295K–413K. The broker marks the position at $2.09 (−3.2%).
  - Spike-bar: `NCPL 2026-10-14  SPIKE  16:19ET  +29%  $2.05  2021 trades / 400k sh  (first co-spike bar) (as-of 18:00ET)`
  - Third-bar: `NCPL 2026-10-14  CONFIRM-3  NO ignition 16:20ET failed third-bar hold/volume as-of 18:00ET`
  - Volume context (`NCPL-1800-volume-metric.json`, source `NCPL-1800-volume-sip.json`):
    - `# NCPL shared SIP volume sip-ah-volume-v2; prior 2026-10-13 48+0zero/48 slots; floor 100; same-date regular peak 841121 sh; log-only`
    - `# reconstructed as-of 2026-10-14T22:00:57+00:00; source fetched 2026-10-14T22:00:58.248493+00:00`
    - Rows 16:00–17:15 ET match the 23:30 section.
    - `NCPL 2026-10-14  VOLUME-CONTEXT 17:20ET start=2026-10-14T21:20:00+00:00 shares=185277 local=0.6269x prior-peak=0.6154x rth-peak=0.2203x status=ok`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 17:25ET start=2026-10-14T21:25:00+00:00 shares=138638 local=0.4691x prior-peak=0.4605x rth-peak=0.1648x status=ok`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 17:30ET start=2026-10-14T21:30:00+00:00 shares=155156 local=0.8374x prior-peak=0.5153x rth-peak=0.1845x status=ok`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 17:35ET start=2026-10-14T21:35:00+00:00 shares=76125 local=0.4906x prior-peak=0.2528x rth-peak=0.0905x status=ok`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 17:40ET start=2026-10-14T21:40:00+00:00 shares=81651 local=0.5890x prior-peak=0.2712x rth-peak=0.0971x status=ok`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 17:45ET start=2026-10-14T21:45:00+00:00 shares=90896 local=1.1132x prior-peak=0.3019x rth-peak=0.1081x status=ok`
    - Consumer verdict with the metric: `NCPL 2026-10-14  CONFIRM-3  NO ignition 16:20ET failed third-bar hold/volume as-of 18:00ET`
  - Book:
    - `NCPL BOOK iex bid $2.16 x100 / ask $2.20 x100 @ 2026-10-14 16:59:34 ET age 1h01m two-sided spread 1.82% of ask`
    - `NCPL BOOK sip-15m bid $2.17 x1300 / ask $2.18 x2200 @ 2026-10-14 17:45:39 ET age 15m01s two-sided spread 0.46% of ask`
    - `NCPL BOOK refresh +15s iex unchanged @ 2026-10-14 16:59:34 ET`
    - `NCPL BOOK verdict: IEX STALE 1h01m; SIP-15m TWO-SIDED (observed 2026-10-14 18:00:39 ET; log-only)`
- SBNYL: untradable (carried). Second AH scan above 10% (+10.4%, an unchanged snapshot), so this is a qualified-but-untradable broker-block for the morning tally. No SIP or catalyst workup.
- JBDI: AH +10.0% displayed, but it is absent from the unrounded >10% list, so it is below 10%. Dead-cat in any case (Day% −26.8%). Not evaluated.
- GMEX, GENK, CLNE, CISS, AGMH, LUCD: AH below 10%. Not evaluated.

## Scan 00:30 CET (6:30 PM ET)

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $1.59 | +14.4% | +30.2% | $2.07 | +48.9% | 8.2M | 12.3M | 0.7x | 4.4M | Miscellaneous Commercial Services |
| YYAI | [TV](https://www.tradingview.com/chart/?symbol=YYAI) | $0.69 | -2.6% | +23.0% | $0.85 | +19.7% | 1.5M | 372K | 4.0x | 4.6M | Containers/Packaging |
| JBDI | [TV](https://www.tradingview.com/chart/?symbol=JBDI) | $2.51 | -26.8% | +34.3% | $3.37 | -1.8% | 1.1M | 9.7M | 0.1x | n/a | Wholesale Distributors |
| CLNE | [TV](https://www.tradingview.com/chart/?symbol=CLNE) | $1.35 | -5.6% | +7.4% | $1.45 | +1.4% | 307K | 949K | 0.3x | 161.1M | Gas Distributors |
| CISS | [TV](https://www.tradingview.com/chart/?symbol=CISS) | $0.53 | -15.5% | +11.3% | $0.59 | -5.9% | 252K | 1.1M | 0.2x | 1.5M | Marine Shipping |
| SBNYL | [TV](https://www.tradingview.com/chart/?symbol=SBNYL) | $1.25 | -0.8% | +10.4% | $1.38 | +9.5% | 180K | 40K | 4.5x | 59.6M | Regional Banks |
| FBGL | [TV](https://www.tradingview.com/chart/?symbol=FBGL) | $2.40 | -31.6% | +13.8% | $2.73 | -22.2% | 83K | 362K | 0.2x | n/a | Engineering & Construction |
| IBG | [TV](https://www.tradingview.com/chart/?symbol=IBG) | $0.82 | -6.6% | +19.1% | $0.98 | +11.2% | 500 | 15K | 0.0x | 3.8M | Beverages: Alcoholic |

Supplementary AH-change-only (>15%, not in volume pass): IBG

AH >10% at this snapshot (unrounded): CISS, FBGL, IBG, JBDI, NCPL, SBNYL, YYAI

**Evaluation notes:**

Final scheduled scan. No new entries: every new >10% name fails a gate (three dead-cats and one thin first-appearance name).

- NCPL: **already entered** (45 sh @ $2.16, 23:00 CET). Fading slowly: scanner $2.07 (+48.9% Total), delayed SIP book $2.03 / $2.04 at 18:16 ET, ~9% under the $2.25 AH high. Volume keeps cooling (36K–131K sh per bar since 17:50 ET). Broker mark $2.04 (−5.6%).
  - Spike-bar: `NCPL 2026-10-14  SPIKE  16:19ET  +29%  $2.05  2021 trades / 400k sh  (first co-spike bar) (as-of 18:30ET)`
  - Third-bar: `NCPL 2026-10-14  CONFIRM-3  NO ignition 16:20ET failed third-bar hold/volume as-of 18:30ET`
  - Volume context (`NCPL-1830-volume-metric.json`, source `NCPL-1830-volume-sip.json`):
    - `# NCPL shared SIP volume sip-ah-volume-v2; prior 2026-10-13 48+0zero/48 slots; floor 100; same-date regular peak 841121 sh; log-only`
    - `# reconstructed as-of 2026-10-14T22:30:10+00:00; source fetched 2026-10-14T22:30:47.900112+00:00`
    - Rows 16:00–17:45 ET match the 00:00 section.
    - `NCPL 2026-10-14  VOLUME-CONTEXT 17:50ET start=2026-10-14T21:50:00+00:00 shares=92980 local=1.1387x prior-peak=0.3088x rth-peak=0.1105x status=ok`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 17:55ET start=2026-10-14T21:55:00+00:00 shares=87481 local=0.9624x prior-peak=0.2905x rth-peak=0.1040x status=ok`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 18:00ET start=2026-10-14T22:00:00+00:00 shares=131138 local=1.4427x prior-peak=0.4355x rth-peak=0.1559x status=ok`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 18:05ET start=2026-10-14T22:05:00+00:00 shares=108698 local=1.1690x prior-peak=0.3610x rth-peak=0.1292x status=ok`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 18:10ET start=2026-10-14T22:10:00+00:00 shares=35814 local=0.3295x prior-peak=0.1189x rth-peak=0.0426x status=ok`
    - `NCPL 2026-10-14  VOLUME-CONTEXT 18:15ET start=2026-10-14T22:15:00+00:00 shares=74844 local=0.6885x prior-peak=0.2486x rth-peak=0.0890x status=ok`
    - Consumer verdict with the metric: `NCPL 2026-10-14  CONFIRM-3  NO ignition 16:20ET failed third-bar hold/volume as-of 18:30ET`
  - Book:
    - `NCPL BOOK iex bid $2.16 x100 / ask $2.20 x100 @ 2026-10-14 16:59:34 ET age 1h31m two-sided spread 1.82% of ask`
    - `NCPL BOOK sip-15m bid $2.03 x1100 / ask $2.04 x800 @ 2026-10-14 18:16:31 ET age 15m02s two-sided spread 0.49% of ask`
    - `NCPL BOOK refresh +15s iex unchanged @ 2026-10-14 16:59:34 ET`
    - `NCPL BOOK verdict: IEX STALE 1h31m; SIP-15m TWO-SIDED (observed 2026-10-14 18:31:32 ET; log-only)`
- YYAI: **already entered** (116 sh @ $0.82, 00:00 CET). Holding: scanner $0.85 (+19.7% Total), delayed SIP book $0.818 / $0.856 at 18:16 ET, ~11% under the $0.95 AH high. A 91K sh bar at 18:05 ET kept volume alive after the 17:40 high. Broker mark $0.81 (−0.9%).
  - Spike-bar: `YYAI 2026-10-14  SPIKE  16:19ET  +22%  $0.84  121 trades / 23k sh  (first co-spike bar) (as-of 18:30ET)`
  - Third-bar: `YYAI 2026-10-14  CONFIRM-3  YES ignition 17:30ET 3.5x; confirmed 17:40ET $0.84 as-of 18:30ET`
  - Volume context (`YYAI-1830-volume-metric.json`, source `YYAI-1830-volume-sip.json`):
    - `# YYAI shared SIP volume sip-ah-volume-v2; prior 2026-10-13 4+44zero/48 slots; floor 100; same-date regular peak 11250 sh; log-only`
    - `# reconstructed as-of 2026-10-14T22:30:10+00:00; source fetched 2026-10-14T22:30:48.551950+00:00`
    - Rows 16:15–17:45 ET match the 00:00 section.
    - `YYAI 2026-10-14  VOLUME-CONTEXT 17:50ET start=2026-10-14T21:50:00+00:00 shares=51307 local=0.4066x prior-peak=102.6140x rth-peak=4.5606x status=ok`
    - `YYAI 2026-10-14  VOLUME-CONTEXT 17:55ET start=2026-10-14T21:55:00+00:00 shares=32748 local=0.2895x prior-peak=65.4960x rth-peak=2.9109x status=ok`
    - `YYAI 2026-10-14  VOLUME-CONTEXT 18:00ET start=2026-10-14T22:00:00+00:00 shares=32629 local=0.6360x prior-peak=65.2580x rth-peak=2.9004x status=ok`
    - `YYAI 2026-10-14  VOLUME-CONTEXT 18:05ET start=2026-10-14T22:05:00+00:00 shares=91689 local=2.7998x prior-peak=183.3780x rth-peak=8.1501x status=ok`
    - `YYAI 2026-10-14  VOLUME-CONTEXT 18:10ET start=2026-10-14T22:10:00+00:00 shares=55130 local=1.6835x prior-peak=110.2600x rth-peak=4.9004x status=ok`
    - `YYAI 2026-10-14  VOLUME-CONTEXT 18:15ET start=2026-10-14T22:15:00+00:00 shares=23336 local=0.4233x prior-peak=46.6720x rth-peak=2.0743x status=ok`
    - Consumer verdict with the metric: `YYAI 2026-10-14  CONFIRM-3  YES ignition 17:30ET 3.5x; confirmed 17:40ET $0.84 as-of 18:30ET`
  - Book:
    - `YYAI BOOK iex bid $0.5942 x100 / ask $0.0000 x0 @ 2026-10-14 16:00:04 ET age 2h31m one-sided/empty`
    - `YYAI BOOK sip-15m bid $0.8181 x300 / ask $0.8564 x100 @ 2026-10-14 18:16:30 ET age 15m03s two-sided spread 4.47% of ask`
    - `YYAI BOOK refresh +15s iex unchanged @ 2026-10-14 16:00:04 ET`
    - `YYAI BOOK verdict: IEX STALE 2h31m; SIP-15m TWO-SIDED (observed 2026-10-14 18:31:32 ET; log-only)`
- JBDI: **Skip: dead-cat** (Day% −26.8%). **DEAD-CAT-OVERRIDE WATCH (borderline)**, hypothetical entry **$3.37 @ 00:30 CET (18:30 ET)**. `tradable=true`. It is the first unrounded >10% AH scan (00:00 showed +10.0% but was absent from the unrounded list), so it also fails the 2-AH-scan gate. Day% below −15% rules out a FINAL-SCAN-GATE-BLOCK note. SIP shows a real late ignition: flat at $2.74–2.77 until 17:45 ET, then 77K → 277K → 308K → 295K sh per bar (453 → 2,727 → 2,874 → 3,118 trades), VWAP $2.88 → $3.60, AH high **$3.80** in the 18:00 bar. That briefly reclaimed above the $3.43 Oct 13 close (+10.8%); the latest SIP bar (18:15 ET) closed $3.44, back at that close, on 136K–158K sh per bar. AH% rose +10.0% → +34.3% across the last two scans. Reclaim is marginal, so the watch is logged as borderline. **MULTI-SESSION-RUNNER**: day 2, Oct 13 ran $1.00 → $3.43 (+243%, high $9.50) on 92.6M sh, then today faded to $2.51. Catalyst (2 searches): no fresh item; StocksToTrade/Sykes Oct 14 morning pieces cover the breakout and "regulatory probe" headlines; background only: Sep 29 ZYMIX $900M convertible-note acquisition and an October extraordinary meeting. **Grade None.**
  - Spike-bar: `JBDI 2026-10-14  SPIKE  17:49ET  +25%  $3.13  339 trades / 36k sh  (first co-spike bar) (as-of 18:30ET)`
  - Third-bar: `JBDI 2026-10-14  CONFIRM-3  YES ignition 17:45ET 12.3x; confirmed 17:55ET $3.77 as-of 18:30ET`
  - Volume context (`JBDI-1830-volume-metric.json`, source `JBDI-1830-volume-sip.json`):
    - `# JBDI shared SIP volume sip-ah-volume-v2; prior 2026-10-13 48+0zero/48 slots; floor 100; same-date regular peak 248075 sh; log-only`
    - `# reconstructed as-of 2026-10-14T22:30:10+00:00; source fetched 2026-10-14T22:30:49.248476+00:00`
    - `JBDI 2026-10-14  VOLUME-CONTEXT 16:00ET start=2026-10-14T20:00:00+00:00 shares=7293 local=unknown prior-peak=0.0157x rth-peak=0.0294x status=warmup`
    - `JBDI 2026-10-14  VOLUME-CONTEXT 16:05ET start=2026-10-14T20:05:00+00:00 shares=7635 local=unknown prior-peak=0.0165x rth-peak=0.0308x status=warmup`
    - `JBDI 2026-10-14  VOLUME-CONTEXT 16:10ET start=2026-10-14T20:10:00+00:00 shares=6448 local=unknown prior-peak=0.0139x rth-peak=0.0260x status=warmup`
    - `JBDI 2026-10-14  VOLUME-CONTEXT 16:15ET start=2026-10-14T20:15:00+00:00 shares=3414 local=0.4681x prior-peak=0.0074x rth-peak=0.0138x status=ok`
    - `JBDI 2026-10-14  VOLUME-CONTEXT 16:20ET start=2026-10-14T20:20:00+00:00 shares=2566 local=0.3980x prior-peak=0.0055x rth-peak=0.0103x status=ok`
    - `JBDI 2026-10-14  VOLUME-CONTEXT 16:25ET start=2026-10-14T20:25:00+00:00 shares=4456 local=1.3052x prior-peak=0.0096x rth-peak=0.0180x status=ok`
    - `JBDI 2026-10-14  VOLUME-CONTEXT 16:30ET start=2026-10-14T20:30:00+00:00 shares=8481 local=2.4842x prior-peak=0.0183x rth-peak=0.0342x status=ok`
    - `JBDI 2026-10-14  VOLUME-CONTEXT 16:35ET start=2026-10-14T20:35:00+00:00 shares=925 local=0.2076x prior-peak=0.0020x rth-peak=0.0037x status=ok`
    - `JBDI 2026-10-14  VOLUME-CONTEXT 16:40ET start=2026-10-14T20:40:00+00:00 shares=942 local=0.2114x prior-peak=0.0020x rth-peak=0.0038x status=ok`
    - `JBDI 2026-10-14  VOLUME-CONTEXT 16:45ET start=2026-10-14T20:45:00+00:00 shares=3752 local=3.9830x prior-peak=0.0081x rth-peak=0.0151x status=ok`
    - `JBDI 2026-10-14  VOLUME-CONTEXT 16:50ET start=2026-10-14T20:50:00+00:00 shares=1073 local=1.1391x prior-peak=0.0023x rth-peak=0.0043x status=ok`
    - `JBDI 2026-10-14  VOLUME-CONTEXT 16:55ET start=2026-10-14T20:55:00+00:00 shares=901 local=0.8397x prior-peak=0.0019x rth-peak=0.0036x status=ok`
    - `JBDI 2026-10-14  VOLUME-CONTEXT 17:00ET start=2026-10-14T21:00:00+00:00 shares=1452 local=1.3532x prior-peak=0.0031x rth-peak=0.0059x status=ok`
    - `JBDI 2026-10-14  VOLUME-CONTEXT 17:05ET start=2026-10-14T21:05:00+00:00 shares=1428 local=1.3308x prior-peak=0.0031x rth-peak=0.0058x status=ok`
    - `JBDI 2026-10-14  VOLUME-CONTEXT 17:10ET start=2026-10-14T21:10:00+00:00 shares=198 local=0.1387x prior-peak=0.0004x rth-peak=0.0008x status=ok`
    - `JBDI 2026-10-14  VOLUME-CONTEXT 17:15ET start=2026-10-14T21:15:00+00:00 shares=1763 local=1.2346x prior-peak=0.0038x rth-peak=0.0071x status=ok`
    - `JBDI 2026-10-14  VOLUME-CONTEXT 17:20ET start=2026-10-14T21:20:00+00:00 shares=1985 local=1.3901x prior-peak=0.0043x rth-peak=0.0080x status=ok`
    - `JBDI 2026-10-14  VOLUME-CONTEXT 17:25ET start=2026-10-14T21:25:00+00:00 shares=11912 local=6.7567x prior-peak=0.0257x rth-peak=0.0480x status=ok`
    - `JBDI 2026-10-14  VOLUME-CONTEXT 17:30ET start=2026-10-14T21:30:00+00:00 shares=6301 local=3.1743x prior-peak=0.0136x rth-peak=0.0254x status=ok`
    - `JBDI 2026-10-14  VOLUME-CONTEXT 17:35ET start=2026-10-14T21:35:00+00:00 shares=22736 local=3.6083x prior-peak=0.0490x rth-peak=0.0916x status=ok`
    - `JBDI 2026-10-14  VOLUME-CONTEXT 17:40ET start=2026-10-14T21:40:00+00:00 shares=2823 local=0.2370x prior-peak=0.0061x rth-peak=0.0114x status=ok`
    - `JBDI 2026-10-14  VOLUME-CONTEXT 17:45ET start=2026-10-14T21:45:00+00:00 shares=77595 local=12.3147x prior-peak=0.1672x rth-peak=0.3128x status=ok`
    - `JBDI 2026-10-14  VOLUME-CONTEXT 17:50ET start=2026-10-14T21:50:00+00:00 shares=276881 local=12.1781x prior-peak=0.5967x rth-peak=1.1161x status=ok`
    - `JBDI 2026-10-14  VOLUME-CONTEXT 17:55ET start=2026-10-14T21:55:00+00:00 shares=308126 local=3.9710x prior-peak=0.6640x rth-peak=1.2421x status=ok`
    - `JBDI 2026-10-14  VOLUME-CONTEXT 18:00ET start=2026-10-14T22:00:00+00:00 shares=295226 local=1.0663x prior-peak=0.6362x rth-peak=1.1901x status=ok`
    - `JBDI 2026-10-14  VOLUME-CONTEXT 18:05ET start=2026-10-14T22:05:00+00:00 shares=136234 local=0.4615x prior-peak=0.2936x rth-peak=0.5492x status=ok`
    - `JBDI 2026-10-14  VOLUME-CONTEXT 18:10ET start=2026-10-14T22:10:00+00:00 shares=147578 local=0.4999x prior-peak=0.3180x rth-peak=0.5949x status=ok`
    - `JBDI 2026-10-14  VOLUME-CONTEXT 18:15ET start=2026-10-14T22:15:00+00:00 shares=158051 local=1.0710x prior-peak=0.3406x rth-peak=0.6371x status=ok`
    - Consumer verdict with the metric: `JBDI 2026-10-14  CONFIRM-3  YES ignition 17:45ET 12.3x; confirmed 17:55ET $3.77 as-of 18:30ET`
  - Book:
    - `JBDI BOOK iex bid $2.12 x100 / ask $0.0000 x0 @ 2026-10-14 16:00:03 ET age 2h31m one-sided/empty`
    - `JBDI BOOK sip-15m bid $3.51 x400 / ask $3.54 x200 @ 2026-10-14 18:16:32 ET age 15m00s two-sided spread 0.85% of ask`
    - `JBDI BOOK refresh +15s iex unchanged @ 2026-10-14 16:00:03 ET`
    - `JBDI BOOK verdict: IEX STALE 2h31m; SIP-15m TWO-SIDED (observed 2026-10-14 18:31:32 ET; log-only)`
- CISS: **Skip: dead-cat** (Day% −15.5%, Total −5.9%, still below the prior close) and first >10% AH scan. `tradable=true`. SIP is thin: the 16:45–16:50 ET bars carried 53K–60K sh, then single-digit-K bars or less; no accumulation, so no book check. Catalyst (1 search): none fresh; background reverse split and $6.0M offering. Grade None.
  - Spike-bar: `CISS 2026-10-14  SPIKE  16:48ET  +17%  $0.62  129 trades / 18k sh  (first co-spike bar) (as-of 18:30ET)`
  - Third-bar: `CISS 2026-10-14  CONFIRM-3  NO no local-volume new-high ignition as-of 18:30ET`
  - Volume context (`CISS-1830-volume-metric.json`, source `CISS-1830-volume-sip.json`):
    - `# CISS shared SIP volume sip-ah-volume-v2; prior 2026-10-13 19+29zero/48 slots; floor 100; same-date regular peak 45550 sh; log-only`
    - `# reconstructed as-of 2026-10-14T22:30:10+00:00; source fetched 2026-10-14T22:30:49.907638+00:00`
    - `CISS 2026-10-14  VOLUME-CONTEXT 16:00ET start=2026-10-14T20:00:00+00:00 shares=4630 local=unknown prior-peak=0.3415x rth-peak=0.1016x status=warmup`
    - `CISS 2026-10-14  VOLUME-CONTEXT 16:20ET start=2026-10-14T20:20:00+00:00 shares=1101 local=11.0100x prior-peak=0.0812x rth-peak=0.0242x status=floored`
    - `CISS 2026-10-14  VOLUME-CONTEXT 16:25ET start=2026-10-14T20:25:00+00:00 shares=12290 local=122.9000x prior-peak=0.9065x rth-peak=0.2698x status=floored`
    - `CISS 2026-10-14  VOLUME-CONTEXT 16:30ET start=2026-10-14T20:30:00+00:00 shares=39330 local=35.7221x prior-peak=2.9009x rth-peak=0.8634x status=ok`
    - `CISS 2026-10-14  VOLUME-CONTEXT 16:35ET start=2026-10-14T20:35:00+00:00 shares=35894 local=2.9206x prior-peak=2.6474x rth-peak=0.7880x status=ok`
    - `CISS 2026-10-14  VOLUME-CONTEXT 16:40ET start=2026-10-14T20:40:00+00:00 shares=12833 local=0.3575x prior-peak=0.9465x rth-peak=0.2817x status=ok`
    - `CISS 2026-10-14  VOLUME-CONTEXT 16:45ET start=2026-10-14T20:45:00+00:00 shares=60122 local=1.6750x prior-peak=4.4344x rth-peak=1.3199x status=ok`
    - `CISS 2026-10-14  VOLUME-CONTEXT 16:50ET start=2026-10-14T20:50:00+00:00 shares=52996 local=1.4765x prior-peak=3.9088x rth-peak=1.1635x status=ok`
    - `CISS 2026-10-14  VOLUME-CONTEXT 16:55ET start=2026-10-14T20:55:00+00:00 shares=7998 local=0.1509x prior-peak=0.5899x rth-peak=0.1756x status=ok`
    - `CISS 2026-10-14  VOLUME-CONTEXT 17:00ET start=2026-10-14T21:00:00+00:00 shares=8394 local=0.1584x prior-peak=0.6191x rth-peak=0.1843x status=ok`
    - `CISS 2026-10-14  VOLUME-CONTEXT 17:05ET start=2026-10-14T21:05:00+00:00 shares=4855 local=0.5784x prior-peak=0.3581x rth-peak=0.1066x status=ok`
    - `CISS 2026-10-14  VOLUME-CONTEXT 17:10ET start=2026-10-14T21:10:00+00:00 shares=7903 local=0.9881x prior-peak=0.5829x rth-peak=0.1735x status=ok`
    - `CISS 2026-10-14  VOLUME-CONTEXT 17:15ET start=2026-10-14T21:15:00+00:00 shares=555 local=0.0702x prior-peak=0.0409x rth-peak=0.0122x status=ok`
    - `CISS 2026-10-14  VOLUME-CONTEXT 17:20ET start=2026-10-14T21:20:00+00:00 shares=1596 local=0.3287x prior-peak=0.1177x rth-peak=0.0350x status=ok`
    - `CISS 2026-10-14  VOLUME-CONTEXT 17:25ET start=2026-10-14T21:25:00+00:00 shares=2011 local=1.2600x prior-peak=0.1483x rth-peak=0.0441x status=ok`
    - `CISS 2026-10-14  VOLUME-CONTEXT 17:30ET start=2026-10-14T21:30:00+00:00 shares=615 local=0.3853x prior-peak=0.0454x rth-peak=0.0135x status=ok`
    - `CISS 2026-10-14  VOLUME-CONTEXT 17:35ET start=2026-10-14T21:35:00+00:00 shares=8643 local=5.4154x prior-peak=0.6375x rth-peak=0.1897x status=ok`
    - `CISS 2026-10-14  VOLUME-CONTEXT 17:40ET start=2026-10-14T21:40:00+00:00 shares=797 local=0.3963x prior-peak=0.0588x rth-peak=0.0175x status=ok`
    - `CISS 2026-10-14  VOLUME-CONTEXT 17:45ET start=2026-10-14T21:45:00+00:00 shares=1951 local=2.4479x prior-peak=0.1439x rth-peak=0.0428x status=ok`
    - `CISS 2026-10-14  VOLUME-CONTEXT 17:50ET start=2026-10-14T21:50:00+00:00 shares=1861 local=0.9539x prior-peak=0.1373x rth-peak=0.0409x status=ok`
    - `CISS 2026-10-14  VOLUME-CONTEXT 17:55ET start=2026-10-14T21:55:00+00:00 shares=1655 local=0.8893x prior-peak=0.1221x rth-peak=0.0363x status=ok`
    - `CISS 2026-10-14  VOLUME-CONTEXT 18:00ET start=2026-10-14T22:00:00+00:00 shares=896 local=0.4815x prior-peak=0.0661x rth-peak=0.0197x status=ok`
    - `CISS 2026-10-14  VOLUME-CONTEXT 18:10ET start=2026-10-14T22:10:00+00:00 shares=880 local=0.9821x prior-peak=0.0649x rth-peak=0.0193x status=ok`
    - `CISS 2026-10-14  VOLUME-CONTEXT 18:15ET start=2026-10-14T22:15:00+00:00 shares=354 local=0.4023x prior-peak=0.0261x rth-peak=0.0078x status=ok`
- FBGL: **Skip: dead-cat** (Day% −31.6%, Total −22.2%) and first >10% AH scan. `tradable=true`. SIP is thin: largest bars 36K sh (16:10 ET) and 16K sh (17:55 ET), mostly hundreds to low thousands; no book check. Catalyst (1 search): FBS Global regained Nasdaq minimum bid-price compliance (GlobeNewswire via Manila Times, dated Oct 14, release time not verified; confirmation letter Oct 12). **Grade C.**
  - Spike-bar: `FBGL 2026-10-14  SPIKE  16:12ET  +18%  $2.84  145 trades / 10k sh  (first co-spike bar) (as-of 18:30ET)`
  - Third-bar: `FBGL 2026-10-14  CONFIRM-3  NO no local-volume new-high ignition as-of 18:30ET`
  - Volume context (`FBGL-1830-volume-metric.json`, source `FBGL-1830-volume-sip.json`):
    - `# FBGL shared SIP volume sip-ah-volume-v2; prior 2026-10-13 45+3zero/48 slots; floor 100; same-date regular peak 17453 sh; log-only`
    - `# reconstructed as-of 2026-10-14T22:30:10+00:00; source fetched 2026-10-14T22:30:50.675855+00:00`
    - `FBGL 2026-10-14  VOLUME-CONTEXT 16:00ET start=2026-10-14T20:00:00+00:00 shares=2548 local=unknown prior-peak=0.0039x rth-peak=0.1460x status=warmup`
    - `FBGL 2026-10-14  VOLUME-CONTEXT 16:05ET start=2026-10-14T20:05:00+00:00 shares=1023 local=unknown prior-peak=0.0016x rth-peak=0.0586x status=warmup`
    - `FBGL 2026-10-14  VOLUME-CONTEXT 16:10ET start=2026-10-14T20:10:00+00:00 shares=36490 local=unknown prior-peak=0.0561x rth-peak=2.0908x status=warmup`
    - `FBGL 2026-10-14  VOLUME-CONTEXT 16:15ET start=2026-10-14T20:15:00+00:00 shares=11208 local=4.3987x prior-peak=0.0172x rth-peak=0.6422x status=ok`
    - `FBGL 2026-10-14  VOLUME-CONTEXT 16:20ET start=2026-10-14T20:20:00+00:00 shares=2086 local=0.1861x prior-peak=0.0032x rth-peak=0.1195x status=ok`
    - `FBGL 2026-10-14  VOLUME-CONTEXT 16:25ET start=2026-10-14T20:25:00+00:00 shares=402 local=0.0359x prior-peak=0.0006x rth-peak=0.0230x status=ok`
    - `FBGL 2026-10-14  VOLUME-CONTEXT 16:30ET start=2026-10-14T20:30:00+00:00 shares=337 local=0.1616x prior-peak=0.0005x rth-peak=0.0193x status=ok`
    - `FBGL 2026-10-14  VOLUME-CONTEXT 16:40ET start=2026-10-14T20:40:00+00:00 shares=827 local=2.4540x prior-peak=0.0013x rth-peak=0.0474x status=ok`
    - `FBGL 2026-10-14  VOLUME-CONTEXT 16:45ET start=2026-10-14T20:45:00+00:00 shares=1060 local=3.1454x prior-peak=0.0016x rth-peak=0.0607x status=ok`
    - `FBGL 2026-10-14  VOLUME-CONTEXT 16:50ET start=2026-10-14T20:50:00+00:00 shares=783 local=0.9468x prior-peak=0.0012x rth-peak=0.0449x status=ok`
    - `FBGL 2026-10-14  VOLUME-CONTEXT 16:55ET start=2026-10-14T20:55:00+00:00 shares=6191 local=7.4861x prior-peak=0.0095x rth-peak=0.3547x status=ok`
    - `FBGL 2026-10-14  VOLUME-CONTEXT 17:00ET start=2026-10-14T21:00:00+00:00 shares=3117 local=2.9406x prior-peak=0.0048x rth-peak=0.1786x status=ok`
    - `FBGL 2026-10-14  VOLUME-CONTEXT 17:05ET start=2026-10-14T21:05:00+00:00 shares=8429 local=2.7042x prior-peak=0.0130x rth-peak=0.4830x status=ok`
    - `FBGL 2026-10-14  VOLUME-CONTEXT 17:10ET start=2026-10-14T21:10:00+00:00 shares=1380 local=0.2229x prior-peak=0.0021x rth-peak=0.0791x status=ok`
    - `FBGL 2026-10-14  VOLUME-CONTEXT 17:15ET start=2026-10-14T21:15:00+00:00 shares=2156 local=0.6917x prior-peak=0.0033x rth-peak=0.1235x status=ok`
    - `FBGL 2026-10-14  VOLUME-CONTEXT 17:20ET start=2026-10-14T21:20:00+00:00 shares=748 local=0.3469x prior-peak=0.0012x rth-peak=0.0429x status=ok`
    - `FBGL 2026-10-14  VOLUME-CONTEXT 17:25ET start=2026-10-14T21:25:00+00:00 shares=311 local=0.2254x prior-peak=0.0005x rth-peak=0.0178x status=ok`
    - `FBGL 2026-10-14  VOLUME-CONTEXT 17:40ET start=2026-10-14T21:40:00+00:00 shares=476 local=4.7600x prior-peak=0.0007x rth-peak=0.0273x status=floored`
    - `FBGL 2026-10-14  VOLUME-CONTEXT 17:45ET start=2026-10-14T21:45:00+00:00 shares=522 local=5.2200x prior-peak=0.0008x rth-peak=0.0299x status=floored`
    - `FBGL 2026-10-14  VOLUME-CONTEXT 17:55ET start=2026-10-14T21:55:00+00:00 shares=15633 local=32.8424x prior-peak=0.0240x rth-peak=0.8957x status=ok`
    - `FBGL 2026-10-14  VOLUME-CONTEXT 18:00ET start=2026-10-14T22:00:00+00:00 shares=4561 local=8.7375x prior-peak=0.0070x rth-peak=0.2613x status=ok`
    - `FBGL 2026-10-14  VOLUME-CONTEXT 18:05ET start=2026-10-14T22:05:00+00:00 shares=2293 local=0.5027x prior-peak=0.0035x rth-peak=0.1314x status=ok`
    - `FBGL 2026-10-14  VOLUME-CONTEXT 18:10ET start=2026-10-14T22:10:00+00:00 shares=2443 local=0.5356x prior-peak=0.0038x rth-peak=0.1400x status=ok`
    - `FBGL 2026-10-14  VOLUME-CONTEXT 18:15ET start=2026-10-14T22:15:00+00:00 shares=151 local=0.0618x prior-peak=0.0002x rth-peak=0.0087x status=ok`
- IBG: **Skip: stale VRatio / thin.** First AH appearance (supplementary change-only pass), Day% −6.6%. `tradable=true`. SIP shows a single 18:00 ET bar of 510 sh / 4 trades at $0.98; no accumulation, so no FINAL-SCAN-GATE-BLOCK note and no book check. Catalyst (1 search): none found; background Nasdaq extension deadline Nov 11. Grade None.
  - Spike-bar: `IBG 2026-10-14  NO-SPIKE  peak +20% @18:00ET  (no bar cleared +15% on a volume co-spike) (as-of 18:30ET)`
  - Third-bar: `IBG 2026-10-14  CONFIRM-3  NO no local-volume new-high ignition as-of 18:30ET`
  - Volume context (`IBG-1830-volume-metric.json`, source `IBG-1830-volume-sip.json`):
    - `# IBG shared SIP volume sip-ah-volume-v2; prior 2026-10-13 0+48zero/48 slots; floor 100; same-date regular peak 5000 sh; log-only`
    - `# reconstructed as-of 2026-10-14T22:30:10+00:00; source fetched 2026-10-14T22:30:51.230380+00:00`
    - `IBG 2026-10-14  VOLUME-CONTEXT 18:00ET start=2026-10-14T22:00:00+00:00 shares=510 local=5.1000x prior-peak=5.1000x rth-peak=0.1020x status=floored`
- SBNYL: untradable (carried). Unchanged snapshot (+10.4%). Spike-bar: `SBNYL 2026-10-14: NO prior-close (daily bar missing)`; third-bar: `SBNYL 2026-10-14  CONFIRM-3  NO-DATA prior close unavailable`.
- CLNE: AH below 10%. Not evaluated.
- Final-scan feed-lag cross-check (SIP last bar vs. Oct 14 regular close): none of the tracked names is above 10% AH. GLND −6.2%, NXGL −5.7% (AH high $6.34), TDIC −12.7%, MXCT +0.8%, BOXL −2.7%, MWYN −0.5%, GENK +4.7%, GRML +0.2%, FMFC 0.0%, KMRK 0.0%, DFNS −5.3%, TCRT +4.3%, TRUG +0.7% (AH high $1.74), SDEV +4.0%, GMEX +3.5%; CCG and GAUZ have no AH bars. Nothing to rescue.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
| NCPL | $2.16 | 23:00 CET (17:00 ET) | 45 | 529b8e3a-fefd-418e-a890-521863b1f423 | Grade C (Nasdaq compliance PR); AH BUILD with new highs on 276K–517K sh/bar; float 4.4M; Total +55.4% |
| YYAI | $0.82 | 00:00 CET (18:00 ET) | 116 | eaba150d-b33d-4dd6-9bd7-e8cfe6435c39 | Grade None (no fresh catalyst); second AH ignition 17:30 ET to $0.95 on 126K–234K sh/bar, CONFIRM-3 YES; float 4.6M; Total +15.8% |

## Morning Evaluation — 10:20 CEST (04:20 ET, October 15)

**Pulse 1: no real winner today.** Nothing in the scan universe cleared +100%. The biggest genuine AH→PM mover is **JBDI** at +51.4% AH / +42.6% PM. The only >100% name is **GP** (+394% SIP high), a sub-$0.50 PM-only gapper with no AH footprint. Both overnight entries are under water: NCPL −10.1% and YYAI −17.6%. Exits belong to the 10:30 position pulse.

Discovery ran before reading this log: `scan.py --all --session premarket` at 04:20 ET found only JBDI +23.5% and NCPL +20.1%. `pm-sweep.py` returned 14 listed names above +10%: GP, SDST, HCAI, SHFS and PPCB are below $0.50, JBDI and NCPL are in-universe, and the rest are thin prints (BIVI 383 sh, RDI 614, BBCI 100, VTIX 150, YCBD 100, CLRB 100) plus WFF (−91.7% crash day). Levels are Alpaca SIP daily closes and 5-minute bars. SIP PM bars end at the 04:05 ET bar, so later PM is unassessed here. Yahoo did serve last night's AH bars this morning, and they match the SIP shape.

### Today's Winner

**No real winner today.** The largest moves are below +100%, below the $0.50 floor, or PM-only:

- **JBDI** (scanner industry Wholesale Distributors), the biggest genuine in-universe mover. Previous close **$2.51** (SIP, Oct 14; Day −26.8% after Oct 13's $1.00 → $3.43 run on 92.6M sh). AH ignition at 17:45 ET, **AH SIP high $3.80 (+51.4%) at 18:00 ET** on 295K sh / 3,118 trades. **PM SIP high $3.58 (+42.6%) at 04:00 ET** on 366K sh / 5,823 trades; 04:05 close $3.24, Yahoo $2.99 at 04:23. That is below the bar on %, and against the previous day it is no spike: Oct 14's largest regular-session 5m bar was 248K (`rth_peak_shares`), the AH peak bars ran 1.1–1.2x that, and Oct 13 traded 92.6M sh. Catalyst **None** (scan searches: only breakout/"regulatory probe" commentary). Float n/a, market cap ~$24M.
- **GP** (GreenPower Motor, electric buses). Close **$0.273**. AH: 4 trades, 1,046 shares total. The 04:00 ET bar ran to **$1.35 (+394%)** on 4.91M sh / 16,327 trades but closed $0.55 (VWAP $0.68); 04:05 H $0.63 C $0.63 on 3.05M sh. PM-only gapper below the price floor. Catalyst **None** found (1 search; Oct 5 Newsfile release is background).
- **HCAI** (Huachen AI, industrial machinery). Close **$0.2792**. Ignited 17:40 ET to **$0.53 (+89.8%) at 17:45 ET** on 2.08M sh / 4,432 trades and sat near $0.46 at the 18:30 ET final scan. PM SIP high $0.44 (+57.6%) at 04:00 on 4.13M sh, then Yahoo $0.25 (−11.7%) by 04:23. Below the bar and below the $0.50 floor.

**Scanner Diagnostic (biggest genuine mover, JBDI):**

- Detectable at screening time (~22:15 CEST)? **NO** at 22:15: JBDI sat at $2.26–2.40 (−4% to −10% AH) until 17:40 ET. **YES** from the 00:30 CEST final scan ($3.37, +34.3% AH); the 00:00 scan showed +10.0% rounded, below the unrounded 10% line.
- Acted on: skipped as a dead-cat (Day −26.8%) and logged as a borderline DEAD-CAT-OVERRIDE WATCH at $3.37. Hypothetical $3.37 → PM SIP $3.58 = **+6.2%**, next bar close $3.24 below the entry.
- Scanner gap: **none.** JBDI was detected in the only window where it moved, and the skip cost little.

### Baseline Tracking

Source: the October 13 log (Days tracked 99, detected 75/86, selected 39/82). The October 13 log is the immediately preceding trading day, so no new baseline gap. Existing gaps stay **Sep 11, Sep 18, Sep 25, Oct 2, Oct 9**.

- Days tracked: **100** (99 + October 14 only).
- Winners detected by scanner: **75/86 (87.2%)**, unchanged. No winner today, so nothing enters the denominator.
- Winner selected for paper trade: **39/82 (47.6%)**, unchanged.
- Target: >80% detection. Status: **BASELINE MET.** Coverage failures, five skipped retrospectives and the price-floor exclusions limit what the rate means.

### Retrospective Scan Results

`scan.py --all --session premarket` (04:20 ET): JBDI +23.5%, NCPL +20.1%. `pm-sweep.py` (04:20 ET): GP +101.5%, SDST +71.5%, HCAI +29.9%, SHFS +24.0%, JBDI, NCPL, PPCB +14.3% (2,652 sh), WFF +10.1%, and thin prints. No forced AH scan was run.

| Ticker | Oct 14 SIP close | AH SIP high / ET | PM SIP high / ET | PM high vs close | Peak-bar shares / trades | Latest | Classification |
|--------|-----------------|------------------|------------------|------------------|--------------------------|--------|----------------|
| GP | $0.273 | $0.28 / 16:05 (1,046 AH sh) | $1.35 / 04:00 | +394% | 4,909,458 / 16,327 | $0.55 (Yahoo 04:23) | PM-only gapper; sub-$0.50; single-wick peak |
| JBDI | $2.51 | $3.80 / 18:00 | $3.58 / 04:00 | +42.6% | 366,076 / 5,823 | $2.99 (Yahoo 04:23) | Biggest genuine mover; detected at final scan; dead-cat skip |
| HCAI | $0.2792 | $0.53 / 17:45 | $0.44 / 04:00 | +57.6% | 4,133,611 / 15,927 | $0.25 (Yahoo 04:23) | Price-floor exclusion (in-window AH); AH better |
| SHFS | $0.23 | $0.33 / 19:10 | $0.34 / 04:00 | +47.8% | 4,326,965 / 20,168 | $0.27 (04:05 C) | Sub-$0.50; ignited 18:50 ET, after the final scan |
| NCPL | $1.59 | $2.25 / 17:10 | $1.97 / 04:00 | +23.9% | 165,354 / 1,606 | $1.94 (Yahoo 04:23) | Detected, entered; AH better |
| YYAI | $0.69 | $1.01 / 19:35 | $0.87 / 04:00 | +25.9% | 420,875 / 3,550 | $0.69 (Yahoo 04:22) | Detected, entered; late-tail AH high, PM gap-down |
| SDST | $0.03 | $0.05 / 19:00 | $0.06 / 04:00 | ~+70% | 95,143,254 / 50,085 | $0.04 | Sub-$0.05 penny; ignored |

### Open Position P&L (Alpaca)

`broker.js positions`: NCPL 45 @ $2.16 now $1.94, YYAI 116 @ $0.82 now $0.68. The `quote` endpoint is stale (NCPL 16:59 ET, YYAI 16:00 ET with `ask $0.00 x0`), but the positions prices match the SIP 04:05 ET closes ($1.92, $0.68) and Yahoo 04:22–04:23 prints ($1.94, $0.69), so they are live, not the prior close.

| Ticker | Entry | Entry Total% | Catalyst | Entry Time | PM Peak | Peak Time | Exit | P&L | P&L % | Status |
|--------|-------|--------------|----------|------------|---------|-----------|------|-----|-------|--------|
| NCPL | $2.16 | +55.4% (vs $1.39 Oct 13) | C — Nasdaq bid-price compliance | 23:00 CEST (17:00 ET) | $1.97 (SIP; Yahoo 04:10 close $2.02) | 04:00 ET | open | −$9.85 | −10.1% | ❌ Open, PM never reclaimed fill |
| YYAI | $0.82 | +15.8% (vs $0.708 Oct 13) | None — no catalyst found | 00:00 CEST (18:00 ET) | $0.87 (SIP) | 04:00 ET | open | −$16.76 | −17.6% | ❌ Open, below fill after +6.1% open pop |

**Total Realized P&L (Alpaca fills only, this session): $0.00** (unrealized −$26.61).

### Scanner Effectiveness

- Evening scans ran: **7 of 7** scheduled checkpoints (21:30, 22:00, 22:30, 23:00, 23:30, 00:00, 00:30 CEST), plus extra observations at 22:05–22:25 and 22:45. The entry window was fully covered.
- Candidates found: **9 unique tickers** with a >10% AH appearance (NCPL, TRUG, TCRT, YYAI, SBNYL, JBDI, CISS, FBGL, IBG).
- Retrospective matches: **3/3** in-universe AH→PM movers of size (JBDI, NCPL, YYAI), all detected.
- Supplementary AH-change-only pass: the line is present in all AH scans. **1 unique ticker: 0 continuation / 0 faded / 1 unassessed.**
  - **IBG: unassessed.** Logged at $0.98 (00:30). SIP shows no PM trades through 04:05 ET; AH carried 610 shares in total (last bar 19:45 ET C $0.85). Persistence unknown.

### Missed Opportunities

| Ticker | AH Change | Why Missed | Would Be Profitable? |
|--------|-----------|------------|---------------------|
| HCAI | +89.8% at 17:45 ET (2.08M sh / 4,432 tr) | Below the $0.50 `MIN_PRICE` floor | No: 18:30 ET ~$0.46 → PM peak $0.44 = −4.3%; fell through the close by 04:15 |
| GP | flat (1,046 AH sh) | PM-only gapper, below $0.50 | Not AH-actionable |

### AH Mover Follow-Through

Every name with two or more >10% AH scans. Current = SIP 04:05 ET close.

| Ticker | AH Peak | Peak Time | AH Trajectory | Current PM | From Peak | From Close | Verdict |
|--------|---------|-----------|---------------|------------|-----------|------------|---------|
| NCPL | $2.25 | 17:10 | **Build→fade** (+17.1 → 13.9 → 11.9 → 31.4 → 31.4 → 39.6 → 35.9 → 30.2%) | $1.92 | −14.7% | +20.8% | PM peak $1.97 **fell short (−12.4%)**; AH better |
| YYAI | $1.01 | 19:35 | **Late surge** (+11.5 → 21.4 → 23.0%, tail high after the final scan) | $0.68 | −32.7% | −1.4% | PM peak $0.87 **fell short (−13.9%)**; gapped down from the $0.96 AH close |
| TRUG | $1.74 | 16:10 | **Spike→fade** (+14.4 → 10.1%) | $1.27 | −27.0% | −8.0% | PM peak $1.38 **fell short (−20.7%)** |
| SBNYL | n/a | — | Unchanged snapshot (+10.4% ×3) | n/a | — | — | No SIP bars (OTC preferred, untradable) |

**AH-peak-vs-PM-peak, extreme zone:** no name reached +130% AH. Tally stays **15 fades / 3 continues (83.3%)**.

**Chase-cap check:** NCPL filled $2.16 below its $2.20 ask and YYAI $0.82 below the $0.84 qualifying price. Standing **1 (XOS), never reclaimed**, unchanged.

### Notes

- **Coverage, last 10 completed sessions (Oct 1–Oct 14):** **Oct 2 0/7, Oct 5 0/7, Oct 9 0/7** (logs exist with no `## Scan` sections). Oct 1, 6, 7, 8, 12, 13 and **Oct 14 ran 7/7.** Sep 30 dropped out of the window: still **3 failures in 10 sessions**, above the ≥2 trigger. The scheduler/bridge investigation stays routed to the email.
- **Raw PM leader / PM-only tracking:** the biggest raw PM mover is **GP (+394% SIP high)**, a **PM-only gapper** below the $0.50 floor. Investability: the $1.35 peak is a single wick (bar closed $0.55, VWAP $0.68), but the 04:00–04:15 ET Yahoo closes stayed above +100% on 3–5M sh/bar. That is holdable at the +100% level and uninvestable at the headline peak. Not a scanner failure. `log/pm-open-scan.csv` has **no October 15 rows yet** at 04:20 ET; confirm the pm-open pulse captures GP. Holdable PM-only count read from the file: **71**. Carry the Initiative-6 cluster to the email.
- **Price-floor exclusions: 12 observations across 9 nights → 13 across 10 nights; >100%-and-holdable stays 1 (TOPP).** HCAI (Oct 14, close $0.2792): +89.8% AH at 17:45 ET on 2.08M sh / 4,432 trades, ~+65% at the 18:30 ET scan; PM peak $0.44 (+57.6%); hypothetical 18:30 entry ~$0.46 → −4.3%; **uninvestable** (PM below the AH peak, unwound below the close by 04:15 ET). Alpaca `tradable` not checked. SHFS ignited at 18:50 ET (after the window, $0.24 at 18:30 ET) and is not counted. GP was PM-only.
- **In-window feed-lag: 8, unchanged.** Every in-universe name with an in-window AH move appeared in the scans. The ≥3 trigger stays reached; carry the whole-universe AH verification to the email.
- **Late-AH-tail tracking: 2 true-tail (ORIS, GNS) / 1 feed-lag (BTCT), unchanged.** YYAI's $1.01 high at 19:35 ET came after the final scan but extended a detected entry and then gapped down; not a winner and not counted.
- **Fade-rule tally: sub-3M 4/25 (16.0%), unchanged; trigger not met.** No candidate was skipped on the fade rule. TRUG (float 1.2M, Grade None) spiked at 16:10 ET and faded (PM $1.38 < AH $1.74), but its skip reason was dead-cat, so it is not counted.
- **DEAD-CAT-OVERRIDE WATCH: JBDI provisional, not counted.** Only one unrounded >10% scan (00:30), so the two-rising-scan condition was not met (MSGY precedent). Raw: $3.37 → PM SIP $3.58 = **+6.2%** on 366K sh / 5,823 trades; next bar closed $3.24, below entry, so **transient**. Day-2 multi-session runner, Grade None. Standing **5 positive / 6 negative**, unchanged.
- **CEILING-OVERRIDE / FIRST-BAR-SPIKE WATCH:** none flagged. NCPL's early 16:05 high was superseded by later highs at 16:25, 16:40 and 17:10 ET. First-bar standing **12 valid (3 ran / 9 faded-flat), 1 pending (ICMB)**, unchanged.
- **Final-scan gate-block: 2 (TRUG, UPC; DKI excluded), unchanged.** JBDI first qualified at the final scan but failed the Day% gate (−26.8%); IBG was thin (510 sh).
- **Execution trackers:** broker-block **2**, stale-book-only **6**, no-fillable-book **4**, float-only **1**, all unchanged. SBNYL (`tradable=false`) is not a broker-block case: float 59.6M exceeds the 50M gate and SIP has no bars. Both qualifiers filled within seconds on limits set from the SIP-15m book while the IEX quote was frozen (NCPL at 16:59 ET, YYAI at 16:00 ET with `ask $0.00 x0`).
- **Actual-entry trackers:**
  - **NCPL: day-1 igniter by the tag rule** (Day +14.4%; no prior ≥+50% session), but a repeat mover with AH footprints on Oct 6/7/12/13. Grade C. $2.16 → PM SIP peak $1.97 = **−8.8%, faded**; AH high $2.25 was the exit.
  - **YYAI: day-1 fresh igniter** (Day −2.6%, flat $0.79 → $0.71 over Oct 6–13). Grade None. $0.82 → PM SIP peak $0.87 = **+6.1%, marginal ran then faded** (SSM precedent), now −17%. AH tail high $1.01 was the exit.
  - First-day igniters **36 → 38 entries (16 ran / 8 flat / 14 faded) = 42.1% ran**. Multi-session runners **2, both faded** (DAIC, OLB), unchanged.
  - Reverse-split tally unchanged (**4/5 this-week faded / 4/6 older continued**). YYAI carries 1-for-40 (May) and 1-for-20 (Aug 13) splits as background only; the catalyst note is not a split.
- **SIP basis checks:** October 14 closes GP $0.27, JBDI $2.51, NCPL $1.59, YYAI $0.69, HCAI $0.28, SHFS $0.23, TRUG $1.38, TCRT $2.07, CISS $0.53, FBGL $2.40, IBG $0.82. October 13 closes for Entry Total%: NCPL $1.39, YYAI $0.708.
- **AEHL day 2 (SIP):** Oct 14 session high **$30.60** (daily bar, includes PM) confirms Yahoo's $29.76 print was real. AEHL closed Oct 14 at $11.49 and trades $10.14 PM (04:05 ET). Our exit at $23.78 caught the PM run before the dump.
- **WINNERS_TRACKING.md:** nothing added. AEHL (day 2) and FCHL (day 3) refreshed.

### Daily Email Routing

- Headline: **No real winner for October 14→15.** Biggest genuine mover JBDI: AH +51.4%, PM +42.6%, detected at the final scan and skipped as a dead-cat (hypothetical +6.2%). GP's +394% was a sub-$0.50 PM-only wick. Detection **75/86 (87.2%)**, selection **39/82 (47.6%)**, 100 days tracked.
- **Open book:** NCPL −10.1% and YYAI −17.6%; neither reclaimed its fill in PM. Both AH peaks ($2.25, $1.01) were the better exits.
- **Scheduler/bridge reliability (decision for Juan):** 3 coverage failures in the last 10 sessions (Oct 2, Oct 5, Oct 9).
- Carry forward: 71-row holdable PM-only cluster → Initiative 6; 8 in-window feed-lag misses → whole-universe AH verification; extreme-runner partial profit (15/3, 83.3%, below threshold); reverse-split recency recommendation; sub-$0.50 floor question (TOPP 1 of 3; HCAI added as uninvestable); stale IEX quote feed. The sub-3M fade (4/25), price-floor, first-bar and final-scan triggers are not met.

### Price Charts

Excerpts from `python3 scripts/price-timeline.py JBDI NCPL YYAI HCAI GP` at ~04:23 ET (Yahoo 5-minute closes; SIP tables above set the peaks). Block charts omitted.

```
JBDI  Previous Close $2.51 (regular close 2026-10-14) | Peak $3.80 (+51.4%) at 10-14 18:00 ET
  [AH]  10-14 17:40 ET: $2.77 (+10.4%)
  [AH]  10-14 17:55 ET: $3.75 (+49.4%)
  [AH]  10-14 18:30 ET: $3.24 (+29.1%)
  [AH]  10-14 19:55 ET: $3.03 (+20.7%)
  [PM]  10-15 04:05 ET: $3.24 (+28.9%)
  [PM]  10-15 04:23 ET: $2.99 (+19.1%)
NCPL  Previous Close $1.59 (regular close 2026-10-14) | AH high $2.25 SIP at 17:10 ET
  [AH]  10-14 17:10 ET: $2.22 (+39.6%)
  [AH]  10-14 19:55 ET: $1.89 (+18.8%)
  [PM]  10-15 04:00 ET: $1.89 (+19.1%)
  [PM]  10-15 04:10 ET: $2.02 (+27.0%)
  [PM]  10-15 04:23 ET: $1.94 (+22.0%)
YYAI  Previous Close $0.6911 (regular close 2026-10-14) | Peak $1.01 (+46.1%) at 10-14 19:35 ET
  [AH]  10-14 19:55 ET: $0.96 (+38.9%)
  [PM]  10-15 04:00 ET: $0.71 (+2.7%)
  [PM]  10-15 04:22 ET: $0.69 (−0.3%)
HCAI  Previous Close $0.2792 (regular close 2026-10-14) | Peak $0.53 (+89.4%) at 10-14 17:45 ET
  [AH]  10-14 19:55 ET: $0.40 (+42.6%)
  [PM]  10-15 04:00 ET: $0.36 (+29.9%)
  [PM]  10-15 04:23 ET: $0.25 (−11.7%)
GP    Previous Close $0.2730 (regular close 2026-10-14) | Peak $1.28 (+368.9%) at 10-15 04:00 ET (Yahoo; SIP $1.35)
  [PM]  10-15 04:00 ET: $0.55 (+101.9%)
  [PM]  10-15 04:10 ET: $0.63 (+132.2%)
  [PM]  10-15 04:20 ET: $0.53 (+93.4%)
  [PM]  10-15 04:23 ET: $0.55 (+101.2%)
```
