---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/agent-development/references/agent-creation-system-prompt.md
title: "Agent creation system prompt (Claude Code internal)"
summarized_at: 2026-05-05
entities_referenced: [Subagent, Memory]
concepts_referenced: []
---

Reference inside the `plugin-dev` toolkit's `agent-development` skill. **Reproduces the exact system prompt Claude Code uses internally** to generate subagent configurations from natural language descriptions, refined through production use.

The prompt instructs the model to act as an "elite AI agent architect" and to:
1. Extract core intent from the user's description (incl. CLAUDE.md context — for code-review agents, assume "recently written code" not whole codebase unless user says otherwise).
2. Design an expert persona embodying domain knowledge.
3. Architect comprehensive instructions covering behavioral boundaries, methodologies, edge cases, output format, and CLAUDE.md alignment.
4. Optimize for performance (decision frameworks, self-verification, workflow patterns, escalation/fallback).
5. Create a kebab-case identifier (2-4 words, descriptive, avoid "helper"/"assistant").
6. Include `<example>` blocks in the `whenToUse` field showing context, user message, assistant action (incl. proactive examples if implied). Examples must show the assistant invoking the Agent tool, not responding directly.

**Output is JSON** with exactly three fields:
- `identifier` — lowercase + numbers + hyphens
- `whenToUse` — starts with "Use this agent when...", includes the `<example>` blocks
- `systemPrompt` — written in second person ("You are...", "You will...")

**Key principles for system prompts**: be specific not generic, include concrete examples, balance comprehensiveness with clarity, give enough context for variations, make agent proactive in seeking clarification, build in self-correction.

The doc shows how to convert the JSON output into an agent markdown file at `agents/<identifier>.md` with frontmatter (`name`, `description` (= the whenToUse), `model`, `color`) plus the system prompt body.

**Customization examples**: append security-focused criteria (OWASP top 10, injection, XSS), test-generation criteria (AAA pattern), documentation criteria (CLAUDE.md standards).

**Best practices**: consider project context (CLAUDE.md), include proactive usage examples, scope assumptions ("recently written code"), define clear output structure (Summary / Findings / Recommendations).

Integration into plugin-dev workflow: take user request → feed to Claude with this system prompt → JSON → markdown file → validate → test triggering → place in plugin's `agents/`.
