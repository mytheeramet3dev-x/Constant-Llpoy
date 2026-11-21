# IV-75 — Square raw fourth-order coefficient correction record

## Graph and couplings
Square C4 with cyclic edges a,b,c,d.

## Error record
The earlier raw polynomial contained a coefficient error in the b^2 c^2 term. The corrected raw expression is recorded below; IV-75 itself is NOT treated as the final reliable version.

Corrected raw term:
E4_raw=-(2a^2b^2+a^2c^2+2a^2d^2+2b^2c^2+b^2d^2+2c^2d^2+10abcd)/(32h^3).

Correction term:
E4_corr=(a^2+b^2+c^2+d^2)^2/(64h^3).

The corrected combined result is:
E4_C4=(a^4+b^4+c^4+d^4-2a^2b^2-2b^2c^2-2c^2d^2-2d^2a^2-20abcd)/(64h^3).
Opposite-edge pair terms a^2c^2 and b^2d^2 cancel.

## Provenance/status
The coefficient error is retained as an audit-history issue. IV-76 carries the consolidated correction. No independent numerical diagonalization is verified here. No Lean proof.