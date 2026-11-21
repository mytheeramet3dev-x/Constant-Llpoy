# IV-72 — Triangle fourth-order analytic audit

## Scope
Triangle graph with couplings a=J12, b=J23, c=J31; h>0. This record consolidates analytic results recovered from the conversation and explicitly excludes unsupported numerical claims.

## Recorded analytic coefficients
Third order: E3=-3abc/(8h^2).

Raw fourth-order walk contribution: E4_raw=-(a^2b^2+a^2c^2+b^2c^2)/(16h^3).

Vacuum-return subtraction/correction recorded for this convention: E4_corr=(a^2+b^2+c^2)^2/(64h^3).

Combined:
E4=(a^4+b^4+c^4-2a^2b^2-2a^2c^2-2b^2c^2)/(64h^3).
At equal couplings a=b=c=J this gives E4=-3J^4/(64h^3).

## Audit caveats
These formulas are analytically recorded but this recovered note does not contain a fresh independent derivation of every path weight. Earlier numerical diagonalization tables associated with IV-72 were unverified/fabricated in the conversation and are explicitly NOT evidence. No numerical pass, general-graph proof, or Lean verification is claimed.