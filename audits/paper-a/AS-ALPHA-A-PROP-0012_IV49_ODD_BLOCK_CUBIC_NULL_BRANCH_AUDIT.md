# IV-49 — Odd-Block Cubic Null-Branch Audit

**Target:** AS-ALPHA-A-PROP-0012, weak-coupling edge response B-C  
**Status:** ANALYTIC-PARTIAL / OPEN / NOT VERIFIED  
**Scope:** Test whether the actual symmetry/selection rules force the cubic null-branch coefficient B_vv to vanish. No full perturbative coefficients or Lean verification claimed.

## 1. What is required

In the leading odd-block eigenbasis (u,v), IV-48 gives
O(r)=r^2 A+r^3 B+r^4 C+..., A=diag(a_+,0), a_+>0.
The small eigenvalue has cubic coefficient B_vv=<v|B|v>. The r^4 formula requires B_vv=0. Rank-one structure at order r^2 does not itself imply this.

## 2. Symmetry assessment

The exact global x-parity constrains the subsystem reduced matrix to even/odd parity blocks. It forbids cross-block matrix elements, but it does not by itself forbid cubic corrections within the odd block. A symmetry argument for B_vv=0 would require an additional transformation that maps the perturbation parameter r to -r while acting within the odd block with a known parity on v. Such a transformation has not been established for the complete coupling graph and edge-parameter setting frozen in Paper A.

Amplitude-path counting also does not settle the cubic coefficient: a reduced-matrix entry is a sum of products of amplitudes from environment configurations, and paths with different perturbative orders can interfere. The exact parity selection rule only fixes allowed spin-flip sectors; it is not a coefficient cancellation theorem.

## 3. Cubic coefficient in the null direction

In the u,v basis, write the cubic block as B. The coefficient is
B_vv = (B_11+B_22-B_12-B_21)/2
in the original odd-block basis, where u=(1,1)/sqrt(2), v=(1,-1)/sqrt(2). For a real symmetric block, this is (B_11+B_22-2B_12)/2. The cancellation condition is therefore a specific combination of cubic reduced-matrix entries, not a consequence of leading rank one.

## 4. Audit disposition

- Exact odd-block parity structure: carried forward.
- Algebraic expression for cubic null coefficient: PASS.
- Global x-parity alone implies B_vv=0: **NO; not implied**.
- Additional r -> -r symmetry for the frozen model and chosen parameterization: **NOT ESTABLISHED**.
- Actual cubic entries and their cancellation: **OPEN**.
- Low eigenvalue branch order (r^3 vs r^4 or later): **OPEN**.
- B/C derivatives, entropy log remainder, B-C: **OPEN**.
- Lean verification: **NOT PERFORMED**.

## 5. Next obligation

IV-50 should compute cubic odd-block entries from explicit second-order amplitudes and the relevant third-order corrections, or establish a valid parameter sign/gauge symmetry that eliminates the cubic contribution. No r^4 claim should be made until this is resolved.
