---
type: summary
source: 01_Raw/anthropic.com/engineering/swe-bench-sonnet.md
source_url: https://www.anthropic.com/engineering/swe-bench-sonnet
title: "Raising the bar on SWE-bench Verified with Claude 3.5 Sonnet"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: [Tool-use, Agentic-loop]
---

Anthropic engineering post (Jan 06, 2025) describing the agent scaffold used to achieve **49% on SWE-bench Verified** with the upgraded Claude 3.5 Sonnet (vs prior SOTA 45%).

**SWE-bench background.** AI eval benchmark testing real GitHub-issue resolution on popular Python repos. Each task: model gets a configured Python environment + repo checkout from just before the issue was resolved; must understand, modify, and test the code. Solutions graded against the actual unit tests from the human-authored PR. Why popular: real engineering tasks (not interview-style), not yet saturated, measures the *agent* (model + scaffolding) not the model alone.

**SWE-bench Verified.** 500-problem human-reviewed subset of SWE-bench filtering out impossible-without-context tasks. The clearest measure of coding-agent performance.

**Anthropic's design philosophy.** Maximum control to the language model itself; minimal scaffolding. The agent has: a prompt, a Bash tool (execute bash commands), an Edit tool (view/create/edit files). Sample until model decides it's done or hits the 200K context limit. No hardcoded workflow.

**The prompt.** Outlines a suggested approach (5 steps: explore repo, write reproduction script, edit source, rerun reproduction, think about edge cases) but doesn't enforce it strictly. The prompt also tells Claude that test files have already been modified — Claude should only change non-test files. "Your thinking should be thorough and so it's fine if it's very long."

**Bash tool.** Simple schema (just `command: string`). The *description* carries the weight: explains escaping, lack of internet access, available `apt`/`pip` mirror, persistent state across calls, how to inspect line ranges via `sed -n`, avoiding huge-output commands, running long-lived commands in the background.

**Edit tool (`str_replace_editor`).** More complex; covers viewing, creating, editing files. `view` on a file shows `cat -n` output; on a dir, lists 2 levels deep. `create` fails if path exists. Long output truncated with `<response clipped>`. `undo_edit` reverts last edit. `str_replace` requires `old_str` to match exactly one or more consecutive lines (whitespace-sensitive); replacement skipped if `old_str` non-unique — instructs the model to include enough surrounding context.

**Key engineering takeaway.** Tool descriptions and specs deserve as much design attention as human-facing UI. Anthropic stress-tests them across many agentic tasks, finds ways the model could misunderstand or trip up, and edits descriptions to preempt those problems. The post is positioned as practical guidance for developers building Claude-powered coding agents — show how minimal scaffolding + carefully-designed tool ergonomics + permissive sampling reaches state-of-the-art on a hard, real-world benchmark.
