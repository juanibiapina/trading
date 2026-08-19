# Post-Market Screening - 2026-08-19

## Scan 21:30 CET (3:30 PM ET)

**Session: REGULAR** (AH opens 22:00 CET / 4:00 PM ET). No entries per regular-session caution rule — watch names flagged for AH confirmation.

Scanner hits (39 total). Small-float / rising-volume movers worth watching into AH:

| Ticker | Price | Chg% | 5mVol | Avg5m | IRVol | VChg% | Float | MCap | Industry |
|--------|-------|------|-------|-------|-------|-------|-------|------|----------|
| FCUL | $0.59 | +63.5% | 35K | 14K | 27.8 | -23.7 | 44.1M | 26.6M | Aerospace & Defense |
| UUU | $6.00 | +32.7% | 4K | 8K | 8.9 | +82.2 | 1.5M | 18.2M | Computer Communications |
| PSIG | $2.06 | +29.6% | 12K | 5K | 2.6 | +19.6 | 8.6M | 31.7M | Air Freight/Couriers |
| QTEX | $1.14 | +27.0% | 35K | 43K | 32.4 | +89.5 | 38.0M | 49.7M | Medical Specialties |
| SUGRF | $9.47 | +14.4% | 15K | 3K | 11.8 | +271.4 | 851K | 219.0M | Wholesale Distributors |
| TGL | $3.01 | +12.7% | 13K | 10K | 144.7 | +48.5 | 1.8M | 5.9M | Misc Commercial Services |

Most other top-%% hits (ZSTK +197%, BTCT +169%, RDAC +69%, AZI, CDTG, SKK, MSS) show VChg% near -99% = single closing prints / illiquid, not live volume. Ignored.

**Watch — pending AH confirmation:** UUU (float 1.5M, VChg +82%), TGL (float 1.8M), SUGRF (float 851K, VChg +271%), PSIG (float 8.6M). Small floats with rising volume. Re-check at 22:00+ CET for sustained AH momentum. No entry until stock reappears in an AH scan with sustained move.

---

## Scan 22:00 CET (4:00 PM ET)

**Session: AFTERHOURS.** Scanner ran at exactly 16:00 ET (AH open) — 0 hits. No accumulated AH volume yet at the bell, expected at the first scan. Observation-only window (learning-phase: no entries before 23:00 CET).

No candidates found.

**Watch names carried from 21:30 regular-session scan** (re-check for sustained AH momentum at 22:30/23:00+): UUU (float 1.5M), TGL (float 1.8M), SUGRF (float 851K), PSIG (float 8.6M). None reappeared in this AH scan yet.

---

## Scan 22:15 CET (4:15 PM ET)

**Session: AFTERHOURS.** Scanner `--all` → 0 hits. Observation-only window (learning-phase: no entries before 23:00 CET).

No candidates found.

**Watch names cross-checked in SIP** (AH-start 20:00:00Z), all thin first-bar only, no accumulation:

| Ticker | AH bar (16:00-05 ET) | Trades | Vol | Note |
|--------|----------------------|--------|-----|------|
| UUU | O$6.24 H$6.24 C$5.86 | 31 | 27K | faded off open, thin |
| TGL | O$2.92 H$2.97 C$2.97 | 16 | 8K | thin |
| PSIG | O$2.04 H$2.06 C$2.05 | 7 | 4K | thin |
| SUGRF | no SIP bars | - | - | no AH liquidity |

None building. Re-check at 22:30/23:00 for sustained AH momentum before any entry consideration.

---

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|

_No entries this session (regular session, pre-AH)._

---

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| MSS | $1.90 | $2.20 | +15.8% | $2.88 | 1 | None | SELL | Grade None, exit first PM at any profit. PM spiked $2.88 then faded, sold on fade |
| TNON | $8.69 | $9.74 | +12.1% | $10.84 | 1 | None | SELL | Grade None, exit first PM at any profit. PM spiked $10.84 then settled, sold into settle |

**Actions taken:**
- SELL 55 MSS @ limit $2.12 ext (id 74711cc2) filled @ $2.20 (price improvement) → +$16.50 (+15.8%)
- SELL 11 TNON @ limit $9.50 ext (id f6452412) filled @ $9.74 (price improvement) → +$11.55 (+12.1%)
- Both Grade None; both green in PM; both liquid SIP. Exited per exit-at-any-profit rule.
- Pulse net: +$28.05. No open positions remaining.
- Note: Alpaca IEX quotes were stale (yesterday timestamps); used SIP 5Min bars for real PM levels.

## Position Evaluation — 14:30 CET

No open positions. All closed at 10:30 CET pulse (MSS +15.8%, TNON +12.1%). Alpaca `positions` empty; `OPEN_POSITIONS.md` matches. Nothing to evaluate.
