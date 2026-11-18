"""Selected mutation-adequacy checks for status_aggregator.py."""
from __future__ import annotations
import pathlib, shutil, subprocess, sys, tempfile, unittest

ROOT = pathlib.Path(__file__).resolve().parent
SOURCE = ROOT / "status_aggregator.py"
TESTS = ROOT / "test_status_aggregator.py"
MUTANTS = {
 "skip_required_component_completeness": (
  'elif stale or duplicates or unknown or missing or pending:',
  'elif stale or duplicates or unknown or pending:'),
 "ignore_stale_source_commit": (
  '("claim_id", p["claim_id"]), ("source_commit", expected_commit),',
  '("claim_id", p["claim_id"]),'),
 "ignore_policy_revision": (
  '("policy_revision", p["policy_revision"]))',
  '("policy_revision", "0" * 40))'),
 "allow_unverified_receipt": (
  'receipt["status"] == "VERIFIED"',
  'receipt["status"] in {"VERIFIED", "UNVERIFIED", "FAILED"}'),
 "skip_subject_digest_binding": (
  'and receipt["subject_sha256"] == actual',
  ''),
 "skip_receipt_source_commit_binding": (
  'and receipt["source_commit"] == expected_commit',
  ''),
 "allow_boolean_run_id": (
  'type(receipt["verifier_run_id"]) is int',
  'isinstance(receipt["verifier_run_id"], int)'),
 "allow_boolean_run_attempt": (
  'type(receipt["verifier_run_attempt"]) is int',
  'isinstance(receipt["verifier_run_attempt"], int)'),
 "accept_empty_evidence": (
  '0 < len(evidence_bytes) <= MAX_EVIDENCE_BYTES',
  '0 <= len(evidence_bytes) <= MAX_EVIDENCE_BYTES'),
 "ignore_verified_failure": (
  'if state == "FAIL" and receipt_valid and cid not in digest_errors:',
  'if False and state == "FAIL" and receipt_valid and cid not in digest_errors:'),
 "ignore_duplicate_components": (
  'elif stale or duplicates or unknown or missing or pending:',
  'elif stale or unknown or missing or pending:'),
 "ignore_digest_mismatch": (
  'if digest_errors or verified_failures:',
  'if verified_failures:'),
}

class AggregatorMutationTests(unittest.TestCase):
 def test_each_mutant_is_killed_by_adversarial_suite(self):
  for name,(old,new) in MUTANTS.items():
   with self.subTest(mutant=name), tempfile.TemporaryDirectory() as td:
    root=pathlib.Path(td)
    source=SOURCE.read_text(encoding="utf-8")
    self.assertIn(old,source,f"mutation anchor absent: {name}")
    mutated=source.replace(old,new,1)
    (root/"status_aggregator.py").write_text(mutated,encoding="utf-8")
    shutil.copy2(TESTS,root/"test_status_aggregator.py")
    syntax=subprocess.run([sys.executable,"-m","py_compile",str(root/"status_aggregator.py")],capture_output=True,text=True)
    self.assertEqual(syntax.returncode,0,syntax.stderr)
    run=subprocess.run([sys.executable,"-m","unittest","-v","test_status_aggregator"],cwd=root,capture_output=True,text=True)
    self.assertNotEqual(run.returncode,0,f"mutant survived: {name}")
    self.assertIn("FAIL:",run.stderr+run.stdout,f"not assertion-driven: {name}\n{run.stderr}\n{run.stdout}")
    print(f"AGGREGATOR MUTANT KILLED: {name}")

if __name__ == "__main__":
 unittest.main(verbosity=2)
