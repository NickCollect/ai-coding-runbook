---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock.md
source_url: https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock
title: "Claude in Amazon Bedrock"
summarized_at: 2026-05-05
entities_referenced: [Enterprise-gateway, Messages-API, Streaming-API, Anthropic-SDK-Python, Anthropic-SDK-TypeScript, Anthropic-SDK-Go, Anthropic-SDK-Java]
concepts_referenced: []
---

Claude in Amazon Bedrock serves Claude through the **standard Messages API** at `/anthropic/v1/messages` on AWS-managed infrastructure (zero Anthropic operator access). Same request body shape and SSE streaming as Anthropic's first-party API. Distinct from the **legacy Bedrock integration** (`InvokeModel`/`Converse` with ARN-versioned IDs).

## Access

- Claude Opus 4.7 and Claude Haiku 4.5 are open to all Bedrock customers.
- Claude Mythos Preview requires invitation + dedicated allowlisted AWS account (Project Glasswing).

## Authentication paths

| Path | Notes |
|---|---|
| Bedrock service role (recommended) | AWS-managed keys; admin grants `iam:PassRole` |
| IAM assumed roles | 12h max; identity-federated (SAML/OIDC/AWS Identity Center); permissions limited to `bedrock-mantle:CreateInference` |
| Bearer tokens | 12h max; least preferred. Minted via `aws-bedrock-token-generator`; pass in `x-api-key`. Restrict via `bedrock:BearerTokenType` deny condition for long-term keys. |

## Endpoint

`https://bedrock-mantle.{region}.api.aws/anthropic/v1/messages`

- cURL: use `--aws-sigv4 "aws:amz:{region}:bedrock-mantle"`.
- SDK credential resolution follows standard AWS precedence: constructor args → env vars (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_SESSION_TOKEN`, `AWS_REGION`) → AWS config file / credential chain (SSO, ECS task role, IMDS).

## SDKs

Bedrock-specific packages/modules:
- Python: `pip install -U "anthropic[bedrock]"` → `AnthropicBedrockMantle`
- TypeScript: `@anthropic-ai/bedrock-sdk` → `AnthropicBedrockMantle`
- C#: `Anthropic.Bedrock` → `AnthropicBedrockMantleClient`
- Go: `github.com/anthropics/anthropic-sdk-go/bedrock` → `bedrock.NewMantleClient`
- Java: `com.anthropic:anthropic-java-bedrock` (uses `BedrockMantleBackend`)
- PHP: `anthropic-ai/sdk` + `aws/aws-sdk-php` → `Anthropic\Bedrock\MantleClient`
- Ruby: `anthropic` + `aws-sdk-core`

## Model id format

Use `anthropic.claude-opus-4-7` (no ARN versioning on this endpoint).

## Notes

- Same Messages API features available; ZDR / HIPAA do **not** apply (Bedrock is third-party platform).
- For ARN-versioned model IDs, region availability tables, and `InvokeModel`/`Converse` shape, see legacy Bedrock page.
