# IV-207 — Radial Derivative Input Reconciliation and Audit Blocker

**Project:** Absolute Symmetry — Paper A  
**Proposition:** AS-ALPHA-A-PROP-0012  
**Status:** PARTIAL / BLOCKED — inconsistency isolated; independent radial re-derivation is not yet justified.

## 1. Scope
Reconcile the radial derivative ceilings carried by IV-203 and IV-204 before attempting a fresh component-level radial derivative audit. IV-201 supplies an improved conditional root derivative ceiling, \(d_t<4.128\), but IV-180's component bounds were computed using the older \(d_t<4.194\) and older \(A_t,G_t,H_t,F_t\) ceilings.

## 2. Records inspected
Fetched and inspected the complete records:
- IV-180, blob SHA 0fe82bffee2aadd9c9f179c54c44f4c5334bdaa1
- IV-201, blob SHA 608d5bcd712278f1a8a6a6d97f3e2f06b932de2a
- IV-203, blob SHA 34d402cb09bf66dee0f193d25c2016e0927aa864
- IV-204, blob SHA 380c473ed61ed1f8edc76fb99718c9bc743b6d50

IV-180 states |(P_u)_t|, |(P_z)_t| < 16.348319 under the old root derivative ceiling. IV-203 gives a dependency-aware pair radial derivative |(P_u+P_z)_t| < 15.879978973, but does not establish the individual component ceilings needed for componentwise quotient differentiation. IV-204's generic quotient computation instead uses an input |(P_u)_t|, |(P_z)_t| < 16.160182018, which is not traceable in the fetched IV-180 record and is not shown to follow from the IV-201 improvement.

## 3. Inconsistency / dependency diagnosis
The radial quotient ceilings cannot be considered reconciled:
- IV-203 reports |(Q_u)_t|, |(Q_z)_t| < 17.685815885, from its stated componentwise propagation.
- IV-204 reports < 17.616462585, using 16.160182018 + 1.081145(1.346979884017405).
- The IV-204 component derivative input 16.160182018 is smaller than IV-180's listed 16.348319, but IV-180 itself uses the older d_t<4.194; a derivation supporting this intermediate value under the revised root ceiling is not present in the inspected records.

Thus IV-204's lower ceiling is not accepted as independently established. IV-203's generic component propagation is retained as a documented prior conservative candidate, but it also remains conditional and is not promoted to a certified bound.

## 4. What can and cannot be concluded
**PASS:** The inconsistency in input provenance is identified and the two competing radial quotient ceilings are explicitly reconciled as non-equivalent derivations.

**OPEN:** A fully independent radial derivative recalculation. It requires the underlying component derivative definitions and intermediate formula for H, and the current radial component derivation record(s). The fetched IV-180 excerpt lists derivative inequalities but not enough derivational detail to safely rebuild every updated ceiling from scratch. Searches for IV-187/IV-202 in the connector did not return usable file excerpts in this run; therefore no missing formulas are guessed.

**Not certified:** source fidelity, root/domain premises, component derivative ceilings, quotient radial ceilings, Jacobian radial norm, full proposition, interval verification, or Lean proof.

## 5. Required next audit
Retrieve the exact upstream component/radial records (particularly IV-186/187 and the full IV-202 correction chain), derive updated H_t, A_t, G_t, F_t and each (P_i)_t using d_t<4.128, recompute D_t, then re-evaluate (Q_i)_t. Only after that should the radial column and Frobenius/Jacobian aggregate be updated using the corrected angular ceilings from IV-205.

## 6. Conclusion
IV-207 is a reconciliation audit, not a completed numerical radial audit. It blocks the unjustified use of IV-204's lower radial ceiling and prevents the existing aggregate Jacobian number from being treated as current. The work remains conditional; no theorem closure is claimed.
