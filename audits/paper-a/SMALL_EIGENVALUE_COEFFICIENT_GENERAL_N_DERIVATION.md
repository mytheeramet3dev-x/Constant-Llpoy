# General-\(N\) Fourth-Order Small-Eigenvalue Derivation

**Scope:** Uniform all-to-all TFIM; fixed finite \(N\ge9\) for the closed symbolic derivation, plus exact-rational finite cases \(N=5,6,7,8\). The exceptional \(N=4\) case is stated separately.  
**Parameter:** \(\varepsilon=h/J\to0^+\).  
**Object:** The small eigenvalue of the symmetric two-site parity block.  
**Status:** Perturbative coefficient derivation at the uniform point. This is not an edge-derivative theorem and does not close the entropy remainder or \(B-C\).

## 1. Computational-basis recurrence

Write the dimensionless Hamiltonian as

\[
H/J=K_0+\varepsilon V,\qquad
K_0=-\sum_{i<j}\sigma_i^z\sigma_j^z,\qquad
V=-\sum_i\sigma_i^x.
\]

For a computational basis state of Hamming weight \(k\), the unperturbed energy is

\[
E_k=-\frac{(N-2k)^2-N}{2},
\qquad E_0=-\binom N2,
\]

and its excitation gap is

\[
\Delta_k=E_k-E_0=2k(N-k).
\]

The uniform ground state is permutation symmetric and even under global bit flip. Let \(u_k=u_{N-k}\) be the common amplitude of each computational basis vector of weight \(k\), in intermediate normalization \(u_0=u_N=1\). The eigenvalue equation gives

\[
\delta E=-N\varepsilon u_1
\]

and, for \(1\le k\le N-1\),

\[
(\Delta_k-\delta E)u_k
=\varepsilon\bigl[(N-k)u_{k+1}+ku_{k-1}\bigr].
\]

For \(N\ge9\), the Hamming-weight sectors \(k=0,1,2,3,4\) and their complements are distinct. Contributions from weights \(k\ge5\) enter beyond order \(\varepsilon^4\) in the reduced two-site block entries used below. Solving the recurrence to the required orders gives

\[
\begin{aligned}
u_1&=\frac{\varepsilon}{2(N-1)}
+\frac{\varepsilon^3}{8(N-2)(N-1)^3}
+O_N(\varepsilon^5),\\[2mm]
u_2&=\frac{\varepsilon^2}{4(N-2)(N-1)}
+\frac{\varepsilon^4}{8(N-3)(N-2)(N-1)^3}
+O_N(\varepsilon^6),\\[2mm]
u_3&=\frac{\varepsilon^3}{8(N-3)(N-2)(N-1)}
+O_N(\varepsilon^5),\\[2mm]
u_4&=\frac{\varepsilon^4}{16(N-4)(N-3)(N-2)(N-1)}
+O_N(\varepsilon^6).
\end{aligned}
\]

These are amplitudes before normalization. The squared norm through fourth order is

\[
\mathcal N
=2\left[1+Nu_1^2+\binom N2u_2^2\right]
+O_N(\varepsilon^6),
\]

and the normalized amplitudes are \(\widehat u_k=u_k/\sqrt{\mathcal N}\).

## 2. Two-site block

Trace out sites \(3,\ldots,N\). In the symmetric parity block with basis

\[
|e\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2},
\qquad
|o\rangle=\frac{|01\rangle+|10\rangle}{\sqrt2},
\]

write

\[
M_{12}(\varepsilon)=
\begin{pmatrix}
A(\varepsilon)&B(\varepsilon)\\
B(\varepsilon)&C(\varepsilon)
\end{pmatrix}.
\]

The partial trace is a finite combinatorial sum over the environment Hamming weight. Substituting the normalized amplitudes above and collecting all terms through order four gives

