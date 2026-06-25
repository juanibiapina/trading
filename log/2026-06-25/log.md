# 2026-06-25

## Morning Evaluation — 10:20 CET

### Today's Winner

**AZI** (Autozi Internet Technology) — Specialty Stores
- Catalyst: None fresh. Recent driver was Jun 9-10 $30M private placement (dilution) + auditor change; stock then bled $1.66 → $1.18 over 2 weeks. AH pop = low-float bounce/squeeze off a downtrend, no same-day 8-K/6-K.
- Previous Close: $1.18
- AH last night: $2.34 (+98.3%) at 18:45 ET (00:45 CET)
- Premarket now: $2.14 (+81.4%), peaked $2.25 (+90.7%) at 04:00 ET
- Hypothetical P&L (AH entry → PM peak): entry $1.62 → PM peak $2.25 = **+38.9%**; AH-entry → AH peak $2.34 = +44.4%
- Float: 4.4M | Market Cap: ~$77.6M

**Scanner Diagnostic:**
- Detectable at screening time? **YES**
- It was the biggest AH mover from the first scan. At 22:30 CET (+37.7%, $1.57), 23:00 (+51.8%, $1.73), built to +82.5% ($2.08) by 00:30. Float 4.4M, clean BUILD trajectory across every scan.
- **We caught AND selected it.** Flagged at 23:00 CET as the night's top candidate (Grade None; concerns logged: no fresh catalyst, not first-day activity, thin Yahoo AH volume). No Alpaca order was placed (pre-Alpaca; execution starts 2026-06-25).
- Scanner gap: none. This is a clean detection + selection win — the scanner found the day's winner in the window.

### Baseline Tracking

- Days tracked: **37** (was 36 + 1)
- Winners detected by scanner: **32/37 (86.5%)** — AZI added
- Winner selected for paper trade: **22/37 (59.5%)** — AZI was traded; we picked the right stock
- Target: >80% detection
- Status: **BASELINE MET**

### Retrospective Scan Results

Live premarket scan (04:20 ET) — 4 hits:

| Ticker | Close | PM Chg% | PM Price | Float | MCap | Industry |
|--------|-------|---------|----------|-------|------|----------|
| AZI | $1.14 | +98.2 | $2.26 | 4.4M | $77.6M | Specialty Stores |
| NEXR | $0.56 | +32.8 | $0.75 | 6.1M | $3.4M | Recreational Products |
| ROLR | $5.30 | +15.8 | $6.14 | 4.9M | $58.1M | Packaged Software |
| BCDA | $1.06 | +12.3 | $1.19 | 10.5M | $15.8M | Biotechnology |

AH reconstruction confirms AZI as the standout AH→PM continuation. NEXR/ROLR/BCDA are PM-side moves with no qualifying AH footprint (NEXR was -4% in AH last night). No other AH→PM winner.

### Trade Execution

**No trades executed.** AZI and AMS were tracked as candidates only. This is the last day of the
pre-Alpaca period: from 2026-06-25 all entries/exits run on the Alpaca paper account via
`scripts/broker.js`, and only real fills are logged. The earlier hand-maintained paper ledger
(assumed prices, never executed) has been discarded.

### Scanner Effectiveness

- Evening scans ran: **6 of 7** (22:00, 22:30, 23:00, 23:30, 00:00, 00:30 CET) — 21:30 scan missing
- Entry window (23:00–00:30 CET) fully covered → not an entry-window loss
- Candidates found: ~20 unique tickers across scans
- Retrospective matches: 1/1 (AZI caught and traded)

### Missed Opportunities

No significant missed opportunities. The day's winner (AZI) was detected and entered.

### AH Mover Follow-Through

| Ticker | AH Peak | Peak Time | AH Trajectory | Current PM | From Peak | From Close | Verdict |
|--------|---------|-----------|---------------|------------|-----------|------------|---------|
| AZI | $2.34 (+98.3%) | 18:45 ET | Build | $2.14 | -8.5% | +81.4% | Continued strong — winner, traded |
| AMS | $1.68 (+14.3%) | 16:30 ET | Spike→hold | $1.52 | -9.5% | +3.4% | Faded — PM gave back the AH gain |
| SAGT | $1.43 (+10.0%) | 16:15 ET | Spike→fade | $1.15 | -19.6% | -11.5% | Faded then crashed — correctly skipped |

