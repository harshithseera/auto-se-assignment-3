# Decision log

| ADR | Decision | Option chosen | Main option rejected | Main reason | Status |
|---|---|---|---|---|---|
| [001](ADR-001.md) | D1 Splitting the work | Builder (stages 1–5, fresh call per stage) + independent reviewer | One agent per stage | Fewest agent setups to build in one day on Pro limits; reviewer must be separate anyway | Accepted |
| [002](ADR-002.md) | D2 Control flow | Fixed Python pipeline + unrolled conditional Actions jobs for review loop | Orchestrator agent | Reliability: code can't skip checks or loop; `GITHUB_TOKEN` events can't re-trigger workflows | Accepted |
| [003](ADR-003.md) | D3 Hand-offs | Full earlier artifacts to builder stages; reviewer gets issue + diff + repo only | Summaries between stages | No information loss; reviewer reads the issue itself | Accepted |
| [004](ADR-004.md) | D4 State | Files in `.autose/issue-N/` on the feature branch | Actions artifacts | Visible in the PR, no expiry; restart = fresh run | Accepted |
| [005](ADR-005.md) | D5 Tools | `claude -p` with `--allowedTools`; scripts do all git/gh; no token in agent env | GitHub MCP server for agents | Only our code can change GitHub, even under prompt injection | Accepted |
| [006](ADR-006.md) | D6 Models | Claude Sonnet for both roles via Claude Pro OAuth token | Different reviewer model | Only Pro available, no API credits; flat fee = hard cost cap | Accepted |
| [007](ADR-007.md) | D7 Checks | All deterministic checks in code; script writes test report | LLM-as-judge | Reliable and reproducible; agent can't grade itself | Accepted |
| [008](ADR-008.md) | D8 Reviewer independence | Separate read-only job, withheld artifacts, adversarial prompt, evidence rule | Isolation only with default prompt | Make blanket approval structurally hard; measured with seeded PRs | Accepted |
| [009](ADR-009.md) | D9 Safety & failures | Turn/time/retry budgets; untrusted-text tags; capability removal | Input filtering / sandboxes | Holds even if an injection succeeds | Accepted |
| [010](ADR-010.md) | D10 Triggers | `autose` label or `/autose` comment by OWNER/MEMBER/COLLABORATOR; per-issue queue | Anyone may trigger; cancel-in-progress | Public fork; never kill a run between push and review | Accepted |

Superseded ADRs are kept; their replacement gets the next number and links back.
