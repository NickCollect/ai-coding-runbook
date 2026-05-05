---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/README.md
title: "Claude Code Plugins (repo plugins directory README)"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Slash-command, Subagent, Hooks, MCP-server, Skill]
concepts_referenced: []
---

Catalog of official Claude Code plugins shipped in the `anthropics/claude-code` repo under `./plugins/`. These are example plugins; many more available via community marketplaces.

**Plugins listed**:
| Name | Purpose |
|---|---|
| **agent-sdk-dev** | `/new-sdk-app` interactive Agent SDK setup; verifier subagents (`agent-sdk-verifier-py`, `agent-sdk-verifier-ts`) |
| **claude-opus-4-5-migration** | Skill migrating model strings + beta headers + prompt adjustments from Sonnet 4.x / Opus 4.1 to Opus 4.5 |
| **code-review** | `/code-review` PR review workflow; 5 parallel Sonnet agents (CLAUDE.md compliance, bug detection, historical context, PR history, code comments) with confidence-based scoring |
| **commit-commands** | `/commit`, `/commit-push-pr`, `/clean_gone` git workflow automation |
| **explanatory-output-style** | SessionStart hook injecting educational context (mimics deprecated Explanatory output style) |
| **feature-dev** | `/feature-dev` 7-phase guided feature workflow; `code-explorer`, `code-architect`, `code-reviewer` subagents |
| **frontend-design** | Skill auto-invoked for frontend work — distinctive design choices, typography, animations |
| **hookify** | `/hookify`, `/hookify:list/configure/help` — generate hooks from conversation patterns; `conversation-analyzer` agent; `writing-rules` skill |
| **learning-output-style** | SessionStart hook for interactive learning mode requesting 5–10-line user contributions at decision points |
| **plugin-dev** | `/plugin-dev:create-plugin` 8-phase guided plugin builder; `agent-creator`, `plugin-validator`, `skill-reviewer` agents; 7 expert skills covering hooks, MCP integration, plugin structure, settings, commands, agents, skill development |
| **pr-review-toolkit** | `/pr-review-toolkit:review-pr` — comments/tests/errors/types/code/simplify/all aspects; 6 specialist agents |
| **ralph-wiggum** | `/ralph-loop`, `/cancel-ralph` self-referential iteration loops; Stop hook intercepts exit |
| **security-guidance** | PreToolUse hook monitoring 9 security patterns (command injection, XSS, eval, dangerous HTML, pickle, os.system) |

**Standard plugin structure**:
```
plugin-name/
├── .claude-plugin/plugin.json
├── commands/ (optional)
├── agents/ (optional)
├── skills/ (optional)
├── hooks/ (optional)
├── .mcp.json (optional)
└── README.md
```

Install plugins via `/plugin` command or configure in `.claude/settings.json`.
