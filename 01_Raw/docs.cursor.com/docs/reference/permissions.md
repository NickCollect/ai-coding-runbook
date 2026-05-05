---
source_url: https://cursor.com/docs/reference/permissions
fetched_at: 2026-05-05T19:55:43.378405+00:00
fetch_method: mintlify_md
---

# permissions.json reference

Use `permissions.json` to configure global MCP tool and terminal command allowlists for [auto-run](https://cursor.com/docs/agent/overview.md#auto-run) without approval.

When `permissions.json` is present and defines an allowlist, it **overrides** the corresponding in-app allowlist in Cursor Settings. The in-app allowlist editor becomes read-only for that allowlist type.

## File location

Place `permissions.json` in your Cursor data folder:

```text
~/.cursor/permissions.json
```

This is a global, per-user file. It applies to all workspaces. There is no per-project override.

The file is read on startup and re-read automatically whenever it changes. JSONC (JSON with comments) is supported.

## Top-level fields

All fields are optional. Unknown keys are ignored.

| Field               | Type       | Default | Description                                                                                              |
| :------------------ | :--------- | :------ | :------------------------------------------------------------------------------------------------------- |
| `mcpAllowlist`      | `string[]` | not set | MCP tools that can auto-run without approval. When set, overrides the in-app MCP allowlist.              |
| `terminalAllowlist` | `string[]` | not set | Terminal commands that can auto-run without approval. When set, overrides the in-app terminal allowlist. |

Non-string entries inside either array are silently dropped.

## Precedence

Allowlists can come from three sources, evaluated in strict priority order:

```text
team admin (dashboard)  >  permissions.json  >  IDE settings UI
       (highest)             (overrides IDE)        (lowest)
```

- **Team admin controls**: If your team admin has configured auto-run controls through the dashboard, those settings take effect. Neither `permissions.json` nor the IDE allowlist can add extra entries.
- **permissions.json**: When auto-run is not admin-controlled and `permissions.json` defines an allowlist key, that key's value **replaces** the corresponding IDE allowlist entirely. The in-app editor for that allowlist becomes read-only, and the "Add to allowlist" button is hidden.
- **IDE settings**: When auto-run is not admin-controlled and `permissions.json` does not define a given allowlist key, the IDE allowlist from Cursor Settings is used.

MCP and terminal allowlists are independent. You can define one in `permissions.json` and manage the other in the IDE. For example, defining only `mcpAllowlist` in the file overrides the MCP allowlist but leaves the terminal allowlist under IDE control.

If the file is missing, unparseable, or does not contain a given key, Cursor falls back to the IDE allowlist for that key. If a key is present but set to an empty array, the effective allowlist for that type is empty — it does **not** fall back to the IDE allowlist.

## How it appears in Cursor Settings

When `permissions.json` defines an allowlist, Cursor Settings notes that the allowlist is configured via `~/.cursor/permissions.json`.

- If the allowlist is controlled by `permissions.json`, the editor becomes read-only and shows the file-defined entries. The "Add to allowlist" option is not available for that allowlist type.
- If the allowlist is admin-controlled, the editor becomes read-only and shows the admin-defined entries.

## MCP allowlist format

Each entry is a `server:tool` string. Both parts are matched case-insensitively. The `*` wildcard matches any value for that part.

| Pattern             | Matches                                                      |
| :------------------ | :----------------------------------------------------------- |
| `my-server:my_tool` | Exactly the tool `my_tool` from the server named `my-server` |
| `my-server:*`       | All tools from `my-server`                                   |
| `*:my_tool`         | The tool `my_tool` from any server                           |
| `*:*`               | All tools from all servers                                   |

The server name is the key you used in `mcp.json` (e.g. `"github"`, `"linear"`). Glob-style `*` patterns also work inside names (e.g. `my-server:list_*` matches `list_issues`, `list_users`, etc.).

Entries that do not contain a `:` are ignored.

## Terminal allowlist format

Each entry is a command or command prefix string.

| Pattern        | Matches                                                                                          |
| :------------- | :----------------------------------------------------------------------------------------------- |
| `git`          | Any command starting with `git` (e.g. `git status`, `git diff`)                                  |
| `git status`   | Only `git status` (and anything starting with `git status `)                                     |
| `npm:install*` | `npm install`, `npm install express`, etc. The `:` separates the base command from an args glob. |

Matching is case-sensitive and uses prefix semantics: `git` matches `git status` but not `gitk`.

## Examples

### Set MCP allowlist globally

```jsonc
{
  // Overrides the in-app MCP allowlist entirely.
  "mcpAllowlist": [
    "github:*",
    "linear:list_issues"
  ]
}
```

### Set terminal allowlist globally

```jsonc
{
  "terminalAllowlist": [
    "git",
    "npm",
    "yarn",
    "pnpm",
    "cargo",
    "make"
  ]
}
```

### Override only one allowlist type

If `permissions.json` only defines `mcpAllowlist`, the MCP allowlist is taken from the file while the terminal allowlist remains under IDE control:

```jsonc
{
  "mcpAllowlist": [
    "github:*",
    "linear:*"
  ]
}
```

Any MCP entries previously set in Cursor Settings are ignored while this file is present. Terminal allowlist entries in Cursor Settings still apply.

### Combined setup

```jsonc
{
  "mcpAllowlist": [
    "github:*",
    "linear:*",
    "notion:search"
  ],
  "terminalAllowlist": [
    "git",
    "npm",
    "cargo build",
    "cargo test"
  ]
}
```

## Notes

- **Auto-run mode required**: `permissions.json` only takes effect when auto-run is enabled in Cursor Settings (either "Auto-Run in Sandbox" or "Run Everything"). In "Ask Every Time" mode, the allowlists are not consulted.
- **Not a security boundary**: Allowlists are best-effort convenience. They are not a security guarantee. See [Agent Security](https://cursor.com/docs/agent/security.md) for details.
- **Override, not merge**: When `permissions.json` defines an allowlist key, it fully replaces the in-app allowlist for that type. Entries configured in Cursor Settings are not merged in.
- **IDE display**: When `permissions.json` controls an allowlist, the corresponding settings section becomes read-only and shows the file-defined entries. The "Add to allowlist" option is hidden.
- **CLI permissions are separate**: The Cursor CLI has its own permissions system. See [CLI Permissions](https://cursor.com/docs/cli/reference/permissions.md) for that reference.


---

## Sitemap

[Overview of all docs pages](/llms.txt)
