"""Adversarial unit tests for the fail-closed evidence-policy evaluator."""
from __future__ import annotations

import base64
import copy
import hashlib
import unittest

from status_evaluator import EvaluationError, evaluate

COMMIT = "a" * 40
CHECKER = "checker-revision-1"
WORKFLOW = "workflow-revision-1"


def artifact_fields(payload: bytes = b"independent-test-artifact") -> dict:
    return {
        "artifact_base64": base64.b64encode(payload).decode("ascii"),
        "artifact_sha256": hashlib.sha256(payload).hexdigest(),
    }


def fixture():
    policy = {
        "schema_version": "1.0",
        "claim_id": "CLAIM-001",
        "checker_revision": CHECKER,
        "workflow_revision": WORKFLOW,
        "required_obligations": ["O-1", "O-2"],
    }
    evidence = {
        "schema_version": "1.0",
        "claim_id": "CLAIM-001",
        "source_commit": COMMIT,
        "checker_revision": CHECKER,
        "workflow_revision": WORKFLOW,
        "obligations": [
            {"obligation_id": "O-1", "result": "ACCEPTED", **artifact_fields(b"certificate-one")},
            {"obligation_id": "O-2", "result": "ACCEPTED", **artifact_fields(b"certificate-two")},
        ],
    }
    return policy, evidence


class EvaluatorTests(unittest.TestCase):
    def test_all_current_valid_evidence_is_accepted(self):
        p, e = fixture()
        self.assertEqual(evaluate(p, e, COMMIT)["status"], "ACCEPTED")

    def test_rejected_evidence_is_rejected(self):
        p, e = fixture()
        e["obligations"][0]["result"] = "REJECTED"
        self.assertEqual(evaluate(p, e, COMMIT)["status"], "REJECTED")

    def test_missing_evidence_is_not_accepted(self):
        p, e = fixture()
        e["obligations"].pop()
        result = evaluate(p, e, COMMIT)
        self.assertEqual(result["status"], "INCONCLUSIVE")
        self.assertEqual(result["reasons"]["missing_obligations"], ["O-2"])

    def test_stale_source_commit_is_not_accepted(self):
        p, e = fixture()
        e["source_commit"] = "b" * 40
        self.assertEqual(evaluate(p, e, COMMIT)["status"], "INCONCLUSIVE")

    def test_stale_checker_revision_is_not_accepted(self):
        p, e = fixture()
        e["checker_revision"] = "old-checker"
        self.assertEqual(evaluate(p, e, COMMIT)["status"], "INCONCLUSIVE")

    def test_stale_workflow_revision_is_not_accepted(self):
        p, e = fixture()
        e["workflow_revision"] = "old-workflow"
        self.assertEqual(evaluate(p, e, COMMIT)["status"], "INCONCLUSIVE")

    def test_skipped_job_not_run_is_not_accepted(self):
        p, e = fixture()
        e["obligations"][0]["result"] = "NOT_RUN"
        self.assertEqual(evaluate(p, e, COMMIT)["status"], "INCONCLUSIVE")

    def test_error_timeout_and_inconclusive_are_not_accepted(self):
        for state in ("ERROR", "TIMEOUT", "INCONCLUSIVE"):
            with self.subTest(state=state):
                p, e = fixture()
                e["obligations"][0]["result"] = state
                self.assertEqual(evaluate(p, e, COMMIT)["status"], "INCONCLUSIVE")

    def test_forged_success_boolean_is_rejected_as_unknown_schema_field(self):
        p, e = fixture()
        e["success"] = True
        with self.assertRaises(EvaluationError):
            evaluate(p, e, COMMIT)

    def test_altered_artifact_bytes_are_detected(self):
        p, e = fixture()
        e["obligations"][0]["artifact_base64"] = base64.b64encode(b"tampered").decode("ascii")
        self.assertEqual(evaluate(p, e, COMMIT)["status"], "REJECTED")

    def test_forged_digest_does_not_match_artifact(self):
        p, e = fixture()
        e["obligations"][0]["artifact_sha256"] = "0" * 64
        self.assertEqual(evaluate(p, e, COMMIT)["status"], "REJECTED")

    def test_duplicate_obligation_is_not_accepted(self):
        p, e = fixture()
        e["obligations"].append(copy.deepcopy(e["obligations"][0]))
        self.assertEqual(evaluate(p, e, COMMIT)["status"], "INCONCLUSIVE")

    def test_unknown_obligation_is_not_accepted(self):
        p, e = fixture()
        extra = {"obligation_id": "O-X", "result": "ACCEPTED", **artifact_fields()}
        e["obligations"].append(extra)
        self.assertEqual(evaluate(p, e, COMMIT)["status"], "INCONCLUSIVE")

    def test_claim_mismatch_is_not_accepted(self):
        p, e = fixture()
        e["claim_id"] = "OTHER-CLAIM"
        self.assertEqual(evaluate(p, e, COMMIT)["status"], "INCONCLUSIVE")

    def test_unknown_evidence_field_fails_schema(self):
        p, e = fixture()
        e["reported_status"] = "ACCEPTED"
        with self.assertRaises(EvaluationError):
            evaluate(p, e, COMMIT)

    def test_unknown_item_field_fails_schema(self):
        p, e = fixture()
        e["obligations"][0]["verified"] = True
        with self.assertRaises(EvaluationError):
            evaluate(p, e, COMMIT)

    def test_duplicate_policy_obligations_are_invalid(self):
        p, e = fixture()
        p["required_obligations"].append("O-1")
        with self.assertRaises(EvaluationError):
            evaluate(p, e, COMMIT)

    def test_unsupported_schema_is_invalid(self):
        p, e = fixture()
        e["schema_version"] = "99"
        with self.assertRaises(EvaluationError):
            evaluate(p, e, COMMIT)

    def test_invalid_base64_is_invalid(self):
        p, e = fixture()
        e["obligations"][0]["artifact_base64"] = "%%%not-base64%%%"
        with self.assertRaises(EvaluationError):
            evaluate(p, e, COMMIT)

    def test_invalid_expected_commit_is_invalid(self):
        p, e = fixture()
        with self.assertRaises(EvaluationError):
            evaluate(p, e, "main")

    def test_empty_artifact_is_validly_hashable_but_not_proof(self):
        p, e = fixture()
        e["obligations"][0].update(artifact_fields(b""))
        self.assertEqual(evaluate(p, e, COMMIT)["status"], "ACCEPTED")


if __name__ == "__main__":
    unittest.main(verbosity=2)
