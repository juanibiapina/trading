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

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
| — | — | — | — | — | No entries (regular-session watch scan, AH not open) |
