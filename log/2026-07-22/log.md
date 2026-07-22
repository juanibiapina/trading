# Morning Evaluation - 2026-07-22

## Morning Evaluation — 10:20 CET

Session evaluated: **2026-07-21** after-hours → **2026-07-22** premarket. Pulse 1.

### Today's Winner

**SXTC** — Pharmaceuticals (China SXT Pharmaceuticals, NasdaqCM small-cap)
- Catalyst: **Unverified/None** — no same-day PR located in this environment (no web-search tool available at pulse). China small-cap pharma PM squeeze; treat as no-catalyst until verified.
- Previous Close: $2.45
- AH last night: peaked **$2.85 (+16.3%)** at ~18:25 ET on **negligible volume** (few hundred sh/bar; single 15k-sh bar at the 16:00 ET open). Never a tradeable AH signal.
- Premarket now: **$5.69 (+132%)**; PM peak **$7.91 (+222.9%)** at 04:05 ET (08:05Z)
- Hypothetical P&L: optimistic AH entry ~$2.75 → PM peak $7.91 = **+188%** (but undetectable, see diagnostic). Realistic PM-open re-entry: first PM bar VWAP $5.45 → peak $7.91 = **+45%**.
- Float: 32.2M | Market Cap: $86.3M
- SIP confirmation it cleared the bar: PM open bar 08:00Z **1,282,250 sh / 23,886 trades** (H $6.44), 08:05Z **1,850,080 sh / 38,738 trades** (H $7.91). Real, accumulating, >100% move.

**Scanner Diagnostic:**
- Detectable at screening time (~22:15 CET)? **NO**
- Why: SXTC was only +16% in AH on essentially no volume (a few hundred shares/bar; VRatio far below threshold). It appeared in **zero** of last night's 9 evening scans. The winner-making >100% explosion fired at **PM open (04:00 ET)**, hours after the final 00:30 CET scan.
- Classification: **PM-only gapper — HOLDABLE** (gain sustained across ≥2 consecutive 5-min PM bars on 1.3–1.85M sh; a real exit window exists — still +132% at pulse). Per the PM-only-gapper rule this is **not** a scanner failure and is **not** counted against the detection baseline. The nominal +16% AH tick was sub-detection-threshold noise, not a detectable AH footprint.
- Scanner gap: none actionable in the AH workflow — structurally a PM-only gapper. Only an early-PM scan (a separate, riskier workflow under evaluation via the PM-only-gapper tally) could catch it.

### Baseline Tracking

Carried from 2026-07-21 log (Days tracked 51; 44/49 detected; 25/49 selected). Today's winner (SXTC) is a **PM-only gapper**, so it is excluded from both the detection numerator and denominator (not a valid AH-detection sample) — detection and selection ratios hold at /49. Days tracked increments by 1 for the session evaluated.

- Days tracked: **52** (was 51 + 1)
- Winners detected by scanner: **44/49 (89.8%)** — unchanged (SXTC excluded, PM-only gapper)
- Winner selected for paper trade: **25/49 (51.0%)** — unchanged (SXTC not tradeable via AH workflow; correctly not traded)
- Target: >80% detection
- Status: **BASELINE MET** (89.8%)
- **Baseline gap (carried):** 2026-07-17 and 2026-07-20 morning evals recorded no `Days tracked:` line — those two trading-day retrospectives were not baseline-counted (denominator understates true trading days). The immediately-preceding trading day (07-21) *does* carry a baseline line, so no new gap this cycle.

### Retrospective Scan Results

- Live PM scan (04:21 ET): 5 hits — **SXTC +121% $5.93**, AEHL +39% $0.90, INLF +58% $3.53, SNTG +22% $2.55, KUST +5% $1.01.
- AH reconstruction (SIP + Yahoo `--ah-history`): only AEHL and KUST had real AH volume last night; SXTC's AH was thin (+16%). Winner move was PM-only.

### Open Position P&L (Alpaca)

**No executed positions.** Account is flat — HIHO and PAPL were both sold yesterday (14:30 CET pulse: HIHO @ $1.26 −16.0%, PAPL @ $0.84 −23.6%). `broker.js positions` returns none.

### Scanner Effectiveness

