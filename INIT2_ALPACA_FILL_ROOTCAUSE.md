# Initiative 2 — Alpaca extended-hours no-fill: root cause

**Question (Juan, 2026-08-06):** "Research the alpaca problem, determine the
root cause." The stale Alpaca AH book has now cost 3 detected, qualifying
winners in ~8 sessions (NUWE +82.4%, KUST +45.9%, CLRO +34.3%). Detection and
selection worked each time; the loss was execution.

## Root cause (confirmed empirically 2026-08-07)

**The Alpaca paper account is on the free IEX-only market-data plan, and
Alpaca's paper fill engine simulates fills against the account's subscribed
feed. IEX publishes almost nothing for micro-float names outside the regular
session, so during extended hours there is no marketable ask for the engine to
cross — the buy-limit sits unfilled even while the consolidated tape (SIP) shows
heavy real volume.**

### Evidence

Ran latest-quote queries at 03:00 ET (post-market already closed):

```
IEX  AAPL: ap 0  as 0 | bp 298.49 bs 40  @ 2026-08-06T20:00:02Z   (= 16:00 ET)
IEX  CLRO: ap 0  as 0 | bp 9.67  bs 100 @ 2026-08-06T20:00:43Z   (= 16:00 ET)
SIP  AAPL: "subscription does not permit querying recent SIP data"
SIP  CLRO: "subscription does not permit querying recent SIP data"
```

Two facts fall out:

1. **The account has no SIP entitlement.** Any recent-SIP query is rejected.
   Free tier = IEX only. Alpaca paper fills use the subscribed feed, so fills
   are simulated off IEX.
2. **The IEX quote goes one-sided and stale at the 16:00 ET close** (`ap=0`,
   timestamp pinned to 20:00Z). IEX is a single lit venue with tiny share of
   micro-cap flow; in post-/pre-market it prints little or nothing for these
   names, so its last quote is the 16:00 close and the ask disappears.

A buy limit order fills in the paper engine when `ask <= limit`. With no IEX
ask after 16:00 ET, there is nothing to cross, so the order never fills. This is
exactly the "quote frozen at 16:00 ET, orders never filled" symptom in the
reports. Meanwhile the real AH prints happen on Nasdaq/Arca/etc. (not IEX) and
show up on SIP — which is why `broker.js bars` (SIP feed) reports heavy real
volume while the fill engine sees a dead book. The contradiction is a
**feed mismatch**, not a data glitch:

- fill simulation feed = IEX (free tier) → empty AH book → no fill
- our volume/chart feed = SIP (historical, >15 min old) → real AH volume

The two data sources disagree by construction for extended-hours micro-caps.

## Fix options (decision needed — Juan)

1. **Pay for SIP data.** Alpaca "Algo Trader Plus" (~$99/mo) gives full SIP
   NBBO incl. extended hours. Paper fills would then simulate against the real
   consolidated book, and AH micro-cap orders would fill like they do live.
   Direct fix; costs money; only worth it once an edge is proven.
2. **Switch broker for the paper phase.** IBKR paper (EU-regulated, already
   noted in Init 2 as the live-trading path) covers consolidated extended-hours
   quotes. More setup overhead; also the eventual live path from the EU.
3. **Decouple scoring from Alpaca fills (no cost).** Accept that free-tier
   Alpaca paper cannot model AH micro-cap fills, and score entries on modeled
   SIP fills — buy@ask / sell@bid reconstructed from the SIP 5m bars we already
   pull. Keep Alpaca for the record where it does fill, but stop treating a
   no-fill as "trade didn't happen." This measures the strategy edge honestly
   without paying; it does not give a real broker fill.

**Recommendation:** option 3 now (free, unblocks the data collection the loss
is currently corrupting), and hold options 1/2 until an edge is proven and we
move toward live — which is exactly the Init 2 step-5 gate. The no-fill is a
data-plan limitation, not a `broker.js` bug, so nothing in the code fixes it.
