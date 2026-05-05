---
type: summary
source: 01_Raw/github/anthropics/anthropic-sdk-python/src/anthropic/lib/foundry.md
source_url: https://github.com/anthropics/anthropic-sdk-python/blob/main/src/anthropic/lib/foundry.md
title: "Anthropic SDK Python — Microsoft Foundry integration"
summarized_at: 2026-05-05
entities_referenced: [Anthropic-SDK-Python, Enterprise-gateway, Streaming-API]
concepts_referenced: []
---

Documentation for using the `anthropic` Python SDK against Microsoft Foundry.

**Setup.** `pip install anthropic` is sufficient — Foundry support is built into the package. Use the `AnthropicFoundry` class (or `AsyncAnthropicFoundry` for async) instead of `Anthropic`/`AsyncAnthropic`.

**Authentication options:**

1. **API key.** `AnthropicFoundry(api_key="...", resource="my-resource")`. The `api_key` defaults to the `ANTHROPIC_FOUNDRY_API_KEY` environment variable. The `resource` parameter identifies the Foundry resource.
2. **Azure AD / Microsoft Entra token provider.** For enhanced security:
   ```python
   from azure.identity import DefaultAzureCredential, get_bearer_token_provider
   credential = DefaultAzureCredential()
   token_provider = get_bearer_token_provider(credential, "https://ai.azure.com/.default")
   client = AnthropicFoundry(azure_ad_token_provider=token_provider, resource="my-resource")
   ```

**Usage.** Once the client is constructed, the API surface mirrors the standard SDK — `client.messages.create(model="claude-3-5-sonnet-20241022", max_tokens=1024, messages=[{"role": "user", "content": "Hello!"}])` returns a Message just like the direct API client. Streaming works the same way: `with client.messages.stream(...) as stream: for text in stream.text_stream: print(text, end="", flush=True)`.

**Async + streaming combos.** `AsyncAnthropicFoundry` supports both `await client.messages.create(...)` and `async with client.messages.stream(...) as stream: async for text in stream.text_stream: ...`.

This file is the SDK's only Foundry-specific reference; for the Bedrock or Vertex variants see the corresponding modules under `src/anthropic/lib/`.
