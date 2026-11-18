#!/usr/bin/env python3
"""Collect and validate GitHub Actions run evidence through the authenticated API.

This is an API evidence collector, not a cryptographic attestation verifier.
"""
from __future__ import annotations
import argparse, hashlib, json, os, re, sys, urllib.error, urllib.parse, urllib.request
from pathlib import Path
from typing import Any

API = "https://api.github.com"
POLICY_KEYS = {"schema_version","workflow_id","workflow_path","workflow_blob_sha","evaluator_path","evaluator_blob_sha","required_jobs","required_steps","allowed_events","required_branch"}
SHA40 = re.compile(r"^[0-9a-f]{40}$")

class CollectionError(ValueError):
    pass

def require(ok: bool, message: str) -> None:
    if not ok: raise CollectionError(message)

def sha(value: Any, label: str) -> str:
    require(isinstance(value,str) and SHA40.fullmatch(value) is not None, f"{label} must be a lowercase 40-character Git SHA")
    return value

def validate_policy(p: Any) -> dict:
    require(isinstance(p,dict) and set(p)==POLICY_KEYS,"policy has missing or unknown fields")
    require(p["schema_version"]=="1.0","unsupported policy schema")
    require(type(p["workflow_id"]) is int and p["workflow_id"]>0,"invalid workflow_id")
    for k in ("workflow_path","evaluator_path","required_branch"):
        require(isinstance(p[k],str) and bool(p[k]),f"{k} must be non-empty")
    sha(p["workflow_blob_sha"],"workflow_blob_sha"); sha(p["evaluator_blob_sha"],"evaluator_blob_sha")
    jobs=p["required_jobs"]
    require(isinstance(jobs,list) and bool(jobs) and all(isinstance(x,str) and x for x in jobs),"required_jobs must be non-empty strings")
    require(len(jobs)==len(set(jobs)),"duplicate required job names")
    steps=p["required_steps"]
    require(isinstance(steps,dict) and set(steps)==set(jobs),"required_steps must define exactly the required jobs")
    for name, values in steps.items():
        require(isinstance(values,list) and bool(values) and all(isinstance(x,str) and x for x in values),f"invalid required steps for {name}")
        require(len(values)==len(set(values)),f"duplicate required steps for {name}")
    require(isinstance(p["allowed_events"],list) and bool(p["allowed_events"]),"allowed_events must be non-empty")
    require(all(x in {"push","workflow_dispatch"} for x in p["allowed_events"]),"event not permitted by collector policy")
    return p

def content_sha(obj: Any, label: str) -> str:
    require(isinstance(obj,dict) and obj.get("type")=="file",f"{label} is not a file")
    return sha(obj.get("sha"),f"{label} blob SHA")

