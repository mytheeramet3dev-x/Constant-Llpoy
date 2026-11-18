"""Adversarial tests for deterministic component-status aggregation."""
from __future__ import annotations
import base64, copy, hashlib, unittest
from status_aggregator import AggregationError, aggregate

COMMIT = "a" * 40
POLICY_REV = "b" * 40
VERIFIER_REV = "c" * 40

def component(cid="C-1", state="PASS", payload=b"evidence-C1", receipt_status="VERIFIED"):
    digest = hashlib.sha256(payload).hexdigest()
    return {
        "component_id": cid, "status": state,
        "evidence_base64": base64.b64encode(payload).decode("ascii"),
        "evidence_sha256": digest,
        "provenance": {
            "status": receipt_status, "subject_sha256": digest, "source_commit": COMMIT,
            "verifier_run_id": 123, "verifier_run_attempt": 1, "verifier_revision": VERIFIER_REV,
        },
    }

def fixture():
    policy = {"schema_version":"1.0","claim_id":"CLAIM-A","policy_revision":POLICY_REV,
              "required_components":["C-1","C-2"]}
    bundle = {"schema_version":"1.0","claim_id":"CLAIM-A","source_commit":COMMIT,
              "policy_revision":POLICY_REV,
              "components":[component("C-1"),component("C-2",payload=b"evidence-C2")]}
    return policy,bundle

class AggregatorTests(unittest.TestCase):
    def test_complete_current_bundle_accepted_structurally(self):
        p,b=fixture(); r=aggregate(p,b,COMMIT)
        self.assertEqual(r["status"],"ACCEPTED")
        self.assertEqual(r["assurance_level"],"STRUCTURAL_ONLY_UNAUTHENTICATED_INPUTS")
    def test_verified_failure_is_rejected(self):
        p,b=fixture(); b["components"][0]["status"]="FAIL"
        self.assertEqual(aggregate(p,b,COMMIT)["status"],"REJECTED")
    def test_unverified_failure_is_inconclusive_not_authoritative_rejection(self):
        p,b=fixture(); b["components"][0]["status"]="FAIL"; b["components"][0]["provenance"]["status"]="UNVERIFIED"
        self.assertEqual(aggregate(p,b,COMMIT)["status"],"INCONCLUSIVE")
    def test_missing_component_is_inconclusive(self):
        p,b=fixture(); b["components"].pop()
        self.assertEqual(aggregate(p,b,COMMIT)["status"],"INCONCLUSIVE")
    def test_duplicate_component_is_inconclusive(self):
        p,b=fixture(); b["components"].append(copy.deepcopy(b["components"][0]))
        self.assertEqual(aggregate(p,b,COMMIT)["status"],"INCONCLUSIVE")
    def test_conflicting_duplicate_cannot_override_original(self):
        p,b=fixture(); duplicate=copy.deepcopy(b["components"][0]); duplicate["status"]="FAIL"
        b["components"].append(duplicate)
        self.assertEqual(aggregate(p,b,COMMIT)["status"],"INCONCLUSIVE")
    def test_unknown_component_is_inconclusive(self):
        p,b=fixture(); b["components"].append(component("C-X"))
        self.assertEqual(aggregate(p,b,COMMIT)["status"],"INCONCLUSIVE")
    def test_stale_commit_is_inconclusive(self):
        p,b=fixture(); b["source_commit"]="d"*40
        self.assertEqual(aggregate(p,b,COMMIT)["status"],"INCONCLUSIVE")
    def test_stale_policy_revision_is_inconclusive(self):
        p,b=fixture(); b["policy_revision"]="d"*40
        self.assertEqual(aggregate(p,b,COMMIT)["status"],"INCONCLUSIVE")
    def test_claim_mismatch_is_inconclusive(self):
        p,b=fixture(); b["claim_id"]="OTHER"
        self.assertEqual(aggregate(p,b,COMMIT)["status"],"INCONCLUSIVE")
    def test_receipt_subject_mismatch_is_inconclusive(self):
        p,b=fixture(); b["components"][0]["provenance"]["subject_sha256"]="0"*64
        self.assertEqual(aggregate(p,b,COMMIT)["status"],"INCONCLUSIVE")
    def test_receipt_commit_mismatch_is_inconclusive(self):
        p,b=fixture(); b["components"][0]["provenance"]["source_commit"]="d"*40
        self.assertEqual(aggregate(p,b,COMMIT)["status"],"INCONCLUSIVE")
    def test_unverified_receipt_is_inconclusive(self):
        p,b=fixture(); b["components"][0]["provenance"]["status"]="UNVERIFIED"
        self.assertEqual(aggregate(p,b,COMMIT)["status"],"INCONCLUSIVE")
    def test_failed_receipt_is_inconclusive(self):
        p,b=fixture(); b["components"][0]["provenance"]["status"]="FAILED"
        self.assertEqual(aggregate(p,b,COMMIT)["status"],"INCONCLUSIVE")
    def test_not_run_timeout_error_and_inconclusive_never_accept(self):
        for state in ("NOT_RUN","TIMEOUT","ERROR","INCONCLUSIVE"):
            with self.subTest(state=state):
                p,b=fixture(); b["components"][0]["status"]=state
                self.assertEqual(aggregate(p,b,COMMIT)["status"],"INCONCLUSIVE")
    def test_evidence_digest_mismatch_rejected(self):
        p,b=fixture(); b["components"][0]["evidence_base64"]=base64.b64encode(b"changed").decode()
        self.assertEqual(aggregate(p,b,COMMIT)["status"],"REJECTED")
    def test_empty_evidence_rejected_as_malformed(self):
        p,b=fixture(); c=b["components"][0]; c["evidence_base64"]=""; c["evidence_sha256"]=hashlib.sha256(b"").hexdigest()
        with self.assertRaises(AggregationError): aggregate(p,b,COMMIT)
    def test_boolean_run_id_rejected(self):
        p,b=fixture(); b["components"][0]["provenance"]["verifier_run_id"]=True
        with self.assertRaises(AggregationError): aggregate(p,b,COMMIT)
    def test_boolean_attempt_rejected(self):
        p,b=fixture(); b["components"][0]["provenance"]["verifier_run_attempt"]=True
        with self.assertRaises(AggregationError): aggregate(p,b,COMMIT)
    def test_duplicate_policy_components_rejected(self):
        p,b=fixture(); p["required_components"].append("C-1")
        with self.assertRaises(AggregationError): aggregate(p,b,COMMIT)
    def test_unknown_bundle_field_rejected(self):
        p,b=fixture(); b["reported_status"]="ACCEPTED"
        with self.assertRaises(AggregationError): aggregate(p,b,COMMIT)
    def test_unknown_component_field_rejected(self):
        p,b=fixture(); b["components"][0]["is_verified"]=True
        with self.assertRaises(AggregationError): aggregate(p,b,COMMIT)
    def test_unknown_provenance_field_rejected(self):
        p,b=fixture(); b["components"][0]["provenance"]["trusted"]=True
        with self.assertRaises(AggregationError): aggregate(p,b,COMMIT)
    def test_invalid_commit_argument_rejected(self):
        p,b=fixture()
        with self.assertRaises(AggregationError): aggregate(p,b,"main")
    def test_invalid_provenance_run_identity_rejected(self):
        for field,value in (("verifier_run_id",0),("verifier_run_attempt",-1)):
            p,b=fixture(); b["components"][0]["provenance"][field]=value
            with self.subTest(field=field), self.assertRaises(AggregationError): aggregate(p,b,COMMIT)

if __name__ == "__main__":
    unittest.main(verbosity=2)
