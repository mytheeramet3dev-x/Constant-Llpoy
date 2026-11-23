# IV-193 — Structural Jacobian, Normalization, and Dependency Consistency Audit

**Project:** Absolute Symmetry — Paper A  
**Proposition:** AS-ALPHA-A-PROP-0012  
**Status:** Structural review of retrieved IV-180, IV-186, IV-187, IV-190, IV-191, and IV-192 records. Conditional bounds only; inherited root/domain assumptions are not certified.

## 1. Scope and source records reviewed

Reviewed source records:
- IV-180 — Recomputed squared-component derivative and normalization bounds
- IV-186 — Joint-constraint analysis of A and G
- IV-187 — Dependency-aware radial derivative bound for P_u + P_z
- IV-190 — Source reconstruction, normalization correction, and quotient recomputation
- IV-191 — Recomputed normalized vector derivative aggregate
- IV-192 — Independent arithmetic and dependency audit of IV-186–IV-191

This audit checks definitions, dependency structure, derivative identities, normalization, vector/Jacobian assembly, norm logic, and consistency of inherited numerical ceilings. It does not certify implicit-root existence, uniqueness, the upstream sign condition R_d <= 0, or all inherited domain bounds.

## 2. Component and normalization structure

The retrieved source defines:
[
A=d^2+16t(1-2p),quad G=d^2+16t(2p-1),
]
[
P_u=16pA^2H,quad P_z=16(1-p)G^2H,quad
P_w=1024tp(1-p)F^{-2},
]
and the normalization:
[
S=P_u+P_z+P_w,qquad D=1+tS.
]
Normalized components are (Q_i=P_i/D); the separately tracked third expression is (Q_3=(P_z+P_w)/D).

**Normalization finding:** IV-190's correction (D=1+tS) is structurally consistent with the retrieved definitions. IV-189's earlier (D=1+S) is invalid for this normalization and is superseded by IV-190. The IV-192 arithmetic uses the corrected normalization.

## 3. Exact dependency identity for the pair

Let (a=d^2), (x=2p-1), and (c=16tx). Then (A=a-c), (G=a+c). The pair's weighted square is:
[
B=pA^2+(1-p)G^2=a^2+x^2(256t^2-32at).
]
Therefore:
[
P_u+P_z=16HB.
]
Under inherited (a=d^2ge16) and (0le tle1/64), (a-8t>0), so the correction (x^2,32t(8t-a)) is nonpositive. The dependency-aware amplitude bound (Ble a^2) is algebraically justified under those conditions.

The radial derivative identity:
[
B_t=2aa_t+x^2(512t-32a_tt-32a)
]
is the correct derivative of the displayed expression for B, assuming the variables and derivative convention held in IV-187. The quotient rule for (Q_i=P_i/D) is structurally:
[
(Q_i)_v=rac{(P_i)_vD-P_iD_v}{D^2}
=rac{(P_i)_v}{D}-rac{P_iD_v}{D^2},
]
for (v=t,p), wherever the derivatives exist and (D
e0. Since D>=1 under the nonnegative component/domain assumptions, the conservative absolute-value estimates in IV-190 are directionally valid.

## 4. Jacobian and norm assembly

For (Q=(Q_u,Q_z,Q_w)) with input coordinates ((t,p)), the Jacobian is a 3-by-2 matrix whose columns are:
[
Q_t=((Q_u)_t,(Q_z)_t,(Q_w)_t)^T,quad
Q_p=((Q_u)_p,(Q_z)_p,(Q_w)_p)^T.
]
Its Frobenius norm satisfies:
[
|J_Q|_{op}le|J_Q|_F
=sqrt{|Q_t|_2^2+|Q_p|_2^2}.
]
Thus IV-191's norm-aggregation route is structurally valid **provided** its component derivative ceilings hold at every point of the domain where the derivative is evaluated. The resulting global Lipschitz conclusion additionally requires differentiability on a domain containing the straight segment between any two inputs (e.g. a convex domain), and uniform derivative bounds along that segment. This condition cannot be inferred from the numeric ceiling alone.

IV-191's (Q) has three components. (Q_3) is not a fourth component in that Jacobian; it is separately bounded in IV-190. This separation is consistent with the retrieved record.

## 5. Historical-ceiling / notation consistency issue

IV-180's preliminary independent component aggregation records (S<2.281390), (|S_t|<33.831188), (|S_p|<4.755005), and preliminary denominator derivative bounds. Later dependency-aware records tighten and replace these:
- IV-186: amplitude (S<1.081145) using the exact joint A/G identity and the (P_w) bound.
- IV-187: radial (|S_t|<17.199242818), ceiling (17.199243).
- IV-188's angular aggregation is referenced by IV-190/192 but its standalone source was not retrieved in this audit.

The IV-180 figures are therefore **historical preliminary ceilings**, not the operative tight ceilings used by IV-190–192. This is not an arithmetic contradiction if explicitly treated as superseded estimates; however, the repository should mark them as superseded to prevent a downstream reader from mixing old and new S bounds. The IV-192 input (S<1.081145) is consistent with IV-186, not with IV-180's older looser aggregation.

## 6. Conditional consistency findings

- Exact A/G, B, and pair identities: algebraically consistent with the retrieved definitions.
- (D=1+tS) and its derivative identities: structurally consistent; IV-189's older (D=1+S) has been superseded.
- Quotient derivative structure: correct conditional form, subject to differentiability and inherited component bounds.
- Three-component / two-input Jacobian assembly: consistent.
- Frobenius-to-operator norm inequality: valid.
- Global Lipschitz inference: conditional on a suitable convex (or segment-contained) domain, differentiability, and uniform derivative ceilings.
- The audit has not independently verified the upstream derivative premises, implicit root existence/uniqueness, domain invariance, or sign premises.

## 7. Outstanding obligations (not closed by IV-193)

1. Retrieve and independently audit the exact IV-188 angular derivative derivation and its input ceilings.
2. Resolve and label historical IV-180 ceilings as superseded in the canonical record or add an explicit supersession note.
3. Establish the full admissible domain and convexity/segment property for the ((t,p)) parameter region.
4. Independently verify differentiability of all component functions and normalized quotients throughout that domain.
5. Re-derive every derivative ceiling from the exact source formulas, including dependency-sensitive derivatives and quotient terms, rather than only checking the aggregation structure.
6. Validate upstream implicit-root and sign assumptions; no claim is made here that (R_d\le0) or a unique root has been established.
7. Only after these obligations close, promote the conditional Lipschitz estimate to a theorem-level result.

## 8. Verdict

**Structural consistency: conditional pass.** The reviewed definitions, normalization, quotient derivative form, Jacobian assembly, and norm inequality are mutually consistent. The operative numerical bounds remain conditional on inherited assumptions and derivative ceilings. The global Lipschitz conclusion is not yet closed because domain/convexity, differentiability, and full upstream premise verification remain open.

This record is an audit result, not a proof of Proposition AS-ALPHA-A-PROP-0012.
