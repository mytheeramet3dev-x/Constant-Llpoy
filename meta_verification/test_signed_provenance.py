"""Adversarial tests for signed-provenance policy enforcement."""
import hashlib
import unittest
from verify_signed_provenance import ProvenanceError, validate_cli_output, validate_cli_version

REPO_ID=1460417275
SOURCE="a"*40
BYTES=b'{"status":"ACCEPTED","run_id":123}\n'
DIGEST=hashlib.sha256(BYTES).hexdigest()

def policy():
    return {
        "schema_version":"1.0",
        "repository":"mytheeramet3dev-x/Constant-Llpoy",
        "repository_id":REPO_ID,
        "signer_workflow":"mytheeramet3dev-x/Constant-Llpoy/.github/workflows/meta-verification-evidence.yml",
        "source_ref":"refs/heads/main",
        "oidc_issuer":"https://token.actions.githubusercontent.com",
        "predicate_type":"https://slsa.dev/provenance/v1",
        "require_verified_timestamps":True,
        "deny_self_hosted_runners":True,
        "gh_cli_version":"2.103.3",
    }

def result():
    return [{
        "verificationResult":{
            "signature":{"certificate":{
                "sourceRepositoryIdentifier":str(REPO_ID),
                "sourceRepositoryRef":"refs/heads/main",
                "sourceRepositoryDigest":SOURCE,
                "buildSignerDigest":SOURCE,
            }},
            "verifiedTimestamps":[{"kind":"rekor","integratedTime":123}],
            "statement":{
                "predicateType":"https://slsa.dev/provenance/v1",
                "subject":[{"name":"github-run-evidence.json","digest":{"sha256":DIGEST}}],
            },
        }
    }]

class SignedProvenanceTests(unittest.TestCase):
    def test_valid_provenance_verified(self):
        report=validate_cli_output(result(),BYTES,policy(),SOURCE)
        self.assertEqual(report["status"],"VERIFIED")
        self.assertEqual(report["repository_id"],REPO_ID)
        self.assertEqual(report["subject_sha256"],DIGEST)

    def test_empty_attestation_set_rejected(self):
        with self.assertRaises(ProvenanceError): validate_cli_output([],BYTES,policy(),SOURCE)

    def test_wrong_repository_id_rejected(self):
        x=result(); x[0]["verificationResult"]["signature"]["certificate"]["sourceRepositoryIdentifier"]="999"
        with self.assertRaises(ProvenanceError): validate_cli_output(x,BYTES,policy(),SOURCE)

    def test_wrong_source_ref_rejected(self):
        x=result(); x[0]["verificationResult"]["signature"]["certificate"]["sourceRepositoryRef"]="refs/heads/attacker"
        with self.assertRaises(ProvenanceError): validate_cli_output(x,BYTES,policy(),SOURCE)

    def test_stale_source_commit_rejected(self):
        x=result(); x[0]["verificationResult"]["signature"]["certificate"]["sourceRepositoryDigest"]="b"*40
        with self.assertRaises(ProvenanceError): validate_cli_output(x,BYTES,policy(),SOURCE)

    def test_wrong_signer_commit_rejected(self):
        x=result(); x[0]["verificationResult"]["signature"]["certificate"]["buildSignerDigest"]="c"*40
        with self.assertRaises(ProvenanceError): validate_cli_output(x,BYTES,policy(),SOURCE)

    def test_missing_certificate_rejected(self):
        x=result(); x[0]["verificationResult"]["signature"].pop("certificate")
        with self.assertRaises(ProvenanceError): validate_cli_output(x,BYTES,policy(),SOURCE)

    def test_missing_verified_timestamp_rejected(self):
        x=result(); x[0]["verificationResult"]["verifiedTimestamps"]=[]
        with self.assertRaises(ProvenanceError): validate_cli_output(x,BYTES,policy(),SOURCE)

    def test_wrong_predicate_rejected(self):
        x=result(); x[0]["verificationResult"]["statement"]["predicateType"]="https://example.invalid/other"
        with self.assertRaises(ProvenanceError): validate_cli_output(x,BYTES,policy(),SOURCE)

    def test_altered_subject_bytes_rejected(self):
        with self.assertRaises(ProvenanceError): validate_cli_output(result(),BYTES+b"tampered",policy(),SOURCE)

    def test_missing_or_ambiguous_subject_rejected(self):
        x=result(); x[0]["verificationResult"]["statement"]["subject"].append(
            {"name":"other","digest":{"sha256":DIGEST}})
        with self.assertRaises(ProvenanceError): validate_cli_output(x,BYTES,policy(),SOURCE)

    def test_policy_unknown_field_rejected(self):
        p=policy(); p["allow_any_signer"]=True
        with self.assertRaises(ProvenanceError): validate_cli_output(result(),BYTES,p,SOURCE)

    def test_policy_cannot_disable_timestamp_requirement(self):
        p=policy(); p["require_verified_timestamps"]=False
        with self.assertRaises(ProvenanceError): validate_cli_output(result(),BYTES,p,SOURCE)

    def test_malformed_source_sha_rejected(self):
        with self.assertRaises(ProvenanceError): validate_cli_output(result(),BYTES,policy(),"not-a-sha")

    def test_cli_version_policy_is_exact(self):
        p=policy(); p["gh_cli_version"]="latest"
        with self.assertRaises(ProvenanceError): validate_cli_output(result(),BYTES,p,SOURCE)

    def test_exact_gh_cli_version_accepted(self):
        self.assertEqual(validate_cli_version("gh version 2.103.3 (2026-10-26)\\n",policy()),"2.103.3")

    def test_wrong_gh_cli_version_rejected(self):
        with self.assertRaises(ProvenanceError): validate_cli_version("gh version 2.103.2\\n",policy())

    def test_malformed_gh_cli_version_rejected(self):
        with self.assertRaises(ProvenanceError): validate_cli_version("GitHub CLI latest",policy())

if __name__=="__main__": unittest.main(verbosity=2)
