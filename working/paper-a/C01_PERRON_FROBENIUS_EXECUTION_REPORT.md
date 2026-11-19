# C-01 Execution Report — Finite-N Perron–Frobenius Ground-State Simplicity

- **Document ID:** CL-PA-C01-ER-001
- **Version:** 0.1.0
- **Working branch:** `paper-a-mcr01-pf-redline`
- **Frozen manuscript:** `mytheeramet3dev-x/Absolute_Sym`
- **Frozen source branch:** `paper-a-interval-audit-2026-11-14`
- **Frozen source commit:** `8deb7de4a49cb2060720246b7101820ee7e08c91`
- **Frozen Section 2 blob:** `541382fa7ab4b9e254c8e7e5158f202c1a975e0d`
- **Scope:** C-01 / AS-ALPHA-A-THM-0002 only
- **Disposition:** ANALYTIC PROOF REVIEW PASS; MODEL ENCODING PARTIALLY FORMALIZED; FULL LEAN CLAIM NOT VERIFIED
- **Upstream policy:** No upstream manuscript edits made.

## 1. Executive result

C-01 is not an unresolved mathematical conjecture. A separate finite-dimensional proof review dated 2026-11-17 accepts the corrected Perron–Frobenius argument for every finite (N\ge1), every (h>0), and arbitrary finite real edge couplings (J_{ij}\).

The remaining problem is **formal completeness and exact source correspondence**, not the underlying finite-dimensional theorem.

The frozen Section 2.1 sentence is under-specified: it says the Hamiltonian is shifted by a sufficiently large multiple of the identity, but does not write the shifted operator. The correct operator must be stated explicitly as
[
K=cI-H,
]
not (H+cI). If the latter was intended, its off-diagonal entries remain (-h) and it is not entrywise nonnegative. The manuscript correction should therefore make the sign and operator explicit rather than leave “shift” ambiguous.

## 2. Correct finite-dimensional proof

In the computational (sigma^z)-basis indexed by bit strings (s\in\{0,1\}^N\), the Hamiltonian
[
H=-\sum_{i<j}J_{ij}\sigma_i^z\sigma_j^z-h\sum_{i=1}^N\sigma_i^x
]
has:
- diagonal entries determined by the Ising couplings;
- off-diagonal entry (-h) exactly when two bit strings differ at one coordinate;
- zero for all other off-diagonal entries.

Choose
[
c=1+\max_s H_{ss},\qquad K=cI-H.
]
Then:
1. (K_{ss}>0) for every basis state.
2. Every single-spin-flip off-diagonal entry equals (+h>0).
3. Every other off-diagonal entry is zero.
4. Thus (K) is entrywise nonnegative and real symmetric.
5. Its positive off-diagonal support graph is the Boolean hypercube, which is connected because one can flip, one by one, exactly the coordinates on which two bit strings differ.
6. Perron–Frobenius for a finite irreducible nonnegative matrix gives a strictly positive eigenvector at the spectral radius and a simple Perron eigenvalue.
7. Since (K) is real symmetric, its spectral radius is its largest eigenvalue. Its eigenvalues are (c-E_j(H)), so the largest eigenvalue of (K) corresponds to the smallest eigenvalue of (H).
8. The ground eigenvalue of (H) is therefore simple, and its eigenvector has a strictly positive computational-basis representative.

The proof is valid for arbitrary finite real (J_{ij}), because the couplings affect only diagonal entries. The hypothesis (h>0) is essential to the positive hypercube edges.

## 3. Independent mathematical review — accepted

The existing review artifact was fetched from the working branch and inspected:

- File: `audits/paper-a/THM-0002_PERRON_FROBENIUS_INDEPENDENT_REVIEW.md`
- Blob SHA: `496185967150f151241217069353096ee8ddd1e0`
- Review date: 2026-11-17
- Disposition: **MATHEMATICAL_PROOF_PASS; LEAN_FORMALIZATION_PENDING**

The review explicitly accepts:
- finite (N\ge1), (h>0), arbitrary finite real (J_{ij});
- entrywise nonnegativity of (K=cI-H);
- irreducibility from hypercube connectivity;
- strict positivity and simplicity of the Perron eigenvector/eigenvalue;
- transfer to ground-state simplicity of (H).

It explicitly does **not** imply:
- strict positivity of reduced density matrices;
- entropy differentiability;
- branch ordering or curvature nondegeneracy;
- any thermodynamic-limit result;
- Lean formalization or manuscript-to-Lean correspondence.

Therefore the analytic review sub-status is PASS. This does not promote the full Paper A claim to VERIFIED.

## 4. What is already formalized in the working branch

The following exact working-branch Lean files were fetched:

