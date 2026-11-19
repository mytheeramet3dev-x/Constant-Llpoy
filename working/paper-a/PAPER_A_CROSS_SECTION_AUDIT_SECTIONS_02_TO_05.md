# Paper A — Cross-Section Dependency Audit (Sections 2–5)

- **Document ID:** CL-PA-XSEC-001
- **Version:** 0.1.0
- **Audit scope:** Frozen revised Sections 2, 3, 4, and 5
- **Frozen upstream repository:** `mytheeramet3dev-x/Absolute_Sym`
- **Frozen source branch:** `paper-a-interval-audit-2026-11-14`
- **Frozen source commit:** `8deb7de4a49cb2060720246b7101820ee7e08c91`
- **Source blobs:**
  - Section 2: `541382fa7ab4b9e254c8e7e5158f202c1a975e0d`
  - Section 3: `9ac164ac67cc121af212c4fb7268b809d9234bd6`
  - Section 4: `a7570431eac62dd4555194df283edb5a9c87a28d`
  - Section 5: `671c97fa68fa48c929760bf9956d197b358c4904`
- **Status:** INTERNAL CROSS-SECTION AUDIT / PROPOSED CORRECTIONS / NOT LEAN-VERIFIED / NOT EXTERNALLY REVIEWED
- **Repository boundary:** This document is stored in Constant Llpoy. It does not modify the upstream manuscript.

## 1. Executive disposition

Sections 2–5 have a coherent intended mathematical spine:

1. Section 2 defines the finite-​N transverse-field Ising model, the dimensionless mutual-information response \(\mathcal G_N(x)\), and the threshold candidate \(\alpha_N=\inf_{x>0}x/\mathcal G_N(x)\).
2. Section 3 derives the tangent equations and proposes a local saddle-node near an attained interior minimizer.
3. Section 4 uses positive energy homogeneity to express the scalar fixed-point map and its multiplier in dimensionless form, then studies near-critical and strong-coupling limits.
4. Section 5 differentiates the full edge-response map at the symmetric point and decomposes its Jacobian into three permutation sectors.

The chain is **not yet a closed proof chain**. The algebraic links can be made consistent, but several links are conditional on results not established in the adjacent sections. The principal blockers are:

- the Perron–Frobenius shift in Section 2 has the wrong sign as written;
- positivity and regularity of \(\mathcal G_N\), especially near the rank-changing endpoint \(x=0\), are not fully established;
- the threshold infimum need not be attained, and the local nondegenerate fold hypotheses are not proved model-specifically;
- Section 3's \(C^2\) hypothesis does not justify its cubic Taylor remainder or its \(O(g-g_c)\) branch remainder;
- Sections 3 and 4 use different meanings for the first derivative subscript on \(F\), and the conversion factor \(h\) should be stated explicitly;
- Section 4's one-dimensional uniform-path derivative must be connected explicitly to Section 5's sum of independent edge partial derivatives;
- Section 4's strong-coupling derivative is a separate fixed-finite-\(N\) derivation, not a consequence of differentiating the function-level big-O estimate and not a proof of Section 5's \(B-C\) sign;
- the weak-coupling opposite-sign sentence in Section 4 conflicts with the corrected response-sign audit and cannot be supported by the current Section 5 evidence.

**Overall disposition:** Sections 2–5 are PARTIALLY COHERENT AT THE ALGEBRAIC LEVEL, WITH RELEASE-BLOCKING SOURCE/MATHEMATICAL OBLIGATIONS OPEN. Paper A remains **NOT VERIFIED**.

## 2. Canonical notation and derivative dictionary

The manuscript should adopt one notation table and preserve it throughout.

