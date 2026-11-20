"""Trust-gated evidence completeness pipeline."""
from __future__ import annotations
from paper_a_policy_trust import verify_policy_pin
from paper_a_evidence_completeness import evaluate_completeness

def evaluate_trust_gated_completeness(manifest, policy, verifier_pin):
    trust = verify_policy_pin(policy, verifier_pin)
    if trust.get("status") != "PASS":
        return {"pipeline_status":"FAIL_CLOSED","policy_trust_status":"FAIL",
                "completeness_status":"NOT_EVALUATED","reason":trust.get("reason"),
                "certification":"NOT_PERFORMED"}
    completeness = evaluate_completeness(manifest, policy)
    return {"pipeline_status":"PASS" if completeness["completeness_status"]=="PASS" else "FAIL",
            "policy_trust_status":"PASS","policy_trust_scope":trust["scope"],
            "completeness_status":completeness["completeness_status"],
            "policy_id":completeness["policy_id"],"policy_version":completeness["policy_version"],
            "missing_required_inputs":completeness["missing_required_inputs"],
            "missing_required_artifacts":completeness["missing_required_artifacts"],
            "missing_required_check_ids":completeness["missing_required_check_ids"],
            "certification":"NOT_PERFORMED",
            "limitations":trust["limitations"]+completeness["limitations"]}
