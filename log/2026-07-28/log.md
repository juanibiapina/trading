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

## Paper Trades (Alpaca fills)

| Ticker | Fill Price | Entry Time | Shares (~$100) | Order ID | Reason |
|--------|------------|------------|-----------------|----------|--------|
| _(none)_ | | | | | Watch-only pulse — regular session, AH not open. |
