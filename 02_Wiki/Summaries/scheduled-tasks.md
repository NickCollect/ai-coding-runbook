---
type: summary
source: 01_Raw/code.claude.com/docs/en/scheduled-tasks.md
source_url: https://code.claude.com/docs/en/scheduled-tasks
title: "Run prompts on a schedule"
summarized_at: 2026-05-05
entities_referenced: [Scheduled-task, Routine, Channel, MCP-server, CI-integration, Slash-command]
concepts_referenced: []
---

Scheduled tasks re-run a prompt automatically on an interval inside an open Claude Code session. **Session-scoped** — stop when you start a new conversation; restored on `--resume`/`--continue` if not [expired](#seven-day-expiry). Requires CC v2.1.72+.

**Comparison**:
| | Cloud Routines | Desktop scheduled tasks | `/loop` |
|---|---|---|---|
| Runs on | Anthropic cloud | Your machine | Your machine |
| Machine on required | No | Yes | Yes |
| Open session required | No | No | **Yes** |
| Persists | Yes | Yes | Restored on resume if unexpired |
| Local file access | No (fresh clone) | Yes | Yes |
| Permission prompts | No (autonomous) | Configurable | Inherited |
| Customizable schedule | Via `/schedule` | Yes | Yes |
| Min interval | 1 hour | 1 minute | 1 minute |

**`/loop`** (bundled skill) — quickest way to repeat:
- `/loop 5m check the deploy` — fixed schedule (cron-converted).
- `/loop check the deploy` — Claude picks interval each iteration (1 min – 1 hour, based on what it observed). Prints chosen delay + reason. May use `Monitor` tool directly to stream a script's output (more efficient than polling).
- `/loop` — runs built-in maintenance prompt (continue unfinished work; tend current branch's PR — review comments, failed CI, merge conflicts; cleanup passes when nothing pending). Bare `/loop` uses dynamic schedule.

Pass another command as prompt: `/loop 20m /review-pr 1234`.

Interval units: `s/m/h/d`. Seconds rounded up to minutes. Non-clean intervals (e.g., 7m, 90m) rounded to nearest cron step — Claude tells you what was picked.

**On Bedrock/Vertex/Foundry**: dynamic interval defaults to fixed 10 min; bare `/loop` (no prompt) prints usage instead of starting maintenance loop.

**Customize default with `loop.md`**:
- `.claude/loop.md` (project, takes precedence) or `~/.claude/loop.md` (user).
- Plain markdown, no required structure. Truncated past 25,000 bytes.
- Edits take effect on next iteration.

**Stop**: press `Esc` while waiting. Tasks scheduled by asking Claude directly NOT affected by Esc.

**One-time reminders**: natural language — "remind me at 3pm to push the release branch", "in 45 minutes, check whether integration tests passed". Single-fire, self-deletes.

**Manage**: ask Claude or via tools: `CronCreate` (5-field cron expression), `CronList`, `CronDelete` (8-char ID). Max 50 tasks per session.

**Execution**: scheduler checks every second, enqueues at low priority. Fires between turns, not mid-response. Local timezone (e.g., `0 9 * * *` = 9am local).

**Jitter** (deterministic, derived from task ID):
- Recurring: up to 10% of period late, capped 15 min.
- One-shot at top/bottom of hour: up to 90 sec early.
- Pick a non-`:00`/`:30` minute (e.g., `3 9 * * *`) to avoid one-shot jitter.

**Seven-day expiry**: recurring tasks fire one final time then delete themselves. For longer durations use Routines/Desktop tasks/GitHub Actions.

**Cron syntax**: standard 5-field, `*`/single/`*/15`/`1-5`/`1,15,30`. Day-of-week: `0` or `7` = Sunday. NO `L`, `W`, `?`, `MON`, `JAN` aliases. Day-of-month + day-of-week: matches if EITHER (vixie-cron semantics).

**Disable scheduler**: `CLAUDE_CODE_DISABLE_CRON=1`.

**Limitations**: only fire while running and idle; no catch-up for missed fires (1 fire only when Claude becomes idle); fresh conversation clears all session-scoped tasks; background Bash/monitor tasks NOT restored on resume.
