import unittest, hmac, hashlib
from paper_a_provenance_hmac import canonical_payload
from paper_a_provenance_trust import InMemoryReplayGuard, ReplayDetected, TrustPolicyError, verify_with_trust_policy

KEY=b"trusted-test-secret-material-32-bytes-long"
BASE={"evaluation_id":"e-15","evidence_bundle_sha256":"a"*64,"policy_sha256":"b"*64,"verifier_id":"test-verifier","verifier_version":"v1","environment_id":"ci","result_record_sha256":"c"*64,"key_id":"test-key-1","nonce":"nonce-1234567890abcdef","issued_at":1000,"status":"PASS","certification":"NOT_PERFORMED"}
def mac(r): return hmac.new(KEY,canonical_payload(r),hashlib.sha256).hexdigest()
TRUST={"test-key-1":{"secret":KEY,"revoked":False}}

class TrustPolicyTests(unittest.TestCase):
 def test_valid_record(self):
  out=verify_with_trust_policy(BASE,mac(BASE),TRUST,InMemoryReplayGuard(),now=1001)
  self.assertTrue(out["authenticated"])
  self.assertEqual(out["certification"],"NOT_PERFORMED")
 def test_unknown_key(self):
  r=dict(BASE,key_id="unlisted")
  with self.assertRaises(TrustPolicyError):
   verify_with_trust_policy(r,mac(r),TRUST,InMemoryReplayGuard(),now=1000)
 def test_revoked_key(self):
  k={"test-key-1":{"secret":KEY,"revoked":True}}
  with self.assertRaises(TrustPolicyError):
   verify_with_trust_policy(BASE,mac(BASE),k,InMemoryReplayGuard(),now=1000)
 def test_tamper(self):
  r=dict(BASE,status="FAIL")
  with self.assertRaises(TrustPolicyError):
   verify_with_trust_policy(r,mac(BASE),TRUST,InMemoryReplayGuard(),now=1000)
 def test_expired(self):
  with self.assertRaises(TrustPolicyError):
   verify_with_trust_policy(BASE,mac(BASE),TRUST,InMemoryReplayGuard(),now=2000,max_age_seconds=100)
 def test_future(self):
  with self.assertRaises(TrustPolicyError):
   verify_with_trust_policy(BASE,mac(BASE),TRUST,InMemoryReplayGuard(),now=900)
 def test_replay(self):
  g=InMemoryReplayGuard()
  verify_with_trust_policy(BASE,mac(BASE),TRUST,g,now=1000)
  with self.assertRaises(ReplayDetected):
   verify_with_trust_policy(BASE,mac(BASE),TRUST,g,now=1000)
 def test_short_nonce(self):
  r=dict(BASE,nonce="tiny")
  with self.assertRaises(TrustPolicyError):
   verify_with_trust_policy(r,mac(r),TRUST,InMemoryReplayGuard(),now=1000)
 def test_missing_metadata(self):
  r=dict(BASE)
  r.pop("issued_at")
  with self.assertRaises(TrustPolicyError):
   verify_with_trust_policy(r,mac(r),TRUST,InMemoryReplayGuard(),now=1000)
 def test_bool_timestamp(self):
  r=dict(BASE,issued_at=True)
  with self.assertRaises(TrustPolicyError):
   verify_with_trust_policy(r,mac(r),TRUST,InMemoryReplayGuard(),now=1000)

if __name__=="__main__": unittest.main()
