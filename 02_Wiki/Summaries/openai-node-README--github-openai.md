---
type: summary
source: 01_Raw/github/openai/openai-node/README.md
source_url: https://github.com/openai/openai-node/blob/main/README.md
title: "openai-node — TypeScript/JavaScript SDK README"
summarized_at: 2026-05-05
entities_referenced: ["OpenAI", "Stainless", "Azure", "Kubernetes", "GCP", "npm", "JSR", "Deno", "Bun", "Cloudflare Workers", "Vercel Edge Runtime"]
concepts_referenced: ["OpenAI API", "TypeScript SDK", "Responses API", "Chat Completions API", "streaming", "SSE", "file uploads", "webhook verification", "auto-pagination", "Realtime API", "workload identity", "error handling", "retries", "timeouts", "logging", "AzureOpenAI", "SemVer"]
---

Official OpenAI TypeScript/JavaScript SDK. Generated from OpenAPI specification with Stainless.

## Installation
npm install openai
or from JSR: deno add jsr:@openai/openai

## Primary APIs
- Responses API (client.responses.create()): Primary API for text generation
- Chat Completions API (client.chat.completions.create()): Legacy but supported indefinitely
- Realtime API: Low-latency multi-modal via WebSocket (OpenAIRealtimeWebSocket / OpenAIRealtimeWS)

## Key Features
- Workload Identity Auth: Kubernetes, Azure managed identity, GCP compute metadata
- Streaming: SSE via stream: true; for await (const event of stream)
- File uploads: File, fs.ReadStream, fetch Response, or toFile() helper
- Webhook Verification: client.webhooks.unwrap() (verify + parse) or verifySignature()
- Error handling: APIError subclasses (400 BadRequestError, 401 AuthenticationError, 403 PermissionDeniedError, 404 NotFoundError, 422 UnprocessableEntityError, 429 RateLimitError, >=500 InternalServerError)
- Auto-pagination: for await ... of on list methods
- Request IDs: _request_id on all responses
- Retries: 2 default with exponential backoff; maxRetries option
- Timeouts: 10 minutes default; timeout option
- Logging: OPENAI_LOG env var or logLevel client option; custom logger support

## Azure OpenAI
Use AzureOpenAI class. Params: azureADTokenProvider, apiVersion, azure_endpoint, azure_deployment.

## Requirements
TypeScript >=4.9; Node.js 20+ LTS, Deno v1.28+, Bun 1.0+, Cloudflare Workers, Vercel Edge Runtime, Jest 28+, Nitro v2.6+. Web browsers require dangerouslyAllowBrowser: true.
