import subprocess, sys, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "working" / "paper-a" / "finite_n_strong_coupling_exact_diagnostic.py"

class StrongCouplingDiagnosticExpectationTests(unittest.TestCase):
    def test_piecewise_fourth_order_coefficients_n4_n5_n6(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--n", "4", "5", "6"],
            cwd=ROOT, capture_output=True, text=True, check=False, timeout=120,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("[epsilon^4]  = 1/648", result.stdout)
        self.assertIn("[epsilon^4]  = 1/6144", result.stdout)
        self.assertIn("[epsilon^4]  = 1/20000", result.stdout)
        self.assertEqual(result.stdout.count("exact_match  = True"), 3)
        self.assertNotIn("exact_match  = False", result.stdout)

if __name__ == "__main__":
    unittest.main(verbosity=2)
