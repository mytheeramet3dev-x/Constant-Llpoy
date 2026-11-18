"""End-to-end policy-activation gate tests; keys are ephemeral test fixtures."""
import base64, copy, hashlib, json, os, subprocess, sys, tempfile, unittest
from pathlib import Path
from policy_activation_gate import ActivationError, canonical, digest, evaluate_active_policy, verify_activation
from status_aggregator import aggregate

NOW = 1800000000
COMMIT = "a" * 40
POLICY_REV = "b" * 40
VERIFIER_REV = "c" * 40

def comp(cid, payload):
    h = hashlib.sha256(payload).hexdigest()
    run_id,attempt=(123,1) if cid=="C1" else (456,2)
    return {"component_id":cid,"status":"PASS","evidence_base64":base64.b64encode(payload).decode(),
      "evidence_sha256":h,"provenance":{"receipt_schema_version":"2.0","subject_sha256":h,"source_commit":COMMIT,
      "attestation_run_id":run_id,"attestation_run_attempt":attempt,"attestation_workflow_revision":COMMIT}}

class GateTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
    cls.tmp=tempfile.TemporaryDirectory(); cls.root=Path(cls.tmp.name); cls.private={}
    reviewers=[]
    for rid in ("R1","R2","R3"):
      priv=cls.root/f"{rid}.key"; pub=cls.root/f"{rid}.pub"
      subprocess.run(["openssl","genpkey","-algorithm","ED25519","-out",str(priv)],check=True,capture_output=True)
      subprocess.run(["openssl","pkey","-in",str(priv),"-pubout","-out",str(pub)],check=True,capture_output=True)
      cls.private[rid]=priv
      reviewers.append({"reviewer_id":rid,"public_key_pem_base64":base64.b64encode(pub.read_bytes()).decode()})
    cls.authorities=canonical({"schema_version":"1.0","authority_set_id":"external-authority-test","threshold":2,"reviewers":reviewers})
    cls.policy=canonical({"schema_version":"1.0","claim_id":"CLAIM-A","policy_revision":POLICY_REV,"required_components":["C1","C2"]})
    cls.policy_obj=__import__("json").loads(cls.policy)
    cls.provenance_policy=canonical({"schema_version":"1.0","repository":"mytheeramet3dev-x/Constant-Llpoy",
      "repository_id":1460417275,
      "signer_workflow":"mytheeramet3dev-x/Constant-Llpoy/.github/workflows/component-evidence.yml",
      "source_ref":"refs/heads/main","oidc_issuer":"https://token.actions.githubusercontent.com",
      "predicate_type":"https://slsa.dev/provenance/v1","require_verified_timestamps":True,
      "deny_self_hosted_runners":True,"gh_cli_version":"2.103.3"})

 @classmethod
 def tearDownClass(cls): cls.tmp.cleanup()
 def make_record(self, status="ACTIVE", sequence=4, policy_bytes=None, authority_bytes=None, expires=NOW+1000, authority_digest_override=None):
    pb=policy_bytes or self.policy; ab=authority_bytes or self.authorities
    record={"schema_version":"1.0","policy_id":"meta-policy-v1","policy_sha256":digest(pb),
      "sequence":sequence,"authority_set_sha256":authority_digest_override or digest(ab),"status":status,
      "issued_at":str(NOW-10),"expires_at":str(expires)}
    msg=canonical(record); msgfile=self.root/"message"; msgfile.write_bytes(msg); signatures=[]
    for rid in ("R1","R2"):
      sig=self.root/"sig"
      subprocess.run(["openssl","pkeyutl","-sign","-inkey",str(self.private[rid]),"-rawin",
        "-in",str(msgfile),"-out",str(sig)],check=True,capture_output=True)
      signatures.append({"reviewer_id":rid,"signature_base64":base64.b64encode(sig.read_bytes()).decode()})
    return canonical({**record,"signatures":signatures})
 def args(self, activation=None, **overrides):
    values=dict(expected_authority_sha256=digest(self.authorities),
      expected_activation_sha256=digest(activation or self.make_record()),
      expected_policy_id="meta-policy-v1",expected_policy_sequence=4,now_epoch=NOW)
    values.update(overrides); return values
 def bundle(self):
    return {"schema_version":"1.0","claim_id":"CLAIM-A","source_commit":COMMIT,"policy_revision":POLICY_REV,
      "components":[comp("C1",b"one"),comp("C2",b"two")]}
 def authenticated(self,bundle):
    result={}
    for c in bundle["components"]:
      r=c["provenance"]
      result[c["component_id"]]={"subject_sha256":r["subject_sha256"],"source_commit":r["source_commit"],
        "attestation_run_id":r["attestation_run_id"],"attestation_run_attempt":r["attestation_run_attempt"],
        "attestation_workflow_revision":r["attestation_workflow_revision"],"repository_id":1460417275,
        "signer_workflow":"mytheeramet3dev-x/Constant-Llpoy/.github/workflows/component-evidence.yml",
        "provenance_policy_sha256":digest(self.provenance_policy),"verified_attestation_count":1}
    return result
 def test_active_policy_without_authenticated_component_attestations_is_inconclusive(self):
    activation=self.make_record()
    r=evaluate_active_policy(self.policy,self.policy_obj,self.authorities,activation,self.bundle(),COMMIT,**self.args(activation))
    self.assertEqual(r["status"],"INCONCLUSIVE")
    self.assertEqual(r["active_policy"]["status"],"POLICY_ACTIVE")
 def test_active_policy_with_authenticated_component_attestations_is_accepted(self):
    activation=self.make_record(); bundle=self.bundle()
    r=evaluate_active_policy(self.policy,self.policy_obj,self.authorities,activation,bundle,COMMIT,
      **self.args(activation),authenticated_receipts=self.authenticated(bundle))
    self.assertEqual(r["status"],"POLICY_ACTIVE_AND_COMPONENT_PROVENANCE_AUTHENTICATED")
 def test_authorized_but_not_activated_never_accepts(self):
    activation=self.make_record(status="AUTHORIZED")
    with self.assertRaisesRegex(ActivationError,"not marked ACTIVE"):
      evaluate_active_policy(self.policy,self.policy_obj,self.authorities,activation,self.bundle(),COMMIT,**self.args(activation))
 def test_missing_external_authority_pin_rejected(self):
    activation=self.make_record()
    with self.assertRaisesRegex(ActivationError,"authority pin"):
      verify_activation(self.policy,self.policy_obj,self.authorities,activation,**self.args(activation,expected_authority_sha256=""))
 def test_missing_external_activation_pin_rejected(self):
    activation=self.make_record()
    with self.assertRaisesRegex(ActivationError,"active-policy pin"):
      verify_activation(self.policy,self.policy_obj,self.authorities,activation,**self.args(activation,expected_activation_sha256=""))
 def test_authority_pin_mismatch_rejected(self):
    wrong_pin="0"*64
    activation=self.make_record(authority_digest_override=wrong_pin)
    with self.assertRaisesRegex(ActivationError,"differs from external pin"):
      verify_activation(self.policy,self.policy_obj,self.authorities,activation,**self.args(activation,expected_authority_sha256=wrong_pin))
 def test_activation_record_pin_mismatch_rejected(self):
    activation=self.make_record()
    with self.assertRaisesRegex(ActivationError,"activation-record digest"):
      verify_activation(self.policy,self.policy_obj,self.authorities,activation,**self.args(activation,expected_activation_sha256="0"*64))
 def test_policy_bytes_tamper_rejected(self):
    activation=self.make_record()
    with self.assertRaisesRegex(ActivationError,"policy digest"):
      verify_activation(self.policy+b" ",self.policy_obj,self.authorities,activation,**self.args(activation))
 def test_separately_supplied_policy_object_cannot_diverge_from_pinned_bytes(self):
    activation=self.make_record()
    altered=copy.deepcopy(self.policy_obj); altered["claim_id"]="ATTACKER-CLAIM"
    with self.assertRaisesRegex(ActivationError,"does not match"):
      verify_activation(self.policy,altered,self.authorities,activation,**self.args(activation))
 def test_wrong_policy_id_rejected(self):
    activation=self.make_record()
    with self.assertRaisesRegex(ActivationError,"policy ID"):
      verify_activation(self.policy,self.policy_obj,self.authorities,activation,**self.args(activation,expected_policy_id="other"))
 def test_rollback_or_sequence_replay_rejected(self):
    activation=self.make_record(sequence=3)
    with self.assertRaisesRegex(ActivationError,"sequence mismatch"):
      verify_activation(self.policy,self.policy_obj,self.authorities,activation,**self.args(activation))
 def test_expired_activation_rejected(self):
    activation=self.make_record(expires=NOW-1)
    with self.assertRaisesRegex(ActivationError,"validity interval"):
      verify_activation(self.policy,self.policy_obj,self.authorities,activation,**self.args(activation))
 def test_wrong_authority_binding_rejected(self):
    activation=self.make_record(authority_digest_override="0"*64)
    with self.assertRaisesRegex(ActivationError,"authority-set digest mismatch"):
      verify_activation(self.policy,self.policy_obj,self.authorities,activation,**self.args(activation))
 def test_boolean_expected_sequence_rejected(self):
    activation=self.make_record(sequence=1)
    with self.assertRaisesRegex(ActivationError,"positive integer"):
      verify_activation(self.policy,self.policy_obj,self.authorities,activation,
        **self.args(activation,expected_policy_sequence=True))
 def test_bad_threshold_signature_rejected(self):
    activation=self.make_record()
    record=__import__("json").loads(activation); record["signatures"]=record["signatures"][:1]
    # The record pin is recomputed only to isolate threshold enforcement.
    raw=canonical(record)
    with self.assertRaisesRegex(ActivationError,"threshold not met"):
      verify_activation(self.policy,self.policy_obj,self.authorities,raw,**self.args(raw,expected_activation_sha256=digest(raw)))
 def test_invalid_signature_rejected(self):
    activation=self.make_record()
    record=__import__("json").loads(activation); record["signatures"][0]["signature_base64"]=base64.b64encode(b"x"*64).decode()
    raw=canonical(record)
    with self.assertRaisesRegex(ActivationError,"invalid activation signature"):
      verify_activation(self.policy,self.policy_obj,self.authorities,raw,**self.args(raw,expected_activation_sha256=digest(raw)))
 def test_nonaccepted_component_stays_nonaccepted_after_activation(self):
    activation=self.make_record(); bundle=self.bundle(); bundle["components"][0]["status"]="INCONCLUSIVE"
    r=evaluate_active_policy(self.policy,self.policy_obj,self.authorities,activation,bundle,COMMIT,**self.args(activation))
    self.assertEqual(r["status"],"INCONCLUSIVE")
 def test_policy_revision_and_commit_still_checked_by_existing_aggregator(self):
    activation=self.make_record(); bundle=self.bundle(); bundle["policy_revision"]="d"*40
    r=evaluate_active_policy(self.policy,self.policy_obj,self.authorities,activation,bundle,COMMIT,**self.args(activation))
    self.assertEqual(r["status"],"INCONCLUSIVE")
 def test_order_invariance_of_component_bundle(self):
    activation=self.make_record(); bundle=self.bundle()
    first=evaluate_active_policy(self.policy,self.policy_obj,self.authorities,activation,bundle,COMMIT,**self.args(activation))
    bundle["components"].reverse()
    second=evaluate_active_policy(self.policy,self.policy_obj,self.authorities,activation,bundle,COMMIT,**self.args(activation))
    self.assertEqual(first["status"],second["status"])
 def test_duplicate_component_does_not_escalate(self):
    activation=self.make_record(); bundle=self.bundle(); bundle["components"].append(copy.deepcopy(bundle["components"][0]))
    r=evaluate_active_policy(self.policy,self.policy_obj,self.authorities,activation,bundle,COMMIT,**self.args(activation))
    self.assertEqual(r["status"],"INCONCLUSIVE")


 def _run_cli(self, policy_bytes=None, expected_activation=None, expected_provenance_pin=None):
    activation=self.make_record()
    inputs={"policy.json":policy_bytes or self.policy,"authority.json":self.authorities,
      "activation.json":activation,"bundle.json":canonical(self.bundle()),
      "provenance-policy.json":self.provenance_policy}
    paths={}
    for name,raw in inputs.items():
      path=self.root/name; path.write_bytes(raw); paths[name]=path
    bindir=self.root/"fake-gh"; bindir.mkdir(exist_ok=True)
    gh=bindir/"gh"
    script = """#!/usr/bin/env python3
import sys,json,hashlib,pathlib
if sys.argv[1:]==["version"]:
 print("gh version 2.103.3 (test)"); raise SystemExit(0)
if sys.argv[1:3]==["attestation","verify"]:
 path=pathlib.Path(sys.argv[3]); cid=path.name.split(".")[0]
 runs={"C1":(123,1),"C2":(456,2)}; run_id,attempt=runs[cid]
 digest=hashlib.sha256(path.read_bytes()).hexdigest()
 repo="mytheeramet3dev-x/Constant-Llpoy"; commit="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
 cert={"sourceRepositoryIdentifier":"1460417275","sourceRepositoryRef":"refs/heads/main",
       "sourceRepositoryDigest":commit,"buildSignerDigest":commit}
 statement={"predicateType":"https://slsa.dev/provenance/v1",
   "subject":[{"name":path.name,"digest":{"sha256":digest}}],
   "predicate":{"runDetails":{"metadata":{"invocationId":f"https://github.com/{repo}/actions/runs/{run_id}/attempts/{attempt}"}}}}
 print(json.dumps([{"verificationResult":{"signature":{"certificate":cert},
   "verifiedTimestamps":[{"kind":"rekor","integratedTime":1}],"statement":statement}}]))
 raise SystemExit(0)
raise SystemExit(2)
"""
    gh.write_text(script,encoding="utf-8"); gh.chmod(0o755)
    cmd=[sys.executable,str(Path(__file__).with_name("policy_activation_gate.py")),
      "--policy",str(paths["policy.json"]),"--authority-set",str(paths["authority.json"]),
      "--activation-record",str(paths["activation.json"]),"--bundle",str(paths["bundle.json"]),
      "--provenance-policy",str(paths["provenance-policy.json"]),
      "--expected-provenance-policy-sha256",expected_provenance_pin if expected_provenance_pin is not None else digest(self.provenance_policy),
      "--expected-commit",COMMIT,"--expected-authority-sha256",digest(self.authorities),
      "--expected-activation-sha256",expected_activation if expected_activation is not None else digest(activation),
      "--expected-policy-id","meta-policy-v1","--expected-policy-sequence","4","--now-epoch",str(NOW)]
    env=dict(os.environ); env["PATH"]=str(bindir)+os.pathsep+env.get("PATH","")
    return subprocess.run(cmd,capture_output=True,text=True,env=env)
 def test_cli_executes_pinned_activation_and_component_attestations(self):
    result=self._run_cli()
    self.assertEqual(result.returncode,0,result.stderr+result.stdout)
    self.assertEqual(json.loads(result.stdout)["status"],"POLICY_ACTIVE_AND_COMPONENT_PROVENANCE_AUTHENTICATED")
 def test_cli_missing_activation_pin_fails_closed(self):
    result=self._run_cli(expected_activation="")
    self.assertEqual(result.returncode,2)
    self.assertEqual(json.loads(result.stdout)["status"],"ERROR")
 def test_cli_missing_component_provenance_pin_fails_closed(self):
    result=self._run_cli(expected_provenance_pin="")
    self.assertEqual(result.returncode,2)
    self.assertIn("provenance-policy pin",json.loads(result.stdout)["error"])
 def test_cli_rejects_duplicate_json_keys(self):
    duplicate=b'{"schema_version":"1.0","schema_version":"1.0","claim_id":"CLAIM-A","policy_revision":"'+POLICY_REV.encode()+b'","required_components":["C1","C2"]}'
    result=self._run_cli(policy_bytes=duplicate)
    self.assertEqual(result.returncode,2)
    self.assertIn("duplicate JSON key",json.loads(result.stdout)["error"])
 def test_cli_rejects_symlink_inputs(self):
    activation=self.make_record()
    target=self.root/"real-policy.json"; target.write_bytes(self.policy)
    link=self.root/"linked-policy.json"
    try: link.symlink_to(target)
    except OSError: self.skipTest("symlink creation unavailable")
    self._run_cli()
    cmd=[sys.executable,str(Path(__file__).with_name("policy_activation_gate.py")),
      "--policy",str(link),"--authority-set",str(self.root/"authority.json"),
      "--activation-record",str(self.root/"activation.json"),"--bundle",str(self.root/"bundle.json"),
      "--provenance-policy",str(self.root/"provenance-policy.json"),
      "--expected-provenance-policy-sha256",digest(self.provenance_policy),
      "--expected-commit",COMMIT,"--expected-authority-sha256",digest(self.authorities),
      "--expected-activation-sha256",digest(activation),"--expected-policy-id","meta-policy-v1",
      "--expected-policy-sequence","4","--now-epoch",str(NOW)]
    env=dict(os.environ); env["PATH"]=str(self.root/"fake-gh")+os.pathsep+env.get("PATH","")
    denied=subprocess.run(cmd,capture_output=True,text=True,env=env)
    self.assertEqual(denied.returncode,2)
    self.assertIn("symlinks are not accepted",json.loads(denied.stdout)["error"])

if __name__ == "__main__": unittest.main(verbosity=2)
