# Initiative 2 — Broker alternatives to Alpaca (research)

**Directive (Juan, 2026-09-04, re: 09-03 email):** "Can you also research
alternative providers besides alpaca? test them and find one that actually works
for trading these stocks." Juan picks the **switch-broker** path over paying for
Alpaca SIP (~$99/mo) or scoring on modeled fills.

**Problem being fixed:** the Alpaca paper account is on the free **IEX-only**
data plan, and Alpaca simulates paper fills against the subscribed feed. IEX
goes one-sided/stale at the 16:00 ET close for micro-float names, so there is no
AH ask to cross and extended-hours buy-limits never fill — even while the real
AH volume prints on other venues (visible only on SIP). Feed mismatch, not a
`broker.js` bug. Full root cause: `INIT2_ALPACA_FILL_ROOTCAUSE.md`. The chronic
cost is ~203% of detected PM upside lost to unfillable AH books (Init 3
`execution-gap.js`). So the decisive criterion for any replacement is: **does
its paper fill engine see a consolidated extended-hours quote for sub-$1
micro-floats** (AKAN, SHPH, GIPR-class)?

## Requirements

1. **Paper account with a programmatic API** (REST/SDK) — to keep `broker.js`-style automation.
2. **Extended-hours LIMIT orders via the API** — AH (16:00-20:00 ET) + PM (04:00-09:30 ET). Limit, not market: micro-cap AH spreads make market orders reckless.
3. **Paper fills simulated against a real consolidated (SIP-class) quote**, so AH micro-float limits actually fill when there is real off-IEX volume.
4. **EU availability** (Juan is in Germany) for the paper phase, and ideally a real live path from the EU later.

## Candidates evaluated (primary sources, 2026-09-07)

### 1. Interactive Brokers (IBKR) paper — RECOMMENDED PRIMARY
- **API:** two options — TWS API (needs TWS/IB-Gateway process running; headless via IBC/ib-gateway docker) or the **Client Portal Web API** (REST, no desktop process, OAuth/session-based).
- **Extended-hours limit orders:** supported (`outsideRth=true` on limit orders).
- **Fill realism:** paper "uses real market conditions"; fills simulated from **top of the book** against **the market data you subscribe to** — and "market data subscriptions for the live account can be shared with the paper account." A community report (Elite Trader) shows IBKR paper filling AH limit orders (DNUT). Because IBKR's consolidated feed spans far more venues than IEX, a proper US-equities data subscription lets the paper engine see AH micro-cap quotes that Alpaca's free IEX feed never shows. **This is the direct fix for the root cause.**
- **EU / live path:** IBKR is EU-regulated (IBIE, Ireland). Same account is the eventual live path (Init 2 step 5).
- **Caveats / setup cost:** (a) needs a **US-equities market-data subscription** that includes extended-hours consolidated quotes (basic bundles are ~USD 1.50-10/mo; the point is any non-IEX-only consolidated NBBO); (b) gateway/session must stay authenticated for the scan/eval pulses (Web API session, or a headless gateway); (c) paper account provisioned within ~24h of request; trial paper accounts get closed if idle. (d) Paper "held until market data arrives" for one-sided books — so if there is genuinely NO consolidated AH quote it still won't fill, but that is the correct/honest behavior and far rarer than IEX-only.

### 2. Webull OpenAPI (EU region) — RECOMMENDED BACKUP
- **API:** official `webull-openapi-python-sdk`; **EU developer portal confirmed** (`developer.webull.eu`); App Key/Secret auth. Region-configurable (US/UK/EU/…).
- **Paper trading:** relaunched Jul 2026 with API connectivity and a "more realistic simulation environment."
- **Extended-hours:** Webull is a retail leader in extended-hours access.
- **Why backup not primary:** unconfirmed whether the **EU** entity's paper API exposes **US micro-cap** extended-hours symbols and how realistic its micro-float AH fills are. Lower setup than IBKR (pure REST, no gateway), so it is the fast fallback if IBKR data-subscription friction stalls.

### 3. Moomoo / Futu OpenAPI — POSSIBLE, EU-ACCESS DOUBTFUL
- Paper trading supports **US-stock ETH (extended trading hours)** — but "only for US-stock **margin** paper trading accounts," and requires the **OpenD** gateway process (like IBKR TWS).
- Overnight (20:00-04:00 ET) not supported in paper, but our AH+PM window is inside ETH, so that is fine.
- **Blocker:** moomoo brokerage entities are US / SG / HK / AU / JP / MY — **no clear EU retail entity**, so a German resident likely cannot open the US-stock account the ETH paper needs. Backup-of-backup.

### 4. Trading 212 API — REJECTED
- The API supports **market orders only for extended hours**; limit/stop orders in extended hours return `invalid payload`. Our micro-cap AH strategy is limit-only. Rules T212 out for this use case (community-confirmed, unchanged as of the API update thread).

## Recommendation

**Primary: IBKR paper** — it is the only candidate that both (a) fixes the exact
root cause (consolidated extended-hours quotes drive the paper fill engine,
unlike Alpaca's IEX-only feed) and (b) is the EU-regulated live path we want
anyway. **Backup: Webull OpenAPI (EU region)** if IBKR's market-data-subscription
or gateway friction stalls the pilot. Moomoo is a distant third (EU access
doubtful); Trading 212 is out.

## Test protocol (run once an account + data are live)

The decisive test cannot be run without an account (fills depend on the broker's
own feed). Once Juan enables one:

1. Wire a read-only `broker2.js` shim (same shape as `broker.js`: `account`,
   `positions`, `buy --ext --limit`, `sell --ext --limit`, `orders`).
2. On the exact chronic-block names — **AKAN, SHPH, GIPR** and the next
   sub-$1 micro-float PM-only gapper — during a live AH session (16:00-20:00 ET),
   place a paper buy-limit at/above the SIP-observed AH print and check whether
   it **fills** (Alpaca never does).
3. Compare fill price vs the SIP 5-min bar we already pull; log to a
   `broker-compare.csv` for a few sessions.
4. If IBKR fills these where Alpaca does not, propose switching `broker.js`'s
   execution backend (a live-cycle change → propose to Juan, not applied alone).

## Needs from Juan (to unblock the test)

- **Primary path:** open an **IBKR paper account** (free; ~24h provision) and
  enable/share a **US-equities market-data subscription that includes
  extended-hours consolidated quotes** (not IEX-only). Provide API access
  (Client Portal Web API credentials, or confirm a headless IB-Gateway can run).
- **Backup path:** register at **developer.webull.eu**, create the API paper
  account, and share the **App Key / App Secret** so the same fill test can run
  there.
- Either one unblocks the empirical fill test on AKAN/SHPH/GIPR. No live-money
  or `broker.js` switch happens until the test shows real AH fills and Juan
  signs off.
