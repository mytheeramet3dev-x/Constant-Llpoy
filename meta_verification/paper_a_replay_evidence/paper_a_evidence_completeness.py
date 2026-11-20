"""Independent completeness check against a separately maintained policy."""
from __future__ import annotations
from pathlib import PurePosixPath

REQUIRED_POLICY_KEYS={"policy_id","version","required_inputs","required_artifacts","required_check_ids"}

def _validate_policy(policy):
    if not isinstance(policy,dict) or set(policy)!=REQUIRED_POLICY_KEYS:
        raise ValueError("policy must contain exactly the required keys")
    for field in ("policy_id","version"):
        if not isinstance(policy[field],str) or not policy[field].strip():
            raise ValueError(f"{field} must be non-empty")
    for field in ("required_inputs","required_artifacts","required_check_ids"):
        values=policy[field]
        if not isinstance(values,list) or any(not isinstance(x,str) or not x.strip() for x in values):
            raise ValueError(f"{field} must be a list of non-empty strings")
        if len(values)!=len(set(values)):
            raise ValueError(f"{field} contains duplicate entries")
    for field in ("required_inputs","required_artifacts"):
        for path in policy[field]:
            parts=path.split("/")
            p=PurePosixPath(path)
            if p.is_absolute() or chr(92) in path or any(x in ("",".","..") for x in parts):
                raise ValueError(f"policy path must be canonical relative POSIX: {path}")
    if not policy["required_inputs"]:
        raise ValueError("required_inputs must not be empty")
    if not policy["required_artifacts"]:
        raise ValueError("required_artifacts must not be empty")
    return True

def evaluate_completeness(manifest,policy):
    _validate_policy(policy)
    inputs={r["path"] for r in manifest.get("inputs",[]) if isinstance(r,dict) and "path" in r}
    artifacts={r["path"] for r in manifest.get("artifacts",[]) if isinstance(r,dict) and "path" in r}
    checks={r["check_id"] for r in manifest.get("checks",[]) if isinstance(r,dict) and "check_id" in r}
    missing_inputs=sorted(set(policy["required_inputs"])-inputs)
    missing_artifacts=sorted(set(policy["required_artifacts"])-artifacts)
    missing_checks=sorted(set(policy["required_check_ids"])-checks)
    missing=missing_inputs or missing_artifacts or missing_checks
    return {"completeness_status":"PASS" if not missing else "FAIL",
      "policy_id":policy["policy_id"],"policy_version":policy["version"],
      "missing_required_inputs":missing_inputs,"missing_required_artifacts":missing_artifacts,
      "missing_required_check_ids":missing_checks,
      "limitations":["Completeness depends on an independently maintained policy inventory.",
      "Check ID presence does not prove execution or PASS status.",
      "Policy authenticity, approval, and version custody are not verified."]}
