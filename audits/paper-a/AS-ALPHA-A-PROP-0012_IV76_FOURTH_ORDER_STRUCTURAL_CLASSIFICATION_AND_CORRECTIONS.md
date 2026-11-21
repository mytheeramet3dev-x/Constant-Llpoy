# IV-76 — Fourth-order structural classification and correction consolidation

## Consolidated results (working analytic status)
### Square C4
Corrected raw term:
E4_raw=-(2a^2b^2+a^2c^2+2a^2d^2+2b^2c^2+b^2d^2+2c^2d^2+10abcd)/(32h^3).

Correction:
E4_corr=(a^2+b^2+c^2+d^2)^2/(64h^3).

Combined:
E4_C4=(a^4+b^4+c^4+d^4-2a^2b^2-2b^2c^2-2c^2d^2-2d^2a^2-20abcd)/(64h^3).
Opposite edge pair terms cancel.

### Triangle C3
E4_raw=-(a^2b^2+a^2c^2+b^2c^2)/(16h^3).
E4_corr=(a^2+b^2+c^2)^2/(64h^3).
Combined:
E4_C3=(a^4+b^4+c^4-2a^2b^2-2a^2c^2-2b^2c^2)/(64h^3).
For equal J, E4=-3J^4/(64h^3); E3=-3abc/(8h^2).

### Single edge
E4=+J^4/(64h^3).

## Correction/provenance
IV-75 contained a raw coefficient mistake (b^2c^2), corrected here. Prior numerical diagonalization tables are NOT verified and must not be cited as numerical evidence. IV-73's Schur sign derivation is invalid; it remains visibly corrected. The general graph formula remains pending independent derivation and validation. No Lean proof. These consolidated formulas are analytic records and are not a verified closure of Proposition 0012.