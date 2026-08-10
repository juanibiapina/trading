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

## Scan 22:30 CET (4:30 PM ET) — OBSERVATION ONLY

`scan.py --all` returned **4 hits**. First names to clear threshold on accumulated AH volume. Learning-phase rule: no entries before 23:00 CET.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| WAFU | [TV](https://www.tradingview.com/chart/?symbol=WAFU) | $1.45 | +0.7% | +37.9% | $2.00 | +38.9% | 4.8M | 1.8M | 2.7x | 3.0M | Misc Commercial Services |
| GENK | [TV](https://www.tradingview.com/chart/?symbol=GENK) | $1.82 | -7.1% | +39.6% | $2.54 | +29.6% | 772K | 121K | 6.4x | 4.8M | Restaurants |
| MGIH | [TV](https://www.tradingview.com/chart/?symbol=MGIH) | $1.74 | +14.1% | +6.9% | $1.86 | +22.0% | 149K | 114K | 1.3x | 1.2M | Containers/Packaging |
| PLBY | [TV](https://www.tradingview.com/chart/?symbol=PLBY) | $1.18 | -3.3% | +14.4% | $1.35 | +10.6% | 129K | 663K | 0.2x | 56.2M | Specialty Stores |

**Instrumentation (log-only, no decision impact):**
- WAFU: `SPIKE 16:00ET +45% $2.10 936 trades / 218k sh (first co-spike bar)` | `CONFIRM-3 NO no local-volume new-high ignition as-of 16:30ET`
- GENK: `SPIKE 16:05ET +59% $2.89 274 trades / 33k sh (first co-spike bar)` | `CONFIRM-3 YES ignition 16:05ET 680.2x; confirmed 16:15ET $2.55 as-of 16:30ET`
- PLBY: `SPIKE 16:09ET +23% $1.45 76 trades / 38k sh (first co-spike bar)` | `CONFIRM-3 NO no local-volume new-high ignition as-of 16:30ET`

**Trajectory notes:**
- WAFU: spiked to $2.10 (+45%) at the 16:00 bell, now $2.00 (+37.9%) — early spike fading off peak. Low float (3.0M), no catalyst checked yet.
- GENK: spiked to $2.89 (+59%) at 16:05, now $2.54 (+39.6%) — early spike, off peak. Low float (4.8M), MCap $60M. CONFIRM-3 YES but that is log-only.
- MGIH: +6.9% AH, below 10% threshold-of-interest.
- PLBY: high float (56.2M), VRatio 0.2x (AH vol below avg), weak signal.

**Action:** No entries (observation scan, before 23:00 CET). Re-scan at 23:00 CET. At 23:00+, evaluate names that have cleared >10% AH across ≥2 AH scans (GENK and WAFU are first appearances this scan — need a second AH appearance to satisfy the 2-scan gate). Run structured catalyst search on GENK/WAFU at 23:00.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
