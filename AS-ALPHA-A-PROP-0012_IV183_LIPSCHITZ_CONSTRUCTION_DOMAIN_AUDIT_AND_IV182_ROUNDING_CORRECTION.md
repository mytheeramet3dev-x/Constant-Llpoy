# IV-183 — Lipschitz construction and domain-validity audit (with IV-182 rounding correction)

Status: conditional theorem and arithmetic correction. No upstream assumptions are independently certified here.

## 1. Arithmetic correction to IV-182
The aggregate Euclidean norms were recomputed:
\[
\sqrt{2(19.531020)^2+(1.179864)^2}
=27.6462215056\ldots,
\]
\[
\sqrt{2(2.429372)^2+(0.065765)^2}
=3.4362802074\ldots.
\]
Thus IV-182 ceilings 27.646217 and 3.436279 were slightly rounded downward and are **not valid upper ceilings**. Correct upward ceilings are:
\[
\|\partial_t\mathbf Q\|_2<27.646222,\quad
\|\partial_p\mathbf Q\|_2<3.436281.
\]
Likewise the L1 arithmetic is:
\[
\|\partial_t\mathbf Q\|_1<40.241904,\quad
\|\partial_p\mathbf Q\|_1<4.924509,
\]
so safe upward ceilings are 40.241905 and 4.924510. This record corrects the numerical ceilings; IV-182 remains in repository as historical record, not silently overwritten.

## 2. Conditional pathwise Lipschitz theorem
Let \(\Omega\subset\mathbb R^2\) be convex and let \(\mathbf Q:\Omega\to\mathbb R^3\) be continuously differentiable. Suppose everywhere on \(\Omega\):
\[
\|\partial_t\mathbf Q\|_2\le M_t,\quad
\|\partial_p\mathbf Q\|_2\le M_p.
\]
For any \(x=(t,p),y=(s,r)\in\Omega\), the segment \(\gamma(\lambda)=x+\lambda(y-x)\) remains in \(\Omega\). By FTC along the segment:
\[
\mathbf Q(y)-\mathbf Q(x)=\int_0^1D\mathbf Q(\gamma(\lambda))(y-x)\,d\lambda.
\]
Using the coordinate derivative bounds:
\[
\|\mathbf Q(y)-\mathbf Q(x)\|_2
\le M_t|s-t|+M_p|r-p|.
\]
With the corrected ceilings, one can use \(M_t=27.646222\), \(M_p=3.436281\) (strict bounds inherited from IV-181). A coarser Euclidean-input Lipschitz ceiling is
\[
L=\sqrt{M_t^2+M_p^2}<27.858960,
\]
rounded upward, giving \(\|\mathbf Q(y)-\mathbf Q(x)\|_2\le L\|y-x\|_2\).

## 3. Domain and assumptions audit
This implication requires: (i) convexity of the chosen domain (or a segment/path contained in it); (ii) differentiability/continuous differentiability of \(\mathbf Q\) along the path; (iii) IV-175–IV-181 derivative bounds valid at every path point; and (iv) all implicit-root and sign assumptions used to derive those bounds, including the unresolved \(R_d\le0\), valid throughout the domain. If the domain is not convex, apply the coordinate estimate along an admissible piecewise-smooth path and integrate path length/coordinate variation; a global Euclidean Lipschitz constant then needs path-length control.

## 4. Scope and next proof obligation
The Lipschitz construction is a valid conditional calculus argument once its premises hold. It does not independently prove those premises, nor does it constitute formal verification or proof of the target proposition. The IV-182 rounding defect is explicitly corrected here.
