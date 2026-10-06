#!/usr/bin/env python3
"""Log-only Initiative 1 study: v2 SIP volume ratios at each real AH paper entry versus its realized return.

Fetch mode archives reduced Alpaca orders, the exchange calendar and every SIP input under OUT, then
computes. `--replay` recomputes from those archives without network access. Each entry is measured
with bars closed at least `--lag-min` minutes before its fill, the free-SIP availability delay.
"""

import argparse
import datetime as dt
import importlib.util
import json
import os
from pathlib import Path
import random
import statistics
import urllib.parse
import urllib.request
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")
spec = importlib.util.spec_from_file_location("volume_metric", Path(__file__).with_name("volume_metric.py"))
vm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vm)

ORDER_FIELDS = ("symbol", "side", "filled_qty", "filled_avg_price", "filled_at", "extended_hours", "status")


def api(path, query):
    base = os.environ.get("ALPACA_BASE_URL", "https://paper-api.alpaca.markets").rstrip("/")
    headers = {"APCA-API-KEY-ID": os.environ["ALPACA_API_KEY"],
               "APCA-API-SECRET-KEY": os.environ["ALPACA_SECRET_KEY"]}
    request = urllib.request.Request(f"{base}{path}?{urllib.parse.urlencode(query)}", headers=headers)
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def fetch_orders(after):
    orders, seen = [], set()
    while True:
        page = api("/v2/orders", {"status": "all", "limit": 500, "direction": "asc", "after": after})
        fresh = [o for o in page if o["id"] not in seen]
        seen.update(o["id"] for o in fresh)
        orders.extend(fresh)
        if len(page) < 500 or not fresh:
            break
        after = page[-1]["submitted_at"]
    return [{k: o.get(k) for k in ORDER_FIELDS} for o in orders if o["status"] == "filled"]


def lots(orders):
    """Pair each AH buy fill with later sells of the same symbol, first in first out."""
    fills = sorted(orders, key=lambda o: o["filled_at"])
    queues, result = {}, []
    for order in fills:
        qty, price = float(order["filled_qty"]), float(order["filled_avg_price"])
        time = vm.timestamp(order["filled_at"])
        if order["side"] == "buy":
            lot = {"symbol": order["symbol"], "fill_utc": time.isoformat(), "qty": qty, "price": price,
                   "open": qty, "proceeds": 0.0, "exits": []}
            queues.setdefault(order["symbol"], []).append(lot)
            result.append(lot)
            continue
        remaining = qty
        for lot in queues.get(order["symbol"], []):
            take = min(lot["open"], remaining)
            if take <= 0:
                continue
            lot["open"] -= take
            lot["proceeds"] += take * price
            lot["exits"].append({"utc": time.isoformat(), "qty": take, "price": price})
            remaining -= take
            if remaining <= 1e-9:
                break
    return result


def session_info(calendar, day):
    dates = [d["date"] for d in calendar]
    index = dates.index(day.isoformat())
    prior = calendar[index - 1]
    return (dt.date.fromisoformat(prior["date"]),
            calendar[index]["close"] == "16:00" and prior["close"] == "16:00")


def measure(lot, calendar, sip_dir, replay, lag):
    fill = vm.timestamp(lot["fill_utc"])
    local = fill.astimezone(ET)
    day = local.date()
    prior, normal = session_info(calendar, day)
    path = sip_dir / f"{lot['symbol']}-{day.isoformat()}.json"
    if replay or path.exists():
        source = json.loads(path.read_text())
    else:
        source = vm.fetch_sip(lot["symbol"], prior, day)
        path.write_text(json.dumps(source, indent=1) + "\n")
    as_of = fill - dt.timedelta(minutes=lag)
    metric = vm.calculate_v2(source, day, prior, as_of)
    rows = metric["rows"]
    xs = [r["prior_peak_ratio"] for r in rows if r["prior_peak_ratio"] is not None]
    local_ratios = [r["local_ratio"] for r in rows if r["local_ratio"] is not None]
    peak_row = max(rows, key=lambda r: r["shares"], default=None)
    # Same-day regular session 09:30-16:00 ET; slots without a bar are zero-trade intervals (later bars exist).
    open_utc = dt.datetime.combine(day, dt.time(9, 30), ET).astimezone(dt.timezone.utc)
    indexed = {vm.timestamp(b["t"]): b["v"] for b in source["bars"]}
    regular = [indexed.get(open_utc + vm.SLOT * i, 0) for i in range(78)]
    rth_max = max(regular)
    cost = lot["qty"] * lot["price"]
    closed = lot["open"] <= 1e-9
    return {"symbol": lot["symbol"], "date": day.isoformat(), "prior_date": prior.isoformat(),
            "normal_sessions": normal, "fill_et": local.strftime("%H:%M"), "entry_price": lot["price"],
            "as_of_utc": as_of.isoformat(), "visible_bars": len(rows),
            "prior_peak_shares": metric["prior_peak_shares"],
            "prior_observed_slots": metric["prior_observed_slots"],
            "session_peak_shares": peak_row["shares"] if peak_row else None,
            "session_peak_bar_et": peak_row["bar_et"] if peak_row else None,
            "cross_ratio_max": max(xs, default=None),
            "local_ratio_max": max(local_ratios, default=None),
            "rth_max_shares": rth_max, "rth_median_shares": statistics.median(regular),
            "ah_vs_rth_max": peak_row["shares"] / max(rth_max, vm.FLOOR_SHARES) if peak_row else None,
            "closed": closed, "cost_usd": round(cost, 4), "pnl_usd": round(lot["proceeds"] - cost, 4) if closed else None,
            "return": lot["proceeds"] / cost - 1 if closed else None,
            "last_exit_utc": lot["exits"][-1]["utc"] if lot["exits"] else None}


