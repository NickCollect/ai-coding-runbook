---
type: summary
source: 01_Raw/code.claude.com/docs/en/tools-reference.md
source_url: https://code.claude.com/docs/en/tools-reference
title: "Tools reference"
summarized_at: 2026-05-05
entities_referenced: [Subagent, Hooks, MCP-server, Permission-mode, Skill, Scheduled-task, Settings, IDE-integration]
concepts_referenced: [Agent-team]
---

Complete list of Claude Code's built-in tools. Tool names here are the EXACT strings used in permission rules, subagent tool lists, hook matchers. Disable a tool by adding to `permissions.deny`. To add custom tools → MCP server. To add reusable prompts → write a Skill (runs through the existing `Skill` tool, not a new tool entry).

**Tool list** (✓ = requires permission):
| Tool | Description | Perm |
|---|---|---|
| `Agent` | Spawn subagent with own context window | No |
| `AskUserQuestion` | Multiple-choice questions | No |
| `Bash` | Shell commands | ✓ |
| `CronCreate`/`Delete`/`List` | Session-scoped scheduled tasks; restored on `--resume`/`--continue` | No |
| `Edit` | Targeted file edits | ✓ |
| `EnterPlanMode` / `ExitPlanMode` | Plan mode entry/exit | (Exit ✓) |
| `EnterWorktree` / `ExitWorktree` | Git worktree session; pass `path` to enter existing one. **Not available to subagents** | No |
| `Glob` / `Grep` | File pattern + content search | No |
| `ListMcpResourcesTool` / `ReadMcpResourceTool` | MCP resource discovery + read | No |
| `LSP` | Language server: definitions, references, type errors. **Inactive until you install a code-intelligence plugin** | No |
| `Monitor` | Background command, each output line fed to Claude. Same permission rules as Bash. v2.1.98+. NOT available on Bedrock/Vertex/Foundry. NOT available with `DISABLE_TELEMETRY` or `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`. Plugins can ship auto-start monitors | ✓ |
| `NotebookEdit` | Jupyter cell modification | ✓ |
| `PowerShell` | Native PowerShell. Auto-enabled on Windows without Git Bash; rolling out on Windows with Git Bash; opt-in on macOS/Linux/WSL via `CLAUDE_CODE_USE_POWERSHELL_TOOL=1` (requires `pwsh` on PATH) | ✓ |
| `Read` | Read files | No |
| `SendMessage` | Message agent-team teammate or resume subagent by ID. Stopped subagents auto-resume in background. Requires `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` | No |
| `Skill` | Execute a skill within main conversation | ✓ |
| `TaskCreate` / `TaskGet` / `TaskList` / `TaskUpdate` | Session task list (interactive mode) | No |
| `TaskOutput` | DEPRECATED — prefer `Read` on output file path | No |
| `TaskStop` | Kill background task by ID | No |
| `TeamCreate` / `TeamDelete` | Agent team mgmt; experimental flag-gated | No |
| `TodoWrite` | Session task checklist for non-interactive / Agent SDK; interactive sessions use TaskCreate/Get/List/Update | No |
| `ToolSearch` | Load deferred MCP tools (when tool search enabled) | No |
| `WebFetch` / `WebSearch` | Fetch URL / web search | ✓ |
| `Write` | Create/overwrite files | ✓ |

**Bash tool persistence**:
- `cd` in main session **carries over** to later Bash commands as long as it stays inside project dir or `additionalDirectories`. Outside → reset to project dir + appended `Shell cwd was reset to <dir>` in result. Disable carry-over: `CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR=1`.
- **Subagents NEVER carry over** working directory changes.
- **Env vars do NOT persist** across Bash calls (no `export` carry-over). Activate venv/conda BEFORE launching Claude Code, or use `CLAUDE_ENV_FILE` or a `SessionStart` hook.

**LSP tool**: auto-reports type errors and warnings after each file edit. Direct usage: jump-to-definition, find-references, type info, list symbols, find implementations, call hierarchies. Inactive until code-intelligence plugin installed.

**Monitor tool**: writes a small background script and feeds each output line to Claude. Use cases: tail logs, poll CI/PR status, watch directories, track long-running scripts. Stop via cancel request or session end.

**PowerShell tool — additional shell-selection settings**:
- `"defaultShell": "powershell"` in `settings.json` — interactive `!` commands route through PowerShell (requires PowerShell tool enabled)
- `"shell": "powershell"` on individual command hooks — works regardless of `CLAUDE_CODE_USE_POWERSHELL_TOOL` (hooks spawn PowerShell directly)
- `shell: powershell` in skill frontmatter — `` !`...` `` blocks run in PowerShell (requires PowerShell tool enabled)

PowerShell tool preview limitations: profiles not loaded; sandboxing not supported on Windows.

To check what's loaded in a session, ask Claude directly or run `/mcp` for exact MCP tool names.
