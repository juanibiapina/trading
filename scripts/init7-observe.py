#!/usr/bin/env python3
"""Run Initiative 7's frozen N1/A1/A2 observations. Log-only: no orders, quotes-as-fills or portfolios.

Subcommands:
  verify   Check the hashes pinned by amendment A2 and reproduce its 12 decision vectors.
  observe  Capture one scheduled observation now: delayed SIP basket bars and IEX books, the
           N1 selection, the SEC source for N1's ticker, at most one Jev call, and the A1/A2
           decisions. Writes log/<ET date>/init7-observe/<HHMM>/.
  daemon   Sleep until each frozen observation time and run `observe`, for N full sessions.
           Start it with `gob add python3 scripts/init7-observe.py daemon --sessions 5`.
  status   Summarize coverage, decisions and Jev usage from archived observations.

Timing rule (orchestration v1). The common decision cutoff is the scheduled time plus the
design's observation_deadline_seconds (120 s). Market and SEC inputs count only if received by
that cutoff, and the SEC capture uses it as its cutoff. Market inputs received after it make
every arm cash. decision.json is written after the single Jev call and before any outcome is
read. A pinned-hash mismatch makes every arm cash, so an edited selector, archiver or classifier
cannot enter the trial silently.

Each stage writes into the observation directory with exclusive creation, so a second run of
the same slot fails instead of overwriting it.
"""

import argparse
import datetime as dt
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import traceback
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))
ET = ZoneInfo("America/New_York")
UTC = dt.timezone.utc
VERSION = "init7-observe-v1"
AMENDMENT = ROOT / "docs" / "investigations" / "init7-amendment-a2.json"
MAPPING = ROOT / "log" / "2026-10-06" / "init7-sec" / "mapping" / "mapping.json"
SELECTOR = SCRIPTS / "init7-comparison-features.py"
CENSUS = SCRIPTS / "init7-data-census.py"
FULL_SESSION = dt.timedelta(hours=6, minutes=30)


def now():
    return dt.datetime.now(UTC)


def iso(value):
    return value.astimezone(UTC).isoformat().replace("+00:00", "Z")


def stamp(value):
    result = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    if result.tzinfo is None:
        raise ValueError(f"Timestamp needs an explicit time zone: {value}")
    return result.astimezone(UTC)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def write_new(path, value):
    with path.open("x") as file:  # exclusive: archived records are never overwritten
        file.write(json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + "\n")


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


def pinned():
    """Load the amendment and design; return hashes and any mismatch with the pinned files."""
    amendment_bytes = AMENDMENT.read_bytes()
    amendment = json.loads(amendment_bytes)
    amends = amendment["amends"]
    files = {"design": (ROOT / amends["design_file"], amends["design_sha256"]),
             "archiver": (ROOT / amends["archiver_file"], amends["archiver_sha256"]),
             "classifier": (ROOT / amends["classifier_file"], amends["classifier_sha256"])}
    hashes = {"amendment": sha(amendment_bytes)}
    problems = []
    for key, (path, expected) in files.items():
        hashes[key] = sha(path.read_bytes())
        if hashes[key] != expected:
            problems.append(f"{key} {path.name} is {hashes[key][:12]}, amendment pins {expected[:12]}")
    hashes.update(selector=sha(SELECTOR.read_bytes()), census_helpers=sha(CENSUS.read_bytes()),
                  orchestrator=sha(Path(__file__).read_bytes()),
                  mapping=json.loads(MAPPING.read_text())["mapping_sha256"])
    design = json.loads(files["design"][0].read_bytes())
    paths = {key: path for key, (path, _) in files.items()}
    return amendment, design, hashes, problems, paths


# ---------------------------------------------------------------- decision rule

