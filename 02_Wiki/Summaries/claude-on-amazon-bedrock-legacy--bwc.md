---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy.md
source_url: https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy
title: "Claude on Amazon Bedrock (legacy)"
summarized_at: 2026-05-05
entities_referenced: [Enterprise-gateway]
concepts_referenced: []
---

Legacy Bedrock integration using `InvokeModel` and `Converse` APIs with **ARN-versioned model identifiers** and AWS event-stream encoding. For the new Messages-API endpoint shape, see "Claude in Amazon Bedrock". Claude Opus 4.7 is reachable through `InvokeModel` on `bedrock-runtime` (same backend as the new endpoint) but has no ARN-versioned model ID, so it's omitted from the legacy table.

## Setup

- AWS CLI ≥ 2.13.23 + configured credentials (`aws sts get-caller-identity`).
- Subscribe to Anthropic models in AWS Console → Bedrock → Model Access.
- Region availability varies by model.

## SDK packages

Same as new Bedrock endpoint:
- Python: `anthropic[bedrock]`
- TypeScript: `@anthropic-ai/bedrock-sdk`
- C#: `Anthropic.Bedrock`
- Go: `github.com/anthropics/anthropic-sdk-go/bedrock`
- Java: `com.anthropic:anthropic-java-bedrock` → `BedrockBackend`
- PHP: `anthropic-ai/sdk` + `aws/aws-sdk-php`
- Ruby: `anthropic` + `aws-sdk-bedrockruntime`
- Boto3 (`pip install boto3>=1.28.59`) supported directly.

## ARN-versioned model IDs

| Model | Bedrock model ID | global | us | eu | jp | apac |
|---|---|---|---|---|---|---|
| Opus 4.6 | `anthropic.claude-opus-4-6-v1` | Y | Y | Y | Y | Y |
| Sonnet 4.6 | `anthropic.claude-sonnet-4-6` | Y | Y | Y | Y | N |
| Sonnet 4.5 | `anthropic.claude-sonnet-4-5-20250929-v1:0` | Y | Y | Y | Y | N |
| Sonnet 4 (deprecated 2026-04-14, retiring 2026-10-14) | `anthropic.claude-sonnet-4-20250514-v1:0` | Y | Y | Y | N | Y |
| Sonnet 3.7 (retired 2026-02-19) | `anthropic.claude-3-7-sonnet-20250219-v1:0` | N | Y | Y | N | Y |
| Opus 4.5 | `anthropic.claude-opus-4-5-20251101-v1:0` | Y | Y | Y | N | N |
| Opus 4.1 | `anthropic.claude-opus-4-1-20250805-v1:0` | N | Y | N | N | N |
| Opus 4 (deprecated 2026-04-14) | `anthropic.claude-opus-4-20250514-v1:0` | N | Y | N | N | N |
| Haiku 4.5 | `anthropic.claude-haiku-4-5-20251001-v1:0` | Y | Y | Y | N | N |
| Haiku 3.5 (retired 2026-02-19) | `anthropic.claude-3-5-haiku-20241022-v1:0` | N | Y | N | N | N |

## Listing models

`aws bedrock list-foundation-models --region=us-west-2 --by-provider anthropic --query "modelSummaries[*].modelId"` (or boto3/SDK equivalents).

## Notes

- Global vs regional inference profile distinction documented in same page.
- Use new Messages API Bedrock endpoint for Opus 4.7 and full feature parity.
