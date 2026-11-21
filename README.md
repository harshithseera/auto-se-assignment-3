# AutoSE A3: Agentic SDLC Workflow

A GitHub Actions workflow that turns a labelled issue into a tested, independently reviewed pull request. A human always makes the final merge decision.

## Fork

| | |
|---|---|
| Fork | https://github.com/harshithseera/tinydb (public) |
| Upstream | https://github.com/msiemens/tinydb |
| Pinned commit | `edff96a`. TinyDB's code in `master` is unchanged from this commit; the only files added are the workflow and agent code |
| Protected branch | `master` (TinyDB uses `master`, not `main`). PR required, admins included |

## How to trigger

On an issue in the fork, as the owner or a collaborator, either:
- add the label **`autose`**, or
- comment exactly **`/autose`**.

The workflow creates `autose/issue-N` and runs stages 1–5, saving each artifact in `.autose/issue-N/`. It then opens a PR, runs CI and posts an independent review as a PR comment, with at most 2 review rounds. It never merges.

To run only the reviewer on any PR, comment `/autose-review` or `/autose-review variant=with-claims|plain|adversarial`. This is used for the seeded PRs and the experiments.

## Demo video

**[Demo video: one complete run, from the issue page to the posted review](https://drive.google.com/file/d/1a-B3oV7mL6tB_6-lmY_jROCKvS1vuGZ8/view?usp=sharing)**. It shows issue [#44](https://github.com/harshithseera/tinydb/issues/44) → PR [#45](https://github.com/harshithseera/tinydb/pull/45).

## Models

- **Builder (stages 1–5) and reviewer (stage 6):** Claude Sonnet (`claude-sonnet-5-5`), run through the Claude Code CLI in headless mode (`claude -p`).
- **Authentication:** the `CLAUDE_CODE_OAUTH_TOKEN` repository secret, a Claude Pro token. There is no API billing, so the flat subscription is the hard spending limit ([ADR-006](architecture/decisions/ADR-006.md)). Each run also has a per-run token budget ([ADR-013](architecture/decisions/ADR-013.md)).
- **Total use across all real runs:** 126 agent calls, 5.32M input tokens (including cache) and 170K output tokens ([results/runs.md](results/runs.md)).

## Repository layout

| Path | Contents |
|---|---|
| `report.pdf` | Report |
| `architecture/views/` | Component view, sequence view (a real run), stage map |
| `architecture/decisions/` | ADR-001 to ADR-013 in Nygard format. ADR-008 and ADR-010 are kept and marked Superseded |
| `workflow/` | Copy of the fork's `.github/workflows/` and `.github/actions/`, plus all agent code and prompts (`autose_agent/`) |
| `experiment/issues/` | The 5 issue texts (v1 set in `v1/`) |
| `experiment/hidden_tests/` | Hidden acceptance tests, kept out of the fork |
| `experiment/seeded_prs/` | 5 reviewer-check PRs: diffs and `labels.csv` |
| `experiment/variants.md` | What each decision-experiment variant changes |
| `experiment/stress/` | 3 extra issues used to exercise the failure paths |
| `results/results.csv` | Per-run and per-review data (v1 in `v1/`) |
| [`results/runs.md`](results/runs.md) | **Start here:** links to every Actions run, PR and review in the current set (v2 issues, seeded PRs, stress, validation and demo runs). The first round is archived in `results/v1/runs.md` |
