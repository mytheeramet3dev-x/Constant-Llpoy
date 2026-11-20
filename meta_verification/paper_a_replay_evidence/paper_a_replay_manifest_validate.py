#!/usr/bin/env python3
"""Validate Paper A replay manifest structure and semantic consistency (stdlib only)."""
from __future__ import annotations
import argparse
import hashlib
import json
import re
from datetime import datetime
from pathlib import Path

SHA40 = re.compile(r"^[0-9a-f]{40}$")
SHA64 = re.compile(r"^[0-9a-f]{64}$")
STATUSES = {"PASS", "FAIL", "INCONCLUSIVE", "NOT_RUN"}
REQUIRED = {"schema_version", "project", "git_commit", "run_timestamp_utc",
             "environment", "command", "inputs", "artifacts", "checks", "scope", "limitations"}


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def validate_manifest(manifest, verify_files=False):
    _require(isinstance(manifest, dict), "manifest must be a JSON object")
    _require(not (set(manifest) - REQUIRED - {"reviewer_notes"}), "unknown top-level field(s)")
    _require(REQUIRED <= set(manifest), "missing required top-level field(s)")
    _require(manifest["schema_version"] == "1.0", "unsupported schema_version")
    _require(manifest["project"] == "Paper A", "project must equal 'Paper A'")
    _require(isinstance(manifest["git_commit"], str) and SHA40.fullmatch(manifest["git_commit"]),
             "git_commit must be a lowercase 40-hex SHA")
    _require(isinstance(manifest["command"], str) and manifest["command"].strip(), "command must be non-empty")
    _require(isinstance(manifest["scope"], str) and manifest["scope"].strip(), "scope must be non-empty")
    _require(isinstance(manifest["limitations"], list) and all(isinstance(x, str) for x in manifest["limitations"]),
             "limitations must be an array of strings")
    _require(isinstance(manifest["run_timestamp_utc"], str), "timestamp must be a string")
    try:
        timestamp = datetime.fromisoformat(manifest["run_timestamp_utc"].replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("run_timestamp_utc must be ISO-8601") from exc
    _require(timestamp.tzinfo is not None and timestamp.utcoffset().total_seconds() == 0,
             "run_timestamp_utc must include UTC timezone")
    env = manifest["environment"]
    _require(isinstance(env, dict) and set(env) == {"python_version", "platform", "dependencies"},
             "environment must contain exactly python_version, platform, dependencies")
    _require(all(isinstance(env[k], str) and env[k].strip() for k in ("python_version", "platform")),
             "environment version/platform must be non-empty strings")
    _require(isinstance(env["dependencies"], dict) and all(isinstance(k, str) and k and isinstance(v, str) and v for k,v in env["dependencies"].items()),
             "dependencies must map non-empty names to non-empty version strings")
    if "reviewer_notes" in manifest:
        _require(isinstance(manifest["reviewer_notes"], str), "reviewer_notes must be a string")
    for section in ("inputs", "artifacts"):
        records = manifest[section]
        _require(isinstance(records, list), f"{section} must be an array")
        seen = set()
        for record in records:
            _require(isinstance(record, dict) and set(record) <= ({"path", "sha256", "exact_values"} if section == "inputs" else {"path", "sha256"}),
                     f"invalid record in {section}")
            _require({"path", "sha256"} <= set(record), f"record missing path/hash in {section}")
            path, digest = record["path"], record["sha256"]
            _require(isinstance(path, str) and path.strip(), f"{section} path must be non-empty")
            _require(path not in seen, f"duplicate path in {section}: {path}")
            seen.add(path)
            _require(isinstance(digest, str) and SHA64.fullmatch(digest), f"invalid SHA-256 for {path}")
            if "exact_values" in record:
                _require(section == "inputs" and isinstance(record["exact_values"], dict) and
                         all(isinstance(k, str) and isinstance(v, str) for k,v in record["exact_values"].items()),
                         "exact_values must be string-to-string map and only on inputs")
            if verify_files:
                target = Path(path)
                _require(target.is_file(), f"referenced file missing or not regular file: {path}")
                actual = hashlib.sha256(target.read_bytes()).hexdigest()
                _require(actual == digest, f"hash mismatch for {path}")
    _require(isinstance(manifest["checks"], list), "checks must be an array")
    check_ids = set()
    for check in manifest["checks"]:
        _require(isinstance(check, dict) and set(check) <= {"check_id", "status", "details"},
                 "invalid check record")
        _require({"check_id", "status"} <= set(check), "check missing ID/status")
        cid, status = check["check_id"], check["status"]
        _require(isinstance(cid, str) and cid.strip() and cid not in check_ids, "empty or duplicate check_id")
        check_ids.add(cid)
        _require(status in STATUSES, f"invalid status for {cid}")
        _require("details" not in check or isinstance(check["details"], str), "check details must be string")
    return True


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", help="JSON replay manifest to validate")
    parser.add_argument("--verify-files", action="store_true", help="also recompute all recorded file hashes")
    args = parser.parse_args(argv)
    try:
        manifest = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
        validate_manifest(manifest, verify_files=args.verify_files)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        parser.error(str(exc))
    print("Manifest validation: PASS" + (" (files verified)" if args.verify_files else " (structure/semantics only)"))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
