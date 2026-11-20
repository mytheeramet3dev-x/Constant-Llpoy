"""Independent completeness check against a separately maintained policy."""
from __future__ import annotations
from pathlib import PurePosixPath
REQUIRED_POLICY_KEYS={"policy_id","version","required_inputs","required_artifacts","required_check_ids"}
def _validate_policy(policy):
 if not isinstance(policy,dict) or set(policy)!=REQUIRED_POLICY_KEYS: raise ValueError("policy must contain exactly the required keys")
 for field in ("policy_id","version"):
  if not isinstance(policy[field],str) or not policy[field].strip(): raise ValueError(f"{field} must be non-empty")
 for field in ("required_inputs","required_artifacts","required_check_ids"):
  value=policy[field]
  if not isinstance(value,list) or any(not isinstance(x,str) or not x.strip() for x in value): raise ValueError(f"{field} must be a list of non-empty strings")
  if len(value)!=len(set(value)): raise ValueError(f"{field} contains duplicate entries")
 for field in ("required_inputs","required_artifacts"):
  for path in policy[field]:
   p=PurePosixPath(path)
   if p.is_absolute() or "\\\\" in path or any(x in ("",".","..") for x in path.split("/")): raise ValueError(f"policy path must be canonical relative POSIX: {path}")
 return True
def evaluate_completeness(manifest,policy):
 _validate_policy(policy)
 ins={r["path"] for r in manifest.get("inputs",[]) if isinstance(r,dict) and "path" in r}
 outs={r["path"] for r in manifest.get("artifacts",[]) if isinstance(r,dict) and "path" in r}
 checks={r["check_id"] for r in manifest.get("checks",[]) if isinstance(r,dict) and "check_id" in r}
 mi=sorted(set(policy["required_inputs"])-ins); mo=sorted(set(policy["required_artifacts"])-outs); mc=sorted(set(policy["required_check_ids"])-checks)
 return {"completeness_status":"PASS" if not (mi or mo or mc) else "FAIL","policy_id":policy["policy_id"],"policy_version":policy["version"],
 "missing_required_inputs":mi,"missing_required_artifacts":mo,"missing_required_check_ids":mc,
 "limitations":["Completeness depends on an independently maintained policy inventory.","Check ID presence does not prove execution or PASS status.","Policy authenticity, approval, and version custody are not verified."]}
