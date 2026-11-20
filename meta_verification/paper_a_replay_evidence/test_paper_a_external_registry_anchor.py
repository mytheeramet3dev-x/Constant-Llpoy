import os,tempfile,unittest
from paper_a_persistent_replay_guard import PersistentReplayGuard
from paper_a_replay_registry_audit import logical_snapshot, ReplayRegistryAuditError
from paper_a_external_registry_anchor import verify_external_anchor, ANCHOR_SCHEMA

class ExternalAnchorTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory(); self.db=os.path.join(self.tmp.name,"registry.db"); self.guard=PersistentReplayGuard(self.db)
  snap=logical_snapshot(self.db); self.anchor={"schema":ANCHOR_SCHEMA,"snapshot_sha256":snap["snapshot_sha256"],"entry_count":snap["entry_count"]}
 def tearDown(self): self.tmp.cleanup()
 def test_anchor_match(self):
  self.assertEqual(verify_external_anchor(self.db,self.anchor)["integrity"],"PASS")
 def test_drift_detected(self):
  self.guard.consume("key","eval","nonce-123456789")
  result=verify_external_anchor(self.db,self.anchor)
  self.assertEqual(result["integrity"],"FAIL")
  self.assertIn("differs from external anchor",result["reason"])
 def test_deleted_database_fails_closed(self):
  os.remove(self.db)
  with self.assertRaises(ReplayRegistryAuditError): verify_external_anchor(self.db,self.anchor)
 def test_missing_anchor_rejected(self):
  with self.assertRaises(ReplayRegistryAuditError): verify_external_anchor(self.db,None)
 def test_digest_malformed(self):
  bad={**self.anchor,"snapshot_sha256":"x"}
  with self.assertRaises(ReplayRegistryAuditError): verify_external_anchor(self.db,bad)
 def test_anchor_count_mismatch(self):
  bad={**self.anchor,"entry_count":self.anchor["entry_count"]+1}
  self.assertEqual(verify_external_anchor(self.db,bad)["integrity"],"FAIL")
 def test_schema_rejected(self):
  bad={**self.anchor,"schema":"wrong"}
  with self.assertRaises(ReplayRegistryAuditError): verify_external_anchor(self.db,bad)
if __name__=="__main__": unittest.main()
