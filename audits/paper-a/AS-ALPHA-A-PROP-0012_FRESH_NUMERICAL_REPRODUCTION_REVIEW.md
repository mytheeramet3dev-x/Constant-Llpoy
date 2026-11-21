# PROP-0012 — Fresh Independent Weak-Coupling Numerical Reproduction

**Claim:** corrected weak-coupling sign of edge-response contrast (B-C).  
**Pinned source:** Paper A frozen commit `8deb7de4a49cb2060720246b7101820ee7e08c91`.  
**Diagnostic:** independent local execution of the full-Hilbert finite-difference procedure described in `working/paper-a/edge_response_weak_coupling_diagnostic.py`; reconstructed from the inspected source code, not by executing the repository file itself.  
**Scope:** finite numerical consistency only; this is not a proof.

## Numerical setup

- (N=4,5,6), Hilbert dimension (2^N).
- (h=1), (J=0.005) and (0.001).
- 40 decimal digits.
- Independent edge perturbations: shared edge (J_{13}) and disjoint edge (J_{34}).
- Central finite-difference step (delta=10^{-4}J).
- Explicit Hamiltonian diagonalization, reduced density matrices, entropy, and response contrast.

The leading analytic coefficient used for comparison is
[
L_N(J)=\frac{J}{8}\ln\frac{2(N-2)}{N-1}
quad (h=1).
]

## Reproduced results

| N | J/h | Numerical B-C | Leading term | Ratio |
|---:|---:|---:|---:|---:|
| 4 | 0.005 | 0.000218180048481 | 0.000179801295282 | 1.21345092725 |
| 4 | 0.001 | 0.0000378968660064 | 0.0000359602590565 | 1.05385408784 |
| 5 | 0.005 | 0.000292382815471 | 0.000253415692568 | 1.15376760022 |
| 5 | 0.001 | 0.0000526367260336 | 0.0000506831385135 | 1.03854511732 |
| 6 | 0.005 | 0.000333923265382 | 0.000293752268279 | 1.1367512746 |
| 6 | 0.001 | 0.0000607452934164 | 0.0000587504536557 | 1.03395445714 |

All reproduced values are positive. For each N, the ratio trends toward 1 as J/h decreases, consistent with the corrected positive leading coefficient. This does not establish the asymptotic theorem, remainder estimate, or sign at arbitrary coupling.

## Independent mathematical spot-check

For fixed finite (N\ge4), set (r=J/h). The shared-edge leading derivatives are (p_1'=r^2/8+O_N(r^3)) and (q'=r^2/8+O_N(r^3)); the disjoint-edge derivatives have no (r^2) contribution. The leading entropy-log terms cancel to leave
[
B-C=\frac{J}{8h^2}\ln\frac{2(N-2)}{N-1}
+O_N\left(\frac{J^2}{h^3}[1+|\ln r|]\right).
]
The logarithm is positive for every N≥4 because (2(N-2)/(N-1)>1). Thus, **if** the stated model-specific differentiated remainder is proved, the leading coefficient implies (B-C>0) for sufficiently small positive J/h at each fixed N. The numerical reproduction is consistent with this route but cannot close its analytic assumptions.

## Disposition

- Independent numerical reproduction: **PASS** (six points).
- Leading coefficient/sign algebra: **spot-check PASS** under the working derivation's local expansion assumptions.
- Full model-specific remainder theorem: **not independently closed in this review**.
- Lean build/formal correspondence: **not run**.
- Global (B-C>0): **not proved**.
- Manuscript source phrase “opposite-sign response”: **still requires semantic correction/reconciliation**.

The script was reconstructed and executed in the temporary runtime; no repo diagnostic file was changed. The frozen manuscript remains unchanged.
