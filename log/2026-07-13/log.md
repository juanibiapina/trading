# Post-Market Screening - 2026-07-13

## Scan 21:30 CET (3:30 PM ET) — REGULAR session, pre-AH

Scanner ran during regular session (AH opens 4:00 PM ET / 22:00 CET). **No entries — regular-session caution rule.** Candidates flagged for AH confirmation; only enter if they reappear in a 22:00+ CET AH scan with sustained momentum.

Notable movers (regular-session, IRVol = intraday relative volume):

| Ticker | Price | Chg% | IRVol | Float | MCap | Industry | Note |
|--------|-------|------|-------|-------|------|----------|------|
| MIMI | $3.04 | +41.4% | 179x | 1.5M | 8.4M | Misc Commercial | Low float, high IRVol — watch AH |
| SOBR | $1.31 | +202.1% | high | 2.3M | 1.2M | Electronic Equip | Big % move, low float — watch AH |
| ACTU | $1.46 | +20.7% | 17x | 10.3M | 34.9M | Pharma Major | Watch AH |
| AURE | $1.68 | +13.5% | 95x | 10.9M | 65.0M | IT Services | Watch AH |
| EHGO | $2.24 | +36.6% | 3.7x | 2.2M | 7.2M | Wholesale Dist | Low float — watch AH |
| GEDC | $0.78 | +94.9% | 3.8x | 7.3M | 10.3M | Eng & Construction | Watch AH |
| SKYQ | $4.09 | +28.7% | 1.2x | 3.8M | 19.6M | Integrated Oil | Fading IRVol — watch AH |

Many other small % movers with negligible real volume (VChg% -99% type = stale). Full scan had 62 hits, mostly illiquid.

**Decision:** No paper trades. Regular-session scan only. Reassess at 22:00+ CET AH scans for entries.

## Scan 22:00 CET (4:00 PM ET) — AH open

Scanner (`scan.py --all`): **0 AH hits.** Observation-only scan (learning phase: no entries before 23:00 CET).

Early-AH quotes on the 21:30 watchlist (scan hit ~30s after AH open, books still forming):

| Ticker | Bid | Ask | Note |
|--------|-----|-----|------|
| MIMI | $2.51 x100 | $3.36 x100 | Wide spread, thin |
| SOBR | $0.61 x500 | $1.70 x1100 | Very wide spread, unstable |
| SKYQ | $3.43 x100 | $0.00 x0 | No AH ask (no fillable book) |
| EHGO | $1.82 x100 | $2.46 x100 | Wide spread, thin |

**Decision:** No paper trades. No scanner AH hits; watchlist books thin/unstable seconds into AH. Reassess at 22:30 / 23:00 CET.

## Scan 22:30 CET (4:30 PM ET) — AH observation