def summarize(rows, label, test):
    def stats(group):
        returns = [r["return"] for r in group]
        return {"n": len(group), "wins": sum(x > 0 for x in returns),
                "mean_return": statistics.mean(returns) if returns else None,
                "median_return": statistics.median(returns) if returns else None,
                "pnl_usd": round(sum(r["pnl_usd"] for r in group), 2)}
    usable = [r for r in rows if r["closed"] and test(r) is not None]
    passed = [r["return"] for r in usable if test(r)]
    failed = [r["return"] for r in usable if not test(r)]
    p_value = None
    if passed and failed:
        # Two-sided permutation test on the mean-return gap, seed 7, 10,000 shuffles.
        rng, pooled = random.Random(7), passed + failed
        observed = abs(statistics.mean(passed) - statistics.mean(failed))
        extreme = 0
        for _ in range(10000):
            rng.shuffle(pooled)
            gap = statistics.mean(pooled[:len(passed)]) - statistics.mean(pooled[len(passed):])
            extreme += abs(gap) >= observed - 1e-12
        p_value = extreme / 10000
    return {"gate": label, "pass": stats([r for r in usable if test(r)]),
            "fail": stats([r for r in usable if not test(r)]), "permutation_p": p_value,
            "unmeasured": sum(1 for r in rows if r["closed"] and test(r) is None)}


def gate(field, threshold):
    return lambda r: None if r[field] is None else r[field] >= threshold


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("out", type=Path, help="Archive directory")
    parser.add_argument("--replay", action="store_true", help="Recompute from archived orders, calendar and SIP")
    parser.add_argument("--after", default="2026-06-01T00:00:00Z")
    parser.add_argument("--lag-min", type=int, default=15)
    args = parser.parse_args()
    sip_dir = args.out / "sip"
    sip_dir.mkdir(parents=True, exist_ok=True)
    if args.replay:
        orders = json.loads((args.out / "orders.json").read_text())
        calendar = json.loads((args.out / "calendar.json").read_text())
    else:
        orders = fetch_orders(args.after)
        calendar = api("/v2/calendar", {"start": args.after[:10], "end": dt.date.today().isoformat()})
        (args.out / "orders.json").write_text(json.dumps(orders, indent=1) + "\n")
        (args.out / "calendar.json").write_text(json.dumps(calendar, indent=1) + "\n")
    entries = []
    for lot in lots(orders):
        local = vm.timestamp(lot["fill_utc"]).astimezone(ET)
        if 16 <= local.hour < 20:
            entries.append(measure(lot, calendar, sip_dir, args.replay, args.lag_min))
    gates = [summarize(entries, "all entries", lambda r: True),
             summarize(entries, "cross_ratio_max >= 1", gate("cross_ratio_max", 1)),
             summarize(entries, "cross_ratio_max >= 3", gate("cross_ratio_max", 3)),
             summarize(entries, "cross_ratio_max >= 10", gate("cross_ratio_max", 10)),
             summarize(entries, "local_ratio_max >= 10", gate("local_ratio_max", 10)),
             # Secondary, added after the first four: Juan's GELS/DAIC remarks compare AH bars with regular hours.
             summarize(entries, "ah_vs_rth_max >= 1 (secondary)", gate("ah_vs_rth_max", 1)),
             summarize(entries, "ah_vs_rth_max >= 3 (secondary)", gate("ah_vs_rth_max", 3))]
    result = {"study": "init1-volume-policy-v2", "metric_version": vm.VERSION_V2, "lag_minutes": args.lag_min,
              "floor_shares": vm.FLOOR_SHARES, "entries": entries, "gates": gates}
    print(json.dumps(result, indent=1))


if __name__ == "__main__":
    main()