def arms(n1, archiver_status, archiver_reason, jev, design, amendment):
    """Frozen A1 (v1) and A2 (amendment) rules.

    jev is None when no call was made, "call_failed", or a dict with choice, confidence and
    dilutive_financing (the noul probability).
    """
    gate, veto_rule = design["bounded_agent"], amendment["arm"]
    no_veto = veto_rule["no_veto_reasons"]
    if n1 is None:
        return {"n1": None, "a1": None, "a1_reason": "n1_cash", "a2": None, "a2_reason": "n1_cash"}
    if archiver_status != "eligible":
        if archiver_reason not in no_veto:
            raise ValueError(f"Unknown archiver reason: {archiver_reason}")
        return {"n1": n1, "a1": None, "a1_reason": archiver_reason, "a2": n1, "a2_reason": no_veto[archiver_reason]}
    if not isinstance(jev, dict):
        return {"n1": n1, "a1": None, "a1_reason": "call_failed", "a2": n1, "a2_reason": no_veto["call_failed"]}
    keep = (jev["choice"] in gate["allowed_catalyst_labels"]
            and jev["confidence"] >= gate["minimum_choice_confidence"]
            and jev["dilutive_financing"] < gate["maximum_dilutive_financing_probability_exclusive"])
    veto = ((jev["choice"] in veto_rule["veto_labels"] and jev["confidence"] >= veto_rule["minimum_veto_confidence"])
            or jev["dilutive_financing"] >= veto_rule["dilutive_financing_veto_probability_inclusive"])
    return {"n1": n1, "a1": n1 if keep else None, "a1_reason": "jev_retain" if keep else "jev_gate",
            "a2": None if veto else n1, "a2_reason": "jev_veto" if veto else "jev_retain"}


def command_verify(args):
    amendment, design, hashes, problems, _ = pinned()
    rows = []
    for vector in amendment["test_vectors"]:
        status, _, reason = vector["archiver"].partition("/")
        result = arms(vector["n1"], status, reason or None, vector["jev"], design, amendment)
        ok = (result["a1"], result["a2"], result["a2_reason"]) == (
            vector["expect_a1"], vector["expect_a2"], vector["a2_reason"])
        rows.append({"id": vector["id"], "ok": ok, "a1": result["a1"], "a2": result["a2"],
                     "a2_reason": result["a2_reason"]})
    failed = [row["id"] for row in rows if not row["ok"]]
    print(json.dumps({"hashes": hashes, "hash_problems": problems, "vectors": rows,
                      "vectors_matched": len(rows) - len(failed), "vectors_total": len(rows)}, indent=2))
    if problems or failed:
        raise SystemExit(1)


# ---------------------------------------------------------------- stages

def capture_market(census, design):
    """Same request shapes as the October 1 census; no history session and no IEX substitution."""
    data = os.environ.get("ALPACA_DATA_URL", "https://data.alpaca.markets")
    trading = os.environ.get("ALPACA_BASE_URL", "https://paper-api.alpaca.markets")
    clock = census.request(trading, "/v2/clock", {})
    current_time = stamp(clock["payload"]["timestamp"])
    day = current_time.astimezone(ET).date().isoformat()
    calendar = census.request(trading, "/v2/calendar", {"start": day, "end": day})
    rows = [row for row in calendar["payload"] if row["date"] == day]
    if not clock["payload"]["is_open"] or not rows:
        raise ValueError("Market is not in a regular session")
    opened, closed = census.session(rows[0])
    end = min(current_time - dt.timedelta(minutes=design["request_buffer_minutes"]), closed)
    if end <= opened:
        raise ValueError("No delayed SIP window yet")
    bars = census.fetch_bars(data, opened, end)
    quotes = census.request(data, "/v2/stocks/quotes/latest", {"symbols": ",".join(census.SYMBOLS), "feed": "iex"})
    return {"version": "init7-data-census-v1", "symbols": list(census.SYMBOLS), "clock": clock,
            "calendar": calendar, "current_session": rows[0], "current_delayed_sip": bars, "iex_quotes": quotes}


def market_receipts(source):
    values = [source[key]["received_utc"] for key in ("clock", "calendar", "iex_quotes")]
    values += [page["received_utc"] for page in source["current_delayed_sip"]["pages"]]
    return max(stamp(value) for value in values)


