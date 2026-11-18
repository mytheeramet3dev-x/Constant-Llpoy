"""Adversarial tests for GitHub Actions run snapshot validation."""
import copy
import unittest
from unittest import mock
import io
import urllib.error
from github_run_collector import CollectionError, validate_snapshot, decode_api_response, api_get, MAX_API_RESPONSE_BYTES

REPO="owner/repository"; HEAD="a"*40; WF="b"*40; EV="c"*40
JOB="Fail-closed policy evaluator unit tests"
STEP_NAMES=["Checkout repository","Set up Python","Run adversarial unit tests"]

def fixture():
    p={"schema_version":"1.0","workflow_id":42,"workflow_path":".github/workflows/meta-verification.yml",
       "workflow_blob_sha":WF,"evaluator_path":"meta_verification/status_evaluator.py","evaluator_blob_sha":EV,
       "required_jobs":[JOB],"required_steps":{JOB:STEP_NAMES},"allowed_events":["push","workflow_dispatch"],"required_branch":"main"}
    run={"id":123,"head_sha":HEAD,"workflow_id":42,"path":p["workflow_path"],"status":"completed","event":"push",
         "head_branch":"main","conclusion":"success","run_attempt":1,"repository":{"id":555,"full_name":REPO},"head_repository":{"id":555,"full_name":REPO}}
    steps=[{"name":n,"status":"completed","conclusion":"success"} for n in STEP_NAMES]
    jobs={"total_count":1,"jobs":[{"id":900,"run_id":123,"run_attempt":1,"name":JOB,"status":"completed","conclusion":"success","steps":steps}]}
    return p,run,jobs,{"type":"file","sha":WF},{"type":"file","sha":EV}

