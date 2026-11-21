# Stress issues (failure-path runs)

Three extra issues, separate from the five experiment issues, to exercise the failure paths the five never hit: stage-1 stop, the test→implement retry, the return to design, and the review/fix loop. Results are reported whatever happens; nothing is forced.

| ID | Intent | Hidden tests |
|---|---|---|
| X1 | Genuinely vague ("make it faster"), so it is likely to stop at stage 1 | none (expected outcome: a stop with an explanation) |
| X2 | Nested-field update operations (medium) | `hidden_tests/test_stress_nested_fields.py` (from A2 T2) |
| X3 | `TinyDB.batch()` across tables and storages (hard, touches several components) | `hidden_tests/test_stress_batch.py` (from A2 T3) |

The hidden tests are reused unchanged from my A2 acceptance tests. On `edff96a`, 7 of them fail and 1 passes (a regression guard for plain string fields).
