---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/libraries.md
source_url: https://ai.google.dev/gemini-api/docs/libraries
title: "Gemini API — Libraries / SDKs"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Gemini API Libraries / SDKs

Source is in Korean (crawler localization).

## Recommended: Google GenAI SDK

Official libraries maintained by Google, production-ready, GA (generally available). Used in all official documentation and examples.

## Supported Languages

| Language | Package | GitHub | Install |
|---|---|---|---|
| Python | `google-genai` | googleapis/python-genai | `pip install google-genai` |
| JavaScript/TypeScript | `@google/genai` | googleapis/js-genai | `npm install @google/genai` |
| Go | `google.golang.org/genai` | googleapis/go-genai | `go get google.golang.org/genai` |
| Java | `google-genai` | googleapis/java-genai | Maven: `com.google.genai:google-genai:1.0.0` |
| C# | `Google.GenAI` | googleapis/dotnet-genai | `dotnet add package Google.GenAI` |

## C# / .NET Support

Also available via `dotnet add package Google.GenAI`.

## Apps Script

Built-in — use REST API via `UrlFetchApp.fetch()`.

## Previous/Legacy SDKs

- Python: `google-generativeai` (deprecated, migrate to `google-genai`)
- JavaScript: `@google/generative-ai` (deprecated, migrate to `@google/genai`)
- Go: `github.com/google/generative-ai-go` (deprecated, migrate to `google.golang.org/genai`)

## Migration

See `migrate.md` for before/after code examples for each language.

## Notes

- Both Gemini Developer API and Gemini Enterprise Agent Platform can be accessed via `google-genai`.
- Only difference is `vertexai=True` in client initialization for Enterprise.
