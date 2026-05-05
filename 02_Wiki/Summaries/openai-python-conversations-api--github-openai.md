---
type: summary
source: 01_Raw/github/openai/openai-python/src/openai/resources/conversations/api.md
source_url: https://github.com/openai/openai-python/blob/main/src/openai/resources/conversations/api.md
title: "openai-python — Conversations API Type Reference"
summarized_at: 2026-05-05
entities_referenced: ["OpenAI"]
concepts_referenced: ["Conversations API", "Python types", "CRUD", "ConversationItem"]
---

Python type reference for client.conversations (from openai.types.conversations).

Types: Conversation, ConversationDeleted, ConversationDeletedResource, Message, SummaryTextContent, TextContent, InputTextContent, OutputTextContent, RefusalContent, InputImageContent, InputFileContent, ConversationItem, ConversationItemList

Methods: create(**params)->Conversation, retrieve(conversation_id)->Conversation, update(conversation_id, **params)->Conversation, delete(conversation_id)->ConversationDeletedResource
Sub-resource: client.conversations.items.create/retrieve/list/delete
