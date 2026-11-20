import unittest

from paper_a_evidence_status_semantics import (
    StatusSemanticsError, validate_status_record, validate_status_continuity,
)

D = "a" * 64
E = "b" * 64


def rec(status="PASS", **kw):
    r = {
        "evaluation_id": "eval-1", "scope": "bundle hash and policy integrity",
        "status": status, "evidence_bundle_sha256": D, "policy_sha256": E,
        "evidence_ids": ["ev-1"], "reason": None,
    }
    r.update(kw)
    return r


class StatusSemanticsTests(unittest.TestCase):
    def test_valid_pass(self):
        self.assertEqual(validate_status_record(rec())["status"], "PASS")

    def test_pass_requires_scope(self):
        with self.assertRaises(StatusSemanticsError):
            validate_status_record(rec(scope=" "))

    def test_pass_requires_evidence_ids(self):
        with self.assertRaises(StatusSemanticsError):
            validate_status_record(rec(evidence_ids=[]))

    def test_invalid_bundle_digest(self):
        with self.assertRaises(StatusSemanticsError):
            validate_status_record(rec(evidence_bundle_sha256="bad"))

    def test_invalid_policy_digest(self):
        with self.assertRaises(StatusSemanticsError):
            validate_status_record(rec(policy_sha256="bad"))

    def test_fail_requires_reason(self):
        with self.assertRaises(StatusSemanticsError):
            validate_status_record(rec("FAIL", reason=None))

    def test_indeterminate_requires_reason(self):
        with self.assertRaises(StatusSemanticsError):
            validate_status_record(rec("INDETERMINATE", reason=" "))

    def test_not_applicable_requires_reason(self):
        with self.assertRaises(StatusSemanticsError):
            validate_status_record(rec("NOT_APPLICABLE", reason=None))

    def test_not_evaluated_requires_reason(self):
        with self.assertRaises(StatusSemanticsError):
            validate_status_record(rec("NOT_EVALUATED", reason=""))

    def test_fail_closed_requires_downstream_not_evaluated(self):
        with self.assertRaises(StatusSemanticsError):
            validate_status_record(rec("FAIL_CLOSED", reason="pin failure"))

    def test_fail_closed_valid(self):
        r = rec("FAIL_CLOSED", reason="pin failure", evidence_ids=[], downstream_status="NOT_EVALUATED")
        self.assertEqual(validate_status_record(r)["status"], "FAIL_CLOSED")

    def test_duplicate_evidence_ids_rejected(self):
        with self.assertRaises(StatusSemanticsError):
            validate_status_record(rec(evidence_ids=["x", "x"]))

    def test_unknown_status_rejected(self):
        with self.assertRaises(StatusSemanticsError):
            validate_status_record(rec("CERTIFIED"))

    def test_same_id_status_promotion_rejected(self):
        old = rec("FAIL", reason="hash mismatch")
        new = rec("PASS")
        with self.assertRaises(StatusSemanticsError):
            validate_status_continuity(old, new)

    def test_same_id_context_digest_mutation_rejected(self):
        old = rec()
        new = rec(evidence_bundle_sha256="c" * 64)
        with self.assertRaises(StatusSemanticsError):
            validate_status_continuity(old, new)

    def test_new_evaluation_id_allows_re_evaluation(self):
        old = rec("FAIL", reason="prior failure")
        new = rec(evaluation_id="eval-2", status="PASS")
        self.assertEqual(validate_status_continuity(old, new)["evaluation_id"], "eval-2")

    def test_fail_closed_cannot_claim_downstream_pass(self):
        with self.assertRaises(StatusSemanticsError):
            validate_status_record(rec("FAIL_CLOSED", reason="pin failure",
                                     evidence_ids=[], downstream_status="PASS"))

    def test_non_failclosed_cannot_smuggle_downstream_status(self):
        with self.assertRaises(StatusSemanticsError):
            validate_status_record(rec(downstream_status="PASS"))


if __name__ == "__main__":
    unittest.main()
