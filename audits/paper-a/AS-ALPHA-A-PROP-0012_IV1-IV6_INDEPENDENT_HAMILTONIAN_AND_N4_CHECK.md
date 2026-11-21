# Paper A — PROP-0012 Independent Verification IV-1 through IV-6

Date: 2026-11-21

## Scope
This record consolidates six independent hand-checks of the weak-coupling leading-coefficient calculation. It is not a full PROP-0012 proof, does not reconcile the frozen source, and does not replace a formal verification/build.

## IV-1. Hamiltonian and first-order normalization
Use
\[
H=-h\sum_i\sigma_i^x-J\sum_{i<j}\sigma_i^z\sigma_j^z,\qquad r=J/h.
\]
At J=0 the ground state is \(|+x\rangle^{\otimes N}\). A two-spin flip costs 4h and has interaction matrix element -J, so the first-order pair-flip amplitude is \(a=J/(4h)=r/4\), with probability coefficient \(a^2=r^2/16\).

## IV-2. Odd two-site reduced block
For sites 1,2 the odd block at leading order has entries
\[
M_{odd}=\begin{pmatrix}
\sum_{k=3}^N a_{2k}^2&\sum_{k=3}^N a_{1k}a_{2k}\\
\sum_{k=3}^N a_{1k}a_{2k}&\sum_{k=3}^N a_{1k}^2
\end{pmatrix}.
\]
At uniform coupling all entries equal \((N-2)a^2\); its eigenvalues are \(q=2(N-2)a^2=(N-2)r^2/8\) and zero at leading order.

## IV-3. Edge derivative rebuilt
Perturb edge 13 as \(J_{13}=J(1+u)\), so \(a_{13}=a(1+u)\). The one-site small eigenvalue is \(p=(N-1)a^2\), and \(p'=2a^2=r^2/8\). For the odd block entries \(A,B,C\), at uniform coupling \(A=B=C=(N-2)a^2\), while \(A'=0, B'=2a^2, C'=a^2\). Differentiating the positive eigenvalue gives \(q'=(A'+B')/2+C'=2a^2=r^2/8\).

## IV-4. Leading entropy contrast
For small eigenvalue \(x\), \(H'(x)=\ln((1-x)/x)=-\ln x+O(x)\). Combining the audited branch contributions yields the conditional leading contrast
\[
B-C=\frac{r^2}{8}\ln\frac{q}{p}+\text{higher-order remainder}
=\frac{r^2}{8}\ln\frac{2(N-2)}{N-1}+\text{remainder}.
\]
The ratio exceeds one for N>=4. Converting from the dimensionless perturbation u to the physical edge coupling gives the coefficient \(J/(8h^2)\). The disjoint edge 34 does not enter the leading one-site/odd-block coefficient.

## IV-5. What is and is not closed
Rebuilt and algebraically checked here: pair amplitude normalization; one-site coefficient; odd-block eigenvalue; adjacent-edge derivative; logarithmic ratio; physical coupling conversion.
Not independently closed by this check: full higher-order eigenbranch expansions and differentiated entropy remainder; source reconciliation; Lean formalization/build; global \(B-C>0\).

## IV-6. N=4 specialization
For N=4,
\[
p=3r^2/16,\qquad q=r^2/4,\qquad q/p=4/3.
\]
Thus the leading term specializes to
\[
B-C=\frac{J}{8h^2}\ln(4/3)+O\!\left(\frac{J^2}{h^3}(1+|\ln(J/h)|)\right),
\]
only conditional on the remainder estimates. The N=4 coefficient-counting/eigenvalue-derivative algebra shows no special leading-order defect; it is not an N=4 remainder proof.

## Disposition
**IV-1 through IV-6: PASS for the stated leading-order algebraic reconstruction.** The overall proposition remains **OPEN / ANALYTIC-PARTIAL**. No full source reconciliation, formal theorem, independent remainder closure, or global sign result is claimed.
