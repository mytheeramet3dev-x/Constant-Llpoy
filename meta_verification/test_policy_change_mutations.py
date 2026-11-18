"""Selected mutation adequacy tests for policy change authorization."""
import pathlib,shutil,subprocess,sys,tempfile,unittest
ROOT=pathlib.Path(__file__).resolve().parent
SOURCE=ROOT/"policy_change_control.py"
TESTS=ROOT/"test_policy_change_control.py"
MUTANTS={
 "bypass_external_authority_pin":('require(sha256(authority_bytes)==expected_authority_sha256,','require(False and sha256(authority_bytes)==expected_authority_sha256,'),
 "bypass_policy_digest_binding":('require(digest(p["policy_sha256"],"policy digest")==actual,','require(True,'),
 "bypass_parent_chain":('require(digest(p["parent_policy_sha256"],"parent digest")==expected_parent_policy_sha256,','require(True,'),
 "bypass_sequence":('require(positive_int(p["sequence"],"sequence")==expected_sequence,','require(True,'),
 "lower_threshold_to_one":('require(len(accepted)>=authorities["threshold"],','require(len(accepted)>=1,'),
 "bypass_expiry":('require(issued<expires and issued<=now_epoch<expires,','require(True,'),
 "allow_duplicate_signer":('require(isinstance(rid,str) and rid.strip() and rid not in accepted,','require(isinstance(rid,str) and rid.strip(),'),
 "skip_cryptographic_signature_check":('require(bool(raw_sig) and verify_sig(keys[rid],raw_sig,message),','require(bool(raw_sig),'),
}
class MutationTests(unittest.TestCase):
 def test_selected_mutants_are_killed_by_assertions(self):
  source=SOURCE.read_text(encoding="utf-8")
  for name,(old,new) in MUTANTS.items():
   with self.subTest(mutant=name),tempfile.TemporaryDirectory() as td:
    root=pathlib.Path(td); self.assertIn(old,source,f"mutation anchor missing: {name}")
    (root/"policy_change_control.py").write_text(source.replace(old,new,1),encoding="utf-8")
    shutil.copy2(TESTS,root/"test_policy_change_control.py")
    syntax=subprocess.run([sys.executable,"-m","py_compile",str(root/"policy_change_control.py")],capture_output=True,text=True)
    self.assertEqual(syntax.returncode,0,syntax.stderr)
    run=subprocess.run([sys.executable,"-m","unittest","-v","test_policy_change_control"],cwd=root,capture_output=True,text=True)
    self.assertNotEqual(run.returncode,0,f"mutant survived: {name}")
    self.assertIn("FAIL:",run.stderr+run.stdout,f"not assertion-driven: {name}")
    print(f"POLICY MUTANT KILLED: {name}")
if __name__=="__main__": unittest.main(verbosity=2)
