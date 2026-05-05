---
type: summary
source: 01_Raw/code.claude.com/docs/en/amazon-bedrock.md
source_url: https://code.claude.com/docs/en/amazon-bedrock
title: "Claude Code on Amazon Bedrock"
summarized_at: 2026-05-05
entities_referenced: [Enterprise-gateway, Settings]
concepts_referenced: [Prompt-caching, Context-window]
---

Configure Claude Code to call Claude through Amazon Bedrock instead of the Anthropic API. Two paths: an interactive sign-in wizard (run `claude`, select **3rd-party platform → Amazon Bedrock**) or manual env-var setup. Re-open the wizard later via `/setup-bedrock`.

Prerequisites: AWS account with Bedrock access, model access granted via the Bedrock console (one-time use case form per AWS account; AWS Orgs management account can submit once for all child accounts via `PutUseCaseForModelAccess`), AWS CLI optional, IAM permissions.

Core env vars:
- `CLAUDE_CODE_USE_BEDROCK=1` — enable Bedrock routing.
- `AWS_REGION=us-east-1` — required; not read from `.aws/config`.
- `ANTHROPIC_SMALL_FAST_MODEL_AWS_REGION` — override region for Haiku.
- `ANTHROPIC_BEDROCK_BASE_URL` — custom endpoint/gateway override.
- `ANTHROPIC_DEFAULT_OPUS_MODEL` / `..._SONNET_MODEL` / `..._HAIKU_MODEL` — pin to specific Bedrock model IDs (e.g. `us.anthropic.claude-opus-4-7`). Without `ANTHROPIC_DEFAULT_OPUS_MODEL`, the `opus` alias resolves to Opus 4.6.

Auth options: AWS CLI profile, access key / SSO env vars, AWS Console credentials, or Bedrock API key (`AWS_BEARER_TOKEN_BEDROCK`). For SSO refresh: `awsAuthRefresh` setting (re-runs SSO login command, displays output) or `awsCredentialExport` (silent, must return JSON with `Credentials.{AccessKeyId,SecretAccessKey,SessionToken}`).

Pinning is critical for team rollouts — without pins, model aliases resolve to the latest version which may not yet be available. `modelOverrides` setting maps individual versions (e.g. `claude-opus-4-7` → application inference profile ARN) so users can switch via `/model`.

Startup model checks (Claude Code v2.1.94+) verify accessibility, prompt to upgrade pins when newer defaults are available, fall back to previous version if current default is unavailable (non-persistent).

IAM policy needs `bedrock:InvokeModel`, `InvokeModelWithResponseStream`, `ListInferenceProfiles`, `GetInferenceProfile`, plus `aws-marketplace:Subscribe` (gated to bedrock.amazonaws.com).

1M context window supported on Opus 4.7, Opus 4.6, Sonnet 4.6 — append `[1m]` to model ID. Service tiers: `default`/`flex`/`priority` via `ANTHROPIC_BEDROCK_SERVICE_TIER`. AWS Guardrails configured via `ANTHROPIC_CUSTOM_HEADERS` setting.

**Mantle endpoint** (v2.1.94+): native Anthropic API shape served from Bedrock. Enable with `CLAUDE_CODE_USE_MANTLE=1`. Model IDs use `anthropic.` prefix (e.g. `anthropic.claude-haiku-4-5`). Can run alongside Invoke API; Mantle-format IDs route to Mantle, others to Invoke. `CLAUDE_CODE_SKIP_MANTLE_AUTH=1` for LLM-gateway setups that inject creds server-side.

Notes: `/login` and `/logout` disabled under Bedrock. Claude Code uses Bedrock Invoke API only — not Converse. Prompt caching available (1H TTL via `ENABLE_PROMPT_CACHING_1H=1`, billed at higher write rate). Common SSO loop fix: drop `awsAuthRefresh` and run `aws sso login` manually.
