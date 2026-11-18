#!/usr/bin/env python3
"""Live smoke test: authenticate a real GitHub-attested collector evidence artifact.

This is an integration test of GitHub/Sigstore verification, not a production
component producer, external trust root, policy activation, or theorem checker.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import re
import stat
from pathlib import Path

from component_provenance_authenticator import authenticate_components
from status_aggregator import aggregate, AggregationError

COMPONENT_ID = "LIVE_META_VERIFICATION_RUN_EVIDENCE"
MAX_BYTES = 8 * 1024 * 1024
SHA40 = re.compile(r"^[0-9a-f]{40}$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _read_regular(path: str, label: str, limit: int) -> bytes:
    flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
    try:
        fd = os.open(path, flags)
    except OSError as exc:
        raise ValueError(f"{label} cannot be opened without following links: {exc}") from None
    try:
        info = os.fstat(fd)
        if not stat.S_ISREG(info.st_mode) or not 0 < info.st_size <= limit:
            raise ValueError(f"{label} is empty, non-regular, or oversized")
        chunks, total = [], 0
        while True:
            chunk = os.read(fd, min(65536, limit + 1 - total))
            if not chunk:
                break
            chunks.append(chunk)
            total += len(chunk)
            if total > limit:
                raise ValueError(f"{label} exceeds size limit")
        raw = b"".join(chunks)
        if len(raw) != info.st_size:
            raise ValueError(f"{label} changed while being read")
        return raw
    finally:
        os.close(fd)


def _json(raw: bytes, label: str):
    try:
        return json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=lambda value: (_ for _ in ()).throw(
                ValueError(f"{label}: non-standard JSON constant {value}")
            ),
        )
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"{label}: invalid UTF-8 JSON: {exc}") from None


def _canonical(value) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode("utf-8")


def run(subject_path: str, provenance_policy_path: str, expected_policy_sha256: str,
        source_commit: str, run_id: int, run_attempt: int) -> dict:
    if not isinstance(source_commit, str) or not SHA40.fullmatch(source_commit):
        raise ValueError("source commit must be a lowercase 40-character Git SHA")
    if type(run_id) is not int or run_id <= 0:
        raise ValueError("run ID must be a positive integer")
    if type(run_attempt) is not int or run_attempt <= 0:
        raise ValueError("run attempt must be a positive integer")
    if not isinstance(expected_policy_sha256, str) or not SHA256.fullmatch(expected_policy_sha256):
        raise ValueError("provenance-policy pin must be a SHA-256 digest")

    subject = _read_regular(subject_path, "attested subject", MAX_BYTES)
    provenance_policy_bytes = _read_regular(
        provenance_policy_path, "provenance policy", 1024 * 1024
    )
    provenance_policy = _json(provenance_policy_bytes, "provenance policy")
    subject_sha = hashlib.sha256(subject).hexdigest()

    # This policy digest is locally computed by the smoke workflow. It is not
    # an independently administered production trust anchor.
    policy = {
        "schema_version": "1.0",
        "claim_id": "LIVE-COMPONENT-PROVENANCE-SMOKE",
        "policy_revision": source_commit,
        "required_components": [COMPONENT_ID],
    }
    policy_bytes = _canonical(policy)
    bundle = {
        "schema_version": "1.0",
        "claim_id": policy["claim_id"],
        "source_commit": source_commit,
        "policy_revision": source_commit,
        "components": [{
            "component_id": COMPONENT_ID,
            "status": "PASS",
            "evidence_base64": base64.b64encode(subject).decode("ascii"),
            "evidence_sha256": subject_sha,
            "provenance": {
                "receipt_schema_version": "2.0",
                "subject_sha256": subject_sha,
                "source_commit": source_commit,
                "attestation_run_id": run_id,
                "attestation_run_attempt": run_attempt,
                "attestation_workflow_revision": source_commit,
            },
        }],
    }

    authenticated = authenticate_components(
        policy_bytes, provenance_policy_bytes, provenance_policy,
        bundle, source_commit, expected_policy_sha256,
    )
    result = aggregate(policy, bundle, source_commit, authenticated)
    if result["status"] != "ACCEPTED":
        raise AggregationError(
            f"authenticated smoke bundle did not aggregate to ACCEPTED: {result}"
        )
    receipt = authenticated[COMPONENT_ID]
    return {
        "status": "LIVE_COMPONENT_PROVENANCE_SMOKE_VERIFIED",
        "status_scope": "REAL_GITHUB_ATTESTATION_INTEGRATION_SMOKE_TEST_ONLY",
        "source_commit": source_commit,
        "attestation_run_id": run_id,
        "attestation_run_attempt": run_attempt,
        "subject_sha256": subject_sha,
        "verified_attestation_count": receipt["verified_attestation_count"],
        "aggregator_status": result["status"],
        "production_activation": "NOT_ACTIVE",
        "external_policy_pin": "NOT_INDEPENDENTLY_GOVERNED",
        "mathematical_correctness": "NOT_ASSESSED",
    }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--subject", required=True)
    parser.add_argument("--provenance-policy", required=True)
    parser.add_argument("--expected-provenance-policy-sha256", required=True)
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--run-id", required=True, type=int)
    parser.add_argument("--run-attempt", required=True, type=int)
    parser.add_argument("--output", required=True)
    args = parser.parse_args(argv)
    try:
        report = run(
            args.subject, args.provenance_policy,
            args.expected_provenance_policy_sha256,
            args.source_commit, args.run_id, args.run_attempt,
        )
        output = Path(args.output)
        with output.open("x", encoding="utf-8") as stream:
            stream.write(json.dumps(report, indent=2, sort_keys=True) + "\n")
        print(json.dumps(report, sort_keys=True))
        return 0
    except (OSError, ValueError, AggregationError) as exc:
        print(json.dumps({
            "status": "ERROR",
            "status_scope": "REAL_GITHUB_ATTESTATION_INTEGRATION_SMOKE_TEST_ONLY",
            "error": str(exc),
            "production_activation": "NOT_ACTIVE",
        }, sort_keys=True))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
