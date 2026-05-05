---
type: summary
source: 01_Raw/code.claude.com/docs/en/llm-gateway.md
source_url: https://code.claude.com/docs/en/llm-gateway
title: "LLM gateway configuration"
summarized_at: 2026-05-05
entities_referenced: [Enterprise-gateway, Settings]
concepts_referenced: [Prompt-caching]
---

LLM gateways = centralized proxy between Claude Code and model providers for auth, usage tracking, cost control, audit logging, model routing.

**Gateway requirements** — must expose at least one of:
1. **Anthropic Messages**: `/v1/messages`, `/v1/messages/count_tokens`. Forward `anthropic-beta`, `anthropic-version` headers.
2. **Bedrock InvokeModel**: `/invoke`, `/invoke-with-response-stream`. Preserve `anthropic_beta`, `anthropic_version` body fields.
3. **Vertex rawPredict**: `:rawPredict`, `:streamRawPredict`, `/count-tokens:rawPredict`. Forward headers.

When using Anthropic Messages format on Bedrock/Vertex, set `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1`.

**Headers** Claude Code sends:
- `X-Claude-Code-Session-Id` — unique per session, lets proxies aggregate without parsing body.
- Attribution block prepended to system prompt (client version + conversation fingerprint). Anthropic API strips before processing → no impact on first-party prompt cache. If your gateway caches on full body, set `CLAUDE_CODE_ATTRIBUTION_HEADER=0` to omit.

**Model discovery** (Anthropic Messages format only): when `ANTHROPIC_BASE_URL` set, Claude Code v2.1.126+ queries gateway's `/v1/models` at startup, adds models to `/model` picker labeled "From gateway" (uses `display_name` if present). Filtered to models whose ID starts with `claude` or `anthropic`. Cached to `~/.claude/cache/gateway-models.json`. Auth: `ANTHROPIC_AUTH_TOKEN` as bearer or `ANTHROPIC_API_KEY` as `x-api-key`, plus `ANTHROPIC_CUSTOM_HEADERS`. Falls back to cache or built-in list on failure. Doesn't run for Bedrock/Vertex pass-through. Use Model Configuration env vars to add manually if names don't match filter.

**LiteLLM warning**: PyPI versions 1.82.7 and 1.82.8 were compromised with credential-stealing malware — remove + rotate credentials. LiteLLM is third-party; not endorsed by Anthropic.

**LiteLLM auth** options:
- Static API key: `ANTHROPIC_AUTH_TOKEN=sk-litellm-static-key` (sent as `Authorization` header).
- Dynamic via `apiKeyHelper` in settings — script returns key (e.g., from vault, JWT). `CLAUDE_CODE_API_KEY_HELPER_TTL_MS` for refresh. Sent as both `Authorization` and `X-Api-Key`. Lower precedence than `ANTHROPIC_AUTH_TOKEN`/`ANTHROPIC_API_KEY`.

**LiteLLM endpoint patterns**:
- **Unified Anthropic format (recommended)**: `ANTHROPIC_BASE_URL=https://litellm-server:4000`. Benefits: load balancing, fallbacks, consistent cost/end-user tracking.
- Anthropic pass-through: `ANTHROPIC_BASE_URL=https://litellm-server:4000/anthropic`.
- Bedrock pass-through: `ANTHROPIC_BEDROCK_BASE_URL=...`, `CLAUDE_CODE_SKIP_BEDROCK_AUTH=1`, `CLAUDE_CODE_USE_BEDROCK=1`.
- Vertex pass-through: `ANTHROPIC_VERTEX_BASE_URL=...`, `ANTHROPIC_VERTEX_PROJECT_ID=...`, `CLAUDE_CODE_SKIP_VERTEX_AUTH=1`, `CLAUDE_CODE_USE_VERTEX=1`, `CLOUD_ML_REGION=us-east5`.
