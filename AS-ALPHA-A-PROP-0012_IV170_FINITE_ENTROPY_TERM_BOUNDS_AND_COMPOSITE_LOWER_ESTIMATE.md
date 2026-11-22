# Paper A — IV-170: Finite Entropy Term Bounds and Composite Lower Estimate

## Status
This note bounds the finite (non-logarithmic) entropy term using the inherited normalized-factor upper bounds from IV-166, and combines it with IV-169's logarithmic-coefficient certificate. The IV-165/166 constants remain provisional pending independent audit; consequently, this composite estimate is conditional on those bounds.

## 1. Finite-term notation
Define
\[
\Phi(a)=a\log(1/a)+a=a(1-\log a),\quad \Phi(0)=0.
\]
For \(q=tQ\), \(q_3=t\varepsilon Q_3\), \(\varepsilon=1-p\), IV-168 gives
\[
h(q)-h(q_3)=tC(t,p)\log(1/t)+t[\Phi(Q)-\Phi(\varepsilon Q_3)]+g(q)-g(q_3).
\]

## 2. Range and elementary bound for Phi
Conditional on IV-166's reported bounds \(0<Q\le2.265265\) and \(0<Q_3\le1.197133\), both arguments of Phi lie in \([0,2.265265]\subset(0,e)\), with endpoint zero understood continuously. Since \(\Phi'(a)=-\log a\), Phi increases on (0,1), decreases on (1,e), and satisfies \(0\le\Phi(a)\le1\) for \(0\le a\le2.265265\). Hence
\[
\boxed{-1\le\Phi(Q)-\Phi(\varepsilon Q_3)\le1.}
\]
This bound is intentionally coarse and does not claim endpoint-uniform cancellation.

## 3. Regularized remainder bound
Since \(q,q_3\le1/2\), IV-168 gives
\[
|g(q)-g(q_3)|\le q^2+q_3^2
=t^2[Q^2+\varepsilon^2Q_3^2].
\]
Using the conditional upper bounds,
\[
Q^2+\varepsilon^2Q_3^2
\le2.265265^2+1.197133^2<6.570.
\]
Thus
\[
|g(q)-g(q_3)|<6.570t^2.
\]

## 4. Combined lower estimate
Combining the finite-term and remainder bounds with IV-169's \(C(t,p)\ge c_*p\) yields, conditionally,
\[
\boxed{
h(q)-h(q_3)\ge
0.83678321389\,tp\log(1/t)-t-6.570t^2
}
\]
for \(0<t\le1/64\). The exact coefficient \(c_*\) is the rational expression recorded in IV-169; displayed decimals are rounded.

For the paper's entropy difference \(\Delta S=2[h(q)-h(q_3)]\), multiply the entire right-hand side by two.

## 5. Endpoint caveat
At \(p=0\), the exact factorization gives \(q=q_3\), so \(h(q)-h(q_3)=0\). The coarse bound above may be negative there and is not sharp. It therefore does not establish global positivity of the full entropy difference, particularly near the angular endpoint where the leading logarithmic term is proportional to \(p\).

## 6. Next proof obligations
1. Independently audit IV-165/166 normalized probability bounds.
2. Improve finite-term estimate to preserve angular factor near \(p=0\), or derive a direct endpoint-aware comparison.
3. Establish an explicit threshold region where the current composite lower estimate is positive, if useful.
4. Do not infer global positivity of \(\Delta S\) from this estimate.

This is a conditional analytic estimate, not Lean-certified.
