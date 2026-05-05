---
type: summary
source: 01_Raw/anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills.md
source_url: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
title: "Equipping agents for the real world with Agent Skills"
summarized_at: 2026-05-05
entities_referenced: [Skill, MCP-server, Agent-SDK]
concepts_referenced: [Context-window]
---

Launch post (Oct 16, 2025; updated Dec 18, 2025 — Skills published as open standard at agentskills.io for cross-platform portability) for **Agent Skills**: organized folders of instructions, scripts, and resources that agents discover and load dynamically.

**What a Skill is.** A directory containing a `SKILL.md` file. The `SKILL.md` must start with YAML frontmatter providing `name` and `description`. At startup, the agent pre-loads only this metadata into its system prompt — the body of `SKILL.md` is not loaded until the model decides the skill is relevant.

**Three levels of progressive disclosure** (the core design principle):
1. *Metadata in system prompt* — name + description for every installed skill, just enough for the model to know when to use which skill.
2. *Body of SKILL.md* — loaded into context only when triggered (model reads via Bash tool).
3. *Bundled supplementary files* — extra Markdown / scripts referenced from SKILL.md, loaded only as needed (e.g., the PDF skill's `forms.md` only loaded when filling forms; `reference.md` for general PDF info).

This means the amount of context that can be bundled into a skill is effectively unbounded.

**Skills + code execution.** Skills can include code Claude executes as tools. The PDF skill ships a Python script that reads a PDF and extracts form fields — Claude runs it without loading either the script or the PDF into context. Code provides deterministic reliability for tasks LLMs are bad at (e.g., sorting large lists is wasteful via token generation).

**Walkthrough — PDF skill that powers Claude's document editing.**
- `SKILL.md` with frontmatter (`name: pdf`, `description: ...`) and pointers to `reference.md` and `forms.md`.
- When user asks Claude to fill a PDF form: (1) Claude sees PDF skill metadata in system prompt, (2) reads `pdf/SKILL.md` via Bash, (3) reads `forms.md`, (4) executes bundled Python script for form-field extraction, (5) proceeds with task.

**Author guidelines.**
- *Start with evaluation* — find capability gaps via representative tasks; build skills incrementally.
- *Structure for scale* — split SKILL.md when it gets unwieldy; mutually-exclusive contexts go in separate files; clarify whether code is for execution or reference.
- *Think from Claude's perspective* — name and description are critical (they decide when the skill triggers); monitor real usage; iterate.
- *Iterate with Claude* — ask Claude to capture successful approaches and common mistakes into reusable skill content; if it goes off track, ask it to self-reflect.

**Security.** Skills are powerful — malicious skills can introduce vulns or direct Claude to exfiltrate data. Install only from trusted sources; audit unfamiliar skills before use, paying attention to bundled code, dependencies, and external-network instructions.

**Where Skills work today.** Claude.ai, Claude Code, Claude Agent SDK, Claude Developer Platform.

**Future direction.** Anthropic plans to add lifecycle features (creation, editing, discovery, sharing), explore Skills + MCP complementarity (Skills for procedural workflows, MCP for tool integrations), and eventually let agents create/edit/evaluate their own Skills. Authors: Barry Zhang, Keith Lazuka, Mahesh Murag.
