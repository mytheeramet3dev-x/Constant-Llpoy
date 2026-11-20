# Paper A PROP-0005 — Edge-response algebra and representation audit

- Audit date: 2026-11-21
- Frozen source: Section 5.2 of Paper A, frozen commit 8deb7de4a49cb2060720246b7101820ee7e08c91
- Verdict: **PARTIAL — finite representation/matrix algebra checks pass conditionally; model-response differentiability and Lean proof remain open.**

## Scope and hypotheses
At the fully permutation-symmetric point, assume the edge-response Jacobian exists and is S_N-equivariant. For an edge e, symmetry makes its row entries three-valued: A on e itself, B on edges sharing one endpoint, and C on disjoint edges. The response matrix is therefore in the Johnson association scheme J(N,2).

## Checks
1. Dimension sum:
   1 + (N-1) + N(N-3)/2 = N(N-1)/2, the edge-space dimension. For N=3 the residual sector has dimension 0; formulas referring to a nontrivial V2 eigen-sector should be scoped to N>=4.
2. Uniform eigenvalue: row sum is A + 2(N-2)B + ((N-2)(N-3)/2)C, matching chi_0.
3. Standard/degree-heterogeneous sector: eigenvalue A +(N-4)B -(N-3)C matches chi_1.
4. Residual sector: eigenvalue A -2B + C matches chi_2.
5. Subtraction: chi_1 - chi_2 = (N-2)B -(N-2)C = (N-2)(B-C), algebraically exact.
6. Since chi_0 is the uniform perturbation eigenvalue, the identification with derivative under simultaneous uniform edge variation is valid provided the response is differentiable and the coordinate convention varies every edge by the same amount.

## Limits
- This audit checks the finite combinatorial/matrix algebra under the symmetry and derivative-existence hypotheses. It does not prove the TFIM reduced mutual-information map is differentiable in independent edge variables, especially at reduced-state rank changes.
- It does not establish B-C positivity; that remains a model-specific conjectural sign claim.
- No direct Lean formalization of this decomposition, eigenvalues, or identity is established here. Auxiliary entropy derivative Lean lemmas do not discharge these obligations.
- For N=3, V2 has dimension zero; the stated three-sector interpretation needs N>=4, though the algebraic expressions remain formally evaluable.

