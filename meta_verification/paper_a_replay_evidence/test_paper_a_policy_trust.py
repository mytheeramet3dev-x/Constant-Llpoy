import unittest
from paper_a_policy_trust import policy_sha256, verify_policy_pin

POLICY={"policy_id":"p-test","version":"v1","required_inputs":["x"],"required_artifacts":["y"],"required_check_ids":["z"]}
def pin_for(policy, **overrides):
    pin={"policy_id":policy["policy_id"],"version":policy["version"],"sha256":policy_sha256(policy),
         "approval_status":"approved","approval_reference":"test-fixture"}
    pin.update(overrides)
    return pin

class PolicyPinTests(unittest.TestCase):
    def test_matching_approved_pin_passes(self):
        self.assertEqual(verify_policy_pin(POLICY,pin_for(POLICY))["status"],"PASS")
    def test_modified_policy_fails_digest(self):
        changed={**POLICY,"required_artifacts":["changed"]}
        self.assertEqual(verify_policy_pin(changed,pin_for(POLICY))["reason"],"policy_digest_mismatch")
    def test_unapproved_fails_closed(self):
        self.assertEqual(verify_policy_pin(POLICY,pin_for(POLICY,approval_status="pending"))["reason"],"pin_not_approved")
    def test_identity_mismatch_fails(self):
        self.assertEqual(verify_policy_pin(POLICY,pin_for(POLICY,version="v2"))["reason"],"policy_identity_mismatch")
    def test_bad_digest_format_fails(self):
        self.assertEqual(verify_policy_pin(POLICY,pin_for(POLICY,sha256="abc"))["reason"],"pin_digest_invalid")
    def test_pin_extra_field_rejected(self):
        self.assertEqual(verify_policy_pin(POLICY,{**pin_for(POLICY),"extra":1})["reason"],"pin_shape_invalid")
    def test_non_json_policy_fails(self):
        invalid={**POLICY,"extra":object()}
        self.assertEqual(verify_policy_pin(invalid,pin_for(POLICY))["reason"],"policy_not_canonicalizable")
    def test_digest_deterministic(self):
        self.assertEqual(policy_sha256(POLICY),policy_sha256(dict(reversed(list(POLICY.items())))))

if __name__=="__main__":
    unittest.main()
