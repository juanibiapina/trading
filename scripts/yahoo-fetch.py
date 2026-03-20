#!/usr/bin/env python3
"""
Fetch Yahoo Finance chart data and output JSON to stdout.

Wraps the Yahoo Finance API with the required User-Agent header.
Sessions can pipe the output to custom python3 -c processing.

Usage:
    python3 scripts/yahoo-fetch.py TICKER [--interval 5m] [--range 2d] [--prepost]

Examples:
    # Get 5-minute bars for last 2 days including pre/post market
    python3 scripts/yahoo-fetch.py DRMA --interval 5m --range 2d --prepost

    # Pipe to custom processing
    python3 scripts/yahoo-fetch.py DRMA --interval 5m --range 2d --prepost | python3 -c "
    import json, sys; data = json.load(sys.stdin); ..."

    # Get 1-minute intraday with extended hours
    python3 scripts/yahoo-fetch.py SUNE --interval 1m --range 1d --prepost
"""

import argparse
import json
import sys
import urllib.request


def main():
    parser = argparse.ArgumentParser(description="Fetch Yahoo Finance chart data")
    parser.add_argument("ticker", help="Stock ticker symbol")
    parser.add_argument("--interval", default="5m", help="Bar interval (1m, 5m, 15m, 1h, 1d)")
    parser.add_argument("--range", default="2d", dest="range_str", help="Time range (1d, 2d, 5d, 1mo)")
    parser.add_argument("--prepost", action="store_true", help="Include pre/post market data")
    args = parser.parse_args()

    url = (
        f"https://query1.finance.yahoo.com/v8/finance/chart/{args.ticker}"
        f"?interval={args.interval}&range={args.range_str}"
        f"&includePrePost={'true' if args.prepost else 'false'}"
    )

    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        resp = urllib.request.urlopen(req, timeout=10)
        data = json.loads(resp.read())
        json.dump(data, sys.stdout)
    except Exception as e:
        print(f"Error fetching {args.ticker}: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
