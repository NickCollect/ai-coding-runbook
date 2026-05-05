---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/hook-development/scripts/README.md
title: "Hook Development Utility Scripts (plugin-dev)"
summarized_at: 2026-05-05
entities_referenced: [Hooks, Plugin]
concepts_referenced: []
---

README for utility scripts bundled with the `hook-development` skill. Three scripts:

1. **`validate-hook-schema.sh path/to/hooks.json`** — checks valid JSON, required fields, valid event names, hook types (`command`/`prompt`), timeout ranges, hardcoded path detection, prompt-hook event compatibility.

2. **`test-hook.sh [-v] [-t N] [--create-sample <event>] <hook-script> <test-input.json>`** — runs a hook script against sample input. Sets up `CLAUDE_PROJECT_DIR`/`CLAUDE_PLUGIN_ROOT` env. Measures execution time. Validates output JSON. Shows exit codes and meaning. Can generate sample test input via `--create-sample PreToolUse > test-input.json`.

3. **`hook-linter.sh <script.sh> [...]`** — checks shebang, `set -euo pipefail`, stdin reading, error handling, variable quoting (injection risk), exit code usage, hardcoded paths, long-running code, error → stderr, input validation.

**Typical workflow**: write script → lint → create test input → test → add to `hooks.json` → validate config → test in Claude Code with `claude --debug`.

**Common issues addressed**:
- Hook doesn't execute → check shebang, executable bit, `${CLAUDE_PLUGIN_ROOT}` path.
- Times out → reduce timeout, optimize, remove long-running ops.
- Fails silently → exit codes 0 or 2, errors to stderr, valid JSON output.
- Injection vulns → quote vars, `set -euo pipefail`, validate inputs, run linter.
