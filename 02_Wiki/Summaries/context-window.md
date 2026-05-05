---
type: summary
source: 01_Raw/code.claude.com/docs/en/context-window.md
source_url: https://code.claude.com/docs/en/context-window
title: "Explore the context window"
summarized_at: 2026-05-05
entities_referenced: [Memory, Skill, MCP-server, Hooks, Subagent, Output-style, Slash-command]
concepts_referenced: [Context-window, Agentic-loop]
---

This page is mostly an interactive JSX simulation; the actual prose content is small. Raw is mostly Mintlify component definitions — this summary captures the substance.

**What loads at session start (before user types)**:
- System prompt (~4.2K tokens) — invisible.
- Auto memory `MEMORY.md` (~680 tokens, first 200 lines or 25KB).
- Environment info (~280 tokens; cwd, platform, shell, OS, git status).
- MCP tool names (~120 tokens deferred — full schemas load via tool search; `ENABLE_TOOL_SEARCH=auto` loads upfront when fits in 10%).
- Skill descriptions (~450 tokens — full body loads on invocation; skills with `disable-model-invocation: true` excluded from index entirely).
- `~/.claude/CLAUDE.md` (~320 tokens user-global) + project `CLAUDE.md` (~1.8K).

**As Claude works**: each file read consumes context (file reads dominate usage). Path-scoped rules (`.claude/rules/*.md` with `paths:` frontmatter) auto-load when matching files are read. PostToolUse hooks fire silently — output via `hookSpecificOutput.additionalContext` JSON enters context; plain stdout on exit 0 goes to debug log only; exit code 2 surfaces stderr to Claude.

**Subagents** get separate context: their own system prompt (no main-session auto memory), own copy of CLAUDE.md (counts against subagent, not main), MCP+skills, and the parent's task prompt. Tools restricted: no plan-mode controls, no background-task tools, no Agent tool by default (anti-recursion). Only the subagent's final text + small metadata trailer returns to main context.

**Bang commands** (`!cmd`) run in shell and prefix output to next message — both command and output enter context.

**`disable-model-invocation: true` skills** stay completely out of context until invoked manually; tip: use for skills with side effects (commit, deploy, send messages).

**What survives `/compact`**:
| Mechanism | After compact |
|---|---|
| System prompt + output style | Unchanged (not in message history) |
| Project-root CLAUDE.md + unscoped rules | Re-injected from disk |
| Auto memory | Re-injected from disk |
| Rules with `paths:` frontmatter | LOST until matching file read again |
| Nested CLAUDE.md in subdirs | LOST until file in subdir read again |
| Invoked skill bodies | Re-injected, capped 5K tokens/skill, 25K total, oldest dropped |
| Hooks | N/A (run as code) |

Skill truncation keeps the start of `SKILL.md` — put critical instructions at top.

**Inspect**: `/context` for live breakdown by category + optimization suggestions; `/memory` to see loaded CLAUDE.md and auto-memory files.
