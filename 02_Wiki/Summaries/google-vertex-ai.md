---
type: summary
source: 01_Raw/code.claude.com/docs/en/google-vertex-ai.md
source_url: https://code.claude.com/docs/en/google-vertex-ai
title: "Claude Code on Google Vertex AI"
summarized_at: 2026-05-05
entities_referenced: [Enterprise-gateway, Settings, MCP-server]
concepts_referenced: [Prompt-caching, Context-window, Extended-thinking]
---

Setup + configuration guide for running Claude Code through Google Vertex AI. Raw is mostly Mintlify component definitions for an experiment-bucketed contact-sales card; the actual content is ~250 lines.

**Prerequisites**: GCP project with billing + Vertex AI API enabled, Claude model access in Vertex AI Model Garden, `gcloud` SDK, region quota.

**Sign-in wizard** (Claude Code v2.1.98+): launch `claude` → 3rd-party platform → Google Vertex AI. Wizard handles ADC / service-account-key / env-vars choice, detects project + region, verifies invokable models, lets you pin them, writes result to `env` block of user settings. Re-open via `/setup-vertex`.

**Region configuration**: `CLOUD_ML_REGION` accepts `global`, multi-region (`eu`, `us`), or specific (`us-east5`). Multi-region locations route through `aiplatform.eu.rep.googleapis.com` / `aiplatform.us.rep.googleapis.com`. Not all models available on every endpoint type.

**Manual setup env vars**:
```bash
export CLAUDE_CODE_USE_VERTEX=1
export CLOUD_ML_REGION=global
export ANTHROPIC_VERTEX_PROJECT_ID=YOUR-PROJECT-ID
# optional
export ANTHROPIC_VERTEX_BASE_URL=...   # custom endpoint/gateway
export DISABLE_PROMPT_CACHING=1
export ENABLE_PROMPT_CACHING_1H=1      # 1h TTL, billed higher
export VERTEX_REGION_CLAUDE_HAIKU_4_5=us-east5
export VERTEX_REGION_CLAUDE_4_6_SONNET=europe-west1
```

**Auth**: standard Google Cloud (ADC, SA key, env). Claude Code v2.1.121+ supports X.509 certificate-based Workload Identity Federation (mTLS) via `GOOGLE_APPLICATION_CREDENTIALS` pointing to credential config file. Project ID can also come from `GCLOUD_PROJECT` / `GOOGLE_CLOUD_PROJECT`. Under Vertex, `/login` and `/logout` are disabled.

**MCP tool search disabled by default** on Vertex (endpoint doesn't accept the required beta header). All MCP tool defs load upfront. Opt in: `ENABLE_TOOL_SEARCH=true`.

**Model pinning** (CRITICAL for multi-user deployments) — without pins, `sonnet`/`opus` aliases resolve to latest, which may not yet be enabled in your project. Default `opus` resolves to Opus 4.6 — set `ANTHROPIC_DEFAULT_OPUS_MODEL='claude-opus-4-7'` to use 4.7.
```bash
export ANTHROPIC_DEFAULT_OPUS_MODEL='claude-opus-4-7'
export ANTHROPIC_DEFAULT_SONNET_MODEL='claude-sonnet-4-6'
export ANTHROPIC_DEFAULT_HAIKU_MODEL='claude-haiku-4-5@20251001'
```

Default fallbacks: primary = `claude-sonnet-4-5@20250929`, small/fast = `claude-haiku-4-5@20251001`.

**Startup model checks** (v2.1.98+): if pinned older model and project can invoke newer → prompts to update pin (writes to user settings + restart). If unpinned and current default unavailable → falls back to previous version for current session (not persisted) with a notice.

**IAM**: `roles/aiplatform.user` (or custom role with `aiplatform.endpoints.predict`). Recommended dedicated GCP project for cost tracking + access control.

**1M token context**: Opus 4.7 / Opus 4.6 / Sonnet 4.6 support 1M on Vertex. Setup wizard offers as option when pinning. Manual: append `[1m]` to model ID.

**Troubleshooting**:
- Quota issues — request via Cloud Console
- "Model not found" 404 — check Model Garden enablement, region availability, global-endpoint support per "Supported features"
- 429 — for regional endpoints ensure both primary and small/fast models supported in region; consider switching to `global`
