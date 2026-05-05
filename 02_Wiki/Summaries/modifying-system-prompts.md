---
type: summary
source: 01_Raw/code.claude.com/docs/en/agent-sdk/modifying-system-prompts.md
source_url: https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts
title: "Modifying system prompts"
summarized_at: 2026-05-05
entities_referenced: [Agent-SDK, Output-style, Memory, Settings]
concepts_referenced: [Prompt-caching]
---

By default the Agent SDK uses a **minimal system prompt** (essential tool instructions only) — Claude Code's full coding guidelines, response style, and project context are NOT included. To opt into the full preset: `systemPrompt: { type: "preset", preset: "claude_code" }` (TS) or `system_prompt={"type": "preset", "preset": "claude_code"}` (Py).

Four customization methods:

1. **CLAUDE.md files** — project-level (`<cwd>/CLAUDE.md` or `<cwd>/.claude/CLAUDE.md`) and user-level (`~/.claude/CLAUDE.md`). Loaded when `settingSources` includes `'project'` / `'user'`. Persistent, version-controlled, team-shared. NOT controlled by the `claude_code` preset — controlled by setting sources.

2. **Output styles** — markdown files in `~/.claude/output-styles/` or `.claude/output-styles/` with frontmatter `name` / `description`. Activate via `/output-style [name]` or settings. Loaded with `settingSources` user/project.

3. **`systemPrompt` with `append`** — preset + `append: "..."` adds instructions while preserving Claude Code's built-in tool/safety/environment context.

4. **Custom string `systemPrompt`** — replaces default entirely. Loses default tools, safety, environment context unless re-added.

**Prompt caching gotcha**: the `claude_code` preset embeds per-session dynamic context (cwd, platform, OS, current date, git status, auto-memory paths) into the system prompt before `append`. Two sessions in different dirs miss cache. Set `excludeDynamicSections: true` (TS) / `"exclude_dynamic_sections": True` (Py) to move that context into the first user message instead, enabling cross-session/cross-machine cache hits. Requires `@anthropic-ai/claude-agent-sdk` v0.2.98+ or `claude-agent-sdk` v0.1.58+. Tradeoff: context still reaches Claude but with marginally less authority. CLI equivalent: `--exclude-dynamic-system-prompt-sections`.

Comparison table contrasts persistence, reusability, default-tool preservation, scope. Methods can be combined (e.g., output style active + per-call `append`).
