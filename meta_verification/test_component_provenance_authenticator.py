"""Black-box tests for direct component-artifact attestation authentication."""
import base64, hashlib, json, subprocess, unittest
from component_provenance_authenticator import (
    ComponentProvenanceError, authenticate_components,
)

REPO="mytheeramet3dev-x/Constant-Llpoy"
REPO_ID=1460417275
COMMIT="a"*40
POLICY_REV="b"*40
RUNS={"C1":(123,1),"C2":(456,2)}

def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(",",":")).encode()

def provenance_policy():
    return {
      "schema_version":"1.0","repository":REPO,"repository_id":REPO_ID,
      "signer_workflow":REPO+"/.github/workflows/meta-verification-evidence.yml",
      "source_ref":"refs/heads/main","oidc_issuer":"https://token.actions.githubusercontent.com",
      "predicate_type":"https://slsa.dev/provenance/v1","require_verified_timestamps":True,
      "deny_self_hosted_runners":True,"gh_cli_version":"2.103.3"
    }

def fixture():
    policy={"schema_version":"1.0","claim_id":"CLAIM-A","policy_revision":POLICY_REV,
            "required_components":["C1","C2"]}
    components=[]
    for cid,payload in (("C1",b"evidence one"),("C2",b"evidence two")):
        run_id,attempt=RUNS[cid]
        digest=hashlib.sha256(payload).hexdigest()
        components.append({
          "component_id":cid,"status":"PASS",
          "evidence_base64":base64.b64encode(payload).decode(),
          "evidence_sha256":digest,
          "provenance":{"receipt_schema_version":"2.0","subject_sha256":digest,
            "source_commit":COMMIT,"attestation_run_id":run_id,
            "attestation_run_attempt":attempt,"attestation_workflow_revision":COMMIT}
        })
    bundle={"schema_version":"1.0","claim_id":"CLAIM-A","source_commit":COMMIT,
            "policy_revision":POLICY_REV,"components":components}
    return canonical(policy),policy,canonical(provenance_policy()),provenance_policy(),bundle

class FakeRunner:
    def __init__(self, mode=None):
        self.mode=mode
        self.commands=[]
    def __call__(self, command, **kwargs):
        self.commands.append(command)
        if command[:2]==["gh","version"]:
            return subprocess.CompletedProcess(command,0,"gh version 2.103.3 (test)\n","")
        if self.mode=="gh_failure":
            return subprocess.CompletedProcess(command,1,"","no attestation")
        path=command[3]
        cid=path.rsplit("/",1)[-1].split(".",1)[0]
        raw=open(path,"rb").read()
        digest=hashlib.sha256(raw).hexdigest()
        run_id,attempt=RUNS[cid]
        invocation=f"https://github.com/{REPO}/actions/runs/{run_id}/attempts/{attempt}"
        if self.mode=="wrong_invocation": invocation+="0"
        cert={
          "sourceRepositoryIdentifier":str(REPO_ID),"sourceRepositoryRef":"refs/heads/main",
          "sourceRepositoryDigest":COMMIT,"buildSignerDigest":COMMIT
        }
        if self.mode=="wrong_signer": cert["sourceRepositoryIdentifier"]="999"
        statement={"predicateType":"https://slsa.dev/provenance/v1",
          "subject":[{"name":cid+".evidence","digest":{"sha256":digest}}],
          "predicate":{"runDetails":{"metadata":{"invocationId":invocation}}}}
        output=[{"verificationResult":{"signature":{"certificate":cert},
          "verifiedTimestamps":[{"kind":"rekor","integratedTime":1}],"statement":statement}}]
        if self.mode=="no_attestation": output=[]
        if self.mode=="wrong_subject": output[0]["verificationResult"]["statement"]["subject"][0]["digest"]["sha256"]="0"*64
        return subprocess.CompletedProcess(command,0,json.dumps(output),"")
        
