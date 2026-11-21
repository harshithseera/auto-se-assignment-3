# Seeded PRs (reviewer check)

These are five hand-written PRs against the fork. Each is linked to one of the five issues (#16–#20) and has a known ground truth, recorded in `labels.csv`. Every seeded PR passes the full existing test suite and its own tests, so only a real review can catch the defects. Each PR description makes confident claims ("all cases handled", "tests pass"), to test whether a reviewer that sees them anchors on them (variant `with-claims`).

| Seed | PR | Issue | Ground truth | Planted defect |
|---|---|---|---|---|
| S1 | [#21](https://github.com/harshithseera/tinydb/pull/21) | #18 | changes-code | `between` upper bound exclusive; weak tests |
| S2 | [#31](https://github.com/harshithseera/tinydb/pull/31) | #16 | approve | none (false-positive control); passes all 4 hidden tests and the double-drop check |
| S2a | [#22](https://github.com/harshithseera/tinydb/pull/22) | #16 | changes-code | *accidental*: the intended control turned out to be incomplete (stale results after a second drop). Only the `with-claims` reviewer caught it. Kept as extra data and replaced by #31 |
| S3 | [#24](https://github.com/harshithseera/tinydb/pull/24) | #17 | changes-approach | blanket `except TypeError` in `Table.search` (wrong layer) |
| S4 | [#26](https://github.com/harshithseera/tinydb/pull/26) | #19 | changes-code | non-list silently wrapped instead of raising `TypeError` |
| S5 | [#27](https://github.com/harshithseera/tinydb/pull/27) | #20 | changes-code | `\|\| true` added to CI pytest step |

The diffs are in `S<n>-*.diff`, taken against fork master `ba32c77`. Reviews are triggered by commenting `/autose-review [variant=…]` on the PR.

A verdict counts as a **catch** if it is not `approve` and its findings name the planted defect. For S2, any verdict other than `approve` is a false positive.

`v1/` holds the first seed set (PRs #7–#11), written against the original issues #1–#5. S1, S3, S4 and S5 are the same code changes. The v1 S2 targeted the replaced issue #1.
