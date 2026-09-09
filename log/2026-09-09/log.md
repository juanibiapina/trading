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

## Scan 23:00 CET (5:00 PM ET)

**AH scan — ENTRIES ALLOWED** (learning-phase default: entries permitted at 23:00+ CET). Scanner ran at 17:00 ET, 6 hits.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| UFG | [TV](https://www.tradingview.com/chart/?symbol=UFG) | $0.72 | +25.0% | +17.7% | $0.85 | +47.1% | 5.2M | 10.1M | 0.5x | 9.8M | Wholesale Distributors |
| FRTT | [TV](https://www.tradingview.com/chart/?symbol=FRTT) | $0.92 | +0.8% | +6.0% | $0.97 | +6.8% | 3.5M | 605K | 5.9x | n/a | Chemicals: Agricultural |
| FTFT | [TV](https://www.tradingview.com/chart/?symbol=FTFT) | $2.09 | +59.5% | +14.5% | $2.39 | +82.6% | 1.9M | 9.0M | 0.2x | 5.4M | Finance/Rental/Leasing |
| HCAI | [TV](https://www.tradingview.com/chart/?symbol=HCAI) | $4.20 | -0.5% | +16.2% | $4.88 | +15.6% | 1.0M | 169K | 6.1x | 3.3M | Industrial Machinery |
| CULP | [TV](https://www.tradingview.com/chart/?symbol=CULP) | $3.49 | +2.0% | +13.5% | $3.96 | +15.8% | 544K | 93K | 5.9x | 11.3M | Textiles |
| PHGE | [TV](https://www.tradingview.com/chart/?symbol=PHGE) | $1.62 | +4.5% | +5.6% | $1.71 | +10.3% | 79K | 317K | 0.2x | 2.3M | Biotechnology |

**Instrumentation (log-only, no decision impact):**
- `HCAI 2026-09-09 SPIKE 16:05ET +28% $5.36 488 trades / 41k sh (first co-spike bar) (as-of 17:00ET)`
- `HCAI 2026-09-09 CONFIRM-3 NO ignition 16:05ET failed third-bar hold/volume as-of 17:00ET`
- `CULP 2026-09-09 SPIKE 16:14ET +16% $4.05 209 trades / 22k sh (first co-spike bar) (as-of 17:00ET)`
- `CULP 2026-09-09 CONFIRM-3 NO ignition 16:10ET failed third-bar hold/volume as-of 17:00ET`
- `FTFT 2026-09-09 SPIKE 16:13ET +22% $2.54 1854 trades / 311k sh (first co-spike bar) (as-of 17:00ET)`
- `FTFT 2026-09-09 CONFIRM-3 NO ignition 16:10ET failed third-bar hold/volume as-of 17:00ET`

**Per-candidate reads:**
- **CULP — ENTERED (Grade B).** Fresh day-1 AH igniter (Day +2.0%, pure AH ignition). Cleared the 2-AH-scan gate (22:45 +16.6% → 23:00 +13.5% AH; Total% +19.0% → +15.8%). **Catalyst Grade B:** Culp Inc Q1 FY2027 earnings after close — turned a quarterly loss into a $6M profit (earnings beat). Real SIP accumulation: 258K sh/2937 trades (16:15, into the AH high $4.18), holding $3.96-4.12 across 16:15-16:45 (VWAP $3.98-4.11 corroborates scanner $3.96 — not a bad print). Current ~$3.98 = -4.8% off AH high = **BUILD/hold**. Float 11.3M (above 10M ideal, not a filter). VRatio 5.9x, Total% +15.8% (well under 150% ceiling). `tradable=true shortable=true`. CONFIRM-3 reads NO but that is log-only instrumentation, not a gate. **BUY 24 @ limit $4.15 ext (id b3754b0e) filled @ $4.10.** CHASE-CAP: qualifying AH $4.07/+19.0% → fill $4.10/+17.5%, chase gap -1.5pp (fill below qualifying, no chase). MULTI-SESSION check: not in WINNERS_TRACKING, Day flat = fresh day-1 igniter.
- **HCAI — ENTERED (Grade C).** Cleared the 2-AH-scan gate 3× (22:30 +23.6% → 22:45 +13.6% → 23:00 +16.2% AH). Fresh igniter (Day -0.5%, not dead-cat). **Catalyst Grade C:** GlobeNewswire ~16:04 ET — strategic *cooperation framework* agreement with Beyinda Limited to expand precision metal components in China (non-binding framework = weak → C). Real SIP accumulation early (356K/496K/227K sh per bar 16:05-16:15, VWAP $5.05-5.25 corroborated). **FIRST-BAR-SPIKE:** AH high $5.55 printed 16:10 ET on the open bars, CONFIRM-3 NO — never made a volume-backed new high; bled to ~$4.90 base (16:25-16:45), volume decaying (496K → 62K → 39K sh/bar). Current $4.90 = -11% off high = still within the 20% hold band. Float 3.3M, VRatio 6.1x, Total% +15.6% (well under ceiling). `tradable=true`. Quote showed stale `ask $0.00 x0` @20:00Z (AH-open snapshot, 60 min stale) — freshness guard: HCAI traded 1M+ sh in SIP, so real liquidity exists; the $0.00 ask is a snapshot artifact, not proof of no book. Placed a limit at SIP level. **BUY 20 @ limit $5.00 ext (id 45f024ee) filled @ $4.80.** CHASE-CAP: qualifying AH $4.77/+13.0% → fill $4.80/+14.3%, chase gap +1.3pp (no chase). Concern noted: FIRST-BAR-SPIKE + CONFIRM-3 NO + decaying volume — this entry instruments whether a first-bar-open-spike that holds within 20% fades overnight.
- **FTFT — SKIP (faded intraday spike / extended runner).** Cleared the 2-AH-scan gate technically (22:30 +13.7% → 23:00 +14.5%) but Day +59.5% / Total% +82.6% is an extended, not-fresh move. Robinhood shows Sept 9 regular-session range $1.25-$3.55: FTFT ran to $3.55 intraday then faded -41% to close $2.09 **before AH even opened**. The AH bounce to $2.54 is a *lower* high than the intraday $3.55 = spike→fade, not a fresh BUILD. Catalyst is non-binding framework agreements (TransGen SC Tech acquisition + S1Quant crypto-asset-management) = Grade C. Dilution history: 1-for-4 reverse split Aug 26, offshore equity financing Aug 4. Faded intraday spike + extended + Grade C + dilution → skip.
- **UFG — DROP.** Only 1 AH scan >10% (this scan +17.7%; 22:45 was +8.3% below threshold) → 2-AH-scan gate NOT cleared. VRatio 0.5x (AH volume not real), Day +25.0% was a regular-session pop that faded.
- **FRTT — DROP.** AH +6.0% below the 10% threshold this scan (was +19.8% at 22:45, now faded). Early-peak-fading; dropped below threshold.
- **PHGE — DROP.** AH +5.6% below the 10% threshold. VRatio 0.2x (AH volume not real).

**Action:** Entered **CULP** (Grade B earnings beat, fresh day-1 BUILD/hold) and **HCAI** (Grade C framework partnership, cleared gate, FIRST-BAR-SPIKE holding within 20%). Both real Alpaca fills. Skipped FTFT (faded intraday spike, extended, dilution). Position management (hold/sell) handled by premarket position-evaluation pulse.

## Scan 23:30 CET (5:30 PM ET)

**AH scan — ENTRIES ALLOWED.** Scanner ran at 17:30 ET, 6 hits.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| UFG | [TV](https://www.tradingview.com/chart/?symbol=UFG) | $0.72 | +25.0% | +12.5% | $0.81 | +40.6% | 9.6M | 10.6M | 0.9x | 9.8M | Wholesale Distributors |
| FTFT | [TV](https://www.tradingview.com/chart/?symbol=FTFT) | $2.09 | +59.5% | +34.9% | $2.82 | +115.3% | 5.6M | 9.4M | 0.6x | 5.4M | Finance/Rental/Leasing |
| CULP | [TV](https://www.tradingview.com/chart/?symbol=CULP) | $3.49 | +2.0% | +17.8% | $4.11 | +20.2% | 713K | 113K | 6.3x | 11.3M | Textiles |
| PHGE | [TV](https://www.tradingview.com/chart/?symbol=PHGE) | $1.62 | +4.5% | +9.3% | $1.77 | +14.2% | 137K | 324K | 0.4x | 2.3M | Biotechnology |
| DPU | [TV](https://www.tradingview.com/chart/?symbol=DPU) | $2.05 | +1.0% | +7.8% | $2.21 | +8.9% | 82K | 850K | 0.1x | 1.7M | Miscellaneous Commercial Services |
| TSSI | [TV](https://www.tradingview.com/chart/?symbol=TSSI) | $8.33 | -3.8% | +6.5% | $8.87 | +2.4% | 65K | 746K | 0.1x | 25.7M | Information Technology Services |

**Instrumentation (log-only, no decision impact):**
- `UFG 2026-09-09 SPIKE 16:30ET +15% $0.83 881 trades / 255k sh (first co-spike bar) (as-of 17:30ET)`
- `UFG 2026-09-09 CONFIRM-3 YES ignition 16:25ET 7.2x; confirmed 16:35ET $0.84 as-of 17:30ET`
- `FTFT 2026-09-09 SPIKE 16:13ET +22% $2.54 1854 trades / 311k sh (first co-spike bar) (as-of 17:30ET)`
- `FTFT 2026-09-09 CONFIRM-3 NO ignition 16:10ET failed third-bar hold/volume as-of 17:30ET`
- `CULP 2026-09-09 SPIKE 16:14ET +16% $4.05 209 trades / 22k sh (first co-spike bar) (as-of 17:30ET)`
- `CULP 2026-09-09 CONFIRM-3 NO ignition 16:10ET failed third-bar hold/volume as-of 17:30ET`

**Per-candidate reads:**
- **UFG — ENTERED (Grade B).** NEW qualifier: cleared the 2-AH-scan gate (23:00 +17.7% → 23:30 +12.5% AH, both >10%). Day +25.0% (positive, not dead-cat). **Catalyst Grade B:** Uni-Fuels Holdings (Singapore marine-fuel trader) H1 2026 record results — revenue +72%, guidance raised (GlobeNewswire/StockTitan today). Fresh day-1 igniter (last traded 09-02 was Grade None, no catalyst; today has a real earnings catalyst). Real SIP accumulation, not a bad print: 2.46M sh/7751 trades (20:30Z, ignition), 1.24M–1.62M sh/bar sustained through 20:50Z, VWAP $0.78–0.88 corroborates scanner $0.81. AH high $0.92 @16:45 ET, stabilized $0.79–0.82 base since (-13% off high, within 20% hold band). Float 9.8M, Total% +40.6% (well under 150% ceiling). `tradable=true`. Quote stale (`bid $0.62 / ask $0.83 @20:00Z`, 90 min behind) — freshness guard: 1M+ sh/bar SIP proves real liquidity, used SIP level. **BUY 118 @ limit $0.85 ext (id 9afbc7bc) filled @ $0.81.** CHASE-CAP: qualifying AH $0.81/+40.6% → fill $0.81/+40.6%, no chase. MULTI-SESSION check: not in WINNERS_TRACKING, Day move is same-day earnings-driven = fresh day-1 igniter.
- **FTFT — SKIP (carried; faded intraday spike / extended runner + dilution).** Skip stands from 23:00. AH% jumped to +34.9% (from +14.5% at 23:00) = discontinuous feed-lag artifact, not real. Day +59.5% / Total% +115.3% is a day-2-type extended move; ran to $3.55 intraday then faded -41% to close before AH opened. CONFIRM-3 NO. Grade C framework agreements + dilution history (1-for-4 reverse split Aug 26, offshore equity financing). Extended + faded + Grade C + dilution → skip.
- **CULP — already entered at 23:00 (Grade B).** Still qualifying (AH +17.8%, Total% +20.2%, VRatio 6.3x). No re-entry (one entry per candidate per night). Position management handled premarket.
- **PHGE — DROP.** AH +9.3% below the 10% threshold. VRatio 0.4x (AH volume not real).
- **DPU — DROP.** AH +7.8% below threshold. VRatio 0.1x.
- **TSSI — DROP.** AH +6.5% below threshold, Day -3.8%, VRatio 0.1x.

**Action:** Entered **UFG** (Grade B earnings beat — revenue +72%/guidance raised, fresh day-1 igniter, cleared 2-AH-scan gate, real SIP volume, holding within 20% of AH high). Real Alpaca fill. Open positions now: CULP, HCAI, UFG. Position management handled by premarket position-evaluation pulse.

## Scan 00:00 CET (6:00 PM ET)

**AH scan — ENTRIES ALLOWED.** Scanner ran at 18:00 ET, 10 hits.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| UFG | [TV](https://www.tradingview.com/chart/?symbol=UFG) | $0.72 | +25.0% | +13.9% | $0.82 | +42.4% | 10.5M | 10.7M | 1.0x | 9.8M | Wholesale Distributors |
| FTFT | [TV](https://www.tradingview.com/chart/?symbol=FTFT) | $2.09 | +59.5% | +30.1% | $2.72 | +107.6% | 7.0M | 9.6M | 0.7x | 5.4M | Finance/Rental/Leasing |
| HCAI | [TV](https://www.tradingview.com/chart/?symbol=HCAI) | $4.20 | -0.5% | +8.6% | $4.56 | +8.1% | 1.2M | 195K | 6.2x | 3.3M | Industrial Machinery |
| CULP | [TV](https://www.tradingview.com/chart/?symbol=CULP) | $3.49 | +2.0% | +18.1% | $4.12 | +20.5% | 759K | 118K | 6.4x | 11.3M | Textiles |
| MIMI | [TV](https://www.tradingview.com/chart/?symbol=MIMI) | $0.94 | +3.7% | +5.1% | $0.99 | +9.0% | 320K | 23.6M | 0.0x | 8.1M | Miscellaneous Commercial Services |
| TNON | [TV](https://www.tradingview.com/chart/?symbol=TNON) | $2.44 | -27.4% | +6.6% | $2.60 | -22.6% | 215K | 2.1M | 0.1x | 551K | Medical/Nursing Services |
| PHGE | [TV](https://www.tradingview.com/chart/?symbol=PHGE) | $1.62 | +4.5% | +9.9% | $1.78 | +14.9% | 152K | 325K | 0.5x | 2.3M | Biotechnology |
| DPU | [TV](https://www.tradingview.com/chart/?symbol=DPU) | $2.05 | +1.0% | +10.2% | $2.26 | +11.3% | 106K | 853K | 0.1x | 1.7M | Miscellaneous Commercial Services |
| TSSI | [TV](https://www.tradingview.com/chart/?symbol=TSSI) | $8.33 | -3.8% | +5.0% | $8.75 | +1.0% | 74K | 747K | 0.1x | 25.7M | Information Technology Services |
| EHGO | [TV](https://www.tradingview.com/chart/?symbol=EHGO) | $0.96 | -7.3% | +5.8% | $1.02 | -1.9% | 55K | 361K | 0.2x | 4.5M | Wholesale Distributors |

**Instrumentation (log-only, no decision impact):**
- `DPU 2026-09-09 SPIKE 16:47ET +15% $2.36 90 trades / 5k sh (first co-spike bar) (as-of 18:00ET)`
- `DPU 2026-09-09 CONFIRM-3 NO no local-volume new-high ignition as-of 18:00ET`

**Per-candidate reads:**
- **CULP — already entered at 23:00 (Grade B).** Still qualifying and holding: AH +18.1%, Total% +20.5%, VRatio 6.4x — best-behaved open position, building toward AH high. No re-entry. Position management handled premarket.
- **UFG — already entered at 23:30 (Grade B).** Still qualifying: AH +13.9%, Total% +42.4%, VRatio now 1.0x. No re-entry. Position management handled premarket.
- **HCAI — already entered at 23:00 (Grade C).** AH faded to +8.6% (below the 10% threshold), Total% +8.1% — the FIRST-BAR-SPIKE + CONFIRM-3 NO fade thesis is playing out (open-bar $5.55 high → $4.56, now -18% off high, at the edge of the 20% hold band). Open position; hold/sell decision is the premarket position-evaluation pulse's job, not this entry pulse.
- **FTFT — SKIP (carried).** Faded intraday spike / extended runner + dilution. AH% now +30.1% / Total% +107.6% is a discontinuous feed-lag-driven extended move; ran $3.55 intraday then faded -41% to close before AH opened. CONFIRM-3 NO, Grade C framework agreements + dilution history. Skip stands from 23:00.
- **DPU — DROP (thin drift, gate not cleared).** AH +10.2% clears threshold this scan but this is only the 1st AH scan >10% (23:30 was +7.8%) → 2-AH-scan gate NOT cleared. SIP confirms **thin drift, not a build**: per-bar volume 2K-16K sh / tens of trades (VRatio 0.1x, sub-1x), no accumulation. SPIKE was a weak 5k-sh bar; CONFIRM-3 NO. Quote wide/stale (`bid $1.78 / ask $2.50 @20:00Z`). Rising Total% on thin per-bar volume = thin drift skip.
- **PHGE — DROP.** AH +9.9% below the 10% threshold. VRatio 0.5x (AH volume not real).
- **TNON — DROP.** Dead-cat: Day -27.4%, AH bounce still -22.6% below prior close, AH +6.6% below threshold.
- **MIMI / TSSI / EHGO — DROP.** All below the 10% AH threshold (+5.1% / +5.0% / +5.8%); MIMI/TSSI/EHGO VRatio ≤0.2x (AH volume not real), EHGO negative Total%.

**Action:** No new entries. No fresh candidate cleared the 2-AH-scan gate — DPU is a thin drift (VRatio 0.1x, 1st scan >10%), all other new names below threshold or dead-cat. Open positions unchanged: CULP (holding/building, Grade B), UFG (holding, Grade B), HCAI (fading past FIRST-BAR-SPIKE thesis, Grade C). Position management handled by premarket position-evaluation pulse. One scheduled scan remains (00:30 CET / 18:30 ET).

## Scan 00:30 CET (6:30 PM ET)

**AH scan — ENTRIES ALLOWED. Final scheduled scan of the night.** Scanner ran at 18:30 ET, 7 hits.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| UFG | [TV](https://www.tradingview.com/chart/?symbol=UFG) | $0.72 | +25.0% | +12.5% | $0.81 | +40.6% | 12.3M | 10.9M | 1.1x | 9.8M | Wholesale Distributors |
| FTFT | [TV](https://www.tradingview.com/chart/?symbol=FTFT) | $2.09 | +59.5% | +24.4% | $2.60 | +98.5% | 7.8M | 9.7M | 0.8x | 5.4M | Finance/Rental/Leasing |
| HCAI | [TV](https://www.tradingview.com/chart/?symbol=HCAI) | $4.20 | -0.5% | +13.8% | $4.78 | +13.3% | 1.2M | 199K | 6.2x | 3.3M | Industrial Machinery |
| CULP | [TV](https://www.tradingview.com/chart/?symbol=CULP) | $3.49 | +2.0% | +16.6% | $4.07 | +19.0% | 799K | 123K | 6.5x | 11.3M | Textiles |
| TNON | [TV](https://www.tradingview.com/chart/?symbol=TNON) | $2.44 | -27.4% | +5.3% | $2.57 | -23.5% | 231K | 2.1M | 0.1x | 551K | Medical/Nursing Services |
| PHGE | [TV](https://www.tradingview.com/chart/?symbol=PHGE) | $1.62 | +4.5% | +11.1% | $1.80 | +16.1% | 158K | 326K | 0.5x | 2.3M | Biotechnology |
| DPU | [TV](https://www.tradingview.com/chart/?symbol=DPU) | $2.05 | +1.0% | +7.8% | $2.21 | +8.8% | 118K | 855K | 0.1x | 1.7M | Miscellaneous Commercial Services |

**Instrumentation (log-only, no decision impact):**
- `UFG 2026-09-09 SPIKE 16:30ET +15% $0.83 881 trades / 255k sh (first co-spike bar) (as-of 18:30ET)`
- `UFG 2026-09-09 CONFIRM-3 YES ignition 16:25ET 7.2x; confirmed 16:35ET $0.84 as-of 18:30ET`
- `FTFT 2026-09-09 SPIKE 16:13ET +22% $2.54 1854 trades / 311k sh (first co-spike bar) (as-of 18:30ET)`
- `FTFT 2026-09-09 CONFIRM-3 NO ignition 16:10ET failed third-bar hold/volume as-of 18:30ET`
- `HCAI 2026-09-09 SPIKE 16:05ET +28% $5.36 488 trades / 41k sh (first co-spike bar) (as-of 18:30ET)`
- `HCAI 2026-09-09 CONFIRM-3 NO ignition 16:05ET failed third-bar hold/volume as-of 18:30ET`
- `CULP 2026-09-09 SPIKE 16:14ET +16% $4.05 209 trades / 22k sh (first co-spike bar) (as-of 18:30ET)`
- `CULP 2026-09-09 CONFIRM-3 NO ignition 16:10ET failed third-bar hold/volume as-of 18:30ET`
- `PHGE 2026-09-09 NO-SPIKE peak +14% @16:16ET (no bar cleared +15% on a volume co-spike) (as-of 18:30ET)`
- `PHGE 2026-09-09 CONFIRM-3 NO no local-volume new-high ignition as-of 18:30ET`

**Per-candidate reads:**
- **CULP — already entered at 23:00 (Grade B).** Still qualifying: AH +16.6%, Total% +19.0%, VRatio 6.5x — best-behaved open position, holding near AH high. No re-entry. Position management handled premarket.
- **UFG — already entered at 23:30 (Grade B).** Still qualifying: AH +12.5%, Total% +40.6%, VRatio 1.1x. No re-entry. Position management handled premarket.
- **HCAI — already entered at 23:00 (Grade C).** AH +13.8% back above threshold, Total% +13.3%. FIRST-BAR-SPIKE + CONFIRM-3 NO thesis still in play (open-bar $5.55 high → $4.78, -14% off high, within the 20% hold band). Open position; hold/sell is the premarket pulse's job.
- **FTFT — SKIP (carried).** Faded intraday spike / extended runner + dilution. AH% +24.4% / Total% +98.5% is a discontinuous feed-lag-driven extended move; ran $3.55 intraday then faded -41% to close before AH opened. CONFIRM-3 NO, Grade C framework agreements + dilution history. Skip stands from 23:00.
- **PHGE — DROP (thin drift, gate not cleared).** First AH scan >10% (23:00 +5.6% → 23:30 +9.3% → 00:00 +9.9% → 00:30 +11.1%), so the 2-AH-scan gate is NOT cleared at the final scan. SIP confirms thin drift, not a build: peak $1.85 @17:00 ET then fade to ~$1.77; per-bar volume tens of trades / few-K sh, single 68K-sh bar at 16:15 ET (VRatio 0.5x). NO-SPIKE, CONFIRM-3 NO. **Not a FINAL-SCAN-GATE-BLOCK** — fails the "real volume-backed late ignition" test (thin, no CONFIRM-3 YES). Rising Total% on thin per-bar volume = thin-drift skip.
- **TNON — DROP.** Dead-cat: Day -27.4%, AH bounce still -23.5% below prior close, AH +5.3% below threshold, VRatio 0.1x.
- **DPU — DROP (thin drift, carried).** AH +7.8% back below the 10% threshold (was +10.2% at 00:00). VRatio 0.1x, per-bar volume 2K-16K sh. Never cleared the 2-AH-scan gate.

**Final-scan feed-lag cross-check (pipeline names):** FRTT (dropped off the scan after peaking +19.8% at 22:45) — SIP confirms a genuine early-peak fade: $1.20 @16:25 ET → ~$0.91 @17:45 ET (back to ~close $0.92). Not under-reported by TradingView; correctly off the scan, no rescue. Other pipeline names (UFG/HCAI/CULP/FTFT) all present in the scan at their real SIP levels; no feed-lag omission this scan.

**FINAL-SCAN-GATE-BLOCK:** none. No name cleared every rule except the 2-AH-scan gate with real volume-backed late ignition — PHGE (the only fresh threshold-crosser) is a thin drift (VRatio 0.5x, NO-SPIKE, CONFIRM-3 NO), not a genuine late igniter.

**Action:** No new entries at the final scan. Open positions unchanged: CULP (Grade B, holding near AH high), UFG (Grade B, holding), HCAI (Grade C, fading past FIRST-BAR-SPIKE thesis but within 20% band). Night complete — 3 entries (CULP, HCAI, UFG). Position management (hold/sell) handled by the premarket position-evaluation pulse.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
| CULP | $4.10 | 23:00 CET (5:00 PM ET) | 24 | b3754b0e | Grade B — Q1 FY2027 earnings beat (loss→$6M profit). Fresh day-1 igniter, BUILD/hold within 5% of AH high, cleared 2-AH-scan gate, real SIP volume. |
| HCAI | $4.80 | 23:00 CET (5:00 PM ET) | 20 | 45f024ee | Grade C — Beyinda framework cooperation agreement (non-binding). Cleared 2-AH-scan gate 3×. FIRST-BAR-SPIKE + CONFIRM-3 NO, holding within 20% of AH high (concern noted). |
| UFG | $0.81 | 23:30 CET (5:30 PM ET) | 118 | 9afbc7bc | Grade B — Uni-Fuels H1 2026 earnings (revenue +72%, guidance raised). Fresh day-1 igniter, cleared 2-AH-scan gate, real SIP volume (2.46M sh ignition bar), holding within 20% of AH high. No chase (fill = qualifying level). |
