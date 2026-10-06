#!/usr/bin/env python3
"""Archive SEC primary sources for Initiative 7's bounded Jev veto; no model calls or orders.

Subcommands:
  map        Freeze the ticker-to-CIK mapping from SEC company_tickers.json.
  capture    Archive the newest 8-K accepted within 24 hours before a decision cutoff,
             its EX-99 exhibits, extracted text and a Jev-ready case when eligible.
  replay     Re-verify an archived capture offline: hashes, extraction and decision.
  census     Count how often each mapped issuer had an eligible 8-K at the frozen
             observation times, and how large the extracted request would be.

SEC asks automated clients for a User-Agent with contact details. Set
SEC_USER_AGENT, or the script builds one from `git config user.email`. Archived
metadata stores the User-Agent with the address redacted.

The submissions JSON `acceptanceDateTime` is not used as the acceptance time.
On 2026-10-06 it read 4 hours (summer) or 5 hours (winter) later than true UTC
for Apple, Amazon and Meta filings, and matched for the other issuers. The filing's
`.hdr.sgml` ACCEPTANCE-DATETIME, interpreted in America/New_York, is authoritative.
"""

import argparse
import datetime as dt
from html.parser import HTMLParser
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import subprocess
import time
import urllib.error
import urllib.request
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
ET = ZoneInfo("America/New_York")
UTC = dt.timezone.utc
VERSION = "init7-sec-archive-v1"
PARSER = "init7-sec-text-v1"
TICKERS_URL = "https://www.sec.gov/files/company_tickers.json"
SUBMISSIONS_URL = "https://data.sec.gov/submissions/CIK{cik}.json"
ARCHIVE_URL = "https://www.sec.gov/Archives/edgar/data/{cik_int}/{acc_nodash}/"
DESIGN = ROOT / "docs" / "investigations" / "init7-comparison-v1.json"
REQUEST_GAP_SECONDS = 0.15  # SEC fair-access limit is 10 requests/second


def now():
    return dt.datetime.now(UTC)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def stamp(value):
    result = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    if result.tzinfo is None:
        raise ValueError(f"Timestamp needs an explicit time zone: {value}")
    return result.astimezone(UTC)


def iso(value):
    return value.astimezone(UTC).isoformat().replace("+00:00", "Z")


