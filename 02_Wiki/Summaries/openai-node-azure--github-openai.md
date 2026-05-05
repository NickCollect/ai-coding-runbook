---
type: summary
source: 01_Raw/github/openai/openai-node/azure.md
source_url: https://github.com/openai/openai-node/blob/main/azure.md
title: "openai-node — Azure OpenAI Guide"
summarized_at: 2026-05-05
entities_referenced: ["OpenAI", "Microsoft Azure"]
concepts_referenced: ["Azure OpenAI", "AzureOpenAI class", "Realtime on Azure", "managed identity", "azureADTokenProvider", "apiVersion"]
---

Use AzureOpenAI class instead of OpenAI. Note: Azure API shape differs slightly from core API.

Setup: import { AzureOpenAI } from 'openai'; use getBearerTokenProvider from @azure/identity; pass azureADTokenProvider and apiVersion.

Realtime on Azure: Use OpenAIRealtimeWS.azure(client) or OpenAIRealtimeWebSocket.azure(client) — pass a fully configured AzureOpenAI client.
