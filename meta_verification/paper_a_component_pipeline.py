#!/usr/bin/env python3
"""Paper A evidence production, traceability and 14-layer trial orchestration.

PASS means an evidence-production operation completed, never that a theorem is true.
"""
from __future__ import annotations
import argparse, base64, hashlib, json, re, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path
from component_provenance_authenticator import authenticate_components
from status_aggregator import aggregate, AggregationError

PRODUCER_WORKFLOW=".github/workflows/paper-a-component-evidence.yml"
CLAIM_ROW=re.compile(r"^\|\s*(AS-ALPHA-A-[A-Z]+-\d{4})\s*\|")
CLAIM_ARTIFACTS={
"AS-ALPHA-A-THM-0002":[("formalization/lean/ConstantLlapoy/PaperA/PerronFrobeniusCore.lean","candidate_formal_artifact","NOT_ESTABLISHED"),("audits/paper-a/THM-0002_PERRON_FROBENIUS_INDEPENDENT_REVIEW.md","independent_proof_audit","REVIEW_REQUIRED")],
"AS-ALPHA-A-PROP-0009":[("formalization/lean/ConstantLlapoy/PaperA/StrongCoupling.lean","candidate_formal_artifact","NOT_ESTABLISHED"),("working/paper-a/finite_n_strong_coupling_exact_diagnostic.py","finite_n_diagnostic","DIAGNOSTIC_ONLY"),("audits/paper-a/UNIFORM_GN_STRONG_COUPLING_FUNCTION_AND_DERIVATIVE_PROOF.md","analytic_working_audit","REVIEW_REQUIRED")],
"AS-ALPHA-A-PROP-0012":[("formalization/lean/ConstantLlapoy/PaperA/WeakCoupling.lean","candidate_formal_artifact","NOT_ESTABLISHED"),("working/paper-a/edge_response_weak_coupling_diagnostic.py","numerical_diagnostic","DIAGNOSTIC_ONLY")],
"AS-ALPHA-A-PROP-0005":[("working/paper-a/dicke_even_basis_exact_diagnostic.py","exact_finite_n_diagnostic","DIAGNOSTIC_ONLY")]}
LAYERS=[
("L-01","Literature, Prior-Art, and Mathematical Claim Specification","REQUIRED","PARTIAL","15 source-linked records and frozen source manifest indexed; complete claim-specific prior-art search not established."),
("L-02","Semantic Correspondence and Formalization Audit","REQUIRED","BLOCKED","Exact line-level statement and hypothesis correspondence not established."),
("L-03","Boundary, Domain, and Scope-Quantifier Audit","REQUIRED","PARTIAL","Obligation and audit documents exist; complete executed audit for all claims not established."),
("L-04","Primary Kernel-Checked Formal Verification (Lean 4)","REQUIRED","PARTIAL","Pinned Lean build covers selected declarations only; whole-paper formalization remains open."),
("L-05","Independent Formal-Proof Route","REQUIRED_FOR_SELECTED_CLAIMS","NOT_RUN","No project-wide second prover route is established."),
("L-06","Exact Computational Verification","CONDITIONAL","PARTIAL","Exact finite-N symbolic diagnostics execute; they do not prove asymptotic or uniform-in-N claims."),
("L-07","Independent Implementation Cross-Checks","CONDITIONAL","PARTIAL","Two separately structured finite-N diagnostics are compared; shared runtime and specification risks remain."),
("L-08","Proof-Certificate Production and Independent Checking","CONDITIONAL","PARTIAL","Attestations authenticate evidence bytes, not mathematical proof certificates."),
("L-09","Numerical Analysis and Adversarial Testing","REQUIRED","PARTIAL","High-precision diagnostics execute; parameter coverage and conditioning analysis remain open."),
("L-10","Manuscript-to-Artifact Traceability and Synchronization","REQUIRED","PARTIAL","Source-linked manifest generated; semantic and line-level correspondence remains unresolved."),
("L-11","Trust, Axiom, Dependency, and Supply-Chain Audit","REQUIRED","PARTIAL","GitHub/Sigstore provenance checked; external trust root and independent administration absent."),
("L-12","Reproducibility, Independent Review, and Evidence Governance","REQUIRED","PARTIAL","Workflow artifacts retained; independent external review remains absent."),
("L-13","Foundational Consistency, Assumption Satisfiability, and Non-Vacuity Audit","REQUIRED","NOT_RUN","Joint hypothesis satisfiability and non-vacuity require claim-specific models or witnesses."),
("L-14","Mathematical Model Adequacy and Applicability Audit","REQUIRED","NOT_ASSESSED","Paper A concerns a TFIM model; model-to-target adequacy has not been assessed.")]
def canon(x): return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False).encode()
def digest(raw): return hashlib.sha256(raw).hexdigest()
def write_json(path,obj):
 p=Path(path); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(obj,sort_keys=True,indent=2,ensure_ascii=False,allow_nan=False)+"\n",encoding="utf-8")
