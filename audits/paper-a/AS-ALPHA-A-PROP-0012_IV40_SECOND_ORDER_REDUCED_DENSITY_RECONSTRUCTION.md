# IV-40 — Second-Order Reduced Density Matrix Reconstruction

**Status:** ONE-SITE STRUCTURE PASS / FULL TWO-SITE RECONSTRUCTION OPEN / ENTROPY COEFFICIENT NOT VERIFIED  
**Scope:** Translate perturbative state amplitudes into reduced density matrices; check which orders can enter one-site eigenvalues and identify the remaining two-site obligations.

## 1. Perturbative state bookkeeping

In the transverse-field (x)-basis, interaction flips occur in pairs. Through second order, the normalized state has structure
[
|psiangle=(1+c_0^{(2)})|0angle+
sum_{e} (a_e^{(1)}+a_e^{(2)})|eangle+
sum_{|F|=4}c_F^{(2)}|Fangle+O(r^3),
]
where (a_e^{(1)}=J_e/(4h)), (a_e^{(2)}) receives shared-vertex path contributions, and (c_F^{(2)}) is the coherent three-pairing four-flip coefficient from IV-39. The displayed state is bookkeeping by perturbative degree; omitted higher-order sectors cannot be ignored when seeking fourth-order probabilities or entropy remainders.

## 2. One-site reduced density matrix structure

The Hamiltonian commutes with global transverse parity (P_x=\prod_i\sigma_i^x). For the unique ground state, the state is a parity eigenstate. Since (P_x) factors into site parity and environment parity, tracing the environment forces the one-site reduced state to commute with (sigma_i^x). Thus in the (x)-basis it is diagonal:
[
\rho_i=\begin{pmatrix}1-p_i&0\\0&p_i\end{pmatrix}
]
(up to which basis vector is designated the small-eigenvalue sector). This symmetry statement is exact in the nondegenerate ground-state regime, not just perturbative.

The leading small eigenvalue comes from first-order pair amplitudes:
[
p_i^{(2)}=\sum_{j\ne i}|a_{ij}^{(1)}|^2
=\sum_{j\ne i}\frac{J_{ij}^2}{16h^2}.
]
For the symmetric coupling (J_{ij}=J), this becomes
[
p_i^{(2)}=\frac{N-1}{16}r^2,quad r=J/h.
]

The next perturbative contribution (degree three in coupling) includes interference between first- and second-order amplitudes:
[
p_i^{(3)}=2\operatorname{Re}\sum_{j\ne i}a_{ij}^{(1)*}a_{ij}^{(2)}.
]
This formula is an order-bookkeeping identity for the two-flip sector. It is not a full expression for (p_i) through degree four; fourth-order probability terms also receive four-flip amplitudes squared, higher-order two-flip amplitudes, and consistent normalization contributions.

## 3. Two-site reduced density matrix: exact construction, unresolved expansion

For any global state with amplitudes (c_{ab}), where (a) labels the two-site basis and (b) the environment basis, the exact reduced matrix is
[
(\rho_{ij})_{aa'}=\sum_b c_{ab}\overline{c_{a'b}}.
]
This is exact and is the reconstruction formula to apply to the perturbative state.

The two-site matrix contains populations and coherences. To obtain its eigenvalues to the order required for entropy derivatives, the expansion must include all amplitudes whose products contribute at that order, including normalization, two-flip corrections, four-flip channels, and relevant off-diagonal blocks. IV-39 path amplitudes alone are not yet a completed second-order reduced-matrix expansion.

## 4. Consequence for entropy and edge-response difference

The exact one-site symmetry/diagonal form is established, and the leading (p_i=O(r^2)) term is recovered. But a complete (B-C) coefficient requires the differentiated one-site and two-site entropy contributions with order-consistent eigenvalue/coherence expansions. In particular, the low-eigenvalue entropy derivative involves (p_u\ln p); the coefficient of (p_u) and the differentiated higher-order remainder cannot be inferred from (p=O(r^2)) alone.

## 5. Findings

- Global parity symmetry implies one-site reduced state diagonal in the (x)-basis: **PASS (exact, nondegenerate ground state)**.
- Leading one-site eigenvalue (\sum_{j\ne i}J_{ij}^2/(16h^2)): **PASS**.
- Degree-three interference term (2\mathrm{Re}\sum a^{(1)*}a^{(2)}): **STRUCTURE DERIVED**; its fully evaluated coefficient is not yet independently checked.
- Exact two-site partial-trace formula: **PASS**.
- Full two-site matrix expansion to the entropy-required order: **OPEN**.
- Recomputed entropy derivative and (B-C): **OPEN**.
- Lean proof/build: **NOT PERFORMED**.

## 6. Disposition

IV-40 is a partial structural audit only. It does not promote the current candidate coefficient to a theorem. PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.
