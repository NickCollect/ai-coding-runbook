---
type: summary
source: 01_Raw/github/openai/openai-node/MIGRATION.md
source_url: https://github.com/openai/openai-node/blob/main/MIGRATION.md
title: "openai-node — Migration Guide"
summarized_at: 2026-05-05
entities_referenced: ["OpenAI", "Stainless"]
concepts_referenced: ["migration", "breaking changes", "Web fetch API", "node-fetch", "named parameters", "ReadableStream", "TypeScript 4.9", "Node.js 20"]
---

Migration guide for upgrading to the latest openai Node.js SDK.

Key Change: SDK now uses built-in Web fetch API instead of node-fetch — zero dependencies.

Migration CLI: ./node_modules/.bin/openai migrate ./your/src/folders (--dry to preview)

Environment Requirements: Node.js 20 LTS, TypeScript 4.9, Jest 28

Breaking Changes:
1. Web types: Response body is now Web ReadableStream (not Node Readable). APIError.headers is now Web Headers class.
   Convert: Readable.fromWeb(res.body).pipe(process.stdout)
2. Named path parameters: Methods with multiple path params now use named args for all but the last:
   Before: client.parents.children.retrieve('p_123', 'c_456')
   After: client.parents.children.retrieve('c_456', { parent_id: 'p_123' })
   Affects: fineTuning.checkpoints.permissions.delete, vectorStores.files.*, beta.threads.runs.*, beta.threads.messages.*, admin organization methods.
