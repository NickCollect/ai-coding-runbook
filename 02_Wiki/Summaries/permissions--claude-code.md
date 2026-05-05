---
type: summary
source: 01_Raw/code.claude.com/docs/en/permissions.md
source_url: https://code.claude.com/docs/en/permissions
title: "Configure permissions"
summarized_at: 2026-05-05
entities_referenced: [Permission-mode, Settings, Hooks, Sandboxing, MCP-server, Subagent, Auto-mode, Plugin-marketplace, Channel]
concepts_referenced: [Channel]
---

Fine-grained permission rules, modes, and managed policies for Claude Code (CLI/main docs version, distinct from the Agent-SDK permissions doc).

**Tiered system**:
| Tool type | Approval required | "Yes, don't ask again" |
|---|---|---|
| Read-only (file reads, Grep) | No | N/A |
| Bash | Yes | Permanently per project dir + command |
| File modification | Yes | Until session end |

**`/permissions` UI**: lists rules + source files. Allow / Ask / Deny rule types.
**Evaluation: deny → ask → allow, first match wins. Deny always precedes.**

**Permission modes**: `default`, `acceptEdits` (auto-approves edits + common FS bash like `mkdir`/`touch`/`mv`/`cp` for cwd or `additionalDirectories`), `plan` (analysis only), `auto` (research preview, classifier-driven), `dontAsk` (denies anything not pre-approved), `bypassPermissions` (skips ALL prompts but still circuit-breaks `rm -rf /` / `rm -rf ~` and writes to `.git`/`.claude`/`.vscode`/`.idea`/`.husky`). Disable via `permissions.disableBypassPermissionsMode: "disable"` (works at any layer; lock yourself out from user settings).

**Rule syntax**: `Tool` (matches all uses) or `Tool(specifier)`. `Bash(*)` ≡ `Bash`.

**Bash wildcards**: `*` at any position. **Space matters**: `Bash(ls *)` matches `ls -la` not `lsof`; `Bash(ls*)` matches both. `:*` suffix ≡ trailing ` *`. `:*` only recognized at end; `Bash(git:* push)` treats `:` as literal.

**Compound commands**: Claude Code is shell-aware; `Bash(safe-cmd *)` doesn't allow `safe-cmd && other`. Recognized separators: `&&`, `||`, `;`, `|`, `|&`, `&`, newlines. Each subcommand must match independently. Approving compound with "don't ask again" saves separate rules per subcommand (up to 5).

**Process wrappers stripped before matching**: `timeout`, `time`, `nice`, `nohup`, `stdbuf`, bare `xargs` (only with no flags). NOT stripped: env runners like `direnv exec`, `devbox run`, `mise exec`, `npx`, `docker exec` — write specific rules per inner command (`Bash(devbox run npm test)`).

**Always prompt** (cannot be auto-approved by prefix): `watch`, `setsid`, `ionice`, `flock`, `find -exec`/`-delete`. Need exact-match rule.

**Built-in read-only Bash** (always run without prompt): `ls`, `cat`, `head`, `tail`, `grep`, `find`, `wc`, `diff`, `stat`, `du`, `cd`, read-only `git` forms. Not configurable. Unquoted globs OK for fully-read-only commands; commands like `find`/`sort`/`sed`/`git` still prompt with unquoted globs (could expand to `-delete` etc.). `cd packages/api && ls` runs without prompt; `cd && git ...` always prompts.

**URL filtering warning**: Bash patterns like `Bash(curl http://github.com/ *)` are FRAGILE — fail on `-X` before URL, `https`, redirects, env vars. Better: deny `curl`/`wget` and use `WebFetch(domain:github.com)`, OR use PreToolUse hook to validate URLs.

**PowerShell rules**: same shape as Bash. AST-parsed, each subcommand checked. Aliases canonicalized — `Get-ChildItem` rule matches `gci`/`ls`/`dir`. Case-insensitive. Pipeline `|`, `;`, and `&&`/`||` (PS 7+) split.

**Read/Edit rules** follow gitignore spec with 4 path types:
- `//path` = absolute filesystem path (e.g., `Read(//Users/alice/secrets/**)`)
- `~/path` = home dir
- `/path` = relative to project root (NOT absolute!)
- `path` or `./path` = relative to cwd

Windows paths normalized to POSIX (`C:\Users\alice` → `/c/Users/alice`); `//c/**/.env` matches drive C; `//**/.env` matches all drives. **Symlinks**: rules check both the symlink AND its target. Allow rules require BOTH match (else prompts). Deny rules trigger if EITHER matches.

**Important**: Read/Edit deny rules apply to Claude's built-in tools, NOT Bash subprocesses. `Read(./.env)` blocks Read tool but doesn't stop `cat .env` in Bash. For OS-level enforcement use sandbox.

**WebFetch**: `WebFetch(domain:example.com)`.

**MCP**: `mcp__puppeteer` (any tool from server), `mcp__puppeteer__*` (wildcard, equivalent), `mcp__puppeteer__puppeteer_navigate` (specific tool).

**Agent**: `Agent(Explore)`, `Agent(Plan)`, `Agent(my-custom-agent)`. Use deny array or `--disallowedTools` to disable specific subagents.

**Hooks extending permissions**: PreToolUse hooks run before permission prompt. Hook `allow`/`ask` does NOT bypass deny/ask rules (deny-first preserved). Hook exit code 2 takes precedence over allow rules. Pattern: allow `Bash` broadly + register PreToolUse hook to reject specific commands.

**Working directories**: extend via `--add-dir <path>` (CLI), `/add-dir` (in session), or `additionalDirectories` (settings). Files follow same rules as cwd.

**Additional directories grant FILE access, not configuration**:
| Loaded from `--add-dir` | |
|---|---|
| Skills (`.claude/skills/`) | Yes, with live reload |
| `enabledPlugins`, `extraKnownMarketplaces` | Yes |
| CLAUDE.md / `.claude/rules/` / `CLAUDE.local.md` | Only with `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1` |
Everything else (subagents, commands, output styles, hooks, other settings) discovered only from cwd+parents, `~/.claude/`, managed.

**Sandboxing complement**: permissions = which tools/files/domains across all tools; sandboxing = OS-level Bash restriction (also covers child processes). Filesystem restrictions in sandbox use Read/Edit deny rules. Network: WebFetch + sandbox `allowedDomains`/`deniedDomains`. Default `autoAllowBashIfSandboxed: true` lets sandboxed Bash run without prompts (sandbox boundary substitutes), but `rm`/`rmdir` of `/`/`~`/critical paths still prompts.

**Managed-only settings** (only effective from managed policy):
- `allowedChannelPlugins`, `channelsEnabled`
- `allowManagedHooksOnly`, `allowManagedMcpServersOnly`, `allowManagedPermissionRulesOnly`
- `blockedMarketplaces`, `strictKnownMarketplaces`, `pluginTrustMessage`
- `forceRemoteSettingsRefresh` (fail-closed startup)
- `sandbox.filesystem.allowManagedReadPathsOnly`, `sandbox.network.allowManagedDomainsOnly`
- `wslInheritsWindowsSettings`

Remote Control + web sessions controlled by claude.ai admin settings, NOT a managed-settings key.

**Settings precedence** (high → low): managed → CLI args → local project → shared project → user. Any-level deny wins.
