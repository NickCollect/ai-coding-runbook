---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry.md
source_url: https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry
title: "Claude in Microsoft Foundry"
summarized_at: 2026-05-05
entities_referenced: [Enterprise-gateway, Messages-API]
concepts_referenced: []
---

Claude in Microsoft Foundry is a preview commercial integration that bills Claude usage through Azure subscription via Microsoft Marketplace. **Claude models still run on Anthropic's infrastructure** (Anthropic acts as independent processor for Microsoft); same data commitments and ZDR availability apply.

## Availability

- Preview integration; Global Standard deployment type at launch (US DataZone coming).
- Pricing per Anthropic standard API rates.
- **SDKs:** C#, Java, PHP, Python, TypeScript. Go and Ruby SDKs **do not** currently support Foundry.

## Provisioning model

Two-level hierarchy:

1. **Foundry resource** — security & billing config.
2. **Deployments** — model instances called via API. Deployment name passed as `model` parameter (defaults to model ID, customizable, immutable after creation). Multiple deployments of same model allowed.

Steps:
1. Create Foundry resource at ai.azure.com (configurable with Entra ID, Azure VNet for private network).
2. **Models + endpoints → Deploy model → Deploy base model** → pick Claude (e.g., `claude-sonnet-4-6`) → Global Standard.
3. Note resource name → endpoint pattern: `https://{resource}.services.ai.azure.com/anthropic/v1/*`.

## Authentication

| Method | Notes |
|---|---|
| API key | From Foundry portal "Keys and Endpoint". Pass via `api-key` or `x-api-key` header. |
| Entra ID token | Role-based access |

## SDK env vars

- `ANTHROPIC_FOUNDRY_API_KEY`
- `ANTHROPIC_FOUNDRY_RESOURCE` — resource name (e.g., `example-resource`); SDK builds full URL.
- `ANTHROPIC_FOUNDRY_BASE_URL` — alternative to resource (mutually exclusive).

## SDK packages

- Python: `anthropic` → `AnthropicFoundry`
- TypeScript: `@anthropic-ai/foundry-sdk` → `AnthropicFoundry`
- C#: `Anthropic.Foundry`
- Java: `com.anthropic:anthropic-java-foundry`
- PHP: `anthropic-ai/sdk`

## Notes

- HIPAA does NOT cover Foundry per the API/data retention page (Bedrock/Vertex/Foundry treated as third-party).
