# Paper A — Section 5 Equation-by-Equation and Evidence Audit

**Audit ID:** CL-PA-S5-AUD-001  
**Frozen source:** Arxiv/paper_01_section_05_revised.md  
**Frozen source commit:** 8deb7de4a49cb2060720246b7101820ee7e08c91  
**Frozen source blob:** 671c97fa68fa48c929760bf9956d197b358c4904  
**Status:** INTERNAL MATHEMATICAL AUDIT / NOT LEAN-VERIFIED / NOT EXTERNAL REVIEW  
**Boundary:** No changes to upstream Absolute_Sym.

## 1. Executive disposition

Section 5 contains a sound scalar derivative identity and a standard representation-theoretic decomposition of the edge space. The sector eigenvalue formulas and the identity chi_1-chi_2=(N-2)(B-C) are algebraically consistent with the three edge-orbit response coefficients A,B,C, provided the response matrix is differentiable and S_N-equivariant at the symmetric point.

However, Section 5 mixes exact representation-theoretic identities, numerical observations, corrected weak-coupling leading coefficients whose differentiated remainder proof is explicitly still open in the frozen weak-coupling audit, and interpretations about dynamical amplification and geometric emergence that do not follow from the sector decomposition alone.

The key conflict is that the frozen weak-coupling audit explicitly says the corrected leading sign is positive but the differentiated remainder is not bounded, so no endpoint theorem follows yet. Until the exact derivation and its proof artifact are reconciled, the theorem-level weak-coupling sign must remain OPEN/CONDITIONAL.

## 2. §5.1 — Uniform response and scalar Picard condition

For the uniform path J_ij=J, define I_12(J,h)=G_N(J/h). Then F(J;g,h)=g I_12(J,h)-J gives

F_J=g chi_0-1,  chi_0=d I_12/dJ.

Therefore F_J<0 iff chi_0<1/g. This is an exact upper bound on the uniform-path response; it does not imply chi_0<0. Negativity requires F_J<-1.

For T(J)=g I_12(J,h), T'(J_*)=1+F_J(J_*), and scalar local linear attraction is exactly |T'|<1 iff -2<F_J<0.

**Disposition:** Algebraically valid, with the explicit scope that this is the one-dimensional uniform scalar iteration. It does not establish stability of the full vector map on all edge couplings or global convergence.

The sentence that F_J<0 is “sufficient for the usual saddle-node branch classification” should be qualified: it identifies the descending side locally when the nondegenerate fold hypotheses of Section 3 hold. F_J<0 alone is not a saddle-node theorem.

## 3. §5.2 — Edge representation decomposition

At the symmetric point, the edge-coordinate space is the permutation representation on unordered pairs of N vertices: V_edge=R^{binom(N,2)}.

For N>=4 it decomposes into three pairwise inequivalent irreducible S_N sectors with dimensions

dim V_0=1, dim V_1=N-1, dim V_2=N(N-3)/2.

The dimensions sum to N(N-1)/2. V_0 is the uniform edge direction; V_1 is the degree/vertex-incidence fluctuation sector; V_2 is the residual sector in the kernel of the vertex-incidence map (degree-preserving edge fluctuations).

The phrase “degree-preserving” should mean the linear constraint that each vertex's incident perturbation sum vanishes, not a general geometric or lattice structure.

For N=3, dim V_2=0, so there are only two nonzero sectors. Any assertion about three nonzero response sectors requires N>=4.

**Disposition:** Representation decomposition is standard and dimensionally consistent. A full proof in the manuscript should either cite/prove the permutation-module decomposition or derive it from the incidence map and its kernel. “Geometry-like” is motivation only.

## 4. Three-orbit response matrix and eigenvalues

Define at the symmetric point A=partial I_12/partial J_12, B=partial I_12/partial J_13 (shared endpoint), and C=partial I_12/partial J_34 (disjoint edge). S_N symmetry implies these are the three edge orbits relative to observed edge {1,2}.

