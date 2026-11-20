import os, tempfile, threading, unittest
from paper_a_persistent_replay_guard import (
    PersistentReplayGuard, PersistentReplayDetected, PersistentReplayError
)

class PersistentReplayGuardTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = os.path.join(self.tmp.name, "replay.sqlite3")
    def tearDown(self):
        self.tmp.cleanup()

    def test_replay_survives_reopen_and_new_evaluation_id(self):
        PersistentReplayGuard(self.db).consume("key-1", "eval-a", "nonce-1234567890")
        reopened = PersistentReplayGuard(self.db)
        with self.assertRaises(PersistentReplayDetected):
            reopened.consume("key-1", "eval-b", "nonce-1234567890")

    def test_nonce_scope_is_key_id(self):
        guard = PersistentReplayGuard(self.db)
        guard.consume("key-a", "eval-a", "nonce-1234567890")
        guard.consume("key-b", "eval-b", "nonce-1234567890")

    def test_concurrent_consumption_is_atomic(self):
        barrier = threading.Barrier(2)
        results = []
        lock = threading.Lock()
        def worker(eval_id):
            g = PersistentReplayGuard(self.db)
            barrier.wait()
            try:
                g.consume("key-1", eval_id, "shared-nonce-123456")
                outcome = "accepted"
            except PersistentReplayDetected:
                outcome = "rejected-replay"
            except PersistentReplayError:
                outcome = "storage-error"
            with lock:
                results.append(outcome)
        threads = [threading.Thread(target=worker, args=(f"eval-{i}",)) for i in range(2)]
        for t in threads: t.start()
        for t in threads: t.join(timeout=15)
        self.assertTrue(all(not t.is_alive() for t in threads), "worker timeout")
        self.assertCountEqual(results, ["accepted", "rejected-replay"])

    def test_empty_identifiers_rejected(self):
        with self.assertRaises(ValueError):
            PersistentReplayGuard(self.db).consume("", "eval", "nonce")

    def test_memory_database_disallowed(self):
        with self.assertRaises(ValueError):
            PersistentReplayGuard(":memory:")

    def test_storage_failure_fails_closed(self):
        # An existing directory is not a valid SQLite database file.
        bad = os.path.join(self.tmp.name, "bad.sqlite")
        os.mkdir(bad)
        with self.assertRaises(PersistentReplayError):
            PersistentReplayGuard(bad)

if __name__ == "__main__":
    unittest.main()
