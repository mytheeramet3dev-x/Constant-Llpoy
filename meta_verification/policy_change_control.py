#!/usr/bin/env python3
"""Verify threshold-approved policy changes against an externally pinned authority set."""
from __future__ import annotations
import argparse, base64, hashlib, json, re, subprocess, tempfile
from pathlib import Path
from typing import Any
SHA256=re.compile(r"^[0-9a-f]{64}$")
AUTHORITY_KEYS={"schema_version","authority_set_id","threshold","reviewers"}
PROPOSAL_KEYS={"schema_version","policy_id","sequence","parent_policy_sha256","policy_sha256","issued_at","expires_at","signatures"}
SIGNATURE_KEYS={"reviewer_id","signature_base64"}
class PolicyChangeError(ValueError): pass
def require(ok,message):
    if not ok: raise PolicyChangeError(message)
def unique_object(pairs):
    result={}
    for k,v in pairs:
        require(k not in result,f"duplicate JSON key: {k}")
        result[k]=v
    return result
def strict_json_bytes(raw,label):
    try:
        return json.loads(raw.decode("utf-8"),object_pairs_hook=unique_object,
            parse_constant=lambda v: (_ for _ in ()).throw(PolicyChangeError(f"{label}: non-standard JSON constant {v}")))
    except (UnicodeDecodeError,json.JSONDecodeError) as exc:
        raise PolicyChangeError(f"{label}: invalid UTF-8 JSON: {exc}") from None
def canonical_json(value):
    return json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False).encode()
def sha256(raw): return hashlib.sha256(raw).hexdigest()
def exact(value,keys,label):
    require(isinstance(value,dict) and set(value)==keys,f"{label} has missing or unknown fields")
    return value
def positive_int(value,label):
    require(type(value) is int and value>0,f"{label} must be a positive integer")
    return value
def digest(value,label):
    require(isinstance(value,str) and SHA256.fullmatch(value) is not None,f"{label} must be lowercase SHA-256")
    return value
def validate_authorities(authorities):
    a=exact(authorities,AUTHORITY_KEYS,"authority set")
    require(a["schema_version"]=="1.0","unsupported authority-set schema")
    require(isinstance(a["authority_set_id"],str) and a["authority_set_id"].strip(),"authority_set_id must be non-empty")
    threshold=positive_int(a["threshold"],"threshold")
    reviewers=a["reviewers"]
    require(isinstance(reviewers,list) and bool(reviewers),"reviewers must be non-empty")
    ids=set()
    for i,item in enumerate(reviewers):
        exact(item,{"reviewer_id","public_key_pem_base64"},f"reviewers[{i}]")
        rid=item["reviewer_id"]
        require(isinstance(rid,str) and rid.strip() and rid not in ids,"reviewer ID empty or duplicated")
        ids.add(rid)
        try: pem=base64.b64decode(item["public_key_pem_base64"],validate=True)
        except (ValueError,TypeError): raise PolicyChangeError(f"reviewer {rid}: invalid key encoding") from None
        with tempfile.NamedTemporaryFile() as f:
            f.write(pem); f.flush()
            result=subprocess.run(["openssl","pkey","-pubin","-in",f.name,"-text","-noout"],capture_output=True,text=True,timeout=15)
        require(result.returncode==0 and "ED25519 Public-Key:" in result.stdout,f"reviewer {rid}: key must be Ed25519")
    require(threshold<=len(ids),"threshold exceeds reviewer count")
    return a
def verify_sig(pem,signature,message):
    with tempfile.TemporaryDirectory() as td:
        root=Path(td); key=root/"key.pem"; sig=root/"sig"; msg=root/"message"
        key.write_bytes(pem); sig.write_bytes(signature); msg.write_bytes(message)
        result=subprocess.run(["openssl","pkeyutl","-verify","-pubin","-inkey",str(key),"-rawin","-in",str(msg),"-sigfile",str(sig)],capture_output=True,timeout=15)
        return result.returncode==0