- Evening scans ran: **7 of 7** scheduled (21:30, 22:00, 22:30, 23:00, 23:30, 00:00, 00:30 CET), plus 2 bonus (22:15, 22:45) = 9 total. **Full coverage — entry window fully captured.**
- Candidates found: AEHL (night's deepest AH mover), KUST, DFNS, NVVE, SNTG (all AH movers logged).
- Retrospective matches: winner SXTC = PM-only gapper, not an AH candidate. AH movers (AEHL, KUST) all faded — correctly skipped.

### Missed Opportunities

| Ticker | AH Change | Why Missed | Would Be Profitable? |
|--------|-----------|------------|---------------------|
| SXTC | +16% AH (thin) | PM-only gapper — real +100% move fired at PM open, no AH volume | Yes on PM re-entry (+45% VWAP→peak), but structurally undetectable by AH scanner — not a scanner miss |

No AH→PM continuation was missed. Every real AH mover was detected and correctly skipped (all faded).

### AH Mover Follow-Through

| Ticker | AH Peak | Peak Time | AH Trajectory | Current PM | From Peak | From Close | Verdict |
|--------|---------|-----------|---------------|------------|-----------|------------|---------|
| AEHL | $1.38 (SIP, +112%) | 16:40 ET | Spike→fade | $0.90 (+38%) | −35% | +38% | Faded; **AH peak > PM peak $1.14 → AH was the better exit**. Correctly gate-blocked (SPIKE→FADE, 1st-scan). Float 15.6M = higher-float negative control. |
| KUST | $1.32 (AH) | ~17:00 ET | Spike→fade | $1.01 (−21% vs $1.27 Yahoo close) | −24% | fade | Dead-cat-override watch (hypo $1.24). SIP PM peak $1.35 first bar (578k sh) then collapsed to $1.01. Reclaim faded instantly. |

**AH-peak-vs-PM-peak:** AEHL AH peak ($1.38) > PM peak ($1.14) — another "AH was the better exit" case (but AH peak only +112%, not an extreme >250% runner, so not a new MSW-class data point).

### Price Charts

```
SXTC — 2-Day Timeline
Prev Close: $2.45 | Range: $2.50–$7.91 | Current: $5.69 (+132.3%)
Peak: $7.91 (+222.9%) at 07-22 08:05 ET
AH 07-21: flat +6–16% on a few hundred sh/bar (non-tradeable)
PM 07-22 04:00 ET: EXPLODES $3.39 → $7.91 on 1.3–1.85M sh/bar (24k–39k trades) → PM-only gapper
```

### Notes

- **Winner is a rare HOLDABLE PM-only gapper.** SXTC's +223% peak came entirely at PM open on 1.3–1.85M sh/bar (24k–39k trades) and held above +130% through the pulse — a genuine, liquid exit window, unlike most PM-only gappers which are instant crashes. Adds to the PM-only-gapper tally as a *holdable* case (see tally). One holdable case does not flip the "AH-blind-spot has low real cost" hypothesis, but it is the strongest holdable PM-only example to date.

- **PM-only gapper tally (updated):** CIIT (Jun 10 +140%), GLXG (Jun 11 +343%, uninvestable), TDIC (Jun 16 +140%), MBRX (Jun 23 +131%, uninvestable), CUPR (Jun 24 +81%, thin), **SXTC (Jul 22 +223%, HOLDABLE — sustained ≥2 PM bars on 1.3–1.85M sh)**. Holdable count now 1 clear + a few borderline; still not a cluster justifying a separate early-PM workflow.

- **Dead-cat-override watch outcome (KUST, 07-21 → 22):** hypo entry $1.24 @ 23:00 CET → SIP PM peak $1.35 (first PM bar, 578k sh) = **+8.9%**, then collapsed to $1.01 within one bar. The reclaim-above-close faded near-instantly — **dead-cat filter roughly validated** (only a thin one-bar +8.9% window, gone immediately). Note: this is a *different* KUST event from the 2026-07-15 winner (577K-float repeat pump name).

- **Broker-block tally (updated):** SHPH (07-21, tradable=false across AH scans, Grade None, AH +18–24%). PM follow-through: PM peak only **$3.22 (+6.3%)** vs $3.03 close — faded from its AH level, so the untradability **cost ≈ nil this time** (would have lost). Prior cases: SHPH Jun 25 (Grade C, hypo untradable), SHPH Jul 13 (hypo +29%/+70%). Recurring low-float-pharma broker-block persists; cumulative cost still modest and this instance was a non-event.

- **Fade-rule false-negative tally (unchanged): sub-3M count 3 of 5, ≥4/5 trigger NOT met.** Tonight's faders were higher-float negative controls: **AEHL float 15.6M** faded (AH peak $1.38 > PM peak $1.14) exactly as the fade rule predicts — corroborates trajectory-over-catalyst, does not count toward the sub-3M trigger. No new sub-3M fader re-exploded. Live-flip exception stays withdrawn pending one more clean sub-3M SIP-verified blow-past.

- **No reverse-split entries** last night (no entries at all — clean no-trade night). Reverse-split recency tally unchanged (this-week splits 3/3 faded).

- **No ceiling-override or late-AH-tail winner cases** this cycle. AEHL's AH peak (16:40 ET) was well inside the scanned window, not a tail surge.

- **Coverage:** full 7/7 (no coverage failure to add to the tally).

- **Active Watch check:** HIHO (entered $1.50, sold $1.26) crashed further to $0.93 day 2 — no-catalyst-grade-B pump fully unwinding. CJMB flat at $1.21 (day 5 → moved to Historical).

## Position Evaluation — 10:30 CET

**No open positions.** Alpaca `broker.js positions` returns none; `OPEN_POSITIONS.md` shows `_(none)_`. Source of truth and mirror agree — no reconciliation needed.

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| _(none)_ | | | | | | | — | Account flat |

**Actions taken:**
- None. Nothing to sell, no stops to update. Account flat since 07-21 14:30 CET pulse (HIHO, PAPL both closed).

## Position Evaluation — 14:30 CET

**No open positions.** Alpaca `broker.js positions` returns none (equity $99,877.41, all cash); `OPEN_POSITIONS.md` shows `_(none)_`. Source of truth and mirror agree — no reconciliation needed.

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| _(none)_ | | | | | | | — | Account flat |

**Actions taken:**
- None. Nothing to sell, no stops to update. Account flat since 07-21 14:30 CET pulse (HIHO, PAPL both closed).

---

# Post-Market Screening - 2026-07-22

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|

## Scan 22:45 CET (4:45 PM ET)

**Bonus AH scan** — observation-only window (learning phase: no entries before 23:00 CET). `scan.py --all` returned **3 hits** (16:45:18 ET): ZYBT, PLAG, STFS. ZCMD/LABT again omitted by the TradingView feed — SIP cross-check is truth.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| ZYBT | [TV](https://www.tradingview.com/chart/?symbol=ZYBT) | $1.38 | −51.6% | +52.2% | $2.10 | −26.3% | 3.4M | 21.1M | 0.2x | 7.7M | Biotechnology |
| PLAG | [TV](https://www.tradingview.com/chart/?symbol=PLAG) | $0.59 | +9.4% | +15.4% | $0.68 | +26.3% | 240K | 185K | 1.3x | 11.6M | Food: Specialty/Candy |
| STFS | [TV](https://www.tradingview.com/chart/?symbol=STFS) | $3.79 | −49.8% | +22.2% | $4.63 | −38.7% | 3K | 98K | 0.0x | 1.1M | Advertising/Marketing Services |

**Spike-bar instrumentation (AH >10% names, log-only):**
- ZYBT: `SPIKE 16:16ET +30% $1.80 724 trades / 135k sh` (first co-spike bar)
- PLAG: `SPIKE 16:18ET +20% $0.71 78 trades / 99k sh` (first co-spike bar)
- STFS: `NO-SPIKE peak +30% @16:18ET` (no bar cleared +15% on a volume co-spike)

**SIP cross-check (bars lag ~15 min to 16:30 ET):**

| Ticker | Close | AH trajectory (SIP bars) | Live quote (fresh) | Verdict |
|--------|-------|--------------------------|--------------------|---------|
| ZYBT | $1.38 | Spike H $2.31 @16:15ET on 1.31M sh/6670tr → oscillating $1.80–$2.10, C $1.80 @16:30ET | bid $1.71 / ask $1.74 x100 (20:45Z) | Dead-cat + spike→fade; live ~+26%, off peak |
| PLAG | $0.59 | H $0.71 @16:15ET (120k sh/116tr) → holding $0.63–$0.68, wick $0.80 @16:30ET | bid $0.53 / ask $0.74 x100 (stale 20:00Z) | Positive-day, real +15% AH, holding — best new candidate |
| STFS | $3.79 | H $4.99 on 472–2471 sh/bar (<52 tr) — thin | bid $3.13 / ask $4.45 x100 (stale) | Dead-cat + illiquid/thin, NO-SPIKE |
| ZCMD | $4.07 | Peak $5.58 @16:00ET (1.28M sh) → fading every bar, C $3.65 @16:30ET (below close) | — | SPIKE→FADE, extended (>180% total) |
| LABT | $3.41 | Surge $3.87 @16:10ET (470k sh) → faded $3.41–$3.47 | — | Faded, below gate |

**Evaluation (observation-only, no entries):**
- **ZYBT** — Day **−51.6%** (crashed in regular session), bouncing in AH on real volume (1.31M sh spike bar). Total% still **−26.3%** (below prior-day close). SIP shows it spiked to $2.31 at the 16:15 ET open bar and is now **fading** (live $1.74, −25% off peak). The scanner's +9.4%→+52.2% jump across 22:30→22:45 is a **feed-lag artifact** (the 22:30 +9.4% was stale opening-bar data; the real spike already fired at 16:15). Not a genuine build — dead-cat spike→fade. **Skip.** Not flagged as dead-cat-override: the reclaim is fading off peak, not building across scans, and it never approaches the prior-day close.
- **PLAG** — Positive-day mover (+9.4% RTH), real **+15.4%** AH on modest but genuine volume (120k sh spike bar, holding $0.63–0.68). SPIKE 16:18ET ignition. Total% +26.3% (well inside ceiling). Float 11.6M. First AH scan appearance above 10% — needs a 2nd AH scan >10% to clear the gate. **Best new candidate — watch 23:00 for hold-vs-fade.**
- **STFS** — Day −49.8% dead-cat, AH volume 3K on <52 trades/bar (thin), NO-SPIKE. Illiquid + dead-cat. **Skip.**
- **ZCMD / LABT / PN** — all faded from opening-bar spikes (ZCMD now below close, extended >180%; LABT faded to $3.41; PN illiquid `ask $0.00 x0`). No BUILD/hold. Skip carried forward.

**No entries** (observation-only window before 23:00 CET). No candidate shows a clean BUILD-and-hold. PLAG is the only positive-day real-volume name holding gains — recheck at 23:00. ZYBT/STFS are dead-cat bounces; ZCMD/LABT faded.

## Scan 22:30 CET (4:30 PM ET)

**AH scan** — observation-only window (learning phase: no entries before 23:00 CET). `scan.py --all` returned **3 hits** (16:30:15 ET). ZCMD (strongest 22:15 candidate) was again **omitted by the TradingView feed** — SIP cross-check below is truth.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| CHAI | [TV](https://www.tradingview.com/chart/?symbol=CHAI) | $0.50 | +28.0% | +5.0% | $0.53 | +34.4% | 730K | 16.5M | 0.0x | 9.0M | Packaged Software |
| LABT | [TV](https://www.tradingview.com/chart/?symbol=LABT) | $3.41 | +83.3% | +7.1% | $3.65 | +96.3% | 473K | 8.1M | 0.1x | 956K | Biotechnology |
| ZYBT | [TV](https://www.tradingview.com/chart/?symbol=ZYBT) | $1.38 | −51.6% | +9.4% | $1.51 | −47.0% | 51K | 20.7M | 0.0x | 7.7M | Biotechnology |

**SIP cross-check (tracked names, feed truth) — bars lag ~15 min to 16:15 ET:**

| Ticker | Close | AH trajectory (SIP bars) | Current AH | Book (quote) | Spike-bar |
|--------|-------|--------------------------|------------|--------------|-----------|
| ZCMD | $4.07 | Peak H $5.58 (+37%) @16:00ET on 1.28M sh → faded $4.25→$3.95→$4.26 across bars | ~$4.26 (+4.7%) | bid $3.69 / ask $4.95 x100 | SPIKE 16:00ET +16% $4.98 1801tr/181k sh |
| PN | ~$8.57 | Peak H $10.45 @16:00ET (505K sh) → faded to $8.29 | ~$8.29 | bid $4.83 / **ask $0.00 x0** | (NO-SPIKE) |
| LABT | $3.41 | Real surge 16:10ET H $3.87 (470K sh/4276tr) → faded to $3.46 | ~$3.46 (+1.5%) | bid $2.93 / ask $3.89 x100 | NO-SPIKE peak +13% @16:11ET |

**Evaluation (observation-only, no entries):**
- **ZCMD** — Classic **SPIKE→FADE** from the opening bar: peaked +37% ($5.58) at 16:00 ET, faded every subsequent bar back toward close (~+5% AH now). Also extremely extended (RTH already +176.9%; total >180% blows past the +150% ceiling). Fillable book (ask $4.95 x100) but trajectory is fading, not building. **Would skip** on both SPIKE→FADE and ceiling even at 23:00. Watch for a base-build across 23:00/23:30 before any consideration.
- **LABT** — Sub-1M float (956K) biotech, real volume surge at 16:10 ET but immediately faded from $3.87 to $3.46. AH only +7.1%, NO-SPIKE (peak +13%, never cleared +15% co-spike). Below the 2-AH-scan >10% gate. Watch.
- **PN** — `ask $0.00 x0` = **no fillable AH book** → illiquid, would skip on liquidity sanity check regardless. Also fading and higher-cap ($57.7M). NO-SPIKE.
- **CHAI** — Low AH change (+5%), NO-SPIKE, 9M float packaged software. Below gate.
- **ZYBT** — Day **−51.6%** (crashed >15% in regular session), bouncing +9.4% in AH but total still **−47%** (far below close). Classic **dead-cat bounce** — skip. No dead-cat-override (reclaim requires building *above* close; ZYBT is nowhere near it).

**No entries** (observation-only window before 23:00 CET). No candidate currently shows a BUILD/hold pattern — the strongest volume names (ZCMD, LABT, PN) all faded from opening-bar spikes. Re-check all at 23:00 CET for hold-vs-fade before any entry decision.

## Scan 22:15 CET (4:15 PM ET)

**Bonus AH scan.** `scan.py --all` returned **0 hits** (16:15:11 ET) — but this is a **feed-lag artifact on the opening bar**. Ad-hoc SIP cross-check of the 21:30 watch names shows real AH accumulation already:

| Ticker | RTH Close | 1st AH bar (16:00 ET) | AH Vol | Trades | AH H | Quote (book) | Spike-bar |
|--------|-----------|-----------------------|--------|--------|------|--------------|-----------|
| ZCMD | $4.07 | C $4.90 (+20%) | 1.28M sh | 15,483 | $5.58 | bid $3.69 / ask $4.95 x100 | **SPIKE 16:00ET +16% $4.98 1801tr/181k sh** |
| PN | ~$8.57 | C $8.46 | 505K sh | 7,622 | $10.45 | bid $4.83 / **ask $0.00 x0** | NO-SPIKE peak +12% @16:00ET |
| LABT | ~$3.17 | C $3.30 | 43.9K sh | 385 | $3.42 | bid $2.93 / ask $3.89 x100 | (thin, not run) |

**Notes:**
- **ZCMD** — real AH liquidity (1.28M sh / 15.5k trades on the first bar) AND a fillable two-sided book (ask $4.95 x100). Spike-bar detector fired an ignition (SPIKE 16:00ET). Strongest AH continuation candidate so far. Total move very extended (RTH already +176.9%, now +20% more in AH) — flag the **+150% extension ceiling** for the 23:00 entry decision. Watch trajectory across 22:30/23:00.
- **PN** — real volume (505K sh) but the Alpaca book shows **ask $0.00 x0** = no fillable AH offer → illiquid (no AH book), would skip on the liquidity sanity check even if it qualifies. Also $57.7M cap, higher-float profile. Spike-bar: NO-SPIKE.
- **LABT** — sub-1M float (956K) but AH volume thin (43.9K sh / 385 trades). Not accumulating yet.
- The scanner's 0-hit is the known opening-bar feed lag; SIP is truth here. No entries (observation-only window before 23:00 CET). Re-check all three at 22:30/23:00 for hold-vs-fade before any entry.

## Scan 22:00 CET (4:00 PM ET)

**First AH scan** — AH opens exactly at 16:00 ET, so this scan runs at the opening tick when little AH volume has accumulated. Scanner returned **0 hits** (`scan.py --all`, 16:00:12 ET). Observation-only window (learning phase: no entries before 23:00 CET).

No AH candidates yet. Carrying the 21:30 regular-session watch names to check for AH confirmation at 22:30+:
- **ZCMD** (+176.9% RTH, 1.1M float) — most extended; watch for hold vs fade into AH.
- **PN** (+112.7%, 1.1M float, $57.7M cap) — utility, unusual for low-float spike.
- **LABT** (+70.2%, 956K float biotech) — prime float profile.
- **INLF** (+52.9%, 1.0M float) — recurring pump name, already faded once in this morning's PM retrospective; watch for fade.
- **KSCP** (+45.7%, 15.2M float) — negative-control profile.
- **KUST** (+40.5%, 577K float) — repeat pump name, deprioritized (faded to $1.01 last night).

No entries this scan (first AH scan + observation-only window). Next scan 22:30 CET.

## Scan 21:30 CET (3:30 PM ET)

**REGULAR session** — 30 min before AH open (16:00 ET / 22:00 CET). Per the regular-session caution rule, **no paper trades**. Candidates below are flagged **Watch — pending AH confirmation**; only enter if they reappear in an AH scan (22:00+ CET) with sustained momentum. Intraday spikers that don't carry into AH tend to fade.

Noise filtered out (sub-1K 5-min volume prints: GLVT +793%, LXEIF +844%, APHD +213%, SKYC +160%, BGMSP +100%, VNOV +72.5%, GAMG +72.3%, PAVLF +60.4% — all <1K shares, not tradeable signals). Real-volume, lower-float watch candidates:

| Ticker | Chart | Price | Day% | 5mVol | Avg5m | IRVol | Float | MCap | Industry |
|--------|-------|-------|------|-------|-------|-------|-------|------|----------|
| ZCMD | [TV](https://www.tradingview.com/chart/?symbol=ZCMD) | $4.07 | +176.9% | 136K | 302K | 163.5 | 1.1M | $1.7M | Misc Commercial Services |
| PN | [TV](https://www.tradingview.com/chart/?symbol=PN) | $8.57 | +112.7% | 336K | 301K | 275.2 | 1.1M | $57.7M | Electric Utilities |
| LABT | [TV](https://www.tradingview.com/chart/?symbol=LABT) | $3.17 | +70.2% | 55K | 125K | 292.6 | 956K | $5.5M | Biotechnology |
| INLF | [TV](https://www.tradingview.com/chart/?symbol=INLF) | $3.41 | +52.9% | 20K | 45K | 231.4 | 1.0M | $3.6M | Industrial Machinery |
| KSCP | [TV](https://www.tradingview.com/chart/?symbol=KSCP) | $2.08 | +45.7% | 70K | 64K | 30.4 | 15.2M | $35.9M | Industrial Machinery |
| NTRX | [TV](https://www.tradingview.com/chart/?symbol=NTRX) | $0.62 | +73.9% | 3K | 1K | 1.9 | 9.8M | $9.4M | Wholesale Distributors |
| INM | [TV](https://www.tradingview.com/chart/?symbol=INM) | $1.70 | +10.1% | 19K | 30K | 777.7 | 2.5M | $5.6M | Pharmaceuticals: Major |

**Watch notes:**
- **ZCMD** — Biggest real-volume mover (+176.9%, 1.1M float, 136K/5min). Total move already extended; watch whether it holds into AH or fades. IRVol 163x = genuine unusual activity.
- **PN** — +112.7% on 336K/5min, 1.1M float, but $57.7M cap (higher). Electric utility is an unusual sector for a low-float spike; catalyst check needed if it carries to AH.
- **LABT** — Sub-1M float (956K) biotech +70.2%. Prime float profile; watch for AH continuation.
- **INLF** — 1.0M float industrial +52.9%. Note: appeared as a fader in this morning's retrospective PM scan (+58% $3.53). Recurring pump name — watch for fade.
- **KSCP** — +45.7%, higher float (15.2M). Negative-control profile.
- **KUST** (+40.5%, 577K float) — carried from last night; was a dead-cat-override watch that faded to $1.01. Repeat pump name, deprioritized.
- No entries this scan (regular session). Next scan 22:00 CET is the first AH scan.
