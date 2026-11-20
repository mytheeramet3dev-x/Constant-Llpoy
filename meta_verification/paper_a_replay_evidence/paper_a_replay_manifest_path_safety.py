"""Path safety primitives for Paper A replay manifest files.

Uses canonical resolution and rejects symlinks by default, with an explicit
workspace-root containment policy. This is a best-effort preflight, not race-free
filesystem attestation; see report for limitations.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path


def resolve_safe_file(raw_path: str, workspace_root: str, reject_symlinks: bool = True) -> Path:
    raw = Path(raw_path)
    root = Path(workspace_root).resolve(strict=True)
    candidate = raw if raw.is_absolute() else root / raw
    # Reject symlinks in every existing component, including a symlinked workspace path.
    if reject_symlinks:
        cursor = candidate
        while True:
            if cursor.is_symlink():
                raise ValueError(f"symlink path component rejected: {cursor}")
            if cursor.parent == cursor:
                break
            cursor = cursor.parent
    resolved = candidate.resolve(strict=True)
    try:
        resolved.relative_to(root)
    except ValueError as exc:
        raise ValueError(f"path escapes workspace root: {raw_path}") from exc
    if not resolved.is_file():
        raise ValueError(f"path is not a regular file: {raw_path}")
    return resolved


def sha256_safe_file(raw_path: str, workspace_root: str, reject_symlinks: bool = True) -> tuple[str, str]:
    resolved = resolve_safe_file(raw_path, workspace_root, reject_symlinks)
    digest = hashlib.sha256()
    with resolved.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return str(resolved), digest.hexdigest()


def verify_record(record: dict, workspace_root: str, reject_symlinks: bool = True) -> bool:
    if not isinstance(record, dict) or set(record) != {"path", "sha256"}:
        raise ValueError("record must contain exactly path and sha256")
    path, actual = sha256_safe_file(record["path"], workspace_root, reject_symlinks)
    expected = record["sha256"]
    if not isinstance(expected, str) or actual != expected:
        raise ValueError(f"SHA-256 mismatch for {path}")
    return True


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="file path relative to workspace root or absolute")
    parser.add_argument("--workspace-root", required=True, help="workspace containment root")
    parser.add_argument("--allow-symlinks", action="store_true", help="allow symlink components (not recommended)")
    args = parser.parse_args(argv)
    try:
        path, digest = sha256_safe_file(args.path, args.workspace_root, not args.allow_symlinks)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    print(json.dumps({"canonical_path": path, "sha256": digest}, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
