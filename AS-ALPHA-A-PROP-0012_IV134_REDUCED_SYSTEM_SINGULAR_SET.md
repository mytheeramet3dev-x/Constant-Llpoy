# AS-ALPHA-A-PROP-0012 — IV-134: Reduced-System Singular-Set Audit

Status: ANALYTIC ALGEBRAIC AUDIT; NOT LEAN-FORMALIZED; no global branch continuation claim.

## 1. Reduced identities
From the component equations:
u=(4x+4yw)/d, z=(4y+4xw)/d,
and substitution into dw=4yu+4xz gives
F w=16xy, where F=d^2-16(x^2+y^2).

When F != 0:
w=16xy/F,
u=(4x/d)(d^2-16x^2)/F,
z=(4y/d)(d^2-16y^2)/F.
For x != 0 and d^2-16x^2 != 0:
w/u=4dy/(d^2-16x^2).

## 2. Algebraic singular locus
F=0 implies d^2=16(x^2+y^2). Together with Fw=16xy, it forces xy=0.

## 3. Check against the physical eigenvalue equation for d>0
On x=0, the component equations imply u=w=0 and z=4y/d. Then delta=-16y^2/d and d=4-delta, so d^2-4d-16y^2=0. If F=0 on x=0, d^2=16y^2, substitution gives -4d=0, contradicting d>0.

On y=0, the component equations imply u=4x/d and w=z=0. Then delta=-16x^2/d and again d^2-4d-16x^2=0. If F=0 on y=0, d^2=16x^2, substitution again gives -4d=0, contradicting d>0.

Hence no physical solution with d>0 satisfies F=0, using the stated equations. This excludes a denominator singularity on this eigenbranch wherever d remains positive, without yet proving global existence/continuity of the branch.

## 4. Sign of F on connected branch
At x=y=0, the low-energy branch has d=4, so F=16>0. Along any connected continuation of this branch for which d>0 and the eigenpair equations hold, F cannot cross zero by Section 3. Thus F remains positive on that connected continuation.

This is a conditional branch-continuation statement, not a theorem that the continuation exists globally or stays d>0.

## 5. Caveats
- Algebraic reduction and singular-set contradiction are derived from the listed equations.
- No Lean proof or independent audit.
- The argument is conditional on correct correspondence between matrix, eigenvector equations, and d=4-delta.
- No global eigenvalue/eigenvector continuation, uniqueness, or entropy positivity is claimed.
