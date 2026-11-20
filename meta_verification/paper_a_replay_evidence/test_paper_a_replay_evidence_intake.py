"""Adversarial tests for descriptor-relative evidence intake."""
import hashlib,json,tempfile,unittest
from pathlib import Path
from paper_a_replay_evidence_intake import intake
class IntakeTests(unittest.TestCase):
 def make_bundle(self,root):
  (root/"input.txt").write_text("sample",encoding="utf-8"); (root/"result.txt").write_text("result",encoding="utf-8")
  m={"schema_version":"1.0","project":"Paper A","git_commit":"a"*40,"run_timestamp_utc":"2026-11-21T00:00:00Z",
  "environment":{"python_version":"3.12","platform":"test","dependencies":{}},
  "command":"replay","inputs":[{"path":"input.txt","sha256":hashlib.sha256(b"sample").hexdigest(),"exact_values":{"x":"1"}}],
  "artifacts":[{"path":"result.txt","sha256":hashlib.sha256(b"result").hexdigest()}],
  "checks":[{"check_id":"producer","status":"PASS"}],"scope":"intake test","limitations":["test"]}
  (root/"manifest.json").write_text(json.dumps(m),encoding="utf-8"); return "manifest.json",m
 def test_pass(self):
  with tempfile.TemporaryDirectory() as td:
   mf,_=self.make_bundle(Path(td)); out=intake(mf,td); self.assertEqual(out["intake_status"],"PASS")
   self.assertEqual(len(out["independent_file_checks"]),2); self.assertTrue(out["independent_file_checks"][0]["exact_values_present"])
   self.assertEqual(out["certification"],"NOT_PERFORMED"); self.assertEqual(out["producer_claimed_checks"][0]["status"],"PASS")
 def test_modified_content_fail(self):
  with tempfile.TemporaryDirectory() as td:
   root=Path(td); mf,_=self.make_bundle(root); (root/"input.txt").write_text("changed")
   self.assertEqual(intake(mf,td)["intake_status"],"FAIL")
 def test_absolute_path_rejected(self):
  with tempfile.TemporaryDirectory() as td:
   root=Path(td); mf,m=self.make_bundle(root); m["inputs"][0]["path"]=str(root/"input.txt"); (root/mf).write_text(json.dumps(m))
   with self.assertRaises(ValueError): intake(mf,td)
 def test_parent_escape_rejected(self):
  with tempfile.TemporaryDirectory() as td:
   root=Path(td); mf,m=self.make_bundle(root); m["inputs"][0]["path"]="../outside"; (root/mf).write_text(json.dumps(m))
   with self.assertRaises(ValueError): intake(mf,td)
 def test_symlink_rejected(self):
  with tempfile.TemporaryDirectory() as td:
   root=Path(td); mf,m=self.make_bundle(root); (root/"link").symlink_to(root/"input.txt"); m["inputs"][0]["path"]="link"; (root/mf).write_text(json.dumps(m))
   self.assertEqual(intake(mf,td)["intake_status"],"FAIL")
 def test_manifest_symlink_rejected(self):
  with tempfile.TemporaryDirectory() as td:
   root=Path(td); mf,_=self.make_bundle(root); (root/"manifest-link.json").symlink_to(root/mf)
   with self.assertRaises((OSError,ValueError)): intake("manifest-link.json",td)
 def test_missing_artifact_fail(self):
  with tempfile.TemporaryDirectory() as td:
   root=Path(td); mf,m=self.make_bundle(root); m["artifacts"][0]["path"]="absent"; (root/mf).write_text(json.dumps(m))
   self.assertEqual(intake(mf,td)["intake_status"],"FAIL")
 def test_empty_evidence_sections_fail(self):
  for sec in ("inputs","artifacts"):
   with self.subTest(sec=sec),tempfile.TemporaryDirectory() as td:
    root=Path(td); mf,m=self.make_bundle(root); m[sec]=[]; (root/mf).write_text(json.dumps(m))
    with self.assertRaisesRegex(ValueError,"incomplete evidence bundle"): intake(mf,td)
 def test_duplicate_path_across_sections_rejected(self):
  with tempfile.TemporaryDirectory() as td:
   root=Path(td); mf,m=self.make_bundle(root); m["artifacts"][0]={"path":"input.txt","sha256":m["inputs"][0]["sha256"]}; (root/mf).write_text(json.dumps(m))
   with self.assertRaisesRegex(ValueError,"duplicate evidence path"): intake(mf,td)
 def test_backslash_path_rejected(self):
  with tempfile.TemporaryDirectory() as td:
   root=Path(td); mf,m=self.make_bundle(root); m["inputs"][0]["path"]="folder\\input.txt"; (root/mf).write_text(json.dumps(m))
   with self.assertRaises(ValueError): intake(mf,td)
 def test_dot_component_rejected(self):
  with tempfile.TemporaryDirectory() as td:
   root=Path(td); mf,m=self.make_bundle(root); m["inputs"][0]["path"]="./input.txt"; (root/mf).write_text(json.dumps(m))
   with self.assertRaises(ValueError): intake(mf,td)
if __name__=="__main__": unittest.main()
