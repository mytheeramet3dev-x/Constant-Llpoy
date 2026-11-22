# IV-157 — Independent Audit of Small-Coupling Probability Expansions

**Project:** Absolute Symmetry — Paper A  
**Proposition:** AS-ALPHA-A-PROP-0012  
**Status:** ANALYTIC SERIES AUDIT; not Lean-verified

## 1. Scope and notation

Use polar couplings \(x=r\cos\theta\), \(y=r\sin\theta\), \(t=r^2\), and \(p=\cos^2\theta\). The corrected eigenvector components and implicit spectral equation are used. The angle-dependent parameter in the spectral equation is \(m=\cos^2(2\theta)\).

The exact implicit equation is
\[
d-4=\frac{16t(d^2-16mt)}{d(d^2-16t)}.
\]
Expanding about \(t=0\) and solving coefficient-by-coefficient gives
\[
\boxed{d=4+4t-4mt^2+4(3m-1)t^3+O(t^4).}
\]
This expansion is not asserted to be uniform beyond the compact angular parameter range; the coefficients are bounded for \(m\in[0,1]\).

## 2. Eigenvector component expansions

With \(c=\cos\theta\), \(s=\sin\theta\), and \(m=(c^2-s^2)^2\), algebraic substitution into the corrected components gives
\[
u=cr\left[1+(s^2-c^2)r^2+
\big(2(c^2-s^2)-4c^2s^2\big)r^4\right]+O(r^7),
\]
\[
w=2csr^2\left[1-r^2+2m r^4\right]+O(r^8),
\]
\[
z=sr\left[1+(c^2-s^2)r^2+
\big(-2(c^2-s^2)-4c^2s^2\big)r^4\right]+O(r^7).
\]
The component series are checked by substitution into the exact rational component formulas, with denominators nonzero near \(r=0\).

## 3. Probability expansions

Define \(q=(u^2+z^2)/D\), \(q_3=(z^2+w^2)/D\), \(D=1+u^2+w^2+z^2\). Set \(p=c^2\). Symbolic expansion and reduction using \(c^2+s^2=1\) yield:
\[
\boxed{q=r^2+(-8p^2+8p-3)r^4+2(24p^2-24p+5)r^6+O(r^8)}
\]
and
\[
\boxed{q_3=(1-p)r^2+(1-p)(8p-3)r^4
-2(1-p)(12p^2-24p+5)r^6+O(r^8).}
\]
These are analytic probability expansions; the displayed coefficient functions are polynomials in \(p\in[0,1]\), hence bounded on the full angle range.

## 4. Numerical spot-checks

Series coefficients were evaluated against direct eigensolver probabilities at sample angles and small radii. The residual scales are consistent with the omitted higher-order terms; these spot-checks are supporting evidence, not the proof of remainder estimates.

## 5. Uniformity audit: probabilities versus entropy

Because the coefficient functions above are polynomials in \(p\) on a compact interval, the probability coefficient bounds are angle-uniform. The exact rational formulas have denominators bounded away from zero in a sufficiently small fixed \(r\)-neighborhood of zero; this supports an angle-uniform analytic remainder for \(q,q_3\), after a uniform neighborhood is explicitly chosen.

However, entropy involves \(q_3\ln q_3\). At \(p=1\) (the \(y=0\) axis), \(q_3=0\) exactly, and the logarithm is singular as a function of its probability argument. Therefore a naive entropy expansion involving \(\ln(1-p)\) is not uniform over all angles. Any IV-147 claim of an angle-uniform entropy remainder must be revisited with a separate endpoint treatment or a split angular domain. No such uniform entropy claim is certified by this record.

## 6. Status

- Spectral expansion for \(d\): coefficient calculation audited.
- Corrected components: series derived through the displayed orders.
- Probability expansions: symbolic coefficients audited.
- Uniform angular boundedness of probability coefficients: established from polynomial dependence.
- Uniform entropy remainder across all angles: **not established**; endpoint \(q_3=0\) requires special handling.
- No Lean proof and no independent human referee review.

## 7. Next task

Derive and audit the entropy expansion on angular subdomains away from \(p=1\), then analyze the \(y=0\) endpoint separately using the exact probability formulas. Determine which statements from IV-147 can be retained, corrected, or must be superseded.
