"""Tests for secure Paper A evidence intake adapter."""
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from paper_a_replay_evidence_intake import intake

class IntakeTests(unittest.TestCase):
    def make_bundle(self, root):
        payload=root/"input.txt"; payload.write_text("sample",encoding="utf-8")
        digest=hashlib.sha256(b"sample").hexdigest()
        manifest={
          "schema_version":"1.0","project":"Paper A","git_commit":"a"*40,
          "run_timestamp_utc":"2026-11-21T00:00:00Z",
          "environment":{"python_version":"3.12","platform":"test","dependencies":{}},
          "command":"replay","inputs":[{"path":"input.txt","sha256":digest,"exact_values":{"x":"1"}}],
          "artifacts":[],"checks":[{"check_id":"producer","status":"PASS"}],
          "scope":"intake test","limitations":["test"]
        }
        mf=root/"manifest.json"; mf.write_text(json.dumps(manifest),encoding="utf-8")
        return mf,manifest
    def test_intake_pass_and_exact_values_metadata_preserved(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); mf,_=self.make_bundle(root)
            out=intake(str(mf),td)
            self.assertEqual(out["intake_status"],"PASS")
            self.assertTrue(out["independent_file_checks"][0]["exact_values_present"])
            self.assertEqual(out["certification"],"NOT_PERFORMED")
    def test_hash_mismatch_fail(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); mf,_=self.make_bundle(root)
            (root/"input.txt").write_text("changed",encoding="utf-8")
            self.assertEqual(intake(str(mf),td)["intake_status"],"FAIL")
    def test_path_escape_fail(self):
        with tempfile.TemporaryDirectory() as td, tempfile.TemporaryDirectory() as out:
            root=Path(td); mf,_=self.make_bundle(root)
            external=Path(out)/"outside.txt"; external.write_text("sample",encoding="utf-8")
            data=json.loads(mf.read_text()); data["inputs"][0]["path"]=str(external)
            data["inputs"][0]["sha256"]=hashlib.sha256(b"sample").hexdigest()
            mf.write_text(json.dumps(data),encoding="utf-8")
            self.assertEqual(intake(str(mf),td)["intake_status"],"FAIL")
    def test_symlink_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); mf,_=self.make_bundle(root)
            link=root/"link.txt"
            try: link.symlink_to(root/"input.txt")
            except (OSError,NotImplementedError): self.skipTest("symlink unavailable")
            data=json.loads(mf.read_text()); data["inputs"][0]["path"]="link.txt"
            mf.write_text(json.dumps(data),encoding="utf-8")
            self.assertEqual(intake(str(mf),td)["intake_status"],"FAIL")
    def test_missing_artifact_fail(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); mf,_=self.make_bundle(root)
            data=json.loads(mf.read_text()); data["artifacts"]=[{"path":"missing","sha256":"0"*64}]
            mf.write_text(json.dumps(data),encoding="utf-8")
            self.assertEqual(intake(str(mf),td)["intake_status"],"FAIL")
if __name__=="__main__": unittest.main()
