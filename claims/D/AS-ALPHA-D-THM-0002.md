# AS-ALPHA-D-THM-0002 — Candidate local coupling-space entropy singularity at the N=4 symmetric point

- Claim ID: `AS-ALPHA-D-THM-0002`
- Paper: D
- Claim version: 0.1.0
- Extraction status: CANDIDATE
- Constant Llapoy verification status: NOT_ASSESSED
- Source repository: `mytheeramet3dev-x/Absolute_Sym`
- Source branch: `paper-d-singularity`
- Source commit: `2678e3f581d707ac57e8a72d3f961fadbba29ade`
- Source path: `papers/paper-d/02-theorems/theorem_2_coupling_space_singularity.md`
- Source blob SHA: `d68fd99ac61a6581d2b841387e4e87c913cb7a4d`
- Source line range: 5-62

## Verbatim source excerpt

```markdown
## 1. N=4 coefficient geometry

Use the six positive couplings in the order
$$
\mathbf J=(J_{12},J_{13},J_{14},J_{23},J_{24},J_{34}).
$$
Stage V-B gives the leading coefficient of the minus pair-block small eigenvalue as
$$
\alpha_-(\mathbf J)=8P_-(\mathbf J)^2,
$$
where
$$
P_-=
\frac{
(q_{14}-q_{13})
\left(d_{12}^{2}s_{34}+d_{34}^{2}s_{12}
-A(s_{12}+s_{34})\right)
+4d_{12}d_{34}q_{13}q_{14}
}{
64r_1r_2r_3r_4q_{13}q_{14}
}.
$$
Here the cut variables $r_i,q_{13},q_{14},s_{12},s_{34},d_{12},d_{34},A$ are defined in Stage V-B.

The denominator is strictly positive throughout the positive-coupling cone. Thus the zero set of $P_-$ is the zero set of its numerator.

## 2. Exact local calculation at the uniform point

Set $J_{ij}=J>0$ for all six edges. Direct substitution gives
$$
P_-(J,J,J,J,J,J)=0.
$$
Differentiating the exact rational expression gives
$$
\nabla_{\mathbf J}P_-\big|_{\mathbf J=J\mathbf 1}
=
\frac{1}{192J^3}
(0,-1,1,1,-1,0).
$$
In particular, this gradient is nonzero. By the implicit function theorem, the set $P_-=0$ is a smooth codimension-one hypersurface in a neighborhood of the uniform point.

Consider the transverse path
$$
\mathbf J(t)=(J,J+t,J-t,J,J,J),
$$
which remains in the positive-coupling cone for $|t|<J$. Along this path,
$$
P_-(\mathbf J(t))
=-\frac{t}{96J^3}+O(t^2).
$$
Therefore
$$
\alpha_-(\mathbf J(t))
=8P_-(\mathbf J(t))^2
=\frac{t^2}{1152J^6}+O(t^3).
$$

These are exact leading Taylor coefficients obtained from the rational formula, not numerical fits.
```

## Extraction notes

The source explicitly calls this a candidate theorem and says final manuscript inclusion follows an independent audit. No acceptance as a theorem is implied.

The current `paper-d-singularity` branch explicitly states that an integrated publication-facing manuscript has not yet been consolidated. These are theorem/proposition source records, not evidence that all are included in a final manuscript.

- Independent extraction review: NOT_RUN.
- Mathematical proof review: NOT_RUN.
- Formal proof correspondence: NOT_RUN.
- Overall status: NOT_VERIFIED.
