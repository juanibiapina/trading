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

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
