---
type: summary
source: 01_Raw/github/anthropics/anthropic-sdk-typescript/README.md
source_url: https://github.com/anthropics/anthropic-sdk-typescript/blob/main/README.md
title: "Claude SDK for TypeScript — README"
summarized_at: 2026-05-05
entities_referenced: [Anthropic-SDK-TypeScript, Messages-API]
concepts_referenced: []
---

The Claude SDK for TypeScript (`npm install @anthropic-ai/sdk`, requires Node.js 18+) provides access to the Claude API from server-side TypeScript or JavaScript applications. Full documentation lives at platform.claude.com/docs/en/api/sdks/typescript. MIT-licensed.

**Getting started:** import `Anthropic` from `@anthropic-ai/sdk`, instantiate with `apiKey` (defaults to `process.env['ANTHROPIC_API_KEY']`), and call `client.messages.create({ max_tokens: 1024, messages: [{ role: 'user', content: 'Hello, Claude' }], model: 'claude-opus-4-6' })`.

This README is intentionally short — see `api.md` (resource/method reference), `helpers.md` (streaming, structured outputs, tool helpers, MCP helpers), `CHANGELOG.md` (release history), and `CONTRIBUTING.md` (yarn-based dev workflow) for deeper documentation.
