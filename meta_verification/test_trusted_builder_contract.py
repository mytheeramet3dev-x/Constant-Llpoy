#!/usr/bin/env python3
"""Structural regression tests for the trusted-builder contract artifacts."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCHEMA_PATH = ROOT / "trusted_builder_report.schema.json"
CONTRACT_PATH = ROOT / "TRUSTED_BUILDER_CONTRACT.md"
BOOTSTRAP_PATH = ROOT / "EXTERNAL_TRUST_ROOT_BOOTSTRAP.md"


class TrustedBuilderContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        cls.contract = CONTRACT_PATH.read_text(encoding="utf-8")
        cls.bootstrap = BOOTSTRAP_PATH.read_text(encoding="utf-8")

    def test_schema_is_draft_2020_12(self):
        self.assertEqual(self.schema["$schema"], "https://json-schema.org/draft/2020-12/schema")

    def test_schema_rejects_unknown_top_level_fields(self):
        self.assertIs(self.schema["additionalProperties"], False)

    def test_schema_requires_builder_caller_source_subject_and_attestation(self):
        self.assertEqual(set(self.schema["required"]), {
            "schema_version", "status", "builder", "caller",
            "source_commit", "subject", "attestation"
        })

    def test_builder_identity_requires_full_immutable_commit(self):
        props = self.schema["properties"]["builder"]["properties"]
        self.assertEqual(props["workflow_commit"]["pattern"], "^[0-9a-f]{40}$")
        self.assertIn("repository_id", self.schema["properties"]["builder"]["required"])

    def test_subject_digest_is_sha256(self):
        props = self.schema["properties"]["subject"]["properties"]
        self.assertEqual(props["sha256"]["pattern"], "^[0-9a-f]{64}$")

    def test_attestation_type_and_oidc_issuer_are_fixed(self):
        props = self.schema["properties"]["attestation"]["properties"]
        self.assertEqual(props["predicate_type"]["const"], "https://slsa.dev/provenance/v1")
        self.assertEqual(props["oidc_issuer"]["const"], "https://token.actions.githubusercontent.com")

    def test_contract_prohibits_floating_refs_and_caller_predicate_override(self):
        self.assertIn("floating action or workflow reference", self.contract)
        self.assertIn("caller to override predicate type or signer identity", self.contract)

    def test_contract_requires_independent_attestation_verification(self):
        self.assertIn("independently retrieve the attestation", self.contract)
        self.assertIn("independent reviewer", self.contract.lower())

    def test_contract_explicitly_marks_builder_inactive_until_gates_pass(self):
        self.assertIn("**NOT ACTIVE**", self.contract)
        self.assertIn("no external builder is provisioned or trusted yet", self.contract)

    def test_bootstrap_links_contract_and_schema(self):
        self.assertIn("TRUSTED_BUILDER_CONTRACT.md", self.bootstrap)
        self.assertIn("trusted_builder_report.schema.json", self.bootstrap)


if __name__ == "__main__":
    unittest.main()
