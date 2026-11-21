# PROP-0012 IV-8 — Direct Environment-Sum Reconstruction of the Even Block

**Scope:** Fixed finite N >= 4, real edge couplings in a local neighborhood, weak coupling r -> 0, and first edge-direction derivatives. This is a fresh algebraic reconstruction from the reduced-block environment sums; it is not source reconciliation or Lean verification.

## 1. Exact block entries

For the even-parity reduced block indexed by the pair configurations (empty pair flip, {1,2}), group the traced-out configurations by the environment flip set E subset {3,...,N}. With coefficients c_F in the x-basis, the entries are

\[
L=\sum_{E\text{ even}}|c_E|^2,\quad
X=\sum_{E\text{ even}}c_E\overline{c_{E\cup\{1,2\}}},\quad
S=\sum_{E\text{ even}}|c_{E\cup\{1,2\}}|^2.
\]

The environment-empty terms are exactly |c_empty|^2, c_empty conjugate(c_12), and |c_12|^2, respectively. Thus, defining the nonempty-environment tails R_L, R_X, R_S, the identities are

\[
L=|c_\emptyset|^2+R_L,\quad
X=c_\emptyset\overline{c_{12}}+R_X,\quad
S=|c_{12}|^2+R_S.
\]

No truncation of the shared amplitude c_12 is made in these identities.

## 2. Orders of the tails

For nonempty even E, |E| >= 2. The pair-flip Taylor-support rule gives c_E=O_N(r^{|E|/2}) and c_{E union {1,2}}=O_N(r^{(|E|+2)/2}), including first edge derivatives.

Termwise:
- R_L=O_N(r^2), and its first edge derivatives O_N(r^2).
- R_X=O_N(r^3), and its first edge derivatives O_N(r^3), because each summand has order at least r^1 times r^2.
- R_S=O_N(r^4), and its first edge derivatives O_N(r^4), because each squared amplitude has order at least r^4.

These are finite sums for fixed N. Constants are not asserted uniform in N.

## 3. Shared-amplitude cancellation

The normalized analytic ground-state gauge has c_empty=1+O_N(r^2), hence c_12=O_N(r), while L=|c_empty|^2+O_N(r^2) and X=c_empty conjugate(c_12)+O_N(r^3).

Then
\[
\frac{|X|^2}{L}=|c_{12}|^2+O_N(r^4).
\]
Indeed, the factor |c_empty|^2/L differs from 1 by O_N(r^2), multiplying |c_12|^2=O_N(r^2) yields O_N(r^4); the cross term between the main X term O_N(r) and R_X=O_N(r^3) is O_N(r^4); and |R_X|^2 is O_N(r^6). The same product/quotient estimates hold after one edge derivative, since the derivative orders above are preserved and c_12, c_12' are O_N(r).

Therefore the Schur complement
\[
D=S-|X|^2/L
\]
and its first edge derivatives are O_N(r^4).

## 4. Small eigenvalue and entropy

For the positive 2x2 block, det M=L D. If lambda_L is the large eigenvalue, it stays bounded away from zero locally; exactly,
\[
\lambda_s=\frac{\det M}{\lambda_L}=\frac{L}{\lambda_L}D.
\]
The analytic bounded factor L/lambda_L and its first edge derivative transfer O_N(r^4) to lambda_s and lambda_s'. The entropy directional derivative is O_N(r^4(1+|ln r|)) on a positive analytic branch with its leading scale verified; an identically-zero/nonnegative branch is treated separately via its interior-minimum derivative, not by evaluating ln(0).

## 5. Independent check result and scope

**IV-8 PASS (conditional analytic order reconstruction):** the environment-tail orders and shared-amplitude cancellation are algebraically consistent and independently reconstructed. This directly addresses the prior provenance gap in the O_N(r^4) integration argument at the level of the displayed environment-sum formulas.

Still required before any promotion of PROP-0012:
1. reconcile exact Hamiltonian, x-basis, and sign conventions with the frozen manuscript source (currently inaccessible);
2. independently verify the pair-flip Taylor-support recursion and its edge-derivative version as a complete proof, not just the stated lemma;
3. verify the positive-branch logarithmic scale against the source and handle the zero branch as specified;
4. integrate every entropy branch into the working proof and update the conservative O_N(r^3) statement with provenance;
5. Lean formalization/build and full manuscript-to-declaration correspondence;
6. establish or refute the global sign B-C>0.

No source-wide pass, formal verification, global sign theorem, or uniform-in-N bound is claimed.
