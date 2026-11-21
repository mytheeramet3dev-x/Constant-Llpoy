# IV-44 — Exact Two-Site Reduced-Matrix Element Formulas

**Status:** EXACT PARTIAL-TRACE FORMULAS PASS / PERTURBATIVE COEFFICIENTS OPEN  
**Scope:** Express every two-site reduced-matrix entry in x-basis from full-state amplitudes and identify the parity-forbidden entries without claiming perturbative coefficients.

## 1. Full-state amplitude notation

Write the normalized ground-state vector in the x-basis as
|psi> = sum_(a,b,e) c_(a,b,e) |a,b,e>, where a,b are the two retained spin labels (+/-) and e indexes the environment basis. The exact reduced matrix elements are
(rho_ij)_(ab,a'b') = sum_e c_(a,b,e) conjugate(c_(a',b',e)).
This is the partial-trace identity and is valid without truncating the amplitudes.

## 2. Four matrix entries per block

Use basis order even: (++ , --); odd: (+- , -+). The even block entries are:
E11 = sum_e |c_(+,+,e)|^2;
E22 = sum_e |c_(-,-,e)|^2;
E12 = sum_e c_(+,+,e) conjugate(c_(-,-,e));
E21 = conjugate(E12).

The odd block entries are:
O11 = sum_e |c_(+,-,e)|^2;
O22 = sum_e |c_(-,+,e)|^2;
O12 = sum_e c_(+,-,e) conjugate(c_(-,+,e));
O21 = conjugate(O12).

Here the environment sum uses the same environment basis label in each product. These are exact formulas, not perturbative estimates.

## 3. Cross-sector entries

The global parity-eigenstate condition implies subsystem parity conservation in rho_ij. Therefore cross-sector matrix entries (even-to-odd) vanish exactly, e.g.
sum_e c_(+,+,e) conjugate(c_(+,-,e)) = 0,
and likewise for the other even/odd combinations. These vanishings are symmetry consequences, not termwise cancellation assumptions.

## 4. Trace and positivity checks

Exact normalization gives Tr(E)+Tr(O)=sum_(a,b,e)|c_(a,b,e)|^2=1.
Both E and O are Gram matrices of environment-indexed amplitude vectors and therefore positive semidefinite. In particular, |E12|^2 <= E11 E22 and |O12|^2 <= O11 O22. These Cauchy-Schwarz bounds are exact, but not sharp perturbative order estimates.

## 5. Perturbative order requirements

To expand entries for edge derivatives, each coefficient c_(a,b,e) must be available with enough order and uniform differentiated remainder. Products can mix orders; normalization and coherent cross terms must be retained. No explicit amplitude series for all environment configurations is calculated in this audit, so no entry coefficient, block determinant, low eigenvalue, entropy derivative, or B-C sign is certified.

## 6. Disposition

Exact entry/partial-trace formulas: **PASS**.  
Exact block Gram structure and positivity: **PASS**.  
Explicit perturbative entries: **OPEN**.  
Entropy-order eigenvalue/derivative expansion: **OPEN**.  
Lean verification/build: **NOT PERFORMED**.

PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.
