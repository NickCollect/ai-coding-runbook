---
type: summary
source: 01_Raw/code.claude.com/docs/en/claude-directory.md
source_url: https://code.claude.com/docs/en/claude-directory
title: "Explore the .claude directory"
summarized_at: 2026-05-05
entities_referenced: [Settings, Skill, Subagent, Hooks, Memory, Plugin, MCP-server, Slash-command, Output-style, Status-line]
concepts_referenced: []
---

Reference for everything Claude Code reads from the project root and `~/.claude/`. Raw is a giant interactive explorer (JSX-driven) — this summary distills the file/folder semantics.

**Project root files (outside `.claude/`)**
- `CLAUDE.md` — Project instructions loaded into context every session. Target <200 lines. `/memory` to edit. Also accepted at `.claude/CLAUDE.md`.
- `.mcp.json` — Project-scoped MCP servers committed to git. Use `${ENV_VAR}` for secrets. Personal servers → `~/.claude.json` via `claude mcp add --scope user`.
- `.worktreeinclude` — `.gitignore`-syntax list of gitignored files (e.g. `.env`) to copy into new worktrees created via `--worktree`, `EnterWorktree` tool, or subagent `isolation: worktree`. Git-only — non-git VCS users must copy in their `WorktreeCreate` hook.

**Inside `.claude/`** (project-level; mirrored at `~/.claude/` for user-level)

| Path | Purpose | Notes |
|---|---|---|
| `settings.json` | Permissions, hooks, statusLine, model, env, outputStyle | Enforced (vs CLAUDE.md which is guidance). Overrides `~/.claude/settings.json`. CLI flags + managed settings override this. |
| `settings.local.json` | Personal per-project overrides | gitignored automatically (added to `~/.config/git/ignore`). Same schema. |
| `rules/` | Topic-scoped instructions, optionally gated by file paths | Rules without `paths:` load at session start; with `paths:` glob, load when matching file enters context. Subdirs OK. |
| `skills/<name>/SKILL.md` | Reusable prompts invoked by name | `/<name>` invocation. `disable-model-invocation: true` for user-only; `user-invocable: false` to hide from menu. `$ARGUMENTS` / `$0`, `$1`. Bundle supporting files; use `${CLAUDE_SKILL_DIR}` placeholder in bash injections. |
| `commands/<name>.md` | Single-file slash commands | Same `/name` mechanism as skills; new workflows should use skills. Skill takes precedence on name collision. |
| `agents/` | Subagent definitions | Each is an `.md` file with frontmatter (tools, model, prompt). |
| `hooks/` | Hook scripts referenced by `settings.json` | Hooks run user scripts on events (e.g. `PostToolUse`). |
| `memory/` | Persistent memory state | |
| `plugins/` | Installed plugins | |
| `output-styles/` | Custom system-prompt styles | Selected via `outputStyle` setting. |

Settings precedence (low → high): user `~/.claude/settings.json` → project `settings.json` → project `settings.local.json` → CLI flags → managed enterprise settings. Array settings (e.g. `permissions.allow`) **combine** across scopes; scalar settings (e.g. `model`) take the most specific value.

Skills vs commands: same `/name` invocation, skills are richer (folder + supporting files + auto-invocation). Commands remain supported but new workflows should use skills.

Project `.claude/` is meant to be committed (team-shared); `.local.json` files and a few personal configs are gitignored. Coexists with other tools' config.
