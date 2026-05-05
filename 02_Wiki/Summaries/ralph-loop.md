---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/ralph-wiggum/commands/ralph-loop.md
title: "/ralph-wiggum:ralph-loop (slash command)"
summarized_at: 2026-05-05
entities_referenced: [Slash-command, Plugin, Hooks]
concepts_referenced: []
---

Slash command in the `ralph-wiggum` plugin (named after the Simpsons character — implements a self-restarting agent loop). Frontmatter: `description: "Start Ralph Wiggum loop in current session"`, `argument-hint: "PROMPT [--max-iterations N] [--completion-promise TEXT]"`, `allowed-tools: ["Bash(${CLAUDE_PLUGIN_ROOT}/scripts/setup-ralph-loop.sh:*)"]`, `hide-from-slash-command-tool: "true"`.

**Mechanism**: runs `${CLAUDE_PLUGIN_ROOT}/scripts/setup-ralph-loop.sh $ARGUMENTS` to initialize a hook-driven loop. When Claude tries to exit, the Ralph loop **feeds the SAME PROMPT back** for the next iteration. Claude sees its previous work in files and git history, enabling iterative refinement.

**Critical rule (told to Claude)**: If a `--completion-promise` text is set, Claude may ONLY output that exact phrase when the statement is completely and unequivocally TRUE. Do NOT output false promises to escape the loop, even if you think you're stuck. The loop is designed to continue until genuine completion.

Args: free-form PROMPT, optional `--max-iterations N` (cap), optional `--completion-promise TEXT` (exit phrase).

The hook side of the plugin (in `hooks/hooks.json`) presumably catches `Stop` events and re-injects the prompt — only relevant code shown in this command file is the bootstrap script invocation.
