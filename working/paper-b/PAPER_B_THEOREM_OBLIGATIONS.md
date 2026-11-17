# Paper B Theorem Obligations and Status Ledger

Official title: **Equivariant Bifurcation, Isotropy Classification, Representation-Resolved Stability, and Nonlinear Branch Structure in Self-Consistent Quantum Interaction Networks**

This ledger records proof obligations for the redesigned scope. No target theorem is marked proven merely because a standard abstract theorem exists.

| ID | Target result | Minimum proof obligation | Current status |
|---|---|---|---|
| B-REG-01 | Ground-state/equivariance foundation | Prove the ground-state projector and mutual-information feedback map transform under the induced (S_N) action on the stated domain. | OPEN — model-specific statement to formalize |
| B-REG-02 | Entropy regularity at symmetric point | Determine ranks and small-eigenvalue asymptotics of (ho_i,ho_{ij}) in ambient, critical, isotropy-fixed, and transverse directions. | NOT YET INVESTIGATED in the redesigned programme |
| B-CRIT-01 | Nontrivial critical mode | Locate or exclude (1insigma(eta Dmathcal I|_{V_k})), (k=1,2), on a specified symmetric branch and parameter interval. | OPEN |
| B-CRIT-02 | Transversality and spectral complement | Prove crossing derivative is nonzero and all complementary modes are noncritical. | OPEN |
| B-ISO-01 | Isotropy subgroup inventory | Compute conjugacy classes and (dim(operatorname{Fix}(H)cap V_k)) for the chosen critical representation and (N). | NOT YET INVESTIGATED |
| B-NL-01 | Quantum reduced normal form | Derive the first nonzero nonlinear coefficients from the actual mutual-information map, with justified regularity. | OPEN |
| B-EX-01 | Nonuniform branch existence | Prove at least one local nonuniform branch in the physical coupling domain. | OPEN |
| B-CLS-01 | Isotropy classification | Classify branches covered by the proved local theorem up to (S_N)-conjugacy; no global completeness without proof. | OPEN |
| B-BR-01 | Nonlinear branch structure | Prove the correct local expansion, branch direction, and multiplicity from the model-specific reduced equation. | OPEN |
| B-STAB-01 | Representation-resolved stability | Analyze all perturbation modes at the nonuniform branch under the explicitly specified Picard iteration. | OPEN |
| B-STAB-02 | Nonlinear asymptotic stability | Prove stability/instability for hyperbolic branches; resolve nonhyperbolic cases separately. | OPEN |
| B-LEAN-01 | Lean formalization | Formalize frozen theorem statements without `sorry`, hidden axioms, or altered assumptions. | NOT STARTED |

## Mandatory negative-result rule

If a critical eigenvalue never reaches (1) on the specified physical branch, if entropy regularity blocks the required smooth reduction, or if the first nonlinear coefficient vanishes, record that outcome as a mathematical finding. Do not tune assumptions or silently change the feedback model to manufacture a branch.

## Relation to archived Paper B

The former (B-C) sign conjecture and linear sector-ordering argument are archived source material, not a target theorem in this redesigned ledger.
