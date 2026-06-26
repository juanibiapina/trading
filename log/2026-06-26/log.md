# 2026-06-26

## Morning Evaluation — 10:20 CET (Pulse 1)

### Today's Winner

**ILLR (Triller Group)** — Packaged Software / social media (TikTok rival)
- Catalyst: **Tier A** — announced acquisition of a *significant SpaceX position* (MT Newswires); the +400% move is a strategic-acquisition narrative, not the reverse split. Confirmed via Stocktwits/GlobeNewswire/MT Newswires.
- Previous Close (Jun 24): $0.77
- Regular close Jun 25: **$3.05 (+296.6%)** — the bulk of the move happened in the *regular* session
- AH last night: built $3.05 → **$4.20 peak (+446% from $0.77) at 19:55 ET** (late surge, steady climb)
- Premarket now (04:20 ET): **$6.62** (+760% from $0.77, +57.6% from AH peak); thin tick to ~$7.20 noted on the 2-day range. PM is only 20 min old.
- Hypothetical P&L (AH entry ~$3.05–$3.44 → PM ~$6.62): **+92% to +117%**
- Float: n/a (scanner) | Market Cap: ~$23M (AH) → ~$60M (PM)

**Scanner Diagnostic:**
- Detectable at screening time? **YES** — ILLR was in **all 7 evening scans** (21:30 through 00:30 CET), flagged from the 21:30 regular-session scan onward.
- Why we didn't act: **SKIP (extension ceiling).** At every scan ILLR was already +296% on the regular day and +347% to +446% Total (>> the 150% extension ceiling). It also failed the ceiling-override (needs VRatio >5x; ILLR printed **VRatio 0.1x–0.4x = no real AH volume**). The entire $3.05→$4.20 AH ramp printed on ~zero recorded AH volume — a regular-day continuation, not a fresh AH base. Per current rules this was a correct skip.
- Scanner gap: This is an **extension-ceiling false negative on an A-catalyst regular-day continuation.** ILLR kept running from +296% (at AH start) to +760% (PM). But it never had real AH volume, so an AH limit order may not have filled cleanly anyway. No rule change justified on one case — log it to the extension-ceiling watch dataset. The lesson is the ceiling correctly protects against chasing, but A-catalyst names (real acquisition) can extend far past it.

### Baseline Tracking

- Days tracked: **38** (was 37 + 1)
- Winners detected by scanner: **33/38 (86.8%)** — ILLR added (detected in all 7 scans)
- Winner selected for paper trade: **22/38 (57.9%)** — we traded IVF, not ILLR. ILLR was correctly skipped (over ceiling + no AH volume), so this is a "detected but not selected" case, not a selection error.
- Target: >80% detection
- Status: **BASELINE MET** (86.8% detection)

### Retrospective Scan Results

Live premarket scan (04:20 ET) — 4 hits: ILLR +97.7% ($6.03), IVF +53.6% ($1.91), TII +46.2% ($3.26), NEXR +10.9% ($1.22). AH reconstruction via `check-prices.py --ah-history`:

| Ticker | Jun 25 close | AH peak | AH peak time | PM now | AH→PM |
|--------|--------------|---------|--------------|--------|-------|
| ILLR | $3.05 | $4.20 (+446% vs $0.77) | 19:55 ET | $6.62 | continued, PM > AH |
| IVF | $1.24 | $1.80 (+36% vs $1.32) | 19:40 ET | $2.08 | continued, PM > AH |
| TII | $2.23 | $4.56 (+110%, zero vol) | 18:25 ET | $3.25 | faded, illiquid |
| NEXR | $1.10 | ~$1.32 (+20%) | late AH | $1.22 | faded |

### Open Position P&L (Alpaca)

| Ticker | Entry | Entry Total% | Catalyst | Entry Time | PM Peak | Peak Time | Exit | P&L | P&L % | Status |
|--------|-------|--------------|----------|------------|---------|-----------|------|-----|-------|--------|
| IVF | $1.58 | +19.7% | None — reverse split, no fresh catalyst | 00:00 CET | $2.08 | 04:10 ET | open | +€27.60 | +29.1% | 🟢 Open |

IVF (60 @ $1.58, Grade None) is up +29.1% on the Alpaca paper account (now ~$2.04). Exit is handled by `position-evaluation.md` (10:30 / 14:30 CET) — not closed here. PM peak $2.08 at 04:10 ET (PM only 20 min old; may extend).

**Total Realized P&L (Alpaca fills only): €0.00** (position still open)

### Scanner Effectiveness

- Evening scans ran: **7 of 7** (21:30 – 00:30 CET). No coverage failure.
- Candidates found: ~11 unique tickers across the night (ILLR, IVF, TII, NEXR, SHPH, LGCL, DLHC, PBK, PROP, HUMA, LABT, ELDN)
- Retrospective matches: 4/4 of this morning's PM movers were in the evening scans (ILLR, IVF, TII, NEXR all detected). **100% detection of PM movers.**

