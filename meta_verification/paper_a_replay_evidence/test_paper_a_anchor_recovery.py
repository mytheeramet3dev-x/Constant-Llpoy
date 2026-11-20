import json, os, tempfile, unittest
from paper_a_persistent_replay_guard import PersistentReplayGuard
from paper_a_replay_registry_audit import logical_snapshot
from paper_a_authenticated_registry_anchor import ANCHOR_SCHEMA, sign_anchor
from paper_a_anchor_recovery import classify_anchor_recovery

class AnchorRecoveryTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.db=os.path.join(self.tmp.name,"registry.sqlite")
        self.anchor_path=os.path.join(self.tmp.name,"anchor.json")
        self.guard=PersistentReplayGuard(self.db)
        self.secret=b"anchor-recovery-tests-secret-32-bytes-minimum"
        snap=logical_snapshot(self.db)
        fields={"schema":ANCHOR_SCHEMA,"key_id":"key1","sequence":3,
                "snapshot_sha256":snap["snapshot_sha256"],"entry_count":snap["entry_count"]}
        self.anchor={**fields,"mac_sha256":sign_anchor(fields,self.secret)}
        self.keys={"key1":self.secret}
        with open(self.anchor_path,"w",encoding="utf-8") as f: json.dump(self.anchor,f)
    def tearDown(self): self.tmp.cleanup()
    def test_valid_final_anchor_passes(self):
        self.assertEqual(classify_anchor_recovery(self.db,self.anchor_path,self.keys,3)["status"],"PASS")
    def test_orphan_stage_is_not_promoted(self):
        staged=os.path.join(self.tmp.name,".anchor-stage-orphan")
        with open(staged,"w") as f: f.write("{}")
        result=classify_anchor_recovery(self.db,self.anchor_path,self.keys,3)
        self.assertEqual(result["status"],"INDETERMINATE")
        self.assertIn(os.path.basename(staged),result["staged_files"])
        with open(self.anchor_path) as f: self.assertEqual(json.load(f),self.anchor)
    def test_missing_final_anchor_indeterminate(self):
        os.unlink(self.anchor_path)
        self.assertEqual(classify_anchor_recovery(self.db,self.anchor_path,self.keys,3)["status"],"INDETERMINATE")
    def test_malformed_final_fail_closed(self):
        with open(self.anchor_path,"w") as f: f.write("{")
        self.assertEqual(classify_anchor_recovery(self.db,self.anchor_path,self.keys,3)["status"],"FAIL_CLOSED")
    def test_registry_drift_fail_closed(self):
        self.guard.consume("key1","recovery-case","nonce-recovery-123")
        self.assertEqual(classify_anchor_recovery(self.db,self.anchor_path,self.keys,3)["status"],"FAIL_CLOSED")
    def test_external_floor_rollback_fail_closed(self):
        self.assertEqual(classify_anchor_recovery(self.db,self.anchor_path,self.keys,4)["status"],"FAIL_CLOSED")
    def test_non_object_fail_closed(self):
        with open(self.anchor_path,"w") as f: json.dump([],f)
        self.assertEqual(classify_anchor_recovery(self.db,self.anchor_path,self.keys,3)["status"],"FAIL_CLOSED")
if __name__=="__main__": unittest.main()
