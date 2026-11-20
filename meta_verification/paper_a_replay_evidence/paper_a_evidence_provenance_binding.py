"""Independent binding of evidence identity, evaluator identity and context.
This validator checks declarations and consistency, not the truth or authenticity of them.
"""
from __future__ import annotations
import re
from typing import Any, Mapping

HEX64 = re.compile(r"^[0-9a-f]{64}$")
REQUIRED = {
    "evaluation_id", "evidence_bundle_sha256", "policy_sha256",
    "verifier_id", "verifier_version", "environment_id", "result_record_sha256",
}

class ProvenanceBindingError(ValueError):
    pass

def validate_provenance_binding(record: Mapping[str, Any]) -> dict[str, Any]:
    if not isinstance(record, Mapping):
        raise ProvenanceBindingError("record must be a mapping")
    missing = REQUIRED - set(record)
    if missing:
        raise ProvenanceBindingError(f"missing fields: {sorted(missing)}")
    for key in ("evaluation_id", "verifier_id", "verifier_version", "environment_id"):
        value = record[key]
        if not isinstance(value, str) or not value.strip():
            raise ProvenanceBindingError(f"{key} must be non-empty")
    for key in ("evidence_bundle_sha256", "policy_sha256", "result_record_sha256"):
        if not isinstance(record[key], str) or not HEX64.fullmatch(record[key]):
            raise ProvenanceBindingError(f"{key} must be lowercase SHA-256 hex")
    if "status" in record and record["status"] == "PASS" and record.get("certification") == "CERTIFIED":
        raise ProvenanceBindingError("provenance PASS cannot claim overall certification")
    return dict(record)

def compare_provenance_bindings(left: Mapping[str, Any], right: Mapping[str, Any]) -> dict[str, Any]:
    a = validate_provenance_binding(left)
    b = validate_provenance_binding(right)
    fields = sorted(REQUIRED)
    differences = {field: (a[field], b[field]) for field in fields if a[field] != b[field]}
    return {"identical": not differences, "differences": differences}
