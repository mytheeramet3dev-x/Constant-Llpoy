#!/usr/bin/env python3
"""Black-box conformance tests for the local Trusted Builder CLI contract.

This suite deliberately does not import the implementation module. It creates
known-answer inputs independently and exercises the documented process interface.
It is still same-repository testing, not independent external governance.
"""
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CLI = ROOT / "trusted_builder_reference.py"
REPO = "mytheeramet3dev-x/Constant-Llpoy"
REPO_ID = 1460417275
WORKFLOW = REPO + "/.github/workflows/meta-verification-evidence.yml"
REF = "refs/heads/main"
COMMIT = "a" * 40
RUN_ID = 73142


def canonical_digest(record):
    body = {key: value for key, value in record.items() if key != "record_sha256"}
    encoded = json.dumps(body, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def known_answer_record():
    record = {
        "schema_version": "1.0",
        "repository": REPO,
        "run_id": RUN_ID,
        "head_sha": COMMIT,
        "workflow_id": 422030574,
        "workflow_path": WORKFLOW,
        "workflow_blob_sha": "b" * 40,
        "evaluator_path": "meta_verification/status_evaluator.py",
        "evaluator_blob_sha": "c" * 40,
        "event": "workflow_run",
        "branch": "main",
        "run_attempt": 1,
        "workflow_conclusion": "success",
        "jobs": [{"name": "policy-evaluator-tests", "conclusion": "success"}],
        "status": "ACCEPTED",
        "failure_reasons": [],
    }
    record["record_sha256"] = canonical_digest(record)
    return record


class TrustedBuilderBlackBoxConformance(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.subject = self.root / "subject.json"
        self.input = self.root / "request.json"
        self.output = self.root / "report.json"
        self.record = known_answer_record()
        self.write_subject(json.dumps(self.record, separators=(",", ":")).encode())
        self.request = {
            "checkout_root": str(self.root),
            "subject_path": "subject.json",
            "expected_subject_sha256": self.subject_digest(),
            "source_commit": COMMIT,
            "caller": {"repository": REPO, "repository_id": REPO_ID,
                       "workflow": WORKFLOW, "ref": REF},
            "upstream": {"run_id": RUN_ID, "status": "completed", "conclusion": "success",
                         "head_sha": COMMIT, "repository_id": REPO_ID,
                         "workflow": WORKFLOW, "ref": REF},
            "expected_repository": REPO,
            "expected_repository_id": REPO_ID,
            "expected_workflow": WORKFLOW,
            "expected_ref": REF,
            "expected_run_id": RUN_ID,
        }

    def tearDown(self):
        self.tmp.cleanup()

    def write_subject(self, raw):
        self.subject.write_bytes(raw)

    def subject_digest(self):
        return hashlib.sha256(self.subject.read_bytes()).hexdigest()

    def invoke(self, request=None, output_path=None, raw_input=None):
        if raw_input is None:
            self.input.write_text(json.dumps(self.request if request is None else request), encoding="utf-8")
        else:
            self.input.write_bytes(raw_input)
        result = subprocess.run(
            [sys.executable, str(CLI), "--input", str(self.input), "--output",
             str(self.output if output_path is None else output_path)],
            cwd=ROOT, text=True, capture_output=True, timeout=10, check=False,
        )
        try:
            stdout = json.loads(result.stdout.strip().splitlines()[-1])
        except (json.JSONDecodeError, IndexError):
            self.fail("CLI did not emit one machine-readable JSON status line: " + result.stdout)
        return result, stdout

    def reject(self, mutate_request=None, raw=None, subject_path=None):
        if raw is not None:
            self.write_subject(raw)
        request = dict(self.request)
        if raw is not None:
            request["expected_subject_sha256"] = self.subject_digest()
        if mutate_request:
            mutate_request(request)
        if subject_path is not None:
            request["subject_path"] = subject_path
        result, stdout = self.invoke(request)
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertEqual(stdout.get("status"), "REJECTED")
        self.assertFalse(self.output.exists())

    def test_known_answer_is_validated_without_signing(self):
        result, stdout = self.invoke()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(stdout, {
            "status": "VALIDATED_LOCAL_UNTRUSTED",
            "signing_performed": False,
            "subject_sha256": self.subject_digest(),
        })
        report = json.loads(self.output.read_text(encoding="utf-8"))
        self.assertEqual(report["status"], "VALIDATED_LOCAL_UNTRUSTED")
        self.assertIs(report["signing_performed"], False)
        self.assertIs(report["attestation_created"], False)
        self.assertIs(report["trust_established"], False)
        self.assertNotEqual(report["status"], "SIGNED")
        self.assertTrue(self.output.read_bytes().endswith(b"\n"))

    def test_subject_digest_substitution_rejected(self):
        self.reject(lambda request: request.update(expected_subject_sha256="0" * 64))

    def test_wrong_caller_repository_identity_rejected(self):
        self.reject(lambda request: request["caller"].update(repository_id=REPO_ID + 1))

    def test_wrong_caller_workflow_rejected(self):
        self.reject(lambda request: request["caller"].update(workflow="attacker.yml"))

    def test_wrong_caller_ref_rejected(self):
        self.reject(lambda request: request["caller"].update(ref="refs/heads/attacker"))

    def test_failed_upstream_run_rejected(self):
        self.reject(lambda request: request["upstream"].update(conclusion="failure"))

    def test_incomplete_upstream_run_rejected(self):
        self.reject(lambda request: request["upstream"].update(status="in_progress", conclusion=None))

    def test_replayed_upstream_run_id_rejected(self):
        self.reject(lambda request: request["upstream"].update(run_id=RUN_ID + 1))

    def test_source_revision_mismatch_rejected(self):
        self.reject(lambda request: request["upstream"].update(head_sha="d" * 40))

    def test_path_traversal_rejected(self):
        escaped = self.root.parent / (self.root.name + "-escaped.json")
        escaped.write_bytes(self.subject.read_bytes())
        try:
            self.reject(subject_path="../" + escaped.name)
        finally:
            escaped.unlink(missing_ok=True)

    def test_absolute_path_rejected(self):
        self.reject(subject_path=str(self.subject))

    def test_symlink_subject_rejected(self):
        link = self.root / "linked.json"
        link.symlink_to(self.subject)
        self.reject(subject_path="linked.json")

    def test_symlink_parent_rejected(self):
        outside = Path(self.tmp.name).parent / (self.root.name + "-outside")
        outside.mkdir()
        try:
            (outside / "subject.json").write_bytes(self.subject.read_bytes())
            (self.root / "linked-dir").symlink_to(outside, target_is_directory=True)
            self.reject(subject_path="linked-dir/subject.json")
        finally:
            (outside / "subject.json").unlink(missing_ok=True)
            outside.rmdir()

    def test_duplicate_json_keys_rejected(self):
        self.reject(raw=b'{"schema_version":"1.0","schema_version":"1.0"}')

    def test_nonstandard_json_constant_rejected(self):
        self.reject(raw=b'{"not_finite":NaN}')

    def test_malformed_utf8_rejected(self):
        self.reject(raw=b"\xff")

    def test_unknown_evidence_field_rejected(self):
        changed = dict(self.record)
        changed["unexpected"] = True
        changed["record_sha256"] = canonical_digest(changed)
        self.reject(raw=json.dumps(changed, separators=(",", ":")).encode())

    def test_stale_record_digest_rejected_even_when_subject_digest_matches(self):
        changed = dict(self.record)
        changed["branch"] = "tampered"
        self.reject(raw=json.dumps(changed, separators=(",", ":")).encode())

    def test_rejected_evidence_record_rejected(self):
        changed = dict(self.record)
        changed["status"] = "REJECTED"
        changed["record_sha256"] = canonical_digest(changed)
        self.reject(raw=json.dumps(changed, separators=(",", ":")).encode())

    def test_oversized_subject_rejected(self):
        request = dict(self.request)
        request["max_subject_bytes"] = 8
        result, stdout = self.invoke(request)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(stdout.get("status"), "REJECTED")

    def test_boolean_caller_repository_id_rejected(self):
        self.reject(lambda request: request["caller"].update(repository_id=True))

    def test_boolean_upstream_run_id_rejected(self):
        self.reject(lambda request: request["upstream"].update(run_id=True))

    def test_extra_caller_metadata_rejected(self):
        self.reject(lambda request: request["caller"].update(repository_owner="attacker"))

    def test_extra_upstream_metadata_rejected(self):
        self.reject(lambda request: request["upstream"].update(original_run_id=RUN_ID))

    def test_missing_caller_field_rejected(self):
        self.reject(lambda request: request["caller"].pop("workflow"))

    def test_missing_upstream_field_rejected(self):
        self.reject(lambda request: request["upstream"].pop("workflow"))

    def test_duplicate_top_level_request_key_rejected(self):
        raw = json.dumps(self.request, separators=(",", ":")).encode()
        raw = raw[:-1] + b',"expected_run_id":73142}'
        result, stdout = self.invoke(raw_input=raw)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(stdout.get("status"), "REJECTED")

    def test_nonstandard_constant_in_request_rejected(self):
        raw = json.dumps(self.request, separators=(",", ":")).encode()
        raw = raw[:-1] + b',"ignored_extension":NaN}'
        result, stdout = self.invoke(raw_input=raw)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(stdout.get("status"), "REJECTED")

    def test_output_symlink_is_not_followed(self):
        target = self.root / "target-report.json"
        target.write_text("do-not-overwrite", encoding="utf-8")
        link = self.root / "report-link.json"
        link.symlink_to(target)
        result, stdout = self.invoke(output_path=link)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(stdout.get("status"), "REJECTED")
        self.assertEqual(target.read_text(encoding="utf-8"), "do-not-overwrite")

    def test_output_parent_symlink_is_not_followed(self):
        outside = self.root.parent / (self.root.name + "-output-outside")
        outside.mkdir()
        try:
            link = self.root / "linked-output-dir"
            link.symlink_to(outside, target_is_directory=True)
            result, stdout = self.invoke(output_path=link / "report.json")
            self.assertEqual(result.returncode, 2)
            self.assertEqual(stdout.get("status"), "REJECTED")
            self.assertFalse((outside / "report.json").exists())
        finally:
            for item in outside.iterdir():
                item.unlink()
            outside.rmdir()

    def test_existing_output_file_is_not_overwritten(self):
        self.output.write_text("preserve-existing", encoding="utf-8")
        result, stdout = self.invoke()
        self.assertEqual(result.returncode, 2)
        self.assertEqual(stdout.get("status"), "REJECTED")
        self.assertEqual(self.output.read_text(encoding="utf-8"), "preserve-existing")


if __name__ == "__main__":
    unittest.main()
