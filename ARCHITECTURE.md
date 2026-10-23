# Architecture and tradeoffs

## Data flow

```text
specifications → weighted cases → built-in candidates → deterministic JSON report
```

The lab contains two original candidate sets: a reference implementation and a plausible but incorrect implementation. Thirteen fixtures cover interval merging, tenant-scoped event deduplication and integer monetary totals. Each case exposes its weight, pass/fail outcome and exception type.

Rubric v1 uses weight 1 for basic behavior, 2 for ordering/nesting correctness, and 3 for tenant isolation. Scores are the sum of passed weights, not a subjective model judgment. Inputs are copied before each invocation. Candidate selection is an allowlist, so the CLI never loads arbitrary submissions.

Task contracts: intervals are closed and touching endpoints merge; intervals are valid pairs with start ≤ end. Events retain the first arrival for each (tenant,id). Totals include settled rows for the requested tenant and allow negative refund amounts. See `CASES` for all fixtures.

## Why this shape

The repository keeps a small, inspectable core and exercises behavior through real storage or HTTP where applicable. No service account, customer environment or paid API is required.

## Boundaries

This is an evaluation-design demonstration, not a comparison of commercial AI models. Both candidates and fixtures were authored for this repository with AI assistance. The reference passes by construction; its score is not independent evidence of model quality. Fixed fixtures do not prove general correctness. Do not run untrusted candidate code in this process; there is no sandbox. No model API, paid service or assessment material is used.

## Test strategy

Five harness tests verify complete reference coverage, detection of deliberate defects, deterministic serialization, allowlisted candidates and task coverage. The report executes 13 weighted cases per candidate.

Tests exercise behavior and failure cases; they do not certify readiness for production. Synthetic examples are intentionally small enough to review in one sitting.