class ComponentProvenanceTests(unittest.TestCase):
    def run_auth(self, mode=None, pin=None, bundle=None, policy_bytes=None):
        pb,policy,ppb,pp,b=fixture()
        runner=FakeRunner(mode)
        result=authenticate_components(policy_bytes or pb,ppb,pp,bundle or b,COMMIT,
            pin if pin is not None else hashlib.sha256(ppb).hexdigest(),runner=runner)
        return result,runner
    def test_all_required_subjects_authenticated_directly(self):
        result,runner=self.run_auth()
        self.assertEqual(set(result),{"C1","C2"})
        self.assertEqual(result["C1"]["attestation_run_id"],123)
        self.assertEqual(result["C2"]["attestation_run_attempt"],2)
        self.assertEqual(sum(1 for x in runner.commands if x[:3]==["gh","attestation","verify"]),2)
        command=next(x for x in runner.commands if x[:3]==["gh","attestation","verify"])
        for flag in ("--repo","--signer-workflow","--cert-oidc-issuer","--predicate-type",
                     "--source-ref","--source-digest","--signer-digest","--deny-self-hosted-runners"):
            self.assertIn(flag,command)
        self.assertEqual(command[command.index("--signer-workflow")+1],provenance_policy()["signer_workflow"])
    def test_missing_external_policy_pin_rejected(self):
        pb,p,ppb,pp,b=fixture()
        with self.assertRaisesRegex(ComponentProvenanceError,"missing or malformed"):
            authenticate_components(pb,ppb,pp,b,COMMIT,"",runner=FakeRunner())
    def test_policy_digest_tamper_rejected(self):
        pb,p,ppb,pp,b=fixture()
        with self.assertRaisesRegex(ComponentProvenanceError,"differ from external pin"):
            authenticate_components(pb,ppb+b" ",pp,b,COMMIT,hashlib.sha256(ppb).hexdigest(),runner=FakeRunner())
    def test_invalid_utf8_aggregation_policy_rejected(self):
        pb,p,ppb,pp,b=fixture()
        with self.assertRaisesRegex(ComponentProvenanceError,"not UTF-8"):
            authenticate_components(b"\xff",ppb,pp,b,COMMIT,hashlib.sha256(ppb).hexdigest(),runner=FakeRunner())
    def test_receipt_run_attempt_boolean_rejected(self):
        pb,p,ppb,pp,b=fixture(); b["components"][0]["provenance"]["attestation_run_attempt"]=True
        with self.assertRaisesRegex(ComponentProvenanceError,"positive integer"):
            authenticate_components(pb,ppb,pp,b,COMMIT,hashlib.sha256(ppb).hexdigest(),runner=FakeRunner())
    def test_receipt_run_id_boolean_rejected(self):
        pb,p,ppb,pp,b=fixture(); b["components"][0]["provenance"]["attestation_run_id"]=True
        with self.assertRaisesRegex(ComponentProvenanceError,"positive integer"):
            authenticate_components(pb,ppb,pp,b,COMMIT,hashlib.sha256(ppb).hexdigest(),runner=FakeRunner())
    def test_receipt_workflow_revision_must_match_source(self):
        pb,p,ppb,pp,b=fixture(); b["components"][0]["provenance"]["attestation_workflow_revision"]="f"*40
        with self.assertRaisesRegex(ComponentProvenanceError,"workflow revision"):
            authenticate_components(pb,ppb,pp,b,COMMIT,hashlib.sha256(ppb).hexdigest(),runner=FakeRunner())
    def test_provenance_policy_object_must_match_pinned_bytes(self):
        pb,p,ppb,pp,b=fixture(); altered=dict(pp); altered["repository_id"]=999
        with self.assertRaisesRegex(ComponentProvenanceError,"object does not match"):
            authenticate_components(pb,ppb,altered,b,COMMIT,hashlib.sha256(ppb).hexdigest(),runner=FakeRunner())
    def test_declared_evidence_digest_must_match_subject_bytes(self):
        pb,p,ppb,pp,b=fixture(); b["components"][0]["evidence_sha256"]="0"*64
        with self.assertRaisesRegex(ComponentProvenanceError,"evidence digest mismatch"):
            authenticate_components(pb,ppb,pp,b,COMMIT,hashlib.sha256(ppb).hexdigest(),runner=FakeRunner())
    def test_invocation_id_must_bind_run_id_and_attempt(self):
        with self.assertRaisesRegex(ComponentProvenanceError,"invocationId"):
            self.run_auth("wrong_invocation")
    def test_wrong_signer_certificate_rejected(self):
        with self.assertRaisesRegex(ComponentProvenanceError,"repository ID mismatch"):
            self.run_auth("wrong_signer")
    def test_no_attestation_rejected(self):
        with self.assertRaisesRegex(ComponentProvenanceError,"no verified attestations"):
            self.run_auth("no_attestation")
    def test_gh_failure_rejected(self):
        with self.assertRaisesRegex(ComponentProvenanceError,"rejected provenance"):
            self.run_auth("gh_failure")
    def test_wrong_subject_digest_rejected(self):
        with self.assertRaisesRegex(ComponentProvenanceError,"subject"):
            self.run_auth("wrong_subject")
    def test_duplicate_component_receipt_rejected(self):
        pb,p,ppb,pp,b=fixture(); b["components"].append(dict(b["components"][0]))
        with self.assertRaisesRegex(ComponentProvenanceError,"duplicate component"):
            authenticate_components(pb,ppb,pp,b,COMMIT,hashlib.sha256(ppb).hexdigest(),runner=FakeRunner())
    def test_missing_component_receipt_rejected(self):
        pb,p,ppb,pp,b=fixture(); b["components"].pop()
        with self.assertRaisesRegex(ComponentProvenanceError,"component set mismatch"):
            authenticate_components(pb,ppb,pp,b,COMMIT,hashlib.sha256(ppb).hexdigest(),runner=FakeRunner())

if __name__=="__main__": unittest.main(verbosity=2)