def validate_snapshot(policy: Any, run: Any, jobs_response: Any, workflow_file: Any, evaluator_file: Any, *, expected_run_id: int, expected_head_sha: str, expected_repo: str) -> dict:
    p=validate_policy(policy); sha(expected_head_sha,"expected_head_sha")
    require(type(expected_run_id) is int and expected_run_id>0,"invalid expected_run_id")
    require(isinstance(expected_repo,str) and "/" in expected_repo,"expected_repo must be owner/name")
    require(isinstance(run,dict),"run response must be an object")
    require(type(run.get("id")) is int and run.get("id")==expected_run_id,"run ID mismatch")
    require(run.get("head_sha")==expected_head_sha,"run head SHA mismatch")
    require(type(run.get("workflow_id")) is int and run.get("workflow_id")==p["workflow_id"] and run.get("path")==p["workflow_path"],"workflow identity mismatch")
    require(run.get("status")=="completed","workflow run is not completed")
    require(run.get("event") in p["allowed_events"],"workflow event is not permitted")
    require(run.get("head_branch")==p["required_branch"],"workflow branch is not permitted")
    require(run.get("conclusion") in {"success","failure","cancelled","timed_out","action_required"},"unsupported workflow conclusion")
    require(isinstance(run.get("repository"),dict) and run["repository"].get("full_name")==expected_repo,"repository mismatch")
    require(isinstance(run.get("head_repository"),dict) and run["head_repository"].get("full_name")==expected_repo,"fork-originated run is not accepted")
    repo_id=run["repository"].get("id"); head_repo_id=run["head_repository"].get("id")
    require(type(repo_id) is int and repo_id>0 and type(head_repo_id) is int and head_repo_id==repo_id,"repository numeric identity mismatch")
    attempt=run.get("run_attempt")
    require(type(attempt) is int and attempt>0,"invalid or missing workflow run attempt")
    wfsha=content_sha(workflow_file,"workflow"); evsha=content_sha(evaluator_file,"evaluator")
    require(wfsha==p["workflow_blob_sha"],"workflow file revision mismatch")
    require(evsha==p["evaluator_blob_sha"],"evaluator file revision mismatch")
    require(isinstance(jobs_response,dict) and isinstance(jobs_response.get("jobs"),list),"malformed jobs response")
    jobs=jobs_response["jobs"]
    require(bool(jobs) and type(jobs_response.get("total_count")) is int and jobs_response.get("total_count")==len(jobs),"jobs response is empty or paginated/incomplete")
    names=[j.get("name") if isinstance(j,dict) else None for j in jobs]
    require(len(names)==len(set(names)),"duplicate job names")
    require(set(names)==set(p["required_jobs"]),"actual job set differs from policy")
    normalized=[]; failures=[]
    for job in jobs:
        name=job["name"]
        require(job.get("status")=="completed",f"job {name} is not completed")
        conclusion=job.get("conclusion")
        require(conclusion in {"success","failure","cancelled","skipped","timed_out","action_required"},f"unsupported conclusion for {name}")
        steps=job.get("steps")
        require(isinstance(steps,list),f"job {name} has no step list")
        by_name={}
        for step in steps:
            require(isinstance(step,dict) and isinstance(step.get("name"),str),f"malformed step in {name}")
            require(step["name"] not in by_name,f"duplicate step in {name}")
            by_name[step["name"]]=step
        missing=set(p["required_steps"][name])-set(by_name)
        require(not missing,f"missing required steps in {name}: {sorted(missing)}")
        selected=[]
        for step_name in p["required_steps"][name]:
            step=by_name[step_name]; state={"name":step_name,"status":step.get("status"),"conclusion":step.get("conclusion")}
            selected.append(state)
            if state["status"]!="completed" or state["conclusion"]!="success":
                failures.append(f"step:{name}/{step_name}:{state['status']}/{state['conclusion']}")
        normalized.append({"id":job.get("id"),"name":name,"status":job["status"],"conclusion":conclusion,"steps":selected})
        if conclusion!="success": failures.append(f"job:{name}:{conclusion}")
    if run["conclusion"]!="success": failures.append(f"workflow:{run['conclusion']}")
    record={"schema_version":"1.0","repository":expected_repo,"run_id":expected_run_id,"head_sha":expected_head_sha,
      "workflow_id":p["workflow_id"],"workflow_path":p["workflow_path"],"workflow_blob_sha":wfsha,
      "evaluator_path":p["evaluator_path"],"evaluator_blob_sha":evsha,"event":run["event"],
      "branch":run["head_branch"],"run_attempt":run.get("run_attempt"),"workflow_conclusion":run["conclusion"],
      "jobs":normalized,"status":"ACCEPTED" if not failures else "REJECTED","failure_reasons":failures}
    canonical=json.dumps(record,sort_keys=True,separators=(",",":")).encode()
    record["record_sha256"]=hashlib.sha256(canonical).hexdigest()
    return record

def api_get(url: str, token: str) -> Any:
    req=urllib.request.Request(url,headers={"Accept":"application/vnd.github+json","Authorization":f"Bearer {token}","X-GitHub-Api-Version":"2022-11-28","User-Agent":"constant-llpoy-meta-verification"})
    try:
        with urllib.request.urlopen(req,timeout=20) as response:
            require(response.status==200,f"GitHub API HTTP {response.status}")
            return json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError,TimeoutError,UnicodeError,json.JSONDecodeError) as exc:
        raise CollectionError(f"GitHub API request failed: {exc}") from None

def collect(policy: Any, repo: str, run_id: int, head_sha: str, token: str) -> dict:
    p=validate_policy(policy); require(bool(token),"GITHUB_TOKEN is required")
    base=f"{API}/repos/{repo}"; ref=urllib.parse.quote(head_sha,safe="")
    wf=urllib.parse.quote(p["workflow_path"],safe="/"); ev=urllib.parse.quote(p["evaluator_path"],safe="/")
    run=api_get(f"{base}/actions/runs/{run_id}",token)
    jobs=api_get(f"{base}/actions/runs/{run_id}/jobs?per_page=100",token)
    wf_file=api_get(f"{base}/contents/{wf}?ref={ref}",token)
    ev_file=api_get(f"{base}/contents/{ev}?ref={ref}",token)
    return validate_snapshot(p,run,jobs,wf_file,ev_file,expected_run_id=run_id,expected_head_sha=head_sha,expected_repo=repo)

def main(argv=None) -> int:
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument("--policy",required=True); parser.add_argument("--output",required=True); args=parser.parse_args(argv)
    try:
        p=json.loads(Path(args.policy).read_text(encoding="utf-8"))
        record=collect(p,os.environ["GITHUB_REPOSITORY"],int(os.environ["UPSTREAM_RUN_ID"]),os.environ["UPSTREAM_HEAD_SHA"],os.environ["GITHUB_TOKEN"])
        Path(args.output).write_text(json.dumps(record,indent=2,sort_keys=True)+"\n",encoding="utf-8")
        print(json.dumps({"status":record["status"],"run_id":record["run_id"],"head_sha":record["head_sha"],"record_sha256":record["record_sha256"],"failure_reasons":record["failure_reasons"]},sort_keys=True))
        return 0
    except (OSError,KeyError,ValueError,CollectionError) as exc:
        print(json.dumps({"status":"ERROR","error":str(exc)},sort_keys=True)); return 2

if __name__=="__main__": raise SystemExit(main())