The proposed eigenvalues are

chi_0=A+2(N-2)B+((N-2)(N-3)/2)C,

chi_1=A+(N-4)B-(N-3)C,

chi_2=A-2B+C.

Checks:
1. chi_0 is the row sum: one observed edge, 2(N-2) adjacent edges, and (N-2)(N-3)/2 disjoint edges.
2. chi_1 and chi_2 match the standard eigenvalues for the Johnson-scheme/triangular-graph adjacency operators.
3. Subtraction gives exactly chi_1-chi_2=(N-2)(B-C).

**Disposition:** Algebraically consistent. A manuscript proof should show the action of the response matrix on each sector or cite a precise representation/association-scheme result. Numerical data are not needed for this identity.

## 5. Uniform-path derivative versus independent-edge partials

The identity chi_0=d I_12/dJ_*=A+2(N-2)B+((N-2)(N-3)/2)C is the derivative along the path on which every edge coupling is varied together. A, B, and C are coordinate partial derivatives in the full edge space. These are not interchangeable.

The manuscript correctly distinguishes the uniform response in §5.1 from the sector decomposition in §5.2, but all later uses must retain this convention. The strong-coupling derivative G_N'(x) in Section 4 is a derivative along the uniform path; it is not B-C or any individual-edge response.

## 6. §5.3 — Sign of B-C and evidence conflict

The exact identity is chi_1>chi_2 iff B-C>0, because N-2>0 for N>=3. This orders the two response eigenvalues. It does not by itself prove chi_1>0 or chi_2<0, a hub mode is dynamically unstable, a geometric mode is suppressed, or a global sign of B-C on an entire branch.

For the feedback Jacobian, eigenvalues are g chi_k. Since g>0, their ordering is preserved, but stability still requires comparison of each multiplier with the chosen stability region (for a discrete iteration, modulus less than one).

### 6.1 Numerical evidence

The frozen manuscript reports positive B-C scans for N=4,6,8,10,20 and an h-scan at N=8, while excluding N=50 near x_c due to a gap below the reliability threshold. These are numerical observations on tested points/ranges, not a theorem over all x or all N.

### 6.2 Weak-coupling source conflict — critical

The frozen file docs/lemma_5_2_audit.md states:
- the original negative-sign derivation omitted the order-r^2 coherence rho_{-+,+-}=sum_{k>=3} a_{1k}a_{2k};
- after including it, the corrected leading coefficient is (B-C)_lead = J/(8h^2) ln(2(N-2)/(N-1)) > 0;
- the remainder and its edge derivative remain unbounded in that audit;
- therefore no weak-coupling endpoint theorem or global sign-flip conclusion follows yet.

The older docs/lemma_5_2_proof.md still claims a negative sign and is invalidated by the omitted coherence. Do not cite or rely on that old proof.

The corrected leading coefficient is positive for every fixed N>=4 because 2(N-2)/(N-1)>1. But a positive leading coefficient alone does not prove B-C>0 for sufficiently small J/h unless the remainder is shown to be o(J/h^2) (or otherwise quantitatively dominated) after the edge derivative is taken.

**Finding S5-01 — P0:** Mark weak-coupling theorem status OPEN until the differentiated remainder is proved and its current proof artifact is identified. Remove any negative-sign claim and any claimed global sign flip.

## 7. §5.4 — Interface to Paper 2

The interface is appropriately limited if interpreted as: Paper A supplies the symmetric branch and local bifurcation analysis conditional on Section 3 assumptions; supplies the exact edge-sector decomposition and chi_1-chi_2 identity; and leaves the ordering/sign of chi_1 and chi_2 beyond what follows from B-C unresolved.

