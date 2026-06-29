# Post-Market Screening - 2026-06-29

## Scan 21:30 CET (3:30 PM ET) — REGULAR SESSION

Scan ran before AH opens (4:00 PM ET / 22:00 CET). **No paper trades** — regular-session caution rule. Candidates flagged as watch pending AH confirmation. Stocks that spike intraday but don't carry into AH tend to fade.

Top movers (regular-session, AH data not yet available):

| Ticker | Chart | Price | Chg% | IRVol | VChg% | Float | MCap | Industry | Note |
|--------|-------|-------|------|-------|-------|-------|------|----------|------|
| TVRD | [TV](https://www.tradingview.com/chart/?symbol=TVRD) | $1.86 | +24.0% | 58.8x | -14.8% | 6.1M | 17.4M | Biotechnology | Watch — low float, strong IRVol |
| AZI | [TV](https://www.tradingview.com/chart/?symbol=AZI) | $2.63 | +41.4% | 10.7x | -99.8% | 4.4M | 179.0M | Specialty Stores | Watch — vol fading |
| ZCMD | [TV](https://www.tradingview.com/chart/?symbol=ZCMD) | $1.32 | +38.5% | 10.3x | -20.7% | 101K | 3.0M | Misc Commercial Svcs | Watch — tiny float |
| KUST | [TV](https://www.tradingview.com/chart/?symbol=KUST) | $1.26 | +32.6% | 7.8x | -92.3% | 577K | 790K | Misc Commercial Svcs | Watch — tiny float, vol fading |
| CNET | [TV](https://www.tradingview.com/chart/?symbol=CNET) | $1.13 | +22.9% | 100.0x | -58.4% | 3.1M | 4.1M | Advertising/Marketing | Watch — low float |

Only enter if a candidate reappears in a subsequent AH scan (22:00+ CET) with sustained momentum.

## Scan 22:00 CET (4:00 PM ET)

First AH scan. `scan.py --all` returned 0 hits — none of the regular-session watch candidates (TVRD, AZI, ZCMD, KUST, CNET) carried into after-hours with qualifying momentum/volume. Observation-only window anyway (22:00/22:30 scans are no-entry during learning phase).

No candidates found.

## Scan 22:30 CET (4:30 PM ET)

Second AH scan. `scan.py --all` returned 4 hits. Observation-only window (22:00/22:30 scans are no-entry during learning phase — entries start at 23:00 CET / 5:00 PM ET).

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| GANX | [TV](https://www.tradingview.com/chart/?symbol=GANX) | $1.98 | +13.1% | +24.7% | $2.47 | +41.1% | 2.9M | 812K | 3.5x | 41.4M | Biotechnology |
| JEM | [TV](https://www.tradingview.com/chart/?symbol=JEM) | $1.08 | -41.9% | +57.4% | $1.70 | -8.6% | 2.1M | 827K | 2.6x | 0 | Wholesale Distributors |
| MNDR | [TV](https://www.tradingview.com/chart/?symbol=MNDR) | $3.57 | +11.2% | +5.9% | $3.78 | +17.8% | 104K | 378K | 0.3x | 1.8M | Medical/Nursing Services |
| TMCI | [TV](https://www.tradingview.com/chart/?symbol=TMCI) | $4.27 | -4.3% | +7.7% | $4.60 | +3.1% | 86K | 1.7M | 0.1x | 48.1M | Medical Specialties |

**Evaluation (observation-only — no entries before 23:00 CET):**

- **GANX** — LEAD CANDIDATE. Biotech, Day +13.1%, AH peak +40.6% ($2.46 at 16:10 ET), holding +33.7% at 16:30 (within ~20% of peak — BUILD/hold profile). Total% +41.1%, well under the +150% extension ceiling. VRatio 3.5x. **Catalyst (Grade B):** Gain Therapeutics presented *positive interim Phase 1b data* for GT-02287 (Parkinson's, GBA1) at the 3rd International GBA1 Meeting 2026 — clinical data catalyst confirmed via company press release. Float 41.4M (above ideal <10M but not a filter; tracked for pattern analysis). First AH-scan appearance (22:00 had 0 hits). Needs to reappear at 23:00 for the 2-AH-scan requirement → then qualifies for entry.
- **JEM** — Skip: dead-cat bounce. Day -41.9% (crashed during regular session), AH bounce to $1.70 still -8.6% *below* prior close. Stays below regular close → genuine dead-cat, not a reclaim. No override flag.
- **MNDR** — Skip: AH +5.9% (<10% threshold), VRatio 0.3x (volume below average, fading).
- **TMCI** — Skip: AH +7.7% (<10% threshold), VRatio 0.1x (negligible AH volume).

No paper trades this scan (pre-23:00 observation window). GANX carried as the entry candidate for the 23:00 scan pending second AH-scan confirmation.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
