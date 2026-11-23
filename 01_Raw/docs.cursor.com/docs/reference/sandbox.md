---
source_url: https://cursor.com/docs/reference/sandbox
fetched_at: 2026-11-23T08:28:26.072416+00:00
fetch_method: mintlify_md
---

# sandbox.json reference

Configure [sandbox](https://cursor.com/docs/agent/security/run-modes.md#sandboxing) behavior with a `sandbox.json` file to control network access, filesystem paths, and more.

## File locations

Place `sandbox.json` in either or both of these locations:

| Location                           | Scope                       | Priority |
| :--------------------------------- | :-------------------------- | :------- |
| `~/.cursor/sandbox.json`           | All workspaces (per-user)   | Lower    |
| `<workspace>/.cursor/sandbox.json` | Single workspace (per-repo) | Higher   |

Both files are optional. When both exist, they are merged with per-repo settings taking priority. Enterprise team-admin policies and Cursor's hardcoded security rules layer on top and cannot be weakened by either file.

Cursor Nightly reads the per-user file from `~/.cursor-nightly/sandbox.json` instead of `~/.cursor/sandbox.json`. The CLI always reads `~/.cursor/sandbox.json`. The per-repo `<workspace>/.cursor/sandbox.json` works in every build.

## Top-level fields

All fields are optional. Missing fields use the defaults shown below.

| Field                      | Type                        | Default                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                       |
| :------------------------- | :-------------------------- | :---------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`                     | string                      | `"workspace_readwrite"` | Sandbox mode. `"workspace_readwrite"` gives read/write access in the workspace. `"workspace_readonly"` restricts to read-only. `"insecure_none"` disables the sandbox entirely.                                                                                                                                                                                                                                                   |
| `additionalReadwritePaths` | `string[]`                  | `[]`                    | Extra paths the agent can read and write. Only applies when `type` is `"workspace_readwrite"`.                                                                                                                                                                                                                                                                                                                                    |
| `additionalReadonlyPaths`  | `string[]`                  | `[]`                    | Extra paths the agent can read.                                                                                                                                                                                                                                                                                                                                                                                                   |
| `readBoundary`             | `"system"` \| `"workspace"` | `"system"`              | [Read access](https://cursor.com/docs/agent/security/run-modes.md#read-access) mode. `"workspace"` asks before the agent reads files outside the workspace and limits what sandboxed commands can read. Requires Cursor 3.23 or later.                                                                                                                                                                                            |
| `additionalReadPaths`      | `string[]`                  | `[]`                    | Read Allowlist paths and globs the agent can read outside the workspace. Only applies when `readBoundary` is `"workspace"`.                                                                                                                                                                                                                                                                                                       |
| `disableTmpWrite`          | `boolean`                   | `false`                 | When `true`, removes default write access to `/tmp` and system temp directories.                                                                                                                                                                                                                                                                                                                                                  |
| `privateTmp`               | `boolean`                   | `false`                 | Linux only. When `true`, `/tmp` inside sandboxed commands becomes the workspace's own [temporary folder](https://cursor.com/docs/reference/sandbox.md#temporary-files). Only applies when `readBoundary` is `"workspace"` and `disableTmpWrite` is off. Requires CLI v2026.11.17 or later. In the IDE, requires Cursor 3.32 or later, first available on the [Nightly channel](https://cursor.com/docs/account/update-access.md). |
| `enableSharedBuildCache`   | `boolean`                   | `false`                 | Redirects build-tool caches (npm, cargo, pip, etc.) to a shared tmpdir so sandboxed and unsandboxed commands share the same caches.                                                                                                                                                                                                                                                                                               |

## `networkPolicy` object

| Field     | Type                  | Default  | Description                                                                                   |
| :-------- | :-------------------- | :------- | :-------------------------------------------------------------------------------------------- |
| `default` | `"allow"` \| `"deny"` | `"deny"` | Action when no allow/deny rule matches.                                                       |
| `allow`   | `string[]`            | `[]`     | Patterns to allow. Supports exact domains, wildcards, and CIDR notation.                      |
| `deny`    | `string[]`            | `[]`     | Patterns to deny. Highest priority; always blocks, even if a pattern also appears in `allow`. |

## Network pattern syntax

The `allow` and `deny` arrays accept three pattern formats:

| Format       | Example                | Matches                                                        |
| :----------- | :--------------------- | :------------------------------------------------------------- |
| Exact domain | `"registry.npmjs.org"` | That exact host                                                |
| Wildcard     | `"*.example.com"`      | Any subdomain of `example.com`, including `example.com` itself |
| CIDR         | `"10.0.0.0/8"`         | Any IP in that range                                           |

**Key rules:**

- Deny always beats allow. If a host matches both lists, it is blocked.
- Private/RFC 1918 addresses (`10.x`, `172.16.x`, `192.168.x`, `127.x`) and cloud metadata endpoints (`169.254.169.254`) are blocked by default to prevent SSRF.
- IPv6 private addresses (`::1`, `fe80::/10`, `fc00::/7`) are also blocked.
- URL paths are ignored; matching is domain/IP only.

## How policies merge

When multiple policy sources exist, they merge in priority order:

```text
per-user  <  per-repo  <  team-admin  <  hardcoded
(lowest)                                (highest)
```

Merge rules:

- **Paths** (`additionalReadwritePaths`, `additionalReadonlyPaths`): unioned across all sources.
- **`readBoundary`**: per-repo replaces per-user. A team-admin `"workspace"` policy applies to everyone.
- **`additionalReadPaths`**: per-repo replaces per-user, then the team-admin Read Allowlist is added. If the admin turns off user extensions, only the admin list applies.
- **Network allow lists**: unioned, unless a team-admin allowlist is present (which replaces the union).
- **Network deny lists**: always unioned.
- **`networkPolicy.default`**: `"deny"` wins over `"allow"`.
- **Restrictive booleans** (`disableTmpWrite`, `networkPolicyStrict`): `true` wins.
- **`privateTmp`**: per-repo replaces per-user.

## Protected paths

Certain paths are always write-protected, regardless of your `sandbox.json` configuration:

- `.cursor/*.json`, `.cursor/**/*.json`, `.cursor/.workspace-trusted`
- `.claude/*.json`, `.claude/**/*.json`
- `.vscode/**`
- `.code-workspace`
- `.git/hooks/**`, `.git/config`, `.git/info/attributes`
- `.cursorignore`

The following `.cursor` subdirectories **are** writable: `rules/`, `commands/`, `worktrees/`, `skills/`, `agents/`.

SSL certificate paths and `~/.ssh` are always readable when `readBoundary` is `"system"`. With `"workspace"`, sandboxed commands can still read certificate stores, but only `~/.ssh/known_hosts` from `~/.ssh`.

## Temporary files

With `readBoundary` set to `"workspace"` and `disableTmpWrite` off, Cursor keeps each workspace's temporary files in a scratch folder named `cursor-sandbox-<workspace>`. The default `"system"` boundary has no scratch folder, and neither does Windows. `<workspace>` is the workspace's absolute path with each run of non-alphanumeric characters replaced by `-` and leading and trailing dashes dropped, so `/home/me/repo` gets `cursor-sandbox-home-me-repo`.

The scratch folder lives in `$TMPDIR`, or in `/tmp` when `TMPDIR` is unset. Inside sandboxed commands, `$TMPDIR` points to its `tmp/` subfolder. With `privateTmp` on, sandboxed commands see that same `tmp/` folder at `/tmp`.

Under the workspace boundary, to keep temporary files off a small `/tmp`, set `TMPDIR` to a folder on a larger disk in the shell that starts the CLI. With `TMPDIR=/data/tmp`, sandboxed commands use `/data/tmp/cursor-sandbox-<workspace>/tmp`.

- **Ownership.** The scratch folder and its `tmp/` subfolder must be real folders, owned by you, and not writable by group or others. Otherwise Cursor uses no scratch folder: `privateTmp` isn't applied and `$TMPDIR` isn't redirected. The `TMPDIR` folder itself can be shared, for example with mode `1777`.
- **Location.** Leave `TMPDIR` unset, set it to `/tmp`, or put it outside `/tmp`. When `TMPDIR` is any folder inside `/tmp`, such as `/tmp/me` or `/tmp/user/1000`, Cursor skips `privateTmp` and each command prints `sandbox: privateTmp not applied: the scratch dir of this sandbox is under /tmp but not directly in it`. Writes to `/tmp` then fail under `readBoundary: "workspace"`, while `$TMPDIR` keeps working.
- **Other skip conditions.** Cursor also skips `privateTmp` and prints `sandbox: privateTmp not applied: <reason>` on stderr when the workspace, an `additionalReadwritePaths` entry, or the main repository of a linked Git worktree is `/tmp`, contains `/tmp`, or is inside `/tmp`.
- **Paths hidden under `/tmp`.** While `privateTmp` is on, `additionalReadPaths` and `additionalReadonlyPaths` entries inside the host's `/tmp` are hidden from sandboxed commands.
- **Inside the workspace.** A `TMPDIR` inside the workspace works, but the scratch folder shows up in `git status`. Add it to `.gitignore`.

## Environment variables

In addition to the configuration above, Cursor injects environment variables into sandboxed child processes, including `CURSOR_SANDBOX`, `CURSOR_ORIG_UID`, and `CURSOR_ORIG_GID`. See [Run Modes: Environment variables](https://cursor.com/docs/agent/security/run-modes.md#environment-variables) for the full list and usage guidance.

## Examples

### Allow specific domains

```json
{
  "networkPolicy": {
    "default": "deny",
    "allow": [
      "registry.npmjs.org",
      "pypi.org",
      "*.githubusercontent.com"
    ]
  }
}
```

Network traffic is denied by default. Only the listed domains are reachable.

### Allow all network

```json
{
  "networkPolicy": {
    "default": "allow"
  }
}
```

All outbound network traffic is permitted inside the sandbox.

### Full-stack web project

A project where the agent needs to install packages, pull container images, access a database on the local network, and read a shared design-tokens repo:

```json
{
  "networkPolicy": {
    "default": "deny",
    "allow": [
      "registry.npmjs.org",
      "registry.yarnpkg.com",
      "pypi.org",
      "files.pythonhosted.org",
      "*.docker.io",
      "ghcr.io",
      "*.googleapis.com"
    ],
    "deny": [
      "*.internal.corp.example.com"
    ]
  },
  "additionalReadwritePaths": [
    "/home/me/.docker"
  ],
  "additionalReadonlyPaths": [
    "/opt/shared/design-tokens"
  ],
  "enableSharedBuildCache": true
}
```

This configuration lets the agent:

- Install npm/pip packages and pull Docker images.
- Hit Google Cloud APIs.
- Block access to internal corporate services.
- Write to `~/.docker` for container operations.
- Read (but not modify) a shared design-tokens directory.
- Share npm/pip/cargo caches between sandboxed and unsandboxed runs.


---

## Sitemap

[Overview of all docs pages](/llms.txt)
