---
type: entity
name: CI-integration
aliases: [GitHub Actions, GitLab CI, CI integration]
category: integration
status: ga
created: 2026-05-05
---

## 一句话定义

Claude Code 在 CI/CD 里的集成（GitHub Actions / GitLab CI/CD）

## 关键属性

- 通过 `anthropics/claude-code-action@v1` 把 `@claude` 提及在 PR/issue/review comment 触发为 CI job，行为基于 Agent SDK [[github-actions]] [[claude]]
- 默认 model 为 Sonnet，需用 `claude_args: "--model claude-opus-4-7"` 升级 [[github-actions]]
- 快速安装：CLI 内 `/install-github-app` — 安装 GitHub App + 写入 `ANTHROPIC_API_KEY` repo secret；要 repo admin 权限 [[github-actions]]
- Workflow 必需 permissions：`contents: write`、`pull-requests: write`、`issues: write`、`id-token: write`（用 OIDC 时） [[github-actions]] [[claude]]
- v1 breaking changes（vs beta）：`mode` 自动检测移除、`direct_prompt` → `prompt`、多个参数（`max_turns`/`model`/`allowed_tools`）合并到 `claude_args`、`claude_env` → `settings` JSON [[github-actions]]
- Bedrock / Vertex 走 GitHub OIDC：AWS 用 `AmazonBedrockFullAccess` IAM role + `AWS_ROLE_TO_ASSUME` secret；GCP 用 Workload Identity Pool + `GCP_WORKLOAD_IDENTITY_PROVIDER` / `GCP_SERVICE_ACCOUNT` secret；推荐配自定义 GitHub App 提升安全 + 品牌 [[github-actions]]
- GitLab CI/CD 集成（**beta，由 GitLab 维护**）：把 `ANTHROPIC_API_KEY` 设为 masked CI variable，job 用 `curl ...claude.ai/install.sh` 装 Claude Code，再跑 `claude -p "${AI_FLOW_INPUT}" --permission-mode acceptEdits --allowedTools "Bash Read Edit Write mcp__gitlab"` [[gitlab-ci-cd]]
- GitLab 同样支持 Bedrock / Vertex via OIDC（用 `CI_JOB_JWT_V2` 换 cloud token）；专属 `mcp__gitlab` MCP tool 处理 GitLab API [[gitlab-ci-cd]]
- GitHub Enterprise Server 支持（Team/Enterprise plan only）：admin 在 `claude.ai/admin-settings/claude-code` 一次性接入；`/install-github-app` 仅 github.com，需手工 workflow setup；GitHub MCP server **不支持**（用 `gh` CLI 替代） [[github-enterprise-server]]
- App 订阅事件：`pull_request`、`issue_comment`、`pull_request_review_comment`、`pull_request_review`、`check_run`；GHES 还需 `Checks` rw + `Repository hooks` rw [[github-enterprise-server]]
- Workflow trigger 通常 if-filter `contains(github.event.comment.body, '@claude')`；可同时绑 `issues`/`issue_comment`/`pull_request_review_comment`/`pull_request_review` 多事件 [[claude]]
- `prompt` 字段也可填一个 installed skill 名来触发该 skill；定时任务可用 GitHub Actions cron schedule [[github-actions]]
- 与 Anthropic 托管的 **Code Review** 服务区分：CI integration 跑在你的 runner（按 token + runner minutes 计费），Code Review 跑在 Anthropic infra（Team/Enterprise + extra usage，每 PR ≈$15-25） [[code-review]] [[github-actions]]
- 三种 scheduling 选项：Routines（cloud cron）、Desktop scheduled tasks（本机）、GitHub Actions（repo-event 触发） [[scheduled-tasks]] [[common-workflows]] [[platforms]]
- 成本控制建议：specific `@claude` 命令、降 `--max-turns`、加 workflow timeout、GitHub concurrency 限制 [[github-actions]] [[gitlab-ci-cd]]

## 出现来源

_20 summaries reference this entity_:

- [[auto-close-duplicates]]
- [[backfill-duplicate-comments-workflow]]
- [[claude]]
- [[claude-dedupe-issues]]
- [[claude-issue-triage]]
- [[code-review]]
- [[common-workflows]]
- [[github-actions]]
- [[github-enterprise-server]]
- [[gitlab-ci-cd]]
- [[issue-lifecycle-comment-workflow]]
- [[issue-opened-dispatch]]
- [[log-issue-events]]
- [[non-write-users-check-workflow]]
- [[overview--claude-code]]
- [[platforms]]
- [[remove-autoclose-label]]
- [[review-pr]]
- [[routines]]
- [[scheduled-tasks]]

## 相关

- [[Headless-mode]] — `claude -p` 是 CI 内的执行模式
- [[Agent-SDK]] — `claude-code-action` 在 SDK 之上构建
- [[Routine]] — 替代方案，由 Anthropic cloud 托管的定时执行
- [[Scheduled-task]] — 桌面端等价物
- [[Enterprise-gateway]] — Bedrock / Vertex 集成路径
- [[MCP-server]] — `mcp__gitlab` 等专属 MCP server 用于 CI 内 API 调用
- [[Memory]] — workflow 借助 `CLAUDE.md` 做 project memory
