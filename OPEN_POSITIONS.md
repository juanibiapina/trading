# Open Positions

Active paper trade positions, executed on the **Alpaca paper account** (`PA37U2Y192A7`).
Alpaca is the source of truth. This file mirrors `node scripts/broker.js positions`.
Every entry/exit must be a real Alpaca order; do not record trades that were not submitted.

## Current Positions

| Ticker | Entry | Shares | Entry Time | Catalyst Grade | Order ID | Notes |
|--------|-------|--------|------------|----------------|----------|-------|
| _(none)_ | | | | | | No open positions. |

## Position Rules

### Entry (after-hours scans)
- Enter when stock meets scanner criteria (float, AH%, catalyst)
- **Multiple concurrent positions allowed** (W24 2026). An open position no longer blocks new entries; enter every qualifying candidate.
- One entry per candidate per night (don't average into the same ticker).
- Position size: ~$100 per trade (learning phase), sized independently per position
- Record catalyst grade at entry (A/B/C/D/None)
- **Execute via Alpaca:** `node scripts/broker.js buy SYM QTY --limit P --ext` (extended-hours limit). Record the real fill price returned by the order, not the quoted/assumed price.

### Holding Rules (based on catalyst grade)
| Grade | Description | Hold Strategy |
|-------|-------------|---------------|
| **A** | Major operational catalyst (acquisition, breakthrough deal) | Hold up to 5 days, trail stop at -20% from peak |
| **B** | Solid catalyst (earnings beat, FDA milestone) | Hold up to 2 days, stop at -15% from entry |
| **C** | Weak catalyst (analyst upgrade, financing) | Exit in premarket, stop at -10% |
| **D/None** | No catalyst or dilution | Exit at first premarket opportunity |

### Exit Triggers
1. **Stop loss hit** — Exit immediately
2. **Target reached** — Trail stop, don't exit all at once
3. **Time limit** — Grade A: 5 days, Grade B: 2 days, Others: premarket
4. **Catalyst invalidated** — News changes thesis → exit

Execute exits via Alpaca: `node scripts/broker.js sell SYM QTY --limit P --ext`. Record the real fill price.

## Risk Calculation

Based on historical data (17 winners tracked):
- Multi-day runners (held = big win): 2/17 = 12%
- Same-day peaks (held = loss): 15/17 = 88%

**Expected value per €100 position if held:**
- 12% chance of +200% avg = +€24
- 88% chance of -50% avg = -€44
- **EV if holding blindly: -€20 per trade**

**But with catalyst filtering:**
- Grade A catalyst runners: 2/2 = 100% (AIIO, UGRO both had real catalysts)
- No-catalyst crashes: 2/2 = 100% (EZGO, WOK)

**Conclusion:** Hold Grade A, exit others quickly.

## Closed Positions

Clean slate as of 2026-06-25. Only real Alpaca paper fills are recorded here going forward.
The pre-Alpaca markdown ledger used assumed prices that were never executed and has been discarded.

| Ticker | Entry | Exit | P&L | P&L % | Hold Days | Catalyst | Notes |
|--------|-------|------|-----|-------|-----------|----------|-------|
| GANX | $2.39 | $1.97 | -$17.22 | -17.6% | 1 | B (Phase 1b Parkinson's data) | Hard stop hit. Held overnight; PM faded from $2.17 to $1.97, below -15% stop ($2.03). Sold per Grade B hard-stop rule. Real fill $1.97. Peak $2.59 (AH 06-29). |
| IVF | $1.58 | $2.00 | +$25.20 | +26.6% | 1 | None (Grade None) | Low-float AH build, no fresh catalyst. Sold premarket per Grade None rule (exit at any profit). PM ran to $2.59 peak (+64% from entry); exited at $2.00. |
| CTNT | $2.05 | $1.90 | -$7.20 | -7.3% | 1 | None (Grade None) | Low-float squeeze, no catalyst. Sold first premarket opportunity per Grade None rule. AH peaked $2.21; faded to $1.94 PM. Exited at $1.90 (real fill). |
| ALZN | $1.31 | $1.29 | -$1.46 | -1.5% | 1 | None (Grade None) | No catalyst (earnings due 7/19; no same-day PR). Sold first PM opportunity per Grade None rule. OVN peak $1.45 (+10.7%); faded overnight. SELL 73 @ $1.29 ext (id f7da27e2) filled 2026-07-01 08:33 UTC. Real fill $1.29. |
| EDHL | $4.81 | $5.10 | +$5.80 | +6.0% | 1 | None (Grade None) | Low-float double-pump momentum, no catalyst. Sold first PM opportunity per Grade None rule. OVN peak $5.83 (+21% from entry); PM opened $6.29 spike then faded to ~$5.15. SELL 20 @ $5.10 ext (id cdfa66da) filled 2026-07-07. Real fill $5.10. |
| DCX | $1.34 | $1.39 | +$3.30 | +3.7% | 1 | None (Grade None) | Low-float AH BUILD, no catalyst. Sold first PM opportunity per Grade None rule. PM 07-08 opened strong ($1.63 H, 2.5M sh/bar) then faded; peak +10% (~$1.48). Exited on the fade. SELL 66 @ $1.39 ext (id a10d862b) filled 2026-07-08. Real fill $1.39. |
| VEEE | $6.28 | $6.17 | -$1.65 | -1.8% | 1 | C (DoD LYNX Platform registration) | Grade C — exit in first PM pulse. AH high $7.31; PM opened $6.97 then faded to $6.30/vwap $6.45. Sold in first PM pulse per Grade C rule, small loss (above -10% stop). SELL 15 @ $6.17 ext (id 590df196) filled 2026-07-08. Real fill $6.17. |
| SEER | $2.26 | $2.20 | -$2.58 | -2.65% | 5 | A (CEO $2.45/share buyout proposal + activist proxy contest) | Grade A held full 5-day window (entry 07-03). Catalyst intact ($2.45 floor) but never re-rated above entry; peak $2.34 (+3.5%, OVN 07-02). Sold on day-5 time limit at 14:30 CET pulse. SELL 43 @ limit $2.12 ext (id 34b9f54e), filled @ $2.20 (real bid). |
| SUNE | $2.56 | $2.44 | -$4.32 | -4.7% | 1 | None | No same-day catalyst (SUNation Energy solar). Sold first PM opportunity per Grade None rule. OVN peak ~$2.67 (+4.3%); PM opened $2.72 spike (single-bar) then faded to $2.41/vwap $2.39. SELL 36 @ limit $2.35 ext (id 54d1a663) filled 2026-07-09. Real fill $2.44. |
| PMA | $1.66 | $1.48 | -$10.80 | -10.8% | 1 | C (ticker change MSW→PMA rebrand + dilutive convertibles) | Grade C — exit first PM pulse. Below -10% hard stop. OVN faded to -18%; PM bounced to $1.67 H then back to $1.48/vwap $1.54. Sold in first PM pulse. SELL 60 @ limit $1.44 ext (id a40736bf) filled 2026-07-10. Real fill $1.48. |
| ELPW | $1.18 | $0.97 | -$17.43 | -17.8% | 1 | D (dilutive $6M offering + 1-for-80 reverse split) | Grade D — exit at first PM opportunity + below -10% stop. OVN peak $1.37 (+16%); faded overnight, PM opened $1.27 H then dropped to $0.95/vwap $0.99. Sold first PM opportunity. SELL 83 @ limit $0.92 ext (id 21ed3062) filled 2026-07-10. Real fill $0.97. |
| YYGH | $1.66 | $1.37 | -$16.82 | -17.5% | 1 | None (low-float 133K, 30-for-1 reverse split, no fresh catalyst) | Grade None — exit at first PM opportunity + below -10% stop. OVN peak $2.00 (pre-entry); post-entry faded, PM $1.37-1.44 on thin volume (~8K/bar). Sold first PM opportunity. SELL 58 @ limit $1.33 ext (id 72970f69) filled 2026-07-10. Real fill $1.37. |
| VMAR | $1.57 | $2.22 | +$40.30 | +41.4% | 1 | None (ultra-low float 670K, no fresh catalyst) | Grade None — exit at first PM opportunity at any profit. Explosive real PM move: 4.5M sh in first PM bar (37,981 trades), peaked $3.35 (+114% from entry) at PM open then dumped ($3.35→$2.94→$2.62). Sold into the fade at 10:30 CET pulse. SELL 62 @ limit $2.15 ext (id edb17587) filled 2026-07-14. Real fill $2.22. |
| VTAK | $0.72 | $0.80 | +$10.00 | +11.1% | 1 | None (squeeze setup, no fresh catalyst) | Grade None — exit at first PM opportunity at any profit. PM spiked $1.27 (+76%) at 08:05 UTC on 6M sh, then faded to ~$0.85. Sold into the fade at 10:30 CET pulse. SELL 125 @ limit $0.80 ext (id 3652f341) filled 2026-07-15. Real fill $0.80. |
| XCUR | $2.40 | $2.00 | -$16.40 | -16.7% | 1 | None (distressed biotech, Nasdaq deadline July 20) | Grade None — exit at first PM opportunity + below -10% hard stop. PM traded $1.96-2.26, faded to ~$1.98. Sold first PM pulse. SELL 41 @ limit $1.92 ext (id 9c193da3) filled 2026-07-15. Real fill $2.00. |
| LVLU | $11.03 | $8.12 | -$26.19 | -26.4% | 2 | B (strategic-alternatives review, special committee) | Grade B — day-2 time limit reached AND below -15% hard stop ($9.38). Entered 07-13 23:01 CET. Held near AH high overnight but never re-rated above entry; faded to $8.00-8.10 PM (thin, 11 trades/bar). Canceled stale $8.40 order, repriced. SELL 9 @ limit $7.85 ext (id 2cdf7fc6) filled 2026-07-15 14:30 CET. Real fill $8.12. |
| TGHL | $1.33962 | $1.09 | -$19.72 | -18.6% | 1 | None (BUILD-and-hold, broad-market move, no catalyst) | Grade None — exit first PM opportunity + below -10% hard stop. Entered 07-15 23:36 CET. PM 07-16 opened $1.15 then faded: 5Min bars $1.33H→$1.08C on 5.6M sh (SIP vwap $1.07-1.20, liquid). Sold first PM pulse into the fade. SELL 79 @ limit $1.04 ext (id e56b50df) filled @ $1.09. Real fill $1.09. |
| BIYA | $4.55 | $3.92 | -$13.86 | -13.8% | 1 | None (low-float China microcap, reverse split + stale BNB narrative, no fresh catalyst) | Grade None — exit at first PM opportunity + below -10% hard stop. Entered 07-16 23:46 CET. OVN peak $5.03 (+51%); PM 07-17 opened $4.04 then faded to $3.94/vwap $4.09 (liquid, 198K sh/bar). Sold first PM pulse. SELL 22 @ limit $3.85 ext (id 9445ec9a) filled @ $3.92. Real fill $3.92. |
| GCTK | $0.8743 | $0.546 | -$33.16 | -37.6% | 2 | A (completed reverse merger with Lōkahi Therapeutics) | Grade A hard stop hit (-25% = $0.6525). Entered 07-14 00:30 CET. Strong AH BUILD to $0.99, but PM collapsed steadily $0.95→$0.55 on day 2 (SIP vwap $0.56, liquid). Reverse-merger structure (dilution/control-change risk flagged at entry) behaved like a dilution event, not an AIIO/UGRO-style runner. SELL 101 @ limit $0.53 ext (id 86275106) filled 2026-07-15 14:30 CET. Real fill $0.546. |
| CJMB | $1.01 | $1.21 | +$19.00 | +19.8% | 1 | B (Alabama State University pharma manufacturing partnership) | Grade B trail stop hit. Entered 07-16 00:30 CET. PM peaked $1.58 (+56%) at open (08:00Z, 2.6M sh first bar) then faded monotonically to $1.21 by 14:30 CET pulse. Trail stop $1.34 (peak-15%, set at 10:30 pulse) breached; sold per Grade B trail rule. Liquid throughout (bid $1.21 x500). SELL 95 @ limit $1.18 ext (id 30aff93a) filled 2026-07-17 14:30 CET. Real fill $1.21. |
