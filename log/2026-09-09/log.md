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

## Scan 22:45 CET (4:45 PM ET)

**AH scan — observation only** (learning-phase default: no entries before 23:00 CET). Scanner ran at 16:45 ET, 5 hits.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| FRTT | [TV](https://www.tradingview.com/chart/?symbol=FRTT) | $0.92 | +0.8% | +19.8% | $1.10 | +20.7% | 1.9M | 429K | 4.4x | n/a | Chemicals: Agricultural |
| HCAI | [TV](https://www.tradingview.com/chart/?symbol=HCAI) | $4.20 | -0.5% | +13.6% | $4.77 | +13.0% | 895K | 146K | 6.1x | 3.3M | Industrial Machinery |
| CULP | [TV](https://www.tradingview.com/chart/?symbol=CULP) | $3.49 | +2.0% | +16.6% | $4.07 | +19.0% | 335K | 67K | 5.0x | 11.3M | Textiles |
| UFG | [TV](https://www.tradingview.com/chart/?symbol=UFG) | $0.72 | +25.0% | +8.3% | $0.78 | +35.4% | 357K | 9.6M | 0.0x | 9.8M | Wholesale Distributors |
| LHSW | [TV](https://www.tradingview.com/chart/?symbol=LHSW) | $1.02 | -22.7% | +6.9% | $1.09 | -17.4% | 273K | 3.2M | 0.1x | 1.0M | Computer Processing Hardware |

**Instrumentation (log-only, no decision impact):**
- `FRTT 2026-09-09 SPIKE 16:27ET +30% $1.20 1715 trades / 295k sh (first co-spike bar) (as-of 16:45ET)`
- `FRTT 2026-09-09 CONFIRM-3 YES ignition 16:15ET 3517.2x; confirmed 16:25ET $1.09 as-of 16:45ET`
- `HCAI 2026-09-09 SPIKE 16:05ET +28% $5.36 488 trades / 41k sh (first co-spike bar) (as-of 16:45ET)`
- `HCAI 2026-09-09 CONFIRM-3 NO ignition 16:05ET failed third-bar hold/volume as-of 16:45ET`
- `CULP 2026-09-09 SPIKE 16:14ET +16% $4.05 209 trades / 22k sh (first co-spike bar) (as-of 16:45ET)`
- `CULP 2026-09-09 CONFIRM-3 NO ignition 16:10ET failed third-bar hold/volume as-of 16:45ET`

**Per-candidate reads:**
- **CULP** — NEW, lead entry candidate. Fresh day-1 AH igniter (Day flat +2.0%, pure AH ignition). **Catalyst FOUND (Grade B):** Culp Inc Q1 FY2027 earnings released after close today (StockTitan ~16:05 ET) — "turned a quarterly loss into a $6M profit" (earnings beat). Real SIP accumulation building: 258K sh/2937 trades (16:15), 129K sh/1591 trades (16:30, into the high); VWAP $3.79-$4.11 corroborates scanner $4.07 — real spike, not a bad print. Holding/building $4.02-4.12, AH high $4.18 at 16:15-16:20 ET (not first bar), current within ~2% of high = BUILD/hold profile. Float 11.3M (above 10M ideal, not a filter). VRatio 5.0x, Total% +19% (well under 150% ceiling). `tradable=true shortable=true`. Quote stale (`ask $4.11 @20:00:02Z` = AH-open snapshot). First AH appearance this scan — **needs 2nd AH scan at 23:00 to clear the 2-AH-scan gate.**
- **FRTT** — NEW. Fort Technology (Nasdaq: FRTT), not Frontier Communications. Real liquid AH mover: SIP 633K/428K/1095K/1248K sh per bar, thousands of trades; two-sided book bid $1.00 x100 / ask $1.03 x100. CONFIRM-3 YES (real accumulation), spike 16:27 ET. BUT **fading from the $1.20 peak (16:25 bar) to $0.98 (16:30 bar)** — early-peak-fading profile. **Catalyst:** company had an Aug 11 M&A (Logia USA 50.1% acquisition) but no confirmed *same-day* driver found in 2 searches — will re-run at 23:00. Float n/a (MCap 8.6M). `tradable=true`. First AH appearance this scan — needs 2nd AH scan; watch whether it rebuilds or keeps fading.
- **HCAI** — 2nd AH appearance (22:30 + 22:45), 2-AH-scan gate now cleared. Partnership catalyst (Beyinda framework agreement, leans Grade B/C). BUT **FIRST-BAR-SPIKE + CONFIRM-3 NO** — AH high $5.55 printed on the open bar (16:10 ET), never made a volume-backed new high; now $4.77 (off the $5.55 open peak −14%, at edge of the 20% hold band). Live book still `ask $0.00 x0` (stale @20:00 snapshot) — recheck real fillable ask at 23:00 before any entry. AH% decaying 22:30 +23.6% → 22:45 +13.6% = fading open-bar spike, not a build.
- **UFG** — DROP. AH +8.3% below the 10% threshold; VRatio 0.0x (dead AH volume). Day +25.0% was a regular-session pop that already faded.
- **LHSW** — DROP (carried). Dead-cat: Day -22.7%, AH bounce still -17.4% below prior close, AH +6.9% below threshold, VRatio 0.1x.

**Action:** none (observation window, before 23:00 CET). Lead 23:00 entry candidate is **CULP** (fresh day-1 igniter, Grade B earnings beat, BUILD/hold on real SIP volume) — enter if it reappears at 23:00 with sustained >10% AH (2nd AH scan) and a live fillable book. HCAI has cleared the gate but is a fading first-bar-open-spike with no fillable ask; FRTT needs a 2nd scan and a same-day catalyst re-check. Re-scan at 23:00 CET.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|

_No entries this pulse — regular-session watch-only scan (AH not open)._
