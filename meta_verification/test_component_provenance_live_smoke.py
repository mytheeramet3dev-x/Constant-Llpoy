"""Tests for the live component-provenance smoke-test adapter."""
import hashlib, json, tempfile, unittest
from pathlib import Path
from unittest.mock import patch
import component_provenance_live_smoke as smoke

class LiveSmokeAdapterTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(); self.root=Path(self.tmp.name)
        self.subject=self.root/"subject.json"; self.subject.write_bytes(b'{"status":"ACCEPTED"}')
        self.policy=self.root/"policy.json"
        self.policy.write_text(json.dumps({
          "schema_version":"1.0","repository":"mytheeramet3dev-x/Constant-Llpoy",
          "repository_id":1460417275,
          "signer_workflow":"mytheeramet3dev-x/Constant-Llpoy/.github/workflows/meta-verification-evidence.yml",
          "source_ref":"refs/heads/main","oidc_issuer":"https://token.actions.githubusercontent.com",
          "predicate_type":"https://slsa.dev/provenance/v1","require_verified_timestamps":True,
          "deny_self_hosted_runners":True,"gh_cli_version":"2.103.3"
        }),encoding="utf-8")
        self.pin=hashlib.sha256(self.policy.read_bytes()).hexdigest(); self.commit="a"*40
    def tearDown(self): self.tmp.cleanup()
    def test_builds_exact_subject_receipt_and_requires_authenticated_aggregate(self):
        subject_sha=hashlib.sha256(self.subject.read_bytes()).hexdigest()
        auth={smoke.COMPONENT_ID:{"subject_sha256":subject_sha,"source_commit":self.commit,
          "attestation_run_id":123,"attestation_run_attempt":2,"attestation_workflow_revision":self.commit,
          "repository_id":1460417275,
          "signer_workflow":"mytheeramet3dev-x/Constant-Llpoy/.github/workflows/meta-verification-evidence.yml",
          "provenance_policy_sha256":self.pin,"verified_attestation_count":1}}
        with patch.object(smoke,"authenticate_components",return_value=auth) as verifier:
            result=smoke.run(str(self.subject),str(self.policy),self.pin,self.commit,123,2)
        self.assertEqual(result["status"],"LIVE_COMPONENT_PROVENANCE_SMOKE_VERIFIED")
        self.assertEqual(result["aggregator_status"],"ACCEPTED")
        bundle=verifier.call_args.args[3]
        self.assertEqual(bundle["components"][0]["provenance"]["attestation_run_attempt"],2)
        self.assertEqual(bundle["components"][0]["evidence_sha256"],subject_sha)
    def test_rejects_boolean_run_identity(self):
        with self.assertRaisesRegex(ValueError,"positive integer"):
            smoke.run(str(self.subject),str(self.policy),self.pin,self.commit,True,1)
    def test_rejects_wrong_policy_pin_format(self):
        with self.assertRaisesRegex(ValueError,"SHA-256"):
            smoke.run(str(self.subject),str(self.policy),"bad",self.commit,123,1)
    def test_rejects_symlink_subject(self):
        link=self.root/"link.json"; link.symlink_to(self.subject)
        with self.assertRaisesRegex(ValueError,"without following links"):
            smoke.run(str(link),str(self.policy),self.pin,self.commit,123,1)

if __name__=="__main__": unittest.main(verbosity=2)
