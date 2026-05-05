---
type: summary
source: 01_Raw/code.claude.com/docs/en/agent-sdk/skills.md
source_url: https://code.claude.com/docs/en/agent-sdk/skills
title: "Agent Skills in the SDK"
summarized_at: 2026-05-05
entities_referenced: [Skill, Agent-SDK, Subagent, Slash-command]
concepts_referenced: []
---

How Claude Agent SDK loads and uses Skills (filesystem-based capability extensions identified by `SKILL.md` files with YAML frontmatter + Markdown).

Key behavior:
- Skills are **filesystem-only artifacts** — unlike subagents, the SDK has no programmatic API to register them. They must live as `SKILL.md` files in `.claude/skills/<name>/`.
- Discovery flows through `settingSources` (TS) / `setting_sources` (Python). Default `query()` loads `user` + `project` sources, so `~/.claude/skills/` and `<cwd>/.claude/skills/` are picked up automatically. If you set `settingSources` explicitly to `[]`, skills disappear unless you re-add `user`/`project` or use the `plugins` option.
- At startup the SDK reads only the metadata; full SKILL.md content loads when Claude decides to invoke the Skill (model-invoked, autonomous).
- Must include `"Skill"` in `allowedTools` / `allowed_tools` to enable the Skill tool.

Skill locations:
- Project: `.claude/skills/` (shared via git)
- User: `~/.claude/skills/`
- Plugin Skills: bundled with installed Claude Code plugins

Important SDK-vs-CLI difference: The `allowed-tools` field in a SKILL.md frontmatter is **honored by the CLI but ignored by the SDK**. In SDK applications, control tool access via the top-level `allowedTools` option (and `permissionMode: "dontAsk"` to deny anything not listed).

Discovery / testing tips: just ask Claude "What Skills are available?" or fire a prompt matching a Skill description (e.g. "Extract text from invoice.pdf") to trigger one.

Troubleshooting:
- Skills not found → check `settingSources` includes `user`/`project`, and that `cwd` points at the dir containing `.claude/skills/`.
- Skill not invoked → make sure `"Skill"` is in `allowedTools`; refine the SKILL.md description for keyword match.

Cross-references: SDK Subagents (similar filesystem pattern, has programmatic alternative), SDK Slash Commands (user-invoked vs Skills which are model-invoked).
