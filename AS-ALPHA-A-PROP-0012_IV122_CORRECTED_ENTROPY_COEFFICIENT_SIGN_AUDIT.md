# IV-122 — Corrected Fourth-Order Entropy Coefficient: Independent Sign Audit

**Target:** AS-ALPHA-A-PROP-0012  
**Status:** Algebraic derivation independently checked; sign is parameter-dependent in general. Numerical samples are evidence, not a universal sign theorem.

## Starting expansions

For binary entropy h(x)=-x ln x-(1-x)ln(1-x), and
q=e^2 S+e^4 T+O(e^6), q3=e^2 R+e^4 T3+O(e^6), the coefficient of e^4 in h(q)-h(q3) is

C4 = -T ln(e^2 S) - S^2/2 + T3 ln(e^2 R) + R^2/2.

This follows from the direct expansion h(q)=e^2 S(1-ln(e^2 S))+e^4[-T ln(e^2 S)-S^2/2]+O(e^6|ln e|).

## Substitution and simplification

Set X=A^2>0, r=B^2/A^2>0, L=ln(e^2 X), so S=X(1+r), R=Xr,
T/X^2=-3+2r-3r^2, and T3/X^2=5r-3r^2.

Then C4/X^2 simplifies to

C4/X^2 = 3(1+r)L
 +(3-2r+3r^2)ln(1+r)
 +(5r-3r^2)ln(r)
 -(1+2r)/2.

The logarithmic coefficient is 3(1+r), checked by collecting (3-2r+3r^2)+(5r-3r^2).

## Sign audit

The sign is not established as uniformly positive or negative for all (r,e,X) by this calculation. However, for each fixed r>0 and X>0, the coefficient of L is positive, and L=ln(e^2 X) tends to -infinity as e tends to 0. Therefore C4/X^2 tends to -infinity in the fixed-r weak-coupling limit. This is a statement about the fourth-order coefficient alone, not the full entropy difference.

Numerical evaluation at X=1 for representative r values:
- r=0.1: C4/X^2 approximately -16.6095 at e=0.1 and -31.8066 at e=0.01
- r=0.25: -18.8926 and -36.1620
- r=0.5: -21.8212 and -42.5445
- r=1: -26.3584 and -53.9895
- r=2: -33.2481 and -74.6946
- r=4: -43.1880 and -112.2655
- r=10: -59.5125 and -211.4831

These sampled values do not prove a global sign result at fixed finite coupling. No zero-crossing classification is claimed.

## Consequences and limitations

- IV-119's entropy correction is retained.
- IV-121's q, q1, q3 coefficient results are the inputs used here, pending full analytic remainder proof.
- Old fourth-order sign-transfer conclusions IV-115–IV-118 remain invalidated.
- Leading-order coefficient C2 controls the fixed-parameter sufficiently-small-epsilon sign only if its positivity and the remainder control are rigorously established.
- This is not a proof of AS-ALPHA-A-PROP-0012 and no Lean proof is claimed.
