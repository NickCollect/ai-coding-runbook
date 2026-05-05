---
type: summary
source: 01_Raw/code.claude.com/docs/en/analytics.md
source_url: https://code.claude.com/docs/en/analytics
title: "Track team usage with analytics"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Two analytics dashboards depending on plan:

| Plan | URL | Includes |
|---|---|---|
| Teams / Enterprise | `claude.ai/analytics/claude-code` | Usage metrics, contribution metrics with GitHub integration, leaderboard, CSV export |
| API (Console) | `platform.claude.com/claude-code` | Usage metrics, spend tracking, team insights |

**Teams/Enterprise dashboard** (Owner/Admin access):
- **Usage metrics**: lines accepted, suggestion accept rate, daily active users and sessions
- **Contribution metrics** (public beta, requires GitHub app install): PRs and lines shipped with Claude Code assistance
- **Leaderboard**: top 10 contributors by Claude Code volume; "Export all users" downloads full CSV
- For per-user token counts/cost estimates → use OpenTelemetry export

**Setup contribution metrics**:
1. GitHub admin installs Claude GitHub app (`github.com/apps/claude`)
2. Claude Owner enables Claude Code analytics at `claude.ai/admin-settings/claude-code`
3. Enable "GitHub analytics" toggle and complete GitHub auth, select organizations
4. Data appears within 24 hours, daily updates
- **Not available** with Zero Data Retention enabled
- Supports GitHub Cloud and GitHub Enterprise Server

**Summary metrics on dashboard**:
- PRs with CC, Lines of code with CC, PRs with CC (%), Suggestion accept rate (Edit/Write/NotebookEdit), Lines of code accepted
- Metrics are deliberately conservative — represent an underestimate

**PR attribution algorithm**:
1. Extract added lines from PR diff
2. Find Claude Code sessions that edited matching files in the time window (21 days before to 2 days after merge)
3. Match PR lines against Claude Code output (multiple strategies)
4. Lines normalized (whitespace trimmed, multi-spaces collapsed, quotes standardized, lowercased)
5. Tagged PRs labeled `claude-code-assisted` in GitHub

**"Effective lines" rule**: only lines with >3 chars after normalization, excluding empty lines and lines with only brackets/trivial punctuation. Lines >1000 chars excluded (likely minified).

**Excluded from attribution**: lock files (package-lock, yarn.lock, Cargo.lock), generated code (protobuf, build artifacts, minified), build dirs (dist/, build/, node_modules/, target/), test fixtures (snapshots, cassettes, mocks). Substantially rewritten code (>20% diff) is not attributed.

**Charts**: Adoption (users/sessions over time), PRs per user, Pull requests breakdown (with vs without CC, toggleable to lines view), Leaderboard.

**API/Console dashboard** (UsageView permission — Developer/Billing/Admin/Owner roles): Lines accepted, suggestion accept rate, Activity (DAU/sessions), Spend (estimated for analytics; refer billing for actual). Per-user team insights: Members, Spend this month, Lines this month. **No GitHub contribution metrics for API customers**.

**Programmatic access**: GitHub query for label `claude-code-assisted`.
