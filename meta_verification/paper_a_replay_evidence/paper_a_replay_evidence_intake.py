#!/usr/bin/env python3
"""Race-reduced Paper A evidence intake using descriptor-relative, no-follow opens."""
from __future__ import annotations
import argparse, hashlib, json, os, stat
from pathlib import Path
from paper_a_replay_manifest_validate import validate_manifest

def _open_workspace(workspace_root: str) -> tuple[int, str]:
    raw = Path(workspace_root)
    if raw.is_symlink(): raise ValueError("workspace root symlink rejected")
    resolved = raw.resolve(strict=True)
    flags = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0) | getattr(os, "O_NOFOLLOW", 0)
    fd = os.open(str(resolved), flags)
    if not stat.S_ISDIR(os.fstat(fd).st_mode):
        os.close(fd); raise ValueError("workspace root must be a directory")
    return fd, str(resolved)

def _clean_relative_parts(raw_path: str) -> tuple[str, ...]:
    if not isinstance(raw_path, str) or not raw_path.strip(): raise ValueError("file path must be a non-empty string")
    if "\\" in raw_path or raw_path.startswith("/") or raw_path.endswith("/"):
        raise ValueError("path must be canonical workspace-relative POSIX form")
    parts = raw_path.split("/")
    if any(p in ("", ".", "..") for p in parts):
        raise ValueError("path must be canonical (no empty, dot, or traversal components)")
    return tuple(parts)

def _open_relative_file(root_fd: int, raw_path: str) -> int:
    parts = _clean_relative_parts(raw_path); current_fd = os.dup(root_fd)
    try:
        for component in parts[:-1]:
            flags = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0) | getattr(os, "O_NOFOLLOW", 0)
            next_fd = os.open(component, flags, dir_fd=current_fd); os.close(current_fd); current_fd = next_fd
        fd = os.open(parts[-1], os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0), dir_fd=current_fd)
        if not stat.S_ISREG(os.fstat(fd).st_mode):
            os.close(fd); raise ValueError("target is not a regular file")
        return fd
    finally: os.close(current_fd)

def _fingerprint(fd: int) -> tuple[int, int, int, int, int]:
    st=os.fstat(fd); return (st.st_dev, st.st_ino, st.st_size, st.st_mtime_ns, st.st_ctime_ns)

def _sha256_stable_fd(fd: int) -> str:
    before=_fingerprint(fd); digest=hashlib.sha256(); os.lseek(fd,0,os.SEEK_SET)
    while True:
        chunk=os.read(fd,1024*1024)
        if not chunk: break
        digest.update(chunk)
    if before != _fingerprint(fd): raise ValueError("file metadata changed during hashing; unstable evidence rejected")
    return digest.hexdigest()

def _read_json_fd(fd: int) -> dict:
    before=_fingerprint(fd); os.lseek(fd,0,os.SEEK_SET); chunks=[]
    while True:
        chunk=os.read(fd,1024*1024)
        if not chunk: break
        chunks.append(chunk)
    if before != _fingerprint(fd): raise ValueError("manifest metadata changed during read")
    data=json.loads(b"".join(chunks).decode("utf-8"))
    if not isinstance(data,dict): raise ValueError("manifest must be a JSON object")
    return data

def intake(manifest_path: str, workspace_root: str) -> dict:
    root_fd, root_name=_open_workspace(workspace_root)
    try:
        mf_fd=_open_relative_file(root_fd,manifest_path)
        try: manifest=_read_json_fd(mf_fd)
        finally: os.close(mf_fd)
        validate_manifest(manifest,verify_files=False)
        if not manifest["inputs"] or not manifest["artifacts"]:
            raise ValueError("incomplete evidence bundle: inputs and artifacts must both be non-empty")
        paths=set()
        for section in ("inputs","artifacts"):
            for record in manifest[section]:
                canonical="/".join(_clean_relative_parts(record["path"]))
                if canonical in paths: raise ValueError(f"duplicate evidence path across bundle: {canonical}")
                paths.add(canonical)
        checked,errors=[],[]
        for section in ("inputs","artifacts"):
            for record in manifest[section]:
                path=record["path"]
                try:
                    fd=_open_relative_file(root_fd,path)
                    try: actual=_sha256_stable_fd(fd)
                    finally: os.close(fd)
                    if actual != record["sha256"]: raise ValueError("SHA-256 mismatch")
                    checked.append({"section":section,"path":path,"sha256":actual,"exact_values_present":"exact_values" in record})
                except (OSError,ValueError) as exc: errors.append({"section":section,"path":path,"error":str(exc)})
        return {"intake_status":"PASS" if not errors else "FAIL","workspace_root":root_name,
          "producer_claimed_checks":manifest["checks"],"independent_file_checks":checked,"errors":errors,
          "certification":"NOT_PERFORMED","limitations":[
          "Producer check statuses are untrusted assertions; intake does not evaluate them.",
          "Stable fstat metadata checks reduce, but cannot eliminate, in-place mutation races during hashing.",
          "Descriptor-relative O_NOFOLLOW checks reduce path substitution races but are not a complete sandbox or filesystem attestation.",
          "Workspace root and parent chain are trusted inputs; hostile mount or privileged filesystem changes are outside guarantees.",
          "No detached-signature verification is performed.","No mathematical claim or producer check status is certified.",
          "exact_values are preserved as metadata; their claim-specific meaning is not independently interpreted."]}
    finally: os.close(root_fd)

def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest",help="manifest path relative to workspace")
    parser.add_argument("--workspace-root",required=True,help="trusted evidence workspace")
    args=parser.parse_args(argv)
    try: result=intake(args.manifest,args.workspace_root)
    except (OSError,json.JSONDecodeError,ValueError) as exc: parser.error(str(exc))
    print(json.dumps(result,indent=2,sort_keys=True))
    return 0 if result["intake_status"]=="PASS" else 1
if __name__=="__main__": raise SystemExit(main())
