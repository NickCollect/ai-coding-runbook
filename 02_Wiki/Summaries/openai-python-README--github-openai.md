---
type: summary
source: 01_Raw/github/openai/openai-python/README.md
source_url: https://github.com/openai/openai-python/blob/main/README.md
title: "openai-python — Python SDK README"
summarized_at: 2026-05-05
entities_referenced: ["OpenAI", "Stainless", "Azure", "Kubernetes", "GCP", "PyPI", "httpx", "aiohttp", "Pydantic"]
concepts_referenced: ["OpenAI API", "Python SDK", "Responses API", "Chat Completions API", "async", "AsyncOpenAI", "streaming", "file uploads", "webhook verification", "auto-pagination", "Realtime API", "workload identity", "error handling", "retries", "timeouts", "AzureOpenAI", "TypedDict", "SemVer"]
---

Official OpenAI Python library. Generated from OpenAPI specification with Stainless. Requires Python 3.9+.

Install: pip install openai

Primary APIs:
- Responses API (client.responses.create()): Primary text generation interface
- Chat Completions API (client.chat.completions.create()): Legacy, supported indefinitely
- Realtime API: Low-latency multi-modal via WebSocket using websockets library

Async: Use AsyncOpenAI (identical interface). Optional aiohttp backend: pip install openai[aiohttp]; pass http_client=DefaultAioHttpClient().

Key features:
- Workload Identity: k8s_service_account_token_provider, azure_managed_identity_token_provider, gcp_id_token_provider
- Streaming: stream=True; for event in stream:
- File uploads: bytes, PathLike, or (filename, contents, media_type) tuple
- Webhook: client.webhooks.unwrap() or verify_signature()
- Error types: APIConnectionError, RateLimitError, APIStatusError (with status_code and response)
- Types: Nested params are TypedDict; responses are Pydantic models with .to_json() / .to_dict()
- Auto-pagination: for job in client.fine_tuning.jobs.list() auto-fetches pages
- Request IDs: response._request_id
- Retries: 2 default; max_retries option
- Timeouts: 10 minutes default; timeout float or httpx.Timeout
- Raw response: .with_raw_response. prefix; .with_streaming_response. for streaming
- HTTP customization: DefaultHttpxClient with proxy/transport

Azure: AzureOpenAI class; params: azure_endpoint, azure_deployment, api_version, azure_ad_token, azure_ad_token_provider.

Vision: Pass image URLs or base64 in input content array with type input_image.

Realtime: async with client.realtime.connect(model=...) as connection; iterate async for event in connection:
