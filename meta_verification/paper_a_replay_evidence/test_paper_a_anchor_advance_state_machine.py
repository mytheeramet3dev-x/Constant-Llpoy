import unittest
from paper_a_anchor_advance_state_machine import State, transition, classify_interruption

class AnchorAdvanceStateMachineTests(unittest.TestCase):
 def test_valid_happy_path(self):
  s=State.STABLE
  for nxt in (State.STAGING,State.STAGED_DURABLE,State.REPLACED,State.READBACK_VERIFIED):
   s=transition(s,nxt)
  self.assertEqual(s,State.READBACK_VERIFIED)
  self.assertEqual(classify_interruption(s,final_anchor_authenticated=True,live_registry_matches=True),"PASS")
 def test_invalid_skipped_transition_rejected(self):
  with self.assertRaises(ValueError): transition(State.STABLE,State.REPLACED)
 def test_no_transition_after_readback(self):
  with self.assertRaises(ValueError): transition(State.READBACK_VERIFIED,State.STAGING)
 def test_crash_at_staging_indeterminate(self):
  for state in (State.STAGING,State.STAGED_DURABLE,State.REPLACED):
   self.assertEqual(classify_interruption(state,final_anchor_authenticated=True,live_registry_matches=True),"INDETERMINATE")
 def test_stage_artifact_prevents_pass(self):
  self.assertEqual(classify_interruption(State.STABLE,final_anchor_authenticated=True,live_registry_matches=True,stage_present=True),"FAIL_CLOSED")
 def test_replaced_without_verified_readback_not_pass(self):
  self.assertEqual(classify_interruption(State.REPLACED,final_anchor_authenticated=True,live_registry_matches=True),"INDETERMINATE")
 def test_aborted_never_passes(self):
  self.assertEqual(classify_interruption(State.ABORTED,final_anchor_authenticated=True,live_registry_matches=True),"INDETERMINATE")
 def test_readback_missing_authentication_fails_closed(self):
  self.assertEqual(classify_interruption(State.READBACK_VERIFIED,live_registry_matches=True),"FAIL_CLOSED")
if __name__=="__main__": unittest.main()