def file_info(root,rel):
 p=root/rel
 if not p.is_file() or p.is_symlink(): raise ValueError("missing, non-regular or symlinked file: "+rel)
 raw=p.read_bytes(); return {"path":rel,"sha256":digest(raw),"size_bytes":len(raw)}
def run_command(component,commit,output,cwd,inputs,timeout,command):
 if not re.fullmatch(r"[0-9a-f]{40}",commit): raise ValueError("invalid source commit")
 root=Path.cwd().resolve(); work=(root/cwd).resolve()
 if root not in work.parents and work!=root: raise ValueError("working directory escapes repository")
 input_info=[file_info(root,p) for p in inputs]; start=datetime.now(timezone.utc).isoformat()
 try:
  p=subprocess.run(command,cwd=work,capture_output=True,text=True,encoding="utf-8",errors="replace",timeout=timeout,check=False)
  code,out,err=p.returncode,p.stdout,p.stderr
 except subprocess.TimeoutExpired as e:
  code=124; out=e.stdout.decode("utf-8","replace") if isinstance(e.stdout,bytes) else (e.stdout or "")
  err=(e.stderr.decode("utf-8","replace") if isinstance(e.stderr,bytes) else (e.stderr or ""))+"\nTIMEOUT"
 record={"schema_version":"1.0","component_id":component,"component_class":"EXECUTION_EVIDENCE","status":"PASS" if code==0 else ("TIMEOUT" if code==124 else "FAIL"),
 "status_meaning":"Command execution result only; no theorem-level conclusion is implied.","source_commit":commit,"workflow_path":PRODUCER_WORKFLOW,
 "working_directory":cwd,"command":command,"timeout_seconds":timeout,"started_at_utc":start,"finished_at_utc":datetime.now(timezone.utc).isoformat(),
 "exit_code":code,"input_files":input_info,"stdout":out,"stderr":err,"stdout_sha256":digest(out.encode()),"stderr_sha256":digest(err.encode()),
 "mathematical_correctness":"NOT_ASSESSED"}
 write_json(output,record); return record
def parse_claim_rows(text):
 claims=[]
 for line in text.splitlines():
  if not CLAIM_ROW.match(line): continue
  c=[x.strip() for x in line.strip().strip("|").split("|")]
  if len(c)!=7: raise ValueError("malformed Paper A claim row: "+line)
  m=re.search(r"\[Record\]\(([^)]+)\)",c[6])
  if not m: raise ValueError("missing claim record link: "+c[0])
  claims.append({"claim_id":c[0],"original_label":c[1],"claim_type":c[2],"source_locator":c[3].strip("`"),
   "extraction_status":c[4],"registry_verification_status":c[5],"record_path":m.group(1)})
 return claims