**AH-peak-vs-PM-peak check:** AZI's AH peak $2.34 marginally exceeded its PM peak so far ($2.25), so late AH was the slightly better exit — but PM is early (only 04:00–04:20 data). Not an extreme runner (AH peak +98%, well under the 250% extreme-runner threshold), so no extreme-runner tally entry. AMS and SAGT both peaked in AH and faded in PM.

### Notes

- **Clean detection + selection win.** AZI is the first day in a while where the scanner found the winner AND we entered it in-window. Detection 86.5%, selection 59.5%.
- **PM-only gapper tracking:** today's biggest raw PM mover = AZI (+98%), which is an AH→PM continuation (moved +98% in after-hours, fully detectable). **Not a PM-only gapper.** No tally addition.
- **Late-AH-tail surge:** AZI's defining move (crossing +10%, building to +50%, +76%) happened during the scanned window; the 18:30–20:00 ET tail only extended an already-qualified open position from +76% to +98%. **Not a tail-surge miss.** No tally addition.
- **Fade-rule false negatives:** none. SAGT (spike→fade, peaked +10% at 16:15) and KIDZ (spike→fade, peaked +25% at 16:45 then collapsed) were both correctly skipped — both stayed down in PM (SAGT crashed -11%, KIDZ -9%). Rule worked.
- **Coverage tally:** Jun 24–25 night ran 6 of 7 scans (missing 21:30, the earliest pre-volume scan). Entry window fully covered; minor, treat as transient. Watch for recurrence.
- **No CEILING-OVERRIDE / DEAD-CAT-OVERRIDE watch candidates** flagged in last night's log.
- AZI entered Grade None with explicit concerns (no fresh catalyst, not first-day activity, dilution-driven recent history). It is running +32% anyway — another data point that low-float (4.4M) + clean BUILD trajectory can carry overnight even without a same-day catalyst (cf. DXST Jun 1, +170% no-catalyst runner).

### Price Charts

```
AZI - 2-Day Price Timeline (5-min)
Previous Close: $1.18
2-Day Range: $1.14 - $2.38
Current: $2.14 (+81.4%)
AH Peak: $2.34 (+98.3%) at 18:45 ET → held +80%+ through AH close → PM $2.25 (+90.7%) at 04:00

AH trajectory: steady BUILD from 16:05 (+26%) → 16:35 (+51%) → 18:00 (+64%) → 18:45 peak (+98%),
then held +82-95% through the AH tail. Textbook AH BUILD → PM hold.
```

## Position Evaluation — 10:30 CET

No open positions on Alpaca. AZI/AMS were never executed (pre-Alpaca candidates). Nothing to evaluate.
Switched the workflow to Alpaca paper execution as source of truth (see OPEN_POSITIONS.md).

## Position Evaluation — 14:30 CET

No open positions on Alpaca (`positions` returns empty; equity $99,998.41). `OPEN_POSITIONS.md`
current table is empty and reconciles with Alpaca. Nothing to hold, trail, or sell.

Order history shows only closed VTAK round-trips from Jun 23–24 — `broker.js` validation test
trades made before today's source-of-truth switch, not strategy entries:
- Jun 23: BUY 67 @ $1.14 → SELL 67 @ $1.13 = −$0.67 (scratch)
- Jun 24: BUY 86 @ $1.35 → SELL 86 @ $1.34 = −$0.86 (scratch)
- Jun 23: canceled $0.50 GTC test order (never filled)

These predate the clean slate and are not logged as strategy trades. No action taken.

## Scan 21:30 CET (3:30 PM ET)

**REGULAR session — after-hours not open yet (close is 4:00 PM ET).** Observation only per the
regular-session caution. No paper entries. Candidates below are flagged **Watch — pending AH
confirmation**; only enter if they reappear with sustained momentum in a 22:00+ CET AH scan. The
`VChg%` of -99/-100% on most names is end-of-day volume tapering, not AH action. Catalyst searches
deferred to the AH scans.

Top day movers worth watching into AH (filtered for float and real activity):

