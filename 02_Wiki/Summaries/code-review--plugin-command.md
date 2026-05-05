---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/code-review/commands/code-review.md
title: "code-review (plugin slash command)"
summarized_at: 2026-05-05
entities_referenced: [Slash-command, Subagent, MCP-server, Memory]
concepts_referenced: []
---

Slash command shipped in the `code-review` plugin. PR code-review orchestrator that dispatches multiple parallel subagents (Haiku/Sonnet/Opus) for different review concerns.

**Frontmatter**:
- `allowed-tools`: `Bash(gh issue view:*)`, `Bash(gh search:*)`, `Bash(gh issue list:*)`, `Bash(gh pr comment:*)`, `Bash(gh pr diff:*)`, `Bash(gh pr view:*)`, `Bash(gh pr list:*)`, `mcp__github_inline_comment__create_inline_comment`
- `description`: Code review a pull request

**Agent assumptions** (applied to all subagents): all tools are functional — don't test/exploratorily call. Only call a tool if needed for the task.

**Workflow** (precise sequence):

1. **Eligibility check (Haiku)**: skip if PR closed, draft, doesn't need review (automated/trivial), or Claude has already commented (`gh pr view <PR> --comments`). **Still review Claude-generated PRs.**
2. **CLAUDE.md gathering (Haiku)**: list paths (not contents) of root CLAUDE.md + any CLAUDE.md in dirs containing modified files
3. **PR summary (Sonnet)**: view PR + return change summary
4. **4 parallel reviewers**:
   - Agents 1+2: CLAUDE.md compliance (Sonnet) — only consider CLAUDE.md files at file's path or parents
   - Agent 3: Opus bug agent — scan for obvious bugs in diff only, no extra context, only significant + validatable
   - Agent 4: Opus bug agent (parallel with #3) — security issues / incorrect logic in introduced code
   - **HIGH SIGNAL ONLY**: only flag if compile/parse will fail, definite wrong-result logic errors, clear unambiguous CLAUDE.md violations with quotable rules. Never flag style/quality, input-dependent issues, subjective suggestions. False positives erode trust.
   - All subagents get PR title + description for author intent
5. **Validation pass**: parallel subagents validate each flagged issue (Opus for bugs/logic, Sonnet for CLAUDE.md). Issue must be genuinely there with high confidence.
6. Filter to validated issues only
7. **Output**: terminal summary always; if `--comment` arg AND no issues → post summary comment; if `--comment` AND issues → continue to step 8
8. Internal list of planned comments (don't post)
9. Post inline comments via `mcp__github_inline_comment__create_inline_comment` with `confirmed: true`. Small fixes get committable suggestion blocks; larger fixes (6+ lines, structural, multi-location) get description only. **Only commit suggestion if it fixes the issue ENTIRELY.** ONE comment per unique issue, no duplicates.

**False-positive blocklist** (do NOT flag): pre-existing issues, things that look like bugs but are correct, pedantic nitpicks senior engineer wouldn't flag, linter-catchable issues (don't run linter), general code-quality concerns unless explicitly required in CLAUDE.md, issues mentioned in CLAUDE.md but explicitly silenced (e.g., lint-ignore comment).

**Linking format** (load-bearing):
`https://github.com/anthropics/claude-code/blob/c21d3c10bc8e898b7ac1a2d745bdc9bc4e423afe/package.json#L10-L15`
- Full git SHA required (`$(git rev-parse HEAD)` won't work — directly rendered in Markdown)
- Repo name must match
- `#` after filename
- Range `L[start]-L[end]`
- Center range with at least 1 line of context before and after the focus line
