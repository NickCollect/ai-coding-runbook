---
type: summary
source: 01_Raw/github/openai/openai-node/src/resources/conversations/api.md
source_url: https://github.com/openai/openai-node/blob/main/src/resources/conversations/api.md
title: "openai-node — Conversations API Type Reference"
summarized_at: 2026-05-05
entities_referenced: ["OpenAI"]
concepts_referenced: ["Conversations API", "TypeScript types", "CRUD", "ConversationItem"]
---

TypeScript type reference for client.conversations.

Types: Conversation, ConversationDeleted, ConversationDeletedResource, Message, ComputerScreenshotContent, SummaryTextContent, TextContent, InputTextContent, OutputTextContent, RefusalContent, InputImageContent, InputFileContent, ConversationItem, ConversationItemList

Methods:
- client.conversations.create({...}) -> Conversation [POST /conversations]
- client.conversations.retrieve(conversationID) -> Conversation [GET /conversations/{id}]
- client.conversations.update(conversationID, {...}) -> Conversation [POST /conversations/{id}]
- client.conversations.delete(conversationID) -> ConversationDeletedResource [DELETE /conversations/{id}]
- client.conversations.items.create/retrieve/list/delete
