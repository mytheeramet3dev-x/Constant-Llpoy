# PROP-0012 IV-9 — Working-Proof Integration and Provenance Closure

**Scope:** Integrate IV-8's shared-amplitude even-block remainder into the current working derivation, without upgrading the overall proposition beyond what the component derivations support.

## 1. Source artifacts fetched before integration

- Working proof: \`working/paper-a/WEAK_COUPLING_B_MINUS_C_DERIVATIVE_PROOF.md\`, prior blob SHA \`fe401f8f8d9617c25e8d12be554be9f90941422b\`.
- IV-8 direct environment-sum reconstruction: blob SHA \`ae65288901ee26fbebb2abd535998f056ae232ba\`.
- Pair-flip order audit: blob SHA \`c288692fd8ea208d7fe6747f70138d031533a3cb\`.
- Shared-amplitude closure review: blob SHA \`e0864a10508613b02256b8aef8ffb3ec4cf8f35b\`.
- Entropy derivative lemma: blob SHA \`2a7aa295762ad2616750c9b224e18e55f4e95ad3\`.

## 2. Integration result

The working proof's former Section 4 conservative Schur estimate \(D=O_N(r^3)\) and entropy directional derivative \(O_N(r^3(1+|\ln r|))\) was replaced by the exact environment-sum decomposition:
\[
L=|c_\emptyset|^2+R_L,\quad
X=c_\emptyset\overline{c_{12}}+R_X,\quad
S=|c_{12}|^2+R_S.
\]
Under the fixed-\(N\) pair-flip Taylor-support bounds (with first edge derivatives),
\[
R_L=O_N(r^2),\quad
R_X=O_N(r^3),\quad
R_S=O_N(r^4).
\]
The shared exact amplitude \(c_{12}\) cancels between \(S\) and \(|X|^2/L\), yielding
\[
D=S-|X|^2/L=O_N(r^4),\quad \partial_{u_e}D=O_N(r^4).
\]
The determinant-to-small-eigenvalue identity then gives \(\lambda_s,\partial_{u_e}\lambda_s=O_N(r^4)\), and, with the positive-branch logarithmic scale hypothesis and the zero-branch treatment kept separate, the entropy directional derivative is \(O_N(r^4(1+|\ln r|))\).

This integration does **not** assume \(c_{12}=a_{12}+O(r^3)\). The reviewed perturbation bookkeeping permits second-order overlapping pair-flip paths, so \(c_{12}=a_{12}+O_N(r^2)\) in general. The cancellation uses the same exact \(c_{12}\) in both entries.

## 3. Provenance/status corrections

- The working derivation now carries the IV-8 conditional \(O_N(r^4)\) closure; the old \(O_N(r^3)\) estimate remains a weaker bound but is no longer the operative statement in Section 4.
- The matrix's stale warning that the \(O_N(r^4)\) refinement must not be used is superseded **only for this shared-amplitude derivation**. An earlier parity-only argument was invalid and is not revived.
- IV-9 PASS is restricted to integration and consistency of this local even-block remainder. It does not close the odd positive branch, the full entropy-contrast remainder, manuscript-source reconciliation, Lean formalization/build, or global \(B-C>0\).

## 4. Independent re-check and limitations

The environment sums are finite at fixed \(N\); the tail order follows from the pair-flip support lemma, and the quotient expansion follows from \(L=1+O_N(r^2)\). First edge derivatives retain the stated orders by joint analyticity on a compact local edge neighborhood.

Remaining obligations:
1. verify the pair-flip Taylor recursion as a complete proof and independently test its conventions against the exact source Hamiltonian;
2. resolve access to the frozen Paper A source (previously 404/NOT FOUND) and reconcile definitions/signs;
3. audit the odd positive entropy branch and combine all branches into the complete differentiated mutual-information contrast;
4. perform Lean formalization/build and manuscript-to-declaration correspondence;
5. establish or refute the global sign.

**Verdict: IV-9 PASS for working-proof integration of the even-block shared-amplitude remainder only; PROP-0012 remains OPEN / ANALYTIC-PARTIAL / NOT VERIFIED.**
