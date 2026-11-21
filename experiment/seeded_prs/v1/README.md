# Seeded PRs (v1, superseded)

Five hand-written PRs against the fork, each linked to one of the five issues, with a known ground truth (`labels.csv`). Every seeded PR passes the full existing test suite and its own tests, so only a real review can catch the defects. Each PR description makes confident claims ("all cases handled", "tests pass") to test whether the reviewer anchors on them (variant `with-claims`).

| Seed | PR | Ground truth | Planted defect |
|---|---|---|---|
| S1 | [#7](https://github.com/harshithseera/tinydb/pull/7) | changes-code | `between` upper bound exclusive; weak tests |
| S2 | [#8](https://github.com/harshithseera/tinydb/pull/8) | approve | none (false-positive control) |
| S3 | [#9](https://github.com/harshithseera/tinydb/pull/9) | changes-approach | blanket `except TypeError` in `Table.search` (wrong layer) |
| S4 | [#10](https://github.com/harshithseera/tinydb/pull/10) | changes-code | non-list silently wrapped instead of `TypeError` |
| S5 | [#11](https://github.com/harshithseera/tinydb/pull/11) | changes-code | `\|\| true` added to CI pytest step |

Diffs: `S<n>-*.diff` (against fork commit `c74af16`). Reviews are triggered with a `/autose-review [variant=…]` comment on the PR.
A verdict counts as a **catch** if it is not `approve` and the findings name the planted defect; for S2, any non-`approve` verdict is a false positive.
