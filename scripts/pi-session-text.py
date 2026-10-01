#!/usr/bin/env python3
"""Extract Pi message text as JSONL without inferring a session-wide schema."""

import argparse
import json
from pathlib import Path


def messages(path):
    with path.open() as source:
        for line_number, line in enumerate(source, 1):
            if not line.strip():
                continue
            try:
                event = json.loads(line)
            except json.JSONDecodeError as error:
                raise ValueError(f"{path}:{line_number}: {error.msg}") from error
            if event.get("type") != "message":
                continue
            message = event.get("message") or {}
            content = message.get("content", [])
            if isinstance(content, str):
                text = content
            elif isinstance(content, list):
                text = "\n".join(
                    item["text"] for item in content
                    if isinstance(item, dict) and item.get("type") == "text"
                    and isinstance(item.get("text"), str)
                )
            else:
                text = ""
            if not text and not message.get("errorMessage"):
                continue
            yield {
                "timestamp": event.get("timestamp"),
                "role": message.get("role"),
                "text": text,
                "toolName": message.get("toolName"),
                "toolCallId": message.get("toolCallId"),
                "isError": message.get("isError"),
                "stopReason": message.get("stopReason"),
                "errorMessage": message.get("errorMessage"),
            }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("session_file", type=Path)
    parser.add_argument("--role", action="append", help="Include this role; repeat for multiple roles")
    parser.add_argument("--contains", help="Include messages containing this literal text or error")
    args = parser.parse_args()
    try:
        for message in messages(args.session_file):
            if args.role and message["role"] not in args.role:
                continue
            if args.contains and args.contains not in (
                message["text"] + "\n" + (message["errorMessage"] or "")
            ):
                continue
            print(json.dumps(message, ensure_ascii=False))
    except (OSError, ValueError) as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()
