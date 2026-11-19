# MCR-01 — Proposed Redline: Perron–Frobenius Ground-State Argument

- **Document ID:** CL-PA-RL-MCR-01
- **Status:** PROPOSED TEXT; INTERNAL MATHEMATICAL CHECK ONLY; NOT UPSTREAM-APPLIED
- **Affected claim:** AS-ALPHA-A-THM-0002
- **Frozen source:** `mytheeramet3dev-x/Absolute_Sym`, commit `8deb7de4a49cb2060720246b7101820ee7e08c91`
- **Source file:** `Arxiv/paper_01_section_02_revised.md`, §2.1
- **Source blob:** `541382fa7ab4b9e254c8e7e5158f202c1a975e0d`
- **Correction register item:** MCR-01

## 1. Exact source passage to replace

The current §2.1 states:

> For finite \(N\) and \(h>0\), the ground state is nondegenerate. This follows from Perron–Frobenius theory after shifting the Hamiltonian by a sufficiently large multiple of the identity: the resulting matrix is nonnegative and irreducible in the computational \(\sigma^z\) basis.

The stated shift direction is incorrect for the Hamiltonian's sign convention. Adding \(cI\) to \(H\) leaves its negative spin-flip off-diagonal entries negative.

## 2. Proposed replacement text

For finite \(N\) and \(h>0\), the ground state is nondegenerate. To apply the Perron–Frobenius theorem with the present sign convention, work in the computational \(\sigma^z\) basis and define
\[
K=cI-H,
\]
where \(c\) is chosen so that \(c-H_{ss}\geq 0\) for every computational-basis configuration \(s\). Such a finite \(c\) exists because the Hilbert space is finite-dimensional.

In this basis, the diagonal entries of \(K\) are nonnegative. The only nonzero off-diagonal entries of \(H\) arise from a single spin flip and equal \(-h\); hence the corresponding off-diagonal entries of \(K\) equal \(+h>0\), while all other off-diagonal entries are zero. Thus \(K\) is entrywise nonnegative.

The graph whose vertices are computational-basis configurations and whose edges join configurations differing by one spin flip is the Boolean hypercube, which is connected. Since every such edge has a strictly positive matrix entry, \(K\) is irreducible. By the Perron–Frobenius theorem, its spectral radius \(\rho(K)\) is an eigenvalue with a strictly positive eigenvector and is algebraically simple. Because \(K=cI-H\), the eigenvectors are shared and the largest eigenvalue of \(K\) corresponds exactly to the smallest eigenvalue of \(H\). Therefore the ground eigenspace of \(H\) is one-dimensional.

## 3. Mathematical check and scope

The argument uses:
1. finite-dimensionality, so a finite diagonal shift parameter \(c\) can be chosen;
2. the stated computational-basis sign pattern;
3. \(h>0\), so every single-spin-flip edge has strictly positive weight in \(K\);
4. connectedness of the Boolean hypercube.

No assumption that \(H+cI\) is entrywise nonnegative is used. The proof establishes nondegeneracy for the finite system under the stated Hamiltonian and \(h>0\). It does not establish any thermodynamic-limit gap, uniform spectral gap, or analyticity claim.

## 4. Proof-artifact and verification obligations

- **Analytic route:** The finite-dimensional Perron–Frobenius argument above is complete at the level of the stated matrix structure, conditional on the Hamiltonian matrix entries being exactly as specified.
- **Lean correspondence:** Not established by this redline. Existing positivity-propagation lemmas must not be represented as proving existence of a Perron eigenvector. A formal proof must establish the relevant nonnegative matrix, irreducibility/connectedness, existence and simplicity of the top eigenvalue, and the order-reversing correspondence between eigenvalues of \(H\) and \(K\).
- **Source correspondence:** Must be re-audited against the exact theorem statement and the complete Lean declaration types.
- **Independent review:** Not yet performed. This internal derivation is not an external referee report.

## 5. Redline disposition

**PROPOSED — READY FOR FORMAL/INDEPENDENT CHECK, NOT ACCEPTED.**

This file is a separate working artifact in Constant Llpoy. It does not modify the frozen source snapshot or the upstream `Absolute_Sym` repository. Do not mark MCR-01 resolved until the formal obligations and manuscript-to-artifact correspondence have been checked.
