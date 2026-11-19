# MCR-11 — Proposed Redline: Uniform-Path Response and Derivative Convention

- **Document ID:** CL-PA-RL-MCR-11
- **Status:** PROPOSED DEFINITION LOCK AND ALGEBRAIC CLARIFICATION
- **Affected claim:** AS-ALPHA-A-PROP-0010
- **Frozen source:** `mytheeramet3dev-x/Absolute_Sym`, commit `8deb7de4a49cb2060720246b7101820ee7e08c91`
- **Source location:** §5.1; cross-reference §5.2
- **Source blob:** `671c97fa68fa48c929760bf9956d197b358c4904`
- **Correction register item:** MCR-11

## 1. Distinguish the uniform path from one-edge derivatives

Let the independent edge couplings be \(\mathbf J=(J_e)_{e\in E(K_N)}\), and define the uniform path by
\[
J_e=J_\mathrm{u}\quad\text{for every edge }e.
\]
For the observed pair \(12\), define the independent-edge response entries at the symmetric point:
\[
A=\partial_{J_{12}}I_{12},\qquad
B=\partial_{J_{13}}I_{12},\qquad
C=\partial_{J_{34}}I_{12},
\]
where \(J_{13}\) shares one endpoint with edge \(12\) and \(J_{34}\) is disjoint.

The derivative along the uniform path is the directional derivative in which every edge changes at unit rate:
\[
\frac{d}{dJ_\mathrm{u}}
I_{12}(J_\mathrm{u},\ldots,J_\mathrm{u};h)
=
\sum_{e\in E(K_N)}\partial_{J_e}I_{12}.
\]
By permutation symmetry, this equals
\[
\chi_0
=A+2(N-2)B+\frac{(N-2)(N-3)}2C.
\]
Thus the notation \(\partial I_{12}/\partial J\) in §5.1 must mean this uniform-path derivative, not one selected edge derivative.

## 2. Exact branch inequality and its non-implication

Define the scalar uniform-path fixed-point function
\[
F(J_\mathrm{u};g,h)
=gI_{12}(J_\mathrm{u},h)-J_\mathrm{u},
\]
where \(I_{12}(J_\mathrm{u},h)\) is evaluated with all edges equal to \(J_\mathrm{u}\). At a differentiable fixed point,
\[
F_J=g\chi_0-1.
\]
For \(g>0\),
\[
F_J<0
\quad\Longleftrightarrow\quad
\chi_0<\frac1g.
\]
This is an exact upper bound. It does not imply \(\chi_0<0\). The latter is equivalent to the strictly stronger condition
\[
F_J<-1.
\]

**Proposed replacement wording:**

> Here \(F_J\) denotes differentiation along the uniform path on which every edge coupling changes together. By permutation symmetry this derivative is the uniform response eigenvalue \(\chi_0\), so \(F_J=g\chi_0-1\). The branch condition \(F_J<0\) gives the exact upper bound \(\chi_0<1/g\); it does not determine the sign of \(\chi_0\). A negative uniform response requires the stronger inequality \(F_J<-1\). None of these uniform-path statements is a claim about an individual edge derivative such as \(A\), \(B\), or \(C\).

## 3. Required definition and domain notes

- State \(g>0\) for the inequality division.
- State differentiability of the mutual information along the uniform path at the point.
- Define the uniform path explicitly before using \(F_J\).
- Keep \(A,B,C\) as ambient independent-edge partial derivatives.
- Use \(\chi_0\) for the uniform direction; do not silently identify it with \(A\) or \(B\).
- Keep the scalar Picard multiplier condition distinct: for the dimensional \(J_\mathrm{u}\)-iteration, \(|1+F_J|<1\) is equivalent to \(-2<F_J<0\).

## 4. Verification obligations

1. Verify the orbit counts in the uniform derivative sum: one observed edge, \(2(N-2)\) adjacent edges, and \((N-2)(N-3)/2\) disjoint edges.
2. Verify the chain rule along the all-edges-equal path.
3. Formalize the algebraic implication and counter-implication.
4. Check that all occurrences of \(F_J\) in §§3–5 use the same dimensional variable and derivative convention, or explicitly distinguish them.
5. Do not infer response negativity or nonuniform-sector stability from \(F_J<0\).

## 5. Disposition

**PROPOSED CLARIFICATION — EXACT UNIFORM-DIRECTION ALGEBRA; RESPONSE SIGN NOT IMPLIED.**

This file is a separate Constant Llpoy redline. It does not modify the frozen source snapshot or upstream `Absolute_Sym`.
