import os,tempfile,unittest
from paper_a_persistent_replay_guard import PersistentReplayGuard
from paper_a_replay_registry_audit import logical_snapshot, ReplayRegistryAuditError
from paper_a_authenticated_registry_anchor import sign_anchor, verify_authenticated_anchor, ANCHOR_SCHEMA, AnchorAuthenticationError

class AuthenticatedAnchorTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory(); self.db=os.path.join(self.tmp.name,"registry.db"); self.guard=PersistentReplayGuard(self.db)
  self.secret=b"test anchor signing key material 32+ bytes"
  snap=logical_snapshot(self.db)
  fields={"schema":ANCHOR_SCHEMA,"key_id":"test-key","sequence":3,"snapshot_sha256":snap["snapshot_sha256"],"entry_count":snap["entry_count"]}
  self.anchor={**fields,"mac_sha256":sign_anchor(fields,self.secret)}
  self.keys={"test-key":self.secret}
 def tearDown(self): self.tmp.cleanup()
 def test_valid_anchor(self):
  self.assertEqual(verify_authenticated_anchor(self.db,self.anchor,self.keys,3)["integrity"],"PASS")
 def test_tampered_digest_fails_auth(self):
  altered={**self.anchor,"snapshot_sha256":"0"*64}
  with self.assertRaises(AnchorAuthenticationError): verify_authenticated_anchor(self.db,altered,self.keys,3)
 def test_untrusted_key_rejected(self):
  with self.assertRaises(AnchorAuthenticationError): verify_authenticated_anchor(self.db,self.anchor,{},3)
 def test_rollback_floor_rejects_older_anchor(self):
  with self.assertRaisesRegex(AnchorAuthenticationError,"rollback"):
   verify_authenticated_anchor(self.db,self.anchor,self.keys,4)
 def test_authenticated_state_drift_returns_fail(self):
  self.guard.consume("k","eval","nonce-123456789")
  self.assertEqual(verify_authenticated_anchor(self.db,self.anchor,self.keys,3)["integrity"],"FAIL")
 def test_bad_mac_rejected(self):
  altered={**self.anchor,"mac_sha256":"0"*64}
  with self.assertRaisesRegex(AnchorAuthenticationError,"authentication"):
   verify_authenticated_anchor(self.db,altered,self.keys,3)
 def test_bad_sequence_rejected(self):
  altered={**self.anchor,"sequence":0}
  with self.assertRaises(AnchorAuthenticationError): verify_authenticated_anchor(self.db,altered,self.keys,1)
 def test_deleted_registry_fails_closed(self):
  os.remove(self.db)
  with self.assertRaises(ReplayRegistryAuditError): verify_authenticated_anchor(self.db,self.anchor,self.keys,3)
if __name__=="__main__": unittest.main()
