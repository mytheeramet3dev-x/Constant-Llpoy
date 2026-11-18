"""End-to-end policy-activation gate tests; keys are ephemeral test fixtures."""
import base64, copy, hashlib, subprocess, tempfile, unittest
from pathlib import Path
from policy_activation_gate import ActivationError, canonical, digest, evaluate_active_policy, verify_activation
from status_aggregator import aggregate

NOW = 1800000000
COMMIT = "a" * 40
POLICY_REV = "b" * 40
VERIFIER_REV = "c" * 40

def comp(cid, payload):
    h = hashlib.sha256(payload).hexdigest()
    return {"component_id":cid,"status":"PASS","evidence_base64":base64.b64encode(payload).decode(),
      "evidence_sha256":h,"provenance":{"status":"VERIFIED","subject_sha256":h,"source_commit":COMMIT,
      "verifier_run_id":123,"verifier_run_attempt":1,"verifier_revision":VERIFIER_REV}}

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
 @classmethod
 def tearDownClass(cls): cls.tmp.cleanup()
 def make_record(self, status="ACTIVE", sequence=4, policy_bytes=None, authority_bytes=None, expires=NOW+1000):
    pb=policy_bytes or self.policy; ab=authority_bytes or self.authorities
    record={"schema_version":"1.0","policy_id":"meta-policy-v1","policy_sha256":digest(pb),
      "sequence":sequence,"authority_set_sha256":digest(ab),"status":status,
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
 def test_valid_active_policy_gates_structural_acceptance(self):
    activation=self.make_record()
    r=evaluate_active_policy(self.policy,self.policy_obj,self.authorities,activation,self.bundle(),COMMIT,**self.args(activation))
    self.assertEqual(r["status"],"POLICY_ACTIVE_AND_BUNDLE_STRUCTURALLY_ACCEPTED")
    self.assertEqual(r["active_policy"]["status"],"POLICY_ACTIVE")
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
    activation=self.make_record()
    with self.assertRaisesRegex(ActivationError,"authority-set digest"):
      verify_activation(self.policy,self.policy_obj,self.authorities,activation,**self.args(activation,expected_authority_sha256="0"*64))
 def test_activation_record_pin_mismatch_rejected(self):
    activation=self.make_record()
    with self.assertRaisesRegex(ActivationError,"activation-record digest"):
      verify_activation(self.policy,self.policy_obj,self.authorities,activation,**self.args(activation,expected_activation_sha256="0"*64))
 def test_policy_bytes_tamper_rejected(self):
    activation=self.make_record()
    with self.assertRaisesRegex(ActivationError,"policy digest"):
      verify_activation(self.policy+b"x",self.policy_obj,self.authorities,activation,**self.args(activation))
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
    activation=self.make_record()
    changed=activation.replace(digest(self.authorities).encode(),b"0"*64)
    with self.assertRaises(ActivationError):
      verify_activation(self.policy,self.policy_obj,self.authorities,changed,**self.args(activation))
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

if __name__ == "__main__": unittest.main(verbosity=2)
