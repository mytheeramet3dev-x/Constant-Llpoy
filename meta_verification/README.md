# Meta-verification harness

## Policy evaluator
`status_evaluator.py` checks schema completeness, revision binding, obligation coverage,
and SHA-256 consistency of embedded artifact bytes. It is not a proof checker or authenticity oracle.

## GitHub Actions run evidence collector
`github_run_collector.py` queries GitHub REST API over HTTPS using a read-only
`GITHUB_TOKEN`. It binds the upstream run to the triggering event's run ID and
head commit, then checks repository, branch, event, workflow ID/path, pinned
workflow-file and evaluator-file blob SHAs, exact job set, required steps, and
completion conclusions. It emits a normalized JSON record with a deterministic
SHA-256 digest.

A separate `workflow_run` workflow runs after the upstream workflow completes;
it checks out the default-branch collector and does not execute the upstream
commit. Fork-originated runs and pull-request events are excluded by policy.

This is **not cryptographic attestation verification**. HTTPS authenticates the
API connection, but the resulting record is not digitally signed. Its digest
detects alteration only if retained through a separately trusted channel.
A repository administrator or compromised workflow/policy can still undermine
the process. A future stage must verify a GitHub-issued signed provenance
statement against independently governed identity and source policy.

## Tests
```sh
python -m unittest discover -s meta_verification -p 'test_*.py' -v
```
Tests use fixed API-response fixtures and do not contact GitHub. Neither component
verifies mathematical proof semantics or establishes that the verification system
is free from defects.
