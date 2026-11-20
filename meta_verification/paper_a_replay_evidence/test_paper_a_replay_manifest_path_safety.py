"""Adversarial tests for replay-manifest path safety primitives."""
import tempfile
import unittest
from pathlib import Path
from paper_a_replay_manifest_path_safety import resolve_safe_file, sha256_safe_file

class PathSafetyTests(unittest.TestCase):
    def test_relative_path_inside_workspace(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); f=root/"a.txt"; f.write_text("x")
            resolved=resolve_safe_file("a.txt",td)
            self.assertEqual(resolved,f.resolve())
    def test_parent_escape_rejected(self):
        with tempfile.TemporaryDirectory() as td, tempfile.TemporaryDirectory() as outside:
            (Path(outside)/"outside.txt").write_text("x")
            with self.assertRaises(ValueError):
                resolve_safe_file(str(Path(outside)/"outside.txt"),td)
    def test_symlink_rejected_when_supported(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); target=root/"target.txt"; target.write_text("target")
            link=root/"link.txt"
            try: link.symlink_to(target)
            except (OSError, NotImplementedError): self.skipTest("symlink unsupported")
            with self.assertRaises(ValueError): resolve_safe_file("link.txt",td)
    def test_directory_not_file_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            with self.assertRaises(ValueError): resolve_safe_file(".",td)
    def test_hash_output_is_canonical_path_and_digest(self):
        import hashlib
        with tempfile.TemporaryDirectory() as td:
            f=Path(td)/"sample"; f.write_bytes(b"abc")
            canonical,digest=sha256_safe_file("sample",td)
            self.assertEqual(canonical,str(f.resolve()))
            self.assertEqual(digest,hashlib.sha256(b"abc").hexdigest())
if __name__=="__main__": unittest.main()
