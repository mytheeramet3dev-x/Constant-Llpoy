"""Independent semantic validation regression tests (stdlib only)."""
import hashlib
import unittest
from paper_a_replay_manifest_validate import validate_manifest

class ManifestValidatorTests(unittest.TestCase):
    def base(self):
        return {
            "schema_version":"1.0", "project":"Paper A", "git_commit":"a"*40,
            "run_timestamp_utc":"2026-11-21T00:00:00+00:00",
            "environment":{"python_version":"3.12","platform":"test","dependencies":{"numpy":"2.0"}},
            "command":"python replay.py", "inputs":[], "artifacts":[],
            "checks":[{"check_id":"replay","status":"PASS","details":"test"}],
            "scope":"fixed-point replay only", "limitations":["not proof"]
        }
    def test_valid_manifest(self):
        self.assertTrue(validate_manifest(self.base()))
    def test_duplicate_check_ids_rejected(self):
        m=self.base(); m["checks"].append(dict(m["checks"][0]))
        with self.assertRaises(ValueError): validate_manifest(m)
    def test_unknown_field_rejected(self):
        m=self.base(); m["extra"]="tampering"
        with self.assertRaises(ValueError): validate_manifest(m)
    def test_non_utc_timestamp_rejected(self):
        m=self.base(); m["run_timestamp_utc"]="2026-11-21T08:00:00+08:00"
        with self.assertRaises(ValueError): validate_manifest(m)
    def test_malformed_hash_rejected(self):
        m=self.base(); m["inputs"]=[{"path":"input.txt","sha256":"123"}]
        with self.assertRaises(ValueError): validate_manifest(m)
    def test_file_hash_verified(self):
        import tempfile
        from pathlib import Path
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"input.txt"; p.write_text("content",encoding="utf-8")
            m=self.base(); m["inputs"]=[{"path":str(p),"sha256":hashlib.sha256(b"content").hexdigest()}]
            self.assertTrue(validate_manifest(m,verify_files=True))
            p.write_text("changed",encoding="utf-8")
            with self.assertRaises(ValueError): validate_manifest(m,verify_files=True)
    def test_empty_scope_rejected(self):
        m=self.base(); m["scope"]=" "
        with self.assertRaises(ValueError): validate_manifest(m)

if __name__=="__main__":
    unittest.main()
