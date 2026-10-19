# Initiative 7: micro-cap short fade, prior-year result (2026-10-19)

Test frozen in `docs/investigations/init7-microcap-short-fade-freeze.json` (2026-10-16 13:15 UTC). Data fetched by gob `KaJ` (finished 2026-10-16 20:50 CEST). Result: `log/2026-10-16/init7-short-fade/result.json`; scored rows in `events.json.gz`.

## Result

872 of 889 events scored (16 without an entry quote, 1 split; 19 used the open fallback at 04:30). Short at the scan bid, 25 bps borrow per night, Bonferroni over 4 cells.

| Cell | n | Base mean | Interval | Halves | Pass | Stress mean |
|---|---|---|---|---|---|---|
| all / cover 04:30 ask | 872 | -0.72% | [-3.46, +1.51] | -0.55 / -0.89 | no | -2.72% |
| **all / cover at open** | 872 | **+3.24%** | **[+1.09, +5.54]** | +4.00 / +2.49 | **yes** | +1.25% [-0.93, +3.57] |
| etb / cover 04:30 ask | 195 | -2.84% | [-5.27, -0.68] | -3.25 / -2.44 | no | -4.72% |
| etb / cover at open | 195 | -1.19% | [-4.27, +1.62] | -1.65 / -0.74 | no | -3.08% |

Gross mid to mid: all events fade +1.57% by 04:30 and +4.73% by the open; ETB names fade +0.28% by the open. Worst 1% of trades in the passing cell: -98.7%.

The 15:00 Oct 16 hypothesis held exactly: the open-cover cell on all events passes, the 04:30 cell does not, and the ETB cells do not.

## Reading under the rule fixed before the result

The October 16 18:00 rule says only the `etb` cells count as executable on the Alpaca paper account. Both fail, and the 04:30 ETB cell is significantly negative. **The short fade is not tradable on this account.** The passing cell needs hard-to-borrow shorts: every recent live entry (YYAI, AGMH, AEHL, NCPL, TCRT, XXII, FCHL, BKYI, CIGL, DKI) is not shortable on Alpaca, and paper has no locate API.

The pass is also thin against borrow cost. The stress case (+100 bps round trip, 100 bps per night) drops it to +1.25% with an interval spanning zero. Hot micro-caps after a 25%+ spike often carry borrow fees above the 91% a year assumed here, plus per-share locate fees (a $0.05 locate on a $2 stock is 2.5%), so the real HTB edge is likely near zero.

Descriptive (cannot rescue a cell): the fade at the open is concentrated in moves of 25% or more (25-50%: +4.55%, 50-150%: +9.40%) and closes under $1 (+7.13%); moves of 10-25% do not fade (+0.71%).

## Decision

Per the freeze, `decision_if_pass` applies to `all/exit_open`, but the pre-fixed executability rule blocks a paper pilot: Alpaca cannot short these names. No pilot, order, rule or pulse change. The finding goes to Juan in the daily email as information for the stop-or-replace decision: the overnight fade in these names is real (about 4.7% to the open before costs), so **buying them is structurally a losing trade**, and the only way to monetise the fade is a broker with hard-to-borrow locates (Initiative 2, deferred), whose fees likely eat it.
