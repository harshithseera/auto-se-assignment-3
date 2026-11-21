# Runs

Every Actions run, PR and review in the fork [harshithseera/tinydb](https://github.com/harshithseera/tinydb). All runs are real. The numbers are in `results.csv`.

There were two rounds. **v1** used issues #1–#5 and seeds #7–#11; it is archived in `v1/`. After v1, the issue set was rewritten: the v1 bug #1 described behaviour that is documented as intended, and the texts read too much like specs. **v2** used issues #16–#20 and seeds #21–#31. Everything below is v2 unless it says otherwise.

## Issue runs (full pipeline, label `autose`, workflow commit `ba32c77`)

| Slot | Issue | Type | Actions run | PR | Review | Artifacts | Hidden tests |
|---|---|---|---|---|---|---|---|
| 01 | [#16](https://github.com/harshithseera/tinydb/issues/16) | bug | [44869473176](https://github.com/harshithseera/tinydb/actions/runs/44869473176) | [#25](https://github.com/harshithseera/tinydb/pull/25) | [approve](https://github.com/harshithseera/tinydb/pull/25#issuecomment-7057731724) | [.autose/issue-16](https://github.com/harshithseera/tinydb/tree/autose/issue-16/.autose/issue-16) | 4/4 |
| 02 | [#17](https://github.com/harshithseera/tinydb/issues/17) | bug | [44869477120](https://github.com/harshithseera/tinydb/actions/runs/44869477120) | [#28](https://github.com/harshithseera/tinydb/pull/28) | [approve](https://github.com/harshithseera/tinydb/pull/28#issuecomment-7057732682) | [.autose/issue-17](https://github.com/harshithseera/tinydb/tree/autose/issue-17/.autose/issue-17) | 4/4 |
| 03 | [#18](https://github.com/harshithseera/tinydb/issues/18) | feature | [44869479937](https://github.com/harshithseera/tinydb/actions/runs/44869479937) | [#30](https://github.com/harshithseera/tinydb/pull/30) | [approve](https://github.com/harshithseera/tinydb/pull/30#issuecomment-7057740017) | [.autose/issue-18](https://github.com/harshithseera/tinydb/tree/autose/issue-18/.autose/issue-18) | 4/4 |
| 04 | [#19](https://github.com/harshithseera/tinydb/issues/19) | feature | [44869483228](https://github.com/harshithseera/tinydb/actions/runs/44869483228) | [#23](https://github.com/harshithseera/tinydb/pull/23) | [approve](https://github.com/harshithseera/tinydb/pull/23#issuecomment-7057733822) | [.autose/issue-19](https://github.com/harshithseera/tinydb/tree/autose/issue-19/.autose/issue-19) | 4/4 |
| 05 | [#20](https://github.com/harshithseera/tinydb/issues/20) | vague | [44869486743](https://github.com/harshithseera/tinydb/actions/runs/44869486743) | [#29](https://github.com/harshithseera/tinydb/pull/29) | [approve](https://github.com/harshithseera/tinydb/pull/29#issuecomment-7057735911) | [.autose/issue-20](https://github.com/harshithseera/tinydb/tree/autose/issue-20/.autose/issue-20) | 4/4 |

No run needed a fix round: all were approved in round 1, so `fix-1`, `ci-2` and `review-2` were skipped every time. After the run on #16, we found a residual defect that neither the hidden tests nor the reviewer caught: a second drop through a kept handle still serves stale results. See seed S2a below.

## Seeded PR reviews (`/autose-review`, experiments)

| Seed | PR | Ground truth | Variant | Verdict | Actions run | Review |
|---|---|---|---|---|---|---|
| S1 | [#21](https://github.com/harshithseera/tinydb/pull/21) | changes-code | default | changes-code | [44869591031](https://github.com/harshithseera/tinydb/actions/runs/44869591031) | [comment](https://github.com/harshithseera/tinydb/pull/21#issuecomment-7057729761) |
| S1 | [#21](https://github.com/harshithseera/tinydb/pull/21) | changes-code | with-claims | changes-code | [44869593682](https://github.com/harshithseera/tinydb/actions/runs/44869593682) | [comment](https://github.com/harshithseera/tinydb/pull/21#issuecomment-7057729558) |
| S1 | [#21](https://github.com/harshithseera/tinydb/pull/21) | changes-code | plain | changes-code | [44869597366](https://github.com/harshithseera/tinydb/actions/runs/44869597366) | [comment](https://github.com/harshithseera/tinydb/pull/21#issuecomment-7057732949) |
| S2 | [#31](https://github.com/harshithseera/tinydb/pull/31) | approve | default | approve | [44869865989](https://github.com/harshithseera/tinydb/actions/runs/44869865989) | [comment](https://github.com/harshithseera/tinydb/pull/31#issuecomment-7057770562) |
| S2 | [#31](https://github.com/harshithseera/tinydb/pull/31) | approve | with-claims | approve | [44869870198](https://github.com/harshithseera/tinydb/actions/runs/44869870198) | [comment](https://github.com/harshithseera/tinydb/pull/31#issuecomment-7057771252) |
| S2 | [#31](https://github.com/harshithseera/tinydb/pull/31) | approve | plain | approve | [44869872508](https://github.com/harshithseera/tinydb/actions/runs/44869872508) | [comment](https://github.com/harshithseera/tinydb/pull/31#issuecomment-7057771953) |
| S3 | [#24](https://github.com/harshithseera/tinydb/pull/24) | changes-approach | default | changes-approach | [44869606513](https://github.com/harshithseera/tinydb/actions/runs/44869606513) | [comment](https://github.com/harshithseera/tinydb/pull/24#issuecomment-7057732559) |
| S3 | [#24](https://github.com/harshithseera/tinydb/pull/24) | changes-approach | with-claims | changes-approach | [44869609132](https://github.com/harshithseera/tinydb/actions/runs/44869609132) | [comment](https://github.com/harshithseera/tinydb/pull/24#issuecomment-7057737712) |
| S3 | [#24](https://github.com/harshithseera/tinydb/pull/24) | changes-approach | plain | changes-approach | [44869610606](https://github.com/harshithseera/tinydb/actions/runs/44869610606) | [comment](https://github.com/harshithseera/tinydb/pull/24#issuecomment-7057734008) |
| S4 | [#26](https://github.com/harshithseera/tinydb/pull/26) | changes-code | default | changes-code | [44869613778](https://github.com/harshithseera/tinydb/actions/runs/44869613778) | [comment](https://github.com/harshithseera/tinydb/pull/26#issuecomment-7057733034) |
| S4 | [#26](https://github.com/harshithseera/tinydb/pull/26) | changes-code | with-claims | changes-code | [44869616214](https://github.com/harshithseera/tinydb/actions/runs/44869616214) | [comment](https://github.com/harshithseera/tinydb/pull/26#issuecomment-7057732737) |
| S4 | [#26](https://github.com/harshithseera/tinydb/pull/26) | changes-code | plain | changes-code | [44869618347](https://github.com/harshithseera/tinydb/actions/runs/44869618347) | [comment](https://github.com/harshithseera/tinydb/pull/26#issuecomment-7057732727) |
| S5 | [#27](https://github.com/harshithseera/tinydb/pull/27) | changes-code | default | changes-code | [44869621613](https://github.com/harshithseera/tinydb/actions/runs/44869621613) | [comment](https://github.com/harshithseera/tinydb/pull/27#issuecomment-7057734772) |
| S5 | [#27](https://github.com/harshithseera/tinydb/pull/27) | changes-code | with-claims | changes-code | [44869623928](https://github.com/harshithseera/tinydb/actions/runs/44869623928) | [comment](https://github.com/harshithseera/tinydb/pull/27#issuecomment-7057735353) |
| S5 | [#27](https://github.com/harshithseera/tinydb/pull/27) | changes-code | plain | changes-code | [44869625373](https://github.com/harshithseera/tinydb/actions/runs/44869625373) | [comment](https://github.com/harshithseera/tinydb/pull/27#issuecomment-7057734625) |
| S2a | [#22](https://github.com/harshithseera/tinydb/pull/22) | changes-code | default | approve ❌ | [44869599483](https://github.com/harshithseera/tinydb/actions/runs/44869599483) | [comment](https://github.com/harshithseera/tinydb/pull/22#issuecomment-7057734273) |
| S2a | [#22](https://github.com/harshithseera/tinydb/pull/22) | changes-code | with-claims | changes-code | [44869601461](https://github.com/harshithseera/tinydb/actions/runs/44869601461) | [comment](https://github.com/harshithseera/tinydb/pull/22#issuecomment-7057732168) |
| S2a | [#22](https://github.com/harshithseera/tinydb/pull/22) | changes-code | plain | approve ❌ | [44869603470](https://github.com/harshithseera/tinydb/actions/runs/44869603470) | [comment](https://github.com/harshithseera/tinydb/pull/22#issuecomment-7057732875) |

S2a (#22) was meant to be the correct control, but it was an incomplete fix. Only the `with-claims` reviewer found the defect. We relabelled its ground truth and replaced it with #31, which is a correct fix and passes all 4 hidden tests plus the double-drop check.

## Stress runs (failure paths; issues #33–#35, workflow `339cec1`)

| ID | Issue | Actions run | PR | Path exercised | Reviews | Hidden tests |
|---|---|---|---|---|---|---|
| X1 vague | [#33](https://github.com/harshithseera/tinydb/issues/33) | [44894981695](https://github.com/harshithseera/tinydb/actions/runs/44894981695) | [#36](https://github.com/harshithseera/tinydb/pull/36) | stage-3 check failed and was retried; review → **design**; second round used up → human | [r1 changes-approach](https://github.com/harshithseera/tinydb/pull/36#issuecomment-7061350099), [r2 changes-code](https://github.com/harshithseera/tinydb/pull/36#issuecomment-7061375616) | n/a |
| X2 nested fields | [#34](https://github.com/harshithseera/tinydb/issues/34) | [44894984204](https://github.com/harshithseera/tinydb/actions/runs/44894984204) | [#37](https://github.com/harshithseera/tinydb/pull/37) | clean | [r1 approve](https://github.com/harshithseera/tinydb/pull/37#issuecomment-7061355166) | 4/4 (A2 T2) |
| X3 `batch()` | [#35](https://github.com/harshithseera/tinydb/issues/35) | [44894986794](https://github.com/harshithseera/tinydb/actions/runs/44894986794) | [#38](https://github.com/harshithseera/tinydb/pull/38) | review → **implementation**, approved in round 2 | [r1 changes-code](https://github.com/harshithseera/tinydb/pull/38#issuecomment-7061362892), [r2 approve](https://github.com/harshithseera/tinydb/pull/38#issuecomment-7061386047) | 4/4 (A2 T3) |

Still never exercised in a real run: the stage-1 stop on blocking questions (even X1 was given invented, checkable criteria instead), a stage-4 test failure leading to a retry, and the ADR-013 token budget (tested locally only).

## ADR-012 validation (new default reviewer, workflow `7fd0104`)

| Seed | PR | Ground truth | Verdict | Actions run | Review |
|---|---|---|---|---|---|
| S1 | [#21](https://github.com/harshithseera/tinydb/pull/21) | changes-code | changes-code | [44913331345](https://github.com/harshithseera/tinydb/actions/runs/44913331345) | [comment](https://github.com/harshithseera/tinydb/pull/21#issuecomment-7064001246) |
| S2 | [#31](https://github.com/harshithseera/tinydb/pull/31) | approve | approve | [44913332824](https://github.com/harshithseera/tinydb/actions/runs/44913332824) | [comment](https://github.com/harshithseera/tinydb/pull/31#issuecomment-7064002236) |
| S3 | [#24](https://github.com/harshithseera/tinydb/pull/24) | changes-approach | changes-approach | [44913335168](https://github.com/harshithseera/tinydb/actions/runs/44913335168) | [comment](https://github.com/harshithseera/tinydb/pull/24#issuecomment-7064005156) |
| S4 | [#26](https://github.com/harshithseera/tinydb/pull/26) | changes-code | changes-code | [44913338044](https://github.com/harshithseera/tinydb/actions/runs/44913338044) | [comment](https://github.com/harshithseera/tinydb/pull/26#issuecomment-7064002673) |
| S5 | [#27](https://github.com/harshithseera/tinydb/pull/27) | changes-code | changes-code | [44913340474](https://github.com/harshithseera/tinydb/actions/runs/44913340474) | [comment](https://github.com/harshithseera/tinydb/pull/27#issuecomment-7064002010) |

5/5 correct, and every defect was named. Output tokens: 4,356 with the ADR-012 prompt, against 6,071 with the ADR-008 prompt and 4,188 with `plain` on the same seeds.

## Excluded runs

- In v1, five `autose` runs failed at the `gate` job because `/autose-review` comments matched the `/autose` prefix (runs 44856950970, 44856951325, 44856954483, 44856956094, 44856958451). Fixed in `7b5bf11` (ADR-011). No agent ran.
- `autose` runs that ended `skipped` were the gate correctly ignoring `/autose-review` comments after that fix.
- `autose-ci` runs with status `action_required` on bot-opened PRs: GitHub holds `pull_request` runs for PRs created by `github-actions[bot]`. The stage-5 check uses the `workflow_call` CI job inside the `autose` run instead (ADR-007).

## Token use

- v2, stress runs and ADR-012 validation: 71 agent calls, 3,209,790 input tokens (including cache), 106,196 output tokens.
- v1 (see `v1/runs.md`): 40 agent calls, 1,475,485 input, 48,622 output.
- **Total for the assignment: 111 agent calls, 4,685,275 input tokens, 154,818 output tokens.** Each call's log is in `.autose/issue-N/usage.jsonl` on its branch, and every review comment ends with a usage line. Cost cap: a flat Claude Pro subscription with no API billing (ADR-006). A per-run token budget has applied since `7fd0104` (ADR-013).
