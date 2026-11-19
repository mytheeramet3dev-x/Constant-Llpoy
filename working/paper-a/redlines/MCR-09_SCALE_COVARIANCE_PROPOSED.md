# MCR-09 — Proposed Redline: Positive-Field Scaling and Projector/Eigenvector Distinction

- **Document ID:** CL-PA-RL-MCR-09
- **Status:** PROPOSED DOMAIN AND SEMANTIC QUALIFICATION
- **Affected claims:** AS-ALPHA-A-PROP-0006 and AS-ALPHA-A-PROP-0011
- **Frozen source:** `mytheeramet3dev-x/Absolute_Sym`, commit `8deb7de4a49cb2060720246b7101820ee7e08c91`
- **Source locations:** §2.3; §5.4
- **Source blobs:** §2 `541382fa7ab4b9e254c8e7e5158f202c1a975e0d`; §5 `671c97fa68fa48c929760bf9956d197b358c4904`
- **Correction register item:** MCR-09

## 1. Domain and positive energy rescaling

The identity
\[
H(\mathbf J,h)=h\,\widetilde H(\mathbf J/h,1)
\]
is used as a positive scalar rescaling only for \(h>0\). For this domain, multiplication by \(h\) preserves the ordering of eigenvalues and the spectral projectors. At \(h=0\), the ratio \(\mathbf J/h\) is undefined and the positive-rescaling argument does not apply.

**Proposed domain sentence for §2.3:**

> Throughout this scaling argument assume \(h>0\). The identity \(H(\mathbf J,h)=h\widetilde H(\mathbf J/h,1)\) is a positive scalar rescaling of the Hamiltonian. It preserves the ground-state spectral projector; it is not a unitary transformation and is not asserted at \(h=0\).

## 2. Projector versus eigenvector

The phase-independent statement is
\[
P_0(\mathbf J,h)
=P_0(\mathbf J/h,1),
\]
where \(P_0\) is the ground-state spectral projector, provided the ground eigenvalue is simple (or, more generally, the corresponding isolated ground spectral subspace is identified consistently).

If the ground state is nondegenerate and normalized, then the state vectors differ by a phase:
\[
|\Psi_0(\mathbf J,h)\rangle
=e^{i\theta}|\widetilde\Psi_0(\mathbf J/h)\rangle.
\]
Do not assert equality of state vectors without a phase convention. Reduced density matrices and entropies depend only on the projector and are phase-independent.

## 3. Response scaling

Assume the reduced-state mutual information is differentiable in the dimensionless edge variables
\[
\mathbf x=\mathbf J/h
\]
on the domain considered, and write
\[
I_{ij}(\mathbf J,h)=\widetilde I_{ij}(\mathbf x).
\]
Then for each edge coordinate,
\[
\frac{\partial I_{ij}}{\partial J_e}
=\frac1h
\frac{\partial\widetilde I_{ij}}{\partial x_e}.
\]
Thus the full response matrix satisfies
\[
\chi(\mathbf J,h)=h^{-1}\widetilde\chi(\mathbf J/h).
\]
If the same edge-space decomposition is used, its eigenvalues scale by the same positive factor:
\[
\chi_k(\mathbf J,h)=h^{-1}\widetilde\chi_k(\mathbf J/h).
\]
The ordering of these eigenvalues is unchanged by the positive factor \(h^{-1}\), but their dimensional values are not invariant under changing \(h\). The feedback eigenvalues \(g\chi_k\) depend on the dimensionless ratio \(g/h\).

This conclusion is conditional on the differentiability of the entropy response. Analyticity of the ground-state projector alone is not sufficient at points where reduced-state eigenvalues vanish.

## 4. Required manuscript edits

1. State \(h>0\) wherever the dimensionless rescaling is used.
2. Use the projector identity as the phase-independent primary statement.
3. State a vector equality only up to phase, under nondegeneracy.
4. Add differentiability hypotheses to the response-matrix chain-rule statement.
5. Distinguish scale covariance from strict invariance: \(\chi_k\) scales as \(h^{-1}\).
6. Keep entropy regularity at rank-deficient reduced states as a separate proof obligation.

## 5. Disposition

**PROPOSED QUALIFICATION — PROJECTOR SCALING EXACT FOR POSITIVE FIELD; RESPONSE SCALING CONDITIONAL ON ENTROPY DIFFERENTIABILITY.**

This file is a separate Constant Llpoy redline. It does not modify the frozen source snapshot or upstream `Absolute_Sym`.
