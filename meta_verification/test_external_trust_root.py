"""Adversarial tests for the external, separately governed trust-root package."""
import hashlib
import json
import os
import subprocess
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

from external_trust_root import TrustRootError, validate_manifest, verify_package

RELYING = "mytheeramet3dev-x/Constant-Llpoy"
RELYING_ID = 1460417275
ROOT = "independent-governance/constant-llpoy-trust-root"
ROOT_ID = 2880000001
BUILDER = "independent-build/constant-llpoy-builder"
BUILDER_ID = 2880000002
SIGNER_WORKFLOW = RELYING + "/.github/workflows/meta-verification-evidence.yml"
BUILDER_WORKFLOW = BUILDER + "/.github/workflows/trusted-builder.yml"
COMMIT = "a" * 40
BUILDER_COMMIT = "b" * 40
NOW = datetime(2026, 11, 18, 12, 0, tzinfo=timezone.utc)


def manifest():
    return {
        "schema_version": "1.0",
        "trust_root_id": "constant-llpoy-independent-root-v1",
        "sequence": 1,
        "issued_at": "2026-11-17T00:00:00Z",
        "expires_at": "2027-11-17T00:00:00Z",
        "relying_party": {"repository": RELYING, "repository_id": RELYING_ID},
        "authorized_signer": {
            "workflow": SIGNER_WORKFLOW,
            "source_ref": "refs/heads/main",
            "oidc_issuer": "https://token.actions.githubusercontent.com",
            "predicate_type": "https://slsa.dev/provenance/v1",
            "commit": COMMIT,
        },
        "trusted_builder": {
            "repository": BUILDER,
            "repository_id": BUILDER_ID,
            "workflow": BUILDER_WORKFLOW,
            "commit": BUILDER_COMMIT,
        },
    }


def validate(m=None, **overrides):
    args = dict(
        relying_repository=RELYING, relying_repository_id=RELYING_ID,
        trust_root_repository=ROOT, trust_root_repository_id=ROOT_ID,
        expected_signer_workflow=SIGNER_WORKFLOW, expected_signer_ref="refs/heads/main",
        expected_signer_commit=COMMIT, expected_builder_repository=BUILDER,
        expected_builder_repository_id=BUILDER_ID, expected_builder_workflow=BUILDER_WORKFLOW,
        expected_builder_commit=BUILDER_COMMIT, now=NOW,
    )
    args.update(overrides)
    return validate_manifest(manifest() if m is None else m, **args)


