---
type: summary
source: 01_Raw/code.claude.com/docs/en/ultrareview.md
source_url: https://code.claude.com/docs/en/ultrareview
title: "Find bugs with ultrareview"
summarized_at: 2026-05-05
entities_referenced: [Headless-mode, Native-interface, Enterprise-gateway]
concepts_referenced: [Agent-team]
---

`/ultrareview` (research preview, Claude Code v2.1.86+) — multi-agent code review run on Claude Code on the Web infrastructure. Launches a fleet of reviewer agents in a remote sandbox, each finding **independently reproduced and verified** before being reported. Higher signal vs. local `/review` (real bugs, not style suggestions), broader coverage (parallel fleet), no local resource use.

**Auth**: requires Claude.ai account (web infra). API-key-only login → must `/login` with Claude.ai first. NOT available on Bedrock/Vertex/Foundry, NOT available with Zero Data Retention.

**Usage**:
```text
/ultrareview            # diff between current branch and default branch (incl. uncommitted/staged)
/ultrareview 1234       # PR #1234 (clones from GitHub directly; requires github.com remote)
```

For repos too large to bundle, prompts you to push and use PR mode. Confirmation dialog shows scope (file/line count for branch), remaining free runs, estimated cost. After confirm, runs in background — keep using session.

**Pricing**:
| Plan | Free runs | After |
|---|---|---|
| Pro | 3 free runs through May 5, 2026 (one-time, no refresh) | extra usage |
| Max | 3 free runs through May 5, 2026 | extra usage |
| Team / Enterprise | none | extra usage |

Typical cost $5-20 per review. Run counts as used once remote session **starts** (stop early or fail still uses one). Paid review billed only for portion that ran. Account/org must have **extra usage enabled** before launching paid reviews. Check/change with `/extra-usage`.

**Tracking**: `/tasks` lists running and completed reviews. Open detail view, stop a running review (archives cloud session, no partial findings returned). Verified findings appear as session notification when done — file location + explanation per finding.

**Non-interactive**: `claude ultrareview [PR-or-branch]` subcommand for CI/scripts. Blocks until done. Stdout = formatted findings (or `--json` for raw `bugs.json`). Stderr = progress + live session URL. Exit codes: 0 (completed with or without findings), 1 (launch fail / session error / timeout), 130 (Ctrl-C). Interrupting the subcommand does NOT kill the remote review — follow URL to watch.

Flags: `--json`, `--timeout <minutes>` (default 30).

Invoking the subcommand counts as consent for the billing/terms prompt.

**vs `/review`**:
| | `/review` | `/ultrareview` |
|---|---|---|
| Where | local session | remote cloud sandbox |
| Depth | single-pass | multi-agent fleet + verification |
| Duration | seconds-minutes | 5-10 min |
| Cost | normal usage | free-then-extra (~$5-20) |
| Best for | iteration feedback | pre-merge confidence on substantial changes |

For automatic per-PR reviews on GitHub, the managed Code Review service is the GitHub-integrated alternative.
