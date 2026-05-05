---
type: summary
source: 01_Raw/code.claude.com/docs/en/devcontainer.md
source_url: https://code.claude.com/docs/en/devcontainer
title: "Development containers"
summarized_at: 2026-05-05
entities_referenced: [Sandboxing, Settings, Auto-mode, Permission-mode, MCP-server, IDE-integration, Enterprise-gateway]
concepts_referenced: []
---

Run Claude Code inside a [Dev Container](https://containers.dev/) for consistent, isolated environments per team. Commands Claude runs execute inside the container; file edits appear in the local repo via bind mount.

**Install** via the Claude Code Dev Container Feature: add to `.devcontainer/devcontainer.json`:
```json
{
  "image": "mcr.microsoft.com/devcontainers/base:ubuntu",
  "features": {
    "ghcr.io/anthropics/devcontainer-features/claude-code:1.0": {}
  }
}
```
Version tag `:1.0` pins the install script, NOT the CLI version. Feature installs latest CLI which auto-updates by default. To pin: install via `npm install -g @anthropic-ai/claude-code@X.Y.Z` in Dockerfile + set `DISABLE_AUTOUPDATER=1`.

**VS Code extension** auto-installed alongside; other editors ignore.

**Auth**: `claude` then browser flow (Anthropic) or cloud creds (Bedrock/Vertex/Foundry — pass via `containerEnv`/Codespaces secret/workload identity, never mount host credential files). Browser callback that doesn't reach container → paste code at "Paste code here if prompted" prompt.

**Persist `~/.claude` across rebuilds** with a named volume:
```json
"mounts": [
  "source=claude-code-config,target=/home/node/.claude,type=volume"
]
```
Use `${devcontainerId}` in source name to isolate state per project. If mounted elsewhere, set `CLAUDE_CONFIG_DIR`. In Codespaces store `ANTHROPIC_API_KEY` or `CLAUDE_CODE_OAUTH_TOKEN` (from `claude setup-token`) as Codespaces secret.

**Org policy** via `/etc/claude-code/managed-settings.json` (highest precedence in settings hierarchy) — copied via Dockerfile. **Caveat**: anyone with repo write access can edit. For unbypassable policy use server-managed settings or MDM.

Set env vars in `containerEnv` (e.g., `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`, `DISABLE_AUTOUPDATER`).

**Network egress restriction**: reference `init-firewall.sh` blocks all outbound except needed domains. Requires `NET_ADMIN` + `NET_RAW` in `runArgs`.

**`--dangerously-skip-permissions` in container**: CLI rejects when launched as root → confirm `remoteUser` non-root. Pair with network restrictions. To prevent entirely: `permissions.disableBypassPermissionsMode: "disable"` in managed settings. Alternative with safety: auto mode.

**Reference container**: `anthropics/claude-code/.devcontainer/` combines CLI, firewall, persistent volumes, Zsh shell — example, not a maintained base image.

**Warning**: `--dangerously-skip-permissions` doesn't prevent malicious projects from exfiltrating things accessible inside container, including `~/.claude` credentials. Only use with trusted repos. Don't mount `~/.ssh` or cloud credential files; prefer repo-scoped/short-lived tokens.
