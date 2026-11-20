"""Tests for independent evidence inventory completeness."""
import unittest
from paper_a_evidence_completeness import evaluate_completeness
class CompletenessTests(unittest.TestCase):
 def setUp(self):
  self.manifest={"inputs":[{"path":"input/a.csv","sha256":"x"}],"artifacts":[{"path":"out/result.json","sha256":"y"}],"checks":[{"check_id":"numeric-replay","status":"PASS"},{"check_id":"spectrum","status":"FAIL"}]}
  self.policy={"policy_id":"PAPER-A-INVENTORY-1","version":"1.0","required_inputs":["input/a.csv"],"required_artifacts":["out/result.json"],"required_check_ids":["numeric-replay","spectrum"]}
 def test_complete_inventory_pass(self): self.assertEqual(evaluate_completeness(self.manifest,self.policy)["completeness_status"],"PASS")
 def test_manifest_omission_fail(self):
  self.manifest["inputs"]=[]; out=evaluate_completeness(self.manifest,self.policy); self.assertEqual(out["completeness_status"],"FAIL"); self.assertEqual(out["missing_required_inputs"],["input/a.csv"])
 def test_missing_artifact_fail(self):
  self.manifest["artifacts"]=[]; out=evaluate_completeness(self.manifest,self.policy); self.assertEqual(out["completeness_status"],"FAIL"); self.assertEqual(out["missing_required_artifacts"],["out/result.json"])
 def test_missing_check_id_fail(self):
  self.manifest["checks"]=[]; out=evaluate_completeness(self.manifest,self.policy); self.assertEqual(out["completeness_status"],"FAIL"); self.assertEqual(out["missing_required_check_ids"],["numeric-replay","spectrum"])
 def test_failed_check_presence_is_not_pass_claim(self):
  out=evaluate_completeness(self.manifest,self.policy); self.assertEqual(out["completeness_status"],"PASS"); self.assertEqual(self.manifest["checks"][1]["status"],"FAIL")
 def test_duplicate_policy_entry_rejected(self):
  self.policy["required_inputs"].append("input/a.csv")
  with self.assertRaisesRegex(ValueError,"duplicate"): evaluate_completeness(self.manifest,self.policy)
 def test_empty_required_artifacts_rejected(self):
  self.policy["required_artifacts"]=[]
  with self.assertRaisesRegex(ValueError,"required_artifacts"): evaluate_completeness(self.manifest,self.policy)
 def test_traversal_policy_path_rejected(self):
  self.policy["required_inputs"]=["../secret"]
  with self.assertRaisesRegex(ValueError,"canonical"): evaluate_completeness(self.manifest,self.policy)
if __name__=="__main__": unittest.main()
