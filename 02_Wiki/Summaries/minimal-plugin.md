---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/plugin-structure/examples/minimal-plugin.md
title: "Minimal Plugin Example"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Slash-command]
concepts_referenced: []
---

Bare-bones plugin example with single command — from the `plugin-structure` skill examples.

**Directory structure**:
```
hello-world/
├── .claude-plugin/
│   └── plugin.json
└── commands/
    └── hello.md
```

**`.claude-plugin/plugin.json`** (minimal — only required `name` field):
```json
{
  "name": "hello-world"
}
```

**`commands/hello.md`** with frontmatter `name: hello`, `description: Prints a friendly greeting message`. Body instructs to print a greeting + include current timestamp.

**Usage**: `/hello` in any session after install.

**Key points**: minimal manifest (only `name`), single command file in `commands/`, auto-discovery (Claude Code finds command), no dependencies (no scripts/hooks/external resources).

**When to use**: quick prototypes, single-purpose utilities, learning plugin development, internal team tools with one specific function.

**Extending**: add more `.md` files in `commands/`, update `plugin.json` with version/description/author, add `agents/` directory, add `hooks/hooks.json` for events.
