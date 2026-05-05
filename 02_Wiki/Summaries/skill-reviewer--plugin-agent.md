---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/agents/skill-reviewer.md
title: "skill-reviewer (plugin subagent)"
summarized_at: 2026-05-05
entities_referenced: [Skill, Subagent]
concepts_referenced: []
---

Subagent definition shipped in the `plugin-dev` plugin. Reviews and improves Claude Code skills for maximum effectiveness/reliability. Triggered when user creates/modifies a skill, asks for "review my skill", "check skill quality", "improve skill description". **Trigger proactively after skill creation.**

**Frontmatter**:
- `name: skill-reviewer`
- `description`: includes inline `<example>` blocks demonstrating triggers
- `model: inherit`
- `color: cyan`
- `tools`: Read, Grep, Glob (read-only)

**Review process** (8 steps):
1. **Locate + read**: find SKILL.md, read frontmatter + body, check supporting dirs (references/ examples/ scripts/)
2. **Validate structure**: YAML frontmatter between `---`, required `name` + `description`, optional `version` + `when_to_use` (DEPRECATED — use description only); body exists + substantial
3. **Evaluate description** (most critical): trigger phrases (specific user phrases), third person ("This skill should be used when..." NOT "Load this skill when..."), specificity (concrete scenarios), length 50-500 chars, lists example user queries
4. **Content quality**: SKILL.md body 1,000-3,000 words (lean focus), imperative/infinitive form ("To do X, do Y" not "You should do X"), clear sections, concrete guidance
5. **Progressive disclosure**: core SKILL.md = essentials; references/ = detailed docs; examples/ = working code; scripts/ = utility scripts; SKILL.md references these clearly
6. **Review supporting files**: references/ (quality, relevance, organization), examples/ (complete + correct), scripts/ (executable + documented)
7. **Identify issues** (severity-categorized): vague triggers, too much in SKILL.md, second person in description, missing key triggers, no examples/references when valuable
8. **Generate recommendations**: specific fixes, before/after examples, prioritized by impact

**Quality standards**: strong specific trigger phrases, lean SKILL.md (<3,000 words ideal), imperative/infinitive style, proper progressive disclosure, working file references, complete + accurate examples.

**Output format**: structured review with sections — Summary (incl. word counts), Description Analysis (current + issues + recommended improved description), Content Quality (word count + style + organization), Progressive Disclosure (current structure: SKILL.md word count + references/examples/scripts file counts), Specific Issues (critical/major/minor categorized with file/location + fix), Positive Aspects, Overall Rating (Pass/Needs Improvement/Needs Major Revision), Priority Recommendations (top 3).

**Edge cases**: no description issues → focus on content/organization; very long >5,000 words → split into references; new skill with minimal content → constructive building guidance; perfect skill → acknowledge + minor enhancements only; missing referenced files → report errors with paths.
