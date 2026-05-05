---
type: summary
source: 01_Raw/github/openai/openai-node/api.md
source_url: https://github.com/openai/openai-node/blob/main/api.md
title: "openai-node — Full API Reference"
summarized_at: 2026-05-05
entities_referenced: ["OpenAI"]
concepts_referenced: ["OpenAI API", "TypeScript SDK", "API reference", "Responses API", "Chat Completions", "Realtime API", "Assistants", "fine-tuning", "embeddings", "images", "audio", "files", "vector stores", "webhooks", "conversations"]
---

File size: 76KB. Comprehensive TypeScript/JavaScript SDK API reference listing all client methods and types.

Major resource groups:
- client.responses: Responses API (primary text generation)
- client.chat.completions: Chat Completions (legacy)
- client.realtime: WebSocket Realtime API
- client.assistants, client.beta.threads, runs, messages: Assistants
- client.fineTuning: Fine-tuning jobs and checkpoints
- client.embeddings, client.images, client.audio: Core AI capabilities
- client.files, client.vectorStores: Data management
- client.moderation, client.webhooks: Safety/webhooks
- client.conversations: Conversations API
- client.models, client.batches, client.uploads: Utilities
- Admin: client.admin.organization (projects, groups, users, roles)

See raw api.md for full type signatures.
