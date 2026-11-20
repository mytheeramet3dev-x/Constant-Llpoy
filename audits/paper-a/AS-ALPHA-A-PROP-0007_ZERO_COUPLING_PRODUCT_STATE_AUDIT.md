# Paper A PROP-0007 — Zero-coupling product state audit

- Claim ID: AS-ALPHA-A-PROP-0007
- Audit date: 2026-11-21
- Frozen source: Section 2.4 at Absolute_Sym commit `8deb7de4a49cb2060720246b7101820ee7e08c91`
- Disposition: ANALYTIC-VERIFIED for the zero-coupling ground state, vanishing mutual information, and trivial fixed point; NOT-LEAN-VERIFIED.

## Source claim

At (x=0), the interaction vanishes and the transverse-field ground state is
[
|widetildePsi_0(0)angle=igotimes_{i=1}^{N}|+xangle_i.
]
The source concludes (mathcal G_N(0)=0) and that (x=0) is a fixed point for every positive feedback and field scale.

## Independent derivation

For (h>0) and (J=0),
[
H(0,h)=-hsum_{i=1}^Nsigma_i^x.
]
Each one-site term has eigenvalues (-h,+h), with (|+xangle) the unique local ground state of (-hsigma^x). The terms act on distinct tensor factors and commute; the total ground state is therefore the unique tensor product (igotimes_i|+xangle_i).

The global density operator is a product. Its one-site reductions are (ho_i=|+xanglelangle+x|), and its two-site reductions are (ho_{ij}=ho_iotimesho_j). Each reduced entropy is zero, so
[
I_{ij}=S(ho_i)+S(ho_j)-S(ho_{ij})=0+0-0=0.
]
Thus (mathcal G_N(0)=0). The dimensionless self-consistency equation (x=etamathcal G_N(x)) is satisfied at (x=0) for every (eta=g/h) (in particular for (g,h>0)).

## Verdict and boundaries

- **PASS:** zero-coupling Hamiltonian ground state, product structure, zero pair mutual information, and trivial fixed point.
- **Not included:** endpoint differentiability of (mathcal G_N), entropy derivatives, stability of the zero fixed point, or any nontrivial-root existence claim.
- **Formal status:** no Lean theorem was established for this complete model-specific statement. This audit is analytic, not formal verification.
