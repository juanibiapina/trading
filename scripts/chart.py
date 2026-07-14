#!/usr/bin/env python3
"""
chart.py - render a 5m + volume candlestick chart for review (Initiative 5).

Dependency-free: fetches Yahoo bars (incl. pre/post market), draws an SVG, and
converts it to PNG with ImageMagick `convert`. AH and PM sessions are shaded so
the AH->PM pattern is visible at a glance.

Usage:
    python3 scripts/chart.py TICKER [--interval 5m] [--range 2d] [--out PATH]

Examples:
    python3 scripts/chart.py ORIS --range 2d --out /tmp/ORIS.png
    python3 scripts/chart.py VTAK --interval 5m --range 2d
"""

import argparse
import datetime as dt
import json
import shutil
import subprocess
import sys
import os
import re
import urllib.request

W, H = 1100, 560
ML, MR, MT, MB = 64, 16, 36, 28          # margins
VOL_FRAC = 0.24                          # bottom fraction for volume panel
GREEN, RED = "#2e7d32", "#c62828"
AH_FILL, PM_FILL = "#fff4e0", "#e8f0fe"  # post (amber), pre (blue) shading
GRID = "#e6e6e6"


def fetch(ticker, interval, rng, prepost):
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
           f"?interval={interval}&range={rng}&includePrePost={'true' if prepost else 'false'}")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=20) as r:
        data = json.load(r)
    res = data["chart"]["result"][0]
    ts = res["timestamp"]
    q = res["indicators"]["quote"][0]
    off = res["meta"].get("gmtoffset", 0)  # seconds; exchange local = utc + off
    bars = []
    for i, t in enumerate(ts):
        o, h, l, c, v = q["open"][i], q["high"][i], q["low"][i], q["close"][i], q["volume"][i]
        if None in (o, h, l, c):
            continue
        local = dt.datetime.fromtimestamp(t + off, dt.timezone.utc).replace(tzinfo=None)
        bars.append({"o": o, "h": h, "l": l, "c": c, "v": v or 0, "t": local})
    return bars, res["meta"]


