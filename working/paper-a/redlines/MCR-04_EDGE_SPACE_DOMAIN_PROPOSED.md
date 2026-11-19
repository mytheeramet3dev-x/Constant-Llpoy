# MCR-04 — Proposed Redline: Domain of the Edge-Space Decomposition

- **Document ID:** CL-PA-RL-MCR-04
- **Status:** PROPOSED DOMAIN CLARIFICATION
- **Affected claim:** AS-ALPHA-A-PROP-0005
- **Frozen source:** `mytheeramet3dev-x/Absolute_Sym`, commit `8deb7de4a49cb2060720246b7101820ee7e08c91`
- **Source location:** §5.2
- **Source blob:** `671c97fa68fa48c929760bf9956d197b358c4904`
- **Correction register item:** MCR-04

## 1. Domain issue

The edge space has dimension \(\binom N2\). The displayed decomposition
\[
\mathcal V_{\rm edge}=\mathcal V_0\oplus\mathcal V_1\oplus\mathcal V_2
\]
with dimensions
\[
\dim\mathcal V_0=1,\qquad
\dim\mathcal V_1=N-1,\qquad
\dim\mathcal V_2=\frac{N(N-3)}2
\]
is valid for \(N\ge3\). At \(N=3\), the last dimension is zero, so \(\mathcal V_2\) is absent as a nonzero sector. For \(N=2\), the displayed three-sector dimension formula is not an appropriate decomposition.

If the manuscript wants all three response-sector eigenvalues to represent nonzero eigenspaces, it should use \(N\ge4\).

## 2. Proposed replacement wording

> For \(N\ge3\), the permutation representation on the edges of the complete graph decomposes into the uniform sector, the standard sector, and the residual sector, with dimensions
> \[
> 1,\qquad N-1,\qquad \frac{N(N-3)}2,
> \]
> respectively. At \(N=3\), the residual sector has dimension zero and is omitted. In the nontrivial three-sector setting \(N\ge4\), the response matrix has the three sector eigenvalues \(\chi_0,\chi_1,\chi_2\) displayed below.

The formulas for \(\chi_0,\chi_1,\chi_2\) may remain as written for \(N\ge4\). If the authors wish to state an \(N=3\) special case, they must state only the two eigenvalues associated with nonzero sectors and must not call \(\chi_2\) an eigenvalue on a zero-dimensional space.

## 3. Exact identity

The algebraic subtraction
\[
\chi_1-\chi_2=(N-2)(B-C)
\]
is valid wherever both displayed expressions are being compared as the stated sector formulas. Keep this exact identity separate from any sign conjecture for \(B-C\).

## 4. Verification obligations

1. Verify the representation decomposition and dimension count for \(N\ge3\).
2. Verify the orbit counts defining \(A,B,C\).
3. Verify the sector eigenvalue formulas and the subtraction identity.
4. Treat \(N=3\) as a zero-dimensional residual-sector edge case.
5. Exclude \(N=2\) from this three-sector statement or prove its separate decomposition.

## 5. Disposition

**PROPOSED DOMAIN QUALIFICATION — THREE NONZERO SECTORS FOR \(N\ge4\); DECOMPOSITION FORMULA WITH ZERO RESIDUAL SECTOR AT \(N=3\).**

This file is a separate Constant Llpoy redline. It does not modify the frozen source snapshot or upstream `Absolute_Sym`.
