# AS-ALPHA-A-PROP-0005 — Edge-response sector decomposition and exact chi identity

- Claim ID: `AS-ALPHA-A-PROP-0005`
- Paper: A
- Claim version: 0.1.0
- Extraction status: CANDIDATE
- Constant Llapoy verification status: NOT_ASSESSED
- Source repository: `mytheeramet3dev-x/Absolute_Sym`
- Source branch: `paper-a-interval-audit-2026-11-14`
- Source commit: `8deb7de4a49cb2060720246b7101820ee7e08c91`
- Source path: `Arxiv/paper_01_section_05_revised.md`
- Source blob SHA: `671c97fa68fa48c929760bf9956d197b358c4904`
- Source line range: 42-93

## Verbatim source excerpt

```markdown
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
```

## Extraction notes

Contains the representation decomposition, response-sector eigenvalues, and exact identity. The source explicitly treats the sign of B-C as a strong numerically supported conjecture, not a theorem. Only the algebraic identity and stated decomposition are registered here as candidate claims.

- Independent extraction review: NOT_RUN.
- Mathematical proof review: NOT_RUN.
- Overall status: NOT_VERIFIED.
