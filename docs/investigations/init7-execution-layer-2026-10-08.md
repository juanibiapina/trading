# Initiative 7 — modeled execution layer and IEX spread finding

## Decision

The modeled execution layer is built ([init7-execute.py](../../scripts/init7-execute.py)) and capturing live: gob job `3t2` records a post-decision book at every slot and at the 15:55 ET flatten through October 13. The first live capture (October 8, 12:30 ET) arrived 0.47 s after the decision was persisted, with no errors.

The frozen design priced fills at the IEX book. IEX spreads on this basket average **17.98 bps against 1.41 bps** at the SIP NBBO for the same instants, so IEX pricing would charge each hourly round trip about 16.6 bps that a routed order does not pay. [Amendment A3](init7-amendment-a3.json) is frozen before any modeled pilot entry: fills are priced at the delayed SIP NBBO for the instant of the IEX capture, the IEX book still decides availability, and the IEX-priced ledger is reported as a conservative scenario. No order is sent.

## What the script does

- `capture` waits for the slot's `decision.json`, then requests IEX latest quotes for all eight basket symbols and the asset status for each. It writes `log/<date>/init7-execute/<HHMM>/capture.json` with exclusive creation. The 15:55 capture is the flatten book.
- `nbbo` runs after the 16-minute SIP delay and stores the last SIP quote in the 60 s up to each capture's receipt time as `nbbo.json`.
- `ledger` replays N1, A1, A2, CASH and QQQ with $100 per arm, 95% of equity per position, exits at the next slot before any new entry, and a single QQQ hold from the first valid entry slot to the flatten. Each fill checks that the quote follows the persisted decision, is no more than 60 s old, has positive sizes, covers the share count, and that the asset is fractionable. Exit quotes must arrive within 60 s. A missing exit marks the arm unresolved and pauses its entries, as the design requires. Both cost scenarios (5 and 25 bps slippage per side plus a 1 bp fee) are reported, with the spread paid on each fill in dollars.
- `spreads` summarizes every archived book.

## Spread evidence

Source: the 64 pre-decision IEX books archived by `init7-observe.py` on October 7 and 8 (8 symbols × 8 slots), each matched to the SIP quote at its receipt time. Raw rows: [iex-vs-sip-spreads.json](../../log/2026-10-08/init7-execute/iex-vs-sip-spreads.json), from [init7-iex-vs-sip.py](../../scripts/init7-iex-vs-sip.py).

| Symbol | IEX median bps | SIP NBBO median bps |
|---|---|---|
| TSLA | 51.6 | 1.47 |
| META | 21.7 | 2.28 |
| GOOGL | 16.3 | 1.43 |
| AAPL | 5.7 | 0.89 |
| AMZN | 3.5 | 1.54 |
| MSFT | 2.5 | 1.61 |
| NVDA | 1.1 | 0.63 |
| QQQ | 0.5 | 0.33 |

The October 8 12:30 slot selected TSLA while its IEX book was $371.77/$377.77, 160 bps wide. The SIP NBBO at that instant was $373.06/$373.17 (2.95 bps), so the IEX ask sat 1.23% above the best ask, and an IEX-priced entry would start 1.2% down. Real-time SIP quotes return HTTP 403 on this data plan, so the NBBO can only be read after the delay; it prices the fill and never feeds the decision.

At NBBO spreads, crossing costs about 1.4 bps per round trip, so the frozen slippage and fee allowance (12 bps base, 52 bps stress per round trip) dominates. Six round trips a day at the base allowance cost about $0.76 on $95, which the N1 selector must beat.

## Verification

- A rehearsal in `/tmp` used today's 10:30 and 11:30 decisions with fresh captures. The NVDA round trip reproduces by hand: 0.403514956 shares × $235.29 × 1.0006 = $95.00 cost, $94.874 proceeds, -$0.126 net, $0.008 spread paid. The open GOOGL position with no next capture was marked unresolved, and QQQ's flatten quote taken before 15:55 was rejected as early.
- `nbbo` wrote SIP quotes for the rehearsal captures after the delay, and the SIP-priced ledger ran.
- `python3 -m py_compile` passed. `init7-observe.py` and its pinned hashes are untouched.

## Next checks

- **October 9 15:00 CEST:** run `nbbo` and both ledgers for October 8 (slots 12:30–15:30 and the flatten); every arm must resolve.
- **October 9 18:00 CEST:** check that October 9 has six slot captures and a flatten capture.
- **October 14 15:00 CEST:** pin this script's SHA-256 with the 20-session calendar, and run both daemons for the pilot window (the observation daemon stops after its fifth session on October 13).
