import copy, tempfile, unittest
from pathlib import Path
from paper_a_semantic_audit_validator import AuditError,git_blob_sha,validate,strict_json
class SemanticAuditValidatorTests(unittest.TestCase):
 def fixture(self):
  with tempfile.TemporaryDirectory() as td:
   root=Path(td); (root/"claims/A").mkdir(parents=True); (root/"formalization/lean/ConstantLlapoy/PaperA").mkdir(parents=True)
   ids=(["AS-ALPHA-A-DEF-0001"]+[f"AS-ALPHA-A-PROP-{i:04d}" for i in range(1,13)]+[f"AS-ALPHA-A-THM-{i:04d}" for i in range(1,3)])
   claims=[]
   for cid in ids:
    raw=(cid+"\n").encode(); (root/"claims/A"/f"{cid}.md").write_bytes(raw)
    claims.append({"claim_id":cid,"source":"Section 1, line 1","claim_blob":git_blob_sha(raw),"lean_status":"NO_DIRECT_FORMALIZATION","lean_declarations":[],"gap":"not yet formalized"})
   modules=[]
   for i in range(5):
    path=f"formalization/lean/ConstantLlapoy/PaperA/Test{i}.lean"; raw=f"theorem test_decl_{i} : True := by trivial\n".encode()
    (root/path).write_bytes(raw); modules.append({"path":path,"blob_sha":git_blob_sha(raw)})
   audit={"schema_version":"1.0","audit_id":"PAPER_A_LEAN_SEMANTIC_CORRESPONDENCE_AUDIT","frozen_source":{},"audit_repository":"test","audited_commit":"a"*40,"lean_toolchain":"test","mathlib_commit":"b"*40,"lean_modules":modules,"claims":claims,"summary":{"total_claims":15,"directly_fully_corresponding":0,"partial_support_or_abstract_core":0,"no_direct_formalization":15,"source_conflict_with_conditional_lemmas_only":0,"claim_verification_promoted":False,"layer_l02":"BLOCKED"},"limits":["not a proof"]}
   yield root,audit
 def test_valid_structural_audit_does_not_promote_semantics(self):
  for root,a in self.fixture():
   r=validate(a,root); self.assertEqual(r["status"],"STRUCTURALLY_VALID_NOT_SEMANTICALLY_VERIFIED"); self.assertEqual(r["layer_l02"],"BLOCKED"); self.assertFalse(r["claim_verification_promoted"])
 def test_missing_claim_rejected(self):
  for root,a in self.fixture():
   a["claims"].pop()
   with self.assertRaisesRegex(AuditError,"claim registry set"): validate(a,root)
 def test_duplicate_claim_rejected(self):
  for root,a in self.fixture():
   a["claims"][-1]=copy.deepcopy(a["claims"][0])
   with self.assertRaisesRegex(AuditError,"duplicate"): validate(a,root)
 def test_claim_blob_substitution_rejected(self):
  for root,a in self.fixture():
   a["claims"][0]["claim_blob"]="0"*40
   with self.assertRaisesRegex(AuditError,"blob mismatch"): validate(a,root)
 def test_module_blob_substitution_rejected(self):
  for root,a in self.fixture():
   a["lean_modules"][0]["blob_sha"]="0"*40
   with self.assertRaisesRegex(AuditError,"module blob mismatch"): validate(a,root)
 def test_unknown_status_rejected(self):
  for root,a in self.fixture():
   a["claims"][0]["lean_status"]="VERIFIED"
   with self.assertRaisesRegex(AuditError,"unsupported status"): validate(a,root)
 def test_no_direct_cannot_claim_declarations(self):
  for root,a in self.fixture():
   a["claims"][0]["lean_declarations"]=["fabricated_theorem"]
   with self.assertRaisesRegex(AuditError,"no-direct status"): validate(a,root)
 def test_summary_counts_recomputed(self):
  for root,a in self.fixture():
   a["summary"]["no_direct_formalization"]=14
   with self.assertRaisesRegex(AuditError,"summary count mismatch"): validate(a,root)
 def test_semantic_pass_forbidden(self):
  for root,a in self.fixture():
   a["summary"]["layer_l02"]="PASS"
   with self.assertRaisesRegex(AuditError,"must remain BLOCKED"): validate(a,root)
 def test_claim_verification_promotion_forbidden(self):
  for root,a in self.fixture():
   a["summary"]["claim_verification_promoted"]=True
   with self.assertRaisesRegex(AuditError,"must not promote"): validate(a,root)
 def test_missing_declaration_rejected(self):
  for root,a in self.fixture():
   a["claims"][0]["lean_status"]="PARTIAL_SUPPORT_ONLY"; a["claims"][0]["lean_declarations"]=["fabricated_theorem"]
   a["summary"]["no_direct_formalization"]=14; a["summary"]["partial_support_or_abstract_core"]=1
   with self.assertRaisesRegex(AuditError,"declaration not found"): validate(a,root)
 def test_duplicate_json_keys_rejected(self):
  with self.assertRaisesRegex(AuditError,"duplicate JSON key"): strict_json(b'{"a":1,"a":2}')
 def test_nonstandard_constant_rejected(self):
  with self.assertRaisesRegex(AuditError,"non-standard JSON"): strict_json(b'{"a":NaN}')
if __name__=="__main__": unittest.main(verbosity=2)
