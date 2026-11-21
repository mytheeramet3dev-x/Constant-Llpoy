# Paper A Audit — Global branch-domain qualification (Section 4.4.3)

**Audit ID:** AS-ALPHA-A-PROP-0015  
**Frozen source:** Paper A Section 4.4.3 and Section 3.3–3.4, source commit \`8deb7de4a49cb2060720246b7101820ee7e08c91\`.

## Claim under review

The manuscript states that \(x_*(\gamma)\ge x_c\) is established for the upper local branch near \(\gamma=1\), while extension to all \(\gamma\ge1\) requires a global continuation assumption excluding reversing turning points or branch exchanges. It also identifies \(0<x<x_c\) as locally unstable near the saddle-node and states distinct/opposite-sign response characteristics.

## Findings

### A. Local branch-domain inequality — CONDITIONAL PASS

From the local saddle-node analysis in Section 3.2–3.3, with \(\mathcal G_N''(x_c)<0\) and supercritical parameter \(\gamma>1\) sufficiently close to 1, the two local roots satisfy
\[
x_\pm-x_c=\pm C\sqrt{\gamma-1}+O(\gamma-1),\quad C>0.
\]
Thus the upper local root satisfies \(x_+>x_c\) in a sufficiently small right-neighborhood of threshold, and the lower local root satisfies \(x_-<x_c\). This is local only and depends on the nondegeneracy/regularity conditions; the curvature remains model-specific and not verified here.

### B. Global extension — NOT PROVED; manuscript qualification is correct

The local theorem does not rule out later turning points, branch exchanges, or other global root structure. Section 4.4.3 explicitly states that extending the inequality to every \(\gamma\ge1\) requires a global continuation assumption. This is a mathematically appropriate scope qualification, not a proof of the global property. The global branch statement remains conditional/open.

### C. Local instability — CONDITIONAL PASS

Section 3.3 gives \(F_x>0\) on the lower local root near a generic saddle-node. The Picard multiplier satisfies \(T'=1+F_x/h>1\), so the lower local root is repelling for the stated iteration in that local regime. This does not establish instability for every root in the entire interval \(0<x<x_c\), absent a global sign argument.

### D. Opposite-sign response assertion — SOURCE-CONFLICT / OPEN

The response-sign statement in Section 4.4.3 cites the weak-coupling expansion in Lemma 5.2. The fresh PROP-0012 audit identified a source conflict and a corrected conditional leading sign that differs from the old derivation. Consequently, the response-sign comparison is not verified and should not be used as support for the branch-domain inequality.

## Verdict

**PARTIAL — local branch-domain and local instability implications are conditionally sound; global extension is explicitly assumption-dependent and remains unproved; response-sign assertion remains conflicted.**

No numerical scan, independent global continuation, or Lean build was run in this audit.
