# Post-Market Screening - 2026-09-14

## Scan 21:30 CET (3:30 PM ET) — REGULAR SESSION (pre-AH watch)

This scan ran during the regular session (15:30 ET, 30 min before close), before after-hours opens at 16:00 ET / 22:00 CET. **No paper trades** per the regular-session caution rule. Candidates below are flagged watch-pending-AH; only names that reappear in AH scans (22:00+ CET) with sustained momentum become entry candidates.

Scanner returned 32 regular-session hits. Filtering out volume-collapse artifacts (`VChg% -99%` = 5m volume far below average, i.e. thin end-of-day prints, not building momentum) and stale/bad-print outliers (BURU +1825.7% on 100 shares — data artifact).

### Watch candidates (small float, live volume, Day% >15%)

| Ticker | Price | Day% | 5mVol | AvgVol | IRVol | Float | MCap | Industry | Note |
|--------|-------|------|-------|--------|-------|-------|------|----------|------|
| VANAF  | $0.75 | +29.3% | 10K | 7K | 11.7 | 5.6M | $12.6M | Financial Conglomerates | Live vol, small float |
| AIXC   | $1.16 | +28.8% | 13K | 36K | 12.9 | 7.1M | $24.4M | Packaged Software | Live vol |
| VSME   | $1.36 | +27.1% | 32K | 44K | 854.1 | 2.6M | $3.8M | Advertising/Marketing | Highest IRVol, tiny float |
| HMR    | $1.75 | +22.7% | 6K | 15K | 10.6 | 6.0M | $103.5M | Oil & Gas Pipelines | Small float |
| MYSE   | $3.10 | +16.3% | 2K | 7K | 4.1 | 4.9M | $15.9M | Packaged Software | Thin |
| PMI    | $6.14 | +15.2% | 200 | 1K | 0.7 | 1.4M | $14.4M | Medical Specialties | Very thin |

### Fading / artifact (excluded from watch)

- **BURU +1825.7%** — 100 shares in 5min, IRVol 0.0. Data artifact / reverse-split print, not a real move.
- **FTFT +187.5%, BMGL +61.4%, VNCE +45.6%, VEEA +34.6%, LHSW +31.9%** — all `VChg% -97% to -99.9%`: volume collapsed into the close. Spike-and-fade end-of-day prints, not building. Watch only if they reappear in AH with real accumulating volume.
- Financial Conglomerates cluster near $9.9–10.0 (IDAC, FWAC, WENC, MYX, TVIV) — flat/near-$10 SPAC-like names, no momentum move.

**Next scan: 22:00 CET (16:00 ET) — AH opens.** Re-check whether any watch name carries into after-hours with real SIP volume. Entries only begin at the 23:00 CET scan per learning-phase rules.

## Scan 22:00 CET (4:00 PM ET) — AH OPEN, observation only

Scanner returned **0 AH hits** — it ran at 16:00:21 ET, ~20 seconds after after-hours opened, before any AH volume had accumulated. Observation-only scan per learning-phase rules (no entries before the 23:00 CET scan).

**Watch-candidate AH book check (21:30 regular-session names):**

| Ticker | AH Quote (16:00 ET) | Read |
|--------|---------------------|------|
| VANAF  | no quote (404) | Not tradable on Alpaca — likely OTC/foreign line. Drop. |
| AIXC   | bid $0.95 x100 / ask $1.20 x500 | Wide spread, closing snapshot only, no AH prints yet |
| VSME   | bid $1.12 x100 / ask $0.00 x0 | No ask book — no fillable AH liquidity |
| HMR    | bid $1.49 x100 / ask $2.08 x100 | Very wide spread, closing snapshot, no AH prints |

No candidate shows a real accumulating AH book this early. Nothing to instrument (no name >10% AH change with live AH volume yet). Next scan 22:30 CET (4:30 PM ET) — re-check whether any 21:30 watch name carries into AH with real SIP volume; entries only begin at the 23:00 CET scan.

## Scan 22:15 CET (4:15 PM ET) — AH OPEN, observation only

Scanner returned **0 AH hits** (ran 16:15:17 ET). Still early in after-hours; scanner sees no name clearing the AH threshold. Observation-only per learning-phase rules (no entries before the 23:00 CET scan).

**Watch-candidate SIP + book check (tracked 21:30 names):** AH-start `2026-09-14T20:00:00Z` (EDT).

| Ticker | Close | AH 1st-bar (16:00 ET) | AH Chg | Quote (16:00 ET) | Read |
|--------|-------|-----------------------|--------|------------------|------|
| AIXC   | $1.16 | C $1.15, 16.3K sh, 85 tr | −0.9% | bid $0.95 x100 / ask $1.20 x500 | Flat, wide spread, no build |
| VSME   | $1.36 | C $1.33, 33.7K sh, 85 tr | −2.2% | bid $1.12 x100 / ask $0.00 x0 | No ask book — no fillable AH liquidity |
| HMR    | $1.75 | C $1.71, 4.8K sh, 24 tr | −2.3% | bid $1.49 x100 / ask $2.08 x100 | Thin, very wide spread |
| MYSE   | $3.10 | C $3.08, 2.9K sh, 4 tr | −0.6% | bid $2.63 x100 / ask $3.53 x100 | 4 trades — dead |
| PMI    | $6.14 | C $6.15, 4.9K sh, 22 tr | +0.2% | bid $5.36 x100 / ask $7.13 x100 | Thin, wide spread |

Every tracked name is flat-to-slightly-down vs its regular close on thin, single-bar volume — no candidate carried its regular-session move into after-hours with real accumulating SIP volume. No name >10% AH change, so no spike-bar / CONFIRM-3 instrumentation applies. **No entries** (also pre-23:00 CET). Next scan 22:30 CET (4:30 PM ET) — re-check whether any name ignites in AH with real SIP volume; entries begin at the 23:00 CET scan.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
