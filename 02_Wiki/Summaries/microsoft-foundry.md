---
type: summary
source: 01_Raw/code.claude.com/docs/en/microsoft-foundry.md
source_url: https://code.claude.com/docs/en/microsoft-foundry
title: "Claude Code on Microsoft Foundry"
summarized_at: 2026-05-05
entities_referenced: [Enterprise-gateway, Settings]
concepts_referenced: [Prompt-caching]
---

Setup guide for routing Claude Code through Microsoft Foundry on Azure. Raw is mostly Mintlify component definitions for an experiment-bucketed contact-sales card; actual content ~120 lines.

**Prerequisites**: Azure subscription with Foundry access, RBAC perms to create Foundry resources/deployments, Azure CLI (optional — only if no other credential mechanism). Pin model versions when deploying to multiple users.

**Setup**:

1. **Provision Foundry resource** at `ai.azure.com`: create resource, create deployments for Opus / Sonnet / Haiku.

2. **Auth** — two options:
   - **API key**: copy from resource → Endpoints and keys section → set `ANTHROPIC_FOUNDRY_API_KEY`
   - **Microsoft Entra ID**: when API key not set, Claude Code uses Azure SDK default credential chain (`az login` for local). Supports remote workload auth too.
   
   Under Foundry, `/login` and `/logout` are disabled.

3. **Configure**:
   ```bash
   export CLAUDE_CODE_USE_FOUNDRY=1
   export ANTHROPIC_FOUNDRY_RESOURCE={resource}
   # OR full base URL:
   # export ANTHROPIC_FOUNDRY_BASE_URL=https://{resource}.services.ai.azure.com/anthropic
   ```

4. **Pin model versions** — without pinning, aliases (`sonnet`/`opus`/`haiku`) may resolve to a model not yet enabled in your Foundry account, breaking users on Anthropic releases. **Also**: when creating Azure deployments select a specific version, NOT "auto-update to latest." Without `ANTHROPIC_DEFAULT_OPUS_MODEL`, the `opus` alias resolves to Opus 4.6.
   ```bash
   export ANTHROPIC_DEFAULT_OPUS_MODEL='claude-opus-4-7'
   export ANTHROPIC_DEFAULT_SONNET_MODEL='claude-sonnet-4-6'
   export ANTHROPIC_DEFAULT_HAIKU_MODEL='claude-haiku-4-5'
   ```

**Prompt caching** automatic. `ENABLE_PROMPT_CACHING_1H=1` for 1-hour TTL (billed higher) instead of 5-min default.

**Azure RBAC**: `Azure AI User` + `Cognitive Services User` roles cover required perms. Custom role only needs `Microsoft.CognitiveServices/accounts/providers/*` data action.

**Troubleshooting**: "Failed to get token from azureADTokenProvider: ChainedTokenCredential authentication failed" → either configure Entra ID or set `ANTHROPIC_FOUNDRY_API_KEY`.
