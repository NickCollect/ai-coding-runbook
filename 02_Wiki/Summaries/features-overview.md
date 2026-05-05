---
type: summary
source: 01_Raw/code.claude.com/docs/en/features-overview.md
source_url: https://code.claude.com/docs/en/features-overview
title: "Extend Claude Code"
summarized_at: 2026-05-05
entities_referenced: [Memory, Skill, Subagent, MCP-server, Hooks, Plugin, Plugin-marketplace]
concepts_referenced: [Agentic-loop, Context-window, Agent-team]
---

Decision guide for picking the right Claude Code extension mechanism. Each feature plugs into a different point of the agentic loop.

**The seven extension surfaces:**
- **CLAUDE.md** — persistent context loaded every session ("always do X" rules).
- **Skills** — reusable knowledge / invocable workflows (`/deploy` style; reference docs).
- **MCP** — connect external services (database, Slack, browser).
- **Subagents** — isolated context, returns only summary (research, parallel tasks).
- **Agent teams** — multiple coordinated independent sessions with peer messaging (parallel research, multi-perspective review).
- **Hooks** — script/HTTP/prompt/subagent triggered by lifecycle events (PostToolUse, SessionStart, etc.).
- **Plugins / Marketplaces** — packaging and distribution layer.

**Trigger-based adoption order**:
| Trigger | Add |
|---|---|
| Claude gets a convention wrong twice | CLAUDE.md |
| Repeating same prompt to start a task | User-invocable skill |
| Pasting same playbook 3rd time | Skill |
| Copying from a tab Claude can't see | MCP server |
| Side task floods conversation | Subagent |
| Want it to happen every time | Hook |
| Second repo needs same setup | Plugin |

**Comparison highlights**:
- Skill vs Subagent: skills = reusable content; subagents = isolated workers with own context. Can combine (`skills:` field on subagent, or `context: fork` on skill).
- CLAUDE.md vs Skill: always-on rules vs on-demand reference / workflow. Both support `@path` imports. Keep CLAUDE.md <200 lines.
- CLAUDE.md vs Rules vs Skills: rules with `paths:` frontmatter load only when matching files open — middle ground between always-on (CLAUDE.md) and on-demand (skills).
- Subagent vs Agent team: subagent reports back to caller; agent teams coordinate independently, much higher token cost.
- MCP vs Skill: MCP = capability; Skill = how to use it well. MCP connects to DB; skill documents schema/query patterns.
- Hook vs Skill: hooks are deterministic guards (block `rm -rf`, lint after edit, post Slack); skills are interpreted instructions. **Guardrails belong in hooks** — instructions in CLAUDE.md/skill are requests, not enforcement.

**Layering** (when same feature defined at multiple levels):
- CLAUDE.md: additive, all levels merge.
- Skills/Subagents: override by name. Skills priority: managed > user > project. Subagents: managed > CLI flag > project > user > plugin. Plugin skills are namespaced (`/my-plugin:review`) so they don't collide.
- MCP servers: local > project > user.
- Hooks: merge — all matching hooks fire regardless of source.

**Combination patterns**:
- Skill + MCP: MCP gives capability, skill teaches usage.
- Skill + Subagent: `/audit` skill spawns security/perf/style subagents.
- CLAUDE.md + Skills: rules for always; skills for sometimes.
- Hook + MCP: hook triggers external action via MCP.

**Context-cost cheatsheet**:
| Feature | When loads | What loads | Cost |
|---|---|---|---|
| CLAUDE.md | Session start | Full content | Every request |
| Skills | Start (descriptions) + on-use (full) | Names+descriptions; full when invoked | Low; zero for `disable-model-invocation: true` |
| MCP | Session start | Tool names; schemas deferred (tool search) | Low until used |
| Subagents | On spawn | Fresh context; specified skills preloaded; CLAUDE.md + git status inherited | Isolated |
| Hooks | On trigger | Nothing by default | Zero unless hook returns output |

Subagents do NOT inherit skills from main session — must be specified explicitly via `skills:` field.

MCP reliability gotcha: connections can drop silently mid-session — Claude may try a tool that no longer exists. Check with `/mcp`.
