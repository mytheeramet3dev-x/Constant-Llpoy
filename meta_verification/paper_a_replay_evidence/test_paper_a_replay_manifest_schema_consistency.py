"""Schema/validator consistency checks using the standard library (no jsonschema dependency)."""
import json
import unittest
from pathlib import Path

SCHEMA_PATH = Path(__file__).with_name("paper_a_replay_manifest.schema.json")

class SchemaConsistencyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    def test_schema_version_and_project_match_validator(self):
        self.assertEqual(self.schema["properties"]["schema_version"]["const"], "1.0")
        self.assertEqual(self.schema["properties"]["project"]["const"], "Paper A")
    def test_commit_and_digest_patterns(self):
        self.assertEqual(self.schema["properties"]["git_commit"]["pattern"], "^[0-9a-f]{40}$")
        self.assertEqual(self.schema["properties"]["inputs"]["items"]["properties"]["sha256"]["pattern"], "^[0-9a-f]{64}$")
        self.assertEqual(self.schema["properties"]["artifacts"]["items"]["properties"]["sha256"]["pattern"], "^[0-9a-f]{64}$")
    def test_check_statuses_match_validator(self):
        self.assertEqual(set(self.schema["properties"]["checks"]["items"]["properties"]["status"]["enum"]),
                         {"PASS", "FAIL", "INCONCLUSIVE", "NOT_RUN"})
    def test_timestamp_schema_explicitly_utc(self):
        pattern = self.schema["properties"]["run_timestamp_utc"]["pattern"]
        self.assertIn("+00:00", pattern)
        self.assertIn("Z", pattern)
    def test_paths_and_check_ids_nonempty(self):
        self.assertEqual(self.schema["properties"]["inputs"]["items"]["properties"]["path"]["minLength"],1)
        self.assertEqual(self.schema["properties"]["artifacts"]["items"]["properties"]["path"]["minLength"],1)
        self.assertEqual(self.schema["properties"]["checks"]["items"]["properties"]["check_id"]["minLength"],1)
if __name__ == "__main__": unittest.main()
