# Paper A — Source Authority Reconciliation Record

**Status:** OPEN DECISION / NO UPSTREAM CHANGE AUTHORIZED  
**Frozen upstream commit:** `8deb7de4a49cb2060720246b7101820ee7e08c91`

## What the frozen manifest says

The Constant Llpoy source manifest v0.2.3 designates six revised section files as authoritative. It labels `Arxiv/paper_01_manuscript.md` as an integrated cross-check only. The claims ledger is secondary.

## What the frozen build does

The frozen generator `code/md_to_arxiv_tex.py` calls:

```python
build("paper_01", "paper_01_manuscript.md")
```

It reads that Markdown file and writes `Arxiv/paper_01.tex`. Therefore the generated TeX does not directly consume the six section files.

## Observed content divergence

Sections 1, 2, 3, and 6 in the integrated Markdown are the corresponding revised sections plus claim-status tags. Section 5 is substantially formatting-normalized and has claim-status tags. Section 4 is materially different:

- Revised Section 4 contains stronger strong-coupling function and derivative expansions, a mismatched Lemma 5.1 citation, and a weak-coupling/opposite-sign statement referring to Lemma 5.2.
- Integrated Markdown Section 4 uses a weaker conditional (O(x^{-2})) derivative statement, explicitly says the endpoint limit alone does not imply derivative decay, cites Kato for the perturbative framework, and removes the opposite-sign phrase.

The integrated Markdown is not the manifest-authoritative source, so its more cautious wording does not automatically replace the revised Section 4. Conversely, the revised Section 4 cannot be accepted without resolving the known proof/citation defects.

## Decision gate

No choice is made here between:

A. promoting the integrated Markdown to canonical authority after a complete six-section reconciliation and a new manifest version; or

B. changing the build system to assemble the six authoritative sections deterministically into a publication source and generating TeX from that source.

The user/research owner must authorize any upstream change. Until a source-policy decision is recorded, Constant Llpoy must preserve both source states and label all proposed changes as working copies.

## Immediate operational rule

Do not regenerate or submit the upstream TeX as if it represented the six manifest-authoritative sections. Do not merge the previous partial Sections 2–5 assembly into upstream. Continue proposed corrections only on the Constant Llpoy working branch.
