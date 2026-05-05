---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/command-development/references/frontmatter-reference.md
title: "plugin-dev: command-development frontmatter-reference"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Slash-command]
concepts_referenced: []
---

Reference inside `plugin-dev`'s `command-development` skill. YAML frontmatter fields for slash commands. All optional — commands work without frontmatter.

**Fields**:

- **`description`** (string, ~60 chars recommended): shown in `/help`. Start with verb (Review, Deploy, Generate). Avoid "This command...". Default = first line of command body.

- **`allowed-tools`** (string or array): restrict tools the command can use. Inherits conversation perms by default.
  - Single: `Read`
  - Multi comma: `Read, Write, Edit`
  - Multi array: `[Read, Write, Bash(git:*)]`
  - Bash with command filter: `Bash(git:*)`, `Bash(npm:*)`, `Bash(docker:*)` — recommended over bare `Bash` or `*`.
  - All tools: `"*"` (not recommended).
  - Best practice: most restrictive that works; document why specific tools needed.

- **`model`** (string): `sonnet` / `opus` / `haiku`. Default inherits from conversation.
  - `haiku`: simple/formulaic, fast execution, frequent invocations.
  - `sonnet`: standard, balanced (default).
  - `opus`: complex analysis, architectural decisions, critical tasks.
  - Best practice: omit unless specific need; reserve `opus` for genuinely complex.

- **`argument-hint`** (string): documents expected positional args for `/help` and autocomplete. Format: `[arg1] [arg2] [optional-arg]`. Use descriptive names (not `arg1`/`arg2`); match positional order. Examples: `[pr-number]`, `[environment] [version]`, `[source-branch] [target-branch] [commit-message]`.

- **`disable-model-invocation`** (boolean, default `false`): when `true`, only user can invoke via typing `/command` — Claude can't via SlashCommand tool. Use for: manual-only commands (production approval), destructive ops, interactive workflows. Use sparingly — limits Claude's autonomy.

**Complete examples**:
- Minimal: just markdown body, no frontmatter.
- Simple: just `description`.
- Standard: `description` + `allowed-tools`.
- Complex: all four common fields.
- Manual-only: `disable-model-invocation: true` + restrictive `allowed-tools` + comment block explaining.

**Common errors**: invalid YAML syntax (missing quotes), bare `Bash` without command filter, invalid model name (e.g., `gpt4`).

**Validation checklist** before commit: YAML valid, description <60 chars, `allowed-tools` proper format, valid model, `argument-hint` matches positional args, `disable-model-invocation` used appropriately.
