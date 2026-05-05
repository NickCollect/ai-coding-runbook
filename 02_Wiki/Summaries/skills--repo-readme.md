---
type: summary
source: 01_Raw/github/anthropics/skills/README.md
title: "anthropics/skills repository README"
summarized_at: 2026-05-05
entities_referenced: [Skill, Plugin-marketplace, Agent-SDK]
concepts_referenced: []
---

README for `anthropics/skills` GitHub repository. Anthropic's reference implementation of skills for Claude. Repo also serves as a Claude Code plugin marketplace.

Defines **Skills**: folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks. Range from creative (art, music, design) → technical (testing web apps, MCP server generation) → enterprise (comms, branding). Each skill self-contained in own folder with `SKILL.md` (YAML frontmatter + instructions).

**License**: many skills are open source (Apache 2.0). The document creation/editing skills powering Claude's document capabilities are **source-available** (NOT open source) — included as production references in `skills/docx`, `skills/pdf`, `skills/pptx`, `skills/xlsx`.

**Repo layout**:
- `./skills` — examples for Creative & Design / Development & Technical / Enterprise & Communication / Document Skills
- `./spec` — the Agent Skills specification
- `./template` — skill template

**Use in Claude Code**:
- Register as marketplace: `/plugin marketplace add anthropics/skills`
- Install bundled plugins: `Browse and install plugins` → `anthropic-agent-skills` → choose `document-skills` or `example-skills`
- Direct: `/plugin install document-skills@anthropic-agent-skills` or `example-skills@anthropic-agent-skills`
- Use skill by mention, e.g. "Use the PDF skill to extract form fields from `path/to/some-file.pdf`"

**Use in Claude.ai**: example skills already available on paid plans. Custom skill upload path documented separately.

**Use in Claude API**: pre-built skills + custom upload via Skills API Quickstart.

**Basic skill creation** (just two required frontmatter fields):
```markdown
---
name: my-skill-name
description: A clear description of what this skill does and when to use it
---
# My Skill Name
[Instructions...]
```

**Disclaimer in raw**: skills are demonstration/educational only; Claude's actual behavior may differ; always test in your environment before relying on them.

Highlighted **Partner Skill**: Notion (link in raw).

Cross-ref: `agentskills.io` is the standalone Agent Skills standard.
