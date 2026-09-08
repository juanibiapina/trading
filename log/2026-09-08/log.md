# 2026-09-08 (Tuesday) — Post-Labor-Day session

## Morning Evaluation — 10:20 CET

### Context: no overnight after-hours session

Monday **Sep 7 was Labor Day — US market closed**. There was no real after-hours
session last night, so the AH→PM overnight pattern was structurally impossible.
- The Sep 7 evening "scans" ran (9 sections logged) but saw only **stale Friday
  `postmarket_volume`** — `broker.js clock` = `is_open=false`, all quotes stamped
  `2026-09-04T20:00Z`. Correctly SKIP-ALL'd as a holiday, no tradable book.
- Friday **Sep 4 evening is never scanned by design** (prior Fridays Aug 28 / Aug 21 /
  Aug 14 all have 0 scan commits — you cannot cleanly hold an AH entry over a weekend).
- **This is a holiday no-session day, not a coverage failure and not a detection miss.**
  Baseline is NOT incremented (a day with no session is not a counted sample).

### Today's Winner

**No AH→PM winner today** — no after-hours session existed (Labor Day). No stock could
have shown the AH→PM pattern.

Biggest **live premarket** mover this morning is a pure PM-only gapper:

**BNC** — CEA Industries Inc. (BNB / crypto-treasury + controlled-env-ag climate systems)
- Catalyst: none verified same-day. BNB digital-asset-treasury name; move is consistent
  with a crypto rally over the long weekend. Grade **None** (unverified).
