# Open Positions

Active paper trade positions, executed on the **Alpaca paper account** (`PA37U2Y192A7`).
Alpaca is the source of truth. This file mirrors `node scripts/broker.js positions`.
Every entry/exit must be a real Alpaca order; do not record trades that were not submitted.

## Current Positions

| Ticker | Entry | Shares | Entry Time | Catalyst Grade | Order ID | Notes |
|--------|-------|--------|------------|----------------|----------|-------|
| DOMO | $3.92 | 25 | 2026-07-22 23:32 CET | A | 32f667b6 | **Grade A catalyst:** Domo announced agreement to sell substantially all assets + certain liabilities to Progress Software for **$400M** (Business Wire ~16:15 ET). AH BUILD-and-hold: 2 AH scans >10% (23:00 +31.7% → 23:30 +24.8%), peaked $3.95 (+14.8%) at 17:00 ET, holding $3.88-3.92. Day -8.4% (not dead-cat), Total +14.2% (low extension). Real accumulating SIP volume (16:45 ET bar 439k sh/1857 trades; sustained 52k-315k sh/bar after). Two-sided book bid $3.82/ask $3.91 x100. Float 36.9M. Grade A → hold up to 5 days, trail stop -20% from peak. **07-23 10:30 CET: HOLD** — day 1, -2.5%, catalyst intact, peak $4.20 PM (+7% from entry, below +50% trail threshold), within -25% hard stop ($2.94). **07-23 14:30 CET: HOLD** — day 1, now $4.19 (+6.9%), bid $4.14. New SIP peak $4.50 at 11:55Z (+14.8% from entry) on heavy real volume (1.98M sh/bar), faded to $4.14. Peak below +50% trail threshold → no trail. Well above -25% hard stop. Catalyst intact. |
| PAVS | $7.17 | 2026-07-23 23:00 CET | 13 | b7fd6a5e | **Grade C** (anti-dilution / momentum squeeze). Paranovus Entertainment (AI-entertainment). Terminated A.G.P. ATM share-sale agreement ~Jul 20/21 (removes dilution overhang); 1-for-100 reverse split Jun 25 (month-old); no fresh Jul 23 PR in 4 searches → low-float continuation. AH BUILD-and-hold: 2 AH scans >10% (22:45 +21.5% → 23:00 +22.7%), ignition 16:25 ET to $7.78 peak, holding $7.17–7.42 (within ~6% of high). Real heavy SIP volume (20:25Z 406k sh/5,764tr, 20:30Z 442k/7,130tr; VWAP $7.11–7.32 corroborates AH $7.25). Day +52.3% (positive, not dead-cat), Total ~+85% (under +150 ceiling). Float 857K (ultra-low). Grade C → exit in premarket, stop -10%. |
| AKAN | $9.47 | 2026-07-23 23:00 CET | 10 | e21b6504 | **Grade None** (no catalyst found). Akanda Corp — cannabis micro-cap. 4 searches: no fresh Jul 23 PR/8-K/earnings; reverse split 1-for-4.5 was Apr 13 (months old); Nasdaq equity-deficiency notice Jun 18 (compliance due Jul 31). Low-float momentum, no fresh catalyst. 2 AH scans >10% (22:45 +10.2% → 23:00 +19.0%, rising). Early spike $10.44 at 16:05 ET → faded to $8.57 → rebuild to $9.40–9.60 (~10% off high, within 20% "holding" band). Real but thin SIP (ignition 573tr, rebuild 768tr; two-sided book ask $9.56 x100 — fillable). Day +0.1% (flat, not dead-cat), Total ~+17.5% (well under ceiling). Float 541K (ultra-low). Grade None → exit at first premarket opportunity. |
| ANY | $2.29 | 41 | 2026-07-23 00:30 CET | C | 5538d150 | **Grade C** (Cathedra Bitcoin acquisition narrative / AI-infra momentum). Sphere 3D Corp. Recently completed all-stock acquisition of Cathedra Bitcoin (~2-3 days ago) → ~53 MW power platform, 100+ MW pipeline, ~1.2 EH/s hash rate, AI-infra/data-center pivot. Fresh bullish coverage 1 day ago; no fresh Jul 23 PR in 3 searches → narrative continuation. 2 AH scans >10% (00:00 +23.5% → 00:30 +35.4%). Late accelerating BUILD: based $1.78–1.91 through 17:10 ET → AH peak $2.52 (+55%) at 18:05 ET → holding $2.33 (within ~8% of high) at 18:31 ET. Real heavy SIP volume (21:35Z 267k sh/2,332tr, VWAP $2.20 corroborates). Day +8.3% (positive, not dead-cat), Total ~+30% from $1.76 (well under +150 ceiling). Float 6.0M (ideal). Grade C → exit in premarket. |
| JEM | $5.37 | 2026-07-23 00:00 CET | 17 | 68fd0c2b | **Grade D** (dilution overhang, no fresh same-day catalyst). 707 Cayman Holdings — Cayman apparel supply-chain micro-cap. 4 searches: no fresh Jul 23 PR/8-K/earnings. Active dilution setup: F-1 for sale of up to 1M Class A shares + 4M warrants at $6.12 (filed ~1 week ago); 6-K authorized-share expansion from 2.08M to 50M shares (~2 days ago, Aug 5 EGM); 1-for-12 reverse split effective Jul 14 (~9 days ago); AI/blockchain/crypto board exploration PR was Jul 1 (3 weeks old). 2 AH scans >10% (23:30 +22.1% → 00:00 +22.0%). Ignition 17:10 ET, peaked $6.84 at 17:30 ET (right through the $6.12 offering price) then faded to $5.57 (~18% off high, within 20% "holding" band; AH% flat across scans, not declining). Real heavy SIP volume (21:10Z 420k sh/4,800tr, 21:20Z 374k/5,134tr; VWAP $5.75–6.21 corroborates AH price). Day +34.3% (positive, not dead-cat), Total ~+52% from $3.53 (under +150 ceiling). MCap $3.0M (ultra-low float). Grade D → exit at first premarket opportunity. |

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
| LGCL | $1.58 | $1.96 | +$22.04 | +24.1% | 1 | None (ideal-float 1.6M AH BUILD, no fresh catalyst) | Grade None — exit at first PM opportunity at any profit. Entered 07-23 00:30 CET. Clean detect+select+continuation: AH BUILD to $1.78, PM 07-23 continued to $2.47 peak (+56% from entry) at 08:05 ET then faded. Sold into the fade at 10:30 CET pulse. SIP liquid (648k-3.1M sh/bar). SELL 58 @ limit $1.82 ext (id d510e021) filled @ $1.96. Real fill $1.96. |
| PLAG | $0.98 | $0.86 | -$11.64 | -12.2% | 1 | None (China food/methanol microcap, no same-day catalyst) | Grade None — exit at first PM opportunity + below -10% hard stop. Entered 07-22 23:01 CET. OVN peak $1.79 (+83%); faded overnight, PM 07-23 spiked $1.13 then faded to $0.86 on real volume (1-3M sh/bar). Sold first PM pulse. SELL 97 @ limit $0.83 ext (id 876ddb3a) filled @ $0.86. Real fill $0.86. |
| AEHL | $0.69 | $0.70 | +$1.36 | +1.5% | 1 | None ("Genius Plan" crypto/BTC-treasury narrative, no fresh same-day PR) | Grade None — exit at first PM opportunity at any profit. Entered 07-23 00:01 CET. OVN peak $0.82 (+19%); PM 07-23 traded $0.67-0.74 on real volume (125k-322k sh/bar). Sold first PM pulse at small profit. SELL 136 @ limit $0.66 ext (id 48266080) filled @ $0.70. Real fill $0.70. |
| HIHO | $1.50 | $1.26 | -$14.16 | -16.0% | 2 | B (Q1 FY2027 earnings: net sales +29.2% YoY, gross profit +58.4%, margin +800bps) | Grade B — day-2 time limit reached AND at -15% hard stop ($1.28). Entered 07-20 23:01 CET. SIP PM 07-21 opened $1.89 (peak, +26%) then faded steadily; live Alpaca quote bid $1.21 x1000 at pulse. Sold on time limit + hard stop. SELL 59 @ limit $1.18 ext (id f879332a) filled @ $1.26. Real fill $1.26. |
| PAPL | $1.10 | $0.84 | -$20.80 | -23.6% | 1 | B (Pineapple Financial Q3 FY2026 earnings) | Grade B — below -15% hard stop ($0.94). Entered 07-21 00:01 CET. Peak $1.33 (+21%, OVN). SIP PM 07-21 opened $1.28 then faded steadily to $0.80-0.85 on real volume (341K/153K/180K sh bars). Alpaca quote stale; SIP liquid. Sold per hard-stop rule. SELL 80 @ limit $0.79 ext (id 9ca4f305) filled @ $0.84. Real fill $0.84. |
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