\[
\begin{aligned}
A(\varepsilon)
&=\frac12+
\frac{\varepsilon^2}{4(N-2)(N-1)^2}
+\frac{(N+5)\varepsilon^4}
{16(N-3)(N-2)(N-1)^4}
+O_N(\varepsilon^6),\\[2mm]
B(\varepsilon)
&=\frac{\varepsilon}{2(N-1)}
+\frac{\varepsilon^3}{4(N-2)(N-1)^3}
+O_N(\varepsilon^5),\\[2mm]
C(\varepsilon)
&=\frac{\varepsilon^2}{2(N-1)^2}
+\frac{3\varepsilon^4}{8(N-2)(N-1)^4}
+O_N(\varepsilon^6).
\end{aligned}
\]

The antisymmetric site-swap vector \((|01\rangle-|10\rangle)/\sqrt2\) is an exact zero eigenvector because the full ground state lies in the fully permutation-symmetric spin sector.

## 3. Schur-complement cancellation and coefficient

Since \(A(0)=1/2\), the small eigenvalue is controlled by the Schur complement

\[
Q=C-\frac{B^2}{A}.
\]

At order \(\varepsilon^2\),

\[
[\varepsilon^2]Q
=\frac{1}{2(N-1)^2}
-\frac{(1/[2(N-1)])^2}{1/2}
=0.
\]

At order \(\varepsilon^4\), substitution of the displayed coefficients gives

\[
\begin{aligned}
[\varepsilon^4]Q
&=\frac{3}{8(N-2)(N-1)^4}
-\frac{1}{2(N-2)(N-1)^4}
+\frac{1}{4(N-2)(N-1)^4}\\
&=\frac{1}{8(N-2)(N-1)^4}.
\end{aligned}
\]

Because \(Q=O(\varepsilon^4)\) and \(B=O(\varepsilon)\), the difference between the small eigenvalue and \(Q\) is \(O(\varepsilon^6)\). Therefore, for fixed \(N\ge9\),

\[
\boxed{
\lambda_{\rm small}(\varepsilon)
=\frac{\varepsilon^4}{8(N-2)(N-1)^4}
+O_N(\varepsilon^6).
}
\]

This derives the coefficient from the Hamiltonian recurrence and the reduced pair state; it does not use the unrelated Lemma 5.1 citation.

## 4. Finite exceptional sizes

The low-weight/complement separation used above is not valid unchanged for \(N=4,5,6,7,8\). The full even-parity complement-orbit recurrence was therefore evaluated with exact rational arithmetic for these finite sizes. It gives:

| \(N\) | Exact coefficient \([\varepsilon^4]\lambda_{\rm small}\) |
|---:|---:|
| 4 | \(1/648\) |
| 5 | \(1/6144\) |
| 6 | \(1/20000\) |
| 7 | \(1/51840\) |
| 8 | \(1/115248\) |

For \(N=5,6,7,8\), these values agree with \(1/[8(N-2)(N-1)^4]\). For \(N=4\), the value is \(1/648\), twice the candidate \(1/1296\). The \(N=4\) coefficient was also checked by direct high-precision diagonalization of the full Hamiltonian.

Thus the coefficient formula is consistent for all \(N\ge5\) across the analytically derived range \(N\ge9\) and the exact finite cases \(N=5,\ldots,8\), whereas \(N=4\) is exceptional. A formal proof package should retain the finite exact calculations as explicit certificates or independently checkable rational recurrences.

## 5. What this result does not prove

- It is a uniform-coupling calculation only; it does not give \(\partial_{J_{13}}\lambda\) or \(\partial_{J_{34}}\lambda\).
- It does not prove the lower/relative eigenvalue bounds needed to control \(\ln\lambda\) under edge perturbations.
- It does not establish the differentiated entropy remainder.
- It does not, by itself, establish the full \(\mathcal G_N(x)\) expansion or its derivative.
- It does not prove \(B-C>0\).

**Conclusion:** The fourth-order small-eigenvalue coefficient is now derived for fixed \(N\ge9\), with exact finite-\(N\) checks for \(N=5,\ldots,8\), and a corrected exceptional value for \(N=4\). The remaining decisive obstruction is the general-edge derivative of the small-eigenvalue branches and its entropy contribution.
