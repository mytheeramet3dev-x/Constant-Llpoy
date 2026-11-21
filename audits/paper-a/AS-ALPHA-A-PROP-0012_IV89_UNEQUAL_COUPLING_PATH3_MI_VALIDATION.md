# IV-89 — Unequal-coupling path-3 mutual-information validation

**Status:** Exploratory numerical cross-check only; no asymptotic proof.

## Model
\[
H=-J_{12}\sigma_1^z\sigma_2^z-J_{23}\sigma_2^z\sigma_3^z
-h(\sigma_1^x+\sigma_2^x+\sigma_3^x),\quad J_{13}=0.
\]
Ground state is computed from the real symmetric 8x8 matrix. Spin 2 is traced out to obtain \(\rho_{13}\), and MI is computed using natural-log entropy.

## Validation
The implementation checks full-state and reduced-state traces equal 1, marginal traces equal 1, Hermiticity, nonnegative reduced eigenvalues within numerical tolerance, and MI nonnegativity. The executable is `tools/paper-a/iv89_unequal_coupling_path3_mi_validation.py`.

## Samples (h=1)
| J12 | J23 | MI(1:3) | MI/(J12^2 J23^2) |
|---:|---:|---:|---:|
| 0.01 | 0.10 | 3.53751377944e-5 | 35.37513779 |
| 0.03 | 0.10 | 1.96565121472e-4 | 21.84056905 |
| 0.10 | 0.03 | 1.96565121472e-4 | 21.84056905 |
| 0.10 | 0.20 | 1.64483917375e-3 | 4.112097934 |
| 0.20 | 0.10 | 1.64483917375e-3 | 4.112097934 |
| 0.01 | 0.01 | 8.66801503403e-6 | 866.8015034 |
| 0.01 | 0.03 | 2.03482201651e-5 | 226.0913352 |
| 0.03 | 0.01 | 2.03482201636e-5 | 226.0913352 |

Swapping \(J_{12}\) and \(J_{23}\) gives equal MI, as expected from path endpoint exchange symmetry.

## Interpretation and limitations
- The values are symmetric under exchanging the two path couplings in these tests.
- \(MI/(J_{12}^2J_{23}^2)\) is not approximately constant across this weak/moderate sample. This ratio alone therefore does not establish a monomial leading term.
- Samples with both couplings small show nontrivial scaling; the asymptotic structure may depend on the ratio of couplings and logarithmic entropy terms. A path-dependent asymptotic expansion is still required.
- These numerical samples do **not** prove the MI leading order, a logarithmic coefficient, any response identity, or Proposition 0012.

## Reproduction
Run:
```bash
python3 tools/paper-a/iv89_unequal_coupling_path3_mi_validation.py
```
Only small finite numerical samples were checked. No Lean theorem or formal proof was performed.
