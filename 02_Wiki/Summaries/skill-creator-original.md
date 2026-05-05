---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/skill-development/references/skill-creator-original.md
title: "skill-creator (original methodology)"
summarized_at: 2026-05-05
entities_referenced: [Skill]
concepts_referenced: []
---

Reference inside `plugin-dev/skills/skill-development/`. Reproduces the **original `skill-creator` skill** that defines the canonical methodology for authoring new skills. This is the source `plugin-dev`'s `skill-development` skill is adapted from (for plugin context).

**About skills**: modular, self-contained packages extending Claude with specialized knowledge, workflows, tool integrations. "Onboarding guides" for specific domains — they turn Claude into a specialized agent equipped with procedural knowledge.

**Anatomy of a skill**:
```
skill-name/
├── SKILL.md  (required)
│   ├── YAML frontmatter (name, description — both required)
│   └── Markdown instructions
└── (optional)
    ├── scripts/      executable code (Python/Bash/etc)
    ├── references/   docs to load into context as needed
    └── assets/       files used IN output (templates, icons, fonts)
```

**Metadata quality**: `name` and `description` determine when Claude triggers the skill. Use **third person**: "This skill should be used when..." (NOT "Use this skill when...").

**When to include each resource type**:
- **Scripts**: same code being rewritten repeatedly OR deterministic reliability needed. Token-efficient (can be executed without loading into context). May still need to be read for patching.
- **References**: docs Claude should consult while working — DB schemas, API specs, domain knowledge, company policies, detailed workflow guides. Loaded only when Claude determines needed. Best practice: if files >10k words, include grep search patterns in SKILL.md. **Avoid duplication** between SKILL.md and references — prefer references for detail; keep only essential procedural instructions in SKILL.md.
- **Assets**: files that go INTO Claude's output — templates, images, icons, boilerplate code, fonts. Not loaded into context, just copied/modified by Claude.

**Three-level progressive disclosure**:
1. Metadata (name + description) — always in context (~100 words)
2. SKILL.md body — when triggered (<5k words)
3. Bundled resources — as needed (unlimited; scripts can execute without reading)

**Skill creation process** (6 steps):
1. **Understanding with concrete examples**: ask user for examples ("What should this support? Editing? Rotating? Other?"), avoid asking too many questions per message.
2. **Plan reusable contents**: per example, ask "How do I execute this from scratch?" + "What scripts/refs/assets would help on repeat?". E.g. PDF rotation → `scripts/rotate_pdf.py`; web app builder → `assets/hello-world/` template; BigQuery → `references/schema.md`.
3. **Initialize**: run `scripts/init_skill.py <name> --path <dir>` — generates template skill dir with proper frontmatter, TODO placeholders, example resource dirs.
4. **Edit the skill** — write FOR another Claude instance. Focus on procedural knowledge, domain-specific details, reusable assets that help another Claude execute the task.
   - **Writing style**: imperative/infinitive form (verb-first), NOT second person. Use objective instructional language ("To accomplish X, do Y" instead of "You should do X" or "If you need to do X").
   - SKILL.md must answer: (1) skill purpose in a few sentences (2) when should it be used (3) how should Claude use it in practice — referencing all bundled resources.
5. **Package** into a distributable zip via `scripts/package_skill.py <skill-folder>`. Validates frontmatter, naming, description completeness, file org, resource references — then zips with proper structure.
6. **Iterate**: use skill on real tasks → notice struggles → update SKILL.md or resources → test again.
