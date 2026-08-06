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

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|

_No entries — regular-session scan, AH not yet open._

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
