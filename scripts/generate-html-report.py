#!/usr/bin/env python3
"""Build a static daily review report for GitHub Pages."""

from __future__ import annotations

import argparse
import html
import json
import re
from datetime import date
from pathlib import Path

from volume_metric import VERSION, VERSION_V2, timestamp

ROOT = Path(__file__).resolve().parents[1]
LOG_ROOT = ROOT / "log"
REPORT_ROOT = ROOT / "reports"
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def available_dates() -> list[str]:
    return sorted(
        (
            entry.name
            for entry in LOG_ROOT.iterdir()
            if entry.is_dir() and DATE_RE.fullmatch(entry.name) and (entry / "log.md").is_file()
        ),
        reverse=True,
    )


def choose_date(value: str | None) -> str:
    if value:
        try:
            date.fromisoformat(value)
        except ValueError as exc:
            raise SystemExit(f"invalid date: {value}") from exc
        if not (LOG_ROOT / value / "log.md").is_file():
            raise SystemExit(f"no daily log found for {value}")
        return value

    dates = available_dates()
    if not dates:
        raise SystemExit("no dated daily logs found")
    return dates[0]


def volume_context_html(paths: list[Path]) -> str:
    sections = []
    for path in paths:
        result = json.loads(path.read_text(encoding="utf-8"))
        version = result["metric_version"]
        if version not in (VERSION, VERSION_V2):
            raise ValueError(f"Unsupported volume metric: {path}")
        v2 = version == VERSION_V2
        as_of = timestamp(result["as_of_utc"])
        rows = []
        for row in result["rows"]:
            if timestamp(row["bar_end_utc"]) > as_of:
                raise ValueError(f"Incomplete volume bar: {path}")
            ratio = lambda value: "unknown" if value is None else f"{value:.4f}x"
            median = row["baseline_median_shares"] if v2 else row["baseline_shares"]
            baseline = "unknown" if median is None else f"{median:,.0f}"
            values = (row["bar_et"], f"{row['shares']:,}", baseline, ratio(row["local_ratio"]),
                      ratio(row["prior_peak_ratio"]), ratio(row.get("rth_peak_ratio")), row["local_status"])
            cells = "".join(f"<td>{html.escape(str(value))}</td>" for value in values)
            rows.append(f'<tr data-bar-start-utc="{html.escape(row["bar_start_utc"])}">{cells}</tr>')
        sections.append(
            f'<section><h3>{html.escape(result["symbol"])} — {html.escape(result["date"])} AH</h3>'
            f'<p>Metric {html.escape(version)}. Previous AH: {html.escape(result["prior_date"])}; '
            f'{result["prior_observed_slots"]}/{result["prior_expected_slots"]} observed bars'
            + (f', {result["prior_inferred_zero_slots"]} inferred zero-trade bars; ratios floor the '
               f'denominator at {result["floor_shares"]:,} shares. ' if v2 else '. ') +
            f'Reconstructed through {html.escape(result["as_of_utc"])}; '
            f'data fetched {html.escape(result["source_observed_utc"])}.</p>'
            '<table><thead><tr><th>Bar start ET</th><th>Shares</th><th>Prior 3-bar median</th>'
            '<th>Local ratio</th><th>Prior AH peak ratio</th><th>Same-date regular peak ratio</th><th>Coverage status</th></tr></thead>'
            f'<tbody>{"".join(rows)}</tbody></table></section>'
        )
    if not sections:
        return ""
    return ('<h2>AH volume context</h2><p>Observation only. Local ratio compares raw SIP shares with the '
            'median of three preceding five-minute bars. Prior ratio compares with the largest bar in the '
            'complete previous AH session. Under v1, missing data or a zero baseline yields unknown; v2 counts '
            'absent bars inside the fetched span as zero trades and floors denominators at 100 shares. '
            'Historical reconstruction does not prove availability at the bar close.</p>' + "".join(sections))


def report_html(day: str, log_text: str, charts: list[Path], volume_context: str = "") -> str:
    escaped_day = html.escape(day)
    chart_markup = "\n".join(
        f'<figure><img src="../../log/{escaped_day}/{html.escape(chart.name)}" '
        f'alt="{html.escape(chart.stem)} chart"><figcaption>{html.escape(chart.name)}</figcaption></figure>'
        for chart in charts
    )
    if not chart_markup:
        chart_markup = "<p>No chart images were generated for this cycle.</p>"

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Trading review {escaped_day}</title>
  <style>
    :root {{ color-scheme: light dark; }}
    body {{ font: 16px/1.5 system-ui, sans-serif; margin: 0 auto; max-width: 1100px; padding: 24px; }}
    a {{ color: #2f6feb; }}
    figure {{ display: inline-block; margin: 0 16px 16px 0; vertical-align: top; width: min(100%, 560px); }}
    img {{ border: 1px solid #888; max-width: 100%; height: auto; }}
    figcaption {{ font-size: 0.85rem; margin-top: 4px; }}
    table {{ border-collapse: collapse; width: 100%; font-size: 0.85rem; }}
    td, th {{ padding: 6px; border-bottom: 1px solid #888; text-align: right; }}
    section {{ overflow-x: auto; }}
    pre {{ background: #222; border-radius: 6px; overflow-x: auto; padding: 16px; white-space: pre-wrap; }}
  </style>
</head>
<body>
  <header>
    <h1>Trading review: {escaped_day}</h1>
    <p><a href="https://github.com/juanibiapina/trading/blob/main/log/{escaped_day}/log.md">Open source log</a></p>
  </header>
  <main>
    <h2>Charts</h2>
    {chart_markup}
    {volume_context}
    <h2>Daily log</h2>
    <pre>{html.escape(log_text)}</pre>
  </main>
</body>
</html>
"""


def write_index(days: list[str]) -> None:
    items = "\n".join(
        f'<li><a href="{html.escape(day)}/index.html">Trading review {html.escape(day)}</a></li>'
        for day in days
    )
    (REPORT_ROOT / "index.html").write_text(
        f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Trading reviews</title></head><body><h1>Trading reviews</h1><ul>{items}</ul></body></html>
""",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", help="daily log date; defaults to the newest dated log")
    parser.add_argument("--volume-metric", type=Path, action="append", default=[],
                        help="include shared metric JSON; dated *-volume-metric.json artifacts also opt in")
    args = parser.parse_args()

    day = choose_date(args.date)
    log_dir = LOG_ROOT / day
    charts = sorted(log_dir.glob("*.png"))
    metric_paths = sorted({path.resolve() for path in [*log_dir.glob("*-volume-metric.json"), *args.volume_metric]})
    volume_context = volume_context_html(metric_paths)
    output_dir = REPORT_ROOT / day
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "index.html").write_text(
        report_html(day, (log_dir / "log.md").read_text(encoding="utf-8", errors="replace"), charts, volume_context),
        encoding="utf-8",
    )
    write_index(sorted({entry.name for entry in REPORT_ROOT.iterdir() if entry.is_dir() and DATE_RE.fullmatch(entry.name)}, reverse=True))
    print(f"wrote reports/{day}/index.html ({len(charts)} charts)")


if __name__ == "__main__":
    main()
