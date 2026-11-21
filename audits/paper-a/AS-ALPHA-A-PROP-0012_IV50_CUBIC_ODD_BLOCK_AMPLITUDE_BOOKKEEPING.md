# IV-50 — Cubic Odd-Block Amplitude Bookkeeping

**Status:** STRUCTURAL DERIVATION / COEFFICIENTS OPEN / NOT VERIFIED  
**Target:** Paper A PROP-0012, odd two-site block for retained sites 1,2  
**No Lean or numerical verification claimed.**

## 1. Configuration-resolved expansion

For odd-block retained states alpha in {+-, -+}, the x-basis environment configurations e must have odd flipped parity so the total configuration has even parity. Write the configuration-resolved amplitudes as
c_(alpha,e)(r)=r a_(alpha,e)+r^2 b_(alpha,e)+O(r^3)
for configurations with a first-order contribution, and c_(alpha,e)=r^2 b_(alpha,e)+O(r^3) for configurations first appearing at second order. These are formal coefficient definitions, not evaluated amplitudes.

The reduced odd block is O_(alpha,beta)=sum_e c_(alpha,e) conjugate(c_(beta,e)). Therefore the cubic coefficient for a real-coupling, real-state expansion is
O^(3)_(alpha,beta)=sum_e [a_(alpha,e)b_(beta,e)+b_(alpha,e)a_(beta,e)]
over environment configurations whose amplitudes start at order r. Configurations starting at order r^2 contribute first at order r^4 to this product and do not enter the cubic coefficient. Normalization corrections to first-order amplitudes begin at order r^3 and multiply r-leading amplitudes, hence contribute at order r^4 to O, not order r^3.

## 2. Null-direction combination

For v=(1,-1)/sqrt(2), the cubic null coefficient is
B_vv=(O^(3)_11+O^(3)_22-O^(3)_12-O^(3)_21)/2.
Substitution of the configuration-sum formulas expresses it as a sum of first/second-order amplitude interferences. This expression is a valid bookkeeping identity but does not establish cancellation.

## 3. What remains to evaluate

- Explicit first-order coefficients a_(alpha,e) are known from pair-flip amplitudes g_ab.
- Explicit second-order coefficients b_(alpha,e), including all allowed intermediate pair-flip paths, must be derived with the correct energy denominators and ground-state normalization convention.
- The configuration sum for B_vv has not been evaluated; no zero/nonzero conclusion is justified.
- Edge-parameter derivatives of the sum remain unevaluated.
- Low eigenvalue order, entropy contribution, and B-C response remain OPEN.
- Lean verification: NOT PERFORMED.

## 4. Disposition

**PASS:** cubic coefficient configuration-sum bookkeeping formula, conditional on the stated analytic amplitude expansion.  
**OPEN:** actual second-order amplitudes and numerical/algebraic evaluation of the cubic null coefficient.  
PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.

## 5. Next obligation

IV-51: derive second-order pair-flip amplitudes for retained-odd/environment-odd configurations, including all shared-vertex intermediate states and energy denominators, then insert into the configuration sum. Avoid using unverified earlier amplitude claims as a substitute for rederivation.
