#!/usr/bin/env python3
"""Classify dated stock catalyst evidence with Jev; record results and costs, place no orders."""

import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import time
import urllib.error
import urllib.request

MODEL = "jev-1.13.0"
SPEC = "stock-catalyst-v1"
ENDPOINT = "https://api.typesafe.ai/v1/systemone"
PRICE = {"currency": "USD", "input_per_million": 0.042, "output_per_million": 0,
         "source": "https://docs.typesafe.ai/models.md", "checked_on": "2026-10-02"}
QUESTIONS = {
    "catalyst": {
        "type": "choice",
        "instructions": "Classify the principal event documented in `sources`. Use only the supplied text. An expected future milestone is not a completed regulatory event. When distinct current events are equally central choose mixed_other. With no documented event choose unknown. Do not predict returns or assign a trading action.",
        "criteria": {
            "earnings_guidance": "Reported financial results or financial guidance update.",
            "regulatory_clinical": "Completed regulatory decision or reported clinical trial result.",
            "commercial_operation": "Executed customer contract, distribution agreement, or demonstrated operational improvement.",
            "financing_dilution": "Capital raised by issuing stock, warrants or convertible securities, including a PIPE closing.",
            "nonbinding_plan": "Exploratory memorandum, letter of intent or planned venture without an executed commercial commitment.",
            "asset_cash_receipt": "Cash received from an existing asset-sale obligation or escrow; no new operating contract.",
            "fixed_price_acquisition": "Definitive acquisition or buyout at a fixed cash price.",
            "mixed_other": "Several equally central current events or a documented event outside these categories.",
            "unknown": "No event text is supplied or the supplied evidence cannot establish an event."
        }
    },
    "dilutive_financing": {
        "type": "noul",
        "instructions": "Do `sources` explicitly document a current issuance of shares, warrants or convertible securities to raise capital? Only use supplied evidence.",
        "criteria": {"true": "An equity or equity-linked financing is stated as agreed or completed.",
                     "false": "No such financing is evidenced, including funding explicitly achieved without an equity offering."}
    },
    "binding_commercial_activity": {
        "type": "noul",
        "instructions": "Do `sources` document a new executed commercial customer, revenue or distribution commitment, or an already demonstrated improvement in operating activity? Only use supplied evidence.",
        "criteria": {"true": "Executed commercial activity or a demonstrated operating improvement is documented.",
                     "false": "Only plans, an exploratory non-binding venture, securities financing, an old asset-sale payment, or no event is documented."}
    }
}


def now():
    return datetime.now(timezone.utc).isoformat()


