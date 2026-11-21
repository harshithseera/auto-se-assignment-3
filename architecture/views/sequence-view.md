# Sequence view: one real run

Issue [#19](https://github.com/harshithseera/tinydb/issues/19) ("Add an operation to append to a list field"), Actions run [44869483228](https://github.com/harshithseera/tinydb/actions/runs/44869483228), PR [#23](https://github.com/harshithseera/tinydb/pull/23), review [comment](https://github.com/harshithseera/tinydb/pull/23#issuecomment-7057733822). All times are UTC on 2026-11-21, taken from the Actions job timestamps, the issue events and `.autose/issue-19/usage.jsonl`.

```mermaid
sequenceDiagram
  actor M as Maintainer
  participant GH as GitHub
  participant G as gate job
  participant B as build job (pipeline.py)
  participant BA as Builder agent (claude -p)
  participant C as ci-1 (autose-ci.yml)
  participant R as review-1 (review.py)
  participant RA as Reviewer agent (claude -p)

  M->>GH: 05:08:51 add label "autose" to #19
  GH->>G: issues.labeled
  G->>G: 05:08:55–58 label check, issue=19
  G->>B: 05:09:00 start
  B->>GH: 05:09:15 comment "AutoSE run started"
  B->>BA: stage 1 (A1 skill + issue in untrusted tags), 3 turns, 8 s
  BA-->>B: spec.md (AC-1..AC-4)
  B->>B: check_spec passes, commit
  B->>BA: stage 2 (ARCHITECTURE.md + spec), 5 turns, 12 s
  BA-->>B: design.md
  B->>B: check_design passes (files exist, append marked new)
  B->>BA: stage 3 implement, 5 turns, 9 s
  B->>B: diff paths allowed, compileall + import pass, diff.patch
  B->>BA: stage 4 tests test_ac1..ac4, 3 turns, 7 s
  B->>B: pytest exit 0, every AC has a test, script writes test_report.md
  B->>GH: 05:09:59 push autose/issue-19, open PR #23 (pr.md), comment on issue
  B->>C: 05:10:04 workflow_call ref=autose/issue-19
  C-->>R: 05:10:25 pytest success
  R->>R: checkout PR head, rm -rf .autose/, diff vs merge-base
  R->>RA: issue + diff only, read/run tools
  RA-->>R: findings (2 minor) + checklist + "VERDICT: approve"
  R->>GH: 05:11:06 PR comment (review-1.md); fix-1, ci-2, review-2 skipped
  Note over M,GH: A human decides whether to merge or close. The workflow never merges.
```

Total time from label to review: 2 min 15 s. Five agent calls, 5,081 output tokens. All 4 hidden tests pass on the branch.
