---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/plugin-structure/examples/standard-plugin.md
title: "Example: standard plugin layout (code-quality)"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Slash-command, Subagent, Skill, Hooks, Memory]
concepts_referenced: []
---

Example showing a **well-structured production plugin** named `code-quality` shipping commands, agents, skills, hooks, and supporting scripts.

**Directory structure**:
```
code-quality/
├── .claude-plugin/plugin.json
├── commands/{lint.md, test.md, review.md}
├── agents/{code-reviewer.md, test-generator.md}
├── skills/
│   ├── code-standards/{SKILL.md, references/style-guide.md}
│   └── testing-patterns/{SKILL.md, examples/...}
├── hooks/
│   ├── hooks.json
│   └── scripts/validate-commit.sh
└── scripts/{run-linter.sh, generate-report.py}
```

**`plugin.json`** complete with: `name`, `version: "1.0.0"`, `description`, `author{name,email}`, `homepage`, `repository`, `license`, `keywords`.

**Commands** show `${CLAUDE_PLUGIN_ROOT}` usage to invoke bundled scripts (`bash ${CLAUDE_PLUGIN_ROOT}/scripts/run-linter.sh`), and integrate with agents (after-test offer to generate tests via `test-generator` agent).

**Agents** define `description` + `capabilities` list in frontmatter, reference companion skills in body ("Automatically loads `code-standards` skill for project-specific guidelines"). Output format specified per agent.

**Skill** (`code-standards`) example demonstrates progressive disclosure: SKILL.md has overview, style guidelines (formatting, naming, docs, error handling, security) with one tabular example per language, then "For comprehensive style guides by language, see `references/style-guide.md`". The reference file expands per-language depth (JS/TS, Python, Go/Rust/Ruby).

**Hooks** show:
- `PreToolUse` matcher `Write|Edit` with `type: "prompt"` referencing the `code-standards` skill, `timeout: 30`
- `Stop` matcher `.*` with `type: "command"` running `bash ${CLAUDE_PLUGIN_ROOT}/hooks/scripts/validate-commit.sh`, `timeout: 45`

**`validate-commit.sh`** demonstrates: skip if no changes, lint changed JS/TS via `eslint`, lint Python via `pylint`, exit 1 with `{"systemMessage": "..."}` if issues found.

**Pattern showcase**: components reference each other (commands invoke scripts and agents; agents auto-load skills; hooks run scripts and reference skills). Section "Key Points": complete manifest, multiple components, rich skills with refs/examples, hooks-driven automation, cohesive integration.

**When to use this layout**: production plugins for distribution, team collaboration tools, plugins requiring consistency enforcement, complex workflows with multiple entry points.
