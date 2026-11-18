#!/usr/bin/env python3
"""Structural integrity checker for the Paper A claim-to-Lean audit.
Success authenticates references/counts only; it never infers mathematical equivalence.
"""
from __future__ import annotations
import argparse, hashlib, json, re
from collections import Counter
from pathlib import Path
EXPECTED_IDS=(["AS-ALPHA-A-DEF-0001"]+[f"AS-ALPHA-A-PROP-{i:04d}" for i in range(1,13)]+[f"AS-ALPHA-A-THM-{i:04d}" for i in range(1,3)])
ALLOWED_STATUSES={"PARTIAL_SUPPORT_ONLY","NO_DIRECT_FORMALIZATION","SOURCE_CONFLICT_WITH_CONDITIONAL_LEMMAS_ONLY","ABSTRACT_MATRIX_CORE_ONLY"}
DECL_RE=re.compile(r"(?m)^\s*(?:@\[[^\]]+\]\s*)*(?:private\s+)?(?:noncomputable\s+)?(?:theorem|lemma|def|abbrev|opaque)\s+([A-Za-z_][A-Za-z0-9_'.]*)")
class AuditError(ValueError): pass
def strict_json(raw):
    def pairs(items):
        out={}
        for k,v in items:
            if k in out: raise AuditError(f"duplicate JSON key: {k}")
            out[k]=v
        return out
    def bad(v): raise AuditError(f"non-standard JSON constant: {v}")
    try: value=json.loads(raw.decode("utf-8"),object_pairs_hook=pairs,parse_constant=bad)
    except (UnicodeDecodeError,json.JSONDecodeError) as e: raise AuditError(f"invalid UTF-8/JSON: {e}") from e
    if not isinstance(value,dict): raise AuditError("top-level JSON value must be an object")
    return value
def git_blob_sha(raw): return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
def require(ok,msg):
    if not ok: raise AuditError(msg)
def validate(audit,root):
    require(audit.get("schema_version")=="1.0","unsupported schema_version")
    require(audit.get("audit_id")=="PAPER_A_LEAN_SEMANTIC_CORRESPONDENCE_AUDIT","wrong audit_id")
    summary=audit.get("summary",{})
    require(summary.get("layer_l02")=="BLOCKED","L-02 must remain BLOCKED until independent semantic review")
    require(summary.get("claim_verification_promoted") is False,"audit must not promote claim verification")
    claims=audit.get("claims")
    require(isinstance(claims,list),"claims must be a list")
    ids=[c.get("claim_id") for c in claims if isinstance(c,dict)]
    require(len(ids)==len(claims),"each claim entry must be an object")
    require(len(ids)==len(set(ids)),"duplicate claim IDs")
    require(sorted(ids)==sorted(EXPECTED_IDS),"claim registry set is incomplete or unexpected")
    modules=audit.get("lean_modules")
    require(isinstance(modules,list) and len(modules)==5,"expected exactly five audited Lean modules")
    module_text={}
    for m in modules:
        path=m.get("path","")
        require(path.startswith("formalization/lean/ConstantLlapoy/PaperA/"),f"unexpected Lean module path: {path}")
        f=root/path
        require(f.is_file() and not f.is_symlink(),f"module missing or symlink: {path}")
        raw=f.read_bytes()
        require(git_blob_sha(raw)==m.get("blob_sha"),f"Lean module blob mismatch: {path}")
        module_text[path]=raw.decode("utf-8")
    declared=set()
    for source in module_text.values(): declared.update(DECL_RE.findall(source))
    statuses=Counter(); declaration_refs=0
    for c in claims:
        cid=c["claim_id"]
        require(set(c)=={"claim_id","source","claim_blob","lean_status","lean_declarations","gap"},f"{cid}: unexpected/missing fields")
        status=c["lean_status"]; require(status in ALLOWED_STATUSES,f"{cid}: unsupported status {status!r}"); statuses[status]+=1
        require(isinstance(c["source"],str) and c["source"].strip(),f"{cid}: missing source locator")
        require(isinstance(c["gap"],str) and c["gap"].strip(),f"{cid}: missing explicit gap")
        require(re.fullmatch(r"[0-9a-f]{40}",c["claim_blob"] or "") is not None,f"{cid}: invalid source blob SHA")
        f=root/"claims"/"A"/f"{cid}.md"
        require(f.is_file() and not f.is_symlink(),f"{cid}: source claim file missing or symlink")
        require(git_blob_sha(f.read_bytes())==c["claim_blob"],f"{cid}: frozen claim blob mismatch")
        decls=c["lean_declarations"]
        require(isinstance(decls,list) and all(isinstance(x,str) and x for x in decls),f"{cid}: invalid declaration list")
        if status=="NO_DIRECT_FORMALIZATION": require(not decls,f"{cid}: no-direct status cannot list declarations")
        for name in decls:
            declaration_refs+=1; require(name in declared,f"{cid}: Lean declaration not found: {name}")
    expected={"total_claims":len(claims),"directly_fully_corresponding":0,
      "partial_support_or_abstract_core":statuses["PARTIAL_SUPPORT_ONLY"]+statuses["ABSTRACT_MATRIX_CORE_ONLY"],
      "no_direct_formalization":statuses["NO_DIRECT_FORMALIZATION"],
      "source_conflict_with_conditional_lemmas_only":statuses["SOURCE_CONFLICT_WITH_CONDITIONAL_LEMMAS_ONLY"]}
    for k,v in expected.items(): require(summary.get(k)==v,f"summary count mismatch: {k}")
    return {"status":"STRUCTURALLY_VALID_NOT_SEMANTICALLY_VERIFIED","claims_checked":len(claims),
      "source_blob_bindings":len(claims),"lean_modules_checked":len(modules),
      "declaration_references_checked":declaration_refs,"status_counts":dict(sorted(statuses.items())),
      "layer_l02":"BLOCKED","claim_verification_promoted":False}
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("--audit",default="meta_verification/paper_a_semantic_correspondence.json"); p.add_argument("--root",default="."); a=p.parse_args(argv)
    try:
        root=Path(a.root).resolve(); result=validate(strict_json((root/a.audit).read_bytes()),root)
        print(json.dumps(result,sort_keys=True)); return 0
    except (OSError,AuditError) as e:
        print(json.dumps({"status":"REJECTED","error":str(e)},sort_keys=True)); return 2
if __name__=="__main__": raise SystemExit(main())
