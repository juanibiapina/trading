# 2026-07-28

## Position Evaluation — 10:30 CET

| Ticker | Entry | Current | P&L % | Peak (SIP PM) | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|---------------|------|-------|----------|--------|
| INLF | $4.12 | $4.89 | +18.7% | $5.36 (+30.1%) | 1 | None | **SELL** | Grade None → exit at first PM opportunity at any profit. Filled @ $4.89. |
| BZFD | $1.30 | $1.29 | -0.8% | $1.52 (+16.9%) | 0 | C | **SELL** | Grade C → exit in first PM pulse. Filled @ $1.29. |
| DOMO | $3.92 | $3.55 | -9.4% | $4.50 (+14.8%) | 5 | A (mis-graded) | **SELL** | Day 5/5 time limit + exit-flagged 07-24 (merger-arb, price pinned). Order resting, PM untraded. |

### Detail

**INLF** — Best case of the AH-build → PM-continuation pattern working. PM opened at 08:00Z with a real 618K-share bar (10,986 trades), ran $4.20 → $5.36 by 08:10Z, then settled $4.85-4.96 (vwap $4.97). Sold into the settle at $4.89, +18.7%. PM peak was +30% from entry; the Grade-None "exit at first PM opportunity" rule left ~11 points on the table but captured the majority of the move on real liquidity.

**BZFD** — PM opened $1.39, spiked $1.52 in the first bar (288K sh), then bled back to $1.27-1.33 on collapsing volume (29K → 17K → 20K sh/bar). Classic spike-and-fade. Grade C rule fired correctly; the $1.52 print was a first-bar-only level that would not have been fillable at size. Exited flat at $1.29.

**DOMO** — Day 5 of the Grade A window and the exit flag from 07-24 (merger-arb name, Progress Software all-cash $400M pins the price and kills AH→PM momentum). Premarket is effectively dead: one 5Min bar, 550 shares, 5 trades at $3.55. Sell 25 @ limit $3.48 ext submitted (id fadb7c40), resting. Will fill when liquidity arrives. Confirmed -9.4% at last SIP print.

**Actions taken:**
- SELL 22 INLF @ limit $4.88 ext (id e444adb3) → **filled @ $4.89**, +$16.94 (+18.7%)
- SELL 76 BZFD @ limit $1.26 ext (id d19bb119) → **filled @ $1.29**, -$0.76 (-0.8%)
- SELL 25 DOMO @ limit $3.48 ext (id fadb7c40) → **resting**, no PM liquidity yet
- OPEN_POSITIONS.md reconciled with Alpaca (BZFD row had shares/entry-time columns swapped)

**Net realized this pulse:** +$16.18

**Note on stale quotes:** `broker.js quote` returned yesterday's 20:00Z close for all three names (paper IEX feed does not carry premarket). All pricing and limit placement came from SIP 5Min/1Min bars. Yahoo `check-prices.py` returned no PM data either. SIP bars remain the only usable premarket source.

**For the daily email:** DOMO is the last open position and its sell is resting unfilled in a dead premarket book. If it does not fill by the 14:30 pulse, it fills at the open. No decision needed from Juan; noting because it closes out the mis-graded merger-arb trade Juan flagged on 07-24.

## Position Evaluation — 14:30 CET

| Ticker | Entry | Current | P&L % | Peak (SIP PM) | Days | Grade | Decision | Reason |
|--------|-------|---------|-------|---------------|------|-------|----------|--------|
| DOMO | $3.92 | $3.55 | -9.4% | $4.50 (+14.8%) | 5 | A (mis-graded) | **SOLD** | Resting order from 10:30 pulse filled @ $3.55 at 11:00Z. |

**Portfolio is flat.** No open positions.

### Detail

**DOMO** — The 10:30 sell (25 @ limit $3.48 ext, id fadb7c40) rested ~2.5 hours in a near-dead premarket book and filled at **$3.55** at 11:00:00Z, 7 cents above the limit. Final: -$9.25, -9.4%, 5 days held. Premarket volume for the whole session was trivial (550 / 179 / 150 / 906 / 350 / 1000 shares per 5Min bar) in a $3.53-3.59 band — confirming the merger-arb pin.

### Closing the DOMO thesis

Juan flagged this trade on 07-24 and he was right. Domo is being bought for cash ($400M, Progress Software). An all-cash acquisition sets a fixed price, so the stock converges to the deal value and stops moving. That is the opposite of what this strategy needs: the AH→PM pattern depends on price discovery and FOMO, and a deal price removes both. The five-day chart is a flat band between $3.5 and $4.5 with a single 1.98M-share spike on 07-23 that immediately mean-reverted.

**Rule change to propose:** an all-cash acquisition/buyout of the traded company is **not** a Grade A catalyst. Grade A means an operational catalyst that expands the range of future outcomes (partnership, contract, FDA event). A cash buyout collapses that range to one number. Treat cash-buyout targets as Grade D (exit at first PM opportunity) or skip at screening.

**Actions taken:**
- DOMO sell confirmed filled @ $3.55 (order fadb7c40)
- OPEN_POSITIONS.md: DOMO moved to Closed Positions, Current Positions now empty
- Account: equity $99,902.63, cash $99,902.63, no positions

**Realized today (all three exits):** INLF +$16.94, BZFD -$0.76, DOMO -$9.25 → **+$6.93 net**

**For the daily email:**
- Flat going into tonight. All three positions closed; day net +$6.93.
- INLF was the strategy working as designed: AH build → PM continuation → +18.7% on real liquidity.
- The DOMO trade is closed at -9.4%. Recommend adopting the rule above (cash-buyout targets are not Grade A). Juan's 07-24 call was correct and the extra four days of holding cost about 4 points versus selling then.

---

## Scan 21:30 CET (3:30 PM ET) — regular session, watch only

**No entries this pulse.** Market is still open (close 16:00 ET). The after-hours
screener returns `AH Chg +0.0% / AH Vol 0 / VRatio 0.0` for every name because
TradingView's `postmarket_*` fields are empty until after the close. Per the
regular-session caution rule, candidates are flagged **Watch — pending AH
confirmation** and only become entry-eligible if they reappear in an AH scan
(22:00+ CET) with sustained momentum.

### Regular-session movers (day% >= 15, listed exchanges)

