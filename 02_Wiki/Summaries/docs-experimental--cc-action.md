---
type: summary
source: 01_Raw/github/anthropics/claude-code-action/docs/experimental.md
source_url: https://github.com/anthropics/claude-code-action/blob/main/docs/experimental.md
title: "Claude Code Action — docs/experimental"
summarized_at: 2026-05-05
entities_referenced: [CI-integration]
concepts_referenced: []
---

Experimental features in the Claude Code Action. Treated as unstable and not supported for production — may change or be removed at any time.

**Automatic mode detection.** The action picks the appropriate execution mode from workflow context, eliminating the need for manual mode configuration.

- **Interactive Mode (Tag Mode).** Activated when Claude detects `@mentions`, issue assignments, or labels — without an explicit `prompt`. Triggers: `@claude` in comments, issue assignment to a Claude user, label application. Features: tracking comments with progress checkboxes, full implementation capabilities. Use case: interactive code assistance, Q&A, implementation requests.
- **Automation Mode (Agent Mode).** Auto-activated when `prompt` is provided. Triggers: any GitHub event when `prompt` is set. Features: direct execution without `@claude`, streamlined for automation. Use case: automated PR reviews, scheduled tasks, workflow automation.

**Resolution logic:**

1. If `prompt` is provided → agent mode.
2. If no `prompt` but `@claude` is mentioned → tag mode.
3. If neither → no action taken.

**Advanced mode control.** Fine-tune behavior via `claude_args`, e.g.:

```yaml
- uses: anthropics/claude-code-action@v1
  with:
    prompt: "Review this PR"
    claude_args: |
      --max-turns 20
      --system-prompt "You are a code review specialist"
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
```

The page is intentionally short — it documents the in-flight detection behavior and reminds callers that everything here is experimental.