Scanner (`scan.py --all`): **3 AH hits.** Observation-only scan (learning phase: no entries before 23:00 CET).

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| JEM | [TV](https://www.tradingview.com/chart/?symbol=JEM) | $0.50 | -7.0% | +22.9% | $0.62 | +14.3% | 6.5M | 26.4M | 0.2x | 0 | Wholesale Distributors |
| SHPH | [TV](https://www.tradingview.com/chart/?symbol=SHPH) | $2.96 | +1.4% | +16.2% | $3.44 | +17.8% | 211K | 435K | 0.5x | 596K | Pharmaceuticals: Major |
| LVLU | [TV](https://www.tradingview.com/chart/?symbol=LVLU) | $8.32 | -3.7% | +27.2% | $10.58 | +22.5% | 123K | 25K | 5.0x | 1.2M | Internet Retail |

**SIP verification (bars from 20:00Z / 16:00 ET):**
- **JEM** — real high volume (1.7M→3.6M→1.6M→629K sh/bar, thousands of trades), VWAP ~$0.60 corroborates AH price. **SPIKE→FADE**: peaked 20:05 ($0.69), fading to $0.57. Catalyst: **1-for-12 reverse split effective Jul 14** (Grade D, compliance/dilution). Sub-penny, Day -7%. Skip-lean.
- **SHPH** — **BUILD** volume (2.7K→68K→194K→174K, accumulating), VWAP $3.43-3.51 corroborates. Float 596K (very low). Pharma. **No catalyst found** (latest news 07/07 insider trades; reverse-split microcap near lows). Note for 23:00.
- **LVLU** — real SIP volume, VWAP ~$10.9 corroborates AH $10.58. Float 1.2M (low). Peaked 20:05 ($11.90), mild fade to ~$11.10 but **holding within 20% of high**. Volume fading after first bar (116K→69K→59K). Catalyst: **strategic-alternatives review** announced ~16:06 ET (24 min before scan) — special committee to evaluate options to maximize stockholder value (**Grade B**, solid news, can precede acquisition). Total +22.5%, well under 150% ceiling. **Strongest candidate for 23:00 if it holds/builds.**

**Decision:** No paper trades (observation-only window). At 23:00 CET, re-evaluate: LVLU (Grade B, low float, holding) is the lead; SHPH (build, no catalyst) secondary; JEM (Grade D split, fading) skip-lean. Watch whether LVLU holds/builds vs continues fading, and whether it stays within 20% of its AH high.

## Scan 23:00 CET (5:00 PM ET) — AH, entries allowed

Scanner (`scan.py --all`): **5 AH hits.** First entry-eligible scan (learning phase: entries at 23:00+ CET).

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| SOBR | [TV](https://www.tradingview.com/chart/?symbol=SOBR) | $1.20 | +176.8% | +10.0% | $1.32 | +204.4% | 8.2M | 27.7M | 0.3x | 2.3M | Electronic Equipment |
| SHPH | [TV](https://www.tradingview.com/chart/?symbol=SHPH) | $2.96 | +1.4% | +37.8% | $4.08 | +39.7% | 1.9M | 650K | 2.9x | 596K | Pharmaceuticals: Major |
| LVLU | [TV](https://www.tradingview.com/chart/?symbol=LVLU) | $8.32 | -3.7% | +25.7% | $10.46 | +21.1% | 216K | 40K | 5.4x | 1.2M | Internet Retail |
| GMEX | [TV](https://www.tradingview.com/chart/?symbol=GMEX) | $1.87 | -11.4% | +19.3% | $2.23 | +5.7% | 202K | 1.7M | 0.1x | 0 | Specialty Stores |
| TOP | [TV](https://www.tradingview.com/chart/?symbol=TOP) | $1.84 | -12.8% | +6.5% | $1.96 | -7.1% | 57K | 401K | 0.1x | 14.3M | Investment Banks |

**Evaluation:**

- **LVLU — ENTERED.** Grade B catalyst (strategic-alternatives review, special committee, ~16:06 ET). Float 1.2M. AH >10% across 2 AH scans (22:30 +27.2%, 23:00 +25.7%). Day -3.7% (> -15%). Total +21% (under 150% ceiling). SIP bars: real volume (2021 trades first bar, VWAP ~$10.9 corroborates AH price). Peaked 16:15 ET ($11.26) but **holding/rebuilding** — Yahoo shows $10.99 at 17:00 ET, within 3% of high (hold, not fade). Passes all gates. `tradable=true`. **Filled 9 @ $11.03** (order 6c546167). Alpaca quote was stale (stuck 20:00Z) but SIP + Yahoo confirm active real AH trading; limit $11.10 filled at $11.03.
- **SHPH — QUALIFIED but NO FILL (`tradable=false` on Alpaca).** Textbook BUILD: SIP volume accumulating hard (68K→194K→174K→480K→588K→1.5M sh/bar, trades to 17,275), price $3.07→$4.94, VWAP corroborates. Float 596K. AH >10% across 2 scans (22:30 +16.2%, 23:00 +37.8%). Re-ran catalyst search: **no fresh catalyst found** (latest news 07/07 insider trades; microcap pharma near lows) — would enter as Grade None with concern noted, but Alpaca reports `tradable=false`. No fill = no position. Recording as a strong BUILD candidate the broker blocked.
- **SOBR — Skip.** Day +176.8% is a regular-session spike; AH only +10.0% (borderline, 1 AH scan). Total +204% **exceeds +150% ceiling**. VRatio 0.3x (weak — AH vol likely stale regular-session volume). Extended-entry skip.
- **GMEX — Skip.** VRatio 0.1x (stale regular-session artifact), Day -11.4%, Total only +5.7%. No real AH liquidity.
- **TOP — Skip.** VRatio 0.1x, Total -7.1% (negative), Day -12.8%. No momentum.

**Decision:** 1 entry — **LVLU** (Grade B, 9 sh @ $11.03). SHPH blocked by broker (`tradable=false`). Others skipped on ceiling / weak VRatio / no liquidity.

## Scan 23:30 CET (5:30 PM ET) — AH, entries allowed

Scanner (`scan.py --all`): **6 AH hits.** New candidate: **VMAR**.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| JEM | [TV](https://www.tradingview.com/chart/?symbol=JEM) | $0.50 | -7.0% | +10.7% | $0.56 | +3.0% | 13.8M | 27.2M | 0.5x | 0 | Wholesale Distributors |
| SHPH | [TV](https://www.tradingview.com/chart/?symbol=SHPH) | $2.96 | +1.4% | +45.3% | $4.30 | +47.3% | 5.7M | 1.2M | 4.9x | 596K | Pharmaceuticals: Major |
| VMAR | [TV](https://www.tradingview.com/chart/?symbol=VMAR) | $1.41 | +11.0% | +19.9% | $1.69 | +33.1% | 4.3M | 5.5M | 0.8x | 670K | Recreational Products |
| GMEX | [TV](https://www.tradingview.com/chart/?symbol=GMEX) | $1.87 | -11.4% | +8.6% | $2.03 | -3.8% | 1.4M | 1.8M | 0.8x | 0 | Specialty Stores |
| LVLU | [TV](https://www.tradingview.com/chart/?symbol=LVLU) | $8.32 | -3.7% | +28.7% | $10.71 | +23.9% | 248K | 44K | 5.6x | 1.2M | Internet Retail |
| TOP | [TV](https://www.tradingview.com/chart/?symbol=TOP) | $1.84 | -12.8% | +6.0% | $1.95 | -7.6% | 57K | 402K | 0.1x | 14.3M | Investment Banks/Brokers |

**Evaluation:**

- **VMAR — WATCH (new, only 1 AH scan; fails 2-AH-scan gate).** Very low float (670K), MCap 1.0M. Strong accelerating **BUILD** on real SIP volume: early AH ~$1.30-1.35, then ramping hard in the last 20 min — 21:00Z bar 1.04M sh / 6,207 trades ($1.52→$1.74), 21:05Z 1.03M sh / 6,599 trades (peak $1.78), 21:10Z 555K, 21:15Z 693K sh / 4,441 trades ($1.75). VWAP corroborates, `tradable=true`, quote bid $1.41 / ask $1.45 (IEX quote ~15 min stale; SIP shows current ~$1.75). Peaked late (17:05 ET) and still building — textbook late BUILD. Total ~+38% at $1.75 (under 150% ceiling). Catalyst search (3 queries): **no fresh same-day catalyst** — running on momentum; recent story is July 9 Fort Lauderdale property-sale plan (~$13.1M gross) plus a reverse split effective 06/17. Only in this one AH scan, so it does not yet meet the ≥2-AH-scan requirement. **If it holds/builds and reappears at 00:00 CET, it becomes entry-eligible** (would enter as Grade None with concern noted).
- **SHPH — QUALIFIED but STILL NO FILL (`tradable=false`).** BUILD strengthened further: SIP volume peaked 20:45Z 1.5M sh / 17,275 trades, price ran to $5.08 (VWAP $4.31-4.78), now $4.30-4.56. AH +45.3% across 3 AH scans. Float 596K. Re-checked `tradable` — Alpaca still reports `tradable=false`. No fill = no position. Recording again as a strong BUILD the broker blocks.
- **LVLU — HELD (open position).** AH +28.7% (up from +25.7% at 23:00). Position: 9 sh @ $11.03, now ~$10.87, P&L -1.5%. Holding near AH high, thesis intact.
- **JEM — Skip.** Grade D reverse split (effective 07/14), sub-penny, Total only +3.0%, fading.
- **GMEX — Skip.** VRatio 0.8x, Day -11.4%, Total -3.8% (negative).
- **TOP — Skip.** VRatio 0.1x, Total -7.6% (negative), Day -12.8%.

**Decision:** No new entries. VMAR is a strong BUILD but needs a 2nd AH scan to clear the gate (watch at 00:00). SHPH still broker-blocked. LVLU held. Others skipped on weak/negative momentum.

## Scan 00:00 CET (6:00 PM ET) — AH, entries allowed

Scanner (`scan.py --all`): **4 AH hits.** VMAR reappears (now 2 AH scans, entry-eligible).

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| SHPH | [TV](https://www.tradingview.com/chart/?symbol=SHPH) | $2.96 | +1.4% | +78.4% | $5.28 | +80.8% | 9.1M | 1.6M | 5.6x | 596K | Pharmaceuticals: Major |
| VMAR | [TV](https://www.tradingview.com/chart/?symbol=VMAR) | $1.41 | +11.0% | +19.1% | $1.68 | +32.3% | 6.5M | 5.7M | 1.1x | 670K | Recreational Products |
| LVLU | [TV](https://www.tradingview.com/chart/?symbol=LVLU) | $8.32 | -3.7% | +36.4% | $11.35 | +31.4% | 275K | 49K | 5.6x | 1.2M | Internet Retail |
| TOP | [TV](https://www.tradingview.com/chart/?symbol=TOP) | $1.84 | -12.8% | +6.0% | $1.95 | -7.6% | 57K | 402K | 0.1x | 14.3M | Investment Banks/Brokers |

**SIP verification (fresh, last bar 21:35Z / 17:35 ET, ~25 min lag):**

- **VMAR — ENTERED.** Now clears the ≥2-AH-scan gate (23:30 +19.9%, 00:00 +19.1%, both >10%). Float 670K (ideal, ultra-low). Day +11.0% (positive — not a dead-cat). Total +32.3% (under 150% ceiling). Real SIP volume: massive accumulation at peak (21:00Z 1.04M sh / 6,207 trades, 21:05Z 1.03M sh / 6,599 trades, peak $1.78), VWAP corroborates. Peaked 21:05Z ($1.78), consolidating $1.55–1.60 (21:35Z C $1.59 / VWAP $1.60) — within ~11% of high, **holding not fading**. Peak was 17:05 ET (before 18:30) but hold-vs-fade is primary signal; it's holding within 20%, so early peak is not disqualifying. `tradable=true`. Catalyst search (23:30, 3 queries): **no fresh same-day catalyst** — running on momentum; July 9 property-sale plan (~$13.1M) + 06/17 reverse split are the recent story. Grade None, concern noted. **Filled 62 @ $1.57** (order d02ec65c; Alpaca IEX quote stale bid $1.41/ask $1.45 @ 20:59Z, SIP shows real ~$1.59; limit $1.62 filled $1.57).
- **SHPH — QUALIFIED but STILL NO FILL (`tradable=false`).** BUILD strengthened massively: AH +78.4% at $5.28, SIP now $5.35 (21:35Z), VWAP $5.48, 906K sh / 12,168 trades that bar; earlier peaks 20:45Z 1.5M sh / 17,275 trades, 21:25Z 1.35M sh / 17,570 trades. Float 596K, VRatio 5.6x. Re-checked `tradable` — Alpaca still `tradable=false`. No fill = no position. Recording again as the strongest BUILD of the night, broker-blocked.
- **LVLU — HELD (open position).** AH +36.4% (up from +28.7% at 23:30), new AH high $11.35. Position 9 @ $11.03, now building above entry. Thesis intact (Grade B strategic-alternatives). Mgmt handled premarket.
- **TOP — Skip.** VRatio 0.1x (stale regular-session artifact), Total -7.6% (negative), Day -12.8%. No momentum, no real AH liquidity.

**Decision:** 1 new entry — **VMAR** (Grade None, 62 sh @ $1.57; ultra-low float 670K, holding BUILD, real SIP volume). SHPH still broker-blocked (`tradable=false`). LVLU held. TOP skipped.

## Scan 00:30 CET (6:30 PM ET) — AH, entries allowed

Scanner (`scan.py --all`): **6 AH hits.** New candidates: EHGO, CDTG.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| SHPH | [TV](https://www.tradingview.com/chart/?symbol=SHPH) | $2.96 | +1.4% | +83.4% | $5.43 | +86.0% | 11.1M | 1.9M | 5.8x | 596K | Pharmaceuticals: Major |
| VMAR | [TV](https://www.tradingview.com/chart/?symbol=VMAR) | $1.41 | +11.0% | +12.1% | $1.58 | +24.4% | 7.2M | 5.8M | 1.2x | 670K | Recreational Products |
| LVLU | [TV](https://www.tradingview.com/chart/?symbol=LVLU) | $8.32 | -3.7% | +29.7% | $10.79 | +24.9% | 293K | 52K | 5.7x | 1.2M | Internet Retail |
| EHGO | [TV](https://www.tradingview.com/chart/?symbol=EHGO) | $2.12 | +29.3% | +7.5% | $2.28 | +39.0% | 209K | 10.1M | 0.0x | 2.2M | Wholesale Distributors |
| CDTG | [TV](https://www.tradingview.com/chart/?symbol=CDTG) | $1.81 | +0.0% | +7.2% | $1.94 | +7.2% | 146K | 235K | 0.6x | 3.0M | Industrial Machinery |
| TOP | [TV](https://www.tradingview.com/chart/?symbol=TOP) | $1.84 | -12.8% | +5.1% | $1.93 | -8.3% | 58K | 402K | 0.1x | 14.3M | Investment Banks/Brokers |

**Evaluation:**

- **EHGO — Skip (new).** AH +7.5% is **below the 10% AH threshold** (no catalyst search triggered). VRatio 0.0x (AH vol 209K vs AvgVol 10.1M = stale/no real AH liquidity). Day +29.3% is a regular-session spike, not AH momentum. Fails the >10%-in-2-AH-scans gate on the first look.
- **CDTG — Skip (new).** AH +7.2%, **below 10% threshold.** VRatio 0.6x (weak). Day flat (+0.0%), Total +7.2%. No real AH momentum.
- **SHPH — QUALIFIED but STILL NO FILL (`tradable=false`).** Strongest BUILD of the night continues: AH +83.4% at $5.43, VRatio 5.8x, float 596K. Re-checked `tradable` — Alpaca still reports `tradable=false`. No fill = no position. Recording again as the strongest broker-blocked BUILD.
- **VMAR — HELD (open position).** AH +12.1% (down from +19.1% at 00:00 but still >10%). Position 62 @ $1.57, now $1.58, P&L +0.6%. Holding above entry, thesis intact.
- **LVLU — HELD (open position).** AH +29.7% (up from +36.4% peak read at 00:00; still strong). Position 9 @ $11.03, now $10.65, P&L -3.4%. Grade B strategic-alternatives thesis intact; premarket exit handled by position-evaluation.
- **TOP — Skip.** VRatio 0.1x (stale), Total -8.3% (negative), Day -12.8%. No momentum, no liquidity.

**Decision:** No new entries. New candidates EHGO/CDTG both below 10% AH threshold with weak/zero VRatio. SHPH still broker-blocked (`tradable=false`). VMAR and LVLU held.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
| LVLU | $11.03 | 2026-07-13 23:01 CET | 9 | 6c546167 | Grade B strategic-alternatives review; float 1.2M; holding near AH high; VRatio 5.4x |
| VMAR | $1.57 | 2026-07-14 00:00 CET | 62 | d02ec65c | Grade None; ultra-low float 670K; holding BUILD (peak $1.78, consol $1.55-60); real SIP vol 1M+ sh/bar; 2 AH scans >10% |

## Morning Evaluation — 10:20 CET

### Today's Winner

**VMAR** — Recreational Products (Vision Marine Technologies)
- Catalyst: **No fresh same-day catalyst** (Grade None) — momentum/short squeeze on ultra-low float. Recent story: July 9 Fort Lauderdale property-sale plan (~$13.1M gross) + reverse split effective 06/17 (weeks-old).
- Previous Close: $1.27 (07-13 regular close)
- AH last night: peak **$1.85 (+45.6%)** at 19:20 ET (01:20 CET) — BUILD across the AH session, real SIP volume (1.0M sh/bar, 6.2k trades at the 21:00Z ramp)
- Premarket now: peak **$3.35 (+163.8%)** at 04:00 ET (SIP: 4.56M sh, 37,981 trades, VWAP $2.62 — real, liquid). Now ~$2.54–2.63, fading from open.
- Hypothetical P&L (our AH entry $1.57 → PM peak $3.35): **+113%**
- Float: 670K | Market Cap: ~$1.0M

**Scanner Diagnostic:**
- Detectable at screening time? **YES**
- Best-case outcome: VMAR appeared in the 23:30, 00:00, and 00:30 CET scans and we **ENTERED it at 00:00 @ $1.57** (62 sh) once it cleared the ≥2-AH-scan gate. Detected AND selected AND it ran — the ideal path.
- Scanner gap: **none.** VMAR is a clean win for the scanner: ultra-low float (670K), real SIP volume, holding BUILD, entered on the second qualifying scan, PM continued well past the AH peak.
- Note: VMAR's AH *peak* ($1.85 @ 19:20 ET) formed in the unscanned 18:30–20:00 ET tail, but detection and entry had already happened during the scanned window on the earlier build — not a tail miss.

### Baseline Tracking

- Days tracked: **47** (was 46 + 1)
- Winners detected by scanner: **40/45 (88.9%)** — VMAR added (detected). GMM still excluded from denominator (late-AH-tail surge).
- Winner selected for paper trade: **23/45 (51.1%)** — VMAR entered. We traded the right stock.
- Target: >80% detection
- Status: **BASELINE MET**

### Retrospective Scan Results

Live PM scan (04:20 ET) top hits: **VMAR +129% ($3.23)**, SHPH +48% ($4.38), BJDX +13%. VMAR AH→PM reconstruction (Yahoo `--ah-history` + SIP bars) confirms the continuation: AH peak $1.85 → PM peak $3.35 on 4.56M sh / 38k trades. SHPH built to AH +100% ($5.86) then faded to PM +52% ($4.46) — AH was the better exit. No forced AH scan needed; SIP bars give the definitive AH footprint.

### Open Position P&L (Alpaca)

Both positions still open — exits handled by `position-evaluation.md` (10:30 / 14:30 CET), not here.

**Quote-freshness note:** The `broker.js quote` endpoint returned stale timestamps (VMAR/SHPH @ 20:59Z, LVLU @ 20:00Z last night). The `broker.js positions` `current_price` values track the live PM prints (VMAR $2.56 ≈ live PM $2.54; LVLU $10.25 ≈ Yahoo PM $10.56), so P&L below is against live PM, not the stale quote.

| Ticker | Entry | Entry Total% | Catalyst | Entry Time | PM Peak | Peak Time | Exit | P&L | P&L % | Status |
|--------|-------|--------------|----------|------------|---------|-----------|------|-----|-------|--------|
| VMAR   | $1.57 | +23.6% | None — low-float squeeze | 00:00 CET | $3.35 (SIP) | 04:00 ET | — | open | +63% (now) / +113% (peak) | 🟢 Held |
| LVLU   | $11.03 | +32.6% | B — strategic-alternatives review | 23:01 CET | $10.90 | 04:05 ET | — | open | −4.3% (now) | 🟡 Held |

**Total Realized P&L (Alpaca fills only): €0.00** (no exits yet)

### Scanner Effectiveness

- Evening scans ran: **7 of 7** (21:30, 22:00, 22:30, 23:00, 23:30, 00:00, 00:30 CET) — full coverage of the entry window.
- Candidates found: JEM, SHPH, LVLU, VMAR, SOBR, GMEX, TOP, EHGO, CDTG (9 unique)
- Retrospective matches: VMAR ✅ (entered), SHPH ✅ (qualified, broker-blocked), LVLU ✅ (entered)

### Missed Opportunities

| Ticker | AH Change | Why Missed | Would Be Profitable? |
|--------|-----------|------------|---------------------|
| SHPH | +100.7% AH peak | **Not a scanner miss** — detected in 5 scans, qualified as strongest BUILD of the night, but Alpaca `tradable=false` blocked the fill | Hypo AH-entry ~$3.45 → PM peak $4.46 = +29%; AH-entry → AH-peak $5.86 = +70% |

No scanner detection misses. SHPH is a broker limitation, not a scanner gap.

### AH Mover Follow-Through

| Ticker | AH Peak | Peak Time | AH Trajectory | Current PM | From Peak | From Close | Verdict |
|--------|---------|-----------|---------------|------------|-----------|------------|---------|
| VMAR | $1.85 (+45.6%) | 19:20 ET | Build→hold | $3.35 peak | +81% | +164% | **PM exceeded AH peak — continued** ✅ (entered) |
| SHPH | $5.86 (+100.7%) | ~18:10 ET | Build | $4.46 peak | −24% | +53% | PM below AH peak — **AH was better exit** (broker-blocked) |
| LVLU | $11.35 (+36.4%) | 18:00 ET | Build | $10.90 peak | −4% | +26% | PM ~flat vs AH peak — held (entered, now −4%) |
| JEM | ~$0.69 (+38%) | 16:05 ET | Spike→fade | faded | — | — | Grade D reverse split, correctly skipped |

**AH-peak-vs-PM-peak check:** SHPH AH peak $5.86 (+100.7%) > PM peak $4.46 — AH was the better exit, but AH peak was +100% from close (not >250%), so it does not test the extreme-runner (>250%) fade hypothesis. VMAR PM peak $3.35 > AH peak $1.85 — a clean AH→PM continuation.

### Price Charts

```
VMAR — 2-Day: prev close $1.27 | range $1.17–$3.35 | peak $3.35 (+163.8%) @ 07-14 08:00 ET
  AH build 20:20Z→23:20Z ($1.50→$1.85), overnight hold ~$1.55–1.60, PM gap to $3.35 at open then fade to ~$2.54.
SHPH — AH build $3.07→$5.86 (peak ~18:10 ET), overnight ~$5.0, PM open $4.37 fading to ~$4.27 (AH was the exit).
LVLU — AH build $8.32→$11.35, PM $10.90 peak fading to ~$10.56 (held, slightly below AH peak).
```

### Notes

- **VMAR is the model win:** ultra-low float (670K), real SIP volume, BUILD across ≥2 AH scans, entered on the second qualifying scan @ $1.57, PM continued to $3.35 (+113% on entry). No catalyst needed — low-float + sustained AH volume carried it.
- **Reverse-split-squeeze fade tracking:** VMAR (06/17 reverse split, **weeks-old**, float 670K, entered $1.57 → PM peak $3.35, **+113%, CONTINUED**). Counter-example supporting the *recency* hypothesis — a weeks-old (not fresh) reverse split ran hard, unlike the fresh-split faders ELPW/YYGH (both this-week splits, both faded −17%). Split recency is looking like the better fade predictor than the split itself.
- **Broker-block cost (SHPH):** the strongest BUILD of the night (AH +100%, float 596K, VRatio 5.8x, 17k+ trades/bar) never filled because Alpaca reports `tradable=false`. Recurring pattern — SHPH was flagged unfillable across all 5 scans. If low-float pharma names keep getting broker-blocked, the paper-account selection rate is being suppressed by broker coverage, not scanner quality. (Infra note for Juan — Alpaca tradability gap.)
- **Multi-day runner:** GMM (07-10 winner, not detected — late-AH-tail) kept running: day-1 PM peak $4.07 → now **$4.57**. Added to the runner watch. Others faded (TDIC $3.68, IOTR $3.30, RPGL $2.13).
- **Coverage:** 7/7 evening scans ran. No coverage failure.
