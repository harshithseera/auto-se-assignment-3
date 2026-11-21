# Runs

Every Actions run, PR and review in the fork [harshithseera/tinydb](https://github.com/harshithseera/tinydb). All runs are real; numbers in `results.csv`.

## Issue runs (full pipeline, label `autose`)

| Issue | Type | Actions run | PR | Review | Artifacts | Hidden tests |
|---|---|---|---|---|---|---|
| [#1](https://github.com/harshithseera/tinydb/issues/1) | bug | [44856860179](https://github.com/harshithseera/tinydb/actions/runs/44856860179) | [#15](https://github.com/harshithseera/tinydb/pull/15) | [approve](https://github.com/harshithseera/tinydb/pull/15#issuecomment-7056075453) | [.autose/issue-1](https://github.com/harshithseera/tinydb/tree/autose/issue-1/.autose/issue-1) | 4/4 |
| [#2](https://github.com/harshithseera/tinydb/issues/2) | bug | [44856863771](https://github.com/harshithseera/tinydb/actions/runs/44856863771) | [#12](https://github.com/harshithseera/tinydb/pull/12) | [approve](https://github.com/harshithseera/tinydb/pull/12#issuecomment-7056068234) | [.autose/issue-2](https://github.com/harshithseera/tinydb/tree/autose/issue-2/.autose/issue-2) | 4/4 |
| [#3](https://github.com/harshithseera/tinydb/issues/3) | feature | [44856868047](https://github.com/harshithseera/tinydb/actions/runs/44856868047) | [#14](https://github.com/harshithseera/tinydb/pull/14) | [approve](https://github.com/harshithseera/tinydb/pull/14#issuecomment-7056070345) | [.autose/issue-3](https://github.com/harshithseera/tinydb/tree/autose/issue-3/.autose/issue-3) | 4/4 |
| [#4](https://github.com/harshithseera/tinydb/issues/4) | feature | [44856522407](https://github.com/harshithseera/tinydb/actions/runs/44856522407) | [#6](https://github.com/harshithseera/tinydb/pull/6) | [approve](https://github.com/harshithseera/tinydb/pull/6#issuecomment-7056022487) | [.autose/issue-4](https://github.com/harshithseera/tinydb/tree/autose/issue-4/.autose/issue-4) | 4/4 |
| [#5](https://github.com/harshithseera/tinydb/issues/5) | vague | [44856873073](https://github.com/harshithseera/tinydb/actions/runs/44856873073) | [#13](https://github.com/harshithseera/tinydb/pull/13) | [approve](https://github.com/harshithseera/tinydb/pull/13#issuecomment-7056067949) | [.autose/issue-5](https://github.com/harshithseera/tinydb/tree/autose/issue-5/.autose/issue-5) | 3/4 |

Issue #4 was the first (smoke-test) run on workflow commit `c74af16`; #1, #2, #3, #5 ran on `9d053fd` (prompt fixes after #4, see fork history). No run needed a fix round (all approved in round 1), so `fix-1`/`ci-2`/`review-2` were skipped in every run.

## Seeded PR reviews (`/autose-review`, experiments)

| Seed | PR | Ground truth | Variant | Verdict | Actions run | Review |
|---|---|---|---|---|---|---|
| S1 | [#7](https://github.com/harshithseera/tinydb/pull/7) | changes-code | default | changes-code | [44856950879](https://github.com/harshithseera/tinydb/actions/runs/44856950879) | [comment](https://github.com/harshithseera/tinydb/pull/7#issuecomment-7056060620) |
| S1 | [#7](https://github.com/harshithseera/tinydb/pull/7) | changes-code | with-claims | changes-code | [44857036098](https://github.com/harshithseera/tinydb/actions/runs/44857036098) | [comment](https://github.com/harshithseera/tinydb/pull/7#issuecomment-7056075106) |
| S1 | [#7](https://github.com/harshithseera/tinydb/pull/7) | changes-code | plain | changes-code | [44857038856](https://github.com/harshithseera/tinydb/actions/runs/44857038856) | [comment](https://github.com/harshithseera/tinydb/pull/7#issuecomment-7056082528) |
| S2 | [#8](https://github.com/harshithseera/tinydb/pull/8) | approve | default | approve | [44856951260](https://github.com/harshithseera/tinydb/actions/runs/44856951260) | [comment](https://github.com/harshithseera/tinydb/pull/8#issuecomment-7056061897) |
| S2 | [#8](https://github.com/harshithseera/tinydb/pull/8) | approve | with-claims | approve | [44857041315](https://github.com/harshithseera/tinydb/actions/runs/44857041315) | [comment](https://github.com/harshithseera/tinydb/pull/8#issuecomment-7056075147) |
| S2 | [#8](https://github.com/harshithseera/tinydb/pull/8) | approve | plain | approve | [44857042844](https://github.com/harshithseera/tinydb/actions/runs/44857042844) | [comment](https://github.com/harshithseera/tinydb/pull/8#issuecomment-7056081333) |
| S3 | [#9](https://github.com/harshithseera/tinydb/pull/9) | changes-approach | default | changes-approach | [44856954408](https://github.com/harshithseera/tinydb/actions/runs/44856954408) | [comment](https://github.com/harshithseera/tinydb/pull/9#issuecomment-7056062649) |
| S3 | [#9](https://github.com/harshithseera/tinydb/pull/9) | changes-approach | with-claims | changes-code ❌ | [44857045788](https://github.com/harshithseera/tinydb/actions/runs/44857045788) | [comment](https://github.com/harshithseera/tinydb/pull/9#issuecomment-7056078176) |
| S3 | [#9](https://github.com/harshithseera/tinydb/pull/9) | changes-approach | plain | changes-approach | [44857047800](https://github.com/harshithseera/tinydb/actions/runs/44857047800) | [comment](https://github.com/harshithseera/tinydb/pull/9#issuecomment-7056086542) |
| S4 | [#10](https://github.com/harshithseera/tinydb/pull/10) | changes-code | default | changes-code | [44856956163](https://github.com/harshithseera/tinydb/actions/runs/44856956163) | [comment](https://github.com/harshithseera/tinydb/pull/10#issuecomment-7056059889) |
| S4 | [#10](https://github.com/harshithseera/tinydb/pull/10) | changes-code | with-claims | changes-code | [44857049905](https://github.com/harshithseera/tinydb/actions/runs/44857049905) | [comment](https://github.com/harshithseera/tinydb/pull/10#issuecomment-7056073514) |
| S4 | [#10](https://github.com/harshithseera/tinydb/pull/10) | changes-code | plain | changes-code | [44857052648](https://github.com/harshithseera/tinydb/actions/runs/44857052648) | [comment](https://github.com/harshithseera/tinydb/pull/10#issuecomment-7056078555) |
| S5 | [#11](https://github.com/harshithseera/tinydb/pull/11) | changes-code | default | changes-code | [44856958437](https://github.com/harshithseera/tinydb/actions/runs/44856958437) | [comment](https://github.com/harshithseera/tinydb/pull/11#issuecomment-7056062295) |
| S5 | [#11](https://github.com/harshithseera/tinydb/pull/11) | changes-code | with-claims | changes-code | [44857054591](https://github.com/harshithseera/tinydb/actions/runs/44857054591) | [comment](https://github.com/harshithseera/tinydb/pull/11#issuecomment-7056074752) |
| S5 | [#11](https://github.com/harshithseera/tinydb/pull/11) | changes-code | plain | changes-code | [44857056767](https://github.com/harshithseera/tinydb/actions/runs/44857056767) | [comment](https://github.com/harshithseera/tinydb/pull/11#issuecomment-7056082959) |

## Excluded runs

- Five `autose` runs failed at the `gate` job (runs 44856950970, 44856951325, 44856954483, 44856956094, 44856958451): the first `/autose-review` comments also matched the `/autose` prefix of the main workflow; the gate rejected them because the seeded branches are not `autose/issue-N`. Fixed in fork commit `7b5bf11` (ADR-011). No agent ran.
- `autose-ci` runs with status `action_required` on bot-opened PRs (#12–#15): GitHub holds `pull_request` runs for PRs created by `github-actions[bot]`. The stage-5 check uses the `workflow_call` CI job inside the `autose` run instead (ADR-007).

## Token use

Total across all 40 agent calls: **1,475,485 input tokens (incl. cache reads/writes) and 48,622 output tokens**. Per-call logs: `.autose/issue-N/usage.jsonl` on each branch, and the usage line of every review comment. Cost cap: Claude Pro flat subscription, no API billing (ADR-006).
