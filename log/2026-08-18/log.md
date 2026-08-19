
# Post-Market Screening - 2026-08-18

## Scan 21:30 CET (3:30 PM ET) — regular session, watch only

Regular session (AH opens 16:00 ET / 22:00 CET). No paper trades per regular-session caution rule. Candidates flagged "Watch — pending AH confirmation"; enter only if they reappear in a 22:00+ CET AH scan with sustained momentum.

| Ticker | Price | Day% | 5mVol | AvgVol | IRVol | Float | MCap | Industry | Note |
|--------|-------|------|-------|--------|-------|-------|------|----------|------|
| XOS | $4.37 | +109.1% | 163K | 180K | 150.3 | 6.9M | 29.7M | Motor Vehicles | Watch — sold this AM at loss; USAF-contract name back running |
| CAST | $2.13 | +147.7% | 1.5M | 1.9M | 122.7 | 19.7M | 40.9M | Internet Software/Svcs | Watch — float >10M |
| CDTG | $5.36 | +91.5% | 534K | 657K | 31.1 | 3.0M | 8.5M | Industrial Machinery | Watch — low float |
| AIXC | $1.34 | +88.2% | 170K | 312K | 2263.4 | 6.8M | 27.0M | Packaged Software | Watch — huge IRVol, volume fading (VChg -62%) |
| SLE | $5.24 | +73.5% | 146K | 82K | 31.1 | 1.6M | 8.9M | Internet Software/Svcs | Watch — low float, VChg +140% |
| SXTC | $5.43 | +44.7% | 158 | 20K | 6.0 | 1.3M | 7.2M | Pharma Major | Watch — volume near-dead (VChg -99.6%) |
| EJH | $2.08 | +43.5% | 11K | 38K | 470.6 | 2.5M | 6.7M | Consumer Services | Watch — low float |

The $10 flat Financial Conglomerates (ACGC, SHOT, MUZE, VII) show extreme IRVol at ~0% change — SPAC/auction artifacts, not momentum. Skipped.

## Scan 22:00 CET (4:00 PM ET) — AH open, observation only

`scan.py --all`: **0 hits.** AH session just opened (16:00 ET exact); postmarket volume not yet accumulated. No candidates from whole-market screen.

21:30 regular-session watch names have not reappeared in an AH scan yet — none crossed into the AH screen at open. Nothing to confirm this scan. Observation-only window regardless (learning phase: no entries before 23:00 CET). Re-check watch names (XOS, CAST, CDTG, AIXC, SLE, EJH) at 22:30/23:00 for AH carry-over.

No paper trades.

## Scan 22:15 CET (4:15 PM ET) — AH open, observation only

`scan.py --all`: **0 hits.** First AH 5-min bar (16:00–16:05 ET) just closed; whole-market screen still shows no candidates above threshold.

SIP cross-check of 21:30 regular-session watch names (first AH bar):

| Ticker | Reg Close | AH C (16:05 ET) | AH move | Vol/bar | Trades | Read |
|--------|-----------|-----------------|---------|---------|--------|------|
| XOS | $4.37 | $4.30 | ~flat | 303K | 1527 | flat, no AH build |
| CAST | $2.13 | $2.15 | ~flat | 1.0M | 4437 | flat |
| CDTG | $5.36 | $3.10 | −42% | 222K | 1386 | collapsing in AH |
| SLE | $5.24 | $4.94 | −6% | 1.0M | 9245 | fading off close |

No watch name is building into AH — all flat or fading on the first bar. Nothing to confirm. Observation-only window regardless (learning phase: no entries before 23:00 CET). Re-check at 22:30/23:00 for any name that starts building.

No paper trades.

## Scan 22:30 CET (4:30 PM ET) — AH open, observation only