def sec_stage(directory, archiver, ticker, cutoff):
    """Run the pinned archiver; any crash or missing record counts as source_request_failed."""
    out = directory / "sec"
    started = now()
    proc = subprocess.run([sys.executable, str(archiver), "capture", "--mapping", str(MAPPING),
                           "--ticker", ticker, "--cutoff", iso(cutoff), "--out", str(out)],
                          capture_output=True, text=True, timeout=110, cwd=ROOT)
    record = {"exit_code": proc.returncode, "started_utc": iso(started), "finished_utc": iso(now()),
              "stderr_tail": proc.stderr[-2000:]}
    path = out / "observation.json"
    observation = json.loads(path.read_text()) if path.exists() else None
    if observation and observation.get("status") in ("cash", "eligible"):
        record.update(status=observation["status"], reason=observation.get("cash_reason"),
                      jev_request_bytes=observation.get("jev_request_bytes"),
                      filing=(observation.get("selected_filing") or {}).get("accession"))
    else:
        record.update(status="cash", reason="source_request_failed")
    return record


def parse_jev(case):
    """Return the decision inputs and usage from one classifier case record."""
    usage = (case.get("response") or {}).get("usage") or {}
    known = isinstance(usage.get("input_tokens"), int) and isinstance(usage.get("output_tokens"), int)
    result = {"status": case.get("status"), "http_status": case.get("http_status"),
              "elapsed_seconds": case.get("elapsed_seconds"),
              "input_tokens": usage.get("input_tokens") if known else None,
              "output_tokens": usage.get("output_tokens") if known else None, "decision_input": "call_failed"}
    if case.get("status") == "ok":
        answers = case["response"]["answers"]
        result["decision_input"] = {"choice": answers["catalyst"]["choice"],
                                    "confidence": answers["catalyst"]["confidence"],
                                    "dilutive_financing": answers["dilutive_financing"]["noul"]}
    return result


def jev_stage(directory, classifier, case_file):
    out = directory / "jev"
    proc = subprocess.run([sys.executable, str(classifier), "--input", str(case_file), "--out-dir", str(out), "--run"],
                          capture_output=True, text=True, timeout=90, cwd=ROOT)
    path = out / "case-01.json"
    result = parse_jev(json.loads(path.read_text())) if path.exists() else {
        "status": "failed", "input_tokens": None, "output_tokens": None, "decision_input": "call_failed"}
    manifest = out / "manifest.json"
    if manifest.exists():
        summary = json.loads(manifest.read_text()).get("summary") or {}
        result["estimated_cost_usd"] = summary.get("estimated_cost_usd_total")
        result["pricing"] = summary.get("pricing")
    result.update(exit_code=proc.returncode, stderr_tail=proc.stderr[-2000:])
    return result


# ---------------------------------------------------------------- observe

