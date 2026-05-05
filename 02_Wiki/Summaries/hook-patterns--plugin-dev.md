---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/hook-development/references/patterns.md
title: "plugin-dev: hook-development patterns reference"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Hooks, MCP-server]
concepts_referenced: []
---

Reference doc inside `plugin-dev`'s `hook-development` skill. Common hook implementation patterns for Claude Code plugins.

**10 patterns**:

1. **Security validation** — `PreToolUse` matcher `Write|Edit` with prompt-type hook checking file path against `/etc`, `.env`, traversal `..`, returns `approve`/`deny`.

2. **Test enforcement** — `Stop` hook with prompt: review transcript; if Write/Edit used and tests not run, block with reason.

3. **Context loading** — `SessionStart` command-type hook running bash script to detect project type (`package.json` → Node.js, `Cargo.toml` → Rust) and write env vars to `$CLAUDE_ENV_FILE`.

4. **Notification logging** — `Notification` matcher `*` running script to log to file/external system.

5. **MCP tool monitoring** — `PreToolUse` matcher `mcp__.*__delete.*` with prompt verifying intentional deletion / undoability / backups.

6. **Build verification** — `Stop` prompt: if Write/Edit used, verify `npm run build`/`cargo build`/etc was run.

7. **Permission confirmation** — `PreToolUse` matcher `Bash` with prompt: if command contains rm/delete/drop, return `ask`; else `approve`.

8. **Code quality checks** — `PostToolUse` `Write|Edit` running script that reads stdin JSON, extracts `tool_input.file_path`, runs `eslint` on `.js`/`.ts` files.

9. **Temporarily active hooks** — script checks for flag file (`.enable-security-scan`); exits 0 quickly if not present. `touch`/`rm` to enable/disable. Requires CC restart.

10. **Configuration-driven hooks** — script reads JSON config (`.claude/my-plugin.local.json`), applies dynamic limits (`strictMode`, `maxFileSize`, `allowedPaths`). Skip if `strictMode` false. Returns deny via stderr + exit 2 when limit exceeded.

**Pattern combinations**: stack `PreToolUse`+`Stop`+`SessionStart` for multi-layered protection.

**Hook shell script pattern**: read stdin JSON → `jq -r '.tool_input.file_path'` → conditional logic → emit decision via stderr + exit 2 to deny.

**Use cases mapping**:
- Security/dangerous commands → patterns 1, 7
- Quality enforcement → patterns 2, 6, 8
- Project context → pattern 3
- Audit/compliance → pattern 4
- MCP safety → pattern 5
- Opt-in/temporary → pattern 9
- Per-project tunable → pattern 10