| File | Blob SHA | Observed declarations / scope |
|---|---|---|
| `formalization/lean/ConstantLlapoy/PaperA/HamiltonianEncoding.lean` | `c168ac95bdd0bd9716a4f1568c8b6391e780664f` | Explicit computational-basis TFIM matrix; Hermiticity; (K=cI-H); diagonal shift; entrywise nonnegativity; exact single-spin-flip support; Boolean-hypercube connectivity; shifted-matrix Hermiticity; conditional Perron multiplicity bridge; eigenvector correspondence |
| `formalization/lean/ConstantLlapoy/PaperA/PerronFrobeniusCore.lean` | `d1553a8dbcf60aaec449a98d59e92ab91c1812ea` | Abstract positive-eigenvector positivity propagation; stochastic/Doob kernel; harmonic-ratio constancy; eigenspace/multiplicity arguments conditional on a supplied positive eigenpair |

Specific model-level declarations observed in `HamiltonianEncoding.lean` include:
- `transverseIsingHamiltonian_isHermitian`
- `isingDiagonalEnergy_lt_shiftConstant`
- `shiftedTFIMHamiltonian_entrywise_nonneg`
- `shiftedTFIMHamiltonian_positive_iff_single_flip`
- `singleSpinFlip_pf_connected`
- `shiftedTFIMHamiltonian_pf_connected`
- `shiftedTFIMHamiltonian_nonneg_eigenvector_strictly_positive`
- `shiftedTFIMHamiltonian_isHermitian`
- `shiftedTFIMHamiltonian_perron_characteristic_root_multiplicity_one`
- `shiftedTFIMHamiltonian_perron_characteristic_root_multiplicity_one_of_nonneg_eigenvector`
- `shiftedTFIMHamiltonian_mulVec_identity`
- `shiftedTFIMHamiltonian_eigenvector_iff`
- `shiftedTFIMHamiltonian_isIrreducible`

Important distinction:
- `shiftedTFIMHamiltonian_nonneg_eigenvector_strictly_positive` proves positivity **if** a nonzero coordinatewise nonnegative eigenvector is supplied. It does not construct one.
- The conditional characteristic-root multiplicity theorem assumes a positive eigenvector/eigenpair. It is not the missing existence theorem.
- `shiftedTFIMHamiltonian_eigenvector_iff` does prove the algebraic eigenvector correspondence for (K=cI-H). The extremal ordering and full ground-eigenvalue multiplicity transfer are still not assembled into the final theorem.
- The model matrix, nonnegativity, Hermiticity, and irreducible support are formalized, but the decisive top-eigenvector existence step remains absent.

## 5. Exact remaining Lean obligations

### C01-L1 — Construct a nonnegative eigenvector at the top eigenvalue

For the actual finite real-symmetric matrix (K), prove existence of a nonzero vector (v\) with (v_s\ge0\) for all (s\), satisfying
[
Kv=\lambda_{\max}(K)v.
]

The current proof-plan artifact recommends the symmetric Rayleigh-maximization route:
1. Obtain a maximizing unit vector for the Rayleigh quotient.
2. Replace coordinates by absolute values.
3. Prove the norm is unchanged and the quadratic form does not decrease because all matrix entries are nonnegative.
4. Use maximality to show the absolute-value vector is also a maximizer.
5. Invoke the pinned finite-dimensional symmetric Rayleigh theorem to obtain an eigenvector at the largest eigenvalue.

This is a proof architecture only; the absolute-value inequality and extremizer transfer are not yet formalized.

### C01-L2 — Prove strict positivity

Once a nonzero nonnegative top eigenvector is constructed, use the already formalized positive-support connectivity and eigen-equation to show that a zero coordinate would force every positive neighbor to be zero, propagating along the connected hypercube and contradicting nonzeroness.

The existing positivity-propagation theorem appears to cover this conditional step, subject to exact theorem statement and build correspondence.

### C01-L3 — Prove the Perron eigenvalue is positive and is the spectral radius

The positive diagonal shift provides positive diagonal entries. A proof must connect this to a strictly positive Rayleigh quotient / positive top eigenvalue. It must also show that the top eigenvalue is the spectral radius in the real-symmetric setting, rather than merely an eigenvalue with a one-dimensional eigenspace.

Do not silently treat “simple eigenvalue” as synonymous with “largest eigenvalue.”

### C01-L4 — Transfer spectral ordering and multiplicity to the physical Hamiltonian

The exact eigenvector identity
[
Kv=\lambda v\iff Hv=(c-\lambda)v
]
is already formalized as `shiftedTFIMHamiltonian_eigenvector_iff`.

Still required:
1. Prove that the largest eigenvalue of (K) corresponds to the smallest eigenvalue of (H).
2. Transfer the one-dimensional eigenspace / characteristic-root multiplicity result under the affine spectral map (E=c-\lambda).
3. State precisely whether the formal target is geometric eigenspace dimension, algebraic characteristic-root multiplicity, or both, and prove the equivalence using the real-symmetric spectral theorem.

