# IV-161 — Explicit Spectral Gap and Denominator Bounds on a Small-Coupling Disk

**Project:** Absolute Symmetry — Paper A  
**Proposition:** AS-ALPHA-A-PROP-0012  
**Status:** ANALYTIC BOUNDS; conditional on matrix model; not Lean-verified

## 1. Domain

Take \(\rho=\sqrt{x^2+y^2}\le 1/8\), \(t=\rho^2\le1/64\), and \(m\in[0,1]\). The ground eigenvalue \(\lambda\le-3\) by the Rayleigh quotient at the first coordinate vector. Set \(d=1-\lambda\), hence \(d\ge4\).

## 2. Lower-block spectral separation

The lower block is \(N=I+K\), with \(\|K\|=4\rho\). Thus
\[
\lambda_{\min}(N)\ge1-4\rho\ge\frac12.
\]
The ground state lies below the lower-block spectrum, and the resolvent gap satisfies
\[
\lambda_{\min}(N-\lambda I)\ge4-4\rho\ge\frac72.
\]
By eigenvalue interlacing for the principal submatrix, the second eigenvalue of the full matrix is at least \(\lambda_{\min}(N)\). Hence the full ground-state spectral gap is at least \(7/2\) on this disk.

## 3. Explicit upper bound on d

Using the implicit equation
\[
d-4=\frac{16t(d^2-16mt)}{d(d^2-16t)}
\]
and \(m\in[0,1]\), \(d\ge4\), obtain
\[
0\le d-4\le\frac{16td}{d^2-16t}
\le\frac{64t}{16-16t}=\frac{4t}{1-t}.
\]
At \(t\le1/64\),
\[
\boxed{4\le d\le4+\frac4{63}=\frac{256}{63}.}
\]

## 4. Explicit denominator bounds

\[
F=d^2-16t\ge16-\frac14=\boxed{\frac{63}{4}}.
\]
For normalized eigenvector \(\psi=(1,v)\), the resolvent bound yields
\[
\|v\|\le\frac{4\rho}{4-4\rho}=\frac{\rho}{1-\rho}\le\frac17.
\]
Consequently
\[
\boxed{1\le D=1+\|v\|^2\le\frac{50}{49}.}
\]
These bounds ensure the component formulas' denominators remain safely away from zero.

## 5. Endpoint-normalized Q3 lower bound

Recall
\[
\[
q_3=t\varepsilon Q_3,\quad \varepsilon=1-p,
\]
and
\[
Q_3=\frac{16G^2/(d^2F^2)+1024tp/F^2}{D},
\quad G=d^2+16x^2-16y^2.
\]
Since \(G\ge d^2-16t\ge63/4\), \(d\le256/63\), \(F\le d^2\le(256/63)^2\), and \(D\le50/49\), it follows that
\[
Q_3\ge\frac{16(63/4)^2}{(256/63)^6(50/49)}
\approx\boxed{0.8639939063}.
\]
This lower bound is intentionally conservative; it is a derived positive bound, not an optimized one.

## 6. What these bounds establish

- Ground-state spectral gap \(\ge7/2\) on \(\rho\le1/8\).
- \(d\) lies in explicit rational interval \([4,256/63]\).
- \(F\ge63/4\), \(D\in[1,50/49]\).
- Endpoint-normalized factor \(Q_3\) has a positive explicit lower bound (conservative).

They do **not** by themselves finish the explicit analytic probability remainder constants or the entropy remainder constant. IV-158/160's uniform remainder certification remains open.

## 7. Next step

IV-162: obtain explicit upper bounds for normalized factors and derivative bounds on the rational component functions, then construct concrete Taylor remainder constants on \(t\in[0,1/64]\), or shrink the disk if the estimates are not adequate.
