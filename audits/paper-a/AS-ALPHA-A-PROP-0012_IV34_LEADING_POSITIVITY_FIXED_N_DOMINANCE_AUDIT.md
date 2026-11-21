# IV-34 — Leading-Term Positivity and Fixed-N Asymptotic Dominance Audit

**Target:** AS-ALPHA-A-PROP-0012 candidate \(B-C\)  
**Status:** OPEN / ANALYTIC-PARTIAL / NOT VERIFIED  
**Scope:** Determine the sign of the candidate logarithmic coefficient for fixed \(N\ge4\) and state the precise conditional asymptotic-dominance implication, without pretending the remainder is already proven.

## 1. Leading coefficient positivity

The corrected candidate from IV-31/32 is
\[
c_N=\ln\frac{2(N-2)}{N-1}.
\]
For \(N\ge4\),
\[
\frac{2(N-2)}{N-1}=2-\frac{2}{N-1}\ge\frac43>1,
\]
hence
\[
c_N\ge\ln(4/3)>0.
\]
Also \(c_N\to\ln2\) as \(N\to\infty\). Thus the displayed leading coefficient is strictly positive for the stated range.

## 2. Conditional sign dominance

Suppose the candidate asymptotic were rigorously established in the form
\[
B-C=\frac{J}{8h^2}c_N+R_N(J,h),
\]
with a finite fixed-N constant \(K_N\) and
\[
|R_N|\le K_N\frac{J^2}{h^3}|\ln(J/h)|
\]
for sufficiently small \(r=J/h>0\). Then
\[
B-C\ge\frac{J}{8h^2}c_N
-K_N\frac{J^2}{h^3}|\ln r|.
\]
For any fixed \(N\ge4\), because \(r|\ln r|\to0\) as \(r\downarrow0\), there exists a threshold \(r_N>0\) such that whenever \(0<r<r_N\), the remainder is smaller than half the positive leading term, implying \(B-C>0\).

For example, the sufficient condition
\[
K_Nr|\ln r|<\frac{c_N}{16}
\]
is adequate for the displayed remainder/leading scales (and can be tightened/adjusted depending on the exact constants in the asymptotic statement).

## 3. What this audit does and does not prove

- Positivity of the algebraic candidate \(c_N\): **PASS**.
- Fixed-N asymptotic sign-dominance logic: **PASS, conditional on a valid remainder theorem**.
- Existence of a concrete threshold \(r_N\) from actual remainder constants: **OPEN**.
- The needed remainder estimate for the exact entropy expression: **OPEN**.
- Proposition itself: **NOT VERIFIED**.
- Lean formalization/build: **NOT PERFORMED**.

The coefficient positivity cannot substitute for proving the asymptotic expansion. PROP-0012 remains **OPEN / ANALYTIC-PARTIAL / NOT VERIFIED**.

## 4. Next

IV-35: **Candidate Formula Provenance and Version-Consistency Audit** — trace every appearance of the old \(+1\) coefficient, the corrected logarithmic candidate, and the remainder statement; identify stale statements that must be marked superseded so no downstream paper text silently uses the wrong coefficient.
