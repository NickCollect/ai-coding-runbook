---
source_url: https://code.claude.com/docs/en/tools-reference
fetched_at: 2026-05-04T15:07:17.925672+00:00
fetch_method: mintlify_md
---

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Tools reference

> Complete reference for the tools Claude Code can use, including permission requirements.

Claude Code has access to a set of built-in tools that help it understand and modify your codebase. The tool names are the exact strings you use in [permission rules](https://code.claude.com/docs/en/permission rules), [subagent tool lists](https://code.claude.com/docs/en/subagent tool lists), and [hook matchers](https://code.claude.com/docs/en/hook matchers). To disable a tool entirely, add its name to the `deny` array in your [permission settings](https://code.claude.com/docs/en/permission settings).

To add custom tools, connect an [MCP server](https://code.claude.com/docs/en/MCP server). To extend Claude with reusable prompt-based workflows, write a [skill](https://code.claude.com/docs/en/skill), which runs through the existing `Skill` tool rather than adding a new tool entry.

| Tool                   | Description                                                                                                                                                                                                                                                  | Permission Required |
| :--------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| `Agent`                | Spawns a [subagent](https://code.claude.com/docs/en/subagent) with its own context window to handle a task                                                                                                                                                                             | No                  |
| `AskUserQuestion`      | Asks multiple-choice questions to gather requirements or clarify ambiguity                                                                                                                                                                                   | No                  |
| `Bash`                 | Executes shell commands in your environment. See [Bash tool behavior](https://code.claude.com/docs/en/Bash tool behavior)                                                                                                                                                                   | Yes                 |
| `CronCreate`           | Schedules a recurring or one-shot prompt within the current session. Tasks are session-scoped and restored on `--resume` or `--continue` if unexpired. See [scheduled tasks](https://code.claude.com/docs/en/scheduled tasks)                                                            | No                  |
| `CronDelete`           | Cancels a scheduled task by ID                                                                                                                                                                                                                               | No                  |
| `CronList`             | Lists all scheduled tasks in the session                                                                                                                                                                                                                     | No                  |
| `Edit`                 | Makes targeted edits to specific files                                                                                                                                                                                                                       | Yes                 |
| `EnterPlanMode`        | Switches to plan mode to design an approach before coding                                                                                                                                                                                                    | No                  |
| `EnterWorktree`        | Creates an isolated [git worktree](https://code.claude.com/docs/en/git worktree) and switches into it. Pass a `path` to switch into an existing worktree of the current repository instead of creating a new one. Not available to subagents                                                | No                  |
| `ExitPlanMode`         | Presents a plan for approval and exits plan mode                                                                                                                                                                                                             | Yes                 |
| `ExitWorktree`         | Exits a worktree session and returns to the original directory. Not available to subagents                                                                                                                                                                   | No                  |
| `Glob`                 | Finds files based on pattern matching                                                                                                                                                                                                                        | No                  |
| `Grep`                 | Searches for patterns in file contents                                                                                                                                                                                                                       | No                  |
| `ListMcpResourcesTool` | Lists resources exposed by connected [MCP servers](https://code.claude.com/docs/en/MCP servers)                                                                                                                                                                                                  | No                  |
| `LSP`                  | Code intelligence via language servers: jump to definitions, find references, report type errors and warnings. See [LSP tool behavior](https://code.claude.com/docs/en/LSP tool behavior)                                                                                                   | No                  |
| `Monitor`              | Runs a command in the background and feeds each output line back to Claude, so it can react to log entries, file changes, or polled status mid-conversation. See [Monitor tool](https://code.claude.com/docs/en/Monitor tool)                                                               | Yes                 |
| `NotebookEdit`         | Modifies Jupyter notebook cells                                                                                                                                                                                                                              | Yes                 |
| `PowerShell`           | Executes PowerShell commands natively. See [PowerShell tool](https://code.claude.com/docs/en/PowerShell tool) for availability                                                                                                                                                              | Yes                 |
| `Read`                 | Reads the contents of files                                                                                                                                                                                                                                  | No                  |
| `ReadMcpResourceTool`  | Reads a specific MCP resource by URI                                                                                                                                                                                                                         | No                  |
| `SendMessage`          | Sends a message to an [agent team](https://code.claude.com/docs/en/agent team) teammate, or [resumes a subagent](https://code.claude.com/docs/en/resumes a subagent) by its agent ID. Stopped subagents auto-resume in the background. Only available when `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` is set | No                  |
| `Skill`                | Executes a [skill](https://code.claude.com/docs/en/skill) within the main conversation                                                                                                                                                                      | Yes                 |
| `TaskCreate`           | Creates a new task in the task list                                                                                                                                                                                                                          | No                  |
| `TaskGet`              | Retrieves full details for a specific task                                                                                                                                                                                                                   | No                  |
| `TaskList`             | Lists all tasks with their current status                                                                                                                                                                                                                    | No                  |
| `TaskOutput`           | (Deprecated) Retrieves output from a background task. Prefer `Read` on the task's output file path                                                                                                                                                           | No                  |
| `TaskStop`             | Kills a running background task by ID                                                                                                                                                                                                                        | No                  |
| `TaskUpdate`           | Updates task status, dependencies, details, or deletes tasks                                                                                                                                                                                                 | No                  |
| `TeamCreate`           | Creates an [agent team](https://code.claude.com/docs/en/agent team) with multiple teammates. Only available when `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` is set                                                                                                                        | No                  |
| `TeamDelete`           | Disbands an agent team and cleans up teammate processes. Only available when `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` is set                                                                                                                                 | No                  |
| `TodoWrite`            | Manages the session task checklist. Available in non-interactive mode and the [Agent SDK](https://code.claude.com/docs/en/Agent SDK); interactive sessions use TaskCreate, TaskGet, TaskList, and TaskUpdate instead                                                                      | No                  |
| `ToolSearch`           | Searches for and loads deferred tools when [tool search](https://code.claude.com/docs/en/tool search) is enabled                                                                                                                                                      | No                  |
| `WebFetch`             | Fetches content from a specified URL                                                                                                                                                                                                                         | Yes                 |
| `WebSearch`            | Performs web searches                                                                                                                                                                                                                                        | Yes                 |
| `Write`                | Creates or overwrites files                                                                                                                                                                                                                                  | Yes                 |

Permission rules can be configured using `/permissions` or in [permission settings](https://code.claude.com/docs/en/permission settings). Also see [Tool-specific permission rules](https://code.claude.com/docs/en/Tool-specific permission rules).

## Bash tool behavior

The Bash tool runs each command in a separate process with the following persistence behavior:

* When Claude runs `cd` in the main session, the new working directory carries over to later Bash commands as long as it stays inside the project directory or an [additional working directory](https://code.claude.com/docs/en/additional working directory) you added with `--add-dir`, `/add-dir`, or `additionalDirectories` in settings. Subagent sessions never carry over working directory changes.
  * If `cd` lands outside those directories, Claude Code resets to the project directory and appends `Shell cwd was reset to <dir>` to the tool result.
  * To disable this carry-over so every Bash command starts in the project directory, set `CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR=1`.
* Environment variables do not persist. An `export` in one command will not be available in the next.

Activate your virtualenv or conda environment before launching Claude Code. To make environment variables persist across Bash commands, set [`CLAUDE_ENV_FILE`](https://code.claude.com/docs/en/`CLAUDE_ENV_FILE`) to a shell script before launching Claude Code, or use a [SessionStart hook](https://code.claude.com/docs/en/SessionStart hook) to populate it dynamically.

## LSP tool behavior

The LSP tool gives Claude code intelligence from a running language server. After each file edit, it automatically reports type errors and warnings so Claude can fix issues without a separate build step. Claude can also call it directly to navigate code:

* Jump to a symbol's definition
* Find all references to a symbol
* Get type information at a position
* List symbols in a file or workspace
* Find implementations of an interface
* Trace call hierarchies

The tool is inactive until you install a [code intelligence plugin](https://code.claude.com/docs/en/code intelligence plugin) for your language. The plugin bundles the language server configuration, and you install the server binary separately.

## Monitor tool

<Note>
  The Monitor tool requires Claude Code v2.1.98 or later.
</Note>

The Monitor tool lets Claude watch something in the background and react when it changes, without pausing the conversation. Ask Claude to:

* Tail a log file and flag errors as they appear
* Poll a PR or CI job and report when its status changes
* Watch a directory for file changes
* Track output from any long-running script you point it at

Claude writes a small script for the watch, runs it in the background, and receives each output line as it arrives. You keep working in the same session and Claude interjects when an event lands. Stop a monitor by asking Claude to cancel it or by ending the session.

Monitor uses the same [permission rules as Bash](https://code.claude.com/docs/en/permission rules as Bash), so `allow` and `deny` patterns you have set for Bash apply here too. It is not available on Amazon Bedrock, Google Vertex AI, or Microsoft Foundry. It is also not available when `DISABLE_TELEMETRY` or `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` is set.

Plugins can declare monitors that start automatically when the plugin is active, instead of asking Claude to start them. See [plugin monitors](https://code.claude.com/docs/en/plugin monitors).

## PowerShell tool

The PowerShell tool lets Claude run PowerShell commands natively. On Windows, this means commands run in PowerShell instead of routing through Git Bash. On Windows without Git Bash, the tool is enabled automatically. On Windows with Git Bash installed, the tool is rolling out progressively. On Linux, macOS, and WSL, the tool is opt-in.

### Enable the PowerShell tool

Set `CLAUDE_CODE_USE_POWERSHELL_TOOL=1` in your environment or in `settings.json`:

```json theme={null}
{
  "env": {
    "CLAUDE_CODE_USE_POWERSHELL_TOOL": "1"
  }
}
```

On Windows, set the variable to `0` to opt out of the rollout. On Linux, macOS, and WSL, the tool requires PowerShell 7 or later: install `pwsh` and ensure it is on your `PATH`.

On Windows, Claude Code auto-detects `pwsh.exe` for PowerShell 7+ with a fallback to `powershell.exe` for PowerShell 5.1. When the tool is enabled, Claude treats PowerShell as the primary shell. The Bash tool remains available for POSIX scripts when Git Bash is installed.

### Shell selection in settings, hooks, and skills

Three additional settings control where PowerShell is used:

* `"defaultShell": "powershell"` in [`settings.json`](https://code.claude.com/docs/en/`settings.json`): routes interactive `!` commands through PowerShell. Requires the PowerShell tool to be enabled.
* `"shell": "powershell"` on individual [command hooks](https://code.claude.com/docs/en/command hooks): runs that hook in PowerShell. Hooks spawn PowerShell directly, so this works regardless of `CLAUDE_CODE_USE_POWERSHELL_TOOL`.
* `shell: powershell` in [skill frontmatter](https://code.claude.com/docs/en/skill frontmatter): runs `` !`command` `` blocks in PowerShell. Requires the PowerShell tool to be enabled.

The same main-session working-directory reset behavior described under the Bash tool section applies to PowerShell commands, including the `CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR` environment variable.

### Preview limitations

The PowerShell tool has the following known limitations during the preview:

* PowerShell profiles are not loaded
* On Windows, sandboxing is not supported

## Check which tools are available

Your exact tool set depends on your provider, platform, and settings. To check what's loaded in a running session, ask Claude directly:

```text theme={null}
What tools do you have access to?
```

Claude gives a conversational summary. For exact MCP tool names, run `/mcp`.

## See also

* [MCP servers](https://code.claude.com/docs/en/MCP servers): add custom tools by connecting external servers
* [Permissions](https://code.claude.com/docs/en/Permissions): permission system, rule syntax, and tool-specific patterns
* [Subagents](https://code.claude.com/docs/en/Subagents): configure tool access for subagents
* [Hooks](https://code.claude.com/docs/en/Hooks): run custom commands before or after tool execution
