---
type: summary
source: 01_Raw/code.claude.com/docs/en/communications-kit.md
source_url: https://code.claude.com/docs/en/communications-kit
title: "Communications kit"
summarized_at: 2026-05-05
entities_referenced: [Skill, Hooks, Permission-mode, MCP-server, Plugin, Memory, Checkpointing, IDE-integration]
concepts_referenced: []
---

Copy-ready launch announcements, drip-campaign messages, and FAQ responses for admins/eng-leads rolling Claude Code out to teams. All material is draft copy — rewrite in org voice, swap example tasks for real bugs/modules, replace `[bracketed placeholders]`.

**Pre-launch checklist**: create `#claude-code` channel, test install on one machine in your env, prepare data-handling link, choose one concrete first task, name an owner for first 48 hours, line up a C-suite sponsor (exec-sent launches see higher first-week adoption than admin-sent).

**Launch message templates**: standard org-wide announcement (Email + Slack/Teams formats), executive sponsor variant ("ten minutes on one real task"), pilot-group variant (pilots prompted to use plan mode on first multi-file change), champion recruitment DM.

Standard install path used throughout: `curl -fsSL https://claude.ai/install.sh | bash` → `cd <repo>` → `claude` → `/init`.

**Tips-and-tricks campaign** (drip 1-2/wk in `#claude-code`). Each msg: hook + payoff + "try it now" + docs link. Topics:
- **Choosing the right model**: Opus = large refactors / gnarly debugging / high-stakes; Sonnet = workhorse default; Haiku = quick questions, formatting, mechanical edits. `/model` to switch.
- **Quick wins**: fix flaky test, walk through an unfamiliar module, sanity-check working diff
- **`/init` and CLAUDE.md**: stop re-explaining repo conventions. Run once per repo, keep CLAUDE.md under two screens.
- **@-references**: `@src/components/Button.tsx`, `@docs/design-system.md` — works on directories too. Tab autocomplete after `@`.
- **Permission modes / Shift+Tab**: cycles default ↔ acceptEdits ↔ plan. Plan mode = trust-builder; start there for multi-file work.
- **`/rewind`** + checkpointing: undo button for the conversation. Esc-Esc opens menu.
- **MCP connectors**: `.mcp.json` at project root for GitHub/Jira/Linear. Ask Claude to write the config.
- **Skills** as `.claude/skills/<name>/SKILL.md` → reusable `/name` command. Make one the second time you re-type a multi-step prompt.
- **Hooks**: Stop hook → desktop notification on long-task completion.
- **Screenshots**: drag screenshot or Ctrl+V (use Ctrl+V on macOS too, not Cmd+V).
- **Git workflows**: "commit this with a good message and open a PR" — Claude handles full git ceremony.
- **Plugins**: `/plugin` browses available skills/commands.
- **Security one-liner**: terminal CLI → Anthropic API direct, no third-party servers, OS sandbox optional, Enterprise = no model training on your code.
- **4 habits to stick**: plan mode for multi-file, run /init early, review diffs, verify critical paths.

**FAQ one-liners**: VS Code / JetBrains supported, no config needed beyond `claude` + `/init`, code goes terminal → Anthropic API direct (no 3rd party), reads only what you grant access to, Copilot autocompletes vs. agent that reads/runs/edits multi-file.

**Prompt templates** for new users: "tests in [file] are failing, figure out why and fix it", "walk me through how [module] works", "refactor [module] to [goal], use plan mode", "write tests for [file] covering edge cases around [scenario]", "look at my working diff and tell me what looks risky", "fix [issue], conventional commit, open PR", "make me a /ship skill that runs tests and lint before commit".
