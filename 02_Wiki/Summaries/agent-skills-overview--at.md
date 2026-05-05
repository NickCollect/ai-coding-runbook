---
type: summary
source: 01_Raw/platform.claude.com/docs/en/agents-and-tools/agent-skills/overview.md
source_url: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
title: "Agent Skills"
summarized_at: 2026-05-05
entities_referenced: [Skill, Code-execution-tool, Files-API, Skill-API, Plugin]
concepts_referenced: [Context-window]
---

Conceptual overview of Agent Skills: modular capabilities that extend Claude's functionality. Each Skill packages instructions, metadata, and optional resources (scripts, templates) that Claude uses automatically when relevant. **Not eligible for Zero Data Retention (ZDR)**—data is retained per the feature's standard policy.

**Why Skills.** Filesystem-based, reusable resources that give Claude domain-specific expertise: workflows, context, best practices that transform a general-purpose agent into a specialist. Unlike prompts (conversation-level, one-off), Skills load on-demand and eliminate the need to repeatedly provide the same guidance. Key benefits: specialization, reduced repetition, composability.

**Pre-built vs. custom.** Anthropic provides pre-built Skills for common document tasks (PowerPoint `pptx`, Excel `xlsx`, Word `docx`, PDF `pdf`); both pre-built and custom Skills work the same way—Claude picks them automatically. Custom Skills can be created in Claude Code, uploaded via the API, or added in claude.ai settings.

**How Skills work.** Skills leverage Claude's VM environment: a virtual machine with filesystem access where Skills exist as directories of instructions, code, and reference materials—organized like an onboarding guide for a new team member. This filesystem-based architecture enables **progressive disclosure**: Claude loads information in stages.

**Three loading levels:**

| Level | When loaded | Token cost | Content |
|---|---|---|---|
| L1: Metadata | Always (startup) | ~100 tokens/Skill | YAML `name` + `description` |
| L2: Instructions | When triggered | <5k tokens | SKILL.md body |
| L3+: Resources | As needed | Effectively unlimited | Bundled files; scripts execute via bash without loading code into context |

A typical PDF Skill flow: startup loads `PDF Processing - Extract text and tables…` into the system prompt; user requests text extraction; Claude bashes `cat pdf-skill/SKILL.md` into context; if FORMS.md isn't relevant, it stays on disk; Claude executes the workflow.

**Skills architecture.** Claude bashes into a code-execution VM. Reading SKILL.md brings instructions into context. Reference files (FORMS.md, schemas) are read with extra bash commands. Executable scripts run via bash—the script's source code never enters context, only its output. This enables on-demand file access, efficient script execution, and no practical limit on bundled content.

**Where Skills work.**
- **Claude API**: supports pre-built and custom. Specify `skill_id` in the `container` parameter alongside the [[Code-execution-tool]]. Three required beta headers: `code-execution-2025-08-25`, `skills-2025-10-02`, `files-api-2025-04-14` ([[Files-API]] is needed for upload/download). Custom Skills are workspace-shared via the [[Skill-API]] (`/v1/skills` endpoints).
- **Claude Code**: supports only custom Skills, filesystem-based, no API uploads.
- **Claude.ai**: supports both. Pre-built Skills run behind the scenes for document creation. Custom Skills are uploaded as zip files via Settings > Features (Pro/Max/Team/Enterprise plans with code execution); they're per-user, not org-wide, no centralized admin management.

**SKILL.md structure.** Required `name` (≤64 chars, lowercase/numbers/hyphens, no XML tags, no reserved words "anthropic"/"claude") and `description` (non-empty, ≤1024 chars, no XML tags, should include both what + when).

**Security considerations.** Use Skills only from trusted sources (your own or Anthropic's). Malicious Skills can direct Claude to invoke tools or execute code unrelated to the stated purpose. Audit thoroughly; external URL fetches are particularly risky (fetched content may contain prompt-injection); even trustworthy Skills can be compromised when external dependencies change.

**Open-source Skills.** Anthropic publishes [anthropics/skills](https://github.com/anthropics/skills) including a Claude API skill that bundles up-to-date API/SDK reference for 8 languages.

**Limitations.**
- *Cross-surface*: custom Skills do not sync across API/Claude Code/claude.ai—each surface needs separate uploads.
- *Sharing scope*: claude.ai is per-user; API is workspace-wide; Claude Code is personal (`~/.claude/skills/`) or project (`.claude/skills/`), shareable via [[Plugin]].
- *Runtime*: claude.ai has variable network access depending on settings; Claude API has **no network access and no runtime package installation** (only pre-installed packages); Claude Code has full host network access and discourages global package installation.
