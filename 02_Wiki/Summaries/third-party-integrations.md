---
type: summary
source: 01_Raw/code.claude.com/docs/en/third-party-integrations.md
source_url: https://code.claude.com/docs/en/third-party-integrations
title: "Enterprise deployment overview"
summarized_at: 2026-05-05
entities_referenced: [Enterprise-gateway, Memory, MCP-server, Settings]
concepts_referenced: [Prompt-caching]
---

Enterprise deployment overview — choose between Anthropic-direct or cloud provider routing for Claude Code. **Note**: raw is mostly Mintlify component definitions and CSS; only ~20% is actual content.

**Recommended default**: **Claude for Teams or Enterprise** — single sub for both Claude Code AND Claude on the web, centralized billing, no infra. Teams self-service ($150/seat Premium with PAYG); Enterprise adds SSO, domain capture, RBAC, compliance API, managed policy settings (contact sales).

**Cloud provider deployment options** (when infra requirements exist):

| | Teams/Enterprise | Anthropic Console | Bedrock | Vertex AI | Foundry |
|---|---|---|---|---|---|
| Best for | Most orgs (recommended) | Individual devs | AWS-native | GCP-native | Azure-native |
| Billing | $150/seat or sales | PAYG | PAYG via AWS | PAYG via GCP | PAYG via Azure |
| Auth | Claude.ai SSO/email | API key | API key or AWS creds | GCP creds | API key or Entra ID |
| Cost tracking | Usage dashboard | Usage dashboard | AWS Cost Explorer | GCP Billing | Azure Cost Management |
| Includes Claude on web | Yes | No | No | No | No |
| Enterprise features | Team mgmt, SSO, monitoring | None | IAM, CloudTrail | IAM, Cloud Audit Logs | RBAC, Azure Monitor |
| Prompt caching | Default on (all) | | | | |

**Proxy / LLM gateway** (different configs, can combine):
- **Corporate proxy**: `HTTPS_PROXY`/`HTTP_PROXY`. For monitoring/compliance/network policy.
- **LLM Gateway**: `ANTHROPIC_BASE_URL`, `ANTHROPIC_BEDROCK_BASE_URL`, `ANTHROPIC_VERTEX_BASE_URL`. For centralized usage tracking, custom rate limits, centralized auth.

**Bedrock through corp proxy**:
```bash
export CLAUDE_CODE_USE_BEDROCK=1
export AWS_REGION=us-east-1
export HTTPS_PROXY='https://proxy.example.com:8080'
```

**Bedrock through LLM gateway**:
```bash
export CLAUDE_CODE_USE_BEDROCK=1
export ANTHROPIC_BEDROCK_BASE_URL='https://your-llm-gateway.com/bedrock'
export CLAUDE_CODE_SKIP_BEDROCK_AUTH=1
```

Same patterns for Foundry (`CLAUDE_CODE_USE_FOUNDRY=1`, `ANTHROPIC_FOUNDRY_RESOURCE`, `ANTHROPIC_FOUNDRY_API_KEY` or Entra ID; `ANTHROPIC_FOUNDRY_BASE_URL` + `CLAUDE_CODE_SKIP_FOUNDRY_AUTH=1` for gateway) and Vertex (`CLAUDE_CODE_USE_VERTEX=1`, `CLOUD_ML_REGION=us-east5`, `ANTHROPIC_VERTEX_PROJECT_ID`; `ANTHROPIC_VERTEX_BASE_URL` + `CLAUDE_CODE_SKIP_VERTEX_AUTH=1`).

Use `/status` to verify proxy/gateway config.

**Best practices for orgs**:
1. **Documentation/memory**: deploy CLAUDE.md at organization-wide (managed-policy paths) AND repository level (in source control)
2. **Simplify deployment**: "one click" install for custom dev envs is key for adoption
3. **Start with guided usage**: codebase Q&A or small fixes first; ask Claude to make a plan; give feedback
4. **Pin model versions for cloud providers**: use `ANTHROPIC_DEFAULT_OPUS_MODEL`, `ANTHROPIC_DEFAULT_SONNET_MODEL`, `ANTHROPIC_DEFAULT_HAIKU_MODEL`. Without pinning, aliases resolve to latest, which may not yet be enabled in your account.
5. **Configure security policies** via managed permissions (cannot be overwritten by local config)
6. **Leverage MCP**: one central team configures + commits `.mcp.json` to repo so all benefit
