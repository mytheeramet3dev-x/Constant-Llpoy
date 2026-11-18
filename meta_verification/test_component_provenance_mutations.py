#!/usr/bin/env python3
"""Selected mutation-adequacy tests for component provenance authentication."""
import py_compile, shutil, subprocess, sys, tempfile, unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parent
FILES=["component_provenance_authenticator.py","verify_signed_provenance.py","status_aggregator.py",
       "test_component_provenance_authenticator.py","test_status_aggregator.py"]
MUTANTS={
 "bypass_external_provenance_policy_pin":(
  "require(actual_policy_sha == expected_provenance_policy_sha256,",
  "require(True,"),
 "bypass_component_evidence_digest":(
  'require(component.get("evidence_sha256") == subject_sha,',
  "require(True,"),
 "bypass_receipt_run_id_type":(
  "require(type(run_id) is int and run_id > 0,",
  "require(True,"),
 "bypass_receipt_run_attempt_type":(
  "require(type(attempt) is int and attempt > 0,",
  "require(True,"),
 "bypass_receipt_workflow_revision":(
  'require(receipt["attestation_workflow_revision"] == expected_commit,',
  "require(True,"),
 "bypass_gh_verification_failure":(
  "require(completed.returncode == 0,",
  "require(True,"),
 "bypass_signer_workflow_constraint":(
  '"--signer-workflow", p["signer_workflow"],',
  '"--signer-workflow", p["repository"],'),
 "bypass_slsa_invocation_id_binding":(
  "require(metadata.get(\"invocationId\") == expected_invocation_id,",
  "require(True,"),
 "bypass_attestation_subject_digest":(
  'if isinstance(digest, dict) and digest.get("sha256") == expected_digest:',
  "if isinstance(digest, dict):"),
 "bypass_authentication_required_by_aggregator":(
  "receipt_valid = (auth_valid and receipt[\"subject_sha256\"] == actual",
  "receipt_valid = (True and receipt[\"subject_sha256\"] == actual"),
}

class ComponentProvenanceMutationTests(unittest.TestCase):
 def test_each_selected_authentication_mutant_is_killed(self):
  sources={name:(ROOT/name).read_text(encoding="utf-8") for name in FILES}
  for mutant,(old,new) in MUTANTS.items():
   target_name=("verify_signed_provenance.py" if "invocation_id" in mutant or "attestation_subject" in mutant
                else "status_aggregator.py" if "aggregator" in mutant else "component_provenance_authenticator.py")
   with self.subTest(mutant=mutant), tempfile.TemporaryDirectory() as td:
    work=Path(td)
    for name in FILES:
     if name!="test_component_provenance_authenticator.py":
      shutil.copy2(ROOT/name,work/name)
    source=sources[target_name]
    if source.count(old)!=1:
     self.fail(f"mutation anchor for {mutant} occurs {source.count(old)} times")
    changed=source.replace(old,new,1)
    target=work/target_name; target.write_text(changed,encoding="utf-8")
    py_compile.compile(str(target),doraise=True)
    shutil.copy2(ROOT/"test_component_provenance_authenticator.py",work/"test_component_provenance_authenticator.py")
    shutil.copy2(ROOT/"test_status_aggregator.py",work/"test_status_aggregator.py")
    run=subprocess.run([sys.executable,"-m","unittest","-v","test_component_provenance_authenticator","test_status_aggregator"],
      cwd=work,text=True,capture_output=True,timeout=60,check=False)
    output=run.stdout+run.stderr
    self.assertNotEqual(run.returncode,0,f"surviving mutant: {mutant}\n{output}")
    self.assertIn("FAILED (",output,f"not assertion-driven: {mutant}\n{output}")
    self.assertIn("Ran ",output,f"no tests executed for {mutant}")
    self.assertNotIn("ImportError",output)
    self.assertNotIn("SyntaxError",output)
    print(f"COMPONENT PROVENANCE MUTANT KILLED: {mutant}")

if __name__=="__main__":
 unittest.main(verbosity=2)
