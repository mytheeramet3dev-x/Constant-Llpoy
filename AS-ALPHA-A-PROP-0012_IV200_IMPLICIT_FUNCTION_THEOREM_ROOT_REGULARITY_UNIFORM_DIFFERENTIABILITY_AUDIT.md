# IV-200 — Implicit Function Theorem, Root Regularity & Uniform Differentiability Audit

**Target:** AS-ALPHA-A-PROP-0012  
**Dependency:** IV-198 and IV-199  
**Scope:** Establish regularity of the uniquely defined root on the closed parameter box, with precise boundary interpretation.

## 1. Root equation and regularity of the defining function

\[
\Phi(d,t,p)=d-4-R(d,t,p),\quad
R=\frac{16t(d^2-16mt)}{d(d^2-16t)},\quad m=(2p-1)^2.
\]
On the box \(d\in[4,256/63]\), \(t\in[0,1/64]\), \(p\in[0,1]\), denominators stay positive:
\[
d\ge4,\qquad d^2-16t\ge63/4.
\]
Therefore \(\Phi\) is smooth in an open neighborhood of every point of the root graph, including parameter-boundary points (using the rational formula's local extension).

IV-198 gives \(\Phi_d=1-R_d\ge1\). Thus \(\Phi_d\) is nonzero at every root.

## 2. Implicit Function Theorem

At every root \(\Phi(d,t,p)=0\), the IFT provides a local smooth root function in a neighborhood of the parameter point. IV-199 proves exactly one root in the stated \(d\)-interval for every parameter pair. These local branches therefore agree wherever they overlap, by uniqueness.

Consequently the unique root defines a globally continuous and locally smooth function \(d(t,p)\) on the parameter box; derivatives extend locally to the box boundary through the smooth ambient formula. This is a local-neighborhood regularity argument, not a claim that the parameter box itself is open.

## 3. First derivative formulas

From \(\Phi=d-4-R=0\):
\[
d_t=\frac{R_t}{1-R_d},\qquad d_p=\frac{R_p}{1-R_d}.
\]
At fixed \(d,p\):
\[
R_t=\frac{16(d^4-32d^2mt+256mt^2)}{d(d^2-16t)^2}.
\]
At fixed \(d,t\):
\[
R_p=-\frac{1024t^2(2p-1)}{d(d^2-16t)}.
\]
Because \(1-R_d\ge1\), the derivative formulas are well-defined. These identities agree with the implicit differentiation rule used downstream, subject to the reconstructed source equation.

## 4. Uniformity over the compact parameter box

The root lies in the compact interval \(I=[4,256/63]\). The displayed derivative formulas are continuous on the compact root/parameter box and their denominators have positive lower bounds. Hence their absolute values admit finite uniform maxima. IV-175/176 inherited numerical ceilings still require source-level reconciliation and exact independent bound computation before those specific decimals are certified by this record.

## 5. Status

- Smoothness of the rational defining function on the root domain: **PASS**.
- Nonvanishing \(\Phi_d\) at roots: **PASS**, with \(\Phi_d\ge1\).
- Local IFT root regularity: **PASS**.
- Unique local branches glue to the unique interval root: **PASS**.
- Global root map on the closed box, continuous and locally smooth with boundary extension: **PASS**, conditional on the reconstructed equation and box.
- First derivative formulas: **PASS (symbolic identities)**.
- Uniform finite derivative bounds: **existence proved by compactness**; particular inherited decimal ceilings not certified here.
- Full proposition/source fidelity: **still requires comparison with the original proposition source**.

## 6. Next action

Perform an exact, independent recomputation of the uniform bounds for \(d_t\) and \(d_p\) over the full root/parameter box, then reconcile them against IV-175/176 ceilings before refreshing downstream component derivatives. Do not assume a bound is valid merely because it is present in an earlier audit file.