def check(x):
    return validate_snapshot(*x,expected_run_id=123,expected_run_attempt=1,expected_head_sha=HEAD,expected_repo=REPO)

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
    def test_boolean_policy_workflow_id_rejected(self):
        x=fixture(); x[0]["workflow_id"]=True; x[1]["workflow_id"]=1
        with self.assertRaises(CollectionError): check(x)
    def test_boolean_expected_run_id_rejected(self):
        x=fixture(); x[1]["id"]=1; x[2]["jobs"][0]["run_id"]=1
        with self.assertRaises(CollectionError):
            validate_snapshot(*x,expected_run_id=True,expected_run_attempt=1,expected_head_sha=HEAD,expected_repo=REPO)
    def test_boolean_run_id_rejected_independently(self):
        x=fixture(); x[1]["id"]=True; x[2]["jobs"][0]["run_id"]=1
        with self.assertRaises(CollectionError):
            validate_snapshot(*x,expected_run_id=1,expected_run_attempt=1,expected_head_sha=HEAD,expected_repo=REPO)
    def test_boolean_workflow_id_binding_rejected_independently(self):
        x=fixture(); x[0]["workflow_id"]=1; x[1]["workflow_id"]=True
        with self.assertRaises(CollectionError): check(x)
    def test_missing_or_invalid_run_attempt_rejected(self):
        for value in (None,0,True,"1"):
            x=fixture(); x[1]["run_attempt"]=value
            with self.subTest(value=value):
                with self.assertRaises(CollectionError): check(x)
    def test_stale_or_replayed_run_attempt_rejected(self):
        for value in (2,3):
            x=fixture(); x[1]["run_attempt"]=value
            with self.subTest(value=value):
                with self.assertRaises(CollectionError): check(x)
    def test_expected_run_attempt_must_be_exact_positive_integer(self):
        x=fixture()
        for value in (True,0,-1,"1"):
            with self.subTest(value=value):
                with self.assertRaises(CollectionError):
                    validate_snapshot(*x,expected_run_id=123,expected_run_attempt=value,expected_head_sha=HEAD,expected_repo=REPO)
    def test_job_run_id_and_attempt_must_match_parent_run(self):
        for key,value in (("run_id",124),("run_attempt",2)):
            x=fixture(); x[2]["jobs"][0][key]=value
            with self.subTest(key=key):
                with self.assertRaises(CollectionError): check(x)
    def test_job_run_id_and_attempt_reject_boolean(self):
        for key in ("run_id","run_attempt"):
            x=fixture(); x[2]["jobs"][0][key]=True
            with self.subTest(key=key):
                with self.assertRaises(CollectionError): check(x)
    def test_jobs_response_over_single_page_rejected(self):
        x=fixture(); x[2]["total_count"]=101
        with self.assertRaises(CollectionError): check(x)
    def test_numeric_repository_identity_must_match(self):
        x=fixture(); x[1]["head_repository"]["id"]=777
        with self.assertRaises(CollectionError): check(x)
    def test_primary_repository_name_must_match(self):
        x=fixture(); x[1]["repository"]["full_name"]="attacker/repository"
        with self.assertRaises(CollectionError): check(x)
    def test_head_repository_name_must_match(self):
        x=fixture(); x[1]["head_repository"]["full_name"]="attacker/repository"
        with self.assertRaises(CollectionError): check(x)
    def test_job_ids_must_be_positive_exact_integers(self):
        for value in (None,0,True,"900"):
            x=fixture(); x[2]["jobs"][0]["id"]=value
            with self.subTest(value=value):
                with self.assertRaises(CollectionError): check(x)
    def test_duplicate_job_ids_rejected(self):
        x=fixture(); other=copy.deepcopy(x[2]["jobs"][0]); other["name"]="unexpected second job"
        x[2]["jobs"].append(other); x[2]["total_count"]=2
        with self.assertRaises(CollectionError): check(x)
    def test_boolean_jobs_total_count_rejected(self):
        x=fixture(); x[2]["total_count"]=True
        with self.assertRaises(CollectionError): check(x)
    def test_duplicate_job_ids_rejected_independently(self):
        x=fixture()
        second="Second required job"
        x[0]["required_jobs"].append(second)
        x[0]["required_steps"][second]=list(STEP_NAMES)
        duplicate=copy.deepcopy(x[2]["jobs"][0]); duplicate["name"]=second
        x[2]["jobs"].append(duplicate); x[2]["total_count"]=2
        with self.assertRaises(CollectionError): check(x)
    def test_api_json_duplicate_keys_rejected(self):
        with self.assertRaises(CollectionError): decode_api_response(b'{"id":1,"id":2}')
    def test_api_json_nonstandard_constants_rejected(self):
        for raw in (b'{"x":NaN}',b'{"x":Infinity}',b'{"x":-Infinity}'):
            with self.subTest(raw=raw):
                with self.assertRaises(CollectionError): decode_api_response(raw)
    def test_api_json_non_object_rejected(self):
        for raw in (b'[]',b'null',b'"string"',b'1'):
            with self.subTest(raw=raw):
                with self.assertRaises(CollectionError): decode_api_response(raw)
    def test_api_json_invalid_utf8_rejected(self):
        with self.assertRaises(CollectionError): decode_api_response(bytes([123,34,120,34,58,34,255,34,125]))
    def test_api_json_size_limit_enforced(self):
        with self.assertRaises(CollectionError): decode_api_response(b' '*(MAX_API_RESPONSE_BYTES+1))
    def test_api_get_http_error_fails_closed(self):
        error=urllib.error.HTTPError("https://api.github.com/test",503,"unavailable",{},io.BytesIO(b""))
        with mock.patch("urllib.request.urlopen",side_effect=error):
            with self.assertRaises(CollectionError): api_get("https://api.github.com/test","token")
    def test_api_get_timeout_fails_closed(self):
        with mock.patch("urllib.request.urlopen",side_effect=TimeoutError("timed out")):
            with self.assertRaises(CollectionError): api_get("https://api.github.com/test","token")
    def test_record_digest_is_deterministic(self):
        self.assertEqual(check(fixture())["record_sha256"],check(fixture())["record_sha256"])

if __name__=="__main__": unittest.main(verbosity=2)
