# IV-73 — Schur derivation sign correction and provenance

## Correction
An earlier Schur/resolvent derivation in this audit sequence contained a sign error in the resolvent expansion. Therefore that derivation is INVALID as written and cannot be cited as proof.

The final coefficients previously reported happened to agree with other analytic path calculations, but agreement of outputs does not repair the invalid derivation. Coefficients must be independently re-derived from a correct convention before this audit can be closed.

## Status
- Incorrect derivation: superseded; preserve as a visible correction, do not silently overwrite.
- Final coefficients from that derivation: not validated by IV-73 itself.
- Independent path calculations: separate provenance and their own limitations apply.
- No Lean verification.
- Paper A claim remains OPEN / ANALYTIC-PARTIAL / NOT VERIFIED.