def save_json(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def user_agent():
    value = os.environ.get("SEC_USER_AGENT")
    if not value:
        email = subprocess.run(["git", "config", "user.email"], cwd=ROOT, capture_output=True,
                               text=True).stdout.strip()
        if not email:
            raise SystemExit("Set SEC_USER_AGENT to 'name contact@example.com' (SEC fair-access policy)")
        value = f"trading-research {email}"
    return value


def redacted(value):
    return re.sub(r"[^\s@]+@", "***@", value)


class Fetcher:
    """Fetch URLs, saving exact bytes and request metadata into one observation directory."""

    def __init__(self, directory, cutoff=None):
        self.directory = directory
        self.cutoff = cutoff
        self.agent = user_agent()
        self.records = []
        self.last = 0.0

    def get(self, url, name):
        wait = REQUEST_GAP_SECONDS - (time.monotonic() - self.last)
        if wait > 0:
            time.sleep(wait)
        record = {"url": url, "file": name, "requested_utc": iso(now()),
                  "user_agent": redacted(self.agent)}
        request = urllib.request.Request(url, headers={"User-Agent": self.agent,
                                                       "Accept-Encoding": "identity"})
        data = b""
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                data = response.read()
                record.update(status=response.status, content_type=response.headers.get("Content-Type"))
        except urllib.error.HTTPError as error:
            data = error.read()
            record.update(status=error.code, content_type=error.headers.get("Content-Type"),
                          error=f"HTTPError: {error.code}")
        except OSError as error:
            record.update(status=None, error=f"{type(error).__name__}: {error}")
        self.last = time.monotonic()
        received = now()
        record.update(received_utc=iso(received), bytes=len(data), sha256=sha(data))
        if self.cutoff is not None:
            record["received_by_cutoff"] = received <= self.cutoff
        if data:
            path = self.directory / name
            with path.open("xb") as file:  # exclusive: never overwrite archived bytes
                file.write(data)
        self.records.append(record)
        if record.get("status") != 200:
            raise FetchError(record)
        return data, record


class FetchError(Exception):
    def __init__(self, record):
        super().__init__(f"{record['url']}: {record.get('error') or record.get('status')}")
        self.record = record


class TextExtractor(HTMLParser):
    """Deterministic text: drop markup, scripts, styles, head and inline-XBRL headers."""

    SKIP = {"script", "style", "head", "ix:header"}
    BLOCK = {"p", "div", "br", "tr", "li", "table", "h1", "h2", "h3", "h4", "h5", "h6", "td", "th"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.depth = 0
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self.depth += 1
        elif tag in self.BLOCK:
            self.parts.append("\n" if tag != "td" and tag != "th" else " ")

    def handle_endtag(self, tag):
        if tag in self.SKIP and self.depth:
            self.depth -= 1
        elif tag in self.BLOCK:
            self.parts.append("\n" if tag != "td" and tag != "th" else " ")

    def handle_data(self, data):
        if not self.depth:
            self.parts.append(data)


def extract_text(data):
    parser = TextExtractor()
    parser.feed(data.decode("utf-8", errors="replace"))
    parser.close()
    lines = (re.sub(r"[ \t\u00a0\u200b]+", " ", line).strip() for line in "".join(parser.parts).splitlines())
    return "\n".join(line for line in lines if line)


def parse_acceptance(header):
    match = re.search(rb"<ACCEPTANCE-DATETIME>(\d{14})", header)
    if not match:
        raise ValueError("Header has no ACCEPTANCE-DATETIME")
    local = dt.datetime.strptime(match.group(1).decode(), "%Y%m%d%H%M%S").replace(tzinfo=ET)
    return local.astimezone(UTC), match.group(1).decode()


def parse_index(html):
    """Return (sequence, description, document, type) rows from an EDGAR filing index page."""
    rows = []
    for row in re.findall(r"<tr[^>]*>(.*?)</tr>", html, re.S):
        cells = [re.sub(r"<[^>]+>", "", cell).replace("&nbsp;", " ").strip()
                 for cell in re.findall(r"<td[^>]*>(.*?)</td>", row, re.S)]
        # Inline-XBRL documents link through the viewer: href="/ix?doc=/Archives/...".
        link = re.search(r'href="(?:/ix\?doc=)?(/Archives/edgar/data/[^"]+)"', row)
        if len(cells) >= 4 and link:
            rows.append({"seq": cells[0], "description": cells[1], "type": cells[3],
                         "path": link.group(1), "document": link.group(1).rsplit("/", 1)[-1]})
    return rows


def load_design(path):
    data = path.read_bytes()
    return json.loads(data), sha(data)


def jev_runner():
    spec = importlib.util.spec_from_file_location("init7_jev_classify", ROOT / "scripts" / "init7-jev-classify.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def make_dir(path):
    path.mkdir(parents=True, exist_ok=False)  # exclusive: refuse to reuse an observation


# ---------------------------------------------------------------- map

def command_map(args):
    design, design_hash = load_design(args.design)
    make_dir(args.out)
    fetcher = Fetcher(args.out)
    data, record = fetcher.get(TICKERS_URL, "company_tickers.json")
    rows = json.loads(data).values()
    mapping, problems = {}, []
    for ticker in design["tradable_candidates"]:
        ciks = sorted({row["cik_str"] for row in rows if row["ticker"] == ticker})
        titles = sorted({row["title"] for row in rows if row["ticker"] == ticker})
        if len(ciks) != 1:
            problems.append(f"{ticker}: {len(ciks)} CIKs")
            continue
        mapping[ticker] = {"cik": f"{ciks[0]:010d}", "title": titles[0]}
    result = {"version": VERSION, "design_sha256": design_hash, "frozen_utc": iso(now()),
              "source": record, "mapping": mapping, "problems": problems,
              "status": "frozen" if not problems else "ambiguous"}
    result["mapping_sha256"] = sha(json.dumps(mapping, sort_keys=True).encode())
    save_json(args.out / "mapping.json", result)
    save_json(args.out / "requests.json", fetcher.records)
    print(json.dumps({k: result[k] for k in ("status", "mapping", "problems", "mapping_sha256")}, indent=2))
    if problems:
        raise SystemExit(1)


# ---------------------------------------------------------------- capture

def eight_k_candidates(submissions, cutoff, max_age):
    """Recent 8-K filings by filing date, newest first. Acceptance is checked later from headers."""
    recent = submissions["filings"]["recent"]
    earliest = (cutoff - max_age).astimezone(ET).date() - dt.timedelta(days=1)
    latest = cutoff.astimezone(ET).date() + dt.timedelta(days=1)
    rows = []
    for i, form in enumerate(recent["form"]):
        filed = dt.date.fromisoformat(recent["filingDate"][i])
        if form == "8-K" and earliest <= filed <= latest:
            rows.append({"accession": recent["accessionNumber"][i], "filing_date": recent["filingDate"][i],
                         "json_acceptance": recent["acceptanceDateTime"][i], "items": recent["items"][i],
                         "primary_document": recent["primaryDocument"][i]})
    return rows


def decide(observation, runner):
    """Return status and the Jev batch, or a cash reason, from archived observation facts."""
    cutoff = stamp(observation["decision_cutoff_utc"])
    filing = observation.get("selected_filing")
    if observation.get("request_failure"):
        return "cash", "source_request_failed", None
    if not filing:
        return "cash", "no_8k_within_window", None
    late = [r["file"] for r in observation["requests"] if not r.get("received_by_cutoff", True)]
    if late:
        return "cash", "received_after_cutoff", None
    if not observation["documents"]:
        return "cash", "missing_documents", None
    sources = [{"url": d["url"], "published_utc": filing["acceptance_utc"],
                "document_type": d["type"], "sha256": d["sha256"], "text": d["text"]}
               for d in observation["documents"]]
    case = {"id": f"{observation['ticker']}-{observation['decision_cutoff_utc']}",
            "kind": "prospective_capture",
            "provenance": f"{VERSION}; accession {filing['accession']}; extracted with {PARSER}",
            "state": {"ticker": observation["ticker"], "decision_cutoff_utc": observation["decision_cutoff_utc"],
                      "sources": sources}}
    if stamp(filing["acceptance_utc"]) > cutoff:
        return "cash", "future_source", None
    batch = {"spec": runner.SPEC, "prepared_on": observation["decision_cutoff_utc"][:10],
             "purpose": "Initiative 7 prospective primary-source capture", "cases": [case]}
    try:
        runner.requests_for(batch)
    except ValueError as error:
        reason = "source_too_large" if "20KB" in str(error) else "invalid_source"
        return "cash", reason, None
    return "eligible", None, batch


def command_capture(args):
    design, design_hash = load_design(args.design)
    mapping = json.loads(args.mapping.read_text())
    if mapping.get("status") != "frozen" or mapping.get("design_sha256") != design_hash:
        raise SystemExit("Mapping is not frozen for this design")
    if args.ticker not in mapping["mapping"]:
        raise SystemExit(f"{args.ticker} is not in the frozen mapping")
    cutoff = stamp(args.cutoff)
    max_age = dt.timedelta(hours=design["primary_source_protocol"]["max_age_hours"])
    make_dir(args.out)
    cik = mapping["mapping"][args.ticker]["cik"]
    observation = {"version": VERSION, "parser": PARSER, "design_sha256": design_hash,
                   "mapping_sha256": mapping["mapping_sha256"], "ticker": args.ticker, "cik": cik,
                   "decision_cutoff_utc": iso(cutoff), "started_utc": iso(now()), "status": "running",
                   "candidates": [], "documents": [], "requests": []}
    save_json(args.out / "observation.json", observation)
    fetcher = Fetcher(args.out, cutoff)
    try:
        data, _ = fetcher.get(SUBMISSIONS_URL.format(cik=cik), "submissions.json")
        candidates = eight_k_candidates(json.loads(data), cutoff, max_age)
        for number, candidate in enumerate(candidates, 1):
            acc = candidate["accession"].replace("-", "")
            base = ARCHIVE_URL.format(cik_int=int(cik), acc_nodash=acc)
            header, _ = fetcher.get(f"{base}{candidate['accession']}.hdr.sgml", f"header-{number:02d}.sgml")
            accepted, raw = parse_acceptance(header)
            json_time = stamp(candidate["json_acceptance"])
            candidate.update(acceptance_utc=iso(accepted), acceptance_header_et=raw,
                             json_minus_header_seconds=(json_time - accepted).total_seconds(),
                             within_window=cutoff - max_age < accepted <= cutoff)
            observation["candidates"].append(candidate)
        eligible = [c for c in observation["candidates"] if c["within_window"]]
        if eligible:
            filing = max(eligible, key=lambda c: c["acceptance_utc"])
            observation["selected_filing"] = filing
            base = ARCHIVE_URL.format(cik_int=int(cik), acc_nodash=filing["accession"].replace("-", ""))
            index, _ = fetcher.get(f"{base}{filing['accession']}-index.htm", "filing-index.htm")
            rows = [r for r in parse_index(index.decode("utf-8", errors="replace"))
                    if r["type"] == "8-K" or r["type"].startswith("EX-99")]
            filing["documents_listed"] = rows
            for number, row in enumerate(rows, 1):
                name = f"doc-{number:02d}-{row['type'].lower()}-{row['document']}"
                body, record = fetcher.get(f"https://www.sec.gov{row['path']}", name)
                text = extract_text(body)
                with (args.out / f"{name}.txt").open("x") as file:
                    file.write(text)
                observation["documents"].append({
                    "type": row["type"], "url": record["url"], "file": name, "sha256": record["sha256"],
                    "text_file": f"{name}.txt", "text_sha256": sha(text.encode()), "text_chars": len(text),
                    "text": text})
    except (FetchError, ValueError, KeyError) as error:
        observation["request_failure"] = str(error)
    observation["requests"] = fetcher.records
    status, reason, batch = decide(observation, jev_runner())
    if batch:
        save_json(args.out / "jev-case.json", batch)
        observation["jev_case_sha256"] = sha((args.out / "jev-case.json").read_bytes())
        observation["jev_request_bytes"] = len(json.dumps(
            {"model": jev_runner().MODEL, "state": batch["cases"][0]["state"],
             "questions": jev_runner().QUESTIONS}, ensure_ascii=False).encode())
    for document in observation["documents"]:
        document.pop("text")  # text lives in its own archived file
    observation.update(finished_utc=iso(now()), status=status, cash_reason=reason)
    save_json(args.out / "observation.json", observation)
    print(json.dumps({k: observation.get(k) for k in
                      ("ticker", "decision_cutoff_utc", "status", "cash_reason", "request_failure",
                       "jev_request_bytes")} | {
        "candidates": [{k: c.get(k) for k in ("accession", "acceptance_utc", "json_minus_header_seconds",
                                               "within_window", "items")} for c in observation["candidates"]],
        "documents": [{k: d[k] for k in ("type", "file", "text_chars")} for d in observation["documents"]],
        "requests": len(observation["requests"])}, indent=2))


# ---------------------------------------------------------------- replay

def command_replay(args):
    observation = json.loads((args.observation / "observation.json").read_text())
    problems = []
    for record in observation["requests"]:
        path = args.observation / record["file"]
        if record["bytes"] and sha(path.read_bytes()) != record["sha256"]:
            problems.append(f"hash mismatch: {record['file']}")
    for document in observation["documents"]:
        body = (args.observation / document["file"]).read_bytes()
        text = extract_text(body)
        if sha(text.encode()) != document["text_sha256"]:
            problems.append(f"extraction differs: {document['file']}")
        if (args.observation / document["text_file"]).read_text() != text:
            problems.append(f"archived text differs: {document['text_file']}")
        document["text"] = text
    status, reason, batch = decide(observation, jev_runner())
    if (status, reason) != (observation["status"], observation["cash_reason"]):
        problems.append(f"decision differs: {status}/{reason}")
    if batch and sha(json.dumps(batch, indent=2, ensure_ascii=False).encode() + b"\n") != observation.get("jev_case_sha256"):
        problems.append("jev case differs")
    print(json.dumps({"observation": str(args.observation), "status": status, "cash_reason": reason,
                      "problems": problems}, indent=2))
    if problems:
        raise SystemExit(1)


# ---------------------------------------------------------------- census

def observation_times(design, start, end):
    times = []
    day = start
    while day <= end:
        if day.weekday() < 5:
            for clock in design["observation_times_et"]:
                hour, minute = map(int, clock.split(":"))
                times.append(dt.datetime(day.year, day.month, day.day, hour, minute, tzinfo=ET).astimezone(UTC))
        day += dt.timedelta(days=1)
    return times


def command_census(args):
    """Development evidence only: metadata, hashes and sizes; raw document bytes are not kept."""
    design, design_hash = load_design(args.design)
    mapping = json.loads(args.mapping.read_text())
    runner = jev_runner()
    end = dt.date.fromisoformat(args.end)
    start = end - dt.timedelta(days=args.days - 1)
    times = observation_times(design, start, end)
    max_age = dt.timedelta(hours=design["primary_source_protocol"]["max_age_hours"])
    scratch = Path(args.out)
    make_dir(scratch)
    fetcher = Fetcher(scratch)
    result = {"version": VERSION, "parser": PARSER, "design_sha256": design_hash,
              "mapping_sha256": mapping["mapping_sha256"], "window_et": [str(start), str(end)],
              "weekday_observations_per_ticker": len(times),
              "limit": "Weekdays include exchange holidays; filings are fetched after the fact, so this measures source frequency and size, not causal receipt.",
              "tickers": {}}
    for ticker, entry in mapping["mapping"].items():
        cik = entry["cik"]
        data, _ = fetcher.get(SUBMISSIONS_URL.format(cik=cik), f"{ticker}-submissions.json")
        recent = json.loads(data)["filings"]["recent"]
        filings = []
        for i, form in enumerate(recent["form"]):
            filed = dt.date.fromisoformat(recent["filingDate"][i])
            if form != "8-K" or not start - dt.timedelta(days=2) <= filed <= end:
                continue
            accession = recent["accessionNumber"][i]
            base = ARCHIVE_URL.format(cik_int=int(cik), acc_nodash=accession.replace("-", ""))
            header, _ = fetcher.get(f"{base}{accession}.hdr.sgml", f"{ticker}-{accession}.hdr.sgml")
            accepted, raw = parse_acceptance(header)
            index, _ = fetcher.get(f"{base}{accession}-index.htm", f"{ticker}-{accession}-index.htm")
            rows = [r for r in parse_index(index.decode("utf-8", errors="replace"))
                    if r["type"] == "8-K" or r["type"].startswith("EX-99")]
            sources = []
            for row in rows:
                body, record = fetcher.get(f"https://www.sec.gov{row['path']}", f"{ticker}-{accession}-{row['document']}")
                sources.append({"url": record["url"], "published_utc": iso(accepted),
                                "document_type": row["type"], "sha256": record["sha256"],
                                "text": extract_text(body)})
            payload = {"model": runner.MODEL, "state": {"ticker": ticker, "decision_cutoff_utc": iso(accepted),
                                                        "sources": sources}, "questions": runner.QUESTIONS}
            size = len(json.dumps(payload, ensure_ascii=False).encode())
            filings.append({"accession": accession, "items": recent["items"][i], "acceptance_utc": iso(accepted),
                            "acceptance_header_et": raw,
                            "json_minus_header_seconds": (stamp(recent["acceptanceDateTime"][i]) - accepted).total_seconds(),
                            "documents": [{"type": s["document_type"], "sha256": s["sha256"],
                                           "text_chars": len(s["text"])} for s in sources],
                            "jev_request_bytes": size, "fits_20kb": size <= 20000})
        covered = [t for t in times if any(t - max_age < stamp(f["acceptance_utc"]) <= t for f in filings)]
        fitting = [t for t in times if any(t - max_age < stamp(f["acceptance_utc"]) <= t and f["fits_20kb"]
                                           for f in filings)]
        result["tickers"][ticker] = {"filings": filings, "observations_with_8k": len(covered),
                                     "observations_with_fitting_8k": len(fitting)}
    total = len(times) * len(mapping["mapping"])
    result["totals"] = {
        "observations": total,
        "with_8k": sum(t["observations_with_8k"] for t in result["tickers"].values()),
        "with_fitting_8k": sum(t["observations_with_fitting_8k"] for t in result["tickers"].values()),
        "filings": sum(len(t["filings"]) for t in result["tickers"].values()),
        "filings_fitting_20kb": sum(f["fits_20kb"] for t in result["tickers"].values() for f in t["filings"]),
        "json_minus_header_seconds": sorted({f["json_minus_header_seconds"] for t in result["tickers"].values()
                                            for f in t["filings"]}),
        "requests": len(fetcher.records)}
    for path in scratch.iterdir():
        path.unlink()  # census keeps hashes and sizes only
    scratch.rmdir()
    with args.report.open("x") as file:
        file.write(json.dumps(result | {"requests": fetcher.records}, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(result["totals"], indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--design", type=Path, default=DESIGN)
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("map")
    p.add_argument("--out", type=Path, required=True)
    p = sub.add_parser("capture")
    p.add_argument("--mapping", type=Path, required=True)
    p.add_argument("--ticker", required=True)
    p.add_argument("--cutoff", required=True, help="Decision cutoff with explicit time zone")
    p.add_argument("--out", type=Path, required=True)
    p = sub.add_parser("replay")
    p.add_argument("--observation", type=Path, required=True)
    p = sub.add_parser("census")
    p.add_argument("--mapping", type=Path, required=True)
    p.add_argument("--end", required=True, help="Last ET date, YYYY-MM-DD")
    p.add_argument("--days", type=int, default=90)
    p.add_argument("--out", type=Path, required=True, help="Scratch directory, removed after the census")
    p.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    {"map": command_map, "capture": command_capture, "replay": command_replay,
     "census": command_census}[args.command](args)


if __name__ == "__main__":
    main()
