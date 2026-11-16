# AS-ALPHA-D-PROP-0003 — Feasibility-preserving contraction and connectedness of the P-minus zero set

- Claim ID: `AS-ALPHA-D-PROP-0003`
- Paper: D
- Claim version: 0.1.0
- Extraction status: TRANSCRIBED
- Constant Llapoy verification status: NOT_ASSESSED
- Source repository: `mytheeramet3dev-x/Absolute_Sym`
- Source branch: `paper-d-singularity`
- Source commit: `2678e3f581d707ac57e8a72d3f961fadbba29ade`
- Source path: `papers/paper-d/02-theorems/proposition_pminus_zero_set_path_connected.md`
- Source blob SHA: `92eb4b9ef1063003b6928e9e25048baf30447398`
- Source line range: 5-18

## Verbatim source excerpt

```markdown
## Statement

Use the invertible coordinates `(x,u,y,v,m,n)` and the feasible-domain inequalities

\[
x,y>0,\quad |u|<x,\quad |v|<y,\quad n>\max(x,y),
\]
\[
-A+|u+v|<m<A-|u-v|,\qquad A=x+y-n>0.
\]

On the zero set, `m=m_*`. For `0<s<=1`, define `u_s=su`, `v_s=sv`, and let `m_s` be the unique admissible zero-set root for the scaled variables, with `x,y,n` fixed. Then the path remains in the feasible domain for every `s` and extends continuously to `s=0` with `(u_0,v_0,m_0)=(0,0,0)`.

Consequently, the full zero set `P_-=0` in the strictly positive coupling cone is path-connected.
```

## Extraction notes

The source labels the proof exact in the strictly positive N=4 coupling cone.

The current `paper-d-singularity` branch explicitly states that an integrated publication-facing manuscript has not yet been consolidated. These are theorem/proposition source records, not evidence that all are included in a final manuscript.

- Independent extraction review: NOT_RUN.
- Mathematical proof review: NOT_RUN.
- Formal proof correspondence: NOT_RUN.
- Overall status: NOT_VERIFIED.
