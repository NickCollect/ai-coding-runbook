---
type: summary
source: 01_Raw/github/anthropics/claude-code/plugins/plugin-dev/skills/plugin-structure/examples/advanced-plugin.md
title: "Advanced Plugin Example (enterprise-devops)"
summarized_at: 2026-05-05
entities_referenced: [Plugin, MCP-server, Subagent, Skill, Slash-command, Hooks]
concepts_referenced: []
---

Reference example of a complex enterprise plugin (`enterprise-devops`) showing multi-level organization across all plugin component types. Used by the `plugin-structure` skill as a target architecture.

**Directory layout** organizes by function:
- `commands/{ci,monitoring,admin}/*.md` — grouped by category.
- `agents/{orchestration,specialized}/*.md` — separated by role.
- `skills/{kubernetes-ops,terraform-iac,ci-cd-pipelines}/SKILL.md` — each skill rich with `references/`, `examples/`, `scripts/` subdirs.
- `hooks/hooks.json` + `hooks/scripts/{security,quality,workflow}/*.sh` — categorized scripts.
- `.mcp.json` + `servers/{kubernetes-mcp,terraform-mcp,github-actions-mcp}/` — three custom MCP servers (Node + Python).
- `lib/{core,integrations,utils}/` — shared JS code (logger, config, auth, Slack/PagerDuty/Datadog clients, retry/validation).
- `config/{environments,templates}/` — env-specific JSON + reusable YAML templates.

**`plugin.json` highlights**:
```json
{
  "name": "enterprise-devops",
  "version": "2.3.1",
  "commands": ["./commands/ci", "./commands/monitoring", "./commands/admin"],
  "agents": ["./agents/orchestration", "./agents/specialized"],
  "hooks": "./hooks/hooks.json",
  "mcpServers": "./.mcp.json"
}
```

**`.mcp.json`** uses `${CLAUDE_PLUGIN_ROOT}` for portability + env-var passthrough (`${KUBECONFIG}`, `${TF_STATE_BUCKET}`, `${GITHUB_TOKEN}`).

**Deployment-orchestrator agent** showcases multi-stage flow: planning → validation → execution → verification → rollback. Uses 3 MCP servers + lib/integrations for monitoring (Datadog) and notifications (Slack).

**Kubernetes-ops skill** is comprehensive: deployment strategies (RollingUpdate / Recreate / Blue-Green / Canary), resource requests/limits, health probes (liveness vs readiness), troubleshooting commands (`kubectl describe/logs/exec/top`), security (non-root, read-only FS, drop capabilities, NetworkPolicy, RBAC), HPA autoscaling, MCP server integration calls.

**`hooks/hooks.json`** mixes prompt + command hooks: PreToolUse (secret scan + bash safety prompt), PostToolUse (status update), Stop (config check + team notification), SessionStart (permission validation).

**Use cases** the architecture supports: multi-env deployments, Terraform IaC, CI/CD automation, monitoring/observability, security enforcement, team collaboration via Slack/PagerDuty.

Pattern is intended for large-scale enterprise plugins where simple flat structure would not scale.