| Ticker | Chart | Price | Day% | 5mVol | IRVol | Float | MCap | Industry | Note |
|--------|-------|-------|------|-------|-------|-------|------|----------|------|
| ILLR | [TV](https://www.tradingview.com/chart/?symbol=ILLR) | $2.85 | +270.6% | 100 | 477.2 | n/a | $15.3M | Packaged Software | Big day move; vol fading into close |
| AZI | [TV](https://www.tradingview.com/chart/?symbol=AZI) | $2.00 | +75.4% | 399 | 13.2 | 4.4M | $136M | Specialty Stores | Last night's AH→PM winner, still elevated |
| ASPD | [TV](https://www.tradingview.com/chart/?symbol=ASPD) | $2.90 | +190.0% | 240 | 4.3 | n/a | $1.7M | REIT | Thin |
| NEXR | [TV](https://www.tradingview.com/chart/?symbol=NEXR) | $1.15 | +104.4% | 200 | 490.5 | 6.1M | $3.4M | Recreational Products | Low float, vol faded into close |
| VINO | [TV](https://www.tradingview.com/chart/?symbol=VINO) | $1.44 | +157.1% | 200 | 0.1 | 920K | $1.4M | Real Estate Dev | Micro float, very thin |

Larger %-movers (APHD +702%, CFOR +345%, KJFI +274%, TNSGF +778%) are all sub-1K 5mVol thin
names — noise, not watched. Will re-scan once AH opens (22:00 CET).

## Scan 22:00 CET (4:00 PM ET)

**AH just opened.** Scanner (`scan.py --all`) returned **0 hits** — no tickers cleared the
after-hours filter at the open. This is the observation-only window (entries don't begin until
23:00 CET per learning-phase rule); nothing to evaluate yet regardless.

Watchlist carried from the 21:30 regular-session scan (ILLR, AZI, ASPD, NEXR, VINO) showed no
qualifying AH footprint at the open. The 21:30 day-movers were end-of-session prints; none has
posted sustained AH momentum yet. Will re-scan at 22:30 / 23:00 CET when AH volume builds and
catalyst searches become productive (PRs often land 4:05-4:30 PM ET).

No candidates found.

## Scan 22:30 CET (4:30 PM ET)

**Observation-only window** — entries begin at 23:00 CET per learning-phase rule. Scanner returned
**6 hits** (first real AH footprint of the night). No paper entries this scan.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| NEXR | [TV](https://www.tradingview.com/chart/?symbol=NEXR) | $1.09 | +93.8% | +13.1% | $1.23 | +119.1% | 7.5M | 32.1M | 0.2x | 6.1M | Recreational Products |
| DLHC | [TV](https://www.tradingview.com/chart/?symbol=DLHC) | $5.50 | +0.0% | +22.7% | $6.75 | +22.7% | 517K | 81K | 6.4x | 12.7M | Personnel Services |
| SHPH | [TV](https://www.tradingview.com/chart/?symbol=SHPH) | $3.78 | +2.4% | +25.1% | $4.73 | +28.2% | 308K | 173K | 1.8x | 596K | Pharmaceuticals: Major |
| NGEN | [TV](https://www.tradingview.com/chart/?symbol=NGEN) | $1.91 | -4.0% | +6.8% | $2.04 | +2.5% | 137K | 924K | 0.1x | 64.0M | Pharmaceuticals: Major |
| ELDN | [TV](https://www.tradingview.com/chart/?symbol=ELDN) | $3.65 | -7.8% | +6.6% | $3.89 | -1.8% | 78K | 1.8M | 0.0x | 73.8M | Pharmaceuticals: Major |
| CNEY | [TV](https://www.tradingview.com/chart/?symbol=CNEY) | $0.52 | -21.6% | +6.8% | $0.55 | -16.3% | 56K | 744K | 0.1x | 5.0M | Electrical Products |

### AH trajectory (5-min)

- **SHPH** — BUILD: +10.6% (16:05) → +30% (16:10) → +37% peak (16:15) → holding +33–37% through 16:30. Float **596K** (very tiny), VRatio 1.8x. Strongest pattern of the night so far.
- **DLHC** — SPIKE then flatten: +16% (16:05) → +22% peak (16:10) → easing to +17% by 16:30. Real volume (VRatio 6.4x). Float 12.7M (>10M ideal).
- **NEXR** — already +93.8% on the *regular* day; AH only +13% and VRatio 0.2x (volume faded into AH). Extended continuation name, not a fresh AH base. On watchlist since the 21:30 scan.

### Catalyst checks (>10% AH movers)

- **DLHC — Grade B (contract win).** Navy logistics IT contract, multiple-award ID/IQ, **$250M ceiling**, announced ~21 min before this scan (StockTitan). Real catalyst + real volume. Concern: float 12.7M above 10M ideal, and price already easing off the +22% spike.
- **SHPH — no catalyst found** (4 searches: earnings, PR, 8-K, clinical). Only notable item is a recent 1-for-10 reverse split (~1 week ago). Tiny 596K float + clean BUILD is the draw; no fresh news to explain the move. Concern noted per no-catalyst handling.
- **NEXR — extended day mover.** AH +13% is continuation of a +93.8% regular-session run; not re-searching catalyst this scan (will re-check at 23:00 if it holds). Volume fading (VRatio 0.2x).

### Watch into 23:00 entry window

- **SHPH** — BUILD + 596K float is the most interesting profile. Watch whether it holds/extends above ~$4.7 into 23:00. No-catalyst is a concern, not a blocker (learning phase). Needs >10% AH in ≥2 AH scans to qualify (this is its 1st).
- **DLHC** — Grade B catalyst, but spike→flatten and float >10M. Watch for a second AH scan above +10% and whether it rebuilds or keeps fading.
- **NEXR** — fading volume; low priority unless it re-accelerates.

No paper trades (observation window). Re-scan at 23:00 CET for the entry decision.

## Scan 23:00 CET (5:00 PM ET) — ENTRY WINDOW OPEN

First entry-eligible scan of the night. Scanner returned **7 hits**.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| NEXR | [TV](https://www.tradingview.com/chart/?symbol=NEXR) | $1.10 | +95.6% | +7.7% | $1.19 | +110.7% | 10.1M | 32.4M | 0.3x | 6.1M | Recreational Products |
| SHPH | [TV](https://www.tradingview.com/chart/?symbol=SHPH) | $3.78 | +2.4% | +72.0% | $6.50 | +76.2% | 3.9M | 670K | 5.8x | 596K | Pharmaceuticals: Major |
| ILLR | [TV](https://www.tradingview.com/chart/?symbol=ILLR) | $3.05 | +296.6% | +12.8% | $3.44 | +347.3% | 3.3M | 22.3M | 0.1x | n/a | Packaged Software |
| IPW | [TV](https://www.tradingview.com/chart/?symbol=IPW) | $2.58 | +8.4% | +24.0% | $3.20 | +34.5% | 1.9M | 515K | 3.6x | 570K | Internet Retail |
| DLHC | [TV](https://www.tradingview.com/chart/?symbol=DLHC) | $5.50 | +0.0% | +13.5% | $6.24 | +13.5% | 1.2M | 183K | 6.6x | 12.7M | Personnel Services |
| YYGH | [TV](https://www.tradingview.com/chart/?symbol=YYGH) | $1.27 | -26.2% | +14.2% | $1.45 | -15.7% | 585K | 2.1M | 0.3x | 4.0M | Misc Commercial Services |
| NGEN | [TV](https://www.tradingview.com/chart/?symbol=NGEN) | $1.91 | -4.0% | +6.8% | $2.04 | +2.5% | 137K | 924K | 0.1x | 64.0M | Pharmaceuticals: Major |

### AH trajectory (5-min)

- **SHPH** — strong BUILD: +10.6% (16:05) → +30% (16:10) → +37% (16:15) → +52% (16:30) → +66% (16:35) → +75.3% (16:40) → **+75.9% peak (16:45)** → easing to +61.8% ($5.97) by 17:00. Currently ~8-12% off the AH high → **holding**, not a deep fade. Float **596K**, VRatio 5.8x. Cleanest profile of the night.
- **DLHC** — SPIKE→FADE: +16.4% (16:05) → **+22.4% peak (16:10)** → steady decline +16.5% (16:30) → +13.5% (16:40) → +10.7% (16:45) → **+6.5% ($5.86) by 17:00**. Early peak + declining across every print, now sub-10%.
- **IPW** — BUILD then ease: +10.9% (16:05) → +25.6% (16:20) → **+34.5% peak (16:40)** → +22% (17:00). Float 570K, VRatio 3.6x. NEW name; first AH scan >10%.
- **NEXR** — AH peaked +127.6% at 16:05 (regular-day continuation), now +7.7%, volume fading (VRatio 0.3).
- **ILLR** — AH peaked +381% (16:55-17:00), holding — but Total +347% (>150 ceiling) and VRatio 0.1 (no real AH volume).
- **YYGH** — AH high $1.48 vs close $1.72: stays *below* regular close (Total -13.9% at best). Day -26.2%.

### Entry evaluation (per-candidate)

- **SHPH — QUALIFIES on all gates, but NOT TRADABLE on Alpaca → no position.**
  - Gates: float 596K (<50M ✓, <10M ideal ✓), AH >10% in 2 AH scans (22:30 +25.1%, 23:00 +72.0% ✓), Day% +2.4% (>-15 ✓), Total% +76% (<150 ceiling ✓), BUILD holding within ~12% of AH high (early 16:45 peak does NOT disqualify a hold per CHAI/MSW precedent ✓), VRatio 5.8x ✓.
  - **Catalyst — Grade C (strategic/crypto-pivot PR).** Subsidiary United Dogecoin (acquired May 2026) outlined a data-centre/power-infrastructure strategy for DOGE mining + future AI hosting (evaluating assets in Idaho/Alberta, electrifying ElphaPex miners). No signed deal, no revenue, no contract — a narrative PR. StockTitan: Neutral sentiment, Moderate impact, *"Pattern Detected: SHPH has often seen sharp declines following seemingly positive strategic announcements"* — prior crypto/AI PRs moved -32.8%, -32.8%, -22.9%. Recent 1-for-10 reverse split (Jun 9). Grade C → would exit premarket.
  - **Execution: `tradable=false shortable=false fractionable=false`.** Alpaca will not trade SHPH. Quote was bid $5.91 / ask $6.03. **No order placed, no position.** Logged as qualified-but-untradable — hypothetical entry ~$6.03 for tracking.
- **DLHC — SKIP (trajectory).** Has 2 AH scans >10% (22:30 +22.7%, 23:00 +13.5%) and a Grade B catalyst (Navy logistics IT contract, $250M ceiling). But it's a textbook early-peak SPIKE→FADE: peaked +22.4% at 16:10, declined every print to +6.5% by 17:00 (now sub-10%). Trajectory overrides catalyst (BUILD-vs-FADE rule); early-peak + declining across scans = 0/7 PM-continuation profile. Skip.
- **IPW — WATCH (only 1 AH scan >10%).** Float 570K, VRatio 3.6x, BUILD to +34.5% then easing. NEW name; needs a 2nd AH scan >10% to qualify. Re-check at 23:30.
- **NEXR — SKIP.** Only 1 AH scan >10% (22:30 +13.1%; now +7.7%). AH is regular-day continuation, volume fading.
- **ILLR — SKIP (extension ceiling).** Total +347% >> 150% ceiling. VRatio 0.1 fails ceiling-override (needs >5x), so no override watch.
- **YYGH — SKIP (Day% gate + dead-cat).** Day -26.2% below the -15 floor. AH high stays *below* regular close → genuine dead-cat bounce, not an override-watch (no reclaim above close).
- **NGEN — SKIP.** Float 64M (>50M), AH +6.8% (<10%).

**Net: 0 entries this scan.** The night's one all-gates qualifier (SHPH) is untradable on Alpaca. No tradable BUILD candidate cleared the 2-scan requirement. Re-scan at 23:30 for IPW 2nd-scan confirmation and any new BUILD names.

## Scan 23:30 CET (5:30 PM ET) — ENTRY WINDOW OPEN

Scanner returned **9 hits**. New names since 23:00: LGCL, IVF, PBK, TII, LABT. Carried: NEXR, SHPH, ILLR, YYGH.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| NEXR | [TV](https://www.tradingview.com/chart/?symbol=NEXR) | $1.10 | +95.6% | +27.3% | $1.40 | +148.9% | 13.1M | 32.7M | 0.4x | 6.1M | Recreational Products |
| SHPH | [TV](https://www.tradingview.com/chart/?symbol=SHPH) | $3.78 | +2.4% | +59.8% | $6.04 | +63.7% | 6.1M | 970K | 6.2x | 596K | Pharmaceuticals: Major |
| ILLR | [TV](https://www.tradingview.com/chart/?symbol=ILLR) | $3.05 | +296.6% | +25.6% | $3.83 | +397.9% | 5.2M | 22.6M | 0.2x | n/a | Packaged Software |
| LGCL | [TV](https://www.tradingview.com/chart/?symbol=LGCL) | $0.94 | -34.2% | +48.9% | $1.40 | -2.1% | 1.9M | 306K | 6.2x | 1.6M | Personnel Services |
| IVF | [TV](https://www.tradingview.com/chart/?symbol=IVF) | $1.24 | -6.1% | +13.7% | $1.41 | +6.8% | 1.3M | 242K | 5.3x | 1.8M | Medical/Nursing Services |
| YYGH | [TV](https://www.tradingview.com/chart/?symbol=YYGH) | $1.27 | -26.2% | +10.2% | $1.40 | -18.6% | 765K | 2.1M | 0.4x | 4.0M | Misc Commercial Services |
| PBK | [TV](https://www.tradingview.com/chart/?symbol=PBK) | $0.73 | -1.9% | +5.5% | $0.77 | +3.4% | 358K | 5.9M | 0.1x | 43.0M | Alternative Power Generation |
| TII | [TV](https://www.tradingview.com/chart/?symbol=TII) | $2.23 | +2.8% | +5.4% | $2.35 | +8.3% | 137K | 314K | 0.4x | 28.5M | Other Metals/Minerals |
| LABT | [TV](https://www.tradingview.com/chart/?symbol=LABT) | $3.43 | -7.8% | +10.2% | $3.78 | +1.6% | 94K | 202K | 0.5x | 1.4M | Biotechnology |

### AH trajectory (5-min)

- **SHPH** — BUILD then hold: peaked **+75.9% ($6.49) at 16:45**, eased to +58-67%, now $6.14 (+66.4%). Holding within ~5-13% of the AH high across the whole session. Float **596K**, VRatio 6.2x. Still the cleanest profile of the night.
- **NEXR** — regular-day continuation on near-zero AH volume. AH peaked +147% ($1.39) at 17:10, now $1.32. AH Vol just 5K total — these are illiquid noise prints, not a real AH base. Already +95.6% on the regular day.
- **IVF** — NEW. Choppy spike→fade→spike: +16.7% peak (17:00) → +5.3% (17:10) → +15.9% (17:20) → +10.7% now. Real volume (VRatio 5.3x), float 1.8M. No clean BUILD; whipsaw pattern.
- **LGCL** — dead-cat bounce that already failed: spiked +49% ($2.13) at 16:50 → faded straight down to -12.6% ($1.25) now, *below* the regular close. Day -34.2%.
- **LABT** — no real move: AH high only +3.2% ($3.84), chopping around flat. The scan's +10.2% is a momentary print; VRatio 0.5x.

### Entry evaluation (per-candidate)

- **SHPH — QUALIFIES on all gates, but STILL NOT TRADABLE on Alpaca → no position.** Gates all pass (float 596K, AH >10% in 3 AH scans, Day +2.4%, Total +63.7% <150, BUILD holding within ~13% of high, VRatio 6.2x). Catalyst already graded **C** at 23:00 (United Dogecoin crypto/AI-hosting narrative PR, no signed deal; StockTitan flagged prior similar PRs faded -23% to -33%). **`tradable=false shortable=false`** on Alpaca; Alpaca shows a quote (bid $5.91 / ask $6.03) but will not accept the order. No position. Hypothetical entry ~$6.03 for tracking (carried from 23:00).
- **NEXR — SKIP (no real AH volume + extension).** Technically 2 AH scans >10% (22:30 +13.1%, 23:30 +27.3%), Total +148.9% just under the 150 ceiling. But AH Vol is ~5K total (VRatio 0.4x) — the AH prints are illiquid noise, not a tradable base. Alpaca quote bid $1.08 / ask $1.22 is a ~12% spread confirming the thin book. Also a chase of an already +95.6% regular-session runner at the ceiling. Skip.
- **IVF — WATCH (only 1 AH scan >10%).** NEW name, first appearance; needs a 2nd AH scan >10% to qualify. Real volume (VRatio 5.3x, float 1.8M) but choppy spike→fade→spike, no clean BUILD. Re-check at 00:00.
- **LGCL — SKIP (Day% gate + dead-cat).** Day -34.2% below the -15 floor. AH spiked +49% then collapsed to -12.6%, staying *below* the regular close → genuine failed dead-cat bounce. No override (price falling, below close).
- **LABT — SKIP.** AH high only +3.2%; no sustained >10% move, VRatio 0.5x.
- **ILLR — SKIP (extension ceiling).** Total +397.9% >> 150%. VRatio 0.2x fails ceiling-override (needs >5x).
- **YYGH — SKIP.** Day -26.2% below floor; AH stays below regular close (dead-cat, no reclaim).
- **PBK / TII — SKIP.** AH <10%.

**Net: 0 entries this scan.** Same as 23:00 — the night's one all-gates qualifier (SHPH) is untradable on Alpaca, and no tradable candidate cleared the 2-scan BUILD requirement on real volume. IVF is the only fresh watch (needs a 2nd scan). Re-scan at 00:00 for IVF confirmation and any new BUILD names.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|

_No entries — pre-AH observation scan only._
