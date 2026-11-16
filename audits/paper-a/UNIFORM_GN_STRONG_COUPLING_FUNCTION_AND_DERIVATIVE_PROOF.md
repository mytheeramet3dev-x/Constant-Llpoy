# Uniform Strong-Coupling Expansion of \(\mathcal G_N\) and Its Derivative

**Target:** Paper A, Section 4.4.2, uniform all-to-all TFIM.  
**Scope:** Fixed finite \(N\ge4\), \(J>0\), \(\varepsilon=h/J=1/x\to0^+\).  
**Status:** Analytic perturbative derivation of the uniform function and its \(x\)-derivative. No uniform-in-\(N\) claim. No claim about independent edge derivatives \(B,C\).

## 1. Required spectral and regularity setup

At \(\varepsilon=0\), the full Ising Hamiltonian has a two-dimensional ground space spanned by the two ferromagnetic product states. Restrict to the global bit-flip even sector. The cat state is a simple eigenvector in that sector, separated from the first even-sector excitations by \(2J(N-1)\). For each fixed finite \(N\), analytic perturbation theory therefore gives an analytic spectral projector for sufficiently small \(\varepsilon\).

For \(\varepsilon>0\), the even-sector branch is the unique full ground state. Its one- and two-site reduced matrices have analytic entries in \(\varepsilon\). The permutation and global-parity symmetries split the two-site reduced matrix into invariant blocks.

The fourth-order small eigenvalue coefficient is established in the companion derivation:
- \(c_4=1/648\) for \(N=4\);
- \(c_N=1/[8(N-2)(N-1)^4]\) for every \(N\ge5\), using the symbolic recurrence for \(N\ge9\) and exact-rational finite calculations for \(N=5,6,7,8\).

In particular, for every fixed \(N\ge4\),

\[
\lambda_s(\varepsilon)
=c_N\varepsilon^4+O_N(\varepsilon^6),
\qquad c_N>0.
\]

The small eigenvalue is an analytic branch: in its \(2\times2\) parity block, the other eigenvalue is \(1/2\) at \(\varepsilon=0\), so the two eigenvalues remain separated near zero. Thus

\[
\lambda_s'(\varepsilon)
=4c_N\varepsilon^3+O_N(\varepsilon^5).
\]

For sufficiently small positive \(\varepsilon\), positivity of \(c_N\) also gives the two-sided estimate

\[
\frac{c_N}{2}\varepsilon^4
\le\lambda_s(\varepsilon)
\le\frac{3c_N}{2}\varepsilon^4.
\]

This lower bound is important: it controls \(|\ln\lambda_s|\) by \(O_N(1+|\ln\varepsilon|)\) on the uniform path.

## 2. One-site entropy

The first-order even-sector state has one-spin-flip amplitude

\[
b(\varepsilon)=\frac{\varepsilon}{2(N-1)}
+O_N(\varepsilon^3).
\]

After tracing out the other sites, the one-site reduced state has eigenvalues

\[
p_\pm(\varepsilon)
=\frac12\pm b(\varepsilon).
\]

Both eigenvalues remain bounded away from zero near \(\varepsilon=0\). With binary entropy \(h_2(p)=-p\ln p-(1-p)\ln(1-p)\),

\[
S(\rho_i)
=h_2\!\left(\frac12+b\right)
=\ln2-2b^2+O_N(b^4).
\]

Therefore

\[
S(\rho_i)
=\ln2-\frac{\varepsilon^2}{2(N-1)^2}
+O_N(\varepsilon^4),
\]

and, because the eigenvalues and \(b\) are analytic,

\[
\frac{d}{d\varepsilon}S(\rho_i)
=-\frac{\varepsilon}{(N-1)^2}
+O_N(\varepsilon^3).
\]

## 3. Two-site entropy and its derivative

Permutation symmetry places the two-site state in the triplet (symmetric) subspace; the antisymmetric singlet eigenvalue is exactly zero. Global parity splits the triplet into one eigenvalue \(\nu_0\) and a \(2\times2\) block with eigenvalues \(\nu_+\) and \(\lambda_s\). At \(\varepsilon=0\),

\[
\nu_0(0)=\nu_+(0)=\frac12,
\qquad \lambda_s(0)=0.
\]

The large eigenvalue branches are analytic and even in \(\varepsilon\), since changing \(\varepsilon\) to \(-\varepsilon\) is implemented by the global \(z\)-rotation \(\prod_i\sigma_i^z\), which does not change reduced-state spectra. Hence

