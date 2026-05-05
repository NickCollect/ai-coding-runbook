---
type: summary
source: 01_Raw/ai.google.dev/gemini-api/docs/partner-integration.md
source_url: https://ai.google.dev/gemini-api/docs/partner-integration
title: "Gemini API — Partner and Library Integration Guide"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

# Partner and Library Integration Guide

Source is in Vietnamese (crawler localization).

## Overview

Architecture strategies for building libraries, platforms, and gateways on top of Gemini API. Covers tradeoffs between using the official GenAI SDK, Direct API (REST/gRPC), and OpenAI compatibility layer.

Target audience: Tool builders for other developers — open-source frameworks, enterprise gateways, SaaS aggregators needing to optimize for dependency hygiene, bundle size, or feature parity.

## 4 Partner Archetypes

| Archetype | Who You Are | Primary Goal |
|---|---|---|
| **Ecosystem Framework** | OSS framework maintainers (LangChain, LlamaIndex, Spring AI) | Broad compatibility across user environments |
| **Runtime/Edge Platform** | SaaS, AI gateways, cloud infra providers (Vercel, Cloudflare, Zapier) | Performance: low latency, minimal bundle, fast cold start |
| **Aggregator** | Multi-LLM platforms/proxies that unify OpenAI + Anthropic + Google into one interface | Portability and uniformity |
| **Enterprise Gateway** | Internal platform teams at large companies building "Golden Paths" for 100s of internal devs | Standardization, governance, unified auth |

## Integration Path Selection

- **Ecosystem Frameworks**: Official `google-genai` SDK (Python/JS); tree-shakeable, environment-compatible
- **Edge Platforms**: REST/gRPC Direct API or OpenAI compatibility layer; minimum deps, no Node-specific modules
- **Aggregators**: OpenAI compatibility layer (`/v1beta/openai/`) for fastest integration
- **Enterprise Gateways**: Direct REST + `x-goog-api-client` header for identity tracking

## Universal Best Practice

**All partners MUST send the `x-goog-api-client` header** for proper tracking and support regardless of integration path.

## Notes

- Security: Treat API keys as secrets; proxy through backend, never expose client-side.
- Streaming: SSE for HTTP, WebSocket for Live API.
