# IV-226 — Edge Symmetry-Breaking and Leading Small-Eigenvalue Response

**Date:** 2026-11-23
**Target:** AS-ALPHA-A-PROP-0012, retained sites 1,2; environment k>=3; finite N>=4
**Status:** FIRST-ORDER EDGE RESPONSE DERIVED / u34 EXACT EXCHANGE SYMMETRY / LEADING u13 RESPONSE DERIVED / HIGHER-ORDER PAPER CLAIMS OPEN
**Scope:** Compute first derivatives of the first-order pair amplitudes and second-order pair amplitudes in the independent-edge convention; identify symmetry implications for the retained odd Gram block. Not a full manuscript parameterization audit.

## 1. Pair-amplitude formulas

From IV-220/221, for retained i and environment k:
A_ik=g_ik/4,
B_ik=(1/8) sum_{m not i,k} g_im g_mk.

At the uniform point g=1:
A_ik=1/4, B_ik=(N-2)/8.

For a single independent edge q, derivative A is 1/4 iff q={i,k}; otherwise zero. For B, q contributes exactly when it is one edge in a two-edge path i-m-k, and derivative equals 1/8 times the other path edge evaluated at uniform coupling.

## 2. Edge u13: first-order symmetry breaking

Let g13=1+u13. Then:
- ∂u13 A_13=1/4; all other retained/environment A_ik derivatives vanish.
- ∂u13 B_14=1/8 (path 1-3-4).
- ∂u13 B_23=1/8 (path 2-1-3).
- Other B_ik derivatives vanish for environment k>=3, under the independent-edge convention.

The first-order row difference vector d_k=A_1k-A_2k has derivative with respect to u13 equal to a vector supported only at k=3, with component 1/4. Let n=N-2 environment coordinates. For a Gram matrix of two nearly equal real rows, its small eigenvalue at leading order is one-half the squared norm of the row difference projected orthogonally to the common row. At uniform A-row is constant, so:
λ_small(M2(u)) = (u13^2/32)(1-1/n)+O(u13^3).
Equivalently, for the physical odd block O(r), its leading small eigenvalue behaves as
λ_small(O)=r^2 u13^2 (1-1/(N-2))/32 + higher orders in r,u13,
provided the stated amplitude-Gram mapping is used. The quadratic coefficient is positive for N>=4. This is a coefficient-level local result, not a uniform remainder bound.

## 3. Edge u34: exact retained-site exchange symmetry

The edge perturbation g34=1+u34 involves environment sites only and is invariant under the exchange 1↔2. The full Hamiltonian, unperturbed state, and retained-odd/environment construction therefore preserve retained-site exchange for every u34 (with all other couplings symmetric as specified). Hence the two Gram rows remain identical, and the odd-block antisymmetric eigenvalue is exactly zero along this u34-only direction, to all orders in r. This is stronger than the vanishing first-order A derivative; it follows from exact symmetry.

The explicit second-order path formula also gives:
∂u34 B_13=∂u34 B_23=1/8,
∂u34 B_14=∂u34 B_24=1/8,
with other environment-pair entries unaffected; these derivatives are matched between retained rows, consistent with symmetry.

## 4. Limits and open issues

- First-order pair-amplitude derivatives: **DERIVED**.
- Listed second-order pair-amplitude derivatives for u13/u34: **DERIVED** by path formula.
- Leading local u13 small-eigenvalue coefficient in the first-order Gram matrix: **DERIVED** for fixed finite N>=4.
- Exact zero along u34-only symmetry-preserving path: **SYMMETRY-DERIVED** within independent-edge model.
- Higher-order cross terms in r and u13, full normalized amplitude reconstruction, uniform remainder, entropy derivatives, manuscript-to-independent-edge parameter mapping, original B-C response sign: **OPEN**.
- No Lean proof or independent executable enumeration performed in this audit.

## 5. Next obligation

IV-227 should test the local u13 result using an explicit finite-N Gram-matrix construction and exact rational arithmetic for representative N, then reconcile the resulting coefficient with the manuscript's B-C derivative (not assume they are the same quantity). It should also audit whether the paper's u34 direction truly preserves retained-site exchange symmetry under the full coupling family.
