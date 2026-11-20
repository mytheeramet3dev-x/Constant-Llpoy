import unittest
from paper_a_provenance_hmac import (
    ProvenanceAuthError, authenticate_record, verify_record_authentication,
)

KEY = b"test-only-secret-key-material-32bytes-minimum"
RECORD = {
    "evaluation_id": "eval-01",
    "evidence_bundle_sha256": "a" * 64,
    "policy_sha256": "b" * 64,
    "verifier_id": "independent-test",
    "verifier_version": "1.0",
    "environment_id": "ci-python",
    "result_record_sha256": "c" * 64,
    "status": "PASS",
    "certification": "NOT_PERFORMED",
}

class ProvenanceHMACTests(unittest.TestCase):
    def test_valid_record_authentication(self):
        mac = authenticate_record(RECORD, KEY)
        self.assertTrue(verify_record_authentication(RECORD, KEY, mac))

    def test_tampered_status_rejected(self):
        mac = authenticate_record(RECORD, KEY)
        changed = dict(RECORD, status="FAIL")
        self.assertFalse(verify_record_authentication(changed, KEY, mac))

    def test_tampered_bundle_digest_rejected(self):
        mac = authenticate_record(RECORD, KEY)
        changed = dict(RECORD, evidence_bundle_sha256="d" * 64)
        self.assertFalse(verify_record_authentication(changed, KEY, mac))

    def test_tampered_certification_field_rejected(self):
        mac = authenticate_record(RECORD, KEY)
        changed = dict(RECORD, certification="CERTIFIED")
        self.assertFalse(verify_record_authentication(changed, KEY, mac))

    def test_wrong_key_rejected(self):
        mac = authenticate_record(RECORD, KEY)
        self.assertFalse(verify_record_authentication(RECORD, b"wrong-key-" * 4, mac))

    def test_key_minimum_length(self):
        with self.assertRaises(ProvenanceAuthError):
            authenticate_record(RECORD, b"short")

    def test_missing_required_field_rejected(self):
        incomplete = dict(RECORD)
        incomplete.pop("verifier_id")
        with self.assertRaises(ProvenanceAuthError):
            authenticate_record(incomplete, KEY)

    def test_malformed_digest_rejected(self):
        malformed = dict(RECORD, policy_sha256="BAD")
        with self.assertRaises(ProvenanceAuthError):
            authenticate_record(malformed, KEY)

    def test_malformed_mac_rejected(self):
        with self.assertRaises(ProvenanceAuthError):
            verify_record_authentication(RECORD, KEY, "z" * 64)

    def test_non_string_record_field_rejected(self):
        malformed = dict(RECORD, environment_id=123)
        with self.assertRaises(ProvenanceAuthError):
            authenticate_record(malformed, KEY)

if __name__ == "__main__":
    unittest.main()
