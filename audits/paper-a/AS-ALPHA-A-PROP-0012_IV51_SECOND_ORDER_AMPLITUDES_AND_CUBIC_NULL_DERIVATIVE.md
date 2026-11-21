# IV-51 — Second-Order Pair Amplitudes and Cubic Null-Direction Derivative

**Status:** SECOND-ORDER SHARED-VERTEX FORMULA RE-DERIVED / CUBIC NULL DERIVATIVE CANCELLED AT UNIFORM POINT / FULL CLAIM OPEN  
**Scope:** Retained sites 1,2; environment configurations with one environment flip; uniform all-to-all coupling J, and edge derivatives B=J13 and C=J34. Analytic algebra only; no Lean or independent numerical check claimed.

## 1. Second-order amplitudes and denominators

In the x-basis, H0=-h sum sigma_i^x. A configuration with q flips has excitation energy 2hq. The first-order pair state |ik> has gap 4h and amplitude a_ik=J_ik/(4h).

For a second-order amplitude ending at the same two-flip configuration {i,k}, only two distinct pair-flip edges sharing one vertex m can have symmetric difference {i,k}: edges (i,m) and (k,m), with m outside {i,k}. Each ordered path has two denominators: final gap 4h and intermediate pair gap 4h, yielding J_im J_km/(16h^2). The two orders add. Thus
b_ik = sum_{m not i,k} J_im J_km/(8h^2).
This is the second-order coefficient for the two-flip configuration, with intermediate vacuum excluded in the standard intermediate-normalization formula. Four-flip final configurations arise from disjoint-edge paths but do not contribute to the cubic odd-block entries considered here, since those environment configurations have no first-order amplitude.

## 2. Cubic odd-block entries

Let environment index k run over {3,...,N}. At uniform couplings J, define g=J/(4h), and b= (N-2)J^2/(8h^2)=2(N-2)g^2. The cubic entries from IV-50 are:
O11^(3)=2 sum_{k=3}^N a_1k b_1k,
O22^(3)=2 sum_{k=3}^N a_2k b_2k,
O12^(3)=sum_{k=3}^N (a_1k b_2k+b_1k a_2k),
with O21=O12 for real couplings.
At the uniform point a_ik=g and b_ik=b for all retained/environment pairs, so every cubic entry equals 2(N-2)g b. The cubic matrix is proportional to [[1,1],[1,1]], hence its null-direction expectation B_vv is zero at the uniform point.

## 3. Derivative in B=J13

At the uniform point, differentiating the formulas with respect to J13 gives:
D_B O11^(3)=J^2(2N-5)/(16h^3),
D_B O22^(3)=J^2/(16h^3),
D_B O12^(3)=J^2(N-2)/(16h^3).
The null combination is
D_B B_vv = (D_B O11+D_B O22-2D_B O12)/2 = 0.
This is an explicit cancellation in the cubic contribution to the low odd-branch coefficient, at the uniform point and for the B edge direction.

## 4. Derivative in C=J34

At the uniform point:
D_C O11^(3)=D_C O22^(3)=D_C O12^(3)=J^2/(8h^3),
so D_C B_vv=(D_C O11+D_C O22-2D_C O12)/2=0.
The edge C is disjoint from the retained pair; its cubic influence enters the shared-vertex second-order amplitudes for environment k=3 or 4, and cancels in the null combination at this order.

## 5. Limits and status

- The shared-vertex second-order two-flip amplitude is re-derived from the energy denominators.
- The cubic null coefficient and its B and C derivatives vanish at this cubic perturbative order at the uniform coupling point.
- This does **not** prove the low odd eigenvalue starts at r^4: fourth-order block entries and the Schur/eigenvalue correction remain necessary.
- It does not prove the full entropy derivative remainder, all-coupling behavior, or the sign of B-C.
- Lean verification: NOT PERFORMED. No independent numerical implementation was performed.

**Disposition:** second-order amplitude formula PASS (analytic path/denominator derivation); cubic null cancellation and B/C derivative cancellation PASS (uniform-point cubic algebra); low-branch r^4 coefficient and Paper A B-C response OPEN. PROP-0012 remains OPEN / ANALYTIC-PARTIAL / NOT VERIFIED.
