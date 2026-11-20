import unittest

from paper_a_ambiguous_anchor_retry_gate import authorize_ambiguous_anchor_retry


class AmbiguousAnchorRetryGateTests(unittest.TestCase):
    def setUp(self):
        self.previous = 5
        self.digest = "a" * 64
        self.recovery = {
            "status": "NOT_COMMITTED",
            "anchor_sequence": self.previous,
            "snapshot_sha256": self.digest,
        }

    def decide(self, **kwargs):
        args = dict(
            recovery_result=self.recovery,
            expected_previous_sequence=self.previous,
            expected_previous_digest=self.digest,
            intended_sequence=6,
            externally_held_minimum_sequence=5,
            caller_freshly_revalidated=True,
        )
        args.update(kwargs)
        return authorize_ambiguous_anchor_retry(**args)

    def test_fresh_revalidated_exact_next_sequence_is_candidate_only(self):
        result = self.decide()
        self.assertEqual(result["decision"], "RETRY_CANDIDATE")
        self.assertFalse(result["retry"])
        self.assertFalse(result["execution_performed"])
        self.assertTrue(result["requires_writer_cas"])

    def test_no_fresh_revalidation_denies(self):
        result = self.decide(caller_freshly_revalidated=False)
        self.assertEqual(result["decision"], "DENY_RETRY")

    def test_committed_state_blocks_duplicate_retry(self):
        result = self.decide(recovery_result={**self.recovery, "status": "COMMITTED"})
        self.assertEqual(result["decision"], "DENY_RETRY")
        self.assertIn("duplicate", result["reason"])

    def test_indeterminate_state_denies(self):
        result = self.decide(recovery_result={**self.recovery, "status": "INDETERMINATE"})
        self.assertEqual(result["decision"], "DENY_RETRY")

    def test_sequence_jump_denies(self):
        result = self.decide(intended_sequence=7)
        self.assertEqual(result["decision"], "DENY_RETRY")

    def test_floor_above_previous_denies(self):
        result = self.decide(externally_held_minimum_sequence=6)
        self.assertEqual(result["decision"], "DENY_RETRY")

    def test_mismatched_observed_sequence_denies(self):
        result = self.decide(recovery_result={**self.recovery, "anchor_sequence": 4})
        self.assertEqual(result["decision"], "DENY_RETRY")

    def test_mismatched_observed_digest_denies(self):
        result = self.decide(recovery_result={**self.recovery, "snapshot_sha256": "b" * 64})
        self.assertEqual(result["decision"], "DENY_RETRY")

    def test_bool_sequence_rejected(self):
        result = self.decide(expected_previous_sequence=True)
        self.assertEqual(result["decision"], "DENY_RETRY")

    def test_non_mapping_recovery_denied(self):
        result = self.decide(recovery_result=None)
        self.assertEqual(result["decision"], "DENY_RETRY")


if __name__ == "__main__":
    unittest.main()
