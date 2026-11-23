# IV-195 — Conditional Lipschitz Inference and Bound Recalculation Audit

**Project:** Absolute Symmetry — Paper A  
**Proposition:** AS-ALPHA-A-PROP-0012  
**Status:** Norm arithmetic independently recomputed; Lipschitz inference remains conditional on derivative and branch/domain hypotheses.

## 1. Inputs

Using the rounded-up IV-190 component derivative ceilings, as inherited and aggregated in IV-191:
\[
|(Q_u)_t|,|(Q_z)_t|<17.877242,\quad |(Q_w)_t|<1.156319,
\]
\[
|(Q_u)_p|,|(Q_z)_p|<2.348837,\quad |(Q_w)_p|<0.064618.
\]

## 2. Recomputed column-norm ceilings

For the radial column:
\[
L_t=\sqrt{2(17.877242)^2+(1.156319)^2}
=25.30866722454758\ldots<25.308668.
\]

For the angular column:
\[
L_p=\sqrt{2(2.348837)^2+(0.064618)^2}
=3.3223855873546646\ldots<3.322387.
\]

Combining the columns:
\[
L_F=\sqrt{L_t^2+L_p^2}
=25.525808168870007\ldots<25.525810.
\]
The stated ceilings are valid upward roundings for these rounded component inputs.

## 3. Conditional Lipschitz statement

If \(Q:\mathcal U\subset\mathbb R^2\to\mathbb R^3\) is differentiable on a neighborhood of the connecting segment between \(x,y\in\mathcal U\), and the above derivative ceilings hold uniformly along that segment, then:
\[
\|Q(x)-Q(y)\|_2\le25.525810\|x-y\|_2.
\]
This follows from the fundamental theorem of calculus along the segment and the Frobenius bound on the Jacobian:
\[
\|J_Q\|_{op}\le\|J_Q\|_F.
\]

The result applies to pairs whose connecting segment stays inside the verified derivative-valid domain. Convexity of the explicit rectangular box \([0,1/64]\times[0,1]\) was verified in IV-194, but the existence, uniqueness, and differentiability of the implicit-root branch on that entire box were **not** established. Therefore the statement is not promoted to a global theorem on the full box or on the complete admissible solution set.

## 4. Scope

- The norm arithmetic is independently recomputed from IV-191's rounded inputs.
- The Frobenius/operator-norm inequality is mathematically valid.
- The conditional mean-value/Lipschitz argument is valid on segments satisfying the stated differentiability and uniform-bound hypotheses.
- Component derivative ceilings and their upstream assumptions have not been fully independently derived in this record.
- No contraction mapping conclusion, implicit-root closure, or proof of PROP-0012 is claimed.

## 5. Verdict

**Conditional Lipschitz inference: pass. Full-domain Lipschitz closure: open.** The numerical aggregate is valid for the inputs; theorem-level promotion requires the implicit branch/domain and uniform derivative premises to be proved.
