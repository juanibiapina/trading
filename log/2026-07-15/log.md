# 2026-07-15

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| GCTK | $0.87 | $0.71 | -18.4% | ~$0.95 (+9%) | 1 | A | HOLD | Above -25% hard stop ($0.6525); peak never >+50% so no trail; day 1 of 5, catalyst intact |
| LVLU | $11.03 | $8.89 | -19.4% | $11.99 (+8.7%) | 2 | B | SELL | Below -15% hard stop ($9.38) AND day-2 time limit; sell @ $8.40 working (no PM liquidity) |
| VTAK | $0.72 | $0.80 | +11.1% | $1.27 (+76%) | 1 | None | SELL | Grade None → exit at any profit; PM spiked $1.27 then faded, sold into fade |
| XCUR | $2.40 | $2.00 | -16.7% | $2.26 | 1 | None | SELL | Grade None → exit first PM opportunity; below -10% hard stop |

**Actions taken:**
- SELL 125 VTAK @ limit $0.80 ext (id 3652f341) — filled @ **$0.80**, +$10.00 (+11.1%)
- SELL 41 XCUR @ limit $1.92 ext (id 9c193da3) — filled @ **$2.00**, -$16.40 (-16.7%)
- SELL 9 LVLU @ limit $8.40 ext (id a2a6a973) — **still working**, no PM liquidity; confirm fill at 14:30 pulse
- HOLD 101 GCTK — Grade A, above hard stop, catalyst intact

**Realized P&L this pulse:** VTAK +$10.00, XCUR -$16.40 = **-$6.40 net** (LVLU pending)

## Position Evaluation — 14:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| GCTK | $0.8743 | $0.55 | -37.6% | ~$0.95 (+9%) | 2 | A | SELL | Below -25% hard stop ($0.6525). SIP PM faded steadily $0.95→$0.55 (12:15Z vwap $0.56, liquid ~660 trades/bar). Grade A hard stop hit → exit |
| LVLU | $11.03 | $8.12 | -26.4% | $11.99 (+8.7%) | 2 | B | SELL | Below -15% hard stop ($9.38) AND day-2 time limit. SIP $8.00-8.10, thin (11 trades/bar). Prior $8.40 order canceled (wouldn't fill) and repriced |

**Actions taken:**
- Canceled stale LVLU order a2a6a973 ($8.40 limit, wouldn't fill against $8.00-8.10 book)
- SELL 101 GCTK @ limit $0.53 ext (id 86275106) — filled @ **$0.546**, -$33.16 (-37.6%)
- SELL 9 LVLU @ limit $7.85 ext (id 2cdf7fc6) — filled @ **$8.12**, -$26.19 (-26.4%)

**Realized P&L this pulse:** GCTK -$33.16, LVLU -$26.19 = **-$59.35 net**

**Day total (both pulses):** VTAK +$10.00, XCUR -$16.40, GCTK -$33.16, LVLU -$26.19 = **-$65.75 net**

**No open positions remaining.** Account equity ~$99,930.

**Note (GCTK):** Grade A operational catalyst (Lōkahi reverse merger) did not produce a multi-day runner — collapsed from PM open $0.95 to $0.55 on day 2. The completed-reverse-merger structure carried dilution/control-change risk flagged at entry; the -25% hard stop did its job. Data point: not every Grade A operational catalyst sustains; reverse-merger completions may behave more like dilution events than AIIO/UGRO-style acquisitions.

---

# Post-Market Screening - 2026-07-15

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|

## Scan 21:30 CET (3:30 PM ET)

**Regular session — AH not yet open. No entries (regular-session caution rule).** Watch candidates flagged for AH confirmation at 22:00+ CET scans. Most scan hits show collapsed VChg% (volume already faded intraday), so few clean watches.

| Ticker | Chart | Price | Chg% | 5mVol | Avg5m | IRVol | VChg% | Float | MCap | Industry |
|--------|-------|-------|------|-------|-------|-------|-------|-------|------|----------|
| JTAI | [TV](https://www.tradingview.com/chart/?symbol=JTAI) | $3.40 | +636.4% | 100 | 68K | 5.5 | -99.9% | 1.2M | 4.8M | Airlines |
| ASPD | [TV](https://www.tradingview.com/chart/?symbol=ASPD) | $2.89 | +189.0% | 478 | 854 | 0.5 | +19.5% | 0 | 4.8M | REIT |
| CPHI | [TV](https://www.tradingview.com/chart/?symbol=CPHI) | $1.15 | +87.1% | 804 | 336K | 23.9 | -99.8% | 37.8M | 46.6M | Pharma: Major |
| MRAI | [TV](https://www.tradingview.com/chart/?symbol=MRAI) | $1.25 | +66.7% | 301 | 4K | 9.3 | -99.0% | 11.3M | 31.6M | Packaged Software |
| SOBR | [TV](https://www.tradingview.com/chart/?symbol=SOBR) | $1.80 | +54.3% | 200 | 332K | 5.2 | -99.9% | 2.3M | 5.1M | Electronic Equip |
| KUST | [TV](https://www.tradingview.com/chart/?symbol=KUST) | $1.37 | +35.6% | 350 | 323K | 6.5 | -99.5% | 577K | 859K | Misc Commercial |

**Notes:** All watch candidates show VChg% near -99% (5-min volume collapsed vs earlier intraday spike) — these spiked earlier in the regular session and are fading, not building. JTAI +636% is the biggest mover (float 1.2M) but volume is dead (100 sh/5min). None qualify for entry at a regular-session scan regardless; re-evaluate any that carry into AH with sustained volume at the 22:00/22:30/23:00 CET scans. Entries only permitted at 23:00+ CET per learning-phase default.

## Scan 22:00 CET (4:00 PM ET)

**No candidates found.** Scanner returned 0 hits at AH open (16:00 ET). Observation-only scan (learning-phase rule: no entries before 23:00 CET). None of the 21:30 regular-session watch names (JTAI, ASPD, CPHI, MRAI, SOBR, KUST) reappeared above threshold as AH opened — consistent with their faded regular-session volume. Re-check at 22:30/23:00 for any AH carry.