def build_traceability(root,commit,expected=15):
 registry=(root/"CLAIM_REGISTRY.md").read_text(encoding="utf-8")
 manifest=(root/"MANUSCRIPT_SOURCE_MANIFEST.md").read_text(encoding="utf-8")
 sec=manifest.split("## 2. Paper A source freeze",1)[1].split("## 3.",1)[0]
 frozen=re.search(r"\|\s*Frozen commit\s*\|\s*[^0-9a-f]*([0-9a-f]{40})",sec)
 if not frozen: raise ValueError("cannot resolve frozen Paper A source commit")
 claims=parse_claim_rows(registry)
 if len(claims)!=expected: raise ValueError(f"expected {expected} Paper A claims, found {len(claims)}")
 ids=[c["claim_id"] for c in claims]
 if len(ids)!=len(set(ids)): raise ValueError("duplicate Paper A claim IDs")
 for c in claims:
  for label,rel in (("record","claims/A/"+c["record_path"].split("/")[-1]),("source_snapshot","source_snapshots/paper-a/"+c["source_locator"])):
   info=file_info(root,rel); c[label+"_path"]=rel; c[label+"_sha256"]=info["sha256"]
  c["candidate_artifact_links"]=[]
  for path,relation,state in CLAIM_ARTIFACTS.get(c["claim_id"],[]):
   info=file_info(root,path); c["candidate_artifact_links"].append({"path":path,"sha256":info["sha256"],"relation":relation,"correspondence":state})
  c["semantic_correspondence"]="NOT_ESTABLISHED"
 lean=["formalization/lean/ConstantLlapoy/PaperA/PerronFrobeniusCore.lean","formalization/lean/ConstantLlapoy/PaperA/StrongCoupling.lean","formalization/lean/ConstantLlapoy/PaperA/WeakCoupling.lean","formalization/lean/ConstantLlapoy/PaperA/ZeroEigenvalueEntropy.lean","formalization/lean/ConstantLlapoy/PaperA/HamiltonianEncoding.lean"]
 diags=["working/paper-a/dicke_even_basis_exact_diagnostic.py","working/paper-a/finite_n_strong_coupling_exact_diagnostic.py","working/paper-a/edge_response_finite_difference_diagnostic.py","working/paper-a/edge_response_weak_coupling_diagnostic.py"]
 return {"schema_version":"1.0","component_id":"PAPER_A_CLAIM_TRACEABILITY","status":"PASS",
  "status_meaning":"All registered Paper A rows, records and frozen local snapshots were located and hashed.",
  "source_commit":commit,"frozen_upstream_source_commit":frozen.group(1),"claim_count":len(claims),"claims":claims,
  "lean_modules":[file_info(root,p) for p in lean],"diagnostic_sources":[file_info(root,p) for p in diags],
  "semantic_correspondence":"NOT_ESTABLISHED","line_level_claim_to_declaration_mapping":"NOT_COMPLETE","mathematical_correctness":"NOT_ASSESSED"}
def build_layer_plan(root,commit,trace_path,evidence_paths):
 trace=json.loads((root/trace_path).read_text(encoding="utf-8"))
 if trace.get("source_commit")!=commit or trace.get("claim_count")!=15: raise ValueError("stale or incomplete claim traceability")
 evidence=[]
 for rel in evidence_paths:
  info=file_info(root,rel); obj=json.loads((root/rel).read_text(encoding="utf-8"))
  if obj.get("source_commit")!=commit or obj.get("status") not in {"PASS","FAIL","TIMEOUT","INCONCLUSIVE"}: raise ValueError("evidence record is missing, stale or has invalid status: "+rel)
  evidence.append({**info,"component_id":obj.get("component_id"),"execution_status":obj.get("status")})
 states={x["component_id"]:x["execution_status"] for x in evidence}
 layers=[{"layer_id":i,"name":n,"applicability":a,"assessment_status":s,"rationale":r} for i,n,a,s,r in LAYERS]
 layer_owner={"L-04":["PAPER_A_LEAN_BUILD"],"L-06":["PAPER_A_DICKE_EXACT_DIAGNOSTIC","PAPER_A_STRONG_COUPLING_EXACT_DIAGNOSTIC"],"L-07":["PAPER_A_DICKE_EXACT_DIAGNOSTIC","PAPER_A_STRONG_COUPLING_EXACT_DIAGNOSTIC"],"L-09":["PAPER_A_FINITE_DIFFERENCE_DIAGNOSTIC","PAPER_A_WEAK_COUPLING_NUMERICAL_DIAGNOSTIC"]}
 for row in layers:
  observed_states=[states.get(cid) for cid in layer_owner.get(row["layer_id"],[])]
  if "FAIL" in observed_states:
   row["assessment_status"]="FAILED"
   row["rationale"] += " The corresponding executed component returned a nonzero exit code."
  elif any(x in {"TIMEOUT","INCONCLUSIVE"} for x in observed_states):
   row["assessment_status"]="INCONCLUSIVE"
   row["rationale"] += " The corresponding executed component did not reach a conclusive successful result."
 return {"schema_version":"1.0","component_id":"PAPER_A_14_LAYER_TRIAL_PLAN","status":"PASS",
  "status_meaning":"All 14 layer rows were assessed for this trial plan; individual layer assessments are not thereby passed.",
  "source_commit":commit,"claim_count":15,"layer_count":14,"layers":layers,"input_evidence":evidence,
  "overall_paper_status":"NOT_VERIFIED","mathematical_correctness":"NOT_ASSESSED","external_trust_root":"NOT_ACTIVE","independent_external_review":"NOT_COMPLETED"}
