"""Selected mutation-adequacy checks for the policy activation gate."""
from __future__ import annotations
import pathlib, shutil, subprocess, sys, tempfile, unittest

ROOT = pathlib.Path(__file__).resolve().parent
GATE = ROOT / "policy_activation_gate.py"
AGGREGATOR = ROOT / "status_aggregator.py"
AUTHENTICATOR = ROOT / "component_provenance_authenticator.py"
PROVENANCE_VERIFIER = ROOT / "verify_signed_provenance.py"
TESTS = ROOT / "test_policy_activation_gate.py"
MUTANTS = {
    "bypass_external_authority_pin": (
        'digest(authority_bytes) == expected_authority_sha256',
        'True'),
    "bypass_external_activation_pin": (
        'digest(activation_bytes) == expected_activation_sha256',
        'True'),
    "treat_authorized_as_active": (
        'record["status"] == "ACTIVE"',
        'record["status"] in {"ACTIVE", "AUTHORIZED"}'),
    "bypass_sequence_binding": (
        'record["sequence"] == expected_policy_sequence',
        'True'),
    "bypass_exact_policy_digest": (
        'record["policy_sha256"] == digest(policy_bytes)',
        'True'),
    "bypass_policy_object_byte_binding": (
        'parsed_policy == policy',
        'True'),
    "bypass_activation_expiry": (
        'issued < expires and issued <= now_epoch < expires',
        'True'),
    "lower_activation_signature_threshold": (
        'len(accepted) >= threshold',
        'len(accepted) >= 1'),
    "skip_ed25519_signature_verification": (
        'checked.returncode == 0',
        'True'),
}

class PolicyActivationMutationTests(unittest.TestCase):
    def test_each_activation_mutant_is_killed_by_gate_tests(self):
        source = GATE.read_text(encoding="utf-8")
        for name, (old, new) in MUTANTS.items():
            with self.subTest(mutant=name), tempfile.TemporaryDirectory() as td:
                root = pathlib.Path(td)
                self.assertIn(old, source, f"mutation anchor absent: {name}")
                mutated = source.replace(old, new, 1)
                (root / "policy_activation_gate.py").write_text(mutated, encoding="utf-8")
                shutil.copy2(AGGREGATOR, root / "status_aggregator.py")
                shutil.copy2(AUTHENTICATOR, root / "component_provenance_authenticator.py")
                shutil.copy2(PROVENANCE_VERIFIER, root / "verify_signed_provenance.py")
                shutil.copy2(TESTS, root / "test_policy_activation_gate.py")
                syntax = subprocess.run([sys.executable, "-m", "py_compile",
                                         str(root / "policy_activation_gate.py")],
                                        capture_output=True, text=True)
                self.assertEqual(syntax.returncode, 0, syntax.stderr)
                run = subprocess.run([sys.executable, "-m", "unittest", "-v",
                                      "test_policy_activation_gate"], cwd=root,
                                     capture_output=True, text=True)
                output = run.stdout + run.stderr
                self.assertNotEqual(run.returncode, 0, f"mutant survived: {name}")
                self.assertIn("FAIL:", output, f"failure was not assertion-driven: {name}\n{output}")
                print(f"ACTIVATION MUTANT KILLED: {name}")

if __name__ == "__main__":
    unittest.main(verbosity=2)
