# Initiative 6 pilot and Initiative 3 replay — October 2 15:00 CEST

## Decisions

SGRX supplies new pilot discovery evidence: it was absent from the frozen cohort, and its available completed tape has no 3,000-trade ignition. No new modeled admission is justified at this cutoff. Finalize after the completed PM window at the 18:00 run.

The resumed AH replay supplies no positive evidence for a schedule or entry promotion. The first-ignition test rejects AMOD's initial signal and does not re-test its later rebuild. That missed rebuild is an open research question, separate from cadence. Existing scan-retirement and exit proposals remain unapplied.

## Initiative 6 — SGRX

`python3 scripts/init6-cohort-audit.py 2026-10-02` reports a frozen **04:10:23 ET / 17-name** cohort. Of four later selected tracker names, SDEV and QTEX were captured; AMOD and the sole PM-only observation SGRX were absent. All 17 snapshot quotes had ages; zero asks had positive size and age <=60 seconds, with ages 42,070–43,831 seconds. This is one selected PM-only discovery miss, not an estimate of whole-universe recall. Untracked cohort outcomes remain unclassified.

Explicit SIP five-minute bars were fetched with:

```bash
node scripts/broker.js bars SGRX --tf 5Min --start 2026-10-02T08:00:00Z --limit 1000 --feed sip --json
```

The dated archive `log/2026-10-02/init6-SGRX-audit-1500.json` retains **58 completed bars**, 04:00–08:45 ET (through 08:50 ET bar end). It uses file-written observation time minus 16 minutes and includes only bars whose five-minute end precedes that cutoff. Maximum trades per bar = **2,651**, below the frozen **3,000-trade ignition**. Thus no ignition, confirmations or entry exist in the observed window. Its last close was **$1.68**. The full 09:30 ET PM window and delayed final SIP delivery remain pending; no final exit or return is recorded.

A separate later IEX quote returned **$1.76 x100 bid / $1.77 x100 ask at 13:01:24.684524179 UTC**, approximately **0.103 seconds old** when the response file was written. This proves that the later displayed book had become fresh; it cannot reconstruct the 04:10 ask or an entry fill. The cohort's stale snapshot cannot be generalized to every later quote.

The script's post-session `holdable` label is not a causal entry rule. Preserve the existing 26-admit completed ledger until a qualifying completed case exists; check SGRX again at **October 2 18:00** for any later ignition and final window. No order or pilot promotion was made.

## Initiative 3 — completion and complete AH replay

The live scheduler was read directly at `/home/juan/workspace/juanibiapina/agent/apps/bot/.local/share/agent/scheduler.json`. All **12 AH scan sessions** from October 1 22:00 CEST through October 2 00:30 CEST reached a final assistant response with `stopReason=stop` and **zero assistant errors**, including all four eligible entry sessions. Evidence is `log/2026-10-02/init3-session-completion.json`; text/errors were read with `scripts/pi-session-text.py`. The September 29 authentication interruption did not recur in this window. This does not establish a causal benefit from retiring observation scans.

Replayed **11 scanner names with at least one >10% AH appearance**, plus QTEX and SMX as retrospective tail/thin controls, using `scripts/ah-5m-confirmation-replay.js`. The AH window is complete. October 2 PM high outcomes were still interim at retrieval; the next PM-open level is already known.

| Variant | Admissions in 13 selected cases | Relevant result |
|---|---|---|
| Second bar | 0 | No new timing comparison |
| Third bar | 1, IPW | Modeled 17:30 ET entry $1.40; legal-grid entry also $1.40; next PM-open return −18.6%; interim PM-high ceiling −10.7% |

AMOD ignited at 16:15, but both variants rejected its initial confirmation. Its later rebuild was excluded by this variant's first-ignition design. SORA/WCT had no eligible local-volume new-high ignition. TARA supplied only two AH bars and is insufficient data. Full per-case rows and limitations are in `log/2026-10-02/init3-opening-replay-1500.json`.

The completed **September 30 AH / October 1 PM** reference replay is archived separately in `log/2026-10-02/init3-sep30-replay.json`. Both variants admit only WETO in its selected 11-case cohort. Second-bar modeled entry $1.22 yields −4.9% to PM open versus $1.15 / +0.9% at the current legal grid; third-bar $1.16 yields 0.0%. Earlier modeled entries were more expensive on this control. BOXL has only one AH bar and is insufficient data.

The CLI's winner/fade denominators are fixed to its original fixture, so those aggregate lines are excluded from the custom-cohort evidence. It also uses active preceding bars and rounded CLI prices, unlike the newly shared exact-slot volume metric. Neither replay measures profitable fills, actual data-arrival time at the modeled next-open entry, whole-universe recall or a frozen prospective strategy.

At **18:00**, finalize October 2 PM outcomes and check SGRX. The next Initiative 3 research delivery is a causal later-rebuild comparison using archived shared measurements before proposing a rule. New exit seeding waits for an actual fill; latest fill remains TOPS on September 23. DST mismatch jobs need a bridge loading check before October 25. Broker testing remains deferred at Juan's request.
