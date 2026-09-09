# Post-Market Screening - 2026-09-09

## Scan 21:30 CET (3:30 PM ET)

**REGULAR session — AH not open yet (opens 16:00 ET / 22:00 CET).** Watch-only pulse per regular-session caution rule. No paper entries. Candidates flagged pending AH confirmation; only enter if they reappear in a 22:00+ CET AH scan with sustained momentum.

Regular-session movers >10% (watch list):

| Ticker | Chg% | Price | Float | MCap | VChg% | Industry | Note |
|--------|------|-------|-------|------|-------|----------|------|
| FTFT | +82.5 | $2.39 | 5.4M | $19.3M | -99.9 | Finance/Rental/Leasing | Volume collapsed intraday — watch AH |
| SUNE | +81.6 | $4.30 | 5.4M | $28.0M | -99.9 | Engineering & Construction | Already traded+sold today (PM +3.7%); ran again into close |
| YMAT | +53.6 | $2.04 | 1.6M | $8.2M | -95.8 | Electrical Products | Low float, volume faded — watch AH |
| UFG | +32.2 | $0.76 | 9.8M | $24.7M | -100.0 | Wholesale Distributors | Volume dead — watch AH |
| SGLY | +22.2 | $1.93 | 5.1M | $10.4M | -99.4 | Air Freight/Couriers | Watch AH |
| GLMD | +17.4 | $4.49 | 1.0M | $4.7M | -80.8 | Pharma Major | Tiny float — watch AH |
| SKYE | +17.2 | $2.20 | 2.8M | $9.8M | +1501.8 | Pharma Major | Volume building into close — watch AH |
| NAUT | +16.7 | $1.08 | 66.4M | $137.8M | -99.2 | Biotechnology | High float — watch AH |
| GTBP | +15.1 | $6.03 | n/a | $10.9M | -91.0 | Pharma Major | Watch AH |
| SDA | +15.2 | $0.57 | 34.7M | $57.9M | -69.1 | Consumer Services | Watch AH |

Notes:
- Most movers show collapsed intraday volume (VChg -90%+), meaning the regular-session pop already faded. SKYE is the exception (VChg +1501.8%, volume building into the close).
- SUNE ran again to +81.6% after this morning's exit — no re-entry (one entry per candidate per night; already traded today).
- No spike-bar / CONFIRM-3 instrumentation this pulse — AH bars do not exist yet (AH opens 16:00 ET).
- **Action:** none. Re-scan at 22:00+ CET to see which names carry real AH liquidity.

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| SUNE | $2.95 | $3.06 | +3.7% | $3.15 | 1 | C | SELL | Grade C exit first PM pulse; filled $3.06 (liquid book, price improvement) |

**Actions taken:**
- SELL 33 SUNE @ limit $2.98 ext (id 7f06a2e3) filled @ $3.06 — real fill, +$3.63 (+3.7%)
- No open positions remain
- SIP PM 09-09: opened $3.11 (631K sh/5768 trades), dipped $2.80, rebuilt $3.02-3.15 (vwap $3.04). Stale Alpaca quote (ask $2.95 @20:59Z) ignored; used SIP level.

## Position Evaluation — 14:30 CET

No open positions. SUNE exited at 10:30 pulse (filled $3.06, +3.7%). Nothing to evaluate.

**Actions taken:**
- None. Flat, all cash ($99,830.84 equity). Alpaca and OPEN_POSITIONS.md agree (no positions).

## Scan 22:00 CET (4:00 PM ET)

**First AH scan — observation only** (learning-phase default: no entries before 23:00 CET). Scanner ran at 16:00:19 ET, one bar into the AH session, so no AH volume has accumulated yet.

No candidates found.

Notes:
- Scanner returned 0 hits — AH just opened, `postmarket_volume` not yet populated. Expected this early; the 21:30 watch names need a bar or two of real AH trades before they surface.
- No spike-bar / CONFIRM-3 instrumentation possible — AH 5-min bars do not exist one minute into the session.
- **Action:** none. Re-scan at 22:30 CET for the first real AH-volume read on the 21:30 watch names (FTFT, SUNE, YMAT, SKYE, etc.).

## Scan 22:15 CET (4:15 PM ET)

**AH scan — observation only** (learning-phase default: no entries before 23:00 CET). Scanner ran at 16:15 ET; returned 0 hits above the 10% AH threshold.

No candidates found by scanner. Manual SIP cross-check of the 21:30 watch names (first AH bar only; free-tier SIP lags ~15 min):

| Ticker | Close | 1st AH bar (16:00-16:05 ET) | AH vs close | Vol / trades | Read |
|--------|-------|------------------------------|-------------|--------------|------|
| YMAT | $2.04 | $2.16-2.27, C $2.16 | +6% to +11% | 159K sh / 1025 | Low float 1.6M, only real volume — but single bar, needs 22:30 confirmation |
| FTFT | $2.39 | $2.00-2.15, C $2.00 | -16% | 104K sh / 554 | Fading below close — dead-cat risk, drop |
| SKYE | $2.20 | $2.23 flat | +1% | 575 sh / 3 | Thin, no follow-through into AH |
| GLMD | $4.49 | $4.63 flat | +3% | 3K sh / 7 | Thin |