- Previous Close (Fri Sep 4, SIP-confirmed): **$3.49**
- Friday AH: **flat** — +3–4% on tiny volume (137–6,400 sh/bar). No AH footprint.
- Premarket now: SIP first bars $6.01 (04:00 ET) / $5.94 (04:05 ET); Yahoo high $6.67 @04:20
- **From correct $3.49 close: ~+72% (SIP $6.01) to ~+93% (peak ~$6.72) — BELOW the >100% bar.**
  (The "+102.7%" Yahoo print used a stale $3.29 = Wed Sep 3 close, not Friday's $3.49.)
- SIP volume: **1.72M sh / 19,336 trades** @04:00, **1.39M sh / 18,550 trades** @04:05 —
  genuine, heavy, liquid. Holdable in character, but **uncapturable overnight** (no AH
  session to enter; flat in the only AH session it had, Friday).
- Float: 36.2M | Market Cap: ~$143.8M

**Scanner Diagnostic:**
- Detectable at screening time? **N/A** — there was no evening screening session (holiday).
- BNC was flat in Friday's AH (+3–4%, no volume) and gapped only in Tuesday premarket on
  weekend news → a **PM-only gapper**, structurally undetectable by the AH scanner.
- Scanner gap: none actionable. Holiday + PM-only gapper. Not a detection miss.

### Baseline Tracking

Holiday, no session evaluated — baseline unchanged (not a counted sample; no back-fill).

- Days tracked: **78** (unchanged — Sep 7 was a market holiday, no session)
- Winners detected by scanner: **64/73 (87.7%)** — unchanged
- Winner selected for paper trade: **35/71 (49.3%)** — unchanged
- Target: >80% detection
- Status: **BASELINE MET** (87.7% detection)

### Retrospective Scan Results

- Live PM scan (Sep 8, 04:22 ET): 6 hits — GMEX +36.4%, BNC +61.5% (scan basis; +72–93%
  vs correct close), ISPC +29.9%, WETO +5.3%, CYPH +6.2%, VIVK +6.4%.
- Only BNC is a strong mover; it is a PM-only gapper (flat Friday AH). GMEX +34% (0.78→1.05),
  low volume by comparison. None cleared the >100% winner bar from the correct prev close.
- No AH reconstruction applies (no AH session last night).

### Open Position P&L (Alpaca)

No open positions. Alpaca (source of truth) shows zero holdings. No executed positions.
Last entries (CHPT, TLYS, GIPR, PLAG) were all exited Sep 4; flat since.

### Scanner Effectiveness

- Evening scans ran: **N/A — market holiday** (Sep 7 Labor Day). The 9 logged "scans"
  saw only stale Friday data; Friday Sep 4 evening is never scanned by design.
- Candidates found: none tradable (holiday).
- Retrospective matches: N/A.

### Missed Opportunities

No significant missed opportunities. BNC (biggest PM mover, ~+72–93%) is a PM-only gapper
on holiday-weekend news — structurally undetectable by the AH scanner, not a miss.

### AH Mover Follow-Through

N/A — no after-hours session last night (Labor Day). No AH movers to follow through.

### Price Charts

```
BNC - 2-Day Price Timeline (5-min intervals)
Previous Close (correct, SIP): $3.49  |  Peak: ~$6.72 (~+93% from $3.49) at 04:20 ET
Friday AH: FLAT (+3-4%, 137-6,400 sh/bar) — no AH footprint
Tuesday PM: gapped $3.49 -> ~$6.0-6.7 on 1.4-1.7M sh/bar, 18-19K trades/bar (heavy, liquid)
Shape: pure PM-only gapper (weekend/holiday news), not an AH->PM continuation
```

### Notes

- **Holiday no-session day (Sep 7 Labor Day).** No AH session → no AH→PM winner possible →
  baseline unchanged at 78 / 64 detected / 35 selected. Not a coverage failure (scanner is
  not scheduled for a closed market) and not a detection miss.
- **Friday evenings are never scanned** (confirmed: Aug 28 / Aug 21 / Aug 14 = 0 scan
  commits). This is by design (no clean weekend hold). Missing Sep 4 evening scan is expected.
- **BNC prev-close correction:** true Friday close is **$3.49** (SIP daily bar), not the
  $3.29 that Yahoo `--pm-history` and `price-timeline.py` use (that $3.29 is Wed Sep 3's
  close). On the correct basis BNC's PM peak is ~+93%, **below** the >100% winner bar — so
  even the biggest mover today does not qualify as a crowned winner. Reinforces checking the
  % basis against the SIP daily bar before crowning.
- **PM-only-gapper tracking:** biggest raw PM mover = BNC (~+72–93%), holdable in character
  (1.4–1.7M sh/bar, 18–19K trades/bar) but uncapturable overnight. The dedicated
  `pm-open-scan` pulse owns the authoritative holdable classification (standing holdable
  count in `pm-open-scan.csv`: **43**). No hand-count maintained here. Not a detection miss.
- All standing tracker counts carry over unchanged (no new cases on a no-session night):
  in-window feed-lag misses 4 (≥3 escalation trigger REACHED); price-floor exclusions 5/0
  holdable; stale-book execution-blocks 3; no-fillable-book skips 2; float-gate skips 1;
  final-scan gate-blocks 2 (TRUG, UPC); AH-peak-vs-PM-peak extreme zone 8 fade / 1 continue
  (routing trigger REACHED); reverse-split this-week bucket 4/4 fade (RESOLVED).

## Position Evaluation — 10:30 CET

No open positions. Alpaca (source of truth) shows zero holdings; `OPEN_POSITIONS.md`
current table also empty — they agree, no reconciliation needed. Nothing to hold, trail,
or sell. Flat since Sep 4 exits (CHPT, TLYS, GIPR, PLAG). Sep 7 was Labor Day (no session).

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| — | — | — | — | — | — | — | — | No open positions |

**Actions taken:**
- None. Flat account, no positions to evaluate.

## Position Evaluation — 14:30 CET

No open positions. Alpaca (source of truth) shows zero holdings; `OPEN_POSITIONS.md`
current table also empty — they agree, no reconciliation needed. Nothing to hold, trail,
or sell. Flat since Sep 4 exits. Sep 7 was Labor Day (no session), no overnight entries.

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| — | — | — | — | — | — | — | — | No open positions |

**Actions taken:**
- None. Flat account, no positions to evaluate.

## Scan 21:30 CET (3:30 PM ET)

**Regular-session watch scan — AH not yet open (15:30 ET). No entries per regular-session
caution rule.** Flag notable low-float movers as "Watch — pending AH confirmation." Only
enter if a name reappears in an AH scan (22:00+ CET) with sustained momentum.

Scanner: 36 regular-session hits. Notable low-float / high-move watch candidates:

| Ticker | Chart | Price | Chg% | Float | MCap | IRVol | Industry | Note |
|--------|-------|-------|------|-------|------|-------|----------|------|
| INDP | [TV](https://www.tradingview.com/chart/?symbol=INDP) | $1.82 | +49.3% | 4.7M | $242.6M | 35.0 | Pharmaceuticals: Major | Watch — pending AH |
| MOBX | [TV](https://www.tradingview.com/chart/?symbol=MOBX) | $1.30 | +40.3% | 14.6M | $22.2M | 43.9 | Semiconductors | Watch — pending AH |
| NUR | [TV](https://www.tradingview.com/chart/?symbol=NUR) | $2.53 | +42.9% | n/a | $33.1M | 1690.5 | Electronics Distributors | Watch — pending AH |
| BNC | [TV](https://www.tradingview.com/chart/?symbol=BNC) | $5.35 | +53.3% | 36.2M | $220.3M | 117.6 | Trucks/Constr Machinery | Same as AM PM-gapper (crypto-treasury) |
| SST | [TV](https://www.tradingview.com/chart/?symbol=SST) | $5.01 | +30.7% | 2.2M | $52.5M | 3.5 | Packaged Software | Watch — pending AH |
| ETS | [TV](https://www.tradingview.com/chart/?symbol=ETS) | $1.09 | +31.3% | n/a | $53.1M | 257.1 | Air Freight/Couriers | Watch — pending AH |
| SWVL | [TV](https://www.tradingview.com/chart/?symbol=SWVL) | $6.40 | +29.8% | 5.3M | $63.8M | 0.3 | Other Transportation | Watch — low IRVol |
| HCWC | [TV](https://www.tradingview.com/chart/?symbol=HCWC) | $8.54 | +21.7% | 711K | $7.9M | 3.0 | Food Retail | Watch — tiny float |
| KPLT | [TV](https://www.tradingview.com/chart/?symbol=KPLT) | $9.50 | +20.3% | 1.2M | $47.2M | 5.5 | Misc Commercial Svcs | Watch — pending AH |
| LABT | [TV](https://www.tradingview.com/chart/?symbol=LABT) | $2.25 | +19.7% | 1.6M | $5.3M | 1.4 | Biotechnology | Watch — pending AH |

**Notes:**
- This is the pre-AH watch scan. No paper trades entered (learning-phase rule: no entries
  before AH opens; observation only until 22:00+ CET, entries only at 23:00+ CET).
- ARBE (+15.0%, IRVol 55.1) and MOBX (+40.3%, IRVol 43.9) show the strongest intraday
  relative-volume; carry both into AH scans.
- BNC already flagged this morning as a PM-only crypto-treasury gapper (Friday AH flat).
  Now +53% in regular session — watch whether it carries an AH footprint tonight.
- No spike-bar / CONFIRM-3 instrumentation run — those apply to AH candidates (>10% AH
  change), and AH is not yet open.

## Scan 22:00 CET (4:00 PM ET)

**Observation-only scan (learning-phase: no entries before 23:00 CET).** AH just opened
this minute (16:00 ET) — VRatio has not accumulated yet.

Scanner: **0 hits.** No candidates cleared the AH threshold at 16:00 ET.

**Notes:**
- AH opened exactly at scan time (16:00:18 ET); `postmarket_volume` has not built, so the
  screener shows no matches yet. Expected at the first AH scan.
- Carry the 21:30 regular-session watch names into later AH scans: **BNC** (+53% RS,
  crypto-treasury gapper), **MOBX** (+40%, IRVol 43.9), **ARBE** (+15%, IRVol 55.1),
  **INDP** (+49%, 4.7M float), **NUR** (+43%), plus tiny-float **HCWC** (711K), **SST**
  (2.2M), **KPLT** (1.2M), **LABT** (1.6M).
- No spike-bar / CONFIRM-3 instrumentation — no AH candidates >10% yet.
- Next scan 22:30 CET (observation), first possible entries at 23:00 CET.

## Scan 22:15 CET (4:15 PM ET)

**Observation-only scan (learning-phase: no entries before 23:00 CET).**

Scanner: **0 hits.** No candidates cleared the AH threshold at 16:15 ET.

SIP cross-check of carry-forward watch names (first AH bar, 16:00–16:05 ET) — all
holding regular-session levels, none spiking further in AH, none >10% AH change:

| Ticker | AH bar C | vs RS close | AH vol | trades | Note |
|--------|----------|-------------|--------|--------|------|
| BNC | $5.25 | ~flat ($5.35 RS) | 80.8K | 307 | crypto-treasury gapper, no AH extension |
| INDP | $1.85 | ~flat ($1.82 RS) | 33.6K | 275 | holding RS gain, no AH spike |
| MOBX | $1.28 | ~flat ($1.30 RS) | 176.9K | 461 | most AH volume, but flat |
| NUR | $2.45 | ~flat ($2.53 RS) | 83.9K | 676 | slight fade off RS |

**Notes:**
- TradingView scanner 0 hits; SIP confirms no name is extending in AH — all carry-forward
  watch candidates are just holding intraday gains, no fresh AH momentum/ignition.
- No spike-bar / CONFIRM-3 instrumentation run — no candidate shows >10% AH change.
- No entries (observation-only window; also no qualifying candidate).
- Carry all watch names forward to 23:00 CET (first possible entry scan). Watch whether any
  builds a real AH footprint before then.

## Scan 22:30 CET (4:30 PM ET)

**Observation-only scan (learning-phase: no entries before 23:00 CET).** First real AH
volume has now accumulated (16:30 ET). Scanner: **5 hits.**

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| SUNE | [TV](https://www.tradingview.com/chart/?symbol=SUNE) | $2.37 | +0.4% | +20.0% | $2.84 | +20.5% | 2.7M | 545K | 4.9x | 5.4M | Engineering & Construction |
| TWG | [TV](https://www.tradingview.com/chart/?symbol=TWG) | $0.52 | +17.8% | +6.5% | $0.56 | +25.4% | 2.3M | 8.4M | 0.3x | 44.5M | Food Distributors |
| LHSW | [TV](https://www.tradingview.com/chart/?symbol=LHSW) | $1.32 | -70.7% | +12.9% | $1.49 | -66.9% | 1.9M | 2.4M | 0.8x | 1.0M | Computer Processing Hardware |
| ANY | [TV](https://www.tradingview.com/chart/?symbol=ANY) | $2.45 | +5.6% | +12.7% | $2.76 | +19.0% | 225K | 313K | 0.7x | 6.5M | Information Technology Services |
| FGL | [TV](https://www.tradingview.com/chart/?symbol=FGL) | $7.57 | -18.6% | +28.1% | $9.70 | +4.3% | 44K | 194K | 0.2x | 60K | Engineering & Construction |

**Spike-bar / CONFIRM-3 instrumentation (log-only, >10% AH names):**
- `SUNE  SPIKE 16:05ET +35% $3.19 942 trades / 248k sh (first co-spike bar)` — `CONFIRM-3 NO ignition 16:05ET failed third-bar hold/volume` — **FIRST-BAR-SPIKE** (AH high in first bar + CONFIRM-3 NO)
- `ANY   SPIKE 16:06ET +20% $2.95 241 trades / 48k sh` — `CONFIRM-3 NO ignition 16:05ET failed third-bar hold/volume` — **FIRST-BAR-SPIKE**
- `LHSW  SPIKE 16:05ET +66% $2.19 2571 trades / 439k sh` — `CONFIRM-3 NO no local-volume new-high ignition`
- `FGL   SPIKE 16:03ET +45% $11.00 365 trades / 9k sh` — `CONFIRM-3 NO no local-volume new-high ignition`

**Per-candidate evaluation:**
- **SUNE — strongest carry candidate.** SIP shows *real, heavy accumulation*: 1.49M / 1.66M
  / 1.0M sh per bar, 10.1k / 14.5k / 8.3k trades — genuine liquid AH, not a stale VRatio.
  VWAP $2.85→$2.99 corroborates scanner AH price (no bad print). Fresh **real-time book**
  bid $2.97 x100 / ask $3.00 x100 (20:30Z). Day% +0.4% = **pure AH ignition** (not a
  dead-cat, not extended intraday). Total +20.5% is well under the +150% ceiling. Float 5.4M.
  `tradable=true`. Catalyst: **SUNation Energy strategic financing agreement with Participate
  Energy** to support residential solar + battery growth (GlobeNewswire, same-day) — **Grade
  C** (financing/partnership, weak). First-bar-spike + CONFIRM-3 NO noted, but volume is
  accumulating across bars and price is *holding within ~6% of the $3.19 peak* ($2.98–3.00),
  which reads as hold, not fade. **Carry to 23:00 CET for entry** — needs a 2nd AH scan >10%
  to clear the gate (this is scan #1 above 10%).
- **TWG** — AH change +6.5% (below the 10% instrumentation/qualifying bar). High float 44.5M,
  VRatio 0.3x (AH vol below its huge 8.4M avg). Day +17.8% is regular-session. Watch only.
- **LHSW** — **dead-cat bounce, skip.** Day −70.7%, Total −66.9% (deep below regular close —
  a true dead-cat, still far under prior close). SIP: spiked $2.19 @16:05 then faded to
  $1.46 (SPIKE→FADE). Recovering from a crash, not building. Skip per dead-cat rule.
- **ANY** — real but light AH vol (120–141k sh/bar), quote stale + wide (bid $1.99 / ask
  $2.84 @20:00Z). SPIKE→FADE off $2.95 @16:06 to ~$2.72. First-bar-spike, CONFIRM-3 NO. Watch
  only, weak.
- **FGL** — **illiquid microfloat, skip.** Float 60K, AH vol only 44K (9–16k sh/bar). $11.84
  print faded to $9.00; quote stale + very wide (bid $6.36 / ask $10.13). Total only +4.3%
  (Day −18.6% dead-cat + bounce). Bad-print / no clean fillable book. Skip.

**Notes:**
- Observation-only window — **no entries this scan.** SUNE is the clear carry candidate; it
  needs to hold >10% AH into the 23:00 CET scan (2nd AH scan) to clear the 2-AH-scan gate.
- Carry-forward 21:30 regular-session watch names (BNC, MOBX, INDP, NUR, etc.) did **not**
  appear in the AH scanner and are not extending in AH — dropping unless they re-ignite.
- Next scan 23:00 CET (first possible entry). If SUNE holds >10% AH with accumulating SIP
  volume, it clears the gate and qualifies for entry.

## Scan 22:45 CET (4:45 PM ET)

**Observation-only scan (learning-phase: no entries before 23:00 CET).** AH volume
accumulating (16:45 ET). Scanner: **5 hits.**

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| SUNE | [TV](https://www.tradingview.com/chart/?symbol=SUNE) | $2.37 | +0.4% | +24.9% | $2.96 | +25.5% | 5.1M | 826K | 6.1x | 5.4M | Engineering & Construction |
| TWG | [TV](https://www.tradingview.com/chart/?symbol=TWG) | $0.52 | +17.8% | +5.1% | $0.55 | +23.7% | 2.7M | 8.4M | 0.3x | 44.5M | Food Distributors |
| ANY | [TV](https://www.tradingview.com/chart/?symbol=ANY) | $2.45 | +5.6% | +19.2% | $2.92 | +25.9% | 746K | 372K | 2.0x | 6.5M | Information Technology Services |
| ARBE | [TV](https://www.tradingview.com/chart/?symbol=ARBE) | $0.74 | +16.9% | +6.3% | $0.79 | +24.3% | 616K | 10.6M | 0.1x | 106.2M | Electrical Products |
| FGL | [TV](https://www.tradingview.com/chart/?symbol=FGL) | $7.57 | -18.6% | +18.5% | $8.97 | -3.5% | 65K | 198K | 0.3x | 60K | Engineering & Construction |

**Spike-bar / CONFIRM-3 instrumentation (log-only, >10% AH names):**
- `SUNE  SPIKE 16:05ET +35% $3.19 942 trades / 248k sh (first co-spike bar)` — `CONFIRM-3 NO ignition 16:05ET failed third-bar hold/volume` — **FIRST-BAR-SPIKE** (AH high in first bar + CONFIRM-3 NO)
- `ANY   SPIKE 16:06ET +20% $2.95 241 trades / 48k sh` — `CONFIRM-3 NO ignition 16:05ET failed third-bar hold/volume` — **FIRST-BAR-SPIKE**
- `FGL   SPIKE 16:03ET +45% $11.00 365 trades / 9k sh` — `CONFIRM-3 NO no local-volume new-high ignition`

**Per-candidate evaluation:**
- **SUNE — cleared the 2-AH-scan gate** (>10% AH at 22:30 +20.0% and 22:45 +24.9%). SIP
  confirms *real, heavy accumulation across every bar*: 1.49M / 1.66M / 1.0M / 1.14M / 674K /
  784K sh, 10.1k / 14.5k / 8.3k / 9.0k / 5.1k / 6.0k trades — VRatio 6.1x, not a stale figure.
  VWAP $2.85→$3.00 corroborates the scanner AH price (no bad print). Fresh real-time book
  bid $2.90 x100 / ask $2.93 x100 (20:45Z), tight. Day% +0.4% = **pure AH ignition** (not
  dead-cat, not intraday-extended). Total +25.5% is well under the +150% ceiling. Float 5.4M
  (<50M). `tradable=true`. Catalyst: SUNation Energy strategic financing agreement with
  Participate Energy for residential solar+battery growth (GlobeNewswire, same-day) — **Grade
  C** (financing/partnership, weak). First-bar-spike + CONFIRM-3 NO noted (log-only, no
  decision impact), but price is *holding within ~7% of the $3.19 first-bar high* ($2.93–3.00)
  on accumulating volume — reads hold, not fade. **Ready for entry at the 23:00 CET scan.**
- **ANY — also cleared the 2-AH-scan gate** (>10% AH at 22:30 +12.7% and 22:45 +19.2%). SIP
  vol lighter and choppier (120K/141K/119K/84K/397K/461K sh; 821/1044/627/583/3077/3323
  trades) — real but a fraction of SUNE. Price churns $2.68–2.98, no clean build; first-bar
  high $2.95, CONFIRM-3 NO. Fresh-ish book bid $2.73 / ask $2.76 (20:33Z). Day% +5.6%, Total
  +25.9% under ceiling, float 6.5M, `tradable=true`. Weaker BUILD than SUNE but qualifies —
  **carry to 23:00 for entry evaluation** (catalyst search pending at 23:00).
- **TWG** — AH +5.1% (below 10% bar), high float 44.5M, VRatio 0.3x. Regular-session mover.
  Watch only.
- **ARBE** — AH +6.3% (below 10% bar), float 106.2M (>50M), VRatio 0.1x. Watch only.
- **FGL** — **illiquid microfloat, skip.** Float 60K, AH vol 65K, quote stale + very wide
  (bid $6.36 / ask $10.13 @20:00Z). Total −3.5% (Day −18.6% dead-cat + bounce). SPIKE→FADE
  $11.00→$8.97, bad-print / no fillable book. Skip.

**Notes:**
- Observation-only window — **no entries this scan** (learning-phase: entries only at 23:00+).
- Two names have now cleared the 2-AH-scan gate: **SUNE** (strong, heavy-volume BUILD, Grade
  C catalyst) and **ANY** (weaker, choppier, no confirmed catalyst yet). Both hold within
  ~20% of their AH highs; multiple positions allowed. Evaluate both for entry at 23:00 CET.
- Carry-forward 21:30 regular-session watch names (BNC, MOBX, INDP, NUR, etc.) still absent
  from the AH scanner — dropped unless they re-ignite.
- Next scan 23:00 CET — first possible entries.

## Scan 23:00 CET (5:00 PM ET)

**First entry-eligible scan (learning-phase: entries allowed 23:00+ CET).** Scanner: **7 hits.**

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| SUNE | [TV](https://www.tradingview.com/chart/?symbol=SUNE) | $2.37 | +0.4% | +20.7% | $2.86 | +21.2% | 6.5M | 1.0M | 6.5x | 5.4M | Engineering & Construction |
| GCDT | [TV](https://www.tradingview.com/chart/?symbol=GCDT) | $0.91 | +143.3% | +9.1% | $0.99 | +165.4% | 17.1M | 39.5M | 0.4x | n/a | Engineering & Construction |
| TWG | [TV](https://www.tradingview.com/chart/?symbol=TWG) | $0.52 | +17.8% | +7.5% | $0.56 | +26.6% | 4.3M | 8.6M | 0.5x | 44.5M | Food Distributors |
| ANY | [TV](https://www.tradingview.com/chart/?symbol=ANY) | $2.45 | +5.6% | +8.9% | $2.67 | +15.0% | 1.3M | 442K | 3.0x | 6.5M | Information Technology Services |
| MOBX | [TV](https://www.tradingview.com/chart/?symbol=MOBX) | $1.27 | +36.5% | +5.5% | $1.34 | +44.1% | 1.2M | 15.8M | 0.1x | 14.6M | Semiconductors |
| FGL | [TV](https://www.tradingview.com/chart/?symbol=FGL) | $7.57 | -18.6% | +30.4% | $9.87 | +6.2% | 94K | 205K | 0.5x | 60K | Engineering & Construction |
| EONR | [TV](https://www.tradingview.com/chart/?symbol=EONR) | $0.58 | +3.8% | +5.5% | $0.61 | +9.5% | 65K | 691K | 0.1x | 39.8M | Integrated Oil |

**Spike-bar / CONFIRM-3 instrumentation (log-only, >10% AH names):**
- `SUNE  SPIKE 16:05ET +35% $3.19 942 trades / 248k sh (first co-spike bar)` — `CONFIRM-3 NO ignition 16:05ET failed third-bar hold/volume` — **FIRST-BAR-SPIKE** (AH high in first bar + CONFIRM-3 NO)
- `ANY   SPIKE 16:06ET +20% $2.95 241 trades / 48k sh` — `CONFIRM-3 NO ignition 16:05ET failed third-bar hold/volume` — **FIRST-BAR-SPIKE**
- FGL — illiquid microfloat carried skip (below), no instrumentation re-run.

**Per-candidate evaluation:**
- **SUNE — ENTERED.** Cleared the 2-AH-scan gate (>10% AH at 22:30 +20.0%, 22:45 +24.9%, 23:00 +20.7% — 3 AH scans). SIP confirms real heavy accumulation across every bar: 1.49M / 1.66M / 1.0M / 1.14M / 674K / 784K / 515K / 443K / 269K sh, 10.1k / 14.5k / 8.3k / 9.0k / 5.1k / 6.0k / 4.1k / 3.8k / 2.5k trades — VRatio 6.5x, not a stale figure. VWAP $2.85→$3.00 corroborates scanner AH price (no bad print). Fresh real-time book bid $2.91 x100 / ask $2.95 x100 (20:59Z), tight. Day% +0.4% = **pure AH ignition** (not dead-cat, not intraday-extended). Total +21.2% well under the +150% ceiling. Float 5.4M (<50M). `tradable=true`. **Not a multi-session runner** — WINNERS_TRACKING SUNE entry is 2026-03-18 (6 months old, unrelated); today Day% +0.4% = fresh day-1 AH igniter. Catalyst: SUNation Energy strategic financing agreement with Participate Energy for residential solar+battery growth (GlobeNewswire, same-day) — **Grade C** (financing/partnership, weak). First-bar-spike + CONFIRM-3 NO noted (log-only, no decision impact); price holding within ~7% of the $3.19 first-bar high on accumulating volume reads hold, not fade. Volume tapering in the latest bars (269K last vs 1.5M first) — noted, but still liquid and within 20% of high. **Order: BUY 33 @ limit $2.99 ext → filled $2.95** (id ca713441).
- **ANY — skip (SPIKE→FADE, faded below threshold).** Cleared the gate earlier (22:30 +12.7%, 22:45 +19.2%) but AH change has now dropped to +8.9% (below 10%) at this entry scan. SIP shows a clear fade: volume peaked 397K/460K sh at 16:25/16:30 ET then collapsed to 151K/62K/33K; price faded $2.98 → $2.65 across bars. First-bar-spike $2.95 @16:06, CONFIRM-3 NO. Declining across scans with collapsing volume = fade, not hold. Trajectory dominates: SUNE (BUILD/hold) preferred over ANY (SPIKE→FADE). Skip.
- **GCDT** — AH +9.1% (below 10% bar). Day% +143.3% (huge regular-session runner), Total +165.4% **above the +150% ceiling**. VRatio 0.4x (AH vol below huge 39.5M avg). Extended intraday, no AH ignition. Skip.
- **TWG** — AH +7.5% (below 10% bar). High float 44.5M, VRatio 0.5x. Regular-session mover. Watch only.
- **MOBX** — AH +5.5% (below 10% bar). VRatio 0.1x (AH vol far below 15.8M avg). Regular-session mover fading in AH. Watch only.
- **FGL** — **illiquid microfloat, skip (carried).** Float 60K, AH vol 94K, Total only +6.2% (Day −18.6% dead-cat + bounce). Stale + very wide quote across prior scans, bad-print / no fillable book. Skip.
- **EONR** — AH +5.5% (below 10% bar), VRatio 0.1x. Watch only.

**Chase-cap check (log-only):** SUNE qualifying-scan Total% +20.5% (22:30) to +25.5% (22:45); fill $2.95 = Entry Total% +24.5%, within the qualifying range. Limit $2.99 filled at the $2.95 ask, no chase above the qualifying AH price. No CHASE-CAP concern (well under the +120% fade zone).

**Notes:**
- **One entry: SUNE** (Grade C, fresh day-1 AH igniter, heavy volume-backed BUILD/hold). Filled $2.95, 33 shares (~$97).
- ANY was the only other gated name; it faded below 10% AH with collapsing volume — SPIKE→FADE, correctly skipped in favor of the SUNE BUILD.
- Carry-forward 21:30 regular-session watch names (BNC, MOBX, INDP, NUR, etc.) never built a real AH footprint — dropped.
- Grade C hold strategy: exit in premarket (stop -10%). Set premarket exit for SUNE.

## Scan 23:30 CET (5:30 PM ET)

**Entry-eligible scan.** Scanner: **8 hits.** SUNE already entered at 23:00 (position held,
no re-entry — one entry per candidate per night). No new entries this scan.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| SUNE | [TV](https://www.tradingview.com/chart/?symbol=SUNE) | $2.37 | +0.4% | +24.9% | $2.96 | +25.4% | 8.7M | 1.3M | 6.9x | 5.4M | Engineering & Construction |
| ANY | [TV](https://www.tradingview.com/chart/?symbol=ANY) | $2.45 | +5.6% | +11.8% | $2.74 | +18.1% | 1.5M | 464K | 3.3x | 6.5M | Information Technology Services |
| ARBE | [TV](https://www.tradingview.com/chart/?symbol=ARBE) | $0.74 | +16.9% | +6.7% | $0.79 | +24.7% | 1.4M | 10.6M | 0.1x | 106.2M | Electrical Products |
| GMEX | [TV](https://www.tradingview.com/chart/?symbol=GMEX) | $0.63 | -14.5% | +6.6% | $0.68 | -8.8% | 1.3M | 3.0M | 0.4x | n/a | Specialty Stores |
| ISPC | [TV](https://www.tradingview.com/chart/?symbol=ISPC) | $1.59 | +3.2% | +6.9% | $1.70 | +10.4% | 238K | 2.1M | 0.1x | 2.5M | Miscellaneous Commercial Services |
| FGL | [TV](https://www.tradingview.com/chart/?symbol=FGL) | $7.57 | -18.6% | +16.2% | $8.80 | -5.4% | 120K | 210K | 0.6x | 60K | Engineering & Construction |
| ONCO | [TV](https://www.tradingview.com/chart/?symbol=ONCO) | $0.84 | -17.6% | +6.6% | $0.90 | -12.2% | 83K | 875K | 0.1x | 3.9M | Pharmaceuticals: Major |
| CMTG | [TV](https://www.tradingview.com/chart/?symbol=CMTG) | $1.54 | -4.9% | +8.4% | $1.67 | +3.1% | 62K | 713K | 0.1x | 105.1M | Real Estate Investment Trusts |

**Spike-bar / CONFIRM-3 instrumentation (log-only, >10% AH names):**
- `SUNE  SPIKE 16:05ET +35% $3.19 942 trades / 248k sh (first co-spike bar)` — `CONFIRM-3 NO ignition 16:05ET failed third-bar hold/volume` — **FIRST-BAR-SPIKE**
- `ANY   SPIKE 16:06ET +20% $2.95 241 trades / 48k sh` — `CONFIRM-3 NO ignition 16:05ET failed third-bar hold/volume` — **FIRST-BAR-SPIKE**
- FGL — illiquid microfloat carried skip (below), no instrumentation re-run.

**Per-candidate evaluation:**
- **SUNE — held, no re-entry.** Already entered at 23:00 ($2.95, 33 sh, Grade C). AH +24.9%,
  still building/holding, VRatio 6.9x. One entry per candidate per night — no averaging in.
  Position management handled by premarket position-evaluation.
- **ANY — skip (SPIKE→FADE, carried).** Bounced back above 10% (+11.8% AH) but SIP confirms
  fade: peaked 16:25/16:30 ET ($2.98, 397K/460K sh) then volume collapsed to 20–51K sh/bar,
  price churning $2.68 (~10% off the $2.98 high) with no fresh volume-backed build. First-bar
  spike $2.95 @16:06, CONFIRM-3 NO. Modest AH% bounce on thin volume is not a build. Peaked
  early + fading = SPIKE→FADE (0/10+ for PM continuation). `tradable=true`, book bid $2.73 /
  ask $2.76, but no volume ignition. Skip (same as 23:00).
- **ARBE** — AH +6.7% (below 10% bar), float 106.2M (>50M), VRatio 0.1x. Regular-session
  mover, no AH ignition. Watch only.
- **GMEX** — Day −14.5%, AH +6.6% (below bar), Total −8.8% (below regular close = dead-cat).
  Skip.
- **ISPC** — AH +6.9% (below 10% bar), VRatio 0.1x. Watch only.
- **FGL** — **illiquid microfloat, skip (carried).** Float 60K, AH vol 120K, Total −5.4%
  (Day −18.6% dead-cat + bounce). Stale wide quote across all scans, bad-print / no fillable
  book. Skip.
- **ONCO** — Day −17.6%, AH +6.6% (below bar), Total −12.2% (below close = dead-cat). Skip.
- **CMTG** — AH +8.4% (below 10% bar), float 105.1M (>50M), VRatio 0.1x. Skip.

**Notes:**
- **No new entries.** SUNE (only qualifying BUILD) already held from 23:00. ANY re-crossed
  10% AH but on collapsed volume (SPIKE→FADE), correctly skipped again. All other hits below
  the 10% AH bar or dead-cat/illiquid.
- No FINAL-SCAN-GATE-BLOCK, CHASE-CAP, or DEAD-CAT/CEILING-OVERRIDE cases this scan.
- Carry-forward 21:30 regular-session watch names never built an AH footprint — dropped.
- Next scan 00:00 CET.

## Scan 00:00 CET (6:00 PM ET)

**Entry-eligible scan.** Scanner: **11 hits.** SUNE held from 23:00 (position open, no
re-entry — one entry per candidate per night). Two **new** >10% AH names this scan: ZJYL and
ACCL. Neither enterable (see below). No new entries.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| SUNE | [TV](https://www.tradingview.com/chart/?symbol=SUNE) | $2.37 | +0.4% | +22.8% | $2.91 | +23.3% | 9.7M | 1.4M | 7.0x | 5.4M | Engineering & Construction |
| TWG | [TV](https://www.tradingview.com/chart/?symbol=TWG) | $0.52 | +17.8% | +6.2% | $0.55 | +25.1% | 5.1M | 8.7M | 0.6x | 44.5M | Food Distributors |
| ANY | [TV](https://www.tradingview.com/chart/?symbol=ANY) | $2.45 | +5.6% | +13.5% | $2.78 | +19.8% | 1.6M | 472K | 3.3x | 6.5M | Information Technology Services |
| ATER | [TV](https://www.tradingview.com/chart/?symbol=ATER) | $0.73 | +16.4% | +5.2% | $0.77 | +22.4% | 1.4M | 9.5M | 0.1x | 13.7M | Internet Retail |
| ZJYL | [TV](https://www.tradingview.com/chart/?symbol=ZJYL) | $2.02 | -2.9% | +28.5% | $2.60 | +24.8% | 306K | 72K | 4.3x | 64.7M | Medical Specialties |
| EONR | [TV](https://www.tradingview.com/chart/?symbol=EONR) | $0.58 | +3.8% | +5.6% | $0.61 | +9.6% | 306K | 715K | 0.4x | 39.8M | Integrated Oil |
| ONCO | [TV](https://www.tradingview.com/chart/?symbol=ONCO) | $0.84 | -17.6% | +6.0% | $0.89 | -12.7% | 251K | 893K | 0.3x | 3.9M | Pharmaceuticals: Major |
| OFAL | [TV](https://www.tradingview.com/chart/?symbol=OFAL) | $0.72 | -7.7% | +5.6% | $0.76 | -2.6% | 154K | 18.3M | 0.0x | 1.9M | Engineering & Construction |
| LASE | [TV](https://www.tradingview.com/chart/?symbol=LASE) | $0.95 | -32.1% | +5.1% | $1.00 | -28.6% | 154K | 3.0M | 0.1x | 37.3M | Electronic Equipment/Instruments |
| ACCL | [TV](https://www.tradingview.com/chart/?symbol=ACCL) | $2.67 | -2.6% | +10.5% | $2.95 | +7.7% | 138K | 26K | 5.3x | 4.9M | Miscellaneous Commercial Services |
| FGL | [TV](https://www.tradingview.com/chart/?symbol=FGL) | $7.57 | -18.6% | +15.6% | $8.75 | -5.9% | 135K | 212K | 0.6x | 60K | Engineering & Construction |

**Spike-bar / CONFIRM-3 instrumentation (log-only, >10% AH names):**
- `SUNE  SPIKE 16:05ET +35% $3.19 942 trades / 248k sh (first co-spike bar)` — `CONFIRM-3 NO ignition 16:05ET failed third-bar hold/volume` — **FIRST-BAR-SPIKE**
- `ANY   SPIKE 16:06ET +20% $2.95 241 trades / 48k sh` — `CONFIRM-3 NO ignition 16:05ET failed third-bar hold/volume` — **FIRST-BAR-SPIKE**
- `ZJYL  SPIKE 17:07ET +33% $2.68 103 trades / 11k sh (first co-spike bar)` — `CONFIRM-3 NO no local-volume new-high ignition`
- `ACCL  SPIKE 17:26ET +42% $3.80 144 trades / 9k sh (first co-spike bar)` — `CONFIRM-3 NO ignition 17:25ET failed third-bar hold/volume`
- FGL — illiquid microfloat carried skip (below), no instrumentation re-run.

**Per-candidate evaluation:**
- **SUNE — held, no re-entry.** Already entered at 23:00 ($2.95, 33 sh, Grade C). AH +22.8%,
  still holding/building, VRatio 7.0x. Position now $2.96 (+0.3%). One entry per candidate per
  night — no averaging in. Premarket exit handled by position-evaluation.
- **ZJYL — qualified-but-untradable broker-block, skip.** `tradable=false` (broker cannot
  fill) — no position possible regardless of the move. Also float 64.7M (>50M float gate) and
  first AH scan appearance (2-AH-scan gate not cleared). SIP shows a *real* late build though:
  240.5K sh / 2,785 trades @17:40 ET, 216.4K / 2,527 @17:45, H $2.68 corroborates scanner AH
  price $2.60 (no bad print). Genuine move, but uninvestable — recorded as a qualified-but-
  untradable broker-block for the morning-eval tally. Skip.
- **ACCL — SPIKE→FADE + first AH scan, skip/watch.** `tradable=true`, float 4.9M (<50M), Day%
  −2.6% (> −15%), VRatio 5.3x, Total +7.7% under ceiling. Catalyst: Acco Group Holdings launch
  of licensed corporate services in Singapore (GlobeNewswire, same-day ~1 hr ago) — **Grade C**
  (minor business-expansion PR). BUT: (1) first AH scan appearance — **2-AH-scan gate not
  cleared** (cannot enter tonight regardless); (2) SIP shows **SPIKE→FADE**: ignition bar 88K
  sh / 1,428 trades @17:25 ET spiking to H $3.80, then volume collapsing 68K→44K→11K→9.6K and
  price bleeding $3.80→$3.05 (~20% off the high); (3) book stale + very wide (bid $2.32 / ask
  $3.09 @20:00Z, ~33% spread). Fading spike on a thin, wide book. Watch only.
- **TWG** — AH +6.2% (below 10% bar), high float 44.5M, VRatio 0.6x. Regular-session mover.
  Watch only.
- **ANY** — AH bounced to +13.5% but SIP still SPIKE→FADE (peaked 16:25/16:30 ET then volume
  collapsed to 20–51K sh/bar; first-bar spike $2.95, CONFIRM-3 NO). Modest AH% bounce on thin
  volume is not a build. 0/10+ SPIKE→FADE pattern. Skip (carried).
- **ATER** — AH +5.2% (below 10% bar), VRatio 0.1x (AH vol far below 9.5M avg). Regular-session
  mover. Watch only.
- **EONR / OFAL** — AH +5.6% each (below 10% bar). Watch only.
- **ONCO** — Day −17.6%, Total −12.7% (below regular close = dead-cat). Skip.
- **LASE** — Day −32.1%, Total −28.6% (deep dead-cat bounce). Skip.
- **FGL** — **illiquid microfloat, skip (carried).** Float 60K, AH vol 135K, Total −5.9%
  (Day −18.6% dead-cat + bounce). Stale wide quote across all scans, bad-print / no fillable
  book. Skip.

**Notes:**
- **No new entries.** SUNE (only qualifying BUILD) held from 23:00, +0.3%. Two new >10% AH
  names both uninvestable: ZJYL untradable (broker-block, recorded for morning tally), ACCL
  SPIKE→FADE + first-AH-scan (2-AH-scan gate). All other hits below the 10% AH bar or
  dead-cat/illiquid.
- No FINAL-SCAN-GATE-BLOCK, CHASE-CAP, or DEAD-CAT/CEILING-OVERRIDE cases this scan.
- Next scan 00:30 CET (final scheduled scan). ACCL is the only new name worth a 2nd-scan
  cross-check — but it is fading; unlikely to qualify.

## Scan 00:30 CET (6:30 PM ET)

**Final scheduled scan.** Scanner: **12 hits.** SUNE held from 23:00 (position open,
+1.0%; no re-entry — one entry per candidate per night). No new entries — the only new
gate-crosser (ACCL) is a fading spike on a stale wide book. No qualifying BUILD.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| SUNE | [TV](https://www.tradingview.com/chart/?symbol=SUNE) | $2.37 | +0.4% | +26.2% | $2.99 | +26.7% | 10.4M | 1.5M | 7.1x | 5.4M | Engineering & Construction |
| TWG | [TV](https://www.tradingview.com/chart/?symbol=TWG) | $0.52 | +17.8% | +5.9% | $0.55 | +24.7% | 5.3M | 8.7M | 0.6x | 44.5M | Food Distributors |
| ANY | [TV](https://www.tradingview.com/chart/?symbol=ANY) | $2.45 | +5.6% | +11.4% | $2.73 | +17.7% | 1.6M | 479K | 3.4x | 6.5M | Information Technology Services |
| ZJYL | [TV](https://www.tradingview.com/chart/?symbol=ZJYL) | $2.02 | -2.9% | +14.4% | $2.31 | +11.1% | 674K | 120K | 5.6x | 64.7M | Medical Specialties |
| GLXG | [TV](https://www.tradingview.com/chart/?symbol=GLXG) | $1.02 | +8.4% | +7.8% | $1.10 | +16.9% | 613K | 98K | 6.2x | 1.7M | Miscellaneous Commercial Services |
| ISPC | [TV](https://www.tradingview.com/chart/?symbol=ISPC) | $1.59 | +3.2% | +6.9% | $1.70 | +10.4% | 365K | 2.2M | 0.2x | 2.5M | Miscellaneous Commercial Services |
| ONCO | [TV](https://www.tradingview.com/chart/?symbol=ONCO) | $0.84 | -17.6% | +6.0% | $0.89 | -12.7% | 255K | 893K | 0.3x | 3.9M | Pharmaceuticals: Major |
| LASE | [TV](https://www.tradingview.com/chart/?symbol=LASE) | $0.95 | -32.1% | +5.1% | $1.00 | -28.6% | 176K | 3.0M | 0.1x | 37.3M | Electronic Equipment/Instruments |
| SGLY | [TV](https://www.tradingview.com/chart/?symbol=SGLY) | $1.58 | +14.5% | +6.3% | $1.68 | +21.7% | 173K | 470K | 0.4x | 5.1M | Air Freight/Couriers |
| ACCL | [TV](https://www.tradingview.com/chart/?symbol=ACCL) | $2.67 | -2.6% | +13.1% | $3.02 | +10.2% | 164K | 30K | 5.5x | 4.9M | Miscellaneous Commercial Services |
| FGL | [TV](https://www.tradingview.com/chart/?symbol=FGL) | $7.57 | -18.6% | +9.2% | $8.27 | -11.1% | 152K | 215K | 0.7x | 60K | Engineering & Construction |
| RETO | [TV](https://www.tradingview.com/chart/?symbol=RETO) | $0.54 | -49.4% | +6.2% | $0.57 | -46.2% | 56K | 298K | 0.2x | 35.8M | Other Metals/Minerals |

**Spike-bar / CONFIRM-3 instrumentation (log-only, >10% AH names):**
- `SUNE  SPIKE 16:05ET +35% $3.19 942 trades / 248k sh (first co-spike bar)` — `CONFIRM-3 NO ignition 16:05ET failed third-bar hold/volume` — **FIRST-BAR-SPIKE**
- `ANY   SPIKE 16:06ET +20% $2.95 241 trades / 48k sh` — `CONFIRM-3 NO ignition 16:05ET failed third-bar hold/volume` — **FIRST-BAR-SPIKE**
- `ACCL  SPIKE 17:26ET +42% $3.80 144 trades / 9k sh (first co-spike bar)` — `CONFIRM-3 NO ignition 17:25ET failed third-bar hold/volume`

**Per-candidate evaluation:**
- **SUNE — held, no re-entry.** Already entered at 23:00 ($2.95, 33 sh, Grade C). AH +26.2%,
  still building/holding, VRatio 7.1x, position $2.98 (+1.0%). One entry per candidate per
  night — no averaging in. Premarket exit handled by position-evaluation.
- **ACCL — skip (SPIKE→FADE on a stale wide book).** Now cleared the 2-AH-scan gate mechanically
  (00:00 +10.5%, 00:30 +13.1%), but it is a fading spike, not a build: SIP ignition bar 88K sh /
  1,428 trades @17:25 ET spiking to H $3.80, then volume collapsing 68K→44K→11K→10K→9K→6K→2K and
  price bleeding $3.80→$3.00–3.18 (~17–20% off the high). Small 10K re-bump @18:10 ET, no fresh
  volume-backed new high. CONFIRM-3 NO. Book stale (quote stamped 20:00Z, ~30 min old) and very
  wide (bid $2.32 / ask $3.09, ~33% spread) — no clean fillable book. `tradable=true`, float 4.9M,
  Grade C (Acco Group Singapore corporate-services PR), Total +10.2% under ceiling — but
  SPIKE→FADE (0/10+ for PM continuation) plus a wide stale book. **Not a FINAL-SCAN-GATE-BLOCK**
  (that requires CONFIRM-3 YES on accumulating volume; ACCL is CONFIRM-3 NO and fading). Skip.
- **ZJYL — qualified-but-untradable broker-block, skip (carried).** `tradable=false` (recorded
  at 00:00) — no position possible. AH +14.4% real (VRatio 5.6x) but uninvestable; also float
  64.7M (>50M gate). Carried untradable, no workup re-run.
- **ANY — skip (SPIKE→FADE, carried).** AH +11.4% but SIP confirms fade: peaked 16:25/16:30 ET
  then volume collapsed to 20–51K sh/bar, price churning ~10% off the $2.98 high on thin volume.
  First-bar spike $2.95, CONFIRM-3 NO. 0/10+ SPIKE→FADE. Skip.
- **TWG** — AH +5.9% (below 10% bar), high float 44.5M, VRatio 0.6x. Regular-session mover. Watch.
- **GLXG / SGLY** — AH +7.8% / +6.3% (below 10% bar). Watch only.
- **ISPC** — AH +6.9% (below 10% bar), VRatio 0.2x. Watch only.
- **ONCO / LASE / RETO / FGL** — all dead-cat (Day −17.6% / −32.1% / −49.4% / −18.6%, Total below
  regular close). Skip. FGL also illiquid microfloat (60K, stale wide book), carried skip.

**Final-scan feed-lag cross-check:** SUNE is the strong, volume-backed name and is already the
scanner's top hit (VRatio 7.1x, SIP-confirmed). No tracked pipeline name (21:30 watch list BNC /
MOBX / INDP / NUR, or earlier AH names) is under-reported by the scan — none shows a real
SIP-backed >10% AH surge that the TradingView feed dropped. No rescue needed.

**Notes:**
- **No new entries.** SUNE (only qualifying BUILD) held from 23:00, +1.0%. The one new gate-crosser
  (ACCL) is a fading spike on a stale wide book — correctly skipped. ZJYL untradable (carried), ANY
  SPIKE→FADE (carried). All other hits below the 10% AH bar or dead-cat/illiquid.
- No FINAL-SCAN-GATE-BLOCK, CHASE-CAP, or DEAD-CAT/CEILING-OVERRIDE cases this scan.
- **Night summary:** one entry tonight — **SUNE $2.95, 33 sh, Grade C** (SUNation Energy financing
  agreement, heavy volume-backed BUILD/hold, fresh day-1 igniter). Grade C hold strategy: exit in
  premarket. Position-evaluation owns the exit.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
| SUNE | $2.95 | 23:00 CET (5:00 PM ET) | 33 | ca713441 | Grade C (SUNation Energy financing agreement). Cleared 2-AH-scan gate (3 scans >10%), VRatio 6.5x heavy SIP accumulation, Day% +0.4% pure AH ignition, Total +21.2% under ceiling, float 5.4M, fresh tight book. Fresh day-1 igniter. |
