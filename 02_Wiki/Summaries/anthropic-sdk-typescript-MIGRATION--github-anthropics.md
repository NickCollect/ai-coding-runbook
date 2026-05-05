---
type: summary
source: 01_Raw/github/anthropics/anthropic-sdk-typescript/MIGRATION.md
source_url: https://github.com/anthropics/anthropic-sdk-typescript/blob/main/MIGRATION.md
title: "anthropic-sdk-typescript — Migration Guide"
summarized_at: 2026-05-05
entities_referenced: ["Anthropic"]
concepts_referenced: ["migration", "breaking changes", "Web fetch API", "node-fetch", "named parameters", "TypeScript 4.9", "Node.js 20"]
---

Migration guide for the Anthropic TypeScript SDK.

Key Change: SDK now uses built-in Web fetch API instead of node-fetch — zero dependencies.

Migration CLI: ./node_modules/.bin/anthropic-ai-sdk migrate ./your/src/folders

Requirements: Node.js 20 LTS, TypeScript 4.9, Jest 28

Breaking Changes:
1. Web types: Response body is now Web ReadableStream. APIError.headers is now Web Headers class.
2. Named path parameters: Methods with multiple path params now use named args for all but the last.
   Affects: client.beta.sessions.resources.*, client.beta.vaults.credentials.*
