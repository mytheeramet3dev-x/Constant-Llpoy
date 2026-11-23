# IV-191 — Recomputed Normalized Vector Derivative Aggregate

**Project:** Absolute Symmetry — Paper A  
**Proposition:** AS-ALPHA-A-PROP-0012  
**Status:** Conditional norm estimate using IV-190 ceilings.

## 1. Vector and inherited coordinate bounds
Let \(Q=(Q_u,Q_z,Q_w)\). Use upward-rounded IV-190 ceilings:
\[
|(Q_u)_t|,|(Q_z)_t|<17.877242,\quad |(Q_w)_t|<1.156319,
\]
\[
|(Q_u)_p|,|(Q_z)_p|<2.348837,\quad |(Q_w)_p|<0.064618.
\]
These are conditional on IV-180 component derivative ceilings and the corrected \(D=1+tS\) denominator bounds.

## 2. Coordinatewise vector norms
The radial derivative vector satisfies
\[
\|Q_t\|_2<\sqrt{2(17.877242)^2+(1.156319)^2}<25.308668.
\]
The angular derivative vector satisfies
\[
\|Q_p\|_2<\sqrt{2(2.348837)^2+(0.064618)^2}<3.322387.
\]
(The last decimals are rounded upward.)

## 3. Euclidean-input Lipschitz ceiling
For \(\Delta Q\) and inputs \((t,p)\), the Jacobian's Frobenius norm bounds its operator norm:
\[
\|J_Q\|_{op}\le\|J_Q\|_F
=\sqrt{\|Q_t\|_2^2+\|Q_p\|_2^2}.
\]
Hence
\[
\boxed{\|J_Q\|_{op}<25.525810}.
\]
This yields the conditional local/global-on-convex-domain Lipschitz estimate
\[
\|Q(t_1,p_1)-Q(t_2,p_2)\|_2
<25.525810\sqrt{(t_1-t_2)^2+(p_1-p_2)^2},
\]
provided differentiability and all stated derivative/domain bounds hold throughout the connecting segment. The segment/domain condition is explicit and cannot be dropped.

## 4. Scope and comparison
This aggregate is a recomputation from corrected IV-190 ceilings, not a sharp operator-norm calculation. It does not include \(Q_3\) as a fourth vector component; \(Q_3\) is separately bounded in IV-190. It is not a proof of Proposition 0012 or of upstream implicit-root conditions.
