# Post-Market Screening - 2026-08-06

## Scan 21:30 CET (3:30 PM ET)

Regular-session scan (15:30 ET, before AH opens at 22:00 CET). Per regular-session caution rule: no entries. Candidates flagged as watch — pending AH confirmation. Only enter if they reappear in an AH scan (22:00+ CET) with sustained momentum.

| Ticker | Chart | Price | Day% | 5mVol | AvgVol | IRVol | VChg% | Float | MCap | Industry |
|--------|-------|-------|------|-------|--------|-------|-------|-------|------|----------|
| XHLD | [TV](https://www.tradingview.com/chart/?symbol=XHLD) | $2.07 | +159.6% | 6.5M | 3.4M | 108.6 | +131.6% | 7.8M | $9.5M | Misc Commercial Services |
| BYAH | [TV](https://www.tradingview.com/chart/?symbol=BYAH) | $3.05 | +15.5% | 32K | 26K | 199.1 | -5.2% | 4.2M | $16.8M | Household/Personal Care |
| ALEC | [TV](https://www.tradingview.com/chart/?symbol=ALEC) | $1.88 | +26.2% | 71K | 161K | 16.4 | -74.8% | 77.7M | $208.7M | Biotechnology |
| WLDS | [TV](https://www.tradingview.com/chart/?symbol=WLDS) | $3.69 | +27.9% | 163K | 74K | 1.5 | +861.5% | 1.7M | $8.1M | Electronic Equipment |

**Notes:**
- **XHLD** — biggest mover (+159.6%), real regular-session volume (6.5M on 3.4M avg, VChg +131.6%). Low float 7.8M. Best watch candidate. Already extended (>150% would be a ceiling concern if it carries to AH). Watch for AH continuation.
- **BYAH** — +15.5%, low float 4.2M, sustained relative volume (IRVol 199x). Note: BYAH is the Jun 11 dead-cat-override example ticker; different setup today. Watch for AH.
- **WLDS** — +27.9%, low float 1.7M, huge VChg +861.5% but only 1.5 IRVol (volume fading). Weaker.
- **ALEC** — +26.2% but float 77.7M and volume below average (IRVol declining). Weak.
- Thin/stale movers skipped from watch (CLRO +161.9%, CELZ +104.1%, AZI +52%, PN, PEPG, III — all show VChg near -99% = single-print/stale, no real sustained volume).
- No spike-bar/confirmation instrumentation run — those apply to AH candidates with AH change >10%; AH session not yet open.

## Scan 22:00 CET (4:00 PM ET)

Observation-only scan (AH just opened at 16:00 ET). Per learning-phase rule, no entries before 23:00 CET. `scan.py --all` returned **0 AH hits** — expected at the AH-open minute (TradingView postmarket feed lags the first few minutes). Cross-checked the four 21:30 regular-session watch names against the live Alpaca book:

| Ticker | 21:30 Close | AH-open Bid | AH-open Ask | Book | Note |
|--------|-------------|-------------|-------------|------|------|
| XHLD | $2.07 | $2.38 x100 | $0.00 x0 | one-sided | Up ~+15% off regular close into AH, but **no ask/size** — illiquid AH book at open. Low float 7.8M. Watch for real two-sided book + accumulation at 22:30. |
| BYAH | $3.05 | $2.72 x100 | $3.63 x100 | two-sided | Wide spread, sitting near regular close. Low float 4.2M. |
| WLDS | $3.69 | $3.50 x100 | $4.79 x100 | two-sided | Very wide spread, below regular close. Float 1.7M. |
| ALEC | $1.88 | $1.52 x100 | $1.87 x100 | two-sided | Below regular close (fading). Float 77.7M. |

**Instrumentation (XHLD, only name >10% into AH so far):**
- `SPIKE-BAR: XHLD 2026-08-06 NO-SPIKE no AH bars yet (as-of 16:00ET)`
- `CONFIRM-3: XHLD 2026-08-06 PENDING no AH bars as-of 16:00ET`
- SIP bars from 20:00Z: `no bars (feed=iex; AH/PM sparse)` — nothing accumulated at the open minute.

**Notes:**
- No entries (observation scan). Nothing has confirmed sustained AH momentum yet.
- XHLD is the name to watch: biggest mover, low float, but needs a real fillable book and AH accumulation at 22:30/23:00 to qualify. Its regular-session Total% is already ~+160%, near the +150% ceiling — a ceiling concern if it carries.
- ALEC and WLDS both trading *below* their regular closes into AH (fading). BYAH flat with a wide spread.
- Next scan 22:30 CET should have real AH bars to run SIP volume confirmation and instrumentation.

## Scan 22:15 CET (4:15 PM ET)

Observation-only scan (~15 min into AH; before 23:00 CET → no entries). `scan.py --all` returned **0 AH hits**. Cross-checked tracked pipeline names against live book + first SIP AH bar (20:00Z = 16:00 ET):

| Ticker | 21:30 Close | AH Bid | AH Ask | 1st AH Bar (VWAP / trades / vol) | AH vs Close | Note |
|--------|-------------|--------|--------|----------------------------------|-------------|------|
| XHLD | $2.07 | $2.38 x100 | $0.00 x0 | $2.25 / 13,561 / 2.27M | ~+9% | Real volume but **still no ask/size** — illiquid AH book. |
| BYAH | $3.05 | $2.72 x100 | $3.63 x100 | $3.19 / 101 / 12K | ~+5% | Thin, flat near close. |
| WLDS | $3.69 | $3.50 x100 | $4.79 x100 | $3.98 / 280 / 31K | ~flat | Thin, wide spread. |
| ALEC | $1.88 | $1.52 x100 | $1.87 x100 | $1.83 / 77 / 87K | below close | Fading. |

**Instrumentation (XHLD, only name near/above 10% into AH):**
- `SPIKE-BAR: XHLD 2026-08-06 NO-SPIKE peak +3% @16:00ET (no bar cleared +15% on a volume co-spike) (as-of 16:15ET)`
- `CONFIRM-3: XHLD 2026-08-06 NO no local-volume new-high ignition as-of 16:15ET`

**Notes:**
- No entries (observation scan, pre-23:00 CET).
- **XHLD** — its +159.6% was the **regular session**; into AH it's only ~+3% off the AH-open reference (NO-SPIKE). Real AH volume (2.27M / 13,561 trades in the first bar, likely close-auction rollover) but the book is still `ask $0.00 x0` — **illiquid (no fillable AH book)**, same one-sided pattern as 22:00. Regular-session Total% ~+160% is also above the +150% ceiling. Not entry-viable unless a real two-sided book + fresh AH accumulation appears at 23:00.
- BYAH / WLDS thin (101 / 280 trades). ALEC fading below its close.
- Quotes all stale-stamped 16:00 ET and only the 16:00 SIP bar is available (~15 min free-tier lag); next scan (23:00 CET) should have real AH bars to confirm accumulation and — if XHLD develops a fillable book — evaluate for entry.

## Scan 22:30 CET (4:30 PM ET)

Observation-only scan (~30 min into AH; before 23:00 CET → no entries). `scan.py --all` returned **8 AH hits**; three above the +10% AH threshold: DSY, RDGT, RCEL.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| DSY | [TV](https://www.tradingview.com/chart/?symbol=DSY) | $3.45 | +3.3% | +80.3% | $6.22 | +86.2% | 1.0M | 185K | 5.6x | 1.3M | Miscellaneous |
| RDGT | [TV](https://www.tradingview.com/chart/?symbol=RDGT) | $0.79 | +10.7% | +25.3% | $0.99 | +38.7% | 4.8M | 786K | 6.1x | 1.4M | Medical Distributors |
| RCEL | [TV](https://www.tradingview.com/chart/?symbol=RCEL) | $4.75 | +6.3% | +13.7% | $5.40 | +20.8% | 62K | 135K | 0.5x | 23.9M | Medical Specialties |

Below-threshold hits (log only): RDGT-tier ignored — FNKO +7.0% (float 40M), CABR +5.6%, EXFY +5.9%, NAUT +9.0%, SENS +7.8%.

**Instrumentation (AH change >10%):**
- `SPIKE-BAR: DSY 2026-08-06 SPIKE 16:03ET +20% $4.14 32 trades / 3k sh (first co-spike bar) (as-of 16:30ET)`
- `CONFIRM-3: DSY 2026-08-06 NO ignition 16:05ET failed third-bar hold/volume as-of 16:30ET`
- `SPIKE-BAR: RDGT 2026-08-06 SPIKE 16:03ET +35% $1.07 783 trades / 186k sh (first co-spike bar) (as-of 16:30ET)`
- `CONFIRM-3: RDGT 2026-08-06 NO no local-volume new-high ignition as-of 16:30ET`
- `SPIKE-BAR: RCEL 2026-08-06 NO-SPIKE peak +19% @16:06ET (no bar cleared +15% on a volume co-spike) (as-of 16:30ET)`
- `CONFIRM-3: RCEL 2026-08-06 NO no local-volume new-high ignition as-of 16:30ET`

**SIP volume + book (20:00Z = 16:00 ET open):**

| Ticker | 1st AH bar (vwap/trades/vol) | Later bars | Quote (bid / ask) | Book | Verdict |
|--------|------------------------------|------------|-------------------|------|---------|
| DSY | $4.13 / 152 / 13K | 20:05 $5.83/14,184/802K, 20:10 $6.21/12,868/811K, 20:15 $5.45/7,712/469K | $6.93 x100 / $7.06 x100 | two-sided | Real accumulating volume; spiked to $7.16 then faded to $5.15, quote rebuilt ~$7. |
| RDGT | $1.03 / 3,404 / 741K | 20:05 $1.05/12,291/2.87M, 20:10 $1.00/6,814/1.73M, 20:15 $1.05/7,571/1.73M | $0.86 x200 / $0.94 x100 | two-sided | Real accumulating volume; spiked $1.20 then faded to ~$0.94. |
| RCEL | $4.80 / 27 / 29K | 20:05 $5.62/80/28K, 20:10 $5.55/22/7K, 20:15 $5.38/2/0.5K | $4.05 x100 / $5.37 x100 (stale 16:00) | thin | Only 22-80 trades/bar; wide stale book. Thin liquidity. |
| XHLD (carried) | $2.25 / 13,561 / 2.27M | 20:15 $2.46/6,393/899K | $2.38 x100 / $0.00 x0 | one-sided | Still **illiquid (no fillable ask)** — regular-session mover, not AH. Skip. |

**Catalyst search:**
- **RDGT** — FY2026 earnings reported: revenue +10.2% to $132.16M, gross profit +23.8% to $4.75M, but **net loss $1.25M** (vs $10.20M prior net income). Earnings catalyst, mixed/weak (net loss). Provisional Grade C (weak earnings). SPIKE at 16:03 aligns with an earnings drop.
- **DSY** — no same-day catalyst found (searched earnings + PR + StockTitan/Benzinga). Prior news is stale (AI business Jan/Feb 2026, 1-for-20 reverse split Feb 2026). Provisional **no catalyst found**.

**Notes:**
- No entries (observation scan, pre-23:00 CET).
- **DSY** — strongest low-float mover (1.3M float, +80% AH, VRatio 5.6x, real two-sided book with real accumulation). Spiked 16:03→$7.16, faded to $5.15 by 16:15, quote rebuilt to ~$7 at 16:25. Total% +86.2% (under +150% ceiling). No catalyst found. Trajectory to watch at 23:00: is the rebuild holding or another fade?
- **RDGT** — low float 1.4M, +25% AH, VRatio 6.1x, real book+volume, earnings catalyst (weak). Spiked 16:03→$1.20 then faded to $0.94 (below AH ref). Early SPIKE→FADE profile. Total% +38.7%. Watch at 23:00.
- **RCEL** — thin (22-80 trades/bar), wide stale book, float 23.9M. Weak; leaning skip.
- Both DSY and RDGT spiked at 16:03 ET (very early). Early-peak-then-fade is 0/6+ for PM continuation — the 23:00 decision hinges on whether either is holding/building vs still fading. DSY's ~$7 quote rebuild is the thing to confirm at 23:00.

## Scan 22:45 CET (4:45 PM ET)

Observation-only scan (~45 min into AH; before 23:00 CET → no entries). `scan.py --all` returned **9 AH hits**; five above the +10% AH threshold: DSY, FNKO, RCEL, ZYBT, RDGT.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| DSY | [TV](https://www.tradingview.com/chart/?symbol=DSY) | $3.45 | +3.3% | +89.6% | $6.54 | +95.8% | 2.6M | 400K | 6.5x | 1.3M | Miscellaneous |
| FNKO | [TV](https://www.tradingview.com/chart/?symbol=FNKO) | $5.28 | -6.2% | +18.4% | $6.25 | +11.0% | 879K | 1.3M | 0.7x | 40.0M | Recreational Products |
| RCEL | [TV](https://www.tradingview.com/chart/?symbol=RCEL) | $4.75 | +6.3% | +17.4% | $5.58 | +24.8% | 64K | 135K | 0.5x | 23.9M | Medical Specialties |
| ZYBT | [TV](https://www.tradingview.com/chart/?symbol=ZYBT) | $2.09 | -11.4% | +15.3% | $2.41 | +2.1% | 180K | 7.9M | 0.0x | 7.7M | Biotechnology |
| RDGT | [TV](https://www.tradingview.com/chart/?symbol=RDGT) | $0.79 | +10.7% | +10.7% | $0.87 | +22.5% | 7.4M | 1.1M | 6.9x | 1.4M | Medical Distributors |

**Instrumentation (AH change >10%):**
- `SPIKE-BAR: DSY 2026-08-06 SPIKE 16:03ET +20% $4.14 32 trades / 3k sh (first co-spike bar) (as-of 16:45ET)`
- `CONFIRM-3: DSY 2026-08-06 NO ignition 16:05ET failed third-bar hold/volume as-of 16:45ET`
- `SPIKE-BAR: RDGT 2026-08-06 SPIKE 16:03ET +35% $1.07 783 trades / 186k sh (first co-spike bar) (as-of 16:45ET)`
- `CONFIRM-3: RDGT 2026-08-06 NO no local-volume new-high ignition as-of 16:45ET`
- `SPIKE-BAR: FNKO 2026-08-06 SPIKE 16:23ET +24% $6.56 45 trades / 7k sh (first co-spike bar) (as-of 16:45ET)`
- `CONFIRM-3: FNKO 2026-08-06 NO ignition 16:20ET failed third-bar hold/volume as-of 16:45ET`
- `SPIKE-BAR: ZYBT 2026-08-06 SPIKE 16:29ET +17% $2.45 295 trades / 33k sh (first co-spike bar) (as-of 16:45ET)`
- `CONFIRM-3: ZYBT 2026-08-06 NO no local-volume new-high ignition as-of 16:45ET`
- `SPIKE-BAR: RCEL 2026-08-06 NO-SPIKE peak +19% @16:06ET (no bar cleared +15% on a volume co-spike) (as-of 16:45ET)`
- `CONFIRM-3: RCEL 2026-08-06 NO no local-volume new-high ignition as-of 16:45ET`

**SIP volume + book (20:00Z = 16:00 ET open):**

| Ticker | AH bars (vwap/trades/vol) | Quote (bid / ask) | Book | Verdict |
|--------|--------------------------|-------------------|------|---------|
| DSY | 20:05 $5.83/14,184/802K, 20:10 $6.21/12,868/811K, 20:15 $5.45/7,712/469K, **20:20 $6.32/13,092/925K (H $7.25, new high)**, 20:25 $6.83/12,329/753K, 20:30 $6.53/6,352/330K | $7.90 x100 / $8.13 x100 | two-sided liquid | **BUILD/reclaim** — faded to $5.15 by 16:15 then made a NEW AH high $7.25 at 16:20 on 925K sh, held $6.5-7 through 16:30, quote now ~$8. Real sustained accumulation. |
| RDGT | 20:05 $1.05/12,291/2.87M, 20:10 $1.00/6,814/1.73M, 20:15 $1.05/7,571/1.73M, 20:20 $0.94/3,639/781K, 20:25 $0.91/1,196/278K, 20:30 $0.85/1,536/319K | $0.81 x3000 / $0.88 x500 | two-sided | **SPIKE→FADE** — peaked $1.20 at 16:05, steady decline to $0.85-0.88, volume/trades fading each bar. |
| FNKO | 20:20 $6.44/391/136K, 20:25 $6.52/338/31K, 20:30 $6.23/252/19K | $6.07 x100 / $6.45 x100 | two-sided | Late ignition 16:20 to $6.88 then fade to $6.23; float 40M (high), volume thin post-spike. Weak. |
| ZYBT | 20:20 $2.23/346/45K, 20:25 $2.32/489/62K, 20:30 $2.24/416/55K | $1.76 x100 / $2.39 x100 (stale 16:00) | wide/thin | Slow grind $2.05→$2.38, VRatio 0.0 (AH vol << avg). Modest, thin book. |

**Notes:**
- No entries (observation scan, pre-23:00 CET).
- **DSY** — the standout. Low float 1.3M, VRatio 6.5x, real two-sided liquid book (bid $7.90 x100 / ask $8.13 x100). Critically, it is **not** a spike→fade: after the early 16:03 spike faded to $5.15, it made a **new AH high $7.25 at 16:20 ET** on 925K sh / 13k trades and held $6.5-7 through 16:30, with the quote now ~$8. This is a BUILD/reclaim profile that keeps making new highs into the entry window. No catalyst found (searched at 22:30). At quote ~$8 the extension is ~+130% off close $3.45 — under the +150% ceiling but rising; if it pushes past +150% by 23:00 it becomes a CEILING-OVERRIDE WATCH candidate (post-17:00 high, holding within 20%, VRatio >5x all hold). **Primary entry candidate for the 23:00 scan** if the book stays two-sided and it holds/builds.
- **RDGT** — SPIKE→FADE (peaked $1.20 16:05, now $0.85-0.88 below AH ref, volume fading). Earnings catalyst is weak (net loss). Early-peak fade is 0/6+ for PM continuation. Leaning skip.
- **FNKO** — float 40M, thin post-spike volume, late spike-fade. Weak.
- **ZYBT** — VRatio 0.0, slow grind, thin/wide book, Day -11.4%. Weak.
- **RCEL** — NO-SPIKE, thin. Weak.
- Next scan 23:00 CET is the first entry-eligible scan. DSY needs to (1) keep a two-sided fillable book and (2) hold/build near its AH high; RDGT/FNKO/ZYBT/RCEL currently all fail trajectory or liquidity.

## Scan 23:00 CET (5:00 PM ET)

First entry-eligible scan. `scan.py --all` returned **8 AH hits**; four above the +10% AH threshold: DSY, CELZ, FNKO, RCEL. RDGT dropped below (+7.4%).

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| DSY | [TV](https://www.tradingview.com/chart/?symbol=DSY) | $3.45 | +3.3% | +112.8% | $7.34 | +119.8% | 3.8M | 571K | 6.6x | 1.3M | Miscellaneous |
| CELZ | [TV](https://www.tradingview.com/chart/?symbol=CELZ) | $1.15 | +71.9% | +17.4% | $1.35 | +101.9% | 3.0M | 30.8M | 0.1x | 4.7M | Medical Specialties |
| FNKO | [TV](https://www.tradingview.com/chart/?symbol=FNKO) | $5.28 | -6.2% | +17.4% | $6.20 | +10.1% | 898K | 1.3M | 0.7x | 40.0M | Recreational Products |
| RCEL | [TV](https://www.tradingview.com/chart/?symbol=RCEL) | $4.75 | +6.3% | +11.8% | $5.31 | +18.8% | 71K | 136K | 0.5x | 23.9M | Medical Specialties |

**Instrumentation (DSY, primary candidate):**
- `SPIKE-BAR: DSY 2026-08-06 SPIKE 16:03ET +20% $4.14 32 trades / 3k sh (first co-spike bar) (as-of 17:00ET)`
- `CONFIRM-3: DSY 2026-08-06 NO ignition 16:05ET failed third-bar hold/volume as-of 17:00ET`

**SIP volume + book (DSY, 20:00Z = 16:00 ET open):**

DSY SIP bars show real sustained accumulation building past the early spike: 16:05 $5.83/14,184/802K, 16:10 $6.21/12,868/811K, 16:15 faded to $5.15, then **new highs**: 16:20 $6.32/13,092/925K (H $7.25), 16:25 $6.83/12,329/753K, 16:35 $7.27/11,194/725K (H $7.95), 16:40 $7.69/10,672/679K (H $8.21), 16:45 $7.34/6,098/384K (C $7.50). Quote: **bid $7.90 x100 / ask $8.13 x100 @ 20:40:38Z** — real two-sided liquid book, fresh (stamped 16:40 ET, ~5 min before scan).

**Catalyst search (DSY):** Big Tree Cloud Holdings. No same-day catalyst found (searched earnings + PR across 3 queries incl. tavily). FY2024 financials are stale. **No catalyst found** → Grade None.

**Decision: ENTER DSY.** Clears all gates:
- Float 1.3M (ideal <10M), VRatio 6.6x (>5x)
- AH >10% in **3 AH scans** (22:30 +80.3%, 22:45 +89.6%, 23:00 +112.8%) — 2-scan gate met
- Day% +3.3% (well above -15%, not a dead-cat)
- Total% +119.8% at scanner price / ~+136% at ask $8.13 — **under +150% ceiling**
- **BUILD/reclaim trajectory**: faded early spike to $5.15 then made repeated new AH highs ($7.25→$7.95→$8.21) into the entry window, holding within 20% of high. Not a spike→fade.
- Real fresh two-sided liquid book, tradable=true
- No catalyst (concern noted per no-catalyst handling — enter, Grade None, exit at first PM opportunity)

**Other candidates (skipped):**
- **CELZ** — Day +71.9% is a **regular-session** mover; AH +17.4% appears for the first time in AH this scan (not in 22:30/22:45 AH scans) → **fails 2-AH-scan gate**. VRatio 0.1 (AH vol 3M << 30.8M avg). Also traded/exited earlier today. Skip.
- **FNKO** — float 40M (high), VRatio 0.7 (AH vol below avg), late spike→fade, Total% only +10.1%. Skip: weak/thin, high float.
- **RCEL** — thin (22-80 trades/bar), NO-SPIKE, float 23.9M, VRatio 0.5, fading (17.4%→11.8%). Skip: thin liquidity + fade.
- **RDGT** — dropped to +7.4% AH (below threshold), SPIKE→FADE from 16:05. Skip.

**Order:** BUY 12 DSY @ limit $8.18 ext (id 5d6d5ed6) → **filled @ $7.10** (price improvement; book had lower fill). 12 sh × $7.10 = $85.20. Grade None. Added to OPEN_POSITIONS.md.

## Scan 23:30 CET (5:30 PM ET)

Entry-eligible scan. `scan.py --all` returned **14 AH hits**; above the +10% AH threshold: CELZ, DSY (held), FNKO, BYAH, SUGP, RCEL, GWH, VATE, PDSB. DSY already entered at 23:00 (managed separately). Focus: new AH names not previously >10% in an AH scan.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| CELZ | [TV](https://www.tradingview.com/chart/?symbol=CELZ) | $1.15 | +71.9% | +22.6% | $1.41 | +110.8% | 8.0M | 31.3M | 0.3x | 4.7M | Medical Specialties |
| DSY | [TV](https://www.tradingview.com/chart/?symbol=DSY) | $3.45 | +3.3% | +98.0% | $6.83 | +104.5% | 4.8M | 720K | 6.7x | 1.3M | Miscellaneous |
| BYAH | [TV](https://www.tradingview.com/chart/?symbol=BYAH) | $3.22 | +21.9% | +27.4% | $4.10 | +55.3% | 608K | 1.7M | 0.4x | 4.2M | Household/Personal Care |
| VATE | [TV](https://www.tradingview.com/chart/?symbol=VATE) | $7.41 | -2.0% | +48.2% | $10.98 | +45.2% | 36K | 97K | 0.4x | 5.1M | Engineering & Construction |
| SUGP | [TV](https://www.tradingview.com/chart/?symbol=SUGP) | $1.96 | +2.5% | +12.2% | $2.20 | +15.1% | 101K | 353K | 0.3x | 3.0M | Miscellaneous Commercial Services |
| PDSB | [TV](https://www.tradingview.com/chart/?symbol=PDSB) | $0.75 | +2.8% | +20.5% | $0.90 | +23.8% | 6K | 217K | 0.0x | 55.0M | Pharmaceuticals: Major |
| GWH | [TV](https://www.tradingview.com/chart/?symbol=GWH) | $0.68 | -7.4% | +12.6% | $0.76 | +4.3% | 66K | 461K | 0.1x | 25.0M | Electrical Products |

Below-threshold / stale (log only): ENSC +8.0%, CLRO +6.7% (stale, VChg -99% type), FNKO +16.5% (float 40M, carried skip), RCEL +11.6% (carried thin skip), EXFY/MWYN/SENS single-digit.

**Instrumentation (AH change >10%, log-only):**
- `SPIKE-BAR: BYAH 2026-08-06 SPIKE 16:59ET +15% $3.71 123 trades / 14k sh (first co-spike bar) (as-of 17:30ET)`
- `CONFIRM-3: BYAH 2026-08-06 YES ignition 16:55ET 5.6x; confirmed 17:05ET $4.07 as-of 17:30ET`
- `SPIKE-BAR: VATE 2026-08-06 SPIKE 17:05ET +52% $11.30 144 trades / 3k sh (first co-spike bar) (as-of 17:30ET)`
- `CONFIRM-3: VATE 2026-08-06 NO ignition 17:00ET failed third-bar hold/volume as-of 17:30ET`
- `SPIKE-BAR: SUGP 2026-08-06 NO-SPIKE peak +12% @17:15ET (no bar cleared +15% on a volume co-spike) (as-of 17:30ET)`
- `CONFIRM-3: SUGP 2026-08-06 NO no local-volume new-high ignition as-of 17:30ET`
- `SPIKE-BAR: GWH 2026-08-06 NO-SPIKE peak +13% @17:11ET (no bar cleared +15% on a volume co-spike) (as-of 17:30ET)`
- `CONFIRM-3: GWH 2026-08-06 NO ignition 17:00ET failed third-bar hold/volume as-of 17:30ET`
- `SPIKE-BAR: PDSB 2026-08-06 NO-SPIKE peak +20% @17:09ET (no bar cleared +15% on a volume co-spike) (as-of 17:30ET)`
- `CONFIRM-3: PDSB 2026-08-06 NO no local-volume new-high ignition as-of 17:30ET`
- `SPIKE-BAR: CELZ 2026-08-06 SPIKE 16:40ET +17% $1.35 795 trades / 379k sh (first co-spike bar) (as-of 17:30ET)`
- `CONFIRM-3: CELZ 2026-08-06 YES ignition 16:40ET 11.3x; confirmed 16:50ET $1.49 as-of 17:30ET`

**SIP volume + book (new candidates, 20:00Z = 16:00 ET open):**

| Ticker | AH bars (vwap/trades/vol) | Quote (bid / ask) | Book | Verdict |
|--------|--------------------------|-------------------|------|---------|
| BYAH | grind $3.27-3.48 to 16:50, then **ignition 17:00 $4.17/6,643/379K (H $4.60)**, 17:05 $4.15/4,536/197K, 17:10 $3.99/1,623/80K, 17:15 $3.95/1,118/78K (C $3.85) | $2.72 x100 / $3.63 x100 (stale 16:00) | two-sided (stale) | **Real late ignition** 17:00 ET on 379K sh / 6,643 trades; peaked $4.60, holding $3.85-4.18 (within ~15% of high). Quote stale-stamped 16:00 — book unconfirmed live. |
| VATE | sparse: 17:00 $10.09/153/10K, 17:05 $10.67/373/11K, 17:10 $10.99/241/16K, 17:15 $10.77/238/18K (peak $11.30) | $6.03 x100 / $8.48 x100 (stale 16:00) | thin/stale | Ignition 17:00 but **thin** (150-18K sh/bar, 8-373 trades). confirm-3 NO. |
| SUGP | grind $1.87-2.19, peak 16:45 $2.14, holding $2.10-2.18 | $1.63 x100 / $2.41 x100 (stale 16:00) | thin | NO-SPIKE, thin (6-327 trades/bar). Modest grind. |

**Catalyst search (BYAH):** Park Ha Biological Technology (renamed; ticker BYAH). Catalyst = **1-for-8 reverse stock split effective today Aug 6, 2026**. Also a securities class action was filed (Robbins LLP) and this is the **same low-float name that ran parabolic Jun 8** ($1.20→$6.49→faded to $1.05 over 3 days — classic backside). Reverse split is a structural/dilution-adjacent catalyst, not operational → **Grade C/D**, with a documented pump-and-fade history.

**Decision: NO NEW ENTRIES this scan.**
- **BYAH** — strongest new mover: low float 4.2M, real **late ignition at 17:00 ET** (379K sh / 6,643 trades), confirm-3 **YES**, holding within ~15% of its $4.60 high, Total% +55.3% (well under +150% ceiling), tradable=true. **But it appears above +10% AH for the FIRST time this scan** — at 22:00-23:00 it was flat/single-digit near close; the ignition only fired at 17:00 ET. **Fails the 2-AH-scan gate** (needs >10% AH in ≥2 AH scans). Catalyst is a reverse split (Grade C/D) on a known parabolic pump-and-fade ticker. **Strong watch for the 00:00 CET scan**: if it holds >10% AH there it clears the 2-scan gate — but weigh the weak catalyst + backside history before entering. Quote is stale-stamped 16:00; confirm a live two-sided book at 00:00 before sizing.
- **VATE** — ignition 17:00 but thin (8-373 trades/bar), confirm-3 NO, first AH scan >10% (fails gate). Watch, low conviction.
- **SUGP** — NO-SPIKE, thin grind, first AH scan >10% (fails gate). Skip.
- **PDSB** — NO-SPIKE, float 55M, AH vol 6K (near-zero real volume). Skip: thin + high float.
- **GWH** — NO-SPIKE, Total% only +4.3% (barely above close), float 25M. Skip.
- **CELZ** — Day +71.9% regular-session mover, confirm-3 YES but VRatio 0.1 (AH vol << avg), and it was already **traded and exited earlier today** (10:30 pulse). Don't re-enter same ticker. Skip.
- **FNKO / RCEL** — carried skips (high float 40M / thin 22-80 trades/bar).

DSY (entered 23:00 @ $7.10) remains the only open position; per scanner at 23:30 it's +98% AH / $6.83 (faded from the ~$8 entry-scan quote toward its scanner AH price). Position management handled in premarket eval.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
| DSY | $7.10 | 2026-08-06 23:00 CET | 12 | 5d6d5ed6 | Float 1.3M, VRatio 6.6x, AH BUILD/reclaim making new highs, 3 AH scans >10%, under +150% ceiling. No catalyst (Grade None). |

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| CELZ | $0.89 | $0.83 | -6.7% | $0.95 (PM) | 1 | None | SELL | Grade None → exit first PM opportunity. Filled @ $0.83. |
| PAVS | $6.61 | $6.65 | +0.6% | $7.98 (PM) | 1 | None | SELL | Grade None → exit first PM at any profit. Filled @ $6.65. |

**Actions taken:**
- SELL 98 CELZ @ limit $0.80 ext (id 9af1c889) filled @ $0.83 → -$5.88 (-6.7%)
- SELL 14 PAVS @ limit $6.80 ext (id b821a331) did not fill (book faded); canceled, repriced @ $6.50 (id 5c8473a1) filled @ $6.65 → +$0.56 (+0.6%)
- Both positions closed. No open positions remaining.

**Notes:**
- Alpaca quote feed stale for both names (stuck at 2026-08-05 close). Priced sells off live SIP 5Min bars, both liquid (CELZ 6754 trades/first bar, PAVS 11,528 trades/bar).
- CELZ: PM opened $0.87, spiked $0.95, faded to $0.79-0.84 (vwap $0.80-0.87). Textbook spike-and-fade.
- PAVS: PM opened $6.94, spiked $7.98 first bar then chopped $6.66-7.40. Exited near flat.
- Net pulse P&L: -$5.32.

## Position Evaluation — 14:30 CET

No open positions. Alpaca `positions` empty; equity $99,887.56, cash $99,887.56. `OPEN_POSITIONS.md` already shows all closed (CELZ, PAVS exited at 10:30 CET pulse). No reconciliation needed, nothing to evaluate.

**Actions taken:**
- None. Flat book.
