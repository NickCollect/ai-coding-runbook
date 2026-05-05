---
type: summary
source: 01_Raw/code.claude.com/docs/en/sandboxing.md
source_url: https://code.claude.com/docs/en/sandboxing
title: "Sandboxing"
summarized_at: 2026-05-05
entities_referenced: [Sandboxing, Permission-mode, Settings, MCP-server, Computer-use]
concepts_referenced: []
---

OS-level filesystem + network isolation for Claude Code's Bash tool. Reduces approval fatigue (safe commands inside the sandbox don't prompt) while triggering immediate notifications on boundary attempts. Built-in file tools (Read/Edit/Write) use the permission system directly, NOT the sandbox.

**Effective sandboxing requires BOTH layers** — without network isolation a compromised agent could exfiltrate; without filesystem isolation it could backdoor system resources.

**OS primitives**:
- macOS — Seatbelt
- Linux / WSL2 — `bubblewrap`
- WSL1 — NOT supported (lacks namespace primitives)

**Filesystem isolation**: write access defaults to cwd + subdirs, read access defaults to entire computer (minus denied dirs). Configurable via `sandbox.filesystem.allowWrite` / `denyWrite` / `denyRead` / `allowRead`. Enforced at OS level, so applies to ALL subprocesses (kubectl, terraform, npm) — not just Claude's file tools.

**Network isolation**: proxy server (outside the sandbox) enforces domain allowlist. New domains prompt unless `allowManagedDomainsOnly` is set. **Built-in proxy does NOT terminate / inspect TLS** — domain decisions made from client-supplied hostname only. Domain fronting is a known risk; use a custom TLS-terminating proxy for stronger guarantees.

**Setup**:
- macOS: works out-of-box with Seatbelt
- Linux: `apt install bubblewrap socat` / `dnf install bubblewrap socat`
- WSL2: same as Linux. Sandboxed commands cannot launch Windows binaries (`cmd.exe`, `powershell.exe`, `/mnt/c/`); add to `excludedCommands` to run outside sandbox.

**Enable**: `/sandbox` slash command opens menu. If deps missing, menu shows install instructions. Default: warn-and-run-without-sandbox if can't start. `sandbox.failIfUnavailable: true` makes that a hard failure (managed deployments).

**Two modes**:
- **Auto-allow**: sandboxed commands are auto-approved. Commands that can't be sandboxed (need non-allowed network host) fall back to regular permission flow. `rm`/`rmdir` targeting `/`, `$HOME`, or critical system paths still trigger prompt. Independent of permission mode setting.
- **Regular permissions**: all bash commands go through standard prompt flow even when sandboxed.

**`allowWrite` path prefix conventions** (different from `Read`/`Edit` permission rules!):
| Prefix | Meaning |
|---|---|
| `/` | absolute (filesystem root) |
| `~/` | home directory |
| `./` or no prefix | project root (project settings) OR `~/.claude` (user settings) |

Older `//path` for absolute still works. `allowWrite`/`denyWrite`/`denyRead`/`allowRead` arrays **MERGE across all settings scopes** (not replace) — users/projects can extend without overriding higher-priority scope. `allowRead` takes precedence over `denyRead` (re-allow within denied region). When `allowManagedReadPathsOnly` enabled, only managed `allowRead` entries respected.

Block reading entire home but allow project:
```json
"sandbox": {
  "filesystem": {
    "denyRead": ["~/"],
    "allowRead": ["."]
  }
}
```

**Compatibility caveats**:
- `watchman` incompatible — use `jest --no-watchman`
- `docker` incompatible — `excludedCommands: ["docker *"]` to escape
- Many CLI tools request specific hosts — grant once, applies forever

**Escape hatch**: `dangerouslyDisableSandbox` parameter — Claude can request running outside sandbox when blocked; goes through normal permission flow. Disable entirely with `allowUnsandboxedCommands: false` — then commands must run sandboxed or be in `excludedCommands`.

**Security limitations** (from raw):
- No TLS inspection — broad domains like `github.com` create exfiltration paths via domain fronting
- `allowUnixSockets` for `/var/run/docker.sock` effectively grants host access via docker socket
- Allowing writes to dirs containing `$PATH` executables, system config, or `.bashrc`/`.zshrc` enables privilege escalation
- Linux `enableWeakerNestedSandbox` lets it run inside Docker without privileged namespaces but considerably weakens security

**Sandbox vs permissions** (complementary):
- Permissions — which tools, which inputs (all tools)
- Sandbox — what Bash + child processes can access at OS level

**Open source**: `npx @anthropic-ai/sandbox-runtime <command>` — sandbox-runtime npm package can sandbox arbitrary commands, including MCP servers. Source: `anthropic-experimental/sandbox-runtime`.