def backfill_ext_volume(ticker, bars, meta):
    """Yahoo reports vol=0 for every extended-hours 5m bar, which blanks the
    volume panel in exactly the AH/PM window our edge lives in. Fill those bars
    from Alpaca SIP 5m bars (real ext-hours volume) via broker.js, matched by
    timestamp. Degrades silently to Yahoo volume if Alpaca is unavailable."""
    off = meta.get("gmtoffset", 0)  # exchange local = utc + off
    # earliest bar -> utc start for the Alpaca pull
    start_utc = min(b["t"] for b in bars) - dt.timedelta(seconds=off)
    start_iso = start_utc.strftime("%Y-%m-%dT%H:%M:%SZ")
    here = os.path.dirname(os.path.abspath(__file__))
    try:
        out = subprocess.run(
            ["node", os.path.join(here, "broker.js"), "bars", ticker,
             "--tf", "5Min", "--start", start_iso, "--limit", "600", "--feed", "sip"],
            capture_output=True, text=True, timeout=40,
        ).stdout
    except Exception:
        return 0
    # parse "2026-07-13T08:00:00Z  O $.. H $.. L $.. C $..  vol N  vwap $..  trades N"
    vol_by_local = {}
    rx = re.compile(r"^(\S+Z)\s+O \$[\d.]+ H \$[\d.]+ L \$[\d.]+ C \$[\d.]+\s+vol (\d+)")
    for line in out.splitlines():
        m = rx.match(line)
        if not m:
            continue
        u = dt.datetime.strptime(m.group(1), "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=None)
        local = u + dt.timedelta(seconds=off)
        vol_by_local[local] = int(m.group(2))
    filled = 0
    for b in bars:
        if b["v"] == 0 and b["t"] in vol_by_local:
            b["v"] = vol_by_local[b["t"]]
            filled += 1
    return filled


def session(t):
    """Classify exchange-local time into pre / regular / post."""
    m = t.hour * 60 + t.minute
    if m < 9 * 60 + 30:
        return "pre"
    if m < 16 * 60:
        return "regular"
    return "post"


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build_svg(ticker, bars, meta):
    n = len(bars)
    if n == 0:
        return None
    px_top, px_bot = MT, int(H - MB - (H - MT - MB) * VOL_FRAC) - 8
    vol_top, vol_bot = px_bot + 8, H - MB
    plot_l, plot_r = ML, W - MR
    pw = plot_r - plot_l

    lo = min(b["l"] for b in bars)
    hi = max(b["h"] for b in bars)
    pad = (hi - lo) * 0.06 or hi * 0.02
    lo -= pad
    hi += pad
    vmax = max(b["v"] for b in bars) or 1

    step = pw / n
    bw = max(1.2, step * 0.62)

    def x(i):
        return plot_l + step * (i + 0.5)

    def yp(p):
        return px_top + (hi - p) / (hi - lo) * (px_bot - px_top)

    def yv(v):
        return vol_bot - (v / vmax) * (vol_bot - vol_top)

    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}" font-family="Arial,Helvetica,sans-serif">']
    s.append(f'<rect width="{W}" height="{H}" fill="white"/>')

    # session shading (contiguous runs)
    i = 0
    while i < n:
        sess = session(bars[i]["t"])
        j = i
        while j < n and session(bars[j]["t"]) == sess:
            j += 1
        if sess in ("pre", "post"):
            x0 = plot_l + step * i
            x1 = plot_l + step * j
            fill = PM_FILL if sess == "pre" else AH_FILL
            s.append(f'<rect x="{x0:.1f}" y="{MT}" width="{x1-x0:.1f}" '
                     f'height="{vol_bot-MT:.1f}" fill="{fill}"/>')
        i = j

    # price gridlines + labels (5 levels)
    for k in range(5):
        p = lo + (hi - lo) * k / 4
        yy = yp(p)
        s.append(f'<line x1="{plot_l}" y1="{yy:.1f}" x2="{plot_r}" y2="{yy:.1f}" stroke="{GRID}"/>')
        s.append(f'<text x="{plot_l-6}" y="{yy+3:.1f}" font-size="10" fill="#666" text-anchor="end">${p:.2f}</text>')

    # candles
    for idx, b in enumerate(bars):
        cx = x(idx)
        up = b["c"] >= b["o"]
        col = GREEN if up else RED
        s.append(f'<line x1="{cx:.1f}" y1="{yp(b["h"]):.1f}" x2="{cx:.1f}" y2="{yp(b["l"]):.1f}" stroke="{col}" stroke-width="1"/>')
        y0, y1 = yp(b["o"]), yp(b["c"])
        top, ht = min(y0, y1), max(1.0, abs(y1 - y0))
        s.append(f'<rect x="{cx-bw/2:.1f}" y="{top:.1f}" width="{bw:.1f}" height="{ht:.1f}" fill="{col}"/>')
        # volume
        s.append(f'<rect x="{cx-bw/2:.1f}" y="{yv(b["v"]):.1f}" width="{bw:.1f}" height="{vol_bot-yv(b["v"]):.1f}" fill="{col}" opacity="0.55"/>')

    # volume panel border + max label
    s.append(f'<line x1="{plot_l}" y1="{vol_bot}" x2="{plot_r}" y2="{vol_bot}" stroke="#ccc"/>')
    s.append(f'<text x="{plot_l-6}" y="{vol_top+8}" font-size="9" fill="#999" text-anchor="end">{vmax/1e6:.1f}M</text>')

    # time axis labels (~6 ticks, day boundaries get a date)
    ticks = max(1, n // 6)
    last_day = None
    for idx in range(0, n, ticks):
        b = bars[idx]
        cx = x(idx)
        lbl = b["t"].strftime("%H:%M")
        if b["t"].date() != last_day:
            lbl = b["t"].strftime("%m/%d %H:%M")
            last_day = b["t"].date()
        s.append(f'<line x1="{cx:.1f}" y1="{vol_bot}" x2="{cx:.1f}" y2="{vol_bot+4}" stroke="#999"/>')
        s.append(f'<text x="{cx:.1f}" y="{vol_bot+15:.1f}" font-size="9" fill="#666" text-anchor="middle">{lbl}</text>')

    # title + legend
    first, last = bars[0]["c"], bars[-1]["c"]
    chg = (last / bars[0]["o"] - 1) * 100
    name = esc(meta.get("longName") or ticker)
    s.append(f'<text x="{plot_l}" y="22" font-size="15" font-weight="bold" fill="#1a1a1a">{esc(ticker)} - {name}</text>')
    s.append(f'<text x="{plot_r}" y="22" font-size="11" fill="#666" text-anchor="end">last ${last:.2f} ({chg:+.1f}% over window)</text>')
    s.append('<rect x="%d" y="28" width="10" height="8" fill="%s"/>' % (plot_r-150, PM_FILL))
    s.append(f'<text x="{plot_r-136}" y="35" font-size="9" fill="#666">premarket</text>')
    s.append('<rect x="%d" y="28" width="10" height="8" fill="%s"/>' % (plot_r-78, AH_FILL))
    s.append(f'<text x="{plot_r-64}" y="35" font-size="9" fill="#666">after-hrs</text>')

    s.append('</svg>')
    return "\n".join(s)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ticker")
    ap.add_argument("--interval", default="5m")
    ap.add_argument("--range", dest="rng", default="2d")
    ap.add_argument("--no-prepost", action="store_true")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()

    bars, meta = fetch(a.ticker, a.interval, a.rng, not a.no_prepost)
    if not bars:
        print(f"No bars for {a.ticker}", file=sys.stderr)
        sys.exit(1)
    if not a.no_prepost:
        n = backfill_ext_volume(a.ticker.upper(), bars, meta)
        if n:
            print(f"backfilled {n} ext-hours volume bars from Alpaca SIP", file=sys.stderr)
    svg = build_svg(a.ticker.upper(), bars, meta)

    out = a.out or f"/tmp/{a.ticker.upper()}-chart.png"
    svg_path = out.rsplit(".", 1)[0] + ".svg"
    with open(svg_path, "w") as f:
        f.write(svg)
    if out.endswith(".png"):
        tool = "magick" if shutil.which("magick") else "convert"
        subprocess.run([tool, "-density", "120", svg_path, out], check=True)
        print(out)
    else:
        print(svg_path)


if __name__ == "__main__":
    main()
