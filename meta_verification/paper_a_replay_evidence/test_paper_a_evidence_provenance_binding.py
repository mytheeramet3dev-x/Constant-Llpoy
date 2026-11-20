import unittest
from paper_a_evidence_provenance_binding import (
    ProvenanceBindingError, validate_provenance_binding, compare_provenance_bindings,
)
H="1"*64
def record(**overrides):
    r={"evaluation_id":"ev-01","evidence_bundle_sha256":H,"policy_sha256":"2"*64,
       "verifier_id":"constant-llpoy","verifier_version":"0.1.0",
       "environment_id":"python-ci-ubuntu","result_record_sha256":"3"*64}
    r.update(overrides); return r
class ProvenanceBindingTests(unittest.TestCase):
    def test_valid_record(self): self.assertEqual(validate_provenance_binding(record())["evaluation_id"],"ev-01")
    def test_missing_field(self):
        r=record(); r.pop("verifier_id")
        with self.assertRaises(ProvenanceBindingError): validate_provenance_binding(r)
    def test_empty_verifier_id(self):
        with self.assertRaises(ProvenanceBindingError): validate_provenance_binding(record(verifier_id=" "))
    def test_empty_environment(self):
        with self.assertRaises(ProvenanceBindingError): validate_provenance_binding(record(environment_id=""))
    def test_malformed_bundle_digest(self):
        with self.assertRaises(ProvenanceBindingError): validate_provenance_binding(record(evidence_bundle_sha256="x"))
    def test_uppercase_digest_rejected(self):
        with self.assertRaises(ProvenanceBindingError): validate_provenance_binding(record(policy_sha256="A"*64))
    def test_malformed_result_digest(self):
        with self.assertRaises(ProvenanceBindingError): validate_provenance_binding(record(result_record_sha256="bad"))
    def test_no_certification_elevation(self):
        with self.assertRaises(ProvenanceBindingError): validate_provenance_binding(record(status="PASS",certification="CERTIFIED"))
    def test_same_bindings_compare_equal(self):
        self.assertTrue(compare_provenance_bindings(record(),record())["identical"])
    def test_evidence_change_detected(self):
        out=compare_provenance_bindings(record(),record(evidence_bundle_sha256="4"*64))
        self.assertFalse(out["identical"]); self.assertIn("evidence_bundle_sha256",out["differences"])
    def test_verifier_change_detected(self):
        out=compare_provenance_bindings(record(),record(verifier_id="other"))
        self.assertFalse(out["identical"]); self.assertIn("verifier_id",out["differences"])
if __name__=="__main__": unittest.main()
