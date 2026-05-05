---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/plugin-settings/examples/create-settings-command.md
title: "Example: create-settings command"
summarized_at: 2026-05-05
entities_referenced: [Slash-command, Plugin, Settings]
concepts_referenced: []
---

Example slash command (in `plugin-dev/skills/plugin-settings/examples/`) demonstrating the **create-plugin-settings pattern**: walks the user through `AskUserQuestion` prompts and writes a `.claude/<plugin-name>.local.md` file with YAML frontmatter + markdown body.

Frontmatter: `description: "Create plugin settings file with user preferences"`, `allowed-tools: ["Write", "AskUserQuestion"]`.

**Steps Claude is told to follow**:
1. **Ask user for preferences** via `AskUserQuestion` JSON: e.g. "Enable plugin?" (Yes/No), "Validation mode?" (Strict/Standard/Lenient).
2. **Parse answers** — `answers["0"]` = enabled, `answers["1"]` = mode.
3. **Create `.claude/my-plugin.local.md`** with frontmatter:
   ```yaml
   ---
   enabled: <true|false>
   validation_mode: <strict|standard|lenient>
   max_file_size: 1000000
   notify_on_errors: true
   ---
   ```
   Plus a brief markdown body summarizing the chosen mode.
4. **Inform user**: file path, current config summary, edit instructions, restart reminder, gitignored note.

**Implementation notes**: validate user input before writing — check mode is valid, numeric fields are numbers, paths don't have traversal, sanitize free-text fields.
