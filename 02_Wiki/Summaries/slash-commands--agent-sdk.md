---
type: summary
source: 01_Raw/code.claude.com/docs/en/agent-sdk/slash-commands.md
source_url: https://code.claude.com/docs/en/agent-sdk/slash-commands
title: "Slash Commands in the SDK"
summarized_at: 2026-05-05
entities_referenced: [Slash-command, Skill, Subagent, Agent-SDK]
concepts_referenced: [Context-window]
---

How to use, discover, and create slash commands through the Claude Agent SDK. Only commands that work without an interactive terminal are dispatchable via SDK; the available list is in `system/init` message under `slash_commands`.

**Sending**: include the slash command in the prompt string: `query({ prompt: "/compact" })`.

**Built-ins** (commonly available): `/compact`, `/context`, `/usage`. Compaction emits a `system` message subtype `compact_boundary` with `compact_metadata.pre_tokens` and `trigger`. **`/clear` is NOT available in the SDK** — each `query()` call already starts a fresh conversation; use `resume` to return to a prior session by ID.

**Custom commands**: Markdown files in `.claude/commands/` (project) or `~/.claude/commands/` (personal). Filename without `.md` becomes the command name.

**Important**: `.claude/commands/` is the **legacy** format. The recommended format is `.claude/skills/<name>/SKILL.md`, which supports both `/name` invocation AND autonomous invocation by Claude. CLI continues to support both; this doc remains accurate for `.claude/commands/`.

**Frontmatter fields**: `allowed-tools` (e.g., `Read, Grep, Glob`), `description`, `model`, `argument-hint`.

**Body features**:
- **Arguments**: `$1`, `$2`, ... or `$ARGUMENTS` for the entire string
- **Bash execution**: `!` `git status` ` ` ` (backtick-wrapped) inlines command output at runtime
- **File references**: `@package.json`, `@.env` injects file contents

**Namespacing**: subdirectories like `.claude/commands/frontend/component.md` create `/component` shown as `(project:frontend)`. Subdir doesn't change the command name itself.

**Example commands shown**: `/refactor`, `/security-check` (with `model: claude-opus-4-7`), `/fix-issue 123 high`, `/git-commit` (with bash context), `/review-config` (with @-references), `/code-review`, `/test`.

Custom commands appear in the `slash_commands` system init list alongside built-ins.
