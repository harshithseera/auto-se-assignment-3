# Stage map

| # | Stage | Agent | Input | Artifact | Check (who decides) | On failure |
|---|---|---|---|---|---|---|
| 1 | Requirements | Builder + A1 skill | issue title/body (quoted as untrusted data) | `.autose/issue-N/spec.md` | Script: ≥1 line `AC-<n>: Given … When … Then …` under `## Acceptance criteria`; `## Blocking open questions` empty | explain in `spec.md`, stop run |
| 2 | Design | Builder + `ARCHITECTURE.md` | `spec.md`, repo | `design.md` | Script: lists ≥1 file that exists in repo and ≥1 function/class found by `grep` in that file | explain, stop |
| 3 | Implementation | Builder | `spec.md`, `design.md`, repo on `autose/issue-N` | `diff.patch` (`git diff master`) | Script: diff non-empty, no `.github/` changes, `compileall` + `import tinydb` succeed | retry ≤2, then stop |
| 4 | Testing | Builder | `spec.md`, `diff.patch` | new tests in `tests/`; `test_report.md` written by the script from pytest output | Script: a test named `*ac<n>*` per criterion, `pytest` exit 0 on full suite | back to 3 (≤3 attempts total); after that back to 2 once; then stop |
| 5 | Release | script only | all artifacts | `pr.md` + PR URL | Script: `gh pr view` state OPEN and `ci` job succeeded | stop |
| 6 | Review | Reviewer (separate job) | issue, `git diff master...HEAD` minus `.autose/`, repo @ PR head | `review.md` with verdict `approve` / `changes-code` / `changes-approach` | Script parses `VERDICT:` line (malformed = stop); approve or 2 review rounds done; posted as PR comment | `changes-approach` → stage 2, `changes-code` → stage 3 |

All checks are deterministic (ADR-007). Final merge: always a human. The workflow never merges.