def observe(scheduled, directory, market_input=None, mode="prospective_instrumentation"):
    """Run one observation into a new directory and return its decision record."""
    amendment, design, hashes, problems, paths = pinned()
    census = module("init7_census", CENSUS)
    selector = module("init7_features", SELECTOR)
    cutoff = scheduled + dt.timedelta(seconds=design["observation_deadline_seconds"])
    directory.mkdir(parents=True, exist_ok=False)
    record = {"version": VERSION, "mode": mode, "scheduled_et": scheduled.astimezone(ET).isoformat(),
              "decision_cutoff_utc": iso(cutoff), "started_utc": iso(now()), "hashes": hashes,
              "hash_problems": problems, "n1_reason": None, "market": None, "sec": None, "jev": None}
    write_new(directory / "started.json", {k: record[k] for k in ("version", "mode", "scheduled_et",
                                                                    "decision_cutoff_utc", "started_utc", "hashes")})
    n1 = None
    if problems:
        record["n1_reason"] = "pinned_hash_mismatch"
    else:
        try:
            source = json.loads(market_input.read_text()) if market_input else capture_market(census, design)
            if not market_input:
                write_new(directory / "market.json", source)
            received = market_receipts(source)
            record["market"] = {"input": str(market_input) if market_input else "market.json",
                                "last_receipt_utc": iso(received), "received_by_cutoff": received <= cutoff}
            result = selector.features(source, design)
            write_new(directory / "features.json", result)
            record["market"].update(feature_cutoff_utc=result["feature_cutoff_utc"],
                                    ranking=result.get("ranking"), book_diagnostic=result.get("book_diagnostic"))
            if received > cutoff:
                record["n1_reason"] = "market_inputs_after_cutoff"
            else:
                n1, record["n1_reason"] = result["numerical_candidate"], result["reason"]
        except Exception as error:  # every failure is recorded; the observation stays cash
            record["n1_reason"] = "market_capture_failed"
            record["market_error"] = f"{type(error).__name__}: {error}"
    status, reason, jev_input = None, None, None
    if n1:
        record["sec"] = sec_stage(directory, paths["archiver"], n1, cutoff)
        status, reason = record["sec"]["status"], record["sec"]["reason"]
        if status == "eligible":
            record["jev"] = jev_stage(directory, paths["classifier"], directory / "sec" / "jev-case.json")
            jev_input = record["jev"]["decision_input"]
    record["decision"] = arms(n1, status, reason, jev_input, design, amendment)
    record["decision_persisted_utc"] = iso(now())
    write_new(directory / "decision.json", record)
    return record


def slot_time(day, clock):
    hour, minute = map(int, clock.split(":"))
    return dt.datetime(day.year, day.month, day.day, hour, minute, tzinfo=ET)


def command_observe(args):
    _, design, _, _, _ = pinned()
    if args.market_input:
        if not args.out or not args.at:
            raise SystemExit("A rehearsal needs --out and --at; it never writes the prospective log")
        scheduled, directory, mode = stamp(args.at), args.out, "rehearsal_excluded_from_trial"
    else:
        if args.slot not in design["observation_times_et"]:
            raise SystemExit(f"{args.slot} is not a frozen observation time")
        scheduled = slot_time(now().astimezone(ET).date(), args.slot)
        late = (now() - scheduled).total_seconds()
        if not 0 <= late <= design["observation_deadline_seconds"]:
            raise SystemExit(f"Outside the {args.slot} ET window ({late:.0f}s from its start)")
        directory = ROOT / "log" / scheduled.date().isoformat() / "init7-observe" / args.slot.replace(":", "")
        mode = "prospective_instrumentation"
    record = observe(scheduled, directory, args.market_input, mode)
    print(json.dumps({k: record.get(k) for k in ("scheduled_et", "n1_reason", "decision", "sec", "jev",
                                                   "market_error", "decision_persisted_utc")}, indent=2))


# ---------------------------------------------------------------- daemon

def log(message):
    print(f"{iso(now())} {message}", flush=True)


def upcoming_sessions(census):
    trading = os.environ.get("ALPACA_BASE_URL", "https://paper-api.alpaca.markets")
    today = now().astimezone(ET).date()
    calendar = census.request(trading, "/v2/calendar",
                              {"start": today.isoformat(), "end": (today + dt.timedelta(days=10)).isoformat()})
    return calendar["payload"]


