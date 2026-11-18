#!/usr/bin/env python3
"""Adversarial tests for the non-signing local trusted-builder reference."""
import hashlib
import json
import os
import tempfile
import unittest
from pathlib import Path

from trusted_builder_reference import BuilderValidationError, validate_subject

REPO = "mytheeramet3dev-x/Constant-Llpoy"
REPO_ID = 1460417275
WORKFLOW = "mytheeramet3dev-x/Constant-Llpoy/.github/workflows/meta-verification-evidence.yml"
REF = "refs/heads/main"
COMMIT = "a" * 40
RUN_ID = 12345


def evidence_record():
    record = {
        "schema_version": "1.0", "repository": REPO, "run_id": RUN_ID,
        "head_sha": COMMIT, "workflow_id": 100, "workflow_path": WORKFLOW,
        "workflow_blob_sha": "b" * 40, "evaluator_path": "meta_verification/status_evaluator.py",
        "evaluator_blob_sha": "c" * 40, "event": "workflow_run", "branch": "main",
        "run_attempt": 1, "workflow_conclusion": "success",
        "jobs": [{"name": "policy-evaluator-tests", "conclusion": "success"}],
        "status": "ACCEPTED", "failure_reasons": [],
    }
    canonical = json.dumps(record, sort_keys=True, separators=(",", ":")).encode()
    record["record_sha256"] = hashlib.sha256(canonical).hexdigest()
    return record


class TrustedBuilderReferenceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.subject = self.root / "evidence.json"
        self.write_record(evidence_record())
        self.caller = {"repository": REPO, "repository_id": REPO_ID,
                       "workflow": WORKFLOW, "ref": REF}
        self.upstream = {"run_id": RUN_ID, "status": "completed", "conclusion": "success",
                         "head_sha": COMMIT, "repository_id": REPO_ID,
                         "workflow": WORKFLOW, "ref": REF}
        self.args = {
            "checkout_root": self.root, "subject_path": "evidence.json",
            "expected_subject_sha256": hashlib.sha256(self.subject.read_bytes()).hexdigest(),
            "source_commit": COMMIT, "caller": self.caller, "upstream": self.upstream,
            "expected_repository": REPO, "expected_repository_id": REPO_ID,
            "expected_workflow": WORKFLOW, "expected_ref": REF,
            "expected_run_id": RUN_ID,
        }

    def tearDown(self):
        self.tmp.cleanup()

    def write_record(self, record):
        self.subject.write_text(json.dumps(record, separators=(",", ":")), encoding="utf-8")

    def refresh_digest(self):
        self.args["expected_subject_sha256"] = hashlib.sha256(self.subject.read_bytes()).hexdigest()

    def reject(self, **changes):
        args = dict(self.args)
        args.update(changes)
        with self.assertRaises(BuilderValidationError):
            validate_subject(**args)

    def test_valid_subject_returns_explicit_non_signing_status(self):
        report = validate_subject(**self.args)
        self.assertEqual(report["status"], "VALIDATED_LOCAL_UNTRUSTED")
        self.assertFalse(report["signing_performed"])
        self.assertFalse(report["attestation_created"])
        self.assertFalse(report["trust_established"])

    def test_subject_digest_mismatch_rejected(self):
        self.reject(expected_subject_sha256="0" * 64)

    def test_wrong_caller_repository_id_rejected(self):
        self.reject(caller={**self.caller, "repository_id": REPO_ID + 1})

    def test_wrong_caller_workflow_rejected(self):
        self.reject(caller={**self.caller, "workflow": "attacker.yml"})

    def test_wrong_caller_ref_rejected(self):
        self.reject(caller={**self.caller, "ref": "refs/heads/attacker"})

    def test_upstream_failed_cancelled_skipped_and_incomplete_rejected(self):
        for status, conclusion in [
            ("completed", "failure"), ("completed", "cancelled"),
            ("completed", "skipped"), ("in_progress", None),
        ]:
            with self.subTest(status=status, conclusion=conclusion):
                self.reject(upstream={**self.upstream, "status": status, "conclusion": conclusion})

    def test_upstream_replay_from_other_run_rejected(self):
        self.reject(upstream={**self.upstream, "run_id": RUN_ID + 1})

    def test_upstream_repository_id_mismatch_rejected(self):
        self.reject(upstream={**self.upstream, "repository_id": REPO_ID + 1})

    def test_upstream_source_commit_mismatch_rejected(self):
        self.reject(upstream={**self.upstream, "head_sha": "d" * 40})

    def test_absolute_path_rejected(self):
        self.reject(subject_path=str(self.subject))

    def test_backslash_path_rejected(self):
        self.reject(subject_path="folder\\\\evidence.json")

    def test_parent_traversal_rejected(self):
        self.reject(subject_path="../evidence.json")

    def test_noncanonical_dot_path_rejected(self):
        self.reject(subject_path="./evidence.json")

    def test_symlink_rejected(self):
        link = self.root / "link.json"
        link.symlink_to(self.subject)
        self.reject(subject_path="link.json")

    def test_symlink_parent_directory_rejected(self):
        with tempfile.TemporaryDirectory() as outside:
            external = Path(outside)
            (external / "evidence.json").write_bytes(self.subject.read_bytes())
            (self.root / "linked-dir").symlink_to(external, target_is_directory=True)
            self.reject(subject_path="linked-dir/evidence.json")

    def test_fifo_subject_rejected_without_blocking(self):
        fifo = self.root / "pipe.json"
        os.mkfifo(fifo)
        self.reject(subject_path="pipe.json")

    def test_directory_rejected(self):
        self.reject(subject_path=".")

    def test_oversized_subject_rejected(self):
        self.reject(max_subject_bytes=5)

    def test_empty_subject_rejected(self):
        self.subject.write_bytes(b"")
        self.refresh_digest()
        self.reject()

    def test_invalid_utf8_rejected(self):
        self.subject.write_bytes(bytes([0xff]))
        self.refresh_digest()
        self.reject()

    def test_malformed_json_rejected(self):
        self.subject.write_text("{not-json", encoding="utf-8")
        self.refresh_digest()
        self.reject()

    def test_nonstandard_nan_constant_rejected(self):
        self.subject.write_text('{"value":NaN}', encoding="utf-8")
        self.refresh_digest()
        self.reject()

    def test_duplicate_json_keys_rejected(self):
        self.subject.write_text('{"schema_version":"1.0","schema_version":"1.0"}', encoding="utf-8")
        self.refresh_digest()
        self.reject()

    def test_unknown_evidence_field_rejected(self):
        record = evidence_record()
        record["attacker_extension"] = True
        self.write_record(record)
        self.refresh_digest()
        self.reject()

    def test_stale_evidence_digest_rejected(self):
        record = evidence_record()
        record["branch"] = "tampered"
        self.write_record(record)
        self.refresh_digest()
        self.reject()

    def test_nonaccepted_upstream_evidence_rejected(self):
        record = evidence_record()
        record["status"] = "REJECTED"
        record["record_sha256"] = "0" * 64
        self.write_record(record)
        self.refresh_digest()
        self.reject()

    def test_wrong_evidence_source_commit_rejected(self):
        record = evidence_record()
        record["head_sha"] = "e" * 40
        canonical = dict(record)
        canonical.pop("record_sha256")
        record["record_sha256"] = hashlib.sha256(
            json.dumps(canonical, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest()
        self.write_record(record)
        self.refresh_digest()
        self.reject()

    def test_wrong_evidence_run_id_rejected(self):
        record = evidence_record()
        record["run_id"] = RUN_ID + 10
        canonical = dict(record)
        canonical.pop("record_sha256")
        record["record_sha256"] = hashlib.sha256(
            json.dumps(canonical, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest()
        self.write_record(record)
        self.refresh_digest()
        self.reject()


if __name__ == "__main__":
    unittest.main()