`scan.py --all`: **2 hits.** First AH movers to cross the whole-market screen tonight.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| TNON | [TV](https://www.tradingview.com/chart/?symbol=TNON) | $5.45 | +10.8% | +56.5% | $8.53 | +73.4% | 1.6M | 350K | 4.6x | 551K | Medical/Nursing Services |
| CNET | [TV](https://www.tradingview.com/chart/?symbol=CNET) | $1.38 | +5.3% | +16.1% | $1.60 | +22.3% | 754K | 107K | 7.1x | 3.0M | Advertising/Marketing Services |

**Instrumentation (log-only, no decision impact):**
- TNON: `SPIKE 16:01ET +28% $7.00 1787 trades / 137k sh` · `CONFIRM-3 NO no local-volume new-high ignition as-of 16:30ET`
- CNET: `NO-SPIKE peak +33% @16:09ET (no bar cleared +15% on volume co-spike)` · `CONFIRM-3 NO`

**SIP 5-min bars (real AH volume):**

| Ticker | Bar C path (16:00→16:15 ET) | Vol/bar | Trades/bar | Read |
|--------|-----------------------------|---------|------------|------|
| TNON | $7.03 → $7.60 → $8.51 → $8.58 | 595K–880K | 9.7k–15.8k | genuine BUILD, real accumulation |
| CNET | $1.67 → $1.60 → $1.38 | 526K→248K | 4.1k→1.8k | SPIKE→FADE, volume fading |

**Evaluation (observation-only, no entries before 23:00 CET):**
- **TNON** — tiny 551K float, Total% +73.4% (under +150% ceiling), SIP confirms real accumulating AH volume and a clean BUILD ($7.03→$8.58). Strong watch. But this is its **first** AH scan appearance (0 hits at 22:00/22:15) — the 2-AH-scan gate is not met. Needs to reappear >10% AH at 23:00 to qualify. No catalyst search yet (defer to 23:00 if it holds).
- **CNET** — SIP shows SPIKE→FADE (peaked $1.84 16:05 ET, now $1.38, volume halving each bar). Fails BUILD/hold. Watch only; likely skip.

No paper trades (learning-phase observation window, both fail 2-AH-scan gate).

## Scan 22:45 CET (4:45 PM ET) — AH open, observation only

`scan.py --all`: **4 hits.** TNON reappears (2nd AH scan) and keeps building; MSS new.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| TNON | [TV](https://www.tradingview.com/chart/?symbol=TNON) | $5.45 | +10.8% | +72.7% | $9.41 | +91.3% | 3.7M | 640K | 5.7x | 551K | Medical/Nursing Services |
| MSS | [TV](https://www.tradingview.com/chart/?symbol=MSS) | $1.57 | +7.5% | +15.3% | $1.81 | +24.0% | 2.0M | 500K | 4.0x | 551K | Food Retail |
| QTRX | [TV](https://www.tradingview.com/chart/?symbol=QTRX) | $2.68 | -8.2% | +7.5% | $2.88 | -1.3% | 81K | 1.3M | 0.1x | 41.8M | Medical Specialties |
| BRNX | [TV](https://www.tradingview.com/chart/?symbol=BRNX) | $2.65 | -13.1% | +16.2% | $3.08 | +1.0% | 65K | 783K | 0.1x | 684K | Engineering & Construction |

**Instrumentation (log-only, no decision impact):**
- TNON: `SPIKE 16:01ET +28% $7.00 1787 trades / 137k sh` · `CONFIRM-3 NO no local-volume new-high ignition as-of 16:45ET`
- MSS: `SPIKE 16:01ET +20% $1.89 474 trades / 84k sh` · `CONFIRM-3 NO`
- BRNX: `SPIKE 16:25ET +20% $3.18 94 trades / 7k sh` · `CONFIRM-3 PENDING (ignition 16:25ET, waiting third bar)`

**SIP 5-min bars (real AH volume):**

| Ticker | Bar C path (16:00→16:30 ET) | Vol/bar | Trades/bar | Read |
|--------|------------------------------|---------|------------|------|
| TNON | $7.03→$7.60→$8.51→$8.58→$9.25→$9.41→$9.67 | 595K–1.08M | 9.7k–16.7k | genuine BUILD, strong accumulation, new highs |
| MSS | $1.82→$1.58→$1.57→$1.81→$1.80→$1.81→$1.95 | 116K–638K | 431–3.4k | choppy BUILD/hold, real volume, new high $1.95 |
| BRNX | $2.65→$2.89→$2.88→$2.96→$2.89 | 0.7K–84K | 1–905 | thin, Day −13% dead-cat, near-flat Total% |
| QTRX | $2.68→$2.88→$2.70 | 1K–80K | 1–6 | near-zero AH trades, stale VRatio |

**Evaluation (observation-only, no entries before 23:00 CET):**
- **TNON** — now clears the **2-AH-scan gate** (22:30 +73.4%, 22:45 +91.3%). Tiny 551K float, Total% +91.3% under +150% ceiling, SIP confirms clean BUILD with heavy accumulating volume ($7.03→$9.67, 600K–1M sh/bar). Strongest candidate of the night. Peaked/building past 16:30 ET. **Primary entry target at 23:00** — run catalyst search then and verify live book.
- **MSS** — real AH volume and a choppy hold/BUILD (new high $1.95), 551K float. **First AH scan appearance** — 2-AH-scan gate not met. Needs to reappear >10% AH at 23:00 to qualify.
- **QTRX** — VRatio 0.1x, 1–6 trades/bar, no real AH liquidity. Skip (stale VRatio).
- **BRNX** — Day% −13.1% dead-cat, thin book (mostly <2k sh/bar), Total% +1.0%. Skip (thin/dead-cat).
- CNET (22:30 candidate) dropped out — SPIKE→FADE confirmed, no longer above threshold.

No paper trades (learning-phase observation window; entries begin at 23:00 CET / 5:00 PM ET).

## Scan 23:00 CET (5:00 PM ET) — AH open, ENTRIES LIVE

`scan.py --all`: **5 hits.** TNON (3rd AH scan) and MSS (2nd AH scan) both clear the 2-AH-scan gate. First entry-eligible scan of the night.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| CAST | [TV](https://www.tradingview.com/chart/?symbol=CAST) | $2.10 | +144.2% | +18.1% | $2.48 | +188.4% | 6.9M | 14.6M | 0.5x | 19.7M | Internet Software/Services |
| TNON | [TV](https://www.tradingview.com/chart/?symbol=TNON) | $5.45 | +10.8% | +59.6% | $8.70 | +76.8% | 4.7M | 792K | 6.0x | 551K | Medical/Nursing Services |
| MSS | [TV](https://www.tradingview.com/chart/?symbol=MSS) | $1.57 | +7.5% | +22.8% | $1.93 | +32.1% | 3.9M | 725K | 5.4x | 551K | Food Retail |
| BRNX | [TV](https://www.tradingview.com/chart/?symbol=BRNX) | $2.65 | -13.1% | +5.9% | $2.81 | -8.0% | 124K | 789K | 0.2x | 684K | Engineering & Construction |
| CRE | [TV](https://www.tradingview.com/chart/?symbol=CRE) | $2.50 | -10.1% | +6.8% | $2.67 | -4.0% | 112K | 38K | 2.9x | 1.1M | Commercial Printing/Forms |

**Instrumentation (log-only, no decision impact):**
- TNON: `SPIKE 16:01ET +28% $7.00 1787 trades / 137k sh` · `CONFIRM-3 NO no local-volume new-high ignition as-of 17:00ET`
- MSS: `SPIKE 16:01ET +20% $1.89 474 trades / 84k sh` · `CONFIRM-3 NO no local-volume new-high ignition as-of 17:00ET`

**SIP 5-min bars (real AH volume, last bar 16:45 ET):**

| Ticker | Bar C path (16:00→16:45 ET) | Vol/bar | Trades/bar | Read |
|--------|------------------------------|---------|------------|------|
| TNON | $7.03→$7.60→$8.51→$8.58→$9.25→$9.41→$9.67→$8.85→$8.70→$8.94 | 368K–1.08M | 6.1k–16.7k | genuine BUILD to $9.67 peak (16:30 ET), mild pullback, holding ~$8.94 (within ~12% of high) |
| MSS | $1.82→$1.58→$1.57→$1.81→$1.80→$1.81→$1.95→$1.91→$1.91→$1.87 | 116K–1.34M | 431–10.3k | choppy BUILD/hold, new high $2.07 (16:35 ET, 1.3M sh bar), holding ~$1.87 |

**Catalyst search:**
- **TNON** — earnings were Aug 13 (5 days ago, EPS -$12.35 miss); no press release or 8-K for today's Aug 18 AH spike found (2 searches). **No fresh catalyst** → enter with concern noted (learning-phase policy).
- **MSS** — no confirmed same-day catalyst. Found Q2/6-month results PR + "Worldcoin treasury initiative" narrative (date unconfirmed) and an analyst PT cut 4.5→3.25 (7/31). **No confirmed catalyst** → enter with concern noted; flag treasury angle for PM eval.

**Evaluation & decisions:**
- **TNON — ENTER.** 2-AH-scan gate met (22:30 +73.4%, 22:45 +91.3%). Ultra-low float 551K (ideal). Total% +76.8% under +150% ceiling. Day% +10.8% (>-15%). SIP confirms real accumulating BUILD; peak 16:30 ET is before 18:30 but the name is *holding within ~12% of its AH high*, not fading (CHAI/MSW precedent). No fresh catalyst = concern noted. **Alpaca quote stale** (`bid $4.55 / ask $0.00 x0 @ 16:00:03 ET`, not updating vs 17:00 scan) — freshness guard: SIP is fresh and shows a real 500K–1M sh/bar book, so this is a staleness artifact, NOT an illiquid/bad-print skip. Order filled, confirming a real book existed.
- **MSS — ENTER.** 2-AH-scan gate met (22:45 +15.3% AH, 23:00 +22.8% AH). Ultra-low float 551K. Total% +32.1% under ceiling. Day% +7.5%. SIP confirms real BUILD/hold (new high $2.07, 1.3M sh peak bar), holding ~$1.87. No confirmed catalyst = concern noted.
- **CAST — SKIP.** Only NOW shows >10% AH (first AH scan; flat ~$2.15 at 22:00/22:15) → fails 2-AH-scan gate. Also Total% +188.4% exceeds +150% extension ceiling, and VRatio 0.5x (AH Vol 6.9M < AvgVol 14.6M) shows no unusual AH accumulation. Float 19.7M > 10M ideal. Multiple skips.
- **BRNX — SKIP (carried).** Day% -13.1% dead-cat, thin (VRatio 0.2x), Total% -8.0%.
- **CRE — SKIP.** AH Chg +6.8% below the 10% threshold; Day% -10.1%, Total% -4.0%.

**Chase-cap instrumentation:**
- TNON: qualifying scan (22:45) $9.41 / +91.3%; fill $8.69 / +59.4%; chase gap -31.9pts — filled **below** qualifying price, no chase into fade zone.
- MSS: qualifying scan (23:00) $1.93 / +32.1%; fill $1.90 / +21.0%; filled below qualifying, no chase.

**Order execution notes:**
- TNON: `buy 11 @ limit $9.20 --ext` → filled @ **$8.69** (id ca88a01e). QTY = floor(100/8.94)=11.
- MSS: first `buy 55 @ limit $1.85 --ext` rested unfilled ~25s against a displayed $1.81 ask (thin/stale book); cancelled, re-submitted `buy 55 @ limit $1.92 --ext` → filled @ **$1.90** (id 649ac871). Old order cancelled cleanly, no double position (verified `positions`).

## Scan 23:30 CET (5:30 PM ET) — AH open, ENTRIES LIVE

`scan.py --all`: **8 hits.** TNON + MSS already held (no re-entry per one-entry-per-candidate rule). HKIT and EJH new to AH screen; CAST 2nd AH appearance.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| CAST | [TV](https://www.tradingview.com/chart/?symbol=CAST) | $2.10 | +144.2% | +14.3% | $2.40 | +179.1% | 11.8M | 15.1M | 0.8x | 19.7M | Internet Software/Services |
| TNON | [TV](https://www.tradingview.com/chart/?symbol=TNON) | $5.45 | +10.8% | +78.2% | $9.71 | +97.4% | 6.0M | 962K | 6.2x | 551K | Medical/Nursing Services |
| MSS | [TV](https://www.tradingview.com/chart/?symbol=MSS) | $1.57 | +7.5% | +15.3% | $1.81 | +24.0% | 4.8M | 826K | 5.8x | 551K | Food Retail |
| HKIT | [TV](https://www.tradingview.com/chart/?symbol=HKIT) | $3.05 | +0.7% | +23.0% | $3.75 | +23.8% | 855K | 279K | 3.1x | 729K | Packaged Software |
| WFF | [TV](https://www.tradingview.com/chart/?symbol=WFF) | $2.22 | +9.9% | +9.2% | $2.42 | +20.0% | 357K | 15.0M | 0.0x | 13.3M | Textiles |
| EJH | [TV](https://www.tradingview.com/chart/?symbol=EJH) | $2.06 | +42.1% | +10.2% | $2.27 | +56.6% | 180K | 2.1M | 0.1x | 2.5M | Other Consumer Services |
| BRNX | [TV](https://www.tradingview.com/chart/?symbol=BRNX) | $2.65 | -13.1% | +11.3% | $2.95 | -3.3% | 131K | 790K | 0.2x | 684K | Engineering & Construction |
| ATOM | [TV](https://www.tradingview.com/chart/?symbol=ATOM) | $4.92 | -9.2% | +5.7% | $5.20 | -4.1% | 57K | 514K | 0.1x | 36.8M | Misc Commercial Services |

**Instrumentation (log-only, no decision impact):**
- TNON: `SPIKE 16:01ET +28% $7.00 1787 trades / 137k sh` · `CONFIRM-3 NO no local-volume new-high ignition as-of 17:30ET`
- MSS: `SPIKE 16:01ET +20% $1.89 474 trades / 84k sh` · `CONFIRM-3 NO no local-volume new-high ignition as-of 17:30ET`
- HKIT: `SPIKE 16:49ET +23% $3.74 85 trades / 8k sh` · `CONFIRM-3 NO ignition 16:45ET failed third-bar hold/volume as-of 17:30ET`
- CAST: `SPIKE 16:39ET +19% $2.49 2949 trades / 577k sh` · `CONFIRM-3 NO ignition 16:35ET failed third-bar hold/volume as-of 17:30ET`
- EJH: `NO-SPIKE peak +12% @17:10ET (no bar cleared +15% on a volume co-spike)` · `CONFIRM-3 NO`

**HKIT SIP 5-min bars (real AH volume, last bar 17:15 ET):**

| Bar C path (16:45→17:15 ET) | Vol/bar | Trades/bar | Read |
|-----------------------------|---------|------------|------|
| $3.74→$3.75→$3.25→$2.74→$4.00→$3.78→$3.21 | 15K–449K | 102–6.4k | real accumulating volume but whippy; peak $4.64 (17:10 ET), now $3.21 ≈31% off high = fade, not hold |

**Evaluation & decisions (entries live, but no new qualifier):**
- **TNON — HELD (no re-entry).** Position open from 23:00 ($8.69, 11 sh), now $8.80 (+1.3%). Still building (AH +78.2%). One entry per candidate per night.
- **MSS — HELD (no re-entry).** Position open from 23:00 ($1.90, 55 sh), now $1.72 (-9.5%). Fading; position management handled premarket.
- **HKIT — SKIP (watch).** First AH-scan appearance (flat/absent 22:00–23:00) → fails 2-AH-scan gate. SIP shows real volume but a whippy, non-BUILD path now ~31% off the $4.64 high (fade > 20% off high, not a CHAI-style hold). Live quote `ask $0.00 x0` = no fillable AH book right now. Re-check at 00:00 only if it rebuilds toward highs.
- **CAST — SKIP.** 2nd AH appearance but Total% +179.1% exceeds +150% ceiling; VRatio 0.8x (AH Vol < AvgVol) = no unusual AH accumulation; float 19.7M > 10M; CONFIRM-3 NO / SPIKE→FADE. Ceiling-override watch not triggered (needs VRatio >5x — fails). Multiple skips.
- **EJH — SKIP.** NO-SPIKE, VRatio 0.1x (180K AH vol vs 2.1M avg) = thin, first AH-scan appearance. Regular-session watch appearance doesn't count toward the gate.
- **WFF — SKIP.** AH +9.2% below the 10% threshold; VRatio 0.0x; float 13.3M.
- **ATOM — SKIP.** AH +5.7% below threshold; Day% -9.2%; float 36.8M.
- **BRNX — SKIP (carried).** Day% -13.1% dead-cat, VRatio 0.2x thin, Total% -3.3%.

No new paper trades this scan. Two positions carried (TNON, MSS).

## Scan 00:00 CET (6:00 PM ET) — AH open, ENTRIES LIVE

`scan.py --all`: **8 hits.** TNON + MSS already held (no re-entry). TGL new and strong; KIDZ new; CAST/EJH/BRNX/CRE carried skips.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| CAST | [TV](https://www.tradingview.com/chart/?symbol=CAST) | $2.10 | +144.2% | +17.6% | $2.47 | +187.3% | 13.3M | 15.3M | 0.9x | 19.7M | Internet Software/Services |
| TNON | [TV](https://www.tradingview.com/chart/?symbol=TNON) | $5.45 | +10.8% | +61.1% | $8.78 | +78.5% | 6.6M | 1.1M | 6.2x | 551K | Medical/Nursing Services |
| MSS | [TV](https://www.tradingview.com/chart/?symbol=MSS) | $1.57 | +7.5% | +9.6% | $1.72 | +17.8% | 5.2M | 872K | 6.0x | 551K | Food Retail |
| TGL | [TV](https://www.tradingview.com/chart/?symbol=TGL) | $2.67 | -6.3% | +55.8% | $4.16 | +46.0% | 1.9M | 285K | 6.7x | 1.8M | Miscellaneous Commercial Services |
| EJH | [TV](https://www.tradingview.com/chart/?symbol=EJH) | $2.06 | +42.1% | +6.8% | $2.20 | +51.7% | 230K | 2.1M | 0.1x | 2.5M | Other Consumer Services |
| BRNX | [TV](https://www.tradingview.com/chart/?symbol=BRNX) | $2.65 | -13.1% | +9.4% | $2.90 | -4.9% | 151K | 793K | 0.2x | 684K | Engineering & Construction |
| KIDZ | [TV](https://www.tradingview.com/chart/?symbol=KIDZ) | $4.72 | +16.0% | +10.8% | $5.23 | +28.5% | 139K | 223K | 0.6x | 859K | Internet Software/Services |
| CRE | [TV](https://www.tradingview.com/chart/?symbol=CRE) | $2.50 | -10.1% | +5.2% | $2.63 | -5.4% | 122K | 39K | 3.1x | 1.1M | Commercial Printing/Forms |

**Instrumentation (log-only, no decision impact):**
- TGL: `SPIKE 17:21ET +18% $3.15 34 trades / 13k sh` · `CONFIRM-3 NO no local-volume new-high ignition as-of 18:00ET`
- KIDZ: `NO-SPIKE peak +14% @17:32ET (no bar cleared +15% on a volume co-spike)` · `CONFIRM-3 NO`

**TGL SIP 5-min bars (real AH volume, last bar 17:45 ET):**

| Bar C path (17:20→17:45 ET) | Vol/bar | Trades/bar | Read |
|-----------------------------|---------|------------|------|
| $3.48→$3.84→$3.79→$3.76→$4.16→$4.08 | 313K–658K | 3.9k–8.8k | genuine BUILD, heavy accumulation, late ignition 17:20 ET; peak $4.33 (17:45 ET), holding $4.08 ≈6% off high |

**Catalyst search:**
- **TGL** (Treasure Global, SE Asia fintech/digital-asset) — no same-day Aug 18 press release or 8-K found (2 searches); only older 2026 revenue-outlook hype PRs. **No confirmed catalyst.**

**Evaluation & decisions:**
- **TNON — HELD (no re-entry).** Position open from 23:00 ($8.69, 11 sh), now $8.80 (+1.3%). Still building (AH +61.1%). One entry per candidate per night.
- **MSS — HELD (no re-entry).** Position open from 23:00 ($1.90, 55 sh), now $1.72/$1.75 (-7.9%). AH faded to +9.6%; position management handled premarket.
- **TGL — SKIP (strong watch).** **First AH-scan appearance tonight** (absent 22:00–23:30) → fails the 2-AH-scan gate; cannot enter this scan. Otherwise strong: 1.8M float, VRatio 6.7x, Total% +46.0% under ceiling, Day% -6.3% (not dead-cat), SIP confirms genuine BUILD with heavy accumulation (300K–658K sh/bar, ignition 17:20 ET = late peak, holding within ~6% of $4.33 high). No confirmed catalyst. `tradable=true`; quote `ask $0.00 x0 @ 16:00 ET` is stale (SIP fresh to 17:45 ET) — staleness artifact, not a bad-print skip. **Primary watch for the 00:30 final scan** — if it reappears >10% AH it clears the 2-scan gate and, past 00:00 CET, becomes entry-eligible.
- **KIDZ — SKIP.** VRatio 0.6x (139K AH vol < 223K avg = no unusual accumulation), NO-SPIKE, first AH-scan appearance. Thin.
- **CAST — SKIP.** Total% +187.3% exceeds +150% ceiling; VRatio 0.9x (AH Vol < AvgVol) = no accumulation; float 19.7M. Ceiling-override watch fails (needs VRatio >5x).
- **EJH — SKIP.** AH +6.8% below the 10% threshold; VRatio 0.1x thin.
- **BRNX — SKIP (carried).** Day% -13.1% dead-cat, VRatio 0.2x thin, Total% -4.9%.
- **CRE — SKIP.** AH +5.2% below threshold; Day% -10.1%.

No new paper trades this scan. Two positions carried (TNON, MSS). TGL is the watch for 00:30.

## Scan 00:30 CET (6:30 PM ET) — AH open, ENTRIES LIVE (final scan)

`scan.py --all`: **8 hits.** Final scheduled scan. TNON + MSS already held (no re-entry). TGL reappears (2nd AH scan) so it clears the 2-AH-scan gate, but has faded off its peak. No new qualifier.

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| CAST | [TV](https://www.tradingview.com/chart/?symbol=CAST) | $2.10 | +144.2% | +23.8% | $2.60 | +202.4% | 16.3M | 15.7M | 1.0x | 19.7M | Internet Software/Services |
| TNON | [TV](https://www.tradingview.com/chart/?symbol=TNON) | $5.45 | +10.8% | +65.1% | $9.00 | +82.9% | 6.9M | 1.1M | 6.2x | 551K | Medical/Nursing Services |
| MSS | [TV](https://www.tradingview.com/chart/?symbol=MSS) | $1.57 | +7.5% | +19.1% | $1.87 | +28.1% | 5.5M | 902K | 6.1x | 551K | Food Retail |
| TGL | [TV](https://www.tradingview.com/chart/?symbol=TGL) | $2.67 | -6.3% | +25.8% | $3.36 | +17.9% | 3.3M | 468K | 7.0x | 1.8M | Miscellaneous Commercial Services |
| XOS | [TV](https://www.tradingview.com/chart/?symbol=XOS) | $4.44 | +112.4% | +5.6% | $4.69 | +124.4% | 3.0M | 14.1M | 0.2x | 6.9M | Motor Vehicles |
| KIDZ | [TV](https://www.tradingview.com/chart/?symbol=KIDZ) | $4.72 | +16.0% | +5.9% | $5.00 | +22.9% | 444K | 268K | 1.7x | 859K | Internet Software/Services |
| EJH | [TV](https://www.tradingview.com/chart/?symbol=EJH) | $2.06 | +42.1% | +5.8% | $2.18 | +50.3% | 277K | 2.1M | 0.1x | 2.5M | Other Consumer Services |
| BRNX | [TV](https://www.tradingview.com/chart/?symbol=BRNX) | $2.65 | -13.1% | +8.3% | $2.87 | -5.9% | 159K | 794K | 0.2x | 684K | Engineering & Construction |

**Instrumentation (log-only, no decision impact):**
- TGL: `SPIKE 17:21ET +18% $3.15 34 trades / 13k sh` · `CONFIRM-3 NO no local-volume new-high ignition as-of 18:30ET`
- TNON: `SPIKE 16:01ET +28% $7.00 1787 trades / 137k sh`
- MSS: `SPIKE 16:01ET +20% $1.89 474 trades / 84k sh`

**TGL SIP 5-min bars (real AH volume, last bar 18:15 ET):**

| Bar C path (17:20→18:15 ET) | Vol/bar | Trades/bar | Read |
|-----------------------------|---------|------------|------|
| $3.48→$3.84→$3.79→$3.76→$4.16→$4.08→$3.79→$3.60→$3.38→$3.47→$3.37→$3.40 | 76K–658K | 927–8.8k | peaked $4.33 (17:45 ET), now $3.40 ≈21% off high; volume collapsing 604K→76K/bar = SPIKE→FADE |

**Final-scan feed-lag cross-check (pipeline names vs SIP):**
- TNON — SIP holding $8.95 (17:35 ET), no under-report. Held.
- MSS — SIP holding $1.74–1.80 (17:35 ET), no under-report. Held.
- HKIT — SIP dead ($3.00, 29–31 trades/bar, 1.7K–3.4K sh), confirmed fade. No rescue.
- No tracked name is under-reported by TradingView while SIP shows a real volume-backed surge above threshold. No feed-lag rescue triggered.

**Evaluation & decisions (final scan):**
- **TNON — HELD (no re-entry).** Position from 23:00 ($8.69, 11 sh). SIP holding ~$8.95 (still building, AH +65.1%). Broker mark $8.17 (-6.0%) reflects a stale/wide AH quote; SIP is the truth. One entry per candidate per night.
- **MSS — HELD (no re-entry).** Position from 23:00 ($1.90, 55 sh). SIP holding ~$1.74–1.80. Broker mark $1.88 (-1.1%). One entry per candidate per night.
- **TGL — SKIP.** Clears the 2-AH-scan gate now (00:00 +46.0%, 00:30 +17.9%) and past 00:00 CET, but it has **faded**: peaked $4.33 (17:45 ET), now $3.40 ≈21% off high with volume collapsing (604K→76K/bar, 7003→927 trades). Fails the "holding within ~20% of high" rule; SPIKE→FADE off peak for 45 min. CONFIRM-3 NO. Not a hold — skip.
- **CAST — SKIP.** Total% +202.4% exceeds +150% ceiling; VRatio 1.0x (AH Vol ≈ AvgVol) = no unusual accumulation; float 19.7M. Ceiling-override watch fails (needs VRatio >5x).
- **XOS — SKIP.** AH Chg +5.6% below the 10% threshold; VRatio 0.2x; already ran intraday (Day +112%) and was sold this AM. No fresh AH build.
- **KIDZ — SKIP.** AH +5.9% below threshold; VRatio 1.7x thin.
- **EJH — SKIP.** AH +5.8% below threshold; VRatio 0.1x thin.
- **BRNX — SKIP (carried).** Day% -13.1% dead-cat, VRatio 0.2x thin, Total% -5.9%.

No new paper trades. Night ends with two positions carried (TNON, MSS). No SPIKE→FADE-only "least bad" entry forced; TGL correctly skipped as a faded spike.

**Night summary for morning eval:** TNON + MSS entered at 23:00 (both 551K float, real AH BUILD, no confirmed catalyst = Grade None). Both held near their AH highs on SIP through the final scan. TGL was the strongest late candidate (1.8M float, VRatio 7.0x, genuine BUILD with heavy accumulation) but peaked 17:45 ET and faded before it cleared the 2-scan gate at an entry-eligible time — a timing miss (gate met only as it started fading). No catalyst confirmed on any candidate tonight.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
| TNON | $8.69 | 23:00 CET | 11 | ca88a01e | 551K float, 2-AH-scan gate, AH BUILD to $9.67 holding, Total +59.4%, no fresh catalyst (Grade None) |
| MSS | $1.90 | 23:00 CET | 55 | 649ac871 | 551K float, 2-AH-scan gate, AH BUILD to $2.07 holding, Total +21.0%, no confirmed catalyst (Grade None) |

## Position Evaluation — 10:30 CET

| Ticker | Entry | Exit/Now | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|----------|-------|------|------|-------|----------|--------|
| DARE | $1.70 | $0.83 | -51.2% | $1.79 | 5 | B | SELL | Day-5 past 2-day limit + far below -15% stop; Juan flagged 08-14 |
| GRSD | $2.17 | $2.01 | -7.4% | $2.35 | 5 | B | SELL | Day-5 time limit; dead book, never re-rated |
| ONFO | $3.02 | $2.26 | -25.2% | $3.88 | 4 | B | SELL | Day-4 past limit + below -15% stop ($2.567) |
| SGLY | $7.01 | $5.35 | -23.7% | $7.25 | 0 | None | SELL | Exit first PM + below -10% stop ($6.31); dumped at open |
| XOS | $4.54 | $3.48 | -23.3% | $4.78 | 1 | B | SELL | Below -15% hard stop ($3.86); dumped at PM open |

**Actions taken:**
- Sold all 5 positions (extended-hours limit, all price-improved over limit).
- DARE 58 @ $0.83 (id 6d0996dc) — realized -$50.46
- GRSD 45 @ $2.01 (id 207f9758) — realized -$7.20
- ONFO 29 @ $2.26 (id 97313753) — realized -$22.04
- SGLY 14 @ $5.35 (id 4b1bca32) — realized -$23.24
- XOS 21 @ $3.48 (id 6e310b97) — realized -$22.26
- **Total realized: -$124.94.** Account flat, no open positions.

**Notes / for daily email:**
- Rough pulse: 5/5 losers. Two Grade B names (DARE, GRSD) were held well past the 2-day time limit — DARE bled from -7% to -51% while stalled. Time-limit exits must fire on schedule, not wait for a crash.
- XOS had a genuine catalyst (USAF contract) + real AH BUILD to +117% yet still gave zero PM follow-through and dumped at open. Reinforces: AH BUILD alone (even with catalyst) does not predict PM continuation.

## Position Evaluation — 14:30 CET

No open positions (Alpaca source of truth confirms flat). All 5 positions closed at the 10:30 CET pulse. OPEN_POSITIONS.md agrees. No action.

## Morning Evaluation — 10:20 CET (Pulse 1)

### Today's Winner

**TNON** — Tenon Medical (medical devices / spinal implants)
- Catalyst: **None confirmed** (Grade None). Benzinga lists it only as an after-market mover (+70.3%); Q2 earnings were Aug 13 (EPS miss), no fresh Aug 18 PR/8-K found. Ultra-low-float squeeze.
- Previous Close: $4.92 (Aug 15; ran +10.8% during Aug 18 regular to $5.45)
- AH last night: SIP high **$10.10 (+105.3% from $4.92)** at 16:30 ET, on 595K–1.08M sh/bar and 9.7K–16.7K trades/bar — heavy real accumulation, clean BUILD
- Premarket now: SIP peak **$10.84 (+120.3%)** in the first PM bar (04:00 ET, 465K sh / 15,236 trades); currently ~$9.4
- Hypothetical P&L (AH first-sighting $7.03 → PM peak $10.84): **+54%**; (our fill $8.69 → PM peak): **+24.7%**
- Float: 551K | Market Cap: ~$3.6M

Clears the winner bar: >100% on high, accumulating SIP volume. Sole real winner today (MSS peaked +83%, under the bar).

**Scanner Diagnostic:**
- Detectable at screening time? **YES**
- Surfaced from the first AH scan (22:30 CET, +73.4% Total) and every scan after; cleared the 2-AH-scan gate at 22:45 (+91.3%). SIP confirmed a genuine BUILD with heavy accumulation.
- **Detected AND selected** — entered at 23:00 CET @ $8.69 (11 sh). Ideal outcome: winner caught and traded.
- Scanner gap: none. Scanner did its job on the night's biggest mover.

### Baseline Tracking

- Days tracked: **68** (was 67 + 1)
- Winners detected by scanner: **55/64 (85.9%)** — TNON detected.
- Winner selected for paper trade: **32/63 (50.8%)** — TNON entered @ $8.69.
- Target: >80% detection
- Status: **BASELINE MET** (85.9% > 80%)

No baseline gap: Aug 17 (last baseline log) immediately precedes the evaluated Aug 18 session.

### Retrospective Scan Results

Live PM scan (04:20 ET) top hits: BIVI +88.7% ($1.82), TNON +71.7% ($9.36), MSS +64.3% ($2.58), CAST +18.6%, TWG +20.2%. TNON is the biggest genuine AH->PM continuation and matches last night's entered position. BIVI (7.2M float biotech) spiked from a mid-AH ignition (18:25 ET) and is a secondary mover, not a winner.

### Open Position P&L (Alpaca)

Both positions carried from last night, still open (exits handled by position-evaluation.md, not here). Alpaca quote endpoint is **stale** for both (TNON @16:00 ET `ask $0.00 x0`; MSS @16:59 ET) — P&L reported against **live SIP PM** price, not the stale book.

| Ticker | Entry | Entry Total% | Catalyst | Entry Time | PM Peak | Peak Time | Exit | P&L | P&L % | Status |
|--------|-------|--------------|----------|------------|---------|-----------|------|-----|-------|--------|
| TNON | $8.69 | +76.6% | None — low-float squeeze | 23:00 CET | $10.84 (SIP) | 04:00 ET | open | — | +8% (live ~$9.4) / +24.7% at PM peak | 🟢 Open |
| MSS | $1.90 | +21.0% | None — low-float squeeze | 23:00 CET | $2.88 (SIP) | 04:05 ET | open | — | +28% (live ~$2.44) / +51.6% at PM peak | 🟢 Open |

Alpaca-reported marks (lagging): TNON $9.62/+10.7%, MSS $2.14/+12.6%. Both understate vs live SIP. **No exits placed here.**

**Total Realized P&L (Alpaca fills only): €0.00** (no exits yet).

### Scanner Effectiveness

- Evening scans ran: **7 of 7 scheduled** (21:30, 22:00, 22:30, 23:00, 23:30, 00:00, 00:30 CET) plus 2 extra (22:15, 22:45). Full coverage of the entry window.
- Candidates found: TNON, MSS, CAST, CNET, BRNX, HKIT, EJH, TGL, KIDZ, CRE
- Retrospective matches: winner (TNON) + strong secondary (MSS) both detected and entered.

### Missed Opportunities

No significant missed opportunities. The night's biggest mover (TNON) was detected and entered; MSS likewise. TGL correctly skipped (faded, see follow-through).

### AH Mover Follow-Through

| Ticker | AH Peak | Peak Time | AH Trajectory | Current PM | From Peak | From Close | Verdict |
|--------|---------|-----------|---------------|------------|-----------|------------|---------|
| TNON | $10.10 SIP (+105%) | 16:30 ET | Build | $10.84 PM peak / ~$9.4 | PM peak EXCEEDED AH peak | +120% peak | 🟢 Continued — PM peak above AH peak, entered |
| MSS | $2.07 SIP | ~17:00 ET | Build/hold | $2.88 PM peak / ~$2.44 | PM peak EXCEEDED AH peak | +83% peak | 🟢 Continued — entered |
| TGL | $4.33 SIP (+62%) | 17:45 ET | Spike->fade | $3.68 PM peak | PM below AH peak | +38% peak | 🔴 Faded — PM fell short of AH peak (skip correct) |
| CAST | ~$5.9 (+179% Total) | early AH | Spike->fade | $2.49 (+18.6%) | far below AH peak | +18.6% | 🔴 Faded hard — ceiling+float skip correct |

**AH-peak-vs-PM-peak:** TNON PM peak ($10.84) EXCEEDED its AH peak ($10.10) — a continuation, not an AH-top fade. TNON sat at ~+105% AH (below the ~+130% extreme-runner fade zone), so it does not test that hypothesis; logged as a continue case in the ~+105/120% band.

### Notes

- **Ideal night.** Scanner detected AND we entered the night's biggest genuine mover (TNON, +120% PM peak on heavy real SIP volume), plus a strong secondary (MSS). Baseline detection 85.9%, above the 80% target.
- **Coverage:** 7/7 scheduled scans ran. No coverage failure.
- **Fade-rule false-negative tally (sub-3M):** TGL (Aug 18->19, float 1.8M, Grade None, AH SIP peak $4.33 +62% @17:45 ET faded -> PM SIP peak $3.68, **fell short**, PM below AH peak). Correctly skipped. **Standing sub-3M count: 4 of 12** (unchanged blow-past count; TGL is another negative). Hypothesis continues weakening — the ≥4/5 (≥80%) trigger stays NOT met.
- **PM-only gapper:** biggest raw PM mover today is TNON (+120%), an **AH->PM continuation** the scanner detected — not a PM-only gapper. No AH-scanner blind spot today. Holdable PM-only-gapper count in log/pm-open-scan.csv: **26** (cluster threshold long exceeded; the Initiative-6 early-PM pilot decision remains routed to Juan's email, not applied here).
- **Late-AH-tail surge:** none. TNON surged at AH open (16:00 ET), not in the 18:30–20:00 ET tail.
- **In-window feed-lag miss:** none new. TNON surfaced from its first AH scan. **Standing count: 4** — AH-data-source-verification recommendation remains routed to Juan's daily email (≥3 trigger still reached, no new evidence).
- **Price-floor exclusion:** no sub-$0.50 in-window volume-backed mover reviewed today. **Standing count: 5 across 2 nights, 0 holdable** (unchanged).
- **Reverse-split-squeeze fade:** no entered/skipped name tonight had a reverse-split catalyst. Tally unchanged (this-week splits 3/3 faded; older splits 3/5 non-fade).
- **Broker-block:** none new.
- **Stale-book execution-block:** TNON's Alpaca quote was stale (`ask $0.00 x0 @16:00 ET`) but the order filled at 23:00, so **not** a block — it is a fillable detected winner we entered. Standing count unchanged at 3.
- **No-fillable-book skip / Float-gate skip / Chase-cap:** none new. TNON filled BELOW its qualifying price ($8.69 vs $9.41), no chase into the fade zone. Chase-cap standing count unchanged at 1.
- **AH-peak-vs-PM-peak (extreme-runner ~+130% zone):** no new case in the >130% band. Standing 4 fade / 1 continue.

### Price Charts

```
 TNON - 2-Day Price Timeline (5-min intervals)
========================================================================

Previous Close: $4.92
2-Day Range: $4.81 - $10.84
Current: $9.54 (+93.9% from prev close)
Peak: $10.84 (+120.3%) at 08-19 08:00 ET

Chart (oldest → newest):
$   9.93 │                                                            
         │                                              █   █         
         │                                             █   █  █       
         │                                               ██  █ █████  
         │                                            █             ██
         │                                                            
         │                                                            
         │                                           █                
         │                                                            
         │                                                            
--
 MSS - 2-Day Price Timeline (5-min intervals)
========================================================================

Previous Close: $1.46
2-Day Range: $1.36 - $2.88
Current: $2.25 (+54.1% from prev close)
Peak: $2.88 (+97.3%) at 08-19 08:05 ET

Chart (oldest → newest):
$   2.44 │                                                            
         │                                                            
         │                                                            
         │                                                            
         │                                                            
         │                                                            
         │                                                            
         │                                                            
         │                                                            
         │                                                           █
```
