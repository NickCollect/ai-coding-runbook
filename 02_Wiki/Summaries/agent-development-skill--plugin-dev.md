---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/agent-development/SKILL.md
title: "plugin-dev: agent-development skill"
summarized_at: 2026-05-05
entities_referenced: [Skill, Plugin, Subagent]
concepts_referenced: []
---

Skill from `plugin-dev` plugin teaching agent structure, triggering, system prompt design for Claude Code plugins. Triggers on "create an agent", "add an agent", "write a subagent", "agent frontmatter", "when to use description", "agent examples", "agent tools", "agent colors", "autonomous agent".

**Key concepts**:
- Agents are FOR autonomous work; commands are FOR user-initiated actions.
- Markdown file with YAML frontmatter; system prompt in body.
- Triggering via `description` field with `<example>` blocks.

**Frontmatter fields**:
- `name` (required): lowercase letters/numbers/hyphens, 3-50 chars, must start/end alphanumeric. Good: `code-reviewer`, `test-generator`. Bad: `helper`, `-agent-`, `my_agent`, `ag`.
- `description` (required, **most critical**): "Use this agent when..." + 2-4 `<example>` blocks with `<commentary>`. Length 10-5,000 chars; best 200-1,000 with 2-4 examples.
- `model` (required): `inherit` (recommended) / `sonnet` / `opus` / `haiku`.
- `color` (required): `blue`, `cyan`, `green`, `yellow`, `magenta`, `red`. Distinct per agent in same plugin. Blue/cyan=analysis, green=success, yellow=caution, red=critical, magenta=creative.
- `tools` (optional, array): least-privilege restriction. Common sets: read-only `["Read", "Grep", "Glob"]`, generation `["Read", "Write", "Grep"]`, testing `["Read", "Bash", "Grep"]`.

**System prompt design**: write in **second person** ("You are..."). Standard template:
```
You are [role] specializing in [domain].

**Your Core Responsibilities:** 1. ... 2. ... 3. ...
**Analysis Process:** 1. ... 2. ... 3. ...
**Quality Standards:** - ...
**Output Format:** ...
**Edge Cases:** [case 1]: [handling]
```

**Best practices**: specific responsibilities (not "help with code"), step-by-step process, defined output format, quality standards, edge cases. Length: 20-10,000 chars; best 500-3,000.

**Creation methods**: AI-assisted via prompt template (returns JSON `{identifier, whenToUse, systemPrompt}`) or manual. All `.md` files in `agents/` auto-discovered. Namespacing: `agent-name` or `plugin:subdir:agent-name` with subdirectories.

**Validation**: identifier rules (3-50 chars, lowercase, hyphens, alphanumeric edges), description (10-5,000), system prompt (20-10,000).

**Testing**: write specific triggering examples, use similar phrasing in test, verify Claude loads agent, check process steps and output format.

**References**: `references/system-prompt-design.md`, `references/triggering-examples.md`, `references/agent-creation-system-prompt.md`. **Examples**: `examples/agent-creation-prompt.md`, `examples/complete-agent-examples.md`. **Scripts**: `scripts/validate-agent.sh`, `scripts/test-agent-trigger.sh`.

**Workflow**: define purpose + triggers → choose method → create file → frontmatter + system prompt + 2-4 examples → validate → test → document in plugin README.
