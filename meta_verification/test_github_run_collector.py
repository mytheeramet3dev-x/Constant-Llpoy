"""Adversarial tests for GitHub Actions run snapshot validation."""
import copy
import unittest
from github_run_collector import CollectionError, validate_snapshot

REPO="owner/repository"; HEAD="a"*40; WF="b"*40; EV="c"*40
JOB="Fail-closed policy evaluator unit tests"
STEP_NAMES=["Checkout repository","Set up Python","Run adversarial unit tests"]

def fixture():
    p={"schema_version":"1.0","workflow_id":42,"workflow_path":".github/workflows/meta-verification.yml",
       "workflow_blob_sha":WF,"evaluator_path":"meta_verification/status_evaluator.py","evaluator_blob_sha":EV,
       "required_jobs":[JOB],"required_steps":{JOB:STEP_NAMES},"allowed_events":["push","workflow_dispatch"],"required_branch":"main"}
    run={"id":123,"head_sha":HEAD,"workflow_id":42,"path":p["workflow_path"],"status":"completed","event":"push",
         "head_branch":"main","conclusion":"success","run_attempt":1,"repository":{"full_name":REPO},"head_repository":{"full_name":REPO}}
    steps=[{"name":n,"status":"completed","conclusion":"success"} for n in STEP_NAMES]
    jobs={"total_count":1,"jobs":[{"id":900,"name":JOB,"status":"completed","conclusion":"success","steps":steps}]}
    return p,run,jobs,{"type":"file","sha":WF},{"type":"file","sha":EV}

def check(x):
    return validate_snapshot(*x,expected_run_id=123,expected_head_sha=HEAD,expected_repo=REPO)

class CollectorTests(unittest.TestCase):
    def test_valid_run_accepted(self): self.assertEqual(check(fixture())["status"],"ACCEPTED")
    def test_workflow_failure_rejected(self):
        x=fixture(); x[1]["conclusion"]="failure"; self.assertEqual(check(x)["status"],"REJECTED")
    def test_failed_or_skipped_job_rejected(self):
        for state in ("failure","skipped","cancelled","timed_out"):
            x=fixture(); x[2]["jobs"][0]["conclusion"]=state
            with self.subTest(state=state): self.assertEqual(check(x)["status"],"REJECTED")
    def test_incomplete_job_is_error(self):
        x=fixture(); x[2]["jobs"][0]["status"]="in_progress"
        with self.assertRaises(CollectionError): check(x)
    def test_failed_or_skipped_required_step_rejected(self):
        for state in ("failure","skipped"):
            x=fixture(); x[2]["jobs"][0]["steps"][1]["conclusion"]=state
            with self.subTest(state=state): self.assertEqual(check(x)["status"],"REJECTED")
    def test_missing_required_step_is_error(self):
        x=fixture(); x[2]["jobs"][0]["steps"].pop()
        with self.assertRaises(CollectionError): check(x)
    def test_run_identity_and_head_binding(self):
        for key,value in (("id",999),("head_sha","d"*40),("workflow_id",99),("path","other.yml")):
            x=fixture(); x[1][key]=value
            with self.subTest(key=key):
                with self.assertRaises(CollectionError): check(x)
    def test_repository_and_fork_binding(self):
        for key in ("repository","head_repository"):
            x=fixture(); x[1][key]["full_name"]="attacker/fork"
            with self.subTest(key=key):
                with self.assertRaises(CollectionError): check(x)
    def test_event_and_branch_policy(self):
        x=fixture(); x[1]["event"]="pull_request"
        with self.assertRaises(CollectionError): check(x)
        x=fixture(); x[1]["head_branch"]="feature"
        with self.assertRaises(CollectionError): check(x)
    def test_workflow_and_evaluator_blob_pins(self):
        for idx in (3,4):
            x=fixture(); x[idx]["sha"]="d"*40
            with self.subTest(index=idx):
                with self.assertRaises(CollectionError): check(x)
    def test_paginated_or_incomplete_jobs_rejected(self):
        x=fixture(); x[2]["total_count"]=2
        with self.assertRaises(CollectionError): check(x)
    def test_unexpected_and_duplicate_jobs_rejected(self):
        x=fixture(); x[2]["jobs"].append(copy.deepcopy(x[2]["jobs"][0])); x[2]["total_count"]=2
        with self.assertRaises(CollectionError): check(x)
    def test_record_digest_is_deterministic(self):
        self.assertEqual(check(fixture())["record_sha256"],check(fixture())["record_sha256"])

if __name__=="__main__": unittest.main(verbosity=2)
