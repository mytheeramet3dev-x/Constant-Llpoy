"""Adversarial tests for descriptor-relative evidence intake."""
import hashlib, json, tempfile, unittest
from pathlib import Path
from paper_a_replay_evidence_intake import intake

class IntakeTests(unittest.TestCase):
    def make_bundle(self, root):
        (root/"input.txt").write_text("sample",encoding="utf-8")
        manifest={"schema_version":"1.0","project":"Paper A","git_commit":"a"*40,
          "run_timestamp_utc":"2026-11-21T00:00:00Z",
          "environment":{"python_version":"3.12","platform":"test","dependencies":{}},
          "command":"replay","inputs":[{"path":"input.txt","sha256":hashlib.sha256(b"sample").hexdigest(),"exact_values":{"x":"1"}}],
          "artifacts":[],"checks":[{"check_id":"producer","status":"PASS"}],
          "scope":"intake test","limitations":["test"]}
        (root/"manifest.json").write_text(json.dumps(manifest),encoding="utf-8")
        return "manifest.json", manifest
    def test_pass_and_exact_values_metadata(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); mf,_=self.make_bundle(root); out=intake(mf,td)
            self.assertEqual(out["intake_status"],"PASS")
            self.assertTrue(out["independent_file_checks"][0]["exact_values_present"])
            self.assertEqual(out["certification"],"NOT_PERFORMED")
    def test_modified_content_fail(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); mf,_=self.make_bundle(root); (root/"input.txt").write_text("changed")
            self.assertEqual(intake(mf,td)["intake_status"],"FAIL")
    def test_absolute_path_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); mf,data=self.make_bundle(root)
            data["inputs"][0]["path"]=str(root/"input.txt")
            (root/mf).write_text(json.dumps(data))
            self.assertEqual(intake(mf,td)["intake_status"],"FAIL")
    def test_parent_escape_rejected(self):
        with tempfile.TemporaryDirectory() as td, tempfile.TemporaryDirectory() as out:
            root=Path(td); mf,data=self.make_bundle(root)
            external=Path(out)/"outside"; external.write_text("sample")
            data["inputs"][0]["path"]="../"+external.name
            (root/mf).write_text(json.dumps(data))
            self.assertEqual(intake(mf,td)["intake_status"],"FAIL")
    def test_symlink_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); mf,data=self.make_bundle(root)
            link=root/"link"; link.symlink_to(root/"input.txt")
            data["inputs"][0]["path"]="link"
            (root/mf).write_text(json.dumps(data))
            self.assertEqual(intake(mf,td)["intake_status"],"FAIL")
    def test_manifest_symlink_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); mf,data=self.make_bundle(root)
            link=root/"manifest-link.json"; link.symlink_to(root/mf)
            with self.assertRaises((OSError,ValueError)): intake("manifest-link.json",td)
    def test_missing_artifact_fail(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); mf,data=self.make_bundle(root)
            data["artifacts"]=[{"path":"absent","sha256":"0"*64}]
            (root/mf).write_text(json.dumps(data))
            self.assertEqual(intake(mf,td)["intake_status"],"FAIL")
if __name__=="__main__": unittest.main()
