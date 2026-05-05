---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/agent-development/examples/agent-creation-prompt.md
title: "AI-Assisted Agent Generation Template"
summarized_at: 2026-05-05
entities_referenced: [Subagent, Skill, Plugin, Memory]
concepts_referenced: []
---

Template for using Claude (with the `agent-creation-system-prompt`) to generate Claude Code subagent definitions. Pattern: describe the agent need → ask Claude to return JSON `{identifier, whenToUse, systemPrompt}` → convert into `agents/[identifier].md`.

**Generated agent file structure**:
```yaml
---
name: <identifier>
description: <whenToUse with <example> blocks>
model: inherit
color: <blue|cyan|green|yellow|magenta|red>
tools: ["Read", "Write", "Grep"]   # optional restriction
---
<systemPrompt>
```

**Three worked examples** (full JSON + agent file): code-quality-reviewer (with critical/major/minor severity output), test-generator (post-implementation triggering), api-docs-writer (documentation).

**Tips for generation prompts**:
- Specific: "review TypeScript PRs for type-safety issues, check for proper annotations, avoid `any`, ensure correct generics" beats "help with code".
- Include triggering preferences (proactive vs explicit-only).
- Mention project context (React+TypeScript) so agent checks framework-specific patterns.
- Define output expectations (file paths, line numbers, perf impact).

**Workflow**: validate generated agent with `./scripts/validate-agent.sh`; iterate manually if examples/system prompt need refinement.

When to manually edit instead of generate: very project-specific patterns, custom tool combinations, unique persona, integration with existing agents, precise triggering conditions.
