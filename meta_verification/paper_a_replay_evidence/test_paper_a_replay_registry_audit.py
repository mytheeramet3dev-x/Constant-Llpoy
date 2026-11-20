import os,sqlite3,tempfile,unittest
from paper_a_persistent_replay_guard import PersistentReplayGuard
from paper_a_replay_registry_audit import logical_snapshot,verify_snapshot,ReplayRegistryAuditError

class RegistryAuditTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory(); self.db=os.path.join(self.tmp.name,"registry.db")
  self.guard=PersistentReplayGuard(self.db)
 def tearDown(self): self.tmp.cleanup()
 def test_snapshot_matches_and_changes_after_insert(self):
  a=logical_snapshot(self.db)
  self.assertEqual(verify_snapshot(self.db,a["snapshot_sha256"])["integrity"],"PASS")
  self.guard.consume("k","e","nonce-123456789")
  b=logical_snapshot(self.db)
  self.assertNotEqual(a["snapshot_sha256"],b["snapshot_sha256"])
  self.assertEqual(verify_snapshot(self.db,a["snapshot_sha256"])["integrity"],"FAIL")
 def test_corrupt_schema_missing_table_fails(self):
  with sqlite3.connect(self.db) as c: c.execute("DROP TABLE consumed_nonces")
  with self.assertRaises(ReplayRegistryAuditError): logical_snapshot(self.db)
 def test_missing_database_fails(self):
  with self.assertRaises(ReplayRegistryAuditError): logical_snapshot(os.path.join(self.tmp.name,"absent.db"))
 def test_bad_anchor_format_fails(self):
  with self.assertRaises(ReplayRegistryAuditError): verify_snapshot(self.db,"not-a-digest")
 def test_database_integrity_and_empty_registry(self):
  s=logical_snapshot(self.db)
  self.assertEqual(s["integrity"],"PASS"); self.assertEqual(s["entry_count"],0)
if __name__=="__main__": unittest.main()
