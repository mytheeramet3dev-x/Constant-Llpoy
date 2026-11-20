#!/usr/bin/env python3
"""Secure intake preflight for Paper A replay evidence bundles.

This is an intake verifier, not a mathematical certification engine.
It validates manifest structure and workspace-contained input/artifact hashes.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from paper_a_replay_manifest_validate import validate_manifest
from paper_a_replay_manifest_path_safety import sha256_safe_file

def intake(manifest_path: str, workspace_root: str) -> dict:
    root = Path(workspace_root).resolve(strict=True)
    manifest_file = Path(manifest_path)
    if not manifest_file.is_absolute():
        manifest_file = root / manifest_file
    manifest_file = manifest_file.resolve(strict=True)
    try:
        manifest_file.relative_to(root)
    except ValueError as exc:
        raise ValueError("manifest path escapes workspace root") from exc
    if not manifest_file.is_file():
        raise ValueError("manifest must be a regular file")
    manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
    validate_manifest(manifest, verify_files=False)
    checked = []
    errors = []
    for section in ("inputs", "artifacts"):
        for record in manifest[section]:
            path = record["path"]
            try:
                canonical, actual = sha256_safe_file(path, str(root), reject_symlinks=True)
                if actual != record["sha256"]:
                    raise ValueError("SHA-256 mismatch")
                # exact_values remain part of the validated manifest metadata.
                checked.append({"section": section, "path": path,
                    "canonical_path": canonical, "sha256": actual,
                    "exact_values_present": "exact_values" in record})
            except (OSError, ValueError) as exc:
                errors.append({"section": section, "path": path, "error": str(exc)})
    return {
        "intake_status": "PASS" if not errors else "FAIL",
        "producer_claimed_checks": manifest["checks"],
        "independent_file_checks": checked,
        "errors": errors,
        "certification": "NOT_PERFORMED",
        "limitations": [
            "Preflight path checks are not race-free against concurrent filesystem mutation (TOCTOU).",
            "No detached-signature verification is performed.",
            "No mathematical claim or producer check status is certified.",
            "exact_values are preserved as metadata; their claim-specific meaning is not independently interpreted."
        ]
    }

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", help="manifest file within workspace")
    parser.add_argument("--workspace-root", required=True, help="trusted evidence workspace")
    args = parser.parse_args(argv)
    try:
        result = intake(args.manifest, args.workspace_root)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        parser.error(str(exc))
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["intake_status"] == "PASS" else 1

if __name__ == "__main__":
    raise SystemExit(main())