### C01-L5 — Assemble the source-matched theorem

Construct the final theorem with no assumed positive eigenvector, no assumed top-eigenvalue property, and no hidden irreducibility premise. Its quantifiers must match the frozen manuscript claim:
[
N\ge1,\quad h>0,\quad J_{ij}\in\mathbb R\text{ finite}.
]

The reference model may impose (J_{ij}\ge0), but the proof itself is stronger because the couplings only affect the diagonal.

## 6. Formalization plan and source artifacts

The existing plan was fetched and inspected:

- File: `PAPER_A_PF_EXISTENCE_FORMALIZATION_PLAN.md`
- Blob SHA: `302f573147de51c90797338b1ff6135ee85bfeb7`
- It records PA-LEAN-027 (positive top-eigenvector existence), PA-LEAN-028 (spectral-shift and multiplicity transfer), and PA-LEAN-029 (final theorem assembly) as not implemented / partial.
- It identifies the pinned Lean and Mathlib revisions and a candidate symmetric Rayleigh proof route.
- It also records external formalization prior art as research context only; no external code is imported or treated as an available theorem.

The semantic correspondence audit was also inspected:
- File: `PAPER_A_LEAN_SEMANTIC_CORRESPONDENCE_AUDIT.md`
- Blob SHA: `4186f4db6589be46bc48e3e147c9f180fab6e9d8`
- It classifies THM-0002 as PARTIAL_SUPPORT_ONLY and explicitly leaves top-eigenvector existence and spectral transfer open.

## 7. Status ledger

| Layer | Status | Reason |
|---|---|---|
| Correct mathematical statement | PASS | Finite-dimensional proof is reviewed under explicit assumptions |
| Independent mathematical proof review | PASS | Review artifact dated 2026-11-17 |
| Frozen source wording | CORRECTION REQUIRED | Shift operator is not specified; write (K=cI-H) explicitly |
| Hamiltonian matrix encoding | FORMALIZED IN SOURCE | Exact declarations observed in working branch; build not run in this report |
| Shifted matrix nonnegativity | FORMALIZED IN SOURCE | Entrywise theorem observed |
| Hypercube support/connectivity | FORMALIZED IN SOURCE | Connectivity and irreducibility declarations observed |
| Conditional positivity propagation | FORMALIZED IN SOURCE | Requires supplied nonzero nonnegative eigenvector |
| Positive top-eigenvector existence | OPEN | Not constructed |
| Spectral radius / largest-eigenvalue bridge | OPEN | Must be proved and connected |
| (K=cI-H) eigenvector correspondence | FORMALIZED IN SOURCE | Exact iff theorem observed |
| Ground-eigenvalue multiplicity transfer | OPEN / PARTIAL | Final extremal and multiplicity assembly absent |
| Exact source-to-Lean theorem correspondence | OPEN | Final theorem not assembled |
| Current Lean build / axiom audit | NOT RUN IN THIS REPORT | No build result is asserted |
| Overall THM-0002 | **NOT VERIFIED** | Decisive existence and transfer obligations remain |

## 8. Next implementation task

Implement **C01-L1** only: the symmetric Rayleigh-maximization construction of a nonzero nonnegative eigenvector at the largest eigenvalue of the actual shifted TFIM matrix.

Do not attempt to mark THM-0002 complete in the same change. Keep C01-L2 through C01-L5 as separately reviewable obligations. After C01-L1 is implemented, run the pinned Lean build, inspect all introduced axioms, and update the semantic correspondence audit with exact theorem names and source hashes.

## 9. Verification boundary

- This report is based on source-level inspection of the frozen Section 2 and the exact working-branch Lean/audit files listed above.
- No Lean build or CI run was executed for this report.
- The mathematical review PASS is inherited from the separately recorded review artifact, not newly claimed as an independent review by this report.
- The frozen upstream `Absolute_Sym` source was not modified.
- Overall Paper A remains **NOT VERIFIED**.


## 10. Clarification added after the C01-L1 API inspection (2026-11-19)

The statement in §5 that the absolute-value inequality was not yet formalized is superseded by the more precise finding in `C01_L1_RAYLEIGH_CONSTRUCTION_DESIGN.md`: the scalar inequality `quadratic_form_le_abs_quadratic_form` is already source-present in `PerronFrobeniusCore.lean`. What remains open is the Euclidean-space coordinate bridge, norm preservation of the coordinatewise absolute-value vector, transfer of the Rayleigh maximizer property, and translation of the resulting eigenvector equation back to the matrix form. No new Lean build is claimed. The detailed pinned Mathlib APIs and the refined C01-L1 proof architecture are recorded in that design report.
