---
source_url: https://cursor.com/docs/cli/shell-mode
fetched_at: 2026-11-23T08:28:22.699184+00:00
fetch_method: mintlify_md
---

# Shell Mode

Shell Mode runs shell commands directly from the CLI without leaving your conversation. Use it for quick, non-interactive commands with safety checks and output displayed in the conversation.

[Media](/docs-static/images/cli/shell-mode/cli-shell-mode.mp4)

## Command execution

Commands run in your shell (`$SHELL` when it's zsh or bash) with the CLI's working directory and environment. Chain commands to run in other directories:

```bash
cd subdir && npm test
```

By default, the shell is a login shell, so your login scripts run:

- **bash**: `/etc/profile`, then the first of `~/.bash_profile`, `~/.bash_login`, and `~/.profile`
- **zsh**: `/etc/zprofile`, `~/.zprofile`, `/etc/zlogin`, and `~/.zlogin`

To skip them, start the CLI with `CURSOR_LOGIN_SHELL=0`. Zsh runs `~/.zshrc` either way. Bash runs `~/.bashrc` when you skip the login scripts, and otherwise only if one of them sources it. Only the value `0` turns the login shell off. The agent's own shell commands follow the same setting.

```bash
CURSOR_LOGIN_SHELL=0 agent
```

## Output

Large outputs are truncated automatically and long-running processes timeout to maintain performance.

## Limitations

- Commands timeout after 30 seconds
- Long-running processes, servers, and interactive prompts are not supported
- Use short, non-interactive commands for best results

## Permissions

Commands are checked against your permissions and team settings before execution. See [Permissions](https://cursor.com/docs/cli/reference/permissions.md) for detailed configuration.

Admin policies may block certain commands, and commands with redirection cannot be allowlisted inline.

## Usage guidelines

Shell Mode works well for status checks, quick builds, file operations, and environment inspection.

Avoid long-running servers, interactive applications, and commands requiring input.

Each command runs independently - use `cd <dir> && ...` to run commands in other directories.

## Troubleshooting

- If a command hangs, cancel with Ctrl+C and add non-interactive flags
- When prompted for permissions, approve once or add to allowlist with Tab
- For truncated output, use Ctrl+O to expand
- To run in different directories, use `cd <dir> && ...` since changes don't persist
- Shell Mode supports zsh and bash from your `$SHELL` variable

## FAQ

### Does \`cd\` persist across runs?

No. Each command runs independently. Use `cd <dir> && ...` to run commands in different directories.

### Can I change the timeout?

No. Commands are limited to 30 seconds and this is not configurable.

### Where are permissions configured?

Permissions are managed by CLI and team configuration. Use the decision banner to add commands to allowlists.

### How do I exit Shell Mode?

Press Escape when the input is empty, Backspace/Delete on empty input, or Ctrl+C to clear and exit.


---

## Sitemap

[Overview of all docs pages](/llms.txt)
