import unittest
from paper_a_policy_trust import policy_sha256
from paper_a_trust_gated_completeness import evaluate_trust_gated_completeness

POLICY={"policy_id":"fixture","version":"v1","required_inputs":["in.dat"],
         "required_artifacts":["out.dat"],"required_check_ids":["check"]}
PIN={"policy_id":"fixture","version":"v1","sha256":policy_sha256(POLICY),
     "approval_status":"approved","approval_reference":"unit-test-only"}
MANIFEST={"inputs":[{"path":"in.dat"}],"artifacts":[{"path":"out.dat"}],
          "checks":[{"check_id":"check","status":"FAIL"}]}

class TrustGatePipelineTests(unittest.TestCase):
    def test_trusted_complete_inventory_passes_pipeline_not_certification(self):
        out=evaluate_trust_gated_completeness(MANIFEST,POLICY,PIN)
        self.assertEqual(out["pipeline_status"],"PASS")
        self.assertEqual(out["policy_trust_status"],"PASS")
        self.assertEqual(out["certification"],"NOT_PERFORMED")
    def test_untrusted_policy_fail_closes_before_completeness(self):
        changed={**POLICY,"required_artifacts":["other"]}
        out=evaluate_trust_gated_completeness(MANIFEST,changed,PIN)
        self.assertEqual(out["pipeline_status"],"FAIL_CLOSED")
        self.assertEqual(out["completeness_status"],"NOT_EVALUATED")
    def test_missing_evidence_fails_after_trust(self):
        manifest={**MANIFEST,"artifacts":[]}
        out=evaluate_trust_gated_completeness(manifest,POLICY,PIN)
        self.assertEqual(out["policy_trust_status"],"PASS")
        self.assertEqual(out["completeness_status"],"FAIL")
        self.assertEqual(out["pipeline_status"],"FAIL")
    def test_bad_pin_fail_closed(self):
        pin={**PIN,"approval_status":"pending"}
        out=evaluate_trust_gated_completeness(MANIFEST,POLICY,pin)
        self.assertEqual(out["pipeline_status"],"FAIL_CLOSED")
        self.assertEqual(out["completeness_status"],"NOT_EVALUATED")
    def test_present_failed_check_does_not_claim_certification(self):
        out=evaluate_trust_gated_completeness(MANIFEST,POLICY,PIN)
        self.assertEqual(out["completeness_status"],"PASS")
        self.assertEqual(out["certification"],"NOT_PERFORMED")

if __name__=="__main__": unittest.main()
