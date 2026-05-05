---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/skill-development/SKILL.md
title: "Skill Development (plugin-dev skill)"
summarized_at: 2026-05-05
entities_referenced: [Skill, Plugin]
concepts_referenced: []
---

Skill in `plugin-dev` plugin guiding creation of effective skills for Claude Code plugins. Triggered by "create a skill", "add a skill to plugin", "write a new skill", "improve skill description", "organize skill content", or guidance on skill structure / progressive disclosure / best practices.

**What skills provide**:
1. Specialized workflows — multi-step procedures for specific domains
2. Tool integrations — instructions for working with specific file formats / APIs
3. Domain expertise — company-specific knowledge, schemas, business logic
4. Bundled resources — scripts, references, assets for complex/repetitive tasks

**Anatomy** of a skill:
```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (required: name, description)
│   └── Markdown instructions (required)
└── Bundled Resources (optional)
    ├── scripts/    - Executable code (Python/Bash/etc.)
    ├── references/ - Docs loaded into context as needed
    └── assets/     - Files used in OUTPUT (templates, icons, fonts)
```

**Metadata quality**: `name` + `description` determine when Claude uses skill. Use third person ("This skill should be used when..." NOT "Use this skill when...").

**Bundled resource types**:
- **Scripts** (`scripts/`): for tasks needing deterministic reliability or repeated rewrites. Token-efficient (may execute without loading into context). Claude may still need to read for patching.
- **References** (`references/`): for documentation Claude loads on demand. Examples: `references/finance.md`, `references/mnda.md`, `references/policies.md`, `references/api_docs.md`. **For files >10k words, include grep search patterns in SKILL.md.** Avoid duplication — info in either SKILL.md OR references file, not both. Prefer references; keep only essential procedural instructions in SKILL.md.
- **Assets** (`assets/`): files used IN output (not loaded into context). Templates, images, icons, boilerplate code, fonts.

**Progressive disclosure** (3 levels):
1. Metadata (name + description) — always in context (~100 words)
2. SKILL.md body — when skill triggers (<5k words)
3. Bundled resources — as needed (Unlimited; scripts can execute without reading)

**Skill creation process**:

**Step 1 — Understand with concrete examples**: ask user (or generate + validate) — "What functionality should X support?", "Examples of how this skill would be used?", "What would a user say that should trigger this skill?". Avoid asking too many questions per message.

**Step 2 — Plan reusable contents**: for each example, consider how to execute from scratch + identify reusable scripts/references/assets. Examples:
- `pdf-editor` for "Help me rotate this PDF" → `scripts/rotate_pdf.py`
- `frontend-webapp-builder` → `assets/hello-world/` boilerplate
- `big-query` for table queries → `references/schema.md`
- Plugin hooks skill → `scripts/validate-hook-schema.sh` + `scripts/test-hook.sh` + `references/patterns.md`

**Step 3 — Create directory structure**:
```bash
mkdir -p plugin-name/skills/skill-name/{references,examples,scripts}
touch plugin-name/skills/skill-name/SKILL.md
```
Note: plugin skills created directly in plugin's `skills/` dir (not via `init_skill.py` like the generic skill-creator).

**Step 4 — Edit**: skill is for ANOTHER Claude instance to use. Focus on info that's beneficial and non-obvious to Claude. Procedural knowledge, domain details, reusable assets.

(Remainder of file — guidance on writing style, validation, etc. — not sampled but referenced from raw.)
