#!/usr/bin/env python3
"""Mutation adequacy tests for the black-box trusted-builder conformance suite.

Each mutant is a single, controlled weakening of one security-relevant check.
The test copies the CLI and black-box suite to a temporary directory, applies
one mutation, syntax-checks the mutated CLI, then requires the black-box suite
to fail through an assertion. This tests whether the conformance suite detects
these specific regressions; it is not a proof of completeness.
"""
import py_compile
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
IMPLEMENTATION = "trusted_builder_reference.py"
CONFORMANCE = "test_trusted_builder_conformance.py"

MUTANTS = {
    "subject_byte_digest_bypass": (
        '_require(actual_sha256 == expected_subject_sha256, "subject SHA-256 mismatch")',
        '_require(True, "subject SHA-256 mismatch")',
    ),
    "canonical_record_digest_bypass": (
        '_require(actual_digest == claimed_digest, "evidence record digest mismatch")',
        '_require(True, "evidence record digest mismatch")',
    ),
    "accept_rejected_upstream_record": (
        '_require(record["status"] == "ACCEPTED", "upstream evidence is not ACCEPTED")',
        '_require(True, "upstream evidence is not ACCEPTED")',
    ),
    "caller_repository_id_bypass": (
        '_require(type(caller.get("repository_id")) is int and\n'
        '             caller.get("repository_id") == expected_repository_id, "caller repository ID mismatch")',
        '_require(True, "caller repository ID mismatch")',
    ),
    "upstream_run_id_replay_bypass": (
        '_require(type(upstream.get("run_id")) is int and upstream["run_id"] == expected_run_id,\n'
        '             "upstream run ID mismatch")',
        '_require(True, "upstream run ID mismatch")',
    ),
    "path_traversal_guard_bypass": (
        '_require(all(part not in ("", ".", "..") for part in relative_path.split("/")),\n'
        '             "non-canonical or traversal subject path is forbidden")',
        '_require(True, "non-canonical or traversal subject path is forbidden")',
    ),
    "signed_status_escalation": (
        '"status": "VALIDATED_LOCAL_UNTRUSTED",',
        '"status": "SIGNED",',
    ),
}


class TrustedBuilderMutationAdequacyTests(unittest.TestCase):
    def test_each_security_mutant_is_killed_by_black_box_suite(self):
        source = (ROOT / IMPLEMENTATION).read_text(encoding="utf-8")
        suite = ROOT / CONFORMANCE
        self.assertTrue(suite.is_file(), "black-box conformance suite missing")

        for name, (original, replacement) in MUTANTS.items():
            with self.subTest(mutant=name):
                self.assertEqual(source.count(original), 1,
                                 f"mutation anchor for {name} must occur exactly once")
                with tempfile.TemporaryDirectory() as tmp:
                    work = Path(tmp)
                    shutil.copy2(suite, work / CONFORMANCE)
                    mutated = source.replace(original, replacement, 1)
                    target = work / IMPLEMENTATION
                    target.write_text(mutated, encoding="utf-8")

                    try:
                        py_compile.compile(str(target), doraise=True)
                    except py_compile.PyCompileError as exc:
                        self.fail(f"{name} is an invalid mutant, not a killed mutant: {exc}")

                    result = subprocess.run(
                        [sys.executable, "-m", "unittest", "-v", "test_trusted_builder_conformance"],
                        cwd=work, text=True, capture_output=True, timeout=30, check=False,
                    )
                    output = result.stdout + result.stderr
                    self.assertNotEqual(result.returncode, 0,
                                        f"surviving mutant: {name}\n{output}")
                    self.assertIn("FAILED (", output,
                                  f"{name} did not fail through a test assertion\n{output}")
                    self.assertIn("Ran ", output,
                                  f"{name} did not execute the conformance suite\n{output}")
                    self.assertNotIn("ImportError", output,
                                     f"{name} failed for an import error, not a detected mutation\n{output}")
                    self.assertNotIn("SyntaxError", output,
                                     f"{name} failed for syntax, not a detected mutation\n{output}")


if __name__ == "__main__":
    unittest.main()
