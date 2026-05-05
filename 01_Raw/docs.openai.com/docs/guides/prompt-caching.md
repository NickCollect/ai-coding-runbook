# Prompt caching

<!-- source: https://platform.openai.com/docs/guides/prompt-caching -->

Model prompts often contain repetitive content. OpenAI routes API requests to servers that recently processed the same prompt prefix, making it cheaper and faster.

- **Latency reduction**: up to 80%
- **Input token cost reduction**: up to 90%
- **No code changes required** — works automatically
- **No additional fees**
- Available for all models gpt-4o and newer

## How to optimize for caching

**Place static content at the beginning** of prompts (instructions, examples), and **variable content at the end** (user-specific information). This also applies to images and tools — they must be identical between requests.

## How it works

Caching activates for prompts 1024 tokens or longer:

1. **Cache Routing**: Requests routed based on hash of initial prefix (~first 256 tokens)
2. **Cache Lookup**: System checks if prefix exists in cache
3. **Cache Hit**: Uses cached result → lower latency + lower cost
4. **Cache Miss**: Processes full prompt, caches prefix for future requests

Use `prompt_cache_key` parameter to influence routing and improve cache hit rates (especially when many requests share long common prefixes). Keep each unique prefix + key combination below ~15 req/min to avoid cache overflow.

## Cache retention policies

### In-memory retention (most models)
- Available for all models that support caching **except** gpt-5.5, gpt-5.5-pro, and future models
- Cached prefixes remain active for **5-10 minutes of inactivity**, up to max 1 hour
- Held in volatile GPU memory only

### Extended retention (gpt-5.x models)
Available for: `gpt-5.5`, `gpt-5.5-pro`, `gpt-5.4`, `gpt-5.2`, `gpt-5.1-*`, `gpt-5`, `gpt-4.1`
- Keeps cached prefixes for up to **24 hours**
- Offloads key/value tensors to GPU-local storage when memory is full
- Default for gpt-5.5 and future models (in_memory not supported on these)

Configure via `prompt_cache_retention`: `"in_memory"` or `"24h"`.

## What can be cached

- Messages (system, user, assistant interactions)
- Images (links or base64, but `detail` parameter must be identical)
- Tool use (messages array + list of available tools)
- Structured outputs (schema serves as prefix to system message)

## Monitoring cache performance

Cache hit info appears in `usage.prompt_tokens_details.cached_tokens` in the response:

```json
"usage": {
  "prompt_tokens": 2006,
  "prompt_tokens_details": { "cached_tokens": 1920 }
}
```

## Key facts

- Caches are NOT shared between organizations
- Only same-organization members can access identical prompt caches
- Cannot manually clear the cache (auto-evicted after inactivity)
- Does NOT affect output generation — response is always computed fresh
- Cached prompts DO count toward TPM rate limits
- Works with Zero Data Retention (in-memory policy; extended caching stores key/value tensors temporarily)
