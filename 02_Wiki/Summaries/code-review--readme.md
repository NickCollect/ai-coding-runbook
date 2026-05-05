---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/code-review/README.md
title: "Code Review Plugin"
summarized_at: 2026-05-05
entities_referenced: [Plugin, Subagent, Slash-command, Memory]
concepts_referenced: []
---

Plugin from anthropics/claude-code repo. Automates PR review using multiple parallel subagents with confidence-based scoring to filter false positives.

**Command**: `/code-review [--comment]` — defaults to terminal output; `--comment` posts as PR review comment.

**Pipeline**:
1. Skip if PR closed/draft/trivial/already-reviewed.
2. Gather relevant CLAUDE.md files.
3. Summarize PR changes.
4. Launch 4 parallel agents:
   - Two CLAUDE.md compliance auditors (redundancy).
   - One bug detector focused only on changes (not pre-existing).
   - One git-blame/history analyzer for context.
5. Each issue scored 0–100 confidence.
6. Filter <80 threshold.
7. Output (terminal or PR comment).

**Confidence scale**: 0=false positive, 25=somewhat confident, 50=moderate but minor, 75=highly confident important, 100=absolutely certain.

**Filtered out**: pre-existing issues, look-alike bugs, pedantic nitpicks, lint-catchable issues, general quality (unless in CLAUDE.md), issues with lint-ignore comments.

**Comment format** uses GitHub permalinks with full SHA + `#L<start>-L<end>` (must include line range).

**Requirements**: Git repo with GitHub integration, `gh` CLI installed/authenticated. CLAUDE.md optional but improves compliance checking.

**Configuration**: edit `commands/code-review.md` to change threshold (`Filter out any issues with a score less than 80`) or add agent tasks (security/perf/accessibility/docs).

Author: Boris Cherny (boris@anthropic.com). Version 1.0.0.
