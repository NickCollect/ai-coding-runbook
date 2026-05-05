---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/plugin-settings/examples/example-settings.md
title: "plugin-dev: plugin-settings example-settings"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Settings, Hooks]
concepts_referenced: []
---

Examples doc inside `plugin-dev`'s `plugin-settings` skill. Templates for plugin-local user settings files (`.claude/<plugin-name>.local.md`).

**Format**: markdown file with YAML frontmatter for settings + body for human-readable notes.

**Templates**:

1. **Basic configuration** — minimal `enabled: true`, `mode: standard`.

2. **Advanced configuration** — `strict_mode`, `max_file_size: 1000000`, `allowed_extensions: [".js", ".ts", ".tsx"]`, `enable_logging: true`, `notification_level: info`, `retry_attempts: 3`, `timeout_seconds: 60`, `custom_path`.

3. **Agent state file** — for multi-agent swarm: `agent_name`, `task_number`, `pr_number`, `coordinator_session`, `dependencies` array, `additional_instructions`. Body documents requirements + success criteria + coordination.

4. **Feature flag pattern** — `enabled: true`, `features: [...]` array, `experimental_mode: false`.

**Reading settings in hooks**:
```bash
if [[ ! -f ".claude/my-plugin.local.md" ]]; then exit 0; fi
FRONTMATTER=$(sed -n '/^---$/,/^---$/{ /^---$/d; p; }' ".claude/my-plugin.local.md")
ENABLED=$(echo "$FRONTMATTER" | grep '^enabled:' | sed 's/enabled: *//')
[[ "$ENABLED" == "true" ]] && # hook is active
```

**Gitignore**: always `.claude/*.local.md` and `.claude/*.local.json` — these are user-local, not committed.

**Editing**: users edit `.local.md` directly. Changes require Claude Code restart — hooks can't be hot-swapped.
