# IV-221 — Environment-Resolved Odd-Block Cubic Null Evaluation

**Date:** 2026-11-23  
**Target:** AS-ALPHA-A-PROP-0012, fixed finite \(N\ge4\), retained sites \(1,2\)  
**Status:** CUBIC COEFFICIENT AT UNIFORM POINT DERIVED / EDGE-DERIVATIVE CANCELLATION DERIVED / HIGHER-ORDER BRANCH OPEN / NOT VERIFIED  
**Scope:** Explicitly map the first- and second-order global x-basis amplitudes to the retained-odd/environment-single-flip sector and evaluate the cubic odd-block null combination. No numerical experiment or Lean proof is claimed.

## 1. Basis and sector mapping

Use the x-polarized unperturbed ground state and flip-set notation \(|S\rangle\). For the retained pair \(1,2\), the odd subsystem basis states \(|+-\rangle\) and \(|-+\rangle\) correspond to global flip sets \(\{1\}\) and \(\{2\}\), respectively. Global parity is even, so the environment must carry odd flip parity. At first order, the only environment configurations in this sector are single flips \(\{k\}\), \(k=3,\dots,N\), giving global pair-flip states \(\{1,k\}\) and \(\{2,k\}\).

For each environment-single-flip configuration \(k\), define the amplitude rows
\[
c_{1k}=r a_{1k}+r^2 b_{1k}+O(r^3),\quad
c_{2k}=r a_{2k}+r^2 b_{2k}+O(r^3).
\]
The first- and second-order pair-flip coefficients are those derived in IV-220:
\[
a_{ik}=g_{ik}/4,
\]
\[
b_{ik}=\frac1{16}\sum_{m\ne i,k}
(g_{im}g_{mk}+g_{km}g_{mi}),
\]
where the two ordered intermediate pair paths are explicitly represented. For real symmetric edge weights this simplifies to
\[
\boxed{b_{ik}=\frac1{8}\sum_{m\ne i,k}g_{im}g_{mk}.}
\]
This formula is equivalent to the IV-220 ordered-path expression for the pair target \(\{i,k\}\). It assumes the same perturbative convention and independent edge weights \(g\).

Environment configurations with three flips first occur at second order and have amplitudes \(O(r^2)\); their products contribute to the reduced odd block at \(O(r^4)\), not at cubic order. The normalized-ground-state correction multiplying first-order amplitudes starts at order \(r^3\), so it likewise cannot change the cubic block coefficient.

## 2. Odd-block cubic entries

The reduced odd block is the environment Gram sum:
\[
O_{ij}=\sum_{k=3}^N c_{ik}\overline{c_{jk}}+O(r^4),
\]
where the omitted three-environment-flip configurations enter at fourth order. For real amplitudes, the cubic coefficient is
\[
O^{(3)}_{ij}=\sum_{k=3}^N(a_{ik}b_{jk}+b_{ik}a_{jk}).
\]
Consequently, for \(v=(1,-1)/\sqrt2\),
\[
B_{vv}=\frac{O^{(3)}_{11}+O^{(3)}_{22}-O^{(3)}_{12}-O^{(3)}_{21}}2
=\boxed{\frac12\sum_{k=3}^N(a_{1k}-a_{2k})(b_{1k}-b_{2k})}.
\]
This last factorization is an explicit algebraic reduction, not a symmetry assumption.

## 3. Uniform complete-graph evaluation

At the uniform point \(g_{ij}=1\),
\[
a_{1k}=a_{2k}=\frac14,\qquad
b_{1k}=b_{2k}=\frac{N-2}{8}
\]
for every environment index \(k\). Thus each term in the factored cubic null sum is zero, and
\[
\boxed{B_{vv}(g\equiv1)=0.}
\]
All four cubic block entries are equal:
\[
O^{(3)}_{11}=O^{(3)}_{22}=O^{(3)}_{12}=O^{(3)}_{21}
= (N-2)\frac{N-2}{16}
=\frac{(N-2)^2}{16}.
\]
The null combination vanishes exactly. This resolves the cubic coefficient at the symmetric coupling point within the stated amplitude-sector reconstruction.

## 4. First derivatives at the uniform point

Let \(u_q\) perturb one edge weight, \(g_q=1+u_q\), while other weights remain at one. Since at the uniform point both differences in the factorization vanish,
\[
\partial_{u_q}B_{vv}
=\frac12\sum_k\left[
(\partial_{u_q}a_{1k}-\partial_{u_q}a_{2k})(b_{1k}-b_{2k})
+(a_{1k}-a_{2k})(\partial_{u_q}b_{1k}-\partial_{u_q}b_{2k})
\right]_{g\equiv1}=0.
\]
This applies to the frozen edge directions \(u_{13}\) and \(u_{34}\), and indeed to any independent edge perturbation, because both base-point difference factors are zero. It does **not** imply \(B_{vv}\) vanishes away from the uniform point; its expression is generally quadratic in the first/second-order amplitude differences.

## 5. Perturbative implication and limitations

The calculation establishes that the cubic null-direction coefficient is zero at the uniform point and its first edge derivatives vanish there, under the explicit x-basis amplitude mapping and finite-N perturbative convention. This removes the previously uncomputed cubic coefficient at the point and in its first directional derivatives.

It does not establish:
- that the small eigenvalue begins at \(r^4\) with a strictly positive coefficient;
- the quartic Schur coefficient \(C_{vv}-|B_{uv}|^2/a_+\);
- the fourth-order determinant or its edge derivatives;
- uniform-in-N remainder bounds;
- entropy derivative closure or the full \(B-C\) sign;
- correspondence of the manuscript's complete perturbation/edge parameterization beyond the explicit independent-edge model stated here;
- Lean verification.

The cubic cancellation is therefore a coefficient-level analytic result, not promotion of PROP-0012.

## 6. Disposition

- Retained-odd/environment-single-flip mapping: **DERIVED** for the stated x-basis convention.
- First-order row amplitudes: **DERIVED**.
- Second-order pair target coefficients: **DERIVED / IV-220 CONSISTENT**.
- Cubic odd-block entry formula and null factorization: **DERIVED**.
- Uniform point \(B_{vv}=0\): **DERIVED**.
- First edge derivatives \(\partial_{u_{13}}B_{vv}=\partial_{u_{34}}B_{vv}=0\) at uniform point: **DERIVED**.
- Cubic coefficient away from uniform point: **NOT CLAIMED ZERO**.
- Quartic branch coefficient, positivity, entropy remainder, and global response sign: **OPEN**.
- Lean or numerical verification: **NOT PERFORMED**.

## 7. Next obligation

IV-222: reconstruct the fourth-order odd-block coefficient, including all fourth-order amplitude contributions and three-flip environment states, then evaluate the Schur correction \(C_{vv}-|B_{uv}|^2/a_+\) and its \(u_{13},u_{34}\) derivatives. Preserve the distinction between a formal coefficient and a controlled remainder/positivity theorem.
