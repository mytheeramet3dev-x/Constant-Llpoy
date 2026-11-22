# IV-165 — Squared Component Derivative and Normalization Bounds

## Domain and inherited constants
Work on \(0\le t\le1/64\), \(0\le p\le1\). Inherit conservative rounded-up bounds
\(d\le d_*=256/63\), \(d\ge4\), \(F=d^2-16t\ge F_*=63/4\),
\(|d_t|\le7.455139\), and \(|d_p|\le0.003968254\).
This calculation uses these inherited bounds as assumptions; it does not re-audit their derivations.

Let \(M=d_*^2+1/4\), and define \(H=(d^2F^2)^{-1}\). Then
\(H\le H_*=1/(16F_*^2)\).
From chain-rule estimates:
\[
|A_t|,|G_t|,|F_t|\le76.587797,\quad
|A_p|,|G_p|\le0.532250,\quad |F_p|\le0.032250.
\]
Using logarithmic differentiation of H:
\[
|H_t|\le H_*\left(2(7.455139)/4+2(76.587797)/F_*\right)<0.003389520,
\]
\[
|H_p|\le H_*\left(2(0.003968254)/4+2(0.032250)/F_*\right)<1.531711\times10^{-6}.
\]

## Squared regularized components
Set
\[
P_u=u^2/t=16pA^2H,\quad
P_z=z^2/t=16(1-p)G^2H,\quad
P_w=w^2/t=1024tp(1-p)/F^2.
\]
Direct product-rule bounds (all rounded upward) are:
\[
P_u,P_z<1.132633,\quad P_w<0.016125,
\]
\[
|(P_u)_t|,|(P_z)_t|<25.587618,\quad |(P_w)_t|<1.188821,
\]
\[
|(P_u)_p|,|(P_z)_p|<1.211448,\quad |(P_w)_p|<0.032250.
\]
These are conservative uniform bounds over the stated closed rectangle, conditional on inherited d-derivative bounds.

## Normalization
Let \(S=P_u+P_z+P_w\), so \(D=1+tS\). Then
\[
S<2.281390,\quad |S_t|<52.364055,\quad |S_p|<2.455146.
\]
Consequently,
\[
1\le D<1.035647,\quad |D_t|<3.099578,\quad |D_p|<0.038362.
\]
The derivative bounds are endpoint-safe because they are derived for squared component factors, avoiding derivatives of square roots.

## Status and limitations
This is an explicit conservative derivative bound for the normalization denominator D, not yet a derivative bound for normalized probabilities Q or Q3. The latter requires carefully applying quotient-rule estimates and verifying all inherited spectral derivative bounds independently. No Taylor remainder or entropy certification is claimed.
