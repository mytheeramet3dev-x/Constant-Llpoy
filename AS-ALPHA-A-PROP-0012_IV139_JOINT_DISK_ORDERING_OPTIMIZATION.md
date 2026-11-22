# AS-ALPHA-A-PROP-0012 — IV-139: Joint Disk Optimization of the Exact Ordering Criterion

Status: ANALYTIC; exact optimization of the stated conservative criterion; NOT LEAN-FORMALIZED.

## 1. Criterion
From IV-135, sufficient ordering is
g(d)=d^2-4d|y|-16x^2>0,
provided d>2|y| and d^2-16x^2>0.

## 2. Improved d lower bound
The Rayleigh bound lambda<=-3 gives d=1-lambda>=4.

## 3. Joint optimization on a disk
For rho<=R and R<1/2, set Y=|y|. Then x^2<=R^2-Y^2 and
Y+x^2<=Y+R^2-Y^2.
The derivative in Y is 1-2Y>0 for 0<=Y<=R<1/2, so the maximum occurs at Y=R, x=0, and
Y+x^2<=R.
Consequently,
g(d)>=g(4)=16-16Y-16x^2>=16(1-R)>0.
This improves IV-138's less sharp disk estimate 16(1-R-R^2), without changing the currently entropy-certified radius R<1/2.

## 4. Denominator prerequisites
For R<1/2, d>=4>2|y| and
d^2-16x^2>=16-16R^2>0.
Thus the prerequisites of the ratio criterion hold.

## 5. Scope
This is sharp for maximizing Y+x^2 on the disk in the regime R<1/2, not a sharpness theorem for the original entropy proposition. It does not improve the entropy/resolvent bottleneck. Analytical, not Lean formalized; branch/source reconciliation remains open.
