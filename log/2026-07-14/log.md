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
