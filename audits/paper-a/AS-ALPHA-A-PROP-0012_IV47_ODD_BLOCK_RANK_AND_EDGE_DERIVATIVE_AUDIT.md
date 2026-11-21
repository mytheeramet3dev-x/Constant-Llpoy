# IV-47 — Symmetric Odd-Block Rank and Edge-Direction Derivative Audit

**Status:** LEADING ODD-BLOCK SPECTRUM PASS / LOW BRANCH DEGENERACY IDENTIFIED / HIGHER ORDER OPEN  
**Scope:** Evaluate the IV-46 leading odd block at the symmetric coupling point and its leading derivatives in the B (J_13) and C (J_34) directions.

## 1. Symmetric leading odd block

For retained sites 1,2 and all couplings J_ab=J, define g=J/(4h), with fixed N>=4. IV-46 gives
O^(leading)=(N-2)g^2 [[1,1],[1,1]].
Its eigenvalues are 2(N-2)g^2 and 0. The nonzero eigenvalue is 2(N-2)(J/(4h))^2=(N-2)J^2/(8h^2)=(N-2)r^2/8, matching the previously recorded leading odd branch. The second branch has zero coefficient at order r^2 and must be resolved at higher order; do not assume it is exactly zero.

## 2. Derivative in incident edge B=J_13

At symmetric point, differentiating leading IV-46 odd entries with respect to J_13 affects k=3 terms:
O11_B=0, O22_B=2g/(4h), O12_B=g/(4h), O21_B=g/(4h), with this basis ordering and real couplings.
The expectation of this derivative matrix in the leading null eigenvector (1,-1)/sqrt(2) is zero. Thus the zero branch has no first-order eigenvalue shift from this leading derivative matrix; this does not settle higher-order eigenvalue derivatives or logarithmic entropy contributions.

## 3. Derivative in disjoint edge C=J_34

The leading IV-46 odd block depends only on couplings incident from retained sites 1 or 2 to environment vertices k. Therefore the leading derivative with respect to J_34 is zero in these odd-block entries. Higher perturbative paths can and generally do introduce J_34 dependence, so this is only a leading-order statement.

## 4. Entropy consequence

The odd block has a rank-one leading matrix at uniform coupling. Consequently, its leading small-coupling spectrum contains one O(r^2) branch and one branch with no r^2 coefficient. Entropy derivative estimates that assume both branches are uniformly O(r^2) with positive leading coefficients are invalid at the symmetric point. The low branch requires a higher-order reconstruction and controlled derivative before its lambda ln(lambda) term is evaluated.

## 5. Disposition

Leading symmetric odd-block eigenvalues: **PASS**.  
Leading B-direction odd-block matrix derivative: **PASS (algebraic)**.  
Leading C-direction odd-block derivative: **PASS (zero from formula)**.  
Higher branch order/entropy derivative: **OPEN**.  
Lean verification/build: **NOT PERFORMED**.

PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.
