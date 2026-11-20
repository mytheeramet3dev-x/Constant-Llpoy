#!/usr/bin/env python3
"""Race-reduced Paper A evidence intake using descriptor-relative, no-follow opens.

Only workspace-relative paths are accepted. Each path component is opened relative
to a pinned directory descriptor with O_NOFOLLOW. This is stronger than path
preflight, but platform support and filesystem semantics still matter.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import stat
from pathlib import Path
from paper_a_replay_manifest_validate import validate_manifest

def _open_workspace(workspace_root: str) -> tuple[int, str]:
    raw = Path(workspace_root)
    if raw.is_symlink():
        raise ValueError("workspace root symlink rejected")
    resolved = raw.resolve(strict=True)
    flags = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0) | getattr(os, "O_NOFOLLOW", 0)
    fd = os.open(str(resolved), flags)
    if not stat.S_ISDIR(os.fstat(fd).st_mode):
        os.close(fd)
        raise ValueError("workspace root must be a directory")
    return fd, str(resolved)

def _open_relative_file(root_fd: int, raw_path: str) -> int:
    if not isinstance(raw_path, str) or not raw_path.strip():
        raise ValueError("file path must be a non-empty string")
    rel = Path(raw_path)
    if rel.is_absolute() or any(part in ("", ".", "..") for part in rel.parts):
        raise ValueError("path must be clean and workspace-relative (no absolute path or traversal)")
    parts = rel.parts
    current_fd = os.dup(root_fd)
    try:
        for component in parts[:-1]:
            flags = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0) | getattr(os, "O_NOFOLLOW", 0)
            next_fd = os.open(component, flags, dir_fd=current_fd)
            os.close(current_fd)
            current_fd = next_fd
        flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0)
        fd = os.open(parts[-1], flags, dir_fd=current_fd)
        if not stat.S_ISREG(os.fstat(fd).st_mode):
            os.close(fd)
            raise ValueError("target is not a regular file")
        return fd
    finally:
        os.close(current_fd)

def _sha256_fd(fd: int) -> str:
    digest = hashlib.sha256()
    os.lseek(fd, 0, os.SEEK_SET)
    while True:
        chunk = os.read(fd, 1024 * 1024)
        if not chunk:
            break
        digest.update(chunk)
    return digest.hexdigest()

def _read_json_fd(fd: int) -> dict:
    os.lseek(fd, 0, os.SEEK_SET)
    chunks = []
    while True:
        part = os.read(fd, 1024 * 1024)
        if not part:
            break
        chunks.append(part)
    data = json.loads(b"".join(chunks).decode("utf-8"))
    if not isinstance(data, dict):
        raise ValueError("manifest must be a JSON object")
    return data

def intake(manifest_path: str, workspace_root: str) -> dict:
    root_fd, canonical_root = _open_workspace(workspace_root)
    try:
        manifest_fd = _open_relative_file(root_fd, manifest_path)
        try:
            manifest = _read_json_fd(manifest_fd)
        finally:
            os.close(manifest_fd)
        validate_manifest(manifest, verify_files=False)
        checked, errors = [], []
        for section in ("inputs", "artifacts"):
            for record in manifest[section]:
                path = record["path"]
                try:
                    fd = _open_relative_file(root_fd, path)
                    try:
                        actual = _sha256_fd(fd)
                    finally:
                        os.close(fd)
                    if actual != record["sha256"]:
                        raise ValueError("SHA-256 mismatch")
                    checked.append({"section": section, "path": path, "sha256": actual,
                                   "exact_values_present": "exact_values" in record})
                except (OSError, ValueError) as exc:
                    errors.append({"section": section, "path": path, "error": str(exc)})
        return {
            "intake_status": "PASS" if not errors else "FAIL",
            "workspace_root": canonical_root,
            "producer_claimed_checks": manifest["checks"],
            "independent_file_checks": checked,
            "errors": errors,
            "certification": "NOT_PERFORMED",
            "limitations": [
                "Descriptor-relative O_NOFOLLOW checks reduce path substitution races, but do not constitute a complete sandbox or filesystem attestation.",
                "Workspace root and its parent chain are trusted inputs; hostile mount or privileged filesystem changes are outside this utility's guarantees.",
                "No detached-signature verification is performed.",
                "No mathematical claim or producer check status is certified.",
                "exact_values are preserved as metadata; their claim-specific meaning is not independently interpreted."
            ]
        }
    finally:
        os.close(root_fd)

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", help="manifest path relative to workspace")
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