| Ticker | Chart | Prev Close | Now | Day% | HOD | HOD Time (ET) | Off HOD | Float | Day Vol | Industry |
|--------|-------|-----------|-----|------|-----|---------------|---------|-------|---------|----------|
| EGG  | [TV](https://www.tradingview.com/chart/?symbol=EGG)  | $2.05 | $3.90 | +90.2% | $7.26 | 10:15 | -46.3% | 8.3M | 19.0M | Misc Commercial Services |
| BIYA | [TV](https://www.tradingview.com/chart/?symbol=BIYA) | $4.17 | $6.55 | +57.1% | $6.82 | 15:00 | **-4.0%** | 2.7M | 28.5M | Personnel Services |
| INLF | [TV](https://www.tradingview.com/chart/?symbol=INLF) | $3.28 | $4.87 | +48.5% | $8.18 | 10:30 | -40.5% | 1.0M | 31.5M | Industrial Machinery |
| CNET | [TV](https://www.tradingview.com/chart/?symbol=CNET) | $1.00 | $1.29 | +29.0% | $1.48 | 09:45 | -12.8% | 3.0M | 972K | Advertising/Marketing |
| STFS | [TV](https://www.tradingview.com/chart/?symbol=STFS) | $3.04 | $3.62 | +19.1% | $8.55 | 12:30 | -57.7% | 1.1M | 2.2M | Advertising/Marketing |
| LHSW | [TV](https://www.tradingview.com/chart/?symbol=LHSW) | $2.31 | $2.82 | +22.1% | $2.85 | 15:00 | **-1.2%** | 1.0M | 196K | Computer Processing Hardware |
| WLDS | [TV](https://www.tradingview.com/chart/?symbol=WLDS) | $3.18 | $3.85 | +21.2% | $5.28 | — | -27.0% | 2.0M | 7.8M | Electronic Equipment |
| PSQH | [TV](https://www.tradingview.com/chart/?symbol=PSQH) | $3.08 | $3.72 | +20.8% | $4.77 | — | -22.0% | 2.7M | 193K | Financial Conglomerates |
| SGLY | [TV](https://www.tradingview.com/chart/?symbol=SGLY) | $4.01 | $4.79 | +19.5% | $5.00 | 13:00 | **-4.2%** | n/a | 54K | Air Freight/Couriers |
| AMSS | [TV](https://www.tradingview.com/chart/?symbol=AMSS) | $0.86 | $1.01 | +18.4% | $1.30 | 13:45 | -21.9% | 3.5M | 772K | Food Distributors |
| WBUY | [TV](https://www.tradingview.com/chart/?symbol=WBUY) | $0.76 | $0.89 | +17.2% | $0.97 | — | -8.5% | 2.5M | 18.4M | Food Retail |
| POLA | [TV](https://www.tradingview.com/chart/?symbol=POLA) | $1.47 | $1.72 | +16.7% | $2.36 | 10:00 | -27.3% | 2.8M | 4.8M | Electronic Equipment |
| NOMA | [TV](https://www.tradingview.com/chart/?symbol=NOMA) | $2.92 | $3.40 | +16.4% | — | — | — | 5.6M | 7K | Movies/Entertainment |
| ANY  | [TV](https://www.tradingview.com/chart/?symbol=ANY)  | $1.95 | $2.25 | +15.6% | $2.30 | — | -1.9% | 6.0M | 1.5M | IT Services |
| MATH | [TV](https://www.tradingview.com/chart/?symbol=MATH) | $0.82 | $0.94 | +14.6% | $1.00 | — | -6.0% | 27.5M | 34K | Air Freight/Couriers |

### Shape read — who is a real AH watch

The useful signal at 15:30 ET is **position relative to the day high**, since a
name that spikes at 10:00 and bleeds all day has already spent its move and
maps onto the SPIKE→FADE bucket that is 0/10+ for PM continuation. A name
grinding into the close near HOD is the regular-session analogue of the BUILD
pattern.

**Tier 1 — building into the close (primary AH watch):**
- **BIYA** — the standout. Opened at the day low ($4.03), ground higher all
  session, HOD $6.82 at 15:00 ET, currently -4.0% off it with the last four
  15-min closes rising monotonically (6.36 → 6.43 → 6.49 → 6.55). Float 2.7M
  against 28.5M shares traded = ~10x float turnover. This is the only name of
  the fifteen making its high in the final hour on expanding volume.
- **LHSW** — HOD $2.85 at 15:00 ET, -1.2% off it. Float 1.0M. Much thinner
  (196K day volume) so AH liquidity is the open question.
- **SGLY** — -4.2% off HOD, holding. Very thin (54K day volume); expect a
  no-AH-book problem.

**Tier 2 — mild fade, still in range:** ANY (-1.9%, but flat rather than
building, and ANY is a prior loser at -21.3%), WBUY (-8.5%), MATH (-6.0%),
CNET (-12.8%, peaked 09:45 which is the earliest peak in the group).

**Tier 3 — deep fade, disqualified as "hold" (>20% off HOD):** EGG (-46.3%),
INLF (-40.5%), STFS (-57.7%), POLA (-27.3%), WLDS (-27.0%), PSQH (-22.0%),
AMSS (-21.9%). EGG's +90.2% day% headline is misleading: it printed $7.26 at
10:15 and has spent five hours giving back half of it. Same story for INLF
($8.18 at 10:30 → $4.87) and STFS ($8.55 → $3.62). A rebuild to a base more
than 20% below the high is a faded spike, not a hold (SKYQ precedent).

### Tradability (checked early, carried forward)

All nine names checked return `tradable=true`: EGG, BIYA, INLF, STFS, LHSW,
POLA, CNET, WLDS, SGLY. No broker blocks to carry tonight.

### Catalyst prep (partial — re-run at AH scans)

- **BIYA** — no same-day catalyst found. Background: 1-for-10 reverse split
  effective 2026-07-10 cut the share count 26.99M → 2.70M, which is why the
  float is so small; the older story is a crypto-treasury pivot ("Binance
  Plan", $1M strategic BNB position, May 2026). The +57% on 10x float turnover
  with no news reads as a low-float squeeze rather than a news move. Provisional
  grade **None**. Re-run the structured search at 22:00/22:30 — post-close PRs
  frequently land 4:00-4:05 PM ET.
- **LHSW** — nothing found. Provisional **None**.
- **EGG** — Enigmatig Limited (NYSE American), cross-border business services,
  Singapore. No same-day release surfaced. Moot for now given the -46% fade.

### Notes on repeat names

- **INLF** was this morning's exit (sold $4.89, +18.7% on the 07-27 entry). It
  is back on the list at +48.5% but as a spent spike, -40.5% off an $8.18 high
  set at 10:30 ET. Per the one-entry-per-candidate-per-night rule this is a new
  night, so it is technically eligible, but the shape disqualifies it.
- **CNET** and **ANY** are both prior losers in the log (early-peak fades).
  Noted for pattern tracking, not auto-skipped.

### Plan for the AH pulses

The 22:00 and 22:15 scans are observation-only under the learning-phase rule;
entries start at 23:00 CET. Watch order into the AH open: **BIYA** first
(needs to hold >10% AH across two AH scans and keep a real two-sided book),
then LHSW and SGLY subject to the `quote` liquidity check — both are thin
enough that an `ask $0.00 x0` book is a live risk. Everything in Tier 3 needs
a fresh AH ignition to come back into consideration; a continued grind lower
is disqualifying.

## Scan 22:00 CET (4:00 PM ET) — AH open, observation only

**No entries this pulse.** Two reasons, both structural rather than judgment
calls: (1) the learning-phase rule bars entries before 23:00 CET, and (2) at
exactly 16:00 ET there is no after-hours data of any kind yet.

### Main AH screener

```
AFTER-HOURS Scan: 2026-07-28 16:00:16 ET  |  0 hits
```

Expected. TradingView's `postmarket_*` fields stay empty until ~16:30 ET, so the
main screener is blind for the first half hour after the close.

### Day-movers pre-seed (log-only)

`scripts/scan.py --day-movers --session afterhours` — 18 hits, day% >= 15,
listed exchanges. Instrumentation only (Initiative 3), not a candidate source.

| Ticker | Chart | Close | Day% | Float | AvgVol | Industry | Spike-bar verdict |
|--------|-------|-------|------|-------|--------|----------|-------------------|
| EGG  | [TV](https://www.tradingview.com/chart/?symbol=EGG)  | $4.02 | +96.1% | 8.3M | 2.1M | Misc Commercial Services | no data |
| INLF | [TV](https://www.tradingview.com/chart/?symbol=INLF) | $4.95 | +50.9% | 1.0M | 8.9M | Industrial Machinery | no data |
| BIYA | [TV](https://www.tradingview.com/chart/?symbol=BIYA) | $6.26 | +50.1% | 2.7M | 23.8M | Personnel Services | no data |
| CNET | [TV](https://www.tradingview.com/chart/?symbol=CNET) | $1.39 | +39.0% | 3.0M | 980K | Advertising/Marketing | no data |
| RYOJ | [TV](https://www.tradingview.com/chart/?symbol=RYOJ) | $5.11 | +34.5% | 2.3M | 45K | Medical/Nursing Services | no data |
| STFS | [TV](https://www.tradingview.com/chart/?symbol=STFS) | $3.83 | +26.0% | 1.1M | 390K | Advertising/Marketing | no data |
| APUS | [TV](https://www.tradingview.com/chart/?symbol=APUS) | $7.67 | +21.9% | n/a | 14K | Biotechnology | no data |
| AMSS | [TV](https://www.tradingview.com/chart/?symbol=AMSS) | $1.04 | +21.9% | 3.5M | 792K | Food Distributors | no data |
| LHSW | [TV](https://www.tradingview.com/chart/?symbol=LHSW) | $2.79 | +20.6% | 1.0M | 197K | Computer Processing Hardware | no data |
| PSQH | [TV](https://www.tradingview.com/chart/?symbol=PSQH) | $3.70 | +20.3% | 2.7M | 197K | Financial Conglomerates | no data |
| WLDS | [TV](https://www.tradingview.com/chart/?symbol=WLDS) | $3.79 | +19.2% | 2.0M | 7.8M | Electronic Equipment | no data |
| WBUY | [TV](https://www.tradingview.com/chart/?symbol=WBUY) | $0.89 | +17.1% | 2.5M | 18.4M | Food Retail | no data |
| NOMA | [TV](https://www.tradingview.com/chart/?symbol=NOMA) | $3.40 | +16.4% | 5.6M | 7K | Movies/Entertainment | no data |
| SGLY | [TV](https://www.tradingview.com/chart/?symbol=SGLY) | $4.66 | +16.2% | n/a | 55K | Air Freight/Couriers | no data |
| PCSA | [TV](https://www.tradingview.com/chart/?symbol=PCSA) | $3.00 | +15.8% | 2.3M | 78K | Pharmaceuticals: Major | no data |
| FIRY | [TV](https://www.tradingview.com/chart/?symbol=FIRY) | $9.67 | +15.7% | 8.1M | 2.2M | Data Processing Services | no data |
| ANY  | [TV](https://www.tradingview.com/chart/?symbol=ANY)  | $2.25 | +15.6% | 6.0M | 1.5M | IT Services | no data |
| RPGL | [TV](https://www.tradingview.com/chart/?symbol=RPGL) | $1.95 | +15.4% | 1.1M | 128K | IT Services | no data |

New vs the 21:30 regular-session list: **RYOJ** (+34.5%, 2.3M float, avg vol only
45K — a 100x+ relative-volume day), **APUS**, **PCSA**, **FIRY**, **RPGL**. EGG,
INLF and BIYA all closed higher than their 15:30 marks, so the closing half hour
was bought rather than sold.

### Spike-bar detector unavailable at this hour (tooling note)

`node scripts/spike-bar.js SYM:2026-07-28 --now 16:00` returned ERROR for all ten
names tested. Root cause is not the script:

```
node scripts/broker.js bars BIYA --tf 1Min --start 2026-07-28T20:00:00Z --feed sip
→ ERROR: 403 Forbidden: subscription does not permit querying recent SIP data
```

The free tier blocks the most recent ~15 minutes of SIP, and at 16:00 ET the
entire after-hours window *is* that blocked period. The IEX fallback returns
`no bars` because nothing has printed yet. Yahoo `--ah-history` still serves
**2026-07-27** data, not today's.

`spike-bar.js` hard-codes `--feed sip` and surfaces the 403 as a generic
`ERROR Command failed`, which hides the cause. Two takeaways for the toolchain:
the detector cannot produce a reading before roughly 16:20 ET regardless of the
name, and its error message should distinguish "403 blocked window" from "no
ignition". Filed as an observation, not fixed in this pulse.

### Books at the close

`broker.js quote` at 20:00:00Z — first-second-of-AH spreads, all provisional:

| Ticker | Bid | Ask | Read |
|--------|-----|-----|------|
| BIYA | $5.59 x100 | $7.30 x100 | Two-sided but 27% wide |
| SGLY | $3.62 x100 | $5.68 x100 | Two-sided, very wide |
| RYOJ | $4.21 x100 | $5.85 x100 | Two-sided, very wide |
| APUS | $6.57 x100 | $9.12 x100 | Two-sided, very wide |
| FIRY | $8.49 x100 | $11.27 x100 | Two-sided, very wide |
| LHSW | $2.32 x100 | **$0.00 x0** | **One-sided — no offer.** Watch for the AH-liquidity skip. |

LHSW was Tier 1 on shape at 21:30 (HOD at 15:00 ET, -1.2% off it) but its 197K
day volume was already the concern, and the missing offer at the close is the
first confirmation. If the book is still one-sided at 22:30/23:00 it is an
automatic skip under the illiquid-ramp rule (TII precedent), no matter what
VRatio prints.

### Tradability (checked early, carried forward)

`tradable=true` for all new names: RYOJ, APUS, PCSA, FIRY, RPGL, NOMA, WBUY,
AMSS. Combined with the 21:30 checks (EGG, BIYA, INLF, STFS, LHSW, POLA, CNET,
WLDS, SGLY), every name in tonight's pipeline is broker-eligible. No blocks to
carry.

### Catalyst prep (partial, re-run at 22:30)

- **RYOJ** — no same-day news found (2 searches; first hit rate-limited, retried
  on tavily). Most recent item is a shareholder letter on 2025 highlights, not
  dated today. The tell is the volume: 45K average against a +34.5% day. Provisional **None**.
- **APUS** — no same-day release surfaced; latest items are an Inscobee
  settlement and a University of Oregon program collaboration, neither dated
  today. Provisional **None**.
- **BIYA** — carried from 21:30: no catalyst, 1-for-10 reverse split 2026-07-10
  explains the 2.7M float, older BNB-treasury narrative. Provisional **None**.

Post-close PRs typically land 16:00-16:05 ET and become searchable 15-30 minutes
later, so all three get a fresh structured search at 22:30.

### Plan for 22:30

Watch order, unchanged from 21:30 with one addition: **BIYA** (best BUILD shape
into the close, 10x float turnover), then **RYOJ** (new, extreme relative volume,
needs a real book), then LHSW and SGLY subject to the liquidity check. Entries
open at 23:00 CET and require >10% AH across two AH scans.

## Scan 22:15 CET (4:15 PM ET) — AH open +15 min, observation only

**No entries this pulse.** Learning-phase rule bars entries before 23:00 CET, and
the main AH screener is still blind. But unlike 22:00, the verification stack now
works, so this pulse produces the night's first real after-hours data.

### Main AH screener

```
AFTER-HOURS Scan: 2026-07-28 16:15:16 ET  |  0 hits
```

Still zero. TradingView's `postmarket_*` fields remain empty 15 minutes after the
close — `AH Chg +0.0% / AH Vol 0 / VRatio 0.0` across every name. Consistent with
the ~16:30 ET fill-in observed on prior nights.

### Day-movers pre-seed (log-only)

`scripts/scan.py --day-movers --session afterhours` — 16 hits. Instrumentation
(Initiative 3), not a candidate source. Spike-bar verdicts as-of 16:15 ET.

| Ticker | Chart | Close | Day% | Float | AvgVol | Industry | Spike-bar verdict |
|--------|-------|-------|------|-------|--------|----------|-------------------|
| EGG  | [TV](https://www.tradingview.com/chart/?symbol=EGG)  | $3.88 | +89.3% | 8.3M | 2.1M | Misc Commercial Services | `NO-SPIKE peak +3% @16:00ET` |
| INLF | [TV](https://www.tradingview.com/chart/?symbol=INLF) | $5.24 | +59.8% | 1.0M | 9.0M | Industrial Machinery | `NO-SPIKE flat/faded (peak <= base)` |
| BIYA | [TV](https://www.tradingview.com/chart/?symbol=BIYA) | $6.43 | +54.2% | 2.7M | 23.9M | Personnel Services | `NO-SPIKE peak +1% @16:00ET` |
| CNET | [TV](https://www.tradingview.com/chart/?symbol=CNET) | $1.43 | +43.0% | 3.0M | 989K | Advertising/Marketing | `NO-SPIKE peak +1% @16:00ET` |
| RYOJ | [TV](https://www.tradingview.com/chart/?symbol=RYOJ) | $4.93 | +29.7% | 2.3M | 52K | Medical/Nursing Services | `NO-SPIKE peak +2% @16:00ET` |
| APUS | [TV](https://www.tradingview.com/chart/?symbol=APUS) | $8.00 | +27.2% | n/a | 15K | Biotechnology | `NO-SPIKE flat/faded (peak <= base)` |
| AMSS | [TV](https://www.tradingview.com/chart/?symbol=AMSS) | $1.07 | +24.8% | 3.5M | 805K | Food Distributors | not run |
| **DCX** | [TV](https://www.tradingview.com/chart/?symbol=DCX) | $0.91 | +24.3% | 2.1M | 65K | Motor Vehicles | not run (**new**) |
| PSQH | [TV](https://www.tradingview.com/chart/?symbol=PSQH) | $3.75 | +21.6% | 2.7M | 201K | Financial Conglomerates | not run |
| LHSW | [TV](https://www.tradingview.com/chart/?symbol=LHSW) | $2.77 | +19.7% | 1.0M | 198K | Computer Processing Hardware | not run |
| PCSA | [TV](https://www.tradingview.com/chart/?symbol=PCSA) | $3.08 | +18.9% | 2.3M | 82K | Pharmaceuticals: Major | not run |
| STFS | [TV](https://www.tradingview.com/chart/?symbol=STFS) | $3.60 | +18.4% | 1.1M | 395K | Advertising/Marketing | not run |
| WBUY | [TV](https://www.tradingview.com/chart/?symbol=WBUY) | $0.90 | +18.4% | 2.5M | 18.4M | Food Retail | not run |
| **ONMD** | [TV](https://www.tradingview.com/chart/?symbol=ONMD) | $0.72 | +18.4% | 16.4M | 840K | Packaged Software | not run (**new**) |
| WLDS | [TV](https://www.tradingview.com/chart/?symbol=WLDS) | $3.71 | +16.7% | 2.0M | 7.8M | Electronic Equipment | not run |
| FIRY | [TV](https://www.tradingview.com/chart/?symbol=FIRY) | $9.75 | +16.6% | 8.1M | 2.2M | Data Processing Services | not run |

Churn vs the 22:00 pre-seed: **DCX** and **ONMD** entered; NOMA, SGLY, ANY and
RPGL dropped out. Note the day% figures keep drifting because the pre-seed reads
the last print, which in AH is a post-close trade — EGG shows $3.88 here vs $4.02
at 22:00, i.e. it gave back part of the close.

### Spike-bar detector: first usable readings of the night

The 22:00 pulse recorded the detector as unavailable (403 on the blocked recent
SIP window). At 16:15 ET it works — the free-tier block had rolled far enough
forward to expose the 16:00 ET bar. **Practical availability is ~16:15 ET, not
16:20+.** Every name returns NO-SPIKE with peaks of +1% to +3%: no after-hours
ignition anywhere in the first 15 minutes. INLF and APUS read `flat/faded (peak
<= base)`, meaning they are trading *below* their 16:00 base.

### SIP after-hours bars — 16:00-16:05 ET (the only bar served yet)

`broker.js bars SYM --tf 5Min --start 2026-07-28T20:00:00Z`

| Ticker | O → C | High | Vol | Trades | VWAP | Read |
|--------|-------|------|-----|--------|------|------|
| BIYA | $6.44 → $6.21 | $6.79 | 244,658 | 2,186 | $6.44 | Real liquidity, **faded inside the bar** (-3.6%) |
| INLF | $5.30 → $5.04 | $5.30 | 77,065 | 712 | $5.13 | Opened at the high, sold off |
| ONMD | $0.70 → $0.71 | $0.72 | 59,147 | 79 | $0.71 | Big size / 79 trades = block prints, not retail flow |
| EGG  | $3.81 → $4.00 | $4.02 | 35,136 | 289 | $3.92 | **Only name closing the bar up** (+5.0%) |
| CNET | $1.40 → $1.26 | $1.42 | 28,613 | 127 | $1.32 | -10% inside the bar |
| DCX  | $0.90 → $0.86 | $0.98 | 22,631 | 98 | $0.90 | Thin, choppy |
| RYOJ | $4.99 → $4.86 | $5.08 | 4,752 | 155 | $4.99 | Very thin despite the +29.7% day |

BIYA has by far the best real AH liquidity (2,186 trades in five minutes), which
matters because it was the 21:30 Tier-1 pick on shape. But the direction is
wrong: it opened AH at $6.44, printed $6.79, and closed the bar at $6.21. First-bar
fade, not first-bar ignition.

### Books at 16:15 ET

| Ticker | Bid | Ask | Quote time | Read |
|--------|-----|-----|-----------|------|
| **EGG** | $4.15 x100 | $4.44 x100 | **20:13:57Z** | **Fresh** and only ~7% wide — the tightest, most current book of the night |
| BIYA | $5.59 x100 | $7.30 x100 | 20:00:00Z | Stale close snapshot |
| RYOJ | $4.21 x100 | $5.85 x100 | 20:00:00Z | Stale |
| APUS | $6.57 x100 | $9.12 x100 | 20:00:00Z | Stale |
| FIRY | $8.49 x100 | $11.27 x100 | 20:00:00Z | Stale |
| DCX | $0.72 x100 | $1.07 x100 | 20:00:00Z | Stale, 49% wide |
| ONMD | $0.59 x100 | $0.82 x100 | 20:00:00Z | Stale, 39% wide |
| **INLF** | $4.49 x100 | **$0.00 x0** | 20:00:02Z | **One-sided — no offer** |
| **CNET** | $1.21 x100 | **$0.00 x0** | 20:00:01Z | **One-sided — no offer** |
| **LHSW** | $2.32 x100 | **$0.00 x0** | 20:00:05Z | **One-sided, 2nd consecutive scan** |

**LHSW is now a carried skip.** It showed no offer at 22:00 and still shows none
at 22:15. Under the illiquid-ramp rule (TII precedent) a one-sided book means any
VRatio it eventually prints is a stale regular-session artifact. It was Tier 1 on
shape at 21:30 (HOD at 15:00 ET, -1.2% off) and is being disqualified purely on
liquidity — worth noting as a shape-vs-fillability divergence. INLF and CNET join
it as no-offer books for now.

### Catalyst work

- **BIYA** — re-ran the structured search now that the 16:00-16:05 PR window has
  passed. **Still nothing same-day.** Most recent GlobeNewswire item is the
  1-for-10 reverse-split record date (2026-07-08); prior item is a Sept 2025
  corporate release. Confirms **Grade None**. The +54% on ~10x float turnover is a
  low-float squeeze, and the reverse split from 26.99M → 2.70M shares three weeks
  ago is the mechanical reason the float is small enough to squeeze.
- **EGG** — no same-day catalyst (1 search; first attempt hit HTTP 429, retried on
  tavily). **Grade None.** But the daily history reframes the name entirely —
  see below.

### EGG is a multi-day bounce, not a fresh mover

Yahoo daily bars, last 10 sessions:

| Date | Open | High | Low | Close | Volume |
|------|------|------|-----|-------|--------|
| ...07-20 → 07-23 | ~$7.2 | ~$7.5 | ~$6.9 | $7.09-7.49 | 6K-122K |
| 2026-07-24 | $6.96 | $9.09 | $6.15 | $6.40 | 161K |
| 2026-07-27 | $5.20 | $5.59 | **$2.05** | **$2.05** | 535K |
| 2026-07-28 | $2.04 | $7.26 | $2.31 | $3.81 | **19.56M** |

EGG collapsed **-68% yesterday** ($6.40 → $2.05) and today's headline +89.3% is a
bounce off that crash, not new momentum. It also spiked to $7.26 at 10:15 ET and
gave back 46% of it during the session. The dead-cat filter keys on *same-day*
Day% ≤ -15%, so EGG's +89% does not trip it — but the multi-day structure is
exactly the pattern the filter exists to avoid, one session displaced. Flagging
this as a **filter-scope observation**: the dead-cat rule's same-day window misses
next-day bounces off a crash. Not proposing a rule change on one case; recording it
so the morning eval can check whether EGG follows through or dies in PM.

Its one genuinely attractive feature is the book: a fresh, 7%-wide two-sided quote
at 16:14 ET while everything else is stale or one-sided. Good fillability on a bad
setup.

### Read going into 22:30

Nothing qualifies and nothing is close. The night's shape so far:

- **No after-hours ignition exists yet.** Every spike-bar reads NO-SPIKE, the best
  AH price action is EGG's +5% inside one 5-minute bar, and the two highest-day%
  names (BIYA, INLF) both faded inside their first AH bar.
- **The 21:30 Tier-1 thesis is not confirming.** BIYA had the liquidity but sold
  off from the AH open; LHSW is disqualified on a missing offer; SGLY dropped out
  of the pre-seed entirely.
- Everything on the board is currently a **Grade None** regular-session carryover.
  Under the entry rules a candidate still needs >10% *after-hours* change across
  two AH scans, and the AH change counter has not started for any name.

Watch order for 22:30, when the TradingView postmarket fields should populate:
**BIYA** (does the first-bar fade continue or base?), **EGG** (best book, worst
structure — needs to reclaim toward $4.44+ on real trades to be interesting),
**RYOJ** (extreme relative volume but only 4.7K AH shares so far). DCX and ONMD
get first spike-bar and catalyst reads at 22:30 if they hold their day%.

## Scan 22:30 CET (4:30 PM ET) — first real AH data, observation only

**No entries this pulse** — the learning-phase rule bars entries before 23:00 CET.
But the night changed character completely at 16:30 ET: TradingView's
`postmarket_*` fields populated on schedule, the screener went from 0 hits to 6,
and the spike-bar detector fired **real ignition bars on four names**. The 22:15
read ("no after-hours ignition exists anywhere") is obsolete.

### Main AH screener

```
AFTER-HOURS Scan: 2026-07-28 16:30:16 ET  |  6 hits
```

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| **AMIX** | [TV](https://www.tradingview.com/chart/?symbol=AMIX) | $2.75 | -1.4% | **+52.7%** | $4.20 | +50.5% | 1.5M | 1.2M | 1.3x | **502K** | Medical Specialties |
| SBNYL | [TV](https://www.tradingview.com/chart/?symbol=SBNYL) | $1.20 | +0.0% | +45.8% | $1.75 | +45.8% | 30K | 11K | 2.7x | 59.6M | Regional Banks |
| YIBO | [TV](https://www.tradingview.com/chart/?symbol=YIBO) | $1.15 | -2.5% | +22.6% | $1.41 | +19.5% | 178K | 50K | 3.6x | 2.1M | Electronics/Appliances |
| IOTR | [TV](https://www.tradingview.com/chart/?symbol=IOTR) | $3.05 | +3.0% | +13.1% | $3.45 | +16.6% | 63K | 31K | 2.0x | 2.7M | IT Services |
| EGG | [TV](https://www.tradingview.com/chart/?symbol=EGG) | $3.81 | +85.9% | +9.4% | $4.17 | +103.4% | 513K | 2.1M | 0.2x | 8.3M | Misc Commercial Services |
| GIPR | [TV](https://www.tradingview.com/chart/?symbol=GIPR) | $0.70 | +7.4% | +7.8% | $0.75 | +15.8% | 91K | 1.2M | 0.1x | 928K | REIT |

Note how little the 21:30/22:00 day-movers pre-seed predicted: of the four names
with real AH ignition, only EGG was on the watch list, and it is the one behaving
worst. **AMIX, YIBO and IOTR have no regular-session footprint at all** (Day%
-1.4%, -2.5%, +3.0%) — they are pure post-close ignitions, the LGCL-shaped case
the pre-seed is structurally blind to. Tonight is a clean example of the pre-seed
being additive-only, exactly as its Initiative-3 caveat states.

### Spike-bar verdicts (instrumentation, verbatim, as-of 16:30 ET)

```
AMIX  2026-07-28  SPIKE  16:03ET  +24%  $3.40  709 trades / 55k sh  (first co-spike bar)
YIBO  2026-07-28  SPIKE  16:06ET  +25%  $1.44  170 trades / 25k sh  (first co-spike bar)
IOTR  2026-07-28  SPIKE  16:08ET  +29%  $3.93  170 trades / 21k sh  (first co-spike bar)
EGG   2026-07-28  SPIKE  16:06ET  +18%  $4.50  582 trades / 49k sh  (first co-spike bar)
SBNYL 2026-07-28: NO prior-close (daily bar missing)
```

All four ignitions landed in the **16:03-16:08 ET** window — the AH-open cluster
Initiative 3 predicts. The detector was returning NO-SPIKE on everything at 16:15
because it was reading the *watch-list* names; the actual ignitions were happening
in names the watch list never contained.

### SIP volume confirmation — the decisive split

`broker.js bars SYM --tf 5Min --start 2026-07-28T20:00:00Z`

**AMIX — accumulating on every bar, price making new highs:**

| Bar (ET) | O → C | High | Vol | Trades | VWAP |
|----------|-------|------|-----|--------|------|
| 16:00 | $2.75 → $3.20 | $3.40 | 154,216 | 1,999 | $3.22 |
| 16:05 | $3.22 → $3.49 | $3.65 | 811,540 | 8,790 | $3.48 |
| 16:10 | $3.49 → $4.20 | $4.30 | 1,013,274 | 11,757 | $3.90 |
| 16:15 | $4.20 → $4.60 | $4.85 | **1,219,927** | **13,972** | $4.57 |

Volume rising every bar (154K → 812K → 1.01M → 1.22M), trades rising every bar
(2.0K → 8.8K → 11.8K → 14.0K), price closing each bar at or near its high, and
VWAP climbing with price ($3.22 → $3.48 → $3.90 → $4.57). This is the opposite of
a stale-VRatio artifact — the scanner's 1.3x VRatio actually *understates* it,
because 3.2M AH shares have now printed against a 1.2M average daily volume.

**YIBO — real but second-tier:** 97K / 115K / 249K sh on 832 / 780 / 1,750 trades.
Accumulating, genuinely two-sided, but an order of magnitude thinner than AMIX.

**IOTR — fading:** 46K / 44K / 14K sh on 590 / 763 / 207 trades. Volume collapsing
bar over bar after the 16:08 ignition.

**EGG — fading:** 375K / 266K / 74K sh on 4,385 / 3,699 / 825 trades. Spiked to
$4.86 in the 16:05 bar, gave it back, and volume fell 80% in ten minutes.

### AH price timelines (Yahoo, shape only)

| Time (ET) | AMIX | YIBO | IOTR | EGG |
|-----------|------|------|------|-----|
| 16:00 | +14.7% | -2.5% | +4.7% | +94.8% |
| 16:05 | +24.7% | +14.3% | **+25.7%** | **+127.4%** |
| 16:10 | +50.5% | +19.5% | +16.6% | +103.4% |
| 16:15 | +64.9% | +16.9% | +10.6% | +99.5% |
| 16:20 | +64.6% | **+24.2%** | +8.4% | +98.5% |
| 16:25 | +59.5% | +12.8% | +13.5% | +94.1% |
| 16:31 | **+67.1%** (new high) | +12.7% | +13.5% | +93.8% |

### Books at 16:30 ET

| Ticker | Bid | Ask | Quote time | Read |
|--------|-----|-----|-----------|------|
| AMIX | $3.94 x100 | $4.00 x100 | 20:14:12Z | Two-sided, **1.5% spread** — tightest of the night. Timestamp lags the tape (SIP has it at $4.60+ by 20:15Z); freshness guard applies, this is staleness not contradiction. |
| YIBO | $1.31 x100 | $1.34 x100 | **20:31:32Z** | Fresh, 2.3% spread, genuinely two-sided |
| EGG | $4.03 x100 | $4.31 x100 | 20:17:49Z | Two-sided, 7% wide |
| IOTR | $2.58 x100 | $3.65 x100 | 20:00:00Z | Stale close snapshot, 41% wide |
| SBNYL | — | — | — | `404 no quote found` |

### Tradability

`tradable=true`: AMIX, YIBO, IOTR, EGG.
**`tradable=false`: SBNYL** (OTC, class us_equity, no quote available) — recorded
once as a qualified-but-untradable broker block and carried forward. Do not re-run
its workup at later scans. Its 59.6M float would have been a poor fit anyway.

### Candidate evaluation

**AMIX — lead candidate, entry-eligible at 23:00 if it holds.** Autonomix Medical,
development-stage medical device (nerve-targeted ablation, pancreatic cancer pain).

- Float **502K** — the smallest float in months of scans, and the mechanical reason
  1.2M shares in one 5-minute bar moves it 15%.
- Day% -1.4%: no dead-cat exposure, nothing to bounce off of. The entire move is
  post-close.
- Total% +50.5% at scan, ~+67% now — **well under the +150% extension ceiling**,
  which is the failure mode that killed PRFX/VCIG/ATPC/ANY. This is in the same
  band as the winners (AMST +76%, DXST +57%).
- Trajectory: **BUILD**, and still building — new AH high at 16:31 ET. Not a
  single fading bar yet.
- Catalyst: **none found** (4 searches: GlobeNewswire/IR page, StockTitan, general
  and PR-targeted queries; one 429 retried on tavily). Most recent releases are a
  Jul 13 Canadian neural-sensing patent grant and a Jul 13 $2.6M warrant inducement
  — both two weeks stale. Grade **None**, entered as a documented concern per the
  no-catalyst rule, which has produced winners across the float range (LNKS 633K,
  OCG 1.9M, PHGE 5.9M/7.4M).
- Concern worth naming: the **Jul 13 warrant inducement** means there is a recent
  dilution overhang on this name. If a same-day catalyst surfaces at 23:00 and it
  turns out to be another financing, that is Grade D and the entry is off.

**YIBO — secondary candidate.** Planet Image International, printer consumables.
Float 2.1M, VRatio 3.6x, Day% -2.5%, Total% +19.5% (very low extension). Peaked
+24.2% at 16:20 ET and sits at +12.7%, i.e. ~10% off its AH high — inside the 20%
"holding" band, so it reads as hold-not-fade, but it is drifting rather than
building. Volume is real and accumulating. No catalyst found (1 search, only
generic quote-page results). Grade **None**. Viable at 23:00 if it firms; second
in line behind AMIX.

**IOTR — skip: SPIKE→FADE.** Ignited 16:08 at $3.93, faded to $3.20-3.36, and
volume collapsed 46K → 14K across three bars. Book is a stale 41%-wide close
snapshot. This is the 0/10+ bucket; the +13.1% AH headline is the tail of a spent
spike.

**EGG — skip: SPIKE→FADE on top of a multi-day dead-cat.** Peaked +127% at 16:05,
now +93.8%, volume down 80% in ten minutes. Carried from 22:15: EGG fell -68%
yesterday ($6.40 → $2.05), so today's move is a bounce off a crash, and it already
spent a +46% intraday fade from its $7.26 high at 10:15 ET. Total% +103% is also
the highest extension on the board. Nothing here argues for an entry.

**GIPR — skip: below threshold.** AH +7.8%, under the 10% gate, VRatio 0.1x.

**SBNYL — skip: untradable.** See tradability above.

### Read going into 23:00

For the first time tonight there is a candidate that fits the winning template on
every axis that has historically mattered: micro float, BUILD trajectory still
making new highs, moderate extension, and volume accumulating on tens of thousands
of real trades rather than a handful of block prints. The one gap is the catalyst,
which the rules explicitly treat as a concern rather than a skip.

**AMIX has now cleared its first AH scan above 10%.** The two-AH-scan gate means
23:00 CET is the earliest legal entry, and it is exactly when the rules open
entries anyway — no conflict. Plan for 23:00:

1. Re-check AMIX trajectory. Enter if it is still building or holding within ~20%
   of its AH high, with a fresh two-sided book and SIP volume still accumulating.
   Size ~$100 at a limit a few cents over the ask.
2. Re-run the AMIX catalyst search once more — the 16:00-16:05 PR window is the
   likeliest source and items become searchable 15-30 min later. A financing/
   dilution find flips it to Grade D and cancels the entry.
3. Evaluate YIBO independently for a second position (multiple positions are
   allowed as of W24 2026); enter it too if it clears every gate on its own.
4. IOTR, EGG, GIPR, SBNYL stay skipped unless something structurally changes.

## Scan 22:45 CET (4:45 PM ET) — observation only

**No entries this pulse** (learning-phase rule: entries open at 23:00 CET). AMIX
cleared its second consecutive AH scan above 10%, which satisfies the two-AH-scan
gate and makes it entry-eligible at 23:00.

### Main AH screener

```
AFTER-HOURS Scan: 2026-07-28 16:45:21 ET  |  5 hits
```

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| **AMIX** | [TV](https://www.tradingview.com/chart/?symbol=AMIX) | $2.75 | -1.4% | **+61.8%** | $4.45 | +59.5% | 3.8M | 1.5M | 2.5x | **502K** | Medical Specialties |
| YIBO | [TV](https://www.tradingview.com/chart/?symbol=YIBO) | $1.15 | -2.5% | +15.7% | $1.33 | +12.7% | 1.1M | 159K | **7.1x** | 2.1M | Electronics/Appliances |
| IOTR | [TV](https://www.tradingview.com/chart/?symbol=IOTR) | $3.05 | +3.0% | +10.2% | $3.36 | +13.5% | 83K | 34K | 2.5x | 2.7M | IT Services |
| SBNYL | [TV](https://www.tradingview.com/chart/?symbol=SBNYL) | $1.20 | +0.0% | +45.8% | $1.75 | +45.8% | 30K | 11K | 2.7x | 59.6M | Regional Banks |
| **MB** | [TV](https://www.tradingview.com/chart/?symbol=MB) | $3.67 | -7.1% | +23.4% | $4.53 | +14.6% | **100** | 5K | 0.0x | 4.7M | Restaurants (**new**) |

EGG dropped out of the screener between 22:30 and 22:45 — its AH fade continued.

### Spike-bar verdicts (instrumentation, verbatim, as-of 16:45 ET)

```
AMIX 2026-07-28  SPIKE  16:03ET  +24%  $3.40  709 trades / 55k sh  (first co-spike bar)
YIBO 2026-07-28  SPIKE  16:06ET  +25%  $1.44  170 trades / 25k sh  (first co-spike bar)
IOTR 2026-07-28  SPIKE  16:08ET  +29%  $3.93  170 trades / 21k sh  (first co-spike bar)
MB   2026-07-28: NO prior-close (daily bar missing)
```

Unchanged from 22:30 — the detector reports the *first* co-spike bar, so these are
the same 16:03-16:08 ET ignitions. No new ignition fired between 16:30 and 16:45.

### SIP volume — the three names diverge cleanly

`broker.js bars SYM --tf 5Min --start 2026-07-28T20:00:00Z`

**AMIX — still accumulating heavily:**

| Bar (ET) | O → C | High | Vol | Trades | VWAP |
|----------|-------|------|-----|--------|------|
| 16:15 | $4.20 → $4.60 | $4.85 | 1,219,927 | 13,972 | $4.57 |
| 16:20 | $4.61 → $4.61 | **$4.96** | 1,076,488 | 11,877 | $4.54 |
| 16:25 | $4.59 → $4.45 | $4.61 | 566,946 | 6,163 | $4.39 |
| 16:30 | $4.45 → $4.25 | $4.72 | 737,571 | 8,295 | $4.48 |

AH high $4.96 set at 16:20 ET; price oscillating $4.18-4.72 since, i.e. **-10% off
the high, inside the 20% hold band**. Roughly 4.8M AH shares against a 1.5M average
daily volume, on tens of thousands of real trades. Not a stale-VRatio artifact.

**YIBO — volume collapsing:** 466K → 377K → 94K sh (16:20 → 16:30) on 3,285 → 2,443
→ 631 trades. Peak $1.56 at 16:20 ET, now $1.32. Real book but the flow is draining.

**IOTR — dead:** 14K → 9.6K → 1.0K → 1.1K sh per bar, 12-18 trades. The ignition is
fully spent.

**MB — one print:** a single 100-share trade at $4.53 in the 16:20 bar. The +23.4%
AH change is that one print.

### Books at 16:45 ET

| Ticker | Bid | Ask | Quote time | Read |
|--------|-----|-----|-----------|------|
| YIBO | $1.28 x100 | $1.30 x100 | **20:41:34Z** | Fresh, tight, genuinely two-sided |
| AMIX | $3.94 x100 | $4.00 x100 | 20:14:12Z | Two-sided but **stale** — SIP has it at $4.45 |
| IOTR | $2.58 x100 | $3.65 x100 | 20:00:00Z | Stale close snapshot, 41% wide |
| MB | $3.78 x100 | **$0.00 x0** | **2026-07-22**T18:23Z | Six days stale, no offer |

**Freshness guard applied to AMIX:** the quote timestamp (20:14Z) is 30 minutes
behind the scan and 45 minutes behind the SIP tape, so the "quote $4.00 vs scanner
$4.45" gap is staleness, not a bad print. SIP bars through 16:35 ET corroborate
$4.18-4.96 on 8K+ trades per bar. This is the USDE Jul 1 case and it is explicitly
not a bad-print rejection.

### Evaluation

- **AMIX** — second consecutive AH scan >10% (+52.7% → +61.8%). Two-AH-scan gate
  cleared. Catalyst search re-run (2 more searches, 6 total): still **nothing
  same-day**. Most recent items are Jul 24 preclinical renal-nerve-sensing results
  and the Jul 13 warrant inducement / patent grant. Grade **None**. Entry-eligible
  at 23:00.
- **YIBO** — AH% went +22.6% → +15.7% while per-bar volume fell 93% from its peak
  bar. Peaked 16:20 ET and declining = **SPIKE→FADE shape**. No catalyst found.
  Downgraded from "secondary candidate" to likely skip; re-check at 23:00.
- **IOTR** — carried skip, confirmed. Volume down to ~1K sh/bar.
- **MB** — **skip: no AH book.** 100 shares on one trade, `ask $0.00 x0`, quote
  timestamp six days old. Textbook stale-VRatio / illiquid ramp (TII precedent).
  `tradable=true` but there is nothing to trade against.
- **SBNYL** — untradable (carried from 22:30). No workup re-run.

## Scan 23:00 CET (5:00 PM ET) — **entry: AMIX**

Entries are open. One position taken.

### Main AH screener

```
AFTER-HOURS Scan: 2026-07-28 17:00 ET  |  8 hits
```

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| **AMIX** | [TV](https://www.tradingview.com/chart/?symbol=AMIX) | $2.75 | -1.4% | **+73.1%** | $4.76 | +70.6% | **5.4M** | 1.7M | 3.2x | **502K** | Medical Specialties |
| YIBO | [TV](https://www.tradingview.com/chart/?symbol=YIBO) | $1.15 | -2.5% | +15.7% | $1.33 | +12.7% | 1.3M | 181K | 7.3x | 2.1M | Electronics/Appliances |
| EGG | [TV](https://www.tradingview.com/chart/?symbol=EGG) | $3.81 | +85.9% | +6.8% | $4.07 | +98.5% | 740K | 2.2M | 0.3x | 8.3M | Misc Commercial Services |
| BIYA | [TV](https://www.tradingview.com/chart/?symbol=BIYA) | $6.44 | +54.4% | +6.8% | $6.88 | +65.0% | 735K | 24.0M | 0.0x | 2.7M | Personnel Services |
| IOTR | [TV](https://www.tradingview.com/chart/?symbol=IOTR) | $3.05 | +3.0% | +8.2% | $3.30 | +11.5% | 85K | 34K | 2.5x | 2.7M | IT Services |
| MGRX | [TV](https://www.tradingview.com/chart/?symbol=MGRX) | $0.56 | +2.4% | +7.9% | $0.60 | +10.5% | 67K | 552K | 0.1x | 14.6M | Pharmaceuticals: Major |
| SBNYL | [TV](https://www.tradingview.com/chart/?symbol=SBNYL) | $1.20 | +0.0% | +45.8% | $1.75 | +45.8% | 30K | 11K | 2.7x | 59.6M | Regional Banks |
| MB | [TV](https://www.tradingview.com/chart/?symbol=MB) | $3.67 | -7.1% | +23.4% | $4.53 | +14.6% | 100 | 5K | 0.0x | 4.7M | Restaurants |

EGG and BIYA reappeared but both below the 10% AH gate (+6.8% each). MGRX is new
and also below gate. Only AMIX and YIBO clear it.

### AMIX — entered

**Autonomix Medical** (NASDAQ, The Woodlands TX), development-stage medical device
company, catheter-based neural sensing and RF ablation for nerve-mediated pain.

Every gate, checked:

| Gate | Value | Pass |
|------|-------|------|
| AH >10% across ≥2 AH scans | +52.7% (22:30) → +61.8% (22:45) → +73.1% (23:00) | yes, 3 scans |
| Float | **502K** | yes (smallest float in months of scans) |
| Day% above -15% | -1.4% | yes — and no dead-cat exposure, the entire move is post-close |
| Entry extension < +150% | fill $4.02 vs $2.75 close = **+46.2%** | yes, comfortably |
| Trajectory | BUILD/HOLD — AH high $4.96 (16:20 ET), retested $4.86 (16:40 ET), currently $4.76 = **-4% off the high** | yes |
| Real AH liquidity | 5.4M AH sh vs 1.7M avg vol, 4K-14K trades per 5-min bar | yes |
| SIP corroborates price | SIP H $4.96 / vwap $4.39-4.69 matches the scanner's $4.76 | yes |
| Tradable | `tradable=true` NASDAQ | yes |
| Catalyst | **none found** (6 searches across 22:30 + 22:45) | concern, not a skip |

SIP tape at entry time:

| Bar (ET) | O → C | High | Vol | Trades | VWAP |
|----------|-------|------|-----|--------|------|
| 16:35 | $4.24 → $4.39 | $4.52 | 365,500 | 4,110 | $4.40 |
| 16:40 | $4.39 → $4.76 | $4.86 | 932,534 | 9,889 | $4.69 |
| 16:45 | $4.76 → $4.18 | $4.76 | 538,345 | 5,757 | $4.39 |
| 16:45 (1Min) | $4.76 → $4.56 | $4.76 | 101,315 | 1,237 | $4.63 |

An hour into after-hours the name is still printing half a million to a million
shares per five minutes. It has now traded roughly 3.5x its average *daily* volume
since the close, in a 502K float. Price is chopping in a $4.18-4.96 band rather
than trending down — this is a hold near the high, not a fade.

**Order:** `buy AMIX 21 --limit 4.85 --ext` → id `ce3a2383`, **filled @ $4.02**.

**Fill artifact worth flagging.** The limit was set at $4.85 to clear the live SIP
market (~$4.56-4.76), but Alpaca's paper book filled against its stale $4.00 ask
from 20:14Z. The realized entry of **$4.02** is therefore about 15% below where the
stock was actually trading at 17:00 ET. This is a paper-feed artifact, not a real
edge — a live account would have paid ~$4.65. Any P&L on this trade should be read
against a notional $4.65 entry, and the morning eval should note it rather than
counting the extra 15 points as strategy performance. (The same stale-IEX-book
mechanic has produced *worse* fills on exits before; it cuts both ways.)

**Catalyst: Grade None.** Six structured searches across two pulses found no
same-day release. The nearest items are Jul 24 (positive preclinical renal-nerve
sensing study) and Jul 13 (warrant inducement + patent grant), both stale. Grade
None means **exit at the first premarket opportunity at any profit**.

**Standing concern:** the Jul 13 warrant inducement is a recent dilution overhang.
If an offering or financing surfaces overnight, the thesis is dead and the exit
should be immediate rather than opportunistic.

### YIBO — skipped: SPIKE→FADE

Cleared the two-AH-scan gate on paper (+22.6% → +15.7% → +15.7%) and has the best
book on the board (fresh 20:59Z quote, $1.23 x100 / $1.26 x100, 2.4% spread) plus
the highest VRatio (7.3x). Skipped anyway on trajectory, which the rules say
dominates:

| Bar (ET) | Close | Vol | Trades |
|----------|-------|-----|--------|
| 16:20 | $1.47 | 466,306 | 3,285 |
| 16:25 | $1.33 | 377,575 | 2,443 |
| 16:30 | $1.32 | 94,460 | 631 |
| 16:35 | $1.27 | 66,271 | 485 |
| 16:40 | $1.33 | 50,938 | 299 |
| 16:45 | $1.30 | 32,372 | 265 |

Peak $1.56 at 16:20 ET, then six consecutive bars of declining volume — down 93%
from the peak bar, trades down 92%. Price is only -15% off the high, so it is
technically inside the 20% band, but the hold-vs-fade test is about whether flow
is still arriving, and here it has stopped. Early peak (16:20 ET, well before the
18:30 benchmark) plus draining volume is the SPIKE→FADE profile that is 0/10+ for
premarket continuation. No catalyst found either.

### Other skips

- **EGG** (+6.8% AH) and **BIYA** (+6.8% AH) — below the 10% gate. Both were 21:30
  watch names; both spent their move in the regular session. EGG additionally
  carries the multi-day dead-cat structure documented at 22:15 (-68% on 07-27).
- **IOTR** (+8.2%) — fell below the gate as well; volume ~1K sh/bar. Spent spike.
- **MGRX** (+7.9%) — below gate, VRatio 0.1x.
- **MB** (+23.4%) — no AH book. 100 shares on a single print; quote `ask $0.00 x0`
  timestamped 2026-07-22. Stale-VRatio artifact.
- **SBNYL** (+45.8%) — untradable (carried from 22:30, no workup re-run).

### Night summary so far

The pre-seed instrumentation was again structurally blind to the actual winner
shape: AMIX, YIBO and IOTR all have flat regular-session tape (Day% -1.4%, -2.5%,
+3.0%) and only ignited after the close, in the 16:03-16:08 ET cluster Initiative 3
predicts. Every 21:30 Tier-1 pick (BIYA, LHSW, SGLY) failed — BIYA faded below the
gate, LHSW was disqualified on a two-scan one-sided book, SGLY dropped out
entirely. The watch list contributed zero candidates; the screener contributed all
of them.

## Scan 23:30 CET (5:30 PM ET) — no new entry (two-AH-scan gate)

**No new entries this pulse.** A second, distinct ignition cluster fired at
**16:59 ET** — ninety minutes after the AH-open cluster — producing two fresh
names (ONMD, GMM). ONMD is the strongest BUILD of the night on live tape and is
making new after-hours highs as this scan runs, but it appears in the AH screener
above 10% for the **first time** here. The two-AH-scan gate makes 00:00 CET its
earliest legal entry. AMIX (entered 23:00) is unchanged in position terms;
hold/sell is the premarket pulse's call.

### Main AH screener

```
AFTER-HOURS Scan: 2026-07-28 17:30:15 ET  |  12 hits
```

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| AMIX | [TV](https://www.tradingview.com/chart/?symbol=AMIX) | $2.75 | -1.4% | +46.9% | $4.04 | +44.8% | **7.0M** | 1.9M | 3.7x | 502K | Medical Specialties |
| **ONMD** | [TV](https://www.tradingview.com/chart/?symbol=ONMD) | $0.71 | +17.0% | **+25.5%** | $0.89 | +46.9% | 1.8M | 1.0M | 1.7x | 16.4M | Packaged Software (**new**) |
| YIBO | [TV](https://www.tradingview.com/chart/?symbol=YIBO) | $1.15 | -2.5% | +7.8% | $1.24 | +5.1% | 1.5M | 201K | 7.5x | 2.1M | Electronics/Appliances |
| EGG | [TV](https://www.tradingview.com/chart/?symbol=EGG) | $3.81 | +85.9% | +12.5% | $4.28 | +109.0% | 801K | 2.2M | 0.4x | 8.3M | Misc Commercial Services |
| **GMM** | [TV](https://www.tradingview.com/chart/?symbol=GMM) | $2.47 | -8.5% | +19.8% | $2.96 | +9.6% | 466K | 3.0M | 0.2x | 1.7M | Packaged Software (**new**) |
| DXST | [TV](https://www.tradingview.com/chart/?symbol=DXST) | $2.24 | -0.9% | +5.8% | $2.37 | +4.9% | 116K | 2.6M | 0.0x | 1.2M | Environmental Services |
| IOTR | [TV](https://www.tradingview.com/chart/?symbol=IOTR) | $3.05 | +3.0% | +5.9% | $3.23 | +9.1% | 89K | 35K | 2.6x | 2.7M | IT Services |
| MGRX | [TV](https://www.tradingview.com/chart/?symbol=MGRX) | $0.56 | +2.4% | +7.8% | $0.60 | +10.4% | 68K | 552K | 0.1x | 14.6M | Pharmaceuticals: Major |
| NNOX | [TV](https://www.tradingview.com/chart/?symbol=NNOX) | $0.88 | -0.9% | +6.0% | $0.93 | +5.0% | 62K | 1.1M | 0.1x | 64.1M | Medical Specialties |
| APUS | [TV](https://www.tradingview.com/chart/?symbol=APUS) | $8.00 | +27.2% | +5.8% | $8.46 | +34.5% | 54K | 22K | 2.5x | n/a | Biotechnology |
| SBNYL | [TV](https://www.tradingview.com/chart/?symbol=SBNYL) | $1.20 | +0.0% | +45.8% | $1.75 | +45.8% | 30K | 11K | 2.7x | 59.6M | Regional Banks |
| MB | [TV](https://www.tradingview.com/chart/?symbol=MB) | $3.67 | -7.1% | +23.4% | $4.53 | +14.6% | 100 | 5K | 0.0x | 4.7M | Restaurants |

Above the 10% AH gate: AMIX (open position), ONMD, EGG, GMM, MB (no book), SBNYL
(untradable). YIBO fell out at +7.8%; IOTR, MGRX, APUS, DXST, NNOX all below gate.

### Spike-bar verdicts (instrumentation, verbatim, as-of 17:30 ET)

```
ONMD 2026-07-28  SPIKE  16:59ET  +20%  $0.85  161 trades / 52k sh  (first co-spike bar)
GMM  2026-07-28  SPIKE  16:59ET  +38%  $3.41  675 trades / 82k sh  (first co-spike bar)
AMIX 2026-07-28  SPIKE  16:03ET  +24%  $3.40  709 trades / 55k sh  (first co-spike bar)
EGG  2026-07-28  SPIKE  16:06ET  +18%  $4.50  582 trades / 49k sh  (first co-spike bar)
```

**The night has two ignition clusters, not one.** The Initiative-3 hypothesis
centres on the 16:03-16:08 ET AH-open cluster, and that fired on schedule (AMIX,
YIBO, IOTR, EGG). But ONMD and GMM both ignited at **16:59 ET** — the same minute,
90 minutes later, in two unrelated names. A single-window watch would have missed
both. Recording it as an Initiative-3 data point: the AH-open cluster is where
ignitions concentrate, not where they exclusively occur, and the second cluster
produced the better-shaped candidate.

### SIP volume — ONMD is the night's cleanest accumulation

`broker.js bars ONMD --tf 5Min --start 2026-07-28T20:00:00Z`

| Bar (ET) | O → C | High | Vol | Trades | VWAP |
|----------|-------|------|-----|--------|------|
| 16:40 | $0.69 → $0.69 | $0.69 | 1,343 | 6 | $0.69 |
| 16:50 | $0.72 → $0.73 | $0.73 | 10,091 | 24 | $0.72 |
| 16:55 | $0.73 → $0.78 | $0.85 | 94,193 | 294 | $0.78 |
| 17:00 | $0.79 → $0.76 | $0.80 | 80,522 | 307 | $0.78 |
| 17:05 | $0.79 → $0.85 | $0.89 | 501,243 | 1,235 | $0.85 |
| 17:10 | $0.87 → $0.89 | **$0.92** | **1,052,556** | **3,182** | $0.88 |
| 17:15 | $0.89 → $0.84 | $0.92 | 850,386 | 2,417 | $0.87 |

1Min tape through 17:16 ET, which is where the scan sits:

| Min (ET) | O → C | High | Vol | Trades |
|----------|-------|------|-----|--------|
| 17:12 | $0.89 → $0.91 | $0.91 | 329,723 | 878 |
| 17:13 | $0.91 → $0.89 | $0.92 | 248,854 | 888 |
| 17:14 | $0.89 → $0.89 | $0.91 | 165,208 | 617 |
| 17:15 | $0.89 → $0.90 | $0.91 | 150,221 | 465 |
| 17:16 | $0.90 → $0.91 | **$0.92** | 212,771 | 541 |

The stock is at its after-hours high *right now*, printing 150K-330K shares per
minute on 465-888 trades per minute. The scanner's $0.89 AH price understates the
tape ($0.91). This is real, two-sided, accumulating flow — not a stale-VRatio
artifact, and the 1.7x VRatio badly undersells it (1.8M+ AH shares against a 1.0M
average daily volume, and rising every bar).

**GMM — SPIKE→FADE, textbook:**

| Bar (ET) | O → C | High | Vol | Trades |
|----------|-------|------|-----|--------|
| 16:55 | $2.73 → $3.29 | $3.41 | 83,513 | 677 |
| 17:00 | $3.29 → $3.27 | **$3.64** | 309,007 | 3,280 |
| 17:05 | $3.28 → $3.00 | $3.28 | 154,574 | 1,723 |
| 17:10 | $3.00 → $2.98 | $3.04 | 44,754 | 462 |
| 17:15 | $2.96 → $2.98 | $3.04 | 21,909 | 232 |

Peak $3.64 at 17:00 ET, then three consecutive bars of collapsing volume (down 93%
from the peak bar, trades down 93%) with price -18% off the high. Same ignition
minute as ONMD, opposite outcome fifteen minutes later.

**EGG — grinding but thin:** 11.7K / 14.2K / 11.5K / 7.9K / 17.3K / 16.7K / 13.2K
sh per bar on 106-184 trades, price $4.02 → $4.29. Genuinely rising, but at ~1%
of the volume ONMD is doing, against a 2.2M average daily volume (VRatio 0.4x).

**YIBO — dead:** 30K → 11.9K → 6.5K → 10.8K sh on 147 → 70 → 60 → 86 trades.
Confirms the 23:00 skip.

### Books at 17:30 ET

| Ticker | Bid | Ask | Quote time | Read |
|--------|-----|-----|-----------|------|
| ONMD | $0.59 x100 | $0.82 x100 | 20:00:00Z | Two-sided but **90 min stale** (close snapshot); re-pulled once, unchanged |
| AMIX | $3.94 x100 | $4.00 x100 | 20:14:12Z | Two-sided, stale (unchanged since 22:30) |
| GMM | $2.08 x100 | **$0.00 x0** | 20:00:02Z | **One-sided — no offer** |

**Freshness guard on ONMD.** The Alpaca quote is a 20:00:00Z close snapshot while
SIP has the stock at $0.91 on 541 trades in the last minute. Per the USDE Jul 1
precedent this is **staleness, not contradiction** — the divergence is not a
bad-print signal, and SIP through 17:16 ET fully corroborates the scanner. The
paper book being stuck at a $0.82 ask is the same mechanic that produced the AMIX
fill artifact at 23:00; noting it now so an 00:00 entry is read correctly.

### Candidate evaluation

**ONMD — lead candidate, NOT entry-eligible this scan.** OneMedNet Corporation
(NASDAQ), real-world healthcare data platform built on Palantir Foundry.

| Gate | Value | Pass |
|------|-------|------|
| AH >10% across ≥2 AH scans | **first AH scan >10%** (absent from the 22:30/22:45/23:00 screener) | **NO — blocks entry** |
| Float | 16.4M | recorded (not a filter) |
| Day% above -15% | +17.0% | yes |
| Entry extension < +150% | Total% +46.9% | yes, comfortable |
| Trajectory | **BUILD, at its AH high**, new high $0.92 at 17:16 ET | yes |
| Real AH liquidity | 1.05M sh / 3,182 trades in the 17:10 bar, rising every bar | yes |
| SIP corroborates price | SIP $0.91 vs scanner $0.89 — scanner understates | yes |
| Tradable | `tradable=true` NASDAQ | yes |
| Catalyst | **none found same-day** (3 searches; one 429 retried on tavily) | Grade None |

Catalyst detail: the OneMedNet newsflow is dense but stale — Risorius EEG/PSG data
licensing (Feb 24), ViuHealth autoimmune partnership (Feb 26), record 2025 bookings
$2.79M (Feb 12), FDA 510(k) support (Jan 22). Nothing dated 07-28 on GlobeNewswire,
the company news archive, or StockTitan. Provisional **Grade None**.

The name clears every gate except the one that matters procedurally: it needs a
second after-hours screener appearance above 10%. Its ignition fired at 16:59 ET,
one minute *before* the 23:00 scan ran, which is why it was invisible then. Under
the rules the earliest legal entry is **00:00 CET**. Re-run the catalyst search
then — the 16:59 ignition is late enough that a PR, if one exists, becomes
searchable around 17:30-18:00 ET.

**GMM — skip on two independent grounds.** (1) SPIKE→FADE: peaked $3.64 at 17:00
ET, -18% off the high with volume down 93% across three bars. The 0/10+ bucket.
(2) No offer in the book (`ask $0.00 x0`). Background note from the catalyst
search: the most recent GMM filing is an **F-3 shelf registration**, which is
dilution machinery — if a same-day catalyst does surface it is more likely to be
Grade D than anything else. No entry under any later scan unless the shape
completely reverses.

**EGG — skip, carried.** Reached +12.5% AH (its first scan above the gate), and
the last seven SIP bars do grind upward $4.02 → $4.29. But: Total% **+109%** is the
highest extension on the board, the multi-day dead-cat structure documented at
22:15 stands (-68% on 07-27, $6.40 → $2.05), and AH volume is 13-17K sh/bar against
a 2.2M average daily volume (VRatio 0.4x) — the flow is not there. Needs a second
gate-clearing scan anyway.

**AMIX — open position, no action this pulse.** Position management belongs to the
premarket evaluation. For the record, the tape has turned since the 23:00 entry:
AH high $4.96 (16:20 ET), then $4.86 (16:40 ET), and it has since oscillated
$3.89-4.46 with the last bars at $4.04-4.14 — roughly **-16% off the AH high**, at
the edge of the 20% hold band. Volume remains real (119K-412K sh, 1,415-4,512
trades per 5-min bar; 7.0M AH shares total against 1.9M average daily volume) so
this is distribution into genuine liquidity rather than a book evaporating.
Marked P&L is +4.6% on the artifact fill of $4.02; against the notional live entry
of ~$4.65 flagged at 23:00 it is roughly **-11%**.

**Carried skips, no workup re-run:** SBNYL (untradable, `tradable=false`), MB (no
AH book, 100 shares on one print, quote timestamped 2026-07-22), IOTR (spent
spike, below gate), YIBO (SPIKE→FADE confirmed, below gate).

### Plan for 00:00 CET

1. **ONMD** is the entry candidate. If it holds >10% AH in the 00:00 screener it
   clears the two-scan gate. Enter only if SIP still shows accumulation and price
   is at or within ~20% of its AH high; size ~$100 at a limit above the live SIP
   market, and expect the stale paper book to fill somewhere below it.
2. Re-run the ONMD catalyst search. A financing or offering flips it to Grade D
   and cancels the entry.
3. EGG needs a second >10% scan *and* a volume expansion to be worth revisiting;
   the extension alone (+109%) makes it marginal.
4. GMM, MB, SBNYL, IOTR, YIBO stay skipped.
5. Watch for a **third ignition cluster**. Two have fired tonight (16:03-16:08 and
   16:59); the 00:00 and 00:30 scans should be read as fresh-ignition hunts rather
   than only as follow-ups on existing names.

### For the daily email

- **AMIX** (the only open position) has faded from its $4.96 after-hours high to
  ~$4.10, about 16% off, though on real volume rather than an empty book. It shows
  +4.6% in the account only because the paper fill at $4.02 came from a stale book
  roughly 15% below the live market — on a live account this trade would currently
  be down about 11%. Grade None, so the plan is to exit at the first premarket
  opportunity regardless.
- **ONMD** was the best-shaped candidate of the night and was blocked purely by the
  two-scan confirmation rule, because its ignition fired at 16:59 ET, one minute
  after the 23:00 scan. This is the second time the gate has cost a look at a
  late-igniting name. **Question for Juan:** should the two-AH-scan gate be
  satisfiable by *two consecutive 15-minute SIP confirmations* on the same scan,
  rather than requiring two separate screener pulses? The intent of the rule is to
  filter one-print artifacts, and SIP accumulation across consecutive bars proves
  that more directly than a second screener appearance thirty minutes later. No
  action taken; flagging for a decision.

## Scan 00:00 CET (6:00 PM ET) — **entry: ONMD**, catalyst found

**One entry this pulse.** ONMD cleared the two-AH-scan gate, and the catalyst
search that came up empty at 23:30 now returns a **$11.5M+ commercial agreement**
dated today. It is the first graded catalyst of the night and the strongest
setup: the stock is making new after-hours highs at 17:46 ET on 80K-270K shares
per minute. A **third ignition cluster** also fired (YHC 17:31 ET, STFS 17:41 ET),
with STFS going near-vertical as this scan runs.

### Main AH screener

```
AFTER-HOURS Scan: 2026-07-28 18:00:10 ET  |  11 hits
```

| Ticker | Chart | Close | Day% | AH Chg | AH Price | Total% | AH Vol | AvgVol | VRatio | Float | Industry |
|--------|-------|-------|------|--------|----------|--------|--------|--------|--------|-------|----------|
| AMIX | [TV](https://www.tradingview.com/chart/?symbol=AMIX) | $2.75 | -1.4% | +50.9% | $4.15 | +48.7% | **7.3M** | 1.9M | 3.8x | 502K | Medical Specialties |
| **ONMD** | [TV](https://www.tradingview.com/chart/?symbol=ONMD) | $0.71 | +17.0% | **+27.6%** | $0.90 | +49.3% | 5.0M | 1.4M | 3.7x | 16.4M | Packaged Software |
| YIBO | [TV](https://www.tradingview.com/chart/?symbol=YIBO) | $1.15 | -2.5% | +5.2% | $1.21 | +2.5% | 1.6M | 207K | 7.5x | 2.1M | Electronics/Appliances |
| EGG | [TV](https://www.tradingview.com/chart/?symbol=EGG) | $3.81 | +85.9% | +12.6% | $4.29 | +109.3% | 947K | 2.2M | 0.4x | 8.3M | Misc Commercial Services |
| GMM | [TV](https://www.tradingview.com/chart/?symbol=GMM) | $2.47 | -8.5% | +28.4% | $3.17 | +17.4% | 705K | 3.0M | 0.2x | 1.7M | Packaged Software |
| **STFS** | [TV](https://www.tradingview.com/chart/?symbol=STFS) | $3.63 | +19.4% | **+44.6%** | $5.25 | +72.7% | 238K | 427K | 0.6x | 1.1M | Advertising/Marketing (**new above gate**) |
| **YHC** | [TV](https://www.tradingview.com/chart/?symbol=YHC) | $1.39 | -14.7% | +11.5% | $1.55 | -4.9% | 133K | 276K | 0.5x | 1.1M | Advertising/Marketing (**new**) |
| IOTR | [TV](https://www.tradingview.com/chart/?symbol=IOTR) | $3.05 | +3.0% | +20.0% | $3.66 | +23.6% | 94K | 36K | 2.6x | 2.7M | IT Services |
| MGRX | [TV](https://www.tradingview.com/chart/?symbol=MGRX) | $0.56 | +2.4% | +7.8% | $0.60 | +10.4% | 68K | 552K | 0.1x | 14.6M | Pharmaceuticals: Major |
| SBNYL | [TV](https://www.tradingview.com/chart/?symbol=SBNYL) | $1.20 | +0.0% | +45.8% | $1.75 | +45.8% | 30K | 11K | 2.7x | 59.6M | Regional Banks |
| MB | [TV](https://www.tradingview.com/chart/?symbol=MB) | $3.67 | -7.1% | +23.4% | $4.53 | +14.6% | 100 | 5K | 0.0x | 4.7M | Restaurants |

Above the 10% AH gate: AMIX (open position), ONMD, EGG, GMM, STFS, YHC, IOTR, MB
(no book), SBNYL (untradable). YIBO has fully died at +5.2%.

### Spike-bar verdicts (instrumentation, verbatim, as-of 18:00 ET)

```
ONMD 2026-07-28  SPIKE  16:59ET  +20%  $0.85  161 trades / 52k sh  (first co-spike bar)
GMM  2026-07-28  SPIKE  16:59ET  +38%  $3.41  675 trades / 82k sh  (first co-spike bar)
AMIX 2026-07-28  SPIKE  16:03ET  +24%  $3.40  709 trades / 55k sh  (first co-spike bar)
IOTR 2026-07-28  SPIKE  16:08ET  +29%  $3.93  170 trades / 21k sh  (first co-spike bar)
YHC  2026-07-28  SPIKE  17:31ET  +22%  $1.70  137 trades / 14k sh  (first co-spike bar)
STFS 2026-07-28  SPIKE  17:41ET  +24%  $4.50  219 trades / 29k sh  (first co-spike bar)
```

**A third ignition cluster: 17:31-17:41 ET.** The night now has three distinct
windows — 16:03-16:08 (AMIX, YIBO, IOTR, EGG), 16:59 (ONMD, GMM), and 17:31-17:41
(YHC, STFS). Ignitions are not confined to the AH open; two of the three clusters
fired more than an hour after it, and the 16:59 cluster produced tonight's graded
catalyst. This is the clearest single-night evidence yet that Initiative 3's
AH-open window is a concentration, not a boundary.

### SIP volume — ONMD is building a second leg to new highs

`broker.js bars ONMD --tf 5Min --start 2026-07-28T20:00:00Z`

| Bar (ET) | O → C | High | Vol | Trades | VWAP |
|----------|-------|------|-----|--------|------|
| 17:10 | $0.87 → $0.89 | $0.92 | 1,052,556 | 3,182 | $0.88 |
| 17:15 | $0.89 → $0.84 | $0.92 | 850,386 | 2,417 | $0.87 |
| 17:20 | $0.84 → $0.84 | $0.89 | 536,844 | 1,597 | $0.84 |
| 17:25 | $0.84 → $0.81 | $0.85 | 205,754 | 557 | $0.82 |
| 17:30 | $0.82 → $0.86 | $0.86 | 326,262 | 1,062 | $0.85 |
| 17:35 | $0.86 → $0.93 | **$0.95** | 846,334 | 2,704 | $0.91 |
| 17:40 | $0.93 → $0.92 | $0.95 | 742,483 | 2,334 | $0.93 |

1Min tape into the scan minute:

| Min (ET) | O → C | High | Vol | Trades |
|----------|-------|------|-----|--------|
| 17:39 | $0.91 → $0.93 | **$0.95** | 270,199 | 860 |
| 17:42 | $0.92 → $0.94 | $0.95 | 205,981 | 520 |
| 17:44 | $0.92 → $0.92 | $0.92 | 110,728 | 416 |
| 17:46 | $0.92 → $0.91 | $0.92 | 107,135 | 301 |

The 17:20-17:25 pullback (volume 1.05M → 206K, price $0.92 → $0.81) looked like the
start of a fade at the 23:30 read. Instead it was a base: volume re-expanded 4x
into 17:35 and price took out the old $0.92 high at $0.95. That is a
higher-low/higher-high structure on rising participation, the textbook BUILD.
~5M AH shares against a 1.4M average daily volume.

**STFS — live vertical ignition, blocked by the two-scan gate:**

| Min (ET) | O → C | High | Vol | Trades |
|----------|-------|------|-----|--------|
| 17:40 | $3.96 → $3.97 | $3.97 | 3,514 | 27 |
| 17:41 | $3.97 → $4.46 | $4.50 | 29,413 | 219 |
| 17:42 | $4.53 → $4.90 | $4.93 | 53,133 | 523 |
| 17:43 | $4.84 → $5.07 | $5.17 | 89,087 | 935 |
| 17:44 | $5.04 → $5.23 | $5.46 | 81,878 | 1,113 |
| 17:45 | $5.33 → $5.09 | $5.38 | 49,476 | 719 |
| 17:46 | $5.09 → $5.52 | **$5.77** | 79,750 | **1,197** |

From a dead $3.40 base (15-70 shares/min all evening) to $5.77 in six minutes on
1,197 trades in the final minute. Real, accelerating, and the scanner's $5.25 is
already stale versus the $5.77 tape.

**GMM — second wave, then fading again:** 98K → 119K → 51K → 40K sh (17:30 → 17:45)
on 1,416 → 1,718 → 625 → 461 trades. Rallied $2.90 → $3.42, back to $3.06. Still
-16% off the $3.64 peak set at 17:00 ET.

**IOTR — thin ramp, not a move:** the +20% AH headline is built on 309-2,900 shares
per 5-min bar at 4-16 trades. The price walked $3.20 → $3.70 on essentially no
participation.

**YHC — spike and fade inside 15 minutes:** 98,724 sh / 733 trades in the 17:30 bar
(peak $1.76), then 45K → 4.5K → 26K on 327 → 66 → 103 trades, price back to $1.48.

### Books at 18:00 ET

| Ticker | Bid | Ask | Quote time | Read |
|--------|-----|-----|-----------|------|
| ONMD | $0.59 x100 | $0.82 x100 | 20:00:00Z | Two-sided but a 2-hour-old close snapshot — **stale, not contradicting** |
| IOTR | $2.58 x100 | $3.65 x100 | 20:00:00Z | Stale close snapshot, 41% wide |
| YHC | $1.19 x100 | $1.62 x100 | 20:00:00Z | Stale, 36% wide |
| **GMM** | $2.08 x100 | **$0.00 x0** | 20:00:02Z | **One-sided — no offer** (2nd consecutive scan) |
| **STFS** | $3.09 x100 | **$0.00 x0** | 20:00:04Z | **One-sided — no offer** |

**Freshness guard on ONMD (USDE precedent).** The paper quote is frozen at the
20:00:00Z close while SIP shows 107,135 shares on 301 trades in the 17:46 minute at
$0.91. The gap is staleness in Alpaca's IEX paper feed, not a bad print — SIP is
current to within ~14 minutes of the scan and corroborates every level. Entry
priced off the SIP tape.

### ONMD — entered

**OneMedNet Corporation** (NASDAQ, Minneapolis), regulatory-grade real-world
healthcare data; its iRWD platform is built on Palantir Foundry and went fully
operational in April 2026 with 80M patient journeys.

**Catalyst (found this pulse, Grade B):** *"OneMedNet Secures $11.5+ Million
Agreement to Supply Regulatory-Grade Real-World Data for Foundational AI Model
Development"* — GlobeNewswire, 2026-07-28. The company entered an agreement to
supply its multi-modal imaging iRWD data for training a foundational AI model.

Three points on the grade:
1. It is a **contract win**, which the grading table maps to **B** (hold up to 2
   days, stop -15%). Graded B.
2. On magnitude it borders A: $11.5M+ against FY2025 bookings of **$2.79M** is
   roughly 4x the company's entire annual bookings in one deal. Recorded as a
   B-that-argues-for-A rather than upgraded, since the table's A tier is reserved
   for acquisitions and major partnerships.
3. **The PR timing explains the ignition.** The release is timestamped ~16:55 ET
   and the spike-bar detector puts the first co-spike bar at **16:59 ET**. This is
   a rare clean case of catalyst → ignition with a four-minute lag, and it is why
   the 23:00 and earlier searches found nothing: the news did not exist yet.

Every gate, checked:

| Gate | Value | Pass |
|------|-------|------|
| AH >10% across ≥2 AH scans | +25.5% (23:30) → +27.6% (00:00) | yes |
| Float | 16.4M | recorded (not a filter) |
| Day% above -15% | +17.0% | yes |
| Entry extension < +150% | fill $0.94 vs $0.71 close = **+32%** (scan Total% +49.3%) | yes, comfortably |
| Trajectory | **BUILD at new AH highs** — $0.95 at 17:39 ET after basing at $0.81 | yes |
| Real AH liquidity | ~5M AH sh vs 1.4M avg vol; 2,334-3,182 trades per 5-min bar | yes |
| SIP corroborates price | SIP $0.91-0.95 vs scanner $0.90 — scanner understates | yes |
| Two-sided book | $0.59 / $0.82 x100, stale but two-sided; SIP proves fillable flow | yes |
| Tradable | `tradable=true` NASDAQ | yes |
| Catalyst | **$11.5M+ AI data agreement, same-day** | **Grade B** |

**Order:** `buy ONMD 108 --limit 0.98 --ext` → id `d40549db`, **filled @ $0.94**,
$101.52 committed. No stale-book artifact this time — the fill landed inside the
live SIP range ($0.91-0.95), unlike the AMIX fill at 23:00.

Hold strategy: Grade B → **hold up to 2 days, stop -15% from entry** ($0.80).
Premarket evaluation owns the exit.

### STFS — skip this pulse (gate), primary watch for 00:30

The most violent move of the night and the only name igniting *as the scan runs*.
Not entered, for two independent reasons:

1. **First AH scan above the gate.** It was absent from the 22:30/22:45/23:00/23:30
   screeners (it sat at $3.36-3.60 on 15-70 shares/min for ninety minutes). The
   two-AH-scan rule makes 00:30 CET its earliest legal entry.
2. **No offer in the book** (`ask $0.00 x0`). Under the illiquid-ramp rule that is
   a skip on its own — though here it is more likely paper-feed staleness than a
   genuinely empty book, given 1,197 real trades in the last minute.

Catalyst: **nothing same-day found** (2 searches). What surfaced instead is
concerning — a **$2.6M Class B share subscription on 07-22** and a CFO purchase of
those same 2,000,000 Class B shares at $1.30. A recent equity raise plus a history
of volatility halts (07-10, 07-16) and an EGM to revise share allotment (07-13)
means the dilution machinery on this name is active. If a same-day release appears
by 00:30 and it is a financing, that is **Grade D** and the entry is off regardless
of the tape. Total% is also already +72.7% and climbing fast; at $5.77 it is
+59% *in after-hours alone*, so extension needs re-checking at 00:30.

### Other skips

- **GMM** — carried skip, now on two grounds it has failed twice: `ask $0.00 x0`
  for a second consecutive scan (automatic skip, TII precedent), and the shape is a
  double-fade (peak $3.64 at 17:00, second wave to $3.42, back to $3.06). Its most
  recent filing is an F-3 shelf. Cleared the two-scan gate on paper (+19.8% →
  +28.4%) and is being skipped purely on liquidity and trajectory.
- **IOTR** — **skip: illiquid ramp.** +20% AH built on 4-16 trades per 5-min bar.
  The 94K AH volume against a 36K average is the stale-VRatio artifact pattern; the
  book is a 41%-wide close snapshot. Nothing fillable here.
- **YHC** — **skip: SPIKE→FADE, first scan.** Ignited 17:31 ET, peaked $1.76 within
  five minutes, and volume collapsed 98K → 4.5K by 17:40. Also Day% -14.7%, a
  hair inside the dead-cat threshold, with Total% still **negative** (-4.9%) — the
  AH pop has not reclaimed the previous close. Blocked by the two-scan gate anyway.
- **EGG** — +12.6% AH, its second scan above the gate, so the gate is cleared. Still
  skipped: Total% **+109.3%** is the highest extension on the board, the multi-day
  dead-cat structure stands (-68% on 07-27, $6.40 → $2.05), and AH volume is 0.4x
  its average against a 2.2M avg daily volume. Grinding higher on no participation.
- **YIBO** — dead at +5.2% AH, below gate. The 23:00 SPIKE→FADE skip is confirmed.
- **MGRX** (+7.8%) — below gate.
- **MB** (+23.4%, 100 shares, quote timestamped 2026-07-22) and **SBNYL**
  (`tradable=false`) — carried skips, no workup re-run.

### AMIX — open position, no action (position management is the PM pulse's call)

For the record: AMIX has stabilised rather than continued fading. After the
$4.96 high (16:20 ET) and the drop to $3.89, it has spent the last hour oscillating
$3.95-4.46 with the 17:35 bar closing $4.12 on 96,676 sh / 1,121 trades. That is
**-17% off the AH high**, still inside the 20% hold band, on genuine two-way
volume (7.3M AH shares vs 1.9M avg). Marked +0.5%... in fact -0.5% at $4.00 on the
artifact fill of $4.02; against the notional live entry of ~$4.65 flagged at 23:00
it is roughly **-14%**.

### Read going into 00:30 (final scheduled scan)

1. **STFS** is the entry candidate if it clears its second gate scan — subject to a
   fresh look at extension (it may blow through +150% Total% at this rate), the
   book, and one more catalyst search. A financing find kills it.
2. **ONMD** needs no action; watch that the second leg does not reverse before the
   close of the session.
3. Run the final-scan feed-lag cross-check on every tracked name (AMIX, ONMD, STFS,
   GMM, YHC, EGG, IOTR, YIBO) against SIP before finalising.
4. A **fourth ignition cluster** is plausible given three have fired. Read 00:30 as
   a fresh-ignition hunt, not only a follow-up.

### For the daily email

- **Two positions open.** AMIX (entered 23:00, Grade None, -14% against its real
  market entry) and **ONMD** (entered 00:00 @ $0.94, **Grade B**).
- ONMD is the best trade the process has produced in a while: a real same-day
  catalyst ($11.5M+ AI-data agreement, ~4x the company's annual bookings), the
  ignition bar firing four minutes after the press release, entry at a new
  after-hours high on genuine accumulation, and a fill inside the live market
  rather than an artifact. Grade B means holding up to 2 days.
- **Answered by tonight's tape:** the question raised at 23:30 about the
  two-AH-scan gate. Waiting the extra 30 minutes on ONMD cost nothing — it was
  $0.89 then and filled at $0.94 now, about 5% worse — but it **bought the
  catalyst**, which did not exist at 23:30. That is an argument for keeping the
  gate as-is rather than replacing it with same-scan SIP confirmation. Still worth
  a decision from Juan, but the evidence now cuts toward the current rule.
- **Question for Juan:** ONMD's $11.5M agreement is roughly 4x the company's entire
  FY2025 bookings. The grading table calls a contract win Grade B (2-day hold), but
  a deal that size relative to the business arguably re-rates the company the way
  Grade A is meant to capture. Should catalyst grade account for deal size relative
  to company size, rather than only deal type? Graded B for now.

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
| ONMD | $0.94 | 2026-07-29 00:00 CET | 108 ($101.52) | d40549db | **First graded catalyst of the night:** $11.5M+ agreement to supply iRWD real-world data for foundational AI model training (GlobeNewswire 07-28, ~16:55 ET), ~4x FY2025 bookings — Grade **B**, hold up to 2 days, stop $0.80. Ignition bar 16:59 ET, four minutes after the PR. Entered at a new AH high $0.95 after basing at $0.81 on re-expanding volume (846K sh / 2,704 trades in the 17:35 bar; ~5M AH sh vs 1.4M avg). Day% +17.0%, entry extension +32% vs the $0.71 close. Fill landed inside the live SIP range — no stale-book artifact. |
| AMIX | $4.02 | 2026-07-28 23:00 CET | 21 ($84.42) | ce3a2383 | Float 502K, Day% -1.4% (no dead-cat), AH BUILD +73% holding -4% off its $4.96 high, 5.4M AH sh vs 1.7M avg vol on 4K-14K trades/bar, entry extension only +46% vs the $2.75 close. Grade **None** (6 searches, no same-day catalyst) → exit at first PM opportunity. Fill is a stale-paper-book artifact ~15% below the live $4.65 market. |

## Morning Evaluation — 10:20 CET

### Today's Winner

**No real winner today.** Nothing cleared the >100% bar in the tradeable AH→PM
window. The morning's biggest *headline* mover, **EGG +170% PM**, is a Yahoo
anchoring artifact: EGG's "previous close" of $2.05 is **two closes ago**. EGG
already ran **+96% during the 07-28 regular session** (Day% +96.1%, regular close
~$4.02, off a −68% dead-cat the prior day). Measured from the actual regular
close, EGG's AH→PM continuation was only **AH SIP $4.95 (+23%) → PM SIP $5.64
(+40%)** — a modest bounce-continuation, not a >100% explosion.

**Biggest genuine AH→PM mover (below the winner bar): AMIX** — Medical Specialties
- Catalyst: **Grade None** (6 searches, no same-day PR; a July 28 TipRanks cash/share-count housekeeping update, 971K shares out / $5.1M cash — dilution-adjacent, not a fresh operational catalyst). Post-reverse-split (1-for-21, Jun 23) ultra-low-float squeeze.
- Previous Close: $2.79 | Day%: −1.4% (flat regular session — clean base, not a dead-cat)
- AH last night: SIP high **$4.96 (+77.8%)** at 16:20 ET on huge accumulating volume (811K → 1.01M → 1.22M → 1.08M sh/bar, 8.8k–14k trades/bar)
- Premarket now: SIP high **$5.29 (+89.6%)** at 08:00 ET on 839K sh / 14,227 trades (Yahoo under-reported this peak at $4.82)
- Hypothetical P&L (AH entry → PM peak): from our $4.02 fill → $5.29 = **+31.6%**; from close $2.79 → $5.29 = +89.6%
- Float: 502K | Market Cap: ~$4M

AMIX's PM SIP peak (+89.6%) is a real, liquid, volume-backed continuation on a
flat-base low-float name — **but +89.6% is below the >100% winner bar** (per the
Jul 14/16 winner-bar rule, a sub-100% move is not crowned as the winner). We
**detected and entered** it, so it is the correct diagnostic subject.

**Scanner Diagnostic (AMIX):**
- Detectable at screening time? **YES**
- We entered AMIX live at 23:00 CET @ $4.02. It was caught in-window with real
  accumulating SIP volume from the 16:00 ET ignition. Detected + selected. No
  scanner gap — this is the strategy working as intended (holding the biggest
  genuine mover).
- Scanner gap: none for AMIX.

**Broker-block tracking:** No broker blocks this session — all pipeline names
returned `tradable=true`. Standing tally unchanged.

### Baseline Tracking

- Days tracked: **56** (was 55 + 1)
- Winners detected by scanner: **46/52 (88.5%)** — AMIX (biggest genuine mover) detected + entered; added to the detected list.
- Winner selected for paper trade: **27/52 (51.9%)** — AMIX entered @ $4.02.
- Target: >80% detection
- Status: **BASELINE MET** (88.5%)
- **Baseline gap:** none new. The prior baseline line lives in 07-27 (the immediately-preceding trading day), so the chain is intact. The two historic un-counted days (07-17, 07-20) remain carried, not re-absorbed.

### Retrospective Scan Results

Live PM scan (04:20 ET) — 5 hits: AMIX +75.3% (PM $4.82 Yahoo / $5.29 SIP peak),
GMM +46.2%, ONMD +22.2%, EGG +22.8% (from the $3.81 AH-print artifact; +40% from
the real $4.02 regular close), BATL +9.4%. AH SIP reconstruction confirmed AMIX
as the only clean flat-base >75% AH→PM continuation on heavy volume; EGG was a
dead-cat bounce-continuation; GMM and YIBO faded as the evening scans predicted.

### Open Position P&L (Alpaca)

**Quote-freshness note:** the `broker.js quote` endpoint returned stale 20:00 ET
books for both names (AMIX @20:14Z, ONMD @20:00Z = last night's regular close).
The `positions` `current_price` however aligns with live PM (AMIX ~$4.50, ONMD
~$0.84), so the P&L below is reported against the live PM level, not the stale book.

| Ticker | Entry | Entry Total% | Catalyst | Entry Time | PM Peak | Peak Time | Exit | P&L | P&L % | Status |
|--------|-------|--------------|----------|------------|---------|-----------|------|-----|-------|--------|
| AMIX | $4.02 | +46.2% | None | 23:00 CET | $5.29 (SIP) | 08:00 ET | open | — | +11.9% (live ~$4.50) | 🟢 Open, up |
| ONMD | $0.94 | +56.7% | B — $11.5M iRWD AI-data deal | 00:00 CET | $0.87 | 04:00 ET | open | — | −10.6% (live ~$0.84) | 🔴 Open, down |

Exits handled by position-evaluation.md (10:30/14:30 CET), not here. No realized fills this session.
**Total Realized P&L (Alpaca fills only): €0.00**

### Scanner Effectiveness

- Evening scans ran: **6 of 7** (21:30, 22:00, 22:30, 23:00, 23:30, 00:00 CET; plus bonus observation scans 22:15 & 22:45). **The 00:30 CET (18:30 ET) final scan did not run** → the 18:30–20:00 ET tail was uncaptured live.
- Candidates found: ~15 unique tickers across the night (EGG, BIYA, INLF, CNET, AMIX, ONMD, GMM, YIBO, IOTR, EGG, MGRX, etc.)
- Retrospective matches: AMIX (entered), ONMD (entered), EGG/GMM/YIBO (tracked, skipped) — all top movers were on the radar.

### Missed Opportunities

No significant missed opportunities. Every top AH→PM mover was surfaced by the evening scans. EGG/GMM/YIBO were tracked and correctly skipped on dead-cat/fade structure.

### AH Mover Follow-Through

| Ticker | AH Peak | Peak Time | AH Trajectory | Current PM | From Peak | From Close | Verdict |
|--------|---------|-----------|---------------|------------|-----------|------------|---------|
| AMIX | $4.96 (SIP) | 16:20 ET | Build | ~$4.50 (PM peak $5.29) | −9% off PM peak | +61% | **PM > AH (continuation)** — entered |
| EGG | $4.95 (SIP) | 19:45 ET | Dead-cat build | ~$4.93 (PM peak $5.64) | −13% off PM peak | +140% from $2.05 / +40% from $4.02 close | PM slightly > AH; skipped (dead-cat) — correct, thin AH vol |
| GMM | $3.64 | 17:00 ET | Spike→fade | $3.64 (PM peak $3.73) | −2% | +35% | Faded then PM ≈ AH; skipped — correct |
| ONMD | $0.95 | 17:35 ET | Build | ~$0.84 (PM peak $0.87) | −3% | +40% | Faded below entry; entered @ $0.94 (Grade B) |

**AH-peak-vs-PM-peak check:** AMIX PM SIP $5.29 > AH SIP $4.96 (continuation — the
name we wanted). EGG PM $5.64 > AH $4.95 by +14% but the whole move sits on top of
a −68% dead-cat, so the incremental from the regular close was small. No
extreme-runner (>250% from close) AH→PM fade case today.

### Fade-rule / override / gapper tallies (this session)

- **Fade-rule false-negatives (sub-3M trigger, standing 3 of 6):** no new sub-3M AH-fader re-explosion today. EGG re-exceeded its AH peak in PM (+14%) but is **8.3M float = higher-float negative control** (does not count toward the ≥4/5 sub-3M trigger). GMM/YIBO/IOTR faded as skipped and did not re-explode. Trigger still **not met**.
- **PM-only gapper (standing holdable 1 of 6):** today's biggest raw PM mover, EGG, is an **AH→PM continuation** (moved >10% in AH), not a PM-only gapper — no new gapper case.
- **Late-AH-tail surge:** none. AMIX's decisive AH surge was 16:00–16:20 ET (in-window). EGG's late build (19:45 ET) fell in the unscanned tail but EGG was already tracked/skipped, and it was not the winner — no new true-tail case.
- **In-window feed-lag miss (standing 3, ≥3 escalation REACHED):** no new case this session — AMIX was caught in real time. The standing recommendation (independent whole-universe AH gainers cross-check at the final scan) remains routed to the daily email.
- **Price-floor exclusion (standing 3, all 2026-07-28, 0 holdable):** the standard PM scan surfaced no new sub-$0.50 in-window AH movers this session; standing count unchanged.
- **Reverse-split-squeeze fade:** **AMIX added** — 1-for-21, ~5 weeks old (Jun 23, weeks/months-old bucket), float 502K, Grade None, entered $4.02 → PM peak $5.29 = **+31.6% continue**. Recency split now: this-week 3/3 fade; weeks/months-old **3 non-fade (EDHL, LGCL, AMIX) / 1 fade (PAVS)**. AMIX reinforces "older splits don't systematically fade." The this-week bucket (3/3 fade) still needs one more case to resolve.

### Notes

- **Coverage failure — 2026-07-28: 6 of 7 evening scans ran** (00:30 CET / 18:30 ET final scan missing). Running coverage-failure tally: this is the notable one this cycle. It did **not** cost a detection (AMIX entered in-window; EGG's tail build was already tracked and correctly skipped). Not counted against the detection baseline. If a second coverage failure lands within ~10 sessions, flag scheduler/bridge reliability for Juan.
- **EGG anchoring caution (recurring):** Yahoo's `--ah-history`/`--pm-history` "prev close" anchored EGG to $2.05 (two closes ago), inflating a +40%-from-regular-close bounce into a "+170%" headline. When a name ran hard *during* the regular session (high Day%), verify the AH/PM change against the **regular close**, not Yahoo's prev-close field, before crowning a winner.
- **AMIX is the clean signal of the night:** flat regular-session base, low float 502K, heavy accumulating SIP volume, PM continuation to +89.6% — detected and entered. The only knock is Grade None (no catalyst), so per plan it's a first-PM-opportunity exit. It fell just short of the +100% winner bar.

### Price Charts

```

========================================================================
 AMIX - 2-Day Price Timeline (5-min intervals)
========================================================================

Previous Close: $2.79
2-Day Range: $2.33 - $5.29
Current: $4.52 (+62.0% from prev close)
Peak: $5.29 (+89.6%) at 07-29 08:00 ET

Chart (oldest → newest):
$   4.82 │                                                            
         │                                                  █         
         │                                                █           
         │                                               █ █  █   █   
         │                                                   █ ███  ██
         │                                                         █  
         │                                                            
         │                                                            
         │                                              █             
         │                               █  ████████████              
         │████████          █  █    █████ ██                          
```
