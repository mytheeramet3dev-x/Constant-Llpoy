# Section 5: Physical Discussion and Connection to Paper 2

## 5.1 Mathematical meaning of the branch condition

For the scalar self-consistency equation

\[
F(J;g,h)=gI_{12}(J,h)-J,
\]

the derivative at a fixed point is

\[
F_J(J_*)=g\left.\frac{\partial I_{12}}{\partial J}\right|_{J_*}-1.
\]

Therefore, the branch condition (F_J(J_*)<0) is equivalent to

\[
\left.\frac{\partial I_{12}}{\partial J}\right|_{J_*}<\frac1g.
\]

This is an exact upper bound on the response to a uniform change of all edge couplings. It does **not** determine the sign of that response. In particular, (F_J<0) does not imply
\(\partial I_{12}/\partial J<0\); negativity would require the stronger condition (F_J<-1).

Let
\[
T(J)=gI_{12}(J,h)
\]
be the scalar Picard map. Since (T'(J_*)=1+F_J(J_*)), the exact local Picard-attractivity condition is

\[
|T'(J_*)|<1
\quad\Longleftrightarrow\quad
-2<F_J(J_*)<0.
\]

Thus (F_J<0) identifies the descending side of the fixed-point curve and is sufficient for the usual saddle-node branch classification, but by itself is not the complete discrete-iteration stability criterion.

For the present model, positivity of the uniform response has been observed numerically on the investigated physical branches for (N=4,6,8,10,20). This remains a numerical observation, not an analytic theorem. The (N=50) data near (x_c) are excluded from this statement because the computed spectral gap is below the reliability threshold.

## 5.2 Representation-theoretic decomposition of edge perturbations

At the permutation-symmetric point (J_{ij}=J_*), an infinitesimal edge perturbation belongs to
\[
\mathcal V_{\mathrm{edge}}\cong\mathbb R^{\binom N2}.
\]
As an (S_N)-representation, this space decomposes as

\[
\mathcal V_{\mathrm{edge}}=\mathcal V_0\oplus\mathcal V_1\oplus\mathcal V_2,
\]

with
\[
\dim\mathcal V_0=1,\qquad
\dim\mathcal V_1=N-1,\qquad
\dim\mathcal V_2=\frac{N(N-3)}2.
\]

Here (mathcal V_0) is the uniform edge direction, (mathcal V_1) is the degree-heterogeneous (standard-representation) sector, and (mathcal V_2) is the residual degree-preserving sector. The last sector is a natural place to look for distributed, geometry-like perturbations, although representation labels alone do not establish the emergence of a lattice or finite-dimensional geometry.

Define the three derivatives

\[
A=\frac{\partial I_{12}}{\partial J_{12}},\qquad
B=\frac{\partial I_{12}}{\partial J_{13}},\qquad
C=\frac{\partial I_{12}}{\partial J_{34}},
\]

where (J_{13}) shares one endpoint with the observed edge and (J_{34}) is disjoint from it. (S_N) symmetry implies that the response matrix is determined by these three numbers. Its sector eigenvalues are

\[
\chi_0=A+2(N-2)B+\frac{(N-2)(N-3)}2C,
\]
\[
\chi_1=A+(N-4)B-(N-3)C,
\]
\[
\chi_2=A-2B+C.
\]

The uniform eigenvalue, obtained by varying every edge simultaneously, satisfies
\[
\chi_0=\frac{\partial I_{12}}{\partial J_*},
\]
and direct subtraction gives the exact identity

\[
\boxed{\chi_1-\chi_2=(N-2)(B-C)}.
\]

This identity is exact at the symmetric point and does not require a numerical approximation.

## 5.3 Status of the (B-C) statement

The sign of (B-C) determines the ordering of the two nontrivial response sectors:

\[
B-C>0\iff\chi_1>\chi_2.
\]

For the feedback map (mathbf J\mapsto g\mathbf I(\mathbf J)), the corresponding linearized eigenvalues are (g\chi_k). Consequently, the statement that one sector is more strongly amplified than another requires comparison of (g\chi_1) and (g\chi_2), together with their signs and the chosen stability convention. The inequality (B-C>0) alone is a response-ordering statement; it is not by itself a proof that a hub mode is dynamically unstable or that a geometric mode is dynamically suppressed.

The current evidence is:

- reduced-solver validation agrees with dense exact diagonalization at small (N);
- near-(x_c) scans give (B-C>0) for (N=4,6,8,10);
- finite-size data are positive for (N=4,6,8,10,20);
- the (h)-scan at (N=8) is positive over the tested range (h=0.5,1.0,\ldots,3.5);
- (N=50) near (x_c) is excluded because the spectral gap is below the reliability threshold.

Accordingly, (B-C>0) should be labelled a **strong numerically supported conjecture**, not an exact theorem. The algebraic proof remains open. The principal barrier is that the perturbations associated with the different edge sectors couple to different excited-state/resolvent channels, while the von Neumann entropy derivative contains noncommuting Fréchet terms. Permutation symmetry fixes the sector decomposition but does not impose an ordering between the resulting reduced matrix elements.

## 5.4 Connection to Paper 2

The results of this paper provide constraints and definitions for the symmetry-breaking analysis in Paper 2.

1. **Branch restriction.** The locally relevant physical branch is the branch emerging on the (x>x_c) side of the nondegenerate tangent point. Statements extending this branch to all (gamma\ge1) require a separate global-continuation argument and should not be inferred from the local saddle-node theorem alone.

2. **Uniform-response bound.** On any fixed point satisfying (F_J<0),
\[
\chi_0=\left.\frac{\partial I_{12}}{\partial J_*}\right|_{J_*}<\frac1g.
\]
Under (g=\gamma\alpha_Nh), this bound scales as (1/h), while the dimensionless response (h\chi_0) depends only on (x).

3. **Scale covariance of perturbations.** Since the ground state depends on (J,h) through (x=J/h), response eigenvalues have the dimensional scaling
\[
\chi_k(J,h)=h^{-1}\,\widetilde\chi_k(x).
\]
Thus the ordering of the sectors is independent of the overall energy scale (h), but the dimensional eigenvalues themselves are not strictly invariant under changing (h). The same qualification applies to the feedback eigenvalues (g\chi_k), which depend on the dimensionless ratio (g/h).

These results establish the precise interface between Paper 1 and Paper 2: Paper 1 supplies the symmetric branch, its local bifurcation structure, and the exact sector identity; Paper 2 must determine whether the unresolved ordering (\chi_1\gtreqless\chi_2) can be proved or whether additional model structure is required.

