# IV-121 — Independent Endpoint Probability Re-Derivation

**Target:** AS-ALPHA-A-PROP-0012  
**Status:** Symbolic coefficient audit executed; endpoint probabilities through epsilon^4 confirmed. This is not a full proposition proof.

## Method

Starting from the four coupled equations for the even-parity X-basis eigenvector (1,u,w,z) and eigenvalue -3+delta,
```
(4-delta)u - 4 b w = 4a
(4-delta)w - 4 b u - 4 a z = 0
(4-delta)z - 4 a w = 4b
delta = -4 a u - 4 b z
```
with a=epsilon A and b=epsilon B, a coefficient-by-coefficient symbolic solution was executed in SymPy for amplitudes through epsilon^5.

## Amplitudes

```
u = A eps + (-A^3 + A B^2) eps^3
    + (2 A^5 - 4 A^3 B^2 - 2 A B^4) eps^5 + O(eps^6)

w = 2 A B eps^2 - 2 A B (A^2+B^2) eps^4 + O(eps^6)

z = B eps + (A^2 B - B^3) eps^3
    + (-2 A^4 B - 4 A^2 B^3 + 2 B^5) eps^5 + O(eps^6)

delta = -4(A^2+B^2) eps^2
      + 4(A^4 - 2 A^2 B^2 + B^4) eps^4 + O(eps^6)
```

## Normalized endpoint probabilities

Using D=1+u^2+w^2+z^2 and q=(u^2+z^2)/D, q1=(u^2+w^2)/D, q3=(z^2+w^2)/D, the executed series give:

```
q  = (A^2+B^2) eps^2
   + (-3 A^4 + 2 A^2 B^2 - 3 B^4) eps^4 + O(eps^6)

q1 = A^2 eps^2
   + (-3 A^4 + 5 A^2 B^2) eps^4 + O(eps^6)

q3 = B^2 eps^2
   + (5 A^2 B^2 - 3 B^4) eps^4 + O(eps^6)
```

## Audit comparison

- IV-107's q1 and q3 coefficients are **confirmed** by this independent coefficient solve.
- IV-110's probability coefficient T = -3 A^4 + 2 A^2 B^2 - 3 B^4 is **confirmed**.
- This audit does not validate the superseded entropy fourth-order formulas. Use IV-119/IV-120's corrected entropy expansion.
- Computation is local symbolic evidence. A full proof still needs a justified analytic remainder/regularity argument and reconciliation with the manuscript's definitions and proposition statement.

