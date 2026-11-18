"""Adversarial tests for threshold-signed policy change control."""
import base64,copy,subprocess,tempfile,unittest
from pathlib import Path
from policy_change_control import PolicyChangeError,canonical_json,sha256,verify_policy_change
NOW=1800000000
PARENT="a"*64
POLICY_ID="constant-llpoy-meta-policy"
def run(cmd): return subprocess.run(cmd,check=True,capture_output=True,text=True)
class Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.td=tempfile.TemporaryDirectory(); cls.root=Path(cls.td.name); cls.keys={}; reviewers=[]
  for rid in ("reviewer-A","reviewer-B","reviewer-C"):
   priv=cls.root/f"{rid}.priv"; pub=cls.root/f"{rid}.pub"
   run(["openssl","genpkey","-algorithm","ED25519","-out",str(priv)])
   run(["openssl","pkey","-in",str(priv),"-pubout","-out",str(pub)])
   cls.keys[rid]=priv
   reviewers.append({"reviewer_id":rid,"public_key_pem_base64":base64.b64encode(pub.read_bytes()).decode()})
  cls.authorities={"schema_version":"1.0","authority_set_id":"independent-policy-authority-v1","threshold":2,"reviewers":reviewers}
  cls.authority_bytes=canonical_json(cls.authorities); cls.authority_digest=sha256(cls.authority_bytes)
  cls.policy=canonical_json({"policy_id":POLICY_ID,"required_components":["A","B"],"rule":"all-pass"})
  cls.base={"schema_version":"1.0","policy_id":POLICY_ID,"sequence":7,"parent_policy_sha256":PARENT,
    "policy_sha256":sha256(cls.policy),"issued_at":str(NOW-100),"expires_at":str(NOW+1000)}
 @classmethod
 def tearDownClass(cls): cls.td.cleanup()
 def signed(self,ids=("reviewer-A","reviewer-B"),base=None):
  p=copy.deepcopy(self.base if base is None else base); msg=canonical_json(p); sigs=[]
  msgfile=self.root/"message"; msgfile.write_bytes(msg)
  for rid in ids:
   sig=self.root/"signature"
   run(["openssl","pkeyutl","-sign","-inkey",str(self.keys[rid]),"-rawin","-in",str(msgfile),"-out",str(sig)])
   sigs.append({"reviewer_id":rid,"signature_base64":base64.b64encode(sig.read_bytes()).decode()})
  return {**p,"signatures":sigs}
 def verify(self,p=None,**kw):
  args=dict(expected_authority_sha256=self.authority_digest,expected_policy_id=POLICY_ID,
   expected_parent_policy_sha256=PARENT,expected_sequence=7,now_epoch=NOW); args.update(kw)
  return verify_policy_change(self.policy,self.signed() if p is None else p,self.authority_bytes,**args)
 def test_valid_two_of_three(self):
  r=self.verify(); self.assertEqual(r["status"],"POLICY_CHANGE_AUTHORIZED"); self.assertIn("NOT_ACTIVATED",r["activation_status"])
 def test_below_threshold(self):
  with self.assertRaisesRegex(PolicyChangeError,"insufficient"): self.verify(self.signed(("reviewer-A",)))
 def test_duplicate_signer(self):
  p=self.signed(("reviewer-A",)); p["signatures"].append(copy.deepcopy(p["signatures"][0]))
  with self.assertRaisesRegex(PolicyChangeError,"duplicate"): self.verify(p)
 def test_unauthorized_signer(self):
  p=self.signed(("reviewer-A",)); p["signatures"][0]["reviewer_id"]="outsider"
  with self.assertRaisesRegex(PolicyChangeError,"unauthorized"): self.verify(p)
 def test_invalid_signature(self):
  p=self.signed(); p["signatures"][0]["signature_base64"]=base64.b64encode(b"x"*64).decode()
  with self.assertRaisesRegex(PolicyChangeError,"invalid signature"): self.verify(p)
 def test_modified_policy_bytes(self):
  with self.assertRaisesRegex(PolicyChangeError,"content digest"):
   verify_policy_change(self.policy+b"x",self.signed(),self.authority_bytes,
    expected_authority_sha256=self.authority_digest,expected_policy_id=POLICY_ID,
    expected_parent_policy_sha256=PARENT,expected_sequence=7,now_epoch=NOW)
 def test_external_authority_pin_mismatch(self):
  with self.assertRaisesRegex(PolicyChangeError,"external pin"): self.verify(expected_authority_sha256="0"*64)
 def test_wrong_parent(self):
  with self.assertRaisesRegex(PolicyChangeError,"parent"): self.verify(expected_parent_policy_sha256="b"*64)
 def test_wrong_sequence(self):
  with self.assertRaisesRegex(PolicyChangeError,"sequence"): self.verify(expected_sequence=8)
 def test_expired(self):
  p=copy.deepcopy(self.base); p["expires_at"]=str(NOW-1)
  with self.assertRaisesRegex(PolicyChangeError,"validity"): self.verify(self.signed(base=p))
 def test_not_yet_valid(self):
  p=copy.deepcopy(self.base); p["issued_at"]=str(NOW+1)
  with self.assertRaisesRegex(PolicyChangeError,"validity"): self.verify(self.signed(base=p))
 def test_unknown_proposal_field(self):
  p=self.signed(); p["force_accept"]=True
  with self.assertRaisesRegex(PolicyChangeError,"unknown"): self.verify(p)
 def test_duplicate_json_key(self):
  from policy_change_control import strict_json_bytes
  with self.assertRaisesRegex(PolicyChangeError,"duplicate"): strict_json_bytes(b'{"x":1,"x":2}',"proposal")
 def test_nan_rejected(self):
  from policy_change_control import strict_json_bytes
  with self.assertRaisesRegex(PolicyChangeError,"non-standard"): strict_json_bytes(b'{"x":NaN}',"proposal")
 def test_boolean_threshold_rejected_when_authority_is_pinned(self):
  from policy_change_control import validate_authorities
  a=copy.deepcopy(self.authorities); a["threshold"]=True
  with self.assertRaisesRegex(PolicyChangeError,"positive integer"): validate_authorities(a)
 def test_duplicate_reviewer_identity_rejected(self):
  from policy_change_control import validate_authorities
  a=copy.deepcopy(self.authorities); a["reviewers"].append(copy.deepcopy(a["reviewers"][0]))
  with self.assertRaisesRegex(PolicyChangeError,"duplicated"): validate_authorities(a)
if __name__=="__main__": unittest.main(verbosity=2)
