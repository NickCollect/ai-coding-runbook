---
type: summary
source: 01_Raw/code.claude.com/docs/en/glossary.md
source_url: https://code.claude.com/docs/en/glossary
title: "Glossary"
summarized_at: 2026-05-05
entities_referenced: [Hooks, Skill, Subagent, MCP-server, Plugin, Permission-mode, Sandboxing, Auto-mode, Output-style, Memory, Checkpointing, Settings, Native-interface, Channel, Agent-team, Headless-mode]
concepts_referenced: [Agentic-loop, Context-window, Channel, Agent-team]
---

Definitions for Claude Code terminology, organized A-Z. Each entry links to its in-depth doc page. Model-level concepts (tokens, temperature, RAG) live in the platform glossary.

**Key entries** (canonical Claude Code concepts):

- **Agent teams** — multiple independent sessions coordinated by team lead with shared task list + peer-to-peer messaging. Experimental; enable via `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`. Different from subagents (each teammate has own context, you talk to any directly).
- **Agentic coding / Agentic harness / Agentic loop** — the workflow where AI reads + acts; the tools+context+exec env (Claude Code) wrapping the model (Claude); the gather-act-verify-repeat cycle.
- **Auto memory** — Claude-written notes per git repo at `~/.claude/projects/`, all worktrees share one dir. First 200 lines / 25 KB of `MEMORY.md` index loaded each session. Counterpart to user-written CLAUDE.md.
- **Auto mode** — permission mode with classifier model that reviews each action; classifier never sees tool results so injected instructions can't influence it. Research preview on Max/Team/Enterprise/API plans.
- **Bare mode** — `--bare` flag; skips hooks/skills/plugins/MCP/auto-memory/CLAUDE.md auto-discovery. For CI consistency.
- **Bundled skills** — prompt playbooks shipped with Claude Code: `/batch`, `/simplify`, `/debug`, `/loop`. Unlike fixed-logic commands, they orchestrate.
- **Channel** — MCP server pushing events to your session so Claude can react; can be two-way. Telegram/Discord/iMessage in research preview.
- **Checkpoint** — auto-snapshot before each Claude edit. `Esc Esc` or `/rewind`. Local to session, separate from git, **doesn't track Bash-tool changes**.
- **`.claude` directory** — project root for settings/hooks/skills/subagents/rules/auto-memory; user-level at `~/.claude/`.
- **CLAUDE.md** — user-written persistent instructions, loaded as user message after system prompt. Survives compaction. Locations (precedence high→low): `./CLAUDE.md` or `./.claude/CLAUDE.md`, `~/.claude/CLAUDE.md`, managed policy.
- **Command** — `/name` prompt. Built-ins (`/clear`, `/model`, `/compact`) control session. Define your own in `.claude/commands/` or via plugin. **Skills are recommended for multi-step**.
- **Compaction** — auto-summarization when context window fills. Older tool outputs cleared first, then conversation summarized. Project-root CLAUDE.md and auto memory survive (reload from disk); in-conversation instructions may be lost. `/compact focus on X` for targeted manual compaction.
- **Context window** — working memory: history + files + outputs + CLAUDE.md + auto memory + skills + system. `/context` to inspect.
- **Dispatch** — phone-initiated task router; spawns Desktop session from Claude mobile app coding task. Pro/Max plans.
- **Effort level** — adaptive-reasoning thinking budget. Supported on Opus 4.7, Opus 4.6, Sonnet 4.6.
- **Extended thinking** — visible step-by-step reasoning before response. Cap with `MAX_THINKING_TOKENS` or effort level. Gray italic in terminal.
- **Hook** — handler at lifecycle point. Three levels: hook event + matcher + hook handler. Handlers can be shell command / HTTP endpoint / MCP tool / LLM prompt / subagent. Deterministic (fires at fixed points, not model discretion).
- **Managed settings** — org-wide settings file at OS-level path outside `~/.claude`. Users cannot override.
- **MCP** — open standard for connecting AI to data/services. Add via `/mcp` or `.mcp.json`.
- **MCP Tool Search** — defers MCP tool schemas until needed; only names load at startup.
- **Non-interactive mode** — `-p`/`--print` flag. Single prompt + exit. Formerly "headless mode."
- **Output style** — modifies system prompt for behavior/tone/format; turns OFF software-engineering-specific parts (different from CLAUDE.md which is appended as user message). Built-ins: Default, Explanatory, Learning.
- **Permission mode** — `default`, `acceptEdits`, `plan`, `auto`, `dontAsk`, `bypassPermissions`. Cycle with `Shift+Tab`.
- **Permission rule** — settings entry: allow/ask/deny on tool name + arg pattern. Evaluated **deny → ask → allow**, first match wins.
- **Plan mode** — permission mode where Claude researches + proposes without editing. Enter via `/plan` or Shift+Tab.
- **Plugin** — bundle of skills/hooks/subagents/MCP servers. Skills namespaced as `plugin-name:skill-name`.
- **Project trust** — one-time dialog before loading project config. Gates auto-installation of marketplace plugins + project-defined hook execution.
- **Prompt injection** — hostile instructions in files/web pages/tool results. Defenses: permission system, command blocklists, trust verification. Auto mode adds server-side probe + classifier that never sees tool results.
- **Remote Control** — continue local session from phone/browser via claude.ai. Code stays local; only UI is remote. Different from Claude Code on the web (cloud sandbox).
- **Rules** — modular `.claude/rules/*.md` files alongside CLAUDE.md. Path-scope via YAML `paths:` frontmatter — load only when Claude reads matching file.
- **Sandboxing** — OS-level FS+network isolation for Bash tool. Separate layer from permission rules.
- **Session** — cwd-tied conversation with own context. Resume `claude -c`, fork `--fork-session`, parallel terminals. `/clear` starts new; previous stays for `/resume`. Stored at `~/.claude/projects/`.
- **Settings layers** (precedence high→low): managed policy → CLI args → `.claude/settings.local.json` → `.claude/settings.json` → `~/.claude/settings.json`. Arrays merge; scalars override.
- **Skill** — `SKILL.md` file with instructions/knowledge/workflow. Loaded automatically when relevant or invoked via `/skill-name`. Recommended successor to custom commands. Both `.claude/commands/deploy.md` and `.claude/skills/deploy/SKILL.md` create `/deploy`.
- **Subagent** — specialized AI in own context with custom system prompt + tools + permissions. Built-ins: Explore, Plan, general-purpose. Different from agent teams (each agent there is a full session you talk to).
- **Surface** — CLI / VS Code / JetBrains / Desktop / claude.ai. All share engine — CLAUDE.md/settings/skills work across. Slack and Chrome extension are integrations, not surfaces.
- **Teleport** — `/teleport` pulls a cloud session into local terminal. Reverse: `--remote` sends local task to web.
- **Tool** — read file, edit, run shell, search web, spawn subagent. Tools make Claude Code agentic.
- **Worktree isolation** — `-w` flag or `isolation: worktree` in subagent config. Runs in separate git worktree under `.claude/worktrees/` so parallel agents don't overwrite.

**Deprecated/renamed**: Headless mode → Non-interactive mode (same `-p`); Custom commands → Skills (`.claude/commands/` still works); Slash commands → Commands ("Slash" dropped from copy).
