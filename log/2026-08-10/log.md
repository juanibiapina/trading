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

## Scan 23:30 CET (5:30 PM ET) — ENTRIES ALLOWED

`scan.py --all` returned **9 hits**. WAFU and FF already held (entered 23:00; position management handled in premarket). This scan finds new entries only.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| WAFU | [TV](https://www.tradingview.com/chart/?symbol=WAFU) | $1.45 | +0.7% | +42.1% | $2.06 | +43.0% | 12.9M | 2.7M | 4.7x | 3.0M | Misc Commercial Services |
| GENK | [TV](https://www.tradingview.com/chart/?symbol=GENK) | $1.82 | -7.1% | +18.1% | $2.15 | +9.7% | 5.4M | 684K | 7.8x | 4.8M | Restaurants |
| HWH | [TV](https://www.tradingview.com/chart/?symbol=HWH) | $1.44 | -3.4% | +13.9% | $1.64 | +10.1% | 3.6M | 498K | 7.3x | 1.5M | Financial Conglomerates |
| MTEN | [TV](https://www.tradingview.com/chart/?symbol=MTEN) | $1.08 | +22.6% | +27.8% | $1.38 | +56.6% | 1.6M | 3.8M | 0.4x | 6.1M | Industrial Machinery |
| MGIH | [TV](https://www.tradingview.com/chart/?symbol=MGIH) | $1.74 | +14.1% | +6.3% | $1.85 | +21.3% | 1.3M | 245K | 5.3x | 1.2M | Containers/Packaging |
| PLBY | [TV](https://www.tradingview.com/chart/?symbol=PLBY) | $1.18 | -3.3% | +26.3% | $1.49 | +22.1% | 1.0M | 760K | 1.4x | 56.2M | Specialty Stores |
| FF | [TV](https://www.tradingview.com/chart/?symbol=FF) | $5.16 | +1.4% | +20.8% | $6.23 | +22.5% | 808K | 403K | 2.0x | 26.1M | Chemicals: Specialty |
| BAOS | [TV](https://www.tradingview.com/chart/?symbol=BAOS) | $0.71 | +8.6% | +7.5% | $0.76 | +16.7% | 286K | 1.2M | 0.2x | 1.0M | Advertising/Marketing |
| DH | [TV](https://www.tradingview.com/chart/?symbol=DH) | $0.70 | -2.1% | +5.3% | $0.74 | +3.1% | 215K | 202K | 1.1x | 29.7M | Packaged Software |

**Instrumentation (log-only, no decision impact):**
- HWH: `SPIKE 16:50ET +38% $1.99 160 trades / 28k sh (first co-spike bar)` | `CONFIRM-3 NO ignition 16:50ET failed third-bar hold/volume as-of 17:30ET`
- MTEN: `SPIKE 17:03ET +16% $1.25 231 trades / 52k sh (first co-spike bar)` | `CONFIRM-3 YES ignition 17:00ET 8.8x; confirmed 17:10ET $1.35 as-of 17:30ET`
- PLBY: `SPIKE 16:09ET +23% $1.45 76 trades / 38k sh (first co-spike bar)` | `CONFIRM-3 NO ignition 16:50ET failed third-bar hold/volume as-of 17:30ET`
- GENK: `SPIKE 16:05ET +59% $2.89 274 trades / 33k sh (first co-spike bar)` | `CONFIRM-3 YES ignition 16:05ET 680.2x; confirmed 16:15ET $2.55 as-of 17:30ET`

**New candidates this scan (HWH, MTEN, BAOS):**
- **HWH → SKIP (fails 2-scan gate + SPIKE→FADE).** First AH appearance, float 1.5M, VRatio 7.3x, `tradable=true`, book two-sided $2.24/$2.28. SIP shows a real, huge ignition at 16:50 ET ($2.49 high, 1.4M sh / 13.6k trades) but it is **fading hard** across every bar since: VWAP $2.20→$2.17→$2.06→$1.92→$1.73→$1.59, last bar 17:15 ET $1.56. Classic SPIKE→FADE (peaked 16:50, declining). Fails the 2-AH-scan gate anyway (first appearance). No same-day catalyst found (Q1 going-concern + $10M equity/warrant shelf noted). No entry.
- **MTEN → SKIP (fails 2-scan gate), WATCH next scan.** First AH appearance, float 6.1M, Day +22.6% (big regular-session run), Total% +56.6%. Scanner VRatio 0.4x but real AH volume **is** accumulating: SIP VWAP building $1.28→$1.30→$1.37→$1.38 with 248k→696k→731k→579k sh/bar, ignition 17:00 ET, CONFIRM-3 YES. `tradable=true`, book $1.00/$1.40 (wide). Genuine BUILD but only 1 AH scan so far — fails the 2-AH-scan >10% gate. No same-day catalyst found. **Watch: if it holds >10% AH into the next scan it satisfies the gate and becomes entry-eligible.**
- **BAOS → SKIP.** AH +7.5%, below the 10% threshold-of-interest.

**Prior-candidate updates:**
- GENK: still fading (AH +31.3% at 23:00 → +18.1% now), volume decaying. SPIKE→FADE thesis intact. Still skip.
- PLBY: AH ticked up to +26.3% but float 56.2M exceeds the <50M gate. Skip.
- MGIH/DH: below 10% AH threshold.

**Action:** No new entries. Both new low-float names (HWH, MTEN) fail the 2-AH-scan gate; HWH is also fading. MTEN is a genuine BUILD to watch next scan. WAFU/FF holds unchanged (managed in premarket).

## Scan 00:00 CET (6:00 PM ET) — ENTRIES ALLOWED

`scan.py --all` returned **14 hits**. WAFU and FF already held (entered 23:00; managed in premarket). This scan finds new entries only. MTEN (watched at 23:30) is now on its 2nd AH appearance and building.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| WAFU | [TV](https://www.tradingview.com/chart/?symbol=WAFU) | $1.45 | +0.7% | +42.8% | $2.07 | +43.8% | 14.1M | 2.9M | 4.9x | 3.0M | Misc Commercial Services |
| GENK | [TV](https://www.tradingview.com/chart/?symbol=GENK) | $1.82 | -7.1% | +21.4% | $2.21 | +12.8% | 5.5M | 704K | 7.9x | 4.8M | Restaurants |
| MTEN | [TV](https://www.tradingview.com/chart/?symbol=MTEN) | $1.08 | +22.6% | +37.0% | $1.48 | +68.0% | 4.9M | 4.1M | 1.2x | 6.1M | Industrial Machinery |
| MGIH | [TV](https://www.tradingview.com/chart/?symbol=MGIH) | $1.74 | +14.1% | +15.5% | $2.01 | +31.8% | 1.8M | 307K | 6.0x | 1.2M | Containers/Packaging |
| JWEL | [TV](https://www.tradingview.com/chart/?symbol=JWEL) | $4.00 | +158.1% | +6.2% | $4.25 | +174.2% | 1.5M | 8.5M | 0.2x | 1.8M | Medical Distributors |
| PLBY | [TV](https://www.tradingview.com/chart/?symbol=PLBY) | $1.18 | -3.3% | +27.1% | $1.50 | +22.9% | 1.2M | 774K | 1.5x | 56.2M | Specialty Stores |
| HUDI | [TV](https://www.tradingview.com/chart/?symbol=HUDI) | $0.93 | +28.0% | +9.2% | $1.01 | +39.8% | 917K | 6.5M | 0.1x | 4.2M | Steel |
| FF | [TV](https://www.tradingview.com/chart/?symbol=FF) | $5.16 | +1.4% | +22.3% | $6.31 | +24.0% | 849K | 407K | 2.1x | 26.1M | Chemicals: Specialty |

(Other hits below 10% AH threshold or high-float: LRHC, ZJYL, DH, BZAI, ARQ, GMEX.)

**Instrumentation (log-only, no decision impact):**
- MTEN: `SPIKE 17:03ET +16% $1.25 231 trades / 52k sh (first co-spike bar)` | `CONFIRM-3 YES ignition 17:00ET 8.8x; confirmed 17:10ET $1.35 as-of 18:00ET`

**MTEN — ENTERED.** Float 6.1M (<10M ideal), Day +22.6% (>-15%, not a dead-cat — positive day). AH BUILD across 2 AH scans (23:30 +27.8% → 00:00 +37.0%), satisfies the 2-AH-scan >10% gate. Total% +68% (well under 150 ceiling). `tradable=true`, two-sided book (bid $1.00 x1000, ask $1.40 x200). SIP confirms a real, accumulating spike: ignition 17:00 ET, 248k→696k→731k→579k→954k→964k sh/bar with 1-5K trades/bar, VWAP building $1.28→$1.58. Peak $1.72 at 17:25 ET, now ~$1.52 (within 20% of AH high = holding, not fading). Catalyst search (4 searches) found **no same-day catalyst** — the registered direct offerings surfaced are June 2026, not today. Grade None, entered with concern noted (learning-phase no-catalyst policy). Filled **64 sh @ $1.39** (id 168e9926). Added to OPEN_POSITIONS.md.

**Prior-candidate updates:**
- GENK → SKIP (unchanged). SPIKE→FADE thesis intact: peaked 16:05 ET ($2.89), now +21.4% AH ($2.21), continuing to decay off peak. Early-peak-fading names are 0/6+ for PM continuation; trajectory dominates the Grade B earnings catalyst.
- JWEL → SKIP. +158% Day% is a regular-session move; AH +6.2% is below the 10% AH threshold-of-interest. VRatio 0.2x (AH vol far below avg).
- HUDI → SKIP. AH +9.2%, below 10% threshold; +28% Day% is regular-session driven, VRatio 0.1x.
- MGIH → SKIP. AH +15.5% but float 1.2M with VRatio 6.0x; only 1 AH scan >10% (was +6.9%/+6.3% earlier, below threshold) — fails the 2-AH-scan gate. Watch only.
- PLBY → SKIP (unchanged). Float 56.2M exceeds the <50M gate.

**Action:** Entered MTEN. WAFU/FF holds unchanged (managed in premarket).

## Scan 00:30 CET (6:30 PM ET) — ENTRIES ALLOWED (FINAL SCAN)

`scan.py --all` returned **14 hits**. WAFU, FF, MTEN already held (managed in premarket). This scan finds new entries only. MGIH (watched since 22:30, now on its 2nd AH scan >10%) becomes entry-eligible.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| WAFU | [TV](https://www.tradingview.com/chart/?symbol=WAFU) | $1.45 | +0.7% | +53.1% | $2.22 | +54.2% | 16.4M | 3.1M | 5.2x | 3.0M | Misc Commercial Services |
| MTEN | [TV](https://www.tradingview.com/chart/?symbol=MTEN) | $1.08 | +22.6% | +35.2% | $1.46 | +65.7% | 5.9M | 4.2M | 1.4x | 6.1M | Industrial Machinery |
| GENK | [TV](https://www.tradingview.com/chart/?symbol=GENK) | $1.82 | -7.1% | +23.1% | $2.24 | +14.3% | 5.6M | 710K | 7.9x | 4.8M | Restaurants |
| MGIH | [TV](https://www.tradingview.com/chart/?symbol=MGIH) | $1.74 | +14.1% | +14.4% | $1.99 | +30.5% | 2.1M | 338K | 6.2x | 1.2M | Containers/Packaging |
| PLBY | [TV](https://www.tradingview.com/chart/?symbol=PLBY) | $1.18 | -3.3% | +25.4% | $1.48 | +21.3% | 1.4M | 799K | 1.8x | 56.2M | Specialty Stores |
| HFFG | [TV](https://www.tradingview.com/chart/?symbol=HFFG) | $1.56 | +0.0% | +37.8% | $2.15 | +37.8% | 1.2M | 296K | 4.2x | 37.1M | Food Distributors |
| FF | [TV](https://www.tradingview.com/chart/?symbol=FF) | $5.16 | +1.4% | +18.4% | $6.11 | +20.0% | 858K | 409K | 2.1x | 26.1M | Chemicals: Specialty |

(Other hits below 10% AH threshold or high-float/regular-session driven: HUDI, LRHC, ZJYL, BZAI, ARQ, GMEX, CRVO.)

**Instrumentation (log-only, no decision impact):**
- MGIH: `SPIKE 16:25ET +22% $2.13 826 trades / 140k sh (first co-spike bar)` | `CONFIRM-3 NO no local-volume new-high ignition as-of 18:30ET`
- HFFG: `SPIKE 18:01ET +23% $1.92 35 trades / 3k sh (first co-spike bar)` | `CONFIRM-3 YES ignition 18:00ET 265.5x; confirmed 18:10ET $2.15 as-of 18:30ET`

**MGIH — ENTERED.** Float 1.2M (<10M ideal), Day +14.1% (>-15%, not a dead-cat). AH >10% across 2 AH scans (00:00 +15.5% → 00:30 +14.4%), satisfies the 2-AH-scan gate. Total% +30.5% (well under 150 ceiling). `tradable=true`, book two-sided (stale $1.49/$1.99 x100). SIP confirms real accumulation: ignition 16:25 ET ($2.13 high, 826 trades / 140k sh), sustained 140k-520k sh/bar with hundreds-thousands trades, and a **rebuild** from a $1.65 dip back to $2.00-2.10 by 17:30-17:35 ET (VWAP $2.01→$2.05, new-high bars) = holding within ~5% of the AH high, BUILD not fade. VRatio 6.2x. Catalyst search (3 searches) found **no same-day catalyst** — the Vietnam facility PR is July 2025, not today. Grade None, entered with concern noted (learning-phase no-catalyst policy). Filled **47 sh @ $2.12** (id 36a4135a). Added to OPEN_POSITIONS.md.

**New-candidate / prior-candidate updates:**
- HFFG → SKIP (fails 2-scan gate). **First AH appearance** this scan, no prior pipeline footprint, so the final-scan feed-lag rescue does not apply (rescue only recovers names already tracked ≥1 prior AH scan). SIP shows a genuine fresh ignition at 18:00 ET (218k→764k→534k→456k sh/bar, thousands of trades, peak $2.30) but the 2-AH-scan >10% gate requires a second appearance. Float 37.1M (<50M), `tradable=true`. Record for morning-eval as a feed-timing note — real mover that arrived too late in the grid to clear the gate.
- GENK → SKIP (unchanged). SPIKE→FADE thesis intact: peaked 16:05 ET ($2.89), now +23.1% AH ($2.24), decaying off peak across all scans. Early-peak-fading names 0/6+ for PM continuation; trajectory dominates the Grade B earnings catalyst.
- PLBY → SKIP (unchanged). AH +25.4% but float 56.2M exceeds the <50M gate.
- Other names below 10% AH threshold or regular-session driven.

**Final-scan feed-lag cross-check:** tracked names (GENK, PLBY, MGIH, HFFG) checked against SIP. MGIH under-report suspicion cleared — SIP corroborates the scanner AH level and it was rescued into entry via the 2-scan gate. No other tracked name is under-reported below its real SIP level. GENK/PLBY correctly skipped on trajectory/float, not on feed lag.

**Action:** Entered MGIH. WAFU/FF/MTEN holds unchanged (managed in premarket). This is the final scheduled scan of the night.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
| WAFU | $1.94 | 23:00 CET | 43 | bc9a1a64 | Float 3.0M, AH BUILD 3 scans, real 1-2M sh/bar vol. Grade None (no catalyst). |
| FF | $6.28 | 23:00 CET | 16 | fe355da6 | Float 26.1M, AH BUILD 2 scans, Q2 earnings today. Grade B. |
| MTEN | $1.39 | 00:00 CET | 64 | 168e9926 | Float 6.1M, Day +22.6%, AH BUILD 2 scans (+27.8%→+37.0%), real SIP 248k→964k sh/bar. Grade None (no catalyst). |
| MGIH | $2.12 | 00:30 CET | 47 | 36a4135a | Float 1.2M, Day +14.1%, AH >10% 2 scans (+15.5%→+14.4%), SIP rebuild to $2.00-2.10 near AH high $2.13, VRatio 6.2x. Grade None (no catalyst). |

## Morning Evaluation — 10:20 CET

### Today's Winner

**NCRA** — Nocera, Inc. (aquaculture → digital-asset pivot)
- Catalyst: **None (unverified)** — no confirmed same-day PR. Background narrative is a digital-asset/BTC-treasury pivot (Dec 2025 $2M BTC allocation, "Nocera Holdings" tech/AI/data-center restructuring, DIVG venture platform). No fresh Aug 11 headline found. Grade None.
- Previous Close: $1.97
- AH last night: **dead flat** — SIP AH was near-zero volume (3–570 sh/bar), price pinned $2.00–2.05 (+2–4%). No AH footprint.
- Premarket now: fired at 04:00 ET PM open — SIP peak **$4.19–4.21 (+113%)** in the 04:00–04:05 ET bar on **1.83M sh / 23,489 trades**; second bar H $3.89 on 1.40M sh / 18,185 trades. Already fading (close $3.22 by 04:10 ET).
- Hypothetical P&L: peak +113%; realistic first-bar VWAP $3.61 = **+83%** (liquid exit around +80%, the >100% wick did not hold ≥2 bars).
- Float: 474K | Market Cap: $3.2M

**Scanner Diagnostic:**
- Detectable at screening time (~22:15 CET)? **NO**
- Why: NCRA was a **PM-only gapper**. It was completely flat in after-hours (SIP volume 3–570 sh/bar, price $2.00–2.05, +2–4%), far below the 10% AH threshold and with no volume. The entire move began at 04:00 ET PM open, hours after the last evening scan (00:30 CET / 18:30 ET). Structurally undetectable by the AH scanner.
- Scanner gap: none actionable — this is the known PM-only-gapper blind spot, not a scanner failure. Not counted against detection baseline.

**Investability (PM-only gapper):** borderline. The +113% peak was a **single-bar spike** ($4.21 wick, 04:00–04:05 ET) that faded to +63% within 10 min. But the first bar traded 1.83M sh at VWAP $3.61 (+83%), so a liquid exit around +80% was available for one bar. Label: **spike — holdable only ~+80% VWAP first bar, >100% peak was a single-bar wick.** Not a clean holdable case.

### Baseline Tracking

- Days tracked: **63** (was 62 + 1)
- Winners detected by scanner: **50/59 (84.7%)** — unchanged. NCRA is a PM-only gapper (structurally undetectable), excluded from the detection ratio per the rules, not counted as a miss.
- Winner selected for paper trade: **28/59 (47.5%)** — unchanged. Winner was undetectable, so no selection opportunity.
- Target: >80% detection
- Status: **BASELINE MET** (84.7%)
- **Baseline gap:** Fri Aug 7 evening scanner did NOT run (no `post-market scan` commits Aug 7; log/2026-08-07 has only position evals). The Aug 7 AH session was therefore never diagnosed — its Monday-morning (Aug 10) retrospective was skipped. Recorded as a **coverage failure**, not a detection miss (no scan opportunity existed).

### Retrospective Scan Results

- Live PM scan (04:21 ET): 4 hits — NCRA +81.4% (peak +113% SIP), WAFU +41.4%, MTEN +28.7%, MGIH +9.2%.
- AH reconstruction (SIP): WAFU real AH BUILD (peak $2.44 +69% @21:55Z, held $2.15–2.40 all evening on 1–2M sh/bar). NCRA flat AH (see above). MTEN/MGIH modest AH movers we entered.
- NCRA (the >100% winner) had **no AH footprint** — PM-only.

### Open Position P&L (Alpaca)

Positions still open at 10:20 (position-evaluation at 10:30/14:30 handles exits). Real Alpaca fills only.

| Ticker | Entry | Entry Total% | Catalyst | Entry Time | PM Peak (SIP) | Peak Time | Exit | P&L | P&L % | Status |
|--------|-------|--------------|----------|------------|---------------|-----------|------|-----|-------|--------|
| WAFU | $1.94 | +34.7% | None | 23:00 CET | $2.60 (+80.6%) | 04:00 ET | open | — | ~+5.7%* | 🟢 Open |
| FF   | $6.28 | +21.7% | B — Q2 earnings | 23:00 CET | $6.21 (+20.3%) | 04:00 ET | open | -1.12 | -1.1% | 🟡 Open |
| MTEN | $1.39 | +28.7% | None | 00:00 CET | ~$1.39 | 04:00 ET | open | -3.18 | -3.6% | 🔴 Open |
| MGIH | $2.12 | +21.8% | None | 00:30 CET | ~$1.90 | 04:00 ET | open | -6.11 | -6.1% | 🔴 Open |

*WAFU: Alpaca mark ($2.22, +14.4%) is **stale** — quote timestamped 2026-08-10T20:41 ET (last night AH). Live PM SIP is ~$2.00–2.12 (opened $2.31 → faded to $1.99). Real P&L vs live PM ~$2.05 = **+5.7%**, not +14.4%. Peak $2.60 was the 04:00 ET first bar; already faded.

**Total Realized P&L (Alpaca fills only): €0.00** (no exits yet; positions open pending 10:30 eval).

### Scanner Effectiveness

- Evening scans ran: **9 of 7 scheduled** (21:30 + 4 observation scans 22:00–22:45 + 4 entry scans 23:00/23:30/00:00/00:30 CET). Full entry-window coverage.
- Candidates found: ~19 unique tickers; 4 entered (WAFU, FF, MTEN, MGIH).
- Retrospective matches: WAFU/MTEN/MGIH all caught + entered. Winner NCRA not caught (PM-only, undetectable).

### Missed Opportunities

| Ticker | AH Change | Why Missed | Would Be Profitable? |
|--------|-----------|------------|---------------------|
| NCRA | flat (+2–4%, no vol) | PM-only gapper — move fired at 04:00 ET, no AH footprint | Yes hypothetically (+83% VWAP first bar) but single-bar spike, not counted as a miss |

### AH Mover Follow-Through

| Ticker | AH Peak (SIP) | Peak Time | AH Trajectory | Current PM | From Peak | From Close | Verdict |
|--------|---------------|-----------|---------------|------------|-----------|------------|---------|
| WAFU | $2.44 (+69%) | 21:55Z (17:55 ET) | Build | ~$2.05 (+42%) | -16% | +42% | PM first-bar $2.60 (+80.6%) **exceeded** AH peak → continuation, then faded |
| MTEN | ~$1.48 (+37%) | ~00:00 CET | Build | ~$1.39 (+29%) | -6% | +29% | Faded modestly into PM |
| MGIH | ~$2.13 (+22%) | ~00:30 CET | Spike→hold | ~$1.90 (+9%) | -11% | +9% | Faded into PM, AH peak better exit |

**AH-peak-vs-PM-peak:** WAFU PM peak $2.60 (+80.6%) exceeded AH peak $2.44 (+69%) — continuation, not a fade (no fade-rule case). MGIH AH peak was the better exit (PM below AH). None cleared the ~+130% extreme-runner threshold.

### Notes

- **Winner NCRA is a PM-only gapper** (7th tracked). Standing PM-only-gapper **holdable count: 1 clear (SXTC) of 7** — NCRA labeled spike/borderline (holdable ~+80% first bar only, >100% peak was a single-bar wick). Not a cluster; early-PM-scan workflow decision stays with Juan, not triggered.
- **Coverage-failure / baseline-gap tally:** Fri Aug 7 evening scanner did not run at all → Aug 7 AH session never diagnosed (skipped Monday retrospective). First coverage failure since the founding Jun 18–19 case. One-off for now; watch for recurrence (≥2 within ~10 sessions → flag scheduler/bridge reliability to Juan via email).
- Fade-rule, late-AH-tail, in-window feed-lag, price-floor, reverse-split, broker-block, stale-book tallies: no new qualifying cases tonight (NCRA is PM-only; WAFU continued rather than faded). Standing counts unchanged: in-window feed-lag misses = 4 (escalation trigger REACHED — AH-data-source cross-check already routed to email); stale-book execution-blocks = 3; price-floor exclusions = 5 (0 holdable).
- **Email item:** surface the Aug 7 coverage failure (scanner didn't run Friday, retrospective skipped) so Juan is aware the baseline chain has a one-night gap.

### Price Charts

**NCRA** (winner, PM-only gapper) — prev close $1.97, 2-day range $1.94–$4.21, peak $4.21 (+113.7%) @ 08-11 04:00 ET:
- AH (16:00–20:00 ET): flat $1.99–2.12, near-zero volume (no footprint)
- PM open 04:00 ET: $2.37 → spike $4.21 on 1.83M sh/23.5K trades → faded to $3.22 by 04:10 ET
- Classic PM-only spike: the entire move is a single 04:00 ET bar.
