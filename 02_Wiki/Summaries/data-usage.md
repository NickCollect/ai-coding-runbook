---
type: summary
source: 01_Raw/code.claude.com/docs/en/data-usage.md
source_url: https://code.claude.com/docs/en/data-usage
title: "Data usage"
summarized_at: 2026-05-05
entities_referenced: [Settings, Enterprise-gateway]
concepts_referenced: []
---

Anthropic's data-usage policies for Claude Code, broken down by account type.

**Training**:
- **Consumer (Free/Pro/Max)**: opt-in switch; if on, data may be used to train new models (including Claude Code from these accounts).
- **Commercial (Team/Enterprise/API/3rd-party platforms/Claude Gov)**: Anthropic does NOT train on code/prompts unless the customer opts in (e.g., Development Partner Program — first-party API only, not Bedrock/Vertex).

**`/feedback` command**: full conversation history including code is sent to Anthropic, transcripts retained 5 years. Optional GitHub issue creation. Disable with `DISABLE_FEEDBACK_COMMAND=1`.

**Session quality survey** ("How is Claude doing?"):
- Responding (incl. "Dismiss") records ONLY the rating — no transcripts/inputs/outputs.
- A separate follow-up may ask to upload session transcript: **Yes** uploads conversation + subagent transcripts + raw session log (API keys/tokens redacted; source code uploaded as-is, retained ≤6 months); **No** declines; **Don't ask again** disables follow-up.
- Survey responses do NOT impact data training preferences and cannot be used to train AI.
- Disable: `CLAUDE_CODE_DISABLE_FEEDBACK_SURVEY=1`, also off when `DISABLE_TELEMETRY` or `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` set. Frequency tunable via `feedbackSurveyRate` (0–1) in settings.
- ZDR orgs / orgs with product feedback disabled never see this follow-up.

**Retention**:
- Consumer: 5 yrs (if opted in to training) or 30 days (if not). Toggle at claude.ai/settings/data-privacy-controls.
- Commercial: 30 days standard. Zero Data Retention available on Enterprise (per-organization, account-team enabled).
- **Local cache**: Claude Code stores session transcripts in plaintext at `~/.claude/projects/` for 30 days by default; tune via `cleanupPeriodDays`.

**Encryption at rest** by provider:
- Anthropic API: AES-256 disk; ZDR for no server-side persistence
- Bedrock: AES-256 with AWS-managed keys; CMK via AWS KMS
- Vertex AI: Google-managed keys; CMEK available
- Foundry: routes to Anthropic infra with AES-256

**Data flow**: local CLI → Anthropic API directly (no third-party servers). TLS 1.2+ encrypts in transit. VPN/LLM-proxy compatible.

**Cloud execution** (Claude Code on the web): repo cloned to isolated VM; GitHub auth via secure proxy (creds never enter sandbox); outbound traffic through security proxy for audit + abuse prevention; same data policies apply.

**Telemetry services**:
- **Statsig** — operational metrics (latency, reliability, usage). NO code or file paths. Opt out: `DISABLE_TELEMETRY`.
- **Sentry** — error logging. Opt out: `DISABLE_ERROR_REPORTING`.
- All disabled by default on Bedrock/Vertex/Foundry except session quality surveys + WebFetch domain safety check. Disable all non-essential at once via `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`.
- v2.1.126: when host platform sets `CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST`, Statsig defaults on for Vertex/Bedrock/Foundry (Sentry/feedback remain off).

**WebFetch domain safety check**: hostname-only sent to `api.anthropic.com` against a safety blocklist (no full URL/path/contents). Cached 5 min/hostname. Runs regardless of provider, not affected by `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`. Disable with `skipWebFetchPreflight: true` (then combine with WebFetch permission rules to restrict domains).
