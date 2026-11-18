#!/usr/bin/env python3
"""Mutation adequacy tests for the GitHub Actions run evidence collector.

Mutants are applied to isolated copies of the collector and its adversarial
unit suite. A kill requires the suite to execute and fail through assertions;
syntax/import failures are not counted.
"""
import py_compile
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
IMPLEMENTATION = "github_run_collector.py"
TEST_SUITE = "test_github_run_collector.py"

MUTANTS = {
    "boolean_workflow_id_policy": (
        'require(type(p["workflow_id"]) is int and p["workflow_id"]>0,"invalid workflow_id")',
        'require(isinstance(p["workflow_id"],int) and p["workflow_id"]>0,"invalid workflow_id")',
    ),
    "boolean_expected_run_id": (
        'require(type(expected_run_id) is int and expected_run_id>0,"invalid expected_run_id")',
        'require(isinstance(expected_run_id,int) and expected_run_id>0,"invalid expected_run_id")',
    ),
    "boolean_run_id": (
        'require(type(run.get("id")) is int and run.get("id")==expected_run_id,"run ID mismatch")',
        'require(run.get("id")==expected_run_id,"run ID mismatch")',
    ),
    "boolean_workflow_id_binding": (
        'require(type(run.get("workflow_id")) is int and run.get("workflow_id")==p["workflow_id"] and run.get("path")==p["workflow_path"],"workflow identity mismatch")',
        'require(run.get("workflow_id")==p["workflow_id"] and run.get("path")==p["workflow_path"],"workflow identity mismatch")',
    ),
    "run_attempt_validation_bypass": (
        'require(type(attempt) is int and attempt==expected_run_attempt,"workflow run attempt mismatch (stale or replayed attempt)")',
        'require(True,"invalid or missing workflow run attempt")',
    ),
    "job_run_id_binding_bypass": (
        'require(type(job.get("run_id")) is int and job.get("run_id")==expected_run_id,"job belongs to a different workflow run")',
        'require(True,"job belongs to a different workflow run")',
    ),
    "job_run_attempt_binding_bypass": (
        'require(type(job.get("run_attempt")) is int and job.get("run_attempt")==expected_run_attempt,"job belongs to a different workflow run attempt")',
        'require(True,"job belongs to a different workflow run attempt")',
    ),
    "run_attempt_expected_binding_bypass": (
        'require(type(attempt) is int and attempt==expected_run_attempt,"workflow run attempt mismatch (stale or replayed attempt)")',
        'require(type(attempt) is int and attempt>0,"workflow run attempt mismatch (stale or replayed attempt)")',
    ),
    "api_response_duplicate_key_rejection_bypass": (
        'require(key not in result,f"duplicate JSON object key: {key}")',
        'require(True,f"duplicate JSON object key: {key}")',
    ),
    "repository_numeric_identity_bypass": (
        'require(type(repo_id) is int and repo_id>0 and type(head_repo_id) is int and head_repo_id==repo_id,"repository numeric identity mismatch")',
        'require(True,"repository numeric identity mismatch")',
    ),
    "primary_repository_name_bypass": (
        'require(isinstance(run.get("repository"),dict) and run["repository"].get("full_name")==expected_repo,"repository mismatch")',
        'require(True,"repository mismatch")',
    ),
    "head_repository_name_bypass": (
        'require(isinstance(run.get("head_repository"),dict) and run["head_repository"].get("full_name")==expected_repo,"fork-originated run is not accepted")',
        'require(True,"fork-originated run is not accepted")',
    ),
    "job_pagination_completeness_bypass": (
        'require(bool(jobs) and type(jobs_response.get("total_count")) is int and jobs_response.get("total_count")==len(jobs) and len(jobs)<=100,"jobs response is empty, paginated, or incomplete")',
        'require(bool(jobs),"jobs response is empty or paginated/incomplete")',
    ),
    "job_id_type_and_range_bypass": (
        'require(all(type(x) is int and x>0 for x in job_ids),"job IDs must be positive integers")',
        'require(True,"job IDs must be positive integers")',
    ),
    "duplicate_job_id_bypass": (
        'require(len(job_ids)==len(set(job_ids)),"duplicate job IDs")',
        'require(True,"duplicate job IDs")',
    ),
    "workflow_blob_pin_bypass": (
        'require(wfsha==p["workflow_blob_sha"],"workflow file revision mismatch")',
        'require(True,"workflow file revision mismatch")',
    ),
    "evaluator_blob_pin_bypass": (
        'require(evsha==p["evaluator_blob_sha"],"evaluator file revision mismatch")',
        'require(True,"evaluator file revision mismatch")',
    ),
}

class CollectorMutationAdequacyTests(unittest.TestCase):
    def test_each_collector_mutant_is_killed(self):
        source = (ROOT / IMPLEMENTATION).read_text(encoding="utf-8")
        suite = ROOT / TEST_SUITE
        self.assertTrue(suite.is_file(), "collector adversarial test suite missing")
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
                        [sys.executable, "-m", "unittest", "-v", "test_github_run_collector"],
                        cwd=work, text=True, capture_output=True, timeout=30, check=False,
                    )
                    output = result.stdout + result.stderr
                    self.assertNotEqual(result.returncode, 0,
                                        f"surviving collector mutant: {name}\n{output}")
                    self.assertIn("FAILED (", output,
                                  f"{name} did not fail through an assertion\n{output}")
                    self.assertIn("Ran ", output,
                                  f"{name} did not execute the collector tests\n{output}")
                    self.assertNotIn("ImportError", output,
                                     f"{name} failed due to import error\n{output}")
                    self.assertNotIn("SyntaxError", output,
                                     f"{name} failed due to syntax error\n{output}")
                    print(f"COLLECTOR MUTANT KILLED: {name}")

if __name__ == "__main__":
    unittest.main(verbosity=2)