def save(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def iso(value):
    result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if result.tzinfo is None:
        raise ValueError("Evidence timestamps must include a time zone")
    return result


def requests_for(batch):
    cases = batch["cases"]
    if not 1 <= len(cases) <= 20 or len({c["id"] for c in cases}) != len(cases):
        raise ValueError("Use 1-20 cases with unique IDs")
    result = []
    for case in cases:
        cutoff = iso(case["state"]["decision_cutoff_utc"])
        for source in case["state"]["sources"]:
            if iso(source["published_utc"]) > cutoff:
                raise ValueError(f"{case['id']}: source published after decision cutoff")
        payload = {"model": MODEL, "state": case["state"], "questions": QUESTIONS}
        encoded = json.dumps(payload, ensure_ascii=False).encode()
        if len(encoded) > 20000:
            raise ValueError(f"{case['id']}: exceeds this runner's 20KB request limit")
        result.append((case, payload, encoded))
    return result


def validate(response):
    if response["model"] != MODEL:
        raise ValueError("Returned model differs from pinned model")
    answers = response["answers"]
    for key, question in QUESTIONS.items():
        answer = answers[key]
        if answer["type"] != question["type"]:
            raise ValueError(f"{key}: answer type mismatch")
        if question["type"] == "choice":
            probabilities = answer["probabilities"]
            if set(probabilities) != set(question["criteria"]):
                raise ValueError(f"{key}: missing or unexpected labels")
            values = list(probabilities.values()) + [answer["confidence"]]
            if answer["choice"] not in probabilities or not math.isclose(sum(probabilities.values()), 1, abs_tol=0.002):
                raise ValueError(f"{key}: invalid choice distribution")
        else:
            values = [answer["noul"]]
        if any(not isinstance(v, (int, float)) or not math.isfinite(v) or not 0 <= v <= 1 for v in values):
            raise ValueError(f"{key}: invalid probability")
    for field in ["input_tokens", "output_tokens"]:
        if type(response["usage"][field]) is not int or response["usage"][field] < 0:
            raise ValueError("Invalid token usage")


def summary(records):
    known = [r for r in records if isinstance(r.get("response", {}).get("usage", {}).get("input_tokens"), int)
             and r["response"].get("model") == MODEL]
    usage = {field: sum(r["response"]["usage"].get(field, 0) for r in known)
             for field in ["input_tokens", "output_tokens"]}
    valid = [r for r in records if r.get("status") == "ok"]
    comparisons = []
    for r in valid:
        answers = r["response"]["answers"]
        predicted = {"catalyst": answers["catalyst"]["choice"],
                     "dilutive_financing": answers["dilutive_financing"]["noul"] >= 0.5,
                     "binding_commercial_activity": answers["binding_commercial_activity"]["noul"] >= 0.5}
        gold = r["case"].get("expected", {})
        comparisons.append({"id": r["case"]["id"], "kind": r["case"]["kind"],
                            "ticker": r["case"]["state"]["ticker"], "predicted": predicted,
                            "expected": gold, "matches": {k: predicted[k] == v for k, v in gold.items()},
                            "confidence": answers["catalyst"]["confidence"]})
    estimate = usage["input_tokens"] * PRICE["input_per_million"] / 1_000_000
    return {"calls_attempted": len(records), "calls_validated": len(valid),
            "calls_with_known_usage": len(known), "usage_known": usage,
            "estimated_cost_usd_known": estimate,
            "estimated_cost_usd_total": estimate if len(known) == len(records) else None,
            "measured_charge": None, "pricing": PRICE, "comparisons": comparisons,
            "limit": "Retrospective/synthetic interface checks; no prospective accuracy or trading edge measured."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path)
    parser.add_argument("--out-dir", type=Path)
    parser.add_argument("--run", action="store_true", help="Send requests; default only prints validated request bodies")
    parser.add_argument("--replay", type=Path, help="Summarize archived responses without network requests")
    args = parser.parse_args()
    if args.replay:
        records = [json.loads(p.read_text()) for p in sorted(args.replay.glob("case-*.json"))]
        print(json.dumps(summary(records), indent=2))
        return
    if not args.input:
        parser.error("--input is required")
    batch = json.loads(args.input.read_text())
    requests = requests_for(batch)
    if not args.run:
        print(json.dumps([payload for _, payload, _ in requests], indent=2))
        return
    if not args.out_dir:
        parser.error("--run requires --out-dir")
    key = os.environ.get("TYPESAFE_API_KEY")
    if not key:
        parser.error("TYPESAFE_API_KEY is missing")
    args.out_dir.mkdir(parents=True, exist_ok=False)
    save(args.out_dir / "inputs.json", batch)
    manifest = {"spec": SPEC, "model_requested": MODEL, "started_utc": now(), "status": "running",
                "input_sha256": hashlib.sha256(args.input.read_bytes()).hexdigest(), "endpoint": ENDPOINT}
    save(args.out_dir / "manifest.json", manifest)
    records = []
    for index, (case, payload, encoded) in enumerate(requests, 1):
        record = {"case": case, "request": payload, "started_utc": now(), "status": "attempted"}
        target = args.out_dir / f"case-{index:02d}.json"
        save(target, record)
        started = time.monotonic()
        request = urllib.request.Request(ENDPOINT, data=encoded, method="POST",
                                         headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                record["http_status"] = response.status
                record["response"] = json.load(response)
            validate(record["response"])
            record["status"] = "ok"
        except urllib.error.HTTPError as error:
            record.update(status="failed", http_status=error.code, error_body=error.read().decode(errors="replace"))
        except (OSError, ValueError, KeyError, TypeError) as error:
            record.update(status="failed", error=f"{type(error).__name__}: {error}")
        record.update(finished_utc=now(), elapsed_seconds=time.monotonic() - started)
        save(target, record)
        records.append(record)
        manifest.update(summary=summary(records))
        save(args.out_dir / "manifest.json", manifest)
        if record["status"] != "ok":
            break  # A failure needs investigation; retrying can hide usage or change the model evidence.
    manifest.update(finished_utc=now(), status="completed" if len(records) == len(requests)
                    and all(r["status"] == "ok" for r in records) else "failed")
    save(args.out_dir / "manifest.json", manifest)
    print(json.dumps(manifest, indent=2))
    if manifest["status"] == "failed":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
