---
source_url: https://cursor.com/docs/cli/reference/parameters
fetched_at: 2026-06-22T06:23:24.763396+00:00
fetch_method: mintlify_md
---

# Parameters

## Global options

Global options can be used with any command:

| Option                     | Description                                                                                                          |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `-v, --version`            | Output the version number                                                                                            |
| `--api-key <key>`          | API key for authentication (can also use `CURSOR_API_KEY` env var)                                                   |
| `-H, --header <header>`    | Add custom header to agent requests (format: `Name: Value`, can be used multiple times)                              |
| `-p, --print`              | Print responses to console (for scripts or non-interactive use). Has access to all tools, including write and shell. |
| `--output-format <format>` | Output format (only works with `--print`): `text`, `json`, or `stream-json` (default: `text`)                        |
| `--stream-partial-output`  | Stream partial output as individual text deltas (only works with `--print` and `stream-json` format)                 |
| `--resume [chatId]`        | Resume a chat session                                                                                                |
| `--continue`               | Continue the previous session (alias for `--resume=-1`)                                                              |
| `--model <model>`          | Model to use                                                                                                         |
| `--mode <mode>`            | Set agent mode: `plan` or `ask` (agent is the default when no mode is specified)                                     |
| `--plan`                   | Start in plan mode (shorthand for `--mode=plan`)                                                                     |
| `--list-models`            | List all available models                                                                                            |
| `-f, --force`              | Force allow commands unless explicitly denied                                                                        |
| `--yolo`                   | Alias for `--force`                                                                                                  |
| `--sandbox <mode>`         | Set sandbox mode: `enabled` or `disabled`                                                                            |
| `--approve-mcps`           | Automatically approve all MCP servers                                                                                |
| `--trust`                  | Trust the workspace without prompting (headless mode only)                                                           |
| `--workspace <path>`       | Workspace directory to use                                                                                           |
| `--plugin-dir <path>`      | Load a local plugin directory (can be specified multiple times)                                                      |
| `-w, --worktree [name]`    | Run in a new Git worktree under `~/.cursor/worktrees/<reponame>/<name>`. If omitted, a name is generated.            |
| `--worktree-base <branch>` | Branch or ref to base the new worktree on (default: current HEAD)                                                    |
| `--skip-worktree-setup`    | Skip running worktree setup scripts from `.cursor/worktrees.json`                                                    |
| `-h, --help`               | Display help for command                                                                                             |

## Commands

| Command                       | Description                                                       | Usage                               |
| ----------------------------- | ----------------------------------------------------------------- | ----------------------------------- |
| `agent [prompt...]`           | Start in agent mode (the default)                                 | `agent agent "fix the tests"`       |
| `login`                       | Authenticate with Cursor                                          | `agent login`                       |
| `logout`                      | Sign out and clear stored authentication                          | `agent logout`                      |
| `status` \| `whoami`          | View authentication status                                        | `agent status`                      |
| `about`                       | Display version, system, and account info                         | `agent about`                       |
| `models`                      | List available models for this account                            | `agent models`                      |
| `mcp`                         | Manage MCP servers                                                | `agent mcp`                         |
| `worker`                      | Start a private cloud worker that runs agents in your environment | `agent worker start`                |
| `acp`                         | Start ACP server mode (advanced, hidden command)                  | `agent acp`                         |
| `update`                      | Update Cursor Agent to the latest version                         | `agent update`                      |
| `ls`                          | Resume a chat session                                             | `agent ls`                          |
| `resume`                      | Resume the latest chat session                                    | `agent resume`                      |
| `create-chat`                 | Create a new empty chat and return its ID                         | `agent create-chat`                 |
| `generate-rule` \| `rule`     | Generate a new Cursor rule with interactive prompts               | `agent generate-rule`               |
| `install-shell-integration`   | Install shell integration to `~/.zshrc`                           | `agent install-shell-integration`   |
| `uninstall-shell-integration` | Remove shell integration from `~/.zshrc`                          | `agent uninstall-shell-integration` |
| `help [command]`              | Display help for command                                          | `agent help [command]`              |

