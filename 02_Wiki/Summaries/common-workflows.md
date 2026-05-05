---
type: summary
source: 01_Raw/code.claude.com/docs/en/common-workflows.md
source_url: https://code.claude.com/docs/en/common-workflows
title: "Common workflows"
summarized_at: 2026-05-05
entities_referenced: [Subagent, Skill, MCP-server, Permission-mode, Headless-mode, Routine, Scheduled-task, CI-integration]
concepts_referenced: []
---

Recipe-style guide for everyday Claude Code tasks. Each recipe is a prompt sequence; nothing requires special config.

Prompt recipes covered:
- **Codebase overview** — broad → specific (architecture, data models, auth flow). Ask for project glossary.
- **Find code** — specific feature queries; install code-intelligence plugin for "go to definition" precision.
- **Bug fixes** — paste error output / repro steps, ask for fix recommendations, apply.
- **Refactoring** — identify legacy patterns, get recommendations, apply in small testable increments, run tests after.
- **Testing** — find untested code, generate scaffolding matching existing patterns, add edge-case tests, run + fix failures.
- **Pull requests** — `"create a pr"` works directly. When created via `gh pr create`, session is auto-linked; resume later with `claude --from-pr <number>` or paste PR URL into `/resume` picker.
- **Documentation** — find undocumented (e.g. "find functions without JSDoc"), generate, refine.
- **Notes/non-code** — Claude works in any dir; `.claude/` and `CLAUDE.md` coexist with other tools' config.
- **Images** — drag-drop, paste with `Ctrl+V` (NOT `Cmd+V`), or path. Use for screenshots, mockups, schemas, error screens.
- **`@` references** — `@file.js` includes content (also pulls CLAUDE.md from that file's dir tree); `@dir` shows listing only; `@server:resource` fetches from MCP servers.

Scheduling options (pick by where it runs):
| Option | Where | Best for |
|---|---|---|
| Routines | Anthropic infra | Runs even when your machine is off; can trigger on API calls / GitHub events |
| Desktop scheduled tasks | Local desktop app | Needs local file / tool access |
| GitHub Actions | CI | Repo-event triggers |
| `/loop` | Current CLI session | Quick polling while session open |

For scheduled tasks: explicit success criteria — task can't ask clarifying questions.

Self-documenting: ask Claude about its own capabilities ("can Claude Code create PRs?", "how does it handle permissions?") — it has docs access. Run `/powerup` for interactive lessons with animated demos.

Session continuity: `claude --continue` (most recent in cwd), `claude --resume` (picker), `/resume` from inside.

Parallelism: `claude --worktree feature-auth` for isolated checkouts.

Plan-before-edit: `claude --permission-mode plan` or `Shift+Tab` mid-session.

Delegate research: "use a subagent to investigate X" — separate context window, only findings return.

Headless: `git log --oneline -20 | claude -p "summarize"` — Unix pipeline friendly.
