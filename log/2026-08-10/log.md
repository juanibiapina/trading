# Post-Market Screening - 2026-08-10

## Scan 21:30 CET (3:30 PM ET) — REGULAR SESSION

Scanner ran in REGULAR session (market close at 22:00 CET / 4:00 PM ET). AH not open yet, so **no entries** this scan (regular-session caution rule). Candidates flagged as "Watch — pending AH confirmation"; only enter if they reappear in a 22:00+ CET AH scan with sustained momentum.

47 hits. Most high-% names show collapsing 5m volume (VChg% -99%) = intraday fade, not building. Notable movers with intact/rising volume:

| Ticker | Chart | Price | Day% | 5mVol | IRVol | VChg% | Float | MCap | Industry | Note |
|--------|-------|-------|------|-------|-------|-------|-------|------|----------|------|
| SBNY | [TV](https://www.tradingview.com/chart/?symbol=SBNY) | $0.50 | +35.1% | 9.0M | 8665 | +huge | 59.6M | 31.5M | Regional Banks | High float; heavy vol |
| JWEL | [TV](https://www.tradingview.com/chart/?symbol=JWEL) | $3.21 | +107.1% | 50K | 3905 | -2.1% | 1.8M | 3.4M | Medical Distributors | Low float, vol holding |
| SALM | [TV](https://www.tradingview.com/chart/?symbol=SALM) | $0.98 | +1.0% | 100K | 37.6 | +1222% | 14.2M | 25.8M | Broadcasting | Vol surge, flat price |
| ZJYL | [TV](https://www.tradingview.com/chart/?symbol=ZJYL) | $2.83 | +31.6% | 9K | 23.2 | -24.3% | 1.8M | 22.2M | Medical Specialties | Low float |
| FEAM | [TV](https://www.tradingview.com/chart/?symbol=FEAM) | $2.04 | +35.7% | 12K | 51.7 | -60.9% | 20.9M | 84.5M | Chemicals: Specialty | Vol fading |
| DETX | [TV](https://www.tradingview.com/chart/?symbol=DETX) | $3.74 | +23.8% | 23K | 4.7 | +443% | 5.1M | 21.2M | Aerospace & Defense | Vol rising |
| AEHL | [TV](https://www.tradingview.com/chart/?symbol=AEHL) | $5.67 | +16.6% | 1K | 8.8 | +85.7% | 15.6M | 114.2M | Building Products | Vol rising |

Many other hits (SCKT +402%, THH +105%, XHLD +46%, AUUD +46%, HUDI +42.6%, ARTW +38%) show VChg% ≈ -99% to -100% = volume dried up = late-session fades, not watch candidates.

**Action:** No entries (regular session). Re-scan at 22:00+ CET once AH opens to see which names carry momentum into after-hours.

## Scan 22:00 CET (4:00 PM ET) — OBSERVATION ONLY

Scanner ran right at AH open (16:00 ET). `scan.py --all` returned **0 hits** — no names cleared threshold yet (AH volume hasn't accumulated one minute after the bell). Learning-phase rule: 22:00 scan is observation-only regardless, no entries before 23:00 CET.

Cross-checked the strongest low-float 21:30 watch names in the live AH book:

| Ticker | Bid | Ask | Note |
|--------|-----|-----|------|
| JWEL | $4.12 x100 | $0.00 x0 | One-sided, no AH offer |
| ZJYL | $2.51 x100 | $3.40 x100 | Two-sided but thin |
| DETX | $2.94 x100 | $0.00 x0 | One-sided, no AH offer |

**Action:** No candidates found. No entries (observation scan + 0 hits). Re-scan at 22:30 / 23:00 CET; catalysts and AH volume often build 15-30 min after the bell.

## Scan 22:15 CET (4:15 PM ET) — OBSERVATION ONLY

`scan.py --all` returned **0 hits** — 15 min into AH, still no name clearing threshold on accumulated AH volume. Learning-phase rule: no entries before 23:00 CET anyway.

**Action:** No candidates found. No entries. Re-scan at 22:30 / 23:00 CET; AH volume and catalysts often build 15-30 min after the bell.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