`agent acp` is intended for custom ACP clients and advanced integrations. It is
hidden from default command help output.

When no command is specified, Cursor Agent starts in interactive agent mode by
default.

## MCP

Manage MCP servers configured for Cursor Agent.

| Subcommand                | Description                                                                              | Usage                               |
| ------------------------- | ---------------------------------------------------------------------------------------- | ----------------------------------- |
| `login <identifier>`      | Authenticate with an MCP server configured in `.cursor/mcp.json` or `~/.cursor/mcp.json` | `agent mcp login <identifier>`      |
| `list`                    | List configured MCP servers and their status                                             | `agent mcp list`                    |
| `list-tools <identifier>` | List available tools and their argument names for a specific MCP                         | `agent mcp list-tools <identifier>` |
| `enable <identifier>`     | Add an MCP server to the local approved list                                             | `agent mcp enable <identifier>`     |
| `disable <identifier>`    | Disable an MCP server so it won't load or prompt for approval                            | `agent mcp disable <identifier>`    |

All MCP commands support `-h, --help` for command-specific help.

## Worker

Start a private cloud worker that connects to Cursor and runs agents in your environment.

| Subcommand       | Description                                                             | Usage                |
| ---------------- | ----------------------------------------------------------------------- | -------------------- |
| `start`          | Start the worker and connect to Cursor                                  | `agent worker start` |
| `debug`          | Run private worker preflight diagnostics for auth, privacy, and routing | `agent worker debug` |
| `help [command]` | Display help for command                                                | `agent worker help`  |

| Option                             | Description                                                                                         |
| ---------------------------------- | --------------------------------------------------------------------------------------------------- |
| `--auth-token-file <path>`         | Path to a file containing the worker auth token                                                     |
| `--worker-dir <path>`              | Workspace root to expose to agents. Repeatable. The first value is the assignment identity.         |
| `--management-addr <address>`      | Listen address for `/healthz`, `/readyz`, and `/metrics`                                            |
| `--label <key=value>`              | Add a worker label. Can be used multiple times. Can't be used with `--labels-file`.                 |
| `--labels-file <path>`             | Path to a JSON or TOML labels file. Can also use `CURSOR_WORKER_LABELS_FILE`.                       |
| `--idle-release-timeout <seconds>` | Seconds the worker may stay connected after becoming idle. Default `0` disables idle-based release. |
| `--pool`                           | Register for pool assignment. One cloud agent claims the worker at a time.                          |
| `--single-use`                     | Legacy alias for `--pool`                                                                           |
| `--pool-name <name>`               | Pool label for pool workers. Requires `--pool` or `--single-use`. Defaults to `default`.            |
| `--name <name>`                    | Custom display name. Defaults to the machine hostname.                                              |
| `--data-dir <path>`                | Base directory for logs, artifacts, and recording data                                              |
| `--debug`                          | Print worker debug diagnostics before starting bridge mode                                          |
| `--verbose`                        | Enable verbose startup logs for `agent worker start`                                                |
| `--json`                           | Output the `agent worker debug` report as JSON                                                      |

## Command-specific options

| Command            | Option              | Description                                       |
| ------------------ | ------------------- | ------------------------------------------------- |
| `status`, `whoami` | `--format <format>` | Output format: `text` or `json` (default: `text`) |
| `about`            | `--format <format>` | Output format: `text` or `json` (default: `text`) |

## Arguments

When starting in chat mode (default behavior), you can provide an initial prompt:

**Arguments:**

- `prompt` — Initial prompt for the agent

## Getting help

All commands support the global `-h, --help` option to display command-specific help.


---

## Sitemap

[Overview of all docs pages](/llms.txt)