| Symbol | Meaning | Scope / convention |
|---|---|---|
| \(N\) | Number of spins | Finite integer; response-sector three-piece decomposition requires \(N\ge4\) for all three sectors to be nonzero |
| \(h\) | Transverse field / positive energy scale | \(h>0\) |
| \(J_{ij}\) | Edge coupling | Reference model \(J_{ij}\ge0\); response derivatives taken in ambient real edge space near the symmetric point |
| \(J\) | Common value of all edges at the symmetric point | Uniform path \(J_{ij}=J\) |
| \(x\) | Dimensionless uniform coupling | \(x=J/h\) |
| \(g\) | Feedback coupling | \(g>0\) |
| \(\eta\) | Dimensionless feedback parameter | \(\eta=g/h\) |
| \(\mathcal G_N(x)\) | Pair mutual information on the symmetric uniform path | Natural logarithms; equals \(I_{12}(J,h)\) at \(J=hx\) |
| \(f(x;\eta)\) | Dimensionless fixed-point function | \(f=\eta\mathcal G_N(x)-x\) |
| \(F^{(x)}(x,g,h)\) | Dimensionful residual written in dimensionless coordinate | \(F^{(x)}=g\mathcal G_N(x)-hx=h f\) |
| \(F^{(J)}(J,g,h)\) | Physical-coupling residual | \(F^{(J)}=g I_{12}(J,h)-J\) |
| \(\alpha_N\) | Threshold infimum | \(\inf_{x>0}x/\mathcal G_N(x)\), only where \(\mathcal G_N>0\) |
| \(x_c\) | Candidate interior minimizer / fold coordinate | Existence, attainment, and nondegeneracy require proof |
| \(g_c\) | Critical feedback at fixed \(h\) | \(g_c=\alpha_N h\) only if the infimum is attained at the stated interior point |
| \(A,B,C\) | Independent-edge partial derivatives of \(I_{12}\) | Same edge / adjacent edge / disjoint edge |
| \(\chi_0,\chi_1,\chi_2\) | Response-Jacobian eigenvalues | Uniform, degree-heterogeneous, residual edge sectors |

### 2.1 Exact derivative conversion

At the symmetric point, with \(J=h x\),

\[
F^{(x)}(x,g,h)=F^{(J)}(hx,g,h).
\]

By the chain rule,

\[
\boxed{F^{(x)}_x=h F^{(J)}_J.}
\]

Equivalently,

\[
F^{(x)}_x=g\mathcal G_N'(x)-h,
\qquad
F^{(J)}_J=\frac gh\mathcal G_N'(x)-1.
\]

Therefore the Section 3 tangent condition \(F^{(x)}_x=0\) and the Section 4 tangent condition \(F^{(J)}_J=0\) are equivalent because \(h>0\). Their numerical values away from the tangent point differ by the factor \(h\). The manuscript must not use the bare symbol \(F_x\) and \(F_J\) as though they were the same derivative.

**Finding XSEC-01 — P1:** Add this conversion explicitly and reserve distinct labels \(F^{(x)}\), \(F^{(J)}\), or an equivalent unambiguous convention.

### 2.2 Uniform-path derivative versus edge partial derivatives

Let \(I_{12}(\mathbf J,h)\) be the pair response for observed edge \(12\). Along the symmetric uniform path \(J_{ij}=J\), the chain rule gives

\[
\frac{d}{dJ}I_{12}(J\mathbf 1,h)
=\sum_{i<j}\frac{\partial I_{12}}{\partial J_{ij}}.
\]

At the symmetric point, permutation symmetry groups the terms into:
- one same-edge term \(A\);
- \(2(N-2)\) adjacent-edge terms \(B\);
- \(\binom{N-2}{2}\) disjoint-edge terms \(C\).

Hence

\[
\boxed{
\frac{d I_{12}}{dJ}\bigg|_{\rm uniform}
=A+2(N-2)B+\frac{(N-2)(N-3)}2C
=\chi_0.
}
\]

Since \(\mathcal G_N(x)=I_{12}(J=hx,h)\),

