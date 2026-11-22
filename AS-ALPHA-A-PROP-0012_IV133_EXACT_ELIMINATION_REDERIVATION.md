# AS-ALPHA-A-PROP-0012 — IV-133: Independent Structural Re-Derivation by Exact Elimination

Status: ANALYTIC IDENTITY AND RATIONAL LOCAL BOUNDS; NOT LEAN-FORMALIZED; source definitions remain to be reconciled.

## 1. Exact elimination
The equations are
d u - 4y w = 4x,
d w - 4y u - 4x z = 0,
d z - 4x w = 4y.

Solving the first and third equations for u,z and substituting into the second gives the exact identity
w = 16xy / [d^2 - 16(x^2+y^2)],
provided the denominator is nonzero.

Substitution back gives
u = (4x/d) [d^2-16x^2]/[d^2-16(x^2+y^2)],
z = (4y/d) [d^2-16y^2]/[d^2-16(x^2+y^2)].

For x != 0, divide the exact expressions:
w/u = 4dy/[d^2-16x^2].

## 2. Exact rational positivity on r=1/1000
IV-129 gives d in [499/125,501/125]. For |x|,|y|<=r:
d^2 -16(x^2+y^2) >= (499/125)^2 -32r^2 = 498001/31250 > 0,
so elimination denominator is strictly positive.

For x != 0:
|w/u| <= [4(501/125)r]/[(499/125)^2-16r^2]
= 334/332001 ≈ 0.0010060210662016077 < 1.
Therefore u^2>w^2, independently of IV-130's iterative component-estimate chain.

## 3. Conservative component bounds for entropy
Using the exact eliminated forms and conservative bounds:
|u| <= C|x|, |z| <= C|y|,
where C = 251001000/248502499 ≈ 1.0100542288711551.
Also |w| <= 16r^2/[(499/125)^2-32r^2] = 1/996002 ≈ 1.004014048164562e-6.

With D>=1:
q <= 2C^2r^2 = 126003004002/61753492009245001 ≈ 2.040419090521008e-6 < 1/2,
q_3 <= C^2r^2 + (1/996002)^2 = 252006257005/247013968036980004 ≈ 1.0202105533047127e-6 < 1/2.

Thus, under the stated q,q3 definitions, for x!=0 we get q3<q<1/2, and binary-entropy monotonicity gives ΔS>0.

## 4. Equality axis
At x=0, the exact expressions yield u=w=0 and z=4y/d; hence q=q3 and ΔS=0. Thus within the box, the local equality set is exactly x=0, conditional on matching the source proposition's definitions and branch.

## 5. What is genuinely independent?
This proof does not rely on IV-130's recursive C_w/C_u component-bound chain. It uses direct elimination and the closed-form ratio w/u. It still relies on the same matrix equations and IV-129 spectral d-range, so it is not fully independent of the foundational assumptions.

## Caveats
No Lean formalization or external independent audit has been completed. This remains a local result on |x|,|y|<=1/1000 only.
