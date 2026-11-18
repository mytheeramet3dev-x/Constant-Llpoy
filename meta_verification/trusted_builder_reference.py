#!/usr/bin/env python3
"""Local contract-validation reference; deliberately does not sign or attest.

This module is a test fixture for the external Trusted Builder Contract. It is
not an independent builder, is not a trust anchor, and must never emit SIGNED.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import stat
from pathlib import Path, PurePosixPath
from typing import Any

SHA40 = re.compile(r"^[0-9a-f]{40}$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
DEFAULT_MAX_BYTES = 1_048_576


class BuilderValidationError(ValueError):
    """Input failed a fail-closed contract check."""


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise BuilderValidationError(message)


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        _require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _reject_constant(value: str) -> None:
    raise BuilderValidationError(f"non-standard JSON constant is forbidden: {value}")


def _strict_json(data: bytes) -> dict[str, Any]:
    try:
        decoded = data.decode("utf-8", errors="strict")
        value = json.loads(decoded, object_pairs_hook=_unique_object, parse_constant=_reject_constant)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise BuilderValidationError(f"subject is not strict UTF-8 JSON: {exc}") from None
    _require(isinstance(value, dict), "evidence subject must be a JSON object")
    return value


def _read_subject(root: Path, relative_path: str, max_bytes: int) -> bytes:
    """Read through directory file descriptors; reject symlinks without TOCTOU path checks."""
    _require(isinstance(relative_path, str) and bool(relative_path), "subject_path must be non-empty")
    _require(chr(92) not in relative_path, "backslash path separators are not accepted")
    posix = PurePosixPath(relative_path)
    _require(not posix.is_absolute(), "absolute subject path is forbidden")
    _require(all(part not in ("", ".", "..") for part in relative_path.split("/")),
             "non-canonical or traversal subject path is forbidden")
    _require(hasattr(os, "O_NOFOLLOW") and hasattr(os, "O_DIRECTORY"),
             "platform lacks required no-follow directory-open flags")

    root_fd = None
    current_fd = None
    file_fd = None
    try:
        root_real = root.resolve(strict=True)
        root_fd = os.open(root_real, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
        _require(stat.S_ISDIR(os.fstat(root_fd).st_mode), "checkout root is not a directory")
        current_fd = root_fd
        for part in posix.parts[:-1]:
            next_fd = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW,
                              dir_fd=current_fd)
            if current_fd != root_fd:
                os.close(current_fd)
            current_fd = next_fd

        file_fd = os.open(posix.parts[-1], os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK,
                          dir_fd=current_fd)
        _require(stat.S_ISREG(os.fstat(file_fd).st_mode), "subject must be a regular file")
        chunks: list[bytes] = []
        total = 0
        while total <= max_bytes:
            chunk = os.read(file_fd, min(65536, max_bytes + 1 - total))
            if not chunk:
                break
            chunks.append(chunk)
            total += len(chunk)
        _require(0 < total <= max_bytes, "subject is empty or exceeds size limit")
        return b"".join(chunks)
    except BuilderValidationError:
        raise
    except (OSError, ValueError) as exc:
        raise BuilderValidationError(f"subject path could not be safely opened: {exc}") from None
    finally:
        if file_fd is not None:
            os.close(file_fd)
        if current_fd is not None and current_fd != root_fd:
            os.close(current_fd)
        if root_fd is not None:
            os.close(root_fd)


def _validate_evidence(record: dict[str, Any], *, source_commit: str,
                       expected_repository: str, expected_run_id: int) -> None:
    expected_keys = {
        "schema_version", "repository", "run_id", "head_sha", "workflow_id",
        "workflow_path", "workflow_blob_sha", "evaluator_path", "evaluator_blob_sha",
        "event", "branch", "run_attempt", "workflow_conclusion", "jobs",
        "status", "failure_reasons", "record_sha256",
    }
    _require(set(record) == expected_keys, "evidence record has missing or unknown fields")
    _require(record["schema_version"] == "1.0", "unsupported evidence schema version")
    _require(record["repository"] == expected_repository, "evidence repository mismatch")
    _require(type(record["run_id"]) is int and record["run_id"] == expected_run_id,
             "evidence run ID mismatch")
    _require(record["head_sha"] == source_commit, "evidence source commit mismatch")
    for key in ("head_sha", "workflow_blob_sha", "evaluator_blob_sha"):
        _require(isinstance(record[key], str) and SHA40.fullmatch(record[key]) is not None,
                 f"invalid {key}")
    _require(record["status"] == "ACCEPTED", "upstream evidence is not ACCEPTED")
    _require(record["workflow_conclusion"] == "success", "upstream workflow did not succeed")
    _require(record["failure_reasons"] == [], "upstream evidence contains failure reasons")
    _require(isinstance(record["jobs"], list) and bool(record["jobs"]), "evidence jobs are empty")
    canonical_record = dict(record)
    claimed_digest = canonical_record.pop("record_sha256")
    canonical = json.dumps(canonical_record, sort_keys=True, separators=(",", ":")).encode("utf-8")
    actual_digest = hashlib.sha256(canonical).hexdigest()
    _require(isinstance(claimed_digest, str) and SHA256.fullmatch(claimed_digest) is not None,
             "invalid evidence record digest")
    _require(actual_digest == claimed_digest, "evidence record digest mismatch")


def validate_subject(*, checkout_root: str | Path, subject_path: str,
                     expected_subject_sha256: str, source_commit: str,
                     caller: dict[str, Any], upstream: dict[str, Any],
                     expected_repository: str, expected_repository_id: int,
                     expected_workflow: str, expected_ref: str,
                     expected_run_id: int, max_subject_bytes: int = DEFAULT_MAX_BYTES) -> dict[str, Any]:
    """Validate one evidence subject and return a NON-SIGNING local report."""
    _require(isinstance(expected_subject_sha256, str) and
             SHA256.fullmatch(expected_subject_sha256) is not None,
             "expected_subject_sha256 must be lowercase SHA-256")
    _require(isinstance(source_commit, str) and SHA40.fullmatch(source_commit) is not None,
             "source_commit must be a full lowercase Git SHA")
    _require(type(max_subject_bytes) is int and max_subject_bytes > 0, "invalid subject size limit")
    _require(type(expected_run_id) is int and expected_run_id > 0, "invalid expected run ID")
    _require(type(expected_repository_id) is int and expected_repository_id > 0,
             "invalid expected repository ID")
    _require(isinstance(expected_repository, str) and "/" in expected_repository,
             "invalid expected repository name")
    _require(isinstance(expected_workflow, str) and bool(expected_workflow),
             "invalid expected workflow identity")
    _require(isinstance(expected_ref, str) and expected_ref.startswith("refs/heads/"),
             "expected ref must be a branch ref")

    _require(isinstance(caller, dict), "caller identity is missing")
    _require(caller.get("repository") == expected_repository, "caller repository mismatch")
    _require(type(caller.get("repository_id")) is int and
             caller.get("repository_id") == expected_repository_id, "caller repository ID mismatch")
    _require(caller.get("workflow") == expected_workflow, "caller workflow mismatch")
    _require(caller.get("ref") == expected_ref, "caller ref mismatch")

    _require(isinstance(upstream, dict), "upstream run metadata is missing")
    _require(type(upstream.get("run_id")) is int and upstream["run_id"] == expected_run_id,
             "upstream run ID mismatch")
    _require(upstream.get("status") == "completed", "upstream run is not completed")
    _require(upstream.get("conclusion") == "success", "upstream run did not succeed")
    _require(upstream.get("head_sha") == source_commit, "upstream source commit mismatch")
    _require(type(upstream.get("repository_id")) is int and
             upstream.get("repository_id") == expected_repository_id,
             "upstream repository ID mismatch")
    _require(upstream.get("workflow") == expected_workflow, "upstream workflow mismatch")
    _require(upstream.get("ref") == expected_ref, "upstream ref mismatch")

    raw = _read_subject(Path(checkout_root), subject_path, max_subject_bytes)
    size = len(raw)
    actual_sha256 = hashlib.sha256(raw).hexdigest()
    _require(actual_sha256 == expected_subject_sha256, "subject SHA-256 mismatch")
    record = _strict_json(raw)
    _validate_evidence(record, source_commit=source_commit,
                       expected_repository=expected_repository, expected_run_id=expected_run_id)

    return {
        "schema_version": "1.0",
        "status": "VALIDATED_LOCAL_UNTRUSTED",
        "signing_performed": False,
        "attestation_created": False,
        "trust_established": False,
        "builder_class": "same-repository-local-reference",
        "caller_repository": expected_repository,
        "caller_repository_id": expected_repository_id,
        "caller_workflow": expected_workflow,
        "caller_ref": expected_ref,
        "source_commit": source_commit,
        "upstream_run_id": expected_run_id,
        "subject_path": subject_path,
        "subject_sha256": actual_sha256,
        "subject_size_bytes": size,
        "limitations": [
            "This is not an independently administered builder.",
            "No signing key, OIDC token, or attestation is created.",
            "The report is not a trusted-builder report and must not be labeled SIGNED.",
            "Caller and upstream metadata are supplied by the local test harness, not independently authenticated here.",
        ],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="JSON file containing validation arguments")
    parser.add_argument("--output", required=True, help="write the local validation report")
    args = parser.parse_args(argv)
    try:
        payload = json.loads(Path(args.input).read_text(encoding="utf-8"),
                             object_pairs_hook=_unique_object)
        report = validate_subject(**payload)
        Path(args.output).write_text(json.dumps(report, indent=2, sort_keys=True) + "\n",
                                     encoding="utf-8")
        print(json.dumps({"status": report["status"], "signing_performed": False,
                          "subject_sha256": report["subject_sha256"]}, sort_keys=True))
        return 0
    except (OSError, KeyError, TypeError, ValueError) as exc:
        print(json.dumps({"status": "REJECTED", "error": str(exc)}, sort_keys=True))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