\[
\boxed{\mathcal G_N'(x)=h\chi_0.}
\]

Consequently,

\[
F^{(J)}_J=g\chi_0-1,
\qquad
T'(x)=\frac gh\mathcal G_N'(x)=g\chi_0.
\]

These are the exact links between Sections 4 and 5, provided the response map is differentiable at the symmetric point and the symmetry assumptions used to identify the partial derivatives hold.

**Finding XSEC-02 — P1:** State this chain-rule identity in the manuscript. Without it, Section 4's scalar derivative and Section 5's \(\chi_0\) may look like unrelated quantities.

## 3. Section 2 → Section 3: threshold and fold dependencies

### 3.1 Perron–Frobenius sign error

Section 2 states that adding a sufficiently large multiple of the identity to \(H\) makes the matrix nonnegative. This is incorrect for the displayed Hamiltonian sign convention: the single-spin-flip off-diagonal entries of \(H\) are \(-h<0\), and adding \(cI\) changes only diagonal entries.

The suitable matrix is

\[
K=cI-H.
\]

For sufficiently large \(c\), its diagonal entries are nonnegative, while its single-spin-flip off-diagonal entries are \(+h>0\). The graph of these transitions is the connected Boolean hypercube, so \(K\) is irreducible and nonnegative. Perron–Frobenius then gives a simple largest eigenvalue of \(K\), corresponding to a simple lowest eigenvalue of \(H\).

This supports finite-\(N\) ground-state nondegeneracy for \(h>0\). It does not, by itself, establish every later entropy regularity claim.

**Finding XSEC-03 — P0:** Correct the shift from \(H+cI\) to \(cI-H\), and reconcile the proof with the formal declaration and proof artifact. This is a direct sign error in a stated justification.

### 3.2 Positivity and regularity of \(\mathcal G_N\)

Section 2 uses \(\mathcal G_N(x)>0\) to rewrite the fixed-point equation as \(x/\mathcal G_N(x)=\eta\), and uses \(\mathcal G_N(0)=0\) at the product-state endpoint.

The manuscript itself notes that at \(x=0\) the reduced states have zero eigenvalues and entropy derivatives require separate care. The following are distinct obligations:

1. continuity at \(x=0\) and \(\mathcal G_N(0)=0\);
2. strict positivity \(\mathcal G_N(x)>0\) for every \(x>0\) in the domain used;
3. differentiability / \(C^2\) regularity near a candidate \(x_c>0\);
4. any stronger regularity used for quantitative fold remainders;
5. endpoint behavior of \(x/\mathcal G_N(x)\) as \(x\to0^+\) and \(x\to\infty\).

Ground-state nondegeneracy and smoothness of the ground-state projector for \(h>0\) do not automatically prove entropy differentiability at rank-changing reduced states. The local fold only needs regularity near a positive interior point, but the global threshold and root-count arguments need additional domain and endpoint control.

**Finding XSEC-04 — P1:** Split positivity, endpoint continuity, and interior entropy regularity into separate explicit lemmas/assumptions. Do not treat them as consequences of Perron–Frobenius alone.

### 3.3 Infimum versus attained critical point

Section 2 defines

\[
\alpha_N=\inf_{x>0}\frac{x}{\mathcal G_N(x)}.
\]

The definition alone supports subcritical exclusion on a domain where \(\mathcal G_N(x)>0\): if \(\eta<\alpha_N\), then \(x/\mathcal G_N(x)>\eta\) and therefore \(f(x;\eta)<0\).

It does **not** imply:
- the infimum is attained;
- an interior minimizer \(x_c>0\) exists;
- the minimizer is unique;
- the minimizer is nondegenerate;
- every \(\eta>\alpha_N\) has roots;
- exactly two roots exist globally.

If the infimum is attained at an interior differentiable minimizer, the tangent identity follows. A strict nondegenerate minimum additionally requires the relevant second-derivative condition. Section 3 must keep this conditional structure visible.

**Finding XSEC-05 — P0:** The paper must not identify the infimum with an actual saddle-node without proving attainment and interior nondegeneracy. Retain the distinction already partially acknowledged in Section 2.

## 4. Section 3 → Section 4: local branch and asymptotic inheritance

### 4.1 C² does not justify the stated remainder

Section 3 assumes only \(\mathcal G_N\in C^2\) near \(x_c\), but writes a cubic Taylor remainder and a branch expansion with \(O(g-g_c)\) correction. Under \(C^2\), the justified expansion is

\[
F^{(x)}
=\mathcal G_N(x_c)\,v
+\frac12g_c\mathcal G_N''(x_c)u^2
+o(u^2)+O(|vu|),
\]

where \(u=x-x_c\), \(v=g-g_c\), and \(h\) is fixed.

With the local fold hypotheses \(\mathcal G_N(x_c)>0\) and \(\mathcal G_N''(x_c)<0\), the leading branch law is

\[
x_\pm-x_c
=\pm C\sqrt{g-g_c}+o(\sqrt{g-g_c}),
\qquad
C=\sqrt{\frac{2\mathcal G_N(x_c)}
{g_c|\mathcal G_N''(x_c)|}}.
\]

The \(O(g-g_c)\) remainder needs stronger regularity and a quantitative argument. The model-specific curvature condition remains open; it is not proved by the formal normal form.

**Finding XSEC-06 — P0:** Correct Section 3's remainder or state and prove stronger regularity. This is inherited by every later claim that uses the quantitative branch expansion.

### 4.2 What Section 4.4.1 actually needs

The limits

\[
x_*(\gamma)\to x_c,\qquad
T'(x_*)\to1,\qquad
F^{(J)}_J\to0
\]

need only a valid local branch converging to \(x_c\), continuity of \(\mathcal G_N'\), and the tangent equations. They do not require the sharper \(O(g-g_c)\) branch remainder.

Thus Section 4.4.1 can remain after Section 3 is corrected to a valid \(C^2\) local fold statement, but it must not cite or rely on the unjustified stronger error order.

**Finding XSEC-07 — P1:** Make Section 4.4.1 explicitly depend on the weaker, valid local branch conclusion, not on the unsupported quantitative remainder.

### 4.3 Global continuation is not supplied by the local fold

The condition \(x_*(\gamma)\ge x_c\) for all \(\gamma\ge1\), and the limit \(x_*(\gamma)\to\infty\), require a selected branch and global continuation/no-turning/no-exchange hypotheses or a proof replacing them. Neither follows from the local fold.

The strong-coupling asymptotics of \(\mathcal G_N\) and \(\mathcal G_N'\) can be composed with a branch only after the branch is known to reach \(x\to\infty\).

**Finding XSEC-08 — P1:** Keep endpoint asymptotics and branch-continuation statements logically separate. The first does not prove the second.

## 5. Section 4 ↔ Section 5: uniform response and edge response

### 5.1 The exact scalar-to-sector bridge

The exact identities are

\[
\mathcal G_N'(x)=h\chi_0,
\qquad
F^{(J)}_J=g\chi_0-1,
\qquad
T'=g\chi_0.
\]

Therefore Section 5's inequality \(F_J<0\) gives

\[
\chi_0<\frac1g,
\]

not \(\chi_0<0\). Negativity of the uniform response would require \(F_J<-1\) for \(g>0\). This is consistent with Section 5.1's own warning and should be preserved in any synthesis.

### 5.2 Independent-edge sectors are not the uniform derivative

The quantities \(A,B,C\) are independent-edge partial derivatives. The eigenvalues

\[
\chi_0=A+2(N-2)B+\frac{(N-2)(N-3)}2C,
\]
\[
\chi_1=A+(N-4)B-(N-3)C,
\qquad
\chi_2=A-2B+C
\]

are eigenvalues of the full edge-response Jacobian under the stated \(S_N\)-equivariance and differentiability assumptions. Only \(\chi_0\) is the uniform-path derivative. The derivative \(\mathcal G_N'(x)\) does not individually equal \(A\), \(B\), or \(C\).

The identity

\[
\chi_1-\chi_2=(N-2)(B-C)
\]

is exact algebraically once the response Jacobian and sector conventions are established. It orders two response eigenvalues when \(B-C\) has a known sign. It does not prove either eigenvalue's sign, feedback stability, or geometric emergence.

**Finding XSEC-09 — P1:** Explicitly distinguish the uniform-path derivative \(\mathcal G_N'\) from the independent-edge derivatives \(A,B,C\), and identify \(\chi_0\) as their specific weighted sum.

### 5.3 Domain and representation hypotheses

The edge permutation representation admits the stated three-sector decomposition for N≥3, with dim V₂=0 at N=3. If the manuscript intends all three sectors to be nonzero, it must state N≥4. This distinction reconciles the present audit with MCR-04 in the existing Manuscript Correction Register.

Schur's lemma gives scalar action on the irreducible sectors only after the response Jacobian is shown to exist and to commute with the permutation action. Symmetry of the Hamiltonian alone is not a substitute for differentiability of the response map at the point in question.

**Finding XSEC-10 — P1:** State \(N\ge3\) for the decomposition formulas and explicitly note the zero-dimensional \(V_2\) sector at \(N=3\); use \(N\ge4\) if all three sectors are intended to be nonzero. Also state differentiability and equivariance as hypotheses for the sector-eigenvalue theorem.

### 5.4 Scale covariance consistency

Because \(x=J/h\), an independent-edge derivative has dimension inverse energy:

\[
\chi_k(J,h)=h^{-1}\widetilde\chi_k(x).
\]

The feedback Jacobian eigenvalues are

\[
g\chi_k=(g/h)\widetilde\chi_k(x)=\eta\widetilde\chi_k(x).
\]

Thus response eigenvalues are not invariant under changing the absolute scale \(h\); the dimensionless response eigenvalues and feedback multipliers are invariant along a ray of fixed \(\eta\) and fixed dimensionless branch coordinate. This matches the intended statement in Section 5.4.

**Disposition:** Algebraically consistent, conditional on the differentiable response map and branch selection.

## 6. Strong-coupling and weak-coupling results must not be conflated

### 6.1 Strong-coupling uniform-path asymptotics

The fixed-finite-\(N\) results recorded in the Section 4 audit are

\[
\mathcal G_N(x)=\ln2-\frac{1}{(N-1)^2x^2}
+O_N\!\left(\frac{\ln x}{x^4}\right),
\]

and, from a separate derivative argument,

\[
\mathcal G_N'(x)=\frac{2}{(N-1)^2x^3}
+O_N\!\left(\frac{\ln x}{x^5}\right).
\]

The derivative estimate must not be inferred merely by differentiating the first big-O statement. Its derivation is along the uniform path and is not an independent-edge response estimate. In particular, it does not establish the sign of \(B-C\), nor does it prove a uniform-in-\(N\) statement.

The Section 4 citation to Lemma 5.1 is mismatched according to the source audit: the located Lemma 5.1 proof concerns \(B-C\), not the \(\mathcal G_N\) strong-coupling expansion. This citation must be corrected after source-authority policy is resolved.

### 6.2 Weak-coupling response-sign conflict

Section 4.4.3 asserts “opposite-sign response characteristics” and points to Lemma 5.2. The frozen audit history records that the original negative-sign derivation omitted an order-\(r^2\) coherence contribution. The corrected fixed-finite-\(N\) candidate has positive leading coefficient

\[
(B-C)_{\rm lead}
=\frac{J}{8h^2}
\ln\!\left(\frac{2(N-2)}{N-1}\right)>0,
\qquad N\ge4.
\]

However, the differentiated remainder control remains an open obligation in the frozen audit record. This is not a global sign theorem. Section 5 itself labels \(B-C>0\) a strong numerically supported conjecture, not an exact theorem.

**Finding XSEC-11 — P0:** Remove or rewrite the “opposite-sign response characteristics” sentence. The current Section 4 assertion is not supported by the corrected audit record, and the corrected endpoint calculation is not yet a complete theorem.

## 7. Cross-section dependency graph

The logical dependency structure should be recorded as follows.

\[
\boxed{
\begin{array}{c}
\text{Section 2: model, ground state, }\mathcal G_N,\alpha_N\\
\downarrow\;\text{positivity, regularity, attainment}\;\downarrow\\
\text{Section 3: tangent point and local fold}\\
\downarrow\;\text{valid local branch }x_*(\gamma)\to x_c\\
\text{Section 4.4.1: near-critical limits}\\
\downarrow\;\text{global continuation to }x\to\infty\\
\text{Section 4.4.2: branch-composed strong-coupling limits}
\end{array}
}
\]

Separately, the edge-response chain is

\[
\boxed{
\begin{array}{c}
\text{Section 2: full edge response }I_{ij}(\mathbf J,h)\\
\downarrow\;\text{differentiability and }S_N\text{-equivariance}\\
\text{Section 5: }A,B,C\text{ and }\chi_0,\chi_1,\chi_2\\
\downarrow\;\text{uniform-path chain rule}\\
\mathcal G_N'(x)=h\chi_0,\quad F_J=g\chi_0-1
\end{array}
}
\]

The strong-coupling derivative in Section 4 and the weak-coupling \(B-C\) question in Section 5 are distinct analytic problems. Neither can be substituted for the other.

## 8. Prioritized consolidated findings

| Finding | Priority | Sections | Required action | Current status |
|---|---|---|---|---|
| XSEC-01 | P1 | 3–4 | Define the two residuals / state \(F_x=hF_J\) | Required |
| XSEC-02 | P1 | 4–5 | State \(\mathcal G_N'=h\chi_0\) chain rule | Required |
| XSEC-03 | P0 | 2 | Correct Perron–Frobenius operator to \(cI-H\) | Required |
| XSEC-04 | P1 | 2–3 | Separate positivity, endpoint continuity, and interior regularity | Open |
| XSEC-05 | P0 | 2–3 | Prove threshold attainment/interior nondegeneracy or retain conditionals | Open |
| XSEC-06 | P0 | 3 | Replace unjustified C² remainders or prove stronger regularity | Required |
| XSEC-07 | P1 | 3–4 | Make near-critical limits depend only on valid local fold | Required |
| XSEC-08 | P1 | 3–4 | Prove global continuation separately | Open |
| XSEC-09 | P1 | 4–5 | Distinguish uniform derivative from edge partials | Required |
| XSEC-10 | P1 | 5 | State \(N\ge4\), differentiability, equivariance | Required |
| XSEC-11 | P0 | 4–5 | Remove unsupported opposite-sign statement | Required |
| XSEC-12 | P1 | 4 | Fix Lemma 5.1 citation; keep fixed-\(N\) scope | Required |
| XSEC-13 | P1 | 4–5 | Do not infer \(B-C\) from uniform-path asymptotics | Required |
| XSEC-14 | P0 | Whole paper | Resolve manifest-authority versus TeX build-input conflict before release build | Blocked |

## 9. Recommended correction order

1. **Correct the Section 2 Perron–Frobenius sign** and reconcile the proof artifact.
2. **Freeze a notation/derivative convention** for \(F^{(x)}\), \(F^{(J)}\), \(\mathcal G_N'\), and \(\chi_0\).
3. **Repair Section 3 regularity claims** using the C² Peano remainder, or add and prove stronger hypotheses for the sharper remainder.
4. **Make threshold attainment and curvature conditional unless proved**; do not silently promote the infimum to an attained fold.
5. **Insert the uniform-path / edge-Jacobian chain rule** linking Sections 4 and 5.
6. **Correct Section 4.4.2's citation** and keep the fixed-finite-\(N\) scope explicit.
7. **Remove the Section 4.4.3 opposite-sign assertion** pending a complete corrected weak-coupling proof and branch interpretation.
8. **Resolve source authority and build pipeline** before generating release TeX or treating an integrated manuscript as canonical.

## 10. Verification boundary

- This document is a cross-section source-level audit, not a formal proof.
- No Lean build was run for this audit.
- No CI result is asserted.
- No independent external mathematical review was run.
- The upstream `Absolute_Sym` repository and its frozen source files were not modified.
- Proposed corrections are not yet applied to the manuscript.
- Paper A remains **NOT VERIFIED**.
