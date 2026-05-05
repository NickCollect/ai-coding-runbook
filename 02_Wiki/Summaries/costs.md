---
type: summary
source: 01_Raw/code.claude.com/docs/en/costs.md
source_url: https://code.claude.com/docs/en/costs
title: "Manage costs effectively"
summarized_at: 2026-05-05
entities_referenced: [Subagent, Skill, MCP-server, Memory, Hooks, Permission-mode, Settings]
concepts_referenced: [Context-window, Prompt-caching, Agent-team, Extended-thinking]
---

How to track and reduce Claude Code spend. Costs scale with context size; the doc gives both observability tools and reduction strategies.

Cost benchmarks (enterprise averages): ~$13/dev/active day, $150–250/dev/month, with 90% of users under $30/active day.

**Tracking**
- `/usage` — session-level token + estimated dollar figure (local estimate, not authoritative billing). Authoritative source: Usage page in Claude Console.
- For Pro/Max subscribers the dollar figure isn't billing-relevant; subscription includes usage.
- Workspace spend limits + cost reports in Claude Console for API users. Auth creates a "Claude Code" workspace automatically; can't create API keys for it.
- On Bedrock/Vertex/Foundry: Claude Code does NOT send metrics to your cloud — for cost metrics, large enterprises use **LiteLLM** (open-source, unaffiliated, unaudited).
- Background token usage exists (~<$0.04/session) for conversation summarization and command processing.

**Per-user TPM/RPM recommendations** scale inversely with team size: 1–5 users → 200–300k TPM/user; 500+ users → 10–15k TPM/user. Org-level limits, so users can temporarily burst above their share.

**Reduce token usage strategies**
- Manage context: `/clear` between unrelated tasks (rename + resume to come back later); `/compact <instructions>` for guided summarization; CLAUDE.md compact instructions.
- Right model: Sonnet for most tasks; Opus only for complex architecture; subagent `model: haiku` for simple ones; `/model` to switch mid-session, `/effort` for thinking effort, `MAX_THINKING_TOKENS=8000` to cap.
- MCP overhead: tool schemas deferred by default; `/context` shows consumers; prefer CLI tools (`gh`, `aws`); `/mcp` to disable unused.
- Code intelligence plugins for typed languages — precise navigation replaces grep + read; auto type-error reports after edits.
- Offload to hooks: example shows a `PreToolUse` Bash hook that grep-filters test output to only show failures (10k tokens → hundreds). Skills give domain knowledge so Claude doesn't explore.
- Move workflow-specific instructions from CLAUDE.md → skills (load on demand). Keep CLAUDE.md <200 lines.
- Adjust extended thinking: enabled by default; thinking tokens billed as output. Lower effort or disable in `/config`.
- Delegate verbose ops (test runs, doc fetches, log processing) to subagents — verbose output stays in subagent context.
- **Agent teams**: ~7x more tokens than standard sessions when teammates run plan mode (each is a separate Claude instance). Disabled by default; enable via `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`.
- Specific prompts beat vague ones; plan mode for complex tasks; course-correct early with Esc / `/rewind`; give verification targets; test incrementally.

Run `claude --version` to check version when behavior changes.
