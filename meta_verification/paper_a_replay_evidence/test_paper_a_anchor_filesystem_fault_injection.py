"""Real filesystem fault-injection tests for atomic anchor advancement (8.23).

These are controlled Python-level exceptions, not power-loss or kernel crash tests.
"""
import json
import os
import tempfile
import unittest
from unittest import mock

from paper_a_persistent_replay_guard import PersistentReplayGuard
from paper_a_replay_registry_audit import logical_snapshot
from paper_a_authenticated_registry_anchor import ANCHOR_SCHEMA, sign_anchor
import paper_a_atomic_anchor_advance as atomic
from paper_a_atomic_anchor_advance import advance_authenticated_anchor, AnchorAdvanceError


class AnchorFilesystemFaultInjectionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = os.path.join(self.tmp.name, "registry.sqlite")
        self.anchor_path = os.path.join(self.tmp.name, "anchor.json")
        self.guard = PersistentReplayGuard(self.db)
        self.secret = b"filesystem-fault-injection-test-key-32bytes"
        snap = logical_snapshot(self.db)
        fields = {
            "schema": ANCHOR_SCHEMA, "key_id": "key1", "sequence": 5,
            "snapshot_sha256": snap["snapshot_sha256"],
            "entry_count": snap["entry_count"],
        }
        self.anchor = {**fields, "mac_sha256": sign_anchor(fields, self.secret)}
        with open(self.anchor_path, "w", encoding="utf8") as stream:
            json.dump(self.anchor, stream)
        self.keys = {"key1": self.secret}

    def tearDown(self):
        self.tmp.cleanup()

    def call(self):
        return advance_authenticated_anchor(
            database_path=self.db, anchor_path=self.anchor_path,
            trusted_keys=self.keys, key_id="key1", secret=self.secret,
            externally_held_minimum_sequence=5,
            expected_current_sequence=5,
            expected_current_digest=self.anchor["snapshot_sha256"],
            new_sequence=6,
        )

    def read_bytes(self):
        with open(self.anchor_path, "rb") as stream:
            return stream.read()

    def test_file_fsync_failure_before_replace_preserves_original_anchor(self):
        original = self.read_bytes()
        with mock.patch.object(atomic.os, "fsync", side_effect=OSError("injected file fsync failure")):
            with self.assertRaisesRegex(OSError, "file fsync"):
                self.call()
        self.assertEqual(self.read_bytes(), original)
        self.assertEqual(json.loads(self.read_bytes())["sequence"], 5)

    def test_replace_failure_preserves_original_anchor_and_cleans_stage(self):
        original = self.read_bytes()
        with mock.patch.object(atomic.os, "replace", side_effect=OSError("injected replace failure")):
            with self.assertRaisesRegex(OSError, "replace failure"):
                self.call()
        self.assertEqual(self.read_bytes(), original)
        self.assertEqual(json.loads(self.read_bytes())["sequence"], 5)
        self.assertEqual([n for n in os.listdir(self.tmp.name) if n.startswith(".anchor-stage-")], [])

    def test_directory_fsync_failure_reports_uncertain_commit_but_new_anchor_visible(self):
        real_fsync = os.fsync
        count = {"calls": 0}
        def injected(fd):
            count["calls"] += 1
            if count["calls"] == 2:
                raise OSError("injected directory fsync failure")
            return real_fsync(fd)
        with mock.patch.object(atomic.os, "fsync", side_effect=injected):
            with self.assertRaisesRegex(OSError, "directory fsync failure"):
                self.call()
        # Replacement already happened. A raised error must not be interpreted as rollback.
        saved = json.loads(self.read_bytes())
        self.assertEqual(saved["sequence"], 6)
        self.assertEqual(count["calls"], 2)

    def test_readback_failure_occurs_after_anchor_replacement(self):
        original_read = atomic._read_anchor
        calls = {"count": 0}
        def injected(path):
            calls["count"] += 1
            if calls["count"] == 2:
                raise AnchorAdvanceError("injected read-back failure")
            return original_read(path)
        with mock.patch.object(atomic, "_read_anchor", side_effect=injected):
            with self.assertRaisesRegex(AnchorAdvanceError, "read-back failure"):
                self.call()
        self.assertEqual(json.loads(self.read_bytes())["sequence"], 6)
        self.assertEqual(calls["count"], 2)

    def test_staging_write_failure_keeps_original_anchor(self):
        original = self.read_bytes()
        class BrokenStream:
            def __init__(self, fd): self.fd = fd
            def __enter__(self): return self
            def __exit__(self, *args):
                os.close(self.fd)
                return False
            def write(self, data): raise OSError("injected staging write failure")
            def flush(self): return None
            def fileno(self): return self.fd
        with mock.patch.object(atomic.os, "fdopen", side_effect=lambda fd, mode="r", **kwargs: BrokenStream(fd)):
            with self.assertRaisesRegex(OSError, "staging write failure"):
                self.call()
        self.assertEqual(self.read_bytes(), original)
        self.assertEqual(json.loads(self.read_bytes())["sequence"], 5)


if __name__ == "__main__":
    unittest.main()
