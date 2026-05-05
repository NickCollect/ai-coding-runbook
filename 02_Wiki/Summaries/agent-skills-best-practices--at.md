---
type: summary
source: 01_Raw/platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.md
source_url: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
title: "Skill authoring best practices"
summarized_at: 2026-05-05
entities_referenced: [Skill, MCP-server, Code-execution-tool]
concepts_referenced: [Context-window]
---

Authoring guide for writing Skills that Claude can discover and use effectively. Companion to the Skills overview; focused on practical decisions during SKILL.md creation rather than architecture.

**Core principles.** "The context window is a public good"—your Skill shares it with the system prompt, conversation history, other Skills' metadata, and the request itself. At startup only metadata (name + description) from all Skills is pre-loaded; SKILL.md body is read only when the Skill becomes relevant; reference files are read only as needed. The default assumption is that Claude is already smart, so authors should challenge each piece of content ("does Claude really need this explanation?"). The doc gives a concise vs. verbose example pair (~50 vs. ~150 tokens) for explaining PDF text extraction with pdfplumber.

**Degrees of freedom.** Match specificity to task fragility. *High freedom* (text instructions) when multiple approaches are valid—e.g. code review steps. *Medium freedom* (pseudocode/parameterized scripts) when a preferred pattern exists. *Low freedom* (specific scripts, no parameters) for fragile operations like database migrations. The "narrow bridge vs. open field" analogy frames this trade-off.

**Test across models.** Skills act as additions to models, so effectiveness depends on the underlying model—test with Haiku, Sonnet, and Opus; what works for Opus may need more detail for Haiku.

**YAML frontmatter requirements.** `name`: max 64 chars, lowercase letters/numbers/hyphens only, no XML tags, no reserved words "anthropic" or "claude". `description`: non-empty, max 1024 chars, no XML tags. Descriptions must include both *what* the Skill does and *when* to use it, written in third person ("Processes Excel files…" not "I can help you…"). Each Skill has exactly one description; Claude uses it to choose among potentially 100+ Skills.

**Naming.** Prefer gerund form (`processing-pdfs`, `analyzing-spreadsheets`) over vague names (`helper`, `utils`). Reserved words like `anthropic-helper` are forbidden.

**Progressive disclosure patterns.** Keep SKILL.md under 500 lines. Three patterns: high-level guide with references; domain-specific organization (e.g. `bigquery-skill/` with `reference/finance.md`, `reference/sales.md`); conditional details. **Keep references one level deep from SKILL.md**—Claude may use `head -100` to preview deeply nested files, resulting in incomplete reads. For reference files >100 lines, include a table of contents at the top.

**Workflows and feedback loops.** For complex tasks, provide a copyable checklist and number steps explicitly. Implement validator → fix → repeat loops (style guide compliance, document XML validation).

**Content guidelines.** Avoid time-sensitive information; prefer "current method" + collapsible "old patterns" sections. Use consistent terminology—pick one term ("API endpoint", "field", "extract") and stick with it.

**Common patterns.** Template pattern (strict vs. flexible templates); examples pattern (input/output pairs for style-sensitive tasks like commit messages); conditional workflow pattern (decision branches inside SKILL.md).

**Evaluation-driven development.** Build evaluations *before* extensive documentation: identify gaps without a Skill, build three test scenarios, establish a baseline, write minimal instructions, iterate. Use a "Claude A" instance to author the Skill, "Claude B" to test it on real tasks, then bring observations back to Claude A. Observe how Claude actually navigates Skills—unexpected exploration paths, missed connections, ignored content.

**Anti-patterns.** Avoid Windows-style backslashes; avoid offering many tool/library options (provide a default with an escape hatch).

**Skills with executable code.** Scripts should *solve* problems rather than punt errors back to Claude. Avoid magic numbers ("voodoo constants"). Pre-made utility scripts are more reliable, save tokens (script body never enters context, only output does), and ensure consistency. Make execution intent explicit ("Run X to extract fields" vs. "See X for the algorithm"). Use the plan-validate-execute pattern for batch/destructive operations: create a `changes.json` plan, validate with a script, then execute.

**Runtime constraints.** On claude.ai, Skills can install npm/PyPI packages and pull from GitHub. On the Claude API, Skills run in the [[Code-execution-tool]] container with no network access and no runtime package installation. Use forward slashes in paths. For [[MCP-server]] tools inside Skills, always use fully qualified `ServerName:tool_name` format to avoid "tool not found" errors.

A pre-flight checklist closes the doc: core quality (description specificity, body <500 lines, references one level deep), code/scripts (explicit error handling, no magic numbers), and testing (≥3 evaluations, tested on Haiku/Sonnet/Opus).
