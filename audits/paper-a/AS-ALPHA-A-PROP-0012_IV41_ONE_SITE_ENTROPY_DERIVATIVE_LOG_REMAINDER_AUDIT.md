# IV-41 — One-Site Entropy Derivative Expansion & Logarithmic Remainder Audit

**Status:** ALGEBRAIC EXPANSION PASS / UNIFORM DERIVATIVE BOUND CONDITIONAL / PAPER COEFFICIENT OPEN  
**Scope:** Derive the one-site entropy and edge derivative expansions from an assumed small-eigenvalue expansion, isolate logarithmic terms, and avoid inferring derivative bounds from value bounds alone.

## 1. Exact entropy and derivative

For a one-site reduced state with eigenvalues (p) and (1-p), where (0<p<1),
[
S(p)=-pln p-(1-p)ln(1-p).
]
Differentiating along an edge parameter (u):
[
S_u=p_ulnrac{1-p}{p}.
]
This is exact. When (pll1),
[
S_u=p_uleft[-ln p+ln(1-p)ight].
]
Since (ln(1-p)=-p+O(p^2)), this yields
[
S_u=-p_uln p-p p_u+O(p^2p_u).
]
This asymptotic form requires small positive p and controlled p_u; it does not extend directly to p=0.

## 2. Expansion with a positive leading coefficient

Assume on an edge-parameter neighborhood that
[
p(u,r)=r^2a(u)+r^3b(u)+O(r^4),
quad r>0,
]
with (a(u)>0). More strongly, suppose
[
p=r^2a(u,r),quad a(u,r)ge a_*>0,
]
and (a,a_u) are bounded on the neighborhood. Then
[
ln p=2ln r+ln a(u,r),
quad p_u=r^2a_u(u,r).
]
Therefore the exact derivative becomes
[
S_u=r^2a_u(u,r)left[-2ln r-ln a(u,r)+ln(1-r^2a(u,r))ight].
]
This formula separates the logarithmic factor from the bounded coefficient. Under the stated bounds, the scale is (O(r^2(1+|ln r|))).

## 3. Formal coefficient through the next order

For a fixed smooth expansion (p=r^2a+r^3b+O(r^4)) with (a>0) and the corresponding derivative expansion controlled,
[
ln p=2ln r+ln a+rac{r b}{a}+O(r^2).
]
Also (p_u=r^2a_u+r^3b_u+O(r^4)). Substitution gives
[
S_u=r^2a_u(-2ln r-ln a)
+r^3left[b_u(-2ln r-ln a)-rac{b,a_u}{a}ight]
+O(r^4(1+|ln r|)),
]
provided the remainder and its edge derivative are uniformly controlled. The term (ln(1-p)) contributes only at order (r^4) to this expression under these assumptions.

## 4. Value bounds do not imply derivative bounds

A remainder (R(u,r)=O(r^4)) pointwise does not imply (R_u=O(r^4)). Uniform derivative control needs additional hypotheses, e.g. a uniformly differentiable remainder bound or a uniform holomorphic neighborhood with Cauchy estimates. This remains one of the project's unresolved proof obligations.

## 5. Zero-leading-coefficient case

If (a(u)=0) at a point, the logarithm (ln a) is invalid. The branch must be treated by a separate factorization or vanishing-order analysis. Positivity of (p) alone does not provide the required derivative estimate near a zero-leading branch.

## 6. Disposition

- Exact binary entropy derivative: **PASS**.
- Positive-leading-coefficient expansion: **PASS, conditional on stated uniform smoothness**.
- (O(r^4)) value remainder implying (O(r^4)) derivative: **NOT VALID WITHOUT ADDITIONAL HYPOTHESES**.
- Zero-leading branch: **OPEN**.
- Reconciliation with full two-site contribution and (B-C): **OPEN**.
- Lean formalization/build: **NOT PERFORMED**.

PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.