\[
\nu_0,\nu_+=\frac12+O_N(\varepsilon^2),
\qquad
\nu_0',\nu_+'=O_N(\varepsilon).
\]

Trace one gives

\[
\nu_0+\nu_++\lambda_s=1,
\qquad
\nu_0'+\nu_+'=-\lambda_s'=O_N(\varepsilon^3).
\]

Let \(f(t)=-t\ln t\). Since \(f'\) and \(f''\) are bounded near \(1/2\), the two large eigenvalues contribute

\[
\begin{aligned}
\frac{d}{d\varepsilon}
\{f(\nu_0)+f(\nu_+)\}
&=f'(1/2)(\nu_0'+\nu_+')
+O_N(\varepsilon^2)\,O_N(\varepsilon)\\
&=O_N(\varepsilon^3).
\end{aligned}
\]

For the small eigenvalue,

\[
\frac{d}{d\varepsilon}f(\lambda_s)
=-(1+\ln\lambda_s)\lambda_s'
=O_N\!\left(\varepsilon^3(1+|\ln\varepsilon|)\right),
\]

where both the derivative expansion and the two-sided scale bound for \(\lambda_s\) are used. Consequently,

\[
S(\rho_{12})
=\ln2+O_N\!\left(\varepsilon^4(1+|\ln\varepsilon|)\right),
\]

and, separately,

\[
\frac{d}{d\varepsilon}S(\rho_{12})
=O_N\!\left(\varepsilon^3(1+|\ln\varepsilon|)\right).
\]

The derivative statement is not obtained by differentiating a bare big-\(O\) term; it follows from the analytic eigenvalue branches and their explicit orders.

## 4. Mutual information and the uniform derivative

At the permutation-symmetric point,

\[
\mathcal G_N(1/\varepsilon)
=I_{12}=2S(\rho_i)-S(\rho_{12}).
\]

Combining the one- and two-site estimates gives

\[
I_{12}(\varepsilon)
=\ln2-\frac{\varepsilon^2}{(N-1)^2}
+O_N\!\left(\varepsilon^4(1+|\ln\varepsilon|)\right),
\]

and, independently,

\[
\frac{dI_{12}}{d\varepsilon}
=-\frac{2\varepsilon}{(N-1)^2}
+O_N\!\left(\varepsilon^3(1+|\ln\varepsilon|)\right).
\]

Since \(x=1/\varepsilon\),

\[
\frac{d}{dx}=-\varepsilon^2\frac{d}{d\varepsilon}.
\]

Therefore, for every fixed finite \(N\ge4\),

\[
\boxed{
\mathcal G_N(x)
=\ln2-\frac{1}{(N-1)^2x^2}
+O_N\!\left(\frac{\ln x}{x^4}\right)
}
\]

and, as a separately justified derivative expansion,

\[
\boxed{
\mathcal G_N'(x)
=\frac{2}{(N-1)^2x^3}
+O_N\!\left(\frac{\ln x}{x^5}\right).
}
\]

In particular,

\[
\lim_{x\to\infty}\mathcal G_N(x)=\ln2,
\qquad
\lim_{x\to\infty}\mathcal G_N'(x)=0.
\]

This closes the mathematical gap in which the derivative asymptotic had previously been inferred from an undifferentiated big-\(O\) estimate.

## 5. Exact scope boundary: this does not prove \(B-C\)

The derivative above is the derivative along the one-dimensional uniform path \(J_{ij}=J\), equivalently \(d/dx\). It is not the ambient edge derivative

\[
B-C=\partial_{J_{13}}I_{12}-\partial_{J_{34}}I_{12}.
\]

The latter varies the couplings independently and breaks permutation symmetry during differentiation. Its proof requires a joint analytic expansion in \(\varepsilon\) and independent edge perturbations, including lower/relative eigenvalue bounds and mixed derivative control for every small eigenvalue branch. None of those edge-direction bounds follows from the uniform derivative calculation.

Thus:
- Uniform \(\mathcal G_N\) function expansion: derived.
- Uniform \(\mathcal G_N'\) expansion and limit: derived separately.
- Full \(B-C\) differentiated entropy remainder: still open.
- Global branch continuation: separate obligation.
- Lean formalization and manuscript correspondence: not yet performed.

## 6. Manuscript-source note

The frozen Section 4.4.2 cites Lemma 5.1, but that source file concerns \(B-C\), not the uniform \(\mathcal G_N\) expansion. The derivation in this document supplies an independent mathematical route inside Constant Llapoy. The upstream manuscript and its citation have not been modified.
