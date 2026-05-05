---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/agent-development/references/triggering-examples.md
title: "Agent Triggering Examples: Best Practices"
summarized_at: 2026-05-05
entities_referenced: [Subagent, Skill, Plugin]
concepts_referenced: []
---

Reference doc on writing effective `<example>` blocks in subagent `description` frontmatter. Examples are how Claude decides when to invoke the agent.

**Standard format**:
```markdown
<example>
Context: [what led to this interaction]
user: "[exact user message]"
assistant: "[Claude's response before triggering]"
<commentary>
[Why this agent should trigger here]
</commentary>
assistant: "[Claude's invocation, e.g. 'I'll use the X agent...']"
</example>
```

**Anatomy**:
- **Context**: specific scenario ("User just implemented authentication"), not vague ("User needs help").
- **User message**: exact phrasing. Include multiple examples to vary phrasings.
- **Assistant pre-trigger**: short acknowledgement, often proactive ("Great! Now let me review the code quality").
- **Commentary**: explain WHY agent fires — explicit request? proactive trigger? tool-usage pattern?
- **Assistant trigger**: standard `I'll use the [agent-name] agent to [what]`.

**Example types**:
1. Explicit request — user directly asks.
2. Proactive triggering — fires after relevant work without ask.
3. Implicit request — user implies need ("This code is confusing" → code-simplifier).
4. Tool-usage pattern — multiple Edits to test files → test-quality-analyzer.

**Multiple examples strategy**:
- Vary phrasings ("Review my code" / "Can you check this?" / "Look over my changes").
- Cover proactive AND reactive scenarios.
- Cover edge cases (large PR → deep-review mode).
- Min 2 examples, recommended 3–4, max 6 (longer descriptions hurt triggering accuracy).

**Common mistakes**:
- Missing context.
- Missing commentary.
- Showing agent's output instead of triggering step.

**Debug triggering**:
- Not triggering → keywords missing from examples; add more phrasing variants.
- Triggering too often → examples too broad / overlap with other agents; tighten.
- Wrong scenarios → examples mismatch intended use; revise.

Includes template library for code-review, test-generation, documentation, validation agents — each with proactive + explicit pair.