class ExternalTrustRootTests(unittest.TestCase):
    def test_valid_manifest_accepted_but_builder_not_claimed_active(self):
        report = validate()
        self.assertEqual(report["status"], "TRUST_ROOT_POLICY_VALID")
        self.assertEqual(report["builder_integration_status"],
                         "AUTHORIZED_BY_ROOT_BUT_NOT_YET_USED_BY_CURRENT_PRODUCER")

    def test_unknown_manifest_field_rejected(self):
        m = manifest(); m["allow_any_signer"] = True
        with self.assertRaises(TrustRootError): validate(m)

    def test_missing_manifest_field_rejected(self):
        m = manifest(); del m["trusted_builder"]
        with self.assertRaises(TrustRootError): validate(m)

    def test_wrong_relying_party_repository_rejected(self):
        m = manifest(); m["relying_party"]["repository"] = "attacker/repo"
        with self.assertRaises(TrustRootError): validate(m)

    def test_wrong_relying_party_numeric_id_rejected(self):
        m = manifest(); m["relying_party"]["repository_id"] += 1
        with self.assertRaises(TrustRootError): validate(m)

    def test_trust_root_must_be_external(self):
        with self.assertRaises(TrustRootError):
            validate(trust_root_repository=RELYING)

    def test_wrong_signer_workflow_rejected(self):
        m = manifest(); m["authorized_signer"]["workflow"] = "attacker/repo/.github/workflows/x.yml"
        with self.assertRaises(TrustRootError): validate(m)

    def test_wrong_signer_commit_rejected(self):
        with self.assertRaises(TrustRootError): validate(expected_signer_commit="c" * 40)

    def test_wrong_oidc_issuer_rejected(self):
        m = manifest(); m["authorized_signer"]["oidc_issuer"] = "https://attacker.invalid"
        with self.assertRaises(TrustRootError): validate(m)

    def test_wrong_predicate_rejected(self):
        m = manifest(); m["authorized_signer"]["predicate_type"] = "https://attacker.invalid"
        with self.assertRaises(TrustRootError): validate(m)

    def test_expired_manifest_rejected(self):
        with self.assertRaises(TrustRootError):
            validate(now=datetime(2028, 1, 1, tzinfo=timezone.utc))

    def test_not_yet_valid_manifest_rejected(self):
        m = manifest(); m["issued_at"] = "2027-01-01T00:00:00Z"
        with self.assertRaises(TrustRootError): validate(m)

    def test_reversed_validity_interval_rejected(self):
        m = manifest(); m["expires_at"] = "2026-11-16T00:00:00Z"
        with self.assertRaises(TrustRootError): validate(m)

    def test_boolean_sequence_rejected_as_integer(self):
        m = manifest(); m["sequence"] = True
        with self.assertRaises(TrustRootError): validate(m)

    def test_wrong_builder_repository_rejected(self):
        with self.assertRaises(TrustRootError):
            validate(expected_builder_repository="attacker/builder")

    def test_builder_cannot_be_relying_party(self):
        m = manifest(); m["trusted_builder"]["repository"] = RELYING
        with self.assertRaises(TrustRootError): validate(m)

    def test_builder_cannot_be_trust_root(self):
        m = manifest(); m["trusted_builder"]["repository"] = ROOT
        with self.assertRaises(TrustRootError): validate(m)

    def test_wrong_builder_commit_rejected(self):
        with self.assertRaises(TrustRootError):
            validate(expected_builder_commit="d" * 40)

    def test_duplicate_json_key_rejected(self):
        from external_trust_root import _unique_object
        with self.assertRaises(TrustRootError):
            json.loads('{"sequence":1,"sequence":2}', object_pairs_hook=_unique_object)

    def test_full_ed25519_package_verifies(self):
        if not all(subprocess.run(["sh", "-c", f"command -v {x} >/dev/null"], check=False).returncode == 0
                   for x in ("git", "openssl")):
            self.skipTest("git and openssl are required")
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "root"; root.mkdir()
            subprocess.run(["git", "init", str(root)], check=True, capture_output=True)
            subprocess.run(["git", "-C", str(root), "config", "user.email", "test@example.invalid"], check=True)
            subprocess.run(["git", "-C", str(root), "config", "user.name", "Test"], check=True)
            subprocess.run(["git", "-C", str(root), "remote", "add", "origin",
                            "https://github.com/" + ROOT + ".git"], check=True)
            mbytes = json.dumps(manifest(), sort_keys=True, separators=(",", ":")).encode()
            (root / "trust-root.json").write_bytes(mbytes)
            subprocess.run(["openssl", "genpkey", "-algorithm", "ED25519", "-out", str(Path(td) / "private.pem")],
                           check=True, capture_output=True)
            subprocess.run(["openssl", "pkey", "-in", str(root / "private.pem"), "-pubout",
                            "-out", str(root / "trust-root.pub")], check=True, capture_output=True)
            subprocess.run(["openssl", "pkeyutl", "-sign", "-inkey", str(root / "private.pem"),
                            "-rawin", "-in", str(root / "trust-root.json"),
                            "-out", str(root / "trust-root.sig")], check=True, capture_output=True)
            subprocess.run(["git", "-C", str(root), "add", "trust-root.json", "trust-root.pub",
                            "trust-root.sig"], check=True)
            subprocess.run(["git", "-C", str(root), "commit", "-m", "test trust root"], check=True,
                           capture_output=True)
            commit = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"],
                                    check=True, capture_output=True, text=True).stdout.strip()
            pub = (root / "trust-root.pub").read_bytes()
            report = verify_package(
                root, trust_root_repository=ROOT, trust_root_repository_id=ROOT_ID,
                trust_root_commit=commit, manifest_path="trust-root.json",
                signature_path="trust-root.sig", public_key_path="trust-root.pub",
                expected_manifest_sha256=hashlib.sha256(mbytes).hexdigest(),
                expected_public_key_sha256=hashlib.sha256(pub).hexdigest(),
                relying_repository=RELYING, relying_repository_id=RELYING_ID,
                expected_signer_workflow=SIGNER_WORKFLOW, expected_signer_ref="refs/heads/main",
                expected_signer_commit=COMMIT, expected_builder_repository=BUILDER,
                expected_builder_repository_id=BUILDER_ID, expected_builder_workflow=BUILDER_WORKFLOW,
                expected_builder_commit=BUILDER_COMMIT)
            self.assertEqual(report["signature_verification"], "VERIFIED")
            self.assertEqual(report["trust_root_commit"], commit)

    def test_tampered_manifest_digest_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            subprocess.run(["git", "init", str(root)], check=True, capture_output=True)
            subprocess.run(["git", "-C", str(root), "config", "user.email", "test@example.invalid"], check=True)
            subprocess.run(["git", "-C", str(root), "config", "user.name", "Test"], check=True)
            subprocess.run(["git", "-C", str(root), "remote", "add", "origin",
                            "https://github.com/" + ROOT + ".git"], check=True)
            (root / "trust-root.json").write_text(json.dumps(manifest()))
            (root / "trust-root.sig").write_bytes(b"not-a-signature")
            (root / "trust-root.pub").write_bytes(b"not-a-public-key")
            subprocess.run(["git", "-C", str(root), "add", "."], check=True)
            subprocess.run(["git", "-C", str(root), "commit", "-m", "tampered root"], check=True,
                           capture_output=True)
            commit = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"],
                                    check=True, capture_output=True, text=True).stdout.strip()
            with self.assertRaisesRegex(TrustRootError, "manifest digest mismatch"):
                verify_package(
                    root, trust_root_repository=ROOT, trust_root_repository_id=ROOT_ID,
                    trust_root_commit=commit, manifest_path="trust-root.json",
                    signature_path="trust-root.sig", public_key_path="trust-root.pub",
                    expected_manifest_sha256="0" * 64,
                    expected_public_key_sha256=hashlib.sha256(b"not-a-public-key").hexdigest(),
                    relying_repository=RELYING, relying_repository_id=RELYING_ID,
                    expected_signer_workflow=SIGNER_WORKFLOW, expected_signer_ref="refs/heads/main",
                    expected_signer_commit=COMMIT, expected_builder_repository=BUILDER,
                    expected_builder_repository_id=BUILDER_ID, expected_builder_workflow=BUILDER_WORKFLOW,
                    expected_builder_commit=BUILDER_COMMIT)


if __name__ == "__main__":
    unittest.main(verbosity=2)