def verify_bundle(commit,run_id,attempt,policy_path,pin,evidence_paths,output):
 if not re.fullmatch(r"[0-9a-f]{40}",commit) or type(run_id)!=int or run_id<=0 or type(attempt)!=int or attempt<=0: raise ValueError("invalid source commit, producer run ID or attempt")
 root=Path.cwd().resolve(); policy_file=root/policy_path; pbytes=policy_file.read_bytes(); pp=json.loads(pbytes.decode("utf-8"))
 components=[]; ids=[]
 for rel in evidence_paths:
  raw=(root/rel).read_bytes(); rec=json.loads(raw.decode("utf-8")); cid=rec.get("component_id")
  if not isinstance(cid,str) or not cid or cid in ids: raise ValueError("invalid or duplicate component ID")
  if rec.get("source_commit")!=commit or rec.get("status") not in {"PASS","FAIL","TIMEOUT","INCONCLUSIVE"}: raise ValueError("stale or invalid evidence status: "+rel)
  ids.append(cid); sha=digest(raw)
  components.append({"component_id":cid,"status":rec["status"],"evidence_base64":base64.b64encode(raw).decode(),"evidence_sha256":sha,
   "provenance":{"receipt_schema_version":"2.0","subject_sha256":sha,"source_commit":commit,"attestation_run_id":run_id,"attestation_run_attempt":attempt,"attestation_workflow_revision":commit}})
 required={"PAPER_A_LEAN_BUILD","PAPER_A_DICKE_EXACT_DIAGNOSTIC","PAPER_A_STRONG_COUPLING_EXACT_DIAGNOSTIC","PAPER_A_FINITE_DIFFERENCE_DIAGNOSTIC","PAPER_A_WEAK_COUPLING_NUMERICAL_DIAGNOSTIC","PAPER_A_CLAIM_TRACEABILITY","PAPER_A_14_LAYER_TRIAL_PLAN"}
 if set(ids)!=required: raise ValueError("required component set mismatch")
 policy={"schema_version":"1.0","claim_id":"PAPER-A-FIRST-14-LAYER-TRIAL","policy_revision":commit,"required_components":sorted(required)}
 bundle={"schema_version":"1.0","claim_id":policy["claim_id"],"source_commit":commit,"policy_revision":commit,"components":components}
 auth=authenticate_components(canon(policy),pbytes,pp,bundle,commit,pin); result=aggregate(policy,bundle,commit,auth)
 report={"schema_version":"1.0","status":("PAPER_A_COMPONENT_EVIDENCE_PIPELINE_VERIFIED" if result["status"]=="ACCEPTED" else
    ("PAPER_A_EVIDENCE_BUNDLE_AUTHENTICATED_WITH_FAILED_CHECKS" if result["status"]=="REJECTED" else
     "PAPER_A_EVIDENCE_BUNDLE_AUTHENTICATED_BUT_INCONCLUSIVE")),
  "status_scope":"EXECUTION_ARTIFACT_COMPLETENESS_AND_GITHUB_SIGSTORE_PROVENANCE_ONLY","source_commit":commit,"producer_run_id":run_id,"producer_run_attempt":attempt,
  "component_aggregation":result,"execution_outcome":result["status"],"paper_a_claims_verified":False,"overall_paper_status":"NOT_VERIFIED","external_trust_root":"NOT_ACTIVE",
  "provenance_policy_pin_origin":"SAME_REPOSITORY_CHECKOUT_NOT_AN_INDEPENDENT_TRUST_ANCHOR","independent_external_review":"NOT_COMPLETED",
  "residual_limitations":["Attestations authenticate evidence bytes, not mathematical truth.","Claim traceability is source-linked but not semantic or line-level correspondence.",
  "Lean covers selected obligations only; major Paper A obligations remain open.","Numerical diagnostics are not proofs and do not establish uniform asymptotics.",
  "External trust root and separately administered trusted builder are not active."]}
 write_json(output,report)
 return report
