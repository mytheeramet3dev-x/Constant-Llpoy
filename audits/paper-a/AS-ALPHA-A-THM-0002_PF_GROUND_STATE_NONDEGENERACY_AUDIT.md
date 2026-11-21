# THM-0002 Audit — Perron–Frobenius Ground-State Nondegeneracy

**Target:** Paper A THM-0002, finite TFIM ground-state nondegeneracy for \(h>0\).  
**Source freeze:** Absolute_Sym commit \`8deb7de4a49cb2060720246b7101820ee7e08c91\`.  
**Formal source inspected:** Constant Llpoy \`formalization/lean/ConstantLlapoy/PaperA/PerronFrobeniusCore.lean\`, plus Hamiltonian encoding module.  
**Audit type:** Proof-chain review; no Lean build or external theorem checker executed in this pass.

## Verdict

**PARTIAL — substantial conditional PF chain is formalized, but existence of the needed nonnegative eigenvector at the maximal eigenvalue is not supplied by the inspected Lean declarations.**

## 1. Correct sign of the spectral shift

For the Hamiltonian sign convention used in the source, the appropriate nonnegative matrix is
\[
K=cI-H,
\]
with \(c\) chosen above every diagonal energy. The source's instruction to shift \(H\) upward by a large positive identity is not the correct PF construction for this sign convention; preserve the frozen manuscript and track a correction separately.

## 2. Model properties checked in the Lean source

The inspected declarations establish the relevant structural route:
- \`shiftedTFIMHamiltonian_entrywise_nonneg\`: entrywise nonnegativity under \(h\ge0\);
- \`shiftedTFIMHamiltonian_positive_iff_single_flip\`: positive off-diagonal support is exactly a single-spin flip for \(h>0\);
- \`singleSpinFlip_pf_connected\` and \`shiftedTFIMHamiltonian_pf_connected\`: Boolean-hypercube positive-support connectivity;
- \`shiftedTFIMHamiltonian_isHermitian\`: real symmetry/Hermitian property;
- \`shiftedTFIMHamiltonian_mulVec_identity\` and \`shiftedTFIMHamiltonian_eigenvector_iff\`: explicit scalar-shift eigenvector correspondence.

The shift constant and diagonal positivity are also handled in the model-level declarations.

## 3. Conditional Perron chain already formalized

The core module contains a long, explicit conditional chain:
1. a supplied strictly positive eigenvector normalizes a stochastic kernel;
2. ratios of eigenvectors become harmonic functions;
3. connected positive support propagates equality, giving geometric eigenspace proportionality;
4. symmetric spectral-basis orthogonality bridges geometric simplicity to a unique spectral-list index;
5. the characteristic-polynomial root multiplicity is shown to be one.

A separate model theorem proves any supplied nonzero coordinatewise nonnegative eigenvector becomes strictly positive under the connected-support hypothesis:
\[
v\ge0,\quad v\ne0,\quad Av=\lambda v
\quad\Longrightarrow\quad v_i>0\ \forall i.
\]
This theorem is conditional on an eigenvector already being supplied.

## 4. Main missing proof obligation

The inspected declarations do **not** construct a nonzero nonnegative eigenvector at the largest eigenvalue of \(K\), nor do they exhibit a completed theorem that supplies this existence step. The source has an auxiliary inequality showing the quadratic form of a nonnegative matrix does not decrease when a vector is replaced coordinatewise by its absolute values. This is useful for a variational existence route but is not, alone, a completed eigenvector-existence theorem.

A completion should:
- use finite-dimensional real symmetric spectral theory / Rayleigh maximization to select a unit eigenvector at the largest eigenvalue;
- apply the absolute-value quadratic-form inequality to show a nonnegative maximizer can be chosen;
- prove its eigenvector equation at the maximizing eigenvalue;
- then invoke the existing strict-positivity propagation and simplicity chain;
- explicitly transfer the maximal eigenvalue of \(K=cI-H\) to the minimal eigenvalue of \(H\).

Do not infer the existence step merely from declarations proving positivity or simplicity conditional on eigenvector hypotheses.

## 5. Scope and nonclaims

- The finite-dimensional analytic PF route is mathematically standard and consistent.
- The model-level support and sign checks are substantially represented in Lean.
- Conditional strict positivity and simplicity chain are present in the inspected source.
- The full model theorem is **not yet Lean-closed** from the declarations reviewed.
- This review did not run Lean, inspect build logs, or independently prove compilation.
- This review does not establish any thermodynamic-limit claim.

**Disposition:** \`ANALYTIC-PARTIAL / FORMALIZATION-INCOMPLETE\`. Keep THM-0002 open until the nonnegative top-eigenvector existence lemma and the final ground-state transfer are closed and built.
