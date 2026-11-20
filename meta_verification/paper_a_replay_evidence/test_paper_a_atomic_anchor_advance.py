import json, os, tempfile, unittest
from unittest import mock
from paper_a_persistent_replay_guard import PersistentReplayGuard
from paper_a_replay_registry_audit import logical_snapshot
from paper_a_authenticated_registry_anchor import ANCHOR_SCHEMA, sign_anchor
from paper_a_atomic_anchor_advance import advance_authenticated_anchor, AnchorAdvanceError

class AtomicAdvanceTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory(); self.db=os.path.join(self.tmp.name,"registry.sqlite")
  self.anchor_path=os.path.join(self.tmp.name,"anchor.json"); self.guard=PersistentReplayGuard(self.db)
  self.secret=b"atomic-anchor-test-secret-material-32bytes-min"
  snap=logical_snapshot(self.db)
  fields={"schema":ANCHOR_SCHEMA,"key_id":"key1","sequence":5,"snapshot_sha256":snap["snapshot_sha256"],"entry_count":snap["entry_count"]}
  self.anchor={**fields,"mac_sha256":sign_anchor(fields,self.secret)}
  with open(self.anchor_path,"w",encoding="utf8") as f: json.dump(self.anchor,f)
  self.keys={"key1":self.secret}
 def tearDown(self): self.tmp.cleanup()
 def call(self, **kwargs):
  defaults=dict(database_path=self.db,anchor_path=self.anchor_path,trusted_keys=self.keys,key_id="key1",secret=self.secret,
   externally_held_minimum_sequence=5,expected_current_sequence=5,expected_current_digest=self.anchor["snapshot_sha256"],new_sequence=6)
  defaults.update(kwargs); return advance_authenticated_anchor(**defaults)
 def test_atomic_advance(self):
  result=self.call()
  self.assertEqual(result["integrity"],"PASS"); self.assertTrue(result["atomic_commit"])
  with open(self.anchor_path) as f: saved=json.load(f)
  self.assertEqual(saved["sequence"],6)
 def test_stale_sequence_rejected(self):
  with self.assertRaisesRegex(AnchorAdvanceError,"stale writer"): self.call(expected_current_sequence=4)
 def test_stale_digest_rejected(self):
  with self.assertRaisesRegex(AnchorAdvanceError,"stale writer"): self.call(expected_current_digest="f"*64)
 def test_sequence_must_increase(self):
  with self.assertRaisesRegex(AnchorAdvanceError,"strictly increase"): self.call(new_sequence=5)
 def test_corrupt_current_anchor_fails_closed(self):
  with open(self.anchor_path,"w") as f: f.write("{}")
  with self.assertRaises(AnchorAdvanceError): self.call()
 def test_untrusted_signing_key_rejected(self):
  with self.assertRaisesRegex(AnchorAdvanceError,"trusted key map"): self.call(secret=b"x"*40)
 def test_replace_failure_preserves_original(self):
  original=open(self.anchor_path,"rb").read()
  with mock.patch("paper_a_atomic_anchor_advance.os.replace",side_effect=OSError("simulated crash")):
   with self.assertRaises(OSError): self.call()
  self.assertEqual(open(self.anchor_path,"rb").read(),original)
 def test_registry_drift_blocks_advance(self):
  self.guard.consume("key1","eval-x","nonce-12345678")
  with self.assertRaises(AnchorAdvanceError): self.call()
if __name__=="__main__": unittest.main()