def main(argv=None):
 p=argparse.ArgumentParser(description=__doc__); s=p.add_subparsers(dest="mode",required=True)
 r=s.add_parser("run"); r.add_argument("--component",required=True); r.add_argument("--source-commit",required=True); r.add_argument("--output",required=True); r.add_argument("--cwd",default="."); r.add_argument("--input",action="append",default=[]); r.add_argument("--timeout",type=int,default=600); r.add_argument("command",nargs=argparse.REMAINDER)
 t=s.add_parser("traceability"); t.add_argument("--source-commit",required=True); t.add_argument("--output",required=True); t.add_argument("--expected-claims",type=int,default=15)
 l=s.add_parser("layer-plan"); l.add_argument("--source-commit",required=True); l.add_argument("--traceability",required=True); l.add_argument("--evidence",action="append",required=True); l.add_argument("--output",required=True)
 v=s.add_parser("verify"); v.add_argument("--source-commit",required=True); v.add_argument("--run-id",type=int,required=True); v.add_argument("--run-attempt",type=int,required=True); v.add_argument("--provenance-policy",required=True); v.add_argument("--expected-provenance-policy-sha256",required=True); v.add_argument("--evidence",action="append",required=True); v.add_argument("--output",required=True)
 a=p.parse_args(argv)
 try:
  if a.mode=="run":
   cmd=a.command[1:] if a.command and a.command[0]=="--" else a.command
   if not cmd: raise ValueError("command after -- required")
   x=run_command(a.component,a.source_commit,a.output,a.cwd,a.input,a.timeout,cmd); print(json.dumps({"component_id":x["component_id"],"status":x["status"],"exit_code":x["exit_code"]})); return 0 if x["status"]=="PASS" else 1
  if a.mode=="traceability":
   x=build_traceability(Path.cwd().resolve(),a.source_commit,a.expected_claims); write_json(a.output,x); print(json.dumps({"status":x["status"],"claim_count":x["claim_count"]})); return 0
  if a.mode=="layer-plan":
   x=build_layer_plan(Path.cwd().resolve(),a.source_commit,a.traceability,a.evidence); write_json(a.output,x); print(json.dumps({"status":x["status"],"layer_count":x["layer_count"]})); return 0
  x=verify_bundle(a.source_commit,a.run_id,a.run_attempt,a.provenance_policy,a.expected_provenance_policy_sha256,a.evidence,a.output); print(json.dumps({"status":x["status"],"source_commit":x["source_commit"]})); return 0
 except (ValueError,OSError,json.JSONDecodeError,AggregationError) as e:
  print(json.dumps({"status":"ERROR","error":str(e)},sort_keys=True),file=sys.stderr); return 2
if __name__=="__main__": raise SystemExit(main())
