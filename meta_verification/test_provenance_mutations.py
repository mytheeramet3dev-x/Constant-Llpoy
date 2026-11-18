#!/usr/bin/env python3
"""Mutation adequacy tests for the signed-provenance verifier.

Mutants are applied to isolated temporary copies of the verifier and its
unit-test suite. A mutant is killed only if the tests execute and fail through
an assertion; syntax/import/harness failures do not count.
"""
import py_compile
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
IMPLEMENTATION = "verify_signed_provenance.py"
TEST_SUITE = "test_signed_provenance.py"

MUTANTS = {
    "certificate_repository_id_bypass": (
        'require(str(certificate.get("sourceRepositoryIdentifier")) == str(policy["repository_id"]),\n'
        '            "signing certificate repository ID mismatch")',
        'require(True, "signing certificate repository ID mismatch")',
    ),
    "certificate_source_ref_bypass": (
        'require(certificate.get("sourceRepositoryRef") == policy["source_ref"],\n'
        '            "signing certificate source ref mismatch")',
        'require(True, "signing certificate source ref mismatch")',
    ),
    "certificate_source_commit_bypass": (
        'require(certificate.get("sourceRepositoryDigest") == source_sha,\n'
        '            "signing certificate source commit mismatch")',
        'require(True, "signing certificate source commit mismatch")',
    ),
    "signer_workflow_commit_bypass": (
        'require(certificate.get("buildSignerDigest") == source_sha,\n'
        '            "signing certificate signer workflow commit mismatch")',
        'require(True, "signing certificate signer workflow commit mismatch")',
    ),
    "verified_timestamp_bypass": (
        'require(isinstance(timestamps, list) and bool(timestamps),\n'
        '            "no verified transparency-log/timestamp evidence")',
        'require(True, "no verified transparency-log/timestamp evidence")',
    ),
    "predicate_type_bypass": (
        'require(statement.get("predicateType") == policy["predicate_type"],\n'
        '            "predicate type mismatch")',
        'require(True, "predicate type mismatch")',
    ),
    "subject_digest_bypass": (
        'if isinstance(digest, dict) and digest.get("sha256") == expected_digest:',
        'if isinstance(digest, dict):',
    ),
    "ambiguous_subject_acceptance": (
        'require(len(matching) == 1, "attestation subject does not uniquely match exact evidence bytes")',
        'require(len(matching) >= 1, "attestation subject does not uniquely match exact evidence bytes")',
    ),
    "boolean_repository_id_policy_acceptance": (
        'require(type(policy["repository_id"]) is int and policy["repository_id"] > 0,',
        'require(isinstance(policy["repository_id"], int) and policy["repository_id"] > 0,',
    ),
    "pinned_cli_version_bypass": (
        'require(match is not None and match.group(1) == p["gh_cli_version"],',
        'require(match is not None,',
    ),
}


class SignedProvenanceMutationAdequacyTests(unittest.TestCase):
    def test_each_verifier_mutant_is_killed(self):
        source = (ROOT / IMPLEMENTATION).read_text(encoding="utf-8")
        suite = ROOT / TEST_SUITE
        self.assertTrue(suite.is_file(), "signed provenance test suite missing")

        for name, (original, replacement) in MUTANTS.items():
            with self.subTest(mutant=name):
                self.assertEqual(source.count(original), 1,
                                 f"mutation anchor for {name} must occur exactly once")
                with tempfile.TemporaryDirectory() as tmp:
                    work = Path(tmp)
                    shutil.copy2(suite, work / TEST_SUITE)
                    target = work / IMPLEMENTATION
                    target.write_text(source.replace(original, replacement, 1), encoding="utf-8")
                    try:
                        py_compile.compile(str(target), doraise=True)
                    except py_compile.PyCompileError as exc:
                        self.fail(f"{name} is an invalid mutant, not a killed mutant: {exc}")

                    result = subprocess.run(
                        [sys.executable, "-m", "unittest", "-v", "test_signed_provenance"],
                        cwd=work, text=True, capture_output=True, timeout=30, check=False,
                    )
                    output = result.stdout + result.stderr
                    self.assertNotEqual(result.returncode, 0,
                                        f"surviving verifier mutant: {name}\n{output}")
                    self.assertIn("FAILED (", output,
                                  f"{name} did not fail through a test assertion\n{output}")
                    self.assertIn("Ran ", output,
                                  f"{name} did not execute the unit tests\n{output}")
                    self.assertNotIn("ImportError", output,
                                     f"{name} failed due to import error\n{output}")
                    self.assertNotIn("SyntaxError", output,
                                     f"{name} failed due to syntax error\n{output}")
                    print(f"PROVENANCE MUTANT KILLED: {name}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
