# Workflow code

Copy of the AutoSE files on the fork's `master` (`harshithseera/tinydb`), including the fix that runs agent-written code without GitHub tokens:

| Path | Role |
|---|---|
| `.github/workflows/autose.yml` | Main workflow: gate → build (stages 1–5) → ci-1 → review-1 → fix-1 → ci-2 → review-2 (ADR-002, ADR-010/011) |
| `.github/workflows/autose-ci.yml` | Stage-5 CI check; reusable via `workflow_call` (ADR-007) |
| `.github/workflows/autose-review.yml` | Review-only trigger `/autose-review [variant=…]` for seeded PRs and experiments |
| `.github/actions/autose-setup/` | Shared setup: checkout work tree, Python deps, pinned Claude Code CLI |
| `autose_agent/pipeline.py` | Builder driver, stages 1–5, all deterministic checks |
| `autose_agent/review.py` | Independent reviewer driver, stage 6 (+ experiment variants) |
| `autose_agent/common.py` | `claude -p` wrapper, tool allow-lists, env scrubbing, usage logging |
| `autose_agent/prompts/` | One prompt per stage; `review_plain.md` is the experiment-2 variant |
| `autose_agent/skill/requirements-spec-builder/SKILL.md` | A1 skill, unmodified |
| `autose_agent/context/ARCHITECTURE.md` | A2 architecture doc for TinyDB, unmodified |

The upstream workflows `ci-workflow.yml` and `publish-workflow.yml` are disabled in the fork and not copied.
