# IV-123 — Leading-Order Positivity: Independent Analytic Proof

**Target:** AS-ALPHA-A-PROP-0012  
**Status:** Leading coefficient positivity proved under an explicit weak-coupling condition; this does not prove the full entropy-difference claim.

## Interior case A,B != 0

Let X=A^2>0, r=B^2/A^2>0, and
C2=1-ln(epsilon^2 X)-(1+r)ln(1+r)+r ln r.

Define H(r)=1-(1+r)ln(1+r)+r ln r. Then
C2=-ln(epsilon^2 X)+H(r).

Algebraically,
H(r)+ln(1+r)=1-r ln(1+1/r).

For r>0, ln(1+t)<t for t>0, so
r ln(1+1/r)<1.
Therefore H(r)>-ln(1+r), strictly.

Consequently,
C2 > -ln(epsilon^2 X)-ln(1+r)
   = -ln(epsilon^2(X+B^2)).

Thus if epsilon^2(X+B^2)<=1, then C2>=0, and the strict inequality above gives C2>0. A slightly more direct sufficient condition is epsilon^2(A^2+B^2)<=1.

## Axis limits

- B=0 (r->0): C2=1-ln(epsilon^2 A^2), positive whenever epsilon^2 A^2<e.
- A=0 (r->infinity, with B fixed): C2=-ln(epsilon^2 B^2), positive whenever epsilon^2 B^2<1.

## Scope / caution

This establishes positivity of the leading-order coefficient C2 for the stated sufficient weak-coupling condition. To infer positivity of the actual entropy difference for sufficiently small epsilon, one still needs the expansion's remainder control, including uniformity/analyticity appropriate to the parameter domain and the entropy logarithms. This is not a full proposition proof and no Lean proof is claimed.
