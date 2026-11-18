import hashlib, json, tempfile, unittest
from pathlib import Path
import paper_a_component_pipeline as p
class Tests(unittest.TestCase):
 def setUp(self): self.tmp=tempfile.TemporaryDirectory(); self.root=Path(self.tmp.name); self.commit="a"*40
 def tearDown(self): self.tmp.cleanup()
 def test_run_hashes_inputs_and_limits_pass_to_execution(self):
  (self.root/"in").write_text("fixed")
  x=p.run_command("TEST",self.commit,str(self.root/"out.json"),".",["in"],10,["python","-c","print('ok')"])
  self.assertEqual(x["status"],"PASS"); self.assertEqual(x["mathematical_correctness"],"NOT_ASSESSED")
  self.assertEqual(x["input_files"][0]["sha256"],hashlib.sha256(b"fixed").hexdigest())
 def test_nonzero_exit_is_fail(self):
  x=p.run_command("TEST",self.commit,str(self.root/"out.json"),".",[],10,["python","-c","raise SystemExit(9)"])
  self.assertEqual(x["status"],"FAIL"); self.assertEqual(x["exit_code"],9)
 def test_working_directory_escape_rejected(self):
  with self.assertRaisesRegex(ValueError,"escapes"): p.run_command("T",self.commit,str(self.root/"x"),"..",[],1,["python","-c","pass"])
 def test_incomplete_claim_registry_rejected(self):
  (self.root/"CLAIM_REGISTRY.md").write_text("| AS-ALPHA-A-THM-0001 | T | theorem | Arxiv/a.md | CANDIDATE | NOT_ASSESSED | [Record](claims/A/a.md) |")
  (self.root/"MANUSCRIPT_SOURCE_MANIFEST.md").write_text("## 2. Paper A source freeze\n| Frozen commit | bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb |\n## 3. Paper D\n")
  with self.assertRaisesRegex(ValueError,"expected 15"): p.build_traceability(self.root,self.commit)
 def test_layer_plan_has_fourteen_rows_and_no_theorem_pass(self):
  (self.root/"trace.json").write_text(json.dumps({"source_commit":self.commit,"claim_count":15}))
  ev=[]
  for i in range(5):
   rel=f"e{i}.json"; (self.root/rel).write_text(json.dumps({"source_commit":self.commit,"status":"PASS","component_id":f"C{i}"})); ev.append(rel)
  x=p.build_layer_plan(self.root,self.commit,"trace.json",ev)
  self.assertEqual(x["layer_count"],14); self.assertEqual(x["overall_paper_status"],"NOT_VERIFIED")
  self.assertEqual(x["layers"][3]["assessment_status"],"PARTIAL"); self.assertEqual(x["layers"][13]["assessment_status"],"NOT_ASSESSED")
 def test_layer_plan_rejects_stale_evidence(self):
  (self.root/"trace.json").write_text(json.dumps({"source_commit":self.commit,"claim_count":15}))
  (self.root/"e.json").write_text(json.dumps({"source_commit":"b"*40,"status":"PASS","component_id":"C"}))
  with self.assertRaisesRegex(ValueError,"not complete"): p.build_layer_plan(self.root,self.commit,"trace.json",["e.json"])
 def test_candidate_links_do_not_claim_correspondence(self):
  self.assertEqual(p.CLAIM_ARTIFACTS["AS-ALPHA-A-PROP-0009"][0][2],"NOT_ESTABLISHED")
if __name__=="__main__": unittest.main(verbosity=2)
