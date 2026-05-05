---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/command-development/README.md
title: "Command Development Skill (README)"
summarized_at: 2026-05-05
entities_referenced: [Slash-command, Plugin, Skill, Subagent, Hooks]
concepts_referenced: []
---

README for the `command-development` skill in the `plugin-dev` plugin. Comprehensive guidance on creating Claude Code slash commands.

**Skill structure** (~22,000 words total via progressive disclosure):
- **SKILL.md** (~2,470 words): core fundamentals (file format, frontmatter overview, dynamic args/file refs/bash exec, namespacing, plugin features overview, validation patterns)
- **References** (~13,500 words across 7 files):
  - `frontmatter-reference.md` (~1,200) — complete YAML frontmatter spec
  - `plugin-features-reference.md` (~1,800) — `${CLAUDE_PLUGIN_ROOT}`, plugin patterns, integration
  - `interactive-commands.md` (~2,500)
  - `advanced-workflows.md` (~1,700)
  - `testing-strategies.md` (~2,200)
  - `documentation-patterns.md` (~2,000)
  - `marketplace-considerations.md` (~2,200)
- **Examples** (~6,000 words): `simple-commands.md` (10 examples), `plugin-commands.md` (10 plugin-specific)

**Triggers**: "create a slash command", "add a command", "write a custom command", "define command arguments", "command frontmatter", "organize commands"/namespacing, file references, bash execution in commands, command development best practices.

**File format quick reference**:
```markdown
---
description: Brief description
argument-hint: [arg1] [arg2]
allowed-tools: Read, Bash(git:*)
---

Command prompt content with:
- Arguments: $1, $2, or $ARGUMENTS
- Files: @path/to/file
- Bash: !`command here`
```

**Locations**: `.claude/commands/` (project), `~/.claude/commands/` (personal), `plugin-name/commands/` (plugin).

**Frontmatter fields**: `description`, `allowed-tools`, `model` (sonnet/opus/haiku), `argument-hint`, `disable-model-invocation` (manual-only).

**Common patterns**: simple review command, command with `$1`/`$2` args, command with `@$1` file ref, command with `!\`git status\``.

**Development workflow**: design (purpose/scope/args/tools) → create (location/file/basic prompt) → frontmatter (start minimal, add as needed) → test → refine.

**Best practices**: single responsibility per command; clear descriptions; document args via `argument-hint`; minimal `allowed-tools`; thorough testing; comments for complex logic; handle missing args/files.

**Status**: completed enhancements include plugin command patterns, integration patterns, validation patterns. In progress: advanced workflows, testing strategies, documentation patterns, marketplace considerations.

**Maintenance**: keep SKILL.md focused on core; move details to references; add examples; imperative/infinitive form throughout; test examples against current Claude Code.
