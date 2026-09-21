#!/usr/bin/env python3
"""Build a static daily review report for GitHub Pages."""

from __future__ import annotations

import argparse
import html
import re
from datetime import date
from pathlib import Path

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


def report_html(day: str, log_text: str, charts: list[Path]) -> str:
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
    args = parser.parse_args()

    day = choose_date(args.date)
    log_dir = LOG_ROOT / day
    charts = sorted(log_dir.glob("*.png"))
    output_dir = REPORT_ROOT / day
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "index.html").write_text(
        report_html(day, (log_dir / "log.md").read_text(encoding="utf-8", errors="replace"), charts),
        encoding="utf-8",
    )
    write_index(sorted({entry.name for entry in REPORT_ROOT.iterdir() if entry.is_dir() and DATE_RE.fullmatch(entry.name)}, reverse=True))
    print(f"wrote reports/{day}/index.html ({len(charts)} charts)")


if __name__ == "__main__":
    main()
