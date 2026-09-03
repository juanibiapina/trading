
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

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|

None this scan (regular session, no entries).
