# PROP-0012 IV-13 — Adversarial Check of Corrected Leading Coefficient

**Scope:** Try to falsify the IV-12 corrected candidate using the current fetched weak-coupling ledger; check excitation-gap normalization, multiplicity, log cancellation, dimensional scaling, and remainder propagation.
**Verdict:** NO INTERNAL COUNTEREXAMPLE FOUND IN THE CHECKED LEDGER; CONDITIONAL CONSISTENCY PASS ONLY. This is not a full independent matrix derivation, source reconciliation, or formal proof.

## 1. First-order normalization

For $H_0=-h\sum_i\sigma_i^x$ and interaction $-J_{ij}\sigma_i^z\sigma_j^z$, a pair flip has gap $4h$. The first-order amplitude is $a_{ij}=J_{ij}/(4h)=r(1+u_{ij})/4$. Its probability is $r^2(1+u_{ij})^2/16$, so at the uniform point its derivative with respect to $u_{ij}$ is $r^2/8$. The $1/8$ is consistent with this Hamiltonian convention.

## 2. Leading multiplicities

The current working ledger gives $p_i=(N-1)r^2/16+O_N(r^3)$ and the odd-block positive branch $q=(N-2)r^2/8+O_N(r^3)$. These counts are consistent with the number of pair partners for a one-site flip probability and the number of environment sites after the selected pair is removed. This check does not reconstruct the complete reduced matrices independently.

## 3. Logarithmic algebra

Using the IV-12 ledger, the combined logarithms are
\[
\ln\frac{16}{(N-1)r^2}+\ln\frac{(N-2)r^2}{8}
=\ln\frac{2(N-2)}{N-1}.
\]
The $r^2$ terms cancel and the explicit $+1$ from the positive-branch entropy derivative remains. No algebraic counterexample was found in this simplification.

## 4. Remainder propagation

If the positive branch and first edge derivatives jointly satisfy $q=r^2Q(u)+O_N(r^3)$ with $Q(0)>0$ and differentiated remainder $O_N(r^3)$, then $\ln q=2\ln r+\ln Q(0)+O_N(r)$ and entropy derivative errors are $O_N(r^3|\ln r|)$. Dividing by $J$ gives the claimed dimensional error $O_N(J^2h^{-3}|\ln(J/h)|)$. This validates the scaling conversion only conditional on the joint differentiated expansion. The manuscript's hypotheses and uniform local bounds have not been independently established.

## 5. Sign of the candidate bracket

For $N\ge4$, $2(N-2)/(N-1)>1$, hence $1+\ln(2(N-2)/(N-1))>1$. The corrected candidate coefficient is positive in this domain.

## 6. Disposition

- Checked: gap/amplitude normalization under stated Hamiltonian; leading multiplicity counts against current ledger; log identity; dimensional conversion and conditional remainder order; positivity of candidate bracket.
- Not checked independently: complete reduced density matrix derivation, source definitions/sign conventions, pair-flip differentiated Taylor bounds, and exact block decomposition.
- No Lean formalization/build performed.

**Verdict:** IV-13 PASS only as an adversarial consistency check of the corrected coefficient against the current ledger; no internal counterexample found. PROP-0012 remains OPEN / ANALYTIC-PARTIAL / NOT VERIFIED.
