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

## Scan 22:45 CET (4:45 PM ET) — OBSERVATION ONLY

`scan.py --all` returned **5 hits**. Learning-phase rule: no entries before 23:00 CET.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| WAFU | [TV](https://www.tradingview.com/chart/?symbol=WAFU) | $1.45 | +0.7% | +40.7% | $2.04 | +41.7% | 6.9M | 2.0M | 3.4x | 3.0M | Misc Commercial Services |
| GENK | [TV](https://www.tradingview.com/chart/?symbol=GENK) | $1.82 | -7.1% | +37.9% | $2.51 | +28.1% | 3.2M | 415K | 7.7x | 4.8M | Restaurants |
| FF | [TV](https://www.tradingview.com/chart/?symbol=FF) | $5.16 | +1.4% | +17.8% | $6.08 | +19.4% | 416K | 353K | 1.2x | 26.1M | Chemicals: Specialty |
| PLBY | [TV](https://www.tradingview.com/chart/?symbol=PLBY) | $1.18 | -3.3% | +15.8% | $1.37 | +12.0% | 247K | 674K | 0.4x | 56.2M | Specialty Stores |
| BZAI | [TV](https://www.tradingview.com/chart/?symbol=BZAI) | $1.03 | -6.4% | +5.8% | $1.09 | -0.9% | 159K | 3.0M | 0.1x | 122.0M | Semiconductors |

**Instrumentation (log-only, no decision impact):**
- WAFU: `SPIKE 16:00ET +45% $2.10 936 trades / 218k sh (first co-spike bar)` | `CONFIRM-3 NO no local-volume new-high ignition as-of 16:45ET`
- GENK: `SPIKE 16:05ET +59% $2.89 274 trades / 33k sh (first co-spike bar)` | `CONFIRM-3 YES ignition 16:05ET 680.2x; confirmed 16:15ET $2.55 as-of 16:45ET`
- FF: `SPIKE 16:19ET +38% $7.10 1029 trades / 102k sh (first co-spike bar)` | `CONFIRM-3 NO ignition 16:15ET failed third-bar hold/volume as-of 16:45ET`
- PLBY: `SPIKE 16:09ET +23% $1.45 76 trades / 38k sh (first co-spike bar)` | `CONFIRM-3 NO no local-volume new-high ignition as-of 16:45ET`

**Trajectory notes:**
- WAFU: second AH appearance (was +37.9% at 22:30, now +40.7%) — holding/slight build near AH high. Low float (3.0M), VRatio 3.4x, MCap $6.4M. Satisfies the 2-AH-scan >10% gate. Peaked at the 16:00 bell (early). No catalyst checked yet — search at 23:00.
- GENK: second AH appearance (was +39.6% at 22:30, now +37.9%) — holding. Low float (4.8M), VRatio up to 7.7x, MCap $60M, but Day% -7.1%. Peaked 16:05 (early). Satisfies 2-AH-scan gate. Search catalyst at 23:00.
- FF: **first AH appearance** (+17.8%). Higher float (26.1M), MCap $226M, VRatio 1.2x. Spiked 16:19, CONFIRM-3 failed third-bar hold. Needs a second AH appearance to satisfy the 2-scan gate.
- PLBY: second AH appearance (was +14.4%, now +15.8%) — holding. High float (56.2M), VRatio 0.4x (AH vol below avg) = weak signal.
- BZAI: +5.8% AH, below 10% threshold-of-interest.

**Action:** No entries (observation scan, before 23:00 CET). At the 23:00 scan, evaluate names clearing >10% AH across ≥2 AH scans — WAFU, GENK, PLBY qualify on the 2-scan gate; run structured catalyst search on WAFU and GENK (both low-float, real VRatio). Both peaked early (16:00–16:05) — watch whether they hold or fade into 23:00.

## Scan 23:00 CET (5:00 PM ET) — ENTRIES ALLOWED

`scan.py --all` returned **6 hits**. First entry-eligible scan of the night (learning-phase rule: no entries before 23:00 CET).

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| WAFU | [TV](https://www.tradingview.com/chart/?symbol=WAFU) | $1.45 | +0.7% | +49.0% | $2.16 | +50.0% | 10.3M | 2.4M | 4.2x | 3.0M | Misc Commercial Services |
| GENK | [TV](https://www.tradingview.com/chart/?symbol=GENK) | $1.82 | -7.1% | +31.3% | $2.39 | +21.9% | 4.6M | 598K | 7.7x | 4.8M | Restaurants |
| FF | [TV](https://www.tradingview.com/chart/?symbol=FF) | $5.16 | +1.4% | +22.1% | $6.30 | +23.8% | 657K | 385K | 1.7x | 26.1M | Chemicals: Specialty |
| PLBY | [TV](https://www.tradingview.com/chart/?symbol=PLBY) | $1.18 | -3.3% | +16.1% | $1.37 | +12.3% | 317K | 682K | 0.5x | 56.2M | Specialty Stores |
| ZJYL | [TV](https://www.tradingview.com/chart/?symbol=ZJYL) | $2.92 | +35.8% | +5.1% | $3.07 | +42.8% | 223K | 4.1M | 0.1x | 1.8M | Medical Specialties |
| DH | [TV](https://www.tradingview.com/chart/?symbol=DH) | $0.70 | -2.1% | +24.7% | $0.87 | +22.1% | 50K | 182K | 0.3x | 29.7M | Packaged Software |

**Instrumentation (log-only, no decision impact):**
- WAFU: `SPIKE 16:00ET +45% $2.10 936 trades / 218k sh (first co-spike bar)` | `CONFIRM-3 NO no local-volume new-high ignition as-of 17:00ET`
- GENK: `SPIKE 16:05ET +59% $2.89 274 trades / 33k sh (first co-spike bar)` | `CONFIRM-3 YES ignition 16:05ET 680.2x; confirmed 16:15ET $2.55 as-of 17:00ET`
- FF: `SPIKE 16:19ET +38% $7.10 1029 trades / 102k sh (first co-spike bar)` | `CONFIRM-3 NO ignition 16:15ET failed third-bar hold/volume as-of 17:00ET`
- PLBY: `SPIKE 16:09ET +23% $1.45 76 trades / 38k sh (first co-spike bar)` | `CONFIRM-3 NO no local-volume new-high ignition as-of 17:00ET`
- DH: `SPIKE 16:43ET +26% $0.88 89 trades / 14k sh (first co-spike bar)` | `CONFIRM-3 PENDING ignition 16:40ET; waiting for third bar as-of 17:00ET`

**SIP volume confirmation (real, accumulating):**
- WAFU: 1-2M sh/bar, 6-13K trades/bar, VWAP climbing $1.82→$2.21 — real, building, corroborates AH price. Book $2.25/$2.29 x100.
- GENK: 400K-1.3M sh/bar early, but **fading** last bars (883K→290K→140K sh), price $2.89→$2.38. Real but decaying.
- FF: 70-290K sh/bar, hundreds-1K trades, price building to $6.45. Real. Book $6.19/$6.24.

**Catalyst search:**
- WAFU: no same-day news found (4 searches). No catalyst → Grade None, enter with concern noted (learning phase).
- GENK: Q2 2026 earnings released after close today (5:00 PM ET call). Grade B.
- FF: Q2 2026 earnings released after close today. Grade B.

**Entry evaluation:**
- **WAFU → ENTERED.** Float 3.0M, Day +0.7%, AH BUILD across 3 scans (37.9%→40.7%→49.0%), making new highs, real 1-2M sh/bar volume. Total% +50% (under 150 ceiling). All gates clear. No catalyst (concern noted). Filled 43 sh @ **$1.94** (id bc9a1a64). Grade None.
- **FF → ENTERED.** Float 26.1M (<50M), Day +1.4%, AH BUILD across 2 scans (17.8%→22.1%), new highs $6.45, Q2 earnings catalyst. Total% +23.8%. All gates clear. Filled 16 sh @ **$6.28** (id fe355da6). Grade B.
- **GENK → SKIP.** Float 4.8M and Grade B earnings, but trajectory is early-peak-fade: peaked 16:05 ET ($2.89), declined across all 3 AH scans (39.6%→37.9%→31.3%), volume decaying (1.3M→140K sh/bar). Early-peak-fading names are 0/6+ for PM continuation; trajectory dominates catalyst. Hypothetical no-entry.
- **PLBY → SKIP.** Float 56.2M exceeds the <50M gate; VRatio 0.4x (AH vol below avg) = weak signal.
- **ZJYL → SKIP.** AH +5.1%, below 10% threshold-of-interest (Total% is regular-session driven, +35.8% Day%).
- **DH → SKIP.** Only 1 AH appearance (fails 2-scan gate); quote stale 16:00 ET, `ask $0.00 x0` = illiquid, no AH book.

**Action:** Entered WAFU and FF. Both added to OPEN_POSITIONS.md. Position management (hold/sell) handled in premarket.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
| WAFU | $1.94 | 23:00 CET | 43 | bc9a1a64 | Float 3.0M, AH BUILD 3 scans, real 1-2M sh/bar vol. Grade None (no catalyst). |
| FF | $6.28 | 23:00 CET | 16 | fe355da6 | Float 26.1M, AH BUILD 2 scans, Q2 earnings today. Grade B. |
