#!/usr/bin/env python3
"""Estimate TradingView screener lag: find which recent IEX 1-minute bars contain each screener price.

Log-only research. Run during premarket or after-hours; it reads the same
`scan()` list the pulses use, then compares each screener extended-hours price
with real-time IEX bars and the latest IEX trade. If the screener price sits in
bars ~15 minutes old but not in the latest bar, the screener is delayed.
"""

import argparse
from datetime import datetime, timedelta, timezone
import json
import os
from pathlib import Path

import requests

from scan import get_session, scan

DATA = os.environ.get("ALPACA_DATA_URL", "https://data.alpaca.markets") + "/v2/stocks"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--top", type=int, default=8)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    session = get_session()
    if session not in ("premarket", "afterhours"):
        raise SystemExit(f"Screener extended-hours fields are only live in premarket/after-hours; now {session}")
    headers = {"APCA-API-KEY-ID": os.environ["ALPACA_API_KEY"], "APCA-API-SECRET-KEY": os.environ["ALPACA_SECRET_KEY"]}
    observed = datetime.now(timezone.utc)
    rows = []
    for row in scan(session)[:args.top]:
        symbol, price = row["ticker"], row["ext_close"]
        trade = requests.get(f"{DATA}/{symbol}/trades/latest", params={"feed": "iex"},
                             headers=headers, timeout=8).json().get("trade") or {}
        bars = requests.get(f"{DATA}/{symbol}/bars", headers=headers, timeout=8, params={
            "feed": "iex", "timeframe": "1Min", "limit": 100,
            "start": (observed - timedelta(minutes=40)).isoformat()}).json().get("bars") or []
        ages = [round((observed - datetime.fromisoformat(b["t"].replace("Z", "+00:00"))).total_seconds() / 60)
                for b in bars if b["l"] <= price <= b["h"]]
        rows.append({"ticker": symbol, "screener_price": price, "screener_change_pct": round(row["change_pct"], 2),
                     "iex_last_trade": trade.get("p"), "iex_last_trade_utc": trade.get("t"),
                     "iex_bars_40m": len(bars), "last_iex_bar_close": bars[-1]["c"] if bars else None,
                     "minutes_ago_of_bars_containing_screener_price": ages,
                     "latest_bar_contains_price": bool(bars) and bars[-1]["l"] <= price <= bars[-1]["h"]})
    result = {"observed_utc": observed.isoformat(), "session": session, "rows": rows}
    with args.out.open("x") as file:
        file.write(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