The scale covariance chi_k(J,h)=h^{-1} tilde_chi_k(x), x=J/h, is dimensionally correct if I_12 depends only on x and edge derivatives are taken with respect to dimensional J_e. Then feedback eigenvalues scale as g chi_k=(g/h) tilde_chi_k(x)=eta tilde_chi_k(x). Response eigenvalue ordering is independent of the absolute energy scale at fixed x, but dimensional response eigenvalues scale as h^{-1}.

This is covariance, not a result that edge response is geometrically local or that continuum geometry emerges.

## 8. Required corrections to Section 5

1. State N>=4 wherever all three sectors are discussed; mention V_2 is zero for N=3.
2. Add a derivation/citation for the three-sector decomposition and A,B,C eigenvalue formulas.
3. Explicitly label chi_0 as the uniform-path derivative and A,B,C as independent-edge partials.
4. Replace “sufficient for usual saddle-node branch classification” by a local statement conditional on Section 3's nondegenerate fold hypotheses.
5. Keep B-C>0 as an ordering statement only; do not infer instability or geometric suppression without signs and multiplier bounds.
6. Keep numerical evidence ranges and N=50 exclusion explicit; do not call them universal.
7. Remove the old Lemma 5.2 negative-sign theorem and global sign-flip conclusion.
8. Treat corrected weak-coupling coefficient as a leading-order result only until the edge-derivative remainder is bounded.
9. Clarify that Paper 2 inherits an exact decomposition/identity, not an established emergent geometry theorem.

## 9. Proposed replacement for the weak-coupling paragraph

At the symmetric point, the corrected weak-coupling calculation gives the leading coefficient

(B-C)_lead = J/(8h^2) ln(2(N-2)/(N-1)) > 0, for N>=4.

The order-r^2 coherence in the reduced two-site state is essential for this sign. The differentiated remainder required to turn this leading coefficient into a rigorous endpoint sign theorem must be established separately. Until that estimate is proved, the statement is a corrected formal leading-order result, not a theorem asserting B-C>0 for all sufficiently small J/h. No global sign change between weak and strong coupling is claimed.

## 10. Proof-obligation matrix

| ID | Obligation | Disposition |
|---|---|---|
| S5-01 | Three-sector S_N decomposition | STANDARD / PROOF OR PRECISE CITATION NEEDED |
| S5-02 | Sector dimensions and N-domain | ALGEBRAICALLY CONSISTENT; state N>=4 for V_2 nonzero |
| S5-03 | A,B,C orbit classification | EXACT UNDER S_N SYMMETRY |
| S5-04 | chi_0, chi_1, chi_2 formulas | ALGEBRAICALLY CONSISTENT; manuscript derivation needed |
| S5-05 | chi_1-chi_2=(N-2)(B-C) | EXACT ALGEBRA |
| S5-06 | F_J=g chi_0-1 | EXACT along uniform path |
| S5-07 | F_J<0 implies response negative | FALSE; only chi_0<1/g |
| S5-08 | B-C global positive theorem | OPEN; numerical conjecture only |
| S5-09 | Corrected weak-coupling leading coefficient | FORMAL LEADING TERM POSITIVE |
| S5-10 | Weak-coupling differentiated remainder | OPEN / CONFLICTING ARTIFACT STATUS |
| S5-11 | Feedback-sector stability | NOT IMPLIED BY ORDERING ALONE |
| S5-12 | Scale covariance chi_k=h^-1 tilde chi_k | VALID CONDITIONAL ON SMOOTH DIMENSIONLESS RESPONSE |
| S5-13 | Emergent geometry interpretation | MOTIVATION / NOT PROVED |
| S5-14 | Lean formalization and build | NOT RUN |
| S5-15 | Independent external review | NOT RUN |

## 11. Verification boundary

- This is an internal source-level audit.
- The frozen source files were inspected; no upstream file was changed.
- No Lean build or CI was run.
- No independent external review was run.
- The weak-coupling remainder conflict is intentionally left OPEN.
- Paper A remains NOT VERIFIED.