Notes:
- Scanner 0 hits: no name cleared the 10% sustained-AH threshold this early. Only one AH bar has accumulated.
- YMAT is the only watch name with real AH volume + an up-move off close, but a single bar is not the 2-AH-scan gate. FTFT already fading below its regular close (recovering-from-pop, not building).
- No spike-bar / CONFIRM-3 instrumentation — only one AH 5-min bar exists, too early for the detectors.
- **Action:** none (observation window). Re-scan at 22:30 / 23:00 CET; enter only if YMAT (or another name) reappears with sustained >10% AH across ≥2 AH scans and clears all gates.

## Scan 22:30 CET (4:30 PM ET)

**AH scan — observation only** (learning-phase default: no entries before 23:00 CET). Scanner ran at 16:30 ET, 4 hits.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| HCAI | [TV](https://www.tradingview.com/chart/?symbol=HCAI) | $4.20 | -0.5% | +23.6% | $5.19 | +23.0% | 554K | 93K | 6.0x | 3.3M | Industrial Machinery |
| FTFT | [TV](https://www.tradingview.com/chart/?symbol=FTFT) | $2.09 | +59.5% | +13.7% | $2.38 | +81.4% | 927K | 8.9M | 0.1x | 5.4M | Finance/Rental/Leasing |
| LHSW | [TV](https://www.tradingview.com/chart/?symbol=LHSW) | $1.02 | -22.7% | +10.8% | $1.13 | -14.4% | 164K | 3.1M | 0.1x | 1.0M | Computer Processing Hardware |
| AMCI | [TV](https://www.tradingview.com/chart/?symbol=AMCI) | $3.18 | -20.7% | +5.9% | $3.37 | -16.0% | 147K | 122K | 1.2x | 3.7M | Packaged Software |

**Instrumentation (log-only, no decision impact):**
- `HCAI 2026-09-09 SPIKE 16:05ET +28% $5.36 488 trades / 41k sh (first co-spike bar) (as-of 16:30ET)`
- `HCAI 2026-09-09 CONFIRM-3 NO ignition 16:05ET failed third-bar hold/volume as-of 16:30ET`
- `FTFT 2026-09-09 SPIKE 16:13ET +22% $2.54 1854 trades / 311k sh (first co-spike bar) (as-of 16:30ET)`
- `FTFT 2026-09-09 CONFIRM-3 PENDING ignition 16:10ET; waiting for third bar as-of 16:30ET`
- `LHSW 2026-09-09 NO-SPIKE peak +12% @16:14ET (no bar cleared +15% on a volume co-spike) (as-of 16:30ET)`
- `LHSW 2026-09-09 CONFIRM-3 PENDING ignition 16:10ET; waiting for third bar as-of 16:30ET`

**Per-candidate reads:**
- **HCAI** — lead watch. Fresh AH igniter (Day flat -0.5%, pure AH ignition, not dead-cat). Real SIP accumulation: 356K sh/6462 trades (16:05), 496K sh/8959 trades (16:10), 227K sh/4073 trades (16:15); VWAP $5.05-5.25 corroborates scanner $5.19 — real spike, not a bad print. Float 3.3M, VRatio 6.0x, Total% +23% (well under 150% ceiling). `tradable=true`. **Catalyst FOUND:** GlobeNewswire 2026-09-09 (~16:04 ET) — strategic cooperation framework agreement with Beyinda Limited to expand precision metal components market in China (partnership/cooperation; framework = leans Grade B/C, decide at entry). **FIRST-BAR-SPIKE:** AH high $5.55 printed 16:10 ET (first AH bar 16:00-16:15) and CONFIRM-3 reads NO — open-bar spike, needs a volume-backed new high to confirm a build vs fade. Off peak $5.55→$5.14 (-7%, still within 20%). Quote showed stale `ask $0.00 x0` @20:00:03Z (AH-open snapshot) — recheck live book at 23:00. **Needs 2nd AH scan at 23:00 to clear the gate.**
- **FTFT** — extended/multi-session risk. Already ran +59.5% in the regular session; Total% +81.4% is a day-2-type move, not a fresh day-1 igniter. Real AH volume (spike-bar 311k sh/1854 trades) but scanner VRatio 0.1x reflects the collapsed intraday base. Was fading below close at 22:15. Watch, do not chase an extended runner.
- **LHSW** — DROP. Dead-cat: Day -22.7%, AH bounce still -14.4% below prior close (Total% negative), NO-SPIKE, VRatio 0.1x. Recovering from a sell-off, not building.
- **AMCI** — DROP. AH +5.9% below the 10% threshold; dead-cat (Day -20.7%, Total% -16.0%).

**Action:** none (observation window, before 23:00 CET). HCAI is the lead entry candidate for 23:00 if it holds/rebuilds with a live fillable book across a 2nd AH scan. Re-scan at 23:00 CET.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|

_No entries this pulse — regular-session watch-only scan (AH not open)._
