# Initiative 7 — D+1 regular-session long on micro-cap AH movers (2026-10-20)

**Result: fails in all four frozen cells.** Buying the 872 prior-year scan events at the D+1 official open (+50 bps) and selling at the D+1 or D+2 close (-50 bps) loses money. The D+1 lane is closed for these events.

- Freeze: `docs/investigations/init7-d1-session-long-freeze.json` (13:01:50 UTC, before any D+1/D+2 session return was computed; no new fetch)
- Script: `scripts/init7-d1-session-long.py`
- Output: `log/2026-10-20/init7-d1-session-long/result.json`, `rows.json.gz`

## Frozen cells (861 scored; 10 missing bars, 1 split dropped)

| Cell | n | Mean | Interval (Bonferroni /4) | Halves | Win rate | Stress (-100 bps) |
|---|---|---|---|---|---|---|
| all / D+1 close | 861 | -0.74% | [-3.53, +4.49] | -0.11 / -1.37 | 38.6% | -1.74% |
| all / D+2 close | 861 | -5.13% | [-7.89, -0.79] | -5.25 / -5.01 | 30.5% | -6.13% |
| gap_up / D+1 close | 732 | -0.20% | [-3.35, +6.27] | +1.08 / -1.48 | 39.2% | -1.20% |
| gap_up / D+2 close | 732 | -4.71% | [-7.82, +0.40] | -3.88 / -5.54 | 30.2% | -5.71% |

Gross open to D+1 close is +0.26% [-2.56, +5.54]; open to D+2 close is -4.18%.

## What drives it

- **One outlier carries the D+1 mean.** DRUG 2024-10-14 (Bright Minds, epilepsy data) opened $2.62 on D+1 and closed $38.49, +1,354% net. Without it, all / D+1 close is **-2.31%** per trade. The median trade is about -4%.
- **Holding a second session loses about 5%.** The fade continues past D+1.
- **Large gaps lose most.** D+1 gap above +50% over the D close: -8.95% [-13.6, -3.5] at the D+1 close (n=108). Gaps of 0–50% sit near zero with intervals spanning it.
- **ETB names (n=194):** +7.40% mean, but DRUG is ETB; without it +0.42%, median -1.57%.
- **Short mirror at D+1 close:** -1.27% all, -9.57% ETB (DRUG again). No short edge in the regular session either.

## Hypothesis check

The frozen hypothesis said all four cells fail and gap_up loses more than all. All four fail. The second part was wrong: gap_up loses slightly less (-0.20% against -0.74%), because the 117 names that open below the D close lose -3.0%.

## Decision (frozen rule)

The D+1 regular-session long lane is closed. The long side of these micro-cap events has now failed at every horizon tested on the prior year: 17:00 ET scan, 17:30–18:30 ET late entry, ignition bar, 04:30, the D+1 open, take-profit limits, the D+1 close and the D+2 close. This joins the stop-or-replace ask to Juan.

## Limits

Official open and close prints stand in for fills; 50 bps understates cost on the widest books. ETB is today's flag. No intraday stop or target was modelled. Survivorship is limited to assets Alpaca still lists.
