#!/usr/bin/env python3
"""Verify GitHub/Sigstore provenance for a meta-verification evidence record."""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

POLICY_KEYS = {
    "schema_version", "repository", "repository_id", "signer_workflow",
    "source_ref", "oidc_issuer", "predicate_type", "require_verified_timestamps",
    "deny_self_hosted_runners",
}
SHA1 = re.compile(r"^[0-9a-f]{40}$")

class ProvenanceError(ValueError):
    pass

def require(condition: bool, message: str) -> None:
    if not condition:
        raise ProvenanceError(message)

def validate_policy(policy: Any) -> dict:
    require(isinstance(policy, dict) and set(policy) == POLICY_KEYS,
            "policy has missing or unknown fields")
    require(policy["schema_version"] == "1.0", "unsupported policy schema")
    require(isinstance(policy["repository"], str) and
            re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", policy["repository"]) is not None,
            "invalid repository")
    require(isinstance(policy["repository_id"], int) and policy["repository_id"] > 0,
            "invalid repository_id")
    require(isinstance(policy["signer_workflow"], str) and
            policy["signer_workflow"].startswith(policy["repository"] + "/.github/workflows/"),
            "signer_workflow must be a workflow path in the expected repository")
    require(isinstance(policy["source_ref"], str) and policy["source_ref"].startswith("refs/heads/"),
            "source_ref must be a branch ref")
    require(policy["oidc_issuer"] == "https://token.actions.githubusercontent.com",
            "unexpected OIDC issuer")
    require(policy["predicate_type"] == "https://slsa.dev/provenance/v1",
            "unsupported predicate type")
    require(policy["require_verified_timestamps"] is True,
            "verified timestamps must be required")
    require(policy["deny_self_hosted_runners"] is True,
            "self-hosted runners must be denied")
    return policy

def _validate_entry(entry: Any, expected_digest: str, policy: dict,
                    source_sha: str) -> dict:
    require(isinstance(entry, dict), "verification result entry is not an object")
    vr = entry.get("verificationResult")
    require(isinstance(vr, dict), "missing verificationResult")
    signature = vr.get("signature")
    require(isinstance(signature, dict), "missing signature result")
    certificate = signature.get("certificate")
    require(isinstance(certificate, dict), "missing verified signing certificate")

    # These fields are extracted from the verified signing certificate, not
    # from the producer-controlled SLSA predicate body.
    require(str(certificate.get("sourceRepositoryIdentifier")) == str(policy["repository_id"]),
            "signing certificate repository ID mismatch")
    require(certificate.get("sourceRepositoryRef") == policy["source_ref"],
            "signing certificate source ref mismatch")
    require(certificate.get("sourceRepositoryDigest") == source_sha,
            "signing certificate source commit mismatch")
    require(certificate.get("buildSignerDigest") == source_sha,
            "signing certificate signer workflow commit mismatch")

    timestamps = vr.get("verifiedTimestamps")
    require(isinstance(timestamps, list) and bool(timestamps),
            "no verified transparency-log/timestamp evidence")

    statement = vr.get("statement")
    require(isinstance(statement, dict), "missing verified in-toto statement")
    require(statement.get("predicateType") == policy["predicate_type"],
            "predicate type mismatch")
    subjects = statement.get("subject")
    require(isinstance(subjects, list) and bool(subjects), "statement has no subjects")
    matching = []
    for subject in subjects:
        if not isinstance(subject, dict):
            continue
        digest = subject.get("digest")
        if isinstance(digest, dict) and digest.get("sha256") == expected_digest:
            matching.append(subject)
    require(len(matching) == 1, "attestation subject does not uniquely match exact evidence bytes")
    return {
        "certificate_repository_id": str(certificate["sourceRepositoryIdentifier"]),
        "certificate_source_ref": certificate["sourceRepositoryRef"],
        "certificate_source_commit": certificate["sourceRepositoryDigest"],
        "certificate_signer_commit": certificate["buildSignerDigest"],
        "verified_timestamp_count": len(timestamps),
        "predicate_type": statement["predicateType"],
        "subject_sha256": expected_digest,
    }

def validate_cli_output(output: Any, subject_bytes: bytes, policy: Any, source_sha: str) -> dict:
    p = validate_policy(policy)
    require(isinstance(source_sha, str) and SHA1.fullmatch(source_sha) is not None,
            "source_sha must be a lowercase 40-character Git commit SHA")
    require(isinstance(subject_bytes, bytes) and bool(subject_bytes),
            "subject artifact is empty or not bytes")
    digest = hashlib.sha256(subject_bytes).hexdigest()
    require(isinstance(output, list) and bool(output), "gh returned no verified attestations")
    checks = [_validate_entry(entry, digest, p, source_sha) for entry in output]
    return {
        "schema_version": "1.0",
        "status": "VERIFIED",
        "repository": p["repository"],
        "repository_id": p["repository_id"],
        "signer_workflow": p["signer_workflow"],
        "source_ref": p["source_ref"],
        "source_commit": source_sha,
        "oidc_issuer": p["oidc_issuer"],
        "subject_sha256": digest,
        "verified_attestations": checks,
        "verification_tool": "GitHub CLI gh attestation verify",
    }

def verify_with_gh(subject_path: Path, policy: Any, source_sha: str) -> dict:
    p = validate_policy(policy)
    require(subject_path.is_file() and not subject_path.is_symlink(),
            "subject must be a regular non-symlink file")
    try:
        subject_bytes = subject_path.read_bytes()
    except OSError as exc:
        raise ProvenanceError(f"cannot read subject: {exc}") from None
    command = [
        "gh", "attestation", "verify", str(subject_path),
        "--repo", p["repository"],
        "--signer-workflow", p["signer_workflow"],
        "--cert-oidc-issuer", p["oidc_issuer"],
        "--predicate-type", p["predicate_type"],
        "--source-ref", p["source_ref"],
        "--source-digest", source_sha,
        "--signer-digest", source_sha,
        "--deny-self-hosted-runners",
        "--format", "json",
    ]
    try:
        completed = subprocess.run(command, capture_output=True, text=True,
                                   timeout=180, check=False)
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise ProvenanceError(f"gh attestation verify could not complete: {exc}") from None
    require(completed.returncode == 0,
            "gh attestation verify rejected provenance: " + (completed.stderr.strip() or "non-zero exit"))
    try:
        output = json.loads(completed.stdout)
    except json.JSONDecodeError:
        raise ProvenanceError("gh attestation verify returned malformed JSON") from None
    return validate_cli_output(output, subject_bytes, p, source_sha)

def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--policy", required=True)
    parser.add_argument("--subject", required=True)
    parser.add_argument("--source-sha", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args(argv)
    try:
        policy = json.loads(Path(args.policy).read_text(encoding="utf-8"))
        report = verify_with_gh(Path(args.subject), policy, args.source_sha)
        Path(args.output).write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(json.dumps({"status": report["status"], "repository_id": report["repository_id"],
                          "source_commit": report["source_commit"], "subject_sha256": report["subject_sha256"],
                          "verified_attestations": len(report["verified_attestations"])}, sort_keys=True))
        return 0
    except (OSError, json.JSONDecodeError, ProvenanceError) as exc:
        print(json.dumps({"status": "REJECTED", "error": str(exc)}, sort_keys=True))
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
