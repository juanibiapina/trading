
## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| GELS | $1.02 | $0.86 | -15.7% | $1.10 | 1 | None | SELL | Grade None exit + below -10% hard stop ($0.918). Filled @ $0.86 |
| UFG | $0.64 | $0.61 | -4.7% | $0.75 | 1 | None | SELL | Grade None exit first PM. Filled @ $0.61 |
| TLYS | $5.15 | $4.90 | -4.9% | $5.28 (+2.5%) | 1 | B | HOLD | Day 1, above -15% stop ($4.38), no trail trigger |
| CHPT | $6.21 | $6.16 | -0.8% | $6.44 (+3.7%) | 1 | B | HOLD | Day 1, above -15% stop ($5.28), no trail trigger |

**Actions taken:**
- SELL 95 GELS @ limit $0.82 ext (id 3767dde8) filled @ $0.86. Real P&L -$15.20 (-15.7%). Grade None + hard stop.
- SELL 147 UFG @ limit $0.57 ext (id e5ee3a9e) filled @ $0.61. Real P&L -$4.41 (-4.7%). Grade None first-PM exit.
- HOLD TLYS and CHPT (Grade B, day 1, within risk params).

Note: Alpaca quotes stale (all @20:00Z prior day). Used SIP 5Min bars for exit levels; both fills got price improvement over limit.

## Position Evaluation — 14:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| CHPT | $6.21 | $6.14 | -1.1% | $6.44 | 1 | B | HOLD | Day 1 of 2, well above -15% stop ($5.28), PM held $6.10-6.20 no new high |
| TLYS | $5.15 | $4.92 | -4.5% | $5.28 | 1 | B | HOLD | Day 1 of 2, above -15% stop ($4.38), PM ranged $4.77-5.12 no new high |

Prices: SIP premarket (09-03), Alpaca quotes stale at 09-02 close, Yahoo PM blank.

**Actions taken:**
- None. Both Grade B positions within risk parameters, day 1 of 2-day hold, no stop or time-limit trigger.
- OPEN_POSITIONS.md reconciled with Alpaca (2 positions match).

# Post-Market Screening - 2026-09-03

## Scan 21:30 CET (3:30 PM ET)

REGULAR session — AH not open yet (opens 22:00 CET / 4:00 PM ET). No entries per regular-session caution. Watch names below pending AH confirmation; re-evaluate at 22:00+ scans.

| Ticker | Price | Day% | IRVol | Float | MCap | Industry | Note |
|--------|-------|------|-------|-------|------|----------|------|
| MIMI | $0.97 | +51.3% | 17.1x | 3.7M | 14.3M | Misc Commercial Svcs | Watch — low float, big intraday move |
| AEHL | $7.45 | +37.2% | 3.4x | 1.3M | 28.8M | Building Products | Watch — low float |
| GRI | $2.47 | +23.4% | 22.8x | 2.2M | 5.4M | Biotechnology | Watch — low float + high IRVol |
| CYCU | $3.75 | +23.8% | 1.6x | 3.0M | 12.1M | IT Services | Watch |
| PECE | $9.99 | +0.1% | 14.5x | 5.9M | 84.3M | Financial Conglomerates | Watch — flat price, VChg high |
| CHPT | $9.13 | +75.9% | 170x | 22.7M | 236M | Electrical Products | Held position (Grade B, day 1) — not a new entry |

Regular-session movers only. AH liquidity and real spike confirmation deferred to 22:00 CET scan. No paper trades at regular-session scan.

## Scan 22:00 CET (4:00 PM ET)

Scanner 0 hits (AH open 16:00 ET, volume not built yet). Observation-only scan — no entries before 23:00 CET per learning phase.

## Scan 22:15 CET (4:15 PM ET)

Scanner 0 hits. Observation-only (before 23:00 CET). SIP cross-check on 21:30 watch names — none igniting in AH:

| Ticker | Reg Close | AH 1st bar C | AH VWAP | Vol | Trades | Note |
|--------|-----------|--------------|---------|-----|--------|------|
| MIMI | $0.97 | $0.94 | $0.95 | 138k | 398 | Fading below close, no build |
| AEHL | $7.45 | $7.38 | $7.41 | 36k | 304 | Flat, no build |
| GRI | $2.47 | $2.25 | $2.28 | 3.7k | 9 | Thin, faded |
| CYCU | $3.75 | $3.56 | $3.58 | 5.2k | 18 | Thin, faded |

