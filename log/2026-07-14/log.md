# Trade Log — 2026-07-14

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| VMAR | $1.57 | $2.22 (fill) | +41.4% | $3.35 (+114%) | 1 | None | SELL | Grade None = exit at any profit. PM peaked $3.35 then dumping. |
| LVLU | $11.03 | $10.01 | -9.2% | $11.99 (+8.7%) | 1 | B | HOLD | Day 1 of 2; above -15% stop ($9.38); peak <+30% so no trail; catalyst intact. |

**Actions taken:**
- SELL 62 VMAR @ limit $2.15 ext (id edb17587) → filled **$2.22**. P&L +$40.30 (+41.4%).
- VMAR verified real via SIP: 4.5M sh in first PM bar, 37,981 trades on a 670K-float name. Peaked $3.35 at PM open, faded fast ($3.35→$2.94→$2.62→$2.23). Classic PM peak-then-dump — exited into the fade.
- LVLU held: Grade B, day 1 of 2, -9.2% is above the -15% hard stop. PM liquidity thin (7.3K sh in first PM bar). Re-evaluate at 14:30 CET pulse.

## Position Evaluation — 14:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| LVLU | $11.03 | $9.44 | -14.4% | $11.99 (+8.7%) | 1 of 2 | B | HOLD | Above -15% hard stop ($9.38); day 1 of 2; catalyst intact |

**Actions taken:**
- No sells. LVLU held per Grade B rule (hold up to 2 days).
- Data reconcile: Alpaca quote feed stale (07-13 20:00Z close, wide $6.55/$10.36 book). Used Alpaca `current_price` $9.44 (-14.4%) as P&L basis; SIP PM bars show latest ~$9.75-9.80 (-11.6%). SIP feed latest 11:55Z (07:55 ET) confirms premarket.
- LVLU never gave a PM spike above entry to exit into profit (OVN peak only +8.7%). Faded from $11.50 PM open to ~$9.75. Now sitting just above the hard stop.
- **Flag for next pulse:** if LVLU prints below $9.38, sell per Grade B hard-stop rule.

## Scan 21:30 CET (3:30 PM ET) — REGULAR session, pre-AH

AH not open yet (opens 22:00 CET / 4:00 PM ET). No paper entries per regular-session caution rule. Candidates below are **Watch — pending AH confirmation**; only actionable if they reappear in a 22:00+ CET AH scan with sustained momentum.

| Ticker | Price | Chg% | 5mVol | IRVol | Float | MCap | Industry | Note |
|--------|-------|------|-------|-------|-------|------|----------|------|
| CNEY | $0.66 | +38.2% | 278K | 293.9 | 5.0M | 3.7M | Electrical Products | Real vol + low float — watch AH |
| CRMT | $4.16 | +37.7% | 43K | 9.8 | 7.6M | 34.5M | Specialty Stores | Real vol — watch AH |
| SHPH | $4.09 | +38.3% | 11K | 180.4 | 596K | 2.6M | Pharma: Major | Untradable on Alpaca (carried, `tradable=false` all prior nights) — skip |
| NIXX | $1.47 | +28.9% | 63K | 1.2 | 24.1M | 42.8M | Personnel Services | Watch AH |
| LOOP | $1.03 | +21.6% | 25K | 5.6 | 26.5M | 49.8M | Chemicals: Specialty | Watch AH |
| NXTC | $6.04 | +176.8% | 100 | 639.9 | 2.4M | 7.9M | Pharma: Major | Thin (100 sh/5m) — likely halt artifact, monitor AH |
| LEDS | $2.17 | +42.8% | 300 | 4918.6 | 3.4M | 17.9M | Semiconductors | Thin print — monitor AH |

Rest of the 63-hit scan was thin regular-session prints (single/low-hundred share 5m vol) or downside movers (SPRO -20%). LVLU (+7.9%, $8.98) appears but is an open managed position (Grade B, day 1 of 2) handled by position-evaluation. No action here.

**Next AH scan ~22:15 CET** will re-run with real extended-hours volume/VRatio and evaluate entries.

## Scan 22:00 CET (4:00 PM ET) — AH open

**No candidates found.** Scanner returned 0 hits with real extended-hours volume.

None of the 21:30 regular-session watch candidates (CNEY, CRMT, NIXX, LOOP, NXTC, LEDS) reappeared in the AH scan — their intraday spikes did not carry into after-hours with sustained volume. Per regular-session caution rule, no entries.

First AH scan of the night; observation only per learning-phase default (no entries before 23:00 CET). Next scan ~22:30 CET.

## Scan 22:30 CET (4:30 PM ET) — AH

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| XCUR | [TV](https://www.tradingview.com/chart/?symbol=XCUR) | $1.72 | +4.2% | +39.0% | $2.39 | +44.8% | 1.2M | 179K | 6.6x | 4.2M | Biotechnology |
| BTTC | [TV](https://www.tradingview.com/chart/?symbol=BTTC) | $0.80 | +5.9% | +8.7% | $0.87 | +15.1% | 145K | 51K | 2.8x | 1.9M | Packaged Software |

**Observation only (before 23:00 CET) — no entries this scan.**

**XCUR (Exicure, Inc.) — strong watch for 23:00 entry scan:**
- **Verified real via SIP:** AH bars show genuine accumulation — 20:05Z 164K sh/1,040 trades, 20:10Z 1.27M sh/10,369 trades, 20:15Z 1.45M sh/12,099 trades. Real two-sided book (bid $2.37 x100 / ask $2.40 x100). `tradable=true`. SIP VWAP $2.36 / high $2.50 corroborates scanner AH price $2.39. Not a stale VRatio or bad print.
- **Trajectory: BUILD** — $1.72 → $2.09 → $2.39, peaked $2.50 at 20:15Z, now ~$2.38. Building across the first three AH bars, not a spike-fade. Day% +4.2% (positive — not a dead-cat bounce).
- **Total% +44.8%** — well under the +150% extension ceiling.
- **Float 4.2M** (ideal <10M range).
- **Catalyst: NONE found (4-search budget exhausted).** Distressed biotech: 66% workforce reduction + halted R&D (June), Nasdaq minimum-equity ($2.5M) non-compliance notice (June 5), plan-to-regain-compliance deadline **July 20, 2026**. No same-day PR/8-K found driving the +39% move. The looming July 20 deadline raises dilution/reverse-split risk → Grade None (exit at first opportunity) if entered. Per no-catalyst handling, enter with concern noted at 23:00+ if it holds the build.
- **Plan:** if XCUR reappears at 23:00 CET still building/holding within ~20% of its AH high, it clears all entry gates (float <50M, AH >10% across 2 AH scans, Day% > -15%, Total% < 150%, real SIP liquidity) — enter a paper trade then.

**BTTC — skip:** no fillable AH book (`ask $0.00 x0`) and AH chg only +8.7% (below the 10% threshold). Illiquid ramp.

Next scan ~23:00 CET — first entry-eligible scan of the night.
