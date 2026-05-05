---
type: summary
source: 01_Raw/code.claude.com/docs/en/code-review.md
source_url: https://code.claude.com/docs/en/code-review
title: "Code Review (managed PR review service)"
summarized_at: 2026-05-05
entities_referenced: [Memory, Plugin-marketplace, CI-integration, Enterprise-gateway]
concepts_referenced: [Agent-team]
---

Anthropic-managed PR-review service (research preview, Team/Enterprise only, NOT available with Zero Data Retention). A fleet of specialized agents review GitHub PRs in parallel on Anthropic infra, then a verification step filters false positives. Findings post as inline comments on diff lines with severity tags. Reviews scale in cost with PR size, complete in ~20 min on average, $15-25 per review average. **Billed separately as extra usage**, not against plan inclusions.

To run reviews in your own CI instead, see `GitHub Actions` / `GitLab CI/CD` / `GitHub Enterprise Server`.

**Severity tags**: 🔴 Important (bug, fix before merge), 🟡 Nit (worth fixing, non-blocking), 🟣 Pre-existing (bug not introduced by this PR). Findings include collapsible extended-reasoning section.

**Trigger modes** per repo:
- *Once after PR creation*
- *After every push* (auto-resolves threads as issues are fixed; most expensive)
- *Manual* — `@claude review` (subscribes PR to push triggers) or `@claude review once` (one-shot, no subscription)

Manual triggers must be top-level PR comments, command at start of comment, posted by owner/member/collaborator on an open PR. Manual triggers also work on draft PRs.

**Check run "Claude Code Review"** completes with **neutral** conclusion (never blocks merge). Findings summary in Details, plus annotations on the Files changed tab. Last line of Details has a machine-readable JSON severity breakdown:
```bash
gh api repos/OWNER/REPO/check-runs/CHECK_RUN_ID \
  --jq '.output.text | split("bughunter-severity: ")[1] | split(" -->")[0] | fromjson'
```
returns `{"normal": N, "nit": N, "pre_existing": N}`. CI can read this to gate merges.

**Customization**:
- **`CLAUDE.md`** — project memory, used for general Claude Code context. Code Review reads it and treats newly introduced violations as nits. Hierarchical (subdir CLAUDE.md scopes to subtree). Bidirectional: edits that contradict CLAUDE.md are flagged so docs get updated.
- **`REVIEW.md`** — review-only, repo-root, injected as highest-priority instruction block. `@import` syntax NOT expanded — paste rules verbatim. Use for: redefining "Important" severity, capping nits, skip-paths/branches/categories, repo-specific must-checks (e.g. "new API routes need integration tests"), verification bar (require file:line citations), re-review convergence ("after first review, suppress new nits"), summary shape (one-line tally up front). Keep focused — long REVIEW.md dilutes priority signal.

**Reactions**: 👍/👎 pre-attached to each comment for one-click rating; counts collected post-merge to tune the reviewer. Reactions don't trigger re-review. Replying inline doesn't prompt Claude — push a fix or use `@claude review once`.

**Setup** by org admin via `claude.ai/admin-settings/claude-code`: install Claude GitHub App (Contents R/W, Issues R/W, PRs R/W), select repos, set per-repo Review Behavior. Spend cap configurable at `claude.ai/admin-settings/usage`.

**Troubleshooting**: failed/timed-out runs surface "Code review encountered an error" / "timed out"; comment `@claude review once` to retry. GitHub's "Re-run" button does NOT work. Spend-cap exhaustion posts a single skip comment until next billing cycle. If check run says findings exist but inline comments missing → check Details table, Files changed annotations, and "Additional findings" in review body (for findings on lines that moved during the review).

Related: `code-review` plugin for local on-demand reviews before pushing.
