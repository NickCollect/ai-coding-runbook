---
type: summary
source: 01_Raw/code.claude.com/docs/en/gitlab-ci-cd.md
source_url: https://code.claude.com/docs/en/gitlab-ci-cd
title: "Claude Code GitLab CI/CD"
summarized_at: 2026-05-05
entities_referenced: [CI-integration, Agent-SDK, Enterprise-gateway, Memory, Permission-mode]
concepts_referenced: []
---

GitLab CI/CD integration for Claude Code (currently **beta**, maintained by GitLab, not Anthropic). Built on top of Claude Code CLI + Agent SDK. Lets `@claude` mentions in issues / MRs / review threads trigger CI jobs that propose code changes via MR.

Why use it: instant MR creation from comments, automated implementation of issues, project-aware (reads `CLAUDE.md`), simple setup (one job + one masked CI variable), enterprise-ready (Claude API / Bedrock / Vertex AI), runs in your runners with branch protection.

**Quick setup**:
1. Add `ANTHROPIC_API_KEY` as a masked CI/CD variable.
2. Add a `claude` job to `.gitlab-ci.yml` that installs Claude Code via `curl -fsSL https://claude.ai/install.sh | bash` and runs `claude -p "${AI_FLOW_INPUT}" --permission-mode acceptEdits --allowedTools "Bash Read Edit Write mcp__gitlab" --debug`.
3. Trigger via MR events, web/manual run, or a webhook listener that fires on `@claude`-containing comments.

**Provider options** (enterprise):
- **Claude API** — `ANTHROPIC_API_KEY` masked variable.
- **Amazon Bedrock** — GitLab OIDC + IAM role + `AWS_ROLE_TO_ASSUME` / `AWS_REGION`. Job exchanges `CI_JOB_JWT_V2` for AWS creds via `aws sts assume-role-with-web-identity`. Models use region prefix (e.g. `us.anthropic.claude-sonnet-4-6`).
- **Google Vertex AI** — Workload Identity Federation, `GCP_WORKLOAD_IDENTITY_PROVIDER` / `GCP_SERVICE_ACCOUNT` / `CLOUD_ML_REGION`. `gcloud auth login --cred-file=<(...)` exchanges OIDC for GCP token without stored keys.

**Project credentials**: `CI_JOB_TOKEN` works by default; for richer permissions create a Project Access Token with `api` scope and store as `GITLAB_ACCESS_TOKEN`.

**Common parameters**: `prompt`/`prompt_file`, `max_turns`, `timeout_minutes`. The `mcp__gitlab` MCP tool is the GitLab-specific one (a `gitlab-mcp-server` binary may be available in the runner image).

**Use cases**: turn issues into MRs (`@claude implement this feature`), propose caching strategies, fix bugs (`@claude fix the TypeError…`).

**Best practices**: keep `CLAUDE.md` focused; use OIDC over long-lived keys; limit job permissions and egress; review Claude's MRs as any contributor; cache npm installs; use specific `@claude` commands to limit turns; set `max_turns` and timeouts.

**Costs**: GitLab runner minutes + Claude API tokens.

**Troubleshooting**:
- `@claude` not responding → verify pipeline trigger, mention listener, mention syntax (`@claude` not `/claude`).
- Can't comment / open MR → `CI_JOB_TOKEN` perms or PAT; `mcp__gitlab` enabled in `--allowedTools`.
- Auth errors → check API key validity / OIDC trust / region.

Run `claude --help` inside the job to discover supported flags for your version.
