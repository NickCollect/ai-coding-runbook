---
type: summary
source: 01_Raw/github/anthropics/claude-code-action/docs/cloud-providers.md
source_url: https://github.com/anthropics/claude-code-action/blob/main/docs/cloud-providers.md
title: "Claude Code Action — docs/cloud-providers"
summarized_at: 2026-05-05
entities_referenced: [CI-integration, Enterprise-gateway]
concepts_referenced: []
---

Authentication options for the Claude Code Action.

**Four supported methods:**

1. Direct Anthropic API (default).
2. Amazon Bedrock with OIDC authentication.
3. Google Vertex AI with OIDC authentication.
4. Microsoft Foundry with OIDC authentication.

Bedrock, Vertex, and Microsoft Foundry all use OIDC exclusively. AWS Bedrock automatically uses cross-region inference profiles for certain models — for those, model access must be requested in **all** regions the inference profile uses.

**Model configuration.** Use provider-specific model names. Examples:

```yaml
# Direct Anthropic API
- uses: anthropics/claude-code-action@v1
  with:
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}

# AWS Bedrock with OIDC
- uses: anthropics/claude-code-action@v1
  with:
    use_bedrock: "true"
    claude_args: |
      --model anthropic.claude-4-0-sonnet-20250805-v1:0

# Google Vertex AI with OIDC
- uses: anthropics/claude-code-action@v1
  with:
    use_vertex: "true"
    claude_args: |
      --model claude-4-0-sonnet@20250805

# Microsoft Foundry with OIDC
- uses: anthropics/claude-code-action@v1
  with:
    use_foundry: "true"
    claude_args: |
      --model claude-sonnet-4-5
```

**OIDC authentication.** AWS Bedrock, GCP Vertex AI, and Microsoft Foundry all support OIDC. The doc continues with full per-provider OIDC setup (e.g., AWS `Configure AWS Credentials (OIDC)` step), required IAM/IDP role configuration, the `id-token: write` workflow permission, and how to wire OIDC trust policies to the GitHub repo.
