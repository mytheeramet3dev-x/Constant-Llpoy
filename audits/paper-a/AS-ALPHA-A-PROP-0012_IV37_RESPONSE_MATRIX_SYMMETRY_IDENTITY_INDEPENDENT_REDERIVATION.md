# IV-37 — Response Matrix and Symmetry Identity Independent Re-derivation

**Target:** Exact identity \\(\\chi_1-\\chi_2=(N-2)(B-C)\\) at the permutation-symmetric point  
**Status:** ANALYTIC-VERIFIED / SOURCE-CONFIRMED / NOT-LEAN-VERIFIED  
**Scope:** Independently reconstruct the edge-response matrix combinatorics from the exact definitions of (A,B,C), then rederive the three sector eigenvalues and subtraction identity. No weak-coupling approximation is used.

## 1. Response matrix on edge space

Let edge indices be unordered pairs (e,f\in E(K_N)). At the fully permutation-symmetric point, the response matrix (R) has entries determined by the orbit of ((e,f)):
- same edge: (R_{e,e}=A);
- distinct edges sharing one vertex: (R_{e,f}=B);
- disjoint edges: (R_{e,f}=C).

For fixed edge (e={1,2}), the counts are:
- one same edge;
- (2(N-2)) adjacent distinct edges;
- ((N-2)(N-3)/2) disjoint edges.

This gives the constant-vector sector eigenvalue
[
\chi_0=A+2(N-2)B+\frac{(N-2)(N-3)}2C.
]

## 2. Degree-vector sector

Represent an edge vector in the standard vertex sector by (v_{ij}=x_i+x_j), with (sum_i x_i=0). For fixed edge (12), the response sum over adjacent edges and disjoint edges is evaluated using the zero-sum constraint. The resulting coefficient of (x_1+x_2) gives
[
\chi_1=A+(N-4)B-(N-3)C.
]

## 3. Residual degree-preserving sector

For (v) in the residual sector, all vertex sums vanish: (sum_{j\ne i}v_{ij}=0). On a fixed edge (12), the adjacent-edge sum is (-2v_{12}), and the disjoint-edge sum is (v_{12}), using total edge sum zero and the endpoint row sums. Thus
[
\chi_2=A-2B+C.
]

## 4. Exact subtraction

Subtract:
[
\begin{aligned}
\chi_1-\chi_2
&=[A+(N-4)B-(N-3)C]-[A-2B+C]\\
&=(N-2)B-(N-2)C\\
&=\boxed{(N-2)(B-C)}.
\end{aligned}
]

This is a purely combinatorial identity in the symmetric edge-response matrix. It does not require differentiability beyond the existence of the response entries, a perturbative expansion, positivity, or spectral estimates.

## 5. Disposition

- Response-matrix orbit counts: **PASS**.
- Constant-sector formula: **PASS**.
- Standard vertex-sector formula: **PASS**.
- Residual sector formula: **PASS**.
- Difference identity: **PASS exact algebraically**.
- Frozen Section 5 source: **CONFIRMED**.
- Lean formalization/build: **NOT PERFORMED**.
- Weak-coupling sign of (B-C): **NOT established by this identity**.

PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.