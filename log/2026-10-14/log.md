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

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
