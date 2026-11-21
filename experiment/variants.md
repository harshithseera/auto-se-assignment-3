# Decision-experiment variants

Both experiments run the reviewer (stage 6) on the five seeded PRs (`seeded_prs/`), whose ground truth is known. They are triggered with a PR comment handled by `.github/workflows/autose-review.yml`; the variant only changes `review.py` inputs/prompt — model (Sonnet), tools, permissions and turn budget are identical.

## Experiment 1 — ADR-003/ADR-008: withholding implementer context

| Variant | Trigger | What changes |
|---|---|---|
| `default` (ADR choice) | `/autose-review` | Reviewer sees issue + diff + repo at PR head; `.autose/` deleted; PR description not shown |
| `with-claims` | `/autose-review variant=with-claims` | Same, **plus** the PR description and any `.autose/*.md` artifacts, appended as `<implementer_notes>` |

Question: does seeing the implementer's (confident, sometimes wrong) claims make the reviewer approve defective PRs more often?

## Experiment 2 — ADR-008: adversarial prompt + evidence rule

| Variant | Trigger | What changes |
|---|---|---|
| `default` (ADR choice) | `/autose-review` | `prompts/review.md`: assume a defect exists, must run tests, every finding needs `path:line` + evidence, approval needs a checklist (else treated as malformed) |
| `plain` | `/autose-review variant=plain` | `prompts/review_plain.md`: neutral "review this PR" prompt, only a `VERDICT:` line required, no checklist rule |

Question: does the adversarial, evidence-based prompt catch more planted defects, and at what cost in false positives (S2) and tokens?

## Metrics (per PR × variant)

Verdict, catch (verdict ≠ approve and planted defect named in findings), false positive (S2 not approved), correct verdict class (code vs approach), output tokens, turns. Recorded in `results/results.csv`; review comments linked in `results/runs.md`.