### Missed Opportunities

No significant missed opportunities — every PM mover was detected in the evening scans. ILLR (winner) and TII were both detected and skipped per rules (extension ceiling / zero AH volume), not missed.

### AH Mover Follow-Through

| Ticker | AH Peak | Peak Time | AH Trajectory | Current PM | From Peak | From Close | Verdict |
|--------|---------|-----------|---------------|------------|-----------|------------|---------|
| ILLR | $4.20 (+446%) | 19:55 ET | Late surge / Build | $6.62 | +57.6% | +760% | 🚀 Continued — PM > AH |
| IVF | $1.80 (+36%) | 19:40 ET | Build (choppy) | $2.08 | +15.6% | +57.6% | ✅ Continued — PM > AH (our trade) |
| TII | $4.56 (+110%) | 18:25 ET | Spike→fade (zero vol) | $3.25 | -28.7% | +49.8% | ❌ Faded — illiquid AH |
| NEXR | ~$1.32 (+20%) | late AH | Build (thin) | $1.22 | -7.6% | +10.9% | ❌ Faded from AH |

**AH-peak-vs-PM-peak check:** ILLR and IVF both had PM peaks *above* their AH peaks (PM was the better exit). TII faded hard from its zero-volume +110% AH spike. **Extreme-runner note:** ILLR's AH peak was +446% (>250% extreme threshold), but PM (+760%) *exceeded* it — a **counter-example** to the MSW hypothesis (that extreme AH runners peak in AH and fade into PM). Difference: ILLR had a real A-catalyst (SpaceX acquisition) and a fresh ongoing news cycle, whereas MSW's extreme run was on dilutive notes. Tally: extreme runners 1 fade (MSW), 1 continued (ILLR).

### Notes

- **Coverage:** 7/7 evening scans ran. No coverage failure. Running coverage-failure tally unchanged (founding case Jun 18–19 only).
- **Extension-ceiling watch (ILLR):** A-catalyst (SpaceX acquisition) regular-day continuation. Skipped at +347%–+446% Total, kept running to +760% PM. Hypothetical AH→PM **+92% to +117%**. BUT zero real AH volume (VRatio 0.1–0.4x) — failed ceiling-override, and an AH fill was questionable. Add to ceiling dataset; not a rule change on one illiquid case.
- **PM-only gapper tracking:** biggest raw PM mover = **ILLR (+760%)**, classified as an **AH→PM continuation** (moved +37% in after-hours, detectable by the AH scanner). **Not** a PM-only gapper, **not** a detection miss. No new PM-only gapper today.
- **Late-AH-tail surge:** ILLR's defining move was the regular session + steady AH build (peak 19:55 ET); not a post-00:30-CET tail surge. TII's +110% peak (18:25 ET) was just inside the scanned window but on zero volume. No new late-AH-tail case.
- **Fade-rule false negatives:** none today. TII faded from its AH spike and stayed below (PM $3.25 < AH $4.56) — but it was never a live entry (zero AH volume). No re-explosion.
- **Ceiling-override / dead-cat-override watch:** none flagged in last night's log.
- **TII trap:** classic zero-AH-volume illiquid ramp (the NEXR pattern). Scanner's "AH Vol 3.4M / VRatio 4.9x" was regular-session close volume, not AH liquidity; Alpaca book showed ask $0.00 x0. Correctly skipped.
- **IVF (our trade):** Grade None (reverse split, no fresh catalyst) but clean low-float (1.8M) BUILD-and-hold on real volume (VRatio 6.2x). Up +29% — the trajectory+volume profile worked even with no catalyst. Watch the premarket exit.

### Price Charts

```
ILLR — 2-Day: Prev close $0.77 | Range $0.71–$7.20 | AH peak $4.20 (19:55 ET) | PM ~$6.62 (+760%), still early
IVF  — 2-Day: Prev close $1.32 | AH peak $1.80 (19:40 ET) | PM peak $2.08 (04:10 ET); entry $1.58 → +31% at PM peak
TII  — 2-Day: Prev close $2.17 | AH peak $4.56 (18:25 ET, ZERO volume) | PM $3.25, faded -29% from AH peak
```

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|------|------|-------|----------|--------|
| IVF | $1.58 | $2.00 | +26.6% | $2.59 | 1 | None | SELL | Grade None rule: exit at any profit in premarket. Sold 60 @ $2.00. |

**Actions taken:**
- SELL IVF 60 @ $2.00 (Alpaca order 89e65d5d, filled@$2.00). Realized **+$25.20 (+26.6%)**.
- IVF moved to Closed Positions in OPEN_POSITIONS.md. No open positions remain.
- Note: PM peaked at $2.59 (+64% from entry) at 08:00 ET, then pulled back to $2.00. Exited at $2.00 per Grade None rule (take any premarket profit, don't chase the peak).
