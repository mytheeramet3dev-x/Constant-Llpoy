# IV-55 — Direct Fourth-Order Null-Block Reconstruction: Dependency Audit

**Status:** BLOCKED — REQUIRED AMPLITUDE DATA NOT PRESENT IN VERIFIED INPUTS  
**Scope:** Determine whether the direct fourth-order coefficient c_vv can be reconstructed from the currently fetched IV-51 through IV-54 artifacts without silently assuming omitted state-amplitude terms.

## 1. What is established from available inputs

The fetched IV-53/54 reports establish the cubic odd-block off-diagonal derivative and a local mixing-square contribution. IV-52's general Schur expression (as summarized in the current audit context) gives the low-branch fourth-order coefficient in the form c_vv - |b_uv|^2/a, subject to its block-expansion assumptions. These results do not specify all fourth-order direct-block contributions.

## 2. Dependency requirements for a direct c_vv calculation

To compute c_vv from the reduced state rather than treating it as a free symbol, the derivation needs a complete, consistently normalized expansion of the relevant state amplitudes through the order that contributes to the reduced odd block at O(r^4), including:
- all third-order amplitudes that interfere with first-order amplitudes;
- all second-order amplitudes and their products contributing at fourth order;
- fourth-order amplitudes paired with the vacuum/leading amplitudes where relevant;
- normalization and orthogonality corrections at the same order;
- explicit environment labels and multiplicities, so terms survive/vanish under partial trace for justified reasons;
- a fixed convention for r and dimensionless couplings.

The fetched IV-53/54 artifacts contain cubic coefficient formulas and local derivatives, but not the complete amplitude list and normalization data above. Therefore no numerical or closed-form c_vv is reconstructed in this audit.

## 3. Why the mixing term cannot close the calculation

The known mixing correction |b_uv|^2/a is only one contribution. Substituting it into the Schur expression while leaving c_vv unknown does not determine the low eigenvalue coefficient or its sign. It would be mathematically invalid to infer positivity or cancellation from the mixing term alone.

## 4. General block algebra (conditional)

For a Hermitian two-branch block with upper branch r^2 a + O(r^3), lower diagonal r^4 c + O(r^5), and off-diagonal r^3 b + O(r^4), with a>0, the small eigenvalue has leading coefficient r^4(c-|b|^2/a)+O(r^5). This is conditional block perturbation algebra; it does not derive c from the physical reduced density matrix.

## 5. Disposition

- Direct c_vv from amplitudes: BLOCKED (missing complete amplitudes and normalization bookkeeping in verified artifacts).
- Mixing correction: known only in the previously stated local cubic-block scope.
- Full fourth-order coefficient/sign: OPEN.
- B-C edge response: OPEN.
- Entropy derivative and remainder: OPEN.
- Lean/numerical verification: NOT PERFORMED.

Paper A PROP-0012 remains OPEN / ANALYTIC-PARTIAL / NOT VERIFIED.
