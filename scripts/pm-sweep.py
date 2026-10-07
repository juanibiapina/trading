#!/usr/bin/env python3
"""Whole-market premarket gainers with no price or market-cap cap.

scan.py screens a capped universe ($0.50-$10, under $300M). Morning
retrospectives also need the uncapped list, e.g. to find movers that the
price floor hid (price-floor exclusion tracking). During premarket, `day%`
and `AH%` refer to the previous session. TradingView's `PMhi` can be a bad
print (BIYA showed $37.1 against a $2.99 SIP high on 2026-10-07); confirm
prices and volume with SIP bars before logging them.
"""

import argparse

import requests

from scan import API_URL

COLUMNS = [
    "name", "close", "premarket_change", "premarket_close", "premarket_high",
    "premarket_volume", "change", "postmarket_change",
    "float_shares_outstanding", "market_cap_basic", "industry",
]
LISTED = ["NASDAQ", "NYSE", "AMEX"]


def number(value, digits=0):
    return "-" if value is None else f"{value:,.{digits}f}"


def price(value):
    return "-" if value is None else f"{value:.4g}"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--min-change", type=float, default=10.0, help="Minimum premarket change %% (default 10)")
    parser.add_argument("--limit", type=int, default=40, help="Rows to return (default 40)")
    parser.add_argument("--include-otc", action="store_true", help="Include OTC names (Alpaca cannot trade most)")
    args = parser.parse_args()

    filters = [{"left": "premarket_change", "operation": "greater", "right": args.min_change}]
    if not args.include_otc:
        filters.append({"left": "exchange", "operation": "in_range", "right": LISTED})
    payload = {
        "columns": COLUMNS,
        "filter": filters,
        "sort": {"sortBy": "premarket_change", "sortOrder": "desc"},
        "markets": ["america"],
        "symbols": {"query": {"types": ["stock"]}},
        "options": {"lang": "en"},
        "range": [0, args.limit],
    }
    resp = requests.post(API_URL, json=payload, timeout=15)
    resp.raise_for_status()
    data = resp.json()

    print(f"PM sweep: premarket change > {args.min_change:g}%, no price/mcap cap, "
          f"{'all exchanges' if args.include_otc else 'listed only'}; "
          f"{len(data.get('data', []))} of {data.get('totalCount', '?')} shown")
    print(f"{'symbol':<14}{'close':>9}{'PM%':>8}{'PMpx':>9}{'PMhi':>9}{'PMvol':>13}"
          f"{'day%':>8}{'AH%':>8}{'float':>14}{'mcap':>15}  industry")
    for item in data.get("data", []):
        d = dict(zip(COLUMNS, item["d"]))
        print(f"{item['s']:<14}{price(d['close']):>9}{number(d['premarket_change'], 1):>8}"
              f"{price(d['premarket_close']):>9}{price(d['premarket_high']):>9}{number(d['premarket_volume']):>13}"
              f"{number(d['change'], 1):>8}{number(d['postmarket_change'], 1):>8}"
              f"{number(d['float_shares_outstanding']):>14}{number(d['market_cap_basic']):>15}  {d['industry'] or '-'}")


if __name__ == "__main__":
    main()
