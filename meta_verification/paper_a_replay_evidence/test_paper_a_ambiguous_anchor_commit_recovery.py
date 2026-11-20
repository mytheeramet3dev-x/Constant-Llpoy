import json, os, tempfile, unittest
from paper_a_persistent_replay_guard import PersistentReplayGuard
from paper_a_replay_registry_audit import logical_snapshot
from paper_a_authenticated_registry_anchor import ANCHOR_SCHEMA, sign_anchor
from paper_a_ambiguous_anchor_commit_recovery import classify_ambiguous_anchor_commit_recovery


class AmbiguousAnchorCommitRecoveryTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.db=os.path.join(self.tmp.name,"registry.sqlite")
        self.anchor_path=os.path.join(self.tmp.name,"anchor.json")
        self.guard=PersistentReplayGuard(self.db)
        self.secret=b"ambiguous-recovery-test-secret-32bytes-min"
        snap=logical_snapshot(self.db)
        self.fields={"schema":ANCHOR_SCHEMA,"key_id":"k1","sequence":5,
          "snapshot_sha256":snap["snapshot_sha256"],"entry_count":snap["entry_count"]}
        self.anchor={**self.fields,"mac_sha256":sign_anchor(self.fields,self.secret)}
        with open(self.anchor_path,"w",encoding="utf8") as f: json.dump(self.anchor,f)
        self.keys={"k1":self.secret}
    def tearDown(self): self.tmp.cleanup()
    def classify(self, **kwargs):
        defaults=dict(database_path=self.db,anchor_path=self.anchor_path,
          trusted_keys=self.keys,externally_held_minimum_sequence=5,
          expected_previous_sequence=5,expected_previous_digest=self.fields["snapshot_sha256"],
          intended_sequence=6)
        defaults.update(kwargs)
        return classify_ambiguous_anchor_commit_recovery(**defaults)
    def test_previous_anchor_verified_means_not_committed_candidate(self):
        result=self.classify()
        self.assertEqual(result["status"],"NOT_COMMITTED")
        self.assertEqual(result["retry_advice"],"RETRY_REQUIRES_CALLER_REVALIDATION")
    def test_intended_sequence_verified_means_committed(self):
        fields={**self.fields,"sequence":6}
        anchor={**fields,"mac_sha256":sign_anchor(fields,self.secret)}
        with open(self.anchor_path,"w") as f: json.dump(anchor,f)
        result=self.classify()
        self.assertEqual(result["status"],"COMMITTED")
        self.assertEqual(result["retry_advice"],"DO_NOT_RETRY")
    def test_staging_file_blocks_retry_classification(self):
        open(os.path.join(self.tmp.name,".anchor-stage-orphan"),"w").close()
        result=self.classify()
        self.assertEqual(result["status"],"INDETERMINATE")
        self.assertEqual(result["retry_advice"],"DO_NOT_RETRY")
    def test_missing_anchor_indeterminate(self):
        os.unlink(self.anchor_path)
        self.assertEqual(self.classify()["status"],"INDETERMINATE")
    def test_unexpected_sequence_indeterminate(self):
        fields={**self.fields,"sequence":7}
        anchor={**fields,"mac_sha256":sign_anchor(fields,self.secret)}
        with open(self.anchor_path,"w") as f: json.dump(anchor,f)
        self.assertEqual(self.classify()["status"],"INDETERMINATE")
    def test_wrong_previous_digest_does_not_authorize_retry(self):
        result=self.classify(expected_previous_digest="0"*64)
        self.assertEqual(result["status"],"INDETERMINATE")
        self.assertEqual(result["retry_advice"],"DO_NOT_RETRY")
    def test_live_registry_mismatch_fails_closed(self):
        self.guard.consume("k1","evaluation-1","nonce-unique-0001")
        result=self.classify()
        self.assertEqual(result["status"],"FAIL_CLOSED")
        self.assertEqual(result["retry_advice"],"DO_NOT_RETRY")
    def test_malformed_anchor_fails_closed(self):
        with open(self.anchor_path,"w") as f: f.write("{bad")
        self.assertEqual(self.classify()["status"],"FAIL_CLOSED")


if __name__=="__main__": unittest.main()