No AH ignition on any watch name. No entries. Re-check at 22:30/23:00.

No candidates found.

Carrying 21:30 watch names (MIMI, AEHL, GRI, CYCU, PECE) for AH confirmation at 22:30+ scans. None yet showing in AH scanner.

## Scan 22:30 CET (4:30 PM ET)

Observation-only (before 23:00 CET per learning phase). Scanner 4 hits:

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| PLAG | [TV](https://www.tradingview.com/chart/?symbol=PLAG) | $0.65 | +7.3% | +15.5% | $0.74 | +24.0% | 1.8M | 4.3M | 0.4x | 11.6M | Food: Specialty/Candy |
| AKAN | [TV](https://www.tradingview.com/chart/?symbol=AKAN) | $3.67 | -1.9% | +18.5% | $4.35 | +16.3% | 418K | 351K | 1.2x | 541K | Agricultural Commodities |
| CNTB | [TV](https://www.tradingview.com/chart/?symbol=CNTB) | $1.93 | -30.1% | +12.4% | $2.17 | -21.4% | 120K | 1.2M | 0.1x | 17.0M | Pharma: Major |
| CURV | [TV](https://www.tradingview.com/chart/?symbol=CURV) | $2.23 | -1.8% | +15.2% | $2.57 | +13.2% | 51K | 185K | 0.3x | 34.2M | Apparel/Footwear Retail |

**Instrumentation (log-only, no decision impact):**
- PLAG: SPIKE 16:11ET +23% $0.80 1241 trades / 446k sh. CONFIRM-3 YES ignition 16:05ET 3.9x, confirmed 16:15ET $0.79. SIP real build: 343k→1.53M→839k sh/bar, thousands of trades. Real accumulation.
- AKAN: SPIKE 16:04ET +16% $4.27 570 trades / 40k sh. CONFIRM-3 PENDING. SIP real build: 256k→331k→358k sh/bar, 4.6-6k trades/bar. Float 541K very low. Strong candidate.
- CNTB: SPIKE 16:12ET +16% $2.23 56 trades / 22k sh. CONFIRM-3 NO. Day -30.1% dead-cat, Total -21.4% still below close. Thin AH (36-169 trades/bar). Skip: dead-cat bounce.
- CURV: SPIKE 16:14ET +15% $2.57 58 trades / 8k sh. CONFIRM-3 NO. Thin (8-636 trades/bar), Float 34.2M. Weak.

No entries (observation-only scan). PLAG and AKAN both showing real volume-backed builds — track for 23:00 entry gate (need AH >10% in ≥2 AH scans). This is their first AH scan appearance. CNTB skip (dead-cat), CURV weak.

Prior watch names (MIMI, AEHL, GRI, CYCU, PECE) not in scanner this scan.

## Scan 22:45 CET (4:45 PM ET)

Observation-only (before 23:00 CET per learning phase). Scanner 7 hits:

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| PLAG | [TV](https://www.tradingview.com/chart/?symbol=PLAG) | $0.65 | +7.3% | +19.4% | $0.77 | +28.1% | 4.7M | 4.6M | 1.0x | 11.6M | Food: Specialty/Candy |
| AKAN | [TV](https://www.tradingview.com/chart/?symbol=AKAN) | $3.67 | -1.9% | +8.2% | $3.97 | +6.1% | 990K | 429K | 2.3x | 541K | Agricultural Commodities |
| GELS | [TV](https://www.tradingview.com/chart/?symbol=GELS) | $0.89 | +27.6% | +15.3% | $1.03 | +47.2% | 628K | 13.9M | 0.0x | n/a | Pharma: Major |
| AEHL | [TV](https://www.tradingview.com/chart/?symbol=AEHL) | $7.45 | +37.2% | +6.7% | $7.95 | +46.4% | 224K | 7.6M | 0.0x | 1.3M | Building Products |
| CURV | [TV](https://www.tradingview.com/chart/?symbol=CURV) | $2.23 | -1.8% | +13.5% | $2.53 | +11.5% | 208K | 203K | 1.0x | 34.2M | Apparel/Footwear Retail |
| CNTB | [TV](https://www.tradingview.com/chart/?symbol=CNTB) | $1.93 | -30.1% | +12.2% | $2.17 | -21.6% | 171K | 1.2M | 0.1x | 17.0M | Pharma: Major |
| SMTK | [TV](https://www.tradingview.com/chart/?symbol=SMTK) | $2.38 | -5.9% | +11.8% | $2.66 | +5.1% | 137K | 884K | 0.2x | 435K | Semiconductors |

**Instrumentation (log-only, no decision impact):**
- PLAG: SPIKE 16:11ET +23% $0.80 1241 trades / 446k sh. CONFIRM-3 YES ignition 16:05ET 3.9x, confirmed 16:15ET $0.79. SIP strong build: 343k→1.53M→839k→1.47M→711k→1.35M sh/bar, thousands of trades, price $0.68→$0.84 making new highs at 16:30ET. Real accumulation. **2nd AH scan** (also in 22:30). Total +28%, under ceiling, Day% +7.3%, Float 11.6M. Clears build/hold. Track for 23:00 entry gate.
- GELS: SPIKE 16:29ET +18% $1.05 1289 trades / 491k sh. CONFIRM-3 PENDING. SIP: one big bar 728k sh @16:25ET spike to $1.05, next bar 475k sh but faded C $0.96 off high. Fresh single-bar spike, early fade signal. Was a held position sold this AM -15.7%; now re-igniting. **1st AH scan today.**
- SMTK: SPIKE 16:27ET +25% $2.97 367 trades / 32k sh. CONFIRM-3 PENDING. SIP: 202k sh @16:25ET spike to $2.99, next bar faded C $2.42 (-19% off high). SPIKE→FADE already. Float 435K. **1st AH scan.**
- CURV: SPIKE 16:14ET +15% $2.57 58 trades / 8k sh. CONFIRM-3 NO. Thin (8-636 trades/bar), Float 34.2M. Weak (carried).
- CNTB: SPIKE 16:12ET +16% $2.23 56 trades / 22k sh. CONFIRM-3 NO. Day -30.1%, Total -21.6% still below close. Thin AH. Skip: dead-cat bounce.

AKAN dropped to +8.2% AH (below 10% threshold, was +18.5% at 22:30). AEHL +6.7% AH (below threshold). No entries (observation-only). PLAG is the clear volume-backed BUILD with 2 AH scans — primary 23:00 entry candidate if it holds. GELS/SMTK fresh single-bar spikes already fading; CNTB dead-cat; CURV weak.

## Scan 23:00 CET (5:00 PM ET)

Entries now allowed (learning-phase 23:00+ gate). Scanner 6 hits:

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| PLAG | [TV](https://www.tradingview.com/chart/?symbol=PLAG) | $0.65 | +7.3% | +31.8% | $0.85 | +41.5% | 8.3M | 5.0M | 1.7x | 11.6M | Food: Specialty/Candy |
| GIPR | [TV](https://www.tradingview.com/chart/?symbol=GIPR) | $0.52 | +32.6% | +12.2% | $0.59 | +48.9% | 1.7M | 42.3M | 0.0x | 2.6M | Real Estate Investment Trusts |
| GELS | [TV](https://www.tradingview.com/chart/?symbol=GELS) | $0.89 | +27.6% | +9.7% | $0.98 | +40.0% | 1.6M | 14.0M | 0.1x | n/a | Pharma: Major |
| AKAN | [TV](https://www.tradingview.com/chart/?symbol=AKAN) | $3.67 | -1.9% | +6.8% | $3.92 | +4.8% | 1.1M | 444K | 2.5x | 541K | Agricultural Commodities |
| CURV | [TV](https://www.tradingview.com/chart/?symbol=CURV) | $2.23 | -1.8% | +14.3% | $2.55 | +12.3% | 250K | 207K | 1.2x | 34.2M | Apparel/Footwear Retail |
| CNTB | [TV](https://www.tradingview.com/chart/?symbol=CNTB) | $1.93 | -30.1% | +11.4% | $2.15 | -22.1% | 199K | 1.2M | 0.2x | 17.0M | Pharma: Major |

**Instrumentation (log-only, no decision impact):**
- PLAG: SPIKE 16:11ET +23% $0.80 1241 trades / 446k sh. CONFIRM-3 YES ignition 16:05ET 3.9x, confirmed 16:15ET $0.79. SIP real accumulation: 88k→343k→1.53M→839k→1.47M→711k→1.35M→1.28M→1.20M→954k sh/bar, thousands of trades, price built $0.65→$0.89 peak 16:35 ET, now ~$0.83. Latest SIP bar 16:45 ET (~15 min lag, fresh). **3rd AH scan** (22:30 +15.5%, 22:45 +19.4%, 23:00 +31.8%) — clears 2-AH-scan gate. Real BUILD.
- GIPR: SPIKE 16:43ET +19% $0.62 748 trades / 360k sh. CONFIRM-3 PENDING. First AH scan today (Day +32.6% already ran regular session). Real 1st-bar volume but 1 AH scan only — does not clear 2-AH-scan gate yet. Watch next scan.
- CURV: SPIKE 16:14ET +15% $2.57 58 trades / 8k sh. CONFIRM-3 NO. SIP thin and fading: 22k→18k→16k→98k→34k→42k→18k→21k→5k→3k sh/bar, peaked $2.68 @16:15 ET, now $2.53. Thin drift not a build. Float 34.2M.
- CNTB: SPIKE 16:12ET +16% $2.23 56 trades / 22k sh. CONFIRM-3 NO. Day -30.1% dead-cat, Total -22.1% still below close. Thin AH.

**Decisions:**
- **PLAG — ENTER.** Clears every gate: 2-AH-scan gate (3 AH scans >10%), Total +41.5% under +150% ceiling, Day +7.3% above -15%, float 11.6M, tradable=true, real volume-backed BUILD (CONFIRM-3 YES, thousands of trades/bar). Quote showed `ask $0.00 x0` but timestamp 20:00:01Z (16:00 ET, 1h stale) — freshness guard: SIP proves a real fillable book (1.35M sh/bar), not a no-liquidity artifact. Catalyst search (3 queries): no fresh same-day catalyst — iFLYTEK contract 3 weeks old, TipRanks item Jul 16. Known speculative name (927% Aug 12 spike unwound -77% next day; this repo lost -12.2% on it 07-22). Grade None, enter with concern noted per no-catalyst learning-phase rule. Fresh day-1 AH igniter (Aug spike unwound weeks ago, not in WINNERS_TRACKING). BUY 113 @ limit $0.88 ext (id 9797f825) **filled @ $0.74** (price improvement). Fill Total% (0.74−0.65)/0.65 = +13.8%, below qualifying 22:45 Total% +28% — no chase, no CHASE-CAP concern.
- CURV — SKIP. Clears 2-AH-scan gate numerically but SIP thin and fading (5k/3k sh last bars), peaked 16:15 ET early, CONFIRM-3 NO, float 34.2M. Thin drift + SPIKE→FADE.
- GIPR — WATCH. First AH scan only, does not clear 2-AH-scan gate. Re-check next scan.
- GELS — SKIP. AH +9.7% below 10% threshold this scan; only 1 AH scan >10% (22:45). Sold this AM -15.7%; re-igniting but fails gate.
- AKAN — SKIP. Faded to +6.8% AH (was +18.5% at 22:30), fails gate.
- CNTB — SKIP. Dead-cat bounce (Day -30.1%, Total still below close), thin AH.

## Scan 23:30 CET (5:30 PM ET)

Entries allowed. Scanner 13 hits (AH >10% subset evaluated):

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| PLAG | [TV](https://www.tradingview.com/chart/?symbol=PLAG) | $0.65 | +7.3% | +12.0% | $0.72 | +20.2% | 11.7M | 5.3M | 2.2x | 11.6M | Food: Specialty/Candy |
| GIPR | [TV](https://www.tradingview.com/chart/?symbol=GIPR) | $0.52 | +32.6% | +13.6% | $0.59 | +50.7% | 9.0M | 43.1M | 0.2x | 2.6M | Real Estate Investment Trusts |
| GELS | [TV](https://www.tradingview.com/chart/?symbol=GELS) | $0.89 | +27.6% | +10.0% | $0.98 | +40.3% | 2.3M | 14.1M | 0.2x | n/a | Pharmaceuticals: Major |
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $0.63 | -39.0% | +13.6% | $0.71 | -30.7% | 1.4M | 82.6M | 0.0x | 4.4M | Misc Commercial Services |
| AKAN | [TV](https://www.tradingview.com/chart/?symbol=AKAN) | $3.67 | -1.9% | +10.9% | $4.07 | +8.8% | 1.2M | 456K | 2.7x | 541K | Agricultural Commodities |
| CURV | [TV](https://www.tradingview.com/chart/?symbol=CURV) | $2.23 | -1.8% | +14.8% | $2.56 | +12.8% | 258K | 208K | 1.2x | 34.2M | Apparel/Footwear Retail |

(Below-threshold hits: GPRO AH +6.5% / Day -17.8%, MIMI AH +5.4%, TWG +5.6%, CHPT +5.7% (held position), MODD +7.3%, INLF +6.2%, DBGI AH +7.7% / Day -18.8% — all skipped, AH <10% or Day <-15%.)

**Instrumentation (log-only, no decision impact):**
- GIPR: SPIKE 16:43ET +19% $0.62 748 trades / 360k sh. CONFIRM-3 YES ignition 16:40 ET 13.6x, confirmed 16:50 ET $0.64. SIP real accumulation: 100k→50k→39k→88k→679k→1.50M→908k→1.82M→1.32M→1.63M→486k→302k sh/bar, 1451-3706 trades/bar at peak, price $0.56→$0.67 peak 17:00 ET, now ~$0.62 (last SIP bar 17:15 ET, fresh). Real BUILD.
- AKAN: SPIKE 16:04ET +16% $4.27 570 trades / 40k sh. CONFIRM-3 NO (ignition 16:10 ET failed third-bar hold/volume). SIP faded then last-bar bounce: 213k→163k→61k→38k→46k→26k→42k→16k→13k→8k→17k→87k sh/bar. Choppy spike-fade-bounce. Float 541K.
- GELS: SPIKE 16:29ET +18% $1.05 1289 trades / 491k sh. CONFIRM-3 NO. SIP single-bar spike then fade: 728k@16:25 ET peak $1.05, faded to $0.91 (last bar). SPIKE→FADE, -13% off high.
- CURV: CONFIRM-3 NO (carried). Thin drift, Float 34.2M.
- NCPL: Day -39.0%, Total -30.7% below close — dead-cat. Skip.

**Decisions:**
- **GIPR — ENTER.** Clears every gate: 2-AH-scan gate (23:00 +12.2%, 23:30 +13.6%), Total +50.7% under +150% ceiling, Day +32.6% above -15% (up move, not dead-cat), float 2.6M ideal, tradable=true, real volume-backed BUILD (CONFIRM-3 YES, 679k-1.82M sh/bar, thousands of trades). Quote stale (ask $5.81 garbage @16:55 ET) but SIP proves a real fillable book (302k-1.82M sh/bar); freshness guard, lean on SIP. Catalyst search (2 queries): no fresh same-day catalyst — latest 8-K Apr 22 2026, no Sep PR. Grade None, enter with concern noted per no-catalyst rule. Fresh day-1 igniter (no prior WINNERS_TRACKING entry). BUY 151 @ limit $0.66 ext (id f84519c6) **filled @ $0.63** (price improvement). Fill Total% (0.63−0.392)/0.392 = +60.7% vs qualifying +50.7% — small chase gap +10pts, well below the +120% fade zone, no CHASE-CAP concern.
- AKAN — SKIP (untradable). `tradable=false` broker-block (matches WINNERS_TRACKING 2026-08-13 note: DETECTED all scans but never entered, `tradable=false` + `ask $0.00 x0`). Numerically clears 2-AH-scan gate (22:30 +18.5%, 23:30 +10.9%) but can never fill. Recorded as qualified-but-untradable broker-block. Also CONFIRM-3 NO / choppy.
- GELS — SKIP. SPIKE→FADE single-bar spike faded -13% off $1.05 high to $0.91, CONFIRM-3 NO, thin VRatio 0.2. Multi-session (was held position sold this AM -15.7%).
- CURV — SKIP. Thin drift not a build, CONFIRM-3 NO, float 34.2M, peaked 16:15 ET early.
- NCPL — SKIP. Dead-cat bounce (Day -39.0%, Total still below close).

PLAG (prior entry) still holding: AH +12.0% above threshold, position now +1.2% ($0.74). No action (position mgmt is premarket).

## Scan 00:00 CET (6:00 PM ET)

Entries allowed. Scanner 15 hits (AH >10% new names evaluated):

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| MODD | [TV](https://www.tradingview.com/chart/?symbol=MODD) | $3.42 | -1.2% | +11.7% | $3.82 | +10.4% | 166K | 278K | 0.6x | 7.6M | Medical Specialties |
| STKE | [TV](https://www.tradingview.com/chart/?symbol=STKE) | $1.29 | +10.3% | +12.4% | $1.45 | +23.9% | 54K | 300K | 0.2x | 30.0M | Financial Conglomerates |

Positions carried: PLAG AH +14.7% $0.74 (Total +23.1%), GIPR AH +15.2% $0.60 (Total +52.8%) — both still above threshold, holding. Position mgmt is premarket.

Below-threshold / prior-skip hits: GPRO +5.0%, GELS +7.9%, TWG +8.6%, WETO +7.4%, CURV +15.2%/thin-drift (carried skip), CNTB +8.8% (dead-cat, now sub-threshold), INLF +9.5%, DAIC +9.3%, DBGI +6.6%; NCPL +12.6% Day -39.0% Total -31.3% dead-cat; AKAN +10.9% untradable (carried).

**Instrumentation (log-only, no decision impact):**
- MODD: SPIKE 17:04ET +15% $3.94 116 trades / 15k sh. CONFIRM-3 NO (ignition 17:00ET failed third-bar hold/volume). SIP thin: peaked $4.14 @17:35ET, faded to $3.76, max bar 53k sh / 238 trades, most bars sub-10k. Thin drift, off peak. Float 7.6M. (Known thin-drift name — Aug 27→28 faded −8.6% as false "late BUILD".)
- STKE: SPIKE 17:42ET +16% $1.50 22 trades / 3k sh. CONFIRM-3 NO (no local-volume new-high ignition). SIP very thin: peaked $1.50 @17:40ET, max bar 15k sh / 111 trades, most bars 1-8 trades. Thin. Float 30.0M.

**Decisions:**
- MODD — SKIP. First AH scan appearance, fails 2-AH-scan gate. Also thin (VRatio 0.6x, sub-10k most bars), CONFIRM-3 NO, already off peak.
- STKE — SKIP. First AH scan appearance, fails 2-AH-scan gate. Also very thin (VRatio 0.2x, single-digit trades most bars), float 30.0M.
- No new entries. Both new names fail the 2-AH-scan gate on first appearance and are thin; neither is a real volume-backed BUILD.

## Scan 00:30 CET (6:30 PM ET) — final scan

Entries allowed. Final scheduled scan. Scanner 14 hits (AH >10% names evaluated):

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| PLAG | [TV](https://www.tradingview.com/chart/?symbol=PLAG) | $0.65 | +7.3% | +22.3% | $0.79 | +31.3% | 13.4M | 5.5M | 2.4x | 11.6M | Food: Specialty/Candy |
| GIPR | [TV](https://www.tradingview.com/chart/?symbol=GIPR) | $0.52 | +32.6% | +16.6% | $0.61 | +54.6% | 12.3M | 43.4M | 0.3x | 2.6M | Real Estate Investment Trusts |
| NCPL | [TV](https://www.tradingview.com/chart/?symbol=NCPL) | $0.63 | -39.0% | +15.2% | $0.72 | -29.7% | 2.9M | 82.8M | 0.0x | 4.4M | Misc Commercial Services |
| AKAN | [TV](https://www.tradingview.com/chart/?symbol=AKAN) | $3.67 | -1.9% | +14.4% | $4.20 | +12.3% | 1.4M | 487K | 3.0x | 541K | Agricultural Commodities |
| CURV | [TV](https://www.tradingview.com/chart/?symbol=CURV) | $2.23 | -1.8% | +12.8% | $2.51 | +10.8% | 305K | 214K | 1.4x | 34.2M | Apparel/Footwear Retail |
| MODD | [TV](https://www.tradingview.com/chart/?symbol=MODD) | $3.42 | -1.2% | +14.6% | $3.92 | +13.3% | 207K | 282K | 0.7x | 7.6M | Medical Specialties |

(Below-threshold / carried hits: GPRO AH +5.0% / Day -17.8%, TWG +6.2%, WETO +6.5% / Day -18.1%, CNTB +7.3% (dead-cat, sub-threshold), EVTL +5.8%, INLF +9.5%, DAIC +5.4%, DBGI +8.5% / Day -18.8% — all skipped, AH <10% or Day <-15%.)

**Instrumentation (log-only, no decision impact):**
- MODD: SPIKE 17:04ET +15% $3.94 116 trades / 15k sh. CONFIRM-3 NO ignition 17:00ET failed third-bar hold/volume. SIP thin drift: peak bar 21:05Z (17:05ET) 53k sh / 238 trades, most bars 6-13k sh / 26-100 trades, VRatio 0.7x. Latest SIP bar 18:15ET (fresh). Price drifted $3.42→$3.95 but per-bar volume never accumulated (hundreds of trades / tens-of-K sh, not thousands / hundreds-of-K). Thin drift, not a build.
- CURV: CONFIRM-3 NO no local-volume new-high ignition (carried). Thin drift, float 34.2M, peaked 16:15ET early.

**Decisions:**
- MODD — SKIP. Now clears the 2-AH-scan gate numerically (00:00 +11.7%, 00:30 +14.6%) but SIP per-bar volume is thin drift, not accumulation (peak 53k sh / 238 trades, most bars sub-13k sh). Rising Total% with thin per-bar SIP volume = thin drift, not a BUILD. CONFIRM-3 NO. Known fader (Aug 27→28 -8.6% as false "late BUILD"). Thin-drift skip.
- CURV — SKIP. Clears 2-AH-scan gate numerically but thin drift, CONFIRM-3 NO, float 34.2M, early peak 16:15ET (carried skip).
- AKAN — SKIP (untradable, carried). `tradable=false` broker-block, `ask $0.00 x0`. Qualified-but-untradable. CONFIRM-3 NO / choppy.
- NCPL — SKIP. Dead-cat (Day -39.0%, Total -29.7% still below close).
- No new entries. No fresh late igniter this final scan — every AH >10% name is a carried skip (untradable, thin drift, or dead-cat). No FINAL-SCAN-GATE-BLOCK case (no name clears all rules except the gate with real volume-backed late ignition). No feed-lag rescue (no pipeline name under-reported by TradingView with SIP above threshold on real accumulation).

**Positions carried (mgmt is premarket, no action here):** PLAG 113 @ $0.74 now $0.82 (+11.3%), AH +22.3% / Total +31.3% still building. GIPR 151 @ $0.63 now $0.62 (-1.5%), AH +16.6% / Total +54.6% holding above threshold.

Night summary: 2 entries (PLAG @ $0.74, GIPR @ $0.63), both Grade None real volume-backed AH BUILDs cleared the 2-AH-scan gate under the +150% ceiling. No entries at the final scan.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
| PLAG | $0.74 | 23:00 CET (5:00 PM ET) | 113 | 9797f825 | Grade None — real volume-backed AH BUILD, cleared 2-AH-scan gate, Total +41.5% under ceiling, no fresh catalyst (concern noted). |
| GIPR | $0.63 | 23:30 CET (5:30 PM ET) | 151 | f84519c6 | Grade None — REIT, real volume-backed AH BUILD (679k-1.82M sh/bar), cleared 2-AH-scan gate, Total +50.7% under ceiling, float 2.6M, no fresh catalyst (concern noted). |