def command_daemon(args):
    _, design, _, problems, _ = pinned()
    if problems:
        raise SystemExit(f"Pinned files differ: {problems}")
    census = module("init7_census", CENSUS)
    deadline = dt.timedelta(seconds=design["observation_deadline_seconds"])
    full, done_dates = 0, set()
    log(f"daemon started; target {args.sessions} full sessions")
    while full < args.sessions:
        try:
            rows = [row for row in upcoming_sessions(census) if row["date"] not in done_dates]
        except Exception as error:
            log(f"calendar request failed: {type(error).__name__}: {error}; retry in 10 minutes")
            time.sleep(600)
            continue
        if not rows:
            time.sleep(3600)
            continue
        row = rows[0]
        day = dt.date.fromisoformat(row["date"])
        opened, closed = census.session(row)
        slots = [slot_time(day, clock) for clock in design["observation_times_et"]]
        if closed - opened < FULL_SESSION:
            log(f"{day} is a half-day ({row['close']} close); excluded before outcomes")
            done_dates.add(row["date"])
            continue
        counted = now() <= slots[0]
        attempted = 0
        for slot in slots:
            wait = (slot - now()).total_seconds()
            if wait > 0:
                time.sleep(wait)
            if now() > slot + deadline:
                log(f"{day} {slot:%H:%M} ET missed (woke {iso(now())})")
                continue
            directory = ROOT / "log" / day.isoformat() / "init7-observe" / slot.strftime("%H%M")
            try:
                record = observe(slot, directory)
                attempted += 1
                log(f"{day} {slot:%H:%M} ET decided: {json.dumps(record['decision'])} ({record['n1_reason']})")
            except Exception:
                log(f"{day} {slot:%H:%M} ET failed:\n{traceback.format_exc()}")
        done_dates.add(row["date"])
        if counted and attempted == len(slots):
            full += 1
        log(f"{day} finished: {attempted}/{len(slots)} observations; full sessions {full}/{args.sessions}")
    log("daemon finished")


# ---------------------------------------------------------------- status

def command_status(args):
    rows = []
    for path in sorted(ROOT.glob("log/*/init7-observe/*/decision.json")):
        record = json.loads(path.read_text())
        if args.since and path.parts[-4] < args.since:
            continue
        jev = record.get("jev") or {}
        rows.append({"date": path.parts[-4], "slot": path.parts[-2], "n1": record["decision"]["n1"],
                     "n1_reason": record["n1_reason"], "a1": record["decision"]["a1"],
                     "a2": record["decision"]["a2"], "a2_reason": record["decision"]["a2_reason"],
                     "sec": (record.get("sec") or {}).get("reason") or (record.get("sec") or {}).get("status"),
                     "jev_status": jev.get("status"), "jev_tokens": (jev.get("input_tokens"), jev.get("output_tokens")),
                     "jev_cost_usd": jev.get("estimated_cost_usd"),
                     "latency_s": (stamp(record["decision_persisted_utc"]) - stamp(record["scheduled_et"])).total_seconds()})
    started = sorted({path.parts[-4] + "/" + path.parts[-2] for path in ROOT.glob("log/*/init7-observe/*/started.json")})
    calls = [row for row in rows if row["jev_status"]]
    costs = [row["jev_cost_usd"] for row in calls]
    print(json.dumps({"observations_started": len(started), "decisions": len(rows),
                      "started_without_decision": [s for s in started if s.replace("/", "") not in
                                                   {r["date"] + r["slot"] for r in rows}],
                      "n1_selected": sum(1 for row in rows if row["n1"]),
                      "veto_could_act": sum(1 for row in calls if row["jev_status"] == "ok"),
                      "a2_vetoes": sum(1 for row in rows if row["a2_reason"] == "jev_veto"),
                      "jev_calls": len(calls),
                      "jev_estimated_cost_usd": sum(costs) if calls and None not in costs else (None if calls else 0),
                      "rows": rows}, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("verify")
    p = sub.add_parser("observe")
    p.add_argument("--slot", help="Frozen ET observation time, e.g. 10:30")
    p.add_argument("--market-input", type=Path, help="Rehearsal only: archived census instead of a live capture")
    p.add_argument("--at", help="Rehearsal only: scheduled time with explicit time zone")
    p.add_argument("--out", type=Path, help="Rehearsal only: new output directory")
    p = sub.add_parser("daemon")
    p.add_argument("--sessions", type=int, default=5)
    p = sub.add_parser("status")
    p.add_argument("--since", help="First ET date, YYYY-MM-DD")
    args = parser.parse_args()
    {"verify": command_verify, "observe": command_observe, "daemon": command_daemon,
     "status": command_status}[args.command](args)


if __name__ == "__main__":
    main()
