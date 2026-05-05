---
type: summary
source: 01_Raw/code.claude.com/docs/en/skills.md
source_url: https://code.claude.com/docs/en/skills
title: "Extend Claude with skills"
summarized_at: 2026-05-05
entities_referenced: [Skill, Slash-command, Subagent, Hooks, Plugin, Settings, Memory]
concepts_referenced: []
---

User-facing guide to Claude Code Skills — `SKILL.md` files that extend Claude's toolkit. Invoked via `/skill-name` or auto-loaded by Claude when description matches.

**Custom commands merged into skills**: `.claude/commands/deploy.md` and `.claude/skills/deploy/SKILL.md` both create `/deploy`. Old commands keep working; skills add bundled supporting files + invocation control + auto-load.

Skills follow the [Agent Skills](https://agentskills.io) open standard, with Claude Code extensions: invocation control, subagent execution, dynamic context injection.

**Bundled skills** ship in every session (`/simplify`, `/batch`, `/debug`, `/loop`, `/claude-api`). Listed in commands reference, marked "Skill".

**Storage / scope**:
| Location | Path | Applies to |
|---|---|---|
| Enterprise | managed settings | All users in org |
| Personal | `~/.claude/skills/<name>/SKILL.md` | All your projects |
| Project | `.claude/skills/<name>/SKILL.md` | This project only |
| Plugin | `<plugin>/skills/<name>/SKILL.md` | Where plugin is enabled |

Precedence: enterprise > personal > project. Plugin skills are namespaced (`plugin-name:skill-name`) so they cannot conflict. If skill and command share a name, **skill takes precedence**.

Live change detection: `~/.claude/skills/`, project `.claude/skills/`, and `--add-dir` `.claude/skills/` are watched — adding/editing/removing applies within current session. Creating a top-level skills dir mid-session needs restart.

Auto-discovery from nested dirs: when working in `packages/frontend/`, `packages/frontend/.claude/skills/` is also discovered (monorepo support).

`--add-dir` flag is exception-grant for file access, but `.claude/skills/` IS auto-loaded from added dirs (other config like agents/commands/output styles is NOT).

**SKILL.md frontmatter** (all optional, only `description` recommended):
| Field | Purpose |
|---|---|
| `name` | Display name (defaults to dir name; lowercase/numbers/hyphens, max 64 chars) |
| `description` | When to use; combined with `when_to_use` capped at 1,536 chars |
| `when_to_use` | Trigger phrases / examples |
| `argument-hint` | Autocomplete hint (e.g. `[issue-number]`) |
| `arguments` | Named positional args (space string or YAML list) |
| `disable-model-invocation: true` | User-only, hidden from Claude's context |
| `user-invocable: false` | Hidden from `/` menu, Claude-only |
| `allowed-tools` | Tools auto-permitted while skill active |
| `model` | Override model for the turn (or `inherit`) |
| `effort` | `low`/`medium`/`high`/`xhigh`/`max` |
| `context: fork` | Run in forked subagent context |
| `agent` | Which subagent type when forking |
| `hooks` | Skill-scoped hook lifecycle |
| `paths` | Glob patterns limiting auto-activation to matching files |
| `shell` | `bash` (default) or `powershell` for `` !`...` `` execution |

**String substitutions**: `$ARGUMENTS`, `$ARGUMENTS[N]`, `$N` (shorthand), `$name` (named arg), `${CLAUDE_SESSION_ID}`, `${CLAUDE_EFFORT}`, `${CLAUDE_SKILL_DIR}` (path to skill's dir, useful for plugin-portable script refs).

**Supporting files**: bundle `reference.md`, `examples.md`, `scripts/helper.py` etc. Reference from SKILL.md so Claude knows what's available. Scripts run via `${CLAUDE_SKILL_DIR}/scripts/...`. Tip: keep SKILL.md <500 lines.

**Dynamic context injection**:
- `` !`<command>` `` runs shell command BEFORE Claude sees content; output replaces placeholder. Preprocessing (Claude doesn't execute it).
- Multi-line: fenced code block opened with ` ```! `.
- Disable globally via `disableSkillShellExecution: true` in settings (managed-only protection useful). Bundled/managed skills unaffected.

**Subagent integration** (`context: fork`):
- Skill content becomes subagent prompt; agent type = execution env.
- Two patterns: skill-runs-in-fork (above) vs subagent-with-skills-field (preloads skills into custom subagent).
- Warning: only useful for skills with explicit task instructions, not pure reference content.

**Skill content lifecycle**:
- On invocation, rendered SKILL.md enters convo as one message and stays for session. Not re-read on later turns.
- Auto-compaction re-attaches most recent invocation of each skill (first 5,000 tokens), shared 25,000 token budget across all re-attached skills. Older invocations dropped first.

**Restrict Claude's skill access**:
- Deny Skill tool in `/permissions` to disable all.
- `Skill(name)` / `Skill(name *)` rules for specific skills.
- `disable-model-invocation: true` removes from Claude's context entirely.
- Note: `user-invocable` only hides from menu, doesn't block programmatic Skill tool access.

**Description char budget**: 1% of context window with 8000-char floor. Override via `SLASH_COMMAND_TOOL_CHAR_BUDGET`.

Example showcased: codebase-visualizer Skill with bundled Python script that generates an interactive HTML tree view.
