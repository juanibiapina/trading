# Initiative 7: micro-cap AH census with quoted fills (2026-10-15)

Log-only study. No order, live rule, size or pulse timing changed.

## Question

Does the core AH→PM micro-cap strategy have any positive subset when entries pay the SIP ask at 17:00 ET and exits receive the SIP bid at 04:30 ET or the next open? Rules were frozen in `docs/investigations/init7-microcap-census-freeze.json` at 13:05 UTC, before any micro-cap data was fetched.

## Method

`scripts/init7-microcap-census.py` (reuses the helpers in `scripts/init7-liquid-ah-census.py`):

- **Universe:** about 2,050–2,230 symbols per day with a regular close of $0.50–$10, minus the point-in-time top 1,000 by dollar volume.
- **Event, October 1, 2025 – September 30, 2026 (250 full sessions):** +10% to +150% above the close at both 16:30 and 17:00 ET, day change above -15%, at least 100k shares and $100k traded 16:00–16:55 ET, and at least 3x the symbol's 20-session median for that window.
- **Fills:** entry at the last SIP ask between 16:45 and 17:00 ET. Exit at the last SIP bid between 04:00 and 04:30 ET, or at the next official open less 50 bps.
- **Statistics:** a date-clustered bootstrap with a Bonferroni correction over 8 cells. A cell passes only if its mean is above zero, its lower bound is above zero and both halves are positive.

Replay: `python3 scripts/init7-microcap-census.py --out log/2026-10-15/init7-microcap-census --replay`.

## Results

502 events. 499 were scored; 2 had no entry quote and 1 had a split. 11 used the open fallback at 04:30. The median entry spread is 72 bps (interquartile range 45–106).

| Cell | n | 04:30 bid, net | Halves | Open, net | Halves |
|---|---:|---:|---:|---:|---:|
| all | 499 | **-3.16%** [-6.13, +0.05] | -3.63 / -2.69 | **-4.00%** [-7.29, -0.62] | -6.54 / -1.48 |
| build (17:00 ≥ 16:30) | 244 | -2.31% [-5.85, +1.63] | -0.37 / -4.25 | -3.37% [-7.56, +1.17] | -4.61 / -2.14 |
| fresh (not a multi-session runner) | 456 | -3.64% [-6.61, -0.13] | -4.07 / -3.22 | -4.31% [-7.80, -0.75] | -6.67 / -1.96 |
| build ∩ fresh | 221 | -2.69% [-6.46, +1.70] | -0.61 / -4.76 | -3.52% [-7.90, +1.16] | -4.42 / -2.63 |

**No cell passes. Every mean and every half is negative.** The win rate is 27–33%, and the median trade loses 5–7%. With the +100 bps stress, means fall to -3.3% to -5.3%. Even before costs (mid to mid), the full set loses -1.79% to the 04:30 mid and -3.06% to the open. The loss is in the price move itself; the spread is only part of it.

**Descriptive only:**

- No bucket of move size, price or AH dollar volume has a positive mean.
- The best bucket is +50–150% movers at 04:30, at -1.1% (n=75, halves +2.2 / -4.4).
- Thin names are the worst: under $1M of AH dollars, n=37, -7.8% to -11.2%.
- Events per month are steady at 23–62, about 2 per session.
- The distribution has a fat right tail: IPST +187%, SDOT +141%, AMST +128%. These trades do not outweigh the losses.

**Agreement with live trading:**

- The census catches 45 of the 89 real paper entries. On those 45, it scores -3.45% at the 04:30 bid; the real entries modeled at the 04:30 open score -2.49%.
- The 44 real entries that the census does not catch model at +1.02%. Most were entered later (17:30–18:30 ET) or crossed +10% after 16:30. This is a descriptive difference on 44 trades with no interval, so it is not evidence of an edge.

**Verification:**

- Two trades were checked by hand: STKH (October 2, 2025: ask $4.97, 04:30 bid $4.75, -4.43%) and CCM (October 17, 2025: ask $6.77, 04:30 bid $4.01, -40.8%).
- On October 1–3, a verification run produced the same 6 events as the full run.

## Finding

The core strategy's 17:00 ET entry loses about 3% per trade at the live exit, in every frozen subset and in both halves of the year. This matches the 89 real entries. Under the freeze, the result leads to a proposal to Juan to stop or replace AH→PM.

One part of the live strategy is untested: entries at 17:30–18:30 ET on names that ignite after 16:30. The 44 unmatched real entries point there. They are descriptive, so that variant needs its own frozen test before it can count.

## Limits

- Entries are at 17:00 ET only.
- There is no catalyst grading and no market-cap filter.
- Survivorship covers only the assets that Alpaca lists.
- Quoted size and partial fills are ignored.
- The open exit uses a flat 50 bps auction slip.
