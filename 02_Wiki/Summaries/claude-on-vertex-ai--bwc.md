---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai.md
source_url: https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai
title: "Claude on Vertex AI"
summarized_at: 2026-05-05
entities_referenced: [Enterprise-gateway, Messages-API]
concepts_referenced: []
---

Claude on Google Cloud Vertex AI is GA. The Vertex API mirrors the Anthropic Messages API with two differences: `model` goes in the URL (not body), and `anthropic_version` goes in the body (not header) and **must be** `vertex-2023-10-16`.

## Setup

- GCP project with Vertex AI enabled. Subscribe to Claude in Vertex AI Model Garden.
- Authenticate: `gcloud auth application-default login`.

## SDK packages

- Python: `google-cloud-aiplatform "anthropic[vertex]"` → `AnthropicVertex`
- TypeScript: `@anthropic-ai/vertex-sdk` → `AnthropicVertex`
- C#: `Anthropic.Vertex`
- Go: `github.com/anthropics/anthropic-sdk-go` (uses Vertex backend)
- Java: `com.anthropic:anthropic-java-vertex` → `VertexBackend`
- PHP: `anthropic-ai/sdk` + `google/auth`
- Ruby: `anthropic` + `googleauth`

## Vertex AI model IDs

| Model | Vertex API model ID |
|---|---|
| Opus 4.7 | `claude-opus-4-7` |
| Opus 4.6 | `claude-opus-4-6` |
| Sonnet 4.6 | `claude-sonnet-4-6` |
| Sonnet 4.5 | `claude-sonnet-4-5@20250929` |
| Sonnet 4 (deprecated 2026-04-14, retiring 2026-09-14) | `claude-sonnet-4@20250514` |
| Sonnet 3.7 (retired 2026-02-19) | `claude-3-7-sonnet@20250219` |
| Opus 4.5 | `claude-opus-4-5@20251101` |
| Opus 4.1 | `claude-opus-4-1@20250805` |
| Opus 4 (deprecated) | `claude-opus-4@20250514` |
| Haiku 4.5 | `claude-haiku-4-5@20251001` |
| Haiku 3.5 (retired) | `claude-3-5-haiku@20241022` |

## Endpoint pattern

`https://{LOCATION}-aiplatform.googleapis.com/v1/projects/{PROJECT_ID}/locations/{LOCATION}/publishers/anthropic/models/{MODEL_ID}:streamRawPredict`

Example body: `{anthropic_version: "vertex-2023-10-16", messages: [...], max_tokens: 100}`.

## Notes

- Model availability varies by region; check Model Garden.
- ZDR/HIPAA not applicable on Vertex (third-party platform).
