---
type: summary
source: 01_Raw/code.claude.com/docs/en/github-actions.md
source_url: https://code.claude.com/docs/en/github-actions
title: "Claude Code GitHub Actions"
summarized_at: 2026-05-05
entities_referenced: [CI-integration, Agent-SDK, Memory, Skill, MCP-server, Enterprise-gateway]
concepts_referenced: []
---

`anthropics/claude-code-action@v1` GitHub Action — `@claude` mention any PR/issue and Claude analyzes, implements, fixes, opens PRs. Built on top of the Agent SDK. Default model is **Sonnet**; pass `--model claude-opus-4-7` via `claude_args` to upgrade. For automatic per-PR review (no trigger needed) use the managed Code Review service instead.

**Quick setup**: in CLI run `/install-github-app`. Repo admin required. Installs the Claude GitHub App (Contents/Issues/PRs R/W) + adds `ANTHROPIC_API_KEY` secret. Quick setup is direct-API only — Bedrock/Vertex go through the manual cloud-provider workflow.

**Manual setup**: install app from `github.com/apps/claude`, add `ANTHROPIC_API_KEY` repo secret, copy workflow from `examples/claude.yml`.

**v1 from beta — breaking changes**:
- `@beta` → `@v1`
- Remove `mode: "tag"|"agent"` (auto-detected from event)
- `direct_prompt` → `prompt`
- `custom_instructions` / `max_turns` / `model` / `allowed_tools` / `disallowed_tools` → consolidated into `claude_args` (e.g. `--append-system-prompt`, `--max-turns`, `--model`, `--allowedTools`, `--disallowedTools`)
- `claude_env` → `settings` JSON

**v1 parameters**:
| Parameter | Required |
|---|---|
| `prompt` | No (omit for `@claude` mention mode) |
| `claude_args` | No (passes any CLI flag) |
| `anthropic_api_key` | Yes for direct API |
| `github_token` | No |
| `trigger_phrase` | No (default `"@claude"`) |
| `use_bedrock` | No |
| `use_vertex` | No |

`prompt` can also accept a skill name to invoke an installed skill.

**Use cases shown**:
- Comment-triggered (`@claude implement this feature`, `how should I implement auth?`, `fix the TypeError in dashboard`)
- Scheduled cron (daily report)
- Auto code review on PR open/sync

**Cost**: GitHub Actions runner minutes + API tokens (per claude.com/platform/api). Optimization: specific `@claude` commands, lower `--max-turns`, workflow timeouts, GitHub concurrency controls.

**Bedrock / Vertex setup** (recommended: use a custom GitHub App for branding + better security):
- **Bedrock**: enable Bedrock + request Claude model access; configure GitHub OIDC identity provider in AWS (`https://token.actions.githubusercontent.com`, audience `sts.amazonaws.com`); IAM role with `AmazonBedrockFullAccess` and trust policy for repo. Required secret: `AWS_ROLE_TO_ASSUME`. Workflow uses `aws-actions/configure-aws-credentials@v4` then `use_bedrock: "true"`. Model IDs prefixed: `us.anthropic.claude-sonnet-4-6`.
- **Vertex AI**: enable IAM Credentials API + STS API + Vertex AI API; create Workload Identity Pool + GitHub OIDC provider; service account with `Vertex AI User`; IAM bindings allowing pool to impersonate SA. Required secrets: `GCP_WORKLOAD_IDENTITY_PROVIDER`, `GCP_SERVICE_ACCOUNT`. Workflow uses `google-github-actions/auth@v2` then `use_vertex: "true"`. Region env vars: `ANTHROPIC_VERTEX_PROJECT_ID`, `CLOUD_ML_REGION`, `VERTEX_REGION_CLAUDE_4_5_SONNET`.

**Custom GitHub App** for cloud providers: create at `github.com/settings/apps/new`, no webhooks, repo perms (Contents R/W, Issues R/W, PRs R/W), generate private key, store as `APP_PRIVATE_KEY` + `APP_ID` secrets, mint tokens via `actions/create-github-app-token@v2`.

**Required workflow permissions**: `contents: write`, `pull-requests: write`, `issues: write`, `id-token: write` (for OIDC).

Customize behavior: `CLAUDE.md` for project rules + `prompt` for workflow-specific instructions.
