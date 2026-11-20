import os, tempfile, threading, unittest

from paper_a_retry_intent_ticket import (
    issue_retry_intent_ticket, redeem_retry_intent_ticket,
)
from paper_a_persistent_replay_guard import PersistentReplayGuard


class RetryIntentTicketTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = os.path.join(self.tmp.name, "replay.sqlite")
        self.secret = b"retry-intent-ticket-test-secret-32bytes"
        self.keys = {"key-test": self.secret}
        self.previous = 12
        self.digest = "c" * 64
        self.ticket = self.make_ticket("nonce-single-use-001")
        self.guard = PersistentReplayGuard(self.db)

    def tearDown(self):
        self.tmp.cleanup()

    def make_ticket(self, nonce, **kwargs):
        args = dict(key_id="key-test", nonce=nonce,
                    expected_previous_sequence=self.previous,
                    expected_previous_digest=self.digest,
                    intended_sequence=13, secret=self.secret)
        args.update(kwargs)
        return issue_retry_intent_ticket(**args)

    def redeem(self, ticket=None, **kwargs):
        args = dict(ticket=self.ticket, trusted_keys=self.keys,
                    expected_previous_sequence=self.previous,
                    expected_previous_digest=self.digest, intended_sequence=13,
                    replay_guard=self.guard)
        if ticket is not None:
            args["ticket"] = ticket
        args.update(kwargs)
        return redeem_retry_intent_ticket(**args)

    def test_valid_ticket_redeems_once_but_does_not_execute(self):
        result = self.redeem()
        self.assertEqual(result["status"], "REDEEMED")
        self.assertTrue(result["single_use"])
        self.assertFalse(result["execution_performed"])
        self.assertTrue(result["requires_writer_cas"])

    def test_second_redemption_denied(self):
        self.assertEqual(self.redeem()["status"], "REDEEMED")
        self.assertEqual(self.redeem()["status"], "DENY")

    def test_tampered_mac_denied(self):
        tampered = dict(self.ticket, hmac_sha256="0" * 64)
        self.assertEqual(self.redeem(tampered)["status"], "DENY")

    def test_expectation_mismatch_denied(self):
        self.assertEqual(self.redeem(expected_previous_sequence=11)["status"], "DENY")

    def test_untrusted_key_denied(self):
        self.assertEqual(self.redeem(trusted_keys={})["status"], "DENY")

    def test_sequence_jump_cannot_be_issued(self):
        with self.assertRaises(ValueError):
            self.make_ticket("nonce-seq-jump-001", intended_sequence=14)

    def test_bool_sequence_rejected(self):
        with self.assertRaises(ValueError):
            self.make_ticket("nonce-bool-001", expected_previous_sequence=True,
                           intended_sequence=2)

    def test_concurrent_redemption_allows_exactly_one_ticket_consumer(self):
        workers = 8
        barrier = threading.Barrier(workers)
        outcomes = []
        lock = threading.Lock()

        def worker():
            local_guard = PersistentReplayGuard(self.db)
            barrier.wait(timeout=10)
            result = redeem_retry_intent_ticket(
                ticket=self.ticket, trusted_keys=self.keys,
                expected_previous_sequence=self.previous,
                expected_previous_digest=self.digest,
                intended_sequence=13, replay_guard=local_guard)
            with lock:
                outcomes.append(result["status"])

        threads = [threading.Thread(target=worker) for _ in range(workers)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join(timeout=20)

        self.assertTrue(all(not thread.is_alive() for thread in threads),
                        "concurrent redemption worker timed out")
        self.assertEqual(outcomes.count("REDEEMED"), 1)
        self.assertEqual(outcomes.count("DENY"), workers - 1)

    def test_bool_expected_sequence_is_rejected(self):
        self.assertEqual(self.redeem(expected_previous_sequence=True)["status"], "DENY")

    def test_malformed_expected_digest_is_rejected(self):
        self.assertEqual(self.redeem(expected_previous_digest="z" * 64)["status"], "DENY")

    def test_expected_sequence_jump_is_rejected(self):
        self.assertEqual(self.redeem(expected_previous_sequence=12, intended_sequence=14)["status"], "DENY")

    def test_unexpected_replay_guard_exception_fails_closed(self):
        class BrokenReplayGuard:
            def consume(self, *args, **kwargs):
                raise RuntimeError("simulated unexpected adapter failure")

        result = redeem_retry_intent_ticket(
            ticket=self.ticket, trusted_keys=self.keys,
            expected_previous_sequence=self.previous,
            expected_previous_digest=self.digest, intended_sequence=13,
            replay_guard=BrokenReplayGuard())
        self.assertEqual(result["status"], "DENY")
        self.assertFalse(result.get("execution_performed", False))

    def test_nonce_scoped_to_key(self):
        other_keys = {"key-other": self.secret}
        # Key change invalidates MAC; issue correctly under alternate key.
        other_ticket = issue_retry_intent_ticket(
            key_id="key-other", nonce="nonce-scope-001",
            expected_previous_sequence=12, expected_previous_digest=self.digest,
            intended_sequence=13, secret=self.secret)
        result = redeem_retry_intent_ticket(
            ticket=other_ticket, trusted_keys=other_keys,
            expected_previous_sequence=12, expected_previous_digest=self.digest,
            intended_sequence=13, replay_guard=self.guard)
        self.assertEqual(result["status"], "REDEEMED")


if __name__ == "__main__":
    unittest.main()
