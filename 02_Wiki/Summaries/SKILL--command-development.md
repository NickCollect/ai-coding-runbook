---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/command-development/SKILL.md
title: "Skill: Command Development (plugin-dev)"
summarized_at: 2026-05-05
entities_referenced: [Slash-command, Skill, Plugin, Subagent, Hooks, MCP-server]
concepts_referenced: []
---

Skill v0.2.0 inside `plugin-dev` toolkit. Triggers on slash-command authoring, frontmatter, dynamic args, file references, bash execution in commands.

**Critical principle**: commands are **instructions FOR Claude, NOT messages TO the user**. Write directives ("Review this code for X, Y, Z") not announcements ("This command will review your code"). Wrong style = command does nothing useful.

**Locations**:
| Where | Path | Label in `/help` |
|---|---|---|
| Project | `.claude/commands/` | `(project)` |
| Personal | `~/.claude/commands/` | `(user)` |
| Plugin | `<plugin>/commands/` | `(plugin-name)` |

Subdirectories create namespaces (e.g. `commands/ci/build.md` → `/build (project:ci)`).

**Frontmatter fields**:
- `description` — shown in `/help`, < 60 chars
- `allowed-tools` — string or array, e.g. `"Read, Write, Edit, Bash(git:*)"`. Patterns scope tools (e.g. `Bash(git:*)` allows only git commands).
- `model` — `sonnet|opus|haiku`; haiku for fast/simple, opus for complex analysis
- `argument-hint` — autocomplete hint, e.g. `"[pr-number] [priority] [assignee]"`
- `disable-model-invocation` — prevents SlashCommand tool from programmatically invoking; user-only

**Dynamic arguments**:
- `$ARGUMENTS` — all args as one string
- `$1`, `$2`, ... — positional
- Mix: `Deploy $1 to $2 environment with options: $3` → `/deploy api staging --force` works

**File references** via `@`:
- `@$1` — read file path passed as arg
- `@src/old.js` and `@src/new.js` — multiple files
- `@package.json` — static reference

**Bash inline execution** for context (full syntax in `references/plugin-features-reference.md`).

**Plugin-specific: `${CLAUDE_PLUGIN_ROOT}`** — env var resolving to plugin's absolute path. Always use for plugin-internal paths (`@${CLAUDE_PLUGIN_ROOT}/templates/foo.md`, `!\`bash ${CLAUDE_PLUGIN_ROOT}/scripts/x.sh\``). Bad alternative `@./templates/foo.md` resolves relative to cwd, not plugin.

**Patterns shown**: review (git diff + per-file checks), testing (`!\`npm test $1\``), documentation (template-driven), workflow (gh CLI orchestration), config-based (load JSON config), template-based (generate from `@template`), multi-script (sequential bash exec), env-aware (per-env config files).

**Validation patterns**: input format check via `!\`echo "$1" | grep -E ...\``, file existence via `!\`test -f $1\``, plugin resource validation, output validation with exit code check, graceful error reporting.

**Multi-component workflows** combine: bash scripts → agent (via Task tool) → skill (mention by name to invoke) → template. Hooks coordinate automatically on tool events; commands can prepare state.

**Common troubleshoot**: command not appearing (wrong dir, missing `.md`), args not working (`$1` syntax check), bash failing (allowed-tools missing Bash), `@` not working (Read tool blocked).
