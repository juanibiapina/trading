# Init 1 — Does volume lead price? (earlier volume-lead entries)

Research artifact for Initiative 1. Juan's idea: "we catch spikes late, once
they are already +50-100%. Charts suggest a volume surge precedes the price
explosion. If we detect the volume ramp (~10x normal) we could enter earlier."

**Tool:** `scripts/volume-lead.js` (log-only, no orders). For a ticker + AH-
evening date D it pulls real Alpaca SIP 5-min bars across the AH session
(D 16:00–20:00 ET) and the next-morning premarket (D+1 04:00–09:30 ET), baseline
= the regular-session close on D, and records the first bar where price crosses
+20% / +50% vs the first bar where per-bar volume crosses K× the median of the
first N bars. `LEAD = t(price+20%) − t(volSurge)`; positive => volume led.

## Batch (2026-07-15, K=5×, N=4)

| sym  | date       | peak   | volSurge first | price+20% first | LEAD    | class        |
|------|------------|--------|----------------|-----------------|---------|--------------|
| IVF  | 2026-06-25 | +109%  | 17:00 ET       | 16:50 ET        | −10 min | AH mover     |
| VTAK | 2026-06-23 | +121%  | 16:45 ET       | 16:45 ET        | 0 min   | AH mover     |
| EDHL | 2026-07-06 | +59%   | 17:05 ET       | 16:10 ET        | −55 min | AH mover     |
| MSW  | 2026-06-08 | +33%   | 19:00 ET       | 19:00 ET        | 0 min   | AH mover     |
| GLXG | 2026-06-10 | +485%  | 19:20 ET (AH)  | 04:00 ET (PM)   | +520 min| PM gapper*   |
| CIIT | 2026-06-09 | +583%  | 17:55 ET (AH)  | 04:00 ET (PM)   | +605 min| PM gapper*   |
| SUNE | 2026-07-07 | +3%    | 16:00 ET       | never           | n/a     | no move      |

\* The GLXG/CIIT "leads" are **false positives.** Their flagged AH-evening
"surge" bars are thin noise — a few hundred to ~4k shares on 1–40 trades, with
price flat ($0.94–1.10 / $1.16–1.41). The 5× threshold fired only because the
quiet-baseline median was tiny. The real move is a news-driven PM explosion at
04:00 ET with **no tradeable AH precursor** (consistent with Init 6: the AH
scanner structurally cannot front-run PM-only gappers).

## Key finding: ignition is a single-minute co-spike, not a volume ramp

Zoomed IVF (2026-06-25) to **1-min** SIP bars around the AH open:

```
16:00–16:52 ET   100–300 sh, 1 trade/min, price flat $1.20–1.24   (dead)
16:53 ET         25,450 sh, 72 trades, $1.24 -> $1.48  (+19% SAME minute)  <-- ignition
16:54–17:09 ET   10k–195k sh/min, ramping to $1.65
```

The move ignites in one minute that carries **both** the volume spike and the
+19% price jump. There is no quiet volume ramp *before* the price move to front-
run. Across the batch every real AH mover has LEAD ≈ 0 or negative (price
reaches +20% at or before the volume threshold). At both 5-min and 1-min
resolution, **volume does not lead price** on our winners.

## Conclusion

The specific Init 1 hypothesis — a pre-explosion volume ramp gives an earlier
entry — is **falsified** on this sample. Volume and price ignite together in a
single minute, so a volume-first trigger buys no lead time over a price-first
trigger.

**Reframe (why "we catch late" is still real, and the actual lever):** IVF
ignited at **16:53 ET**, but our AH scan runs ~22:15 CET = **16:15 ET**, ~38 min
*before* ignition — so the scan sees IVF flat and the ignition is missed until a
later scan, by which point it is already +50-100%. The gap is not a missing
lead-signal; it is **monitoring frequency / scan timing** — catching the
ignition minute (a volume+price co-spike) quickly. That is Initiative 3
(adaptive scheduling) territory, plus a possible real-time volume-spike alert,
not a volume-lead entry rule. Init 1 as originally framed does not carry an edge;
its value folds into Init 3.

**Caveats:** n=4 real AH movers (decisive on the clearest, IVF; consistent
across the rest). Free-tier SIP historical bars used; no NBBO. A larger sample
would firm the "co-spike, no lead" result, but the mechanism (single-minute
ignition) is clean enough to reprioritize on.
