# AS-ALPHA-A-PROP-0012 — IV-135: Exact Positivity Criterion and Domain Optimization

Status: ANALYTIC DOMAIN CRITERION; no enlarged theorem domain claimed; NOT LEAN-FORMALIZED.

## 1. Exact criterion from the ratio
From the eliminated formulas, for x != 0 and nonzero denominators:
w/u = 4dy/(d^2-16x^2).
Thus u^2>w^2 follows exactly if
d^2-16x^2-4d|y|>0,
provided d>0 and d^2-16x^2>0.

Equivalent completed-square form:
(d-2|y|)^2 > 4y^2+16x^2.
If d>2|y|, this is equivalent to
d > 2|y| + 4 sqrt(x^2+y^2).

## 2. Explicit sufficient domain using the existing local spectral bound
The IV-129 spectral estimate only certifies d>=d0=499/125 on the original box |x|,|y|<=1/1000. It cannot be used globally without a new spectral estimate.

Within that original box, a conservative sufficient criterion is
16x^2 + 4d0|y| < d0^2,
where d0=499/125.
Indeed, d^2-4d|y|-16x^2 is increasing in d when d>2|y|, and the displayed domain implies d0>2|y|. Hence replacing d by d0 gives a positive lower bound for the ratio criterion. This explicit domain is an auxiliary sufficient condition; it is not a new certified larger domain because the validity of d>=d0 is still tied to the original box.

## 3. Boundary cases
The ratio argument is for x != 0. On x=0, the exact axis analysis gives u=w=0 and q=q3, hence entropy equality. Do not use the ratio formula at x=0.

## 4. Domain-expansion limitation
The exact criterion itself is potentially useful beyond the small box, but extending its certified domain requires an independent lower bound for d on the candidate region, or a self-consistent eigenvalue analysis. No enlarged domain is claimed here.

## 5. Proof status
Exact algebraic criterion derived. Local sufficient condition recorded. No Lean proof or independent external audit. Original Proposition definitions/branch still require reconciliation.
