# IV-187 — Dependency-Aware Radial Derivative Bound for P_u + P_z

**Project:** Absolute Symmetry — Paper A  
**Proposition:** AS-ALPHA-A-PROP-0012  
**Status:** Conditional analytic estimate; inherited root/domain premises remain unverified.

## 1. Joint identity from IV-186
Let \(a=d^2\), \(x=2p-1\), and
\[
B=pA^2+(1-p)G^2=a^2+x^2(256t^2-32at).
\]
Then \(P_{pair}=P_u+P_z=16HB\), where \(H=1/(d^2F^2)\).

## 2. Radial derivative
\[
B_t=2aa_t+x^2(512t-32a_t t-32a),\quad a_t=2dd_t.
\]
For a conservative absolute-value enclosure, use \(a\le a_*=(256/63)^2\), \(|a_t|\le a_{t,*}=2(256/63)(4.194)\), \(|x|\le1\), \(t\le1/64\):
\[
|B_t|\le2a_*a_{t,*}+512t_*+32a_{t,*}t_*+32a_*<1679.031943.
\]
Also \(0\le B\le a_*^2\) (the upper bound follows from the nonpositive correction because \(a\ge16>8t\)), and use \(H\le1/3969\), \(|H_t|<0.002131\).
Therefore
\[
|(P_{pair})_t|\le16(|B_t|H+B|H_t|)<16.064690910,
\]
rounded upward:
\[
\boxed{|(P_u+P_z)_t|<16.064691}.
\]

## 3. Aggregate S radial derivative
From IV-180, \(|(P_w)_t|<1.134551908\). Hence
\[
|S_t|<16.064690910+1.134551908=17.199242818,
\]
rounded upward:
\[
\boxed{|S_t|<17.199243}.
\]
This is a modest improvement over IV-185's dependency-aware \(|S_t|<17.482869921\), and a substantial improvement over the earlier independent component sum.

## 4. Arithmetic / scope notes
All displayed ceilings are rounded upward. The derivative enclosure intentionally uses triangle inequalities and is not claimed sharp. It assumes the IV-175/179 conditional bounds, the inherited domain \(d\in[4,256/63]\), \(F\ge63/4\), \(t\le1/64\), and the component formulas. The joint identity itself is exact. This record does not update angular derivatives, normalized-vector Lipschitz constants, or prove root existence/uniqueness or \(R_d\le0\).
