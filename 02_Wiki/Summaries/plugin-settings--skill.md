---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/plugin-settings/SKILL.md
title: "Plugin Settings (plugin-dev skill)"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Settings, Hooks, Slash-command, Subagent]
concepts_referenced: []
---

Skill documenting the `.claude/plugin-name.local.md` pattern — per-project plugin configuration via YAML frontmatter + markdown body, gitignored. Triggered by "plugin settings", "store plugin configuration", "user-configurable plugin", ".local.md files", "plugin state files", "read YAML frontmatter", "per-project plugin settings".

**File location**: `.claude/plugin-name.local.md` in project root. **Lifecycle**: user-managed (not in git, should be in `.gitignore`). Read from hooks, commands, agents.

**Structure**:
```markdown
---
enabled: true
setting1: value1
setting2: value2
numeric_setting: 42
list_setting: ["item1", "item2"]
---

# Additional Context

This markdown body can contain task descriptions, additional instructions,
prompts to feed back to Claude, documentation or notes.
```

**Reading from hooks (Bash)**:
```bash
#!/bin/bash
set -euo pipefail
STATE_FILE=".claude/my-plugin.local.md"
[[ ! -f "$STATE_FILE" ]] && exit 0  # Plugin not configured

# Parse YAML frontmatter (between --- markers)
FRONTMATTER=$(sed -n '/^---$/,/^---$/{ /^---$/d; p; }' "$STATE_FILE")
ENABLED=$(echo "$FRONTMATTER" | grep '^enabled:' | sed 's/enabled: *//' | sed 's/^"\(.*\)"$/\1/')
[[ "$ENABLED" != "true" ]] && exit 0  # Disabled

# Use config in hook logic
if [[ "$STRICT_MODE" == "true" ]]; then ... fi
```

**Reading from commands** (markdown): describe steps to read settings via Read tool, parse YAML, apply to logic.

**Reading from agents** — covered later in raw, not sampled.

The pattern enables: enable/disable flags, per-project tunables, state shared between hooks/commands/agents (e.g., coordinator session names, agent IDs, task IDs).
