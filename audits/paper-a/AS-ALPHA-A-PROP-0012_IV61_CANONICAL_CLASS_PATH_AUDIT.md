# IV-61 — Canonical Class-by-Class Path Audit

## Scope
This audit independently re-enumerates the four-operation edge multiset space on eight labeled vertices, groups configurations into weighted-support canonical classes, and accumulates sequence/intermediate-state bookkeeping class-by-class.

## Executed totals
- Vertex pool: 8; available unordered pair edges: 28.
- Four-edge multisets: 31,465.
- Weighted-support canonical classes: 23.
- Unique ordered sequences across all multiset configurations: 614,656.
- Orders returning to the vacuum at intermediate step 2 or 3: 31,360.

## Per-class ledger (class number follows deterministic signature sort)
|Class|Represented multisets|Ordered sequences|Vacuum returns (step 2/3)|Representative edge multiset|
|---:|---:|---:|---:|---|
|1|105|2,520|0|01, 23, 45, 67|
|2|1,260|15,120|2,520|01×2, 23, 45|
|3|2,520|60,480|0|01, 02, 34, 56|
|4|420|1,680|840|01×3, 23|
|5|560|13,440|3,360|01, 02, 12, 34|
|6|3,360|40,320|6,720|01×2, 02, 34|
|7|1,680|40,320|0|01, 02, 03, 45|
|8|5,040|120,960|0|01, 02, 13, 45|
|9|210|1,260|420|01×2, 23×2|
|10|1,680|20,160|3,360|01×2, 23, 24|
|11|28|28|28|01×4|
|12|2,520|60,480|0|01, 02, 34, 35|
|13|168|2,016|1,344|01×2, 02, 12|
|14|336|1,344|672|01×3, 02|
|15|168|1,008|336|01×2, 02×2|
|16|840|20,160|5,040|01, 02, 03, 12|
|17|840|10,080|1,680|01×2, 02, 03|
|18|210|5,040|0|01, 02, 13, 23|
|19|1,680|20,160|3,360|01×2, 02, 23|
|20|840|10,080|1,680|01×2, 02, 13|
|21|280|6,720|0|01, 02, 03, 04|
|22|3,360|80,640|0|01, 02, 03, 14|
|23|3,360|80,640|0|01, 02, 13, 24|

The sum across the class ledger agrees with the exhaustive totals above.

## Interpretation and limitations
- The class aggregates distinguish edge-multiset configurations from their distinct orderings.
- Vacuum-return counts flag sequences requiring reducible-path/normalization treatment; they are not subtracted or corrected here.
- Intermediate flip cardinality and energy denominators are retained as bookkeeping obligations for the next audit, not evaluated as full perturbative amplitudes.
- No coupling weights, signs, amplitude interference, normalized density matrix, entropy, or B−C response is computed.

**Paper A status: OPEN / ANALYTIC-PARTIAL / NOT VERIFIED.** No Lean proof or proposition-level verification is claimed.
