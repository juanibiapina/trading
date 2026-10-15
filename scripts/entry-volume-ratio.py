#!/usr/bin/env python3
"""Report the same-date regular-session volume ratio a fill could see at entry.

Reads the archived evening `SYM-HHMM-volume-metric.json` files (sip-ah-volume-v2)
in log/DATE/ and picks the latest one written at or before the fill's ET time.
Prints the largest completed AH bar's `rth_peak_ratio` (AH bar shares over the
largest 5-minute bar of the same date's 09:30-16:00 ET regular session).

Log-only evidence for the morning evaluation's volume-spike entry tracker; it
does not fetch data and does not gate entries.

Usage: entry-volume-ratio.py SYM DATE FILL_HHMM_ET [SYM DATE FILL_HHMM_ET ...]
Example: entry-volume-ratio.py BKYI 2026-10-13 1832
"""
import glob
import json
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def report(sym, date, fill_hhmm):
    pattern = os.path.join(REPO, "log", date, f"{sym}-[0-9][0-9][0-9][0-9]-volume-metric.json")
    files = []
    for path in glob.glob(pattern):
        hhmm = os.path.basename(path)[len(sym) + 1:len(sym) + 5]
        if hhmm <= fill_hhmm:
            files.append((hhmm, path))
    if not files:
        return f"{sym} {date} fill {fill_hhmm} ET: unknown (no volume-metric file at or before the fill)"
    hhmm, path = max(files)
    with open(path) as fh:
        data = json.load(fh)
    rel = os.path.relpath(path, REPO)
    if data.get("metric_version") != "sip-ah-volume-v2" or data.get("rth_peak_shares") is None:
        return f"{sym} {date} fill {fill_hhmm} ET: unknown (no rth_peak_shares in {rel})"
    rows = [r for r in data.get("rows", []) if r.get("rth_peak_ratio") is not None]
    if not rows:
        return f"{sym} {date} fill {fill_hhmm} ET: unknown (no completed AH bars in {rel})"
    top = max(rows, key=lambda r: r["rth_peak_ratio"])
    ratio = top["rth_peak_ratio"]
    bucket = "<2x" if ratio < 2 else ("2-10x" if ratio < 10 else ">=10x")
    complete = "" if data.get("rth_complete") else " (regular session incomplete: unverified)"
    return (
        f"{sym} {date} fill {fill_hhmm} ET: max rth-peak {ratio:.2f}x [{bucket}] "
        f"at {top['bar_et']} ET ({top['shares']:,} sh vs regular-session peak "
        f"{data['rth_peak_shares']:,} sh), last bar {rows[-1]['bar_et']} ET; "
        f"source {rel}{complete}"
    )


def main(argv):
    if len(argv) < 3 or len(argv) % 3 != 0 or argv[0] in ("-h", "--help"):
        print(__doc__.strip())
        return 0 if argv[:1] in (["-h"], ["--help"]) else 2
    for i in range(0, len(argv), 3):
        sym, date, fill = argv[i].upper(), argv[i + 1], argv[i + 2].replace(":", "")
        print(report(sym, date, fill))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
