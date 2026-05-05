---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/hook-development/references/advanced.md
title: "Advanced Hook Use Cases (hook-development reference)"
summarized_at: 2026-05-05
entities_referenced: [Hooks]
concepts_referenced: []
---

Reference doc from the `hook-development` skill. Advanced hook patterns and techniques. Note: only first ~100 lines sampled — covers initial patterns.

**Multi-stage validation**: combine `command` + `prompt` hook types in same matcher group for layered validation. Fast deterministic check first (e.g., 5s timeout), then intelligent prompt analysis (e.g., 15s timeout). Example: command hook quick-approves obviously safe commands (`ls`, `pwd`, `echo`, `date`, `whoami` regex match → exit 0), prompt hook analyzes everything else.

**Conditional hook execution**: gate hook logic on environment context. Examples:
- Only run in CI: `if [ -z "$CI" ]; then echo '{"continue": true}'; exit 0; fi`
- Skip for trusted users: `if [ "$USER" = "admin" ]; then exit 0; fi`
- Project-specific validation, user-specific rules

**Hook chaining via state**: share state between hooks using temp files:
- Hook 1: analyze → save state → `echo "$risk_level" > /tmp/hook-state-$$`
- Subsequent hooks read the state file (PID-suffixed for isolation)

(Remaining content not sampled — likely covers more advanced patterns: HTTP hooks, MCP tool hooks, async patterns, error recovery, etc.)
