---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/authentication/overview.md
source_url: https://platform.claude.com/docs/en/api/authentication/overview
title: "Authentication"
summarized_at: 2026-05-07
entities_referenced: [Workload-Identity-Federation, Service-account, Federation-issuer, Federation-rule, API-key, Workspace, Messages-API]
concepts_referenced: [JWT]
---

Two ways to authenticate to the Claude API:

| Method | Credential | Best for |
|---|---|---|
| **API key** | Long-lived `sk-ant-api...` in `x-api-key` header | Local dev, prototyping, scripts, single-tenant servers |
| **Workload Identity Federation** | Short-lived bearer token exchanged from IdP identity token | Production cloud workloads (AWS/GCP/Azure), CI/CD, Kubernetes |

Both grant the same access. Choose API keys for fast start; switch to WIF when the workload already has a platform-issued identity to federate.

## API keys

- Generated in Console → **Settings → API keys**. Use **workspaces** to scope by project / environment.
- Send via `x-api-key` header or `ANTHROPIC_API_KEY` env var (SDKs pick up automatically).
- **No expiry**. Store in secrets manager, rotate periodically, revoke any suspected leak.

## Workload Identity Federation

- WIF lets workloads authenticate with a short-lived identity token from an IdP they already trust (AWS IAM, GCP, GitHub Actions, K8s service accounts, Microsoft Entra ID, Okta).
- Workload exchanges its IdP-issued JWT at `POST /v1/oauth/token` for a short-lived Claude API access token; SDK refreshes automatically.
- No `sk-ant-api...` to mint, distribute, or rotate.
- Configure 3 resources in Console: **service account**, **federation issuer**, **federation rule** (full setup in WIF setup walkthrough).
- Federation does not on its own guarantee end-to-end security: trust chain is only as strong as the IdP, and a long-lived secret one hop upstream can still undermine it. Pair with IdP controls (IP allowlists, MFA, audit logging).
