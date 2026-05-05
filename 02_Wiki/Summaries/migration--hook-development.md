---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/hook-development/references/migration.md
title: "Migrating from basic to advanced hooks"
summarized_at: 2026-05-05
entities_referenced: [Hooks, Plugin]
concepts_referenced: []
---

Reference inside `plugin-dev/skills/hook-development/`. Guides migration from **command hooks** (bash scripts running on tool events) to **prompt-based hooks** (LLM-evaluated hooks).

**Why migrate**: prompt hooks reason in natural language, handle edge cases adaptively, require no bash scripting, support more flexible validation.

**Migration example — Bash command validation**:

Before: `validate-bash.sh` does `if [[ "$command" == *"rm -rf"* ]]; then exit 2`. Misses `rm -fr`, `rm -r -f`, `dd`, `mkfs`. No context awareness.

After: prompt hook config:
```json
{
  "PreToolUse": [{
    "matcher": "Bash",
    "hooks": [{
      "type": "prompt",
      "prompt": "Command: $TOOL_INPUT.command. Analyze for: 1) Destructive operations (rm -rf, dd, mkfs) 2) Privilege escalation (sudo) 3) Network operations without consent. Return 'approve' or 'deny' with explanation.",
      "timeout": 15
    }]
  }]
}
```

**Migration example — file write validation**: replace per-pattern bash checks with a prompt that considers `$TOOL_INPUT.file_path` AND `$TOOL_INPUT.content` (first 200 chars), checking system directories, credentials, path traversal, AND content secrets.

**When to KEEP command hooks**:
1. **Deterministic perf checks** (file size: `stat -c%s "$file"`, fast `< 50ms` regex matches)
2. **External tool integration** (security-scanner, linter that returns yes/no)
3. **Very fast checks** (whitelist-only safe commands like `ls|pwd|echo`)

**Hybrid approach** — chain a fast command hook + a prompt hook in the same matcher. Command does deterministic gate, prompt does deep reasoning.

**Migration patterns** (substitution recipes):
- String contains → natural language: `[[ "$cmd" == *"sudo"* ]]` → `"Check for privilege escalation (sudo, su, etc)"`
- Regex → intent: `=~ \.(env|secret|key|token)$` → `"Verify not writing to credential files (.env, secrets, keys, tokens)"`
- Multi-condition → criteria list: `if [ c1 ] || [ c2 ] || [ c3 ]` → `"Check: 1) c1 2) c2 3) c3. Deny if any fail."`

**Migration checklist**: identify validation logic → translate to natural language → test edge cases the old hook missed → verify intent comprehension → set timeout (15-30s for prompt hooks) → document → archive old scripts (don't delete; reference value).

**Closing recommendation**: prompt hooks for most validation; reserve command hooks for deterministic checks and external tool integration.
