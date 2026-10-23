# AI Code Review Benchmark Lab

An inspectable rubric for reviewing coding solutions against explicit behavioral requirements.

[Guia em português](README.pt-BR.md) · [Architecture and tradeoffs](ARCHITECTURE.md)

## Run locally

Python 3.11+; standard library only.

```sh
python -m unittest -v
python benchmark.py
```

## How it works

```text
specifications → weighted cases → built-in candidates → deterministic JSON report
```

The lab contains two original candidate sets: a reference implementation and a plausible but incorrect implementation. Thirteen fixtures cover interval merging, tenant-scoped event deduplication and integer monetary totals. Each case exposes its weight, pass/fail outcome and exception type.

Rubric v1 uses weight 1 for basic behavior, 2 for ordering/nesting correctness, and 3 for tenant isolation. Scores are the sum of passed weights, not a subjective model judgment. Inputs are copied before each invocation. Candidate selection is an allowlist, so the CLI never loads arbitrary submissions.

Task contracts: intervals are closed and touching endpoints merge; intervals are valid pairs with start ≤ end. Events retain the first arrival for each (tenant,id). Totals include settled rows for the requested tenant and allow negative refund amounts. See `CASES` for all fixtures.

## Verification

Five harness tests verify complete reference coverage, detection of deliberate defects, deterministic serialization, allowlisted candidates and task coverage. The report executes 13 weighted cases per candidate.

## Scope and limitations

This is an evaluation-design demonstration, not a comparison of commercial AI models. Both candidates and fixtures were authored for this repository with AI assistance. The reference passes by construction; its score is not independent evidence of model quality. Fixed fixtures do not prove general correctness. Do not run untrusted candidate code in this process; there is no sandbox. No model API, paid service or assessment material is used.

## Provenance

This is an original portfolio demonstration created for Douglas Chiodi with AI assistance. All fixtures, identities, identifiers, amounts and examples are synthetic. No customer code, production configuration, credentials, proprietary assets or existing repository history are included. It does not claim deployment experience or business outcomes from these sample applications.

MIT applies to the original source in this repository; third-party dependencies retain their own licenses.

## Portfolio

- [Durable Job Queue](https://github.com/douglaschiodi/python-durable-job-queue)
- [SQL Reconciliation Lab](https://github.com/douglaschiodi/sql-reconciliation-lab)
- [Tenant Access Demo](https://github.com/douglaschiodi/typescript-tenant-access-demo)
- [Reliable Webhooks Lab](https://github.com/douglaschiodi/dotnet-reliable-webhooks)
