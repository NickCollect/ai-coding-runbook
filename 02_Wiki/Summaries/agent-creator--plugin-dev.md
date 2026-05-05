---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/agents/agent-creator.md
title: "plugin-dev: agent-creator subagent"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Subagent]
concepts_referenced: []
---

Subagent from `plugin-dev` plugin that automates creation of high-quality agent configurations.

**Frontmatter**: `name: agent-creator`, `model: sonnet`, `color: magenta`, `tools: ["Write", "Read"]`. Triggers on "create an agent", "generate an agent", "build a new agent", "make me an agent that...", or descriptions of agent functionality.

**Process**:
1. **Extract core intent** — fundamental purpose, key responsibilities, success criteria. Consider CLAUDE.md context. For code-review agents, assume "recently written code" unless specified otherwise.
2. **Design expert persona** — compelling identity with deep domain knowledge.
3. **Architect comprehensive instructions** — system prompt with behavioral boundaries, methodologies, edge cases, output format, project alignment.
4. **Optimize for performance** — decision-making frameworks, quality control, efficient workflow, escalation strategies.
5. **Create identifier** — concise (2-4 words hyphen-joined), lowercase letters/numbers/hyphens, 3-50 chars, descriptive (avoid "helper"/"assistant").
6. **Craft 2-4 `<example>` blocks** showing different phrasings, explicit + proactive triggering, with `<commentary>`.

**Generation steps**:
- Write description starting with "Use this agent when..."
- Pick model: `inherit` default; `sonnet` for complex; `haiku` for simple.
- Pick color by purpose: blue/cyan analysis-review, green generation, yellow validation, red security/critical, magenta transformation/creative.
- Recommend minimal tool set (least privilege) or omit for full access.
- Write file via Write tool to `agents/[identifier].md`.

**Output format**: brief summary with name, triggers, model, color, tools, file path + word count, how to use, test scenario, validation command (`scripts/validate-agent.sh agents/[identifier].md`), suggest running `plugin-validator` agent.

**Quality standards**: identifier follows naming rules, description has strong trigger phrases + 2-4 examples, examples show explicit + proactive, system prompt 500-3,000 words with clear structure (role/responsibilities/process/output), appropriate model and color choice, minimal tools.

**Edge cases**: vague request → ask clarifying questions; conflict with existing agent → suggest different scope/name; very complex → break into multiple specialized agents; honor specific tool/model requests; create agents/ dir if first.