def verify_policy_change(policy_bytes,proposal,authority_bytes,*,expected_authority_sha256,expected_policy_id,expected_parent_policy_sha256,expected_sequence,now_epoch):
    digest(expected_authority_sha256,"expected authority pin")
    digest(expected_parent_policy_sha256,"expected parent digest")
    positive_int(expected_sequence,"expected sequence")
    require(sha256(authority_bytes)==expected_authority_sha256,"authority-set digest mismatch against external pin")
    authorities=validate_authorities(strict_json_bytes(authority_bytes,"authority set"))
    p=exact(proposal,PROPOSAL_KEYS,"proposal")
    require(p["schema_version"]=="1.0","unsupported proposal schema")
    require(p["policy_id"]==expected_policy_id,"policy ID mismatch")
    require(positive_int(p["sequence"],"sequence")==expected_sequence,"not the expected next policy sequence")
    require(digest(p["parent_policy_sha256"],"parent digest")==expected_parent_policy_sha256,"parent policy digest mismatch")
    actual=sha256(policy_bytes)
    require(digest(p["policy_sha256"],"policy digest")==actual,"policy content digest mismatch")
    require(isinstance(p["issued_at"],str) and p["issued_at"].isdigit() and isinstance(p["expires_at"],str) and p["expires_at"].isdigit(),"validity times must be integer epoch strings")
    issued,expires=int(p["issued_at"]),int(p["expires_at"])
    require(issued<expires and issued<=now_epoch<expires,"proposal outside validity interval")
    keys={x["reviewer_id"]:base64.b64decode(x["public_key_pem_base64"],validate=True) for x in authorities["reviewers"]}
    require(isinstance(p["signatures"],list),"signatures must be a list")
    message=canonical_json({k:p[k] for k in PROPOSAL_KEYS if k!="signatures"})
    accepted=set()
    for i,raw in enumerate(p["signatures"]):
        sig=exact(raw,SIGNATURE_KEYS,f"signatures[{i}]"); rid=sig["reviewer_id"]
        require(isinstance(rid,str) and rid.strip() and rid not in accepted,"empty or duplicate reviewer signature")
        require(rid in keys,f"unauthorized reviewer: {rid}")
        try: raw_sig=base64.b64decode(sig["signature_base64"],validate=True)
        except (ValueError,TypeError): raise PolicyChangeError(f"reviewer {rid}: invalid signature encoding") from None
        require(bool(raw_sig) and verify_sig(keys[rid],raw_sig,message),f"reviewer {rid}: invalid signature")
        accepted.add(rid)
    require(len(accepted)>=authorities["threshold"],"insufficient independent reviewer signatures")
    return {"status":"POLICY_CHANGE_AUTHORIZED","authority_set_id":authorities["authority_set_id"],
        "authority_set_sha256":expected_authority_sha256,"policy_id":expected_policy_id,
        "policy_sha256":actual,"parent_policy_sha256":expected_parent_policy_sha256,
        "sequence":expected_sequence,"valid_reviewer_ids":sorted(accepted),"threshold":authorities["threshold"],
        "assurance_scope":"THRESHOLD_SIGNATURES_VALID_AGAINST_EXTERNALLY_PINNED_AUTHORITY_SET",
        "activation_status":"NOT_ACTIVATED_UNTIL_EXTERNAL_POLICY_PIN_AND_PROTECTED_CONTROLS_ARE_UPDATED"}
def main(argv=None):
    ap=argparse.ArgumentParser(description=__doc__)
    for flag in ("policy","proposal","authority-set","authority-sha256","policy-id","parent-policy-sha256","sequence","now-epoch"):
        ap.add_argument("--"+flag,required=True)
    a=ap.parse_args(argv)
    try:
        read=lambda x:Path(x).read_bytes()
        result=verify_policy_change(read(a.policy),strict_json_bytes(read(a.proposal),"proposal"),read(a.authority_set),
            expected_authority_sha256=a.authority_sha256,expected_policy_id=a.policy_id,
            expected_parent_policy_sha256=a.parent_policy_sha256,expected_sequence=int(a.sequence),now_epoch=int(a.now_epoch))
    except (OSError,PolicyChangeError,subprocess.TimeoutExpired) as exc:
        print(json.dumps({"status":"ERROR","error":str(exc)},sort_keys=True)); return 2
    print(json.dumps(result,sort_keys=True)); return 0
if __name__=="__main__": raise SystemExit(main())
