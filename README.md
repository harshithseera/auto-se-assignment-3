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

## Try it yourself

### 1. Write an issue

Open a new issue in the fork: **[github.com/harshithseera/tinydb/issues/new](https://github.com/harshithseera/tinydb/issues/new)**. Describe it the way a user would: what you want, a short example, and what should happen in the edge cases. The agents write their acceptance criteria from this text, so concrete expectations give better results.

Example (**[open this issue pre-filled](https://github.com/harshithseera/tinydb/issues/new?title=Add%20an%20operation%20to%20remove%20an%20item%20from%20a%20list%20field&body=%60tinydb.operations%60%20has%20helpers%20like%20%60increment%60%20and%20%60set%60%2C%20but%20nothing%20to%20take%20a%20value%20out%20of%20a%20list%20field.%20Could%20we%20get%20something%20like%3A%0A%0A%60%60%60python%0Afrom%20tinydb.operations%20import%20remove_item%0Adb.update%28remove_item%28%27tags%27%2C%20%27urgent%27%29%2C%20Query%28%29.id%20%3D%3D%203%29%0A%60%60%60%0A%0AIt%20should%20remove%20the%20first%20matching%20value%20from%20the%20list.%20If%20the%20value%20isn%27t%20in%20the%20list%2C%20nothing%20should%20change.%20If%20the%20field%20is%20missing%20or%20isn%27t%20a%20list%2C%20I%27d%20expect%20a%20%60TypeError%60%20rather%20than%20silently%20doing%20nothing.)**):

> **Title:** Add an operation to remove an item from a list field
>
> `tinydb.operations` has helpers like `increment` and `set`, but nothing to take a value out of a list field. Could we get something like:
> ```python
> from tinydb.operations import remove_item
> db.update(remove_item('tags', 'urgent'), Query().id == 3)
> ```
> It should remove the first matching value from the list. If the value isn't in the list, nothing should change. If the field is missing or isn't a list, I'd expect a `TypeError` rather than silently doing nothing.

### 2. Start the run

Only the repo owner or a collaborator can start a run (ADR-011). Anyone can open an issue, but someone else's `autose` label or `/autose` comment is ignored by the `gate` job.
- **Owner or collaborator:** add the `autose` label to the issue, or comment exactly `/autose`.
- **Anyone else:** open the issue and ask a maintainer to add the label.
- **Course TAs:** are being given collaborator access to the fork. Once you accept the invitation, you can start runs yourself, using the label or the comment.

### 3. Follow it

After about 20 seconds the bot comments **"AutoSE run started"** with a link to the Actions run. A run usually takes 2–3 minutes:
1. **Actions run:** the `build` job runs stages 1–5, then `ci-1` runs the tests, then `review-1` reviews the change.
2. **Issue:** the bot comments **"AutoSE opened PR #M"**.
3. **PR #M → Files changed:** the code change and tests, plus each stage's artifact in `.autose/issue-N/` (`spec.md`, `design.md`, `test_report.md`, `pr.md`).
4. **PR #M → Conversation:** the independent review, with its findings, checklist and `VERDICT`. If the reviewer asks for changes, a fix round and a second review follow automatically.
5. **You decide** whether to merge or close. The workflow never merges.

If a stage can't pass its check, or the token budget runs out, the run stops and the bot comments on the issue with the reason.

### Running it in your own copy

1. Fork `harshithseera/tinydb`. In your fork, enable **Issues** and **Actions**.
2. Run `claude setup-token` (this needs a Claude Pro or Max plan) and store the result as the repository secret `CLAUDE_CODE_OAUTH_TOKEN`.
3. Under Settings → Actions → General, enable **"Allow GitHub Actions to create and approve pull requests"**.
4. Create a label named `autose`, then follow steps 1–3 above.

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
| `results/runs.md` | Links to every Actions run, PR and review |
