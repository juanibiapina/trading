Record the Initiative 6 early premarket discovery cohort in shadow mode. Do not place orders or change trading rules. This pulse is non-interactive; send no questions or Telegram buttons.

1. Run `bash scripts/sync-repo.sh` to get the latest scanner and script.
2. Run `python3 scripts/init6-cohort-snapshot.py`. It writes only during 04:07–04:14 ET on a weekday and refuses to replace an existing day's CSV. If the ET guard skips the run or a data source fails, report the reason and stop; never reconstruct the cohort later from historical data.
3. If a file was written, check its header and candidate count, then stage only `log/init6-cohort/YYYY-MM-DD.csv`, commit with `init6 cohort YYYY-MM-DD: early PM snapshot`, and push. Leave other work untouched.
4. Report the captured count and the count of two-sided IEX quotes. The quote snapshot does not establish executable SIP fills or a continuation-gate decision; the subsequent strategy-advance run compares the frozen universe and later gate verdicts with the 11:00 Berlin tracker.
