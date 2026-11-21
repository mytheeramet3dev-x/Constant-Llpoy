# IV-35 — Candidate Formula Provenance & Version-Consistency Audit

**Target:** AS-ALPHA-A-PROP-0012, weak-coupling candidate for (B-C)  
**Status:** OPEN / ANALYTIC-PARTIAL / NOT VERIFIED  
**Scope:** Trace the coefficient versions recorded in the accessible working derivation and IV-31–IV-34 audit records. This is a provenance and consistency check, not a new independent derivation from the frozen manuscript.

## 1. Candidate-version ledger

| Version | Formula | Provenance | Disposition |
|---|---|---|---|
| V0 / prior candidate | (rac{J}{8h^2}[1+ln(2(N-2)/(N-1))]) | Earlier working candidate referenced by IV-31 and IV-32 | **SUPERSEDED for leading-branch bookkeeping**; extra (+1) is not supported by displayed leading branches |
| V1 / corrected displayed-branch candidate | (rac{J}{8h^2}ln(2(N-2)/(N-1))) | Working derivation and IV-31/IV-32; IV-33 checks physical scaling; IV-34 checks coefficient positivity and conditional dominance | Current candidate only; not theorem |

## 2. Consistency findings

- IV-31 and IV-32 agree on the logarithmic coefficient from the displayed one-site and positive odd-block branches.
- Their regular entropy (-1) terms cancel when the leading directional eigenvalue derivatives match.
- IV-33 verifies the chain-rule and dimensional conversion for the displayed term.
- IV-34 verifies positivity of the displayed logarithmic coefficient for fixed (N\ge4), and only conditional sign dominance if the remainder theorem is supplied.
- The accessible working derivation contains the corrected logarithmic candidate, not an established theorem.
- The earlier (+1) candidate is documented as a previous version and is not to be copied into current derivations without a new derivation and explicit reconciliation.

## 3. Source-provenance limitation

The frozen manuscript source previously cited in the matrix is not currently fetchable from the reported frozen branch/commit (earlier fetch returned NOT FOUND). IV-35 therefore does **not** claim to trace the V0 coefficient to an exact frozen manuscript line or independently validate all source definitions. Source reconciliation remains blocked. The target's exact (B,C) definitions, convention, and full block entropy bookkeeping must be checked against an accessible frozen source before promoting V1.

## 4. No status promotion

No coefficient version is theorem-level. Higher/zero spectral branches, complete entropy derivatives, differentiated remainder closure, exact frozen-source reconciliation, and Lean verification remain open. No counterexample to the exact proposition is established.

**Disposition:** provenance consistency PASS within accessible artifacts; source provenance incomplete; V0 marked superseded for the displayed-branch calculation; V1 retained as current unverified candidate. PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.

## 5. Next

IV-36: **Frozen-Source Definition and Edge-Convention Reconciliation Attempt** — retrieve the exact manuscript source at the recorded frozen ref if accessible, compare the target definition, signs, normalization and edge labels against the current derivation, and report failure if source access remains unavailable.