# MCR-13 — Proposed Redline: Notation and Parameter-Domain Lock

- **Document ID:** CL-PA-RL-MCR-13
- **Status:** PROPOSED EDITORIAL/MATHEMATICAL CONSISTENCY PASS
- **Affected claims:** DEF-0001; PROP-0001–0004; PROP-0010–0011; cross-cutting §§2–5
- **Frozen source:** `mytheeramet3dev-x/Absolute_Sym`, commit `8deb7de4a49cb2060720246b7101820ee7e08c91`
- **Source locations:** §§2–5
- **Source blobs:** §2 `541382fa7ab4b9e254c8e7e5158f202c1a975e0d`; §3 `9ac164ac67cc121af212c4fb7268b809d9234bd6`; §4 `a7570431eac62dd4555194df283edb5a9c87a28d`; §5 `671c97fa68fa48c929760bf9956d197b358c4904`
- **Correction register item:** MCR-13

## 1. Proposed notation table

| Symbol | Meaning | Domain/convention |
|---|---|---|
| \(N\) | Number of spins/sites | Positive integer; each theorem states its sharper lower bound |
| \(\sigma_i^\alpha\) | Pauli operator at site \(i\) | \(\alpha\in\{x,y,z\}\) |
| \(J_{ij}\) | Coupling on edge \(ij\) | Reference ferromagnetic model has \(J_{ij}\ge0\); ambient edge derivatives are taken in a real neighborhood where defined |
| \(J\) | Common coupling on the permutation-symmetric path | \(J_{ij}=J\) for every edge |
| \(h\) | Transverse field | \(h>0\) for all dimensionless-scaling claims |
| \(H(\mathbf J,h)\) | TFIM Hamiltonian | \(-\sum_{i<j}J_{ij}\sigma_i^z\sigma_j^z-h\sum_i\sigma_i^x\) |
| \(P_0\) | Ground-state spectral projector | Phase-independent; rank one when ground state is nondegenerate |
| \(I_{ij}(\mathbf J,h)\) | Mutual information of sites \(i,j\) | Natural logarithms; differentiability must be established where derivatives are used |
| \(x\) | Uniform dimensionless coupling | \(x=J/h\), for \(h>0\) |
| \(\mathcal G_N(x)\) | Uniform-path dimensionless mutual information | \(I_{12}(J,h)=\mathcal G_N(J/h)\) when the positive-rescaling/projector identity applies |
| \(g\) | Feedback parameter | \(g>0\) for threshold/response inequalities |
| \(\eta\) | Dimensionless feedback ratio | \(\eta=g/h\) |
| \(\alpha_N\) | Infimum-defined threshold coefficient | \(\inf_{x>0}x/\mathcal G_N(x)\), only where \(\mathcal G_N(x)>0\) |
| \(x_c\) | Interior threshold/tangent coordinate | Exists only if the infimum is attained at an interior point |
| \(g_c\) | Critical feedback value | \(g_c=\alpha_Nh\) only when the threshold scaling/attainment statement applies |
| \(f(x;\eta)\) | Dimensionless fixed-point function | \(\eta\mathcal G_N(x)-x\) |
| \(F_x\) | Derivative of \(F(x,g,h)=g\mathcal G_N(x)-hx\) in \(x\) | \(g\mathcal G_N'(x)-h\) |
| \(F_J\) | Derivative of dimensional uniform-path function \(F(J;g,h)=gI_{12}(J,h)-J\) in common coupling \(J\) | \(g\,dI_{12}/dJ-1\); do not confuse with \(F_x\) |
| \(T(x)\) | Dimensionless scalar Picard map | \((g/h)\mathcal G_N(x)\) |
| \(A\) | \(\partial_{J_{12}}I_{12}\) | Independent-edge partial at the symmetric point |
| \(B\) | \(\partial_{J_{13}}I_{12}\) | Shared-endpoint edge partial |
| \(C\) | \(\partial_{J_{34}}I_{12}\) | Disjoint-edge partial |
| \(\chi_0\) | Uniform response eigenvalue | Sum of all independent-edge partials along the all-edges-equal path |
| \(\chi_1,\chi_2\) | Nonuniform response-sector eigenvalues | Defined on their nonzero representation sectors; domain depends on \(N\) |
| \(\mathbf u\) | Independent edge perturbation coordinates | Specify normalization, e.g. \(J_e=J(1+u_e)\), in each asymptotic derivation |
| \(r\) | Weak-coupling parameter | \(r=J/h\to0^+\) |
| \(\varepsilon\) | Strong-coupling perturbation parameter | \(\varepsilon=h/J=1/x\to0^+\) |

## 2. Derivative convention lock

The manuscript must distinguish these three operations:

1. **Uniform-path derivative:** all edges are set equal to \(J\), then the common value changes. This is \(dI_{12}(J,h)/dJ=\chi_0\).
2. **Independent-edge partial:** vary one coordinate \(J_e\) while holding all other edge coordinates fixed. These define \(A,B,C\).
3. **Dimensionless derivative:** differentiate \(\mathcal G_N(x)\) with respect to \(x=J/h\). For fixed \(h>0\), the chain rule relates it to the uniform-path derivative by \(dI_{12}/dJ=(1/h)\mathcal G_N'(x)\).

No formula may use an unqualified \(\partial I/\partial J\) if the distinction matters.

## 3. Domain and positivity lock

At the beginning of the relevant subsection or theorem, state the assumptions actually used:
- \(h>0\) for \(x=J/h\), positive energy rescaling, and field-scale covariance;
- \(g>0\) for inequalities involving \(1/g\) and positive threshold scaling;
- \(N\ge4\) for the weak-/strong-coupling edge-response asymptotics and the three nonzero edge-response sectors;
- \(N\ge3\) for the stated edge-space dimension formula, with the residual sector zero-dimensional at \(N=3\);
- \(\mathcal G_N(x)>0\) wherever dividing by it;
- differentiability/analyticity only where proved, particularly for entropy derivatives at rank-deficient reduced states.

Do not impose a global assumption once and silently use it in a theorem whose proof needs only a local one; list the theorem's exact domain.

## 4. Consistency checks across §§2–5

- Use \(J\) only for the uniform common coupling; use \(J_{ij}\) for independent edge coordinates.
- Keep \(x=J/h\) and \(\eta=g/h\) dimensionless.
- Distinguish \(\alpha_N\) as an infimum from an attained minimum; use \(x_c\) only after attainment.
- Keep \(F_x\) and \(F_J\) distinct, with the factor of \(h\) in the relation between their multiplier formulas.
- Define \(A,B,C\) before using the identity \(\chi_1-\chi_2=(N-2)(B-C)\).
- Do not use \(B-C\) as a synonym for a generic “response” without naming the observable and edge directions.
- Use \(O_N(\cdot)\) whenever the implied constants may depend on fixed finite \(N\).
- Do not infer a derivative remainder by differentiating a function-level big-O estimate.
- Keep natural logarithms fixed throughout, or explicitly convert the feedback parameter if another base is used.

## 5. Disposition

**PROPOSED NOTATION/DOMAIN LOCK.** This table is a consistency checklist, not proof that every listed definition is already used consistently or that every regularity assumption holds. It must be checked against the final revised manuscript and all claim records before acceptance.

This file is a separate Constant Llpoy redline. It does not modify the frozen source snapshot or upstream `Absolute_Sym`.
