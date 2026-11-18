#!/usr/bin/env python3
"""Fail-closed verifier for an externally governed Constant Llpoy trust-root package."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

SHA1 = re.compile(r"^[0-9a-f]{40}$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
MANIFEST_KEYS = {
    "schema_version", "trust_root_id", "sequence", "issued_at", "expires_at",
    "relying_party", "authorized_signer", "trusted_builder",
}


class TrustRootError(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise TrustRootError(message)


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _utc(value: Any, field: str) -> datetime:
    require(isinstance(value, str), f"{field} must be an ISO-8601 string")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        raise TrustRootError(f"{field} is not valid ISO-8601") from None
    require(parsed.tzinfo is not None, f"{field} must include a timezone")
    return parsed.astimezone(timezone.utc)


def _repo(value: Any, field: str) -> str:
    require(isinstance(value, str) and re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", value) is not None,
            f"{field} must be owner/repository")
    return value


def _positive_int(value: Any, field: str) -> int:
    require(type(value) is int and value > 0, f"{field} must be a positive integer")
    return value


def validate_manifest(manifest: Any, *, relying_repository: str, relying_repository_id: int,
                      trust_root_repository: str, trust_root_repository_id: int,
                      expected_signer_workflow: str, expected_signer_ref: str,
                      expected_signer_commit: str, expected_builder_repository: str,
                      expected_builder_repository_id: int, expected_builder_workflow: str,
                      expected_builder_commit: str, now: datetime | None = None) -> dict:
    require(isinstance(manifest, dict) and set(manifest) == MANIFEST_KEYS,
            "trust-root manifest has missing or unknown fields")
    require(manifest["schema_version"] == "1.0", "unsupported trust-root manifest schema")
    require(isinstance(manifest["trust_root_id"], str) and manifest["trust_root_id"].strip(),
            "trust_root_id must be non-empty")
    sequence = _positive_int(manifest["sequence"], "sequence")

    issued = _utc(manifest["issued_at"], "issued_at")
    expires = _utc(manifest["expires_at"], "expires_at")
    instant = now or datetime.now(timezone.utc)
    if instant.tzinfo is None:
        instant = instant.replace(tzinfo=timezone.utc)
    instant = instant.astimezone(timezone.utc)
    require(issued < expires, "trust-root validity interval is empty or reversed")
    require(issued <= instant < expires, "trust-root manifest is not currently valid")

    relying = manifest["relying_party"]
    require(isinstance(relying, dict) and set(relying) == {"repository", "repository_id"},
            "relying_party has missing or unknown fields")
    require(_repo(relying["repository"], "relying_party.repository") == relying_repository,
            "trust root is not scoped to this relying repository")
    require(_positive_int(relying["repository_id"], "relying_party.repository_id") == relying_repository_id,
            "relying-party repository ID mismatch")

    signer = manifest["authorized_signer"]
    signer_keys = {"workflow", "source_ref", "oidc_issuer", "predicate_type", "commit"}
    require(isinstance(signer, dict) and set(signer) == signer_keys,
            "authorized_signer has missing or unknown fields")
    require(signer["workflow"] == expected_signer_workflow, "authorized signer workflow mismatch")
    require(signer["source_ref"] == expected_signer_ref, "authorized signer source ref mismatch")
    require(signer["oidc_issuer"] == "https://token.actions.githubusercontent.com",
            "authorized signer OIDC issuer mismatch")
    require(signer["predicate_type"] == "https://slsa.dev/provenance/v1",
            "authorized signer predicate type mismatch")
    require(signer["commit"] == expected_signer_commit and
            isinstance(signer["commit"], str) and SHA1.fullmatch(signer["commit"]) is not None,
            "authorized signer commit mismatch or malformed commit")

    builder = manifest["trusted_builder"]
    builder_keys = {"repository", "repository_id", "workflow", "commit"}
    require(isinstance(builder, dict) and set(builder) == builder_keys,
            "trusted_builder has missing or unknown fields")
    builder_repo = _repo(builder["repository"], "trusted_builder.repository")
    require(builder_repo == expected_builder_repository, "trusted builder repository mismatch")
    require(builder_repo not in {relying_repository, trust_root_repository},
            "trusted builder must be separate from both relying party and trust root")
    require(_positive_int(builder["repository_id"], "trusted_builder.repository_id") ==
            expected_builder_repository_id, "trusted builder repository ID mismatch")
    require(builder["workflow"] == expected_builder_workflow, "trusted builder workflow mismatch")
    require(builder["commit"] == expected_builder_commit and
            isinstance(builder["commit"], str) and SHA1.fullmatch(builder["commit"]) is not None,
            "trusted builder commit mismatch or malformed commit")

    require(trust_root_repository != relying_repository,
            "trust-root repository must be external to the relying repository")
    _positive_int(trust_root_repository_id, "trust_root_repository_id")
    return {
        "schema_version": "1.0",
        "status": "TRUST_ROOT_POLICY_VALID",
        "trust_root_id": manifest["trust_root_id"],
        "trust_root_repository": trust_root_repository,
        "trust_root_repository_id": trust_root_repository_id,
        "trust_root_sequence": sequence,
        "relying_repository": relying_repository,
        "authorized_signer": signer,
        "trusted_builder": builder,
        "valid_from": issued.isoformat(),
        "valid_until": expires.isoformat(),
        "builder_integration_status": "AUTHORIZED_BY_ROOT_BUT_NOT_YET_USED_BY_CURRENT_PRODUCER",
    }


def _git(root: Path, *args: str) -> str:
    try:
        result = subprocess.run(["git", "-C", str(root), *args], capture_output=True,
                                text=True, timeout=20, check=False)
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise TrustRootError(f"cannot inspect trust-root checkout: {exc}") from None
    require(result.returncode == 0, "git trust-root identity check failed")
    return result.stdout.strip()


def _normalise_remote(remote: str) -> str:
    value = remote.strip()
    if value.startswith("git@github.com:"):
        value = value[len("git@github.com:"):]
    else:
        parsed = urlparse(value)
        require(parsed.hostname == "github.com", "trust-root remote is not hosted on github.com")
        value = parsed.path.lstrip("/")
    value = value.removesuffix(".git").strip("/")
    return value


def verify_package(root: Path, *, trust_root_repository: str, trust_root_repository_id: int,
                   trust_root_commit: str, manifest_path: str, signature_path: str,
                   public_key_path: str, expected_manifest_sha256: str,
                   expected_public_key_sha256: str, relying_repository: str,
                   relying_repository_id: int, expected_signer_workflow: str,
                   expected_signer_ref: str, expected_signer_commit: str,
                   expected_builder_repository: str, expected_builder_repository_id: int,
                   expected_builder_workflow: str, expected_builder_commit: str) -> dict:
    require(SHA1.fullmatch(trust_root_commit) is not None, "trust-root commit must be a full Git SHA")
    require(SHA256.fullmatch(expected_manifest_sha256) is not None, "expected manifest SHA-256 is malformed")
    require(SHA256.fullmatch(expected_public_key_sha256) is not None, "expected public-key SHA-256 is malformed")
    require(root.is_dir() and not root.is_symlink(), "trust-root checkout must be a real directory")
    actual_remote = _normalise_remote(_git(root, "remote", "get-url", "origin"))
    require(actual_remote.lower() == trust_root_repository.lower(), "trust-root checkout remote mismatch")
    actual_commit = _git(root, "rev-parse", "HEAD")
    require(actual_commit == trust_root_commit, "trust-root checkout commit mismatch")

    manifest_file = root / manifest_path
    signature_file = root / signature_path
    public_key_file = root / public_key_path
    for item in (manifest_file, signature_file, public_key_file):
        require(item.is_file() and not item.is_symlink(), f"required trust-root file missing or unsafe: {item.name}")
    manifest_bytes = manifest_file.read_bytes()
    signature_bytes = signature_file.read_bytes()
    public_key_bytes = public_key_file.read_bytes()
    require(hashlib.sha256(manifest_bytes).hexdigest() == expected_manifest_sha256,
            "trust-root manifest digest mismatch")
    require(hashlib.sha256(public_key_bytes).hexdigest() == expected_public_key_sha256,
            "trust-root public-key fingerprint mismatch")
    require(bool(signature_bytes) and bool(public_key_bytes), "trust-root signature or public key is empty")

    try:
        manifest = json.loads(manifest_bytes.decode("utf-8"), object_pairs_hook=_unique_object)
    except (UnicodeDecodeError, json.JSONDecodeError):
        raise TrustRootError("trust-root manifest is not valid UTF-8 JSON") from None

    # Ed25519 verification is delegated to the pinned runner's OpenSSL CLI.
    # The public-key fingerprint is pinned outside this repository in the
    # protected GitHub Environment; a key shipped beside its own signature
    # is never trusted on its own.
    import tempfile
    with tempfile.TemporaryDirectory(prefix="constant-llpoy-trust-root-") as temp:
        temp_path = Path(temp)
        pub = temp_path / "trust-root.pub"
        sig = temp_path / "trust-root.sig"
        data = temp_path / "trust-root.json"
        pub.write_bytes(public_key_bytes)
        sig.write_bytes(signature_bytes)
        data.write_bytes(manifest_bytes)
        try:
            verified = subprocess.run(
                ["openssl", "pkeyutl", "-verify", "-pubin", "-inkey", str(pub),
                 "-rawin", "-in", str(data), "-sigfile", str(sig)],
                capture_output=True, text=True, timeout=30, check=False)
        except (OSError, subprocess.TimeoutExpired) as exc:
            raise TrustRootError(f"OpenSSL signature verification unavailable: {exc}") from None
        require(verified.returncode == 0, "trust-root Ed25519 signature verification failed")

    report = validate_manifest(
        manifest, relying_repository=relying_repository, relying_repository_id=relying_repository_id,
        trust_root_repository=trust_root_repository, trust_root_repository_id=trust_root_repository_id,
        expected_signer_workflow=expected_signer_workflow, expected_signer_ref=expected_signer_ref,
        expected_signer_commit=expected_signer_commit, expected_builder_repository=expected_builder_repository,
        expected_builder_repository_id=expected_builder_repository_id,
        expected_builder_workflow=expected_builder_workflow, expected_builder_commit=expected_builder_commit)
    report["trust_root_commit"] = actual_commit
    report["manifest_sha256"] = expected_manifest_sha256
    report["public_key_sha256"] = expected_public_key_sha256
    report["signature_algorithm"] = "Ed25519"
    report["signature_verification"] = "VERIFIED"
    return report


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args(argv)
    try:
        def env(name: str) -> str:
            value = __import__("os").environ.get(name, "")
            require(bool(value), f"required protected environment variable is missing: {name}")
            return value
        report = verify_package(
            Path(args.root),
            trust_root_repository=env("TRUST_ROOT_REPOSITORY"),
            trust_root_repository_id=int(env("TRUST_ROOT_REPOSITORY_ID")),
            trust_root_commit=env("TRUST_ROOT_COMMIT"),
            manifest_path=env("TRUST_ROOT_MANIFEST_PATH"),
            signature_path=env("TRUST_ROOT_SIGNATURE_PATH"),
            public_key_path=env("TRUST_ROOT_PUBLIC_KEY_PATH"),
            expected_manifest_sha256=env("TRUST_ROOT_MANIFEST_SHA256"),
            expected_public_key_sha256=env("TRUST_ROOT_PUBLIC_KEY_SHA256"),
            relying_repository="mytheeramet3dev-x/Constant-Llpoy",
            relying_repository_id=1460417275,
            expected_signer_workflow="mytheeramet3dev-x/Constant-Llpoy/.github/workflows/meta-verification-evidence.yml",
            expected_signer_ref="refs/heads/main",
            expected_signer_commit=env("AUTHORIZED_SIGNER_COMMIT"),
            expected_builder_repository=env("TRUSTED_BUILDER_REPOSITORY"),
            expected_builder_repository_id=int(env("TRUSTED_BUILDER_REPOSITORY_ID")),
            expected_builder_workflow=env("TRUSTED_BUILDER_WORKFLOW"),
            expected_builder_commit=env("TRUSTED_BUILDER_COMMIT"),
        )
        Path(args.output).write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(json.dumps({"status": report["status"], "trust_root_id": report["trust_root_id"],
                          "trust_root_commit": report["trust_root_commit"],
                          "manifest_sha256": report["manifest_sha256"],
                          "builder_integration_status": report["builder_integration_status"]}, sort_keys=True))
        return 0
    except (OSError, ValueError, TrustRootError) as exc:
        print(json.dumps({"status": "REJECTED", "error": str(exc)}, sort_keys=True))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
